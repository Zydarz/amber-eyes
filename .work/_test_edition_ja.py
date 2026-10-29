import os
import sys
from pathlib import Path

sys.path.insert(0, ".work")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

import edition as ED

print("ED.EPN:", ED.EPN)
print("ED.JA:", ED.JA)
print("ED.EP_DIR:", ED.EP_DIR)
print("ED.OUT_DIR:", ED.OUT_DIR)
print("ED.PLAN:", ED.PLAN)
print("ED.MASTER:", ED.MASTER)
print("ED.SCRIPT_JSON:", ED.SCRIPT_JSON)
print("ED.ACTING:", ED.ACTING)
print("ED.INTRO_MOV:", ED.INTRO_MOV)
print("ED.INTRO_MOV exists:", ED.INTRO_MOV.exists())
print("ED.w('timeline_s.json'):", ED.w("timeline_s.json"))
print("ED.w('audio_s'):", ED.w("audio_s"))
