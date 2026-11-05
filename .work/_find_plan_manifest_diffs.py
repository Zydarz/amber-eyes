import json
import re

plan = open("02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md", encoding="utf-8").read()
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
lines = [l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]

manifest = json.load(open(".work/tts_manifest_EN_t02.json", encoding="utf-8"))
m_sents = set(x["id"] for x in manifest)

mismatches = []
for l in lines:
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    sid, cau = cells[0], cells[1]
    sents = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cau):
        for k in range(int(a), int(b or a) + 1):
            sents.append(f"{ma}#{k}")
    
    missing = [s for s in sents if s not in m_sents]
    if missing:
        mismatches.append((sid, cau, missing))

print(f"Total shots with invalid sentence IDs: {len(mismatches)}")
for sid, cau, miss in mismatches:
    print(f"  Shot {sid:5s} | Plan: {cau:25s} | Missing in manifest: {miss}")
