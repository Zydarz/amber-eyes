# -*- coding: utf-8 -*-
"""Cap nhat BAO_CAO_QC_TIKTOK_TAP04.md sau khi TRON LAI master EN TK2 (BGM + ambience, het loi T6/TP)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
P = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04" / "BAO_CAO_QC_TIKTOK_TAP04.md"

raw = P.read_text(encoding="utf-8")
nl = "\r\n" if "\r\n" in raw else "\n"
txt = raw.replace("\r\n", "\n")
lines = txt.split("\n")

lines[2] = ("*Ngày: 27/11/2026 (cập nhật lần 2 — sau khi **trộn lại master EN TK2**) · 15 clip 9:16 "
            "(5 clip × 3 ngôn ngữ) · có logo kênh theo **H29***")
lines[4] = ("*Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 4 (Bước 4–7) · Luật logo: `AGENTS.md` H29 · "
            "A11 #198, #199, #200, **#201** · Luật audio: `AGENTS.md` **H30, H31***")

for i, l in enumerate(lines):
    if l.startswith("| Âm lượng trên mp4 cuối |"):
        lines[i] = ("| Âm lượng trên mp4 cuối | **−16,4 … −16,0 LUFS** (ngưỡng −16 ± 1) — **15/15 đạt** · "
                    "true peak **−4,5 … −4,0 dBFS** (trần −1,5) — **15/15 đạt** |")
    if l.startswith("| Khoảng câm > 0,3 s @ −60 dB |"):
        lines[i] = ("| Khoảng câm > 0,3 s @ −60 dB | **0** trên cả **15/15 clip** (kể cả EN TK2 sau khi trộn lại master) |")
    if l.startswith("| **Lỗi còn lại** |"):
        lines[i] = ("| **Lỗi còn lại** | **2 lỗi T13 (từ cấm) ở clip VN** (lỗi kịch bản, cần duyệt) · "
                    "**T9/L7: nguồn nhạc nền của 14 clip còn lại không truy vết được** (mục 5.3) — "
                    "EN TK2 **đã hết lỗi audio** |")
    if l.startswith("| EN | TK2 |"):
        lines[i] = ("| EN | TK2 | 72,34 s | 25,6 | −16,3 | −4,5 | 0 | ✓ | **ĐẠT** (đã trộn lại master 27/11 — mục 5.1) |")
    if l.startswith("**Tổng: 12/15 clip đạt trọn"):
        lines[i] = ("**Tổng: 13/15 clip đạt trọn 14 cổng · 2 clip VN trượt cổng T13 (từ cấm `sát hại` — "
                    "lỗi có sẵn trong kịch bản, cần người dùng duyệt) · EN TK2 đã hết lỗi audio sau khi trộn lại master.**")

# --- muc 5.1: viet lai ---
i51 = next(i for i, l in enumerate(lines) if l.startswith("### 5.1."))
i52 = next(i for i, l in enumerate(lines) if l.startswith("### 5.2."))

new51 = """### 5.1. EN TK2 — ĐÃ TRỘN LẠI MASTER (27/11) · hết lỗi T6 + true peak

**Bối cảnh 2 vòng:** (1) bản cũ báo "thiếu 2 câu"; (2) master mới 27/11 của người dùng có **đủ 11/11 câu** nhưng **không có nhạc nền** ⇒ 11 khoảng câm + true peak vượt trần. Người dùng đã **cho phép trộn lại master** ⇒ đã trộn theo đúng công thức của dự án và dựng lại clip.

| Bước | Kết quả đo thật |
|---|---|
| Nguyên nhân "thiếu 2 câu" | **Không phải audio thiếu.** `faster-whisper` transcribe **cả file** 72,34 s chỉ trả về tới **57,72 s** ⇒ 2 câu cuối bị ghi "NOI SUY". ASR riêng đuôi (58,2–72,3 s) ⇒ **nhận đủ**; ASR riêng đuôi **WAV cũ 70,90 s** ⇒ **cũng đủ 11 câu** ⇒ *không phiên bản nào thiếu câu*. Giải mã `s16le` cắt sớm hơn `f32le` ⇒ lỗi ở **cách đọc file dài** |
| Cách sửa ASR | **Cửa sổ 20,5 s** (overlap 4 s, cửa sổ cuối neo vào cuối file) + khử trùng (text, mốc) < 0,6 s ⇒ **11/11 câu khớp 100 %**, `asr_end` 72,00/72,34 s |
| Vì sao phải trộn lại | Master mới: **nền im lặng −70,6 dB**, **8,1 % file là im lặng tuyệt đối** (14 clip khác: 0,00 % / −16…−17 dB) ⇒ **không có bed nhạc nền** ⇒ 11 khoảng câm > 0,3 s (**trượt T6**) · peak **+1,25 dBFS**, **312 mẫu > 0 dBFS** (**vượt trần A7**) |
| Công thức trộn (giống Tập 03) | voice + BGM `bgm_ambient_deep.mp3` **ducking** (−24 dB khi nói / −16 dB khi nghỉ, smooth 0,2 s) + **ambience phòng kín −42 dB** ⇒ đạt A1/V4 · fade cuối 0,8 s · **loudnorm 2 lượt** I −16 / TP −1,5 / LRA 11 |
| Headroom (bắt buộc) | voice hạ về peak **−6 dBFS**, raw mix về **−3 dBFS** trước khi ghi WAV 16-bit. Nếu không: WAV clip cứng ⇒ `measured_TP` sai ⇒ **loudnorm cho kết quả sai** (đo được: peak +19,49 dBFS ⇒ TP **−12,11 dBFS** thay vì −4,5) |
| **Master sau khi trộn** | **72,34 s · 0 khoảng câm > 0,3 s @ −60 dB · 0 mẫu > 0 dBFS · peak −1,47 dBFS · I −16,0 LUFS · TP −4,48 dBFS** — đạt trọn |
| Clip sau khi dựng lại | `Tap04_EN/TK2_video.mp4` — 72,34 s · 1080×1920 · h264+aac @30,00 · **0 lỗi giải mã** · 11 shot đúng nền · logo (684, 60) · **QC 14 cổng ĐẠT** |
| Phủ đuôi 15 clip | `timeline_end` cách `speech_end` (RMS > −45 dBFS) **0,10 – 1,06 s** ⇒ **15/15 phủ đủ đuôi** |

**Một bài học phát sinh lúc trộn (đã ghi A11 #201 + H31):** chạy ASR trên **master đã trộn BGM** ⇒ **9/11 dòng lỗi** (2 `NOI SUY`, 6 `MATCH YEU`, `asr_end` 68,48/72,34 s) dù audio hoàn toàn đúng ⇒ nghi nhầm "sai timeline". Chạy lại trên **voice stem** (file giọng thuần, lưu riêng `TK2_voice_stem.mp3`) ⇒ **11/11 câu khớp 100 %**. Vì trộn không dịch/lùi voice ⇒ **mốc thời gian không đổi**, chỉ cần trỏ ASR sang stem.

**Chọn BGM:** SPEC yêu cầu `bgm_jazz_noir.mp3` — **file không còn trên đĩa** (đã xoá ở đợt dọn media). Chọn `bgm_ambient_deep.mp3`: có trên đĩa + có dòng provenance đầy đủ (MiniMax) + **là bed mà clip TK2 của Tập 03 cũng dùng** (tiền lệ trong dự án) + tông noir hợp Act 1. ⇒ **EN TK2 có nguồn nhạc nền truy vết được** (khác 14 clip còn lại — mục 5.3).

**Còn lại:** master gốc + WAV cũ lưu ở `.work/_cu/entk2_master_premix_20261127_1517/` (không xoá).

"""
lines[i51:i52] = new51.rstrip("\n").split("\n")

# --- muc 5.3 #1: cap nhat ---
for i, l in enumerate(lines):
    if l.startswith("| 1 | **Nhạc nền không truy vết được**"):
        lines[i] = ("| 1 | **Nhạc nền không truy vết được (14/15 clip)** | `SPEC_AUDIO_CLIP_TAP04.json` ghi "
                    "`bgm_ambient_tension.mp3` (TK1) / `bgm_jazz_noir.mp3` (TK2) / `bgm_sub_drone.mp3` (TK3) / "
                    "`bgm_ambient_deep.mp3` (TK4) / `bgm_piano_warm.mp3` (TK5) — **`bgm_ambient_tension.mp3` và "
                    "`bgm_jazz_noir.mp3` KHÔNG còn trên đĩa** (đã bị xoá ở đợt dọn media). Đối chiếu 3 cách "
                    "(tương quan envelope · tương quan envelope toàn bộ khoảng nghi · **cross-correlation sóng thô** có bù lag) "
                    "với 11 BGM còn lại trong `assets/bgm/`: **không ứng viên nào khớp** (|corr| tối đa 0,72 ở cổng khác, "
                    "0,02–0,20 ở đúng clip) ⇒ bed là BGM MiniMax đã mất file nguồn. **EN TK2 (TK2.01) đã dùng lại "
                    "`bgm_ambient_deep.mp3` ⇒ nguồn truy vết được** | **Vi phạm T9/L7** cho 14 clip còn lại — không chứng minh "
                    "được nguồn âm thanh. Cần user xác nhận: bed là BGM MiniMax (đã kiểm tra thương mại) không, và có cho phép "
                    "đăng TikTok không |")

# --- muc 6 ---
for i, l in enumerate(lines):
    if l.startswith("1. **EN TK2 — đã dựng lại xong**"):
        lines[i] = ("1. **EN TK2 — ĐÃ XONG** (trộn lại master + dựng lại clip + QC 14 cổng ĐẠT). Còn 2 việc nhỏ: "
                    "**(a)** xác nhận `bgm_ambient_deep.mp3` (MiniMax) là bed được phép dùng cho TikTok — **EN TK2 dùng file này**; "
                    "**(b)** cho phép tạo lại `.wav` từ mp3 — **đã làm** (wav/mp3 hiện đồng bộ 72,34 s).")

# --- muc 7 script ---
for i, l in enumerate(lines):
    if l.startswith("`_audit_tk04_assets.py` (kiểm ảnh nền)"):
        lines[i] = ("`_audit_tk04_assets.py` (kiểm ảnh nền) · `_tk_asr_timeline_t04.py` (dựng timeline — **ASR cửa sổ + đọc mp3 + "
                    "`--audio` trỏ voice stem**, A11 #200/#201) · `_build_tk_tap04_video_notext.py` (dựng clip + logo H29) · "
                    "`_remix_entk2.py` (**trộn lại master**: voice + BGM ducking + ambience + loudnorm 2 lượt) · "
                    "`_audit_audio_tk04.py` (quét audio 15 master) · `_qc_tk_tap04_clip.py` (14 cổng T1–T14 + H26 + H29) · "
                    "`_check_tail_coverage.py` (kiểm phủ đuôi 15 clip) · `_clip_scan.py` (đếm mẫu clip) · "
                    "`_silence_scan_mp3.py` (đếm khoảng câm) · `_identify_bed.py` / `_match_bed_full.py` / `_match_bed_wave.py` "
                    "(truy vết bed) · `_qc_tk04_frames/` (khung hình QC)")

P.write_text("\n".join(lines), encoding="utf-8", newline="")
print("da ghi", P, "| so dong:", len(lines))
