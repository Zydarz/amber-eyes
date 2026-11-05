import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))

matches = [r for r in prov if "Tap02_JA" in r.get("file", "")]
print(f"Total matching entries for Tap02_JA: {len(matches)}")
for m in matches:
    print(f"  {m.get('file')} ({m.get('loai')})")
