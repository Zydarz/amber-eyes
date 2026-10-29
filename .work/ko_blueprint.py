#!/usr/bin/env python3
"""BAN DO (blueprint) de dich 1 tap sang tieng Han.

    usage: py -3 .work/ko_blueprint.py 01_KICH_BAN/Tap07/kichban_tap07_23102026.md [out.txt]

In ra, theo thu tu file, moi phan tu:
  - loai (LOI / SFX / BGM / NGHI), vai, so cau, chi danh doc
  - tung cau cua file VN (de dich 1-1)
  - cac chu so phai giu nguyen, cac ten rieng Latin phai giu nguyen
  - danh sach dau nhay ('...') va so gach dau dong
Cuoi file in tong hop: so element, so cau, so trich dan, so gach dau dong.
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402
import _qc_ko_parity as QC  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

src = Path(sys.argv[1])
out = Path(sys.argv[2]) if len(sys.argv) > 2 else None
if out:
    sys.stdout = out.open("w", encoding="utf-8")

raw = src.read_text(encoding="utf-8")
lines = raw.splitlines()
els = PK.parse_lines(lines)

role_re = re.compile(r"^\*\*(" + "|".join(PK.ROLES) + r")\*\*\s*(?:\*\((.*?)\)\*)?\s*:")
cue_re = re.compile(r"^\*\*\[(SFX|BGM)\]:\*\*")
pause_re = re.compile(r"^\*\*\[(?:Nghỉ |Pause |정지 |休止 )")
act_re = re.compile(r"^## (?:HỒI|ACT|막|第)\s*(\d)")

# ---- doc moi phan tu theo thu tu file (co canh bao merge) ----
items = []
cur = None
for ln in lines:
    s = ln.strip()
    if act_re.match(s):
        cur = None
        items.append({"kind": "ACT", "text": s})
        continue
    if not s or s == "---":
        continue
    if cue_re.match(s):
        cur = None
        items.append({"kind": "CUE", "text": s})
        continue
    if pause_re.match(s):
        cur = None
        items.append({"kind": "PAUSE", "text": s})
        continue
    m = role_re.match(s)
    if m:
        cur = {"kind": "ROLE", "role": PK.ROLES[m.group(1)], "dir": m.group(2) or "", "lines": []}
        items.append(cur)
        continue
    if cur is None:
        continue
    t = re.sub(r"^\*\s+", "", s)
    t = re.sub(r"^\d+\.\s+", "", t)
    t = t.replace("**", "").replace("*", "")
    t = t.strip().strip('"“”').strip()
    t = re.sub(r"'([^']+)'", r"\1", t)
    if t:
        cur["lines"].append(t)


def nsent(b):
    n = 0
    for ln in b["lines"]:
        if any(ch in ln for ch in "。！？"):
            n += len([x for x in PK.ja_split(ln) if x.strip()])
        else:
            n += len([x for x in re.split(PK.LATIN_SPLIT, ln) if x.strip()])
    return n


# gop cac block lien tiep cung vai, khong co cue giua -> parser gop thanh 1 element
groups = []
for it in items:
    if it["kind"] != "ROLE":
        groups.append([it])
        continue
    if groups and groups[-1][0]["kind"] == "ROLE" and groups[-1][-1]["role"] == it["role"]:
        groups[-1].append(it)
    else:
        groups.append([it])

print("#" * 100)
print(f"# BLUEPRINT: {src}")
print(f"# elements={len(els)}  sentences={sum(len(e['sentences']) for e in els if e['kind']=='LOI')}")
print("#" * 100)

loi_els = [e for e in els if e["kind"] == "LOI"]
ei = 0
for g in groups:
    if g[0]["kind"] == "ACT":
        print(f"\n{g[0]['text']}")
        continue
    if g[0]["kind"] == "CUE":
        print(f"  {g[0]['text']}")
        continue
    if g[0]["kind"] == "PAUSE":
        print(f"  {g[0]['text']}")
        continue
    ei += 1
    e = loi_els[ei - 1]
    print(f"\n--- element {ei} | {e['id']} | role={e['role']} | SENTENCES={len(e['sentences'])} "
          f"| blocks={len(g)} ---")
    for b in g:
        print(f"  [role line] **{b['role']}** *({b['dir']})*")
        for k, ln in enumerate(b["lines"], 1):
            print(f"    {k}. {ln}")
    print(f"  NUM: {sorted(QC.numset(e['text']))}")
    print(f"  PRN: {sorted(QC.props(e['text']))}")

vn_q = re.findall(r"'([^']{2,})'", raw)
LIST_ITEM = re.compile(r"^\s*(?:\*\s{2,}|\d+\.\s{1,})\S")
items_l = [l for l in lines if LIST_ITEM.match(l)]
print("\n" + "#" * 100)
print(f"# TRICH DAN (type-1: giu nguyen tieng Anh trong '...'; type-2: dich ben trong): {len(vn_q)}")
for i, q in enumerate(vn_q, 1):
    print(f"  [{i}] {q}")
print(f"# GACH DAU DONG: {len(items_l)}")
for l in items_l:
    print(f"  | {l[:140]}")
print(f"# TONG: elements={len(els)} sentences={sum(len(e['sentences']) for e in els if e['kind']=='LOI')} "
      f"quotes={len(vn_q)} listitems={len(items_l)}")
