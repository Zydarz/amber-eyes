"""Tao thu muc push cho Kaggle kernel (notebook + kernel-metadata.json).

Moi kernel dung slug rieng de khong de len nhau:
  pilot v6 -> chiduong2026/amber-eyes-higgs-v6-pilot-kaggle-gpu
  san xuat  -> chiduong2026/amber-eyes-higgs-prod-t02-kaggle-gpu

LUU Y: `id` trong kernel-metadata.json PHAI khop slug that, neu khong
`kaggle kernels push` tra 409 Conflict.
"""
import json
import pathlib
import shutil
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
KG = HERE / "kaggle_higgs"

DATASET = "chiduong2026/amber-eyes-voice-ref-voxcpm2"

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
        "slug": "chiduong2026/amber-eyes-higgs-smoke-2gpu-kaggle-gpu",
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
    "prod": {
        "slug": "chiduong2026/amber-eyes-higgs-prod-t02-kaggle-gpu",
        "title": "Amber Eyes Higgs prod T02 Kaggle GPU",
        "nb": "higgs_prod_kaggle.ipynb",
        "dir": "_push_prod",
    },
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
        "keywords": ["tts", "higgs-audio-v3", "vietnamese"],
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
