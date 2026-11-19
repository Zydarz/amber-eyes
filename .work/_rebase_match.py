#!/usr/bin/env python
# Do khop shots (phia LOCAL) voi 2 phia conflict cua timeline_s
import json
import os
import subprocess

REPO = r"D:/TEST/Gax/amber-eyes"

PAIRS = [
    (".work/shots_t14.json", ".work/timeline_s_t14.json", "t14"),
    (".work/shots_JA_t14.json", ".work/timeline_s_JA_t14.json", "JA t14"),
    (".work/shots_t15.json", ".work/timeline_s_t15.json", "t15"),
    (".work/shots_EN_t15.json", ".work/timeline_s_EN_t15.json", "EN t15"),
    (".work/shots_JA_t15.json", ".work/timeline_s_JA_t15.json", "JA t15"),
]


def read_file(p):
    with open(os.path.join(REPO, p), encoding="utf-8") as f:
        return json.load(f)


def read_stage(stage, p):
    raw = subprocess.check_output(["git", "-C", REPO, "show", f":{stage}:{p}"], stderr=subprocess.DEVNULL)
    return json.loads(raw.decode("utf-8"))


for shots_p, tl_p, label in PAIRS:
    print("=" * 90)
    print(label)
    try:
        s = read_file(shots_p)
    except Exception as e:
        print("  shots doc loi:", e)
        continue
    print("  shots total:", s.get("total"), "| acts:", json.dumps(s.get("acts"), ensure_ascii=False)[:200])
    for stage, name in ((2, "OURS(remote)"), (3, "THEIRS(local)")):
        t = read_stage(stage, tl_p)
        print(f"  {name}: total={t.get('total')} acts={json.dumps(t.get('acts'), ensure_ascii=False)[:200]}")
        for k in ("items", "shots"):
            if k in s and isinstance(s[k], list) and k in t and isinstance(t[k], list):
                ids_s = [x.get("id") for x in s[k]]
                ids_t = [x.get("id") for x in t[k]]
                print(f"    [{k}] shots={len(ids_s)} timeline={len(ids_t)} id_same={ids_s == ids_t}")
