#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H13 — khop 3 CHIEU: (Anh) — (Chu) — (Loi thoai).

1. Vai trong bang shot == vai doc cau trong timeline? (100%)
2. Cau trong shot co trong cau goc cua phien ban JA? (V3: chu tren hinh lay tu cau dang doc)
3. Con so tren hinh co trong cau dang doc khong? (H6/A9.2)
4. Cau trich (dau " ") co nguyen van trong kich ban?
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]
sent = {it["id"]: it for it in tl["items"]}
script = (ROOT / "01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md").read_text(encoding="utf-8-sig")

print("=== 1. VAI: bang shot vs timeline ===")
bad_role = []
for s in shots:
    if not s["sentences"]:
        continue
    roles = {sent[i]["role"] for i in s["sentences"]}
    if s["role"] not in roles:
        bad_role.append((s["id"], s["role"], sorted(roles)))
print(f"  shot co vai khac vai cau: {len(bad_role)} {bad_role[:8]}")

print("\n=== 2/3. CHU tren hinh lay tu cau dang doc (V3/H6) ===")
norm = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’()（）\-—–…]", "", t)
not_in_sent, num_missing = [], []
for s in shots:
    if not s["sentences"]:
        continue
    txt = " ".join(sent[i]["text"] for i in s["sentences"])
    ntxt = norm(txt)
    for seg in s["segments"]:
        for kind, v in seg["elems"]:
            if kind == "bold":
                # chu in dam: phai lay tu cau (dung 1 phan) — chap nhan trich danh tuong doi
                if norm(v) not in ntxt:
                    not_in_sent.append((s["id"], v[:46]))
            # so tren hinh phai co trong cau
            for num in re.findall(r"\d+", v):
                if num not in txt and num not in "".join(
                        re.findall(r"[0-9０-９]+", txt)):
                    num_missing.append((s["id"], num, v[:40]))
print(f"  chu in dam KHONG xuat hien trong cau: {len(not_in_sent)} / 131")
for x in not_in_sent[:12]:
    print(f"     {x[0]}: {x[1]!r}")
print(f"  CON SO tren hinh khong co trong cau: {len(num_missing)}")
for x in num_missing[:12]:
    print(f"     {x[0]}: so {x[1]!r} trong {x[2]!r}")

print("\n=== 4. CAU TRICH (dau nhay) co nguyen van trong kich ban? ===")
quotes = []
for s in shots:
    for seg in s["segments"]:
        for kind, v in seg["elems"]:
            if kind == "quote":
                quotes.append((s["id"], v))
nq_ok = 0
nq_bad = []
for sid, q in quotes:
    core = norm(q.strip("“”\"' "))
    if core and core in norm(script):
        nq_ok += 1
    else:
        nq_bad.append((sid, q[:60]))
print(f"  cau trich: {len(quotes)} · nam nguyen van trong kich ban: {nq_ok} · khong tim thay: {len(nq_bad)}")
for x in nq_bad[:10]:
    print(f"     {x[0]}: {x[1]!r}")

print("\n=== 5. TEN RIENG trong chu tren hinh co trong kich ban? ===")
names = ["DAVID RUSSELL WILLIAMS", "RUSSELL WILLIAMS", "NISSAN PATHFINDER", "JESSICA LLOYD",
         "MARIE-FRANCE COMEAU", "JIM SMYTH", "Elisabeth", "Elizabeth"]
for nm in names:
    inplan = nm.lower() in script.lower()
    print(f"  {nm:<26} trong kich ban JA: {inplan}")
