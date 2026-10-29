"""Kiem tra parser doc duoc ban tieng Han dung chua: so ho(i), vai, cau, nhi."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))

import parse_kichban as P

VN = ROOT / "01_KICH_BAN" / "Tap01" / "kichban_tap01_22102026_v2.md"
KO = ROOT / "01_KICH_BAN" / "Tap01_KO" / "kichban_tap01_KO.md"


def summarize(path):
    els = P.parse_file(path)
    acts, roles, n_sent, n_pause = [], {}, 0, 0
    for e in els:
        if e["act"] not in acts:
            acts.append(e["act"])
        if e["kind"] == "LOI":
            roles[e["role"]] = roles.get(e["role"], 0) + 1
            n_sent += len(e["sentences"])
        elif e["kind"] == "NGHI":
            n_pause += 1
    return acts, roles, n_sent, n_pause


for label, path in (("VN", VN), ("KO", KO)):
    acts, roles, n_sent, n_pause = summarize(path)
    print(f"{label}: acts={len(acts)} {acts} sentences={n_sent} pauses={n_pause}")
    print(f"    roles={roles}")

print()
print("--- KO first 3 LOI elements ---")
els = P.parse_file(KO)
shown = 0
for e in els:
    if e["kind"] != "LOI":
        continue
    print(f"[{e['id']}] role={e['role']} dir={e.get('direction','')!r}")
    for s in e["sentences"]:
        print(f"   #{s['id'].split('#')[1]} {s['text'][:80]}")
    shown += 1
    if shown >= 3:
        break
