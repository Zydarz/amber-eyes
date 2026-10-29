import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/act2_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print(text[1500:])
