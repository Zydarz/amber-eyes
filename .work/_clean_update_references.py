import os, re

def update_file(path):
    try:
        content = open(path, encoding='utf-8', errors='ignore').read()
        if '01_KICH_BAN' not in content:
            return 0
            
        new_content = content
        new_content = new_content.replace('01_KICH_BAN/Ho_So_Toi_Pham/Tap', '01_KICH_BAN/Ho_So_Toi_Pham/Tap')
        new_content = new_content.replace('01_KICH_BAN\\Ho_So_Toi_Pham\\Tap', '01_KICH_BAN\Ho_So_Toi_Pham\Tap')
        
        # Simple plain string replaces (safe and no regex escape issues)
        new_content = new_content.replace('01_KICH_BAN/Ho_So_Toi_Pham/Tap', '01_KICH_BAN/Ho_So_Toi_Pham/Tap')
        new_content = new_content.replace('01_KICH_BAN\\Ho_So_Toi_Pham\\Tap', '01_KICH_BAN\\Ho_So_Toi_Pham\\Tap')
        new_content = new_content.replace('01_KICH_BAN\\\\Tap', '01_KICH_BAN\\\\Ho_So_Toi_Pham\\\\Tap')
        
        # Pathlib replaces: "01_KICH_BAN" / "Ho_So_Toi_Pham" / f"Tap" -> "01_KICH_BAN" / "Ho_So_Toi_Pham" / f"Tap"
        new_content = re.sub(r'("01_KICH_BAN")\s*/\s*(f?"Tap)', r'\1 / "Ho_So_Toi_Pham" / \2', new_content)
        new_content = re.sub(r"('01_KICH_BAN')\s*/\s*(f?'Tap)", r"\1 / 'Ho_So_Toi_Pham' / \2", new_content)
        
        new_content = new_content.replace('01_KICH_BAN/Ho_So_Toi_Pham/Tap', '01_KICH_BAN/Ho_So_Toi_Pham/Tap')
        new_content = new_content.replace('01_KICH_BAN\Ho_So_Toi_Pham\Tap', '01_KICH_BAN\\Ho_So_Toi_Pham\\Tap')
        
        if new_content != content:
            open(path, 'w', encoding='utf-8').write(new_content)
            return 1
        return 0
    except Exception as e:
        print(f"Error {path}: {e}")
        return 0

total = 0

# 1. Root files
for f in os.listdir('.'):
    if os.path.isfile(f) and f.endswith(('.md', '.py', '.json', '.txt')):
        total += update_file(f)

# 2. 00_TIEU_CHUAN
for f in os.listdir('00_TIEU_CHUAN'):
    p = os.path.join('00_TIEU_CHUAN', f)
    if os.path.isfile(p):
        total += update_file(p)

# 3. 02_SAN_XUAT
for d in os.listdir('02_SAN_XUAT'):
    dp = os.path.join('02_SAN_XUAT', d)
    if os.path.isdir(dp):
        for f in os.listdir(dp):
            p = os.path.join(dp, f)
            if os.path.isfile(p) and p.endswith(('.md', '.txt', '.json')):
                total += update_file(p)

# 4. 90_LUU_TRU
for f in os.listdir('90_LUU_TRU'):
    p = os.path.join('90_LUU_TRU', f)
    if os.path.isfile(p):
        total += update_file(p)

# 5. .work
for f in os.listdir('.work'):
    p = os.path.join('.work', f)
    if os.path.isfile(p) and f.endswith(('.py', '.json', '.md')):
        total += update_file(p)

# 6. 01_KICH_BAN/Ho_So_Toi_Pham
hs_base = '01_KICH_BAN/Ho_So_Toi_Pham'
for d in os.listdir(hs_base):
    dp = os.path.join(hs_base, d)
    if os.path.isdir(dp):
        for f in os.listdir(dp):
            p = os.path.join(dp, f)
            if os.path.isfile(p) and p.endswith(('.md', '.txt', '.json')):
                total += update_file(p)

print(f"Targeted update completed! Total files updated: {total}")
