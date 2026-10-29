import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.find('| 27 |')
print(text[idx:idx+1500])
