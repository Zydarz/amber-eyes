import re, pathlib
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\00_TIEU_CHUAN\TIEU_CHUAN_DUNG_VIDEO.md")
t = p.read_text(encoding="utf-8")
nums = [int(m.group(1)) for m in re.finditer(r"^\|\s*(\d+)\s*\|", t, re.M)]
a11 = [n for n in nums]
print("so muc A11 trong toan file:", len(a11))
# kiem tra vung A11
i = t.find("## A11")
j = t.find("## A12")
seg = t[i:j]
rows = [int(m.group(1)) for m in re.finditer(r"^\|\s*(\d+)\s*\|", seg, re.M)]
print("A11:", len(rows), "tu", rows[0], "den", rows[-1], "| lien tiep:", rows == list(range(rows[0], rows[-1]+1)), "| trung:", len(rows)!=len(set(rows)))
