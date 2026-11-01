"""Chi tiet F0 cho 3 cau bi loai toan bo ban + thong ke danh sach loai T04.

Doc: .work/_f0_t04.json, .work/higgs_exclude_f0_t04.json,
     .work/kaggle_higgs/out_higgs_prod_t04/out_higgs_prod_t04/higgs_manifest.json
     .work/higgs_cer_rows_t04.json
"""
import json
import pathlib
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
EPN = "04"

f0 = json.loads((HERE / "_f0_t04.json").read_text(encoding="utf-8-sig"))
excl = set(json.loads((HERE / ("higgs_exclude_f0_t%s.json" % EPN)).read_text(encoding="utf-8-sig")))
man_p = HERE / "kaggle_higgs" / ("out_higgs_prod_t%s" % EPN) / ("out_higgs_prod_t%s" % EPN) / "higgs_manifest.json"
man = json.loads(man_p.read_text(encoding="utf-8-sig"))
cer_rows = json.loads((HERE / ("higgs_cer_rows_t%s.json" % EPN)).read_text(encoding="utf-8-sig"))
cer_by_file = {r["file"]: r["cer"] for r in cer_rows if r.get("cer_ok")}

print("== khoa _f0_t04.json ==")
print("type:", type(f0).__name__, "| len:", len(f0))
if isinstance(f0, dict):
    ks = list(f0.keys())[:5]
    print("vi du key:", ks)
    for k in ks:
        print("   ", k, "->", f0[k])
else:
    for r in f0[:5]:
        print("   ", r)

print("\n== danh sach loai (%d file) ==" % len(excl))
by_id = defaultdict(list)
for r in man:
    if r.get("ok"):
        by_id[r["id"]].append(r)

all_excl_ids = []
for sid, v in sorted(by_id.items()):
    files = [r["file"] for r in v]
    if all(f in excl for f in files):
        all_excl_ids.append(sid)
print("cau bi loai TOAN BO ban:", all_excl_ids)

print("\n== chi tiet tung cau bi loai toan bo ==")
for sid in all_excl_ids:
    print("\n--- %s ---" % sid)
    for r in sorted(by_id[sid], key=lambda x: x.get("variant", 0)):
        info = f0.get(r["file"]) if isinstance(f0, dict) else None
        print("   variant %s | %s | cer=%s | dur=%s | f0info=%s" % (
            r.get("variant"), r["file"],
            ("%.3f%%" % (100 * cer_by_file[r["file"]])) if r["file"] in cer_by_file else "NA",
            r.get("duration_s"), info))
