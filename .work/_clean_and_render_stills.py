import os
import sys
import shutil
from pathlib import Path

os.environ["AE_EP"] = "02"
os.environ["AE_LANG"] = "en"

ROOT = Path("D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work"))

stills_dir = ROOT / ".work/video3_EN_t02/stills"
if stills_dir.exists():
    for f in stills_dir.glob("*.png"):
        f.unlink()
    print("Cleaned old stills.")

import build_video3
sys.argv = ["build_video3.py", "--stills", "all"]
build_video3.main()

rendered = list(stills_dir.glob("*.png"))
print(f"Rendered {len(rendered)} stills into {stills_dir}")
