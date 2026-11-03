#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fallback: neu luot render bi HUY vi gioi han gio cu task, render phan DUOI
cua tung part roi ghép lai.

Cach dung (chay khi luot chinh da bi huy):
    py -3 .work/_render_tail_t03_en.py

Tinh:
  - part_k phu frame [k*PER, (k+1)*PER) voi PER = TOTAL_FRAMES // 6
  - dem frame thuc te cua tung part bang ffprobe
  - render phan thieu vao thu muc rieng (.work/video3_EN_t03_tail/tail_k.mp4)
  - ghep: part_00, tail_00, part_01, tail_01, ... bang ffmpeg concat -c copy
"""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
VD = W / "video3_EN_t03"
TAIL = W / "video3_EN_t03_tail"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FFMPEG = FF / "ffmpeg.exe"
FFPROBE = FF / "ffprobe.exe"
FPS = 30
WORKERS = 6

env = dict(os.environ)
env.update({"AE_EP": "03", "AE_LANG": "en", "PYTHONIOENCODING": "utf-8"})

total = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["total"]
TOTAL_FRAMES = int(total * FPS)
PER = TOTAL_FRAMES // WORKERS
print(f"total={total:.3f}s · TOTAL_FRAMES={TOTAL_FRAMES} · PER={PER} (×{WORKERS}={PER*WORKERS})")


def nframes(p: Path) -> int:
    r = subprocess.run([str(FFPROBE), "-v", "error", "-select_streams", "v:0", "-count_frames",
                        "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    try:
        return int(r.stdout.strip().split(",")[0])
    except Exception:
        return 0


plan = []
for k in range(WORKERS):
    part = VD / f"part_{k:02d}.mp4"
    if not part.exists():
        print(f"part_{k:02d}: THIEU")
        continue
    have = nframes(part)
    want = PER if k < WORKERS - 1 else TOTAL_FRAMES - PER * (WORKERS - 1)
    start = k * PER
    print(f"part_{k:02d}: co {have} frame, can {want} (frame {start}..{start+want-1})")
    if have < want:
        plan.append((k, start, start + have, start + want))

if not plan:
    print("KHONG THIEU frame nao — khong can render tail")
    sys.exit(0)

TAIL.mkdir(parents=True, exist_ok=True)
for k, f0, f1 in plan:
    print(f"\n=== render tail part_{k:02d}: frame {f0}..{f1-1} ===")
    t0, t1 = f0 / FPS, f1 / FPS
    r = subprocess.run([sys.executable, str(W / "_build_video3_split.py"),
                        "--from", f"{t0:.6f}", "--to", f"{t1:.6f}", "--workers", "4",
                        "--out", str(TAIL / f"tail_{k:02d}.mp4")],
                       env={**env, "AE_VID": str(TAIL), "AE_PIPE_BUF": str(4 * 1024 * 1024)},
                       cwd=str(ROOT), capture_output=True, text=True, encoding="utf-8", errors="replace")
    print(r.stdout[-1500:])
    if r.returncode != 0:
        print("STDERR:", r.stderr[-800:])
        raise SystemExit(f"tail part_{k:02d} that bai")

# ---- ghep
lst = TAIL / "concat.txt"
entries = []
for k in range(WORKERS):
    p = VD / f"part_{k:02d}.mp4"
    if p.exists():
        entries.append(p)
    t = TAIL / f"tail_{k:02d}.mp4"
    if t.exists():
        entries.append(t)
lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in entries), encoding="utf-8")
out = VD / "picture.mp4"
print(f"\nghep {len(entries)} phan -> {out}")
r = subprocess.run([str(FFMPEG), "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c", "copy", str(out)],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print(r.stderr[-600:])
if r.returncode != 0:
    raise SystemExit("ghep that bai")
print("xong")
