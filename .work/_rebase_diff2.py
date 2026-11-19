#!/usr/bin/env python
# So sanh sâu 2 phia conflict: :2 = upstream, :3 = local
import json
import subprocess

REPO = r"D:/TEST/Gax/amber-eyes"
FILES = [
    ".work/timeline_s_EN_t15.json",
    ".work/timeline_s_JA_t14.json",
    ".work/timeline_s_JA_t15.json",
    ".work/timeline_s_t14.json",
    ".work/timeline_s_t15.json",
]


def load(stage, path):
    raw = subprocess.check_output(
        ["git", "-C", REPO, "show", f":{stage}:{path}"], stderr=subprocess.DEVNULL
    )
    return json.loads(raw.decode("utf-8"))


for f in FILES:
    a = load(2, f)
    b = load(3, f)
    print("=" * 100)
    print(f)
    ka, kb = set(a), set(b)
    print("  chi o OURS   :", sorted(ka - kb))
    print("  chi o THEIRS :", sorted(kb - ka))
    for k in sorted(ka & kb):
        va, vb = a[k], b[k]
        if va == vb:
            continue
        if isinstance(va, list) and isinstance(vb, list):
            if len(va) != len(vb):
                print(f"  [{k}] len ours={len(va)} theirs={len(vb)}")
                continue
            diff = [i for i, (x, y) in enumerate(zip(va, vb)) if x != y]
            print(f"  [{k}] {len(diff)} phan tu khac nhau (vi du idx {diff[:5]})")
            if diff:
                i = diff[0]
                print("      OURS  :", json.dumps(va[i], ensure_ascii=False)[:220])
                print("      THEIRS:", json.dumps(vb[i], ensure_ascii=False)[:220])
        elif isinstance(va, dict) and isinstance(vb, dict):
            dk = set(va) ^ set(vb)
            diff = [k2 for k2 in set(va) & set(vb) if va[k2] != vb[k2]]
            print(f"  [{k}] key khac: {sorted(dk)} | value khac: {diff[:8]}")
            for k2 in diff[:2]:
                print(f"      OURS   {k2}:", json.dumps(va[k2], ensure_ascii=False)[:200])
                print(f"      THEIRS {k2}:", json.dumps(vb[k2], ensure_ascii=False)[:200])
        else:
            print(f"  [{k}] OURS={va!r} THEIRS={vb!r}")
