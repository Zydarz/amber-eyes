"""Do F0 tren chính 416 file SAN XUAT (theo vai) de xac nhan master dung giong."""
import json
import pathlib
import sys
from collections import defaultdict

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from g9_decide import f0_p2, fix_octave, nc  # noqa: E402
from check_reel_f0 import ac_of  # noqa: E402

PROD = HERE / "kaggle_higgs" / "out_higgs_prod" / "out_higgs_prod"
man = json.loads((PROD / "higgs_manifest.json").read_text(encoding="utf-8-sig"))
ok = [r for r in man if r.get("ok")]

by_role = defaultdict(list)
for r in ok:
    by_role[r["role"]].append(r)

print("%-4s %-12s %5s %8s %8s %9s" % ("vai", "clip", "n", "F0_ac", "F0_pp2", "trung vị"))
med = {}
for role in sorted(by_role):
    rows = sorted(by_role[role], key=lambda r: r["file"])
    # lay deu 6 file moi vai
    step = max(1, len(rows) // 6)
    pick = rows[::step][:6]
    acs, p2s, ref = [], [], pick[0].get("ref_wav", "?")
    for r in pick:
        p = PROD / r["file"]
        if not p.exists():
            continue
        import soundfile as sf
        x, sr = sf.read(str(p), dtype="float32")
        if x.ndim > 1:
            x = x.mean(axis=1)
        ac = ac_of(x, sr)
        p2 = f0_p2(x, sr)
        p2f, _ = fix_octave(ac, p2)
        acs.append(ac)
        p2s.append(p2f)
    if not acs:
        continue
    m_ac = float(np.median(acs))
    m_p2 = float(np.median(p2s))
    med[role] = (m_ac, m_p2)
    print("%-4s %-12s %5d %8.1f %8.1f %9.1f" % (role, ref, len(acs), m_ac, m_p2, m_ac))

print()
print("KHOANG CACH nc GIUA MOI CAP (van mapping san xuat):")
keys = list(med)
for i in range(len(keys)):
    for j in range(i + 1, len(keys)):
        a, b = keys[i], keys[j]
        v = min(nc(med[a][0], med[b][0]), nc(med[a][1], med[b][1]))
        print("  %-3s vs %-3s : %6.2f nc  %s" % (a, b, v, "OK" if v >= 4 else "DUOI 4"))
