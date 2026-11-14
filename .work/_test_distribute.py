import json

sc = json.load(open('.work/script_tap13.json', encoding='utf-8'))
old_jobs = json.load(open('.work/bg_jobs_tap13.json', encoding='utf-8'))

from collections import defaultdict
elem_to_jobs = defaultdict(list)
for j in old_jobs:
    elem = j['sentences'].split('#')[0]
    elem_to_jobs[elem].append(j)

# Test proportional distribution
for e in sc:
    if 'sentences' not in e or not e['sentences']:
        continue
    eid = e['id']
    sents = [s['id'] for s in e['sentences']]
    jobs = elem_to_jobs[eid]
    n_s = len(sents)
    n_j = len(jobs)
    
    # distribute n_s into n_j buckets
    # e.g. base = n_s // n_j, rem = n_s % n_j
    # first rem buckets get base + 1, rest get base
    buckets = []
    idx = 0
    for i in range(n_j):
        sz = n_s // n_j + (1 if i < (n_s % n_j) else 0)
        chunk = sents[idx : idx + sz]
        idx += sz
        buckets.append((jobs[i]['name'], chunk))
    
    # print summary
    ranges = [f"{b[0]} -> {b[1][0].split('#')[1]}-{b[1][-1].split('#')[1]} ({len(b[1])})" for b in buckets]
    print(f"{eid} ({e.get('role')}): " + " | ".join(ranges))
