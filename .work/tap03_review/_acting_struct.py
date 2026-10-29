import json
import collections
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
els = json.loads((ROOT / ".work" / "script_tap03.json").read_text(encoding="utf-8"))

roles = collections.Counter()
actrole = collections.Counter()
for e in els:
    if e["kind"] != "LOI":
        continue
    role = e.get("role", "?")
    roles[role] += 1
    actrole[(e["id"].split(".")[0], role)] += 1
print("vai:", dict(roles))
print("act x vai:", dict(actrole))
print()
n = 0
for e in els:
    if e["kind"] != "LOI":
        continue
    role = e.get("role", "?")
    ss = e["sentences"]
    n += len(ss)
    print(f"{e['id']:<6} act{e['id'].split('.')[0]} vai={role:<2} n={len(ss):<2} | {ss[0]['text'][:70]}")
print("\ntong cau LOI:", n)
print("tong cau het (LOI):", sum(len(e['sentences']) for e in els if e['kind'] == 'LOI'))
