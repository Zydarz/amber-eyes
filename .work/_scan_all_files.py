# -*- coding: utf-8 -*-
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

files_to_check = [
    '01_KICH_BAN/Tap10/kichban_tap10_23102026.md',
    '01_KICH_BAN/Tap10/NghienCuu_TamLy_BoSung_KichBan_Tap10.md',
    r'C:\Users\ADMIN\AppData\Local\Google\antigravity\brain\ef8034a9-4598-4e44-b04a-9f83c79b0401\NghienCuu_TamLy_Tap10.md',
    r'C:\Users\ADMIN\.gemini\antigravity\brain\ef8034a9-4598-4e44-b04a-9f83c79b0401\NghienCuu_TamLy_Tap10.md'
]

import os
existing = [f for f in files_to_check if os.path.exists(f)]

for path in existing:
    print(f"\n==========================================")
    print(f"QUÉT TỆP: {path}")
    print(f"==========================================")
    with open(path, 'r', encoding='utf-8') as fp:
        lines = fp.readlines()
        
    for idx, line in enumerate(lines):
        line_num = idx + 1
        s = line.strip()
        if not s:
            continue
            
        # 1. Missing space between two words (e.g. word1word2 where word1 is lower and word2 is lower, but no space)
        # Check specific joined words
        for bad in ['thờơ', 'quáđỗi', 'sựcứu', 'thựctại', 'ngườimẹ', 'ngườicha', 'ngườiđàn', 'nạnnhân']:
            if bad in s.lower():
                print(f"  [L{line_num}] Dính chữ: '{bad}' trong \"{s}\"")
                
        # 2. Double spaces
        if '  ' in s and not s.startswith('#') and not s.endswith('  '):
            # In markdown, trailing 2 spaces is a line break, so check middle double spaces
            mid = s.rstrip()
            if '  ' in mid:
                print(f"  [L{line_num}] Khoảng trắng kép: \"{mid}\"")
                
        # 3. Space before punctuation
        m = re.search(r'\s+[,.:;?!]', s)
        if m:
            print(f"  [L{line_num}] Khoảng trắng trước dấu câu: '{m.group()}' trong \"{s}\"")
            
        # 4. Ellipsis
        if '...' in s or '…' in s:
            print(f"  [L{line_num}] Dấu ba chấm vi phạm G1: \"{s}\"")
            
        # 5. Common spelling mistakes
        for pat, err_name in [
            (r'\bchuẩn đoán\b', 'chẩn đoán'),
            (r'\bsơ xuất\b', 'sơ suất'),
            (r'\bxuất sứ\b', 'xuất xứ'),
            (r'\bgiành cho\b', 'dành cho'),
            (r'\bgiành riêng\b', 'dành riêng'),
            (r'\bdãy dụa\b', 'giãy giụa'),
            (r'\bchăn trở\b', 'trăn trở'),
            (r'\bhụt hẫn\b', 'hụt hẫng'),
            (r'\bbàng hoảng\b', 'bàng hoàng'),
            (r'\btàn cốc\b', 'tàn khốc'),
            (r'\bman rợn\b', 'man rợ'),
            (r'\btựu chung\b', 'tựu trung'),
            (r'\bcứu dỗi\b', 'cứu rỗi'),
            (r'\bcắn dứt\b', 'cắn rứt'),
            (r'\bngỡ ngàn\b', 'ngỡ ngàng'),
            (r'\btrấn thương\b', 'chấn thương'),
            (r'\bchân trọng\b', 'trân trọng'),
            (r'\bthấu xuất\b', 'thấu suốt'),
            (r'\bxuy nghĩ\b', 'suy nghĩ'),
            (r'\bxâu sắc\b', 'sâu sắc'),
            (r'\bxâu xa\b', 'sâu xa'),
        ]:
            if re.search(pat, s, re.IGNORECASE):
                print(f"  [L{line_num}] Sai chính tả '{err_name}': \"{s}\"")
