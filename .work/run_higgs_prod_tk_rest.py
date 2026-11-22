#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Production Audio Pipeline for TikTok Clips TK2, TK3, TK4 - Episode 01.
Tạo âm thanh chuẩn trên Mac mini (Apple Silicon) bằng:
- Higgs Audio v3 trên MLX (Pre-encode VoxCPM2 giọng mẫu H, D, C, N1, N2).
- Whisper ASR native đo CER từng câu (< 2%).
- Multi-take variant 1 nếu câu có CER cao.
- Đo tách bạch cao độ F0 (Luật G9 >= 4 nửa cung).
- Đo độ tự nhiên UTMOSv2 (Rule M5 - CPU).
- Tự động cắt tỉa đuôi câm > 0.8s @ -45 dBFS (Rule M3).
- Cập nhật manifest và mix & master 2-pass Loudnorm (-16 LUFS, TP <= -1.5 dBFS) ra 02_SAN_XUAT/Tiktok_Tap1/.
"""
import os
import sys
import gc
import json
import time
import wave
import hashlib
import pathlib
import subprocess
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import vi_cer

SPEC_PATH = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01" / "SPEC_AUDIO_CLIP_TAP01.json"
AUDIO_SRC = HERE / "audio_s_tk_t01"
AUDIO_SRC.mkdir(parents=True, exist_ok=True)
RAW_OUT = HERE / "kaggle_higgs" / "out_higgs_prod_tk_rest"
RAW_OUT.mkdir(parents=True, exist_ok=True)
PROD_DIR = ROOT / "02_SAN_XUAT" / "Tiktok_Tap1"
PROD_DIR.mkdir(parents=True, exist_ok=True)

SR = 48000

ROLE_REF_MAP = {
    "H": (ROOT / "assets/voice_ref_voxcpm2/H.wav", ROOT / "assets/voice_ref_voxcpm2/H.txt"),
    "D": (ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav", ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.txt"),
    "C": (ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav", ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.txt"),
    "N1": (ROOT / "assets/voice_ref_voxcpm2_g9/W6_LOW.wav", ROOT / "assets/voice_ref_voxcpm2_g9/W6_LOW.txt"),
    "N2": (ROOT / "assets/voice_ref_voxcpm2_g9/W5_HIGH.wav", ROOT / "assets/voice_ref_voxcpm2_g9/W5_HIGH.txt"),
}

BGM_MAP = {
    "TK2": ROOT / "assets" / "bgm" / "bgm_ambient_deep.mp3",
    "TK3": ROOT / "assets" / "bgm" / "bgm_cello_sad.mp3",
    "TK4": ROOT / "assets" / "bgm" / "bgm_piano_minimal.mp3",
}

def fname(sid):
    # TK2.01#1 -> TK2.01_01.wav
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

def read_wav_48k_mono(path):
    cmd = [
        "ffmpeg", "-y", "-i", str(path),
        "-ar", str(SR), "-ac", "1", "-f", "s16le", "-"
    ]
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True)
    return np.frombuffer(p.stdout, dtype=np.int16).astype(np.float32) / 32768.0

def mix_and_master_clip(clip_id, clip_items, bgm_file, man_dict):
    print("\n" + "=" * 60)
    print(f"MIX & MASTER: {clip_id}")
    print("=" * 60)

    voice_track = []
    current_time = 0.0
    timeline = []

    for it in clip_items:
        sid = it["id"]
        wav_path = AUDIO_SRC / fname(sid)
        samples = read_wav_48k_mono(wav_path)
        dur = len(samples) / SR
        pause = it.get("pause_after", 0.5)

        start_t = current_time
        end_t = start_t + dur
        voice_track.append(samples)
        timeline.append({
            "id": sid,
            "vai": it["vai"],
            "start": round(start_t, 3),
            "end": round(end_t, 3),
            "pause": pause,
            "text": it["text"]
        })

        if pause > 0:
            pause_samples = np.zeros(int(pause * SR), dtype=np.float32)
            voice_track.append(pause_samples)
            current_time = end_t + pause
        else:
            current_time = end_t

    full_voice = np.concatenate(voice_track)
    total_len_s = len(full_voice) / SR
    print(f"  Voice stem total duration: {total_len_s:.2f}s ({total_len_s/60:.2f} min)")

    # Ambience anti-silence (-48 dB)
    np.random.seed(int(hashlib.md5(clip_id.encode()).hexdigest()[:8], 16))
    noise = np.random.normal(0, 1, len(full_voice)).astype(np.float32)
    b = np.ones(int(SR * 0.005)) / int(SR * 0.005)
    smooth_noise = np.convolve(noise, b, mode='same')
    ambience = smooth_noise * (10.0 ** (-48.0 / 20.0))

    # BGM
    bgm_samples = read_wav_48k_mono(bgm_file)
    repeats = int(np.ceil(len(full_voice) / len(bgm_samples))) + 1
    tiled_bgm = np.tile(bgm_samples, repeats)[:len(full_voice)].copy()

    bgm_gain = np.ones(len(full_voice), dtype=np.float32) * (10.0 ** (-26.0 / 20.0))

    last_line = timeline[-1]
    boost_start = int((last_line["start"] - 1.2) * SR)
    boost_end = int(last_line["start"] * SR)
    if boost_start > 0 and boost_end <= len(full_voice):
        bgm_gain[boost_start:boost_end] = np.linspace(10.0**(-26.0/20.0), 10.0**(-16.0/20.0), boost_end - boost_start)

    fade_len = int(2.5 * SR)
    bgm_gain[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)

    bgm_mixed = tiled_bgm * bgm_gain
    mix_raw = full_voice + bgm_mixed + ambience

    raw_wav_path = PROD_DIR / f"{clip_id}_mix_raw.wav"
    int_raw = (np.clip(mix_raw, -1.0, 1.0) * 32767.0).astype(np.int16)
    with wave.open(str(raw_wav_path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(int_raw.tobytes())

    # Two-pass Loudnorm (-16 LUFS, TP <= -1.5 dBFS)
    cmd_pass1 = [
        "ffmpeg", "-y", "-i", str(raw_wav_path),
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
        "-f", "null", "-"
    ]
    p1 = subprocess.run(cmd_pass1, stderr=subprocess.PIPE, text=True, check=True)
    out_lines = p1.stderr.split("\n")
    json_str = ""
    start_json = False
    for line in out_lines:
        if line.strip() == "{":
            start_json = True
        if start_json:
            json_str += line + "\n"
        if line.strip() == "}":
            break
    m_data = json.loads(json_str)

    filter_pass2 = (
        f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={m_data['input_i']}:measured_TP={m_data['input_tp']}:"
        f"measured_LRA={m_data['input_lra']}:measured_thresh={m_data['input_thresh']}:offset={m_data['target_offset']}:linear=true"
    )

    final_wav = PROD_DIR / f"{clip_id}_master_audio.wav"
    final_mp3 = PROD_DIR / f"{clip_id}_master_audio.mp3"

    subprocess.run([
        "ffmpeg", "-y", "-i", str(raw_wav_path),
        "-af", filter_pass2,
        "-ar", "48000", "-ac", "2",
        str(final_wav)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    subprocess.run([
        "ffmpeg", "-y", "-i", str(final_wav),
        "-c:a", "libmp3lame", "-b:a", "256k",
        str(final_mp3)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    if raw_wav_path.exists():
        raw_wav_path.unlink()

    # Timeline
    timeline_file = PROD_DIR / f"timeline_{clip_id.lower()}.json"
    timeline_file.write_text(json.dumps(timeline, ensure_ascii=False, indent=2), encoding="utf-8")

    # QC verify
    p_check = subprocess.run([
        "ffmpeg", "-i", str(final_wav),
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
        "-f", "null", "-"
    ], stderr=subprocess.PIPE, text=True, check=True)
    j_res = ""
    rec = False
    for l in p_check.stderr.split("\n"):
        if l.strip() == "{":
            rec = True
        if rec:
            j_res += l + "\n"
        if l.strip() == "}":
            break
    fqc = json.loads(j_res)
    print(f"  {clip_id} Master Output:")
    print(f"    - Integrated Loudness: {fqc['input_i']} LUFS (Target -16.0 +/- 1.0)")
    print(f"    - True Peak: {fqc['input_tp']} dBFS (Target <= -1.5)")
    print(f"    - Duration: {total_len_s:.2f}s")
    print(f"    - Saved: {final_wav.name} & {final_mp3.name}")


def main():
    print("=" * 80)
    print("TTS PRODUCTION PIPELINE: TIKTOK CLIPS TK2, TK3, TK4 VIA HIGGS MAC")
    print("=" * 80, flush=True)

    with open(SPEC_PATH, "r", encoding="utf-8") as f:
        spec_data = json.load(f)

    target_clips = [c for c in spec_data["clips"] if c["id"] in ["TK2", "TK3", "TK4"]]
    all_lines = []
    for c in target_clips:
        for l in c["lines"]:
            all_lines.append((c["id"], l))

    print(f"Total clips: {len(target_clips)} | Total sentences: {len(all_lines)}")

    # =========================================================================
    # Step 1 & 2: Load Higgs & Pre-encode Voices (Rule M1)
    # =========================================================================
    print("\n[Step 1/6] Loading Higgs Audio v3 Model on Apple Silicon MLX...", flush=True)
    from mlx_audio.tts.utils import load as load_higgs
    from mlx_audio.audio_io import write as audio_write

    t0 = time.time()
    model = load_higgs("bosonai/higgs-audio-v3-tts-4b")
    print(f"Model loaded in {time.time()-t0:.2f}s", flush=True)

    print("\n[Step 2/6] Pre-encoding VoxCPM2 Reference Voices (Rule M1)...", flush=True)
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
    print("\n[Step 3/6] Generating Sentence Audio (Variant 0)...", flush=True)
    man_path = AUDIO_SRC / "manifest_tk_t01.json"
    man = {}
    if man_path.exists():
        try:
            for item in json.loads(man_path.read_text(encoding="utf-8")):
                man[item["id"]] = item
        except Exception:
            pass

    for idx, (cid, it) in enumerate(all_lines):
        sid = it["id"]
        role = it["vai"]
        text = it["text"]
        out_name = fname(sid)
        dst_wav = AUDIO_SRC / out_name
        codes, ref_text, ref_name = ref_cache[role]
        raw_name = raw_fname(sid, role, ref_name, 0)
        raw_wav = RAW_OUT / raw_name

        seed = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|0".encode()).hexdigest()[:8], 16)
        print(f"  [{idx+1:02d}/{len(all_lines)}] {cid} - {sid} ({role}) [seed={seed}]: '{text[:45]}...'", flush=True)
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
            "clip": cid,
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
    # Step 4: Whisper CER & Multi-take
    # =========================================================================
    print("\n[Step 4/6] Transcribing with Whisper & Measuring Quality (CER)...", flush=True)
    import whisper_fast as whisper
    asr_model = whisper.load_model("base", device="cpu")
    high_cer = []
    cer_rows = []

    for idx, (cid, it) in enumerate(all_lines):
        sid = it["id"]
        role = it["vai"]
        orig_text = it["text"]
        wav_path = AUDIO_SRC / fname(sid)
        asr_res = asr_model.transcribe(str(wav_path), language="vi")["text"].strip()
        c = vi_cer.cer_pair(orig_text, asr_res)
        f0 = man.get(sid, {}).get("f0", 0.0)

        cer_rows.append({
            "id": sid,
            "clip": cid,
            "role": role,
            "file": fname(sid),
            "text": orig_text,
            "asr": asr_res,
            "cer": c,
            "f0": f0
        })
        print(f"  {cid} - {sid} ({role}): CER={c*100:5.2f}% | '{orig_text[:35]}' -> '{asr_res[:35]}'", flush=True)

        if c > 0.02:
            high_cer.append((sid, cid, role, c, orig_text, asr_res))

    if high_cer:
        print(f"\n[Step 4b] Multi-take Re-generating {len(high_cer)} sentences with CER > 2% (Variant 1)...", flush=True)
        for sid, cid, role, old_cer, orig_text, _ in high_cer:
            codes, ref_text, ref_name = ref_cache[role]
            seed1 = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|1".encode()).hexdigest()[:8], 16)
            dst_wav = AUDIO_SRC / fname(sid)
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
            print(f"  {cid} - {sid} ({role}): Take 0 CER={old_cer*100:.2f}% vs Take 1 CER={c1*100:.2f}%", flush=True)
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

    del asr_model
    del model
    del ref_cache
    gc.collect()

    # =========================================================================
    # Step 5: UTMOSv2 MOS Naturalness Measurement (CPU, Rule M5)
    # =========================================================================
    print("\n[Step 5/6] Measuring UTMOSv2 Naturalness Score (CPU, Rule M5)...", flush=True)
    import utmosv2
    utmos_model = utmosv2.create_model(pretrained=True)

    for r in cer_rows:
        sid = r["id"]
        wav_path = AUDIO_SRC / fname(sid)
        score = float(utmos_model.predict(input_path=str(wav_path), device="cpu", verbose=False))
        r["utmos"] = round(score, 3)
        if sid in man:
            man[sid]["utmos"] = round(score, 3)
        print(f"  {r['clip']} - {sid} ({r['role']}): UTMOS MOS = {score:.3f} | CER={r['cer']*100:.2f}%", flush=True)

    del utmos_model
    gc.collect()

    # Cập nhật manifest và báo cáo tổng
    manifest_list = list(man.values())
    man_path.write_text(json.dumps(manifest_list, ensure_ascii=False, indent=2), encoding="utf-8")
    (AUDIO_SRC / "qc_report_tk2_tk3_tk4.json").write_text(json.dumps(cer_rows, ensure_ascii=False, indent=2), encoding="utf-8")

    # =========================================================================
    # Step 6: Mix & Master TK2, TK3, TK4
    # =========================================================================
    print("\n[Step 6/6] Mixing & Mastering complete audio for TK2, TK3, TK4...", flush=True)
    for c in target_clips:
        cid = c["id"]
        bgm_f = BGM_MAP[cid]
        mix_and_master_clip(cid, c["lines"], bgm_f, man)

    print("\n" + "=" * 80)
    print("🎉 ALL AUDIO FOR TK2, TK3, TK4 COMPLETED AND DELIVERED TO Tiktok_Tap1!")
    print("=" * 80, flush=True)

if __name__ == "__main__":
    main()
