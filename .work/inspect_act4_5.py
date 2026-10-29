import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/acts3_4_5_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split("ACT ")
for p in parts:
    if p.startswith("4 "):
        print("=== ACT 4 ===")
        print(p)
    elif p.startswith("5 "):
        print("=== ACT 5 ===")
        print(p)
