"""Bao cao ngan gon: phan tu nao lech so cau, kem cau nao khong khop."""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import parse_kichban as PK  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

vn = PK.parse_lines(Path(sys.argv[1]).read_text(encoding="utf-8").splitlines())
ko = PK.parse_lines(Path(sys.argv[2]).read_text(encoding="utf-8").splitlines())

print(f"VN elements {len(vn)}   KO elements {len(ko)}")

i = j = 0
while i < len(vn) and j < len(ko):
    a, b = vn[i], ko[j]
    same = a["kind"] == b["kind"] and (a["kind"] != "LOI" or a["role"] == b["role"])
    if not same:
        d = None
        for k in range(1, 4):
            if i + k < len(vn) and j + k < len(ko) and vn[i + k]["kind"] == ko[j + k]["kind"] \
               and (vn[i + k]["kind"] != "LOI" or vn[i + k]["role"] == ko[j + k]["role"]):
                d = k
                break
        if d is None:
            print(f"!! DIVERGE VN[{i}] {a['id']}/{a['kind']}/{a.get('role','')} :: {a.get('text', a.get('desc',''))[:70]}")
            print(f"            KO[{j}] {b['id']}/{b['kind']}/{b.get('role','')} :: {b.get('text', b.get('desc',''))[:70]}")
            i += 1
            j += 1
            continue
        print(f"!! RESYNC +{d} at VN[{i}] KO[{j}]")
        for k in range(d):
            print(f"   VN {vn[i+k]['id']} {vn[i+k]['kind']}/{vn[i+k].get('role','')} :: {vn[i+k].get('text', vn[i+k].get('desc',''))[:80]}")
        i += d
        j += d
        continue
    if a["kind"] == "LOI":
        na, nb = len(a["sentences"]), len(b["sentences"])
        if na != nb:
            print(f"XX {a['id']} role={a['role']}: VN {na} vs KO {nb}")
            for k in range(max(na, nb)):
                sa = a["sentences"][k]["text"] if k < na else "<<< MISSING IN KO >>>"
                sb = b["sentences"][k]["text"] if k < nb else "<<< EXTRA IN KO >>>"
                print(f"   VN[{k+1}] {sa[:120]}")
                print(f"   KO[{k+1}] {sb[:120]}")
    i += 1
    j += 1
print(f"TAIL: VN left {len(vn)-i}, KO left {len(ko)-j}")
for a in vn[i:]:
    print(f"   VN {a['id']} {a['kind']}/{a.get('role','')} :: {a.get('text', a.get('desc',''))[:90]}")
for b in ko[j:]:
    print(f"   KO {b['id']} {b['kind']}/{b.get('role','')} :: {b.get('text', b.get('desc',''))[:90]}")
