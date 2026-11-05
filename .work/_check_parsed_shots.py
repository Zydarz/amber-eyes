# -*- coding: utf-8 -*-
import sys, json
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

p = Path(".work/shots_EN_t06.json")
if not p.exists():
    print("shots_EN_t06.json DOES NOT EXIST!")
    sys.exit(1)

shots = json.load(p.open(encoding="utf-8"))
print(f"Total shots parsed: {len(shots)}")
for s in shots[:5]:
    print(s["id"], s.get("start"), s.get("end"), s.get("template"), s.get("bg"), s.get("text"))
print("...")
for s in shots[-3:]:
    print(s["id"], s.get("start"), s.get("end"), s.get("template"), s.get("bg"), s.get("text"))
