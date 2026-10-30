"""Dung SPEC + PAYLOAD cho Kaggle (pilot v6 va san xuat Tap 02).

Vai -> clip tham chieu nam trong `.work/g9_role_map.json` (sua duoc, khong phai
dich code). Sau pilot v6 chi can sua file nay roi chay lai script nay.

Sinh ra (trong .work/kaggle_higgs/dataset_voxcpm2/):
  pilot_spec_v6.json    gen_params + danh sach item pilot
  pilot_payload_v6.json items pilot (id -> text/emotion/ref_wav)
  prod_spec.json        gen_params + 203 item san xuat
  higgs_payload_t02.json items san xuat voi clip moi theo role map

Quy tac §7: moi cau 2 ban (variant 0/1). Cau he lo/trich -> 3 ban (bo sung o
vong 2 bang spec rieng `prod_spec_r2.json` sau khi do CER).
"""
import json
import pathlib
import re
import sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent          # .work/
ROOT = HERE.parent
DS = HERE / "kaggle_higgs" / "dataset_voxcpm2"
DS.mkdir(parents=True, exist_ok=True)

ROLE_MAP_P = HERE / "g9_role_map.json"
_ROLE_MAP_RAW = json.loads(ROLE_MAP_P.read_text(encoding="utf-8-sig"))
# chi lay khoa vai that (bo khoa metadata bat dau bang "_")
ROLE_MAP = {k: v for k, v in _ROLE_MAP_RAW.items()
            if not k.startswith("_") and isinstance(v, str) and v.endswith(".wav")}
assert ROLE_MAP, "g9_role_map.json khong co vai nao"
print("phan gan vai -> clip:")
for k, v in ROLE_MAP.items():
    print("   %-3s -> %s" % (k, v))

PAYLOAD_SRC = HERE / "kaggle_higgs" / "higgs_payload_t02.json"
payload_src = json.loads(PAYLOAD_SRC.read_text(encoding="utf-8-sig"))
ITEMS_SRC = payload_src["items"]

# ------------------------------------------------------------------ gen params (§6)
GEN_PARAMS = {
    "temperature": 0.8,
    "temp_by_role": {"H": 0.8, "D": 0.8, "C": 0.8, "N1": 0.8, "N2": 0.8},
    "top_p": 0.95,
    "top_k": 50,
    "max_new_tokens": 1196,     # = int(47.5 * 25.02) + 8
    "sample_rate": 24000,
    "fade_in_ms": 30,
    "seed_scheme": "sha256(id|role|ref|temp|vN) -> int(hex[:8],16)",
}

# ================================================================== PILOT v6
# 13 o: 4 clip moi + 4 bien the hao cao do + 5 o co so de doi chieu C/va chay
# cung batch (cung nhieu thieu so dong giua cac o).
PILOT_CELLS = [
    ("H", "M_LOW.wav", "H <- M_LOW (nam rat tram, 95.6 Hz)"),
    ("D", "M_HIGH.wav", "D <- M_HIGH (nam cao, 192.0 Hz)"),
    ("C", "C.wav", "CO SO: C <- C.wav (da do 205.1/194.9 o pilot v3/v4)"),
    ("N1", "W6_LOW.wav", "N1 <- W6_LOW (chua hao, 179.1 Hz)"),
    ("N1", "W6_LOW_S25.wav", "N1 <- W6_LOW hao -2.5 nua cung"),
    ("N1", "W6_LOW_S30.wav", "N1 <- W6_LOW hao -3.0 nua cung"),
    ("N1", "W6_LOW_S35.wav", "N1 <- W6_LOW hao -3.5 nua cung"),
    ("N1", "W6_LOW_S40.wav", "N1 <- W6_LOW hao -4.0 nua cung"),
    ("N2", "W5_HIGH.wav", "N2 <- W5_HIGH (nu cao, 289.2 Hz)"),
    ("N2", "W2.wav", "CO SO: N2 <- W2.wav (da do 206.9/198.7 o pilot v3/v4)"),
    ("N2", "W1.wav", "CO SO: N2 <- W1.wav (da do 275.9/258.3 o pilot v3/v4)"),
    ("H", "H.wav", "CO SO: H <- H.wav (da do 131.1/125.7 o pilot v3/v4)"),
    ("D", "D.wav", "CO SO: D <- D.wav (da do 122.4/125.6 o pilot v3/v4)"),
]

# 6 cau dung chung cho MOI o -> so sanh F0 giua cac o khong nhieu nhau.
# 5 cau trung tinh + 1 cau co the emotion (kiem lai §5 tren clip moi).
RE_HIGGS_TAG = re.compile(r"<\|[^|]+\|>")


def pick_pilot_sentences():
    by_role = {}
    for it in ITEMS_SRC:
        by_role.setdefault(it["role"], []).append(it)
    out, seen = [], set()

    def take(role, need_tag, want_long=None):
        cands = by_role.get(role, [])
        if want_long is True:
            cands = sorted(cands, key=lambda x: -len(x["text"]))
        elif want_long is False:
            cands = sorted(cands, key=lambda x: len(x["text"]))
        for c in cands:
            has_tag = bool(RE_HIGGS_TAG.search(c["text"]))
            if has_tag != need_tag:
                continue
            if c["id"] in seen:
                continue
            seen.add(c["id"])
            out.append(c)
            return c
        return None

    take("H", False, True)      # cau dai, trung tinh
    take("H", False, False)     # cau ngan, trung tinh
    take("D", False, None)      # tham tu
    take("C", False, None)      # chuyen gia
    take("N2", True, None)      # cau co the emotion (kiem §5)
    take("H", False, None)      # them 1 cau trung tinh
    return out


pilot_sent = pick_pilot_sentences()
print("cau pilot dung chung:", len(pilot_sent))
for c in pilot_sent:
    print("   %-8s %-3s %s" % (c["id"], c["role"], c["text"][:88]))

pilot_items = []
for role, ref, why in PILOT_CELLS:
    for j, s in enumerate(pilot_sent):
        pid = "P6_%s__%s__%d" % (role, ref.replace(".wav", ""), j)
        pilot_items.append({
            "id": pid,
            "role": role,
            "ref_wav": ref,
            "ref_txt": ref.replace(".wav", ".txt"),
            "text_plain": s["text_plain"],
            "text": s["text"],
            "emotion": s["emotion"],
            "emotion_tag": s.get("emotion_tag", ""),
            "src_id": s["id"],
            "why": why,
        })

pilot_spec = {
    "episode": "02",
    "mode": "pilot_v6",
    "purpose": "Do F0 CLONE thuc + CER cho 4 clip moi + bien the hao cao do (G9)",
    "gen_params": GEN_PARAMS,
    "variants": [0, 1],
    "items": [it["id"] for it in pilot_items],
}
pilot_payload = {
    "episode": "02",
    "model": "bosonai/higgs-tts-3-4b",
    "role_ref": {r: {"wav": w, "txt": w.replace(".wav", ".txt")}
                 for r, w in ROLE_MAP.items()},
    "items": pilot_items,
}

(DS / "pilot_spec_v6.json").write_text(
    json.dumps(pilot_spec, ensure_ascii=False, indent=1), encoding="utf-8")
(DS / "pilot_payload_v6.json").write_text(
    json.dumps(pilot_payload, ensure_ascii=False, indent=1), encoding="utf-8")
print("\npilot: %d item x %d ban = %d file" % (
    len(pilot_items), len(pilot_spec["variants"]),
    len(pilot_items) * len(pilot_spec["variants"])))
print("  theo clip:", dict(Counter(it["ref_wav"] for it in pilot_items)))

# ================================================================== PILOT v7 (kit nghe mu H3)
# V7 (QUY_TAC_GIONG_MAU_VOXCPM2.md): 4 cap phai nghe mu — H<->D, H<->W4, D<->W4, W2<->C.
# Can BAN CLONE cua clip W4 (nam 50) va W2 (nu 50) de so voi giong H/D moi.
V7_CELLS = [
    ("XW4", "W4.wav", "W4 — nam 50, giong gan vung cua H/D (doi thu nghiem kho tach)"),
    ("XW2", "W2.wav", "W2 — nu 50, doi thu voi vai C (nu)"),
]
v7_items = []
for role, ref, why in V7_CELLS:
    for j, s in enumerate(pilot_sent):
        v7_items.append({
            "id": "P7_%s__%d" % (role, j),
            "role": role, "ref_wav": ref, "ref_txt": ref.replace(".wav", ".txt"),
            "text_plain": s["text_plain"], "text": s["text"],
            "emotion": s["emotion"], "emotion_tag": s.get("emotion_tag", ""),
            "src_id": s["id"], "why": why,
        })
v7_spec = {
    "episode": "02", "mode": "pilot_v7",
    "purpose": "Ban clone cua W4/W2 de lam kit nghe mu H3 (V7) + kiem G8",
    "gen_params": GEN_PARAMS, "variants": [0, 1],
    "items": [it["id"] for it in v7_items],
}
v7_payload = {
    "episode": "02", "model": "bosonai/higgs-tts-3-4b",
    "role_ref": {r: {"wav": w, "txt": w.replace(".wav", ".txt")}
                 for r, w in ROLE_MAP.items()},
    "items": v7_items,
}
(DS / "pilot_spec_v7.json").write_text(
    json.dumps(v7_spec, ensure_ascii=False, indent=1), encoding="utf-8")
(DS / "pilot_payload_v7.json").write_text(
    json.dumps(v7_payload, ensure_ascii=False, indent=1), encoding="utf-8")
print("\npilot v7 (kit nghe mu): %d item x %d ban = %d file" % (
    len(v7_items), len(v7_spec["variants"]),
    len(v7_items) * len(v7_spec["variants"])))

# ================================================================== PILOT v8
# Bien the TD-PSOLA (giai thuoc so + resample FFT) thay cho phase vocoder.
# Pilot v6 cho thay bien the S25-S40 co CER 9,5-12,5% khi CLONE, trong khi
# CLIP GOC chinh ra ASR 0,00% => phase vocoder lam nhieu, KHONG phai noi dung.
v8_cells = [
    ("N1", "W6_LOW_PS20.wav", "N1 <- W6_LOW TD-PSOLA -2.0 nua cung"),
    ("N1", "W6_LOW_PS25.wav", "N1 <- W6_LOW TD-PSOLA -2.5 nua cung"),
    ("N1", "W6_LOW_PS30.wav", "N1 <- W6_LOW TD-PSOLA -3.0 nua cung"),
]
v8_items = []
for role, ref, why in v8_cells:
    for j, s in enumerate(pilot_sent):
        v8_items.append({
            "id": "P8_%s__%s__%d" % (role, ref.replace(".wav", ""), j),
            "role": role, "ref_wav": ref, "ref_txt": ref.replace(".wav", ".txt"),
            "text_plain": s["text_plain"], "text": s["text"],
            "emotion": s["emotion"], "emotion_tag": s.get("emotion_tag", ""),
            "src_id": s["id"], "why": why,
        })
v8_spec = {
    "episode": "02", "mode": "pilot_v8",
    "purpose": "Kiem tra bien the TD-PSOLA co giu duoc do phat am khi Higgs clone hay khong",
    "gen_params": GEN_PARAMS, "variants": [0, 1],
    "items": [it["id"] for it in v8_items],
}
v8_payload = {
    "episode": "02", "model": "bosonai/higgs-tts-3-4b",
    "role_ref": {r: {"wav": w, "txt": w.replace(".wav", ".txt")}
                 for r, w in ROLE_MAP.items()},
    "items": v8_items,
}
(DS / "pilot_spec_v8.json").write_text(
    json.dumps(v8_spec, ensure_ascii=False, indent=1), encoding="utf-8")
(DS / "pilot_payload_v8.json").write_text(
    json.dumps(v8_payload, ensure_ascii=False, indent=1), encoding="utf-8")
print("\npilot v8 (TD-PSOLA): %d item x %d ban = %d file" % (
    len(v8_items), len(v8_spec["variants"]),
    len(v8_items) * len(v8_spec["variants"])))

# ================================================================== SAN XUAT
# §7: moi cau 2 ban; cau TRICH (co dau trich dan) sinh 3 ban.
# Danh sach "cau he lo" phai do nguoi dung bo sung — xay dung o file rieng.
EXTRA_P = HERE / "higgs_extra_variants.json"
extra = {}
if EXTRA_P.exists():
    extra = json.loads(EXTRA_P.read_text(encoding="utf-8-sig"))
extra = {k: v for k, v in extra.items() if not k.startswith("_")}


def find_quoted():
    """Cau co dau trich dan trong script_tap02.json -> can 3 ban theo §7."""
    sp = HERE / "script_tap02.json"
    if not sp.exists():
        return []
    sc = json.loads(sp.read_text(encoding="utf-8-sig"))
    out = []
    for e in sc:
        if e.get("kind") != "LOI":
            continue
        for s in e["sentences"]:
            if any(c in s["text"] for c in ["\u201c", "\u201d", '"']):
                out.append(s["id"])
    return out


quoted = find_quoted()
variants_by_item = {sid: [0, 1, 2] for sid in quoted}
variants_by_item.update(extra)
print("cau trich (3 ban):", len(quoted))
print("cau them do nguoi dung chi dinh:", len(extra), extra)

prod_items = []
for it in ITEMS_SRC:
    role = it["role"]
    if role not in ROLE_MAP:
        raise SystemExit("role chua co clip trong g9_role_map.json: %s" % role)
    ref = ROLE_MAP[role]
    p = dict(it)
    p["ref_wav"] = ref
    p["ref_txt"] = ref.replace(".wav", ".txt")
    prod_items.append(p)

n_files = sum(len(variants_by_item.get(it["id"], [0, 1])) for it in prod_items)

prod_spec = {
    "episode": "02",
    "mode": "prod",
    "gen_params": GEN_PARAMS,
    "variants": [0, 1],
    "variants_by_item": variants_by_item,
    "items": [it["id"] for it in prod_items],
}
prod_payload = {
    "episode": payload_src.get("episode", "02"),
    "lang": payload_src.get("lang", "vi"),
    "model": payload_src.get("model", "bosonai/higgs-tts-3-4b"),
    "ref_dir": payload_src.get("ref_dir", "/kaggle/input/amber-eyes-voice-ref-voxcpm2"),
    "role_ref": {r: {"wav": w, "txt": w.replace(".wav", ".txt")}
                 for r, w in ROLE_MAP.items()},
    "items": prod_items,
}

(DS / "prod_spec.json").write_text(
    json.dumps(prod_spec, ensure_ascii=False, indent=1), encoding="utf-8")
(DS / "higgs_payload_t02.json").write_text(
    json.dumps(prod_payload, ensure_ascii=False, indent=1), encoding="utf-8")

print("\nsan xuat: %d cau | %d file (2 ban/cau; cau trich 3 ban)" % (
    len(prod_items), n_files))
print("  theo vai:", dict(Counter(it["role"] for it in prod_items)))
print("  theo clip:", dict(Counter(it["ref_wav"] for it in prod_items)))
print("  co the emotion:", sum(1 for it in prod_items if it.get("emotion_tag")))

# ------------------------------------------------------------------ kiem tra clip ton tai
missing = []
for w in set(list(ROLE_MAP.values()) + [c[1] for c in PILOT_CELLS]):
    if not (DS / w).exists():
        missing.append(w)
    if not (DS / w.replace(".wav", ".txt")).exists():
        missing.append(w.replace(".wav", ".txt"))
if missing:
    print("\n!! THIEU file trong dataset:", sorted(set(missing)))
else:
    print("\nOK: moi clip + file .txt deu co trong dataset")

print("\n-> ", DS)
