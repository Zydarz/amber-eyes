# -*- coding: utf-8 -*-
"""Comprehensive spellcheck and linguistic verification for Episode 15 in 4 languages."""
import sys, re, io, json
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

files = {
    "VN": "01_KICH_BAN/Tap15/kichban_tap15_23102026.md",
    "EN": "01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md",
    "JA": "01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md",
    "KO": "01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md",
}

print("=== BẮT ĐẦU KIỂM TRA CHÍNH TẢ TOÀN BỘ KỊCH BẢN TẬP 15 ===")

# Danh sách từ sai chính tả tiếng Việt thực sự cần cảnh báo
CONFUSING_VN = [
    (r"\bsát nhập\b", "sáp nhập"),
    (r"\bdấu diếm\b", "giấu giếm"),
    (r"\bdấu giếm\b", "giấu giếm"),
    (r"\bvô hình chung\b", "vô hình trung"),
    (r"\bxoay sở\b", "xoay xở"),
    (r"\bchuẩn đoán\b", "chẩn đoán"),
    (r"\bthăm quan\b", "tham quan"),
    (r"\bchấp vá\b", "chắp vá"),
    (r"\bchăn chở\b", "trăn trở"),
    (r"\bbạt vô âm tín\b", "bặt vô âm tín"),
    (r"\bchải nghiệm\b", "trải nghiệm"),
    (r"\btựu chung\b", "tựu trung"),
    (r"\bsuông sẻ\b", "suôn sẻ"),
    (r"\bchững chạt\b", "chững chạc"),
    (r"\bchần trừ\b", "chần chừ"),
    (r"\blãng mạng\b", "lãng mạn"),
    (r"\bgiằn vặt\b", "dằn vặt"),
    (r"\bdằng xé\b", "giằng xé"),
    (r"\bsao nhãng\b", "xao nhãng"),
    (r"\bbàng quang\b", "bàng quan"),
    (r"\bxúc tích\b", "súc tích"),
    (r"\bchính chắn\b", "chín chắn"),
    (r"\bchia xẻ\b", "chia sẻ"),
    (r"\bchẽn chẽ\b", "chặt chẽ"),
    (r"\bnhận chức\b", "nhậm chức"),
    (r"\bkhe khắt\b", "khắt khe"),
]

V9_BANNED = {
    "VN": ["máu", "thi thể", "xác chết", "tự sát", "cắt cổ", "bóp cổ", "ngạt thở", "đâm", "trói", "sát hại", "chém", "bắn chết", "chết chóc", "đập nát", "đập vỡ", "đập tan", "chặt"],
    "EN": ["blood", "corpse", "decapitat", "strangl", "suicide", "stab", "murdered"],
    "JA": ["死体", "血液", "自殺", "首を絞", "刺殺", "毒殺"],
    "KO": ["시체", "피투", "자살", "목을 졸"],
}

# Whitelist các từ lặp tự nhiên
NATURAL_DUP_VN = {"ngày", "người", "từng", "dần", "lần", "rất", "đêm", "mãi", "nhà", "ai", "lớp", "bước", "điểm", "vết", "song"}
NATURAL_DUP_EN = {"that", "had"}

for lang, path in files.items():
    print(f"\n=======================================================")
    print(f"--- KIỂM TRA NGÔN NGỮ: {lang} ({path}) ---")
    print(f"=======================================================")
    parsed = PK.parse_file(path)
    loi_elements = [e for e in parsed if e["kind"] == "LOI"]
    all_sentences = []
    for el in loi_elements:
        for s in el.get("sentences", []):
            all_sentences.append((s["id"], el.get("role", ""), s["text"]))
            
    print(f"Tổng số elements: {len(parsed)} (LOI: {len(loi_elements)})")
    print(f"Tổng số câu thoại: {len(all_sentences)}")
    
    issues = []
    
    # 1. Dấu câu kết thúc
    for sid, role, txt in all_sentences:
        if lang in ["VN", "EN"]:
            if not re.search(r'[.?!]["”\']?$', txt.strip()):
                issues.append((sid, "Lỗi kết câu", f"Câu không kết thúc bằng dấu chấm/hỏi/cảm: '{txt}'"))
        elif lang == "JA":
            if not re.search(r'[。！？"”」]$', txt.strip()):
                issues.append((sid, "Lỗi kết câu", f"Câu không kết thúc bằng dấu 。/！/？/」: '{txt}'"))
        elif lang == "KO":
            if not re.search(r'[.?!]["”\']?$', txt.strip()):
                issues.append((sid, "Lỗi kết câu", f"Câu không kết thúc bằng dấu ./!/?: '{txt}'"))
                
    # 2. Quy tắc G1: Dấu chấm lửng (...) hoặc (…)
    for sid, role, txt in all_sentences:
        if "..." in txt or "…" in txt:
            issues.append((sid, "Vi phạm G1 (chấm lửng)", f"Chứa dấu chấm lửng: '{txt}'"))
            
    # 3. Lỗi khoảng trắng thừa
    for sid, role, txt in all_sentences:
        if "  " in txt:
            issues.append((sid, "Khoảng trắng đôi", f"Chứa '  ': '{txt}'"))
        if re.search(r"\s+[,.:;?!]", txt):
            issues.append((sid, "Khoảng trắng trước dấu câu", f"'{txt}'"))
        if lang in ["VN", "EN"]:
            m = re.findall(r'([,;?!])([^\s"”\'\)])', txt)
            # loại trừ số thập phân
            m = [x for x in m if not (x[0] == ',' and x[1].isdigit())]
            if m:
                issues.append((sid, "Thiếu khoảng trắng sau dấu câu", f"{m} trong: '{txt}'"))

    # 4. Ngoặc kép không cân
    for sid, role, txt in all_sentences:
        q_straight = txt.count('"')
        q_left = txt.count('“')
        q_right = txt.count('”')
        if q_straight % 2 != 0:
            issues.append((sid, "Ngoặc kép thẳng không cân", f"{q_straight} dấu: '{txt}'"))
        if q_left != q_right:
            issues.append((sid, "Ngoặc kép cong không cân", f"“={q_left}, ”={q_right}: '{txt}'"))
            
    # 5. Viết tắt có dấu chấm dễ làm vỡ câu
    for sid, role, txt in all_sentences:
        if re.search(r"\b(Dr|Mr|Mrs|Ms|vs)\.", txt, re.IGNORECASE):
            issues.append((sid, "Viết tắt có dấu chấm", f"'{txt}'"))
            
    # 6. Từ cấm V9
    fb_list = V9_BANNED.get(lang, [])
    for sid, role, txt in all_sentences:
        for fb in fb_list:
            if lang in ["VN", "EN"]:
                if re.search(r"\b" + re.escape(fb) + r"\b", txt, re.IGNORECASE):
                    issues.append((sid, "Từ cấm V9", f"Chứa từ cấm '{fb}': '{txt}'"))
            else:
                if fb in txt:
                    issues.append((sid, "Từ cấm V9", f"Chứa từ cấm '{fb}': '{txt}'"))
                    
    # 7. Lặp từ bất thường
    for sid, role, txt in all_sentences:
        words = txt.split()
        for i in range(len(words) - 1):
            w1 = re.sub(r"[^\w\s]", "", words[i]).lower()
            w2 = re.sub(r"[^\w\s]", "", words[i+1]).lower()
            if w1 and w1 == w2:
                if lang == "VN" and w1 not in NATURAL_DUP_VN:
                    issues.append((sid, f"Lặp từ: '{words[i]} {words[i+1]}'", txt))
                elif lang == "EN" and w1 not in NATURAL_DUP_EN:
                    issues.append((sid, f"Duplicate word: '{words[i]} {words[i+1]}'", txt))

    # 8. Riêng Tiếng Việt: Cặp từ dễ sai
    if lang == "VN":
        for pat, note in CONFUSING_VN:
            for sid, role, txt in all_sentences:
                m = re.search(pat, txt, re.IGNORECASE)
                if m:
                    issues.append((sid, f"Cặp từ dễ lẫn ({note})", f"Khớp '{m.group(0)}' trong: '{txt}'"))
                    
    print(f"-> Tổng số vấn đề phát hiện [{lang}]: {len(issues)}")
    for iss in issues:
        print(f"   [{iss[0]}] {iss[1]}: {iss[2]}")

print("\n=== HOÀN TẤT QUÉT CƠ BẢN ===")
