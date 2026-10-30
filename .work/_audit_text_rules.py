import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
shots = json.loads((ROOT / ".work" / "shots_t04.json").read_text(encoding="utf-8"))["shots"]
script = json.loads((ROOT / ".work" / "script_tap04.json").read_text(encoding="utf-8"))

sents_dict = {}
for e in script:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sents_dict[s["id"]] = s["text"]

print("=== KIỂM TRA CHỮ TRÊN HÌNH (SEGMENTS) & NGUYÊN VĂN CÂU TRÍCH (RULE H6/H7) ===")

text_issues = []
for s in shots:
    sid = s["id"]
    tmpl = s.get("template") or ""
    segs = s.get("segments", [])
    s_sents = s.get("sentences", [])
    
    combined_text = " ".join(sents_dict.get(k, "") for k in s_sents)
    
    # Kiểm tra Rule H7: Mẫu T5 chỉ hiện MỘT số / tiêu đề lớn
    if tmpl == "T5":
        bold_count = 0
        for sg in segs:
            for k, v in sg.get("elems", []):
                if k == "bold":
                    bold_count += 1
        if bold_count > 1:
            text_issues.append(f"Shot {sid} (T5): Có {bold_count} cụm **bold** (Rule H7 chỉ cho phép 1 số/tiêu đề lớn, các thông tin khác viết *nghiêng*)")

    # Kiểm tra câu trích nguyên văn (T4 hoặc quote)
    for sg in segs:
        for k, v in sg.get("elems", []):
            if k == "quote":
                # v phải có trong câu thoại
                # Chuẩn hóa bỏ dấu câu để so sánh
                v_clean = re.sub(r"[^\w\s]", "", v.lower())
                sent_clean = re.sub(r"[^\w\s]", "", combined_text.lower())
                if v_clean not in sent_clean:
                    text_issues.append(f"Shot {sid}: Câu trích “{v}” không khớp nguyên văn trong câu thoại!")

print(f"Tổng số vấn đề về chữ: {len(text_issues)}")
for iss in text_issues:
    print(f"  [!] {iss}")
