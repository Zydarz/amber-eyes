#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — kiểm tra parity mã câu giữa VN/EN/JA + dựng worklist 3 ngôn ngữ."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

KB = {
    "vi": "01_KICH_BAN/Tap05/kichban_tap05_23102026.md",
    "en": "01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md",
    "ja": "01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md",
}
ids = {}
txt = {}
for lang, kb in KB.items():
    els = parse_file(str(ROOT / kb))
    ids[lang] = {s["id"] for e in els if e.get("kind") == "LOI" for s in e.get("sentences", [])}
    txt[lang] = {s["id"]: s["text"] for e in els if e.get("kind") == "LOI" for s in e.get("sentences", [])}

print("parity mã câu:")
base = ids["vi"]
for lang in ("vi", "en", "ja"):
    same = ids[lang] == base
    print(f"  {lang}: {len(ids[lang])} câu · trùng khớp VN = {same}"
          + ("" if same else f" · chỉ có ở {lang}: {sorted(ids[lang]-base)[:6]}"))

# worklist 3 ngôn ngữ theo shot
sk = json.loads((W / "_t05_skeleton.json").read_text(encoding="utf-8"))
lines = []
for r in sk["rows"]:
    if r["kind"] != "shot":
        lines.append(f"### [META] {r['sid']} | Câu={r['cells'][1]} | Mẫu={r['cells'][3]} | "
                     f"Nền={r['cells'][4]} | CHỮ={r['cells'][5][:60]}")
        continue
    ids_row = [f"{eid}#{k}" for eid, a, b in r["spans"] for k in range(a, b + 1)]
    lines.append(f"### {r['sid']} | Vai={r['cells'][2]} | Mẫu={r['cells'][3]} | "
                 f"Nền={r['cells'][4]} | NV={r['cells'][7]}")
    lines.append(f"    CHỮ CŨ: {r['cells'][5]}")
    for tag, lang in (("VN", "vi"), ("EN", "en"), ("JA", "ja")):
        for sid in ids_row:
            lines.append(f"    {tag} {sid}: {txt[lang][sid]}")
    lines.append("")
open(W / "_t05_worklist3.txt", "w", encoding="utf-8", newline="\n").write("\n".join(lines))
print("worklist 3 ngôn ngữ -> .work/_t05_worklist3.txt")
