"""Khoanh vung loi giai ma AAC (mau no full-scale tai ~869,496 s) + thu tai lap lai."""
import pathlib
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

T = 869.496
sr = 48000
i0 = int(T * sr)

# --- 1. vung la mau ---
dec = TMP / "final_audio.wav"
if not dec.exists():
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(FINAL), "-vn", "-c:a", "pcm_s16le",
                    "-ar", "48000", "-ac", "2", str(dec)], check=True)
b, sb = sf.read(str(dec), dtype="int16", always_2d=True)
a, sa = sf.read(str(WAV), dtype="int16", always_2d=True)
print("nguon WAV frames=%d | mp4 frames=%d" % (len(a), len(b)))
for off in range(-6, 7):
    i = i0 + off
    if 0 <= i < min(len(a), len(b)):
        print("  i=%d t=%.6f | WAV L/R = %6d / %6d | mp4 L/R = %6d / %6d" % (
            i, i / sr, a[i][0], a[i][1], b[i][0], b[i][1]))

# dem bao nhieu mau "no" (|mp4| > |WAV| + 8000) trong ca file
n = min(len(a), len(b))
d = np.abs(b[:n].astype(np.int32)) - np.abs(a[:n].astype(np.int32))
bad = np.where(d.max(axis=1) > 8000)[0]
print("\nso mau 'no' (|mp4| - |WAV| > 8000):", len(bad))
if len(bad):
    print("vi tri (s):", ["%.4f" % (x / sr) for x in bad[:20]])
    print("|WAV| tai do:", [int(np.abs(a[x]).max()) for x in bad[:10]])
    print("|mp4| tai do:", [int(np.abs(b[x]).max()) for x in bad[:10]])

# --- 2. co tai lap khong: encode lai dung vung do voi chuoi filter cua mux ---
print("\n--- encode lai vung 860-880 s voi chuoi filter cua package.py ---")
for label, extra in (("khong filter", []),
                     ("alimiter -2.0 attack 5", ["-af", "alimiter=limit=0.7943:attack=5:release=50:level=disabled"])):
    out = TMP / ("re_%s.m4a" % abs(hash(label)))
    r = subprocess.run([str(FF), "-y", "-v", "error", "-ss", "860", "-t", "20", "-i", str(WAV),
                        *extra, "-c:a", "aac", "-b:a", "192k", str(out)], capture_output=True, text=True)
    if r.returncode:
        print("  %s: LOI %s" % (label, r.stderr[:150]))
        continue
    w = TMP / ("re_%s.wav" % abs(hash(label)))
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(out), "-c:a", "pcm_s16le", "-ar", "48000",
                    "-ac", "2", str(w)], check=True)
    x, _ = sf.read(str(w), dtype="int16", always_2d=True)
    print("  %-24s |mau| max = %6d | so mau > 32000: %d" % (
        label, int(np.abs(x.astype(np.int32)).max()), int((np.abs(x.astype(np.int32)).max(axis=1) > 32000).sum())))
    out.unlink()
    w.unlink()
