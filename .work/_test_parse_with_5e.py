import json
import subprocess
import sys
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Get 5e9910b9 timeline
cmd = ["git", "show", "5e9910b9:.work/timeline_s_JA_t02.json"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
tl_5e = json.loads(res.stdout)

# Write to temp file
W = Path("D:/TEST/Gax/amber-eyes/.work")
(W / "_temp_tl_5e.json").write_text(json.dumps(tl_5e, ensure_ascii=False, indent=2), encoding="utf-8")

# Let's inspect parse_shots logic with this timeline
import parse_shots
# Temporarily mock TL and SENT
parse_shots.TL = tl_5e
parse_shots.SENT = {it["id"]: it for it in tl_5e["items"]}
parse_shots.MARK = {m.get("id"): m for m in tl_5e["markers"] if m.get("id")}
parse_shots.ACTS = [m for m in tl_5e["markers"] if m["type"] == "ACT"]

# Count rows in PLAN
lines = parse_shots.PLAN.read_text(encoding="utf-8").splitlines()
table_rows = [l for l in lines if l.startswith("|") and not l.startswith("|---") and not l.startswith("| Shot")]
print(f"Table rows in KeHoach_Video_Tap02_JA.md: {len(table_rows)}")

# Let's see what parse_shots produces
try:
    shots = parse_shots.parse_all()
    print(f"parse_shots output: {len(shots)} shots, total = {shots[-1]['end'] if shots else 0}")
except Exception as e:
    import traceback
    traceback.print_exc()
