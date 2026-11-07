# -*- coding: utf-8 -*-
"""Comprehensive spell check and linguistic validation for Tap 14 scripts."""
import sys, re, io
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

p_vn = PK.parse_file("01_KICH_BAN/Tap14/kichban_tap14_23102026.md")
p_en = PK.parse_file("01_KICH_BAN/Tap14_EN/kichban_tap14_EN.md")
p_ja = PK.parse_file("01_KICH_BAN/Tap14_JA/kichban_tap14_JA.md")
p_ko = PK.parse_file("01_KICH_BAN/Tap14_KO/kichban_tap14_KO.md")

print("=== KIỂM TRA CHÍNH TẢ & QUY CHUẨN KỊCH BẢN TẬP 14 ===")

# 1. Kiểm tra Tiếng Việt
print("\n--- 1. RÀ SOÁT KỊCH BẢN TIẾNG VIỆT ---")
vn_issues = []
for e in p_vn:
    if e["kind"] == "LOI":
        for s in e.get("sentences", []):
            txt = s["text"]
            sid = s["id"]
            # Khoảng trắng thừa
            if "  " in txt:
                vn_issues.append((sid, "Khoảng trắng đôi", txt))
            # Khoảng trắng trước dấu câu
            if re.search(r"\s+[.,!?;:]", txt):
                vn_issues.append((sid, "Khoảng trắng trước dấu câu", txt))
            # Từ lặp vô nghĩa (lỗi đánh máy)
            dup = re.findall(r"\b(\w+)\s+\1\b", txt, re.I)
            if dup:
                for d in dup:
                    if d.lower() not in ["ngày", "người", "nhà", "ai", "từng", "lớp"]:
                        vn_issues.append((sid, f"Lặp từ bất thường: '{d}'", txt))
            # Dấu ngoặc kép không cân
            if txt.count('"') % 2 != 0:
                vn_issues.append((sid, "Dấu ngoặc kép không cân", txt))
            # Ký hiệu số chưa chuyển sang chữ (ví dụ %, $, km)
            if "%" in txt or "$" in txt:
                vn_issues.append((sid, "Chứa ký hiệu %, $ chưa đổi chữ", txt))
            # Viết tắt có dấu chấm dễ làm vỡ câu (ví dụ Dr., Mr., vs.)
            if re.search(r"\b(Dr|Mr|Mrs|Ms|vs)\.", txt, re.I):
                vn_issues.append((sid, "Viết tắt có dấu chấm", txt))

print(f"Tổng số lỗi phát hiện trong bản Tiếng Việt: {len(vn_issues)}")
for iss in vn_issues:
    print(f"  [{iss[0]}] {iss[1]}: \"{iss[2]}\"")

# 2. Kiểm tra Tiếng Anh
print("\n--- 2. RÀ SOÁT KỊCH BẢN TIẾNG ANH ---")
en_issues = []
for e in p_en:
    if e["kind"] == "LOI":
        for s in e.get("sentences", []):
            txt = s["text"]
            sid = s["id"]
            if "  " in txt:
                en_issues.append((sid, "Double space", txt))
            if re.search(r"\s+[.,!?;:]", txt):
                en_issues.append((sid, "Space before punctuation", txt))
            # Duplicate words in English
            dup = re.findall(r"\b([a-zA-Z]+)\s+\1\b", txt, re.I)
            if dup:
                for d in dup:
                    if d.lower() not in ["that", "had"]:
                        en_issues.append((sid, f"Duplicate word: '{d}'", txt))
            # Abbreviation with dot that might break sentence
            if re.search(r"\b(Mr|Mrs|Ms|Dr|vs)\.", txt):
                en_issues.append((sid, "Abbreviation with dot", txt))

print(f"Tổng số lỗi phát hiện trong bản Tiếng Anh: {len(en_issues)}")
for iss in en_issues:
    print(f"  [{iss[0]}] {iss[1]}: \"{iss[2]}\"")

# 3. Kiểm tra Tiếng Nhật
print("\n--- 3. RÀ SOÁT KỊCH BẢN TIẾNG NHẬT ---")
ja_issues = []
for e in p_ja:
    if e["kind"] == "LOI":
        for s in e.get("sentences", []):
            txt = s["text"]
            sid = s["id"]
            if "  " in txt:
                ja_issues.append((sid, "Double space", txt))
            # Check if sentence does not end with punctuation
            if not txt.endswith(("。", "！", "？", "”", "」")):
                ja_issues.append((sid, "Sentence not ending with punctuation", txt))

print(f"Tổng số lỗi phát hiện trong bản Tiếng Nhật: {len(ja_issues)}")
for iss in ja_issues:
    print(f"  [{iss[0]}] {iss[1]}: \"{iss[2]}\"")

# 4. Kiểm tra Tiếng Hàn
print("\n--- 4. RÀ SOÁT KỊCH BẢN TIẾNG HÀN ---")
ko_issues = []
for e in p_ko:
    if e["kind"] == "LOI":
        for s in e.get("sentences", []):
            txt = s["text"]
            sid = s["id"]
            if "  " in txt:
                ko_issues.append((sid, "Double space", txt))
            if re.search(r"\s+[.,!?;:]", txt):
                ko_issues.append((sid, "Space before punctuation", txt))
            if not txt.endswith((".", "!", "?", "”")):
                ko_issues.append((sid, "Sentence not ending with punctuation", txt))

print(f"Tổng số lỗi phát hiện trong bản Tiếng Hàn: {len(ko_issues)}")
for iss in ko_issues:
    print(f"  [{iss[0]}] {iss[1]}: \"{iss[2]}\"")
