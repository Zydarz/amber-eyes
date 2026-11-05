import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path(".work/_transcribe_t02_en.py")
if p.exists():
    print(p.read_text(encoding="utf-8")[500:1500])
