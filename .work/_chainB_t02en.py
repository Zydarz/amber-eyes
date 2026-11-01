#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chai B: cho render nua A xong -> render nua B -> ghep picture.mp4.

Render toan bo can ~73 phut > gioi han 3600 s cua 1 task nen tach 2 nua
(dung --from/--to de cat chinh xac theo khung 30 fps).
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
VD = W / "video3_EN_t02"
PIC_A = VD / "pic_a.mp4"
PIC_B = VD / "pic_b.mp4"
PIC = VD / "picture.mp4"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
os.environ["AE_LANG"] = "en"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
PY = sys.executable

TL = json.loads((W / "timeline_s_EN_t02.json").read_text(encoding="utf-8-sig"))
TOTAL = TL["total"]
MID = 696.4                      # int(696.4*30) = 20892 -> cat bang khung
N_FRAMES = int(TOTAL * 30)


def log(p):
    print(p, flush=True)


def wait_file(p, label, limit=3600):
    t0 = time.time()
    last = -1
    while True:
        if p.exists() and p.stat().st_size > 1_000_000:
            sz = p.stat().st_size
            time.sleep(20)
            if p.exists() and p.stat().st_size == sz:
                log("[B] %s xong (%d byte)" % (label, sz))
                return
        if time.time() - t0 > limit:
            log("[B] TIMEOUT cho %s" % label)
            raise SystemExit(2)
        time.sleep(15)


log("[B] cho pic_a.mp4 ...")
wait_file(PIC_A, "nua A")

log("[B] render nua B: --from %s --to %s" % (MID, TOTAL))
t = time.time()
r = subprocess.run([PY, str(W / "build_video3.py"), "--from", str(MID), "--to", str(TOTAL),
                    "--workers", "6", "--out", str(PIC_B)], cwd=ROOT,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
log((r.stdout or "")[-1500:])
log((r.stderr or "")[-1500:])
log("[B] nua B exit=%d · %.0f s" % (r.returncode, time.time() - t))
if r.returncode != 0:
    raise SystemExit(3)

log("[B] ghep pic_a + pic_b -> picture.mp4")
lst = VD / "parts_final.txt"
lst.write_text("file '%s'\nfile '%s'\n" % (PIC_A.as_posix(), PIC_B.as_posix()), encoding="utf-8")
r = subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                    "-c", "copy", str(PIC)], capture_output=True, text=True, errors="replace")
log("[B] ghep exit=%d %s" % (r.returncode, (r.stderr or "")[-400:]))
if r.returncode != 0:
    raise SystemExit(4)

r = subprocess.run([str(FF.with_name("ffprobe.exe")), "-v", "error", "-count_frames",
                    "-select_streams", "v:0", "-show_entries",
                    "stream=nb_read_frames,duration,r_frame_rate,width,height",
                    "-of", "default=noprint_wrappers=1", str(PIC)],
                   capture_output=True, text=True, errors="replace")
log("[B] picture.mp4: %s" % r.stdout.replace("\n", " "))
log("[B] khung mong doi = %d" % N_FRAMES)
log("[B] XONG")
