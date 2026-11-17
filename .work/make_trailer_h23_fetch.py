#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tải + chuẩn hoá 4 clip Hailuo-2.3 đã sinh xong (tải nguyên tử, có validate).

Dùng: py -3 .work/make_trailer_h23_fetch.py
Input: .work/trailer_a/h23/tasks.json (đã có node_id)
Output: videos/<ten>.mp4            (bản gốc H2.3)
        .work/trailer_a/h23_norm/<key>.mp4  (1920x1080@30, KHÔNG grain/vignette — lớp chung áp ở pipeline trailer)
"""
import json
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
H23 = ROOT / ".work" / "trailer_a" / "h23"
NORM = ROOT / ".work" / "trailer_a" / "h23_norm"
VIDEOS = ROOT / "videos"
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFPROBE = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
PROV = ROOT / "provenance.json"


def probe(path):
    r = subprocess.run([str(FFPROBE), "-v", "error", "-show_entries",
                        "format=duration:stream=codec_type,codec_name,width,height",
                        "-of", "json", str(path)], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[:300])
    return json.loads(r.stdout)


def normalise(src, dst):
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(src),
                    "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,fps=30,format=yuv420p",
                    "-c:v", "libopenh264", "-b:v", "8M", "-maxrate", "12M", "-bufsize", "16M", "-an",
                    str(dst)], check=True)


def main():
    NORM.mkdir(parents=True, exist_ok=True)
    VIDEOS.mkdir(parents=True, exist_ok=True)
    rec = json.loads((H23 / "tasks.json").read_text(encoding="utf-8"))
    prov = json.loads(PROV.read_text(encoding="utf-8")) if PROV.exists() else []

    for key, t in rec.items():
        node = t.get("node_id")
        if not node:
            print(f"!! {key}: chưa có node_id")
            continue
        out = ROOT / t["output_file"]
        if out.exists() and out.stat().st_size > 0:
            print(f"  {key}: đã có {out.name} ({out.stat().st_size / 1e6:.1f} MB) — bỏ qua tải")
        else:
            r = subprocess.run(["cmd", "/c", "mcode-tools", "get_asset_url", node],
                               capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=300)
            if r.returncode != 0:
                print(f"!! {key}: get_asset_url lỗi: {(r.stderr or r.stdout)[:200]}")
                continue
            url = json.loads(r.stdout)["download_url"]
            part = out.with_suffix(out.suffix + ".part")
            urllib.request.urlretrieve(url, part)
            info = probe(part)
            if not info.get("streams"):
                part.unlink(missing_ok=True)
                print(f"!! {key}: file tải về không có stream — đã xoá bản .part")
                continue
            dur = float(info["format"]["duration"])
            if not (4.0 <= dur <= 8.0):
                part.unlink(missing_ok=True)
                print(f"!! {key}: thời lượng {dur:.2f}s ngoài 4–8 s — đã xoá bản .part")
                continue
            part.replace(out)
            print(f"  {key}: tải xong {out.name} ({dur:.2f}s, {out.stat().st_size / 1e6:.1f} MB)")

        normalise(out, NORM / f"{key}.mp4")
        info = probe(NORM / f"{key}.mp4")
        vs = [s for s in info["streams"] if s.get("codec_type") == "video"][0]
        print(f"     chuẩn hoá: {vs['width']}x{vs['height']} {vs['codec_name']} "
              f"{float(info['format']['duration']):.2f}s -> {NORM / (key + '.mp4')}")

        f = t["output_file"]
        prov = [p for p in prov if p.get("file") != f] + [{
            "file": f, "loai": "clip video AI (b-roll trailer, first-frame)",
            "cong_cu": "MiniMax Hailuo-2.3 qua mcode-tools",
            "ngay": str(date.today()), "prompt": t.get("prompt", ""), "seed": None,
            "mo_ta": f"{key} — khung đầu: assets/bg/{t.get('bg')}.png",
            "dieu_khoan": "Tạo bằng MiniMax — phải kiểm tra điều khoản thương mại trước khi bật kiếm tiền",
            "kiem_tra_thuong_mai": "chưa"}]
    PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
    print("provenance đã cập nhật")


if __name__ == "__main__":
    main()
