import os, json, re

shuffle_data = json.load(open('.work/_proposed_shuffle.json', encoding='utf-8'))
mapping = {item['old_ep']: item['new_ep'] for item in shuffle_data}

# 1. Update file names inside 01_KICH_BAN/Ho_So_Toi_Pham/TapYY and 02_SAN_XUAT/Ho_So_Toi_Pham/TapYY
# e.g., kichban_tap34_19112026.md -> kichban_tap30_19112026.md
# KeHoach_Video_Tap34.md -> KeHoach_Video_Tap30.md

def update_internal_files():
    for old_ep, new_ep in mapping.items():
        if old_ep == new_ep:
            continue
            
        old_str = f"tap{old_ep:02d}"
        new_str = f"tap{new_ep:02d}"
        old_cap = f"Tap{old_ep:02d}"
        new_cap = f"Tap{new_ep:02d}"
        
        # Check all folders matching Tap{new_ep}* in 01_KICH_BAN and 02_SAN_XUAT
        for base in ["01_KICH_BAN", "02_SAN_XUAT"]:
            for d in os.listdir(base):
                if d.startswith(new_cap):
                    dir_path = os.path.join(base, d)
                    for f in os.listdir(dir_path):
                        if old_str in f.lower() or old_cap in f:
                            new_f = f.replace(old_str, new_str).replace(old_cap, new_cap)
                            src = os.path.join(dir_path, f)
                            dst = os.path.join(dir_path, new_f)
                            os.rename(src, dst)

update_internal_files()

# 2. Update titles inside Markdown files:
# Replace "TẬP XX" -> "TẬP YY", "Tập XX" -> "Tập YY", "TapXX" -> "TapYY"
def update_markdown_headers():
    for old_ep, new_ep in mapping.items():
        if old_ep == new_ep:
            continue
            
        old_2d = f"{old_ep:02d}"
        new_2d = f"{new_ep:02d}"
        new_cap = f"Tap{new_2d}"
        
        for base in ["01_KICH_BAN", "02_SAN_XUAT"]:
            for d in os.listdir(base):
                if d.startswith(new_cap):
                    dir_path = os.path.join(base, d)
                    for f in os.listdir(dir_path):
                        if f.endswith(".md") or f.endswith(".txt"):
                            p = os.path.join(dir_path, f)
                            try:
                                txt = open(p, encoding='utf-8').read()
                                # Patterns to replace:
                                # TẬP {old_ep} -> TẬP {new_ep}
                                # Tập {old_ep} -> Tập {new_ep}
                                # Tap{old_2d} -> Tap{new_2d}
                                # tap{old_2d} -> tap{new_2d}
                                new_txt = re.sub(rf'\bTẬP\s*{old_ep}\b', f'TẬP {new_ep}', txt)
                                new_txt = re.sub(rf'\bTẬP\s*{old_2d}\b', f'TẬP {new_2d}', new_txt)
                                new_txt = re.sub(rf'\bTập\s*{old_ep}\b', f'Tập {new_ep}', new_txt)
                                new_txt = re.sub(rf'\bTập\s*{old_2d}\b', f'Tập {new_2d}', new_txt)
                                new_txt = new_txt.replace(f"Tap{old_2d}", f"Tap{new_2d}")
                                new_txt = new_txt.replace(f"tap{old_2d}", f"tap{new_2d}")
                                if new_txt != txt:
                                    open(p, 'w', encoding='utf-8').write(new_txt)
                            except Exception as e:
                                print(f"Error reading {p}: {e}")

update_markdown_headers()
print("Internal filenames and headers updated successfully!")
