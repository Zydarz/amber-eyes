import sys
with open('.work/build_audio3.py', encoding='utf-8') as f:
    lines = f.readlines()
for i, l in enumerate(lines[:120], 1):
    print(f"{i:3d}: {l}", end='')
