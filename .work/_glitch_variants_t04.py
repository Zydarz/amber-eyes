"""Bien thich: biet loi no full-scale (869,496 s) do ai gay ra.

Moi bien thich encode TOAN BO WAV master -> AAC -> do:
  - true peak (ebur128)
  - mau tai 869,496 s
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
TMP = ROOT / ".work" / "_peak_lab"
TMP.mkdir(exist_ok=True)
IDX = 41735802

VARIANTS = [
    ("1. AAC thuan (khong filter)", ["-c:a", "aac", "-b:a", "192k"]),
    ("2. + alimiter -2.0 a5 (hien tai)", ["-af", "alimiter=limit=0.7943:attack=5:release=50:level=disabled",
                                          "-c:a", "aac", "-b:a", "192k"]),
    ("3. AAC thuan, aac_coder=fast", ["-c:a", "aac", "-aac_coder", "fast", "-b:a", "192k"]),
    ("4. AAC thuan, 256k", ["-c:a", "aac", "-b:a", "256k"]),
    ("5. AAC thuan + volume=-1dB truoc encode", ["-af", "volume=-1dB", "-c:a", "aac", "-b:a", "192k"]),
]

for label, extra in VARIANTS:
    out = TMP / ("v_%d.m4a" % abs(hash(label)))
    r = subprocess.run([str(FF), "-y", "-v", "error", "-i", str(WAV), *extra, str(out)],
                       capture_output=True, text=True)
    if r.returncode:
        print("%-42s LOI: %s" % (label, r.stderr[:160]))
        continue
    r2 = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(out), "-af", "ebur128=peak=true",
                         "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    lu = re.findall(r"I:\s*(-?[\d.]+) LUFS", r2.stderr)
    pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", r2.stderr)
    w = TMP / ("v_%d.wav" % abs(hash(label)))
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(out), "-c:a", "pcm_s16le", "-ar", "48000",
                    "-ac", "2", str(w)], check=True)
    b, _ = sf.read(str(w), dtype="int16", always_2d=True)
    a, _ = sf.read(str(WAV), dtype="int16", always_2d=True)
    mx = int(np.abs(b.astype(np.int32)).max())
    g = "CO LOI" if mx > 28000 else "sach"
    print("%-42s LUFS %6s | truePeak %6s | |mau| max %6d | mau 869,496s = %6d/%6d (WAV %6d/%6d) => %s" % (
        label, lu[-1] if lu else "?", pk[-1] if pk else "?", mx,
        b[IDX][0], b[IDX][1], a[IDX][0], a[IDX][1], g))
    out.unlink()
    w.unlink()
