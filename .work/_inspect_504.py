import sys
sys.path.insert(0, '.work')
from parse_kichban import parse_file

for el in parse_file('01_KICH_BAN/Tap09/kichban_tap09_23102026.md'):
    if el['id'] == '5.04':
        print('Element 5.04:')
        for i, s in enumerate(el.get('sentences', []), 1):
            print(f'  5.04#{i}: {s["text"]}')
