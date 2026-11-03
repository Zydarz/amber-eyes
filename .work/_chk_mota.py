import pathlib, re
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban\mo_ta.txt")
t = p.read_text(encoding="utf-8")
blk = t.split("SOURCES",1)[1].split("\n\n",1)[0] if "SOURCES" in t else ""
links = re.findall(r"https?://\S+", blk)
print("do dai mo_ta.txt:", len(t), "ky tu (gioi han 5000)")
print("so link trong khoi SOURCES:", len(links))
print("con '[PENDING'?", "[PENDING" in t)
for k in ("CHAPTERS","AMBER EYES","988","111"):
    print(f"  co {k!r}: {k in t}")
