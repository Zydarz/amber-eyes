import os

matches = []
# Only scan root, .work, 00_TIEU_CHUAN, 02_SAN_XUAT, 90_LUU_TRU
# Specifically skip 01_KICH_BAN itself (except markdown headers), .git, assets, node_modules
target_dirs = ['.', '.work', '00_TIEU_CHUAN', '02_SAN_XUAT', '90_LUU_TRU']

for td in target_dirs:
    for root, dirs, files in os.walk(td):
        if any(skip in root for skip in ['.git', 'assets', '__pycache__', '_backup']):
            continue
        # also if walking '.', don't descend into 01_KICH_BAN or videos
        if root.startswith('.\\01_KICH_BAN') or root.startswith('./01_KICH_BAN') or root.startswith('.\\videos'):
            continue
        for f in files:
            if f.endswith(('.py', '.json', '.md', '.txt', '.sh', '.bat', '.ps1')):
                p = os.path.join(root, f)
                try:
                    c = open(p, encoding='utf-8', errors='ignore').read()
                    if '01_KICH_BAN' in c:
                        cnt = c.count('01_KICH_BAN')
                        matches.append((p, cnt))
                except:
                    pass

print(f"Total files referencing '01_KICH_BAN': {len(matches)}")
# Sort by python files first, then json, then md
matches.sort(key=lambda x: (0 if x[0].endswith('.py') else (1 if x[0].endswith('.json') else 2), x[0]))

open('.work/_kb_references_list.json', 'w', encoding='utf-8').write(
    __import__('json').dumps(matches, ensure_ascii=False, indent=2)
)

py_files = [m for m in matches if m[0].endswith('.py')]
print(f"Python files count: {len(py_files)}")
for p, cnt in py_files[:25]:
    print(f"  {cnt:3d} refs | {p}")

md_files = [m for m in matches if m[0].endswith('.md')]
print(f"Markdown files count: {len(md_files)}")
for p, cnt in md_files[:15]:
    print(f"  {cnt:3d} refs | {p}")
