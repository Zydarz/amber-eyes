import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"

recog_path = WORK / "speech_full_recognized_en_t02_novad.json"
recog = json.loads(recog_path.read_text(encoding="utf-8"))

# Insert the missing Act 4 opening segments between 129 and 130
seg_sunday = {
    "index": 129.5,
    "start": 812.50,
    "end": 815.36,
    "duration": 2.86,
    "text": "Sunday, February 7th, 2010.",
    "words": []
}
seg_ottawa = {
    "index": 129.6,
    "start": 816.14,
    "end": 818.72,
    "duration": 2.58,
    "text": "Police headquarters in Ottawa, 3:00 PM.",
    "words": []
}

new_recog = []
for r in recog:
    new_recog.append(r)
    if r["start"] == 804.52 and r["end"] == 809.86:
        new_recog.append(seg_sunday)
        new_recog.append(seg_ottawa)

# Re-index
for i, r in enumerate(new_recog):
    r["index"] = i + 1

recog = new_recog
print(f"Patched recog now has {len(recog)} segments.")

# Now load script
script_path = WORK / "script_tap02_EN.json"
script = json.loads(script_path.read_text(encoding="utf-8"))

sents = []
for e in script:
    if e.get("kind") == "LOI":
        role = e.get("vai") or e.get("role")
        if role == "N":
            role = "N1" if e["id"] == "1.07" else "N2"
        for s in e.get("sentences", []):
            sents.append({
                "id": s["id"],
                "element": e["id"],
                "act": e["act"],
                "role": role,
                "text": s["text"]
            })

print(f"Total script sentences: {len(sents)}")

def norm(text):
    text = unicodedata.normalize("NFKC", text or "").lower()
    text = text.replace("’", "'").replace("“", '"').replace("”", '"').replace("—", " ").replace("–", " ")
    text = re.sub(r"[^\w\s]", " ", text)
    return [w for w in text.split() if w]

for s in sents:
    s["tokens"] = norm(s["text"])
    s["norm_text"] = " ".join(s["tokens"])

for r in recog:
    r["tokens"] = norm(r["text"])
    r["norm_text"] = " ".join(r["tokens"])

def sim_score(s_tok, r_tok):
    if not s_tok or not r_tok:
        return 0.0
    s_set = set(s_tok)
    r_set = set(r_tok)
    common = s_set & r_set
    if not common:
        return -2.0
    overlap = len(common) / ((len(s_set) * len(r_set)) ** 0.5)
    len_ratio = min(len(s_tok), len(r_tok)) / max(len(s_tok), len(r_tok))
    return overlap * 3.0 + len_ratio

N = len(sents)
M = len(recog)

dp = {}
dp[(0, 0)] = (0.0, 0)

for i in range(1, N + 1):
    s_tok = sents[i - 1]["tokens"]
    exp_j = int(round(i * (M / N)))
    min_j = max(i, exp_j - 45)
    max_j = min(M - (N - i), exp_j + 45)
    if i == N:
        min_j, max_j = M - 4, M

    for j in range(min_j, max_j + 1):
        best_val = -1e9
        best_pj = -1
        for k in range(1, 6):
            pj = j - k
            if (i - 1, pj) in dp:
                combo_tok = []
                for p in range(pj, j):
                    combo_tok.extend(recog[p]["tokens"])
                sc = sim_score(s_tok, combo_tok)
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
        avail = [pj for pj in range(max(0, cur_j - 5), cur_j) if (i - 1, pj) in dp]
        prev_j = max(avail, key=lambda pj: dp[(i - 1, pj)][0]) if avail else cur_j - 1
    mapping.append((sents[i - 1], list(range(prev_j, cur_j))))
    cur_j = prev_j

mapping.reverse()
print(f"Alignment completed! Mapped {len(mapping)} sentences.")

mismatches = 0
for idx, (s, p_idxs) in enumerate(mapping):
    matched_text = " ".join(recog[p]["text"] for p in p_idxs)
    s_set = set(s["tokens"])
    r_set = set(norm(matched_text))
    overlap = len(s_set & r_set) / max(1, len(s_set))
    if overlap < 0.4:
        mismatches += 1
        print(f"  [WARN {overlap:.2f}] {s['id']}: '{s['text']}' vs '{matched_text}'")

print(f"Total low-overlap (<0.40): {mismatches}/{N}")

items_tl = []
prev_end = 22.41

for idx, (s, p_idxs) in enumerate(mapping):
    matched = [recog[p] for p in p_idxs if recog[p]["tokens"]]
    if not matched:
        matched = [recog[p_idxs[0]]]
    
    st = matched[0]["start"]
    en = matched[-1]["end"]
    
    if s["id"] == "1.03#1":
        st = max(22.86, st)
    
    if st < prev_end + 0.10:
        st = prev_end + 0.10
    if en <= st + 0.4:
        en = st + max(1.0, len(s["tokens"]) * 0.25)
    
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
        m_st = round(max(prev_act_end + 0.10, m_en - 2.0), 3)
        markers.append({"type": "ACT", "act": act, "start": m_st, "end": m_en})
    cur_act = act
    
    if e.get("kind") == "NGHI":
        sec = e.get("sec", 1.5)
        prev_elem_id = script[idx - 1]["id"] if idx > 0 else None
        next_elem_id = script[idx + 1]["id"] if idx < len(script) - 1 else None
        
        p_end = elem_span.get(prev_elem_id, [22.86, 22.86])[1] if prev_elem_id in elem_span else 22.86
        n_st = elem_span.get(next_elem_id, [p_end + sec, p_end + sec])[0] if next_elem_id in elem_span else p_end + sec
        
        mst = round(p_end + 0.05, 3)
        men = round(min(n_st - 0.15, mst + sec), 3)
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
        at_time = elem_span.get(next_elem_id, [22.86, 22.86])[0] if next_elem_id in elem_span else 22.86
        markers.append({
            "type": e.get("kind"),
            "id": eid,
            "at": round(at_time, 3),
            "desc": e.get("desc", "")
        })

TOTAL_DUR = 1396.910

timeline_out = {
    "total": round(TOTAL_DUR, 3),
    "intro": 22.41,
    "items": items_tl,
    "markers": markers,
    "acts": {str(k): [round(a, 3), round(b, 3)] for k, (a, b) in acts.items()}
}

out_tl = WORK / "timeline_s_EN_t02.json"
out_tl.write_text(json.dumps(timeline_out, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Saved new timeline to {out_tl}")
print(f"Total sentences: {len(items_tl)}, Total markers: {len(markers)}")
print(f"First sentence start: {items_tl[0]['start']}s, Last sentence end: {items_tl[-1]['end']}s")
print(f"Acts boundaries: {timeline_out['acts']}")
