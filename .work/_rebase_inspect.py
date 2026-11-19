#!/usr/bin/env python
# So sanh 2 phia cua conflict (rebase): :2 = upstream (origin/main), :3 = commit dang ap (local)
import json
import subprocess
import sys

REPO = r"D:/TEST/Gax/amber-eyes"

FILES = [
    ".work/timeline_s_EN_t15.json",
    ".work/timeline_s_JA_t14.json",
    ".work/timeline_s_JA_t15.json",
    ".work/timeline_s_t14.json",
    ".work/timeline_s_t15.json",
]


def show(stage, path):
    try:
        raw = subprocess.check_output(
            ["git", "-C", REPO, "show", f":{stage}:{path}"], stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        return "KHONG DOC DUOC"
    try:
        d = json.loads(raw.decode("utf-8"))
    except Exception as e:
        return f"JSON LOI: {e}"
    out = []
    if isinstance(d, dict):
        for k, v in d.items():
            if isinstance(v, list):
                out.append(f"{k}=list[{len(v)}]")
            elif isinstance(v, dict):
                out.append(f"{k}=dict[{len(v)}]")
            else:
                out.append(f"{k}={v!r}")
    elif isinstance(d, list):
        out.append(f"list[{len(d)}]")
    return " | ".join(out)[:400]


for f in FILES:
    print("=" * 100)
    print(f)
    print("  OURS   (upstream fdde269):", show(2, f))
    print("  THEIRS (local b250e5a)   :", show(3, f))
