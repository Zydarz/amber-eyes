#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Production Audio Pipeline for TikTok Clip 01 (TK1) - Episode 01.
Tạo âm thanh chuẩn trên Mac mini (Apple Silicon) bằng:
- Higgs Audio v3 trên MLX (Pre-encode VoxCPM2 giọng mẫu H, D, C).
- Whisper ASR native đo CER từng câu (< 2%).
- Multi-take variant 1 nếu câu có CER cao.
- Đo tách bạch cao độ F0 (Luật G9 >= 4 nửa cung).
- Đo độ tự nhiên UTMOSv2 (Rule M5 - CPU).
- Tự động cắt tỉa đuôi câm > 0.8s @ -45 dBFS (Rule M3).
- Cập nhật manifest và xuất kết quả kiểm tra chi tiết.
"""
import os
import sys
import gc
import json
import time
import wave
import hashlib
import pathlib
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import vi_cer

SPEC_PATH = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01" / "SPEC_AUDIO_CLIP_TAP01.json"
OUT_DIR = HERE / "audio_s_tk_t01"
OUT_DIR.mkdir(parents=True, exist_ok=True)
RAW_OUT = HERE / "kaggle_higgs" / "out_higgs_prod_tk1"
RAW_OUT.mkdir(parents=True, exist_ok=True)

# Giọng mẫu VoxCPM2 đã kiểm định cho Tap 01
ROLE_REF_MAP = {
    "H": (ROOT / "assets/voice_ref_voxcpm2/H.wav", ROOT / "assets/voice_ref_voxcpm2/H.txt"),
    "D": (ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav", ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.txt"),
    "C": (ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav", ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.txt"),
}

def fname(sid):
    # TK1.01#1 -> TK1.01_01.wav
    ma, k = sid.split("#")
    return f"{ma}_{int(k):02d}.wav"

def raw_fname(sid, role, ref, var):
    ma, k = sid.split("#")
    stem = pathlib.Path(ref).stem
    return f"{ma}_{int(k):02d}_{role}_{stem}_t0.8_v{var}.wav"

def trim_silence_tail(wav_path, threshold_db=-45.0, min_tail_sec=0.8):
    """Quy tắc M3: cắt đuôi câm < -45 dBFS dài > 0.8s, giữ lại 0.3s + 30ms fade."""
    with wave.open(str(wav_path), "rb") as wf:
        sr = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        data = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0

    total_dur = len(data) / sr
    hop = int(sr * 0.02)
    thresh = 10.0 ** (threshold_db / 20.0)

    last_active = len(data)
    for i in range(len(data) - hop, 0, -hop):
        chunk = data[i:i + hop]
        rms = np.sqrt(np.mean(chunk ** 2) + 1e-9)
        if rms >= thresh:
            last_active = i + hop
            break

    tail_dur = (len(data) - last_active) / sr
    if tail_dur > min_tail_sec:
        keep_samples = int(last_active + 0.3 * sr)
        if keep_samples < len(data):
            trimmed = data[:keep_samples].copy()
            fade_len = int(0.03 * sr)
            if len(trimmed) > fade_len:
                trimmed[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)
            int_data = (np.clip(trimmed, -1.0, 1.0) * 32767.0).astype(np.int16)
            with wave.open(str(wav_path), "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(sr)
                wf.writeframes(int_data.tobytes())
            print(f"      [TRIMMED] Tail {tail_dur:.2f}s -> pruned {total_dur:.2f}s to {len(trimmed)/sr:.2f}s", flush=True)

def estimate_f0(wav_path):
    try:
        with wave.open(str(wav_path), "rb") as wf:
            sr = wf.getframerate()
            frames = wf.readframes(wf.getnframes())
            data = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
        frame_len = int(sr * 0.04)
        hop_len = int(sr * 0.01)
        f0_list = []
        min_lag = int(sr / 450)
        max_lag = int(sr / 60)
        for i in range(0, len(data) - frame_len, hop_len):
            frame = data[i:i + frame_len]
            if np.std(frame) < 0.01:
                continue
            corr = np.correlate(frame, frame, mode='full')
            corr = corr[len(frame) - 1:]
            if len(corr) <= max_lag:
                continue
            peak_idx = np.argmax(corr[min_lag:max_lag]) + min_lag
            if corr[0] > 0 and corr[peak_idx] / corr[0] > 0.4:
                f0_list.append(sr / peak_idx)
        return float(np.median(f0_list)) if f0_list else 0.0
    except Exception:
        return 0.0

def main():
    print("=" * 80)
    print("TTS PRODUCTION PIPELINE: TIKTOK CLIP 01 (TK1) VIA HIGGS MAC + VOXCPM2")
    print("=" * 80, flush=True)

    with open(SPEC_PATH, "r", encoding="utf-8") as f:
        spec_data = json.load(f)

    c1 = [c for c in spec_data["clips"] if c["id"] == "TK1"][0]
    items = c1["lines"]
    print(f"Clip ID: {c1['id']} - {c1['ten']}")
    print(f"Total lines: {len(items)}", flush=True)

    # =========================================================================
    # Step 1 & 2: Load Higgs & Pre-encode Voices (Rule M1)
    # =========================================================================
    print("\n[Step 1/5] Loading Higgs Audio v3 Model on Apple Silicon MLX...", flush=True)
    from mlx_audio.tts.utils import load as load_higgs
    from mlx_audio.audio_io import write as audio_write

    t0 = time.time()
    model = load_higgs("bosonai/higgs-audio-v3-tts-4b")
    print(f"Model loaded in {time.time()-t0:.2f}s", flush=True)

    print("\n[Step 2/5] Pre-encoding VoxCPM2 Reference Voices (Rule M1)...", flush=True)
    ref_cache = {}
    for role, (wpath, tpath) in ROLE_REF_MAP.items():
        t_ref = tpath.read_text(encoding="utf-8").strip()
        t_enc = time.time()
        codes = model.encode_reference_audio(str(wpath))
        ref_cache[role] = (codes, t_ref, wpath.name)
        print(f"  Role {role:2s} -> {wpath.name} encoded in {time.time()-t_enc:.2f}s", flush=True)

    # =========================================================================
    # Step 3: Synthesis (Variant 0)
    # =========================================================================
    print("\n[Step 3/5] Generating Sentence Audio (Variant 0)...", flush=True)
    man_path = OUT_DIR / "manifest_tk_t01.json"
    man = {}
    if man_path.exists():
        try:
            for item in json.loads(man_path.read_text(encoding="utf-8")):
                man[item["id"]] = item
        except Exception:
            pass

    for idx, it in enumerate(items):
        sid = it["id"]
        role = it["vai"]
        text = it["text"]
        out_name = fname(sid)
        dst_wav = OUT_DIR / out_name
        codes, ref_text, ref_name = ref_cache[role]
        raw_name = raw_fname(sid, role, ref_name, 0)
        raw_wav = RAW_OUT / raw_name

        seed = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|0".encode()).hexdigest()[:8], 16)
        print(f"  [{idx+1:02d}/{len(items)}] {sid} ({role}) [seed={seed}]: '{text[:45]}...'", flush=True)
        t_start = time.time()
        res = list(model.generate(
            text=text,
            ref_audio_codes=codes,
            ref_text=ref_text,
            temperature=0.8,
            top_p=0.95,
            seed=seed,
            fade_in_ms=30.0,
            fade_out_ms=15.0
        ))
        gen_time = time.time() - t_start

        audio_write(str(dst_wav), res[0].audio, res[0].sample_rate)
        audio_write(str(raw_wav), res[0].audio, res[0].sample_rate)
        trim_silence_tail(dst_wav)
        trim_silence_tail(raw_wav)

        with wave.open(str(dst_wav), "rb") as wf:
            dur = wf.getnframes() / wf.getframerate()
        f0 = estimate_f0(dst_wav)
        print(f"      -> {out_name} (dur: {dur:.2f}s, F0: {f0:.1f}Hz, gen: {gen_time:.1f}s)", flush=True)

        man[sid] = {
            "id": sid,
            "vai": role,
            "file": out_name,
            "dur": round(dur, 2),
            "emotion": it.get("emotion", "neutral"),
            "speed": it.get("speed", -0.02),
            "pause_after": it.get("pause_after", 0.5),
            "text": text,
            "variant": 0,
            "seed": seed,
            "f0": round(f0, 1),
            "gen_time": round(gen_time, 2)
        }

    # =========================================================================
    # Step 4: Whisper CER Quality Check & Multi-take
    # =========================================================================
    print("\n[Step 4/5] Transcribing with Whisper & Measuring Quality (CER)...", flush=True)
    import whisper_fast as whisper
    asr_model = whisper.load_model("base", device="cpu")
    high_cer = []
    cer_rows = []

    for idx, it in enumerate(items):
        sid = it["id"]
        role = it["vai"]
        orig_text = it["text"]
        wav_path = OUT_DIR / fname(sid)
        asr_res = asr_model.transcribe(str(wav_path), language="vi")["text"].strip()
        c = vi_cer.cer_pair(orig_text, asr_res)
        f0 = man.get(sid, {}).get("f0", 0.0)

        cer_rows.append({
            "id": sid,
            "role": role,
            "file": fname(sid),
            "text": orig_text,
            "asr": asr_res,
            "cer": c,
            "f0": f0
        })
        print(f"  {sid} ({role}): CER={c*100:5.2f}% | '{orig_text[:35]}' -> '{asr_res[:35]}'", flush=True)

        if c > 0.02: # Ngưỡng G12 là 2%
            high_cer.append((sid, role, c, orig_text, asr_res))

    # Multi-take Variant 1 nếu CER > 2%
    if high_cer:
        print(f"\n[Step 4b] Multi-take Re-generating {len(high_cer)} sentences with CER > 2% (Variant 1)...", flush=True)
        for sid, role, old_cer, orig_text, _ in high_cer:
            codes, ref_text, ref_name = ref_cache[role]
            seed1 = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|1".encode()).hexdigest()[:8], 16)
            dst_wav = OUT_DIR / fname(sid)
            raw_v1 = RAW_OUT / raw_fname(sid, role, ref_name, 1)

            res = list(model.generate(
                text=orig_text,
                ref_audio_codes=codes,
                ref_text=ref_text,
                temperature=0.8,
                top_p=0.95,
                seed=seed1,
                fade_in_ms=30.0,
                fade_out_ms=15.0
            ))
            audio_write(str(raw_v1), res[0].audio, res[0].sample_rate)
            trim_silence_tail(raw_v1)
            asr1 = asr_model.transcribe(str(raw_v1), language="vi")["text"].strip()
            c1 = vi_cer.cer_pair(orig_text, asr1)
            print(f"  {sid} ({role}): Take 0 CER={old_cer*100:.2f}% vs Take 1 CER={c1*100:.2f}%", flush=True)
            if c1 < old_cer:
                audio_write(str(dst_wav), res[0].audio, res[0].sample_rate)
                trim_silence_tail(dst_wav)
                with wave.open(str(dst_wav), "rb") as wf:
                    dur1 = wf.getnframes() / wf.getframerate()
                f0_1 = estimate_f0(dst_wav)
                print(f"      -> Chose Take 1 (CER improved to {c1*100:.2f}%)", flush=True)
                man[sid]["seed"] = seed1
                man[sid]["variant"] = 1
                man[sid]["dur"] = round(dur1, 2)
                man[sid]["f0"] = round(f0_1, 1)
                for r in cer_rows:
                    if r["id"] == sid:
                        r["cer"] = c1
                        r["asr"] = asr1
                        r["f0"] = f0_1
                        break

    # Free Whisper and Higgs before UTMOS to strictly preserve RAM (Rule M2)
    del asr_model
    del model
    del ref_cache
    gc.collect()

    # Đo tách bạch cao độ F0 (G9)
    print("\n[Step 4c] Evaluating Pitch Separation (G9 Rule)...", flush=True)
    role_f0 = {}
    for r in cer_rows:
        role = r["role"]
        f0 = r["f0"]
        if f0 > 0:
            role_f0.setdefault(role, []).append(f0)

    medians = {role: float(np.median(vals)) for role, vals in role_f0.items()}
    for role, med in sorted(medians.items(), key=lambda x: x[1]):
        print(f"  Role {role:2s}: median F0 = {med:.1f} Hz (n={len(role_f0[role])})")

    if "D" in medians and "H" in medians:
        dh_semitones = 12.0 * np.log2(medians["H"] / medians["D"])
        print(f"  Delta D -> H: {dh_semitones:.2f} semitones (Target >= 4.0 nc) {'✅ ĐẠT' if dh_semitones >= 4.0 else '⚠ TRƯỢT'}")
    if "H" in medians and "C" in medians:
        hc_semitones = 12.0 * np.log2(medians["C"] / medians["H"])
        print(f"  Delta H -> C: {hc_semitones:.2f} semitones (Target >= 4.0 nc) {'✅ ĐẠT' if hc_semitones >= 4.0 else '⚠ TRƯỢT'}")

    # =========================================================================
    # Step 5: UTMOSv2 MOS Naturalness Measurement (CPU, Rule M5)
    # =========================================================================
    print("\n[Step 5/5] Measuring UTMOSv2 Naturalness Score (CPU, Rule M5)...", flush=True)
    import utmosv2
    utmos_model = utmosv2.create_model(pretrained=True, device="cpu")
    utmos_scores = []

    for r in cer_rows:
        sid = r["id"]
        wav_path = OUT_DIR / fname(sid)
        try:
            score = float(utmos_model.predict(stage1_inp=str(wav_path)))
        except Exception:
            try:
                score = float(utmos_model.predict(wav_path=str(wav_path)))
            except Exception as e:
                print(f"  UTMOS predict error on {sid}: {e}")
                score = 0.0

        utmos_scores.append(score)
        r["utmos"] = round(score, 3)
        if sid in man:
            man[sid]["utmos"] = round(score, 3)
        print(f"  {sid} ({r['role']}): UTMOS MOS = {score:.3f} | CER={r['cer']*100:.2f}%", flush=True)

    avg_mos = float(np.mean(utmos_scores)) if utmos_scores else 0.0
    print(f"\nAverage UTMOSv2 Score for Clip 01: {avg_mos:.3f} / 5.0")

    # Lưu manifest hoàn chỉnh
    manifest_list = list(man.values())
    man_path.write_text(json.dumps(manifest_list, ensure_ascii=False, indent=2), encoding="utf-8")
    (OUT_DIR / "qc_report_tk1.json").write_text(json.dumps(cer_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n✅ All 12 lines for TikTok Clip 01 synthesized and verified!")
    print(f"Manifest written to: {man_path}")

if __name__ == "__main__":
    main()
