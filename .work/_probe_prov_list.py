import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))

print(f"Total entries in provenance: {len(prov)}")
found_02 = [item for item in prov if "Tap02" in item.get("path", "") or "Tap02" in item.get("target", "")]
print(f"Entries for Tap02: {len(found_02)}")
for item in found_02[:5]:
    print(item)
