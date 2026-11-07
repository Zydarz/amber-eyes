# -*- coding: utf-8 -*-
"""Apply orthographical and typographical fixes to Tap 15 and Tap 18 scripts."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

# --- FIX TAP 15 VN ---
p15_vn = '01_KICH_BAN/Tap15/kichban_tap15_23102026.md'
with open(p15_vn, encoding='utf-8') as f:
    t15_vn = f.read()

# Fix 1: RUỘNG BỎ -> RUỒNG BỎ
t15_vn = t15_vn.replace('CƠN CUỒNG NỘ RUỘNG BỎ', 'CƠN CUỒNG NỘ RUỒNG BỎ')
# Fix 2: Tái hiện hiện trường -> Tái hiện bối cảnh hiện trường
t15_vn = t15_vn.replace('tái hiện hiện trường', 'tái hiện bối cảnh hiện trường')
# Fix 3: SFX Cốp... cốp... cốp
t15_vn = t15_vn.replace('Tiếng búa gỗ của thẩm phán gõ đanh thép "Cốp... cốp... cốp", tiếng xì xào của phòng xử án.',
                        'Tiếng búa gỗ của thẩm phán gõ ba tiếng đanh thép dứt khoát, tiếng xì xào của phòng xử án.')

with open(p15_vn, 'w', encoding='utf-8') as f:
    f.write(t15_vn)
print(f"Fixed Tap 15 VN: {p15_vn}")

# --- FIX TAP 15 EN ---
for p15_en in ['01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md', '01_KICH_BAN/Tap15/kichban_tap15_EN.md']:
    with open(p15_en, encoding='utf-8') as f:
        t15_en = f.read()
    t15_en = t15_en.replace('"Bang... bang... bang"', 'three times with authoritative finality')
    t15_en = t15_en.replace('“Bang... bang... bang”', 'three times with authoritative finality')
    t15_en = t15_en.replace('The judge’s wooden gavel strikes authoritatively three times "Bang... bang... bang", murmurs fill the courtroom.',
                            'The judge’s wooden gavel strikes three times with authoritative finality, murmurs fill the courtroom.')
    with open(p15_en, 'w', encoding='utf-8') as f:
        f.write(t15_en)
    print(f"Fixed Tap 15 EN: {p15_en}")

# --- FIX TAP 15 JA ---
p15_ja = '01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md'
with open(p15_ja, encoding='utf-8') as f:
    t15_ja = f.read()
t15_ja = t15_ja.replace('「カン…カン…カン」', '')
t15_ja = t15_ja.replace('裁判長の木槌が威厳をもって3度響く音、傍聴席のざわめき。',
                        '裁判長の木槌が威厳をもって3度きっぱりと響く音、傍聴席のざわめき。')
with open(p15_ja, 'w', encoding='utf-8') as f:
    f.write(t15_ja)
print(f"Fixed Tap 15 JA: {p15_ja}")

# --- FIX TAP 15 KO ---
p15_ko = '01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md'
with open(p15_ko, encoding='utf-8') as f:
    t15_ko = f.read()
t15_ko = t15_ko.replace('"탕... 탕... 탕"', '')
t15_ko = t15_ko.replace('판사의 법봉이 단호하게 세 번 울리는 소리, 방청석에서 웅성거리는 탄식.',
                        '판사의 법봉이 단호하게 세 번 울리는 소리, 방청석에서 웅성거리는 탄식.')
with open(p15_ko, 'w', encoding='utf-8') as f:
    f.write(t15_ko)
print(f"Fixed Tap 15 KO: {p15_ko}")

# --- FIX TAP 18 VN ---
p18_vn = '01_KICH_BAN/Tap18/kichban_tap18_23102026.md'
with open(p18_vn, encoding='utf-8') as f:
    t18_vn = f.read()

# Fix ellipsis in line 238
t18_vn = t18_vn.replace('‘Chúa Giê-su biết rằng không ai bị hại oan ức cả... các con tôi đang bận rộn và hạnh phúc ở thế giới bên kia’',
                        '‘Chúa Giê-su biết rằng không ai bị hại oan ức cả – các con tôi đang bận rộn và hạnh phúc ở thế giới bên kia’')

with open(p18_vn, 'w', encoding='utf-8') as f:
    f.write(t18_vn)
print(f"Fixed Tap 18 VN: {p18_vn}")

# Reparse and re-verify parity for both episodes
for ep, files in [
    ('Tap15', [('VN', '01_KICH_BAN/Tap15/kichban_tap15_23102026.md'),
               ('EN', '01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md'),
               ('JA', '01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md'),
               ('KO', '01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md')]),
    ('Tap18', [('VN', '01_KICH_BAN/Tap18/kichban_tap18_23102026.md'),
               ('EN', '01_KICH_BAN/Tap18_EN/kichban_tap18_EN.md'),
               ('JA', '01_KICH_BAN/Tap18_JA/kichban_tap18_JA.md'),
               ('KO', '01_KICH_BAN/Tap18_KO/kichban_tap18_KO.md')]),
]:
    print(f"\n=== VERIFYING PARITY FOR {ep} ===")
    parsed = {}
    for lang, path in files:
        out_json = f".work/script_{ep.lower()}" + ("" if lang=="VN" else f"_{lang}") + ".json"
        els = PK.parse_file(path, out_json)
        loi = [e for e in els if e['kind'] == 'LOI']
        s_cnt = sum(len(e['sentences']) for e in loi)
        parsed[lang] = els
        print(f"  {lang:4}: elements={len(els)}, LOI={len(loi)}, sentences={s_cnt}")
    
    vn_els = parsed['VN']
    all_ok = True
    for lang in ['EN', 'JA', 'KO']:
        target_els = parsed[lang]
        if len(target_els) != len(vn_els):
            all_ok = False
            continue
        for i, (ve, te) in enumerate(zip(vn_els, target_els)):
            if ve['kind'] != te['kind'] or (ve['kind']=='LOI' and (ve['role']!=te['role'] or len(ve['sentences'])!=len(te['sentences']))):
                all_ok = False
    print(f"  Result: {'100% PARITY OK' if all_ok else 'PARITY MISMATCH'}")
