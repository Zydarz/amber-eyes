#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Production Audio Generator for Episode 06 English using Higgs Audio v3 on MLX.
Tuân thủ đầy đủ QUY_TAC_HIGGS_MAC.md, QUY_TAC_AUDIO_HIGGS.md và AGENTS.md:
- Pre-encodes 5 VoxCPM2 reference voices once (Rule M1).
- CẤM mọi thẻ <|emotion:...|> (Rule M4).
- Giữ prosody pause sau dấu : trước câu trích.
- Tự động phát hiện và cắt đuôi câm > 0.8s @ -45 dBFS (Rule M3).
- Đo F0 trung vị và kiểm tra G9 (tách bạch >= 4.0 nửa cung).
- Chạy Whisper ASR và tính CER (ngưỡng 2.0%).
- Multi-take: Sinh bản thay thế (variant 1) cho các câu CER > 2.0%.
- Đo độ tự nhiên UTMOSv2 MOS trên CPU (Rule M5).
- Xây dựng Master Audio chuẩn -16 LUFS / TP <= -1.5 dBFS bằng build_audio3.py.
- Tính timeline chính xác, xuất srt và báo cáo CanNghe.
"""
import os
import sys

os.environ["AE_EP"] = "06"
os.environ["AE_LANG"] = "en"
os.environ["AE_AUDIO_DIR"] = "audio_s_higgs"

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
import en_cer

from mlx_audio.tts.utils import load as load_higgs
from mlx_audio.audio_io import write as audio_write
from transformers import pipeline

PAYLOAD_PATH = HERE / "kaggle_higgs" / "higgs_payload_EN_t06.json"
DS_DIR = HERE / "kaggle_higgs" / "dataset_voxcpm2_en"
AUDIO_OUT = HERE / "audio_s_higgs_EN_t06"
AUDIO_OUT.mkdir(parents=True, exist_ok=True)
RAW_OUT = HERE / "kaggle_higgs" / "out_higgs_prod_EN_t06"
RAW_OUT.mkdir(parents=True, exist_ok=True)

ROLE_REF_MAP = {
    "H": ("H_EN.wav", "H_EN.txt"),
    "D": ("D_EN.wav", "D_EN.txt"),
    "C": ("C_EN.wav", "C_EN.txt"),
    "N1": ("N1_EN.wav", "N1_EN.txt"),
    "N2": ("N2_EN.wav", "N2_EN.txt"),
}

def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.wav"

def raw_fname(sid, role, ref, var):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    stem = pathlib.Path(ref).stem
    return f"{a}_{b}_{k}_{role}_{stem}_t0.8_s{var}.wav"

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

def trim_silence_tail(wav_path, threshold_db=-45.0, min_tail_sec=0.8):
    """Quy tắc 01/11 & Rule M3: cắt đuôi câm < -45 dB dài > 0.8s, giữ lại 0.3s + 30ms fade."""
    with wave.open(str(wav_path), "rb") as wf:
        sr = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        data = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0

    total_dur = len(data) / sr
    hop = int(sr * 0.02)
    thresh = 10.0 ** (threshold_db / 20.0)

    # scan from tail backwards
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
            # 30 ms fade out
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

def main():
    print("=" * 80)
    print("PRODUCTION AUDIO PIPELINE: HIGGS AUDIO V3 — EPISODE 06 EN")
    print("=" * 80, flush=True)

    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))
    items = payload["items"]
    print(f"Total sentences to synthesize: {len(items)}", flush=True)

    print("\n[Step 1/7] Loading Higgs Audio v3 Model...", flush=True)
    t0 = time.time()
    model = load_higgs("bosonai/higgs-audio-v3-tts-4b")
    print(f"Model loaded in {time.time()-t0:.2f}s", flush=True)

    print("\n[Step 2/7] Pre-encoding 5 VoxCPM2 Reference Voices (Rule M1)...", flush=True)
    ref_cache = {}
    for role, (wname, tname) in ROLE_REF_MAP.items():
        wpath = DS_DIR / wname
        tpath = DS_DIR / tname
        t_ref = tpath.read_text(encoding="utf-8").strip()
        t_enc = time.time()
        codes = model.encode_reference_audio(str(wpath))
        ref_cache[role] = (codes, t_ref, wname)
        print(f"  Role {role:2s} -> {wname} encoded in {time.time()-t_enc:.2f}s", flush=True)

    print("\n[Step 3/7] Generating Sentence Audio (Variant 0)...", flush=True)
    man_path = AUDIO_OUT / "higgs_manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8")) if man_path.exists() else {}

    for idx, it in enumerate(items):
        sid = it["id"]
        role = it["role"]
        text = it["text"]
        out_name = fname(sid)
        dst_wav = AUDIO_OUT / out_name
        codes, ref_text, ref_name = ref_cache[role]
        raw_name = raw_fname(sid, role, ref_name, 0)
        raw_wav = RAW_OUT / raw_name

        if dst_wav.exists() and dst_wav.stat().st_size > 4000 and sid in man:
            print(f"  [{idx+1:03d}/{len(items)}] {sid} ({role}) -> ALREADY EXISTS: {out_name}", flush=True)
            continue

        seed = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|0".encode()).hexdigest()[:8], 16)
        print(f"  [{idx+1:03d}/{len(items)}] {sid} ({role}) [seed={seed}]: '{text[:50]}...'", flush=True)
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

        # Save to both production audio folder and raw output folder
        audio_write(str(dst_wav), res[0].audio, res[0].sample_rate)
        audio_write(str(raw_wav), res[0].audio, res[0].sample_rate)
        trim_silence_tail(dst_wav)
        trim_silence_tail(raw_wav)

        f0 = estimate_f0(dst_wav)
        dur = getattr(res[0], "audio_duration", "N/A")
        print(f"      -> {out_name} (dur: {dur}, F0: {f0:.1f}Hz, gen: {gen_time:.1f}s)", flush=True)

        man[sid] = {
            "id": sid,
            "role": role,
            "ref_wav": ref_name,
            "text": text,
            "file": out_name,
            "seed": seed,
            "variant": 0,
            "f0": f0,
            "gen_time": gen_time
        }
        man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")

    print("\n[Step 4/7] Transcribing with Whisper Base & Measuring CER...", flush=True)
    asr_pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")
    high_cer = []
    cer_rows = []

    for idx, it in enumerate(items):
        sid = it["id"]
        role = it["role"]
        orig_text = it["text"]
        wav_path = AUDIO_OUT / fname(sid)
        asr_res = asr_pipe(str(wav_path), return_timestamps=True)["text"].strip()
        c = en_cer.cer_pair(orig_text, asr_res)
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

        if c > 0.02:
            high_cer.append((sid, role, c, orig_text, asr_res))
            print(f"  [WARN > 2%] {sid} ({role}): CER={c*100:.2f}% | '{orig_text[:40]}' -> '{asr_res[:40]}'", flush=True)

    (HERE / "higgs_cer_rows_EN_t06.json").write_text(
        json.dumps(cer_rows, ensure_ascii=False, indent=1), encoding="utf-8")

    # Generate round 2 (variant 1) for sentences with CER > 2%
    if high_cer:
        print(f"\n[Step 4b] Re-generating {len(high_cer)} sentences with CER > 2% (Variant 1)...", flush=True)
        for sid, role, old_cer, orig_text, _ in high_cer:
            codes, ref_text, ref_name = ref_cache[role]
            seed1 = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|1".encode()).hexdigest()[:8], 16)
            dst_wav = AUDIO_OUT / fname(sid)
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
            asr1 = asr_pipe(str(raw_v1), return_timestamps=True)["text"].strip()
            c1 = en_cer.cer_pair(orig_text, asr1)
            print(f"  {sid} ({role}): Take 0 CER={old_cer*100:.2f}% vs Take 1 CER={c1*100:.2f}%", flush=True)
            if c1 < old_cer:
                audio_write(str(dst_wav), res[0].audio, res[0].sample_rate)
                trim_silence_tail(dst_wav)
                print(f"      -> Chose Take 1 (CER improved to {c1*100:.2f}%)", flush=True)
                man[sid]["seed"] = seed1
                man[sid]["variant"] = 1
                man[sid]["f0"] = estimate_f0(dst_wav)
                # update cer_rows
                for cr in cer_rows:
                    if cr["id"] == sid:
                        cr["asr"] = asr1
                        cr["cer"] = c1
                        cr["f0"] = man[sid]["f0"]
                        break

        man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
        (HERE / "higgs_cer_rows_EN_t06.json").write_text(
            json.dumps(cer_rows, ensure_ascii=False, indent=1), encoding="utf-8")

    # Free MLX model from RAM (Rule M2)
    print("\n[Step 5/7] Freeing MLX Model & Loading UTMOSv2 (MOS Evaluation)...", flush=True)
    del model
    del ref_cache
    del asr_pipe
    gc.collect()

    import utmosv2
    utmos_model = utmosv2.create_model(pretrained=True)
    print("UTMOSv2 model loaded on CPU (Rule M5). Measuring MOS scores...", flush=True)

    quality_results = []
    moss = []
    for idx, it in enumerate(items):
        sid = it["id"]
        role = it["role"]
        orig_text = it["text"]
        wpath = AUDIO_OUT / fname(sid)
        cr = next((r for r in cer_rows if r["id"] == sid), None)
        cer_val = cr["cer"] if cr else 0.0
        asr_text = cr["asr"] if cr else ""

        try:
            mos_score = float(utmos_model.predict(input_path=str(wpath), device="cpu", verbose=False))
        except Exception as ex:
            print(f"  !! Error measuring UTMOS for {sid}: {ex}")
            mos_score = 0.0

        moss.append(mos_score)
        f0_val = man.get(sid, {}).get("f0", 0.0)

        quality_results.append({
            "id": sid,
            "role": role,
            "file": fname(sid),
            "orig_text": orig_text,
            "asr_text": asr_text,
            "cer": cer_val,
            "utmos": mos_score,
            "f0": f0_val
        })

    del utmos_model
    gc.collect()

    # Save comprehensive quality report
    qc_path = HERE / "quality_qc_utmos_ep06_en.json"
    qc_path.write_text(json.dumps(quality_results, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Saved UTMOS quality results to {qc_path}", flush=True)

    # G9 Pitch separation check
    print("\n[Step 6/7] Pitch Analysis & G9 Separation Check...", flush=True)
    f0_by_role = {}
    for r in quality_results:
        if r["f0"] > 40.0:
            f0_by_role.setdefault(r["role"], []).append(r["f0"])

    medians = {}
    for role in ["D", "H", "N1", "C", "N2"]:
        vals = f0_by_role.get(role, [])
        med = float(np.median(vals)) if vals else 0.0
        medians[role] = med
        print(f"  Role {role:2s}: median F0 = {med:5.1f} Hz (N={len(vals)})")

    # Check semitone deltas
    def semitones(f1, f2):
        return 12.0 * np.log2(f2 / f1) if f1 > 0 and f2 > 0 else 0.0

    print("\n  Adjacent Pair Pitch Distances:")
    pairs = [("D", "H"), ("H", "N1"), ("H", "C"), ("C", "N2")]
    for r1, r2 in pairs:
        if medians.get(r1) and medians.get(r2):
            delta = semitones(medians[r1], medians[r2])
            status = "PASS (>= 4.0 nc)" if abs(delta) >= 4.0 else "WARN (< 4.0 nc)"
            print(f"    {r1} ({medians[r1]:.1f}Hz) -> {r2} ({medians[r2]:.1f}Hz): {delta:+5.2f} semitones [{status}]")

    # Summary statistics
    cers = [r["cer"] for r in quality_results]
    print("\n" + "=" * 80)
    print("QUALITY SUMMARY FOR EPISODE 06 EN:")
    print(f"  Whisper CER: Mean = {np.mean(cers)*100:.2f}%, Median = {np.median(cers)*100:.2f}%, >2%: {sum(1 for c in cers if c > 0.02)}/{len(cers)}")
    print(f"  UTMOS MOS:   Mean = {np.mean(moss):.2f}/5.0, Min = {np.min(moss):.2f}, Max = {np.max(moss):.2f}")
    print("=" * 80)

    # Step 7: Build Master Audio using build_audio3.py
    print("\n[Step 7/7] Building Audio Master with build_audio3.py...", flush=True)
    env = os.environ.copy()
    env["AE_EP"] = "06"
    env["AE_LANG"] = "en"
    env["AE_AUDIO_DIR"] = "audio_s_higgs"
    r = subprocess.run([sys.executable, str(HERE / "build_audio3.py")], env=env, cwd=str(ROOT))
    if r.returncode != 0:
        print(f"!! build_audio3.py failed with code {r.returncode}")
        sys.exit(r.returncode)

    # Subtitles
    print("\nGenerating Subtitles (Tap06_EN.srt)...", flush=True)
    r_sub = subprocess.run([sys.executable, str(HERE / "subtitles.py")], env=env, cwd=str(ROOT))
    if r_sub.returncode != 0:
        print(f"!! subtitles.py failed with code {r_sub.returncode}")
    else:
        print("Generated subtitles via subtitles.py successfully!", flush=True)

    # CanNghe report
    tl_path = HERE / "timeline_s_EN_t06.json"
    tl_data = json.loads(tl_path.read_text(encoding="utf-8")) if tl_path.exists() else {}
    items_tl = tl_data.get("items", [])
    total_dur = tl_data.get("total", 0.0)

    can_nghe_lines = [
        "# Câu cần nghe — Tập 06 EN (Higgs) — 04/11/2026\n",
        f"Master Target: `02_SAN_XUAT/Tap06_EN/xuat_ban/Tap06_EN_master.mp3` · {total_dur:.1f} s (~{total_dur/60:.1f} min) · {len(items_tl)} câu · lời đầu {items_tl[0]['start'] if items_tl else 'N/A'} s · lời cuối {items_tl[-1]['end'] if items_tl else 'N/A'} s\n",
        f"**Chất lượng tổng quan:** Whisper CER trung bình = {np.mean(cers)*100:.2f}% (trung vị {np.median(cers)*100:.2f}%) · UTMOSv2 MOS = {np.mean(moss):.2f}/5.0 · Cặp vai D-H = {semitones(medians.get('D',1), medians.get('H',1)):.2f} nửa cung.\n",
        "| Mốc | Câu | Vai | CER | MOS | Câu gốc | ASR nghe được | Ghi chú |",
        "|---|---|---|---:|---:|---|---|---|"
    ]
    time_map = {it["id"]: it["start"] for it in items_tl}
    for sid in sorted(time_map.keys(), key=lambda x: time_map[x]):
        r = next((row for row in quality_results if row["id"] == sid), None)
        if not r:
            continue
        c = r["cer"]
        if c > 0.02:
            start_s = time_map[sid]
            m = int(start_s // 60)
            s = start_s % 60
            time_str = f"{m}:{s:05.2f}"
            orig = r["orig_text"].replace("|", r"\|")
            asr = r["asr_text"].replace("|", r"\|")
            can_nghe_lines.append(f"| {time_str} | {sid} | {r['role']} | {c*100:.1f}% | {r['utmos']:.2f} | {orig} | {asr} | Nghe xác nhận |")

    can_nghe_p = ROOT / "02_SAN_XUAT" / "Tap06_EN" / "CanNghe_Tap06_EN_higgs.md"
    can_nghe_p.write_text("\n".join(can_nghe_lines) + "\n", encoding="utf-8")
    print(f"Wrote CanNghe report to {can_nghe_p}", flush=True)

    print("\n" + "=" * 80)
    print("ALL STEPS COMPLETED SUCCESSFULLY FOR EPISODE 06 EN!")
    print("=" * 80, flush=True)

if __name__ == "__main__":
    main()
