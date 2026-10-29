# -*- coding: utf-8 -*-
import json

with open(".work/timeline_s_t06.json", encoding="utf-8") as f:
    tl = json.load(f)

with open(".work/shots_t06.json", encoding="utf-8") as f:
    sh = json.load(f)

# Tìm các câu xung quanh 1.06#8 và 1.08#1
print("=== TIMELINE CÁC CÂU LIÊN QUAN ===")
for it in tl["items"]:
    if it["id"].startswith("1.06") or it["id"].startswith("1.08") or it["id"].startswith("1.09"):
        print(f"Câu {it['id']:8s} | {it['start']:7.2f}s - {it['end']:7.2f}s | {it['text'][:60]}")

print("\n=== CÁC SHOT TƯƠNG ỨNG TRONG SHOTS.JSON ===")
for s in sh["shots"]:
    if s["id"] in ["1-10", "1-11", "1-12", "1-13", "1-14"]:
        print(f"Shot {s['id']:5s} | {s['start']:7.2f}s - {s['end']:7.2f}s | BG: {s['bg']:30s} | Cues: {s.get('sentences')} | Chữ: {s.get('segments', [{}])[0].get('elems', [{}])[0].get('text', '')}")
