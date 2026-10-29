import json
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

out = ".work/_tmp_inspect_split.json"
subprocess.run(["py", "-3", ".work/parse_kichban.py", "01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md", out], check=True)
d = json.load(open(out, encoding="utf-8"))

turns = [e for e in d if e["kind"] == "LOI"]

for idx in [3, 24, 27]:
    t = turns[idx - 1]
    print(f"\n==========================================")
    print(f"Turn {idx} [{t['id']}] Role {t['role']} ({len(t['sentences'])} sentences):")
    for s in t["sentences"]:
        print(f"  [{s['id']}] {s['text']}")
