import sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK
import importlib.util

spec = importlib.util.spec_from_file_location("qc", ".work/_qc_ko_parity.py")
qc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(qc)

vn = PK.parse_lines(open("01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md", encoding="utf-8").read().splitlines())
ko = PK.parse_lines(open("01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md", encoding="utf-8").read().splitlines())

for eid in ("1.03", "1.13", "3.02"):
    a = next(e for e in vn if e["id"] == eid)
    b = next(e for e in ko if e["id"] == eid)
    print("=" * 70)
    print("VN", eid, "sents", len(a["sentences"]))
    print(repr(a["text"][:300]))
    print("KO", eid, "sents", len(b["sentences"]))
    print(repr(b["text"][:300]))
    print("props VN:", sorted(qc.props(a["text"])))
    print("props KO:", sorted(qc.props(b["text"])))
    print("MISSING :", sorted(qc.props(a["text"]) - qc.props(b["text"])))
