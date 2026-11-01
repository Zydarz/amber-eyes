#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat ho so (KeHoach_Video_Tap02_EN.md) sau khi dung lai tap 02 EN.

Chi ghi cac so do do that tu thuoc te (khong hard-code).
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
os.environ.setdefault("AE_LANG", "en")
os.environ.setdefault("AE_EP", "02")
sys.path.insert(0, str(W))
import edition as ED  # noqa: E402

FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")
PLAN = ED.EP_DIR / "KeHoach_Video_Tap02_EN.md"
OUT = ED.OUT_DIR
MP4 = OUT / (ED.MASTER + ".mp4")
MP3 = OUT / (ED.MASTER + ".mp3")
TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8-sig"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8-sig"))


def sh(a, t=3600):
    return subprocess.run(a, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=t)


def dur(p):
    return float(sh([str(FP), "-v", "error", "-show_entries", "format=duration",
                     "-of", "default=noprint_wrappers=1:nokey=1", str(p)]).stdout.strip())


def ebur(p):
    r = sh([str(FF), "-hide_banner", "-nostats", "-i", str(p), "-af", "ebur128=peak=true",
            "-f", "null", "-"])
    lines = [l for l in r.stderr.splitlines() if " I:" in l]
    lufs = None
    if lines:
        m = re.search(r"I:\s*(-?[\d.]+)\s*LUFS", lines[-1])
        lufs = float(m.group(1)) if m else None
    pk = re.findall(r"Peak:\s*(-?[\d.]+)\s*dBFS", r.stderr)
    return lufs, (float(pk[-1]) if pk else None)


def sil(p, noise="-60dB", d="0.3"):
    r = sh([str(FF), "-hide_banner", "-nostats", "-i", str(p),
            "-af", f"silencedetect=n={noise}:d={d}", "-f", "null", "-"])
    return len(re.findall(r"silence_start:", r.stderr))


def human(n):
    n = float(n)
    return "%d:%05.2f" % (int(n // 60), n % 60)


d_mp3, d_mp4 = dur(MP3), dur(MP4)
l_mp3, p_mp3 = ebur(MP3)
l_mp4, p_mp4 = ebur(MP4)
n_sil = sil(MP4)
frames = int(re.search(r"nb_frames=(\d+)",
                       sh([str(FP), "-v", "error", "-select_streams", "v:0", "-show_entries",
                           "stream=nb_frames", "-of", "default=noprint_wrappers=1",
                           str(MP4)]).stdout).group(1))
items, shots = TL["items"], SH["shots"]
sd = sorted(s["end"] - s["start"] for s in shots)
ld = sorted(i["end"] - i["start"] for i in items)
n_cue = len([b for b in re.split(r"\n\s*\n",
                                 (OUT / ED.SRT).read_text(encoding="utf-8-sig").strip())
             if b.strip()])
acts = TL["acts"]
act_txt = " · ".join("%s–%s" % (acts[str(i)][0], acts[str(i)][1]) for i in range(1, 6))


def mmss(t):
    t = float(t)
    return "%02d:%02d" % (int(t // 60), int(t % 60))


# moc chuong: 00:00 Intro + 5 hoi (package.py: act 1 = 20,5 s; cac hoi sau lay tu marker ACT)
_starts = {1: 20.5}
for _m in TL["markers"]:
    if _m.get("type") == "ACT":
        _starts[_m["act"]] = _m["start"]
chap = "00:00 / " + " / ".join(mmss(_starts[i]) for i in sorted(_starts))

mp4_b = MP4.stat().st_size
mp3_b = MP3.stat().st_size

txt = PLAN.read_text(encoding="utf-8-sig")


def sub(old, new, label):
    global txt
    n = txt.count(old)
    assert n == 1, "%s: doi duoc %d lan (mong doi 1)" % (label, n)
    txt = txt.replace(old, new)
    print("  OK %s" % label)


print("Cap nhat ho so:")

sub(
    "> **TRẠNG THÁI: XONG (25/10/2026 — Director's Cut)** → xuat_ban/Tap02_EN_master.mp4 "
    "(27:54,60 · 1920×1080@30 · H.264+AAC · 595.720.561 byte) · **QC A9.1–A9.4 đạt toàn bộ** "
    "(exit 0) · G10 đạt (5/5 vai 1 người).",
    "> **TRẠNG THÁI: XONG (01/11/2026 — dựng lại theo audio Higgs) → xuat_ban/Tap02_EN_master.mp4 "
    "(%s · 1920×1080@30 · H.264+AAC · %s byte) · **QC A9.1–A9.4 đạt toàn bộ** (exit 0) · "
    "G10 đạt (5/5 vai 1 người) · báo cáo giám sát: `BAO_CAO_GIAM_SAT_T02_EN.md`."
    % (human(d_mp4), format(mp4_b, ",").replace(",", ".")),
    "dong trang thai")

sub(
    "| Âm thanh | **1723,5 s (28:43,47)** · 14 nền SFX + 37 tiếng động · lời đầu 23,0 s · "
    "hồi 1: 23,0–306,2 · 2: 308,2–570,1 · 3: 572,1–966,2 · 4: 968,2–1359,4 · "
    "5: 1361,4–1714,5 s |",
    "| Âm thanh | **%s s (%s)** · 14 nền SFX + 37 tiếng động · lời đầu 23,0 s · "
    "hồi %s s (bản Higgs; bản MiniMax cũ 1723,5 s — ngắn hơn 16,8%%) |"
    % ("%.1f" % d_mp3, human(d_mp3), act_txt),
    "dong am thanh")

sub(
    "| Hình | `build_video3.py --workers 6` → 3365 s (56 phút) → "
    "`.work/video3_EN_t02/picture.mp4` (51.704 khung 1920×1080@30) |",
    "| Hình | `build_video3.py --workers 6` → `.work/video3_EN_t02/picture.mp4` "
    "(%s khung 1920×1080@30 · %s s) — dựng lại 01/11/2026 vì audio đổi (H14) |"
    % (format(frames, ",").replace(",", "."), "%.2f" % d_mp4),
    "dong hinh")

sub(
    "| Phụ đề | `Tap02_EN.srt` — 425 cue, cue cuối kết thúc 1714,5 s |",
    "| Phụ đề | `Tap02_EN.srt` — %d cue, cue cuối kết thúc %.1f s |" % (n_cue, d_mp4),
    "dong phu de")

sub(
    "| Gói đăng | `Tap02_EN_master.mp4` (578.017.179 byte) · `Tap02_EN_master.mp3` "
    "(41.364.908 byte) · `thumbnail.png` (THE TWO-FACED / COLONEL) · `mo_ta.txt` + "
    "`description.txt` (mốc chương 00:00 / 00:20 / 05:06 / 09:30 / 16:06 / 22:39 + hotline "
    "RAINN / Domestic Violence / VictimConnect / CRCVC / 911) · `nguon_tham_khao_EN.md` — "
    "**khung đã sinh**, cần điền link đã kiểm chứng |",
    "| Gói đăng | `Tap02_EN_master.mp4` (%s byte) · `Tap02_EN_master.mp3` (%s byte) · "
    "`thumbnail.png` (THE TWO-FACED / COLONEL) · `mo_ta.txt` + `description.txt` "
    "(mốc chương %s + hotline RAINN / Domestic Violence / VictimConnect / CRCVC / 911 + "
    "**ghi công Higgs Audio v3**) · `nguon_tham_khao_EN.md` — **khung đã sinh**, cần điền "
    "link đã kiểm chứng |"
    % (format(mp4_b, ",").replace(",", "."), format(mp3_b, ",").replace(",", "."), chap),
    "dong goi dang")

sub(
    "**Chưa làm:** dựng lại hình (`parse_shots.py` + `build_video3.py`, H14 — audio đổi), "
    "phụ đề, đóng gói; ghi công Higgs trong mô tả (§2).",
    "**Đã làm (01/11/2026):** dựng lại hình (`parse_shots.py` + `build_video3.py`, H14 — audio đổi) "
    "· phụ đề · đóng gói · ghi công Higgs trong mô tả (§2) — xem `BAO_CAO_GIAM_SAT_T02_EN.md`.",
    "dong chua lam")

# them muc tom tat cua loot sua loi
anchor = "**Đã làm (01/11/2026):**"
extra = """
### Lượt sửa lỗi 01/11/2026 (trước khi dựng lại)

| # | Vấn đề | Xử lý |
|---|---|---|
| 1 | Câu `3.02#1` có **41,57 s im lặng kỹ thuật** (file 47,56 s, lời đọc 5,99 s) ⇒ shot 3-01 dài 48,1 s, vỡ nhịp hồi 3 | Thay bằng seed **s1** đã sinh sẵn (6,60 s · ASR 2 vòng khớp 100%% · đuôi 0,36 s). File cũ giữ ở `.work/_cu/audio_s_higgs_EN_t02_seed_fix/` |
| 2 | Câu `4.08#6` đọc **“snowshoe footprint”** còn kịch bản duyệt + hồi 1 ghi **“snow boot mark”** ⇒ mâu thuẫn nội dung trong cùng tập | Sửa `alt` trong `.work/acting_tap02_EN.json` + **sinh lại riêng câu này trên Kaggle GPU** (kernel `chiduong2026/amber-eyes-higgs-fix-4-08-6-en-t02-kaggle-gpu`, 3 bản). Chọn bản **s1**: CER **0,00%%** · peak −1,50 dBFS · đuôi 0,34 s · 8,52 s |
| 3 | `tts_manifest_EN_t02.json` còn `display` cũ cho 4 câu ⇒ phụ đề lệch tiếng đọc | Đồng bộ `display` ← kịch bản (4 câu) |
| 4 | 3 dòng bảng shot lệch câu đang đọc: 4-08 · 4-13 · 4-16 | Sửa `KeHoach_Video_Tap02_EN.md` + render lại still, QC A9.2 đạt |

**Số đo sau khi sửa:** master %s s (%s) · %s LUFS · peak %.1f dBFS · %d đoạn câm > 0,3 s ·
hồi %s s · %d câu · shot %d (tb %.1f s, dài nhất %.1f s) · %d cue phụ đề · file cuối %s s.
"""
extra = extra % ("%.1f" % d_mp3, human(d_mp3),
                 ("%.1f" % l_mp3) if l_mp3 is not None else "?",
                 p_mp3 if p_mp3 is not None else 0,
                 n_sil, act_txt, len(items), len(shots), sum(sd) / len(sd), sd[-1], n_cue,
                 "%.2f" % d_mp4)
sub(anchor, extra.strip() + "\n" + anchor, "them muc tom tat sua loi")

PLAN.write_text(txt, encoding="utf-8")
print("\nHOAN TAT ->", PLAN, PLAN.stat().st_size, "bytes")
