# -*- coding: utf-8 -*-
"""G: TAP 02 — bien doi that cua code .py: quotes, ACT['alt'], vi_numbers, thau ngat, diem nghien."""
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_EP"] = "02"
WORK = Path(r"D:\TEST\Gax\Audi\.work")
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402
import tts_sentences as TS  # noqa: E402  (dung chinh ham vi_numbers cua du an)

man = json.loads((WORK / "tts_manifest_t02.json").read_text(encoding="utf-8"))
act = json.loads((WORK / "acting_tap02.json").read_text(encoding="utf-8"))

print("=== 1. ACT (acting_tap02.json): bao nhieu muc, bao nhieu co 'alt' (loi doc rieng) ===")
alts = {k: v for k, v in act.items() if not k.startswith("_") and len(v) > 3 and v[3]}
print(f"   tong muc ACT: {len([k for k in act if not k.startswith('_')])}   co 'alt': {len(alts)}")
for k, v in alts.items():
    print(f"   {k}: {v[3]!r}")
print()

print("=== 2. Cac bien doi tren MOT cau mau (1.05#1) ===")
it = next(x for x in man if x["id"] == "1.05#1")
print(f"   display (cau goc) : {it['display']!r}")
print(f"   text   (sau .py)  : {it['text']!r}")
print(f"   -> chi doi '46' thanh 'bốn mươi sáu' (vi_numbers) + bo dau ngoac kép")
print()

print("=== 3. Con chu so trong loi doc cua BAN TIENG VIET? ===")
left = [(x["id"], x["text"]) for x in man if re.search(r"\d", x["text"])]
print(f"   so con: {len(left)}")
for i in left[:5]:
    print("   ", i)
print()

print("=== 4. G1 — 3 cau con dau '...' trong loi doc (nghi vi pham) ===")
for x in man:
    if "..." in x["text"]:
        print(f"   {x['id']:8s} [{x['role']}] {x['text']}")
        print(f"   {'':8s} goc: {x['display']}")
        print(f"   {'':8s} co ACT alt? {'CO' if x['id'] in alts else 'KHONG'}")
print()

print("=== 5. G7 — con chu thich trong ngoac trong loi doc ===")
for x in man:
    if re.search(r"\([^)]*\)", x["text"]):
        print(f"   {x['id']:8s} [{x['role']}] {x['text']}")
        print(f"   {'':8s} co ACT alt? {'CO' if x['id'] in alts else 'KHONG'}")
print()

print("=== 6. Vi tri thau ngat <#x#> trong cau ===")
for x in man:
    for m in re.finditer(r"<#[\d.]+#>", x["text"]):
        a, b = max(0, m.start() - 30), m.end() + 30
        truoc = x["text"][max(0, m.start() - 12):m.start()].rstrip()
        print(f"   {x['id']:8s} tag={m.group(0):9s} ky tu lien truoc = ...{truoc[-12:]!r}")
print()

print("=== 7. So sanh voi audio da xuat: 3 cau co dau '...' co that trong file mp3 khong? ===")
for x in man:
    if "..." in x["text"] or re.search(r"\([^)]*\)", x["text"]):
        ma, k = x["id"].split("#")
        a, b = ma.split(".")
        f = WORK / "audio_s_t02" / f"s{a}_{b}_{int(k):02d}.mp3"
        print(f"   {x['id']:8s} file: {f.name:14s} ton tai: {f.exists()}"
              f"  dung thoi luong cua cau: {x.get('display','')[:0]}")
print()

print("=== 8. Kiem tra lai: cac bien doi ma .py ap dung cho BAN VN ===")
src = (WORK / "tts_sentences.py").read_text(encoding="utf-8")
for pat in ["TTS_FIX", "vi_numbers(text)", "pause_tags", "ACT[s", "CAST[role]"]:
    for m in re.finditer(re.escape(pat), src):
        line_no = src[:m.start()].count("\n") + 1
        line = src.splitlines()[line_no - 1].strip()
        print(f"   dòng {line_no:4d}: {line}")
print("   edition.py:1105 -> TTS_FIX = (EP.get('tts_fix', {}) if EN else {})  ==> BAN VN: TTS_FIX rong")
print(f"   TTS_FIX thuc te cua VN Tap 02 = {ED.TTS_FIX}")
