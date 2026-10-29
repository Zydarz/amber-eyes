#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nhập tiếng động vào bộ âm thanh Tập 02.

Nguồn có thể là video AI (Gemini / Veo, MiniMax…) hoặc tiếng tải tay từ YouTube Audio Library.
Người dùng đặt file vào 02_SAN_XUAT/Tap02/sfx_gemini/ với tên đúng mã, ví dụ fx_gavel_triple.mp3
(chấp nhận .mp4 .mov .webm .wav .mp3 .m4a). Script:
  1. lấy rãnh âm thanh → wav stereo 44,1 kHz, cắt lặng đầu/cuối, chuẩn hoá đỉnh
  2. chép bản tự tổng hợp cùng tên sang assets/sfx/t2/_code/ (quay lại được), rồi ghi đè assets/sfx/t2/<mã>.wav
  3. ghi provenance.json (công cụ, nguồn, ngày, prompt lấy từ hướng dẫn)
Chạy:  py -3 .work/import_sfx_video.py --tool "YouTube Audio Library (YouTube Studio)"
"""
import argparse
import json
import re
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
INBOX = ROOT / "02_SAN_XUAT" / "Tap02" / "sfx_gemini"
GUIDE = ROOT / "02_SAN_XUAT" / "Tap02" / "HuongDan_TaoSFX_Gemini.md"
OUT = ROOT / "assets" / "sfx" / "t2"
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFP = FF.with_name("ffprobe.exe")
EXT = (".mp4", ".mov", ".webm", ".wav", ".mp3", ".m4a")
MANIFEST = ROOT / ".work" / "yt_audio_library" / "manifest.json"

AMB_RMS_TARGET = -28.0   # moi nen moi chuan hoa ve RMS nay (dBFS)


def mean_volume(path):
    """mean_volume (dB) cua file - dung de do RMS."""
    r = subprocess.run([str(FF), "-hide_banner", "-i", str(path), "-af", "volumedetect",
                        "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"mean_volume: (-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else -60.0


def peak_volume(path):
    """max_volume (dB) cua file."""
    r = subprocess.run([str(FF), "-hide_banner", "-i", str(path), "-af", "volumedetect",
                        "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace")
    m = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else -60.0


# Kiểm tra 23/10/2026 (nghe bằng mô hình nhận dạng + đo năng lượng từng giây):
# CUTS: chỉ lấy đoạn chứa đúng hành động — file tải về là cả bài 14–59 s, đặt nguyên sẽ kéo dài qua nhiều câu.
#       (bắt đầu s, độ dài s). Nền môi trường (amb_*) không cắt: càng dài càng ít lộ chỗ lặp.
CUTS = {"fx_door_metal_slam": (8.6, 2.4),   # Dumpster Door Slam: 1 cu dong sat nhat o ~9,25 s
        "fx_tire_snow": (34.0, 11.0),        # Car Drive By: lan xe cham nhat o ~38,5 s
        "fx_fire_whoosh": (0.0, 8.0),        # Wind Drawn Into Fire: bat lua 0-2 s roi cháy
        "fx_footsteps_snow": (0.0, 6.0),     # Walk on Snow Series: buoc chan o dau file
        "fx_chair_scrape": (7.5, 4.0),       # Slide On Metal Grate Series: doan qua gan nhat o 8,25 s
        "fx_gavel_triple": (0.1, 1.9),       # Wooden Bead Hitting Series: 3 cuc go 0,25-1,5 s
        "fx_window_down": (0.0, 2.4),        # Trunk Window Open Hydraulic Hiss: file chi 2,4 s
        "fx_camera_shutter": (1.1, 2.6),     # Play And Stop On A Camera: tieng chup o ~1,5-2 s
        "fx_cup_down": (19.8, 3.0),          # Cup on Saucer: cuc lon nhat o 20,25 s
        "fx_drawer_open": (4.3, 3.0),        # Drawer Open/Close: dot lon nhat o 5,0 s
        "fx_flashlight": (1.3, 2.0),         # Lamp Switch On/Off: hai click o 1,5 s va 2,75 s
        "fx_hdd_spin": (0.0, 9.0),           # Disk Drive Insert and Spinning: cam + quay
        "fx_map_unfold": (11.0, 3.5),        # Paper Folding: dot lon nhat o 11,75 s
        "fx_paper_folder": (0.6, 2.5),       # Clipboard: cuc kep o 1,0 s
        "fx_pen_scribble": (0.5, 8.0),       # Pen Writing: 8 s viet lien tuc
        "fx_phone_ring": (5.5, 4.0),         # Phone Alerts And Rings: chuong o ~6,5-7,5 s
        "fx_photo_slide": (2.0, 4.0),        # Feeling Paper: cuc lon nhat o 3,25 s
        "fx_stinger": (21.0, 4.5),           # Sci Fi Vortex: vung nang nhat o 22,75 s
        "fx_sub_drop": (16.0, 8.0),          # High To Low Sweep: doan xuong tan, dam o 16-24 s
        "fx_tension_tick": (5.8, 6.5)}       # Setting Alarm Clock: tieng tick o 6-12 s
# KEEP_CODE: file tải về sai nội dung → giữ bản tự tổng hợp (assets/sfx/t2/_code/)
KEEP_CODE = {}   # 23/10/2026: da doi sang tieng that tu YouTube Audio Library cho ca 32 ma


def yt_manifest():
    """mã → thông tin track YouTube (nếu có manifest của trình thu thập YouTube Audio Library)."""
    if not MANIFEST.exists():
        return {}
    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    return {d["mã"]: d for d in data if d.get("mã")}


def terms(tool, src_name, yt):
    """Câu chữ provenance đúng với nguồn thật của file."""
    if "YouTube Audio Library" in tool:
        track = yt.get("track_youtube") or "(không ghi trong thẻ ID3)"
        return {
            "cong_cu": (f"{tool} — tải tay từ YouTube Studio, nhập bằng .work/import_sfx_video.py "
                        f"(file gốc: {src_name})"),
            "dieu_khoan": ("YouTube Audio Library — miễn phí dùng trong video/nội dung do chính kênh sáng tạo; "
                           "KHÔNG được cung cấp, phân phối hoặc phát hành riêng file âm thanh"),
            "kiem_tra_thuong_mai": "đạt (có điều kiện: chỉ dùng trong video của kênh, không phát hành riêng file)",
            "track_youtube": track,
            "the_loai_youtube": yt.get("the_loai", ""),
        }
    return {
        "cong_cu": (f"{tool} — rãnh âm thanh của video AI, nhập bằng .work/import_sfx_video.py "
                    f"(file gốc: {src_name})"),
        "dieu_khoan": "Tạo bằng công cụ AI của bên thứ ba — kiểm tra điều khoản thương mại trước khi bật kiếm tiền",
        "kiem_tra_thuong_mai": "chưa",
        "track_youtube": None,
        "the_loai_youtube": None,
    }


def prompts():
    """Mã → prompt, đọc từ các khối ```text``` ngay sau tiêu đề '### <mã>' trong hướng dẫn."""
    t = GUIDE.read_text(encoding="utf-8") if GUIDE.exists() else ""
    return {m.group(1): m.group(2).strip() for m in re.finditer(r"^### `?(\w+)`?.*?```text\n(.*?)```", t, re.S | re.M)}


def has_audio(p):
    r = subprocess.run([str(FFP), "-v", "error", "-select_streams", "a", "-show_entries", "stream=index",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return bool(r.stdout.strip())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tool", default="Gemini (Veo)")
    a = ap.parse_args()
    INBOX.mkdir(parents=True, exist_ok=True)
    (OUT / "_code").mkdir(parents=True, exist_ok=True)
    pr = prompts()
    ytm = yt_manifest()
    known = {p.stem for p in OUT.glob("*.wav")} | set(pr)
    prov = json.loads((ROOT / "provenance.json").read_text(encoding="utf-8"))
    done = 0
    for src in sorted(p for p in INBOX.iterdir() if p.suffix.lower() in EXT):
        name = src.stem
        if name not in known:
            print(f"!! {src.name}: tên không khớp mã nào trong hướng dẫn — bỏ qua")
            continue
        if not has_audio(src):
            print(f"!! {src.name}: không có rãnh âm thanh — bỏ qua")
            continue
        dst = OUT / f"{name}.wav"
        f = f"assets/sfx/t2/{name}.wav"
        code = OUT / "_code" / dst.name
        if name in KEEP_CODE:
            if code.exists():
                shutil.copy2(code, dst)
                prov = [p for p in prov if p.get("file") != f] + [{
                    "file": f, "loai": "hiệu ứng âm thanh (SFX)",
                    "cong_cu": ".work/make_sfx3.py (tổng hợp bằng numpy/scipy) — giữ lại vì file tải về sai nội dung",
                    "ngay": str(date.today()), "prompt": None, "seed": "cố định trong code", "mo_ta": name,
                    "dieu_khoan": "Kênh tự tạo bằng code, không dùng AI hay tài sản bên thứ ba",
                    "kiem_tra_thuong_mai": "đạt", "ghi_chu": f"Bỏ {src.name}: {KEEP_CODE[name]}"}]
            print(f"  giữ bản code {name}: {KEEP_CODE[name]}")
            continue
        if dst.exists() and not code.exists():
            shutil.copy2(dst, code)
        if name in CUTS:
            ss, dur = CUTS[name]
            af = (f"atrim=start={ss}:duration={dur},asetpts=PTS-STARTPTS,"
                  f"afade=t=in:d=0.03,afade=t=out:st={max(0.0, dur - 0.6)}:d=0.6")
        else:
            af = ("silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.05,"
                  "areverse,silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.3,areverse,"
                  "afade=t=in:d=0.02")
        # chuẩn hoá đỉnh −1 dBFS, giữ nguyên độ động (build_audio3 tự đặt mức theo RMS lời)
        # --- nen moi truong: chuan hoa RMS ve AMB_RMS_TARGET, nen fx: chuan hoa dinh -1 dBFS ---
        subprocess.run([str(FF), "-y", "-v", "error", "-i", str(src), "-vn", "-af", af,
                        "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", str(dst.with_suffix(".tmp.wav"))], check=True)
        tmp = dst.with_suffix(".tmp.wav")
        if name.startswith("amb_"):
            rms0 = mean_volume(tmp)
            gain = max(-12.0, min(15.0, AMB_RMS_TARGET - rms0))
            chain = (f"volume={gain:.2f}dB,"
                     "acompressor=threshold=-25dB:ratio=4:attack=5:release=150,"
                     "alimiter=limit=0.891:attack=3:release=80")
            subprocess.run([str(FF), "-y", "-v", "error", "-i", str(tmp), "-af", chain,
                            "-c:a", "pcm_s16le", str(dst)], check=True)
            rms_final, peak_final = mean_volume(dst), peak_volume(dst)
        else:
            peak = peak_volume(tmp)
            subprocess.run([str(FF), "-y", "-v", "error", "-i", str(tmp), "-af",
                            f"volume={-1.0 - peak}dB", "-c:a", "pcm_s16le", str(dst)], check=True)
            rms_final, peak_final = mean_volume(dst), peak_volume(dst)
        tmp.unlink()
        yt = ytm.get(name, {})
        t = terms(a.tool, src.name, yt)
        prov = [p for p in prov if p.get("file") != f] + [{
            "file": f, "loai": "nền môi trường (ambience)" if name.startswith("amb_") else "hiệu ứng âm thanh (SFX)",
            "cong_cu": t["cong_cu"],
            "ngay": str(date.today()), "prompt": pr.get(name), "seed": None, "mo_ta": name,
            "dieu_khoan": t["dieu_khoan"],
            "kiem_tra_thuong_mai": t["kiem_tra_thuong_mai"],
            "track_youtube": t["track_youtube"], "the_loai_youtube": t["the_loai_youtube"],
            "nguon_goc": src.name, "rms_dbfs": round(rms_final, 2), "peak_dbfs": round(peak_final, 2)}]
        print(f"  nhập {src.name} → {dst.relative_to(ROOT)}")
        done += 1
    (ROOT / "provenance.json").write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{done} file đã nhập. Bản tự tổng hợp cũ nằm ở assets/sfx/t2/_code/ (chép ngược lại để quay về).")


if __name__ == "__main__":
    main()
