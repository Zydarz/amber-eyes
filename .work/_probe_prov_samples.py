import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))

print(prov[0])
print(prov[-1])
