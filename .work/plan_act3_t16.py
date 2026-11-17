import json

tl = json.load(open('.work/timeline_s_t16.json', encoding='utf-8'))['items']
jobs_83 = json.load(open('.work/bg_jobs_tap16.json', encoding='utf-8'))
assigned = set()
for j in jobs_83:
    s = j['sentences']
    if '–' in s:
        parts = s.split('–')
        elem = parts[0].split('#')[0]
        s_idx = int(parts[0].split('#')[1])
        e_idx = int(parts[1].replace('#',''))
        for i in range(s_idx, e_idx + 1):
            assigned.add(f'{elem}#{i}')
    else:
        assigned.add(s)

uncovered_act3 = [x for x in tl if x['act'] == 3 and x['id'] not in assigned]
print(f"Total Act 3 sentences: {len([x for x in tl if x['act'] == 3])}")
print(f"Uncovered Act 3 sentences: {len(uncovered_act3)}")

chunks = []
cur = []
for item in uncovered_act3:
    if len(cur) >= 2 or (cur and (cur[0]['end'] - cur[0]['start']) + (item['end'] - item['start']) > 24.0):
        chunks.append(cur)
        cur = [item]
    else:
        cur.append(item)
if cur:
    chunks.append(cur)

# Adjust to exactly 13 chunks
idx = 0
while len(chunks) < 13 and idx < len(chunks):
    if len(chunks[idx]) == 2:
        item1 = [chunks[idx][0]]
        item2 = [chunks[idx][1]]
        chunks.pop(idx)
        chunks.insert(idx, item2)
        chunks.insert(idx, item1)
        idx += 2
    else:
        idx += 1

while len(chunks) > 13:
    min_len = 999
    merge_idx = 0
    for i in range(len(chunks)-1):
        total_time = sum(x['end'] - x['start'] for x in chunks[i] + chunks[i+1])
        if total_time < min_len:
            min_len = total_time
            merge_idx = i
    merged = chunks.pop(merge_idx) + chunks.pop(merge_idx)
    chunks.insert(merge_idx, merged)

print(f"Final chunks for Act 3: {len(chunks)}")
for i, ch in enumerate(chunks, 1):
    sent_str = ch[0]['id'] if len(ch) == 1 else f"{ch[0]['id']}–#{ch[-1]['id'].split('#')[1]}"
    print(f"Chunk {i:02d}: {sent_str} | {[x['text'][:35] for x in ch]}")

with open('.work/act3_chunks_t16.json', 'w', encoding='utf-8') as f:
    json.dump([{"idx": i+1, "sents": ch[0]['id'] if len(ch) == 1 else f"{ch[0]['id']}–#{ch[-1]['id'].split('#')[1]}", "items": ch} for i, ch in enumerate(chunks)], f, ensure_ascii=False, indent=2)
