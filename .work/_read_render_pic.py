import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

p = Path(".work/_render_picture_ja_t02.py")
print(p.read_text(encoding="utf-8"))
