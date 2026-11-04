#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghep 4 chunk render + mux Tap05 EN voi mp3 master.

QUAN TRONG (A11 #114 + T17):
  - KHONG dung `package.py --mux` cho tap nay: no lay `audio_master_EN_t05.wav`
    (1449,24 s — WAV STALE cua ban MiniMax 25/10), trong khi mp3 master moi
    (Higgs 03/11) chi 1272,51 s. Mux sai wav => lech 177 s.
  - Lay truc tiep `02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp3`.
  - Chuoi limiter lay tu edition.py EPISODES["05"]["mux_af"] (EN: 0,63 + latency=1).

Chay: py -3 .work/_mux_en_t05.py
"""
import json
import os
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ.setdefault("AE_EP", "05")
os.environ.setdefault("AE_LANG", "en")
WORK = pathlib.Path(__file__).resolve().parents[1] / ".work"
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
OUT_DIR = ED.OUT_DIR
MP3 = OUT_DIR / (ED.MASTER + ".mp3")
MP4 = OUT_DIR / (ED.MASTER + ".mp4")
PICTURE = WORK / "video3_EN_t05" / "picture.mp4"
CHUNKS = [WORK / f"video3_EN_t05_{t}" / "picture.mp4" for t in ("A", "B", "C", "D")]
TL = json.loads((WORK / "timeline_s_EN_t05.json").read_text(encoding="utf-8"))
TOT = TL["total"]
FPS = 30


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if p.returncode != 0:
        raise SystemExit(f"LOI: {' '.join(str(c) for c in cmd[:4])}...\n{p.stderr[:1200]}")
    return p.stdout


def probe(path):
    out = run([str(FP), "-v", "error", "-count_frames", "-select_streams", "v:0",
               "-show_entries", "stream=nb_read_frames,width,height,r_frame_rate,codec_name",
               "-show_entries", "format=duration", "-of", "json", str(path)])
    return json.loads(out)


print("===== GHEP + MUX Tap05 EN =====")
print(f"  mp3 master : {MP3}")
print(f"  timeline   : {TOT} s")

# ---------- 1. kiem tra 4 chunk
for c in CHUNKS:
    if not c.exists():
        raise SystemExit(f"THIEU CHUNK: {c}")
    print(f"  chunk {c.parent.name}: {c.stat().st_size:,} bytes")

# ---------- 2. concat 1 lan
lst = WORK / "video3_EN_t05" / "parts_concat.txt"
lst.parent.mkdir(parents=True, exist_ok=True)
lst.write_text("".join(f"file '{c.as_posix()}'\n" for c in CHUNKS), encoding="utf-8")
print("  concat 4 chunk -> picture.mp4 ...")
run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
     "-c", "copy", str(PICTURE)])
info = probe(PICTURE)
v = info["streams"][0]
nf = int(v["nb_read_frames"])
dur = float(info["format"]["duration"])
exp = int(TOT * FPS)
print(f"  picture.mp4: {nf} khung · {dur:.3f} s · {v['width']}x{v['height']} @ {v['r_frame_rate']}")
if nf != exp:
    raise SystemExit(f"LOI: so khung {nf} != {exp}")
if abs(dur - TOT) > 0.05:
    raise SystemExit(f"LOI: thoi luong picture {dur:.3f} != timeline {TOT}")
if v["width"] != 1920 or v["height"] != 1080:
    raise SystemExit(f"LOI: khung hinh {v['width']}x{v['height']}")

# ---------- 3. mux voi mp3 master
mux_af = ED.EP.get("mux_af", "alimiter=limit=0.7943:attack=5:release=50:level=disabled")
print(f"  mux_af = {mux_af}")
cmd = [str(FF), "-y", "-v", "error", "-i", str(PICTURE), "-i", str(MP3),
       "-map", "0:v", "-map", "1:a", "-c:v", "copy"]
if mux_af:
    cmd += ["-af", mux_af]
cmd += ["-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(MP4)]
run(cmd)
print(f"  -> {MP4}")

# ---------- 4. do lai tren chinh mp4
mi = json.loads(run([str(FP), "-v", "error", "-count_frames", "-select_streams", "v:0",
                     "-show_entries", "stream=nb_read_frames,width,height,r_frame_rate",
                     "-show_entries", "format=duration", "-of", "json", str(MP4)]))
mv = mi["streams"][0]
mdur = float(mi["format"]["duration"])
mnf = int(mv["nb_read_frames"])
print(f"  mp4: {mnf} khung · {mdur:.3f} s · {mv['width']}x{mv['height']} @ {mv['r_frame_rate']}")
if abs(mdur - TOT) > 0.05:
    raise SystemExit(f"LOI: thoi luong mp4 {mdur:.3f} != {TOT}")
if mnf != exp:
    raise SystemExit(f"LOI: so khung mp4 {mnf} != {exp}")
print(f"  OK: mp4 khop timeline ({TOT} s, {exp} khung)")
