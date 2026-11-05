#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — ánh xạ 83 dòng bảng shot VN (CŨ) sang kịch bản MỚI.

In ra: mỗi dòng bảng shot — element phủ, khoảng câu CŨ, khoảng câu MỚI (ánh xạ),
và câu MỚI nằm trong dòng đó (rút gọn). Dùng để soạn lại cột "Chữ".

Dùng:  py -3 .work/_map_t04_rows.py
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

PLAN = ROOT / "02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md"
NEW_KB = ROOT / "01_KICH_BAN/Tap04/kichban_tap04_23102026.md"


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def index(els):
    d = {}
    for el in els:
        if el["kind"] == "LOI":
            d[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]
    return d


new_idx = index(parse_file(str(NEW_KB)))

text = PLAN.read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
sec = text[m.end():]
sec = sec[:re.search(r"^\*\*Tổng:", sec, re.M).start()]
rows = [cells(l) for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]

print(f"{len(rows)} dòng · câu trong kịch bản mới: {sum(len(v) for v in new_idx.values())}\n")
covered = {}
for r in rows:
    sid, cau, vai, mau, nen, chu, beat, nv, tr = (r + [""] * 9)[:9]
    # các mã element trong cột Câu
    els_in = re.findall(r"`(\d)\.(\d+)`", cau)
    spans = []
    for ma, mb in els_in:
        eid = f"{ma}.{mb}"
        if eid not in new_idx:
            spans.append((eid, None, None))
            continue
        n = len(new_idx[eid])
        spans.append((eid, 1, n))
    # dạng `1.03#1`–`#2`  =>  lấy phạm vi con số sau #
    detail = []
    for m2 in re.finditer(r"`(\d)\.(\d+)#(\d+)`(?:\s*[–-]\s*`?#(\d+)`?)?", cau):
        eid = f"{m2.group(1)}.{m2.group(2)}"
        a = int(m2.group(3))
        b = int(m2.group(4) or m2.group(3))
        detail.append((eid, a, b, len(new_idx.get(eid, []))))
    print(f"--- {sid} | vai={vai} | mẫu={mau}")
    print(f"    nền : {nen[:90]}")
    print(f"    chữ : {chu[:150]}")
    if detail:
        for eid, a, b, n in detail:
            flag = "" if b <= n else f"  ⚠ câu mới chỉ có {n}"
            print(f"    map : {eid} #{a}–#{b}  (mới có {n} câu){flag}")
            for i, (sid2, tx) in enumerate(new_idx.get(eid, []), 1):
                if a <= i <= min(b, n):
                    print(f"         {sid2}: {tx[:150]}")
    else:
        print(f"    map : (không có mã câu) cau={cau[:90]}")
        for eid, a, n in spans:
            print(f"         {eid}: {n} câu mới")
