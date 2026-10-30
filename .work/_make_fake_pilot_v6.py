"""Tao du lieu GIA cho pilot v6 de kiem chung script phan tich (khong goi ASR).

Muc dich: chay thu `.work/analyze_pilot_v6.py` tren manifest gia de bat loi
(trong luong file, tim file, tinh bang G9) TRUOC khi co du lieu that.

Khong dung tai len: thu muc nay la du lieu ao.
"""
import json
import pathlib
import shutil
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
TEST = HERE / "_test_pilot_v6"
WAVDIR = TEST / "out_higgs_v6" / "out_higgs_v6"
WAVDIR.mkdir(parents=True, exist_ok=True)

CELLS = [
    ("H", "M_LOW.wav", 140.0), ("D", "M_HIGH.wav", 200.0), ("C", "C.wav", 205.0),
    ("N1", "W6_LOW.wav", 186.0), ("N1", "W6_LOW_S25.wav", 170.0),
    ("N1", "W6_LOW_S30.wav", 160.0), ("N1", "W6_LOW_S35.wav", 150.0),
    ("N1", "W6_LOW_S40.wav", 145.0), ("N2", "W5_HIGH.wav", 295.0),
    ("N2", "W2.wav", 207.0), ("N2", "W1.wav", 276.0),
    ("H", "H.wav", 131.0), ("D", "D.wav", 122.0),
]
SENT = ["5.02#4", "2.04#1", "1.17#1", "3.05#1", "4.06#1", "1.03#1"]
TEXT = "Chào mừng bạn đến với chuyên mục giải mã tâm lý tội phạm mỗi hồ sơ đều bắt đầu."

SR = 24000


def tone(f0, dur=2.0):
    t = np.arange(int(SR * dur)) / SR
    return (0.3 * np.sin(2 * np.pi * f0 * t)).astype(np.float32)


rows = []
for role, ref, f0 in CELLS:
    for si, sid in enumerate(SENT):
        for vi in (0, 1):
            fn = f"{sid.replace('#','_').replace('.','_')}_{role}_{ref.replace('.wav','')}_t0.8_s{vi}.wav"
            with wave.open(str(WAVDIR / fn), "wb") as w:
                w.setnchannels(1)
                w.setsampwidth(2)
                w.setframerate(SR)
                w.writeframes((tone(f0 + (vi - 0.5) * 3.0) * 32767).astype(np.int16).tobytes())
            rows.append({
                "key": f"{sid}__{role}__{ref.replace('.wav','')}__{0.8:.1f}__s{vi}",
                "id": sid, "role": role, "ref_wav": ref, "emotion": "neutral",
                "emotion_tag": "", "text_sent": TEXT, "text_plain": TEXT,
                "temp": 0.8, "variant": vi, "seed": 12345, "top_p": 0.95, "top_k": 50,
                "max_new_tokens": 1196, "sr": SR, "file": fn,
                "duration_s": 2.0, "gen_s": 4.0, "rtf": 2.0,
                "peak": 0.3, "peak_dbfs": -10.5, "vram_gb": 9.9,
                "tag_words_risk": False, "shard": 0, "ok": True,
            })

(WAVDIR / "higgs_manifest.json").write_text(
    json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
(WAVDIR / "higgs_summary.json").write_text(json.dumps({"n_task": len(rows)}, indent=1),
                                            encoding="utf-8")
print("tao du lieu gia: %d dong -> %s" % (len(rows), WAVDIR))
