# -*- coding: utf-8 -*-
"""
Deep inspection of all 199 sentences in Episode 09 Vietnamese script.
"""
import sys, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban as PK

p_vn = PK.parse_file(str(ROOT / "01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))
loi_vn = [e for e in p_vn if e["kind"] == "LOI"]

print(f"Total LOI elements: {len(loi_vn)}")

# Common Vietnamese misspelling patterns to watch out for:
# s/x, tr/ch, d/gi/r, l/n, c/k, hỏi/ngã
suspicious_patterns = [
    (r'\bxơ suất\b', 'sơ suất'),
    (r'\bsơ xuất\b', 'sơ suất'),
    (r'\bxắp xếp\b', 'sắp xếp'),
    (r'\bsắp sếp\b', 'sắp xếp'),
    (r'\bchia xẻ\b', 'chia sẻ'),
    (r'\bgiấu diếm\b', 'giấu giếm'),
    (r'\bdấu diếm\b', 'giấu giếm'),
    (r'\bdấu giếm\b', 'giấu giếm'),
    (r'\bchẩn đoán\b', 'chẩn đoán (chú ý luật K5 không khẳng định chẩn đoán tâm thần)'),
    (r'\bsáng lạng\b', 'xán lạn'),
    (r'\bxán lạng\b', 'xán lạn'),
    (r'\bphong phanh\b', 'phong phanh / phong thanh'),
    (r'\blãng mạng\b', 'lãng mạn'),
    (r'\bvô hình chung\b', 'vô hình trung'),
    (r'\bbàng hoang\b', 'bàng hoàng'),
    (r'\bđầy đọa\b', 'đày đọa'),
    (r'\bđày đoạ\b', 'đày đọa'),
    (r'\bchâm ngòi\b', 'châm ngòi'),
    (r'\btrơ lỳ\b', 'trơ lỳ / trơ lì'),
    (r'\bbản ngả\b', 'bản ngã'),
    (r'\bảo tưởng\b', 'ảo tưởng'),
    (r'\bhoan tưởng\b', 'hoang tưởng'),
    (r'\bchủ mưu\b', 'chủ mưu'),
    (r'\bchu mưu\b', 'chủ mưu'),
    (r'\bchiến dịch\b', 'chiến dịch'),
    (r'\btrừng phạt\b', 'trừng phạt'),
    (r'\bnghiệt ngã\b', 'nghiệt ngã'),
    (r'\bnghiệt ngả\b', 'nghiệt ngã'),
    (r'\blương tâm\b', 'lương tâm'),
    (r'\blương tri\b', 'lương tri'),
    (r'\btrắc ẩn\b', 'trắc ẩn'),
    (r'\bchắc ẩn\b', 'trắc ẩn'),
    (r'\bbãi bỏ\b', 'bãi bỏ'),
    (r'\bbải bỏ\b', 'bãi bỏ'),
    (r'\bthao túng\b', 'thao túng'),
    (r'\btẩy não\b', 'tẩy não'),
    (r'\bgiải phẫu\b', 'giải phẫu'),
    (r'\bgiải phẩu\b', 'giải phẫu'),
    (r'\bquy trình\b', 'quy trình'),
    (r'\bphán quyết\b', 'phán quyết'),
    (r'\btuyên án\b', 'tuyên án'),
]

found_issues = []

for elem in loi_vn:
    act = elem.get("act", 1)
    role = elem.get("role", "Unknown")
    elem_id = elem.get("id", "??")
    for s in elem["sentences"]:
        sid = s["id"]
        txt = s["text"]
        
        for pat, note in suspicious_patterns:
            if re.search(pat, txt, re.IGNORECASE):
                # check if it's the wrong variant
                found_issues.append((sid, f"Matched pattern '{pat}': {note}", txt))

print(f"Pattern matches found: {len(found_issues)}")
for sid, note, txt in found_issues:
    print(f"[{sid}] {note}\n  Text: {txt}\n")
