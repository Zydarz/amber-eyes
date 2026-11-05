import json

tl = json.load(open(".work/timeline_s_EN_t02.json", encoding="utf-8"))
for it in tl["items"]:
    if it["id"].startswith("3.08") or it["id"].startswith("3.11"):
        print(f"{it['id']:7s} | {it['start']:7.2f} - {it['end']:7.2f} ({it['end']-it['start']:4.2f}s) | {it['text'][:60]}")
