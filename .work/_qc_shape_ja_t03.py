#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC hinh hoc: so sanh CAU TRUC chu tren hinh cua JA voi VN.

Moi shot: tach chu theo dung quy tac renderer (parse_text -> split_elems) roi so:
  - so segment
  - chuoi kieu phan tu (bold / ital / quote) theo tung segment
  - voi shot T8: so muc danh sach sau khi tach " · " (chi con 1 nhom italic)
Neu khac -> chu JA se render khac VN (sai so dong, mat so "01 ·", ...).
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"


def parse_text(cell):
    """Sao che parse_text() cua build_video3.py."""
    cell = re.sub(r"\*\*.+?\*\*|\*[^*]+?\*|“.+?”", lambda m: m.group(0).replace("→", "⟶"), cell)
    segs = []
    for part in cell.split(" → "):
        part = part.strip()
        if not part:
            continue
        elems = []
        for piece in re.split(r"(\*\*.*?\*\*|\*[^*]+?\*|“.+?”)", part):
            piece = piece.strip()
            if not piece:
                continue
            if piece.startswith("**") and piece.endswith("**"):
                elems.append(["bold", piece[2:-2]])
            elif piece.startswith("*") and piece.endswith("*"):
                elems.append(["ital", piece[1:-1]])
            elif piece.startswith("“") and piece.endswith("”"):
                elems.append(["quote", piece[1:-1]])
            else:
                elems.append(["plain", piece])
        if elems:
            segs.append({"elems": elems})
    return segs


def split_elems(elems):
    lab, head, quo = [], [], []
    for k, v in elems:
        (head if k == "bold" else quo if k == "quote" else lab).append(v)
    return lab, head, quo


def shape(segs):
    out = []
    for sg in segs:
        lab, head, quo = split_elems(sg["elems"])
        out.append((len(sg["elems"]), tuple(k for k, _ in sg["elems"])))
    return out


def t8_items(segs):
    """So muc danh sach T8 nhu renderer t8_list()."""
    if not segs:
        return []
    lab, head, _ = split_elems(segs[0]["elems"])
    if lab:
        if len(lab) > 1:
            return lab[1].split(" · ")
        return lab[0].split(" · ")
    return []


# --- doc bang VN (nguon chu) va bang JA (da dung)
vn_lines = (ROOT / "02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_lines) if i > i0 and l.startswith("**Tổng:"))
VN = {}
for l in vn_lines[i0:i1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    VN[m.group(1)] = {"chu": c[5], "mau": c[3]}

JA = {}
ja_lines = (ROOT / "02_SAN_XUAT/Tap03_JA/KeHoach_Video_Tap03_JA.md").read_text(encoding="utf-8").splitlines()
j0 = next(i for i, l in enumerate(ja_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
for l in ja_lines[j0:]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    JA[m.group(1)] = {"chu": c[5], "mau": c[3]}

bad = []
for sid, v in VN.items():
    if sid not in JA:
        bad.append((sid, "thieu dong JA"))
        continue
    j = JA[sid]
    if v["chu"] == "—" and j["chu"] == "—":
        continue
    vs = parse_text(v["chu"])
    js = parse_text(j["chu"])
    if shape(vs) != shape(js):
        bad.append((sid, f"cau truc khac: VN {shape(vs)} vs JA {shape(js)}"))
        continue
    if v["mau"].startswith("T8"):
        vi, ji = t8_items(vs), t8_items(js)
        if len(vi) != len(ji):
            bad.append((sid, f"T8 so muc khac: VN {len(vi)} vs JA {len(ji)} | JA={ji}"))

print(f"so shot doi chieu = {len(VN)}")
if bad:
    print(f"KHAC BIET ({len(bad)}):")
    for b in bad:
        print("  ", b[0], "->", b[1])
    sys.exit(1)
print("KET QUA: PASS — cau truc chu JA khop VN")
