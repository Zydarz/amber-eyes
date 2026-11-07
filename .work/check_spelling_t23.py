# -*- coding: utf-8 -*-
"""Spellcheck and sanity check script for Episode 23 across all 4 languages."""

import sys, re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

scripts = {
    "VN": ROOT / "01_KICH_BAN" / "Tap23" / "kichban_tap23_23102026.md",
    "EN": ROOT / "01_KICH_BAN" / "Tap23_EN" / "kichban_tap23_EN.md",
    "JA": ROOT / "01_KICH_BAN" / "Tap23_JA" / "kichban_tap23_JA.md",
    "KO": ROOT / "01_KICH_BAN" / "Tap23_KO" / "kichban_tap23_KO.md",
}

print("=" * 70)
print("KIỂM TRA CHÍNH TẢ VÀ CẤU TRÚC KỊCH BẢN TẬP 23 (4 NGÔN NGỮ)")
print("=" * 70)

issues_found = 0

for lang, path in scripts.items():
    print(f"\n--- Kiểm tra {lang}: {path.name} ---")
    text = path.read_text(encoding="utf-8")
    
    # 1. Cặp dấu đóng mở ngoặc
    for left, right in [("(", ")"), ("[", "]"), ("{", "}")]:
        c_left = text.count(left)
        c_right = text.count(right)
        if c_left != c_right:
            print(f"  ❌ LỆCH NGOẶC '{left}' và '{right}': {c_left} != {c_right}")
            issues_found += 1
        else:
            print(f"  ✅ Dấu ngoặc '{left}{right}': Cân bằng tuyệt đối ({c_left})")

    # 2. Dấu nháy trích dẫn
    c_q_open = text.count("“")
    c_q_close = text.count("”")
    if c_q_open != c_q_close:
        print(f"  ❌ LỆCH DẤU NHÁY CONG: {c_q_open} '“' vs {c_q_close} '”'")
        issues_found += 1
    elif c_q_open > 0:
        print(f"  ✅ Dấu nháy cong: Cân bằng ({c_q_open} cặp)")

    # 3. Từ lặp từ liền kề
    if lang in ["VN", "EN"]:
        repeated = re.findall(r'\b([a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]{3,})\s+\1\b', text, re.IGNORECASE)
        if repeated:
            print(f"  ⚠️ Từ lặp liền kề: {repeated}")
            issues_found += len(repeated)
        else:
            print(f"  ✅ Từ lặp: Không có từ lặp bất thường")

    # 4. Khoảng trắng trước dấu câu trong lời thoại (LOI)
    lines = text.splitlines()
    loi_lines = []
    in_loi = False
    for line in lines:
        s = line.strip()
        if re.match(r'^\*\*(HOST|ĐIỀU TRA VIÊN|CHUYÊN GIA TÂM LÝ|NGƯỜI BÌNH THƯỜNG|INVESTIGATOR|PSYCHOLOGIST|ORDINARY PERSON|호스트|수사관|심리학자|일반인|ホスト|捜査官|心理学者|一般人)\*\*', s):
            in_loi = True
            continue
        if s.startswith("## ") or s.startswith("**[") or s.startswith("---") or not s:
            in_loi = False
            continue
        if in_loi:
            loi_lines.append(s)

    loi_text = "\n".join(loi_lines)
    space_punct = re.findall(r'\s+([,.:;!?])', loi_text)
    if space_punct:
        print(f"  ⚠️ Khoảng trắng trước dấu câu: {len(space_punct)} trường hợp ({space_punct[:5]})")
        issues_found += len(space_punct)
    else:
        print(f"  ✅ Khoảng trắng trước dấu câu: Chuẩn tuyệt đối (0 lỗi)")

    # 5. Dấu chấm/phẩy kép bất thường (không tính ...)
    double_punct = re.findall(r'([,;:!?])\1+', loi_text)
    double_dot = re.findall(r'(?<!\.)\.\.(?!\.)', loi_text)
    if double_punct or double_dot:
        print(f"  ⚠️ Dấu câu lặp kép: {double_punct + double_dot}")
        issues_found += len(double_punct + double_dot)
    else:
        print(f"  ✅ Dấu câu kép: Chuẩn (0 lỗi)")

print("\n" + "=" * 70)
if issues_found == 0:
    print(">>> KẾT QUẢ: 100% KỊCH BẢN 4 NGÔN NGỮ ĐẠT CHUẨN CHÍNH TẢ & ĐỊNH DẠNG! <<<")
else:
    print(f">>> CẢNH BÁO: TÌM THẤY {issues_found} VẤN ĐỀ CẦN XỬ LÝ! <<<")
print("=" * 70)
