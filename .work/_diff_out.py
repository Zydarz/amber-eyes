import pathlib, hashlib
BK = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\_cu\en_t03_fix_20261103")
OUT = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban")
for name, bak in (("mo_ta.txt", "mo_ta.txt.bak"), ("description.txt", "description.txt.bak"), ("thumbnail.png", "thumbnail.png.bak")):
    a = (BK / bak)
    b = (OUT / name)
    if not a.exists() or not b.exists():
        print(name, "thieu", a.exists(), b.exists()); continue
    ha = hashlib.sha256(a.read_bytes()).hexdigest()[:12]
    hb = hashlib.sha256(b.read_bytes()).hexdigest()[:12]
    print(f"{name:16} cu {a.stat().st_size:7d}B -> moi {b.stat().st_size:7d}B | sha {ha} -> {hb} | {'GIONG' if ha==hb else 'DA DOI'}")
t = (OUT / "mo_ta.txt").read_text(encoding="utf-8")
print("do dai mo_ta.txt moi:", len(t), "ky tu (gioi han YouTube 5000)")
