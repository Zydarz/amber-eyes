# -*- coding: utf-8 -*-
import pathlib, re
p = pathlib.Path("02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv")
b = p.read_bytes()
print("size", len(b), "crlf", b.count(b"\r\n"), "lf-total", b.count(b"\n"))
txt = b.decode("utf-8")
parts = re.split(r"(\r\n|\n|\r)", txt)
print("parts", len(parts))
rows = [p_ for p_ in parts if p_ not in ("\r\n", "\n", "\r", "")]
print("rows", len(rows))
for r in rows:
    if r.startswith("TK04"):
        print(repr(r[:400]))
        print("  EOL-after:", repr(parts[parts.index(r)+1] if parts.index(r)+1 < len(parts) else "END"))
