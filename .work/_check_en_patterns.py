# -*- coding: utf-8 -*-
import sys, io, re, urllib.request

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('.work/_en_vocab_tap10.txt', 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f if line.strip()]

# Check for suspicious letter patterns in English
suspicious = []
for w in words:
    wl = w.lower()
    # triple letters e.g. 'lll', 'eee'
    if re.search(r'([a-z])\1\1', wl):
        suspicious.append((w, "Triple repeated letter"))
    # q not followed by u
    if re.search(r'q(?!u)', wl):
        suspicious.append((w, "q without u"))
    # apostrophe at weird place
    if "'" in w:
        if not re.search(r"^[a-zA-Z]+'[a-zA-Z]+$", w):
            suspicious.append((w, "Weird apostrophe"))

print(f"Suspicious English words: {len(suspicious)}")
for s in suspicious:
    print(f"  {s[0]}: {s[1]}")
