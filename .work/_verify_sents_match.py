import json
import subprocess
import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Load script_tap02_JA.json
with open(".work/script_tap02_JA.json", "r", encoding="utf-8") as f:
    script_els = json.load(f)

script_sents = []
for el in script_els:
    if el.get("kind") == "LOI":
        for s in el.get("sentences", []):
            script_sents.append((s["id"], s["text"]))

print(f"Total sentences in script_tap02_JA.json: {len(script_sents)}")

# Load timeline from 5e9910b9
cmd = ["git", "show", "5e9910b9:.work/timeline_s_JA_t02.json"]
res = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
tl_5e = json.loads(res.stdout)
tl_items = tl_5e.get("items", [])
print(f"Total sentences in 5e9910b9 timeline: {len(tl_items)}")

# Compare
mismatches = 0
for idx, (sid, stext) in enumerate(script_sents):
    if idx >= len(tl_items):
        print(f"Missing in timeline: {sid}")
        mismatches += 1
        continue
    item = tl_items[idx]
    if item["id"] != sid:
        print(f"ID mismatch at {idx}: script {sid} vs timeline {item['id']}")
        mismatches += 1
    elif item["text"] != stext:
        # Check text difference
        print(f"Text mismatch at {sid}:\n  script:   {stext}\n  timeline: {item['text']}")
        mismatches += 1

if mismatches == 0:
    print("ALL 203 SENTENCES MATCH 100% PERFECTLY!")
else:
    print(f"Total mismatches: {mismatches}")
