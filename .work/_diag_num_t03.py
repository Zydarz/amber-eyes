import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
os.environ.setdefault("AE_EP", "03")
os.environ.setdefault("AE_LANG", "vi")
sys.path.insert(0, str(WORK))
import edition as ED

TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))["shots"]
SENT = {it["id"]: it for it in TL["items"]}

for target in ("1-02", "1-22"):
    s = next(x for x in SH if x["id"] == target)
    ids = s["sentences"]
    if not ids and s.get("inherit"):
        for p in SH:
            if p["id"] == s["inherit"]:
                ids = p["sentences"]
                break
    ctx = " ".join(SENT[x]["text"] for x in ids)
    if not ctx:
        ctx = " ".join(ED.EP["act_titles"].values())
    print("=" * 90)
    print(f"SHOT {target}  sentences={ids}")
    print("  on-screen elems:")
    for seg in s.get("segments", []):
        for kind, t in seg["elems"]:
            print(f"     [{kind}] {t!r}")
    print("  ctx (câu của shot):")
    for x in ids:
        print(f"     {x}: {SENT[x]['text']!r}")
    flat = ctx.replace(" ", "")
    allowed = set(re.findall(r"\d+", flat))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    screen = " ".join(str(e[1]) for seg in s.get("segments", []) for e in seg["elems"] if len(e) >= 2)
    print("  flat    :", flat[:200])
    print("  allowed :", sorted(allowed))
    print("  screen  :", screen[:200])
    for m in set(re.findall(r"\d[\d.,]*", screen)):
        tok = m.replace(".", "")
        print(f"     m={m!r} tok={tok!r} in_allowed={m in allowed} tok_in={tok in allowed} "
              f"raw_in_ctx={m in ctx} tok_in_ctx={tok in flat}")
