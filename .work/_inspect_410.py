import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
W = Path(r"D:\TEST\Gax\Audi\.work")
shots = json.load(open(W / "_shots_analysis.json", encoding="utf-8"))

for s in shots:
    if s["sid"] in ['4-10', '4-11', '4-12', '4-13', '4-14', '4-15', '4-16']:
        print(f"=== {s['sid']} (ids: {s['ids']}) ===")
        print("VN:", s["chu_vn"])
        print("EN:", s["chu_en"])
        print("JA:", s["ctx_ja"])
        print()
