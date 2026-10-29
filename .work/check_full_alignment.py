import json
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.stderr.reconfigure(encoding="utf-8", errors="replace")

script = json.loads(open(".work/script_tap04.json", encoding="utf-8").read())
shots = json.loads(open(".work/shots_t04.json", encoding="utf-8").read())["shots"]

sents_dict = {}
for e in script:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sents_dict[s["id"]] = {
                "text": s["text"],
                "role": e["role"],
                "element": e["id"]
            }

print(f"Loaded {len(sents_dict)} sentences, {len(shots)} shots.")

# Kiểm tra từng shot
issues = []
for s in shots:
    sid = s["id"]
    s_sents = s.get("sentences", [])
    tmpl = s.get("template") or ""
    bg = s.get("bg") or ""
    role = s.get("role")
    flags = s.get("flags", {})
    segs = s.get("segments", [])
    
    if not s_sents:
        continue
        
    # 1. Kiểm tra vai nhân vật
    expected_roles = {sents_dict[sid_]["role"] for sid_ in s_sents if sid_ in sents_dict}
    if len(expected_roles) > 1:
        issues.append(f"[LỆCH VAI] Shot {sid}: Chứa nhiều vai khác nhau {expected_roles} ({s_sents})")
    elif len(expected_roles) == 1:
        exp = list(expected_roles)[0]
        if role != exp:
            issues.append(f"[SAI VAI] Shot {sid}: Bảng shot ghi role={role}, nhưng kịch bản là role={exp} ({s_sents})")

    # 2. Kiểm tra chữ trên hình so với câu thoại
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
            if match_rate < 0.5:
                issues.append(f"[CHỮ KHÔNG CÓ TRONG LỜI] Shot {sid} seg {idx_seg} [{kind}]: '{text}' (match {match_rate:.0%})\n    Lời đọc ({at_s or 'all'}): '{active_sent}'")

print(f"\nTổng số vấn đề phát hiện: {len(issues)}")
for iss in issues[:30]:
    print(iss)
if len(issues) > 30:
    print(f"... và {len(issues) - 30} vấn đề khác.")
