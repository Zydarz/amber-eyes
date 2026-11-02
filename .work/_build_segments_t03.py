#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung picture.mp4 theo SEGMENT de co the RESUME va khong bi gioi han 3600 s.

- Chia 50511 khung thanh 4 segment, moi segment la 1 file mp4 DA finalize.
- Segment da co file -> bo qua (resume).
- Cuoi cung concat bang -c copy ra picture.mp4.
Chay:  py -3 _build_segments_t03.py [so worker]
"""
import os
import subprocess
import sys
import time
from pathlib import Path

W = Path(r"D:\TEST\Gax\amber-eyes\.work")
VD = W / "video3_t03"
BUILD = W / "build_video3.py"
LOG = W / "_build_seg_t03.log"
FPS = 30
NSEG = 4

env = dict(os.environ)
env["AE_EP"] = "03"
env["PYTHONIOENCODING"] = "utf-8"
env["OPENBLAS_NUM_THREADS"] = "1"
env["OMP_NUM_THREADS"] = "1"

WORKERS = sys.argv[1] if len(sys.argv) > 1 else "6"


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


def main():
    VD.mkdir(parents=True, exist_ok=True)
    import json
    tl = json.loads((W / "timeline_s_t03.json").read_text(encoding="utf-8-sig"))
    total_frames = int(tl["total"] * FPS)
    step = (total_frames + NSEG - 1) // NSEG
    bounds = [(min(i * step, total_frames), min((i + 1) * step, total_frames)) for i in range(NSEG)]
    bounds = [(a, b) for a, b in bounds if b > a]
    log(f"tong {total_frames} khung · {len(bounds)} segment · {WORKERS} worker")
    for i, (a, b) in enumerate(bounds):
        log(f"  seg{i}: khung {a}..{b}  ({b - a} khung, {(b - a) / FPS:.1f} s)")

    for i, (a, b) in enumerate(bounds):
        out = VD / f"seg_{i:02d}.mp4"
        if out.exists() and out.stat().st_size > 100000:
            log(f"seg{i} DA CO -> bo qua")
            continue
        t0 = time.time()
        log(f"seg{i}: bat dau render {a}..{b}")
        r = subprocess.run([sys.executable, str(BUILD), "--from", str(a / FPS), "--to", str(b / FPS),
                            "--workers", WORKERS, "--out", str(out)],
                           env=env, cwd=str(W.parent),
                           stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                           text=True, encoding="utf-8", errors="replace")
        if r.returncode != 0:
            log(f"seg{i}: LOI rc={r.returncode}\n{(r.stdout or '')[-1500:]}")
            sys.exit(1)
        log(f"seg{i}: xong trong {time.time() - t0:.0f}s -> {out.name} ({out.stat().st_size / 1e6:.0f} MB)")

    # concat
    lst = VD / "segs.txt"
    lst.write_text("".join(f"file '{VD / f'seg_{i:02d}.mp4'}'\n" for i in range(len(bounds))), encoding="utf-8")
    ff = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
    pic = VD / "picture.mp4"
    log("concat -> picture.mp4")
    r = subprocess.run([str(ff), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c", "copy", str(pic)], env=env, cwd=str(W.parent),
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                       text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        log(f"concat LOI:\n{(r.stdout or '')[-1500:]}")
        sys.exit(1)
    log(f"DONE picture.mp4 ({pic.stat().st_size / 1e6:.0f} MB)")


if __name__ == "__main__":
    main()
