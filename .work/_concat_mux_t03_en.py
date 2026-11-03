#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghep 3 chunk cua EN Tap03 -> picture.mp4, roi mux audio -> thanh pham mp4.

Usage: py -3 .work/_concat_mux_t03_en.py
"""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FFMPEG, FFPROBE = FF / "ffmpeg.exe", FF / "ffprobe.exe"
VD = W / "video3_EN_t03"
FPS = 30

# ---------------------------------------------------------------- 1. kiem tra 3 chunk
parts = []
for k in ("A", "B", "C"):
    p = W / f"video3_EN_t03_c{k}" / f"chunk{k}.mp4"
    if not p.exists():
        raise SystemExit(f"thieu chunk {k}: {p}")
    r = subprocess.run([str(FFPROBE), "-v", "error", "-select_streams", "v:0", "-count_frames",
                        "-show_entries", "stream=nb_read_frames,width,height,r_frame_rate",
                        "-of", "default=nw=1", str(p)],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    info = dict(l.split("=", 1) for l in r.stdout.splitlines() if "=" in l)
    nf = int(info.get("nb_read_frames", 0))
    print(f"chunk {k}: {nf} khung · {info.get('width')}x{info.get('height')} @ {info.get('r_frame_rate')}"
          f" · {p.stat().st_size / 1e6:.1f} MB")
    parts.append((p, nf))

total_frames = sum(n for _, n in parts)
tl = json.loads((W / "timeline_s_EN_t03.json").read_text(encoding="utf-8"))
expect = int(tl["total"] * FPS)
print(f"\nTONG khung: {total_frames} · timeline.total*30 = {expect} · "
      f"{'OK' if total_frames == expect else 'LECH!'}")
if total_frames != expect:
    raise SystemExit("so khung khong khop timeline - dung mux")

# ---------------------------------------------------------------- 2. concat
lst = VD / "chunks.txt"
lst.write_text("".join(f"file '{p.as_posix()}'\n" for p, _ in parts), encoding="utf-8")
pic = VD / "picture.mp4"
print(f"\nghep -> {pic}")
r = subprocess.run([str(FFMPEG), "-y", "-v", "error", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c", "copy", str(pic)],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
if r.returncode != 0:
    print(r.stderr[-1500:])
    raise SystemExit("concat that bai")
print(f"picture.mp4: {pic.stat().st_size / 1e6:.1f} MB")

r = subprocess.run([str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
                    "-of", "default=nw=1:nk=1", str(pic)], capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
d = float(r.stdout.strip())
print(f"picture.mp4 dai {d:.3f} s · timeline.total {tl['total']:.3f} s · "
      f"lech {d - tl['total']:+.3f} s")
if abs(d - tl["total"]) > 0.05:
    raise SystemExit("dai picture.mp4 lech timeline.total qua 0,05 s")

# ---------------------------------------------------------------- 3. mux (package.py --mux)
env = dict(os.environ)
env.update({"AE_EP": "03", "AE_LANG": "en", "PYTHONIOENCODING": "utf-8"})
print("\n=== package.py --mux ===", flush=True)
r = subprocess.run([sys.executable, str(W / "package.py"), "--mux"], env=env, cwd=str(ROOT),
                   text=True, encoding="utf-8", errors="replace",
                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(r.stdout[-3000:])
if r.returncode != 0:
    raise SystemExit("package.py --mux that bai")

mp4 = ROOT / "02_SAN_XUAT" / "Tap03_EN" / "xuat_ban" / "Tap03_EN_master.mp4"
print(f"\nthanh pham: {mp4} ({mp4.stat().st_size / 1e6:.1f} MB)")
