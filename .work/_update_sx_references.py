import os, re

def update_file(path):
    try:
        content = open(path, encoding='utf-8', errors='ignore').read()
        if '02_SAN_XUAT' not in content:
            return 0
            
        new_content = content
        new_content = new_content.replace('02_SAN_XUAT/Ho_So_Toi_Pham/Tap', '02_SAN_XUAT/Ho_So_Toi_Pham/Tap')
        new_content = new_content.replace('02_SAN_XUAT\\Ho_So_Toi_Pham\\Tap', '02_SAN_XUAT\Ho_So_Toi_Pham\Tap')
        
        # Simple plain string replaces
        new_content = new_content.replace('02_SAN_XUAT/Ho_So_Toi_Pham/Tap', '02_SAN_XUAT/Ho_So_Toi_Pham/Tap')
        new_content = new_content.replace('02_SAN_XUAT\\Ho_So_Toi_Pham\\Tap', '02_SAN_XUAT\\Ho_So_Toi_Pham\\Tap')
        new_content = new_content.replace('02_SAN_XUAT\\\\Tap', '02_SAN_XUAT\\\\Ho_So_Toi_Pham\\\\Tap')
        
        # Pathlib replaces: "02_SAN_XUAT" / "Ho_So_Toi_Pham" / f"Tap" -> "02_SAN_XUAT" / "Ho_So_Toi_Pham" / f"Tap"
        new_content = re.sub(r'("02_SAN_XUAT")\s*/\s*(f?"Tap)', r'\1 / "Ho_So_Toi_Pham" / \2', new_content)
        new_content = re.sub(r"('02_SAN_XUAT')\s*/\s*(f?'Tap)", r"\1 / 'Ho_So_Toi_Pham' / \2", new_content)
        
        # In edition.py:
        # EP_DIR = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / EP["dir"] -> EP_DIR = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / EP["dir"]
        new_content = new_content.replace('ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / EP["dir"]', 'ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / EP["dir"]')
        new_content = new_content.replace("ROOT / '02_SAN_XUAT' / 'Ho_So_Toi_Pham' / EP['dir']", "ROOT / '02_SAN_XUAT' / 'Ho_So_Toi_Pham' / EP['dir']")
        
        new_content = new_content.replace('02_SAN_XUAT/Ho_So_Toi_Pham/Tap', '02_SAN_XUAT/Ho_So_Toi_Pham/Tap')
        new_content = new_content.replace('02_SAN_XUAT\Ho_So_Toi_Pham\Tap', '02_SAN_XUAT\\Ho_So_Toi_Pham\\Tap')
        
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

# 3. 02_SAN_XUAT non-tap files
for f in os.listdir('02_SAN_XUAT'):
    p = os.path.join('02_SAN_XUAT', f)
    if os.path.isfile(p):
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
hs_base_kb = '01_KICH_BAN/Ho_So_Toi_Pham'
if os.path.exists(hs_base_kb):
    for d in os.listdir(hs_base_kb):
        dp = os.path.join(hs_base_kb, d)
        if os.path.isdir(dp):
            for f in os.listdir(dp):
                p = os.path.join(dp, f)
                if os.path.isfile(p) and p.endswith(('.md', '.txt', '.json')):
                    total += update_file(p)

# 7. 02_SAN_XUAT/Ho_So_Toi_Pham
hs_base_sx = '02_SAN_XUAT/Ho_So_Toi_Pham'
if os.path.exists(hs_base_sx):
    for d in os.listdir(hs_base_sx):
        dp = os.path.join(hs_base_sx, d)
        if os.path.isdir(dp):
            for f in os.listdir(dp):
                p = os.path.join(dp, f)
                if os.path.isfile(p) and p.endswith(('.md', '.txt', '.json')):
                    total += update_file(p)

print(f"Targeted update completed! Total files updated: {total}")
