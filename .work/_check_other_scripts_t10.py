import sys, re
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

files = [
    ('EN', Path('01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md')),
    ('EN_copy', Path('01_KICH_BAN/Tap10/kichban_tap10_EN.md')),
    ('JA', Path('01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md')),
    ('KO', Path('01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md')),
]

for name, p in files:
    print(f"\n=== KIỂM TRA FILE {name}: {p} ===")
    if not p.exists():
        print("  FILE KHÔNG TỒN TẠI!")
        continue
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    print(f"  Số dòng: {len(lines)}, Dung lượng: {len(text):,} ký tự")
    
    # Check ellipsis G1
    ellipses = [i+1 for i, l in enumerate(lines) if ('...' in l or '…' in l) and not l.startswith('|')]
    if ellipses:
        print(f"  Cảnh báo G1 (dấu chấm lửng): dòng {ellipses}")
    else:
        print("  G1 (dấu chấm lửng): SẠCH (0 lỗi)")
        
    # Check double spaces inside text
    dbl = [i+1 for i, l in enumerate(lines) if '  ' in l.strip() and not l.strip().startswith('|') and not l.strip().startswith('-')]
    if dbl:
        print(f"  Khoảng trắng kép: dòng {dbl[:10]}")
    else:
        print("  Khoảng trắng kép: SẠCH (0 lỗi)")
