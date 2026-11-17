#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh clip H3 (MiniMax) cho trailer Concept A — lớp nâng cấp động.

Dùng: py -3 .work/make_trailer_h3.py [--model MiniMax-H3] [--only tên1,tên2]

Output: .work/trailer_a/h3/<tên>.mp4        (bản gốc của H3)
        .work/trailer_a/h3_norm/<tên>.mp4   (đã chuẩn hoá 1920x1080@30 cho pipeline Pillow)

⚠ CHI PHÍ: H3 ăn hạn mức tuần của M Plan, hết thì trừ credit tài khoản.
   Luật L4: phải có người dùng duyệt trước khi chạy.
⚠ Luật chữ (bẫy A11 #87 + bài học Tập 10): TUYỆT ĐỐI không nhắc chữ trong prompt —
   mọi bề mặt giấy/tường mô tả là trống, không ký tự.
⚠ Luật K4/V9: không mô tả bạo lực, thương tích, thi thể; người thật chỉ hiện dạng bóng.
"""
import argparse
import json
import subprocess
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work" / "trailer_a"
RAW = WORK / "h3"
NORM = WORK / "h3_norm"
PROV = ROOT / "provenance.json"
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

STYLE = ("Cinematic 16:9, dark graphic novel noir illustration, bold black ink linework, "
         "deep chiaroscuro lighting, subtle mist and film grain, desaturated muted palette, "
         "ominous quiet tension, highly detailed. ")
NO_TEXT = ("Every surface is completely blank and unmarked, with no writing, no lettering, "
           "no symbols, no signs and no logos of any kind. ")
NO_AUDIO = ("Ambient room tone only, recorded realistically with a film-quality microphone. "
            "Absolutely no music, no score, no speech, no voices, no narration.")

JOBS = [
    ("tr_hook", 8,
     "A taut red evidence thread draws itself slowly across a pitch-black void, stretched "
     "between two invisible pins; drifting dust and cold fog move through the frame; at the "
     "far end of the thread two amber-gold eyes slowly open in the darkness and glow faintly, "
     "their light catching the dust. Slow cinematic push-in. "
     + STYLE + NO_TEXT + NO_AUDIO),

    ("tr_board", 8,
     "A dark cork evidence board covered with blank sheets of paper pinned by taut red threads, "
     "the threads swaying gently; a few loose sheets flutter in a cold draught; a single bare "
     "metal desk lamp throws a hard pool of light and a hard shadow of the threads onto the "
     "board. No people, only a moving shadow. Slow cinematic push-in. "
     + STYLE + NO_TEXT + NO_AUDIO),

    ("tr_interrogation", 6,
     "An empty interrogation room at night seen from a corner: one steel table, two chairs, a "
     "single overhead lamp throwing a cone of light through the dust, faint haze in the beam, "
     "a closed door at the back. No people. Slow cinematic push-in. "
     + STYLE + NO_TEXT + NO_AUDIO),

    ("tr_corridor", 6,
     "A long empty institutional corridor at night, worn wooden doors along both walls, one "
     "ceiling light flickering far at the end, deep shadows pooling on the floor, low fog "
     "creeping along the ground. No people. Slow forward dolly. "
     + STYLE + NO_TEXT + NO_AUDIO),
]


def mcode(args, timeout=900):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "")[:500])
    return json.loads(r.stdout)


def call(tool, args, name):
    af = RAW / f"{name}_{tool.split('__')[-1]}.json"
    af.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    return mcode(["connector", "call", f"connector__matrix__{tool}", "--args-file", str(af)])


def find(d, keys):
    if isinstance(d, dict):
        for k, v in d.items():
            if k in keys and isinstance(v, str) and v:
                return v
            got = find(v, keys)
            if got:
                return got
    if isinstance(d, list):
        for v in d:
            got = find(v, keys)
            if got:
                return got
    return None


def normalise(src, dst):
    """Chuẩn hoá clip: scale+crop 16:9, 1920x1080, 30 fps, có grain + vignette như trailer."""
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(src),
                    "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
                           "fps=30,noise=alls=3:allf=t+u,vignette=PI/5,format=yuv420p",
                    "-c:v", "libopenh264", "-b:v", "8M", "-maxrate", "12M", "-bufsize", "16M",
                    "-an", str(dst)], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="MiniMax-H3", choices=["MiniMax-H3", "MiniMax-H3-Max"])
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    NORM.mkdir(parents=True, exist_ok=True)

    res = 768 if a.model == "MiniMax-H3" else 480
    jobs = [j for j in JOBS if not a.only or j[0] in set(a.only.split(","))]
    tasks = {}
    for name, dur, prompt in jobs:
        state = RAW / f"{name}.task.json"
        if state.exists():
            tasks[name] = json.loads(state.read_text(encoding="utf-8"))
            print(f"  có sẵn {name}", flush=True)
            continue
        r = call("submit_video_generation",
                 {"model": a.model, "prompt": prompt, "duration": max(5, dur),
                  "ratio": "16:9", "resolution": f"{res}P"}, name)
        tid = find(r, {"task_id"})
        if not tid:
            print(f"!! {name}: không nhận được task_id: {json.dumps(r, ensure_ascii=False)[:300]}")
            continue
        tasks[name] = {"task_id": tid, "model": a.model, "prompt": prompt, "duration": dur}
        state.write_text(json.dumps(tasks[name], ensure_ascii=False), encoding="utf-8")
        print(f"  gửi {name}: {tid}", flush=True)

    pending = dict(tasks)
    t0 = time.time()
    while pending and time.time() - t0 < 3600:
        for name in list(pending):
            tk = pending[name]
            r = call("query_video_generation", {"task_id": tk["task_id"], "model": tk["model"]}, name)
            st = (find(r, {"status"}) or "").lower()
            if st in ("failed", "cancelled", "canceled"):
                print(f"!! {name}: {st} {json.dumps(r, ensure_ascii=False)[:250]}")
                pending.pop(name)
                continue
            if st not in ("succeeded", "success", "finished"):
                continue
            url = find(r, {"download_url", "video_url", "url"})
            node = find(r, {"node_id"})
            if not url and node:
                url = mcode(["get_asset_url", node], 120)["download_url"]
            if not url:
                print(f"!! {name}: xong nhưng không thấy link tải")
                pending.pop(name)
                continue
            mp4 = RAW / f"{name}.mp4"
            urllib.request.urlretrieve(url, mp4)
            normalise(mp4, NORM / f"{name}.mp4")
            print(f"  xong {name} -> {NORM / (name + '.mp4')}", flush=True)
            pending.pop(name)
        if pending:
            time.sleep(15)

    if PROV.exists():
        prov = json.loads(PROV.read_text(encoding="utf-8"))
        for name, dur, prompt in JOBS:
            if not (RAW / f"{name}.mp4").exists():
                continue
            f = f".work/trailer_a/h3/{name}.mp4"
            prov = [p for p in prov if p.get("file") != f] + [{
                "file": f, "loai": "clip video AI (b-roll trailer)",
                "cong_cu": f"MiniMax {a.model} qua mcode-tools",
                "ngay": str(date.today()), "prompt": prompt, "seed": None,
                "mo_ta": name,
                "dieu_khoan": "Tạo bằng MiniMax — phải kiểm tra điều khoản thương mại trước khi bật kiếm tiền",
                "kiem_tra_thuong_mai": "chưa"}]
        PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
        print("provenance đã cập nhật")

    if pending:
        print("!! còn chờ (chạy lại lệnh để tiếp tục, không gửi lại):", list(pending))
        sys.exit(2)


if __name__ == "__main__":
    main()
