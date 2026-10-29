import sys, os, glob, re

sys.stdout.reconfigure(encoding="utf-8")

with open("02_SAN_XUAT/Tap07/Danh_Sach_Anh_Tap07.md", "r", encoding="utf-8") as f:
    text = f.read()

# find all `t7_...`
md_bgs = re.findall(r"`(t7_[a-zA-Z0-9_]+)`", text)
md_bgs_unique = list(dict.fromkeys(md_bgs))

disk_bgs = [os.path.basename(p)[:-4] for p in glob.glob("assets/bg/t7_*.png")]

print(f"BGs in markdown: {len(md_bgs_unique)}")
print(f"BGs on disk: {len(disk_bgs)}")

missing_on_disk = [b for b in md_bgs_unique if b not in disk_bgs]
extra_on_disk = [b for b in disk_bgs if b not in md_bgs_unique]

print("Missing on disk:", missing_on_disk)
print("Extra on disk:", extra_on_disk)
