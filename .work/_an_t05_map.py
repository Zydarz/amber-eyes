#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — kiểm tra bảng shot CŨ còn dùng được với kịch bản MỚI không.

Đo:
  * các element trong bảng shot cũ có còn tồn tại trong kịch bản mới?
  * có element MỚI nào bảng shot cũ chưa phủ?
  * phân bố câu mới theo element.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

LANGS = [
    ("VN", "01_KICH_BAN/Tap05/kichban_tap05_23102026.md",
     "02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md"),
    ("EN", "01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md",
     "02_SAN_XUAT/Tap05_EN/KeHoach_Video_Tap05_EN.md"),
    ("JA", "01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md",
     "02_SAN_XUAT/Tap05_JA/KeHoach_Video_Tap05_JA.md"),
]


def rows_of(plan):
    t = plan.read_text(encoding="utf-8")
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", t, re.M)
    sec = t[m.end():]
    mt = re.search(r"^\*\*Tổng:", sec, re.M)
    if mt:
        sec = sec[: mt.start()]
    out = []
    for line in sec.splitlines():
        if re.match(r"\|\s*[1-5]-\d+", line):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            out.append(c)
    return out


for lang, kb, plan in LANGS:
    print("=" * 80)
    print(f"### {lang}")
    els = parse_file(str(ROOT / kb))
    loi = {e["id"]: e for e in els if e["kind"] == "LOI"}
    n_sent = {eid: len(e.get("sentences", [])) for eid, e in loi.items()}
    rows = rows_of(ROOT / plan)

    used_els, covered = [], set()
    for c in rows:
        for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", c[1]):
            used_els.append(ma)
            for k in range(int(a), int(b or a) + 1):
                covered.add(f"{ma}#{k}")

    missing_el = [e for e in dict.fromkeys(used_els) if e not in loi]
    new_els = [e for e in loi if e not in used_els]
    print(f"  element LOI trong kịch bản mới: {len(loi)}")
    print(f"  element có dùng trong bảng shot: {len(dict.fromkeys(used_els))}")
    print(f"  element bảng shot KHÔNG còn trong kịch bản: {missing_el}")
    print(f"  element MỚI chưa có trong bảng shot: {new_els}")
    for e in new_els:
        txt = " ".join(s["text"] for s in loi[e]["sentences"])
        print(f"      {e} ({n_sent[e]} câu): {txt[:150]}")

    # câu trong bảng shot có còn hợp lệ (mã câu có tồn tại)?
    allids = {s["id"] for e in loi.values() for s in e["sentences"]}
    bad = sorted(x for x in covered if x not in allids)
    uncov = sorted(allids - covered)
    print(f"  câu bảng shot dùng: {len(covered)} · không tồn tại: {len(bad)} {bad[:6]}")
    print(f"  câu mới CHƯA phủ: {len(uncov)}  {uncov[:10]}{'…' if len(uncov) > 10 else ''}")

    # bảng shot cũ dùng element nào với bao nhiêu câu; element mới có bao nhiêu câu
    from collections import Counter
    old_cnt = Counter()
    for c in rows:
        for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", c[1]):
            old_cnt[ma] += int(b or a) - int(a) + 1
    delta = [(e, old_cnt.get(e, 0), n_sent[e]) for e in loi if old_cnt.get(e, 0) != n_sent[e]]
    print(f"  element có SỐ CÂU khác (cũ → mới): {len(delta)}")
    for e, o, n in delta:
        print(f"      {e}: {o} → {n}")
