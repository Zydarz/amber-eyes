#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — remap cấu hình theo shot ID trong edition.py (shot ID đã đánh số lại).

Các khóa cấu hình theo shot ID của tập 04:
  text_scrim, combo, inset, bg2, route_pins, flag_hold_shots
Remap: mọi shot MỚI sinh ra từ shot CŨ (kể cả các dòng tách) đều nhận cùng giá trị.

Dùng:  py -3 .work/_remap_edition_t04.py [--apply]
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
APPLY = "--apply" in sys.argv

ED = W / "edition.py"
sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))

# shot cũ -> các shot mới sinh ra từ nó
from_old = {}
for r in sk["rows"]:
    from_old.setdefault(r["from"], []).append(r["sid"])

text = ED.read_text(encoding="utf-8")
# khoanh vùng khối EPISODES["04"]
i = text.index('    "04": {')
j = text.index('\n    "05": {', i)
block = text[i:j]

OLD_SCRIM = ["1-06", "1-10", "1-15", "1-17", "2-08", "4-03", "4-07", "4-13"]
new_scrim = []
for o in OLD_SCRIM:
    new_scrim += from_old.get(o, [])
print("text_scrim cũ:", OLD_SCRIM)
print("text_scrim mới:", new_scrim)

m = re.search(r'"text_scrim":\s*\[[^\]]*\]', block)
print("hiện tại trong edition.py:", m.group(0) if m else "(không có)")
if m and APPLY:
    rep = '"text_scrim": ' + json.dumps(new_scrim, ensure_ascii=False)
    block2 = block[:m.start()] + rep + block[m.end():]
    text = text[:i] + block2 + text[j:]
    ED.write_text(text, encoding="utf-8", newline="\n")
    print("→ đã ghi edition.py")
else:
    print("→ chưa ghi (thêm --apply để ghi)")
