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
        if e.get('id') in ('2.04', '3.02'):
            sents = e.get('sentences', [])
            print(f'=== {lang} {e.get("id")} ({len(sents)} sentences) ===')
            for s in sents[:2]:
                print(f"  {s['id']}: {s['text']}")
