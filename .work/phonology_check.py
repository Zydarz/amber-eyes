# -*- coding: utf-8 -*-
"""Check Vietnamese words against standard Vietnamese phonology and patterns."""

import sys, re
sys.stdout.reconfigure(encoding="utf-8")

with open(".work/unique_words_vn.txt", "r", encoding="utf-8") as f:
    words = [line.strip() for line in f if line.strip()]

known_foreign = {
    "stephen", "mcdaniel", "lauren", "giddings", "mercer", "macon", "georgia",
    "barristers", "hall", "wgxa", "freeze", "response", "predatory", "stalking",
    "voyeurism", "precipitating", "stressor", "compartmentalization", "pathological",
    "self", "pity", "narcissistic", "collapse", "the", "gift", "of", "fear",
    "gavin", "de", "becker", "howard", "simms", "bibb", "atlanta", "amber", "eyes",
    "web", "video", "radar", "camera", "tông"
}

# Standard Vietnamese finals
valid_finals = ("c", "ch", "m", "n", "ng", "nh", "p", "t", "a", "e", "ê", "i", "o", "ô", "ơ", "u", "ư", "y",
                "à", "á", "ả", "ã", "ạ", "ă", "ằ", "ắ", "ẳ", "ẵ", "ặ", "â", "ầ", "ấ", "ẩ", "ẫ", "ậ",
                "è", "é", "ẻ", "ẽ", "ẹ", "ề", "ế", "ể", "ễ", "ệ", "ì", "í", "ỉ", "ĩ", "ị",
                "ò", "ó", "ỏ", "õ", "ọ", "ô", "ồ", "ố", "ổ", "ỗ", "ộ", "ơ", "ờ", "ớ", "ở", "ỡ", "ợ",
                "ù", "ú", "ủ", "ũ", "ụ", "ư", "ừ", "ứ", "ử", "ữ", "ự", "ỳ", "ý", "ỷ", "ỹ", "ỵ")

unusual = []
for w in words:
    if w in known_foreign:
        continue
    # Check if end char is valid
    if not w.endswith(valid_finals):
        unusual.append((w, "invalid final letter"))

print(f"Unusual final endings: {unusual}")

# Now let's print all words in chunks to inspect them visually
print(f"Total words to review: {len(words)}")
