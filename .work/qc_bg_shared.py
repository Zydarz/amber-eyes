"""Cong H17: nen dung chung moi ngon ngu (tieu chuan A8.1).
DIEU KIEN: cac ngon ngu phai dung tu CUNG phien ban kich ban/bang shot (ma shot trung nhau);
lech ma shot = ban ngon ngu do chua dong bo -> dong bo bang shot truoc.
Kiem: (1) tap nen moi ngon ngu bang nhau; (2) TUNG SHOT (cung id) dung cung nen;
(3) moi nen co file trong assets/bg; (4) 0 file nen mang hau to ngon ngu.
Dung: py -3 .work/qc_bg_shared.py --ep 08   (tap moi: LUON chay voi --ep)
      py -3 .work/qc_bg_shared.py           (quet het; tap trong MIEN_TRU chi canh bao)
exit 1 = loi."""
import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]; W = ROOT / ".work"; BG = ROOT / "assets/bg"
LANG_RE = re.compile(r"_(EN|JA|KO|VI|VN)\.(png|jpg|webp)$", re.I)
# Tap da dung/dang truoc khi co cong (10/11/2026) — lech da ghi nhan o tieu chuan A11 #145.
# Chi bo khi nguoi dung quyet dinh sua; --ep XX van bao LOI that.
MIEN_TRU = {"01": "KO con o bang shot cu 24/10 (122 shot); VN/EN/JA da dung lai 09/11 (203 shot)",
            "02": "VN/KO 161 shot, EN/JA 151 shot - lech phien ban bang shot (chua kiem noi dung)",
            "03": "EN/JA thua t3_car_door"}
only = sys.argv[sys.argv.index("--ep") + 1] if "--ep" in sys.argv else None

def load(p):
    d = json.loads(p.read_text(encoding="utf-8"))
    return {s.get("id"): s.get("bg") for s in (d["shots"] if isinstance(d, dict) else d)}

def exists(b):
    return (BG / b).exists() or any(BG.glob(b + ".*"))

eps = {}
for p in W.glob("shots*.json"):
    m = re.fullmatch(r"shots(?:_(EN|JA|KO))?(?:_t(\d\d))?\.json", p.name)
    if m: eps.setdefault(m.group(2) or "01", {})[m.group(1) or "VN"] = p
err = 0
for ep in sorted(eps):
    if only and ep != only: continue
    L = {k: load(v) for k, v in eps[ep].items()}
    bk = "VN" if "VN" in L else next(iter(L))
    base = L[bk]; sets = {k: {b for b in v.values() if b} for k, v in L.items()}
    probs = []
    for k, v in L.items():
        if k == bk: continue
        a, b = sorted(sets[bk] - sets[k]), sorted(sets[k] - sets[bk])
        if a or b: probs.append(f"{k}: thieu nen {a[:5]} · thua nen {b[:5]}")
        ids = sorted(set(base) ^ set(v))
        if ids: probs.append(f"{k}: {len(ids)} ma shot khong khop {bk}, vd {ids[:5]}")
        sh = [i for i in base if i in v and base[i] != v[i]]
        if sh: probs.append(f"{k}: {len(sh)} shot khac nen, vd " + ", ".join(f"{i}:{base[i]}->{v[i]}" for i in sh[:3]))
    miss = sorted(b for b in set().union(*sets.values()) if not exists(b))
    if miss: probs.append(f"thieu file assets/bg: {len(miss)}, vd {miss[:5]}")
    exempt = ep in MIEN_TRU and not only
    tag = "DAT " if not probs else ("MIEN" if exempt else "LOI ")
    err += bool(probs) and not exempt
    print(f"Tap{ep} {tag} " + " ".join(f"{k}={len(sets[k])}nen/{len(L[k])}shot" for k in sorted(L))
          + (f"  [mien tru: {MIEN_TRU[ep]}]" if exempt and probs else ""))
    for x in probs: print("   " + x)
bad = [f.name for f in BG.rglob("*") if LANG_RE.search(f.name)]
print(f"File nen co hau to ngon ngu: {len(bad)}", bad[:10]); err += bool(bad)
print("KET QUA:", "LOI" if err else "DAT"); sys.exit(1 if err else 0)
