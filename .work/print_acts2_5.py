import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/shot_semantic_review.txt', 'r', encoding='utf-8') as f:
    text = f.read()

acts = {}
for block in text.split("======================================================================\n"):
    block = block.strip()
    if not block:
        continue
    m = re.search(r'\[(\d+)-\d+\]', block)
    if m:
        act_num = m.group(1)
        acts.setdefault(act_num, []).append(block)

for a in ['2', '3', '4', '5']:
    print(f"\n############################# ACT {a} #############################")
    for b in acts[a]:
        print(b)
