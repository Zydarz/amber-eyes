import json, re
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
tl = json.loads((W/"timeline_s_t03.json").read_text(encoding="utf-8-sig"))
sent = {i["id"]: i["text"] for i in tl["items"]}
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]; sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
want = {"1-09","1-13","1-14","1-15","2-21","2-22","4-09","5-15"}
for l in sec.splitlines():
    if not re.match(r"\|\s*[1-5]-\d+", l): continue
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if c[0] not in want: continue
    codes=[]
    for ma,x,y in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", c[1]):
        codes += [f"{ma}#{k}" for k in range(int(x), int(y or x)+1)]
    print(f"### {c[0]} | {c[1]} | bo cuc: {c[5][:150]}")
    for q in codes:
        print(f"    {q}: {sent.get(q,'?')}")
    for q in re.findall(r"“([^”]+)”", c[5]):
        print(f"    >>> QUOTE: {q}")
    print()
