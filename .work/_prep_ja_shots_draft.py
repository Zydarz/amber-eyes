import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
W = ROOT / ".work"

shots = json.load(open(W / "_shots_analysis.json", encoding="utf-8"))

for s in shots[:20]:
    print(f"=== {s['sid']} (ids: {s['ids']}) ===")
    print(f"VN: {s['chu_vn']}")
    print(f"EN: {s['chu_en']}")
    print(f"VN Beat: {s['beat_vn']}")
    print(f"JA Ctx: {s['ctx_ja']}")
    print()
