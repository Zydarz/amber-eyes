with open(".work/edition.py", "r", encoding="utf-8") as f:
    c = f.read()

target = '"summary": ("1.11#3", "3.02#1")'
replacement = '"summary": ("1.10#5", "3.02#1")'

if target in c:
    c = c.replace(target, replacement, 1)
    with open(".work/edition.py", "w", encoding="utf-8") as f:
        f.write(c)
    print("SUCCESS")
else:
    print("TARGET NOT FOUND")
