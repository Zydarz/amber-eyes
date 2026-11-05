import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

txt1 = Path(".work/verify_all_descriptions.py").read_text(encoding='utf-8')
print("=== verify_all_descriptions.py ===")
print(txt1)

txt2 = Path(".work/verify_all_multilingual.py").read_text(encoding='utf-8')
print("=== verify_all_multilingual.py ===")
print(txt2)
