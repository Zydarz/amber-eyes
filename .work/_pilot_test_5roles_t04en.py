#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pilot test 5 roles for Episode 04 English using Higgs Audio v3 on MLX.
Checks:
1. Audio generation with pre-encoded reference codes from VoxCPM2.
2. F0 estimation (autocorrelation) to verify pitch separation between roles.
3. Whisper ASR transcription and CER calculation using en_cer.
"""
import os
import sys
import json
import time
import hashlib
import pathlib
import wave
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import en_cer

from mlx_audio.tts.utils import load as load_higgs
from mlx_audio.audio_io import write as audio_write
from transformers import pipeline

DS_DIR = HERE / "kaggle_higgs" / "dataset_voxcpm2_en"
OUT_DIR = HERE / "thu_giong_kiem_vai_t04_en"
OUT_DIR.mkdir(parents=True, exist_ok=True)

ROLES = {
    "H": ("H_EN.wav", "H_EN.txt", "1.03#1", "Autumn 2003."),
    "N1": ("N1_EN.wav", "N1_EN.txt", "1.07#1", "In the eyes of every nurse among us, Charlie was a wonderful friend."),
    "D": ("D_EN.wav", "D_EN.txt", "1.14#1", "When we pulled Charles Cullen's complete employment history, an appalling truth unraveled before our task force."),
    "C": ("C_EN.wav", "C_EN.txt", "2.11#1", "From the perspectives of organizational psychology and legal dynamics, this is a textbook demonstration of the Institutional Bystander Effect."),
    "N2": ("N2_EN.wav", "N2_EN.txt", "4.06#1", "When the detectives laid out Charlie's medication logs before me, the ground beneath my feet gave way completely."),
}

def estimate_f0(wav_path):
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

def main():
    print("=== [1/4] Loading Higgs Audio v3 Model ===", flush=True)
    t0 = time.time()
    model = load_higgs("bosonai/higgs-audio-v3-tts-4b")
    print(f"Model loaded in {time.time()-t0:.2f}s", flush=True)

    print("\n=== [2/4] Pre-encoding Reference Audio from VoxCPM ===", flush=True)
    ref_cache = {}
    for role, (wname, tname, _, _) in ROLES.items():
        wpath = DS_DIR / wname
        tpath = DS_DIR / tname
        t_ref = tpath.read_text(encoding="utf-8").strip()
        t_start = time.time()
        codes = model.encode_reference_audio(str(wpath))
        ref_cache[role] = (codes, t_ref)
        print(f"  Role {role:2s} -> {wname} encoded in {time.time()-t_start:.2f}s", flush=True)

    print("\n=== [3/4] Generating Audio for 5 Sample Roles ===", flush=True)
    gen_results = {}
    for role, (wname, _, sid, text) in ROLES.items():
        codes, ref_text = ref_cache[role]
        out_wav = OUT_DIR / f"{role}_{sid.replace('.', '_').replace('#', '_')}.wav"
        seed = int(hashlib.sha256(f"{sid}|{role}|{wname}|0.8|0".encode()).hexdigest()[:8], 16)
        print(f"  Generating {role} ({sid}): '{text[:40]}...' [seed={seed}]", flush=True)
        t_gen = time.time()
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
        gen_time = time.time() - t_gen
        audio_write(str(out_wav), res[0].audio, res[0].sample_rate)
        f0 = estimate_f0(str(out_wav))
        gen_results[role] = {
            "id": sid,
            "text": text,
            "wav": str(out_wav),
            "f0": f0,
            "gen_time": gen_time,
            "duration": getattr(res[0], "audio_duration", "N/A")
        }
        print(f"    -> Saved {out_wav.name} (dur: {gen_results[role]['duration']}, F0: {f0:.1f}Hz, time: {gen_time:.1f}s)", flush=True)

    print("\n=== [4/4] Transcribing with Whisper & Measuring CER ===", flush=True)
    asr_pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")
    report_rows = []
    for role in ["H", "D", "C", "N1", "N2"]:
        info = gen_results[role]
        trans = asr_pipe(info["wav"])["text"].strip()
        c = en_cer.cer_pair(info["text"], trans)
        info["transcription"] = trans
        info["cer"] = c
        report_rows.append((role, info["id"], info["f0"], c, info["text"], trans))

    print("\n" + "="*80)
    print("PILOT TEST SUMMARY REPORT — TAP 04 EN (HIGGS + VOXCPM REFERENCES)")
    print("="*80)
    print(f"{'Role':<5} {'ID':<8} {'F0 (Hz)':<10} {'CER':<8} {'Original Text':<30} -> {'ASR Transcription'}")
    print("-"*80)
    for r, sid, f0, c, orig, tr in report_rows:
        print(f"{r:<5} {sid:<8} {f0:<10.1f} {c*100:<7.2f}% {orig[:28]:<30} -> {tr}")
    print("="*80)

    # Check G9 semitone separation between roles
    f0_map = {r: info["f0"] for r, info in gen_results.items() if info["f0"] > 0}
    print("\nPITCH INTERVALS (SEMITONES):")
    pairs = [("H", "D"), ("H", "C"), ("D", "C"), ("H", "N1"), ("C", "N2")]
    for r1, r2 in pairs:
        if r1 in f0_map and r2 in f0_map:
            nc = abs(12 * np.log2(f0_map[r1] / f0_map[r2]))
            status = "PASS (>= 4 nc)" if nc >= 4.0 else "WARN (< 4 nc)"
            print(f"  {r1} ({f0_map[r1]:.1f} Hz) <-> {r2} ({f0_map[r2]:.1f} Hz) = {nc:.2f} semitones -> {status}")

if __name__ == "__main__":
    main()
