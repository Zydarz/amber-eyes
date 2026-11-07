# -*- coding: utf-8 -*-
"""Word-by-word spelling analysis for Tap 15 Vietnamese script."""
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open('01_KICH_BAN/Tap15/kichban_tap15_23102026.md', encoding='utf-8') as f:
    text = f.read()

# Collect all Vietnamese syllables
words = set(re.findall(r'[A-Za-zÀ-ỹ]+', text))
print(f"Total unique words/tokens in Tap 15 VN: {len(words)}")

# Suspicious patterns:
# 1. Unusual double consonants or typos
typo_patterns = [
    r'[a-z][A-Z]', # CamelCase inside text
    r'[fwrz]',     # Non-Vietnamese letters (except in proper names / English terms)
    r'[j]',        # j except in Jodi
]

# Check words containing 'j', 'w', 'f', 'z', 'r' in odd places
english_allowed = {'Jodi', 'Arias', 'Travis', 'Alexander', 'Mesa', 'Arizona', 'California', 'Maricopa', 'Flores',
                   'Martinez', 'BGM', 'SFX', 'HOST', 'Ryan', 'Burns', 'PCL', 'R', 'Folie', 'Deux', 'Borderline',
                   'Personality', 'Disorder', 'BPD', 'Splitting', 'Gaslighting', 'The', 'Gift', 'of', 'Fear',
                   'Dehumanization', 'Compartmentalization', 'Narcissistic', 'Collapse', 'Signature', 'Modus',
                   'Operandi', 'MO', 'DNA', 'Flash', 'Memory', 'Recovery', 'Sony', 'Cyber', 'shot', 'Cancun',
                   'Mexico', 'Pasadena', 'Utah', 'Ford', 'Focus', 'FaceTime', 'YouTube', 'Amber', 'eyes'}

suspicious = []
for w in words:
    if any(c in 'fjwz' for c in w.lower()):
        if w not in english_allowed and not any(eng in w for eng in english_allowed):
            suspicious.append(w)

print("Các từ có ký tự lạ (f, j, w, z):", suspicious)

# Check lines with unusual punctuation like double dots '..' or '??' or ',,'
unusual_punct = re.findall(r'(\.\.|,,|\?\?|!!)', text)
print("Dấu câu lặp lạ:", set(unusual_punct))
