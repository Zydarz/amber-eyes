#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
import time
import re
from pathlib import Path
import numpy as np
import soundfile as sf
import torch
from voxcpm import VoxCPM

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT_DIR = WORK / "voxcpm_raw" / "W_MALE_EXTRA"
OUT_DIR.mkdir(parents=True, exist_ok=True)

CONTROL_INSTRUCTION = (
    "A young man in his early to mid twenties, medium-pitched and clear with a light youthful timbre, "
    "conversational and natural, Vietnamese Standard, strictly neutral tone, steady everyday pace"
)

TARGET_TEXT = (
    "Lúc tôi đi qua ngã tư thì đèn đường đã tắt gần hết, chỉ còn lại ánh sáng vàng mờ ở góc quán nước. "
    "Đường phố ban đêm khá yên tĩnh, thỉnh thoảng có vài người đi bộ hoặc xe máy chạy chậm qua. "
    "Mọi chuyện diễn ra rất bình thường, không có bất kỳ dấu hiệu xáo trộn hay tiếng động lạ nào xung quanh."
)

control_clean = re.sub(r"[()（）]", "", CONTROL_INSTRUCTION).strip()
FINAL_TEXT = f"({control_clean}){TARGET_TEXT}"

def measure_f0(audio_np, sr=48000):
    import subprocess
    import shutil
    ff = shutil.which("ffmpeg") or "ffmpeg"
    tmp_in = f"/tmp/_f0_tmp_{os.getpid()}_{time.time_ns()}.wav"
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
    win, hop = int(0.04 * sr_res), int(0.01 * sr_res)
    freqs = []
    for s in range(0, len(x) - win, hop):
        seg = x[s:s + win]
        if np.sqrt((seg ** 2).mean()) < 0.02:
            continue
        corr = np.correlate(seg, seg, mode="full")[win - 1:]
        lag_min, lag_max = int(sr_res / 350), int(sr_res / 70)
        corr_seg = corr[lag_min:lag_max]
        if len(corr_seg) > 0 and corr_seg.max() > 0.3 * corr[0]:
            p = lag_min + corr_seg.argmax()
            freqs.append(sr_res / p)
    return float(np.median(freqs)) if freqs else 0.0

def main():
    print(f"[{time.strftime('%H:%M:%S')}] Khởi tạo VoxCPM trên Apple Silicon MPS (local_files_only=True, load_denoiser=False)...")
    model = VoxCPM.from_pretrained(
        "openbmb/VoxCPM2",
        optimize=False,
        device="mps",
        local_files_only=True,
        load_denoiser=False
    )
    
    seeds = [123, 456, 789, 101112]
    results = []
    
    print(f"[{time.strftime('%H:%M:%S')}] Bắt đầu sinh 4 take giọng nam phụ trẻ (mục tiêu F0: 160–175 Hz)...")
    for i, seed in enumerate(seeds, start=1):
        print(f"\n--- Sinh Take {i:02d} (seed={seed}, cfg=2.0) ---", flush=True)
        t0 = time.time()
        torch.manual_seed(seed)
        if torch.backends.mps.is_available():
            torch.mps.manual_seed(seed)
            
        audio = model.generate(
            text=FINAL_TEXT,
            cfg_value=2.0,
            inference_timesteps=10,
            normalize=False,
        )
        dur = len(audio) / 48000.0
        elapsed = time.time() - t0
        
        f0 = measure_f0(audio, sr=48000)
        
        out_wav = OUT_DIR / f"male_young_take{i:02d}_s{seed}.wav"
        out_txt = OUT_DIR / f"male_young_take{i:02d}_s{seed}.txt"
        
        sf.write(str(out_wav), audio, 48000)
        out_txt.write_text(TARGET_TEXT, encoding="utf-8")
        
        status = "OK" if 155 <= f0 <= 180 else "NGOÀI DẢI"
        print(f"Take {i:02d}: Thời lượng {dur:.1f}s | F0 median: {f0:.1f} Hz [{status}] | Thời gian chạy: {elapsed:.1f}s", flush=True)
        results.append({
            "take": i,
            "seed": seed,
            "wav": str(out_wav),
            "txt": str(out_txt),
            "f0": f0,
            "dur": dur,
            "status": status
        })
        
    print("\n" + "="*50)
    print("TỔNG KẾT KẾT QUẢ SINH GIỌNG NAM PHỤ:")
    for r in results:
        print(f"Take {r['take']:02d} (seed {r['seed']}): F0 = {r['f0']:.1f} Hz ({r['status']}) -> {r['wav']}")

if __name__ == "__main__":
    main()
