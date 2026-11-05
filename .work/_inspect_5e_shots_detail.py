import json
import subprocess
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Let's see what 5e9910b9 shots_JA_t02.json looks like
cmd = ["git", "show", "5e9910b9:.work/shots_JA_t02.json"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
shots_5e = json.loads(res.stdout)

print("5e shots total:", shots_5e["total"])
print("5e shots count:", len(shots_5e["shots"]))
# Look at first 5 shots
for s in shots_5e["shots"][:5]:
    print(f"  {s['id']}: {s['start']} -> {s['end']}, sents: {s['sentences']}, bg: {s['bg']}, tpl: {s['template']}")

# Look at last 5 shots
for s in shots_5e["shots"][-5:]:
    print(f"  {s['id']}: {s['start']} -> {s['end']}, sents: {s['sentences']}, bg: {s['bg']}, tpl: {s['template']}")
