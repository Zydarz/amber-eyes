# -*- coding: utf-8 -*-
"""Map cau CU -> MOI cho Tap05 (164 -> 162) va danh sach dong bang shot can sua.

Dung difflib.SequenceMatcher de canh hai danh sach cau theo noi dung.
"""
import difflib
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

W = Path(r"D:\TEST\Gax\amber-eyes\.work")
OLD = W / "_cu" / "t05_pre_higgs_20261101" / "script_tap05.json"
NEW = W / "script_tap05.json"
PLAN = Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap05\KeHoach_Video_Tap05.md")


def load(p):
    return {el["id"]: el for el in json.loads(p.read_text(encoding="utf-8-sig"))}


old, new = load(OLD), load(NEW)
so = {k: [(s["id"], s["text"]) for s in v.get("sentences", [])] for k, v in old.items()}
sn = {k: [(s["id"], s["text"]) for s in v.get("sentences", [])] for k, v in new.items()}
print("TONG cau: CU %d | MOI %d" % (sum(len(v) for v in so.values()),
                                    sum(len(v) for v in sn.values())))

mapping = {}          # id_cu -> id_moi (None = bi bo)
diff_elems = []
for e in sorted(set(so) | set(sn)):
    a = [t for _, t in so.get(e, [])]
    b = [t for _, t in sn.get(e, [])]
    if a == b:
        for i, (sid, _) in enumerate(so.get(e, [])):
            mapping[sid] = sn[e][i][0]
        continue
    diff_elems.append(e)
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                mapping[so[e][i1 + k][0]] = sn[e][j1 + k][0]
        elif tag == "replace":
            n = min(i2 - i1, j2 - j1)
            for k in range(n):
                mapping[so[e][i1 + k][0]] = sn[e][j1 + k][0]
            for k in range(n, i2 - i1):
                mapping[so[e][i1 + k][0]] = None
            for k in range(n, j2 - j1):
                mapping[sn[e][j1 + k][0]] = None      # cau moi, chua co trong bang shot cu
        elif tag == "delete":
            for k in range(i1, i2):
                mapping[so[e][k][0]] = None
        elif tag == "insert":
            for k in range(j1, j2):
                mapping[sn[e][k][0]] = None

print("\nelement co thay doi noi dung/so cau:", diff_elems)
for e in diff_elems:
    a, b = so.get(e, []), sn.get(e, [])
    print("\n=== %s : CU %d -> MOI %d ===" % (e, len(a), len(b)))
    sm = difflib.SequenceMatcher(None, [t for _, t in a], [t for _, t in b], autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                print("   = %-10s %s" % (sn[e][j1 + k][0], a[i1 + k][:100]))
        elif tag == "replace":
            for k in range(i1, i2):
                print("   - %-10s %s" % (a[k][0], a[k][1][:100]))
            for k in range(j1, j2):
                print("   + %-10s %s" % (b[k][0], b[k][1][:100]))
        elif tag == "delete":
            for k in range(i1, i2):
                print("   - %-10s %s   (BI BO)" % (a[k][0], a[k][1][:100]))
        elif tag == "insert":
            for k in range(j1, j2):
                print("   + %-10s %s   (CAU MOI)" % (b[k][0], b[k][1][:100]))

print("\n" + "=" * 78)
print("ID CU bi bo khoi kich ban moi :", sorted(k for k, v in mapping.items() if v is None and k in so))
newonly = sorted(k for k, v in mapping.items() if v is None and k not in so)
print("ID MOI khong co trong ban cu   :", newonly)

# --- dong bang shot can sua ---
text = PLAN.read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
sec = text[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
RE_SENT = re.compile(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?")
print()
print("DONG BANG SHOT:")
covered = set()
for line in sec.splitlines():
    if not re.match(r"\|\s*[1-5]-\d+", line):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    sid, cau = cells[0], cells[1]
    ids = []
    for ma, a2, b2 in RE_SENT.findall(cau):
        ids += [f"{ma}#{k}" for k in range(int(a2), int(b2 or a2) + 1)]
    covered |= set(ids)
    if not ids:
        continue
    newids = [mapping.get(i, i) for i in ids]
    if newids != ids:
        print("  %-6s | %-26s -> %s" % (sid, cau, " ".join(str(x) for x in newids)))

tl = json.loads((W / "timeline_s_t05.json").read_text(encoding="utf-8-sig"))
allids = [it["id"] for it in tl["items"]]
print()
print("cau timeline MOI chua shot nao dung:", [i for i in allids if i not in covered])
print("ID trong bang shot khong con trong timeline moi:",
      sorted(i for i in covered if i not in allids and i not in {mk.get("id") for mk in tl["markers"]}))
