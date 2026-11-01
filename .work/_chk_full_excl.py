import json, pathlib
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")


def check(ep):
    prod = HERE / "kaggle_higgs" / ("out_higgs_prod_t%s" % ep) / ("out_higgs_prod_t%s" % ep)
    man_p = prod / "higgs_manifest.json"
    ex_p = HERE / ("higgs_exclude_f0_t%s.json" % ep)
    if not man_p.exists() or not ex_p.exists():
        print("T%s: thieu manifest hoac exclude (man=%s excl=%s)" % (ep, man_p.exists(), ex_p.exists()))
        return
    man = [r for r in json.loads(man_p.read_text(encoding="utf-8-sig")) if r.get("ok")]
    excl = set(json.loads(ex_p.read_text(encoding="utf-8-sig")))
    by = {}
    for r in man:
        by.setdefault(r["id"], []).append(r["file"])
    full = sorted([i for i, fs in by.items() if all(f in excl for f in fs)])
    print("T%s: %d file | %d cau | exclude=%d | cau bi loai TOAN BO: %s" % (ep, len(man), len(by), len(excl), full))


check("03")
check("04")
