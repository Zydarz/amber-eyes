# -*- coding: utf-8 -*-
"""Deep orthographic and stylistic audit for Tap 15 and Tap 17 scripts."""
import json, re, io, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

def audit_file(path_str):
    p = Path(path_str)
    if not p.exists():
        print(f"File not found: {path_str}")
        return
    lines = p.read_text(encoding='utf-8').splitlines()
    parsed = PK.parse_file(str(p))
    
    print(f"\n====================================================================")
    print(f"KIỂM TOÁN CHÍNH TẢ & ĐỊNH DẠNG: {p.name} ({p.parent.name})")
    print(f"====================================================================")
    
    errors = []
    
    # 1. Quét dấu cách bất thường
    for idx, l in enumerate(lines, 1):
        # Dấu cách trước dấu câu (trừ table markdown)
        if not l.strip().startswith('|'):
            for m in re.finditer(r'([A-Za-zÀ-ỹĐđ0-9])\s+([,.:;?!])', l):
                errors.append((idx, 'PUNCT_SPACE', f"Dấu cách trước '{m.group(2)}'", l.strip()[:80]))
        # Thiếu dấu cách sau dấu phẩy (trừ số thập phân, giờ)
        for m in re.finditer(r'([A-Za-zÀ-ỹĐđ]),([A-Za-zÀ-ỹĐđ])', l):
            errors.append((idx, 'NO_SPACE_COMMA', f"Thiếu dấu cách sau dấu phẩy '{m.group(0)}'", l.strip()[:80]))
            
        # Lỗi dấu ngoặc kép lệch hoặc dấu nháy không chuẩn
        # Dấu ba chấm
        if '...' in l or '…' in l:
            errors.append((idx, 'ELLIPSIS_G1', "Chứa dấu ba chấm", l.strip()[:80]))
            
    # 2. Quét từ lặp và từ nghi vấn trong các câu thoại parsed
    for e in parsed:
        if e['kind'] != 'LOI': continue
        role = e['role']
        eid = e['id']
        for s in e['sentences']:
            sid = s['id']
            txt = s['text']
            words = txt.split()
            
            # Lặp từ liên tiếp
            for i in range(len(words)-1):
                w1 = words[i].strip('.,!?:;"“”‘’()[]').lower()
                w2 = words[i+1].strip('.,!?:;"“”‘’()[]').lower()
                if w1 == w2 and len(w1) > 1 and w1 not in ['ngày', 'năm', 'tháng', 'từng', 'rất']:
                    errors.append((sid, 'WORD_DUPLICATION', f"Lặp từ liên tiếp: '{w1} {w2}'", txt[:80]))
                    
            # Dấu kết câu
            if not txt.endswith(('.', '?', '!', '”', '"', '’', ')')):
                errors.append((sid, 'MISSING_END_PUNCT', f"Thiếu dấu kết câu", txt[-30:]))
                
    if not errors:
        print("-> 0 lỗi phát hiện! File hoàn toàn sạch sẽ.")
    else:
        print(f"-> Phát hiện {len(errors)} vấn đề:")
        for loc, code, desc, snip in errors:
            print(f"   [{loc}] {code}: {desc} | Trích đoạn: '{snip}'")
    return errors

print("=== QUÉT TẬP 15 ===")
audit_file("01_KICH_BAN/Tap15/kichban_tap15_23102026.md")
audit_file("01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md")
audit_file("01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md")
audit_file("01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md")

print("\n=== QUÉT TẬP 17 ===")
audit_file("01_KICH_BAN/Tap17/kichban_tap17_23102026.md")
audit_file("01_KICH_BAN/Tap17_EN/kichban_tap17_EN.md")
audit_file("01_KICH_BAN/Tap17_JA/kichban_tap17_JA.md")
audit_file("01_KICH_BAN/Tap17_KO/kichban_tap17_KO.md")
