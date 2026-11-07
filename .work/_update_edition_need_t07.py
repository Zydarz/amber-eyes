import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import edition, json

script = json.load(open('.work/script_tap07.json', encoding='utf-8'))
all_sent_ids = {s['id']: s['text'] for el in script if 'sentences' in el for s in el['sentences']}

# Replacements for shifted IDs
mapping = {
    '1.13#1': '1.11#2',
    '2.04#3': '2.03#1',
    '2.04#5': '2.03#4',
    '2.07#1': '2.05#4',
    '3.05#1': '3.04#1',
    '3.05#2': '3.04#3',
    '4.10#1': '4.08#6',
    '4.10#2': '4.09#1',
}

old_need = edition.EPISODES['07']['need']
new_need = [mapping.get(k, k) for k in old_need]

# Verify all in new_need exist
missing = [k for k in new_need if k not in all_sent_ids]
print("Missing in updated need:", missing)
assert len(missing) == 0, f"Still missing: {missing}"

# Update edition.py safely (L5 backup first)
edition_path = '.work/edition.py'
content = open(edition_path, encoding='utf-8').read()

# Replace the need list for episode 07
# Find "07": { ... "need": [ ... ]
pattern = r'("07":\s*\{[\s\S]*?"need":\s*\[)([\s\S]*?)(\])'
m = re.search(pattern, content)
if m:
    need_str = ",\n      ".join(f'"{k}"' for k in new_need)
    new_block = m.group(1) + "\n      " + need_str + "\n    " + m.group(3)
    content = content[:m.start()] + new_block + content[m.end():]
    with open(edition_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully updated edition.py EPISODES['07']['need'] with 100% valid keys!")
else:
    print("Could not match pattern in edition.py!")
