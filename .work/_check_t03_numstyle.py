#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — soi quy tắc "câu đọc viết số bằng CHỮ => hình cũng viết bằng CHỮ".

CHỈ xét chữ THỰC SỰ được vẽ lên hình = shots[*]["segments"][*]["elems"][*][1].
Không xét "beat_text" (đó là chỉ dẫn đặt nhịp, KHÔNG vẽ lên hình).

Cách chọn số: mỗi con số trên hình phải tìm được trong câu đọc của shot
(dạng số HOẶC dạng chữ). Nếu câu đọc dùng DẠNG CHỮ mà hình dùng DẠNG SỐ
=> vi phạm quy tắc kênh.

Tiếng Nhật bỏ qua: kịch bản JA viết số bằng chữ số (5年間/3つ/10回) ngay trong lời đọc.

Dùng:  py -3 .work/_check_t03_numstyle.py
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
]

# số viết bằng chữ -> giá trị. "năm" (VI) = NĂM (năm dương lịch) KHÔNG phải số 5.
WORD_NUM = {
    "vi": {"một": "1", "hai": "2", "ba": "3", "bốn": "4", "sáu": "6", "bảy": "7",
           "tám": "8", "chín": "9", "mười": "10"},
    "en": {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
           "six": "6", "seven": "7", "eight": "8", "nine": "9", "ten": "10",
           "twelve": "12", "twenty": "20", "thirty": "30", "fifty": "50",
           "hundred": "100", "thousand": "1000"},
}
# số trên hình có thể gắn nhãn cấu trúc (không so)
STRUCT = re.compile(r"(第\s*\d+\s*幕|HỒI\s*\d+|ACT\s*\d+|CASE FILE\s*\d+|TẬP\s*\d+|"
                    r"概念\s*\d+|兆候\s*\d+|RED FLAG\s*\d+|CONCEPT\s*\d+|LAYER\s*\d+)", re.I)


def norm(s):
    return re.sub(r"\s+", " ", s.replace("“", '"').replace("”", '"')
                  .replace("‘", "'").replace("’", "'")).strip()


def drawn(shot):
    out = []
    for seg in shot.get("segments") or []:
        for el in seg.get("elems") or []:
            if len(el) >= 2:
                out.append(str(el[1]))
    return " ".join(out)


def digits(s):
    # bỏ số nằm trong nhãn cấu trúc
    clean = STRUCT.sub(" ", s)
    return set(re.findall(r"\d[\d.,]*", clean))


def wordnums(lang, s):
    out = {}
    low = s.lower()
    for w, d in WORD_NUM.get(lang, {}).items():
        if re.search(r"\b" + re.escape(w) + r"\b", low):
            out.setdefault(d, w)
    return out


viol = []
for lang, tl_name, sh_name in LANGS:
    tl = json.loads((WORK / tl_name).read_text(encoding="utf-8"))
    sh = json.loads((WORK / sh_name).read_text(encoding="utf-8"))
    sent = {it["id"]: norm(it.get("text") or "") for it in tl["items"]}
    print("=" * 78)
    print(f"[{lang}]")
    for s in sh["shots"]:
        st = drawn(s)
        if not st.strip():
            continue
        sd = {d.replace(",", "") for d in digits(st)}
        if not sd:
            continue
        ids = s.get("sentences") or []
        body = norm(" ".join(sent.get(i, "") for i in ids))
        wn = wordnums(lang, body)
        hit = sorted(sd & set(wn))
        if hit:
            viol.append((lang, s["id"], hit, wn, st, body))
            print(f"  ⚠ {s['id']}: hình {hit} · câu đọc viết chữ "
                  f"{[wn[h] for h in hit]}")
            print(f"       HÌNH: {st[:190]}")
            print(f"       CÂU : {body[:190]}")
        else:
            print(f"  ✔ {s['id']}: số trên hình {sorted(sd)} — câu đọc cũng viết số")
print("=" * 78)
print(f"VI PHẠM quy tắc: {len(viol)} shot")
for lang, sid, hit, wn, st, body in viol:
    print(f"  [{lang}] {sid}  hình={hit}  câu={wn}")
sys.exit(0 if not viol else 1)
