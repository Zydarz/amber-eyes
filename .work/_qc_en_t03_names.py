#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soi danh tu rieng (proper noun) tren hinh khong co trong loi thoai.

H6 noi "cau trich phai nguyen van" — nhung mot ten rieng / nhan hieu / so lieu
khong xuat hien trong cau doc cung la loai "khong co nguon" (chi co the lo
neu validator quet ca dau nhay ASCII). Lop nay quet rieng:
  - tu viet hoa giua cau (ten rieng) khong co trong ngu canh
  - so + don vi (IQ 145, 0.13%, 6-foot-9) khong co trong ngu canh
  - nhan trong ngoac kép khong co trong ngu canh
  - so la (mười hai...) khong co trong ngu canh
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

shots = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["shots"]
script = json.loads((W / "script_tap03_EN.json").read_text(encoding="utf-8"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

EFF, prev = [], []
for s in shots:
    if s.get("sentences"):
        prev = s["sentences"]
    EFF.append(prev)


def elems(shot):
    return [(str(el[0]), str(el[1]))
            for sg in (shot.get("segments") or []) for el in (sg.get("elems") or [])]


# ---- tu viet hoa giua cau (ten rieng) -------------------------------------
COMMON_CAP = set("""The A An And But For From His Her Its Their This That These Those Was Were
He She They We You It In On At Of To With For Not No All Any Each Every One Two Three Four
Five Six Seven Eight Nine Ten Twenty Thirty Forty Fifty Hundred I Am As By But From If
Her His Its Our Out So Than Then There These They Up Us We When Where Which Who Will With
""".split())

name_err = []
for s, eff in zip(shots, EFF):
    ctx = " ".join(S.get(x, "") for x in eff)
    ctx_low = ctx.lower()
    for kind, txt in elems(s):
        # bo qua chu in dau tien cua moi dong (tieu de)
        words = re.findall(r"[A-Za-z][A-Za-z'\-\.]*", txt)
        caps = [w for w in words if w[:1].isupper() and w.lower() not in COMMON_CAP]
        for w in caps:
            bare = w.strip(".,'\"")
            if len(bare) < 3:
                continue
            if bare.lower() in ctx_low:
                continue
            # so thuong dung: IQ 145, 0.13%, 6-foot-9 -> tach phan chu
            if re.fullmatch(r"\d[\d,\.]*", bare):
                continue
            name_err.append((s["id"], bare, txt[:80], ctx[:90]))
print(f"1. Tu viet hoa / nhan hieu tren hinh khong co trong loi: {len(name_err)}")
seen = set()
for e in name_err:
    k = (e[0], e[1])
    if k in seen:
        continue
    seen.add(k)
    print("   ", e)

# ---- so + don vi ---------------------------------------------------------
unit_err = []
for s, eff in zip(shots, EFF):
    ctx = " ".join(S.get(x, "") for x in eff)
    flat = ctx.replace(",", "").lower()
    for kind, txt in elems(s):
        for num, unit in re.findall(r"\b(\d[\d,\.]*)\s*([A-Za-z%\-]+)\b", txt):
            u = unit.lower().rstrip(".,")
            n = num.replace(",", "")
            if n in flat:
                continue
            # don vi la tu rieng -> dung so lieu rieng
            unit_err.append((s["id"], f"{num} {unit}", txt[:80], ctx[:90]))
print(f"\n2. So + don vi tren hinh khong co trong loi: {len(unit_err)}")
for e in unit_err[:20]:
    print("   ", e)

# ---- so la tieng anh -----------------------------------------------------
WORDS = ("zero one two three four five six seven eight nine ten eleven twelve thirteen "
         "fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty "
         "sixty seventy eighty ninety hundred thousand million billion").split()
numword_err = []
for s, eff in zip(shots, EFF):
    ctx = " ".join(S.get(x, "") for x in eff)
    ctx_low = ctx.lower()
    for kind, txt in elems(s):
        for w in re.findall(r"\b[A-Za-z]+\b", txt.lower()):
            if w in WORDS and w not in ctx_low:
                numword_err.append((s["id"], w, txt[:80], ctx[:90]))
print(f"\n3. So la tieng anh tren hinh khong co trong loi: {len(numword_err)}")
for e in numword_err[:20]:
    print("   ", e)

# ---- nhan trong ngoac kep -------------------------------------------------
q_err = []
for s, eff in zip(shots, EFF):
    ctx = " ".join(S.get(x, "") for x in eff)
    for kind, txt in elems(s):
        for q in re.findall(r"“([^”]+)”", txt) + re.findall(r'"([^"]+)"', txt):
            if q.strip() and q.strip() not in ctx:
                q_err.append((s["id"], q, txt[:90], ctx[:90]))
print(f"\n4. Nhan trong ngoac kep khong co trong loi: {len(q_err)}")
for e in q_err:
    print("   ", e)

total = len(name_err) + len(unit_err) + len(numword_err) + len(q_err)
print("\n" + "=" * 72)
print(f"TONG: {total} muc can xac nhan")
sys.exit(1 if q_err or unit_err or numword_err else 0)
