import re
p = r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap02_KO/KeHoach_Video_Tap02_KO.md"
rows = [l for l in open(p, encoding="utf-8").read().splitlines() if re.match(r"\|\s*[1-5]-\d+\s*\|", l)]
for sid in ["1-03","1-13","3-24","3-29","4-13","5-10","5-31","1-35","2-25","3-30","4-34"]:
    for l in rows:
        if l.strip().startswith("| "+sid+" |"):
            c = l.split("|")
            print(sid, "| BEAT:", c[7].strip())
# any row whose beat still contains Vietnamese quoted phrase
vn = [l for l in open(r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md", encoding="utf-8").read().splitlines() if re.match(r"\|\s*[1-5]-\d+\s*\|", l)]
rem = []
for a,b in zip(vn, rows):
    for ph in re.findall(r'ở "([^"]+)"', a.split("|")[7]):
        if 'ở "%s"' % ph in b.split("|")[7]:
            rem.append(a.split("|")[1].strip()+" -> "+ph)
print("con cum beat VN chua thay:", rem)
