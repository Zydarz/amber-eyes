# -*- coding: utf-8 -*-
"""Comprehensive spellcheck and typographical audit for Tap 15 (VN, EN, JA, KO)."""
import sys, re, unicodedata
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files_t15 = {
    'VN': '01_KICH_BAN/Tap15/kichban_tap15_23102026.md',
    'EN': '01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md',
    'JA': '01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md',
    'KO': '01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md',
}

print("=== 1. KIỂM TRA PARITY VÀ PARSE CẤU TRÚC TẬP 15 ===")
parsed = {}
for lang, path in files_t15.items():
    els = PK.parse_file(path)
    loi = [e for e in els if e['kind'] == 'LOI']
    s_cnt = sum(len(e['sentences']) for e in loi)
    parsed[lang] = els
    print(f"  {lang:4}: elements={len(els)}, LOI={len(loi)}, sentences={s_cnt}")

vn_els = parsed['VN']
parity_ok = True
for lang in ['EN', 'JA', 'KO']:
    target_els = parsed[lang]
    if len(target_els) != len(vn_els):
        print(f"  MISMATCH element count {lang}: {len(target_els)} vs {len(vn_els)}")
        parity_ok = False
        continue
    for i, (ve, te) in enumerate(zip(vn_els, target_els)):
        eid = ve['id']
        if ve['kind'] != te['kind']:
            print(f"  MISMATCH kind at {eid} ({lang}): {te['kind']} vs {ve['kind']}")
            parity_ok = False
        if ve['kind'] == 'LOI':
            if ve['role'] != te['role']:
                print(f"  MISMATCH role at {eid} ({lang}): {te['role']} vs {ve['role']}")
                parity_ok = False
            vc = len(ve['sentences'])
            tc = len(te['sentences'])
            if vc != tc:
                print(f"  MISMATCH sentences at {eid} ({lang}): {tc} vs VN={vc}")
                parity_ok = False
        elif ve['kind'] == 'NGHI':
            if ve.get('sec') != te.get('sec'):
                print(f"  MISMATCH pause sec at {eid} ({lang}): {te.get('sec')} vs VN={ve.get('sec')}")
                parity_ok = False

if parity_ok:
    print("  -> PARITY 1:1: 100% HOÀN HẢO QUA CẢ 4 NGÔN NGỮ!")
else:
    print("  -> CẢNH BÁO: CÓ LỆCH PARITY!")

print("\n=== 2. KIỂM TRA ĐỊNH DẠNG, KHOẢNG TRẮNG VÀ DẤU CÂU TẬP 15 ===")
for lang, path in files_t15.items():
    with open(path, encoding='utf-8') as f:
        text = f.read()
    
    # Unicode NFC check
    nfc_text = unicodedata.normalize('NFC', text)
    is_nfc = (text == nfc_text)
    
    lines = text.splitlines()
    non_table_lines = [l for l in lines if not l.strip().startswith('|')]
    non_table = '\n'.join(non_table_lines)
    
    # Check space before punctuation
    space_before_punct = re.findall(r'\s+[,.?!;:]', non_table)
    # Check punctuation without space after (Latin/Korean)
    if lang in ['VN', 'EN', 'KO']:
        punct_no_space = re.findall(r'[,;:][A-Za-zÀ-ỹ가-힣]', non_table)
    else:
        punct_no_space = []
        
    double_spaces = re.findall(r'[^\S\r\n]{2,}', non_table)
    
    # Quotes
    curled_single_diff = text.count('‘') - text.count('’')
    curled_double_diff = text.count('“') - text.count('”')
    straight_single = text.count("'")
    straight_double = text.count('"')
    
    print(f"--- {lang} ---")
    print(f"  Unicode NFC: {'OK' if is_nfc else 'CẦN CHUẨN HÓA'}")
    print(f"  Khoảng trắng kép: {len(double_spaces)}")
    print(f"  Khoảng trắng trước dấu câu: {len(space_before_punct)} -> {space_before_punct[:5]}")
    print(f"  Dấu câu thiếu khoảng trắng sau: {len(punct_no_space)} -> {punct_no_space[:5]}")
    print(f"  Dấu nháy: ‘-’={curled_single_diff}, “-”={curled_double_diff}, straight '={straight_single}, straight \"={straight_double}")

print("\n=== 3. KIỂM TRA TỪ CẤM V9 (TIÊU CHUẨN A9.2) TRÊN BẢN VN TẬP 15 ===")
with open(files_t15['VN'], encoding='utf-8') as f:
    vn_text = f.read().lower()

banned = ['máu', 'thi thể', 'sát hại', 'đòn', 'trói', 'bầm', 'đập', 'đầu độc', 'diệt cỏ', 'bỏ đói', 'móc áo']
found_banned = {}
for w in banned:
    cnt = vn_text.count(w)
    if cnt > 0:
        found_banned[w] = cnt

print("  Từ cấm V9 tìm thấy:", found_banned if found_banned else "0 (HOÀN TOÀN SẠCH)")
