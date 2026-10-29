#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Demo: the Act 1 opening (Host lines) read with acting_EN.json, one file per candidate host voice.
Output: 02_SAN_XUAT/Tap01_EN/thu_giong/host_moi/demo_<voice>.mp3
"""
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402
import tts_sentences as TS  # noqa: E402
from voice_audition import FF  # noqa: E402

OUT = ED.EP_DIR / "thu_giong" / "host_moi"
VOICES = ["English_CaptivatingStoryteller", "English_magnetic_voiced_man", "English_expressive_narrator"]
IDS = ["1.03#1", "1.03#2", "1.03#3", "1.05#1", "1.08#1", "1.08#2", "1.08#3", "1.08#4", "1.08#5"]


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    plan = {it["id"]: it for it in TS.plan_items()}
    reqs = []
    for v in VOICES:
        for k, sid in enumerate(IDS):
            it = plan[sid]
            reqs.append({"text": it["text"], "voice_id": v, "emotion": it["emotion"], "speed": it["speed"],
                         "pitch": it.get("pitch", 0), "volume": 1.0, "output_file": f"d_{v}_{k:02d}"})
    got = {}
    for b in range(0, len(reqs), 10):
        af = OUT / f"demo_args_{b // 10}.json"
        af.write_text(json.dumps({"requests": reqs[b:b + 10]}, ensure_ascii=False), encoding="utf-8")
        res = TS.mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)])
        for f in res.get("failed_items", []):
            print("!! failed", reqs[b + f["index"]]["output_file"], f.get("error_msg"))
        for it in res.get("success_items", []):
            stem = it["file_name"].rsplit(".", 1)[0]
            url = TS.mcode(["get_asset_url", it["node_id"]], 120)["download_url"]
            urllib.request.urlretrieve(url, OUT / (stem + ".mp3"))
            got[stem] = OUT / (stem + ".mp3")
    for v in VOICES:
        parts = [got[f"d_{v}_{k:02d}"] for k in range(len(IDS)) if f"d_{v}_{k:02d}" in got]
        lst = OUT / f"demo_{v}.txt"
        lst.write_text("".join(f"file '{p.as_posix()}'\n" for p in parts), encoding="utf-8")
        # 0.4 s between sentences, like the episode
        subprocess.run([str(FF), "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-af", "apad=pad_dur=0.4", "-c:a", "libmp3lame", "-b:a", "160k",
                        str(OUT / f"demo_{v}.mp3")], check=True)
        print("demo ->", OUT / f"demo_{v}.mp3")


if __name__ == "__main__":
    main()
