# -*- coding: utf-8 -*-
"""Cập nhật bg_jobs_tap20.json với 124 ảnh nền chuẩn H25."""
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK / "kaggle_flux"))
from t20_jobs_124_data import JOBS_124

old_file = WORK / "bg_jobs_tap20.json"
backup_dir = WORK / "_cu"
backup_dir.mkdir(parents=True, exist_ok=True)
shutil.copy2(old_file, backup_dir / "bg_jobs_tap20_old63.json")
print(f"Backed up old bg_jobs to {backup_dir / 'bg_jobs_tap20_old63.json'}")

STYLE_PREFIX = (
    "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, "
    "bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
)
MOOD_ATMOSPHERE = (
    "gloomy overcast suffocating atmosphere, cold mist floating over the ground, unsettling silence, "
    "creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, "
    "decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
)
NEGATIVE_SUFFIX = (
    "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, "
    "no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, "
    "no signs, no labels, no logos, no watermark, full-bleed 16:9."
)

new_jobs = []
for i, j in enumerate(JOBS_124, 1):
    sids_str = "–".join(j["sids"]) if len(j["sids"]) > 1 else j["sids"][0]
    full_p = f"{STYLE_PREFIX}{j['prompt']}, {MOOD_ATMOSPHERE}{NEGATIVE_SUFFIX}"
    new_jobs.append({
        "name": j["name"],
        "act": j["act"],
        "sentences": sids_str,
        "desc": j["desc"],
        "seed": 30000 + i,
        "prompt": full_p
    })

old_file.write_text(json.dumps(new_jobs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Wrote {len(new_jobs)} jobs to {old_file}")
