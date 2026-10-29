import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

script = json.load(open('.work/script_tap05.json', encoding='utf-8'))
all_sent_ids = []
for el in script:
    if el.get('kind') == 'LOI':
        for s in el.get('sentences', []):
            all_sent_ids.append(s['id'])

print(f"Total sentences in script: {len(all_sent_ids)}")
print(f"First sent: {all_sent_ids[0]}, Last sent: {all_sent_ids[-1]}")

# Read Danh_Sach_Anh_Tap05.md
ds = open('02_SAN_XUAT/Tap05/Danh_Sach_Anh_Tap05.md', encoding='utf-8').read()
# Extract table rows: | stt | t5_name | desc | moc_cau |
rows = re.findall(r'\|\s*(\d+)\s*\|\s*`?(t5_[a-z0-9_]+)`?\s*\|([^|]+)\|([^|]+)\|', ds)
print(f"Total rows in Danh_Sach_Anh: {len(rows)}")

covered = set()
for stt, name, desc, mocs in rows:
    mocs = mocs.strip()
    # parse mocs like `1.03#1`–`#2` or `1.07#1`, `1.09#1`–`#2`
    parts = [p.strip().strip('`') for p in re.split(r'[,·]', mocs)]
    # print(name, parts)
