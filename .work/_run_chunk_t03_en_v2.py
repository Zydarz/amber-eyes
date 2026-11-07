#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render MOT CHUNK cua video EN Tap03 (A11 #103: chia theo FRAME de khong vuot
gioi han gio cu task; moi chunk tao ra 1 file mp4 co moov => bi huy cung khong mat chunk truoc).

Usage:  py -3 .work/_run_chunk_t03_en.py <A|B|C>

Khung hinh (30 fps, tong 49464):
  A: 0     -> 16469   (t 0     -> 549.0)
  B: 16470 -> 32939   (t 549.0 -> 1098.0)
  C: 32940 -> 49397   (t 1098.0-> 1648.80)
Moi moc t deu la boi so 30 chinh xac => int(t*30) ra dung khung hinh.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FPS = 30

CHUNKS = {
    "A": (0.0, 549.0, 0, 16470),
    "B": (549.0, 1098.0, 16470, 16470),
    "C": (1098.0, 1648.80, 32940, 16524),
}

which = sys.argv[1].strip().upper()
if which not in CHUNKS:
    raise SystemExit(f"chunk phai la A/B/C, nhan {which}")
t0, t1, expect0, expect_n = CHUNKS[which]
VD = W / f"video3_EN_t03_c{which}"
VD.mkdir(parents=True, exist_ok=True)
out = VD / f"chunk{which}.mp4"

env = dict(os.environ)
env.update({
    "AE_EP": "03", "AE_LANG": "en", "PYTHONIOENCODING": "utf-8",
    "AE_VID": str(VD),
    "AE_PIPE_BUF": str(4 * 1024 * 1024),      # pipe Windows 4 KB -> 4 MB (A11 #100)
    "AE_FAST_FINISH": "1",                    # finishing() toi uu, BIT-IDENTICAL (A11 #102)
})

print(f"=== chunk {which}: t {t0} -> {t1} s · frame {expect0} + {expect_n} = {expect0 + expect_n} ===")
print(f"    AE_VID={VD}\n    out={out}\n", flush=True)

cmd = [sys.executable, str(W / "_build_video3_split.py"),
       "--from", f"{t0:.6f}", "--to", f"{t1:.6f}", "--workers", "6", "--out", str(out)]
print("CMD:", " ".join(cmd), flush=True)

r = subprocess.run(cmd, env=env, cwd=str(ROOT), text=True,
                   encoding="utf-8", errors="replace",
                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(r.stdout[-4000:], flush=True)
if r.returncode != 0:
    raise SystemExit(f"chunk {which} that bai (rc={r.returncode})")

FFP = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
p = subprocess.run([str(FFP), "-v", "error", "-select_streams", "v:0", "-count_frames",
                    "-show_entries", "stream=nb_read_frames,width,height,r_frame_rate",
                    "-of", "default=nw=1", str(out)],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print(p.stdout.strip())
nf = None
for l in p.stdout.splitlines():
    if "nb_read_frames" in l:
        nf = int(l.split("=")[1])
print(f"khung hinh thuc te: {nf} · mong doi {expect_n} · {'OK' if nf == expect_n else 'LECH!'}")
if nf != expect_n:
    raise SystemExit("SO KUNG KHUNG KHONG DUNG - dung render lai chunk nay")
print(f"chunk {which} XONG -> {out} ({out.stat().st_size / 1e6:.1f} MB)")
