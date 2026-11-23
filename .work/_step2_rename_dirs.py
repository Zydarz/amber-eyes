import os, json, re, shutil

# Mapping list: (new_ep, old_ep)
shuffle_data = json.load(open('.work/_proposed_shuffle.json', encoding='utf-8'))
mapping = {item['old_ep']: item['new_ep'] for item in shuffle_data}

print(f"Total mappings: {len(mapping)}")

# Step 2A: Rename to temporary staging names
# Example: 01_KICH_BAN/Ho_So_Toi_Pham/Tap34 -> 01_KICH_BAN/_STAGING_Tap30 (if 34 -> 30)
# We handle all language variations: TapXX, TapXX_EN, TapXX_JA, TapXX_KO

def stage_and_rename_dir(base_path):
    print(f"--- Processing {base_path} ---")
    staged = []
    # 1. Rename to _STAGING_
    for d in sorted(os.listdir(base_path)):
        m = re.match(r"^Tap(\d+)(.*)$", d)
        if m:
            old_ep = int(m.group(1))
            suffix = m.group(2)
            if old_ep in mapping:
                new_ep = mapping[old_ep]
                src = os.path.join(base_path, d)
                staged_name = f"_STAGING_Tap{new_ep:02d}{suffix}"
                dst = os.path.join(base_path, staged_name)
                os.rename(src, dst)
                staged.append((dst, f"Tap{new_ep:02d}{suffix}"))

    # 2. Rename from _STAGING_ to final TapYY
    for src, final_name in staged:
        dst = os.path.join(base_path, final_name)
        os.rename(src, dst)
    print(f"Renamed {len(staged)} folders in {base_path}")

stage_and_rename_dir("01_KICH_BAN")
stage_and_rename_dir("02_SAN_XUAT")

print("Directory renaming completed successfully!")
