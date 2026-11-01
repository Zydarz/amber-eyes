"""P7 — Do F0 moi file Higgs cua mot tap, lap danh sach loai (lech >= 4 nua cung).

  AE_EP=03 py -3 .work/check_higgs_f0.py            -> do moi file trong manifest
  AE_EP=03 py -3 .work/check_higgs_f0.py --new-only -> chi do file chua co trong _f0_tXX.json (sau vong 2/3)

F0 = trung vi YIN (`voxcpm_yin_f0.yin`) + AC (`voice_audition.f0_median`); moc so sanh = trung vi
cau neutral cua chinh vai (QUY_TAC_AUDIO_HIGGS §8). In G9 cho cac cap vai dung lien nhau trong kich ban.
Ghi: .work/_f0_tXX.json (tung file) · .work/higgs_exclude_f0_tXX.json (gop voi danh sach cu, khong xoa).
"""
import json
import math
import os
import pathlib
import sys
from collections import Counter, defaultdict

import numpy as np
import soundfile as sf

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
from voice_audition import f0_median  # noqa: E402
from voxcpm_yin_f0 import yin  # noqa: E402

import higgs_paths as P  # noqa: E402  (tap + ngon ngu, §4.4)
EPN = P.EPN
PROD = P.PROD_EP / P.PROD_EP.name
PAYLOAD = P.PAYLOAD_SRC
SCRIPT = P.SCRIPT
OUT_F0 = P.F0_JSON
OUT_EXCL = P.EXCLUDE


def nc(a, b):
    return abs(12 * math.log2(a / b))


def measure(path):
    x, sr = sf.read(str(path), dtype="float32")
    if x.ndim > 1:
        x = x.mean(axis=1)
    y = yin(x, sr)
    y = y[y > 0]
    return f0_median(x, sr), float(np.median(y)) if len(y) else float("nan")


def main():
    emo = {i["id"]: i["emotion"] for i in json.loads(PAYLOAD.read_text(encoding="utf-8-sig"))["items"]}
    man = [r for r in json.loads((PROD / "higgs_manifest.json").read_text(encoding="utf-8-sig")) if r.get("ok")]
    old = json.loads(OUT_F0.read_text(encoding="utf-8")) if OUT_F0.exists() else []
    done = {r["file"] for r in old} if "--new-only" in sys.argv else set()
    rows = [r for r in old if r["file"] in done]
    todo = [r for r in man if r["file"] not in done]
    print("tap %s | file: %d | can do: %d" % (EPN, len(man), len(todo)))
    for r in todo:
        ac, yv = measure(PROD / r["file"])
        rows.append({"file": r["file"], "id": r["id"], "role": r["role"], "emo": emo.get(r["id"], "?"),
                     "ac": ac, "yin": yv})

    med = {}
    for role in sorted({r["role"] for r in rows}):
        n = [r for r in rows if r["role"] == role and r["emo"] == "neutral"]
        if n:
            med[role] = (float(np.median([r["ac"] for r in n])), float(np.median([r["yin"] for r in n])))
            print("  %-3s neutral n=%-4d AC %.1f / YIN %.1f Hz" % (role, len(n), *med[role]))

    excl = set(json.loads(OUT_EXCL.read_text(encoding="utf-8"))) if OUT_EXCL.exists() else set()
    new_bad = []
    for r in rows:
        if r["role"] in med and nc(r["yin"], med[r["role"]][1]) >= 4 and r["file"] not in excl:
            new_bad.append(r["file"])
    excl |= set(new_bad)

    # G9: cap vai dung lien nhau trong kich ban (ke ca khac gioi)
    sc = json.loads(SCRIPT.read_text(encoding="utf-8"))
    n_el = {}
    try:
        import edition as ED  # noqa: E402
        n_el = ED.EPISODES[EPN]["n_element"]
    except Exception:
        pass
    seq = [n_el.get(e["id"], e["role"]) for e in sc if e["kind"] == "LOI" for _ in e["sentences"]]
    pairs = Counter(tuple(sorted(p)) for p in zip(seq, seq[1:]) if p[0] != p[1])
    print("G9 (cap lien ke, min AC/YIN):")
    for (a, b), k in pairs.most_common():
        if a in med and b in med:
            v = min(nc(med[a][0], med[b][0]), nc(med[a][1], med[b][1]))
            print("  %-3s-%-3s x%-2d %5.2f nc %s" % (a, b, k, v, "DAT" if v >= 4 else "TRUOT"))

    by_id = defaultdict(list)
    for r in rows:
        by_id[r["id"]].append(r["file"])
    all_out = [i for i, fs in by_id.items() if all(f in excl for f in fs)]
    print("G8 file lech moi: %d %s" % (len(new_bad), new_bad))
    print("tong danh sach loai: %d | cau MOI ban deu bi loai: %s" % (len(excl), all_out))
    OUT_F0.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    OUT_EXCL.write_text(json.dumps(sorted(excl), indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
