# -*- coding: utf-8 -*-
"""Check named entities and consistency across all 4 languages in Tap 14."""
import sys, re, io
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

files = {
    "VN": "01_KICH_BAN/Tap14/kichban_tap14_23102026.md",
    "EN": "01_KICH_BAN/Tap14_EN/kichban_tap14_EN.md",
    "JA": "01_KICH_BAN/Tap14_JA/kichban_tap14_JA.md",
    "KO": "01_KICH_BAN/Tap14_KO/kichban_tap14_KO.md",
}

print("=== KIỂM TRA ĐỐI CHIẾU THỰC THỂ TÊN RIÊNG & TÍNH NHẤT QUÁN ===")

# Danh sách thực thể chuẩn
entities = {
    "Betty": {"VN": ["Betty", "Elisabeth Anne Broderick", "Elisabeth Broderick"], "EN": ["Betty", "Elisabeth Anne Broderick", "Elisabeth Broderick"], "JA": ["ベティ", "エリザベス"], "KO": ["베티", "엘리자베스"]},
    "Dan": {"VN": ["Daniel Broderick", "Dan", "Daniel"], "EN": ["Daniel Broderick", "Dan", "Daniel"], "JA": ["ダニエル", "ダン"], "KO": ["대니얼", "댄"]},
    "Linda": {"VN": ["Linda Kolkena", "Linda"], "EN": ["Linda Kolkena", "Linda"], "JA": ["リンダ・コルケナ", "リンダ"], "KO": ["린다 콜케나", "린다"]},
    "Kim": {"VN": ["Kim Broderick", "Kim"], "EN": ["Kim Broderick", "Kim"], "JA": ["キム・ブロデリック", "キム"], "KO": ["킴 브로데릭", "킴"]},
    "La Jolla": {"VN": ["La Jolla"], "EN": ["La Jolla"], "JA": ["ラ・ホヤ"], "KO": ["라호야"]},
    "Marston Hills": {"VN": ["Marston Hills"], "EN": ["Marston Hills"], "JA": ["マーストン・ヒルズ"], "KO": ["마스턴 힐스"]},
    "Coral Reef": {"VN": ["Coral Reef"], "EN": ["Coral Reef"], "JA": ["コーラル・リーフ"], "KO": ["코럴 리프"]},
}

for lang, path in files.items():
    p = PK.parse_file(path)
    loi = [e for e in p if e["kind"] == "LOI"]
    print(f"\n--- Ngôn ngữ: {lang} ({path}) ---")
    print(f"Tổng số lượt thoại LOI: {len(loi)}")
    print(f"Tổng số câu: {sum(len(e.get('sentences', [])) for e in loi)}")
    
    # Kiểm tra xem có câu nào kết thúc bất thường không
    unusual_endings = []
    for e in loi:
        for s in e.get("sentences", []):
            t = s["text"].strip()
            sid = s["id"]
            if lang in ["VN", "EN"]:
                if not re.search(r'[.!?]["”\']?$', t):
                    unusual_endings.append((sid, t))
            elif lang == "JA":
                if not re.search(r'[。！？]["”」\']?$', t):
                    unusual_endings.append((sid, t))
            elif lang == "KO":
                if not re.search(r'[.!?]["”\']?$', t):
                    unusual_endings.append((sid, t))
                    
    print(f"Số câu kết thúc bất thường: {len(unusual_endings)}")
    for u in unusual_endings:
        print(f"  [{u[0]}]: {u[1]}")
