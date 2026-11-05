import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
lines = (ROOT / "README.md").read_text(encoding="utf-8").splitlines()
for i, l in enumerate(lines[15:35], 16):
    print(f"{i}: {l}")
