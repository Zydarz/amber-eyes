# -*- coding: utf-8 -*-
"""Kiểm tra chính tả chuyên sâu cho cả Tập 10 và Tập 13."""
import sys, re, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

def audit_script(ep_num, path):
    print("=" * 70)
    print(f"BÁO CÁO KIỂM TRA CHÍNH TẢ & VĂN PHONG TẬP {ep_num}")
    print(f"Tệp: {path}")
    print("=" * 70)
    
    p = PK.parse_file(path)
    loi = [e for e in p if e['kind'] == 'LOI']
    sentences = []
    for e in loi:
        for s in e['sentences']:
            sentences.append((s['id'], e['role'], s['text']))
            
    print(f"Tổng số lượt thoại (LOI): {len(loi)}")
    print(f"Tổng số câu đọc (Sentences): {len(sentences)}")
    
    # 1. Kiểm tra lỗi khoảng trắng / dấu câu
    punct_errors = []
    for sid, role, text in sentences:
        if '  ' in text:
            punct_errors.append((sid, "Khoảng trắng kép", text))
        if re.search(r'\s[,\.\?!;:]', text):
            punct_errors.append((sid, "Khoảng trắng trước dấu ngắt câu", text))
        if re.search(r'[,;:][^\s”\"’\'\)\d]', text):
            punct_errors.append((sid, "Dấu câu không có khoảng trắng theo sau", text))
        if text.endswith((' ', '\t')):
            punct_errors.append((sid, "Khoảng trắng thừa cuối câu", text))
            
    print(f"\n1. Lỗi dấu câu và định dạng khoảng trắng: {len(punct_errors)}")
    for err in punct_errors:
        print(f"  - [{err[0]}] {err[1]}: '{err[2]}'")
        
    # 2. Kiểm tra từ cấm V9 và dấu ba chấm G1
    v9_forbidden = ['máu', 'thi thể', 'xác chết', 'tự sát', 'cắt cổ', 'bóp cổ', 'khí độc', 'ngạt thở', 'đâm', 'trói', 'sát hại', 'diệt chủng', 'đầu độc', 'bỏ đói', 'móc áo']
    v9_hits = []
    g1_hits = []
    for sid, role, text in sentences:
        for fb in v9_forbidden:
            if re.search(r'\b' + re.escape(fb) + r'\b', text, re.IGNORECASE):
                v9_hits.append((sid, fb, text))
        if '...' in text or '…' in text:
            g1_hits.append((sid, text))
            
    print(f"2. Từ cấm bạo lực V9 (A9.2): {len(v9_hits)}")
    for h in v9_hits:
        print(f"  - [{h[0]}] Từ cấm '{h[1]}' trong: '{h[2]}'")
    print(f"3. Dấu lửng giữa câu G1: {len(g1_hits)}")
    for g in g1_hits:
        print(f"  - [{g[0]}]: '{g[1]}'")
        
    # 4. Kiểm tra các lỗi chính tả phụ âm / vần / thanh điệu
    spelling_checks = [
        (r'\bxắp xếp\b', 'sắp xếp'),
        (r'\bsản suất\b', 'sản xuất'),
        (r'\bsơ xài\b', 'sơ sài'),
        (r'\bsảy ra\b', 'xảy ra'),
        (r'\bdằng xé\b', 'giằng xé'),
        (r'\bchôn dấu\b', 'chôn giấu'),
        (r'\bche dấu\b', 'che giấu'),
        (r'\bdấu giếm\b', 'giấu giếm'),
        (r'\bsử lý\b', 'xử lý'),
        (r'\bxử dụng\b', 'sử dụng'),
        (r'\bchuẩn đoán\b', 'chẩn đoán'),
        (r'\bxuất sứ\b', 'xuất xứ'),
        (r'\brạng rở\b', 'rạng rỡ'),
        (r'\bngở ngàng\b', 'ngỡ ngàng'),
        (r'\btrăn trở\b', 'trăn trở (đúng)'),
        (r'\btrăn chở\b', 'trăn trở'),
        (r'\bchăn trở\b', 'trăn trở'),
        (r'\bsơ suất\b', 'sơ suất (đúng)'),
        (r'\bsơ xuất\b', 'sơ suất'),
        (r'\bxơ suất\b', 'sơ suất'),
        (r'\bchắp vá\b', 'chắp vá (đúng)'),
        (r'\bchắp phá\b', 'chắp vá'),
        (r'\bchắt chiu\b', 'chắt chiu (đúng)'),
        (r'\bchắt lọc\b', 'chắt lọc (đúng)'),
        (r'\bchắt lọc\b', 'chắt lọc'),
        (r'\bgiành giật\b', 'giành giật (đúng)'),
        (r'\bdành giật\b', 'giành giật'),
        (r'\bđầy đọa\b', 'đày đọa / đầy đọa'),
        (r'\bđoạt mạng\b', 'đoạt mạng (đúng)'),
        (r'\bđoạt mệnh\b', 'đoạt mạng'),
    ]
    
    spell_hits = []
    for sid, role, text in sentences:
        for pat, fix in spelling_checks:
            if re.search(pat, text, re.IGNORECASE):
                if 'đúng' not in fix:
                    spell_hits.append((sid, pat, fix, text))
                    
    print(f"4. Lỗi sai từ vựng / chính tả phát hiện: {len(spell_hits)}")
    for sh in spell_hits:
        print(f"  - [{sh[0]}] '{sh[1]}' -> Sửa: '{sh[2]}'\n    Câu: {sh[3]}")
        
    return len(sentences), len(punct_errors), len(v9_hits), len(g1_hits), len(spell_hits)

s10 = audit_script("10", "01_KICH_BAN/Tap10/kichban_tap10_23102026.md")
print("\n\n")
s13 = audit_script("13", "01_KICH_BAN/Tap13/kichban_tap13_23102026.md")
