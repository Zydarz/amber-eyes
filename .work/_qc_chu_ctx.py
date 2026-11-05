#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""In ngữ cảnh câu cho từng lỗi QC chữ để sửa nhanh."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

W = ROOT / ".work"
LANG = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
KB = {"vi": "01_KICH_BAN/Tap04/kichban_tap04_23102026.md",
      "en": "01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md",
      "ja": "01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md"}[LANG]
idx = {}
for el in parse_file(str(ROOT / KB)):
    if el["kind"] == "LOI":
        idx[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]
sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
CHU = json.loads((W / f"_t04_chu_{LANG}.json").read_text(encoding="utf-8"))


def norm(s):
    s = s.lower().replace("“", '"').replace("”", '"')
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


def contains(frag, ctx):
    fw, cw = norm(frag).split(), norm(ctx).split()
    for i in range(len(cw) - len(fw) + 1):
        if cw[i:i + len(fw)] == fw:
            return True
    return False


for r in sk["rows"]:
    if r["kind"] != "shot":
        continue
    sid = r["sid"]
    chu = CHU.get(sid, "")
    eid, a, b = r["spans"][0]
    sents = idx[eid]
    cur = a
    for part in re.split(r"\s+→\s+", chu):
        m = re.match(r"(?:ở\s+)?`#(\d+)`:?\s*(.*)", part, re.S)
        if m:
            cur = max(cur, int(m.group(1)))
            part = m.group(2)
        ctx = " ".join(t for _, t in sents[cur - 1:b])
        for g in re.findall(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", part):
            txt = g[0] or g[1] or g[2]
            if not contains(txt, ctx):
                print(f"--- {sid} [{eid} #{cur}-{b}]  «{txt}»")
                for i in range(cur, b + 1):
                    print(f"      #{i}: {sents[i - 1][1]}")
