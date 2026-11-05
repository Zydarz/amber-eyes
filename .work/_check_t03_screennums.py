#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — so CHỮ TRÊN HÌNH với câu đọc của shot (3 ngôn ngữ).

Chữ trên hình nằm ở shots[*]["segments"][*]["elems"] = [[style, text], ...]
(đã kiểm: không có khoá "text" ở cấp shot).

Quy tắc kênh (báo cáo Tập 02, shot 5-09):
  "câu đọc viết số bằng chữ  ⇒  chữ trên hình cũng viết bằng chữ"
V3/A9.2: mọi SỐ trên hình phải truy được về câu đọc của shot.

Script này in ra:
  - shot nào có số trên hình
  - số đó có trong câu đọc không (dạng số HOẶC dạng chữ)
  - cảnh báo khi câu đọc viết số bằng CHỮ còn hình viết bằng SỐ (quy tắc kênh)

Dùng:  py -3 .work/_check_t03_screennums.py
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

LANGS = [
    ("vi", "timeline_s_t03.json", "shots_t03.json"),
    ("en", "timeline_s_EN_t03.json", "shots_EN_t03.json"),
    ("ja", "timeline_s_JA_t03.json", "shots_JA_t03.json"),
]

# số viết bằng chữ -> giá trị (mỗi ngôn ngữ một bộ)
WORD_NUM = {
    "vi": {"một": "1", "hai": "2", "ba": "3", "bốn": "4", "năm": "5", "sáu": "6",
           "bảy": "7", "tám": "8", "chín": "9", "mười": "10", "chục": "10"},
    "en": {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
           "seven": "7", "eight": "8", "nine": "9", "ten": "10", "twelve": "12",
           "twenty": "20", "thirty": "30", "fifty": "50", "hundred": "100",
           "thousand": "1000"},
    "ja": {},
}


def norm(s):
    return re.sub(r"\s+", " ", s.replace("“", '"').replace("”", '"')
                  .replace("‘", "'").replace("’", "'")).strip()


def screen_text(shot):
    """Toàn bộ chữ trên hình của shot (gộp mọi segment + beat_text)."""
    out = []
    for seg in shot.get("segments") or []:
        for el in seg.get("elems") or []:
            if len(el) >= 2:
                out.append(str(el[1]))
    bt = (shot.get("beat_text") or "").strip()
    if bt and bt != "—":
        out.append(bt)
    return " ".join(out)


def digits(s):
    return set(re.findall(r"\d[\d.,]*", s))


def words(lang, s):
    out = set()
    low = s.lower()
    for w, d in WORD_NUM.get(lang, {}).items():
        if re.search(r"\b" + re.escape(w) + r"\b", low):
            out.add(d)
    return out


bad_missing = []
bad_style = []
for lang, tl_name, sh_name in LANGS:
    tl = json.loads((WORK / tl_name).read_text(encoding="utf-8"))
    sh = json.loads((WORK / sh_name).read_text(encoding="utf-8"))
    sent = {it["id"]: norm(it.get("text") or "") for it in tl["items"]}
    print("=" * 78)
    print(f"[{lang}]")
    n_with = 0
    for s in sh["shots"]:
        st = screen_text(s)
        sd = digits(st)
        if not sd:
            continue
        n_with += 1
        ids = s.get("sentences") or []
        body = norm(" ".join(sent.get(i, "") for i in ids))
        body_d = {d.replace(",", "") for d in digits(body)}
        body_w = words(lang, body)
        miss = {n for n in sd if n.replace(",", "") not in body_d and n not in body_w}
        # quy tắc kênh: câu đọc viết số bằng CHỮ mà hình viết bằng SỐ
        style = sorted({n for n in sd if n.replace(",", "") in body_w})
        tag = ""
        if miss:
            bad_missing.append((lang, s["id"], sorted(miss), st[:90], body[:90]))
            tag = "  ✗ SỐ KHÔNG CÓ TRONG CÂU"
        elif style:
            bad_style.append((lang, s["id"], style, st[:90], body[:90]))
            tag = "  ⚠ câu đọc viết BẰNG CHỮ, hình viết bằng SỐ"
        print(f"  {s['id']}: số trên hình {sorted(sd)}{tag}")
    print(f"  -> {n_with} shot có số trên hình")

print("=" * 78)
print(f"A. Số trên hình KHÔNG truy được về câu đọc: {len(bad_missing)}")
for lang, sid, miss, st, body in bad_missing:
    print(f"   [{lang}] {sid} thiếu {miss}\n      hình: {st}\n      câu : {body}")
print(f"B. Câu đọc viết số BẰNG CHỮ, hình viết bằng SỐ (quy tắc kênh): {len(bad_style)}")
for lang, sid, stl, st, body in bad_style:
    print(f"   [{lang}] {sid} {stl}\n      hình: {st}\n      câu : {body}")
sys.exit(0 if not bad_missing and not bad_style else 1)
