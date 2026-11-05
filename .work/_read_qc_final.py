import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path(".work/_qc_final_ja_t02.py")
print(p.read_text(encoding="utf-8")[:1500])
