#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nhập SFX từ inbox YouTube Audio Library → assets/sfx/ (wav) + provenance.json.

Nguồn : 02_SAN_XUAT/sfx_youtube/<mã>.mp3  (watcher _yt_watch.py đã đổi tên)
Đích  : assets/sfx/<mã>.wav  (dùng ≥2 tập)  hoặc  assets/sfx/tXX/<mã>.wav  (1 tập)
        — đường dẫn lấy từ bảng mục 4 của 02_SAN_XUAT/Danh_Sach_SFX_Tap03-29.md
Cắt   : tự động — nền (amb_*) lấy đoạn ổn định tối đa 120 s; tiếng động (fx_*)
        lấy quanh đỉnh tiếng (mặc định 6 s).

Chạy:  py -3 .work/import_sfx_series.py
"""
import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _yt_envelope import envelope, pick_amb_cut, pick_fx_cut  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
DOC = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
MAP = ROOT / ".work" / "yt_map.tsv"
PROV = ROOT / "provenance.json"
NGAY = "2026-10-24"

DIEU_KHOAN = ("YouTube Audio Library — miễn phí dùng trong video/nội dung do chính kênh sáng tạo; "
              "KHÔNG được cung cấp, phân phối hoặc phát hành riêng file âm thanh")
KIEM_TM = "đạt (có điều kiện: chỉ dùng trong video của kênh, không phát hành riêng file)"


def doc_dest():
    """mã (không .wav) -> đường dẫn đích tương đối trong assets/sfx"""
    out = {}
    for line in io.open(DOC, encoding="utf-8").read().splitlines():
        p = [x.strip() for x in line.split("|")]
        if len(p) < 6 or not p[2].startswith("`"):
            continue
        name = p[2].strip("`")
        dest = p[5].strip("`")
        if not name.endswith(".wav") or not dest.startswith("assets/sfx/"):
            continue
        out[name[:-4]] = dest
    return out


def manifest():
    """mã -> dict(track, loai, genre, dur)"""
    out = {}
    for raw in io.open(MAP, encoding="utf-8-sig").read().splitlines():
        p = raw.split("\t")
        if len(p) < 6 or not p[1].strip():
            continue
        out[p[1].strip()] = {"track": p[0].strip(), "loai": p[2].strip(),
                              "genre": p[4].strip(),
                              "dur": float(p[5]) if p[5].strip() else 0.0}
    return out


def thr_for(env, start, dur):
    """Ngưỡng 'im lặng' TƯƠNG ĐỐI so với đỉnh của chính đoạn cắt.

    Ngưỡng cố định -45 dB xoá sạch các nguồn nhỏ (hơi thở, tiếng máy vặn nhỏ,
    tiếng ngân xa) -> file ra 0 giây. Ở đây lấy đỉnh của đoạn đã chọn rồi
    hạ 18 dB, tối thiểu -90 dB.
    """
    seg = [db for t, db in env if start <= t < start + dur]
    if not seg:
        seg = [db for _, db in env]
    if not seg:
        return -45.0
    return max(-90.0, max(seg) - 18.0)


def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r


def max_volume(path):
    r = run([str(FF), "-hide_banner", "-i", str(path), "-af", "volumedetect", "-f", "null", "-"])
    m = re.search(r"max_volume: (-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else -120.0


def probe_dur(path):
    r = run([str(FF), "-hide_banner", "-i", str(path), "-f", "null", "-"])
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r.stderr)
    if not m:
        return 0.0
    return int(m.group(1)) * 3600 + int(m.group(2)) * 60 + float(m.group(3))


def main():
    dest_map = doc_dest()
    mf = manifest()
    prov = json.load(io.open(PROV, encoding="utf-8"))
    by_file = {e.get("file"): e for e in prov}

    made = 0
    only = set(sys.argv[1:])
    for mp3 in sorted(INBOX.glob("*.mp3")):
        ma = mp3.stem
        if only and ma not in only:
            continue
        dest = dest_map.get(ma)
        if dest is None:
            print("!! KHONG co duong dan dich cho %s (bo qua)" % ma)
            continue
        info = mf.get(ma, {})
        src_dur = probe_dur(mp3)
        env = envelope(mp3)
        is_amb = ma.startswith("amb_")
        if is_amb:
            start, dur = pick_amb_cut(env, maxlen=min(120.0, max(10.0, src_dur)))
            loai = "nền môi trường (ambience)"
            fade_in, fade_out = 0.5, 2.0
        else:
            start, dur = pick_fx_cut(env, window=8.0)
            loai = "hiệu ứng âm thanh (SFX)"
            fade_in, fade_out = 0.01, 0.4
        dur = min(dur, max(0.5, src_dur - start))
        thr = thr_for(env, start, dur)
        if src_dur < 2.0:
            # nguồn cực ngắn (tiếng bấm 1 lần): cắt lặng sẽ nuốt mất tiếng,
            # giữ nguyên toàn bộ rồi mới fade + chuẩn hoá.
            trim_af = "anull"
        elif is_amb:
            trim_af = ("silenceremove=start_periods=1:start_silence=0.05:start_threshold=%.0fdB" % thr)
        else:
            trim_af = ("areverse,silenceremove=start_periods=1:start_silence=0.05:start_threshold=%.0fdB,areverse" % thr)
        out = ROOT / dest
        out.parent.mkdir(parents=True, exist_ok=True)
        tmp = ROOT / ".work" / "_tmp_a.wav"
        tmp2 = ROOT / ".work" / "_tmp_b.wav"
        # pass 1: cắt + bỏ khoảng lặng đầu/cuối
        r = run([str(FF), "-y", "-v", "error", "-ss", "%.3f" % start, "-t", "%.3f" % dur,
                 "-i", str(mp3), "-af", trim_af, "-ac", "2", "-ar", "44100",
                 "-c:a", "pcm_s16le", str(tmp)])
        if r.returncode != 0 or not tmp.exists():
            print("!! ffmpeg that bai cho %s: %s" % (ma, r.stderr[:300]))
            continue
        d1 = probe_dur(tmp)
        if d1 < 0.15:
            print("!! %s sau khi cat chi con %.2fs — bo qua" % (ma, d1))
            tmp.unlink(missing_ok=True)
            continue
        # pass 2: fade + chuan hoa dinh -1 dBFS
        # apad: file nguon rat ngan (tieng click 0,3 s) duoi 0,6 s de khong bi
        # cat cut trong DAW (duoi nguong QC 0,5 s).
        af2 = ("afade=t=in:st=0:d=%.3f,afade=t=out:st=%.3f:d=%.3f,apad=whole_dur=0.6"
               % (fade_in, max(0.0, d1 - fade_out), fade_out))
        run([str(FF), "-y", "-v", "error", "-i", str(tmp), "-af", af2,
             "-ac", "2", "-ar", "44100", "-c:a", "pcm_s16le", str(tmp2)])
        mv = max_volume(tmp2)
        # chuan hoa ve -1 dBFS; ghi cap khuuyen dai <= +17 dB de khong
        # khuuyen dai nhieu nen (tieng gio/gio rong rat nhe, neu de nguyen se
        # khong nghe thay khi mix).
        gain = (-1.0 - mv)
        if gain > 17.0:
            gain = 17.0
        # nguồn rất khẽ: nếu sau +17 dB vẫn nhỏ hơn -25 dBFS thì nâng tiếp
        # (tới -25 dBFS, tối đa +30 dB) để nghe được trong bản trộn.
        if mv + gain < -25.0:
            gain = min(30.0, -25.0 - mv)
        if abs(gain) > 0.1:
            run([str(FF), "-y", "-v", "error", "-i", str(tmp2), "-af", "volume=%.2fdB" % gain,
                 "-ac", "2", "-ar", "44100", "-c:a", "pcm_s16le", str(out)])
        else:
            os.replace(tmp2, out)
        tmp.unlink(missing_ok=True)
        tmp2.unlink(missing_ok=True)
        real = probe_dur(out)
        entry = {
            "file": dest,
            "loai": loai,
            "cong_cu": ("YouTube Audio Library (YouTube Studio → Thư viện âm thanh) — tải tay, "
                        "nhập bằng .work/import_sfx_series.py (file gốc: %s.mp3)" % ma),
            "ngay": NGAY,
            "prompt": None,
            "seed": None,
            "mo_ta": ma,
            "font": None,
            "dieu_khoan": DIEU_KHOAN,
            "kiem_tra_thuong_mai": KIEM_TM,
            "track_youtube": info.get("track", ""),
            "the_loai_youtube": info.get("genre", ""),
            "nguon_goc": "%s.mp3" % ma,
            "cat_goc": "%.1fs + %.1fs (nguồn %.1fs)" % (start, real, src_dur),
        }
        by_file[dest] = entry
        made += 1
        print("OK  %-34s -> %s  (%.1fs + %.1fs / nguồn %.1fs, gain %.1f dB)"
              % (ma, dest, start, real, src_dur, gain))

    out = [e for e in prov if e.get("file") not in by_file or by_file[e.get("file")] is e]
    for f, e in by_file.items():
        if not any(x.get("file") == f for x in out):
            out.append(e)
    json.dump(out, io.open(PROV, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("--- da tao %d file, provenance.json hien co %d muc ---" % (made, len(out)))


if __name__ == "__main__":
    main()
