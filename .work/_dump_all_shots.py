import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
W = ROOT / ".work"

shots = json.load(open(W / "_shots_analysis.json", encoding="utf-8"))

for i in range(1, 6):
    act_shots = [s for s in shots if s["sid"].startswith(f"{i}-")]
    print(f"=== ACT {i}: {len(act_shots)} shots ===")
    for s in act_shots:
        has_ph = f" [phrases: {s['vn_ph']}]" if s['vn_ph'] else ""
        print(f"  {s['sid']}: EN='{s['chu_en']}'{has_ph}")
