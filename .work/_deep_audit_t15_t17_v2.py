# -*- coding: utf-8 -*-
"""Refined deep audit for Tap 15 and Tap 17 scripts across all languages."""
import json, re, io, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

def audit_file(path_str, lang):
    p = Path(path_str)
    if not p.exists():
        print(f"File not found: {path_str}")
        return []
    lines = p.read_text(encoding='utf-8').splitlines()
    parsed = PK.parse_file(str(p))
    
    print(f"\n====================================================================")
    print(f"KIỂM TOÁN CHÍNH TẢ & ĐỊNH DẠNG: {p.name} [{lang}] ({p.parent.name})")
    print(f"====================================================================")
    
    errors = []
    
    # 1. Quét từng dòng
    for idx, l in enumerate(lines, 1):
        # Dấu cách trước dấu câu (trừ table markdown)
        if not l.strip().startswith('|'):
            for m in re.finditer(r'([A-Za-zÀ-ỹĐđ0-9])\s+([,.:;?!])', l):
                errors.append((idx, 'PUNCT_SPACE', f"Dấu cách thừa trước '{m.group(2)}'", l.strip()[:80]))
                
        # Dấu ba chấm vi phạm G1
        if '...' in l or '…' in l:
            errors.append((idx, 'ELLIPSIS_G1', "Chứa dấu ba chấm", l.strip()[:80]))
            
    # 2. Quét các câu thoại
    for e in parsed:
        if e['kind'] != 'LOI': continue
        role = e['role']
        eid = e['id']
        for s in e['sentences']:
            sid = s['id']
            txt = s['text'].strip()
            
            # Kiểm tra dấu kết câu chuẩn theo ngôn ngữ
            if lang in ['VN', 'EN']:
                if not txt.endswith(('.', '?', '!', '”', '"', '’', ')')):
                    errors.append((sid, 'MISSING_END_PUNCT', f"Thiếu dấu kết câu: '{txt[-1]}'", txt[:80]))
            elif lang == 'JA':
                if not any(txt.endswith(ch) for ch in ('。', '？', '！', '」', '』', '）', ')')):
                    errors.append((sid, 'MISSING_END_PUNCT', f"Thiếu dấu kết câu tiếng Nhật: '{txt[-1]}'", txt[:80]))
            elif lang == 'KO':
                if not txt.endswith(('.', '?', '!', '”', '"', '’', ')')):
                    errors.append((sid, 'MISSING_END_PUNCT', f"Thiếu dấu kết câu tiếng Hàn: '{txt[-1]}'", txt[:80]))

            # Lặp từ bất thường
            words = txt.split()
            for i in range(len(words)-1):
                w1 = words[i].strip('.,!?:;"“”‘’()[]').lower()
                w2 = words[i+1].strip('.,!?:;"“”‘’()[]').lower()
                if w1 == w2 and len(w1) > 1 and w1 not in ['ngày', 'năm', 'tháng', 'từng', 'rất', 'dần', 'song']:
                    errors.append((sid, 'WORD_DUPLICATION', f"Lặp từ liên tiếp: '{w1} {w2}'", txt[:80]))

    if not errors:
        print("-> 0 LỖI PHÁT HIỆN! File đạt chuẩn chất lượng tuyệt đối.")
    else:
        print(f"-> PHÁT HIỆN {len(errors)} VẤN ĐỀ:")
        for loc, code, desc, snip in errors:
            print(f"   [{loc}] {code}: {desc} | Trích đoạn: '{snip}'")
    return errors

print("=== KIỂM TRA TẬP 15 ===")
audit_file("01_KICH_BAN/Tap15/kichban_tap15_23102026.md", "VN")
audit_file("01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md", "EN")
audit_file("01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md", "JA")
audit_file("01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md", "KO")

print("\n=== KIỂM TRA TẬP 17 ===")
audit_file("01_KICH_BAN/Tap17/kichban_tap17_23102026.md", "VN")
audit_file("01_KICH_BAN/Tap17_EN/kichban_tap17_EN.md", "EN")
audit_file("01_KICH_BAN/Tap17_JA/kichban_tap17_JA.md", "JA")
audit_file("01_KICH_BAN/Tap17_KO/kichban_tap17_KO.md", "KO")
