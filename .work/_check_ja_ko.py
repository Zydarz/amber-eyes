# -*- coding: utf-8 -*-
"""Deep inspection of Japanese and Korean scripts for Tap 15."""
import sys, re
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

files = {
    "JA": "01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md",
    "KO": "01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md"
}

for lang, p in files.items():
    print(f"\n==========================================")
    print(f"KIỂM TRA CHUYÊN SÂU: {lang}")
    print(f"==========================================")
    parsed = PK.parse_file(p)
    loi = [e for e in parsed if e["kind"] == "LOI"]
    sents = []
    for el in loi:
        for s in el.get("sentences", []):
            sents.append((s["id"], s["text"]))
            
    print(f"Tổng số câu LOI: {len(sents)}")
    issues = []
    for sid, txt in sents:
        # Check double space
        if "  " in txt:
            issues.append((sid, "Khoảng trắng đôi", txt))
            
        # Check space before punctuation
        if re.search(r"\s+[.,!?;:。、！？]", txt):
            issues.append((sid, "Khoảng trắng trước dấu câu", txt))
            
        # Check quotes balance
        if lang == "JA":
            if txt.count("「") != txt.count("」"):
                issues.append((sid, "Ngoặc vuông 「」 không cân", txt))
            if txt.count("“") != txt.count("”"):
                issues.append((sid, "Ngoặc kép “” không cân", txt))
            if txt.count('"') % 2 != 0:
                issues.append((sid, "Ngoặc kép thẳng không cân", txt))
            # Ending punctuation for Japanese
            if not re.search(r'[。！？」”]$', txt.strip()):
                issues.append((sid, "Không kết thúc bằng 。！？」”", txt))
            # Check Western full stop in Japanese
            if re.search(r'[\u3040-\u30ff\u4e00-\u9faf]\.', txt):
                issues.append((sid, "Dấu chấm phương Tây sau chữ Nhật", txt))
                
        elif lang == "KO":
            if txt.count("“") != txt.count("”"):
                issues.append((sid, "Ngoặc kép “” không cân", txt))
            if txt.count('"') % 2 != 0:
                issues.append((sid, "Ngoặc kép thẳng không cân", txt))
            if not re.search(r'[.?!’”]$', txt.strip()):
                issues.append((sid, "Không kết thúc bằng .?!’”", txt))
            # Check Japanese punctuation in Korean
            if "。" in txt or "、" in txt:
                issues.append((sid, "Chứa dấu câu Nhật (。/、)", txt))
                
        # Check ellipsis (G1)
        if "..." in txt or "…" in txt:
            issues.append((sid, "Vi phạm G1 (chấm lửng)", txt))
            
    print(f"Tổng số vấn đề: {len(issues)}")
    for iss in issues:
        print(f"  [{iss[0]}] {iss[1]}: '{iss[2]}'")
