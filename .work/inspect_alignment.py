import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/_shots_full_alignment.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:60]):
    print(f"{i:02d}: {l.rstrip()}")
