import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path(".work/parse_shots.py")
print(p.read_text(encoding="utf-8")[1000:2500])
