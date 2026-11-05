import json
import re
import unicodedata

m = json.load(open(".work/tts_manifest_EN_t02.json", encoding="utf-8"))
recog = json.load(open(".work/speech_full_recognized_en_t02.json", encoding="utf-8"))
recog = [r for r in recog if r["start"] >= 20.0]

def norm(text):
    text = unicodedata.normalize("NFKC", text or "").lower()
    text = re.sub(r"<#[^#]+#>", " ", text)
    text = text.replace("’", "'").replace("“", '"').replace("”", '"').replace("—", " ").replace("–", " ")
    text = re.sub(r"[^\w\s]", " ", text)
    return [w for w in text.split() if w]

sents = []
for item in m:
    sents.append({
        "id": item["id"],
        "text": re.sub(r"<#[^#]+#>", "", item["text"]).strip(),
        "tokens": norm(item["text"])
    })

for r in recog:
    r["tokens"] = norm(r["text"])

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
    min_j = max(i, exp_j - 40)
    max_j = min(M - (N - i), exp_j + 40)
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
