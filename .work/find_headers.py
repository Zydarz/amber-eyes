import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if l.startswith('#'):
        print(f"Line {i+1}: {l.strip()}")
