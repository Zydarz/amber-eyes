#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit font JA Tap02:
(1) T5 shots: 'big' text -> do co ky tu ma Bahnschrift (F_NUM) khong co?
(2) Font coverage: moi ky tu tren hinh co trong font JA dung khong?
(3) Dem do rong khi doi F_NUM sang YuGothB (co vua khung khong).
"""
import json
import re
import sys
from pathlib import Path

from PIL import ImageFont

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
FONTS = Path(r"C:\Windows\Fonts")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]

print("=== 1. TAI FONT JA CO SAN ===")
for n in ["YuGothB.ttc", "YuGothM.ttc", "bahnschrift.ttf", "msgothic.ttc", "meiryo.ttc",
          "msgothicbd.ttc", "YUGOTH*.TTF"]:
    p = sorted(FONTS.glob(n))
    print(f"  {n:<20} {[x.name for x in p]}")

print("\n=== 2. COT 'Chu' CO KY TU NHI (Kanji/Hiragana/Katakana) ===")


def has_jp(t):
    return any("\u3040" <= c <= "\u30ff" or "\u4e00" <= c <= "\u9fff" or
               "\uff00" <= c <= "\uffef" for c in t)


jp_shots = []
for s in shots:
    txts = [v for seg in s["segments"] for k, v in seg["elems"]]
    if any(has_jp(t) for t in txts):
        jp_shots.append((s["id"], s["template"], txts))
print(f"  so shot co tieng Nhat tren hinh: {len(jp_shots)} / {len(shots)}")

print("\n=== 3. T5 SHOT: 'big' -> phan so co ky tu Nhat (F_NUM/Bahnschrift) ===")
NUMRE = re.compile(r"^([−-]?)(\d+)(.*)$")
t5_bad = []
for s in shots:
    if s["template"] != "T5":
        continue
    for seg in s["segments"]:
        for kind, v in seg["elems"]:
            if kind != "bold":
                continue
            m = NUMRE.match(v)
            if not m:
                continue
            rest = m.group(3)
            if rest and has_jp(rest):
                t5_bad.append((s["id"], v, m.group(2), rest))
print(f"  T5 co phan sau so chua ky tu Nhat (bi tofu): {len(t5_bad)}")
for x in t5_bad:
    print(f"    {x[0]}: big={x[1]!r}  num={x[2]!r}  rest={x[3]!r}")

print("\n=== 4. T5 'date' variant (F_MONO) co ky tu Nhat khong ===")
t5_date_bad = []
for s in shots:
    if s["template"] != "T5" or s["variant"] != "date":
        continue
    for seg in s["segments"]:
        for kind, v in seg["elems"]:
            if kind == "bold" and has_jp(v):
                t5_date_bad.append((s["id"], v))
print(f"  T5-date co chu Nhat (F_MONO=YuGothM -> OK): {len(t5_date_bad)}")
for x in t5_date_bad[:10]:
    print(f"    {x[0]}: {x[1]!r}")

print("\n=== 5. DO RONG: Bahnschrift vs YuGothB cho cac 'big' cua T5 ===")
fb = ImageFont.truetype(str(FONTS / "bahnschrift.ttf"), 250)
fy = ImageFont.truetype(str(FONTS / "YuGothB.ttc"), 250)
for s in shots:
    if s["template"] != "T5":
        continue
    for seg in s["segments"]:
        for kind, v in seg["elems"]:
            if kind != "bold":
                continue
            m = NUMRE.match(v)
            if not m:
                continue
            num, rest = m.group(2), m.group(3)
            sz = 250 if len(v) < 7 else 170
            fb2 = ImageFont.truetype(str(FONTS / "bahnschrift.ttf"), sz)
            fy2 = ImageFont.truetype(str(FONTS / "YuGothB.ttc"), sz)
            w_b = fb2.getlength(f"{num}{rest}")
            w_y = fy2.getlength(f"{num}{rest}")
            print(f"  {s['id']:<6} {v!r:<28} sz={sz:<4} "
                  f"Bahnschrift={w_b:>7.0f}px  YuGothB={w_y:>7.0f}px  "
                  f"{'VUOT' if w_y > 1920 - 60 - 30 else 'vua'}")

print("\n=== 6. COVERAGE: ky tu Nhat co trong font JA khong? ===")
jm = ImageFont.truetype(str(FONTS / "YuGothM.ttc"), 40)
jb = ImageFont.truetype(str(FONTS / "YuGothB.ttc"), 40)


def missing(fnt, chars):
    ref = fnt.getmask("\uffff").tobytes()
    out = set()
    for ch in chars:
        if ch in " \n\t":
            continue
        if fnt.getmask(ch).tobytes() == ref and ch != "\uffff":
            out.add(ch)
    return out


alltxt = set()
for s in shots:
    for seg in s["segments"]:
        for k, v in seg["elems"]:
            alltxt |= set(v)
jpchars = {c for c in alltxt if has_jp(c)}
print(f"  tong ky tu tren hinh: {len(alltxt)} · ky tu Nhat: {len(jpchars)}")
print(f"  YuGothM thieu: {sorted(missing(jm, jpchars))}")
print(f"  YuGothB thieu: {sorted(missing(jb, jpchars))}")
lat = {c for c in alltxt if not has_jp(c)}
print(f"  ky tu Latin/so: {sorted(lat)}")
print(f"  Bahnschrift thieu (trong so Latin): {sorted(missing(fb, lat))}")
