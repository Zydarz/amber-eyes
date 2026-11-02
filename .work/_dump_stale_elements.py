#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DUMP: moi phan tu chua khop giua plan JA (25/10) va loi noi that (31/10).

Cho: shot · beat JA cu · beat VN · cau noi JA moi · cau VN · trich dan cu · cau noi moi.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
n = lambda t: re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t or "")

pay = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json").read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}
shots = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))["shots"]

# cau VN tu script_tap02.json (cho doi chieu)
vn = {}
try:
    sc = json.loads((W / "script_tap02.json").read_text(encoding="utf-8-sig"))
    for turn in sc:
        for s in turn.get("sentences", []):
            vn[s["id"]] = s["text"]
except Exception as e:
    print("KHONG DOC DUOC script VN:", e)

# beat VN tu plan VN
vn_plan = (ROOT / "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md").read_text(encoding="utf-8-sig").splitlines()
i0 = next(i for i, l in enumerate(vn_plan) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_plan) if i > i0 and l.startswith("**Tổng:"))
vnbeat = {}
for l in vn_plan[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if m:
        c = l.strip().strip("|").split("|")
        vnbeat[m.group(1)] = re.findall(r'ở "([^"]+)"', c[6])

print("=" * 100)
print("A. BEAT CU KHONG NẰM TRONG CÂU NÓI MỚI")
for s in shots:
    spoken = " ".join(pm[i]["display"] for i in s["sentences"] if i in pm)
    for b in s.get("beats") or []:
        if n(b) and n(b) not in n(spoken):
            vnb = vnbeat.get(s["id"], [])
            print(f"\n  SHOT {s['id']}  (cau: {s['sentences']})")
            print(f"    beat JA CU : {b!r}")
            print(f"    beat VN    : {vnb}")
            print(f"    NOI MOI    : {spoken[:200]}")

print("\n" + "=" * 100)
print("B. TRICH DAN CU KHONG NGUYEN VAN TRONG CAU NOI MOI")
for s in shots:
    spoken = " ".join(pm[i]["display"] for i in s["sentences"] if i in pm)
    for seg in s["segments"]:
        for k, v in seg["elems"]:
            if k == "quote" and n(v.strip("“”\"'")) not in n(spoken):
                print(f"\n  SHOT {s['id']}  (cau: {s['sentences']})")
                print(f"    trich CU   : {v!r}")
                print(f"    NOI MOI    : {spoken[:230]}")

print("\n" + "=" * 100)
print("C. BOLD CHUA TEN RIENG / CON SO (can doi chinh khi doi cau)")
PROPER = ["ジェシカ・ロイド", "Jessica Lloyd", "Nissan Pathfinder", "Pathfinder", "BMW",
          "Williams", "WILLIAMS", "LLOYD", "Lloyd", "COMEAU", "Trois-Rivières", "エリザベス",
          "Elizabeth", "/elizabeth", "エ辽阔"]
for s in shots:
    spoken = " ".join(pm[i]["display"] for i in s["sentences"] if i in pm)
    for seg in s["segments"]:
        for k, v in seg["elems"]:
            if k != "bold":
                continue
            for pn in PROPER:
                if pn in v and pn not in spoken:
                    print(f"  {s['id']}: bold {v[:50]!r} chua {pn!r} · noi moi: {spoken[:110]}")
                    break
