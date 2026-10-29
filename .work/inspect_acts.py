import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/shot_semantic_review.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect shots per act
acts = {}
for block in text.split("======================================================================\n"):
    block = block.strip()
    if not block:
        continue
    m = re.search(r'\[(\d+)-\d+\]', block)
    if m:
        act_num = m.group(1)
        acts.setdefault(act_num, []).append(block)

print(f"Acts found: {list(acts.keys())}")
for act_num, act_shots in acts.items():
    print(f"Act {act_num}: {len(act_shots)} shots")
