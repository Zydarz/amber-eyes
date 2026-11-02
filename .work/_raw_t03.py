from pathlib import Path
P = Path(r"D:\TEST\Gax\amber-eyes\.work\build_video3.py")
b = P.read_bytes()
print("BOM:", b[:3].hex(), "| CRLF count:", b.count(b"\r\n"), "| LF count:", b.count(b"\n"))
s = b.decode("utf-8-sig")
i = s.find("def badge_base")
print(repr(s[i-40:i+900]))
