"""Khoanh vung loi cua bo loc alimiter (bien thich 2 gay loi).

Bien thich: encode TOAN BO WAV master voi tung cau hinh alimiter -> do true peak + mau tai 869,496 s.
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
    ("a. limit=1 (KHONG gioi han) a5", ["-af", "alimiter=limit=1:attack=5:release=50:level=disabled"]),
    ("b. limit=-2.0 a5 + latency=1", ["-af", "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1"]),
    ("c. limit=-2.0 attack=1", ["-af", "alimiter=limit=0.7943:attack=1:release=50:level=disabled"]),
    ("d. limit=-2.0 attack=20 release=200", ["-af", "alimiter=limit=0.7943:attack=20:release=200:level=disabled"]),
]

for label, extra in VARIANTS:
    out = TMP / ("w_%d.m4a" % abs(hash(label)))
    r = subprocess.run([str(FF), "-y", "-v", "error", "-i", str(WAV), *extra, "-c:a", "aac",
                        "-b:a", "192k", str(out)], capture_output=True, text=True)
    if r.returncode:
        print("%-40s LOI: %s" % (label, r.stderr[:160]))
        continue
    r2 = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(out), "-af", "ebur128=peak=true",
                         "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    lu = re.findall(r"I:\s*(-?[\d.]+) LUFS", r2.stderr)
    pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", r2.stderr)
    w = TMP / ("w_%d.wav" % abs(hash(label)))
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(out), "-c:a", "pcm_s16le", "-ar", "48000",
                    "-ac", "2", str(w)], check=True)
    b, _ = sf.read(str(w), dtype="int16", always_2d=True)
    mx = int(np.abs(b.astype(np.int32)).max())
    print("%-40s LUFS %6s | truePeak %6s | |mau| max %6d | 869,496s = %6d/%6d => %s" % (
        label, lu[-1] if lu else "?", pk[-1] if pk else "?", mx, b[IDX][0], b[IDX][1],
        "CO LOI" if mx > 28000 else "sach"))
    out.unlink()
    w.unlink()
