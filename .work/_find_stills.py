with open('.work/build_video3.py', encoding='utf-8') as f:
    for i, line in enumerate(f):
        if 'stills' in line:
            print(f"{i+1}: {line.strip()}")
