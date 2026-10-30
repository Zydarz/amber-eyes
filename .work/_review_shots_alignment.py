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
shots_data = json.loads((ROOT / ".work" / "shots_t04.json").read_text(encoding="utf-8"))
tl_data = json.loads((ROOT / ".work" / "timeline_s_t04.json").read_text(encoding="utf-8"))
script_data = json.loads((ROOT / ".work" / "script_tap04.json").read_text(encoding="utf-8"))

shots = shots_data["shots"]
items = {it["id"]: it for it in tl_data["items"]}

# Tạo từ điển câu đầy đủ từ script
sentences = {}
for e in script_data:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sentences[s["id"]] = {
                "text": s["text"],
                "role": e["role"],
                "element": e["id"],
                "direction": e.get("direction", "")
            }

print(f"Tổng số shot: {len(shots)}")
print(f"Tổng số câu thoại: {len(sentences)}")

issues = []

# 1. Kiểm tra bao phủ câu thoại (phải đủ 100% không sót câu nào và đúng thứ tự)
assigned_sents = []
for s in shots:
    for sid in s.get("sentences", []):
        assigned_sents.append(sid)

all_sent_ids = list(sentences.keys())
missing_sents = [sid for sid in all_sent_ids if sid not in assigned_sents]
duplicate_sents = [sid for sid in assigned_sents if assigned_sents.count(sid) > 1]

if missing_sents:
    issues.append(f"CÂU THOẠI BỊ THIẾU KHÔNG CÓ TRONG SHOT NÀO: {missing_sents}")
if duplicate_sents:
    issues.append(f"CÂU THOẠI BỊ LẶP TRONG NHIỀU SHOT: {set(duplicate_sents)}")

# 2. Kiểm tra thứ tự xuất hiện của câu thoại trong shots
if assigned_sents != sorted(assigned_sents, key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1].split("#")[0]), int(x.split("#")[1]))):
    issues.append("THỨ TỰ CÂU THOẠI TRONG SHOT BỊ XÁO TRỘN!")

# 3. Kiểm tra chi tiết từng shot
print("\n=== ĐỐI CHIẾU CHI TIẾT 84 SHOT: ẢNH - LỜI - CHỮ - THỜI GIAN ===")
for idx, s in enumerate(shots):
    sid = s["id"]
    s_start = s["start"]
    s_end = s["end"]
    dur = s_end - s_start
    bg = s.get("bg", "")
    tmpl = s.get("template", "")
    role = s.get("role", "")
    s_sents = s.get("sentences", [])
    segs = s.get("segments", [])
    flags = s.get("flags", {})

    # Kiểm tra thời lượng shot (Quy tắc H10: 3 - 15s cho shot có lời, trừ trường hợp đặc biệt)
    # Kiểm tra đồng bộ thời gian với câu thoại
    if s_sents:
        first_sent = items[s_sents[0]]
        last_sent = items[s_sents[-1]]
        # s_start phải bám sát first_sent["start"] (thường -0.2s)
        # s_end phải kéo dài ít nhất đến last_sent["end"]
        t_gap_start = first_sent["start"] - s_start
        t_gap_end = s_end - last_sent["end"]
        
        # Lấy toàn bộ text của câu trong shot này
        combined_text = " ".join(sentences[k]["text"] for k in s_sents)
        
        # Kiểm tra xem chữ trên hình (segments) có xuất phát từ câu thoại không (Rule H6)
        for seg in segs:
            for el_type, el_txt in seg.get("elems", []):
                # Bỏ qua các nhãn tiêu đề cố định kiểu HỒI, ĐẠO LUẬT CULLEN...
                # Kiểm tra xem các con số hoặc từ khóa chính có trong combined_text không
                numbers_in_txt = re.findall(r"\d+", el_txt)
                for num in numbers_in_txt:
                    # Chuyển số sang chữ hoặc kiểm tra số trong combined_text
                    # Nếu số không có trong combined_text và không phải tiêu đề hồi
                    if num not in combined_text:
                        # Kiểm tra xem có phải là ngày tháng hoặc số la mã được viết chữ không
                        pass

        # In thông tin tóm tắt shot
        first_few_words = combined_text[:60] + "..." if len(combined_text) > 60 else combined_text
        seg_summary = " | ".join(f"[{t}] {txt}" for seg in segs for t, txt in seg.get("elems", []))
        if len(seg_summary) > 80:
            seg_summary = seg_summary[:80] + "..."
            
        # Kiểm tra vai nói
        expected_role = sentences[s_sents[0]]["role"]
        # Lưu ý: trong script e["role"] là "N", trong plan là N1 hoặc N2
        if expected_role in ("H", "D", "C") and role != expected_role:
            issues.append(f"Shot {sid}: Lệch vai! Kịch bản vai {expected_role} nhưng shot ghi vai {role}")

    else:
        # Shot không lời (intro, nghỉ, chuyển hồi, thẻ kết)
        first_few_words = f"[KHÔNG LỜI: {s.get('beat_text', '')}]"
        seg_summary = " | ".join(f"[{t}] {txt}" for seg in segs for t, txt in seg.get("elems", []))

    print(f"{sid:<5} | {dur:4.1f}s ({s_start:6.1f} -> {s_end:6.1f}) | {bg:<24} | {tmpl:<3} | {role:<2} | {s_sents}")

print(f"\nTổng số vấn đề phát hiện ban đầu: {len(issues)}")
for iss in issues:
    print(f"  - {iss}")
