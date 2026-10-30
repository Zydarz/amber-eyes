#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh anh nền song song: chia danh sach thanh N worker, moi worker 1 file provenance rieng,
sau do gop vao provenance.json chinh. Khong worker nao ghi cung 1 file anh.

usage: py -3 .work/gen_parallel.py .work/bg_jobs_tap03.json 3
"""
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BG = ROOT / "assets" / "bg"

jobs_path = Path(sys.argv[1])
N = int(sys.argv[2]) if len(sys.argv) > 2 else 3
RETRY_ROUNDS = int(sys.argv[3]) if len(sys.argv) > 3 else 2

jobs = json.loads(jobs_path.read_text(encoding="utf-8"))
todo = [j["name"] for j in jobs if not (BG / f"{j['name']}.png").exists()]
print(f"{len(jobs)} tong · {len(todo)} chua co · {N} worker", flush=True)
if not todo:
    raise SystemExit(0)

# chia vay bang, moi worker mot phan khong chong nhau
chunks = [todo[i::N] for i in range(N)]
chunks = [c for c in chunks if c]

ep_tag = jobs_path.stem
provs = []
procs = []
for i, chunk in enumerate(chunks):
    pf = WORK / f"_prov_{ep_tag}_w{i}.json"
    if pf.exists():
        pf.unlink()
    provs.append(pf)
    env = dict(os.environ)
    env["AE_PROV"] = str(pf)
    env["PYTHONIOENCODING"] = "utf-8"
    args = [sys.executable, str(WORK / "gen_images.py"), str(jobs_path),
            "--only", ",".join(chunk)]
    print(f"worker {i}: {len(chunk)} anh -> {pf.name}", flush=True)
    procs.append(subprocess.Popen(args, env=env, cwd=str(ROOT),
                                  stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                  text=True, encoding="utf-8", errors="replace"))

# theo doi
for i, p in enumerate(procs):
    for line in p.stdout:
        line = line.rstrip()
        if line:
            print(f"[w{i}] {line}", flush=True)
    p.wait()
    print(f"[w{i}] done rc={p.returncode}", flush=True)

# ---- vong retry cho anh con thieu (lo loi "image post-processing failed") ----
retry_pf = WORK / f"_prov_{ep_tag}_retry.json"
for rnd in range(RETRY_ROUNDS):
    missing = [j["name"] for j in jobs if not (BG / f"{j['name']}.png").exists()]
    if not missing:
        break
    print(f"\n=== vong retry {rnd+1}: {len(missing)} anh con thieu ===", flush=True)
    for name in missing:
        env = dict(os.environ)
        env["AE_PROV"] = str(retry_pf)
        env["PYTHONIOENCODING"] = "utf-8"
        r = subprocess.run([sys.executable, str(WORK / "gen_images.py"), str(jobs_path),
                            "--only", name], env=env, cwd=str(ROOT),
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        print(f"  {name}: rc={r.returncode} {(r.stdout or '').strip()[-120:]}", flush=True)
        time.sleep(2)

# ---- gop provenance ----
main_prov = ROOT / "provenance.json"
merged = json.loads(main_prov.read_text(encoding="utf-8")) if main_prov.exists() else []
seen = {p.get("file") for p in merged}
added = 0
for pf in provs + [retry_pf]:
    if not pf.exists():
        continue
    try:
        recs = json.loads(pf.read_text(encoding="utf-8"))
    except Exception:
        continue
    for rec in recs:
        if rec.get("file") not in seen:
            merged.append(rec)
            seen.add(rec.get("file"))
            added += 1
main_prov.write_text(json.dumps(merged, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"\ngop provenance: +{added} ban ghi -> {main_prov.name}", flush=True)

missing = [j["name"] for j in jobs if not (BG / f"{j['name']}.png").exists()]
print(f"HOAN TAT: {len(jobs)-len(missing)}/{len(jobs)}", flush=True)
if missing:
    print("THIEU:", ", ".join(missing), flush=True)
    sys.exit(2)
