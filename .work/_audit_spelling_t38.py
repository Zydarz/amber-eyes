# -*- coding: utf-8 -*-
"""
Audit chính tả và ngôn ngữ cho Tập 38 trên cả 3 thứ tiếng: Tiếng Việt, Tiếng Anh, Tiếng Nhật.
"""
import sys, os, re, json
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(r"d:\TEST\Gax\amber-eyes")

def audit_vn():
    print("="*60)
    print("1. KIỂM TRA CHÍNH TẢ & NGÔN NGỮ TIẾNG VIỆT (Tap 38 VN)")
    print("="*60)
    vn_file = ROOT / "01_KICH_BAN" / "Tap38" / "kichban_tap38_19112026.md"
    content = vn_file.read_text(encoding="utf-8")
    
    # 1. Từ lặp liên tiếp
    dup_words = re.findall(r'\b([a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]+)\s+\1\b', content, re.IGNORECASE)
    intentional = {'chầm', 'rôm', 'lách', 'không', 'ròng', 'bíp'}
    real_dups = [w for w in dup_words if w.lower() not in intentional]
    print(f"Từ lặp liên tiếp bất thường (VN): {real_dups if real_dups else '0 lỗi'}")
    
    # 2. Ngoặc và dấu trích dẫn
    open_curly_quotes = content.count('“') - content.count('”')
    open_straight_quotes = content.count('"') % 2
    open_parens = content.count('(') - content.count(')')
    print(f"Kiểm tra ngoặc: “ ” lệch = {open_curly_quotes}, \" chẵn lẻ = {open_straight_quotes}, ( ) lệch = {open_parens}")
    
    # 3. Lỗi chính tả tiếng Việt thường gặp
    typo_patterns = [
        (r'\bchuẩn đoán\b', 'chẩn đoán'),
        (r'\bxắp xếp\b', 'sắp xếp'),
        (r'\bsử lí\b', 'xử lý'),
        (r'\bgiành giật\b', 'giành giật/tranh giành'),
        (r'\bxuất xắc\b', 'xuất sắc'),
        (r'\bchính chắn\b', 'chín chắn'),
        (r'\bchần chừ\b', 'chần chừ'),
        (r'\bngoan nghoãn\b', 'ngoan ngoãn'),
        (r'\bsuy xụp\b', 'suy sụp'),
        (r'\bxơ xác\b', 'xơ xác'),
        (r'\bmanh manh\b', 'manh manh'),
        (r'\bsát nhân\b', 'sát nhân'),
        (r'\blảng vảng\b', 'lảng vảng'),
        (r'\btrần trừ\b', 'chần chừ'),
    ]
    for pat, corr in typo_patterns:
        m = re.findall(pat, content, re.IGNORECASE)
        if m:
            print(f"  Phát hiện: {m} -> gợi ý: {corr}")

    # 4. Khoảng trắng thừa trước dấu câu
    space_before_punct = re.findall(r'\s+([,.:;?!])', content)
    print(f"Khoảng trắng thừa trước dấu câu: {len(space_before_punct)} lỗi")

    # 5. Dấu câu cuối dòng trong hội thoại
    lines = content.splitlines()
    no_punct = []
    in_dialogue = False
    for idx, line in enumerate(lines, 1):
        l = line.strip()
        if l.startswith('**HOST**') or l.startswith('**ĐIỀU TRA') or l.startswith('**CHUYÊN') or l.startswith('**NGƯỜI'):
            in_dialogue = True
            continue
        if l.startswith('**[') or l.startswith('#') or l.startswith('---') or not l:
            in_dialogue = False
            continue
        if in_dialogue:
            if not l.endswith(('.', '!', '?', '”', '"', '…', ':')):
                no_punct.append((idx, l))
    print(f"Câu thoại thiếu dấu kết câu (VN): {len(no_punct)}")
    for line_no, l in no_punct:
        print(f"  Dòng {line_no}: {l}")

def audit_en():
    print("\n" + "="*60)
    print("2. KIỂM TRA CHÍNH TẢ & NGÔN NGỮ TIẾNG ANH (Tap 38 EN)")
    print("="*60)
    en_file = ROOT / "01_KICH_BAN" / "Tap38_EN" / "kichban_tap38_EN.md"
    content = en_file.read_text(encoding="utf-8")
    
    # 1. Duplicate words
    dup_en = re.findall(r'\b(the|and|to|in|of|that|is|was|for|on|with|as|at|by|this|it|his|her|their|a|an)\s+\1\b', content, re.IGNORECASE)
    print(f"Duplicate words (EN): {dup_en if dup_en else '0 lỗi'}")
    
    # 2. Common English typos
    common_typos = [
        r'\bgoverment\b', r'\baccomodate\b', r'\bwich\b', r'\bthier\b', r'\bundoubtly\b',
        r'\bseperate\b', r'\boccured\b', r'\brecieve\b', r'\buntill\b', r'\bdefinately\b',
        r'\bteh\b', r'\badolencent\b', r'\bschizoprenia\b', r'\bhalluciation\b', r'\bunconcious\b'
    ]
    for typo in common_typos:
        m = re.findall(typo, content, re.IGNORECASE)
        if m:
            print(f"  Typo EN: {m}")
            
    # 3. Punctuation balance
    open_parens = content.count('(') - content.count(')')
    open_curly_quotes = content.count('“') - content.count('”')
    print(f"Punctuation balance: ( ) = {open_parens}, “ ” = {open_curly_quotes}")
    
    # 4. Sentence ending punctuation in dialogue lines
    lines = content.splitlines()
    no_punct = []
    in_dialogue = False
    for idx, line in enumerate(lines, 1):
        l = line.strip()
        if l.startswith('**HOST**') or l.startswith('**INVESTIGATOR') or l.startswith('**PSYCHOLOGIST') or l.startswith('**ORDINARY'):
            in_dialogue = True
            continue
        if l.startswith('**[') or l.startswith('#') or l.startswith('---') or not l:
            in_dialogue = False
            continue
        if in_dialogue:
            if not l.endswith(('.', '!', '?', '”', '"', '…', ':')):
                no_punct.append((idx, l))
    print(f"Câu thoại thiếu dấu kết câu (EN): {len(no_punct)}")
    for line_no, l in no_punct:
        print(f"  Dòng {line_no}: {l}")

def audit_ja():
    print("\n" + "="*60)
    print("3. KIỂM TRA CHÍNH TẢ & NGÔN NGỮ TIẾNG NHẬT (Tap 38 JA)")
    print("="*60)
    ja_file = ROOT / "01_KICH_BAN" / "Tap38_JA" / "kichban_tap38_JA.md"
    content = ja_file.read_text(encoding="utf-8")
    
    # 1. Punctuation balance
    open_brackets = content.count('「') - content.count('」')
    open_parens = content.count('（') - content.count('）') + content.count('(') - content.count(')')
    print(f"Punctuation balance: 「 」 = {open_brackets}, ( ) = {open_parens}")
    
    # 2. Check ending marks for dialogue lines
    lines = content.splitlines()
    no_punct = []
    in_dialogue = False
    for idx, line in enumerate(lines, 1):
        l = line.strip()
        if l.startswith('**ホスト**') or l.startswith('**捜査官') or l.startswith('**心理学者') or l.startswith('**一般人'):
            in_dialogue = True
            continue
        if l.startswith('**[') or l.startswith('#') or l.startswith('---') or not l:
            in_dialogue = False
            continue
        if in_dialogue:
            if not l.endswith(('。', '！', '？', '」', '』', '…', '：', ':')):
                no_punct.append((idx, l))
    print(f"Câu thoại thiếu dấu kết câu (JA): {len(no_punct)}")
    for line_no, l in no_punct:
        print(f"  Dòng {line_no}: {l}")

    # 3. Check for half-width kana or suspicious punctuation
    half_width = re.findall(r'[\uFF61-\uFF9F]', content)
    print(f"Ký tự half-width kana: {len(half_width)}")

if __name__ == "__main__":
    audit_vn()
    audit_en()
    audit_ja()
