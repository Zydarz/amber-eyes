import os, shutil, json

# 1. Backup all 01_KICH_BAN, 02_SAN_XUAT folders for 29-68 and assets/bg for 29-34
backup_dir = ".work/_backup_before_shuffle"
if os.path.exists(backup_dir):
    shutil.rmtree(backup_dir)
os.makedirs(backup_dir, exist_ok=True)

# Backup directories
kb_backup = os.path.join(backup_dir, "01_KICH_BAN")
sx_backup = os.path.join(backup_dir, "02_SAN_XUAT")
bg_backup = os.path.join(backup_dir, "assets_bg")
os.makedirs(kb_backup, exist_ok=True)
os.makedirs(sx_backup, exist_ok=True)
os.makedirs(bg_backup, exist_ok=True)

# Copy 01_KICH_BAN
for d in os.listdir("01_KICH_BAN"):
    for ep in range(29, 69):
        if d.startswith(f"Tap{ep:02d}"):
            src = os.path.join("01_KICH_BAN", d)
            dst = os.path.join(kb_backup, d)
            shutil.copytree(src, dst)

# Copy 02_SAN_XUAT
for d in os.listdir("02_SAN_XUAT"):
    for ep in range(29, 69):
        if d.startswith(f"Tap{ep:02d}"):
            src = os.path.join("02_SAN_XUAT", d)
            dst = os.path.join(sx_backup, d)
            shutil.copytree(src, dst)

# Copy assets/bg for t29..t34
for f in os.listdir("assets/bg"):
    for ep in range(29, 35):
        if f.startswith(f"t{ep}_"):
            shutil.copy2(os.path.join("assets/bg", f), os.path.join(bg_backup, f))

# Copy provenance.json
shutil.copy2("provenance.json", os.path.join(backup_dir, "provenance.json"))

print("Backup completed successfully!")
print(f"Backed up {len(os.listdir(kb_backup))} folders in 01_KICH_BAN")
print(f"Backed up {len(os.listdir(sx_backup))} folders in 02_SAN_XUAT")
print(f"Backed up {len(os.listdir(bg_backup))} image files in assets/bg")
