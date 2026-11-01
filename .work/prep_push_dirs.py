"""Tao thu muc push cho Kaggle kernel (notebook + kernel-metadata.json).

Moi kernel dung slug rieng de khong de len nhau:
  pilot v6 -> chiduong2026/amber-eyes-higgs-v6-pilot-kaggle-gpu
  san xuat  -> chiduong2026/amber-eyes-higgs-prod-t02-kaggle-gpu

LUU Y: `id` trong kernel-metadata.json PHAI khop slug that, neu khong
`kaggle kernels push` tra 409 Conflict.
"""
import json
import os
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
KG = HERE / "kaggle_higgs"

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import higgs_paths as P  # noqa: E402  (AE_LANG=en -> dataset ...-voxcpm2-en, §4.4)
DATASET = P.DATASET

KERNELS = {
    "pilot_v6": {
        # KHONG sua title sau khi push: Kaggle tu tao slug tu title. Neu doi
        # title => doi slug => tao kernel moi. `id` phai khop slug that.
        "slug": "chiduong2026/amber-eyes-higgs-v6-pilot-g9-f0-cer",
        "title": "Amber Eyes Higgs v6 pilot (G9 F0 + CER)",
        "nb": "higgs_pilot_v6_kaggle.ipynb",
        "dir": "_push_v6",
    },
    "smoke": {
        # Kaggle slug hoa "2 GPU" -> "2-gpu". Slug that da ton tai tren Kaggle
        # la amber-eyes-higgs-smoke-2-gpu-kaggle-gpu (KHONG phai "2gpu").
        "slug": "chiduong2026/amber-eyes-higgs-smoke-2-gpu-kaggle-gpu",
        "title": "Amber Eyes Higgs smoke 2 GPU Kaggle GPU",
        "nb": "higgs_smoke_kaggle.ipynb",
        "dir": "_push_smoke",
    },
    "v7": {
        "slug": "chiduong2026/amber-eyes-higgs-v7-listen-kit-kaggle-gpu",
        "title": "Amber Eyes Higgs v7 listen kit Kaggle GPU",
        "nb": "higgs_pilot_v7_kaggle.ipynb",
        "dir": "_push_v7",
    },
    "v8": {
        # slug phai khop slug Kaggle TU SINH tu title
        "slug": "chiduong2026/amber-eyes-higgs-v8-td-psola-kaggle-gpu",
        "title": "Amber Eyes Higgs v8 TD-PSOLA Kaggle GPU",
        "nb": "higgs_pilot_v8_kaggle.ipynb",
        "dir": "_push_v8",
    },
    "v9": {
        # slug phai khop slug Kaggle TU SINH tu title
        "slug": "chiduong2026/amber-eyes-higgs-v9-voice-dc-kaggle-gpu",
        "title": "Amber Eyes Higgs v9 voice DC Kaggle GPU",
        "nb": "higgs_pilot_v9_kaggle.ipynb",
        "dir": "_push_v9",
    },
    "v10": {
        "slug": "chiduong2026/amber-eyes-higgs-v10-voice-d3-kaggle-gpu",
        "title": "Amber Eyes Higgs v10 voice D3 Kaggle GPU",
        "nb": "higgs_pilot_v10_kaggle.ipynb",
        "dir": "_push_v10",
    },
    "prod": {
        "slug": "chiduong2026/amber-eyes-higgs-prod-t02-kaggle-gpu",
        "title": "Amber Eyes Higgs prod T02 Kaggle GPU",
        "nb": "higgs_prod_kaggle.ipynb",
        "dir": "_push_prod",
    },
    "r2": {
        "slug": "chiduong2026/amber-eyes-higgs-prod-t02-r2-kaggle-gpu",
        "title": "Amber Eyes Higgs prod T02 r2 Kaggle GPU",
        "nb": "higgs_r2_kaggle.ipynb",
        "dir": "_push_r2",
    },
}

# Tap khac Tap 02 (L8): AE_EP=03 [AE_ACT=3] -> kernel rieng cua tap, khong de len kernel Tap 02.
# Slug Kaggle sinh tu title: "Amber Eyes Higgs prod T03 Kaggle GPU" -> amber-eyes-higgs-prod-t03-kaggle-gpu
_EPN, _ACT = P.EPN, P.ACT
_LT = P.LANG.upper() + " " if P.FOREIGN else ""                   # ban EN: "...prod-en-t02-..."
if P.SFX:
    _sfx = P.SFX
    _tag = "%sT%s%s" % (_LT, _EPN, " A" + _ACT if _ACT else "")
    KERNELS["prod"] = {
        "slug": "chiduong2026/amber-eyes-higgs-prod-%s-kaggle-gpu" % _tag.lower().replace(" ", "-"),
        "title": "Amber Eyes Higgs prod %s Kaggle GPU" % _tag,
        "nb": "higgs_prod%s_kaggle.ipynb" % _sfx,
        "dir": "_push_prod%s" % _sfx,
    }
    if not _ACT:
        KERNELS["r2"] = {
            "slug": "chiduong2026/amber-eyes-higgs-prod-%st%s-r2-kaggle-gpu" % (_LT.lower().replace(" ", "-"), _EPN),
            "title": "Amber Eyes Higgs prod %sT%s r2 Kaggle GPU" % (_LT, _EPN),
            "nb": "higgs_r2%s_kaggle.ipynb" % _sfx,
            "dir": "_push_r2%s" % _sfx,
        }

README = """# Amber Eyes — Higgs Audio v3 (Boson AI) tren Kaggle GPU

Notebook dung chung cho pilot va san xuat. Worker 1 tiep trinh = 1 GPU.
Ket qua khong phu thuoc card nao: seed co dinh theo `(id|role|ref|temp|variant)`.

- Truong so goc: `bosonai/higgs-tts-3-4b` (khong dung GGUF)
- Loader: `multimodalart/higgs-audio-v3-tts-4b-transformers` + `auto_map` tu them
- 24 kHz mono, WAV 16-bit, `max_new_tokens` tu tinh tu frame-rate do that (25,02 Hz)

Bien tap goc: `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` cua du an Amber Eyes.
"""


def build(kind):
    k = KERNELS[kind]
    out = KG / k["dir"]
    out.mkdir(parents=True, exist_ok=True)
    nb_src = HERE / k["nb"]
    if not nb_src.exists():
        raise SystemExit("thieu notebook: %s (chay .work/build_nb.py --mode %s)" % (
            nb_src, kind))
    shutil.copy2(nb_src, out / k["nb"])
    meta = {
        "id": k["slug"],
        "title": k["title"],
        "code_file": k["nb"],
        "language": "python",
        "kernel_type": "notebook",
        "is_private": True,
        "enable_gpu": True,
        "enable_tpu": False,
        "enable_internet": True,
        "keywords": ["tts", "higgs-audio-v3", {"en": "english", "ja": "japanese"}.get(P.LANG, "vietnamese")],
        "dataset_sources": [DATASET],
        "competition_sources": [],
        "model_sources": [],
    }
    (out / "kernel-metadata.json").write_text(
        json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    (out / "README.md").write_text(README, encoding="utf-8")
    print("%-10s -> %s" % (kind, out))
    print("   slug :", k["slug"])
    print("   nb   :", (out / k["nb"]).name, (out / k["nb"]).stat().st_size, "bytes")
    assert meta["id"] == k["slug"], "id phai khop slug"


if __name__ == "__main__":
    for kind in sys.argv[1:] or list(KERNELS):
        build(kind)
