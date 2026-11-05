import os
import sys
from pathlib import Path

os.environ["AE_EP"] = "02"
os.environ["AE_LANG"] = "en"

ROOT = Path("D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work"))

import parse_shots
parse_shots.main()
