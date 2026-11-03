"""Bench song song: render() co hay khong di qua pipe -> tim nut thot that.

Che do:
  pure : chi render(), bo qua frame (khong ghi ra gi) -> do chi phi render thuan
  pipe : render() + ghi 6.2 MB/frame vao stdin cua ffmpeg (nhu build that)
  fast : giong 'pipe' nhung finishing() duoc toi uu (bit-identical, kiem chung rieng)

Chay 6 tien trinh song song de do AGGREGATE throughput.
"""
import argparse
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import numpy as np  # noqa: E402

import build_video3 as B  # noqa: E402

FF = B.FF


def make_fast_finishing():
    """finishing() toi uu: cast float32 ro + vignette pre-expand (H,W,3).
    Ket qua phai BIT-IDENTICAL voi finishing() goc (kiem bang _bench_fast_check.py).
    """
    ORIG = B.finishing
    V3 = {"v": None}

    def finishing_fast(arr, fi):
        if V3["v"] is None:
            ORIG(arr, fi)                 # khoi tao VIGNETTE/GRAIN/ABUF
            V3["v"] = np.repeat(B.VIGNETTE, 3, axis=2).copy()
        a = arr.astype(np.float32)
        np.multiply(a, V3["v"], out=a)
        np.add(a, B.GRAIN[fi % 6], out=a)
        red = a[:, :, 0].copy()
        a[:, 1:, 0] = red[:, :-1]
        np.clip(a, 0, 255, out=a)
        return a.astype(np.uint8)

    return finishing_fast


def big_pipe_popen(cmd, bufsize, **kw):
    """Popen voi pipe buffer lon.

    Khong the tao pipe roi tra ve (se lam p2cwrite = -1 => ffmpeg khong nhan
    handle lam stdin). Thay vao do patch _winapi.CreatePipe: subprocess tu tao
    ca hai dau, chi can buffer lon hon mac dinh 4 KB cua Windows.
    """
    import _winapi

    _real = _winapi.CreatePipe

    def _create(readable, writable):
        if readable is None and not writable:
            return _real(None, bufsize)
        return _real(readable, writable)

    _winapi.CreatePipe = _create
    try:
        return subprocess.Popen(cmd, **kw)
    finally:
        _winapi.CreatePipe = _real


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["pure", "pipe", "fast", "pipebig"], default="pure")
    ap.add_argument("--n", type=int, default=350)
    ap.add_argument("--t0", type=float, default=100.0)
    ap.add_argument("--out", default="")
    a = ap.parse_args()

    if a.mode == "fast":
        B.finishing = make_fast_finishing()

    f0 = int(a.t0 * B.FPS)
    idxs = list(range(f0, f0 + a.n))

    p = None
    if a.mode in ("pipe", "fast", "pipebig"):
        cmd = [str(FF), "-y", "-hide_banner", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24",
               "-s", f"{B.W}x{B.H}", "-r", str(B.FPS), "-i", "-", "-c:v", "libopenh264", "-b:v", "3000k",
               "-maxrate", "5000k", "-bufsize", "8000k", "-pix_fmt", "yuv420p", "-r", str(B.FPS), a.out]
        if a.mode == "pipebig":
            p = big_pipe_popen(cmd, int(os.environ.get("AE_PIPE_BUF", 4 * 1024 * 1024)),
                               stdin=subprocess.PIPE)
        else:
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE)

    t0 = time.perf_counter()
    for fi in idxs:
        data = B.render(fi).convert("RGB").tobytes()
        if p is not None:
            p.stdin.write(data)
    if p is not None:
        p.stdin.close()
        p.wait()
    dt = time.perf_counter() - t0
    print(f"{os.getpid()} mode={a.mode} n={a.n} dt={dt:.1f}s fps={a.n / dt:.2f}", flush=True)


if __name__ == "__main__":
    main()
