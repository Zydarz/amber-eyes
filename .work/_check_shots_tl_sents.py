import json

shots = json.load(open(".work/shots_EN_t02.json", encoding="utf-8"))["shots"]
tl = json.load(open(".work/timeline_s_EN_t02.json", encoding="utf-8"))
tl_sents = {it["id"]: it for it in tl["items"]}

shot_sents = []
missing_in_tl = []
for sh in shots:
    sents = sh.get("sentences", [])
    if sents:
        for sid in sents:
            shot_sents.append(sid)
            if sid not in tl_sents:
                missing_in_tl.append((sh["id"], sid))

print(f"Total shot sentence references: {len(shot_sents)}")
print(f"Unique sentences in shots: {len(set(shot_sents))}")
print(f"Total sentences in timeline: {len(tl_sents)}")
print(f"Missing in timeline: {len(missing_in_tl)}")
if missing_in_tl:
    print("First 10 missing:", missing_in_tl[:10])

# Check sentences in timeline that are not in shots
shot_set = set(shot_sents)
tl_missing_in_shots = [sid for sid in tl_sents if sid not in shot_set]
print(f"Timeline sentences missing in shots: {len(tl_missing_in_shots)}")
if tl_missing_in_shots:
    print("First 10 tl missing in shots:", tl_missing_in_shots[:10])
