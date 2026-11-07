import sys
sys.path.insert(0, '.work')
sys.stdout.reconfigure(encoding='utf-8')
import parse_kichban

for lang, path in [
    ('VN', '01_KICH_BAN/Tap11/kichban_tap11_23102026.md'),
    ('EN', '01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md'),
    ('JA', '01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md'),
    ('KO', '01_KICH_BAN/Tap11_KO/kichban_tap11_KO.md'),
]:
    p = parse_kichban.parse_file(path)
    for e in p:
        if e.get('id') == '3.04':
            sents = e.get('sentences', [])
            for s in sents:
                if s['id'] == '3.04#6':
                    print(f"[{lang} 3.04#6] {s['text']}")
