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

print("ACT 1 SHOTS:")
for b in acts['1']:
    print(b)
