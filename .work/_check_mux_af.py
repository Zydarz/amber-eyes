import re

text = open(".work/edition.py", encoding="utf-8").read()
for ep in ["04", "05", "06", "07", "08", "09"]:
    idx = text.find(f'"{ep}": {{')
    if idx != -1:
        block = text[idx:idx+3500]
        m = re.search(r'"mux_af":\s*([^\n]+)', block)
        if m:
            print(f"EP {ep}: {m.group(1)}")
        else:
            print(f"EP {ep}: NONE")
