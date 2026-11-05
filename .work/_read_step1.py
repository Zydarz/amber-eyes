import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path(".work/_step1_shots_srt_ja_t02.py")
if p.exists():
    print(p.read_text(encoding="utf-8"))
