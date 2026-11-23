import os, re, glob

# We need to update occurrences of:
# "01_KICH_BAN/Ho_So_Toi_Pham/Tap" -> "01_KICH_BAN/Ho_So_Toi_Pham/Tap"
# "01_KICH_BAN\\Ho_So_Toi_Pham\\Tap" -> "01_KICH_BAN\\Ho_So_Toi_Pham\\Tap"
# '01_KICH_BAN", f"Tap' -> '01_KICH_BAN", "Ho_So_Toi_Pham", f"Tap' (in Python Path objects)
# '01_KICH_BAN" / f"Tap' -> '01_KICH_BAN" / "Ho_So_Toi_Pham" / f"Tap'
# '01_KICH_BAN" / "Tap' -> '01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap'

patterns = [
    (re.compile(r'01_KICH_BAN/Ho_So_Toi_Pham/Tap'), '01_KICH_BAN/Ho_So_Toi_Pham/Tap'),
    (re.compile(r'01_KICH_BAN\\\\Tap'), '01_KICH_BAN\\\\Ho_So_Toi_Pham\\\\Tap'),
    (re.compile(r'01_KICH_BAN\\Ho_So_Toi_Pham\\Tap'), '01_KICH_BAN\\Ho_So_Toi_Pham\\Tap'),
    (re.compile(r'01_KICH_BAN"\s*/\s*f?"Tap'), lambda m: m.group(0).replace('01_KICH_BAN"', '01_KICH_BAN" / "Ho_So_Toi_Pham"')),
    (re.compile(r'01_KICH_BAN\'\s*/\s*f?\'Tap'), lambda m: m.group(0).replace("01_KICH_BAN'", "01_KICH_BAN' / 'Ho_So_Toi_Pham'")),
]

def update_file(path):
    try:
        content = open(path, encoding='utf-8', errors='ignore').read()
        if '01_KICH_BAN' not in content:
            return 0
        new_content = content
        # Don't double replace Ho_So_Toi_Pham
        # Protect already replaced ones
        new_content = new_content.replace('01_KICH_BAN/Ho_So_Toi_Pham/Tap', '__ALREADY_REPLACED_FORWARD__')
        new_content = new_content.replace('01_KICH_BAN\\Ho_So_Toi_Pham\\Tap', '__ALREADY_REPLACED_BACK__')
        
        # Replace
        new_content = re.sub(r'01_KICH_BAN/Ho_So_Toi_Pham/Tap', '01_KICH_BAN/Ho_So_Toi_Pham/Tap', new_content)
        new_content = re.sub(r'01_KICH_BAN\\\\Tap', '01_KICH_BAN\\\\Ho_So_Toi_Pham\\\\Tap', new_content)
        new_content = re.sub(r'01_KICH_BAN\\Ho_So_Toi_Pham\\Tap', '01_KICH_BAN\\Ho_So_Toi_Pham\\Tap', new_content)
        new_content = re.sub(r'("01_KICH_BAN")\s*/\s*(f?"Tap)', r'\1 / "Ho_So_Toi_Pham" / \2', new_content)
        new_content = re.sub(r"('01_KICH_BAN')\s*/\s*(f?'Tap)", r"\1 / 'Ho_So_Toi_Pham' / \2", new_content)
        
        # Restore
        new_content = new_content.replace('__ALREADY_REPLACED_FORWARD__', '01_KICH_BAN/Ho_So_Toi_Pham/Tap')
        new_content = new_content.replace('__ALREADY_REPLACED_BACK__', '01_KICH_BAN\\Ho_So_Toi_Pham\\Tap')
        
        if new_content != content:
            open(path, 'w', encoding='utf-8').write(new_content)
            return 1
        return 0
    except Exception as e:
        print(f"Error updating {path}: {e}")
        return 0

total_updated = 0

# 1. Update root files (*.md, *.py, *.json)
for f in glob.glob('*.*'):
    if f.endswith(('.md', '.py', '.json', '.txt')):
        total_updated += update_file(f)

# 2. Update 00_TIEU_CHUAN
for f in glob.glob('00_TIEU_CHUAN/**/*.*', recursive=True):
    total_updated += update_file(f)

# 3. Update 02_SAN_XUAT
for f in glob.glob('02_SAN_XUAT/**/*.*', recursive=True):
    total_updated += update_file(f)

# 4. Update 90_LUU_TRU
for f in glob.glob('90_LUU_TRU/**/*.*', recursive=True):
    total_updated += update_file(f)

# 5. Update .work (excluding _backup)
for f in glob.glob('.work/**/*.*', recursive=True):
    if '_backup' not in f:
        total_updated += update_file(f)

# 6. Update 01_KICH_BAN inside Ho_So_Toi_Pham
for f in glob.glob('01_KICH_BAN/Ho_So_Toi_Pham/**/*.*', recursive=True):
    total_updated += update_file(f)

print(f"Completed! Total files updated: {total_updated}")
