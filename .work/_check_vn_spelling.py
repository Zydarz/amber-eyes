# -*- coding: utf-8 -*-
import io, sys, re
from pathlib import Path
from collections import Counter

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_vn_words(path_str):
    text = Path(path_str).read_text(encoding='utf-8')
    # Filter out code/metadata/markdown markers
    # split into words
    words = re.findall(r'[a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]+', text)
    print(f"\nUnique words in {path_str}: {len(set(w.lower() for w in words))}")
    
    # Check for words with suspicious character combinations
    suspicious = []
    for w in set(words):
        wl = w.lower()
        # common typos in typing telex: 's', 'r', 'x', 'f', 'j' at end of words or double accents
        if re.search(r'[a-z][fjsrwz]$', wl) and wl not in ['travis', 'alexander', 'arias', 'martinez', 'nurmi', 'mesa', 'california', 'perris', 'turpin', 'jodi', 'david', 'louise', 'jordan', 'flores', 'springville', 'utah', 'hughes', 'borden', 'alex', 'carl', 'show', 'view', 'sfx', 'bgm', 'act', 'host', 'dvd', 'tv', 'gps', 'dna', 'mo', 'fbi', 'cop', 'bang', 'clip']:
            suspicious.append(w)
    print(f"Suspicious ends: {suspicious}")

check_vn_words('01_KICH_BAN/Tap15/kichban_tap15_23102026.md')
check_vn_words('01_KICH_BAN/Tap17/kichban_tap17_23102026.md')
