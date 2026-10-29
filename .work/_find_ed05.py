import sys
with open('.work/edition.py', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if '"05": {' in l:
        for j in range(max(0, i-2), min(len(lines), i+30)):
            print(f"{j+1:4d}: {lines[j]}", end='')
        break
