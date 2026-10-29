# -*- coding: utf-8 -*-
import json
from pathlib import Path

with open(".work/timeline_s_t06.json", encoding="utf-8") as f:
    tl = json.load(f)

with open(".work/shots_t06.json", encoding="utf-8") as f:
    sh = json.load(f)

sent_map = {it["id"]: it for it in tl["items"]}

shots_audit = []

for s in sh["shots"]:
    sid = s["id"]
    start = s["start"]
    end = s["end"]
    dur = round(end - start, 2)
    bg = s["bg"]
    sents = s.get("sentences", [])
    
    # Lấy text của các câu
    sent_texts = [f"[{sid_c}] {sent_map[sid_c]['text']}" for sid_c in sents if sid_c in sent_map]
    full_text = " ".join(sent_texts)
    
    # Lấy text hiển thị trên hình
    segs = s.get("segments", [])
    display_parts = []
    for seg in segs:
        for el in seg.get("elems", []):
            if len(el) > 1:
                display_parts.append(el[1])
    display_text = " · ".join(display_parts)
    
    shots_audit.append({
        "shot_id": sid,
        "start": start,
        "end": end,
        "dur": dur,
        "bg": bg,
        "sents": sents,
        "text": full_text,
        "display": display_text
    })

# In từng shot để rà soát
with open(".work/_shots_full_alignment.txt", "w", encoding="utf-8") as f:
    for item in shots_audit:
        f.write(f"SHOT {item['shot_id']} ({item['start']:.2f}s -> {item['end']:.2f}s, {item['dur']:.1f}s) | BG: {item['bg']}\n")
        f.write(f"  CHỮ TRÊN HÌNH: {item['display']}\n")
        f.write(f"  LỜI ĐỌC THẬT : {item['text']}\n\n")

print(f"Đã xuất toàn bộ 70 shot ra .work/_shots_full_alignment.txt ({len(shots_audit)} shot)")
