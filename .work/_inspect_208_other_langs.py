import sys, json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

for lang, path in [('EN', '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md'),
                   ('JA', '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md'),
                   ('KO', '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md')]:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    print(f"\n=== {lang} 2.08 ===")
    lines = text.splitlines()
    in_208 = False
    for line in lines:
        if '2.08' in line or 'ĐIỀU TRA VIÊN' in line or 'INVESTIGATOR' in line or '捜査官' in line or '수사관' in line:
            if '2.08' in line or '2.08' in prev_line:
                in_208 = True
        if in_208:
            if line.startswith('**') and '2.08' not in line and not line.startswith('**INVESTIGATOR') and not line.startswith('**捜査官') and not line.startswith('**수사관'):
                break
            if line.strip():
                print(line)
        prev_line = line
