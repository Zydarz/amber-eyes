# -*- coding: utf-8 -*-
import json
from pathlib import Path

with open(".work/timeline_s_t06.json", encoding="utf-8") as f:
    tl = json.load(f)

with open(".work/shots_t06.json", encoding="utf-8") as f:
    sh = json.load(f)

sent_map = {it["id"]: it for it in tl["items"]}

lines = ["=== PHÂN TÍCH CHI TIẾT TỪNG SHOT TẬP 06 ==="]

for s in sh["shots"]:
    sid = s["id"]
    bg = s["bg"]
    sents = s.get("sentences", [])
    if not sents:
        continue
    
    # Text hiển thị
    segs = s.get("segments", [])
    display_words = []
    for seg in segs:
        for el in seg.get("elems", []):
            if len(el) > 1:
                display_words.append(el[1])
    display_str = " · ".join(display_words)
    
    lines.append(f"\n[{sid}] BG: {bg}")
    lines.append(f"  TIÊU ĐỀ: {display_str}")
    for sc in sents:
        if sc in sent_map:
            lines.append(f"  - ({sc}): {sent_map[sc]['text']}")

Path(".work/_all_shots_detail.txt").write_text("\n".join(lines), encoding="utf-8")
print("SUCCESS: written in UTF-8!")
