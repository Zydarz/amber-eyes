import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

for lang, p in [
    ('VN', '02_SAN_XUAT/Tap04/mo_ta.txt'),
    ('EN', '02_SAN_XUAT/Tap04_EN/mo_ta.txt'),
    ('JA', '02_SAN_XUAT/Tap04_JA/mo_ta.txt'),
    ('KO', '02_SAN_XUAT/Tap04_KO/mo_ta.txt')
]:
    f = Path(p)
    if f.exists():
        txt = f.read_text(encoding='utf-8')
        print(f"=== {lang} ({p}) [{len(txt)} chars, {len(txt.splitlines())} lines] ===")
        print(txt[:600])
        print("...\n")
    else:
        print(f"=== {lang} ({p}) DOES NOT EXIST ===")
