import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, ".work")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

import edition as ED

print("thumb:", ED.EP["thumb"])
print("title:", ED.EP["title"])
print("act_titles:", ED.EP["act_titles"])
