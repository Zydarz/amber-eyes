import pathlib, re, os, time
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\_chunk_B_t03_en.log")
print("log exists:", p.exists(), "size:", p.stat().st_size if p.exists() else 0)
if p.exists():
    b = p.read_bytes()
    txt = b.decode("utf-16", errors="replace") if (b[:2] in (b"\xff\xfe", b"\xfe\xff") or b.count(0) > len(b)*0.02) else b.decode("utf-8-sig", errors="replace")
    lines = [l for l in txt.splitlines() if l.strip()]
    print("lines:", len(lines))
    for l in lines[-12:]:
        print("|", l[:200])
d = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cB")
for f in sorted(d.glob("*.mp4")):
    print(f.name, os.path.getsize(f))
