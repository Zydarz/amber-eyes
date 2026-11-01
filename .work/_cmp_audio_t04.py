"""So mau am thanh giua WAV master va mp4 cuoi de dinh vi chenh lech (gia nghi giai ma AAC).

- doc WAV master (int16 stereo 48k) va audio cua mp4 cuoi (giai ma cung format)
- so tung mau theo khung 100 ms, tim khung lech lon nhat
- in vi tri + gia tri tai do
"""
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
TMP = ROOT / ".work" / "_cmp_audio"
TMP.mkdir(exist_ok=True)

info = sf.info(str(WAV))
print("WAV master:", info.samplerate, "Hz", info.channels, "kenh", info.subtype, "| khung:", info.frames)

dec = TMP / "final_audio.wav"
r = subprocess.run([str(FF), "-y", "-v", "error", "-i", str(FINAL), "-vn", "-c:a", "pcm_s16le",
                    "-ar", "48000", "-ac", "2", str(dec)], capture_output=True, text=True)
print("giai ma mp4 -> wav:", r.returncode, r.stderr[:200])
info2 = sf.info(str(dec))
print("audio tu mp4 cuoi:", info2.samplerate, "Hz", info2.channels, "kenh", info2.subtype, "| khung:", info2.frames)

a, sa = sf.read(str(WAV), dtype="int16", always_2d=True)
b, sb = sf.read(str(dec), dtype="int16", always_2d=True)
n = min(len(a), len(b))
print("do dai so sanh:", n, "khung =", n / sa, "s")
a, b = a[:n], b[:n]
diff = np.abs(a.astype(np.int32) - b.astype(np.int32)).max(axis=1)

win = int(0.1 * sa)
m = n // win
dmax = diff[: m * win].reshape(m, win).max(axis=1)
amax = np.abs(a[: m * win].astype(np.int32)).reshape(m, win, -1).max(axis=(1, 2))
bmax = np.abs(b[: m * win].astype(np.int32)).reshape(m, win, -1).max(axis=(1, 2))

order = np.argsort(dmax)[::-1][:12]
print("\n12 khung 100 ms lech nhieu nhat (t, lech mau, |WAV|, |mp4|):")
for i in sorted(order):
    print("  t=%8.1f s | lech=%6d | WAV=%6d | mp4=%6d" % (i * 0.1, dmax[i], amax[i], bmax[i]))

j = int(np.argmax(np.abs(b.astype(np.int32)).max(axis=1)))
print("\nmau lon nhat trong mp4: %d (t=%.3f s) | WAV cung vi tri: %d" % (
    b[j].max() if b[j].max() > 0 else b[j].min(), j / sb, a[j].max() if a[j].max() > 0 else a[j].min()))
k = int(np.argmax(np.abs(a.astype(np.int32)).max(axis=1)))
print("mau lon nhat trong WAV: %d (t=%.3f s)" % (
    a[k].max() if a[k].max() > 0 else a[k].min(), k / sa))
print("|WAV| max = %d | |mp4| max = %d" % (np.abs(a.astype(np.int32)).max(), np.abs(b.astype(np.int32)).max()))
