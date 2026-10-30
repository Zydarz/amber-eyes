#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dựng bảng shot Tập 03 bản tiếng Anh từ bảng VN + shots_text_tap03_EN.json.

Sao yên bảng VN ở cột Câu, Vai, Mẫu, Nền, Nhân vật, chuyển cảnh;
chỉ thay:
  - cột Chữ -> tiếng Anh (chữ hiện trên màn hình)
  - cụm `ở "…"` trong cột Beat -> cụm tiếng Anh CÓ THẬT trong câu EN

Tự kiểm (trả về exit code khác 0 nếu lỗi):
  1. mọi shot trong bảng VN đều có bản EN
  2. cụm beat EN phải có thật trong câu EN của shot
  3. mọi con số trên hình phải truy được về câu EN (kể cả số viết bằng chữ,
     tên tháng, và nhãn thứ tự)
  4. trích dẫn trong ngoặc kép phải nguyên văn trong câu EN (lược bằng …)

python .work/_build_plan_tap03_en.py
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

en_table = json.loads((W / "shots_text_tap03_EN.json").read_text(encoding="utf-8"))
en_table = {k: v for k, v in en_table.items() if not k.startswith("_")}
script = json.loads((W / "script_tap03_EN.json").read_text(encoding="utf-8"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

vn_lines = (ROOT / "02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md").read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(vn_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(vn_lines) if i > i0 and l.startswith("**Tổng:"))

MONTHS = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
          "july": "7", "august": "8", "september": "9", "october": "10", "november": "11",
          "december": "12"}
NUMWORDS = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6",
            "seven": "7", "eight": "8", "nine": "9", "ten": "10", "eleven": "11", "twelve": "12",
            "twenty": "20", "thirty": "30", "forty": "40", "fifty": "50", "hundred": "100",
            "thousand": "1000"}
STRUCT = ("ACT", "STAGE", "LAYER", "CONCEPT", "RED FLAG", "FLAG", "EPISODE", "HỒI", "TẬP", "TẦNG", "DẤU HIỆU", "KHÁI NIỆM", "CASE FILE", "FILE")
ACT_TITLES_EN = {
    1: "Act 1 · The Midnight Call from a Colorado Payphone",
    2: "Act 2 · The Scene & Escalation — The Ladder of Substitution",
    3: "Act 3 · Psychological Autopsy — Inside the Mind of an Analytical Psychopath",
    4: "Act 4 · Conversations with the FBI — The Foundations of Criminal Profiling",
    5: "Act 5 · The Verdict, Behavioral Red Flags & Final Thoughts",
}


def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out


errors = []
warnings = []
out_lines = []
used = set()

for l in vn_lines[i0:i1 + 1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        out_lines.append(l)
        continue
    sid = m.group(1)
    c = l.strip().strip("|").split("|")
    if sid not in en_table:
        if c[5].strip() != "—":
            errors.append(f"{sid}: thiếu bản EN")
        out_lines.append(l)
        continue
    used.add(sid)
    chu, phrases = en_table[sid][0], en_table[sid][1]
    override = en_table[sid][2] if len(en_table[sid]) > 2 else None
    ids = sents(c[1])
    ctx = " ".join(S.get(x, "") for x in ids)
    flat = ctx.replace(" ", "").lower()

    # --- beat: thay cụm `ở "…"` bằng cụm EN
    if override is not None:
        beat = override
    else:
        vn_ph = re.findall(r'ở "([^"]+)"', c[6])
        if len(vn_ph) != len(phrases):
            errors.append(f"{sid}: {len(vn_ph)} cụm beat VN ≠ {len(phrases)} cụm EN")
            beat = c[6]
        else:
            it = iter(phrases)
            beat = re.sub(r'ở "([^"]+)"', lambda _: 'ở "' + next(it) + '"', c[6])

    # --- kiểm cụm beat EN có thật trong câu EN (dòng không lời: giữ cue VN, không cần cụm EN)
    if ctx.strip():
        for p in re.findall(r'ở "([^"]+)"', beat):
            if p.lower() not in ctx.lower():
                errors.append(f"{sid}: cụm beat \"{p}\" không có trong câu EN")

    # --- kiểm trích dẫn nguyên văn
    for q in re.findall(r"“([^”]+)”", chu):
        for frag in [f.strip() for f in q.split("…") if f.strip()]:
            if frag not in ctx:
                errors.append(f"{sid}: trích dẫn “{frag[:45]}…” không nguyên văn trong câu EN")

    # --- kiểm số trên hình (bỏ marker câu `→ `#k`:` — đó là mốc, không phải số trên hình)
    screen = re.sub(r"→\s*`#\d+`:", " ", chu)
    allowed = set(re.findall(r"\d+", flat))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    for w, d in MONTHS.items():
        if w in flat:
            allowed.add(d)
            allowed.add(d.zfill(2))
    for w, d in NUMWORDS.items():
        if w in flat:
            allowed.add(d)
            allowed.add(d.zfill(2))
    act_en = ACT_TITLES_EN.get(int(sid.split("-")[0]), "")
    for tok in set(re.findall(r"\d[\d,.]*", screen)):
        t = tok.replace(",", "").replace(".", "")
        if tok in allowed or t in allowed or tok in flat or t in flat:
            continue
        if any(re.search(r"\b" + re.escape(st) + r"\s*" + re.escape(tok) + r"\b", screen, re.I) for st in STRUCT):
            continue
        # dòng chuyển hồi: số lấy từ tên hồi EN
        if not ctx.strip() and any(re.search(r"\b" + re.escape(t) + r"\b", v) for v in ACT_TITLES_EN.values()):
            continue
        errors.append(f"{sid}: số “{tok}” không truy được về câu EN")

    c[5] = " " + chu + " "
    c[6] = " " + beat.strip() + " "
    out_lines.append("|" + "|".join(c) + "|")

for k in en_table:
    if k not in used:
        errors.append(f"{k}: có bản EN nhưng không có dòng VN")

print("\n".join(errors) if errors else "OK", "· dòng EN", len(used))
if warnings:
    print("CANH:", "; ".join(warnings))
if errors:
    sys.exit(1)

# ---------------------------------------------------------------- ghi file kế hoạch EN
HEADER = """# PRODUCTION PLAN EPISODE 03 · ENGLISH EDITION · "THE IQ 145 GIANT" (PART B)

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A)  
**Script:** `01_KICH_BAN/Tap03/kichban_tap03_EN.md` · **Release Target:** `02_SAN_XUAT/Tap03_EN/xuat_ban/`  
**Fixed Text & Cards:** `02_SAN_XUAT/Tap03_EN/CHU_CO_DINH_EN.md`  

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap03/kichban_tap03_EN.md` — 55 elements · 220 sentences · 4,067 words |
| Cast (Voice Set A) | H: `English_CaptivatingStoryteller` · D: `Korean_ColdYoungMan` · C: `English_AssertiveQueen` · N1: `Vietnamese_kindhearted_girl` · N2: `English_captivating_female1` |
| Video Structure | 110 shots — 93 spoken shots + 17 pauses/transitions |
| Act Titles | Act 1: The Midnight Call from a Colorado Payphone · Act 2: The Scene & Escalation — The Ladder of Substitution · Act 3: Psychological Autopsy · Act 4: Conversations with the FBI · Act 5: The Verdict, Red Flags & Final Thoughts |

## B2. Visual Rules & Alignment
- V5: Real persons depicted strictly in silhouette / shadow.
- V9: Focus on psychological analysis; no gore or explicit violence.
- H3: Exact semantic match between spoken speech and background imagery.

<!--TABLE-->
"""

body = "\n".join(out_lines)
tail = "\n**Total: 110 shots — 93 spoken shots + 17 pauses / transitions**\n"
(ROOT / "02_SAN_XUAT/Tap03_EN/KeHoach_Video_Tap03_EN.md").write_text(HEADER + body + tail, encoding="utf-8")
print("da ghi 02_SAN_XUAT/Tap03_EN/KeHoach_Video_Tap03_EN.md")
sys.exit(0)
