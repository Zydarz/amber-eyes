import io, json, os, re, sys
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

els = parse_file(str(ROOT/"01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))
sent = {}
for e in els:
    for i, s in enumerate(e.get("sentences", []), 1):
        sent[f"{e['id']}#{i}"] = s["text"]

jobs = json.loads((ROOT/".work/bg_jobs_tap09.json").read_text(encoding="utf-8"))

RANGE = re.compile(r"^(\d+)\.(\d+)#(\d+)(?:\D+(\d+))?$")
bad = []
used = set()
for j in jobs:
    m = RANGE.match(j["sentences"].strip())
    if not m:
        bad.append((j["name"], repr(j["sentences"]), "PARSE")); continue
    el = f"{int(m.group(1))}.{int(m.group(2)):02d}"
    a = int(m.group(3)); b = int(m.group(4) or a)
    for k in range(a, b+1):
        sid = f"{el}#{k}"
        if sid not in sent:
            bad.append((j["name"], j["sentences"], f"missing {sid}"))
        else:
            used.add(sid)

print(f"jobs={len(jobs)} broken={len(bad)}")
for b in bad[:20]: print("  ", b)
print(f"mapped sentences: {len(used)}/{len(sent)}")
un = [s for s in sent if s not in used]
print(f"NOT mapped: {len(un)}")
print("  ", un)

# per-element check: which elements are covered vs full
print()
print("=== per-element coverage (mapped / total) ===")
from collections import defaultdict
tot = defaultdict(int); cov = defaultdict(int)
for s in sent: tot[s.split("#")[0]] += 1
for s in used: cov[s.split("#")[0]] += 1
for el in sorted(tot, key=lambda x:(int(x.split('.')[0]), int(x.split('.')[1]))):
    flag = "" if cov[el]==tot[el] else "   <-- MISMATCH"
    print(f"  {el}: {cov[el]}/{tot[el]}{flag}")
