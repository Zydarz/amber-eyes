import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

for fn in ["_render_picture_ja_t02.py", "_qc_final_ja_t02.py", "_build_stems_ja_t02.py"]:
    p = Path(f".work/{fn}")
    if p.exists():
        print(f"=== {fn} ===")
        print(p.read_text(encoding="utf-8")[:1000])
