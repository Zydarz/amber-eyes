import pathlib
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban\mo_ta.txt")
t = p.read_text(encoding="utf-8")
for i, l in enumerate(t.splitlines(), 1):
    print(f"{i:3} [{len(l):4}] {l[:120]}")
print("TONG:", len(t))
