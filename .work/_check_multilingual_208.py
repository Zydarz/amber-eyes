import sys
sys.path.insert(0, '.work')
sys.stdout.reconfigure(encoding='utf-8')
import parse_kichban

for lang, path in [
    ('VN', '01_KICH_BAN/Tap10/kichban_tap10_23102026.md'),
    ('EN', '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md'),
    ('JA', '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md'),
    ('KO', '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md'),
]:
    res = parse_kichban.parse_file(path)
    for e in res:
        if e.get('id') == '2.08':
            sents = e.get('sentences', [])
            print(f'=== {lang} 2.08 ({len(sents)} sentences) ===')
            for s in sents:
                print(f"  {s.get('id')}: {s.get('text')}")
