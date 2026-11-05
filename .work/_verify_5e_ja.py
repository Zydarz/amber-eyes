import json
import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Load timeline from 5e9910b9
cmd = ["git", "show", "5e9910b9:.work/timeline_s_JA_t02.json"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
tl_5e = json.loads(res.stdout)

print("5e9910b9 timeline:")
print(f"Total: {tl_5e.get('total')}")
print(f"Intro: {tl_5e.get('intro')}")
items = tl_5e.get("items", [])
print(f"Number of items: {len(items)}")
print(f"First item: {items[0]}")
print(f"Last item: {items[-1]}")

# Also check markers/acts
print("Acts:", tl_5e.get("acts"))

# Check shots from 5e9910b9
cmd_shots = ["git", "show", "5e9910b9:.work/shots_JA_t02.json"]
res_shots = subprocess.run(cmd_shots, capture_output=True, text=True, encoding="utf-8")
shots_5e = json.loads(res_shots.stdout)
print("5e9910b9 shots:")
print(f"Total: {shots_5e.get('total')}")
shots_list = shots_5e.get("shots", [])
print(f"Number of shots: {len(shots_list)}")
print(f"First shot: {shots_list[0]}")
print(f"Last shot: {shots_list[-1]}")
