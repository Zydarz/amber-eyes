import re, sys, hashlib
sys.stdout.reconfigure(encoding="utf-8")
p = r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md"
txt = open(p, encoding="utf-8").read()
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", txt, re.M)
sec = txt[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
rows = [l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]
print("rows:", len(rows))
print("first:", rows[0][:160])
print("last :", rows[-1][:160])
tot = re.search(r"^\*\*Tổng:.*$", txt, re.M)
print("TONG:", tot.group(0)[:220] if tot else None)
