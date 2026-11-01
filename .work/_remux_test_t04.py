"""Tai lap dung lenh mux cua package.py -> file tam, do true peak + so mau tai 869,496 s."""
import pathlib
import re
import subprocess
import sys

import numpy as np
import soundfile as sf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
PICT = ROOT / ".work" / "video3_t04" / "picture.mp4"
WAV = ROOT / ".work" / "audio_master_t04.wav"
TMP = ROOT / ".work" / "_peak_lab"
TMP.mkdir(exist_ok=True)
OUT = TMP / "remux_test.mp4"

cmd = [str(FF), "-y", "-v", "error", "-i", str(PICT), "-i", str(WAV), "-map", "0:v", "-map", "1:a",
       "-c:v", "copy", "-af", "alimiter=limit=0.7943:attack=5:release=50:level=disabled",
       "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(OUT)]
print("$", " ".join(cmd))
r = subprocess.run(cmd, capture_output=True, text=True)
print("rc =", r.returncode, r.stderr[:200])

r2 = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(OUT), "-af", "ebur128=peak=true",
                     "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
lufs = re.findall(r"I:\s*(-?[\d.]+) LUFS", r2.stderr)
pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", r2.stderr)
print("remux -> LUFS %s | true peak %s dBFS" % (lufs[-1] if lufs else "?", pk[-1] if pk else "?"))

w = TMP / "remux_audio.wav"
subprocess.run([str(FF), "-y", "-v", "error", "-i", str(OUT), "-vn", "-c:a", "pcm_s16le",
                "-ar", "48000", "-ac", "2", str(w)], check=True)
b, _ = sf.read(str(w), dtype="int16", always_2d=True)
a, _ = sf.read(str(WAV), dtype="int16", always_2d=True)
i0 = int(869.496 * 48000)
print("\nmau tai 869,496 s (remux moi):")
for off in range(-2, 3):
    i = i0 + off
    print("  t=%.6f | WAV %6d/%6d | remux %6d/%6d" % (i / 48000, a[i][0], a[i][1], b[i][0], b[i][1]))
print("|remux| max toan file: %d" % int(np.abs(b.astype(np.int32)).max()))
