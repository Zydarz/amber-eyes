# -*- coding: utf-8 -*-
with open('.work/build_tap31_216.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    # If line has single quotes around an english sentence that contains an internal apostrophe:
    # replace outer single quotes with double quotes
    s = line.strip()
    if s.startswith("'") and (s.endswith("',") or s.endswith("'")):
        inner = s[1:-2] if s.endswith("',") else s[1:-1]
        if "'" in inner:
            indent = line[:len(line) - len(line.lstrip())]
            comma = "," if s.endswith("',") else ""
            line = f'{indent}"{inner}"{comma}\n'
    new_lines.append(line)

with open('.work/build_tap31_216.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Cleaned all internal apostrophes.')
