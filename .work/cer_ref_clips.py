"""Do chat luong cac CLIP THAM CHIEU bang ASR (khong can GPU).

Moi clip co .txt kem theo = loi doc mau da biet. ASR chep lai, tinh CER
(chuan hoa 2 ve bang vi_cer). Muc dich: tach 2 loai loi:
  - loi ASR tren danh tu rieng (bo danh tu rieng -> cer_pair_prop)
  - loi thiet ke cua clip (phase vocoder lam tho) -> ca 2 vong ASR deu sai giong nhau

Ket qua quyet dinh clip nao dung duoc lam ref cho Higgs.
"""
import json
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import vi_cer  # noqa: E402

CACHE = HERE / "kaggle_higgs" / "_asr_cache_refclip"
CACHE.mkdir(parents=True, exist_ok=True)

G9 = HERE.parent / "assets" / "voice_ref_voxcpm2_g9"
BASE = HERE.parent / "assets" / "voice_ref_voxcpm2"

CLIPS = ([("W6_LOW", G9), ("W6_LOW_S20", G9), ("W6_LOW_S25", G9),
          ("W6_LOW_S30", G9), ("W6_LOW_S35", G9), ("W6_LOW_S40", G9),
          ("W6_LOW_TRIM", G9),
          ("W6_LOW_PS15", G9), ("W6_LOW_PS20", G9), ("W6_LOW_PS25", G9),
          ("W6_LOW_PS30", G9),
          ("W5_HIGH", G9), ("M_LOW", G9), ("M_HIGH", G9),
          ("C", BASE), ("W1", BASE), ("W2", BASE), ("W3", BASE), ("W4", BASE)])


def mcode(args, timeout=600):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "")[:400])
    return json.loads(r.stdout)


def asr(path, rnd):
    cf = CACHE / f"{path.stem}__r{rnd}.json"
    if cf.exists():
        try:
            return json.loads(cf.read_text(encoding="utf-8"))
        except Exception:
            pass
    up = mcode(["upload-temp-url", str(path), "--mime-type", "audio/wav"])
    url = up.get("temp_url")
    if not url:
        return {"transcription": "", "code": -1}
    af = CACHE / f"{path.stem}__r{rnd}.args.json"
    af.write_text(json.dumps(
        {"audio_info": {"url": url, "mime_type": "audio/wav",
                        "prompt": "Chép lại nguyên văn bằng tiếng Việt, không thêm bớt."}},
        ensure_ascii=False), encoding="utf-8")
    res = mcode(["connector", "call", "connector__matrix__listen_audio",
                 "--args-file", str(af)])
    res["_round"] = rnd
    cf.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    return res


def hyp_of(res):
    h = res.get("transcription") or res.get("text") or ""
    if "blocked" in h.lower() or "safety" in h.lower():
        return ""
    return h


rows = []
for name, folder in CLIPS:
    wav = folder / (name + ".wav")
    txt_p = folder / (name + ".txt")
    if not wav.exists() or not txt_p.exists():
        print("thieu file:", name)
        continue
    ref = txt_p.read_text(encoding="utf-8-sig").strip()
    hyps = []
    for rnd in (1, 2):
        try:
            hyps.append(hyp_of(asr(wav, rnd)))
        except Exception as e:
            print("  !! loi ASR", name, e)
            hyps.append("")
    c = max([vi_cer.cer_pair(ref, h) for h in hyps if h], default=None)
    cp = max([vi_cer.cer_pair_prop(ref, h) for h in hyps if h], default=None)
    same = len(set(h for h in hyps if h)) <= 1
    rows.append({"clip": name, "cer": c, "cer_prop": cp, "same": same,
                 "hyps": hyps, "ref": ref})
    print("%-14s CER %6s | CER bo danh tu rieng %6s | 2 vong giong nhau: %s"
          % (name,
             ("%.2f%%" % (100 * c)) if c is not None else "n/a",
             ("%.2f%%" % (100 * cp)) if cp is not None else "n/a",
             "YES" if same else "no"))

print()
print("=== CHI TIET ===")
for r in rows:
    print("-" * 100)
    print("%s  CER=%.2f%%  prop=%.2f%%" % (r["clip"], 100 * (r["cer"] or 0), 100 * (r["cer_prop"] or 0)))
    print("  REF: %s" % r["ref"][:300])
    for i, h in enumerate(r["hyps"], 1):
        if h:
            print("  HYP%d: %s" % (i, h[:300]))

(HERE / "cer_ref_clips.json").write_text(
    json.dumps([{k: v for k, v in r.items()} for r in rows], ensure_ascii=False, indent=1),
    encoding="utf-8")
print()
print("-> .work/cer_ref_clips.json")
