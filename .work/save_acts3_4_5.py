import sys

with open('.work/acts2_5_review.txt', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split("############################# ACT ")
out = []
for p in parts:
    if p.startswith("3 ") or p.startswith("4 ") or p.startswith("5 "):
        out.append("ACT " + p)

with open('.work/acts3_4_5_full.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out))

print("Wrote .work/acts3_4_5_full.txt")
