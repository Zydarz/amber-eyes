# -*- coding: utf-8 -*-
"""Kiem tra du anh nen cho TikTok Tap 04 (VI/EN/JA).

Kiem tra:
  1. Shot trong 3 ke hoach (VN/EN/JA) + 3 SPEC JSON
  2. Nen dung trong ke hoach co ton tai trong assets/bg/?
  3. Kich thuoc 1080x1920?
  4. Dong provenance.json cho tung nen?
  5. Co bao nhieu file WAV cau (de dung video)?
"""
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:/TEST/Gax/amber-eyes"
TIK = os.path.join(ROOT, "02_SAN_XUAT", "TIKTOK")
BG = os.path.join(ROOT, "assets", "bg")

LANGS = [
    ("VI", os.path.join(TIK, "Tap04"), "KE_HOACH_CLIP_TAP04.md", "SPEC_AUDIO_CLIP_TAP04.json"),
    ("EN", os.path.join(TIK, "Tap04_EN"), "KE_HOACH_CLIP_TAP04_EN.md", "SPEC_AUDIO_CLIP_TAP04.json"),
    ("JA", os.path.join(TIK, "Tap04_JA"), "KE_HOACH_CLIP_TAP04_JA.md", "SPEC_AUDIO_CLIP_TAP04.json"),
]

SHOT_RE = re.compile(r"^\|\s*`(TK\d\.\d+#\d+)`\s*\|")


def parse_plan(path):
    """Tra ve {clip: [(code, bg, motion), ...]} tu bang shot."""
    per = defaultdict(list)
    cur = None
    with io.open(path, encoding="utf-8") as f:
        for line in f:
            m = SHOT_RE.match(line.strip())
            if not m:
                continue
            code = m.group(1)
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            # cells: code | vai | emotion | speed | nghỉ | nen | motion | lời | nguồn
            bg = cells[5].strip("`") if len(cells) > 5 else ""
            mv = cells[6].strip("`") if len(cells) > 6 else ""
            cur = code.split(".")[0]
            per[cur].append((code, bg, mv))
    return per


def parse_spec(path):
    d = json.load(io.open(path, encoding="utf-8"))
    out = []
    if isinstance(d, dict):
        raw_clips = d.get("clips") or d.get("items") or []
        if isinstance(raw_clips, dict):
            clips = list(raw_clips.values())
        else:
            clips = raw_clips
    else:
        clips = d
    for c in clips:
        cid = c.get("id") or c.get("clip") or ""
        for it in (c.get("items") or c.get("lines") or []):
            iid = it.get("clip_line_id") or it.get("id")
            out.append((cid, iid, it.get("bg")))
    return out, d


print("=" * 78)
print("A. BANG SHOT TRONG 3 KE HOACH")
print("=" * 78)

plan_bgs = {}
for tag, d, plan, spec in LANGS:
    p = os.path.join(d, plan)
    if not os.path.exists(p):
        print("  %s: THIEU %s" % (tag, p))
        continue
    per = parse_plan(p)
    total = sum(len(v) for v in per.values())
    allbg = [bg for v in per.values() for _, bg, _ in v]
    plan_bgs[tag] = per
    print("  %-3s %2d clip · %2d shot · %2d nen duy nhat" % (
        tag, len(per), total, len(set(allbg))))

# so sanh bg giua 3 ngon ngu
tags = list(plan_bgs)
if len(tags) == 3:
    print()
    same_code = True
    for i in range(3):
        for j in range(i + 1, 3):
            a = plan_bgs[tags[i]]
            b = plan_bgs[tags[j]]
            ka = [c for v in a.values() for c, _, _ in v]
            kb = [c for v in b.values() for c, _, _ in v]
            ba = [bg for v in a.values() for _, bg, _ in v]
            bb = [bg for v in b.values() for _, bg, _ in v]
            if ka != kb:
                same_code = False
            print("  %s vs %s: ma shot giong = %s · nen giong = %s" % (
                tags[i], tags[j], ka == kb, ba == bb))
    print("  => 3 ngon ngu cung bo ma shot:", "CO" if same_code else "KHONG")

print()
print("=" * 78)
print("B. NEN TRONG KE HOACH: TON TAI + KICH THUOC")
print("=" * 78)

from PIL import Image

all_used = set()
missing = []
badsize = []
for tag, per in plan_bgs.items():
    miss = []
    bad = []
    n = 0
    for clip, rows in per.items():
        for code, bg, mv in rows:
            n += 1
            all_used.add(bg)
            name = bg if bg.endswith(".png") else bg + ".png"
            fp = os.path.join(BG, name)
            if not os.path.exists(fp):
                miss.append((code, name))
                continue
            with Image.open(fp) as im:
                if im.size != (1080, 1920):
                    bad.append((name, im.size))
    print("  %-3s %2d shot · thieu nen: %d · sai kich thuoc: %d" % (
        tag, n, len(miss), len(bad)))
    for m in miss:
        print("        THIEU:", m[0], m[1])
    for b in bad:
        print("        SAI KT:", b[0], b[1])
    missing += miss
    badsize += bad

print()
print("  Tong nen duy nhat dung trong 3 ke hoach: %d" % len(all_used))

# nen dang ton tai nhung khong dung
on_disk = sorted(f for f in os.listdir(BG) if f.startswith("tk04_"))
unused = [f for f in on_disk if f[:-4] not in all_used]
print("  File tk04_* tren dia: %d · trong do khong dung: %d" % (len(on_disk), len(unused)))
for u in unused:
    print("        KHONG DUNG:", u)

print()
print("=" * 78)
print("C. SPEC_AUDIO_CLIP_TAP04.json")
print("=" * 78)
for tag, d, plan, spec in LANGS:
    sp = os.path.join(d, spec)
    if not os.path.exists(sp):
        print("  %s: THIEU %s" % (tag, sp))
        continue
    rows, raw = parse_spec(sp)
    bgs = [b for _, _, b in rows if b]
    miss = [b for b in bgs if not os.path.exists(os.path.join(BG, b + ".png" if not b.endswith(".png") else b))]
    print("  %-3s spec: %2d item · %2d nen · thieu file: %d" % (
        tag, len(rows), len(set(bgs)), len(miss)))
    for m in sorted(set(miss)):
        print("        THIEU:", m)
    # doi chieu bg voi ke hoach
    per = plan_bgs.get(tag, {})
    planmap = {c: bg for v in per.values() for c, bg, _ in v}
    spmap = {i: b for _, i, b in rows if i}
    diff = [(k, planmap.get(k), spmap.get(k)) for k in planmap
            if k in spmap and planmap[k] != spmap[k]]
    miss2 = [k for k in planmap if k not in spmap]
    print("        lech bg vs ke hoach: %d · thieu item trong spec: %d" % (len(diff), len(miss2)))
    for x in diff[:10]:
        print("          ", x)
    for x in miss2[:10]:
        print("           THIEU ITEM:", x)

print()
print("=" * 78)
print("D. PROVENANCE.JSON")
print("=" * 78)
pp = os.path.join(ROOT, "provenance.json")
if os.path.exists(pp):
    prov = json.load(io.open(pp, encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san") or prov.get("items") or []
    by_file = {it.get("file"): it for it in items}
    ai = fb = 0
    noprov = []
    for bg in sorted(all_used):
        key = "assets/bg/%s.png" % bg
        row = by_file.get(key)
        if not row:
            noprov.append(bg)
        elif row.get("prompt"):
            ai += 1
        else:
            fb += 1
    print("  Dong provenance cho nen: AI that %d · du phong %d · thieu dong %d" % (ai, fb, len(noprov)))
    for n in noprov:
        print("        THIEU DONG:", n)
else:
    print("  KHONG tim thay provenance.json")

print()
print("=" * 78)
print("E. FILE AM THANH DE DUNG VIDEO")
print("=" * 78)
for tag, d, plan, spec in LANGS:
    if not os.path.isdir(d):
        continue
    wav = [f for f in os.listdir(d) if f.lower().endswith(".wav")]
    mp4 = [f for f in os.listdir(d) if f.lower().endswith(".mp4")]
    mp3 = [f for f in os.listdir(d) if f.lower().endswith(".mp3")]
    print("  %-3s thu muc: wav %d · mp3 %d · mp4 %d" % (tag, len(wav), len(mp3), len(mp4)))
    for f in sorted(mp3):
        print("        ", f)
    # thu muc con
    for sub in sorted(os.listdir(d)):
        sp = os.path.join(d, sub)
        if os.path.isdir(sp):
            files = os.listdir(sp)
            print("        [dir] %s/ : %d file" % (sub, len(files)))
            for f in sorted(files)[:6]:
                print("               ", f)
            if len(files) > 6:
                print("               ... +%d" % (len(files) - 6))
