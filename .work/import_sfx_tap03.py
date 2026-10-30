#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nhập tiếng động tải tay từ YouTube Audio Library cho Tập 03.

Nguồn: 02_SAN_XUAT/Tap03/sfx_youtube/<mã>.mp3  (tải tay trên YouTube Studio → Thư viện âm thanh)
Script:
  1. rãnh âm thanh → wav stereo 44,1 kHz 16-bit, cắt lặng đầu/cuối, chuẩn hoá đỉnh −1 dBFS
  2. ghi assets/sfx/t3/<mã>.wav
  3. ghi provenance.json (nguồn track YouTube + điều khoản)
Chạy: py -3 .work/import_sfx_tap03.py
"""
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "02_SAN_XUAT" / "Tap03" / "sfx_youtube"
OUT = ROOT / "assets" / "sfx" / "t3"
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFP = FF.with_name("ffprobe.exe")
PROV = ROOT / "provenance.json"

# mã → track YouTube (tên hiển thị trong Thư viện âm thanh) + thể loại.
# Thể loại chỉ ghi khi đã đọc được trên UI; không có thì để "" (không bịa).
YT = {
    "amb_rain_storm":        ("Summer Thunder and Rain", ""),
    "amb_pipe_drain":        ("Water Drains In Pipe with Pump", ""),
    "amb_crickets_traffic":  ("Crickets with Distant Traffic", "Không gian xung quanh"),
    "fx_coin_shuffle":       ("Coins Shuffling", ""),
    "fx_phone_ring":         ("Telephone Ring", ""),
    "fx_twisting_dial":      ("Twisting Dial Clicks", ""),
    "fx_paper_crunch":       ("Paper Crunching", "Tiếng động thực tế"),
    "fx_paper_fold":         ("Paper Folding", "Tiếng động thực tế"),
    "fx_cassette_motor":     ("Cassette Tape Motor", "Tiếng động thực tế"),
    "fx_cassette_button":    ("Cassette Tape Button", "Tiếng động thực tế"),
}

# CUTS: (bắt đầu s, độ dài s) — file tải về là cả bài 8–10 phút, đặt nguyên sẽ tràn qua nhiều câu.
# Nền môi trường (amb_*) cắt dài vừa đủ; tiếng động độc lập (fx_*) cắt đúng đoạn có hành động.
# Điểm cắt đo bằng envelope max/0,25 s (.work/tap03_review/_fine_t3.py) trên chính file nguồn.
CUTS = {
    "amb_rain_storm":       (0.0, 180.0),   # 9:32 nguyên bản → 3 phút đủ làm nền xe đêm mưa
    "amb_pipe_drain":       (0.0, 120.0),   # nước nhỏ giọt trong hầm
    "amb_crickets_traffic": (0.0, 66.0),    # đêm ngoài trời: chuộn + xe đi xa
    "fx_coin_shuffle":      (3.60, 4.00),   # đồng xu leng keng: vang nhất ở 4,0 s
    "fx_twisting_dial":     (0.15, 5.20),   # 5 cú quay số rõ (0,25 / 0,50 / 1,75 / 2,50 / 3,75 s)
    "fx_phone_ring":        (0.15, 4.50),   # một chuông điện thoại 0,25–2,0 s rồi tắt dần
    "fx_paper_crunch":      (0.15, 5.00),   # loạt giấy nhăn lúc mở đầu
    "fx_paper_fold":        (0.20, 6.00),   # tiếng gấp giấy 0,25–2,0 s
    "fx_cassette_button":   (4.20, 3.80),   # cú bấm nút rõ nhất ở 4,5 s, nhả nút ở 7,5 s
    "fx_cassette_motor":    (0.0, 20.0),    # rè băng từ quay chậm — liên tục, không đứt
}


def dur(p):
    r = subprocess.run([str(FFP), "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=noprint_wrappers=1:nokey=1", str(p)],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def peak_db(p):
    r = subprocess.run([str(FF), "-hide_banner", "-i", str(p), "-af", "volumedetect",
                        "-f", "null", "-"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    m = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else -3.0


def rms_profile(p, n=12):
    """RMS dB theo từng đoạn — dùng để mô tả trung thực nội dung file (không nghe được)."""
    r = subprocess.run([str(FF), "-hide_banner", "-i", str(p), "-af", "astats=metadata=1:reset=1",
                        "-f", "null", "-"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    vals = [float(x) for x in re.findall(r"RMS level dB: (-?[\d.]+|-inf)", r.stderr)]
    vals = [v for v in vals if v > -120]
    if not vals:
        return ""
    step = max(1, len(vals) // n)
    chunks = [vals[i:i + step] for i in range(0, len(vals), step)]
    return " ".join(f"{max(c):.0f}" for c in chunks)


def main():
    INBOX.mkdir(parents=True, exist_ok=True)
    OUT.mkdir(parents=True, exist_ok=True)
    prov = json.loads(PROV.read_text(encoding="utf-8"))
    done = 0
    for src in sorted(INBOX.glob("*.mp3")):
        name = src.stem
        if name not in YT:
            print(f"!! {src.name}: chưa khai báo track YouTube — bỏ qua")
            continue
        sd = dur(src)
        ss, cd = CUTS.get(name, (0.0, sd))
        cd = min(cd, sd - ss)
        if cd <= 0.05:
            print(f"!! {src.name}: không còn đoạn nào sau khi cắt — bỏ qua")
            continue
        dst = OUT / f"{name}.wav"
        tmp = OUT / f"{name}.tmp.wav"
        # nền: bỏ khoảng lặng đầu/cuối, fade 0,5 s / 2 s | hiệu ứng: cắt cứng + fade ngắn
        if name.startswith("amb_"):
            af = ("silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.05,"
                  "areverse,silenceremove=start_periods=1:start_threshold=-55dB:start_silence=0.3,areverse,"
                  f"atrim=start={ss}:duration={cd},asetpts=PTS-STARTPTS,"
                  f"afade=t=in:d=0.5,afade=t=out:st={max(0.0, cd - 2.0)}:d=2.0")
        else:
            af = (f"atrim=start={ss}:duration={cd},asetpts=PTS-STARTPTS,"
                  f"afade=t=in:d=0.01,afade=t=out:st={max(0.0, cd - 0.4)}:d=0.4")
        subprocess.run([str(FF), "-y", "-v", "error", "-i", str(src), "-vn", "-af", af,
                        "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le", str(tmp)], check=True)
        pk = peak_db(tmp)
        subprocess.run([str(FF), "-y", "-v", "error", "-i", str(tmp), "-af",
                        f"volume={-1.0 - pk}dB", "-c:a", "pcm_s16le", str(dst)], check=True)
        tmp.unlink()
        track, genre = YT[name]
        f = f"assets/sfx/t3/{name}.wav"
        prov = [p for p in prov if p.get("file") != f] + [{
            "file": f,
            "loai": "nền môi trường (ambience)" if name.startswith("amb_") else "hiệu ứng âm thanh (SFX)",
            "cong_cu": ("YouTube Audio Library (YouTube Studio) — tải tay từ Thư viện âm thanh, "
                        f"nhập bằng .work/import_sfx_tap03.py (file gốc: {src.name})"),
            "ngay": str(date.today()), "prompt": None, "seed": None, "mo_ta": name,
            "font": None,
            "dieu_khoan": ("YouTube Audio Library — miễn phí dùng trong video/nội dung do chính kênh sáng tạo; "
                           "KHÔNG được cung cấp, phân phối hoặc phát hành riêng file âm thanh"),
            "kiem_tra_thuong_mai": "đạt (có điều kiện: chỉ dùng trong video của kênh, không phát hành riêng file)",
            "track_youtube": track, "the_loai_youtube": genre, "nguon_goc": src.name,
            "cat_goc": f"{ss:.1f}s + {cd:.1f}s (nguồn {sd:.1f}s)"}]
        print(f"  {name:<22} {track:<34} {cd:6.1f}s  peak {pk:+.1f}dB -> {dst.relative_to(ROOT)}")
        done += 1
    PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\n{done} file đã nhập vào assets/sfx/t3/.")
    print("Nghe lại từng file trước khi chốt mức dB trong .work/sfx_tap03.json.")


if __name__ == "__main__":
    main()
