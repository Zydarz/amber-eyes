import os
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
sys.path.insert(0, str(Path("D:/TEST/Gax/amber-eyes/.work")))
import edition as ED

print("ED.PLAN:", ED.PLAN)
print("ED.w('timeline_s.json'):", ED.w("timeline_s.json"))
print("ED.w('shots.json'):", ED.w("shots.json"))
