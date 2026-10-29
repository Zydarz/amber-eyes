import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

script = json.loads(open(".work/script_tap04_EN.json", encoding="utf-8").read())
shots = json.loads(open(".work/shots_EN_t04.json", encoding="utf-8").read())["shots"]

sents_dict = {}
for e in script:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sents_dict[s["id"]] = {
                "text": s["text"],
                "role": e["role"]
            }

issues = []
for s in shots:
    sid = s["id"]
    s_sents = s.get("sentences", [])
    tmpl = s.get("template") or ""
    role = s.get("role")
    segs = s.get("segments", [])
    
    if not s_sents:
        continue

    # Role check
    expected_roles = {sents_dict[k]["role"] for k in s_sents if k in sents_dict}
    if len(expected_roles) == 1:
        exp = list(expected_roles)[0]
        # In EN, N1/N2 map to N in script
        if role in ["N1", "N2"] and exp == "N":
            pass
        elif role != exp:
            issues.append(f"[SAI VAI] Shot {sid}: role={role} != exp={exp}")

    # Text check
    for idx_seg, sg in enumerate(segs):
        at_s = sg.get("at_sentence")
        if at_s:
            t_sids = [k for k in s_sents if k.endswith(f"#{at_s}")]
            active_sent = sents_dict[t_sids[0]]["text"] if t_sids and t_sids[0] in sents_dict else ""
        else:
            active_sent = " ".join(sents_dict[k]["text"] for k in s_sents if k in sents_dict)
            
        clean_sent = re.sub(r"[^\w\s]", " ", active_sent.lower())
        sent_words = set(clean_sent.split())

        for kind, text in sg.get("elems", []):
            if tmpl in ["T10", "T5"]:
                continue
            clean_txt = re.sub(r"[^\w\s]", " ", text.lower())
            txt_words = [w for w in clean_txt.split() if len(w) >= 3 and not w.isdigit()]
            if not txt_words:
                continue
            matches = [w for w in txt_words if w in sent_words]
            match_rate = len(matches) / len(txt_words)
            if match_rate < 0.40:
                issues.append(f"[CHỮ KHÔNG KHỚP] Shot {sid} seg {idx_seg} [{kind}]: '{text}' (match {match_rate:.0%})\n    Lời đọc ({at_s or 'all'}): '{active_sent}'")

print(f"Tổng số vấn đề phát hiện: {len(issues)}")
for iss in issues:
    print("  ", iss)
