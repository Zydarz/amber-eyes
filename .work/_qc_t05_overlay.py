#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — QC lớp phủ chữ trên hình, theo ĐÚNG quy tắc cổng dự án.

Áp dụng: _qc_tap02_shots.py (A9.2 số trên hình · V3 trích dẫn nguyên văn · V9 từ cấm)
Dùng:  py -3 .work/_qc_t05_overlay.py vi|en|ja
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

CFG = {
    "vi": ("01_KICH_BAN/Tap05/kichban_tap05_23102026.md", "_t05_chu_vi.json", False),
    "en": ("01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md", "_t05_chu_en.json", True),
    "ja": ("01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md", "_t05_chu_ja.json", True),
}
lang = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
kb_rel, ov_rel, EN = CFG[lang]

els = parse_file(str(ROOT / kb_rel))
idx = {e["id"]: {s["id"]: s["text"] for s in e.get("sentences", [])}
       for e in els if e["kind"] == "LOI"}
sk = json.loads((W / "_t05_skeleton.json").read_text(encoding="utf-8"))
ov = json.loads((W / ov_rel).read_text(encoding="utf-8"))

ORDINAL = {"thứ nhất": "1", "thứ hai": "2", "thứ ba": "3", "thứ tư": "4"}
ORDINAL_EN = {"first": "1", "second": "2", "third": "3", "fourth": "4"}
ORD_EN_RE = [(r"red flag number one\b", "1"), (r"red flag number two\b", "2"),
             (r"red flag number three\b", "3"), (r"red flag number four\b", "4"),
             (r"\bfirst\b", "1"), (r"\bsecond\b", "2"), (r"\bthird\b", "3"), (r"\bfourth\b", "4")]
LADDER_LAST = {"cuối cùng": "4"}
MONTHS_EN = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
             "july": "7", "august": "8", "september": "9", "october": "10", "november": "11",
             "december": "12"}
STRUCT_VN = r"(HỒI|TẬP|NẤC|TẦNG)"
STRUCT_EN = r"(ACT|STAGE|LAYER|COMPARTMENT|EPISODE|CASE\s+FILE)"
STRUCT_JA = r"(第\s*\d+\s*幕)"
STRUCT_ANY = r"(?:" + STRUCT_VN + "|" + STRUCT_EN + "|" + STRUCT_JA + ")"
FORBIDDEN = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập", "đầu độc",
             "diệt cỏ", "bỏ đói", "móc áo", "đồ lót", "quan hệ tình dục", "hiếp", "cưỡng ép"]
SAFE = ["ung thư máu", "đấu tập", "bàn tay", "cánh tay", "đầu tư", "đầu học", "đầu tiên",
        "đầu não", "trọng đầu", "bầu cửa", "trời xanh", "đập đầu", "trói buộc"]
FORBIDDEN_EN = ["blood", "corpse", "strangle", "choke", "struggle", "raped", "rape",
                "underwear", "sexual intercourse", "orgasm", "penis", "vagina", "suffocat",
                "mutilat", "dismember", "torture"]
SAFE_EN = ["blood type", "blood pressure", "blood vessel", "bloodstream", "blood cell",
           "struggle to survive", "struggled to"]


def segs_of(cell):
    out = []
    cell = re.sub(r"\*\*.+?\*\*|\*[^*]+?\*|“.+?”",
                  lambda m: m.group(0).replace("→", "⟶"), cell)
    for raw in re.split(r"\s+→\s+", cell):
        raw = raw.replace("⟶", "→")
        for tok in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", raw):
            if tok.group(1):
                out.append(("bold", tok.group(1)))
            elif tok.group(2):
                out.append(("ital", tok.group(2)))
            else:
                out.append(("quote", tok.group(3)))
    return out


errs, warns = [], []
shots = [r for r in sk["rows"] if r["kind"] == "shot"]
covered = set()
for r in shots:
    sid = r["sid"]
    if sid not in ov:
        errs.append(f"{sid}: THIẾU chữ trong overlay")
        continue
    covered.add(sid)
    ctx = " ".join(idx[eid][f"{eid}#{k}"] for eid, a, b in r["spans"] for k in range(a, b + 1))
    elems = segs_of(ov[sid])
    if not elems:
        errs.append(f"{sid}: ô \"Chữ\" rỗng / không parse được")
    # --- V3: trích dẫn nguyên văn
    for kind, t in elems:
        if kind != "quote":
            continue
        core = t.strip().strip("“”\"")
        for frag in [x.strip() for x in core.split("…") if x.strip()]:
            if frag not in ctx:
                errs.append(f"{sid}: trích dẫn KHÔNG NGUYÊN VĂN: “{frag[:55]}”")
    # --- A9.2: số trên hình
    flat = ctx.replace(" ", "")
    allowed = set(re.findall(r"\d+", flat))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    for word, d in (ORDINAL_EN if EN else ORDINAL).items():
        if word in ctx.lower():
            allowed.add(d)
            allowed.add(d.zfill(2))
    if EN:
        for pat, d in ORD_EN_RE:
            if re.search(pat, ctx.lower()):
                allowed.add(d)
                allowed.add(d.zfill(2))
        for word, d in MONTHS_EN.items():
            if word in ctx.lower():
                allowed.add(d)
                allowed.add(d.zfill(2))
        if "4 stages" in ctx.lower():
            allowed.add("4")
            allowed.add("04")
    else:
        for word, d in LADDER_LAST.items():
            if word in ctx.lower() and "4 nấc" in ctx.lower():
                allowed.add(d)
                allowed.add(d.zfill(2))
    screen = " ".join(t for _k, t in elems)
    for m in set(re.findall(r"\d[\d.,]*", screen)):
        tok = m.replace(".", "")
        if m in allowed or m in flat or tok in allowed:
            continue
        if re.search(r"第\s*" + re.escape(m) + r"\s*[幕話]", screen):
            continue
        if re.search(STRUCT_ANY + r"\s*" + re.escape(m) + r"\b", screen):
            continue
        errs.append(f"{sid}: số “{m}” không có trong câu")
    # --- V9: từ cấm
    low = screen.lower()
    for w in (FORBIDDEN_EN if EN else FORBIDDEN):
        if not re.search(r"(?<!\w)" + r"\s+".join(re.escape(x) for x in w.split()) + r"(?!\w)", low):
            continue
        if EN:
            if any(g in low for g in SAFE_EN if g in w or w in g):
                continue
        elif not any(g in low for g in SAFE if g in w or w in g):
            errs.append(f"{sid}: từ cấm “{w}”")

extra = sorted(set(ov) - covered)
if extra:
    warns.append(f"overlay có ID không thuộc shot nào: {extra}")
miss = sorted(s["sid"] for s in shots if s["sid"] not in ov)
print(f"=== QC overlay [{lang}] ===")
print(f"  shot: {len(shots)} · có chữ: {len(covered)} · thiếu: {len(miss)}")
if miss:
    print("  THIẾU:", miss)
if errs:
    print(f"  LỖI ({len(errs)}):")
    for e in errs:
        print("    ", e)
else:
    print("  ✔ không lỗi")
for w in warns:
    print("  ⚠", w)
