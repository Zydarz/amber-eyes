#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quet TOAN BO 151 shot: phan tu chu tren hinh (chu/italic/quote) co stale so voi loi noi moi khong?

Tieu chi:
  - quote      : phai nguyen van trong cau noi (V3)      -> BAT BUOC sua
  - beat       : phai la cum co that trong cau noi        -> BAT BUOC sua (la moc thoi gian)
  - so (chu)   : phai truy duoc ve cau noi hoac nhan hop  -> BAT BUOC sua
  - ten rieng  : chu hoa chu thuong phai co trong cau noi   -> nen sua
  - italic     : ngan han, doi chieu thu cong              -> thong bao
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

TXT = json.loads((W / "shots_text_tap02_JA.json").read_text(encoding="utf-8-sig"))
TXT = {k: v for k, v in TXT.items() if not k.startswith("_")}

CAT = {
    "quote": [],
    "beat": [],
    "num": [],
    "name": [],
    "ital": [],
}
for s in shots:
    sid = s["id"]
    spoken = " ".join(pm[i]["display"] for i in s["sentences"] if i in pm)
    ns = n(spoken)
    entry = TXT.get(sid)
    if not entry:
        continue
    chu, beats = entry[0], entry[1]
    # quote
    for q in re.findall(r"“([^”]+)”", chu):
        for frag in [f.strip() for f in q.split("…") if f.strip()]:
            if n(frag) not in ns:
                CAT["quote"].append((sid, frag))
    # beat
    for b in beats or []:
        if n(b) and n(b) not in ns:
            CAT["beat"].append((sid, b))
    # so + ten rieng trong chu
    screen = re.sub(r"→\s*`#\d+`:", " ", chu)
    for tok in set(re.findall(r"\d[\d,.]*", screen)):
        t = tok.replace(",", "").replace(".", "")
        if tok in spoken or t in spoken:
            continue
        if re.search(r"[第幕段階弾]\s*" + re.escape(tok), screen) or re.search(re.escape(tok) + r"\s*[幕段階弾件人話話者目击話者目撃者]", screen):
            continue
        if re.search(r"第\d+話", screen) or re.search(r"第\d+幕", screen):
            continue
        CAT["num"].append((sid, tok, screen[:60]))
    for m in re.finditer(r"[A-Z][A-Za-zÀ-ɏ]{2,}(?:\s+[A-Z][A-Za-zÀ-ɏ]{2,})*", screen):
        nm = m.group(0)
        if nm.lower() in spoken.lower():
            continue
        if nm in ("Malignant", "Narcissism", "God", "Complex", "Signature", "Russell", "Williams"):
            if nm.lower() in spoken.lower():
                continue
        CAT["name"].append((sid, nm, screen[:70]))
    # italic
    for it in re.findall(r"\*([^*]+)\*", screen):
        if it.strip() and n(it) not in ns:
            CAT["ital"].append((sid, it.strip()))

for k, label in [("quote", "TRICH DAN (bat buoc nguyen van)"),
                 ("beat", "BEAT (moc thoi gian - bat buoc co that)"),
                 ("num", "SO TREN HINH (bat buoc truy duoc)"),
                 ("name", "TEN RIENG (nen sua)"),
                 ("ital", "ITALIC (ngan han - thong bao)")]:
    print("=" * 90)
    print(f"{label}: {len(CAT[k])}")
    for x in CAT[k]:
        print(f"   {x[0]:<7} {x[1][:46]!r}" + (f"   | {x[2][:44]!r}" if len(x) > 2 else ""))

print("=" * 90)
print("TONG:", {k: len(v) for k, v in CAT.items()})
