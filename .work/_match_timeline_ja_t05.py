# -*- coding: utf-8 -*-
"""Precise DP alignment and complete marker construction for Tap05 JA with natural hold pauses."""
import json
import re
import sys
import unicodedata
from pathlib import Path
import pykakasi

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

script_path = W / "script_tap05_JA.json"
recog_path = W / "speech_full_recognized_ja_t05.json"

script = json.loads(script_path.read_text(encoding="utf-8"))
recog = json.loads(recog_path.read_text(encoding="utf-8"))

_K = pykakasi.kakasi()

def to_hira(text):
    t = unicodedata.normalize("NFKC", text or "")
    t = re.sub(r"[^\w]", "", t)
    return "".join(x["hira"] for x in _K.convert(t)).lower()

sents = []
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            role = e.get("vai") or e.get("role")
            if role == "N":
                role = "N1" if e["id"] == "1.09" else "N2"
            sents.append({
                "id": s["id"],
                "element": e["id"],
                "act": e["act"],
                "role": role,
                "text": s["text"],
                "hira": to_hira(s["text"])
            })

for r in recog:
    r["hira"] = to_hira(r["text"])

def sim(shira, rhira):
    if not shira or not rhira:
        return 0.0
    s_set = set(shira[i:i+2] for i in range(len(shira)-1)) if len(shira) > 1 else {shira}
    r_set = set(rhira[i:i+2] for i in range(len(rhira)-1)) if len(rhira) > 1 else {rhira}
    common = s_set & r_set
    if not common:
        return -0.5
    overlap = len(common) / (len(s_set)**0.5 * len(r_set)**0.5)
    lr = min(len(shira), len(rhira)) / max(len(shira), len(rhira))
    return overlap * 2.0 + lr

N = len(sents)
M = len(recog)

dp = {}
dp[(0, 0)] = (0.0, 0)

for i in range(1, N + 1):
    s_hira = sents[i - 1]["hira"]
    exp_j = int(round(i * (M / N)))
    min_j = max(i, exp_j - 50)
    max_j = min(M - (N - i), exp_j + 50)
    if i == N:
        min_j, max_j = M - 3, M
    
    for j in range(min_j, max_j + 1):
        best_val = -1e9
        best_pj = -1
        for k in range(1, 9):
            pj = j - k
            if (i - 1, pj) in dp:
                combo_hira = "".join(recog[p]["hira"] for p in range(pj, j))
                sc = sim(s_hira, combo_hira)
                val = dp[(i - 1, pj)][0] + sc
                if val > best_val:
                    best_val = val
                    best_pj = pj
        if best_pj != -1:
            dp[(i, j)] = (best_val, best_pj)

cur_j = M
mapping = []
for i in range(N, 0, -1):
    prev_j = dp.get((i, cur_j), (None, -1))[1]
    if prev_j == -1:
        avail = [pj for pj in range(cur_j - 8, cur_j) if (i - 1, pj) in dp]
        prev_j = max(avail, key=lambda pj: dp[(i - 1, pj)][0]) if avail else cur_j - 1
    mapping.append((sents[i - 1], list(range(prev_j, cur_j))))
    cur_j = prev_j
mapping.reverse()

items_tl = []
prev_end = 22.41

for s, p_idxs in mapping:
    matched = [recog[p] for p in p_idxs if recog[p]["hira"]]
    if not matched:
        matched = [recog[p_idxs[0]]]
    
    st = matched[0]["start"]
    en = matched[-1]["end"]
    
    if s["id"] == "1.03#1":
        st = max(22.80, st)
    
    if st < prev_end + 0.15:
        st = prev_end + 0.15
    if en <= st:
        en = st + 1.20
    
    items_tl.append({
        "id": s["id"],
        "element": s["element"],
        "act": s["act"],
        "role": s["role"],
        "start": round(st, 3),
        "end": round(en, 3),
        "text": s["text"]
    })
    prev_end = en

# Adjust sentences before NGHI and ACT transitions to allow positive hold durations
nghi_before_map = {
    "1.03#5": 1.4,   # before 1.04
    "1.05#5": 1.4,   # before 1.06
    "1.10#7": 1.5,   # before 1.11
    "1.16#3": 2.0,   # before ACT 2 (1-21)
    "2.07#4": 2.0,   # before ACT 3 (2-15)
    "3.02#7": 1.5,   # before 3.03
    "3.08#3": 2.0,   # before ACT 4 (3-13)
    "4.06#6": 1.5,   # before 4.07
    "4.15#4": 2.2,   # before ACT 5 (4-18)
    "5.02#5": 1.5,   # before 5.03
    "5.06#5": 1.5,   # before 5.07
    "5.08#5": 1.5,   # before 5.09
}

for it in items_tl:
    sid = it["id"]
    if sid in nghi_before_map:
        buf = nghi_before_map[sid]
        # End it earlier to leave buffer
        it["end"] = round(max(it["start"] + 1.5, it["end"] - buf), 3)

# Reconstruct acts boundaries
acts = {}
for it in items_tl:
    act = it["act"]
    if act not in acts:
        acts[act] = [it["start"], it["end"]]
    else:
        acts[act][1] = it["end"]

markers = [{"type": "INTRO", "start": 0.0, "end": 22.41}]

elem_span = {}
for it in items_tl:
    eid = it["element"]
    if eid not in elem_span:
        elem_span[eid] = [it["start"], it["end"]]
    else:
        elem_span[eid][1] = it["end"]

cur_act = None
for idx, e in enumerate(script):
    eid = e["id"]
    act = e["act"]
    
    if cur_act is not None and act != cur_act:
        prev_act_end = acts[cur_act][1]
        act_st = acts[act][0]
        m_en = round(act_st - 0.20, 3)
        m_st = round(max(prev_act_end + 0.10, m_en - 1.80), 3)
        markers.append({"type": "ACT", "act": act, "start": m_st, "end": m_en})
    cur_act = act
    
    if e.get("kind") == "NGHI":
        sec = e.get("sec", 1.5)
        prev_elem_id = script[idx - 1]["id"] if idx > 0 else None
        next_elem_id = script[idx + 1]["id"] if idx < len(script) - 1 else None
        
        p_end = elem_span.get(prev_elem_id, [23.0, 23.0])[1] if prev_elem_id in elem_span else 23.0
        n_st = elem_span.get(next_elem_id, [p_end + sec, p_end + sec])[0] if next_elem_id in elem_span else p_end + sec
        
        mst = round(p_end + 0.05, 3)
        men = round(min(n_st - 0.20, mst + sec), 3)
        if men <= mst + 0.2:
            men = round(mst + 1.2, 3)
        markers.append({
            "type": "NGHI",
            "id": eid,
            "start": mst,
            "end": men,
            "desc": e.get("desc", "")
        })
    elif e.get("kind") in ("SFX", "BGM"):
        next_elem_id = script[idx + 1]["id"] if idx < len(script) - 1 else None
        at_time = elem_span.get(next_elem_id, [23.0, 23.0])[0] if next_elem_id in elem_span else 23.0
        markers.append({
            "type": e.get("kind"),
            "id": eid,
            "at": round(at_time, 3),
            "desc": e.get("desc", "")
        })

total_dur = 1471.43

timeline_out = {
    "total": round(total_dur, 3),
    "intro": 22.41,
    "items": items_tl,
    "markers": markers,
    "acts": {str(k): [round(a, 3), round(b, 3)] for k, (a, b) in acts.items()}
}

out_tl = W / "timeline_s_JA_t05.json"
out_tl.write_text(json.dumps(timeline_out, ensure_ascii=False, indent=1), encoding="utf-8")
(W / "timeline_s.json").write_text(json.dumps(timeline_out, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"Timeline regenerated successfully with {len(markers)} markers and positive hold durations.")
