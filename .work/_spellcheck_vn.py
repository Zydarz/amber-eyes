import re, sys
sys.stdout.reconfigure(encoding='utf-8')

def spellcheck_vn():
    text = open('01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md', encoding='utf-8').read()
    # Các lỗi gõ telex phổ biến, khoảng trắng trước dấu câu, lặp từ, v.v.
    issues = []
    # Khoảng trắng trước dấu chấm, phẩy
    for m in re.finditer(r'\s+([,.:;?!])', text):
        issues.append(f"Khoảng trắng thừa trước dấu câu: '{m.group(0)}'")
    # Dấu ngoặc kép lộn xộn
    # Lặp từ
    for m in re.finditer(r'\b(\w+)\s+\1\b', text, re.IGNORECASE):
        issues.append(f"Lặp từ: '{m.group(0)}'")
    print(f"VN issues: {len(issues)}")
    for iss in issues[:10]:
        print("  -", iss)

spellcheck_vn()
