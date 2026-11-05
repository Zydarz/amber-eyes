#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liệt kê ĐẦY ĐỦ lỗi số trên hình, theo đúng logic cổng QC (A9.2), kèm câu đọc.

    py -3 .work/_an_num_full.py en
"""
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
LANG = sys.argv[1] if len(sys.argv) > 1 else "en"
os.environ["AE_EP"] = "03"
os.environ["AE_LANG"] = LANG
sys.path.insert(0, str(ROOT / ".work"))
import edition as ED  # noqa: E402

TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))
SENT = {it["id"]: it for it in TL["items"]}
EN = LANG == "en"

ORDINAL = {"thứ nhất": "1", "thứ hai": "2", "thứ ba": "3", "thứ tư": "4"}
ORDINAL_EN = {"first": "1", "second": "2", "third": "3", "fourth": "4"}
ORD_EN_RE = [(r"red flag number one\b", "1"), (r"red flag number two\b", "2"),
             (r"red flag number three\b", "3"), (r"red flag number four\b", "4"),
             (r"\bfirst\b", "1"), (r"\bsecond\b", "2"), (r"\bthird\b", "3"), (r"\bfourth\b", "4")]
MONTHS_EN = {"january": "1", "february": "2", "march": "3", "april": "4", "may": "5", "june": "6",
             "july": "7", "august": "8", "september": "9", "october": "10", "november": "11",
             "december": "12"}
STRUCT_EN = r"(ACT|STAGE|LAYER|COMPARTMENT|EPISODE)"
STRUCT_VN = r"(HỒI|TẬP|NẤC|TẦNG)"
STRUCT_JA = r"(第\s*\d+\s*幕|ACT|STAGE|LAYER|COMPARTMENT|EPISODE)"


def ctx_of(s):
    ids = s["sentences"]
    ctx = " ".join(SENT[x]["text"] for x in ids)
    if not ctx and s["template"] == "T10":
        ctx = " ".join(ED.EP["act_titles"].values())
    return ctx


def on_screen(s):
    out = []
    for seg in s["segments"]:
        for kind, t in seg["elems"]:
            out.append((kind, t))
    return out


print(f"===== TAP 03 {LANG.upper()} — lỗi số trên hình (A9.2) =====")
total = 0
for s in SH["shots"]:
    ctx = ctx_of(s)
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
            allowed |= {"4", "04"}
    struct = STRUCT_JA if LANG == "ja" else (STRUCT_EN if EN else STRUCT_VN)
    hits = []
    for m in set(re.findall(r"\d[\d.,]*", " ".join(t for _k, t in on_screen(s)))):
        tok = m.replace(".", "")
        if m in allowed or m in flat or tok in allowed:
            continue
        if re.search(struct + r"\s*" + re.escape(m) + r"\b", " ".join(t for _k, t in on_screen(s))):
            continue
        hits.append(m)
    if hits:
        total += len(hits)
        print(f"\n{s['id']}  ({s['template']})  số lỗi: {hits}")
        print(f"   câu đọc:")
        for x in s["sentences"]:
            print(f"     {x} :: {SENT[x]['text']}")
        print(f"   chữ trên hình:")
        for kind, t in on_screen(s):
            mark = "  <<<" if any(h in t for h in hits) else ""
            print(f"     [{kind}] {t}{mark}")
print(f"\nTỔNG: {total} lỗi số")
