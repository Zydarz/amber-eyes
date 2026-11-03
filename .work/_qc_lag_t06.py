"""Do lag A/V cua Tap06_master.mp4 so voi audio master (mp3) — BAN FFT.

Cach do: trich cung mot doan audio tu track trong mp4 va tu file audio nguon,
roi tim lech toi da bang TUONG QUAN CHEO qua FFT (O(n log n)).
|lag| ~ 0 => khop hinh anh / loi thoai.

LUU Y: dung np.correlate(mode='full') se O(n^2) -> 480.000 mau = 2,3e11 phep,
chay hang gio. Dung FFT (np.fft) hoac scipy.signal.correlate(method='fft').
"""
import os
import subprocess
import sys
import wave
from pathlib import Path

os.environ.setdefault("AE_EP", "06")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

import numpy as np  # noqa: E402

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
OUT = ROOT / "02_SAN_XUAT" / "Tap06" / "xuat_ban"
MASTER = OUT / "Tap06_master.mp4"
MP3 = OUT / "Tap06_master.mp3"
TMP = WORK / "_qc_lag_t06"
TMP.mkdir(parents=True, exist_ok=True)

SR = 16000
T0 = 120.0
DUR = 30.0
TOL_MS = 40.0


def extract(src, dst):
    cmd = [str(FF), "-y", "-v", "error", "-ss", f"{T0}", "-t", f"{DUR}",
           "-i", str(src), "-vn", "-ac", "1", "-ar", str(SR), "-f", "wav", str(dst)]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        raise SystemExit(f"extract that bai {src}: {r.stderr.strip()}")


def read_wav(p):
    import array
    with wave.open(str(p), "rb") as wf:
        n = wf.getnframes()
        raw = wf.readframes(n)
    a = array.array("h")
    a.frombytes(raw)
    return a


def xcorr_fft(x, y):
    """Tra ve (lags, values) cho tuong quan cheo chuan hoa.
    Chu thuoc FFT: c[m] = sum_n x[n] * y[n - m]  =>  dinh tai m = do tre cua x so voi y.
    Quy uoc: lag > 0 => x (am thanh trong video) TRE hon y (am thanh nguon).
    """
    n = len(x) + len(y)
    N = 1 << (n - 1).bit_length()
    X = np.fft.rfft(x, N)
    Y = np.fft.rfft(y, N)
    c = np.fft.irfft(X * np.conj(Y), N)
    # linear lag: m < len(x) -> lag = m ; m >= len(x) -> lag = m - N (vong qua 0)
    lags = np.concatenate([np.arange(len(x)), np.arange(len(x), N) - N])
    return lags, c


def measure(x, y, label):
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    x -= x.mean()
    y -= y.mean()
    nx, ny = np.linalg.norm(x), np.linalg.norm(y)
    if nx == 0 or ny == 0:
        raise SystemExit("CHẶN - doan audio im")
    lags, c = xcorr_fft(x, y)
    m = SR  # +/- 1 s
    sel = (lags >= -m) & (lags <= m)
    l = lags[sel]
    v = c[sel] / (nx * ny)
    k = int(np.argmax(v))
    lag_ms = float(l[k]) / SR * 1000.0
    print(f"  {label}: lag {lag_ms:+.1f} ms | r = {float(v[k]):.4f}")
    return lag_ms, float(v[k])


def self_test():
    """Kiem thuat: x = y chuyen doc 7 mau => lag phai = +7 mau (x tre hon y)."""
    rs = np.random.default_rng(7)
    y = rs.normal(0, 1, 8000)
    x = np.concatenate([np.zeros(7), y[:-7]])   # x tre hon y 7 mau
    lag, r = measure(x, y, "self-test")
    print(f"  (kỳ vọng lag = +{7 * 1000 / SR:.1f} ms | r ≈ 1)")
    if abs(lag - 7 * 1000 / SR) > 2.0 or r < 0.9:
        raise SystemExit("CHẶN - thuật toán đo lag SAI dấu")
    # truong hop am thanh SOM PHAN: x = y chuyen trai 7 mau => lag = -7 mau
    x2 = np.concatenate([y[7:], np.zeros(7)])
    lag2, r2 = measure(x2, y, "self-test (ngược dấu)")
    if abs(lag2 + 7 * 1000 / SR) > 2.0 or r2 < 0.9:
        raise SystemExit("CHẶN - thuật toán đo lag SAI ở chiều âm")
    print("  OK  thuật toán đo lag đúng dấu (cả hai chiều)")


def main():
    self_test()
    print()
    for p in (MASTER, MP3):
        if not p.exists():
            raise SystemExit(f"CHẶN - thieu {p}")

    a = TMP / "final_seg.wav"
    b = TMP / "master_seg.wav"
    extract(MASTER, a)
    extract(MP3, b)

    x = read_wav(a)      # tu video (mp4)
    y = read_wav(b)      # tu audio nguon (mp3)
    n = min(len(x), len(y))
    if n < SR * 5:
        raise SystemExit("CHẶN - doan audio qua ngan")
    print(f"  doan mau: t={T0:.0f}s, {DUR:.0f}s, {SR} Hz mono, {n} mau")
    lag_ms, r = measure(x[:n], y[:n], "video vs mp3")

    ok = abs(lag_ms) <= TOL_MS and r > 0.5
    print(f"  => {'ĐẠT' if ok else 'KHÔNG ĐẠT'} (nguong |lag| <= {TOL_MS:.0f} ms, r > 0,5)")
    if not ok:
        raise SystemExit("CHẶN - lag A/V ngoai nguong")
    print("OK  lag A/V trong nguong")


if __name__ == "__main__":
    main()
