import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ["AE_LANG"] = "ja"
os.environ["AE_EP"] = "02"

sys.path.insert(0, str(Path("D:/TEST/Gax/amber-eyes/.work")))
import edition as ED

print("ED.EPN:", ED.EPN)
print("ED.LANG:", ED.LANG)
print("ED.EP['master']:", ED.EP["master"])
print("ED.EP['dir']:", ED.EP["dir"])
print("ED.EP['title']:", ED.EP["title"])
print("ED.EP['mux_af']:", ED.EP.get("mux_af"))
print("ED.EP['intro']:", ED.EP["intro"])
