#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate and package VoxCPM2 voice reference sets for EN, JA, and KO.

Standards:
- 7 roles: H, D, C, W1, W2, W3, W4
- Duration: ~20s (18-26s)
- Format: WAV PCM 16-bit mono 24000 Hz, -18 LUFS, True Peak <= -1.5 dBFS
- Clean transcripts in .txt (Unicode NFC)
- refs.json with provenance metadata
"""
import datetime
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from voxcpm import VoxCPM

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = shutil.which("ffmpeg") or "ffmpeg"
FP = shutil.which("ffprobe") or "ffprobe"

LANGS = ["en", "ja", "ko"]

F0_TARGET = {
    "H": (100, 118),
    "D": (115, 135),
    "C": (200, 220),
    "W1": (220, 255),
    "W2": (175, 205),
    "W3": (150, 180),
    "W4": (115, 135),
}

def pcm(p, sr=16000):
    cmd = [FF, "-v", "error", "-i", str(p), "-ac", "1", "-ar", str(sr), "-f", "s16le", "-"]
    r = subprocess.run(cmd, capture_output=True, check=True)
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768.0, sr

def frames_db(x, sr, win_s=0.02, hop_s=0.01):
    win, hop = int(win_s * sr), int(hop_s * sr)
    rms = [np.sqrt(np.mean(x[s:s+win]**2) + 1e-12) for s in range(0, len(x)-win, hop)]
    return 20.0 * np.log10(np.maximum(rms, 1e-6))

def speech_span(db, thr=-50.0, hop_s=0.01):
    voiced = np.where(db > thr)[0]
    if len(voiced) == 0:
        return 0.0, 0.0, 0.0, 0.0
    lead_s = float(voiced[0] * hop_s)
    trail_s = float((len(db) - 1 - voiced[-1]) * hop_s)
    speech_s = float((voiced[-1] - voiced[0] + 1) * hop_s)
    gaps, cur = [], 0
    for v in db[voiced[0]:voiced[-1] + 1] > thr:
        if not v:
            cur += 1
        elif cur:
            gaps.append(cur * hop_s)
            cur = 0
    return speech_s, lead_s, trail_s, max(gaps) if gaps else 0.0

def f0_track(x, sr=16000, win_s=0.04, hop_s=0.01):
    win, hop = int(win_s * sr), int(hop_s * sr)
    lo, hi = int(sr / 400), int(sr / 70)
    out = []
    for s in range(0, len(x) - win, hop):
        seg = x[s:s + win]
        if np.sqrt(np.mean(seg ** 2)) < 0.02:
            continue
        seg = seg - seg.mean()
        ac = np.correlate(seg, seg, "full")[win - 1:]
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.3 * ac[0]:
            out.append(sr / k)
    return np.array(out)

def loudness(p):
    r = subprocess.run([FF, "-nostats", "-i", str(p), "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    tail = r.stderr[r.stderr.rfind("Summary:"):]
    i = re.search(r"I:\s*(-?[\d.]+) LUFS", tail)
    tp = re.search(r"Peak:\s*(-?[\d.inf]+) dBFS", tail)
    return (float(i.group(1)) if i else None, float(tp.group(1)) if tp and "inf" not in tp.group(1) else None)

def main():
    print("=" * 70)
    print("VOXCPM2 MULTILINGUAL VOICE REFERENCE GENERATOR (EN, JA, KO)")
    print("=" * 70)

    print("\n[1/3] Loading VoxCPM2 model on MPS...")
    t0 = time.time()
    model = VoxCPM.from_pretrained(
        "openbmb/VoxCPM2",
        optimize=False,
        device="mps",
        local_files_only=True
    )
    sr_model = getattr(model.tts_model, "sample_rate", 48000)
    print(f"✓ Model loaded in {time.time() - t0:.2f}s!")

    flt = ("aresample=24000,"
           "loudnorm=I=-18:TP=-2.0:LRA=11,"
           "silenceremove=start_periods=1:start_threshold=-50dB,"
           "areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse")

    summary_results = {}

    for lang in LANGS:
        print(f"\n{'='*30} LANGUAGE: {lang.upper()} {'='*30}")
        mf_path = WORK / f"voxcpm_refs_manifest_{lang}.json"
        if not mf_path.exists():
            print(f"Error: missing {mf_path}")
            continue
        manifest = json.loads(mf_path.read_text(encoding="utf-8"))

        out_dir = ROOT / "assets" / f"voice_ref_voxcpm2_{lang}"
        raw_dir = WORK / f"voxcpm_raw_{lang}"
        out_dir.mkdir(parents=True, exist_ok=True)
        raw_dir.mkdir(parents=True, exist_ok=True)

        refs_meta = {}
        summary_results[lang] = []

        for role, data in manifest.items():
            ctrl_raw = data.get("control", "").strip()
            ctrl_clean = re.sub(r"[()（）]", "", ctrl_raw).strip()
            target_text = data.get("text", "").strip()
            full_prompt = f"({ctrl_clean}){target_text}"

            print(f"\n--- [{lang.upper()}] Vai {role} ---")
            print(f"Prompt text: {target_text[:60]}...")

            # Seeds to try
            seeds = [42, 101, 2024, 777]
            best_take = None
            best_f0_diff = 9999.0

            for seed in seeds:
                raw_wav = raw_dir / f"{role}_seed{seed}.wav"
                torch.manual_seed(seed)
                if torch.backends.mps.is_available():
                    torch.mps.manual_seed(seed)
                t_start = time.time()
                try:
                    audio = model.generate(text=full_prompt, cfg_value=2.0, inference_timesteps=10, normalize=False)
                except Exception as e:
                    print(f"  Seed {seed} error: {e}")
                    continue
                gen_dur = time.time() - t_start
                raw_dur = len(audio) / sr_model
                sf.write(str(raw_wav), audio, sr_model)

                # Check F0 and duration
                x_p, sr_p = pcm(raw_wav)
                db = frames_db(x_p, sr_p)
                sp, _, _, gap = speech_span(db)
                f0s = f0_track(x_p, sr_p)
                f0_med = float(np.median(f0s)) if len(f0s) else 0.0

                lo_f0, hi_f0 = F0_TARGET[role]
                mid_f0 = (lo_f0 + hi_f0) / 2
                f0_diff = abs(f0_med - mid_f0)

                print(f"  > Seed {seed} ({gen_dur:.1f}s): speech={sp:.2f}s, gap={gap:.2f}s, F0={f0_med:.1f}Hz (target {lo_f0}–{hi_f0}Hz)")

                # If speech is between 16s and 27s
                if 16.0 <= sp <= 27.0:
                    if best_take is None or f0_diff < best_f0_diff:
                        best_take = raw_wav
                        best_f0_diff = f0_diff
                        if lo_f0 * 0.93 <= f0_med <= hi_f0 * 1.07:
                            # Found a good one!
                            break

            if best_take is None:
                best_take = raw_wav

            # Package best take
            dst_wav = out_dir / f"{role}.wav"
            dst_txt = out_dir / f"{role}.txt"
            dst_txt.write_text(target_text + "\n", encoding="utf-8")

            subprocess.run([
                FF, "-y", "-i", str(best_take),
                "-af", flt,
                "-c:a", "pcm_s16le", "-ar", "24000", "-ac", "1",
                str(dst_wav)
            ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

            # Measure packaged
            x_fin, sr_fin = pcm(dst_wav)
            db_fin = frames_db(x_fin, sr_fin)
            sp_fin, lead_fin, trail_fin, gap_fin = speech_span(db_fin)
            f0s_fin = f0_track(x_fin, sr_fin)
            f0_fin = float(np.median(f0s_fin)) if len(f0s_fin) else 0.0
            lufs_val, tp_val = loudness(dst_wav)
            sha = hashlib.sha256(dst_wav.read_bytes()).hexdigest()

            rec = {
                "role": role,
                "language": lang,
                "seconds": round(sp_fin, 2),
                "f0_median_hz": round(f0_fin, 1),
                "f0_target_hz": list(F0_TARGET[role]),
                "lufs": lufs_val,
                "true_peak": tp_val,
                "max_gap_s": round(gap_fin, 2),
                "source_file": str(best_take.relative_to(ROOT)),
                "control_instruction": ctrl_raw,
                "target_text": target_text,
                "sample_rate": 24000,
                "channels": 1,
                "sha256": sha,
                "license": "Apache-2.0"
            }
            refs_meta[role] = rec
            summary_results[lang].append(rec)
            print(f"  ✓ ĐÓNG GÓI {role}.wav: {sp_fin:.2f}s | F0: {f0_fin:.1f}Hz | LUFS: {lufs_val} | TP: {tp_val} dBFS")

        (out_dir / "refs.json").write_text(json.dumps(refs_meta, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n" + "=" * 70)
    print("HOÀN TẤT SINH VÀ ĐÓNG GÓI CHO EN, JA, KO!")
    print("=" * 70)

if __name__ == "__main__":
    main()
