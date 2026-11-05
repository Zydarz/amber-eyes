import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

txt1 = Path(".work/generate_all_descriptions.py").read_text(encoding='utf-8')
print("=== generate_all_descriptions.py top 1000 chars ===")
print(txt1[:1000])

txt2 = Path(".work/generate_multilingual_descriptions.py").read_text(encoding='utf-8')
print("\n=== generate_multilingual_descriptions.py top 1000 chars ===")
print(txt2[:1000])
