import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
MEM = Path(r"C:\Users\ADMIN\.minimax\agents\mavis\memory\MEMORY.md")
text = """
### AMBER EYES — bản tiếng Anh Tập 02: trạng thái 24/10/2026 (dừng ở bước TTS, hết số dư gói)
Type: project

**ĐÃ XONG (bản EN Tập 02):**
- Bảng shot EN `02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md` — 151 dòng, tự kiểm **151/151 đạt** (`.work/_build_plan_tap02_en.py`). 1 sửa nội dung: on-screen `2-11` "WOMEN'S UNDERWEAR AND PERSONAL BELONGINGS" → **"WOMEN'S PERSONAL BELONGINGS"** (khớp đúng chữ bản VN "ĐỒ RIÊNG TƯ CỦA PHỤ NỮ", tránh từ nhạy cảm YouTube).
- `edition.py`: `EPISODES["02"]` có nhánh EN (`AE_LANG=en AE_EP=02` → hậu tố `_EN_t02`, thư mục `Tap02_EN`, master `Tap02_EN_master`, srt `Tap02_EN.srt`, act_titles/badge/thẻ cảnh báo EN, title + thumbnail EN).
- `acting_tap02_EN.json` — 215 câu (`.work/make_acting_tap02_en.py`): 4 cảm xúc an toàn, **cao độ = 0**, 6 bậc tốc độ (bậc lớn nhất 29% — bản VN dồn 51%), 9 lời đọc riêng (chỉ thêm `<#0.35#>` sau `:` đứng trước câu trích), 70 khoảng lặng / 27,2 s y hệt bản VN.
- Intro EN riêng `assets/brand/intro_kenh_EN_t02.mov` — thẻ A "ABOUT THIS DOCUMENTARY" + thẻ B "VIEWER DISCRETION & ADVISORY" đúng `CHU_CO_DINH_EN.md` §2. `make_intro.py` đã sửa để **tự xuống dòng** (chữ dài hơn bản Tập 01) + nhận `ED.EP["card_geom"]`; mặc định giữ nguyên hành vi cũ.
- `thumbnail.png` (THE TWO-FACED / COLONEL) ✅ · `nguon_tham_khao_EN.md` (khung, chưa có link) ✅ · `package.py` sửa: `description_en()` đọc khối ``` có "CHAPTERS" (bất kỳ § nào), giữ nhãn chương của tài liệu + thay mốc đo thực tế, tự sinh khung nguồn, ghi cả `description.txt` lẫn `mo_ta.txt`.
- **QC A9.2 bản EN: EXIT=0, đạt toàn bộ** (`.work/_qc_tap02_shots.py` đã sửa cho EN: số thứ tự viết bằng chữ "Red flag number one/two/…", danh sách từ cấm EN).
- `build_audio3` EN đã chạy (bản tạm): **1735,0 s (28:54)**, 14 nền SFX + 37 SFX, lời đầu 23,0 s.

**⛔ BLOCKER:** API TTS trả **402 — hết số dư gói** (không retry được; `batch_text_to_audio` và `synthesize_speech` dùng chung hạn mức). Thiếu **18 câu vai D**: `4.08#9`, `4.10#1–10`, `5.08#1–7`.
- Lý do đổi giọng vai D: `English_Deep-VoicedGentleman` (giọng D của Tập 01 EN) **đổi danh tính theo CẢM XÚC** (sad/fearful) → G10 báo "3 người". Đã đổi sang **`English_Trustworth_Man`** (SPEAKERS: 1 ở cả 4 cảm xúc) — đã đọc lại 40 câu, còn thiếu 18 câu nêu trên.
- 18 file còn thiếu đã **khôi phục tạm** từ `node_id` cũ (`.work/_restore_from_nodes.py`, dùng `mcode-tools get_asset_url`) ⇒ **âm thanh tạm đang lệch giọng ở 18 câu đó**, không được dùng để giao.

**SAU KHI NẠP TIỀN — chạy 1 lệnh:**
`$env:AE_LANG='en'; $env:AE_EP='02'; py -3 .work/_finish_tap02_en.py`
(TTS → G10 → build_audio3 → parse_shots → QC A9.2 → build_video3 6 worker ≈ 92 phút → subtitles → package → QC A9.1/A9.3/A9.4.)

**BẪY đã mắc:** xoá mp3 cũ rồi đọc lại ⇒ hết số dư là mất file ⇒ **luôn giữ `node_id` trong `.work/tts_s_EN_t02/res_*.json`** và có script khôi phục.
"""
with MEM.open("a", encoding="utf-8") as f:
    f.write(text)
print("đã ghi vào", MEM, "·", MEM.stat().st_size, "byte")
