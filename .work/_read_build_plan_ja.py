import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path(".work/_build_plan_tap02_ja.py")
print(p.read_text(encoding="utf-8")[:1200])
