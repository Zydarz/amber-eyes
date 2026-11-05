# -*- coding: utf-8 -*-
import sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

data = json.load(open(".work/shots_EN_t06.json", encoding="utf-8"))
print("Type of data:", type(data))
if isinstance(data, dict):
    print("Keys:", data.keys())
    for k in data.keys():
        val = data[k]
        if isinstance(val, list):
            print(f"Key '{k}' has {len(val)} items")
            if val:
                print(f"  First: {val[0].get('id')} Last: {val[-1].get('id')}")
        else:
            print(f"Key '{k}': {val}")
