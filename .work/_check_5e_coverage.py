import json
import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

cmd_shots = ["git", "show", "5e9910b9:.work/shots_JA_t02.json"]
res_shots = subprocess.run(cmd_shots, capture_output=True, text=True, encoding="utf-8")
shots_5e = json.loads(res_shots.stdout)["shots"]

print(f"5e shots: {len(shots_5e)}")
sents_5e = []
for s in shots_5e:
    sents_5e.extend(s.get("sentences", []))

print(f"Sentences covered in 5e shots: {len(sents_5e)} / unique: {len(set(sents_5e))}")

# Check timeline 5e
cmd_tl = ["git", "show", "5e9910b9:.work/timeline_s_JA_t02.json"]
res_tl = subprocess.run(cmd_tl, capture_output=True, text=True, encoding="utf-8")
tl_5e = json.loads(res_tl.stdout)
tl_sents = [it["id"] for it in tl_5e["items"]]

missing_in_5e = [s for s in tl_sents if s not in sents_5e]
print(f"Sentences missing in 5e shots: {len(missing_in_5e)}: {missing_in_5e}")

extra_in_5e = [s for s in sents_5e if s not in tl_sents]
print(f"Sentences extra in 5e shots: {len(extra_in_5e)}: {extra_in_5e}")
