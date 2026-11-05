import re, sys
sys.stdout.reconfigure(encoding="utf-8")
p = r"D:/TEST/Gax/amber-eyes/01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md"
src = open(p, encoding="utf-8").read()
new, n = re.subn(r"(?<=[A-Za-z])'(?=[A-Za-z])", "\u2019", src)
open(p, "w", encoding="utf-8", newline="").write(new)
print("thay", n, "dau nhay trong tu -> ’")
