#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra các mảnh ghép trước khi mux (JA Tap03): intro · ảnh tĩnh · stems · assets."""
import glob
import io
import json
import os
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

fails = []


def chk(name, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}  {detail}")
    if not ok:
        fails.append(name)


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")


def probe(p):
    r = run([str(FP), "-v", "error", "-show_entries",
             "format=duration,size:stream=codec_type,codec_name,width,height,sample_rate,channels",
             "-of", "json", str(p)])
    return json.loads(r.stdout or "{}")


def frame_bright(p, t):
    fr = subprocess.run([str(FF), "-v", "error", "-ss", f"{t:.3f}", "-i", str(p),
                         "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                        capture_output=True).stdout
    if not fr:
        return None, None
    a = np.asarray(Image.open(io.BytesIO(fr)).convert("L"), dtype=np.float64)
    return float((a > 140).mean()), fr


print("=" * 74)
print("KIỂM TRA MẢNH GHÉP TRƯỚC KHI MUX — JA TAP03")
print("=" * 74)

# ---- intro
print("\n-- intro --")
INTRO = ROOT / "assets" / "brand" / "intro_kenh_JA_t03.mov"
if INTRO.exists():
    p = probe(INTRO)
    d = float(p["format"]["duration"])
    vs = [s for s in p["streams"] if s.get("codec_type") == "video"]
    chk("intro tồn tại + có video", bool(vs), f"{d:.2f}s · {vs[0].get('width')}x{vs[0].get('height')} "
        f"@{vs[0].get('r_frame_rate') if vs else '?'}")
    # Parity với intro chuẩn của dự án: profile độ sáng phải khớp `intro_kenh.mov`.
    # (T=1 s đen là fade-in CỐ Ý — không được dùng làm cổng "không đen".)
    TS = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0, 10.0, 15.0, 20.0, 21.5]
    REF = ROOT / "assets" / "brand" / "intro_kenh.mov"

    def profile(path):
        out = []
        for t in TS:
            fr = subprocess.run([str(FF), "-v", "error", "-ss", f"{t:.3f}", "-i", str(path),
                                 "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                                capture_output=True).stdout
            if not fr:
                out.append(None)
                continue
            a = np.asarray(Image.open(io.BytesIO(fr)).convert("L"), dtype=np.float64)
            out.append(float((a > 140).mean()) * 100)
        return out

    pr = profile(REF) if REF.exists() else None
    pj = profile(INTRO)
    if pr:
        diffs = [abs(a - b) for a, b in zip(pr, pj) if a is not None and b is not None]
        worst = max(diffs) if diffs else 999
        chk("intro khớp profile intro chuẩn (≤ 1,5 % điểm sáng)", worst <= 1.5,
            f"lớn nhất {worst:.2f} điểm % · ref={['%.1f' % v for v in pr]} · ja={['%.1f' % v for v in pj]}")
    else:
        chk("intro có nội dung ở 5–20 s", all(v is not None and v > 5 for v in pj[5:9]),
            f"{pj}")
else:
    chk("intro tồn tại", False, str(INTRO))

# ---- ảnh tĩnh
print("\n-- ảnh tĩnh --")
shots = json.loads((W / "shots_JA_t03.json").read_text(encoding="utf-8-sig"))["shots"]
STILL = W / "video3_JA_t03" / "stills"
missing = [s["id"] for s in shots if not (STILL / f"shot_{s['id']}.png").exists()]
chk("110/110 ảnh tĩnh có mặt", not missing, f"thiếu {len(missing)} {missing[:5]}")
dims = set()
for s in shots:
    f = STILL / f"shot_{s['id']}.png"
    if f.exists():
        dims.add(Image.open(f).size)
chk("ảnh tĩnh đủ kích thước 1920x1080", dims == {(1920, 1080)}, f"{dims}")

# ---- stems
print("\n-- stems (badge vai) --")
STEM = W / "stems_JA_t03"
for role in ["H", "D", "C", "N1", "N2"]:
    f = STEM / f"{role}.wav"
    if f.exists():
        p = probe(f)
        d = float(p["format"]["duration"])
        chk(f"stem {role}", d > 0.1, f"{d:.2f}s · {os.path.getsize(f)} B")
    else:
        chk(f"stem {role}", False, "thiếu")

# ---- nền
print("\n-- nền --")
bgs = sorted({s["bg"] for s in shots if s.get("bg")} | {s["bg2"] for s in shots if s.get("bg2")})
miss_bg = [b for b in bgs if not (ROOT / "assets" / "bg" / f"{b}.png").exists()]
chk("mọi nền dùng trong shot đều tồn tại", not miss_bg, f"{len(bgs)} nền · thiếu {miss_bg}")

# ---- contact sheets
print("\n-- contact sheet --")
for f in sorted(glob.glob(str(W / "_qc_sheets_ja_t03" / "*.png"))):
    im = Image.open(f)
    print(f"       {os.path.basename(f):20s} {im.size}")
sheets = glob.glob(str(W / "_qc_sheets_ja_t03" / "sheet_*.png"))
chk("contact sheet cho soi mắt (H9)", len(sheets) >= 5, f"{len(sheets)} file")

print()
print("=" * 74)
print(f"KET QUA: {'PASS' if not fails else 'FAIL - ' + str(len(fails)) + ' loi'}")
for f in fails:
    print("  -", f)
sys.exit(0 if not fails else 1)
