import re

c = open('.work/edition.py', encoding='utf-8').read()
m34 = re.search(r'"34":\s*\{[^}]+\}', c)
print('Tap 34 in edition.py:', m34.group(0) if m34 else 'None')
m29 = re.search(r'"29":\s*\{[^}]+\}', c)
print('Tap 29 in edition.py:', m29.group(0) if m29 else 'None')
m36 = re.search(r'"36":\s*\{[^}]+\}', c)
print('Tap 36 in edition.py:', m36.group(0) if m36 else 'None')
