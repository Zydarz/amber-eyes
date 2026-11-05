# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

tl_vn = json.load(open(".work/timeline_s_t06.json", encoding="utf-8"))
print("Markers in VN timeline:")
for m in tl_vn.get("markers", []):
    print(m)
