import os
import sys
from pathlib import Path

os.environ["AE_EP"] = "02"
os.environ["AE_LANG"] = "en"

ROOT = Path("D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work"))

if __name__ == "__main__":
    import build_video3
    sys.argv = ["build_video3.py", "--workers", "6"]
    build_video3.main()
