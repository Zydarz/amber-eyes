#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""(1) Audio da cai = audio Higgs PROD? (2) Phan loai lech: so/chu hay khac tu?"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# ---------- (1) audio da cai ----------
prod = W / "kaggle_higgs/out_higgs_prod_JA_t02/out_higgs_prod_JA_t02"
inst = W / "audio_s_higgs_JA_t02"
print("=== (1) AUDIO DA CAI vs PROD ===")
if prod.exists():
    pf = sorted(p for p in prod.rglob("*.mp3"))
    print(f"  prod: {len(pf)} file mp3 · cai: {len(list(inst.glob('*.mp3'))) if inst.exists() else 0}")
    man = json.loads((prod / "higgs_manifest.json").read_text(encoding="utf-8-sig"))
    rows = [r for r in man if isinstance(r, dict) and r.get("id")]
    print(f"  manifest rows: {len(rows)}")
    r0 = [r for r in rows if r.get("id") == "3.08#10"]
    if r0:
        r = r0[0]
        print(f"  3.08#10 file = {r.get('file')}")
        for cand in list(prod.rglob(r.get("file", "x"))) + [inst / r.get("file", "x")]:
            if cand.exists():
                print(f"     {cand.relative_to(ROOT)}  {cand.stat().st_size} byte")
else:
    print("  KHONG CO thu muc prod")

# ---------- (2) phan loai lech ----------
KANJI = {"〇": "0", "一": "1", "二": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7",
         "八": "8", "九": "9", "十": "10", "百": "100", "千": "1000", "万": "10000"}


def to_digits(t):
    """doi so kanji -> arabic de so sanh nghia."""
    t = t.replace("〇", "0")
    for k, v in sorted(KANJI.items(), key=lambda x: -len(x[0])):
        t = t.replace(k, v)
    # '二千九年' -> '2009' : don gian: gom cac so lai
    def rep(m):
        return str(sum(int(c) * 10 ** i for i, c in enumerate(reversed(m.group(0)), )))
    t = re.sub(r"[0-9]{2,}", lambda m: m.group(0), t)
    return t


def canon(t):
    t = to_digits(t or "")
    t = re.sub(r"[\s　、。・,.:：;；!！?？\"'“”‘’「」『』()（）\-—–…]", "", t)
    # bo khoang trang latin: 'Jessica Lloyd' vs 'ジェシ atroyd'
    t = re.sub(r"[A-Za-z]+", "", t)
    return t


tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it["text"] for it in tl["items"]}
pay = json.loads((W / "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json").read_text(encoding="utf-8-sig"))
pm = {r["id"]: r for r in pay["items"] if r.get("id")}

only_fmt, real_diff, missing = [], [], []
for i, cur in sent.items():
    p = pm.get(i)
    if not p:
        missing.append(i)
        continue
    disp = p.get("display", "")
    if canon(cur) == canon(disp):
        if cur != disp:
            only_fmt.append((i, cur, disp))
    else:
        real_diff.append((i, cur, disp))

print()
print("=== (2) PHAN LOAI LECH 203 CAU ===")
print(f"  giong het (chu thuong)        : {203 - len(only_fmt) - len(real_diff) - len(missing)}")
print(f"  khac CHI o so/chu cach (an toan): {len(only_fmt)}")
print(f"  khac TU THAT (can sua)          : {len(real_diff)}")
print(f"  thieu trong payload             : {len(missing)}")
print("\n  --- mau khac chu thuong (khong can sua) ---")
for i, a, b in only_fmt[:6]:
    print(f"    {i}\n      sub : {a[:88]}\n      noi : {b[:88]}")
print("\n  --- mau khac TU THAT ---")
for i, a, b in real_diff[:10]:
    print(f"    {i}\n      sub : {a[:88]}\n      noi : {b[:88]}")
