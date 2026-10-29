import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/acts2_5_review.txt', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split("############################# ACT ")
for p in parts:
    if p.startswith("3 "):
        print("ACT 3:")
        print(p)
    elif p.startswith("4 "):
        print("ACT 4:")
        print(p)
    elif p.startswith("5 "):
        print("ACT 5:")
        print(p)
