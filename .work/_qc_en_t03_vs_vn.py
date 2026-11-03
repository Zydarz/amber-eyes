#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Soi 110 shot EN voi 110 shot VN: chu tren hinh co gia y (bo sung) so voi ban VN?

Neu EN them chi tiet ma loi thoai EN khong co -> phai canh bao (H6).
Bao cao ca 2 chieu:
  - phan COT CHU cua plan EN (shots_text_tap03_EN.json) so voi plan VN
  - phan segments that render ra (shots_EN_t03.json vs shots_t03.json)
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"


def elems(shot):
    return [(str(el[0]), str(el[1]))
            for sg in (shot.get("segments") or []) for el in (sg.get("elems") or [])]


en = {s["id"]: s for s in json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["shots"]}
vn = {s["id"]: s for s in json.loads((W / "shots_t03.json").read_text(encoding="utf-8"))["shots"]}
sc = json.loads((W / "script_tap03_EN.json").read_text(encoding="utf-8"))
S = {}
for e in sc:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

# ngu canh hieu dung cho shot EN (ke thua cho shot giu)
eff, prev = [], []
for sid in sorted(en):
    s = en[sid]
    if s.get("sentences"):
        prev = s["sentences"]
    eff.append((sid, prev))

print(f"{'shot':7} {'VN elems':9} {'EN elems':9}  EN-rieng-chua-co-trong-VN")
print("-" * 100)
enrich = []
for sid, ctxids in eff:
    e = en[sid]
    v = vn.get(sid)
    ne = elems(e)
    nv = elems(v) if v else []
    ctx = " ".join(S.get(x, "") for x in ctxids)
    # cac cum tieng anh chi co o EN, khong co o VN
    en_only = []
    for _, t in ne:
        if not any(t == tv or t.lower() == tv.lower() for _, tv in nv):
            en_only.append(t)
    if en_only:
        enrich.append((sid, ne, nv, en_only, ctx))
        print(f"{sid:7} {len(nv):9} {len(ne):9}  {en_only}")

print("\n" + "=" * 100)
print(f"Tong shot EN khac pham vi so voi VN: {len(enrich)} / {len(en)}")

# ---- phan 'bo sung chi tiet' : cum EN co chua (tinh) ma cau EN khong co ----
EXTRA = re.compile(r"[a-z]{3,}")
STOP = set("""the a an and or of to in on at for with from by as is was were be been being that this
those these it its his her their they he she we you i not no so but if then than when while
into over under about after before near around there here all any each every one two three
four five six seven eight nine ten days years year ago later early just only very more most
much many other another such own same never always often sometimes usually again once
because since until though although however rather quite really yet still even
""".split())


def kws(t):
    return {w for w in EXTRA.findall(t.lower()) if w not in STOP}


print("\n--- Cum EN co chi tiet ma cau EN khong he noi (ung vien H6) ---")
flag = []
for sid, ne, nv, en_only, ctx in enrich:
    ck = kws(ctx)
    for t in en_only:
        miss = sorted(k for k in kws(t) if k not in ck)
        if len(miss) >= 1:
            flag.append((sid, miss, t, ctx[:100]))
            print(f"  {sid}: thieu {miss}")
            print(f"       chu : {t}")
            print(f"       loi : {ctx[:160]}")
print(f"\nTong cum bi nghi: {len(flag)}")
