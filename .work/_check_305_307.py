import json

tl = json.load(open(".work/timeline_s_EN_t02.json", encoding="utf-8"))
items = {it["id"]: it for it in tl["items"]}

for it in tl["items"]:
    if it["id"].startswith("3.05") or it["id"].startswith("3.07"):
        print(f"{it['id']:8s} | {it['start']:7.2f} - {it['end']:7.2f} | {it['text'][:50]}")
