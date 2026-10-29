import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
text = open('02_SAN_XUAT/Tap04/Danh_Sach_Anh_Tap04.md', encoding='utf-8').read()

lines = text.splitlines()
cur_act = "None"
act_counts = {}
for line in lines:
    if line.startswith('### HỒI'):
        cur_act = line.split('·')[0].strip('# ')
        act_counts[cur_act] = []
    elif line.startswith('| `t4_'):
        m = re.match(r'\|\s*`([^`]+)`\s*\|\s*([^|]+)\s*\|\s*([^|]+)\s*\|', line)
        if m:
            act_counts[cur_act].append((m[1], m[2].strip(), m[3].strip()))

total = 0
for act, rows in act_counts.items():
    print(f"\n{act} ({len(rows)} rows):")
    total += len(rows)
    for r in rows:
        print(f"  {r[0]}: {r[1][:40]} ({r[2]})")

print(f"\nTotal rows in mapping tables: {total}")
