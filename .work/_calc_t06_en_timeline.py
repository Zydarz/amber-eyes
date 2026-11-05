# -*- coding: utf-8 -*-
"""Compute exact timeline for Episode 06 English from recognized master audio."""
import json
import re

script = json.load(open(".work/script_tap06_EN.json", encoding="utf-8"))
recognized = json.load(open(".work/speech_full_recognized.json", encoding="utf-8-sig"))

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
M = len(recognized)
dp = {}
dp[(0, 0)] = (0.0, 0)
for i in range(1, N + 1):
    s_text = sents[i - 1]["text"]
    for j in range(i, M - (N - i) + 1):
        best_val = -1e9
        best_pj = -1
        for k in (1, 2, 3):
            pj = j - k
            if (i - 1, pj) in dp:
                combo_text = " ".join(recognized[p]["text"] for p in range(pj, j))
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

# Calculate raw voice duration for each sentence
voice_durs = {}
for s, p_idxs in mapping:
    if s["id"] == "1.02#1":
        # First speech starts at 23.00s and ends at 34.22s
        voice_durs[s["id"]] = 34.22 - 23.00
    else:
        d = sum(recognized[p]["duration"] for p in p_idxs)
        voice_durs[s["id"]] = round(d, 3)

FIRST_VOICE = 23.0
GAP_ACT = 2.0
GAP_SPEAKER = 0.65
GAP_SENT = 0.40
GAP_Q = 0.60
MAX_PAUSE = 3.0

t = FIRST_VOICE
items_tl = []
markers = [{"type": "INTRO", "start": 0.0, "end": 22.41}]
acts = {}
cur_act = None
pending = None

for e in script:
    act = e["act"]
    if cur_act is not None and act != cur_act:
        markers.append({"type": "ACT", "act": act, "start": round(t, 3), "end": round(t + GAP_ACT, 3)})
        t += GAP_ACT
        pending = None
    if act not in acts:
        acts[act] = [t, t]
    cur_act = act
    if e["kind"] == "NGHI":
        sec = min(e["sec"], MAX_PAUSE)
        markers.append({"type": "NGHI", "id": e["id"], "start": round(t, 3), "end": round(t + sec, 3), "desc": e.get("desc", "")})
        t += sec
        pending = None
    elif e["kind"] in ("SFX", "BGM"):
        markers.append({"type": e["kind"], "id": e["id"], "at": round(t, 3), "desc": e.get("desc", "")})
    else:
        role = e.get("vai") or e.get("role")
        if pending:
            g = GAP_SPEAKER if pending[0] != role else GAP_SENT
            if pending[1].rstrip('”" ').endswith("?"):
                g = max(g, GAP_Q)
            t += g
        for k, s in enumerate(e["sentences"]):
            d = voice_durs[s["id"]]
            items_tl.append({"id": s["id"], "element": e["id"], "act": act, "role": role,
                             "start": round(t, 3), "end": round(t + d, 3), "text": s["text"]})
            t += d
            if k < len(e["sentences"]) - 1:
                t += GAP_Q if s["text"].rstrip('”" ').endswith("?") else GAP_SENT
        pending = (role, e["sentences"][-1]["text"])
    acts[act][1] = t

end_voice = t
total_calc = end_voice + 1.0 + 5.0 + 3.0
print(f"Voice ended at: {end_voice:.2f}s")
print(f"Calculated total: {total_calc:.2f}s")
print(f"Target master mp3 duration: 1283.54s")
print(f"Difference: {total_calc - 1283.54:+.2f}s")
