import re

files = [
    ('VN', '01_KICH_BAN/Tap33/kichban_tap33_19112026.md'),
    ('EN', '01_KICH_BAN/Tap33_EN/kichban_tap33_EN.md'),
    ('JA', '01_KICH_BAN/Tap33_JA/kichban_tap33_JA.md')
]

for lang, fn in files:
    lines = open(fn, encoding='utf-8').readlines()
    speech = [l.strip() for l in lines if not l.startswith(('#', '*', '|', '[', '-')) and l.strip()]
    no_end = [l for l in speech if not l.endswith(':') and not re.search(r'[.!?。！？\x22\x27\u201d\u2019]$', l)]
    print(lang, 'true speech lines without ending punctuation:', len(no_end))
    if no_end:
        for x in no_end[:5]:
            print('  ->', repr(x))
