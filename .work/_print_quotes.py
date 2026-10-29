import json
import sys

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

s = json.loads(open(".work/script_tap04.json", encoding="utf-8").read())
targets = ("1.07#1", "1.07#2", "1.07#3", "1.07#4", "4.06#1", "4.06#2", "4.06#3", "4.06#4", "4.06#5", "4.12#6", "4.12#7")

for e in s:
    for it in e.get("sentences", []):
        if it["id"] in targets:
            print(f"[{it['id']}]: \"{it['text']}\"")
