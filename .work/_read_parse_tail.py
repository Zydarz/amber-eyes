import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path(".work/parse_shots.py")
lines = p.read_text(encoding="utf-8").splitlines()
print("\n".join(lines[-50:]))
