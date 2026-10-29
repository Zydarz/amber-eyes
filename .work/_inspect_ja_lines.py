import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

lines = open("01_KICH_BAN/Tap02_JA/kichban_tap02_JA_backup.md", encoding="utf-8").readlines()

for i, l in enumerate(lines):
    if l.startswith("**ホスト**") or l.startswith("**捜査官**") or l.startswith("**心理学者**") or l.startswith("**一般人**"):
        next_lines = [lines[j].strip() for j in range(i+1, min(i+4, len(lines))) if lines[j].strip()]
        preview = " // ".join(next_lines[:2])
        print(f"Line {i+1:03d}: {l.strip()[:40]} ---> {preview[:60]}")
