import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
rows = json.loads((ROOT / ".work/higgs_cer_rows_t06.json").read_text(encoding="utf-8-sig"))
print("type:", type(rows).__name__, "len:", len(rows))
r0 = rows[0] if isinstance(rows, list) else list(rows.values())[0]
print("field:", list(r0.keys()))
print("mau:", json.dumps(r0, ensure_ascii=False)[:500])

DONG = ["1.08#1", "2.06#3", "2.11#2", "2.11#3", "3.06#1", "3.11#1", "5.02#3"]
if isinstance(rows, list):
    print("\n=== 7 CAU DA SUA ===")
    for sid in DONG:
        sel = [r for r in rows if r.get("id") == sid or r.get("sid") == sid]
        if not sel:
            print(f"  {sid}: (khong co dong trong rows)")
            continue
        cers = [r.get("cer") for r in sel if r.get("cer") is not None]
        best = min(cers) if cers else None
        print(f"  {sid}: {len(sel)} ban · CER: {sorted(cers)}")
        for r in sel:
            txt = r.get("hyp") or r.get("text") or r.get("asr") or ""
            if txt:
                print(f"      - [{r.get('cer')}] {str(txt)[:170]}")
