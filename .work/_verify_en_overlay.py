#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra ket qua cua lop phu EN: JSON hop le, so khoa, bang shot EN sinh ra."""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path("D:/TEST/Gax/amber-eyes")

p = ROOT / ".work/shots_text_tap02_EN.json"
raw = p.read_bytes()
print("BOM:", raw[:3] == b"\xef\xbb\xbf")
d = json.loads(raw.decode("utf-8"))
keys = [k for k in d if not k.startswith("_")]
print("khoa shot:", len(keys), "| co '_note':", "_note" in d)
badshape = []
for k in keys:
    v = d[k]
    ok = (isinstance(v, list) and len(v) == 3 and isinstance(v[0], str)
          and isinstance(v[1], list) and (v[2] is None or isinstance(v[2], str)))
    if not ok:
        badshape.append(k)
print("gia tri sai dang:", badshape)

plan = ROOT / "02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md"
rows = [l for l in plan.read_text(encoding="utf-8").splitlines() if re.match(r"\|\s*[1-5]-\d+\s*\|", l)]
print("dong shot trong bang EN:", len(rows))

# bang EN phai khop bang VN 161 dong
vn = ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md"
vnrows = [l for l in vn.read_text(encoding="utf-8").splitlines() if re.match(r"\|\s*[1-5]-\d+\s*\|", l)]
print("dong shot trong bang VN:", len(vnrows))
en_ids = [re.match(r"\|\s*([1-5]-\d+)\s*\|", l).group(1) for l in rows]
vn_ids = [re.match(r"\|\s*([1-5]-\d+)\s*\|", l).group(1) for l in vnrows]
print("thu tu ma shot EN == VN:", en_ids == vn_ids)

# cot Beat EN: cụm tiếng Anh phải nằm trong câu EN
script = json.loads((ROOT / ".work/script_tap02_EN.json").read_text(encoding="utf-8"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]


def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


bad = 0
for l in rows:
    c = l.strip().strip("|").split("|")
    sid = re.match(r"\|\s*([1-5]-\d+)\s*\|", l).group(1)
    ctx = " ".join(S.get(x, "") for x in sents(c[1].strip()))
    for ph in re.findall(r'ở "([^"]+)"', c[6].strip()):
        if ctx.strip() and ph.lower() not in ctx.lower():
            print("BEAT khong khop:", sid, ph)
            bad += 1
print("cụm beat EN sai:", bad)

# backup khop git HEAD
head = subprocess.run(["git", "-C", str(ROOT), "show", "HEAD:.work/shots_text_tap02_EN.json"],
                       capture_output=True, check=True).stdout
bk = (ROOT / ".work/_cu/shots_text_tap02_EN_pre_20261105.json").read_bytes()
print("backup == HEAD:", head == bk)
