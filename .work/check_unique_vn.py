# -*- coding: utf-8 -*-
"""Check all 1208 unique words in Vietnamese script for spelling errors."""

import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open(".work/all_sentences_vn.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Filter out sentence IDs and header tags
lines = [l for l in text.splitlines() if l.startswith("[")]
clean_text = " ".join([l.split(":", 1)[1] for l in lines if ":" in l])

words = re.findall(r'[a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]+', clean_text)
unique_words = sorted(list(set(w.lower() for w in words)))

# Known English / Proper nouns
known_foreign = {
    "stephen", "mcdaniel", "lauren", "giddings", "mercer", "macon", "georgia",
    "barristers", "hall", "wgxa", "freeze", "response", "predatory", "stalking",
    "voyeurism", "precipitating", "stressor", "compartmentalization", "pathological",
    "self", "pity", "narcissistic", "collapse", "the", "gift", "of", "fear",
    "gavin", "de", "becker", "howard", "simms", "bibb", "atlanta", "amber", "eyes"
}

# Simple heuristic check for valid Vietnamese syllables:
# Vietnamese syllable structure: [C1] [W] V [C2] + Tone
# Let's inspect words that look suspicious or foreign
non_standard = []
for w in unique_words:
    if w in known_foreign:
        continue
    # If contains characters not standard in Vietnamese orthography (f, j, w, z)
    if any(c in w for c in "fjwz"):
        non_standard.append((w, "contains f/j/w/z"))
    # Check if ends with consonant other than c, ch, m, n, ng, nh, p, t
    # Vietnamese finals: c, ch, m, n, ng, nh, p, t
    # If not ending in vowel or valid final
    # Let's list words that might be misspelled

print(f"Total words: {len(words)}, Unique: {len(unique_words)}")
print("Non standard words flagged:", non_standard)

# Let's dump all unique words to a file so we can scan them
with open(".work/unique_words_vn.txt", "w", encoding="utf-8") as out:
    for i, w in enumerate(unique_words):
        out.write(f"{w}\n")

print("Saved unique words to .work/unique_words_vn.txt")
