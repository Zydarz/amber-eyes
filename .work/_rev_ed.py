import json, sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import edition as ED

print("=== 2. KIỂM TRA EDITION.PY CHO TẬP 05 ===")
ep = ED.EPISODES["05"]
print("dir:", ep["dir"])
print("plan:", ep["plan"])
print("act1_cue:", ep["act1_cue"])
print("silence_cue:", ep["silence_cue"])
print("click_cues:", ep["click_cues"])
print("bed:", ep["bed"])
print("sfx_sheet:", ep["sfx_sheet"])

# Simulate marker generation from build_audio3.py
script = json.load(open(".work/script_tap05.json", encoding="utf-8"))
markers = [{"type": "INTRO", "start": 0.0, "end": 22.41}]
t = 23.0
cur_act = None
acts = {}
for e in script:
    act = e["act"]
    if cur_act is not None and act != cur_act:
        markers.append({"type": "ACT", "act": act, "start": round(t, 3), "end": round(t + 2.0, 3)})
        t += 2.0
    cur_act = act
    if e["kind"] == "NGHI":
        markers.append({"type": "NGHI", "id": e["id"], "start": round(t, 3), "end": round(t + e["sec"], 3), "desc": e.get("desc", "")})
        t += e["sec"]
    elif e["kind"] in ("SFX", "BGM"):
        markers.append({"type": e["kind"], "id": e["id"], "at": round(t, 3), "desc": e.get("desc", "")})
    else:
        # Dummy sentence lengths for simulation
        for s in e["sentences"]:
            t += 2.5

# Test act1_cue lookup
cue_act1 = next((m["at"] for m in markers if m.get("id") == ep["act1_cue"]), None)
print(f"act1_cue ({ep['act1_cue']}) found at t={cue_act1}s -> {'OK' if cue_act1 is not None else 'FAILED!'}")

# Test silence_cue lookup
cue_silence = next((m for m in markers if m.get("id") == ep["silence_cue"]), None)
print(f"silence_cue ({ep['silence_cue']}) found at [{cue_silence.get('start')}-{cue_silence.get('end')}]s -> {'OK' if cue_silence is not None else 'FAILED!'}")

# Test click_cues lookup
for cid in ep["click_cues"]:
    cue_click = next((m["at"] for m in markers if m.get("id") == cid), None)
    print(f"click_cue ({cid}) found at t={cue_click}s -> {'OK' if cue_click is not None else 'FAILED!'}")
