import sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

for ep in ['11', '12']:
    print(f"\n================ EPISODE {ep} ================")
    for folder in [f"Tap{ep}", f"Tap{ep}_EN", f"Tap{ep}_JA", f"Tap{ep}_KO"]:
        p = Path("02_SAN_XUAT") / folder
        if p.exists():
            files = list(p.rglob("*"))
            print(f"Folder {p}: {len(files)} items")
            for f in files:
                if f.is_file():
                    print(f"  {f.relative_to(p)} ({f.stat().st_size} bytes)")
