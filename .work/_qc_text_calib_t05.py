#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Hieu chuan gate 5/6/7 (chu tren hinh) cho VN va EN Tap05.

Gate 5  : chu tieu de (bold/ital) lay tu cau dang doc
Gate 6  : chu so tren hinh phai co trong cau (so chu -> so)
Gate 7  : trich danh (quote) phai nguyen van

Chay: py -3 .work/_qc_text_calib_t05.py
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

PUNCT = re.compile(r"[^\w\s]", re.UNICODE)

EN_UNITS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
            "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
            "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
            "seventeen": 17, "eighteen": 18, "nineteen": 19}
EN_TENS = {"twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
           "seventy": 70, "eighty": 80, "ninety": 90}
EN_ORD = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6,
          "seventh": 7, "eighth": 8, "ninth": 9, "tenth": 10, "eleventh": 11,
          "twelfth": 12, "thirteenth": 13, "fourteenth": 14, "fifteenth": 15,
          "sixteenth": 16, "seventeenth": 17, "eighteenth": 18, "nineteenth": 19,
          "twentieth": 20, "thirtieth": 30, "fortieth": 40, "fiftieth": 50,
          "sixtieth": 60, "seventieth": 70, "eightieth": 80, "ninetieth": 90}


def en_words_to_digits(t):
    """'seventeen active years' -> '17 active years'; 'thirtieth' -> '30'."""
    t = t.lower()
    # ordinals
    for w, d in EN_ORD.items():
        t = re.sub(rf"\b{w}\b", str(d), t)
    # tens + unit: 'twenty one' -> 21
    def tens(m):
        a = EN_TENS[m.group(1)]
        b = EN_UNITS.get(m.group(2))
        return f" {a + (b or 0)} "
    t = re.sub(r"\b(twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)(?:[- ](one|two|three|four|five|six|seven|eight|nine))?\b",
               tens, t)
    for w, d in EN_UNITS.items():
        t = re.sub(rf"\b{w}\b", str(d), t)
    # '19th' -> '19'
    t = re.sub(r"\b(\d+)(?:st|nd|rd|th)\b", r"\1", t)
    return t


def norm(t, lang):
    t = t.replace("\u2019", "'").replace("\u2018", "'")
    t = t.replace("\u2014", " ").replace("\u2013", " ").replace("\u00b7", " ")
    t = t.replace("\u2026", " ")
    t = PUNCT.sub(" ", t.lower())
    t = re.sub(r"\s+", " ", t).strip()
    if lang == "en":
        t = en_words_to_digits(t)
        t = re.sub(r"\s+", " ", t).strip()
    return t


def frags(q):
    """Tach trich danh theo dau cham ellipsis -> cac doan phai dung."""
    return [f.strip() for f in re.split(r"\u2026|\.\.\.", q) if f.strip()]


def run(tag, timeline_file, shots_file, script_file, lang):
    tl = json.loads(pathlib.Path(timeline_file).read_text(encoding="utf-8"))
    sh = json.loads(pathlib.Path(shots_file).read_text(encoding="utf-8"))
    S = {it["id"]: it for it in tl["items"]}
    g5, g6, g7 = [], [], []
    n_seg = n_num = n_quote = 0
    for s in sh["shots"]:
        if not s["sentences"]:
            continue
        body_all = norm(" ".join(S[c]["text"] for c in s["sentences"]), lang)
        for seg in s["segments"]:
            at = seg.get("at_sentence")
            if at is not None and 1 <= at <= len(s["sentences"]):
                body = norm(S[s["sentences"][at - 1]]["text"], lang)
            else:
                body = body_all
            for style, txt in seg["elems"]:
                n_seg += 1
                t = norm(txt, lang)
                if style == "quote":
                    n_quote += 1
                    for fr in frags(txt):
                        if norm(fr, lang) not in body:
                            g7.append((s["id"], fr[:80]))
                else:
                    if t and t not in body:
                        g5.append((s["id"], style, txt[:70]))
                for tok in re.findall(r"\d+", txt):
                    n_num += 1
                    tokc = tok.lstrip("0") or "0"
                    if tok not in body and not re.search(r"(?<!\d)" + re.escape(tokc) + r"(?!\d)", body):
                        g6.append((s["id"], tok, txt[:60]))
    print(f"--- {tag} ---")
    print(f"  doan chu: {n_seg} · so: {n_num} · trich danh: {n_quote}")
    print(f"  gate5 (tieu de khong verbatim): {len(g5)}")
    print(f"  gate6 (so khong co trong cau):  {len(g6)}")
    for i, t, p in g6:
        print(f"      {i}: so '{t}' — '{p}'")
    print(f"  gate7 (trich danh khong verbatim): {len(g7)}")
    for i, q in g7:
        print(f"      {i}: '{q}'")
    print()
    return g5, g6, g7


print("===== Hieu chuan gate 5/6/7 — Tap05 VN vs EN =====\n")
v5, v6, v7 = run("VN Tap05", WORK / "timeline_s_t05.json", WORK / "shots_t05.json",
                 WORK / "script_tap05.json", "vi")
e5, e6, e7 = run("EN Tap05", WORK / "timeline_s_EN_t05.json", WORK / "shots_EN_t05.json",
                 WORK / "script_tap05_EN.json", "en")

print("===== So sanh =====")
print(f"gate5: VN {len(v5)} / EN {len(e5)}")
print(f"gate6: VN {len(v6)} / EN {len(e6)}")
print(f"gate7: VN {len(v7)} / EN {len(e7)}")
