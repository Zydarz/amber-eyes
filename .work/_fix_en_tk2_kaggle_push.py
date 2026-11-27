#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua EN TK2 TikTok Tap 04: sinh 2 cau bi THIEU bang Higgs Audio v3 tren Kaggle.

EN TK2 master audio (Tap04_EN/TK2_master_audio.mp3) chi co 9/11 cau:
  - loi dung o 56.14s ("...serial killers in history."), roi 14.76s chi co BGM
  - thieu TK2.01#10 (vai C) va TK2.01#11 (CTA vai H)

Fix: sinh 2 cau bang dung giong vai (C_EN.wav / H_EN.wav) tren Kaggle GPU,
sau do splice vao master audio tai dung vi tri (xem _fix_en_tk2_splice.py).

Buoc nay: (1) tao Kaggle dataset chua ref + payload 2 cau
          (2) tao kernel tu notebook EN t03 co san (chi doi dataset/slug)
          (3) push dataset + kernel

Dung: py -3 .work/_fix_en_tk2_kaggle_push.py
"""
import json
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
KH = ROOT / ".work" / "kaggle_higgs"
REFSRC = KH / "dataset_voxcpm2_en"

DS_DIR = KH / "_fix_en_tk02_ds"
KB_DIR = KH / "_push_fix_en_tk02"
DS_ID = "chiduong2026/amber-eyes-higgs-fix-en-tk02-t04"
KB_ID = "chiduong2026/amber-eyes-higgs-fix-en-tk02-t04-kaggle-gpu"

GEN_PARAMS = {
    "temperature": 0.8,
    "temp_by_role": {"H": 0.8, "D": 0.8, "C": 0.8, "N1": 0.8, "N2": 0.8},
    "top_p": 0.95, "top_k": 50, "max_new_tokens": 1196,
    "sample_rate": 24000, "fade_in_ms": 30,
    "seed_scheme": "sha256(id|role|ref|temp|vN) -> int(hex[:8],16)",
}

# id goc cua tap chinh cho cau #10 (2.11#1) -> seed trung voi lan render tap chinh
ITEMS = [
    {
        "id": "2.11#1", "role": "C", "ref_wav": "C_EN.wav", "ref_txt": "C_EN.txt",
        "text_plain": ("Through the lens of criminal psychology, Charles Cullen exhibited "
                       "classic hallmarks of psychological Objectification and severe dehumanization."),
        "text": ("Through the lens of criminal psychology, Charles Cullen exhibited "
                 "classic hallmarks of psychological Objectification and severe dehumanization."),
        "emotion": "neutral", "emotion_tag": "", "speed": 0.94, "speed_base": None,
        "file": "2_11_1.wav",
        "display": ("Through the lens of criminal psychology, Charles Cullen exhibited "
                    "classic hallmarks of psychological \u201cObjectification\u201d and severe dehumanization."),
    },
    {
        "id": "TK2.01#11", "role": "H", "ref_wav": "H_EN.wav", "ref_txt": "H_EN.txt",
        "text_plain": "Episode four of Amber Eyes. Watch the full documentary via the bio link.",
        "text": "Episode four of Amber Eyes. Watch the full documentary via the bio link.",
        "emotion": "neutral", "emotion_tag": "", "speed": 0.94, "speed_base": None,
        "file": "TK2_01_11.wav",
        "display": "Episode four of Amber Eyes. Watch the full documentary via the bio link.",
    },
]


def sh(args, **kw):
    print(">>", " ".join(str(a) for a in args), flush=True)
    return subprocess.run([str(a) for a in args], **kw)


def main():
    # ---------- 1. dataset ----------
    if DS_DIR.exists():
        shutil.rmtree(DS_DIR)
    DS_DIR.mkdir(parents=True)
    for f in ("C_EN.wav", "C_EN.txt", "H_EN.wav", "H_EN.txt"):
        shutil.copy2(REFSRC / f, DS_DIR / f)
    payload = {"episode": "t04_fix_en_tk02", "lang": "en",
               "model": "bosonai/higgs-tts-3-4b", "ref_dir": "",
               "role_ref": {}, "items": ITEMS}
    spec = {"episode": "t04_fix_en_tk02", "mode": "prod",
            "gen_params": GEN_PARAMS, "variants": [0],
            "variants_by_item": {}, "items": [it["id"] for it in ITEMS]}
    (DS_DIR / "higgs_payload_EN_t03.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=1), encoding="utf-8")
    (DS_DIR / "prod_spec_EN_t03.json").write_text(
        json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
    (DS_DIR / "dataset-metadata.json").write_text(json.dumps({
        "title": "Amber Eyes Higgs fix EN TK2 Tap04 (private)",
        "id": DS_ID,
        "subtitle": "2 cau bi thieu trong clip TikTok Tap04 EN TK2",
        "description": ("Bo ref giong EN (H_EN, C_EN) + payload 2 cau cho viec sua "
                        "EN TK2 TikTok Tap 04. Chi dung noi bo."),
        "licenses": [{"name": "other", "other": "Apache-2.0 (VoxCPM2 Voice Design)"}],
        "keywords": ["voice-reference", "english", "tts", "higgs-audio-v3", "fix"],
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    print("dataset dir:", DS_DIR)

    # ---------- 2. kernel ----------
    if KB_DIR.exists():
        shutil.rmtree(KB_DIR)
    KB_DIR.mkdir(parents=True)
    nb_src = KH / "_push_prod_EN_t03" / "higgs_prod_EN_t03_kaggle.ipynb"
    nb = json.loads(nb_src.read_text(encoding="utf-8"))
    nb["cells"][0]["source"] = [
        "# FIX EN TK2 TikTok Tap 04 — Higgs Audio v3\n",
        "\n",
        "Sinh 2 cau bi thieu trong clip TikTok Tap 04 EN TK2 (TK2.01#10 vai C, TK2.01#11 CTA vai H).\n",
        "Cung pipeline Higgs v3 2 GPU cua ban Tap 03 EN.\n",
    ]
    # doi ten thu muc output de khong lam nham voi ban t03
    for c in nb["cells"]:
        s = "".join(c.get("source", []))
        if "out_higgs_prod_EN_t03" in s:
            c["source"] = [x.replace("out_higgs_prod_EN_t03", "out_higgs_fix_en_tk02")
                           for x in c.get("source", [])]
    (KB_DIR / "higgs_fix_en_tk02_kaggle.ipynb").write_text(
        json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
    (KB_DIR / "kernel-metadata.json").write_text(json.dumps({
        "id": KB_ID,
        "title": "Amber Eyes Higgs fix EN TK02 T04 Kaggle GPU",
        "code_file": "higgs_fix_en_tk02_kaggle.ipynb",
        "language": "python", "kernel_type": "notebook",
        "is_private": True, "enable_gpu": True, "enable_tpu": False,
        "enable_internet": True,
        "keywords": ["tts", "higgs-audio-v3", "english", "fix"],
        "dataset_sources": [DS_ID],
        "competition_sources": [], "model_sources": [],
    }, ensure_ascii=False, indent=1), encoding="utf-8")
    (KB_DIR / "README.md").write_text(
        "# Higgs fix EN TK2 Tap 04\n\n2 cau: 2.11#1 (vai C) + TK2.01#11 (CTA vai H).\n",
        encoding="utf-8")
    print("kernel dir:", KB_DIR)

    # ---------- 3. push ----------
    r = sh(["py", "-3", "-m", "kaggle.cli", "datasets", "create", "-p", str(DS_DIR),
            "--dir-mode", "zip"], capture_output=True, text=True, errors="replace")
    print("dataset create rc=", r.returncode)
    print(r.stdout[-1500:]); print(r.stderr[-1500:])
    if r.returncode != 0:
        raise SystemExit("push dataset that bai")

    r = sh(["py", "-3", "-m", "kaggle.cli", "kernels", "push", "-p", str(KB_DIR)],
           capture_output=True, text=True, errors="replace")
    print("kernel push rc=", r.returncode)
    print(r.stdout[-1500:]); print(r.stderr[-1500:])
    if r.returncode != 0:
        raise SystemExit("push kernel that bai")
    print("OK: da push dataset + kernel")


if __name__ == "__main__":
    main()
