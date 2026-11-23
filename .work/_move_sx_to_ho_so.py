import os, shutil

src_base = "02_SAN_XUAT"
target_base = os.path.join(src_base, "Ho_So_Toi_Pham")

os.makedirs(target_base, exist_ok=True)

# List all items starting with Tap
tap_folders = [d for d in os.listdir(src_base) if d.startswith("Tap")]
print(f"Moving {len(tap_folders)} folders into {target_base}...")

moved = 0
for d in tap_folders:
    src = os.path.join(src_base, d)
    dst = os.path.join(target_base, d)
    shutil.move(src, dst)
    moved += 1

print(f"Successfully moved {moved} folders into {target_base}!")
remaining = os.listdir(src_base)
print(f"Remaining in 02_SAN_XUAT: {remaining}")
