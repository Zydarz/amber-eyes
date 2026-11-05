import os
import sys

os.environ["AE_EP"] = "02"
os.environ["AE_LANG"] = "en"

from pathlib import Path
ROOT = Path("D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT / ".work"))

import make_intro
make_intro.main()
