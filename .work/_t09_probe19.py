import io, json, os, glob
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
print("=== THỜI LƯỢNG SHOT NỘI DUNG trong các tập đã dựng (để biết tiền lệ) ===")
for p in sorted(glob.glob(str(ROOT/".work"/"shots_*.json"))):
    n = os.path.basename(p)
    if "text" in n: continue
    try:
        d = json.loads(io.open(p, encoding="utf-8").read())
        sh = d["shots"] if isinstance(d, dict) else d
    except Exception as e:
        print(f"  {n}: ERR {e}"); continue
    content = [s for s in sh if (s.get("template") or "") not in ("T10","T8") and s["id"] != sh[-1]["id"]]
    if not content: continue
    durs = [s["end"]-s["start"] for s in content]
    over = [x for x in durs if x > 15.0]
    under = [x for x in durs if x < 3.0]
    print(f"  {n:26s} n={len(content):4d} TB={sum(durs)/len(durs):5.2f} max={max(durs):6.2f} "
          f">15s={len(over):3d} <3s={len(under):3d}")
