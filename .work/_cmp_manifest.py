# -*- coding: utf-8 -*-
"""So sanh manifest EN hien tai voi ban HEAD (doc qua git show, khong ghi file tam)."""
import json
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
p = ".work/_tk_notext_manifest_EN_t04.json"
cur = json.loads(open(p, encoding="utf-8").read())
head = json.loads(subprocess.check_output(["git", "show", f"HEAD:{p}"]).decode("utf-8"))
print("Hien tai:", len(cur), "entry | HEAD:", len(head), "entry")
for e in cur:
    print("  CUR ", e["lang"], e["clip"], round(e["audio_s"], 2))
for e in head:
    print("  HEAD", e["lang"], e["clip"], round(e["audio_s"], 2))
