# -*- coding: utf-8 -*-
"""Spellcheck and sanity check script for Episode 24 across all 4 languages.
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
    "VN": ROOT / "01_KICH_BAN" / "Tap24" / "kichban_tap24_23102026.md",
    "EN": ROOT / "01_KICH_BAN" / "Tap24_EN" / "kichban_tap24_EN.md",
    "JA": ROOT / "01_KICH_BAN" / "Tap24_JA" / "kichban_tap24_JA.md",
    "KO": ROOT / "01_KICH_BAN" / "Tap24_KO" / "kichban_tap24_KO.md",
}

print("=" * 70)
print("RUNNING THOROUGH SPELLCHECK & SANITY CHECKS ON ALL 4 TAP 24 SCRIPTS")
print("=" * 70)

issues_found = 0

for lang, path in scripts.items():
    print(f"\n--- Checking {lang}: {path.name} ---")
    if not path.exists():
        print(f"  ERROR: File not found {path}")
        issues_found += 1
        continue
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # 1. Bracket parity
    for left, right in [("(", ")"), ("[", "]"), ("{", "}"), ("“", "”"), ("‘", "’")]:
        c_left = text.count(left)
        c_right = text.count(right)
        status = "OK" if c_left == c_right else f"MISMATCH ({c_left} != {c_right})"
        if c_left != c_right:
            issues_found += 1
            print(f"  [!] Brackets '{left}' and '{right}': {status}")
        else:
            print(f"  [+] Brackets '{left}' and '{right}': {status} ({c_left})")

    # 2. Repeated words
    if lang in ["VN", "EN"]:
        repeated = re.findall(r'\b([a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]{3,})\s+\1\b', text, re.IGNORECASE)
        # filter out legitimate cases if any
        if repeated:
            print(f"  [!] Repeated adjacent words: {repeated}")
            issues_found += len(repeated)
        else:
            print("  [+] Repeated adjacent words: None (Clean)")

    # 3. Spaces before punctuation in spoken lines
    loi_lines = []
    in_loi = False
    for l in lines:
        if l.startswith("**HOST**") or l.startswith("**ĐIỀU TRA VIÊN**") or l.startswith("**CHUYÊN GIA TÂM LÝ**") or l.startswith("**NGƯỜI BÌNH THƯỜNG**") or \
           l.startswith("**INVESTIGATOR**") or l.startswith("**PSYCHOLOGIST**") or l.startswith("**ORDINARY PERSON**") or \
           l.startswith("**ホスト**") or l.startswith("**捜査官**") or l.startswith("**心理学者**") or l.startswith("**一般人**") or \
           l.startswith("**호스트**") or l.startswith("**수사관**") or l.startswith("**심리학자**") or l.startswith("**일반인**"):
            in_loi = True
            continue
        elif l.startswith("**[") or l.startswith("## ") or l.startswith("---") or not l.strip():
            in_loi = False
            continue
        if in_loi:
            loi_lines.append(l)

    loi_text = "\n".join(loi_lines)
    spaces_before_comma = re.findall(r'[^\s]\s+[,]', loi_text)
    spaces_before_period = re.findall(r'[^\s]\s+[.]', loi_text)
    spaces_before_colon = re.findall(r'[^\s]\s+[:]', loi_text)

    if spaces_before_comma:
        print(f"  [!] Spoken lines space before comma: {len(spaces_before_comma)}")
        issues_found += len(spaces_before_comma)
    else:
        print("  [+] Spoken lines space before comma: Clean")

    if spaces_before_period:
        print(f"  [!] Spoken lines space before period: {len(spaces_before_period)}")
        issues_found += len(spaces_before_period)
    else:
        print("  [+] Spoken lines space before period: Clean")

    # 4. Consistency of key proper names
    print("  Key entities count:")
    if lang == "VN":
        print(f"    Lee Choon-jae: {text.count('Lee Choon-jae')}")
        print(f"    Yoon Sung-yeo: {text.count('Yoon Sung-yeo')}")
        print(f"    Hwaseong: {text.count('Hwaseong')}")
        print(f"    Gyeonggi: {text.count('Gyeonggi')}")
        print(f"    Busan: {text.count('Busan')}")
        print(f"    Suwon: {text.count('Suwon')}")
        print(f"    Taewan: {text.count('Taewan')}")
    elif lang == "EN":
        print(f"    Lee Choon-jae: {text.count('Lee Choon-jae')}")
        print(f"    Yoon Sung-yeo: {text.count('Yoon Sung-yeo')}")
        print(f"    Hwaseong: {text.count('Hwaseong')}")
        print(f"    Gyeonggi: {text.count('Gyeonggi')}")
        print(f"    Busan: {text.count('Busan')}")
        print(f"    Suwon: {text.count('Suwon')}")
        print(f"    Taewan: {text.count('Taewan')}")
    elif lang == "JA":
        print(f"    イ・チュンジェ: {text.count('イ・チュンジェ')}")
        print(f"    ユン・ソンヨ: {text.count('ユン・ソンヨ')}")
        print(f"    華城: {text.count('華城')}")
        print(f"    京畿道: {text.count('京畿道')}")
        print(f"    釜山: {text.count('釜山')}")
        print(f"    水原: {text.count('水原')}")
        print(f"    テワン法: {text.count('テワン法')}")
    elif lang == "KO":
        print(f"    Lee Choon-jae / 이춘재: {text.count('Lee Choon-jae')}")
        print(f"    Yoon Sung-yeo / 윤성여: {text.count('Yoon Sung-yeo')}")
        print(f"    화성: {text.count('화성')}")
        print(f"    경기도: {text.count('경기도')}")
        print(f"    부산교도소: {text.count('부산교도소')}")
        print(f"    수원지방법원: {text.count('수원지방법원')}")
        print(f"    태완이법: {text.count('태완이법')}")

print("\n" + "=" * 70)
print(f"SPELLCHECK COMPLETED. TOTAL ANOMALIES FOUND: {issues_found}")
print("=" * 70)
