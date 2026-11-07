# -*- coding: utf-8 -*-
"""Comprehensive Spell & Format Checker for Tap 15 and Tap 17 Scripts."""
import json, re, io, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

# Danh sách từ sai chính tả tiếng Việt thường gặp
TYPO_MAP_VN = {
    r'\bchuẩn đoán\b': 'chẩn đoán',
    r'\bxuất sứ\b': 'xuất xứ',
    r'\bsắp sếp\b': 'sắp xếp',
    r'\bsơ sài\b': 'sơ sài',  # check regex
    r'\bsơ xài\b': 'sơ sài',
    r'\bthăm quan\b': 'tham quan',
    r'\bvãng cảnh\b': 'vãn cảnh',
    r'\bbạt mạng\b': 'bạt mạng',
    r'\bchín chu\b': 'chỉn chu',
    r'\bchỉnh chu\b': 'chỉn chu',
    r'\bđọc giả\b': 'độc giả',
    r'\bgiả thuyết\b': 'giả thiết', # tuỳ ngữ cảnh
    r'\bnhậm chức\b': 'nhậm chức',
    r'\bnhận chức\b': 'nhận chức',
    r'\btựu chung\b': 'tựu trung',
    r'\bsáng lạng\b': 'xán lạn',
    r'\bxán lạng\b': 'xán lạn',
    r'\bvô hình chung\b': 'vô hình trung',
    r'\bcọ sát\b': 'cọ xát',
    r'\bcọ xát\b': 'cọ xát',
    r'\bđều đặn\b': 'đều đặn',
    r'\btỷ lệ\b': 'tỉ lệ', # cả hai đều dùng được
}

FORBIDDEN_WORDS = {
    'VN': ['máu', 'thi thể', 'xác chết', 'tự sát', 'cắt cổ', 'bóp cổ', 'khí độc', 'ngạt thở', 'đâm', 'trói', 'sát hại', 'diệt chủng', 'đầu độc', 'bỏ đói', 'móc áo'],
    'EN': ['blood', 'corpse', 'decapitat', 'strangl', 'suicide'],
    'JA': ['死体', '血液', '自殺', '首を絞', '刺殺', '毒殺'],
    'KO': ['시체', '피투', '자살', '목을 졸'],
}

def check_script(name, path, lang):
    p = Path(path)
    if not p.exists():
        print(f"[{name}] File not found: {path}")
        return
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    
    parsed = PK.parse_file(str(p))
    loi_elements = [e for e in parsed if e['kind'] == 'LOI']
    total_sents = sum(len(e.get('sentences', [])) for e in loi_elements)
    
    print(f"\n========================================================")
    print(f"KIỂM TRA: {name} ({lang})")
    print(f"Tệp: {path}")
    print(f"Số Elements: {len(parsed)} | LOI: {len(loi_elements)} | Số câu thoại: {total_sents}")
    print(f"========================================================")
    
    issues = []
    
    # 1. Kiểm tra từng dòng trong file
    for line_idx, line in enumerate(lines, 1):
        # Kiểm tra khoảng trắng trước dấu câu
        m_space_punct = re.search(r'\s+([,.:;?!])', line)
        if m_space_punct and not re.search(r'^\s*[*_#\s-]', line[:m_space_punct.start()]): # tránh markdown bullet/formatting
            issues.append((line_idx, f"Khoảng trắng thừa trước dấu câu '{m_space_punct.group(1)}'", line.strip()[:70]))
            
        # Kiểm tra dấu ba chấm (G1)
        if '...' in line or '…' in line:
            # Ngoại trừ hướng dẫn âm thanh hoặc trích dẫn đặc biệt nếu có
            issues.append((line_idx, "Dấu ba chấm '...' hoặc '…' (vi phạm G1)", line.strip()[:70]))
            
        # Kiểm tra lỗi telex gõ phím tiếng Việt
        if lang == 'VN':
            m_telex = re.search(r'\b[A-Za-zÀ-ỹĐđ]*([a-z])\1{2,}[A-Za-zÀ-ỹĐđ]*\b', line) # lặp ký tự >= 3 lần (trừ từ tượng thanh nếu có)
            if m_telex:
                issues.append((line_idx, f"Lặp ký tự nghi gõ sai: '{m_telex.group(0)}'", line.strip()[:70]))
            # Kiểm tra từ điển chính tả thường gặp
            for typo_regex, correct in TYPO_MAP_VN.items():
                if re.search(typo_regex, line, re.IGNORECASE):
                    issues.append((line_idx, f"Từ nghi sai chính tả (gợi ý: '{correct}')", line.strip()[:70]))
                    
        # Kiểm tra lặp từ liền kề
        if lang in ['VN', 'EN']:
            m_dup = re.search(r'\b([A-Za-zÀ-ỹĐđ]+)\s+\1\b', line, re.IGNORECASE)
            if m_dup and m_dup.group(1).lower() not in ['ngày', 'năm', 'tháng']: # trừ 'ngày ngày', v.v.
                issues.append((line_idx, f"Lặp từ liền kề: '{m_dup.group(0)}'", line.strip()[:70]))
                
        # Kiểm tra từ cấm V9
        for fb in FORBIDDEN_WORDS.get(lang, []):
            if lang in ['VN', 'EN']:
                if re.search(r'\b' + re.escape(fb) + r'\b', line, re.IGNORECASE):
                    issues.append((line_idx, f"Từ cấm V9: '{fb}'", line.strip()[:70]))
            else:
                if fb in line:
                    issues.append((line_idx, f"Từ cấm V9: '{fb}'", line.strip()[:70]))

    # 2. Kiểm tra câu trong parsed LOI
    # Kiểm tra dấu câu kết thúc của từng câu thoại
    for e in loi_elements:
        for s in e['sentences']:
            txt = s['text'].strip()
            sid = s['id']
            # Thiếu dấu kết câu
            if lang in ['VN', 'EN'] and not txt.endswith(('.', '?', '!', '”', '"', "'", '’', ')')):
                issues.append((sid, f"Câu không kết thúc bằng dấu chấm/hỏi/cảm: '{txt[-1]}'", txt[:60]))
            elif lang == 'JA' and not any(txt.endswith(ch) for ch in ('。', '？', '！', '」', '』', '）', ')')):
                issues.append((sid, f"Câu tiếng Nhật không kết thúc bằng 。/？/！: '{txt[-1]}'", txt[:60]))
            elif lang == 'KO' and not txt.endswith(('.', '?', '!', '”', '"', "'", '’', ')')):
                issues.append((sid, f"Câu tiếng Hàn không kết thúc bằng dấu câu chuẩn: '{txt[-1]}'", txt[:60]))

    if issues:
        print(f"-> PHÁT HIỆN {len(issues)} VẤN ĐỀ:")
        for idx, msg, snippet in issues:
            print(f"   [Dòng/Mã {idx}] {msg} -> '{snippet}'")
    else:
        print(f"-> HOÀN HẢO! 0 lỗi chính tả, 0 từ cấm, 0 lỗi dấu câu, 0 vi phạm G1/V9.")
    return len(issues)

# Chạy kiểm tra cho Tập 15 và Tập 17
targets = [
    # Tập 15
    ("Tập 15 - VN", "01_KICH_BAN/Tap15/kichban_tap15_23102026.md", "VN"),
    ("Tập 15 - EN", "01_KICH_BAN/Tap15_EN/kichban_tap15_EN.md", "EN"),
    ("Tập 15 - JA", "01_KICH_BAN/Tap15_JA/kichban_tap15_JA.md", "JA"),
    ("Tập 15 - KO", "01_KICH_BAN/Tap15_KO/kichban_tap15_KO.md", "KO"),
    # Tập 17
    ("Tập 17 - VN", "01_KICH_BAN/Tap17/kichban_tap17_23102026.md", "VN"),
    ("Tập 17 - EN", "01_KICH_BAN/Tap17_EN/kichban_tap17_EN.md", "EN"),
    ("Tập 17 - JA", "01_KICH_BAN/Tap17_JA/kichban_tap17_JA.md", "JA"),
    ("Tập 17 - KO", "01_KICH_BAN/Tap17_KO/kichban_tap17_KO.md", "KO"),
]

total_errors = 0
for name, path, lang in targets:
    errs = check_script(name, path, lang)
    if errs: total_errors += errs

print(f"\n========================================================")
print(f"TỔNG KẾT: {total_errors} vấn đề cần xử lý trên toàn bộ 8 kịch bản.")
print(f"========================================================")
