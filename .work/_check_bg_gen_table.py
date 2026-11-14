import re, os
from pathlib import Path

txt = Path('.work/_t09/_t09_gen_table.py').read_text(encoding='utf-8')
m = re.findall(r'"(\d\.\d+#\d+)":\s*"([^"]+)"', txt)
missing = []
for sid, bg in m:
    p = Path('assets/bg') / f"{bg}.png"
    if not p.exists():
        missing.append((sid, bg))

print(f"Total mapped: {len(m)}")
print(f"Missing count: {len(missing)}")
for sid, bg in missing:
    print(f"  {sid}: {bg}")
