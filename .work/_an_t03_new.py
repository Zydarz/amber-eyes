#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A1 — new script (Tap03) vs shot table in the plan doc: coverage + content diff.

Usage: py -3 .work/_an_t03_new.py [ep=03] [lang=vi|en|ja|ko]
Prints: element/sentence inventory of the NEW script, then per-shot analysis.
"""
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
EP = os.environ.get("AE_EP", "03").zfill(2)
LANG = os.environ.get("AE_LANG", "vi").strip().lower()
SUF = {"vi": "", "en": "_EN", "ja": "_JA", "ko": "_KO"}[LANG]

SCRIPT = ROOT / ".work" / f"script_tap{EP}{SUF}.json"
PLAN_DIR = ROOT / "02_SAN_XUAT" / (f"Tap{EP}{SUF}" if LANG != "vi" else f"Tap{EP}")
PLAN = PLAN_DIR / f"KeHoach_Video_Tap{EP}{SUF}.md"

els = json.loads(SCRIPT.read_text(encoding="utf-8"))

# ---- inventory of the new script
sent_ids = []
print(f"=== SCRIPT {SCRIPT.name} — {len(els)} elements ===")
for e in els:
    sents = e.get("sentences") or []
    ids = [f"{e['id']}#{i+1}" for i in range(len(sents))]
    sent_ids += ids
    kind = e.get("kind", "")
    tag = f"[{kind}]" if kind else ""
    txts = [s["text"] for s in sents[:2]] if sents else []
    print(f"{e['id']:>6} {tag:<6} n={len(sents):<3} {e.get('role','')or'':<3} "
          f"{('| ' + ' / '.join(t[:40] for t in txts)) if txts else (e.get('desc') or '')[:70]}")
print(f"\nTỔNG CÂU (mới): {len(sent_ids)}")

# ---- shot table from the plan doc
if not PLAN.exists():
    print(f"\n!! KHÔNG CÓ HỒ SƠ: {PLAN}")
    sys.exit(0)

text = PLAN.read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
if not m:
    print("!! không thấy mục 6")
    sys.exit(0)
sec = text[m.end():]
t = re.search(r"^\*\*Tổng:", sec, re.M)
if t:
    sec = sec[: t.start()]
rows = []
for line in sec.splitlines():
    if re.match(r"\|\s*\d-\d+", line):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)

print(f"\n=== BẢNG SHOT (hồ sơ) — {len(rows)} dòng ===")

covered = []
for r in rows:
    sid, cau = r[0], r[1]
    ids = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cau):
        ids += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    covered += ids
    print(f"{sid:<6} {cau:<34} -> {len(ids):>2} câu")

newset = set(sent_ids)
covset = set(covered)
print(f"\n--- ĐỐI CHIẾU ---")
print(f"câu trong script mới : {len(newset)}")
print(f"câu được bảng shot phủ: {len(covset)}")
print(f"THIẾU (script mới có, bảng shot không phủ): {sorted(newset - covset, key=lambda x: (x.split('#')[0], int(x.split('#')[1])))}")
print(f"THỪA (bảng shot có, script mới không có): {sorted(covset - newset, key=lambda x: (x.split('#')[0], int(x.split('#')[1])))}")

# element-level count diff
print(f"\n--- SỐ CÂU MỖI ELEMENT (mới) ---")
by_el = {}
for e in els:
    by_el[e["id"]] = len(e.get("sentences") or [])
old = {}
for r in rows:
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", r[1]):
        for k in range(int(a), int(b or a) + 1):
            old.setdefault(ma, set()).add(k)
for eid, n in by_el.items():
    o = old.get(eid, set())
    om = max(o) if o else 0
    flag = "" if om == n else f"  <<< ĐỔI (bảng shot cũ {om} -> mới {n})"
    print(f"{eid:<6} mới={n:<3} bảng shot cũ max#={om}{flag}")
