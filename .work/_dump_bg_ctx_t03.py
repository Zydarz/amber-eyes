import json
import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
os.environ.setdefault("AE_EP", "03")
os.environ.setdefault("AE_LANG", "vi")
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))["shots"]
SENT = {i["id"]: i["text"] for i in TL["items"]}

for s in SH:
    ids = s["sentences"]
    if not ids and s.get("inherit"):
        for p in SH:
            if p["id"] == s["inherit"]:
                ids = p["sentences"]
                break
    if not ids:
        ctx = "(thẻ tiêu đề / chuyển hồi)"
    else:
        ctx = " ".join(SENT[x] for x in ids)
    print(f"{s['id']:>5s} | {str(s.get('bg')):24s} | tmpl={str(s.get('template')):>4s} | "
          f"{round(s['end']-s['start'],1):5.1f}s | {ctx[:96]}")
