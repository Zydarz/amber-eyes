import re, sys, hashlib
sys.stdout.reconfigure(encoding="utf-8")
a = r"D:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap02/kichban_tap02_EN.md"
b = r"D:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md"
src = open(a, encoding="utf-8").read()
new, n = re.subn(r"(?<=[A-Za-z])'(?=[A-Za-z])", "\u2019", src)
open(a, "w", encoding="utf-8", newline="").write(new)
print("thay", n, "dau nhay trong tu -> ’ (ban trong Tap02/)")
print("trung khop ban Tap02_EN/:", open(a, encoding="utf-8").read() == open(b, encoding="utf-8").read())
