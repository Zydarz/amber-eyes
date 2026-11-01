"""Do độ lệch thời gian (lag) giữa WAV master và audio giải mã từ mp4 cuối.

Nếu alimiter (latency=false) chèn trễ, mp4 sẽ lệch WAV vài chục mẫu ⇒ âm thanh lệch hình.
"""
import pathlib
import sys

import numpy as np
import soundfile as sf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
WAV = ROOT / ".work" / "audio_master_t04.wav"
DEC = ROOT / ".work" / "_cmp_audio" / "final_audio.wav"

a, sr = sf.read(str(WAV), dtype="float32", always_2d=True)
b, _ = sf.read(str(DEC), dtype="float32", always_2d=True)
print("WAV %d khung | mp4 %d khung | sr %d" % (len(a), len(b), sr))

for t0 in (300.0, 600.0, 1000.0, 1100.0):
    i0 = int(t0 * sr)
    N = 48000                      # 1 s
    x = a[i0:i0 + N, 0]
    y = b[i0 - 2000:i0 + N + 2000, 0]
    y = y - y.mean()
    x = x - x.mean()
    c = np.correlate(y, x, mode="valid")
    lag = int(np.argmax(c)) - 2000
    print("  t=%7.1f s -> lag mp4 so voi WAV = %+d mau (%.2f ms)" % (t0, lag, 1000 * lag / sr))

# lag o vung "yen tinh" ngay truoc loi (869,45 s)
for t0 in (868.0, 869.0, 869.4, 870.0):
    i0 = int(t0 * sr)
    N = 24000
    x = a[i0:i0 + N, 0]
    y = b[i0 - 2000:i0 + N + 2000, 0]
    y = y - y.mean()
    x = x - x.mean()
    c = np.correlate(y, x, mode="valid")
    lag = int(np.argmax(c)) - 2000
    print("  vung loi t=%7.2f s -> lag = %+d mau (%.2f ms) | corr max %.3f" % (
        t0, lag, 1000 * lag / sr, c.max() / (np.linalg.norm(x) * np.linalg.norm(c) / np.sqrt(len(c)) + 1e-9)))
