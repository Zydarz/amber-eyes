import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = Path(".work/_tl_apply.txt")
if p.exists():
    print(p.read_text(encoding="utf-8")[:1000])
else:
    print("No _tl_apply.txt")
