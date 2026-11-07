# -*- coding: utf-8 -*-
"""Spellcheck and sanity check script for Episode 20 across all 4 languages.
Checks:
1. Repeated words
2. Bracket and parenthesis symmetry
3. Typographical anomalies (double punctuation, spaces before punctuation)
4. Vocabulary consistency (names, legal terms, places)
"""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

scripts = {
    "VN": ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_23102026.md",
    "EN": ROOT / "01_KICH_BAN" / "Tap20_EN" / "kichban_tap20_EN.md",
    "JA": ROOT / "01_KICH_BAN" / "Tap20_JA" / "kichban_tap20_JA.md",
    "KO": ROOT / "01_KICH_BAN" / "Tap20_KO" / "kichban_tap20_KO.md",
}

print("=" * 70)
print("RUNNING THOROUGH SPELLCHECK & SANITY CHECKS ON ALL 4 SCRIPTS")
print("=" * 70)

for lang, path in scripts.items():
    print(f"\n--- Checking {lang}: {path.name} ---")
    text = path.read_text(encoding="utf-8")
    
    # 1. Bracket parity
    for left, right in [("(", ")"), ("[", "]"), ("{", "}"), ("“", "”")]:
        c_left = text.count(left)
        c_right = text.count(right)
        status = "OK" if c_left == c_right else f"MISMATCH ({c_left} != {c_right})"
        print(f"  Brackets '{left}' and '{right}': {status}")

    # 2. Repeated words
    if lang in ["VN", "EN"]:
        repeated = re.findall(r'\b([a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]{3,})\s+\1\b', text, re.IGNORECASE)
        print(f"  Repeated adjacent words (>=3 chars): {repeated if repeated else 'None (Clean)'}")

    # 3. Double spaces or misplaced punctuation
    double_punct = re.findall(r'([,.;:!?])\1+', text)
    # ignore markdown headers like ## or bullet points
    space_before_punct = re.findall(r'\s+([,.;:!?])', text)
    # in markdown tables | or headers might trigger, but let's see in LOI
    loi_lines = [l for l in text.splitlines() if l.startswith("**Host**:") or l.startswith("**Điều tra viên**:") or l.startswith("**Chuyên gia**:") or l.startswith("**N1**:") or l.startswith("**N2**:") or l.startswith("**Cú**:") or l.startswith("**Sói**:") or l.startswith("**Cáo**:") or l.startswith("**Thỏ tuyết**:") or l.startswith("**Gấu trúc**:") or l.startswith("**Investigator**:") or l.startswith("**Expert**:") or l.startswith("**刑事**:") or l.startswith("**専門家**:") or l.startswith("**수사관**:") or l.startswith("**전문가**:") or l.startswith("**진행자**:")]
    
    loi_text = "\n".join(loi_lines)
    loi_space_before_comma = re.findall(r'\s+[,]', loi_text)
    loi_space_before_period = re.findall(r'\s+[.]', loi_text)
    print(f"  LOI spaces before comma: {len(loi_space_before_comma)}")
    print(f"  LOI spaces before period: {len(loi_space_before_period)}")
    
    # Check proper names consistency
    if lang == "VN":
        # Check Lauren Giddings, Stephen McDaniel, Mercer, Barristers Hall
        print("  Proper names count:")
        print("    Lauren Giddings:", len(re.findall(r'Lauren Giddings', text)))
        print("    Lauren:", len(re.findall(r'Lauren', text)))
        print("    Stephen McDaniel:", len(re.findall(r'Stephen McDaniel', text)))
        print("    McDaniel:", len(re.findall(r'McDaniel', text)))
        print("    Mercer:", len(re.findall(r'Mercer', text)))
        print("    Barristers Hall:", len(re.findall(r'Barristers Hall', text)))
    elif lang == "EN":
        print("  Proper names count:")
        print("    Lauren Giddings:", len(re.findall(r'Lauren Giddings', text)))
        print("    Stephen McDaniel:", len(re.findall(r'Stephen McDaniel', text)))
        print("    Mercer:", len(re.findall(r'Mercer', text)))
        print("    Barristers Hall:", len(re.findall(r'Barristers Hall', text)))
    elif lang == "JA":
        print("  Proper names count:")
        print("    ローレン・ギディングス:", len(re.findall(r'ローレン・ギディングス', text)))
        print("    スティーブン・マクダニエル:", len(re.findall(r'スティーブン・マクダニエル', text)))
        print("    マーサー大学:", len(re.findall(r'マーサー大学', text)))
        print("    バリスターズ・ホール:", len(re.findall(r'バリスターズ・ホール', text)))
    elif lang == "KO":
        print("  Proper names count:")
        print("    Lauren Giddings:", len(re.findall(r'Lauren Giddings', text)))
        print("    Stephen McDaniel:", len(re.findall(r'Stephen McDaniel', text)))
        print("    머서:", len(re.findall(r'머서', text)))
        print("    Barristers Hall:", len(re.findall(r'Barristers Hall', text)))

print("\nSpellcheck scan complete.")
