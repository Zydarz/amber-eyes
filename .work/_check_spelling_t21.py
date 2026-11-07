# -*- coding: utf-8 -*-
"""Check spelling and punctuation anomalies across all 4 script files of Episode 21."""

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parent.parent

paths = {
    "VN": ROOT / "01_KICH_BAN" / "Tap21" / "kichban_tap21_23102026.md",
    "EN": ROOT / "01_KICH_BAN" / "Tap21_EN" / "kichban_tap21_EN.md",
    "JA": ROOT / "01_KICH_BAN" / "Tap21_JA" / "kichban_tap21_JA.md",
    "KO": ROOT / "01_KICH_BAN" / "Tap21_KO" / "kichban_tap21_KO.md",
}

for lang, p in paths.items():
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    print(f"\n--- SPELLING & SYNTAX AUDIT: {lang} ({len(lines)} lines, {len(text)} chars) ---")
    
    # 1. Trailing spaces
    trailing = [i + 1 for i, line in enumerate(lines) if line.endswith(" ") or line.endswith("\t")]
    print(f"Lines with trailing whitespace: {len(trailing)}")
    
    # 2. Punctuation spacing anomalies (e.g., " ,", " .")
    punct_space = []
    for i, line in enumerate(lines):
        if re.search(r'\s+[,.!?:;]', line):
            punct_space.append((i + 1, line))
    print(f"Punctuation with leading space (e.g. ' ,'): {len(punct_space)}")
    for ln, l in punct_space[:5]:
        print(f"  Line {ln}: {l}")
        
    # 3. Repeated consecutive identical words (e.g., "trong trong", "the the")
    dup_words = []
    for i, line in enumerate(lines):
        if line.startswith("#") or line.startswith("*") or line.startswith("|"):
            continue
        m = re.findall(r'\b([A-Za-zÀ-ỹ가-힣]+)\s+\1\b', line, re.IGNORECASE)
        if m:
            dup_words.append((i + 1, m, line))
    print(f"Consecutive duplicated words: {len(dup_words)}")
    for ln, w, l in dup_words:
        print(f"  Line {ln}: duplicated {w} in '{l}'")
        
    # 4. Check unmatched parentheses, brackets, or quotes
    unmatched = []
    for i, line in enumerate(lines):
        for op, cl in [("(", ")"), ("[", "]"), ("{", "}"), ("“", "”"), ("「", "」"), ("『", "』")]:
            if line.count(op) != line.count(cl):
                unmatched.append((i + 1, f"{op}...{cl}", line))
    print(f"Unmatched brackets/quotes: {len(unmatched)}")
    for ln, b, l in unmatched[:5]:
        print(f"  Line {ln}: unmatched {b} in '{l}'")

print("\nAll spelling and syntax checks complete.")
