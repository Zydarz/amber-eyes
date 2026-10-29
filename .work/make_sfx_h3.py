#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tiếng động "thật" bằng MiniMax-H3 (Tập 02) — người dùng chọn MiniMax thay vì tải tiếng thu sẵn.

MiniMax-H3 / H3-Max sinh video KÈM rãnh âm thanh gốc theo mô tả (không khí, tiếng động).
Script chỉ giữ rãnh âm thanh: video → wav stereo 44,1 kHz, cắt lặng đầu/cuối, chuẩn hoá đỉnh.
Mỗi tiếng ghi vào provenance.json (công cụ, mô hình, prompt, ngày).

⚠ CHI PHÍ: H3 / H3-Max trả bằng hạn mức tuần của M Plan, hết thì trừ credit tài khoản.
   Chỉ chạy khi người dùng đã chọn mô hình:
       py -3 .work/make_sfx_h3.py --model MiniMax-H3-Max            (nhanh, 480P đủ vì chỉ lấy tiếng)
       py -3 .work/make_sfx_h3.py --model MiniMax-H3 --only fx_gavel_triple
Output: assets/sfx/t2/<tên>.wav — GHI ĐÈ bản tự tổng hợp cùng tên (bản cũ chép sang assets/sfx/t2/_code/).
"""
import argparse
import json
import shutil
import subprocess
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
OUT = ROOT / "assets" / "sfx" / "t2"
RAW = WORK / "sfx_h3"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

NO = (" Audio: only natural diegetic sound, recorded realistically with a film-quality microphone."
      " Absolutely no music, no score, no speech, no voices, no singing, no narration.")

# tên file (trùng bộ make_sfx3 để bảng sfx_tap02.json dùng luôn), thời lượng, mô tả hình + tiếng
JOBS = [
    ("fx_tire_snow", 8, "Close low angle at night on a snowy rural road: a dark SUV rolls slowly forward over packed snow and "
     "comes to a stop, its engine idling. Sound: tyres crunching and squeaking on cold packed snow, a low engine idle, light wind."),
    ("fx_window_down", 6, "Night, close-up of the driver's side window of a stopped SUV in light snowfall; the window glass slides "
     "down slowly. Sound: the electric window motor whirring, rubber seal squeak, cold wind rushing in, engine idling."),
    ("fx_police_radio", 6, "Night, close-up of a police radio clipped to an officer's winter jacket at a roadside checkpoint, red "
     "and blue lights reflecting. Sound: radio squelch, a short burst of unintelligible distorted dispatcher chatter, squelch off, wind."),
    ("fx_footsteps_snow", 8, "Night, low shot of heavy winter boots walking slowly through fresh deep snow on a quiet suburban "
     "sidewalk. Sound: crisp crunching footsteps in snow, each step distinct, faint wind, nothing else."),
    ("fx_chair_scrape", 6, "A small bare interrogation room with fluorescent light; a metal chair is pulled back across a tiled "
     "floor and someone sits; a ceramic coffee mug is set down on a wooden table. Sound: metal chair legs scraping on tile, "
     "the chair creaking, the mug landing with a solid knock, fluorescent hum."),
    ("fx_gavel_triple", 6, "An empty wood-panelled courtroom; a wooden judge's gavel strikes its sound block three times, slow and "
     "deliberate. Sound: three sharp wooden knocks with natural courtroom reverb, then silence of a large room."),
    ("fx_fire_whoosh", 8, "Inside a concrete storage room, a folded military jacket on top of a metal drum catches fire and the "
     "flames grow. Sound: ignition whoosh, fabric burning, fire crackling and roaring inside the drum, concrete room echo."),
    ("fx_metal_crush", 8, "At a scrapyard by day in winter, a hydraulic crusher slowly flattens an old SUV. Sound: hydraulic "
     "whine, heavy metal crumpling and groaning, glass cracking, deep creaks and thuds."),
    ("amb_interrogation", 12, "Static shot of an empty small interrogation room: one table, two chairs, a flickering fluorescent "
     "tube. Sound: steady fluorescent light buzz, air vent hum, distant muffled corridor, very quiet room tone."),
    ("amb_road_night", 12, "Static wide shot of a dark snowy rural highway at night with a police checkpoint in the distance, "
     "flashing lights, snow falling. Sound: cold winter wind, a car engine idling nearby, distant car passing on wet snow."),
]


def mcode(args, timeout=900):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[:500] or r.stdout[:500])
    return json.loads(r.stdout)


def call(tool, args, name):
    af = RAW / f"{name}_{tool.split('__')[-1]}.json"
    af.write_text(json.dumps(args, ensure_ascii=False), encoding="utf-8")
    return mcode(["connector", "call", f"connector__matrix__{tool}", "--args-file", str(af)])


def find(d, keys):
    """Tìm giá trị đầu tiên theo tên khoá trong kết quả lồng nhau."""
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


def to_wav(video, wav):
    """Rãnh âm thanh → wav stereo 44,1 kHz, cắt lặng đầu/cuối, đỉnh −1 dBFS."""
    af = ("silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.05,"
          "areverse,silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.3,areverse,"
          "afade=t=in:d=0.02,dynaudnorm=p=0.89:m=1:f=500")
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(video), "-vn", "-af", af,
                    "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", str(wav)], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=["MiniMax-H3", "MiniMax-H3-Max"])
    ap.add_argument("--only", nargs="*")
    a = ap.parse_args()
    RAW.mkdir(parents=True, exist_ok=True)
    (OUT / "_code").mkdir(parents=True, exist_ok=True)
    jobs = [j for j in JOBS if not a.only or j[0] in a.only]
    res = 480 if a.model == "MiniMax-H3-Max" else 768
    tasks = {}
    for name, dur, prompt in jobs:
        state = RAW / f"{name}.task.json"
        if state.exists():
            tasks[name] = json.loads(state.read_text(encoding="utf-8"))
            continue
        r = call("submit_video_generation", {"model": a.model, "prompt": prompt + NO, "duration": max(5, dur),
                                             "ratio": "16:9", "resolution": f"{res}P"}, name)
        tid = find(r, {"task_id"})
        if not tid:
            print(f"!! {name}: không nhận được task_id: {json.dumps(r)[:300]}")
            continue
        tasks[name] = {"task_id": tid, "model": a.model, "prompt": prompt + NO}
        state.write_text(json.dumps(tasks[name], ensure_ascii=False), encoding="utf-8")
        print(f"  gửi {name}: {tid}", flush=True)

    prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
    pending = dict(tasks)
    t0 = time.time()
    while pending and time.time() - t0 < 1800:
        for name in list(pending):
            tk = pending[name]
            r = call("query_video_generation", {"task_id": tk["task_id"], "model": tk["model"]}, name)
            st = (find(r, {"status"}) or "").lower()
            if st in ("failed", "cancelled", "canceled"):
                print(f"!! {name}: {st} {json.dumps(r)[:300]}")
                pending.pop(name)
                continue
            if st not in ("succeeded", "success", "finished"):
                continue
            url = find(r, {"download_url", "video_url", "url"})
            node = find(r, {"node_id"})
            if not url and node:
                url = mcode(["get_asset_url", node], 120)["download_url"]
            if not url:
                print(f"!! {name}: xong nhưng không thấy link tải: {json.dumps(r)[:300]}")
                pending.pop(name)
                continue
            mp4 = RAW / f"{name}.mp4"
            urllib.request.urlretrieve(url, mp4)
            dst = OUT / f"{name}.wav"
            if dst.exists():
                shutil.copy2(dst, OUT / "_code" / dst.name)       # giữ bản tự tổng hợp để quay lại được
            to_wav(mp4, dst)
            f = f"assets/sfx/t2/{name}.wav"
            prov = [p for p in prov if p.get("file") != f] + [{
                "file": f, "loai": "nền môi trường (ambience)" if name.startswith("amb_") else "hiệu ứng âm thanh (SFX)",
                "cong_cu": f"MiniMax {tk['model']} (rãnh âm thanh gốc của video sinh ra) qua mcode-tools",
                "ngay": str(date.today()), "prompt": tk["prompt"], "seed": None, "mo_ta": name,
                "dieu_khoan": "Tạo bằng MiniMax — phải kiểm tra điều khoản thương mại trước khi bật kiếm tiền",
                "kiem_tra_thuong_mai": "chưa"}]
            print(f"  xong {name} → {dst}", flush=True)
            pending.pop(name)
        if pending:
            time.sleep(15)
    (ROOT / "provenance.json").write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
    if pending:
        print("!! còn chờ (chạy lại lệnh để tiếp tục, không gửi lại):", list(pending))
        sys.exit(2)


if __name__ == "__main__":
    main()
