import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

txt = Path("02_SAN_XUAT/Tap04/mo_ta.txt").read_text(encoding='utf-8')
print("=== 02_SAN_XUAT/Tap04/mo_ta.txt ===")
print(txt)

print("\n=== 02_SAN_XUAT/Tap04/nguon_mo_ta.txt ===")
print(Path("02_SAN_XUAT/Tap04/nguon_mo_ta.txt").read_text(encoding='utf-8'))
