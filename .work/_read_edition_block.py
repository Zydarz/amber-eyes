import re

c = open('.work/edition.py', encoding='utf-8').read()
ep_block = re.search(r'EPISODES\s*=\s*\{.*?\n\}', c, re.DOTALL)
if ep_block:
    keys = re.findall(r'"(\d+)":\s*\{', ep_block.group(0))
    print('EPISODES keys in edition.py:', keys)
    for k in ['29', '34', '36', '37', '38']:
        m = re.search(r'"' + k + r'":\s*\{[^\}]+\}', ep_block.group(0))
        if m:
            print(f"Key {k}:", m.group(0))
