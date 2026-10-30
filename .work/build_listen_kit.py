"""Dung KIT NGHE MU cho H3 (V7 + G8).

V7 (00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md): 4 cap phai nghe mu —
   H<->D · H<->W4 · D<->W4 · W2<->C
G8: cung mot vai, 2 cau khac nhau, nguoi nghe phai nhan ra cung mot nguoi.

Cach dung:
  1. Mo file `01_THEO_THU_TU_THANH_AM.wav` (12 file) va `02_G8.wav` (10 file) — nghe thu tu.
  2. Tra loi bang cach viet vao file `03_BANG_TR_LOI.md`.
  3. SAU DO moi mo `DAP_AN_KHOA.txt` de cham.

Output: .work/listen_kit_v6/
"""
import argparse
import json
import pathlib
import random
import shutil
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/

ap = argparse.ArgumentParser()
ap.add_argument("--v6", default=str(HERE / "kaggle_higgs" / "out_higgs_v6" / "out_higgs_v6"))
ap.add_argument("--v7", default=str(HERE / "kaggle_higgs" / "out_higgs_v7" / "out_higgs_v7"))
ap.add_argument("--map", default=str(HERE / "g9_role_map.json"))
ap.add_argument("--out", default=str(HERE / "listen_kit_v6"))
ap.add_argument("--n-sent", type=int, default=4, help="so cau lay moi giong")
ap.add_argument("--seed", type=int, default=20261030)
a = ap.parse_args()

V6 = pathlib.Path(a.v6)
V7 = pathlib.Path(a.v7)
OUT = pathlib.Path(a.out)
OUT.mkdir(parents=True, exist_ok=True)

ROLE_MAP = {k: v for k, v in json.loads(pathlib.Path(a.map).read_text(encoding="utf-8-sig")).items()
            if not k.startswith("_") and isinstance(v, str) and v.endswith(".wav")}
print("phan gan vai:", ROLE_MAP)


def load_manifest(d):
    p = d / "higgs_manifest.json"
    if not p.exists():
        cands = sorted(d.rglob("higgs_manifest.json"))
        if not cands:
            return []
        p = cands[0]
    return [r for r in json.loads(p.read_text(encoding="utf-8-sig")) if r.get("ok")]


man6, man7 = load_manifest(V6), load_manifest(V7)
if not man6:
    raise SystemExit("khong co manifest pilot v6 (%s)" % V6)
print("pilot v6:", len(man6), "| pilot v7:", len(man7))

# gom theo (role, ref)
pool = defaultdict(list)
for r in man6 + man7:
    pool[(r["role"], r["ref_wav"])].append(r)

# ---- lay mau: moi (vai, clip) lay n_sent cau KHAC NHAU -------------------
def pick(role, ref):
    v = pool.get((role, ref)) or []
    by_src = defaultdict(list)
    for r in v:
        by_src[r.get("id")].append(r)
    out = []
    for src in sorted(by_src):
        # uu tien variant 0
        rs = sorted(by_src[src], key=lambda r: r.get("variant", 0))
        out.append(rs[0])
    return out


# Vai trong tap 02 lay tu role map; W4/W2 la clip doi chieu (vai gia lap XW4/XW2)
VOICES = {
    "H": ("H", ROLE_MAP["H"]),
    "D": ("D", ROLE_MAP["D"]),
    "C": ("C", ROLE_MAP["C"]),
    "W4": ("XW4", "W4.wav"),
    "W2": ("XW2", "W2.wav"),
}
for k, (role, ref) in VOICES.items():
    n = len(pick(role, ref))
    print("  %-3s <- %-16s : %d mau" % (k, ref, n))
    if n == 0:
        raise SystemExit("khong co mau cho %s (%s / %s)" % (k, role, ref))

rng = random.Random(a.seed)

# ---- 1) bo 4 cap V7 ------------------------------------------------------
PAIRS = [("H", "D"), ("H", "W4"), ("D", "W4"), ("W2", "C")]
key = {"pairs": {}, "g8": {}}
files = []

for pi, (v1, v2) in enumerate(PAIRS, start=1):
    s1 = pick(*VOICES[v1])[:a.n_sent]
    s2 = pick(*VOICES[v2])[:a.n_sent]
    items = [(v1, r) for r in s1] + [(v2, r) for r in s2]
    rng.shuffle(items)
    entries = []
    for i, (vname, r) in enumerate(items, start=1):
        src = None
        for base in (V6, V7):
            c = base / r["file"]
            if c.exists():
                src = c
                break
            cands = list(base.rglob(r["file"]))
            if cands:
                src = cands[0]
                break
        if src is None:
            raise SystemExit("thieu file %s" % r["file"])
        fn = "01_THEO_THU_TU_THANH_AM_P%d_%02d.wav" % (pi, i)
        shutil.copy2(src, OUT / fn)
        files.append(fn)
        entries.append({"file": fn, "voice": vname, "role": r["role"],
                        "ref_wav": r["ref_wav"], "src_id": r.get("id"),
                        "variant": r.get("variant"), "src_file": r["file"]})
    key["pairs"]["P%d" % pi] = {"pair": [v1, v2], "entries": entries}

# ---- 2) bo G8: cung vai, 2 cau khac nhau --------------------------------
g8_items = []
for vname, (role, ref) in VOICES.items():
    s = pick(role, ref)[:2]
    for r in s:
        g8_items.append((vname, r))
rng.shuffle(g8_items)
entries = []
for i, (vname, r) in enumerate(g8_items, start=1):
    src = None
    for base in (V6, V7):
        c = base / r["file"]
        if c.exists():
            src = c
            break
        cands = list(base.rglob(r["file"]))
        if cands:
            src = cands[0]
            break
    if src is None:
        raise SystemExit("thieu file %s" % r["file"])
    fn = "02_G8_%02d.wav" % i
    shutil.copy2(src, OUT / fn)
    files.append(fn)
    entries.append({"file": fn, "voice": vname, "role": r["role"],
                    "ref_wav": r["ref_wav"], "src_id": r.get("id"),
                    "variant": r.get("variant"), "src_file": r["file"]})
key["g8"] = {"entries": entries}

# ---- 3) ghi bang tra loi + dap an khoa ----------------------------------
q = ["# Bảng trả lời — nghe mù H3", "",
     "Nghe từng file, **không** xem `DAP_AN_KHOA.txt` trước khi trả lời.", "",
     "## Phần 1 — 4 cặp V7 (mỗi cặp 8 file)", "",
     "Với mỗi cặp P1..P4: ghi xuống **cặp nào là giọng nào**.", "",
     "| Cặp | File | Bạn nghe là giọng nào? (H/D/C/W4/W2 hoặc 'vô hình') | Có chắc không? |",
     "|---|---|---|---|"]
for pi in range(1, len(PAIRS) + 1):
    q.append("| P%d | 01_THEO_THU_TU_THANH_AM_P%d_01..08.wav | | |" % (pi, pi))
q += ["", "## Phần 2 — G8 (10 file, `02_G8_*.wav`)", "",
      "Những file nào **cùng một người**? Ghi nhóm (ví dụ `02_G8_03, 02_G8_07`).", "",
      "| File | Cùng người với file nào? |", "|---|---|"]
for i in range(1, len(g8_items) + 1):
    q.append("| 02_G8_%02d.wav | |" % i)
q += ["", "## Tiêu chí đạt (do bạn tự chấm)", "",
      "- **V7**: mỗi cặp phải xác định đúng **2 giọng** khác nhau (không nhập nhằng), "
      "và trong mỗi cặp 2 nhóm phải là 2 giọng **khác nhau**.",
      "- **G8**: trong 10 file, mỗi giọng (5 giọng) phải tìm ra đủ **2 file cùng người**, "
      "tức 5 cặp đúng.",
      "- Nếu trượt: **báo lại tên file + lý do**, không cần sửa lại audio.", ""]
(OUT / "03_BANG_TR_LOI.md").write_text("\n".join(q), encoding="utf-8")

kl = ["# ĐÁP ÁN (KHÓA — mở sau khi đã trả lời)", ""]
for pi, (v1, v2) in enumerate(PAIRS, start=1):
    kl.append("## P%d — cặp %s vs %s" % (pi, v1, v2))
    for e in key["pairs"]["P%d" % pi]["entries"]:
        kl.append("- %s → **%s** (clip %s, câu %s)" % (
            e["file"], e["voice"], e["ref_wav"], e["src_id"]))
    kl.append("")
kl.append("## G8 — 5 nhóm, mỗi nhóm 2 file cùng người")
byv = defaultdict(list)
for e in key["g8"]["entries"]:
    byv[e["voice"]].append(e["file"])
for v in sorted(byv):
    kl.append("- %s: %s" % (v, ", ".join(byv[v])))
kl.append("")
(OUT / "DAP_AN_KHOA.txt").write_text("\n".join(kl), encoding="utf-8")

(OUT / "_blind_key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1),
                                     encoding="utf-8")

readme = """# KIT NGHE MU H3 — Higgs Audio v3, Tập 02

## Cách dùng
1. Nghe `01_THEO_THU_TU_THANH_AM_P*.wav` (12 file, 4 cặp × 3 câu) và `02_G8_*.wav` (10 file).
   **Nghe thuần tai**, không xem đáp án.
2. Điền `03_BANG_TR_LOI.md`.
3. Xong thì mở `DAP_AN_KHOA.txt` để tự chấm.

## Bối cảnh
- Tập 02 có 5 vai: H (nam, dẫn chuyện) · D (nam, thám tử) · C (nữ, chuyên gia tâm lý) ·
  N1 (nữ, người kể 1) · N2 (nữ, người kể 2).
- H và D đã bị trùng cao độ (chỉ cách 1,19 nửa cung) ⇒ đổi clip tham chiếu:
  H dùng clip rất trầm, D dùng clip cao hơn. Bộ kit này kiểm tra **người nghe có
  phân biệt được 2 giọng nam không**, và có tách được khỏi giọng nam trung niên W4 không.
- N2 (clip nữ cao) đối chiếu với W2 (nữ trung niên) và C (nữ chuyên gia).

## Tiêu chí đạt
- V7: mỗi cặp nhận diện đúng 2 giọng khác nhau.
- G8: mỗi giọng tìm đủ 2 file cùng người (5 cặp).
"""
(OUT / "README.md").write_text(readme, encoding="utf-8")

print("\nda dung kit nghe mu -> %s" % OUT)
print("  %d file" % len(files))
print("  4 cap V7 + 10 file G8")
print("  bang tra loi: 03_BANG_TR_LOI.md | dap an: DAP_AN_KHOA.txt")
