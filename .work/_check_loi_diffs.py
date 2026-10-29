import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

j = json.load(open(".work/test_parse_ja.json", encoding="utf-8"))
v = json.load(open(".work/_temp_vn2.json", encoding="utf-8"))

print(f"{'ID':<6} | {'ROLE':<4} | {'VN':<3} | {'JA':<3} | {'MATCH'}")
print("-" * 30)

mismatches = []
for ev, ej in zip(v, j):
    if ev["kind"] == "LOI":
        nv = len(ev["sentences"])
        nj = len(ej["sentences"])
        match = "OK" if nv == nj else "DIFF"
        print(f"{ev['id']:<6} | {ev['role']:<4} | {nv:<3} | {nj:<3} | {match}")
        if nv != nj:
            mismatches.append((ev["id"], ev["role"], nv, nj))

print("-" * 30)
print(f"Total LOI elements: {len([e for e in v if e['kind'] == 'LOI'])}")
print(f"Mismatched elements: {len(mismatches)}")
for m in mismatches:
    print(f"  {m[0]} (Role {m[1]}): VN has {m[2]} sents, JA has {m[3]} sents (diff: {m[3] - m[2]})")
