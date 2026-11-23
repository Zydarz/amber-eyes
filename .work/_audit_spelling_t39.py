# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path

ROOT = Path(r"d:\TEST\Gax\amber-eyes")

def audit():
    files = [
        (ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap39" / "kichban_tap39_19112026.md", "VN"),
        (ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap39_EN" / "kichban_tap39_EN.md", "EN"),
        (ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap39_JA" / "kichban_tap39_JA.md", "JA"),
    ]
    
    for path, lang in files:
        print("="*50)
        print(f"AUDITING {lang}: {path.name}")
        text = path.read_text(encoding="utf-8")
        
        # 1. Parentheses balance
        p_diff = text.count("(") - text.count(")")
        print(f"Parentheses diff (open - close): {p_diff}")
        
        # 2. Curly quotes balance
        q_diff = text.count("“") - text.count("”")
        print(f"Curly quotes diff (“ - ”): {q_diff}")
        
        # 3. Japanese brackets balance
        if lang == "JA":
            b_diff = text.count("「") - text.count("」")
            print(f"Japanese brackets diff (「 - 」): {b_diff}")
            
        # 4. Trailing punctuation on dialogue lines
        lines = text.splitlines()
        no_end = []
        in_sp = False
        valid_ends = (".", "!", "?", '"', "'", "”", "。", "！", "？", "」", "』", "…", ":", "：")
        for i, line in enumerate(lines, 1):
            s = line.strip()
            if any(s.startswith(p) for p in ["**HOST", "**ĐIỀU", "**CHUYÊN", "**NGƯỜI", "**INVESTIGATOR", "**PSYCHOLOGIST", "**ORDINARY", "**ホスト", "**捜査官", "**心理学者", "**一般人"]):
                in_sp = True
                continue
            if s.startswith("**[") or s.startswith("#") or s.startswith("---") or not s:
                in_sp = False
                continue
            if in_sp:
                if not s.endswith(valid_ends):
                    no_end.append((i, s))
                    
        print(f"Dialogue lines missing punctuation: {len(no_end)}")
        for idx, s in no_end:
            print(f"  Line {idx}: {s}")
            
        # 5. Consecutive duplicate words
        if lang in ("VN", "EN"):
            dups = re.findall(r"\b([a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]+)\s+\1\b", text, re.IGNORECASE)
            allowed = {"chầm", "rôm", "lách", "không", "ròng", "bíp"}
            filtered_dups = [w for w in dups if w.lower() not in allowed]
            print(f"Suspicious consecutive duplicate words: {filtered_dups}")

        # 6. Check common VN typos if VN
        if lang == "VN":
            typo_patterns = [
                (r"\bchuẩn đoán\b", "chẩn đoán"),
                (r"\bxắp xếp\b", "sắp xếp"),
                (r"\bsử lí\b", "xử lý"),
                (r"\bxuất xắc\b", "xuất sắc"),
                (r"\bchính chắn\b", "chín chắn"),
                (r"\bchần chừ\b", "chần chừ"),
                (r"\bngoan nghoãn\b", "ngoan ngoãn"),
                (r"\bsuy xụp\b", "suy sụp"),
                (r"\bxơ xác\b", "xơ xác"),
                (r"\blảng vảng\b", "lảng vảng"),
                (r"\btrần trừ\b", "chần chừ"),
                (r"\bvả lại\b", "vả lại"),
                (r"\btrơ trẽn\b", "trơ trẽn"),
            ]
            for pat, corr in typo_patterns:
                m = re.findall(pat, text, re.IGNORECASE)
                if m and pat != r"\btrơ trẽn\b":
                    print(f"  Typo alert: {m} -> {corr}")

        # 7. Check common EN typos if EN
        if lang == "EN":
            en_typos = [
                r"\bgoverment\b", r"\baccomodate\b", r"\bwich\b", r"\bthier\b", r"\bundoubtly\b",
                r"\bseperate\b", r"\boccured\b", r"\brecieve\b", r"\buntill\b", r"\bdefinately\b",
                r"\bteh\b", r"\badolencent\b", r"\bschizoprenia\b", r"\bhalluciation\b", r"\bunconcious\b"
            ]
            for pat in en_typos:
                m = re.findall(pat, text, re.IGNORECASE)
                if m:
                    print(f"  EN typo alert: {m}")

        # 8. Check JA half-width kana if JA
        if lang == "JA":
            half_width = re.findall(r"[\uFF61-\uFF9F]", text)
            print(f"JA half-width kana count: {len(half_width)}")

if __name__ == "__main__":
    audit()
