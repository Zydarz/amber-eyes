"""Sinh kernel Kaggle KIEM CHAT LUONG audio Higgs: Whisper large-v3 (ban chep) + UTMOS (diem MOS).

Dau vao: output cua kernel Higgs (khai `kernel_sources`, KHONG upload lai wav).
Dau ra : /kaggle/working/qc_<TAG>/qc.json — moi file: ban chep Whisper, UTMOS, do dai.
CER tinh o may bang `qc_whisper_cer.py` (vi_cer, chuan hoa ca hai ve — Q3a) de giu
dung mot bo chuan hoa voi `measure_cer_prod.py`.

  AE_EP=06 py -3 .work/build_qc_nb.py                    -> nguon = kernel prod tap 06
  AE_EP=06 py -3 .work/build_qc_nb.py --round r2         -> nguon = kernel r2 tap 06
  roi: kaggle kernels push -p .work\\kaggle_higgs\\_push_qc_t06[_r2]   (PowerShell, K10)

Luu y:
- Whisper giai ma greedy => tat dinh, 1 luot/file la du (khac listen_audio, Q6).
- UTMOS (utmos22_strong) huan luyen tren tieng Anh: dung SO SANH TUONG DOI giua cac ban /
  cac vai cua cung tap, KHONG dung nguong tuyet doi kieu "MOS < 3 la hong".
"""
import argparse
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import higgs_paths as P  # noqa: E402

ap = argparse.ArgumentParser()
ap.add_argument("--round", default="prod", choices=["prod", "r2"])
a = ap.parse_args()

USER = "chiduong2026"
LANG_W = {"vi": "vietnamese", "en": "english", "ja": "japanese"}[P.LANG]
if a.round == "prod":
    src = "%s/amber-eyes-higgs-prod-%s-kaggle-gpu" % (USER, P.TAG.lower().replace("_", "-"))
    tag = P.TAG
else:
    src = "%s/amber-eyes-higgs-prod-%s-r2-kaggle-gpu" % (USER, P.EP_TAG.lower().replace("_", "-"))
    tag = P.EP_TAG + "_r2"
slug = "amber-eyes-qc-%s-kaggle-gpu" % tag.lower().replace("_", "-")
OUT = P.KH / ("_push_qc_" + tag)

CODE = r'''
import os, json, glob, time, subprocess, sys
TAG = "__TAG__"
LANG = "__LANG__"
OUT = "/kaggle/working/qc_" + TAG
os.makedirs(OUT, exist_ok=True)

wavs = sorted(p for p in glob.glob("/kaggle/input/**/*.wav", recursive=True))
mans = sorted(glob.glob("/kaggle/input/**/higgs_manifest.json", recursive=True))
print("wav:", len(wavs), "| manifest:", mans)
assert wavs, "khong thay wav trong /kaggle/input — kiem kernel_sources"
'''

CODE2 = r'''
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "librosa", "soundfile"], check=True)
import torch, librosa, numpy as np
from transformers import pipeline
dev = "cuda:0" if torch.cuda.is_available() else "cpu"
print("GPU:", torch.cuda.get_device_name(0) if dev != "cpu" else "KHONG CO")
asr = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3",
               torch_dtype=torch.float16 if dev != "cpu" else torch.float32, device=dev)
utmos = torch.hub.load("tarepan/SpeechMOS:v1.2.0", "utmos22_strong", trust_repo=True).to(dev).eval()
'''

CODE3 = r'''
rows, t0 = [], time.time()
B = 8
for i in range(0, len(wavs), B):
    chunk = wavs[i:i + B]
    audios = [librosa.load(p, sr=16000, mono=True)[0] for p in chunk]
    # File > 30 s (vd duoi cam cham tran token) lam vo padding khi chay lo cung file ngan
    # (Tap06 EN/JA 06/11/2026: RuntimeError 3000 vs 4756) -> chay rieng tung file, co timestamps.
    if any(len(x) > 30 * 16000 for x in audios):
        res = [asr({"raw": x, "sampling_rate": 16000},
                   generate_kwargs={"language": LANG, "task": "transcribe"},
                   return_timestamps=len(x) > 30 * 16000) for x in audios]
    else:
        res = asr([{"raw": x, "sampling_rate": 16000} for x in audios], batch_size=B,
                  generate_kwargs={"language": LANG, "task": "transcribe"})
    for p, x, r in zip(chunk, audios, res):
        with torch.no_grad():
            mos = float(utmos(torch.from_numpy(x).unsqueeze(0).to(dev), 16000).item())
        rows.append({"file": os.path.basename(p), "transcription": r["text"].strip(),
                     "utmos": round(mos, 3), "duration_s": round(len(x) / 16000, 2)})
    print("%d/%d  %.0f s" % (len(rows), len(wavs), time.time() - t0), flush=True)
json.dump({"tag": TAG, "asr": "openai/whisper-large-v3 (greedy, language=%s)" % LANG,
           "mos": "tarepan/SpeechMOS v1.2.0 utmos22_strong", "rows": rows},
          open(OUT + "/qc.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("XONG:", len(rows), "file ->", OUT + "/qc.json")
'''


def cell(src):
    return {"cell_type": "code", "metadata": {}, "execution_count": None, "outputs": [],
            "source": src.strip("\n").splitlines(keepends=True)}


nb = {"nbformat": 4, "nbformat_minor": 5,
      "metadata": {"kernelspec": {"name": "python3", "display_name": "Python 3", "language": "python"}},
      "cells": [cell(CODE.replace("__TAG__", tag).replace("__LANG__", LANG_W)), cell(CODE2), cell(CODE3)]}
OUT.mkdir(parents=True, exist_ok=True)
nbname = "qc_%s_kaggle.ipynb" % tag.lower()
(OUT / nbname).write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
meta = {"id": "%s/%s" % (USER, slug), "title": slug.replace("-", " ").title().replace("Qc", "QC"),
        "code_file": nbname, "language": "python", "kernel_type": "notebook", "is_private": True,
        "enable_gpu": True, "enable_tpu": False, "enable_internet": True, "keywords": [],
        "dataset_sources": [], "kernel_sources": [src], "competition_sources": [], "model_sources": []}
# Kaggle sinh slug tu title (README §11) => title phai ra dung slug
assert meta["title"].lower().replace(" ", "-") == slug, (meta["title"], slug)
(OUT / "kernel-metadata.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("nguon :", src)
print("kernel:", meta["id"])
print("->    ", OUT)
