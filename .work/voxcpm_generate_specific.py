#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    print("Loading VoxCPM2 model on MPS...")
    model = VoxCPM.from_pretrained(
        "openbmb/VoxCPM2",
        optimize=False,
        device="mps",
        local_files_only=True
    )
    sample_rate = getattr(model.tts_model, "sample_rate", 48000)

    # 1. Generate role H with expanded text (37 words, ~8.5-9.5s)
    h_text = "Chào mừng bạn đến với chuyên mục giải mã tâm lý tội phạm. Mỗi hồ sơ đều bắt đầu bằng câu hỏi nặng trĩu, mà không ai trả lời nổi, dù sự thật vẫn luôn nằm ở đó."
    h_control = "A man in his early forties, low-pitched and warm with a deep chesty resonance, calm and unhurried, intimate late-night podcast narration, Vietnamese Standard, neutral and reflective tone, moderately slow pace"
    h_final = f"({h_control}){h_text}"
    h_dir = RAW / "H"
    h_records = []
    print("\n--- Regenerating H ---")
    for idx, (seed, cfg) in enumerate([(42, 2.0), (101, 2.0), (2024, 2.0), (777, 2.5)]):
        fn = f"H_take{idx+1:02d}.wav"
        out_p = h_dir / fn
        torch.manual_seed(seed)
        if torch.backends.mps.is_available():
            torch.mps.manual_seed(seed)
        audio = model.generate(text=h_final, cfg_value=cfg, inference_timesteps=10, normalize=False)
        sf.write(str(out_p), audio, sample_rate)
        f0 = f0_median(audio, sample_rate)
        dur = len(audio) / sample_rate
        in_range = (100 * 0.94 <= f0 <= 106 * 1.06)
        print(f"H {fn}: dur={dur:.2f}s, F0={f0:.1f}Hz, in_range={in_range}")
        h_records.append({
            "take": fn, "role": "H", "file": str(out_p.relative_to(ROOT)),
            "seed": seed, "cfg": cfg, "timesteps": 10, "normalize": False,
            "sample_rate": sample_rate, "duration_s": round(dur, 2), "f0_hz": round(f0, 1),
            "f0_target_hz": [100, 106], "f0_in_range": in_range,
            "generated_at": datetime.datetime.now().isoformat(),
            "tool": "VoxCPM2 (OpenBMB, Voice Design)", "license": "Apache-2.0"
        })
    (h_dir / "takes.json").write_text(json.dumps(h_records, ensure_ascii=False, indent=2), encoding="utf-8")

    # 2. Generate extra takes for W3 targeting 162-175 Hz
    w3_text = "Xe buýt cuối tuyến chạy khá thưa, nên tôi thường phải đi bộ thêm đoạn dài nữa. Đường lúc đó vắng lặng, chỉ có mấy cây đèn còn sáng, và tôi hay tự hỏi mình sẽ đi bao xa, nửa như không biết."
    w3_control = "A young man in his mid twenties, clear with a youthful timbre, slightly bright tone, open and casual, Vietnamese Standard, neutral and relaxed, natural everyday pace"
    w3_final = f"({w3_control}){w3_text}"
    w3_dir = RAW / "W3"
    w3_json_path = w3_dir / "takes.json"
    w3_records = json.loads(w3_json_path.read_text(encoding="utf-8")) if w3_json_path.exists() else []
    print("\n--- Additional takes for W3 ---")
    for idx, (seed, cfg) in enumerate([(123, 2.0), (456, 2.0), (888, 2.0)]):
        take_num = len(w3_records) + 1
        fn = f"W3_take{take_num:02d}.wav"
        out_p = w3_dir / fn
        torch.manual_seed(seed)
        if torch.backends.mps.is_available():
            torch.mps.manual_seed(seed)
        audio = model.generate(text=w3_final, cfg_value=cfg, inference_timesteps=10, normalize=False)
        sf.write(str(out_p), audio, sample_rate)
        f0 = f0_median(audio, sample_rate)
        dur = len(audio) / sample_rate
        in_range = (162 * 0.94 <= f0 <= 175 * 1.06)
        print(f"W3 {fn}: dur={dur:.2f}s, F0={f0:.1f}Hz, in_range={in_range}")
        w3_records.append({
            "take": fn, "role": "W3", "file": str(out_p.relative_to(ROOT)),
            "seed": seed, "cfg": cfg, "timesteps": 10, "normalize": False,
            "sample_rate": sample_rate, "duration_s": round(dur, 2), "f0_hz": round(f0, 1),
            "f0_target_hz": [162, 175], "f0_in_range": in_range,
            "generated_at": datetime.datetime.now().isoformat(),
            "tool": "VoxCPM2 (OpenBMB, Voice Design)", "license": "Apache-2.0"
        })
    w3_json_path.write_text(json.dumps(w3_records, ensure_ascii=False, indent=2), encoding="utf-8")

    # 3. Generate extra takes for W4 targeting 120-128 Hz
    w4_text = "Tôi mở quán trước nhà từ sáng sớm, và mỗi ngày đều đóng cửa khá muộn. Hàng xóm quen mặt, nên ai gọi cửa tôi cũng mở. Có hỏi chuyện buôn bán, tôi cũng chịu nói, nửa như người quen."
    w4_control = "A man in his early fifties, low-pitched and slightly rough with an aged timbre, steady and grounded, conversational, Vietnamese Standard, neutral and calm tone, slow natural pace"
    w4_final = f"({w4_control}){w4_text}"
    w4_dir = RAW / "W4"
    w4_json_path = w4_dir / "takes.json"
    w4_records = json.loads(w4_json_path.read_text(encoding="utf-8")) if w4_json_path.exists() else []
    print("\n--- Additional takes for W4 ---")
    for idx, (seed, cfg) in enumerate([(321, 2.0), (654, 2.0)]):
        take_num = len(w4_records) + 1
        fn = f"W4_take{take_num:02d}.wav"
        out_p = w4_dir / fn
        torch.manual_seed(seed)
        if torch.backends.mps.is_available():
            torch.mps.manual_seed(seed)
        audio = model.generate(text=w4_final, cfg_value=cfg, inference_timesteps=10, normalize=False)
        sf.write(str(out_p), audio, sample_rate)
        f0 = f0_median(audio, sample_rate)
        dur = len(audio) / sample_rate
        in_range = (120 * 0.94 <= f0 <= 128 * 1.06)
        print(f"W4 {fn}: dur={dur:.2f}s, F0={f0:.1f}Hz, in_range={in_range}")
        w4_records.append({
            "take": fn, "role": "W4", "file": str(out_p.relative_to(ROOT)),
            "seed": seed, "cfg": cfg, "timesteps": 10, "normalize": False,
            "sample_rate": sample_rate, "duration_s": round(dur, 2), "f0_hz": round(f0, 1),
            "f0_target_hz": [120, 128], "f0_in_range": in_range,
            "generated_at": datetime.datetime.now().isoformat(),
            "tool": "VoxCPM2 (OpenBMB, Voice Design)", "license": "Apache-2.0"
        })
    w4_json_path.write_text(json.dumps(w4_records, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\nDone generating targeted takes!")

if __name__ == "__main__":
    main()
