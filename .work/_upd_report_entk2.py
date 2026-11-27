# -*- coding: utf-8 -*-
"""Cap nhat BAO_CAO_QC_TIKTOK_TAP04.md sau khi dung lai EN TK2 (master moi 27/11).

Giu nguyen line-ending goc (LF) va so o cua tung bang.
"""
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
print("line-ending goc:", "CRLF" if nl == "\r\n" else "LF", "| so dong:", len(lines))

# ---------- 1. Tieu de ----------
lines[2] = ("*Ngày: 27/11/2026 (cập nhật sau khi dựng lại EN TK2) · 15 clip 9:16 (5 clip × 3 ngôn ngữ) "
            "· có logo kênh theo **H29***")
lines[4] = ("*Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 4 (Bước 4–7) · "
            "Luật logo: `AGENTS.md` H29 · A11 #198, #199, **#200** (ASR cửa sổ + nguồn mp3)*")

# ---------- 2. Bang tom tat ----------
for i, l in enumerate(lines):
    if l.startswith("| Thời lượng |"):
        lines[i] = ("| Thời lượng | **68,83 – 88,28 s** (mục tiêu 60–90 s · cổng QC 45–95 s) — 15/15 trong ngưỡng "
                    "|")
    if l.startswith("| Âm lượng trên mp4 cuối |"):
        lines[i] = ("| Âm lượng trên mp4 cuối | **−16,4 … −16,0 LUFS** (ngưỡng −16 ± 1) — 15/15 đạt · "
                    "true peak **−4,4 … −1,8 dBFS** (trần −1,5) — **14/15 đạt, EN TK2 trượt** |")
    if l.startswith("| Khoảng câm > 0,3 s @ −60 dB |"):
        lines[i] = ("| Khoảng câm > 0,3 s @ −60 dB | **0** trên 14 clip · **11 khoảng** trên EN TK2 "
                    "(master mới không có nhạc nền — mục 5.1) |")
    if l.startswith("| **Lỗi còn lại** |"):
        lines[i] = ("| **Lỗi còn lại** | **2 lỗi T13 (từ cấm) ở clip VN** · **1 lỗi T6 (khoảng câm) + "
                    "true peak vượt trần ở EN TK2** (mục 5.1) · từ cấm + BGM (mục 5.2, 5.3) |")

# ---------- 3. Bang ket qua do 15 clip ----------
for i, l in enumerate(lines):
    if l.startswith("| EN | TK2 |"):
        lines[i] = ("| EN | TK2 | 72,34 s | 25,6 | −16,3 | **−1,8** | **11** | ✓ | "
                    "**TRƯỢT T6** (11 khoảng câm) — audio mới (mục 5.1) |")

for i, l in enumerate(lines):
    if l.startswith("**Tổng: 13/15 clip đạt trọn"):
        lines[i] = ("**Tổng: 12/15 clip đạt trọn 14 cổng · 2 clip VN trượt cổng T13 (từ cấm) · "
                    "1 clip EN TK2 trượt cổng T6 (khoảng câm, do master audio mới) — lỗi kịch bản/audio, "
                    "không phải lỗi dựng.**")

# ---------- 4. Muc 5.1 thay bang bang do moi ----------
i51 = next(i for i, l in enumerate(lines) if l.startswith("### 5.1."))
i52 = next(i for i, l in enumerate(lines) if l.startswith("### 5.2."))

new51 = """### 5.1. EN TK2 — ĐÃ DỰNG LẠI (master mới 27/11) · còn 1 lỗi T6 + true peak vượt trần

**Bối cảnh:** bản cũ báo "thiếu 2 câu". Người dùng đã tạo lại `Tap04_EN/TK2_master_audio.mp3` (27/11/2026, 14:04) — **72,34 s** (bản cũ 70,90 s). Đo lại toàn bộ:

| Đo được | Kết quả |
|---|---|
| Số câu trong `SPEC_AUDIO_CLIP_TAP04.json` | **11** |
| Số câu thật sự có trong master mới | **11/11** — ASR căn cửa sổ 20,5 s: `#1`–`#10` khớp **100 %**, `#11` khớp **12/13 (92,3 %)** |
| Timeline dựng lại | `timeline_tk2.json` — **0 dòng NOI SUY, 0 dòng MATCH YEU**; `asr_end` 72,00 / audio 72,34 s |
| Clip render lại | `Tap04_EN/TK2_video.mp4` — 72,34 s · 1080×1920 · h264+aac @30,00 · **0 lỗi giải mã** · 11 shot đúng nền · logo (684, 60) |

**Nguyên nhân thật của lỗi "thiếu 2 câu" (không phải audio thiếu):**

| Kiểm chứng | Kết quả |
|---|---|
| ASR **cả file** mp3 mới (72,34 s) | chỉ trả về tới **57,72 s** ⇒ 2 câu cuối bị ghi "NOI SUY" |
| ASR **riêng đoạn đuôi** (58,2–72,3 s) | **nhận đủ cả 2 câu**, 100 % khớp |
| ASR **riêng đuôi WAV cũ** (50,9–70,9 s) | **nhận đủ cả 2 câu**: *"Through the lens of criminal psychology…"* 56,90–62,32 s và *"Episode 4 of Amber Eyes…"* 65,88–70,06 s ⇒ **bản WAV cũ CŨNG ĐỦ 11 câu** |
| Giải mã `s16le` vs `f32le` | `s16le` ⇒ whisper dừng ở **57,72 s**; `f32le` ⇒ tới 67,22 s (vẫn mất câu cuối) ⇒ lỗi ở **cách đọc file dài** |
| Cửa sổ 20,5 s (overlap 4 s, cửa sổ cuối neo vào cuối file) | **11/11 câu, asr_end 72,00/72,34 s** ⇒ cách sửa |

⇒ **Không phiên bản nào thiếu câu nào.** Lỗi là ASR bỏ đuôi file dài + builder đọc `.wav` (24/11) trong khi renderer đọc `.mp3` (27/11). Đã ghi **A11 #200** và sửa builder: đọc `.mp3` (đúng file renderer dùng), ASR theo cửa sổ, giải mã `f32le`, in cảnh báo khi wav/mp3 lệch > 0,05 s.

**Phủ đuôi kiểm cho cả 15 clip** (`.work/_check_tail_coverage.py`): `timeline_end` cách `speech_end` (RMS > −45 dBFS) **0,10 – 1,06 s** ⇒ **15/15 phủ đủ đuôi**, không clip nào khác bị mất câu.

**Lỗi CÒN LẠI trên master mới — cần người dùng quyết:**

| # | Lỗi | Đo được | Cổng vi phạm |
|---|---|---|---|
| 1 | **11 khoảng câm > 0,3 s** | 0,316 – 0,843 s tại 1,93 · 4,30 · 6,12 · 9,66 · 20,30 · 28,58 · 36,57 · 42,58 · 48,54 · 58,30 · 67,41 s | **T6 trượt** (cổng này đạt ở 14 clip còn lại) |
| 2 | **True peak vượt trần** | **+1,25 dBFS** (trần −1,5) · **312 mẫu > 0 dBFS** rải rác 29 đoạn · 380 mẫu > −0,1 dBFS | **A7 / trần TP** |
| 3 | **Master mới KHÔNG có nhạc nền** | nền im lặng trung bình **−70,6 dB** (14 clip khác: −16,2…−17,2 dB) · **8,1 % file là im lặng tuyệt đối** (peak < −100 dBFS; 14 clip khác: **0,00 %**) | Gốc rễ của lỗi #1 |
| 4 | **WAV cũ còn trên đĩa** | `TK2_master_audio.wav` = 70,90 s (24/11) — **lệch 1,44 s** với mp3 | Không ảnh hưởng dựng (builder đã đọc mp3) nhưng dễ nhầm |

**Vì sao không tự sửa:** (a) thêm nhạc nền / hạ đỉnh = **sửa audio** ⇒ cần người dùng duyệt; (b) `bgm_ambient_tension.mp3` **không còn trên đĩa** (mục 5.3) ⇒ không có nguồn để trộn; (c) WAV là file của người dùng.

**Cách khắc phục (đề xuất, chờ duyệt):** trộn lại nhạc nền có sẵn + `alimiter` (A11 #38: `limit=0.7943:attack=5:release=50:level=disabled:latency=1`) để peak ≤ −1,5 dBFS ⇒ xoá được cả 11 khoảng câm lẫn lỗi TP. Cần người dùng: **(1)** xác nhận nguồn nhạc nền được phép dùng, **(2)** cho phép trộn/ghi lại `TK2_master_audio.mp3`, **(3)** cho phép tạo lại `.wav` từ mp3 để hai bản đồng bộ.

"""
lines[i51:i52] = new51.rstrip("\n").split("\n")

# ---------- 5. Muc 6 viec con lai ----------
for i, l in enumerate(lines):
    if l.startswith("1. **Quyết định về EN TK2**"):
        lines[i] = ("1. **EN TK2 — đã dựng lại xong** (11/11 câu, 0 lỗi giải mã). Còn 2 lỗi audio trên master mới "
                    "(mục 5.1): **11 khoảng câm > 0,3 s (T6)** + **true peak +1,25 dBFS (vượt trần)** — "
                    "gốc rễ: master mới **không có nhạc nền**. Cần người dùng: xác nhận nguồn nhạc nền + cho phép "
                    "trộn lại/hạ đỉnh master + cho phép tạo lại `.wav` từ mp3.")

# ---------- 6. Muc 7 danh sach script ----------
for i, l in enumerate(lines):
    if l.startswith("`_audit_tk04_assets.py` (kiểm ảnh nền)"):
        lines[i] = ("`_audit_tk04_assets.py` (kiểm ảnh nền) · `_tk_asr_timeline_t04.py` (dựng timeline — **đã đổi sang "
                    "ASR cửa sổ + đọc mp3**, A11 #200) · `_build_tk_tap04_video_notext.py` (dựng clip + logo H29) · "
                    "`_audit_audio_tk04.py` (quét audio 15 master) · `_qc_tk_tap04_clip.py` (14 cổng T1–T14 + H26 + H29) · "
                    "`_check_tail_coverage.py` (kiểm phủ đuôi 15 clip) · `_clip_scan.py` (đếm mẫu clip) · "
                    "`_silence_scan_mp3.py` (đếm khoảng câm) · `_qc_tk04_frames/` (khung hình QC)")

P.write_text("\n".join(lines), encoding="utf-8", newline="")
print("da ghi", P)
print("so dong moi:", len(lines))
