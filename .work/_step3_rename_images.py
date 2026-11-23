import os, json, re

shuffle_data = json.load(open('.work/_proposed_shuffle.json', encoding='utf-8'))
mapping = {item['old_ep']: item['new_ep'] for item in shuffle_data}

# Episodes with images: 29, 30, 31, 32, 33, 34
# Old -> New:
# 29 -> 29 (no change)
# 30 -> 31
# 31 -> 34
# 32 -> 40
# 33 -> 38
# 34 -> 30

image_mapping = {
    30: 31,
    31: 34,
    32: 40,
    33: 38,
    34: 30
}

print("Image mapping (old_ep -> new_ep):", image_mapping)

bg_dir = "assets/bg"
files = os.listdir(bg_dir)

# 1. Rename files in assets/bg via staging
staged_files = []
for f in files:
    m = re.match(r"^t(\d+)_(.+)$", f)
    if m:
        old_ep = int(m.group(1))
        rest = m.group(2)
        if old_ep in image_mapping:
            new_ep = image_mapping[old_ep]
            src = os.path.join(bg_dir, f)
            staged_name = f"_STAGING_t{new_ep}_{rest}"
            dst = os.path.join(bg_dir, staged_name)
            os.rename(src, dst)
            staged_files.append((dst, f"t{new_ep}_{rest}", f, f"t{new_ep}_{rest}"))

# Final rename from staging
for src, final_name, old_file, new_file in staged_files:
    dst = os.path.join(bg_dir, final_name)
    os.rename(src, dst)

print(f"Renamed {len(staged_files)} image files in {bg_dir}")

# 2. Update provenance.json
prov_path = "provenance.json"
prov = json.load(open(prov_path, encoding='utf-8'))

# Build a lookup for fast replacement
file_rename_dict = {old_f: new_f for _, _, old_f, new_f in staged_files}

updated_prov = []
for entry in prov:
    # If entry is dict
    if isinstance(entry, dict):
        # check fields like 'file', 'path', 'asset'
        for k, v in list(entry.items()):
            if isinstance(v, str):
                for old_f, new_f in file_rename_dict.items():
                    if old_f in v:
                        entry[k] = v.replace(old_f, new_f)
        updated_prov.append(entry)
    else:
        updated_prov.append(entry)

open(prov_path, 'w', encoding='utf-8').write(json.dumps(updated_prov, ensure_ascii=False, indent=2))
print("Updated provenance.json successfully!")
