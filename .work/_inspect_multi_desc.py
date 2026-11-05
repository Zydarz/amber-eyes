import sys
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path

txt = Path(".work/generate_multilingual_descriptions.py").read_text(encoding='utf-8')
lines = txt.splitlines()
print(f"Total lines: {len(lines)}")
# print main or function definitions
for i, ln in enumerate(lines):
    if ln.startswith("def ") or ln.startswith("if __name__"):
        print(f"Line {i}: {ln}")
