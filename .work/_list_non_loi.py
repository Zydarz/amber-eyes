# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

sc = json.load(open(".work/script_tap06_EN.json", encoding="utf-8"))
tl = json.load(open(".work/timeline_s_EN_t06.json", encoding="utf-8"))
items = {it["id"]: it for it in tl["items"]}

print("Script elements:")
for el in sc:
    eid = el["id"]
    ekind = el.get("kind")
    if ekind != "LOI":
        print(f"Non-LOI element: {eid} | kind: {ekind} | desc: {el.get('desc')} | sec: {el.get('sec')}")
