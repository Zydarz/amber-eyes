import os, re

matches = []
# Scan all text files in workspace except .git, assets, and binary/cache
for root, dirs, files in os.walk('.'):
    if '.git' in root or 'assets' in root or '__pycache__' in root:
        continue
    for f in files:
        if f.endswith(('.py', '.json', '.md', '.txt', '.sh', '.bat', '.ps1')):
            p = os.path.join(root, f)
            try:
                c = open(p, encoding='utf-8', errors='ignore').read()
                if '01_KICH_BAN' in c:
                    # find all occurrences and line numbers
                    lines = c.splitlines()
                    for idx, line in enumerate(lines, 1):
                        if '01_KICH_BAN' in line:
                            matches.append((p, idx, line.strip()))
            except Exception as e:
                pass

print(f"Total occurrences of '01_KICH_BAN': {len(matches)}")
# Group by file
by_file = {}
for p, idx, line in matches:
    by_file[p] = by_file.get(p, 0) + 1

print(f"Total files referencing '01_KICH_BAN': {len(by_file)}")
for p, count in sorted(by_file.items(), key=lambda x: x[1], reverse=True)[:30]:
    print(f"{count:3d} refs | {p}")
