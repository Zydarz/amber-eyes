#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gửi 4 task Hailuo-2.3 (6 s, 1080P, first-frame) để hoạt họng nền có sẵn của kênh.

Model: MiniMax-Hailuo-2.3 (dùng được hạn mức Token Plan; H3 bị chặn 402).
Mode : first-frame (input_image + reference_type=first_frame) — không dùng `ratio`,
        không dùng reference_images/videos/audios (H2.3 không hỗ trợ).
Mode đồng bộ âm thanh: H2.3 **không có tiếng** — trailer dùng VO + nhạc sẵn có.

Dùng: py -3 .work/make_trailer_h23.py
Ghi : .work/trailer_a/h23/tasks.json   (bản ghi provider_task_id → model → output → mốc thời gian)
      videos/<ten>.mp4                (sau khi tải)
"""
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work" / "trailer_a"
H23 = WORK / "h23"
VIDEOS = ROOT / "videos"
MODEL = "MiniMax-Hailuo-2.3"
DURATION = 6
RESOLUTION = "1080P"

# prompt ≤ 3000 ký tự (giới hạn của H2.3). Không nhắc chữ — chỉ mô tả chuyển động.
NO_ADD = ("No new objects appear, no people appear, no writing appears anywhere, no text, no letters, "
          "no numbers, no symbols, no logos, no watermark, no graphics.")

JOBS = [
    dict(key="hook", bg="void", out="videos/soi-chi-do-hook.mp4",
         prompt=("The frame is a dark misty void. Keep the exact composition, darkness and colour of the "
                 "first frame. Only the fog drifts slowly and thickens toward the lower half, faint dust "
                 "motes float through the air, and a very subtle slow camera push-in makes the void feel "
                 "deeper. Lighting stays low and cold with deep black shadows. " + NO_ADD +
                 " Cinematic, ominous, restrained.")),
    dict(key="board", bg="pinboard", out="videos/bang-ho-so-chay.mp4",
         prompt=("The frame is a cork evidence board covered with blank pinned sheets of paper strung by "
                 "red threads, lit by a single desk lamp. Keep the exact composition, the papers, the "
                 "threads and the lighting of the first frame. The red threads sway gently as if in a cold "
                 "draught, one loose sheet lifts and settles back, dust drifts through the lamp beam, and "
                 "the camera pushes in very slowly. " + NO_ADD + " Cinematic, restrained, ominous.")),
    dict(key="interrogation", bg="interrogation", out="videos/phong-tham-van-mo.mp4",
         prompt=("The frame is an empty interrogation room with a steel table, two chairs and a hard cone of "
                 "light from the overhead lamp. Keep the exact composition, the furniture and the lighting "
                 "of the first frame. Only the dust inside the light beam drifts, the haze shifts slightly, "
                 "the lamp flickers once, and the camera pushes in very slowly. " + NO_ADD +
                 " Cinematic, restrained, tense.")),
    dict(key="corridor", bg="corridor", out="videos/hanh-lang-dem.mp4",
         prompt=("The frame is a long empty corridor at night with wooden doors and a single flickering light "
                 "at the far end. Keep the exact composition, the doors, the lighting and the colour of the "
                 "first frame. Only the low fog creeps slowly along the floor, the far light flickers, and "
                 "the camera dollies forward very slowly. " + NO_ADD + " Cinematic, restrained, ominous.")),
]


def mcode(args, timeout=600):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "")[:600])
    return json.loads(r.stdout)


def upload(path):
    r = subprocess.run(["cmd", "/c", "mcode-tools", "upload-temp-url", str(path),
                        "--mime-type", "image/png"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=600)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "")[:600])
    j = json.loads(r.stdout)
    return j["temp_url"]


def main():
    H23.mkdir(parents=True, exist_ok=True)
    VIDEOS.mkdir(parents=True, exist_ok=True)
    rec_path = H23 / "tasks.json"
    rec = json.loads(rec_path.read_text(encoding="utf-8")) if rec_path.exists() else {}

    for job in JOBS:
        key = job["key"]
        if rec.get(key, {}).get("task_id"):
            print(f"  {key}: đã có task_id {rec[key]['task_id']} — không gửi lại")
            continue
        bg = ROOT / "assets" / "bg" / f"{job['bg']}.png"
        print(f"  {key}: upload khung đầu {bg.name}", flush=True)
        url = upload(bg)
        args = {
            "model": MODEL,
            "prompt": job["prompt"],
            "duration": DURATION,
            "resolution": RESOLUTION,
            "reference_type": "first_frame",
            "input_image": {"url": url, "mime_type": "image/png"},
        }
        af = H23 / f"{key}.submit-args.json"
        af.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
        # bản ghi "đã thử gửi" TRƯỚC khi gọi có phí
        rec[key] = {"task_id": None, "model": MODEL, "duration": DURATION, "resolution": RESOLUTION,
                    "output_file": job["out"], "submission_attempted": True,
                    "submitted_at_ms": int(time.time() * 1000), "last_query_at_ms": None,
                    "poller_task_id": None, "terminal_status": None}
        rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")

        out_f = H23 / f"{key}.submit.stdout.txt"
        err_f = H23 / f"{key}.submit.stderr.txt"
        with open(out_f, "w", encoding="utf-8") as fo, open(err_f, "w", encoding="utf-8") as fe:
            r = subprocess.run(["cmd", "/c", "mcode-tools", "connector", "call",
                                "connector__matrix__submit_video_generation",
                                "--args-file", str(af)], stdout=fo, stderr=fe, text=True,
                               encoding="utf-8", errors="replace", timeout=900)
        raw = out_f.read_text(encoding="utf-8")
        if r.returncode != 0:
            msg = (err_f.read_text(encoding="utf-8") or raw)[:300]
            rec[key]["terminal_status"] = "submit_failed"
            rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"!! {key}: gửi lỗi: {msg}", flush=True)
            continue
        try:
            j = json.loads(raw)
        except Exception:
            j = {}
        tid = j.get("task_id") or (j.get("data") or {}).get("task_id")
        if not tid:
            rec[key]["terminal_status"] = "unverified_submission_state"
            rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"!! {key}: không lấy được task_id — KHÔNG gửi lại. raw: {raw[:300]}", flush=True)
            continue
        rec[key]["task_id"] = tid
        rec_path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  {key}: task_id={tid}", flush=True)

    print("\n=== bản ghi ===")
    for k, v in rec.items():
        print(f"  {k:14s} {v.get('task_id')}  {v.get('terminal_status')}")


if __name__ == "__main__":
    main()
