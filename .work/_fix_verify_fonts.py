#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render lai cac shot bi TOFU (1-05, 5-04, 5-05) + kiem tra coverage toan bo chu tren hinh."""
import os
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FONTS = Path(r"C:\Windows\Fonts")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

LOG = W / "_stills_ja_t02_fix.log"
with open(LOG, "w", encoding="utf-8") as fh:
    r = subprocess.run([sys.executable, str(W / "build_video3.py"),
                        "--stills", "1-05,5-04,5-05,2-10,5-02,1-01,1-14,4-01,5-01"],
                       cwd=ROOT, stdout=fh, stderr=subprocess.STDOUT)
print("rc =", r.returncode)
for line in LOG.read_text(encoding="utf-8", errors="replace").splitlines()[-3:]:
    print("  ", line)


def render_mask(fnt, ch):
    im = Image.new("L", (fnt.size * 2 + 20, fnt.size * 2 + 20), 0)
    ImageDraw.Draw(im).text((10, 10), ch, font=fnt, fill=255)
    return im.tobytes()


def missing(fnt, chars):
    ref = render_mask(fnt, "\uffff")
    return sorted({c for c in chars
                   if c not in " \n\t" and render_mask(fnt, c) == ref and c != "\uffff"})


import json  # noqa: E402

shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
allchars = set()
for s in shots:
    for seg in s["segments"]:
        for k, v in seg["elems"]:
            allchars |= set(v)
# them ca chu UI/role ten hien tren khung
allchars |= set("AMBER EYES 実際の事件記録から読み解く犯罪心理学 ホスト 捜査官 心理学者 証人 一般人 関係者 住民")

jp = {c for c in allchars if any("\u3040" <= c <= "\u30ff" or "\u4e00" <= c <= "\u9fff"
                                 or "\uff00" <= c <= "\uffef" for c in c)}
lat = allchars - jp
print(f"\n=== COVERAGE ({len(allchars)} ky tu · {len(jp)} Nhat) ===")
for name in ["YuGothB.ttc", "YuGothM.ttc", "bahnschrift.ttf"]:
    f = ImageFont.truetype(str(FONTS / name), 40)
    miss = missing(f, allchars)
    print(f"  {name:<20} thieu {len(miss)} ky tu: {miss[:40]}")

print("\n=== KICH THUOC file sau khi render lai ===")
for sid in ["1-05", "5-04", "5-05"]:
    p = W / "video3_JA_t02" / "stills" / f"shot_{sid}.png"
    with Image.open(p) as im:
        print(f"  {sid}: {im.size} · {p.stat().st_size} byte")
