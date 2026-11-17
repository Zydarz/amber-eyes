#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC trailer Concept A — kéo khung hình theo mốc, ghép montage, đo âm lượng.

Dùng: py -3 .work/_qc_trailer.py
Ghi: .work/qc_montage/trailer_frames.jpg · .work/qc_montage/trailer_audio.txt
"""
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work" / "trailer_a"
OUT = ROOT / ".work" / "qc_montage"
OUT.mkdir(parents=True, exist_ok=True)
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

STAMPS = [0.8, 2.0, 3.6, 6.4, 9.9, 12.0, 15.9, 18.0, 21.9, 24.0, 27.9, 30.0, 33.9,
          35.6, 37.9, 40.5, 43.5, 45.9, 47.6, 49.5]


def run(cmd):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0:
        print("!!", r.stderr[-600:])
    return r.stdout + "\n" + r.stderr


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", default="vi", choices=["vi", "en"])
    a = ap.parse_args()
    suf = "" if a.lang == "vi" else "_" + a.lang.upper()
    src = WORK / f"trailer_master{suf}.mp4"
    if not src.exists():
        src = WORK / f"picture{suf}.mp4"
    frames = []
    for i, t in enumerate(STAMPS):
        p = OUT / f"tr_{i:02d}.jpg"
        run([FF, "-y", "-v", "error", "-ss", str(t), "-i", str(src), "-frames:v", "1", "-q:v", "3", str(p)])
        if p.exists():
            frames.append((t, p))
    cell, cols = 620, 4
    font = ImageFont.truetype("arial.ttf", 20)
    items = []
    for t, p in frames:
        im = Image.open(p).convert("RGB")
        h = int(cell * im.height / im.width)
        items.append((t, im.resize((cell, h), Image.LANCZOS)))
    rows = (len(items) + cols - 1) // cols
    rh = [max(it[1].height for it in items[r * cols:(r + 1) * cols]) for r in range(rows)]
    sheet = Image.new("RGB", (cols * cell, sum(rh) + rows * 30), (16, 16, 20))
    d = ImageDraw.Draw(sheet)
    y = 0
    for r in range(rows):
        for c, (t, im) in enumerate(items[r * cols:(r + 1) * cols]):
            x = c * cell
            sheet.paste(im, (x, y + 30))
            d.text((x + 8, y + 5), f"t={t:.1f}s", font=font, fill=(255, 205, 120))
        y += rh[r] + 30
    dst = OUT / f"trailer_frames{suf}.jpg"
    sheet.save(dst, quality=90)
    print("wrote", dst, sheet.size)

    if (WORK / f"trailer_master{suf}.mp4").exists():
        out = run([FF, "-i", str(WORK / f"trailer_master{suf}.mp4"), "-af",
                   "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"])
        j = out[out.rfind("{"):out.rfind("}") + 1]
        print("=== loudness mp4 cuối ===")
        print(json.dumps(json.loads(j), indent=1))
        sil = run([FF, "-i", str(WORK / f"trailer_master{suf}.mp4"), "-af",
                   "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"])
        segs = [l.strip() for l in sil.splitlines() if "silence_" in l]
        print("=== khoảng câm > 0,3s ===")
        print("\n".join(segs) if segs else "(không có)")
        err = run([FF, "-v", "error", "-i", str(WORK / f"trailer_master{suf}.mp4"), "-f", "null", "-"])
        print("=== lỗi giải mã ===")
        print(err.strip() or "(0 lỗi)")
        pr = run([str(FF).replace("ffmpeg.exe", "ffprobe.exe"), "-v", "error", "-show_entries",
                  "format=duration:stream=codec_name,width,height,r_frame_rate,sample_rate,channels",
                  "-of", "json", str(WORK / f"trailer_master{suf}.mp4")])
        print("=== thông tin file ===")
        print(pr)


if __name__ == "__main__":
    main()
