import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:\TEST\Gax\Audi")
shots = json.loads((ROOT / ".work" / "shots_t04.json").read_text(encoding="utf-8"))["shots"]
script = json.loads((ROOT / ".work" / "script_tap04.json").read_text(encoding="utf-8"))

sentences = {}
for e in script:
    if e["kind"] == "LOI":
        r = e["role"]
        if e["id"] == "1.07": r = "N1"
        elif e["id"] == "4.06": r = "N2"
        for s in e["sentences"]:
            sentences[s["id"]] = {"role": r, "text": s["text"], "elem": e["id"]}

print("=== KIỂM TRA ĐỐI ỨNG VAI CHO TOÀN BỘ 84 SHOT ===")
mismatches = []
for s in shots:
    sid = s["id"]
    s_role = s.get("role")
    s_sents = s.get("sentences", [])
    if s_sents:
        real_role = sentences[s_sents[0]]["role"]
        if s_role != real_role:
            mismatches.append((sid, s_role, real_role, s_sents, sentences[s_sents[0]]["elem"]))
            print(f"LỆCH: Shot {sid:<5} | Shot ghi: {str(s_role):<2} | Thực tế nói: {real_role:<2} | Câu: {s_sents} (Elem {sentences[s_sents[0]]['elem']})")

if not mismatches:
    print("Tất cả các shot có lời đều khớp vai 100%!")
else:
    print(f"\nTổng cộng phát hiện {len(mismatches)} shot bị lệch vai!")
