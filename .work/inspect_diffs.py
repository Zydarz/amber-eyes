# -*- coding: utf-8 -*-
import json

vn = json.load(open(".work/t32_vn.json", encoding="utf-8"))
en = json.load(open(".work/t32_en.json", encoding="utf-8"))
ja = json.load(open(".work/t32_ja.json", encoding="utf-8"))

diff_ids = ["2.06", "2.07", "4.02", "4.05", "4.07", "5.02", "5.05"]
for did in diff_ids:
    v = [x for x in vn if x["id"] == did][0]["sentences"]
    e = [x for x in en if x["id"] == did][0]["sentences"]
    j = [x for x in ja if x["id"] == did][0]["sentences"]
    print(f"=== {did} ===")
    print(f"VN ({len(v)}):")
    for idx, s in enumerate(v):
        print(f"  {idx+1}: {s['text'][:50]}")
    print(f"EN ({len(e)}):")
    for idx, s in enumerate(e):
        print(f"  {idx+1}: {s['text'][:50]}")
    print(f"JA ({len(j)}):")
    for idx, s in enumerate(j):
        print(f"  {idx+1}: {s['text'][:50]}")
