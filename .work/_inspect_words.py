# -*- coding: utf-8 -*-
import sys, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent
t9_txt = (ROOT / '01_KICH_BAN/Tap09/kichban_tap09_23102026.md').read_text(encoding='utf-8')

vn_words = ['chàm', 'cỗi', 'hủ', 'lũng', 'mùng', 'ngoạc', 'nguệch', 'thung', 'uyên', 'đung']
for w in vn_words:
    matches = re.findall(rf'([^\n.!?]*\b{w}\b[^\n.!?]*)', t9_txt, re.IGNORECASE)
    print(f'=== Word "{w}" ({len(matches)} matches) ===')
    for m in matches:
        print('  ...', m.strip(), '...')
