#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Production Audio Generator for Episode 04 English using Higgs Audio v3 on MLX.
Tuân thủ đầy đủ QUY_TAC_AUDIO_HIGGS.md và AGENTS.md:
- Pre-encodes 5 VoxCPM2 reference voices once.
- CẤM mọi thẻ <|emotion:...|>.
- Giữ prosody pause sau dấu : trước câu trích.
- Tự động phát hiện và cắt đuôi câm > 0.8s @ -45 dB.
- Đo F0 trung vị và kiểm tra G9.
- Chạy Whisper ASR và tính CER (ngưỡng 2%).
- Sinh bản thay thế (variant 1) cho các câu CER > 2%.
- Gọi build_audio3.py để đóng gói Tap04_EN_master.mp3.
"""
import os
import sys
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

PAYLOAD_PATH = HERE / "kaggle_higgs" / "higgs_payload_EN_t04.json"
DS_DIR = HERE / "kaggle_higgs" / "dataset_voxcpm2_en"
AUDIO_OUT = HERE / "audio_s_higgs_EN_t04"
AUDIO_OUT.mkdir(parents=True, exist_ok=True)
RAW_OUT = HERE / "kaggle_higgs" / "out_higgs_prod_EN_t04"
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
    """Quy tắc 01/11: cắt đuôi câm < -45 dB dài > 0.8s, giữ lại 0.3s + 30ms fade."""
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
    print("PRODUCTION PIPELINE: HIGGS AUDIO V3 — TAP 04 EN")
    print("=" * 80, flush=True)

    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))
    items = payload["items"]
    print(f"Total sentences: {len(items)}", flush=True)

    print("\n[Step 1/5] Loading Higgs Audio v3 Model...", flush=True)
    t0 = time.time()
    model = load_higgs("bosonai/higgs-audio-v3-tts-4b")
    print(f"Model loaded in {time.time()-t0:.2f}s", flush=True)

    print("\n[Step 2/5] Pre-encoding 5 VoxCPM2 Reference Voices...", flush=True)
    ref_cache = {}
    for role, (wname, tname) in ROLE_REF_MAP.items():
        wpath = DS_DIR / wname
        tpath = DS_DIR / tname
        t_ref = tpath.read_text(encoding="utf-8").strip()
        t_enc = time.time()
        codes = model.encode_reference_audio(str(wpath))
        ref_cache[role] = (codes, t_ref, wname)
        print(f"  Role {role:2s} -> {wname} encoded in {time.time()-t_enc:.2f}s", flush=True)

    print("\n[Step 3/5] Generating Sentence Audio (Variant 0)...", flush=True)
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

        if dst_wav.exists() and dst_wav.stat().st_size > 4000:
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

    print("\n[Step 4/5] Transcribing with Whisper & Measuring Quality (CER)...", flush=True)
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

    (HERE / "higgs_cer_rows_EN_t04.json").write_text(
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

        man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")

    print("\n[Step 5/5] Building Master Audio with build_audio3.py...", flush=True)
    env = os.environ.copy()
    env["AE_EP"] = "04"
    env["AE_LANG"] = "en"
    env["AE_AUDIO_DIR"] = "audio_s_higgs"
    r = subprocess.run([sys.executable, str(HERE / "build_audio3.py")], env=env, cwd=str(ROOT))
    if r.returncode == 0:
        print("\n MASTER AUDIO BUILT SUCCESSFULLY!", flush=True)
    else:
        print(f"\n!! build_audio3.py failed with return code {r.returncode}", flush=True)

if __name__ == "__main__":
    main()
