import json
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

def parse(path):
    out = f".work/_tmp_vfy.json"
    subprocess.run(["py", "-3", ".work/parse_kichban.py", str(path), out], check=True)
    d = json.load(open(out, encoding="utf-8"))
    return d

vn = parse("01_KICH_BAN/Tap02/kichban_tap02_22102026.md")
print(f"Total elements: {len(vn)}")
for i, e in enumerate(vn):
    if e["kind"] == "LOI":
        s_count = len(e["sentences"])
        first_sent = e["sentences"][0]["text"][:40] if s_count > 0 else ""
        print(f"El {i+1:02d} [{e['id']}] Act {e['act']} Role {e['role']} ({s_count} sents): {first_sent}...")
    else:
        print(f"El {i+1:02d} [{e['id']}] Act {e['act']} Kind {e['kind']}")
