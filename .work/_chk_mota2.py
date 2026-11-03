import pathlib, re
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban\mo_ta.txt")
t = p.read_text(encoding="utf-8")
i = t.find("\U0001F4DA SOURCES")
blk = t[i:].split("\n\n",1)[0]
print("do dai mo_ta.txt:", len(t), "ky tu")
print("so link trong khoi SOURCES:", len(re.findall(r"https?://\S+", blk)))
print("con '[PENDING'?", "[PENDING" in t)
for k in ("CHAPTERS","00:23","05:32","10:45","16:28","22:02","988","911","#AmberEyes"):
    print(f"  co {k!r}: {k in t}")
