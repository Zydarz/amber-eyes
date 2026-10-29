import json
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

def parse(path):
    p = Path(path)
    out = f".work/_tmp_{p.stem}.json"
    subprocess.run(["py", "-3", ".work/parse_kichban.py", str(p), out], check=True)
    d = json.load(open(out, encoding="utf-8"))
    return d

vn = parse("01_KICH_BAN/Tap02/kichban_tap02_22102026.md")
ja = parse("01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md")

lv = [e for e in vn if e["kind"] == "LOI"]
lj = [e for e in ja if e["kind"] == "LOI"]

print(f"VN turns: {len(lv)}, JA turns: {len(lj)}")

diff_turns = [(i + 1, e_vn, e_ja) for i, (e_vn, e_ja) in enumerate(zip(lv, lj)) 
              if len(e_vn["sentences"]) != len(e_ja["sentences"])]

for idx, e_v, e_j in diff_turns:
    print(f"\n=======================================================")
    print(f"Turn {idx} (ID: {e_v['id']}, Role: {e_v['role']}): VN has {len(e_v['sentences'])} sents, JA has {len(e_j['sentences'])} sents")
    print("--- VN Sentences ---")
    for s in e_v["sentences"]:
        print(f"  [{s['id']}] {s['text']}")
    print("--- JA Sentences ---")
    for s in e_j["sentences"]:
        print(f"  [{s['id']}] {s['text']}")
