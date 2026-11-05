# -*- coding: utf-8 -*-
import sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

for p in [Path(".work/shots_EN_t06.json"), Path(".work/shots.json"), Path(".work/shots_t06.json")]:
    if p.exists():
        data = json.load(p.open(encoding="utf-8"))
        print(f"{p}: {len(data)} items")
        if data:
            print(f"  First: {data[0].get('id')} Last: {data[-1].get('id')}")
