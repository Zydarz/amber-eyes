"""Sinh SPEC + PAYLOAD cho VONG 2 (§7): cau trượt CER > 2% -> sinh them toi da 2 ban.

Input : .work/higgs_cer_rows_t02.json     (ket qua do cua measure_cer_prod.py)
        .work/kaggle_higgs/higgs_payload_t02.json (payload lượt 1)
        .work/g9_role_map.json              (phe gan vai)
Output: .work/kaggle_higgs/dataset_voxcpm2/prod_spec_r2.json
        .work/kaggle_higgs/dataset_voxcpm2/higgs_payload_r2.json

Bien variant: moi cau da co [0,1] (hoac [0,1,2] neu cau trich) -> vong 2 dung
[3,4] (hoac [4,5]) => seed khac => ket qua khac, khong ghi de ban cu.

Usage:
  python .work/build_spec_r2.py --max-cer 0.02
"""
import argparse
import json
import pathlib
import sys
from collections import Counter, defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
DS = HERE / "kaggle_higgs" / "dataset_voxcpm2"
DS.mkdir(parents=True, exist_ok=True)

ap = argparse.ArgumentParser()
ap.add_argument("--max-cer", type=float, default=0.02)
ap.add_argument("--rows", default=str(HERE / "higgs_cer_rows_t02.json"))
ap.add_argument("--extra", type=int, default=2, help="so ban them toi da")
a = ap.parse_args()

ROLE_MAP_RAW = json.loads((HERE / "g9_role_map.json").read_text(encoding="utf-8-sig"))
ROLE_MAP = {k: v for k, v in ROLE_MAP_RAW.items()
            if not k.startswith("_") and isinstance(v, str) and v.endswith(".wav")}
print("phan gan vai:", ROLE_MAP)

payload_src = json.loads((HERE / "kaggle_higgs" / "higgs_payload_t02.json").read_text(encoding="utf-8-sig"))
ITEMS_SRC = payload_src["items"]

spec_p = DS / "prod_spec.json"
spec1 = json.loads(spec_p.read_text(encoding="utf-8-sig")) if spec_p.exists() else {}
V_BY_ITEM_1 = spec1.get("variants_by_item", {})
VARIANTS_1 = spec1.get("variants", [0, 1])

# ---- doc CER, tim cau trượt ------------------------------------------------
rows_p = pathlib.Path(a.rows)
if not rows_p.exists():
    raise SystemExit("khong co %s — chay measure_cer_prod.py truoc" % rows_p)
rows = json.loads(rows_p.read_text(encoding="utf-8-sig"))
by_id = defaultdict(list)
for r in rows:
    if r.get("cer_ok") is not None:
        by_id[r["id"]].append(r)

bad = []
for sid, v in sorted(by_id.items()):
    cs = [x["cer"] for x in v if x.get("cer") is not None]
    if not cs:
        continue
    best = min(cs)          # dung bai tot nhat cua cau
    if best > a.max_cer:
        bad.append((sid, best, len(v)))

print("cau co du lieu CER: %d | trượt > %.0f%%: %d" % (len(by_id), 100 * a.max_cer, len(bad)))
for sid, c, n in bad:
    print("   %-12s CER tot nhat %.1f%% (%d ban)" % (sid, 100 * c, n))

if not bad:
    raise SystemExit("khong co cau nao trượt -> khong can vong 2")

# ---- sinh payload + spec vong 2 -------------------------------------------
by_src = {it["id"]: it for it in ITEMS_SRC}
r2_items = []
variants_by_item = {}
for sid, c, n in bad:
    src = by_src.get(sid)
    if src is None:
        print("!! khong tim thay cau %s trong payload" % sid)
        continue
    have = list(V_BY_ITEM_1.get(sid, VARIANTS_1))
    new_v = [max(have) + 1 + i for i in range(a.extra)]
    variants_by_item[sid] = new_v
    p = dict(src)
    p["ref_wav"] = ROLE_MAP[p["role"]]
    p["ref_txt"] = p["ref_wav"].replace(".wav", ".txt")
    r2_items.append(p)

r2_spec = {
    "episode": "02",
    "mode": "prod_r2",
    "purpose": "§7 — sinh them %d ban cho %d cau trượt CER > %.0f%%" % (
        a.extra, len(r2_items), 100 * a.max_cer),
    "gen_params": spec1.get("gen_params") or {
        "temperature": 0.8,
        "temp_by_role": {r: 0.8 for r in ROLE_MAP},
        "top_p": 0.95, "top_k": 50, "max_new_tokens": 1196,
        "sample_rate": 24000, "fade_in_ms": 30,
        "seed_scheme": "sha256(id|role|ref|temp|vN) -> int(hex[:8],16)",
    },
    "variants": VARIANTS_1,
    "variants_by_item": variants_by_item,
    "items": [it["id"] for it in r2_items],
}
r2_payload = {
    "episode": payload_src.get("episode", "02"),
    "lang": payload_src.get("lang", "vi"),
    "model": payload_src.get("model", "bosonai/higgs-tts-3-4b"),
    "ref_dir": payload_src.get("ref_dir", "/kaggle/input/amber-eyes-voice-ref-voxcpm2"),
    "role_ref": {r: {"wav": w, "txt": w.replace(".wav", ".txt")}
                 for r, w in ROLE_MAP.items()},
    "items": r2_items,
}

(DS / "prod_spec_r2.json").write_text(
    json.dumps(r2_spec, ensure_ascii=False, indent=1), encoding="utf-8")
(DS / "higgs_payload_r2.json").write_text(
    json.dumps(r2_payload, ensure_ascii=False, indent=1), encoding="utf-8")

n_files = sum(len(v) for v in variants_by_item.values())
print("\nvong 2: %d cau | %d file" % (len(r2_items), n_files))
print("theo vai:", dict(Counter(it["role"] for it in r2_items)))
print("-> ", DS / "prod_spec_r2.json")
print("-> ", DS / "higgs_payload_r2.json")
