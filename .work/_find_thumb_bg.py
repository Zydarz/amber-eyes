import sys
sys.stdout.reconfigure(encoding='utf-8')
with open('.work/package.py', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'thumb_bg' in line or 'thumbnail' in line.lower():
            print(f"{i+1}: {line.strip()}")
