import pathlib
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban\mo_ta.txt")
lines = p.read_text(encoding="utf-8").splitlines()
for i in (2, 4, 6, 7, 8, 9, 10, 11):
    print(f"--- dong {i+1} ({len(lines[i])} ky tu) ---")
    print(lines[i])
