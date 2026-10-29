import sys, difflib
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

VN = sys.argv[1]
KO = sys.argv[2]
vn = PK.parse_lines(open(VN, encoding="utf-8").read().splitlines())
ko = PK.parse_lines(open(KO, encoding="utf-8").read().splitlines())

for a, b in zip(vn, ko):
    if a["kind"] != "LOI":
        continue
    sa = [s["text"] for s in a["sentences"]]
    sb = [s["text"] for s in b["sentences"]]
    if len(sa) == len(sb):
        continue
    print("=" * 100)
    print(f'TURN {a["id"]}  VN {len(sa)} vs KO {len(sb)}')
    sm = difflib.SequenceMatcher(None, sa, sb, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            continue
        if tag in ("replace", "delete"):
            for s in sa[i1:i2]:
                print(f"  VN- {s}")
        if tag in ("replace", "insert"):
            for s in sb[j1:j2]:
                print(f"  KO+ {s}")
