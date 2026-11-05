import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))

for k in list(prov.keys()):
    if "02" in k:
        print(f"Key: {k}")
        print("  Value:", prov[k])
