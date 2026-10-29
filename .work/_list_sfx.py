import os
from pathlib import Path
root = Path("assets/sfx")
for p in sorted(root.glob("**/*")):
    if p.is_file():
        print(p.relative_to(root))
