import json, re
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
tl = json.loads((W/"timeline_s_t03.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it for it in tl["items"]}
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]; sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
want = set("2-13 2-14 2-15 2-16 2-17 2-18 5-01 5-02 5-03 5-04 5-05".split())
for l in sec.splitlines():
    if not re.match(r"\|\s*[1-5]-\d+", l): continue
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    if cells[0] not in want: continue
    sid, cau, vai, mau, nen, chu = cells[:6]
    print(f"### {sid} | cau={cau} | vai={vai} | mau={mau} | nen={nen}")
    print(f"    CHU: {chu}")
    ids=[]
    for ma,a,b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cau):
        for k in range(int(a), int(b or a)+1): ids.append(f"{ma}#{k}")
    for i in ids:
        if i in sent:
            s = sent[i]
            print(f"    {i} [{s['role']}] {s['text']}")
        else:
            print(f"    {i}  <<< KHONG CO >>>")
    print()
