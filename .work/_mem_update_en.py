import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
MEM = Path(r"C:\Users\ADMIN\.minimax\agents\mavis\memory\MEMORY.md")
t = MEM.read_text(encoding="utf-8")

OLD_HEAD = "### AMBER EYES — bản tiếng Anh Tập 02: trạng thái 24/10/2026 (dừng ở bước TTS, hết số dư gói)"
NEW_HEAD = "### AMBER EYES — bản tiếng Anh Tập 02: HOÀN TẤT 24/10/2026 ✅"
assert OLD_HEAD in t, "không tìm thấy mục cũ"
t = t.replace(OLD_HEAD, NEW_HEAD, 1)

# thay các dòng trạng thái cũ bằng kết quả thật
t = t.replace(
    "**⛔ BLOCKER:** API TTS trả **402 — hết số dư gói** (không retry được; `batch_text_to_audio` và `synthesize_speech` dùng chung hạn mức). Thiếu **18 câu vai D**: `4.08#9`, `4.10#1–10`, `5.08#1–7`.",
    "**BLOCKER ĐÃ GỠ:** API TTS trả 402 hết số dư gói giữa chừng → sau khi nạp tiền, đọc lại đúng 18 câu vai D (`4.08#9`, `4.10#1–10`, `5.08#1–7`) trong 64 s. G10 **ĐẠT: cả 5 vai đều 1 người**.", 1)
t = t.replace(
    "- 18 file còn thiếu đã **khôi phục tạm** từ `node_id` cũ (`.work/_restore_from_nodes.py`, dùng `mcode-tools get_asset_url`) ⇒ **âm thanh tạm đang lệch giọng ở 18 câu đó**, không được dùng để giao.",
    "- 18 file từng khôi phục tạm từ `node_id` cũ đã **dời sang `.work/audio_s_EN_t02/_dg_backup/`** (để `tts_sentences.py` không tưởng \"đã có\" mà bỏ qua) rồi đọc lại bằng giọng mới.", 1)
t = t.replace(
    "**SAU KHI NẠP TIỀN — chạy 1 lệnh:**\n`$env:AE_LANG='en'; $env:AE_EP='02'; py -3 .work/_finish_tap02_en.py`\n(TTS → G10 → build_audio3 → parse_shots → QC A9.2 → build_video3 6 worker ≈ 92 phút → subtitles → package → QC A9.1/A9.3/A9.4.)",
    "**THÀNH PHẨM (đã bàn giao):** `02_SAN_XUAT/Tap02_EN/xuat_ban/` — `Tap02_EN_master.mp4` (578.017.179 byte · **1723,5 s = 28:43,47** · 1920×1080@30 · 51.704 khung · H.264+AAC) · `Tap02_EN_master.mp3` (41.364.908 byte) · `Tap02_EN.srt` (425 cue) · `thumbnail.png` · `mo_ta.txt` + `description.txt` (mốc chương 00:00/00:20/05:06/09:30/16:06/22:39 + hotline Mỹ) · `nguon_tham_khao_EN.md` (khung, chưa có link).\n"
    "**QC A9.1–A9.4: TẤT CẢ ĐẠT (exit 0)** — lệch hình/tiếng **0,017 s** · giải mã mp4 0 lỗi · 0 khoảng câm > 0,3 s · loudness **−16,0 LUFS** · lời đầu 23,0 s · 151 khung giữa shot lấy từ mp4 thành phẩm → `.work/qc_final_EN_t02/`.\n"
    "Render 6 worker mất **3365 s (56 phút)** — nhanh hơn 92 phút của bản VN.\n"
    "**Chạy lại cả chuỗi:** `$env:AE_LANG='en'; $env:AE_EP='02'; py -3 .work/_finish_tap02_en.py`", 1)
t = t.replace(
    "- `build_audio3` EN đã chạy (bản tạm): **1735,0 s (28:54)**, 14 nền SFX + 37 SFX, lời đầu 23,0 s.",
    "- `build_audio3` EN: **1723,5 s (28:43)**, 14 nền SFX + 37 SFX, lời đầu 23,0 s.", 1)
t += """
### AMBER EYES — 2 lỗi tự vấp của tôi trong chuỗi EN Tập 02 (24/10/2026) — bài học
Type: technique

1. **`package.py` cần tham số `--mux`.** Không có `--mux` ⇒ chỉ sinh thumbnail + mô tả, **KHÔNG sinh mp4**,
   nhưng exit code vẫn 0 ⇒ chuỗi tưởng đã xong. Bản VN dùng `package.py --mux` (xem `.work/_finish_tap02.ps1`).
   ⇒ Khi viết script chạy nhiều bước, **kiểm tra file thành phẩm thực sự tồn tại**, không chỉ exit code.
2. **Xoá mp3 TTS rồi đọc lại là mất vĩnh viễn nếu hết số dư.** Lần này xoá 58 file vai D, đọc lại được 40
   thì hết quota ⇒ 18 file mất node_id (batch res_00–01 bị ghi đè bằng payload 402).
   ⇒ **Xoá file TTS chỉ khi chắc chắn còn quota**, và luôn lưu `node_id` (`.work/tts_s_*/res_*.json`).
3. **Render bản "tạm" rồi sửa audio là phí 56–92 phút.** Đã dừng đúng: chờ quota mở, đọc lại 18 câu,
   dựng âm thanh cuối, rồi mới render 1 lần.
"""
MEM.write_text(t, encoding="utf-8")
print("đã cập nhật MEMORY.md ·", MEM.stat().st_size, "byte")
