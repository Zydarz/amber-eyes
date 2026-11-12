import io, json, os, re, glob, sys
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

# ---- current script ids
els = parse_file(str(ROOT/"01_KICH_BAN/Tap09/kichban_tap09_23102026.md"))
sent = {}
for e in els:
    for i, s in enumerate(e.get("sentences", []), 1):
        sent[f"{e['id']}#{i}"] = s["text"]

print("=== current script: elements ===")
for e in els:
    print(f"  {e['id']:>6} {e['kind']:>5} role={e.get('role','-'):>4} n_sent={len(e.get('sentences',[]))}")

# ---- bg jobs mapping check
jobs = json.loads((ROOT/".work/bg_jobs_tap09.json").read_text(encoding="utf-8"))
print()
print("=== bg_jobs mapping vs current script ===")
bad = []
used = set()
for j in jobs:
    m = re.match(r"^(\d\.\d+)#(\d+)(?:[–-](\d+))?$", j["sentences"])
    if not m:
        bad.append((j["name"], j["sentences"], "PARSE")); continue
    el, a, b = m.group(1), int(m.group(2)), int(m.group(3) or m.group(2))
    for k in range(a, b+1):
        sid = f"{el}#{k}"
        if sid not in sent:
            bad.append((j["name"], j["sentences"], f"missing {sid}"))
        else:
            used.add(sid)
print("  jobs:", len(jobs), "· broken:", len(bad))
for b in bad[:15]: print("   ", b)
covered = sorted(used, key=lambda x: (int(x.split(".")[0]), int(x.split(".")[1]), int(x.split("#")[1])))
print(f"  sentences mapped by bg_jobs: {len(used)}/{len(sent)}")
un = [s for s in sent if s not in used]
print("  sentences NOT mapped:", len(un), un[:20])

# ---- elements referenced by bg jobs
print()
print("=== elements referenced by bg_jobs ===")
print(" ", sorted({j['sentences'].split('#')[0] for j in jobs}))
