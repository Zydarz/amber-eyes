# -*- coding: utf-8 -*-
"""Align 187 recognized phrases with absolute timestamps into 165 script sentences for Tap06 EN."""
import json
import re

script = json.load(open(".work/script_tap06_EN.json", encoding="utf-8"))
rec = json.load(open(".work/speech_async_absolute.json", encoding="utf-8-sig"))

sents = []
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            sents.append({
                "id": s["id"],
                "element": e["id"],
                "act": e["act"],
                "role": e.get("vai") or e.get("role"),
                "text": s["text"]
            })

def norm(text):
    t = re.sub(r"[^\w\s]", " ", text.lower())
    return set(t.split())

def score(s_text, r_text):
    sw = norm(s_text)
    rw = norm(r_text)
    if not sw or not rw:
        return 0
    common = sw & rw
    return len(common) / (len(sw) ** 0.5 * len(rw) ** 0.5)

N = len(sents)
M = len(rec)
dp = {}
dp[(0, 0)] = (0.0, 0)

for i in range(1, N + 1):
    s_text = sents[i - 1]["text"]
    for j in range(i, M - (N - i) + 1):
        best_val = -1e9
        best_pj = -1
        for k in (1, 2, 3, 4):
            pj = j - k
            if (i - 1, pj) in dp:
                combo_text = " ".join(rec[p]["text"] for p in range(pj, j))
                sc = score(s_text, combo_text)
                val = dp[(i - 1, pj)][0] + sc
                if val > best_val:
                    best_val = val
                    best_pj = pj
        if best_pj != -1:
            dp[(i, j)] = (best_val, best_pj)

cur_j = M
mapping = []
for i in range(N, 0, -1):
    prev_j = dp[(i, cur_j)][1]
    mapping.append((sents[i - 1], list(range(prev_j, cur_j))))
    cur_j = prev_j
mapping.reverse()

items_tl = []
acts = {}
markers = [{"type": "INTRO", "start": 0.0, "end": 22.41}]

for s, p_idxs in mapping:
    assigned = [rec[p] for p in p_idxs]
    sid = s["id"]
    act = s["act"]
    role = s["role"]
    
    if sid == "1.02#1":
        # First sentence: speech starts at 23.00s
        start = 23.00
        end = round(assigned[-1]["end"], 3)
    else:
        start = round(assigned[0]["start"], 3)
        end = round(assigned[-1]["end"], 3)
        
    items_tl.append({
        "id": sid,
        "element": s["element"],
        "act": act,
        "role": role,
        "start": start,
        "end": end,
        "text": s["text"]
    })
    
    if act not in acts:
        acts[act] = [start, end]
    else:
        acts[act][1] = end

# Markers for ACT transitions
for act in range(1, 6):
    a_start, a_end = acts[act]
    markers.append({"type": "ACT", "act": act, "start": a_start, "end": a_end})

# Sort items by start time just to be 100% sure
items_tl.sort(key=lambda x: x["start"])

timeline_out = {
    "total": 1283.54,
    "intro": 22.41,
    "items": items_tl,
    "markers": markers,
    "acts": {str(k): [round(a, 3), round(b, 3)] for k, (a, b) in acts.items()}
}

out_p = ".work/timeline_s_EN_t06.json"
with open(out_p, "w", encoding="utf-8") as f:
    json.dump(timeline_out, f, ensure_ascii=False, indent=2)

print(f"SUCCESS: Generated {out_p} with {len(items_tl)} items!")
print(f"Total: {timeline_out['total']} s")
for act in range(1, 6):
    print(f"  Act {act}: {acts[act][0]:.2f}s -> {acts[act][1]:.2f}s (dur={acts[act][1]-acts[act][0]:.2f}s)")
