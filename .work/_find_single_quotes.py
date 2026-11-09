import sys
sys.stdout.reconfigure(encoding='utf-8')
raw = open('01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md', encoding='utf-8').read()
for i, line in enumerate(raw.splitlines(), 1):
    if "'" in line:
        print(f"Line {i}: {line}")
