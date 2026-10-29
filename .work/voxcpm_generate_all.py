#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate VoxCPM2 Voice Design takes for 7 roles according to:
- 00_TIEU_CHUAN/TAO_GIONG_MAU_VOXCPM2.md
- 00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md

Run using:
  /Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_all.py
"""
import datetime
import json
import os
import re
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from voxcpm import VoxCPM

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
RAW = WORK / "voxcpm_raw"
MANIFEST = WORK / "voxcpm_refs_manifest.json"

F0_TARGET = {
    "H": (100, 106),
    "D": (138, 148),
    "C": (202, 212),
    "W1": (228, 242),
    "W2": (180, 192),
    "W3": (162, 175),
    "W4": (120, 128),
}

def f0_median(audio_np, sr=48000):
    # Resample to 16kHz for pitch detection
    import subprocess
    import shutil
    ff = shutil.which("ffmpeg") or "ffmpeg"
    tmp_in = f"/tmp/_f0_tmp_{os.getpid()}.wav"
    sf.write(tmp_in, audio_np, sr)
    r = subprocess.run([ff, "-v", "error", "-i", tmp_in, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                       capture_output=True)
    try:
        os.remove(tmp_in)
    except OSError:
        pass
    if r.returncode != 0 or not r.stdout:
        return 0.0
    x = np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768
    sr_res = 16000
    win, hop, out = int(0.04 * sr_res), int(0.01 * sr_res), []
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.02:
            continue
        f = f - f.mean()
        ac = np.correlate(f, f, "full")[win - 1:]
        lo, hi = int(sr_res / 400), int(sr_res / 70)
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.3 * ac[0]:
            out.append(sr_res / k)
    return float(np.median(out)) if out else 0.0

def main():
    print("=" * 70)
    print("VOXCPM2 VOICE DESIGN GENERATOR (7 ROLES)")
    print("=" * 70)

    if not MANIFEST.exists():
        sys.exit(f"Missing manifest: {MANIFEST}")

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    RAW.mkdir(parents=True, exist_ok=True)

    print("\n[1/2] Loading VoxCPM2 model on MPS...")
    t0 = time.time()
    model = VoxCPM.from_pretrained(
        "openbmb/VoxCPM2",
        optimize=False,
        device="mps",
        local_files_only=True
    )
    print(f"✓ Model loaded in {time.time() - t0:.2f}s!")

    sample_rate = getattr(model.tts_model, "sample_rate", 48000)

    # Seeds and CFG configs for takes
    # Takes 1-3: standard seeds with CFG 2.0
    # Takes 4-5: alternative seeds or CFG 2.5 if needed
    take_configs = [
        {"cfg": 2.0, "seed": 42},
        {"cfg": 2.0, "seed": 101},
        {"cfg": 2.0, "seed": 2024},
        {"cfg": 2.5, "seed": 777},
        {"cfg": 2.5, "seed": 999},
    ]

    print("\n[2/2] Generating takes for 7 roles...")

    for role, data in manifest.items():
        role_dir = RAW / role
        role_dir.mkdir(parents=True, exist_ok=True)

        control_raw = data.get("control", "").strip()
        control_clean = re.sub(r"[()（）]", "", control_raw).strip()
        target_text = data.get("text", "").strip()
        final_text = f"({control_clean}){target_text}"

        lo_f0, hi_f0 = F0_TARGET.get(role, (0, 0))
        print(f"\n--- Vai {role} (Target F0: {lo_f0}–{hi_f0} Hz) ---")
        print(f"Text: {target_text}")

        takes_records = []
        takes_json_path = role_dir / "takes.json"
        if takes_json_path.exists():
            try:
                takes_records = json.loads(takes_json_path.read_text(encoding="utf-8"))
            except Exception:
                takes_records = []

        # We will generate at least 3 takes, up to 5 if F0 not in range
        max_takes = 3
        current_take_idx = 0

        while current_take_idx < len(take_configs):
            cfg_info = take_configs[current_take_idx]
            cfg = cfg_info["cfg"]
            seed = cfg_info["seed"]
            take_num = current_take_idx + 1
            take_filename = f"{role}_take{take_num:02d}.wav"
            out_path = role_dir / take_filename

            print(f"  > Sinh {take_filename} (seed={seed}, cfg={cfg})...", end="", flush=True)
            t_start = time.time()

            try:
                torch.manual_seed(seed)
                if torch.backends.mps.is_available():
                    torch.mps.manual_seed(seed)
                audio = model.generate(
                    text=final_text,
                    cfg_value=cfg,
                    inference_timesteps=10,
                    normalize=False,
                )
            except Exception as e:
                print(f" LỖI: {e}")
                current_take_idx += 1
                continue

            t_dur = time.time() - t_start
            audio_len_s = len(audio) / sample_rate
            sf.write(str(out_path), audio, sample_rate)

            # Measure F0
            f0_measured = f0_median(audio, sample_rate)
            f0_in_range = (lo_f0 * 0.94 <= f0_measured <= hi_f0 * 1.06)

            print(f" Xong ({t_dur:.1f}s) | Độ dài: {audio_len_s:.2f}s | F0: {f0_measured:.1f}Hz {'[ĐẠT F0]' if f0_in_range else '[LỆCH F0]'}")

            rec = {
                "take": take_filename,
                "role": role,
                "file": str(out_path.relative_to(ROOT)),
                "seed": seed,
                "cfg": cfg,
                "timesteps": 10,
                "normalize": False,
                "sample_rate": sample_rate,
                "duration_s": round(audio_len_s, 2),
                "f0_hz": round(f0_measured, 1),
                "f0_target_hz": [lo_f0, hi_f0],
                "f0_in_range": f0_in_range,
                "generated_at": datetime.datetime.now().isoformat(),
                "tool": "VoxCPM2 (OpenBMB, Voice Design)",
                "license": "Apache-2.0"
            }
            takes_records.append(rec)
            takes_json_path.write_text(json.dumps(takes_records, ensure_ascii=False, indent=2), encoding="utf-8")

            current_take_idx += 1
            # If we've completed at least 3 takes, check if any take has F0 in range
            if current_take_idx >= 3:
                has_passing_f0 = any(t.get("f0_in_range") for t in takes_records)
                if has_passing_f0 or current_take_idx >= 5:
                    break
                else:
                    print(f"    (Chưa có bản nào trong dải F0 {lo_f0}–{hi_f0}Hz, tiếp tục sinh take {current_take_idx + 1}...)")

    print("\n" + "=" * 70)
    print("HOÀN TẤT SINH GIỌNG MẪU CHO 7 VAI!")
    print(f"Các file đã được lưu tại: {RAW}")
    print("=" * 70)

if __name__ == "__main__":
    main()
