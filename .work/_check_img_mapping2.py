import json, re, sys
sys.stdout.reconfigure(encoding='utf-8')

script = json.load(open('.work/script_tap05.json', encoding='utf-8'))
all_sent_ids = []
sent_lookup = {}
for el in script:
    if el.get('kind') == 'LOI':
        for s in el.get('sentences', []):
            all_sent_ids.append(s['id'])
            sent_lookup[s['id']] = s['text']

ds = open('02_SAN_XUAT/Tap05/Danh_Sach_Anh_Tap05.md', encoding='utf-8').read()
rows = re.findall(r'\|\s*(\d+)\s*\|\s*`?(t5_[a-z0-9_]+)`?\s*\|([^|]+)\|([^|]+)\|', ds)

def expand_mocs(mocs_str):
    # e.g. `1.03#1`–`#2` or `1.07#1`, `1.09#1`–`#2`
    res = []
    # split by comma
    chunks = [c.strip() for c in mocs_str.split(',')]
    for chunk in chunks:
        chunk = chunk.replace('`', '').strip()
        # check range like 1.03#1–#2 or 1.05#1–#2 or 1.10#5–#7
        m = re.match(r'(\d+\.\d+)#(\d+)\s*[–-]\s*#?(\d+)', chunk)
        if m:
            el, start, end = m.group(1), int(m.group(2)), int(m.group(3))
            for i in range(start, end + 1):
                res.append(f"{el}#{i}")
        else:
            m2 = re.match(r'(\d+\.\d+)#(\d+)', chunk)
            if m2:
                res.append(f"{m2.group(1)}#{m2.group(2)}")
            else:
                print(f"Unknown format: '{chunk}' in '{mocs_str}'")
    return res

mapped_sents = {}
for stt, name, desc, mocs in rows:
    expanded = expand_mocs(mocs)
    for sid in expanded:
        if sid in mapped_sents:
            mapped_sents[sid].append(name)
        else:
            mapped_sents[sid] = [name]

unmapped = [sid for sid in all_sent_ids if sid not in mapped_sents]
invalid = [sid for sid in mapped_sents if sid not in sent_lookup]
overlap = {sid: names for sid, names in mapped_sents.items() if len(names) > 1}

print(f"Mapped sentences: {len(mapped_sents)}/{len(all_sent_ids)}")
print(f"Unmapped sentences: {len(unmapped)} -> {unmapped}")
print(f"Invalid sentence IDs in Danh_Sach_Anh: {len(invalid)} -> {invalid}")
print(f"Overlapping sentences: {len(overlap)} -> {overlap}")
