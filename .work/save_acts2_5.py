import re
import sys

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

out = []
for a in ['2', '3', '4', '5']:
    out.append(f"\n############################# ACT {a} #############################")
    for b in acts[a]:
        out.append(b)

with open('.work/acts2_5_review.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Wrote .work/acts2_5_review.txt successfully.")
