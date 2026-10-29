import re, io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

text = open('01_KICH_BAN/Tap04/kichban_tap04_23102026.md', encoding='utf-8').read()

matches = re.findall(r'\b[A-Za-z0-9]+\.\s+[A-ZÀ-ỸĐ]', text)
print("Matches of word. Capital:", matches)

# Check all occurrences of . in text that are not end of sentence
for i, line in enumerate(text.splitlines(), 1):
    m = re.findall(r'([A-Za-z0-9À-ỹ]+\.[A-Za-z0-9À-ỹ\s]+)', line)
    # look specifically for single letter or title abbr like St., Dr., Mr., etc.
    abbr = re.findall(r'\b(St|Dr|Mr|Mrs|Ms|Prof|Rev|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec|Jr|Sr)\.\s*', line, re.I)
    if abbr:
        print(f"L{i}: Abbreviation found: {abbr} in: {line.strip()}")
