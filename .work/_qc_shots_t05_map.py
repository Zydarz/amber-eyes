# -*- coding: utf-8 -*-
"""Kiem tra bang shot T05 (muc 6 cua ho so) khop voi timeline audio moi 162 cau.

Muc tieu: truoc khi chay parse_shots.py, biet truoc co ID cau nao trong bang shot
khong con ton tai trong timeline moi (do tach lai kich ban 164 -> 162 cau).
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")
W = ROOT / ".work"
TL_PATH = W / "timeline_s_t05.json"
PLAN = ROOT / "02_SAN_XUAT" / "Tap05" / "KeHoach_Video_Tap05.md"

tl = json.loads(TL_PATH.read_text(encoding="utf-8-sig"))
SENT = {it["id"]: it for it in tl["items"]}

text = PLAN.read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
sec = text[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
rows = [l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]

RE_SENT = re.compile(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?")
RE_ELEM = re.compile(r"`(\d\.\d+)`")

print("so dong shot trong bang :", len(rows))
used = []
missing = {}
for line in rows:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    sid, cau = cells[0], cells[1]
    ids = []
    for ma, a, b in RE_SENT.findall(cau):
        ids += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    if not ids:
        ids += RE_ELEM.findall(cau)
    for i in ids:
        used.append(i)
        if i not in SENT:
            missing.setdefault(sid, []).append(i)

print("so ID duoc tham chieu    :", len(used), "| ID thieu:", sum(len(v) for v in missing.values()))
if missing:
    print("!! DANH SACH ID THIEU (parse_shots.py se KeyError):")
    for sid, ids in missing.items():
        print("   shot %-6s -> %s" % (sid, ids))
else:
    print("OK: moi ID trong bang shot deu ton tai trong timeline moi")

# --- phu: timeline nao dang duoc dung, so cau theo vai, moc ---
print()
print("timeline dang dung:", TL_PATH.name, "| total:", tl["total"], "| intro:", tl["intro"])
roles = {}
for it in tl["items"]:
    roles[it["role"]] = roles.get(it["role"], 0) + 1
print("so cau theo vai    :", roles)
print("markers:", [(mk.get("id"), mk.get("type")) for mk in tl["markers"]][:12])

# --- in cac dong shot co lien quan 4.12 / 4.02 / 2.04 / 2.02 ---
print()
print("--- cac dong shot bi anh huong khi doi ma cau ---")
KEYS = ("4-12", "4-13", "4-14", "4-15", "4-16", "4-09", "4-10", "4-11",
        "2-03", "2-04", "2-05", "2-06", "2-07", "1-19", "1-20", "1-21")
for line in rows:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if cells[0] in KEYS:
        print("   %-6s | %-46s | vai %-3s | %s" % (cells[0], cells[1][:46], cells[2][:3], cells[4][:40]))

# --- dem bao phu: cau nao trong timeline chua xuat hien trong bang shot ---
shot_ids = set(used)
covered = set()
for line in rows:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    for ma, a, b in RE_SENT.findall(cells[1]):
        covered |= {f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)}
    covered |= set(RE_ELEM.findall(cells[1]))
uncovered = sorted(set(SENT) - covered)
print()
print("cau co trong timeline nhung KHONG xuat hien trong bang shot:", len(uncovered), uncovered[:20])
