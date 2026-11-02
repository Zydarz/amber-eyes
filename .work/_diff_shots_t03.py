import json, re
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
ROOT = Path(r"D:\TEST\Gax\amber-eyes")
tl = json.loads((W/"timeline_s_t03.json").read_text(encoding="utf-8-sig"))
sent = {it["id"]: it for it in tl["items"]}
plan = (ROOT/"02_SAN_XUAT"/"Tap03"/"KeHoach_Video_Tap03.md").read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
rows = [l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]
refs = []
for l in rows:
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    sid, cau = cells[0], cells[1]
    for ma,a,b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cau):
        for k in range(int(a), int(b or a)+1):
            refs.append((sid, f"{ma}#{k}"))
missing = [(s,r) for s,r in refs if r not in sent]
print("Tong so cau tham chieu:", len(refs), "| thieu:", len(missing))
print()
# group by element
from collections import defaultdict
missing_by_el = defaultdict(list)
for s,r in missing:
    el = r.split("#")[0]
    missing_by_el[el].append((s,r))
for el in sorted(missing_by_el):
    ids = [r for _,r in missing_by_el[el]]
    have = sorted([k for k in sent if k.startswith(el+"#")], key=lambda x:int(x.split("#")[1]))
    print(f"--- element {el} ---  thieu: {ids}")
    print(f"    timeline co: {have}")
    for h in have:
        print(f"      {h} [{sent[h]['role']}] {sent[h]['text'][:110]}")
    print()
