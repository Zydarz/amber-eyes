# -*- coding: utf-8 -*-
"""Detailed consistency and syllable verification for Episode 10 scripts."""
import sys, io, re, json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

files = {
    'VN': '01_KICH_BAN/Tap10/kichban_tap10_23102026.md',
    'EN': '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md',
    'JA': '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md',
    'KO': '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md',
}

def analyze_vn(sentences):
    print("\n=== CHI TIẾT TIẾNG VIỆT ===")
    # 1. Punctuation issues
    for sid, text, role in sentences:
        if re.search(r'\.{2,}', text):
            print(f"[{sid}] Dấu chấm liên tiếp: {text}")
        if re.search(r',{2,}', text):
            print(f"[{sid}] Dấu phẩy liên tiếp: {text}")
        if re.search(r'[!?]{2,}', text):
            print(f"[{sid}] Dấu chấm than/hỏi liên tiếp: {text}")
        if re.search(r'“\s+', text):
            print(f"[{sid}] Khoảng trắng thừa sau ngoặc kép mở: {text}")
        if re.search(r'\s+”', text):
            print(f"[{sid}] Khoảng trắng thừa trước ngoặc kép đóng: {text}")
            
    # 2. Check proper names in VN
    names = ['Colleen Stan', 'Cameron Hooker', 'Janice Hooker', 'Red Bluff', 'Westwood', 'Eugene', 'Riverside', 'Tehama', 'The Company']
    for sid, text, role in sentences:
        for n in ['colleen', 'cameron', 'janice', 'hooker', 'stan']:
            for m in re.finditer(r'\b' + n + r'\b', text, re.IGNORECASE):
                matched = m.group(0)
                # Check if properly capitalized
                if matched not in ['Colleen', 'Cameron', 'Janice', 'Hooker', 'Stan']:
                    print(f"[{sid}] Sai viết hoa tên riêng '{matched}': {text}")

def analyze_en(sentences):
    print("\n=== CHI TIẾT TIẾNG ANH ===")
    for sid, text, role in sentences:
        if re.search(r'\.{2,}', text):
            print(f"[{sid}] Consecutive dots: {text}")
        if re.search(r',{2,}', text):
            print(f"[{sid}] Consecutive commas: {text}")
        if re.search(r'“\s+', text):
            print(f"[{sid}] Space after open quote: {text}")
        if re.search(r'\s+”', text):
            print(f"[{sid}] Space before close quote: {text}")
        for n in ['colleen', 'cameron', 'janice', 'hooker', 'stan']:
            for m in re.finditer(r'\b' + n + r'\b', text, re.IGNORECASE):
                matched = m.group(0)
                if matched not in ['Colleen', 'Cameron', 'Janice', 'Hooker', 'Stan']:
                    print(f"[{sid}] Lowercase/improper name '{matched}': {text}")

def analyze_ja(sentences):
    print("\n=== CHI TIẾT TIẾNG NHẬT ===")
    for sid, text, role in sentences:
        # Check name variations in JA
        # Colleen: コリーン・スタン or コリーン
        # Cameron: キャメロン・フッカー or キャメロン
        # Janice: ジャニス・フッカー or ジャニス
        # Check if Roman letters remain where Katakana should be
        for eng_name in ['Colleen', 'Cameron', 'Janice', 'Hooker', 'Stan']:
            if eng_name in text:
                print(f"[{sid}] Tên tiếng Anh chưa chuyển katakana '{eng_name}': {text}")
        if '、、' in text or '。。' in text:
            print(f"[{sid}] Dấu câu lặp: {text}")

def analyze_ko(sentences):
    print("\n=== CHI TIẾT TIẾNG HÀN ===")
    for sid, text, role in sentences:
        if '..' in text or ',,' in text:
            print(f"[{sid}] Dấu câu lặp: {text}")
        # Check English names in KO: Colleen, Cameron, Janice, etc.
        # Let's see if English names are kept or transliterated
        for eng_name in ['Hooker', 'Stan']:
            pass

def main():
    for lang, path in files.items():
        p = PK.parse_file(path)
        loi = [e for e in p if e['kind'] == 'LOI']
        s_list = []
        for e in loi:
            for s in e['sentences']:
                s_list.append((s['id'], s['text'], e.get('role')))
        if lang == 'VN':
            analyze_vn(s_list)
        elif lang == 'EN':
            analyze_en(s_list)
        elif lang == 'JA':
            analyze_ja(s_list)
        elif lang == 'KO':
            analyze_ko(s_list)

if __name__ == '__main__':
    main()
