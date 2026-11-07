import sys, json, re
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('01_KICH_BAN/Tap12/kichban_tap12_23102026.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract words
words = re.findall(r'[A-Za-zÀ-ỹ]+', text)
print(f"Total words in Tap 12 script: {len(words)}")

foreign_words = {
    'audio', 'podcast', 'host', 'driven', 'documentary', 'narrator', 'led',
    'dark', 'ambient', 'solo', 'cello', 'minimalist', 'piano', 'drone', 'warm', 'db',
    'jim', 'jones', 'peoples', 'temple', 'jonestown', 'guyana', 'georgetown', 'port',
    'kaituma', 'leo', 'ryan', 'christine', 'miller', 'leslie', 'wagner', 'wilson',
    'don', 'harris', 'new', 'west', 'fbi', 'rymur', 'tape', 'q', 'death', 'kool', 'aid',
    'san', 'francisco', 'indiana', 'california', 'sykes', 'matza', 'amber', 'eyes',
    'modus', 'operandi', 'signature', 'mo', 'god', 'complex', 'theory', 'mind',
    'empathy', 'deficit', 'coercive', 'persuasion', 'foot', 'door', 'sunk', 'cost',
    'halo', 'effect', 'red', 'flags', 'gift', 'fear', 'gavin', 'de', 'becker',
    'flac16', 'sdsu', 'scheeres', 'reiterman', 'zimbardo', 'poa', 'aum',
    'act', 'n1', 'n2', 'brief', 'format', 'bgm', 'sfx', 'nghi', 'loi', 'white', 'nights',
    'house', 'foreign', 'affairs', 'committee', 'report', 'no', 'vault', 'the'
}

# Check unusual syllables or non-Vietnamese letters
unusual_words = []
for w in set(words):
    if w.lower() in foreign_words:
        continue
    if re.search(r'[fjwz]', w, re.IGNORECASE):
        unusual_words.append(w)
print(f"Words with non-Vietnamese letters: {unusual_words}")

# Unique Vietnamese words
unique_vn = sorted(set(w.lower() for w in words if w.lower() not in foreign_words and not re.search(r'[fjwz]', w, re.IGNORECASE)))
print(f"Unique Vietnamese syllables: {len(unique_vn)}")

# Check rare syllables (appearing once)
counts = Counter(w.lower() for w in words if w.lower() not in foreign_words)
rare = [w for w, c in counts.items() if c == 1]
print(f"Rare syllables appearing once: {len(rare)}")

# Print rare syllables
for i in range(0, len(rare), 50):
    print(f"{i}-{i+50}:", ", ".join(rare[i:i+50]))

