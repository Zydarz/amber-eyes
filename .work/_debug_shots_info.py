# -*- coding: utf-8 -*-
import json

with open(".work/shots_t06.json", encoding="utf-8") as f:
    sh = json.load(f)

for s in sh["shots"]:
    if s["id"] in ["1-10", "1-11", "1-12", "1-13", "1-14"]:
        print(f"Shot {s['id']:5s} | {s['start']:7.2f}s - {s['end']:7.2f}s (dur={s['end']-s['start']:5.2f}s) | BG: {s['bg']:32s} | Sents: {s.get('sentences')}")
