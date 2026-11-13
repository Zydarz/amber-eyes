# -*- coding: utf-8 -*-
import sys, re
sys.path.insert(0, '.work')
import parse_kichban as PK

path = '01_KICH_BAN/Tap12/kichban_tap12_23102026.md'
p = PK.parse_file(path)

loi = [e for e in p if e['kind'] == 'LOI']
total_sentences = sum(len(x.get('sentences', [])) for x in loi)
total_words = sum(sum(s['words'] for s in x['sentences']) for x in loi)

print(f"Total elements: {len(p)}")
print(f"Total LOI turns: {len(loi)}")
print(f"Total sentences: {total_sentences}")
print(f"Total words: {total_words}")

forbidden = ['máu', 'thi thể', 'xác chết', 'tự sát', 'cắt cổ', 'bóp cổ', 'khí độc', 'ngạt thở', 'sát hại', 'đầu độc']
fb_hits = []
ellipsis_hits = []

for e in loi:
    for s in e['sentences']:
        txt = s['text']
        sid = s['id']
        for fb in forbidden:
            if re.search(r'\b' + re.escape(fb) + r'\b', txt, re.IGNORECASE):
                fb_hits.append((sid, fb, txt))
        if '...' in txt or '…' in txt:
            ellipsis_hits.append((sid, txt))

print(f"Forbidden word hits (V9): {len(fb_hits)}")
for h in fb_hits:
    print(f"  - {h[0]}: {h[1]} in '{h[2]}'")

print(f"Ellipsis hits (G1): {len(ellipsis_hits)}")
for d in ellipsis_hits:
    print(f"  - {d[0]}: '{d[1]}'")
