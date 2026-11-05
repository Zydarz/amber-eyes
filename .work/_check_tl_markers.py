# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

tl = json.load(open(".work/timeline_s_EN_t06.json", encoding="utf-8"))
print("Keys in timeline:", tl.keys())
print("Total markers:", len(tl.get("markers", [])))
for m in tl.get("markers", []):
    print(m)
