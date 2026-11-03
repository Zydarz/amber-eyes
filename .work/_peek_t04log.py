import pathlib
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\render_tap04_en.log")
b = p.read_bytes()
t = b.decode("utf-16", errors="replace") if (b[:2] in (b"\xff\xfe", b"\xfe\xff") or b.count(0) > len(b)*0.02) else b.decode("utf-8-sig", errors="replace")
lines = t.splitlines()
print("--- 12 dong dau ---")
for l in lines[:12]: print("  ", l[:200])
print("--- 14 dong cuoi ---")
for l in lines[-14:]: print("  ", l[:200])
