import json
import re

plan = open("02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md", encoding="utf-8").read()
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", plan, re.M)
sec = plan[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
lines = [l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]

plan_sents = set()
for l in lines:
    cells = [c.strip() for c in l.strip().strip("|").split("|")]
    cau = cells[1]
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cau):
        for k in range(int(a), int(b or a) + 1):
            plan_sents.add(f"{ma}#{k}")

s = json.load(open(".work/_cu/script_tap02_EN_bak.json", encoding="utf-8"))
script_sents = set()
for e in s:
    for sent in e.get("sentences", []):
        script_sents.add(sent["id"])

print(f"Plan unique sentences: {len(plan_sents)}")
print(f"Script unique sentences: {len(script_sents)}")
print(f"Difference Plan - Script: {plan_sents - script_sents}")
print(f"Difference Script - Plan: {script_sents - plan_sents}")
