"""Kiem chung file cuoi MOI sau khi va limiter (latency=1):
   - true peak tren chinh mp4 (A7)
   - mau tai 869,496 s co bang mau WAV master khong
   - do lech (lag) audio mp4 so voi WAV master = 0?
   - |mau| max toan file
"""
import pathlib
import re
import subprocess
import sys

import numpy as np
import soundfile as sf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
WAV = ROOT / ".work" / "audio_master_t04.wav"
FINAL = ROOT / "02_SAN_XUAT" / "Tap04" / "xuat_ban" / "Tap04_master.mp4"
TMP = ROOT / ".work" / "_peak_lab"
TMP.mkdir(exist_ok=True)

r = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(FINAL), "-af", "ebur128=peak=true",
                    "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
lu = re.findall(r"I:\s*(-?[\d.]+) LUFS", r.stderr)
pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", r.stderr)
print("FILE CUOI MOI: LUFS %s | true peak %s dBFS | A7 (<= -1,5) => %s" % (
    lu[-1] if lu else "?", pk[-1] if pk else "?", "DAT" if pk and float(pk[-1]) <= -1.5 else "VUOT"))

dec = TMP / "final_audio_v2.wav"
subprocess.run([str(FF), "-y", "-v", "error", "-i", str(FINAL), "-vn", "-c:a", "pcm_s16le",
                "-ar", "48000", "-ac", "2", str(dec)], check=True)
b, sr = sf.read(str(dec), dtype="float32", always_2d=True)
a, _ = sf.read(str(WAV), dtype="float32", always_2d=True)
print("|mau| max mp4 = %d | WAV = %d" % (
    int(np.abs(b).max() * 32768), int(np.abs(a).max() * 32768)))

i0 = int(869.496 * sr)
print("\nmau tai 869,496 s:")
for off in range(-3, 4):
    i = i0 + off
    print("  t=%.6f | WAV %7d/%7d | mp4 %7d/%7d" % (
        i / sr, int(a[i][0] * 32768), int(a[i][1] * 32768), int(b[i][0] * 32768), int(b[i][1] * 32768)))

print("\ndo lech (lag) mp4 so voi WAV:")
for t0 in (300.0, 600.0, 869.3, 1000.0):
    i0b = int(t0 * sr)
    N = 48000
    x = a[i0b:i0b + N, 0] - a[i0b:i0b + N, 0].mean()
    y = b[i0b - 2000:i0b + N + 2000, 0] - b[i0b - 2000:i0b + N + 2000, 0].mean()
    c = np.correlate(y, x, mode="valid")
    lag = int(np.argmax(c)) - 2000
    print("  t=%7.1f s -> lag %+d mau (%.2f ms)" % (t0, lag, 1000 * lag / sr))
