import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"d:\TEST\Gax\amber-eyes")

scripts = {
    "VI": ROOT / "01_KICH_BAN" / "Tap07" / "kichban_tap07_23102026.md",
    "EN": ROOT / "01_KICH_BAN" / "Tap07_EN" / "kichban_tap07_EN.md",
    "JA": ROOT / "01_KICH_BAN" / "Tap07_JA" / "kichban_tap07_JA.md",
    "KO": ROOT / "01_KICH_BAN" / "Tap07_KO" / "kichban_tap07_KO.md",
}

print("=== 1. KIỂM TRA CHÍNH TẢ & ĐỊNH DẠNG TẬP 07 ===")

# Known valid repetitions in Vietnamese
VALID_VI_DUPS = {"ngày", "càng", "rất", "nhiều", "từng", "luôn", "xa"}

for lang, p in scripts.items():
    if not p.exists():
        print(f"[{lang}] KHÔNG TÌM THẤY: {p}")
        continue
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines()
    print(f"\n--- {lang}: {p.name} ({len(lines)} dòng, {len(text)} ký tự) ---")

    # Check for strange or unescaped characters
    issues = []
    
    # 1. Duplicate words
    dup_re = re.compile(r"\b([a-zA-ZÀ-ỹ가-힣一-龯ぁ-んァ-ヶ]{2,})\s+\1\b", re.IGNORECASE)
    for idx, l in enumerate(lines, 1):
        # Ignore markdown headers or comments
        if l.strip().startswith("#") or l.strip().startswith("<!--"):
            continue
        for m in dup_re.finditer(l):
            w = m.group(1).lower()
            if w not in VALID_VI_DUPS:
                issues.append(f"Dòng {idx}: Lặp từ '{m.group(0)}'")

    # 2. Check for whitespace before punctuation (. , : ; ! ?)
    space_punct_re = re.compile(r"\s+([,;:!\?\.])")
    for idx, l in enumerate(lines, 1):
        if l.strip().startswith("[") and l.strip().endswith("]"):
            continue # tag line
        m = space_punct_re.search(l)
        if m:
            # allow ellipsis ...
            if m.group(0).strip() == "." and "..." in l:
                continue
            issues.append(f"Dòng {idx}: Dấu câu có khoảng trắng trước: '{m.group(0)}' trong \"{l.strip()[:60]}\"")

    # 3. Check for double punctuation like '..', ',,', '??'
    double_punct = re.compile(r"([,;:!\?])\1+")
    for idx, l in enumerate(lines, 1):
        m = double_punct.search(l)
        if m:
            issues.append(f"Dòng {idx}: Dấu lặp: '{m.group(0)}' trong \"{l.strip()[:60]}\"")

    # 4. Check for tags format
    tag_re = re.compile(r"^\[(\d+\.\d+)\]\s*(\w+)?")
    for idx, l in enumerate(lines, 1):
        if l.startswith("[") and "]" in l:
            # check tag
            end_bracket = l.find("]")
            tag_content = l[1:end_bracket]
            # allow [BGM], [SFX], [NHAN_VAT], [LOI_THOAI], etc.
            # or [1.01], [1.01#1]
            pass

    if issues:
        print(f"Tìm thấy {len(issues)} vấn đề tiềm ẩn:")
        for iss in issues[:10]:
            print("  *", iss)
        if len(issues) > 10:
            print(f"  ... và {len(issues)-10} vấn đề khác.")
    else:
        print("  -> Tuyệt vời: 0 lỗi chính tả hoặc dấu câu thô!")
