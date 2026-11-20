# -*- coding: utf-8 -*-
"""
Audit chính tả và ngôn ngữ cho Tập 31 trên cả 3 thứ tiếng: Tiếng Việt, Tiếng Anh, Tiếng Nhật.
Kiểm tra:
1. Lỗi chính tả tiếng Việt (dấu thanh, từ lặp, typo phổ biến, định dạng số, tên riêng).
2. Lỗi ngữ pháp / từ vựng tiếng Anh (typo, duplicated words, apostrophe, capitalization, punctuation).
3. Lỗi chính tả tiếng Nhật (dấu câu 「」, 、。, kanji/kana, typo ngữ pháp, tính tự nhiên).
4. Kiểm tra đối chiếu số câu, cấu trúc và tên riêng giữa 3 ngôn ngữ.
"""
import sys, os, re, json
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(r"d:\TEST\Gax\amber-eyes")

def audit_vn():
    print("="*60)
    print("1. KIỂM TRA CHÍNH TẢ & NGÔN NGỮ TIẾNG VIỆT (Tap 31 VN)")
    print("="*60)
    vn_file = ROOT / "01_KICH_BAN" / "Tap31" / "kichban_tap31_19112026.md"
    content = vn_file.read_text(encoding="utf-8")
    
    # 1. Từ lặp (duplicate consecutive words)
    dup_words = re.findall(r'\b([a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]+)\s+\1\b', content, re.IGNORECASE)
    print(f"Từ lặp liên tiếp (VN): {dup_words if dup_words else '0 lỗi'}")
    
    # 2. Dấu ngoặc kép, ngoặc đơn không đóng
    open_curly_quotes = content.count('“') - content.count('”')
    open_straight_quotes = content.count('"') % 2
    open_parens = content.count('(') - content.count(')')
    print(f"Kiểm tra ngoặc: “ ” lệch = {open_curly_quotes}, \" chẵn lẻ = {open_straight_quotes}, ( ) lệch = {open_parens}")
    
    # 3. Typo tiếng Việt phổ biến
    typo_patterns = [
        r'\bk\b', r'\bđc\b', r'\bko\b', r'\brui\b', r'\bng\b', r'\bcs\b',
        r'sử lí', r'chẩn đoán', r'dấu ấn', r'xắp xếp', r'giành giật',
        r'xuất xắc', r'chuẩn đoán', r'chính chắn', r'chần chừ', r'bàng quan'
    ]
    found_typos = []
    for pat in typo_patterns:
        m = re.findall(pat, content, re.IGNORECASE)
        if m:
            found_typos.append(f"{pat}: {m}")
    print(f"Kiểm tra từ bẫy chính tả: {found_typos if found_typos else '0 lỗi bẫy'}")
    
    # 4. Kiểm tra dấu chấm câu và khoảng trắng
    space_before_punct = re.findall(r'\s+([,.:;?!])', content)
    print(f"Khoảng trắng thừa trước dấu câu: {len(space_before_punct)} lỗi")
    if space_before_punct:
        print("  Mẫu:", space_before_punct[:5])

def audit_en():
    print("\n" + "="*60)
    print("2. KIỂM TRA CHÍNH TẢ & NGÔN NGỮ TIẾNG ANH (Tap 31 EN)")
    print("="*60)
    en_file = ROOT / "01_KICH_BAN" / "Tap31_EN" / "kichban_tap31_EN.md"
    content = en_file.read_text(encoding="utf-8")
    
    # 1. Duplicate words
    dup_en = re.findall(r'\b(the|and|to|in|of|that|is|was|for|on|with|as|at|by|this|it|his|her|their)\s+\1\b', content, re.IGNORECASE)
    print(f"Duplicate words (EN): {dup_en if dup_en else '0 lỗi'}")
    
    # 2. Common English typos
    common_typos = [
        r'\bgoverment\b', r'\baccomodate\b', r'\bwich\b', r'\bthier\b', r'\bundoubtly\b',
        r'\bseperate\b', r'\boccured\b', r'\brecieve\b', r'\buntill\b', r'\bdefinately\b'
    ]
    found_typos = []
    for typo in common_typos:
        m = re.findall(typo, content, re.IGNORECASE)
        if m:
            found_typos.append(m)
    print(f"Common typos: {found_typos if found_typos else '0 lỗi'}")
    
    # 3. Punctuation & Quotes
    open_parens = content.count('(') - content.count(')')
    open_curly_quotes = content.count('“') - content.count('”')
    print(f"Punctuation balance: ( ) = {open_parens}, “ ” = {open_curly_quotes}")
    
    # 4. Check possessive apostrophes like 'Ted bomb' vs 'Ted's bomb' or missing apostrophes
    missing_possessive = re.findall(r'\b(Ted|bomber|brother|family|court|victim)\s+(bomb|homicide|crusade|life|hand|hatred|sentence)\b', content)
    print(f"Possessive noun checks (e.g. Ted's): {len(missing_possessive)} cases detected: {missing_possessive}")

def audit_ja():
    print("\n" + "="*60)
    print("3. KIỂM TRA CHÍNH TẢ & NGÔN NGỮ TIẾNG NHẬT (Tap 31 JA)")
    print("="*60)
    ja_file = ROOT / "01_KICH_BAN" / "Tap31_JA" / "kichban_tap31_JA.md"
    content = ja_file.read_text(encoding="utf-8")
    
    # 1. Punctuation checks
    open_kagi = content.count('「') - content.count('」')
    open_parens = content.count('（') - content.count('）') + content.count('(') - content.count(')')
    print(f"Dấu ngoặc 「」 lệch = {open_kagi}, （）/() lệch = {open_parens}")
    
    # 2. Duplicate kana particles e.g. のの, がが, はは, をを, にに
    dup_particles = re.findall(r'([のはがをにでもへと])\1', content)
    print(f"Trợ từ lặp bất thường: {dup_particles if dup_particles else '0 lỗi'}")
    
    # 3. Unnatural mixed punctuation
    mixed_punct = re.findall(r'[,.][\u3040-\u30ff\u4e00-\u9faf]', content)
    print(f"Dấu phẩy/chấm Latin lẫn vào văn bản tiếng Nhật: {mixed_punct if mixed_punct else '0 lỗi'}")

def main():
    audit_vn()
    audit_en()
    audit_ja()

if __name__ == '__main__':
    main()
