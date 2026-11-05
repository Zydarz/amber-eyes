import json
import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

with open(".work/shots_JA_t02.json", "r", encoding="utf-8") as f:
    shots_curr = json.load(f)

curr_list = shots_curr.get("shots", []) if isinstance(shots_curr, dict) else shots_curr
print(f"Current shots count: {len(curr_list)}, total: {shots_curr.get('total') if isinstance(shots_curr, dict) else 'none'}")

cmd_shots = ["git", "show", "5e9910b9:.work/shots_JA_t02.json"]
res_shots = subprocess.run(cmd_shots, capture_output=True, text=True, encoding="utf-8")
shots_5e = json.loads(res_shots.stdout)
list_5e = shots_5e.get("shots", []) if isinstance(shots_5e, dict) else shots_5e
print(f"5e9910b9 shots count: {len(list_5e)}, total: {shots_5e.get('total') if isinstance(shots_5e, dict) else 'none'}")

curr_ids = [s["id"] for s in curr_list]
ids_5e = [s["id"] for s in list_5e]

print("IDs in current but not 5e:", [i for i in curr_ids if i not in ids_5e])
print("IDs in 5e but not current:", [i for i in ids_5e if i not in curr_ids])

# Check Vietnamese shots count
with open(".work/shots_t02.json", "r", encoding="utf-8") as f:
    shots_vn = json.load(f)
vn_list = shots_vn.get("shots", []) if isinstance(shots_vn, dict) else shots_vn
print(f"VN shots count: {len(vn_list)}, total: {shots_vn.get('total') if isinstance(shots_vn, dict) else 'none'}")

# Check EN shots count
with open(".work/shots_EN_t02.json", "r", encoding="utf-8") as f:
    shots_en = json.load(f)
en_list = shots_en.get("shots", []) if isinstance(shots_en, dict) else shots_en
print(f"EN shots count: {len(en_list)}, total: {shots_en.get('total') if isinstance(shots_en, dict) else 'none'}")
