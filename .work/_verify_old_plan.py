import json
import re

plan = open(".work/_cu/KeHoach_Video_Tap02_EN_pre_countfix_20261101_103816.md", encoding="utf-8").read()
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

s = json.load(open(".work/_cu/script_tap02_EN.json.bak_20261031", encoding="utf-8"))
script_sents = set()
for e in s:
    for sent in e.get("sentences", []):
        script_sents.add(sent["id"])

print(f"Plan shots: {len(lines)}")
print(f"Plan unique sentences: {len(plan_sents)}")
print(f"Script unique sentences: {len(script_sents)}")
print(f"Diff Plan - Script: {plan_sents - script_sents}")
print(f"Diff Script - Plan: {script_sents - plan_sents}")
