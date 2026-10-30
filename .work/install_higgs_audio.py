"""Cai audio Higgs (buoc chon ban theo CER) vao thu muc RIENG — KHONG de MiniMax.

L5: thu muc `audio_s_t02` (MiniMax, 203 mp3) giu nguyen. Higgs vao
`.work/audio_s_higgs_t02/` (24 kHz WAV).

Chon ban: moi cau nhieu ban (variant 0/1/...) => chon ban CER thap nhat.
Tiep theo: `AE_AUDIO_DIR=audio_s_higgs_t02` khi chay `build_audio3.py`.

Input : .work/kaggle_higgs/out_higgs_prod/out_higgs_prod/  (higgs_manifest.json)
        .work/higgs_cer_rows_t02.json                      (do boi measure_cer_prod.py)
Output: .work/audio_s_higgs_t02/*.wav
        .work/higgs_selection_t02.json
"""
import argparse
import json
import pathlib
import shutil
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent

ap = argparse.ArgumentParser()
ap.add_argument("--dir", default=str(HERE / "kaggle_higgs" / "out_higgs_prod" / "out_higgs_prod"))
ap.add_argument("--cer", default=str(HERE / "higgs_cer_rows_t02.json"))
ap.add_argument("--out", default=str(HERE / "audio_s_higgs_t02"))
ap.add_argument("--max-cer", type=float, default=0.02)
ap.add_argument("--no-copy", action="store_true", help="chi tinh, khong ghi file")
a = ap.parse_args()

WAVDIR = pathlib.Path(a.dir)
OUT = pathlib.Path(a.out)
OUT.mkdir(parents=True, exist_ok=True)

man_p = WAVDIR / "higgs_manifest.json"
if not man_p.exists():
    cands = sorted((HERE / "kaggle_higgs" / "out_higgs_prod").rglob("higgs_manifest.json"))
    if not cands:
        raise SystemExit("khong tim thay manifest san xuat")
    man_p = cands[0]
man = json.loads(man_p.read_text(encoding="utf-8-sig"))
rows = [r for r in man if r.get("ok")]

# ---- ghep CER (theo file wav) -------------------------------------------
cer_by_file = {}
cp = pathlib.Path(a.cer)
if cp.exists():
    crows = json.loads(cp.read_text(encoding="utf-8-sig"))
    for r in crows:
        if r.get("cer_ok"):
            cer_by_file[r["file"]] = r["cer"]
    print("doc CER: %d/%d dong" % (len(cer_by_file), len(crows)))
else:
    print("!! khong co file CER (%s) => se chon theo thu tu variant" % cp)

# ---- nhom theo cau (id) --------------------------------------------------
by_id = defaultdict(list)
for r in rows:
    by_id[r["id"]].append(r)

# ten file cua manifest MiniMax (gia dung ten de build_audio3 tim thay)
tman_p = HERE / "tts_manifest_t02.json"
stem_of = {}
if tman_p.exists():
    for m in json.loads(tman_p.read_text(encoding="utf-8")):
        stem_of[m["id"]] = pathlib.Path(m["file"]).stem
else:
    print("!! khong co tts_manifest_t02.json => dung ten id lam ten file")

sel = {}
bad = []
for sid, v in sorted(by_id.items()):
    def key(r):
        c = cer_by_file.get(r["file"])
        return (c if c is not None else 9.9, r.get("variant", 0))
    v2 = sorted(v, key=key)
    win = v2[0]
    c = cer_by_file.get(win["file"])
    stem = stem_of.get(sid) or sid.replace("#", "_").replace(".", "_")
    sel[sid] = {
        "id": sid, "role": win["role"], "ref_wav": win["ref_wav"],
        "temp": win["temp"], "variant": win.get("variant", 0), "seed": win.get("seed"),
        "cer": c, "cer_all": {r["file"]: cer_by_file.get(r["file"]) for r in v2},
        "duration_s": win.get("duration_s"), "peak_dbfs": win.get("peak_dbfs"),
        "src_file": win["file"], "dst": stem + ".wav",
    }
    if c is None:
        bad.append((sid, "khong co CER"))
    elif c > a.max_cer:
        bad.append((sid, "CER %.1f%%" % (100 * c)))

print()
print("cau: %d | da chon: %d | vuot %.0f%%: %d" % (
    len(by_id), len(sel), 100 * a.max_cer, len(bad)))

if not a.no_copy:
    n = 0
    for sid, s in sel.items():
        src = WAVDIR / s["src_file"]
        if not src.exists():
            cands = list((HERE / "kaggle_higgs" / "out_higgs_prod").rglob(s["src_file"]))
            if not cands:
                print("!! thieu file:", s["src_file"])
                continue
            src = cands[0]
        shutil.copy2(src, OUT / s["dst"])
        n += 1
    print("da cai %d file -> %s" % (n, OUT))

out_p = HERE / "higgs_selection_t02.json"
out_p.write_text(json.dumps({
    "source_manifest": str(man_p),
    "out_dir": str(OUT),
    "n_sentences": len(sel),
    "n_over_max_cer": len(bad),
    "max_cer": a.max_cer,
    "selection": sel,
}, ensure_ascii=False, indent=1), encoding="utf-8")
print("->", out_p)

if bad:
    print()
    print("!! CAN VONG 2 (theo §7) cho %d cau:" % len(bad))
    for sid, why in bad:
        print("   %-10s %s" % (sid, why))
