# -*- coding: utf-8 -*-
"""In cac dong bang shot Tap05 bi anh huong boi ban script moi (162 cau)
keo theo noi dung cau moi de sua lai bang shot."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

W = Path(r"D:\TEST\Gax\amber-eyes\.work")
PLAN = Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap05\KeHoach_Video_Tap05.md")
CHANGED = {"1.03", "1.05", "1.07", "1.09", "1.10", "1.12", "1.14", "2.02", "2.04",
           "2.05", "2.06", "3.02", "3.05", "3.07", "4.02", "4.04", "4.08", "4.10",
           "4.12", "4.14", "4.15", "5.02", "5.08"}

script = {el["id"]: el for el in json.loads((W / "script_tap05.json").read_text(encoding="utf-8-sig"))}
sent = {}
for el in script.values():
    for s in el.get("sentences", []):
        sent[s["id"]] = s["text"]

text = PLAN.read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
sec = text[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]

RE_SENT = re.compile(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?")
for line in sec.splitlines():
    if not re.match(r"\|\s*[1-5]-\d+", line):
        continue
    c = [x.strip() for x in line.strip().strip("|").split("|")]
    ids = []
    for ma, a, b in RE_SENT.findall(c[1]):
        ids += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    elems = {i.split("#")[0] for i in ids}
    if not (elems & CHANGED):
        continue
    print("=" * 100)
    print("SHOT %-5s | vai %-4s | mau %-12s | nen %s" % (c[0], c[2][:4], c[3][:12], c[4][:60]))
    print("  range : %s" % c[1])
    print("  CHU   : %s" % c[5])
    print("  BEAT  : %s" % c[6][:70])
    for i in ids:
        if i in sent:
            print("   %-10s %s" % (i, sent[i]))
        else:
            print("   %-10s (KHONG TON TAI)" % i)
