#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap04 VN — tạo .work/audio_master_EN_t04.wav từ master mp3 (nguồn audio duy nhất).

package.py mux đọc ED.w("audio_master.wav") = .work/audio_master_EN_t04.wav.
File đó bị xoá khi dọn đĩa nên phải dựng lại TỪ master mp3 (giữ đúng nội dung
người dùng đã duyệt). Giữ nguyên 48 kHz stereo (mẫu gốc của mp3) để không
lệch nhịp. Cắt đúng timeline.total để -shortest khớp picture.mp4.
"""
import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
FP = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffprobe.exe"
MP3 = ROOT / "02_SAN_XUAT/Tap04_EN/xuat_ban/Tap04_EN_master.mp3"
WAV = WORK / "audio_master_EN_t04.wav"

tl = json.loads((WORK / "timeline_s_EN_t04.json").read_text(encoding="utf-8"))
total = float(tl["total"])


def dur(p):
    o = subprocess.run([str(FP), "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", str(p)],
                       capture_output=True, text=True).stdout.strip()
    return float(o)


d_mp3 = dur(MP3)
print(f"timeline.total = {total:.3f}s | master mp3 = {d_mp3:.3f}s | lech = {d_mp3 - total:+.3f}s")
if abs(d_mp3 - total) > 0.05:
    raise SystemExit("ABORT: master mp3 lech timeline.total qua 0,05 s -> phai dung lai timeline")

print("decoding mp3 -> wav (48 kHz stereo, cat dung timeline.total)...")
subprocess.run([str(FF), "-y", "-v", "error", "-i", str(MP3),
                "-t", f"{total:.3f}", "-ar", "48000", "-ac", "2",
                "-c:a", "pcm_s16le", str(WAV)], check=True)
d_wav = dur(WAV)
print(f"audio_master_EN_t04.wav = {d_wav:.3f}s  ({WAV.stat().st_size/1e6:.1f} MB)")
if abs(d_wav - total) > 0.05:
    raise SystemExit(f"ABORT: wav lech {d_wav - total:+.3f}s")

# do LUFS + true peak tren chinh wav
e = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(WAV),
                    "-af", "ebur128=peak=true", "-f", "null", "-"],
                   capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
import re
i = e.rfind("Integrated loudness:")
seg = e[i:i + 2200]
I = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", seg)
LRA = re.findall(r"LRA:\s*(-?[\d.]+)\s*LU", seg)
PK = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", seg)
print(f"  LUFS={I[-1] if I else '?'}  LRA={LRA[-1] if LRA else '?'}  true peak={PK[-1] if PK else '?'} dBFS")
print("OK")
