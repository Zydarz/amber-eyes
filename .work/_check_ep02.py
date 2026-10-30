import json
from pathlib import Path

W = Path(__file__).resolve().parents[1] / ".work"
import edition as ED

ep02 = ED.EPISODES["02"]
script = json.loads((W / "script_tap02.json").read_text(encoding="utf-8"))
sids = {s["id"] for e in script if e["kind"] == "LOI" for s in e["sentences"]}
eids = {e["id"] for e in script}

print("Checking EPISODES['02']:")
print("summary:", ep02.get("summary"))
for sid in ep02.get("summary", []):
    if sid not in sids:
        print("  MISSING summary sid:", sid)

print("need count:", len(ep02.get("need", [])))
missing_need = [sid for sid in ep02.get("need", []) if sid not in sids]
print("  MISSING need sids:", missing_need)

print("act1_cue:", ep02.get("act1_cue"), "exists?", ep02.get("act1_cue") in eids or ep02.get("act1_cue") in sids)
print("silence_cue:", ep02.get("silence_cue"), "exists?", ep02.get("silence_cue") in eids or ep02.get("silence_cue") in sids)
print("click_cues:", ep02.get("click_cues"))
