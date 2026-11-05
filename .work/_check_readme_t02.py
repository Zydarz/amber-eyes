import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
lines = (ROOT / "README.md").read_text(encoding="utf-8").splitlines()
for l in lines:
    if "Tap02" in l or "Tập 02" in l or "Tap 02" in l:
        print(l)
