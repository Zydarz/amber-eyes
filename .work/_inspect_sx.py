import os

items = os.listdir("02_SAN_XUAT")
print(f"Total items in 02_SAN_XUAT: {len(items)}")

tap_folders = [d for d in items if d.startswith("Tap")]
non_tap = [d for d in items if not d.startswith("Tap")]

print(f"Tap folders count: {len(tap_folders)}")
print(f"Sample Tap folders: {tap_folders[:10]}")
print(f"Non-Tap items in 02_SAN_XUAT: {non_tap}")
