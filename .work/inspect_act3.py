import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('.work/acts3_4_5_full.txt', 'r', encoding='utf-8') as f:
    text = f.read()

parts = text.split("ACT ")
for p in parts:
    if p.startswith("3 "):
        print("=== ACT 3 ===")
        print(p)
