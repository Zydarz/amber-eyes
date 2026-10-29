with open(".work/edition.py", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        if '"04":' in line or "'04':" in line:
            print(f"Line {i}: {line.strip()}")
