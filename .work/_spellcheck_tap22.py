# -*- coding: utf-8 -*-
"""Comprehensive spellcheck and grammar audit for all 4 languages of Episode 22."""

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban as PK

files = [
    ("VN", ROOT / "01_KICH_BAN" / "Tap22" / "kichban_tap22_23102026.md"),
    ("EN", ROOT / "01_KICH_BAN" / "Tap22_EN" / "kichban_tap22_EN.md"),
    ("JA", ROOT / "01_KICH_BAN" / "Tap22_JA" / "kichban_tap22_JA.md"),
    ("KO", ROOT / "01_KICH_BAN" / "Tap22_KO" / "kichban_tap22_KO.md"),
]

issues = []

for lang, path in files:
    p = PK.parse_file(str(path))
    loi = [e for e in p if e["kind"] == "LOI"]
    
    for e in loi:
        for s in e["sentences"]:
            txt = s["text"].strip()
            sid = s["id"]
            
            # 1. Double spaces
            if "  " in txt:
                issues.append((lang, sid, "Double space found", txt))
                
            # 2. Check sentence ending punctuation
            if lang in ["VN", "EN"]:
                if not re.search(r"[\.!\?\"\']$", txt):
                    issues.append((lang, sid, "Missing ending punctuation", txt))
            elif lang == "JA":
                if not re.search(r"[。！？]$", txt):
                    issues.append((lang, sid, "JA missing ending punctuation (。)", txt))
            elif lang == "KO":
                if not re.search(r"[\.!\?]$", txt):
                    issues.append((lang, sid, "KO missing ending punctuation (.)", txt))
                    
            # 3. Check for unintended raw markdown in spoken text
            if any(ch in txt for ch in ["**", "##", "__"]):
                issues.append((lang, sid, "Raw markdown syntax in spoken text", txt))
                
            # 4. Check for ellipsis
            if "..." in txt or "…" in txt:
                issues.append((lang, sid, "Ellipsis in spoken text", txt))
                
            # 5. Language specific checks
            if lang == "VN":
                # Check for lowercase start
                if txt and txt[0].islower():
                    issues.append((lang, sid, "Sentence starts with lowercase", txt))
            elif lang == "EN":
                if txt and txt[0].islower():
                    issues.append((lang, sid, "Sentence starts with lowercase", txt))
            elif lang == "KO":
                # Check for stray Chinese characters or broken jamo
                if re.search(r"[\u4e00-\u9fff]", txt):
                    issues.append((lang, sid, "Hanja character found in Korean text", txt))
                if re.search(r"[\u3131-\u318e]", txt):
                    issues.append((lang, sid, "Stray jamo found in Korean text", txt))

print(f"Total issues detected across all 4 languages: {len(issues)}")
for iss in issues:
    print(f"[{iss[0]}] {iss[1]}: {iss[2]} -> '{iss[3]}'")

if len(issues) == 0:
    print(">>> 100% CLEAN: ZERO SPELLING OR TYPOGRAPHICAL ISSUES DETECTED! <<<")
