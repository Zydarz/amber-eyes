# -*- coding: utf-8 -*-
"""Tạo STEM GIẢ LẬP từ master mp3 khi KHÔNG có stems thật (vd. audio Higgs sinh trên máy khác chỉ chuyển sang bản mp3).

    AE_EP=11 [AE_LANG=en|ja] py -3 .work/make_pseudo_stems.py

Mỗi vai H/D/C/N1/N2 = master (mono, 24 kHz) chỉ giữ trong CỬA SỔ THỜI GIAN câu của vai đó
(theo timeline_s*.json), ngoài cửa sổ = 0. Renderer (build_video3.py) và cổng H24
(qc_wave_gate.py) đọc như stems thật — KHÔNG sửa script dùng chung.

GIỚI HẠN (ghi rõ trong báo cáo): trong cửa sổ câu, master còn lẫn nhạc nền/SFX (đã bị ducking
dưới giọng). Do đó:
  - Chỉ dùng cho SÓNG BADGE + cổng H24. KHÔNG thay stems thật cho cổng A14 (mất giọng) —
    A14 trên stems giả là vô nghĩa; thư mục có file _PSEUDO.txt để các cổng/AI sau nhận ra.
  - Thư mục stems cũ (nếu có) được chuyển sang .work/_cu/ trước khi ghi (L5).
"""
import json
import shutil
import subprocess
import sys
import time
import wave
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
import edition as ED  # noqa: E402

SR = 24000
ROLES = ["H", "D", "C", "N1", "N2"]


def ffmpeg():
    w = ED.WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
    return str(w) if w.exists() else shutil.which("ffmpeg")


def main():
    master = ED.OUT_DIR / f"{ED.EP['master']}.mp3"
    if not master.exists():
        sys.exit(f"thiếu master: {master}")
    tl = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
    sd = ED.w("stems")
    if sd.exists() and any(sd.glob("*.wav")) and not (sd / "_PSEUDO.txt").exists():
        sys.exit(f"{sd} đang có stems THẬT — không ghi đè (L5). Chuyển đi trước nếu thực sự muốn.")
    if sd.exists():
        shutil.rmtree(sd)
    sd.mkdir(parents=True)
    raw = sd / "_master.raw"
    subprocess.run([ffmpeg(), "-v", "error", "-y", "-i", str(master), "-ac", "1", "-ar", str(SR),
                    "-f", "s16le", str(raw)], check=True)
    pcm = np.fromfile(raw, np.int16)
    raw.unlink()
    dur = len(pcm) / SR
    print(f"master {master.name}: {dur:.2f} s (timeline.total {tl['total']:.2f} s, lệch {abs(dur - tl['total']):.2f} s)")
    roles = sorted({it["role"] for it in tl["items"] if it.get("role")} | set())
    for r in ROLES:
        buf = np.zeros_like(pcm)
        n = 0
        for it in tl["items"]:
            if it.get("role") != r:
                continue
            a, b = int(it["start"] * SR), min(int(it["end"] * SR), len(pcm))
            if b > a:
                buf[a:b] = pcm[a:b]
                n += 1
        with wave.open(str(sd / f"{r}.wav"), "wb") as wf:
            wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(SR)
            wf.writeframes(buf.tobytes())
        print(f"  {r:3} {n:3} câu")
    (sd / "_PSEUDO.txt").write_text(
        f"STEM GIẢ LẬP tạo {time.strftime('%Y-%m-%d %H:%M:%S')} từ {master.name} theo timeline (make_pseudo_stems.py).\n"
        "Còn lẫn nhạc/SFX trong cửa sổ câu. CHỈ dùng cho sóng badge + cổng H24. KHÔNG dùng cho A14.\n",
        encoding="utf-8")
    print("xong ->", sd)


if __name__ == "__main__":
    main()
