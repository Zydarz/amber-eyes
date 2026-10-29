import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/acts2_5_review.txt', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split("############################# ACT ")
for p in parts:
    if p.startswith("2 "):
        print("ACT 2:")
        print(p[:3000])
        # print remaining if any
        if len(p) > 3000:
            with open('.work/act2_full.txt', 'w', encoding='utf-8') as f2:
                f2.write(p)
