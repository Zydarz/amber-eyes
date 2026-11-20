# Báo cáo QC clip TikTok TK2 (Tập 01) — 20/11/2026

> Thành phẩm: `02_SAN_XUAT/TIKTOK/Tap01/clip02_TK2.mp4` (media → không commit, L10). Đo thật trên mp4 cuối.

## 0. Tóm tắt

| Hạng mục | Kết quả |
|---|---|
| File | 1080×1920 · 30 fps · H.264 + AAC · **27,22 MB** · **72,92 s** |
| Cổng QC | **13/14 ĐẠT — TRƯỢT cổng 13 (từ cấm V9: "bầm")** |
| Âm lượng | **−16,0 LUFS** · true peak **−4,4 dBFS** (đo trên mp4) |
| Khoảng câm / lệch AV / giải mã | 0 / 0,0000 s / 0 lỗi |
| Safe zone / tương phản | 0 vi phạm / thấp nhất 7,29 : 1 |
| G6 / H6 | phụ đề khớp 10/10 câu / hook là trích nguyên văn `TK2.01#1` |

## 1. Cổng trượt — cần người dùng quyết

`TK2.01#8` nói "…bàn tay mẹ sẽ siết chặt đến **bầm** tím". Từ "bầm" nằm trong danh sách V9 (A9.2). Audio giữ nguyên theo yêu cầu "dùng audio hiện tại", nên phụ đề (G6: nguyên văn lời đọc) cũng chứa từ này. Cụm có trong kịch bản gốc Tập 01 (dòng 229); `MoTa_Dai_TK2.txt` đã làm nhẹ thành "siết chặt hơn nữa" nên lời đọc và mô tả đang lệch nhau.
Hướng xử lý: (a) sinh lại riêng câu #8 với cụm nhẹ hơn rồi dựng lại; (b) chấp nhận rủi ro và đăng nguyên trạng.

## 2. Quyết định đã tự chọn (có thể đổi)

- **Hook:** spec ghi *"Vì sao cô ấy không bao giờ chạy trốn?"* nhưng câu này không nằm trong `TK2.01#1` ⇒ vi phạm H6. Đã dùng đoạn trích nguyên văn *"chưa từng một lần đứng bật dậy khỏi chiếc xe lăn"* (khoá `hook_render`/`hook_line` trong SPEC). Câu hỏi gốc vẫn ở caption.
- **SFX:** tiếng kim loại va chạm tự tổng hợp, đặt tại đầu câu `TK2.01#5` (khoá `sfx_clank_at`). Nền: `bgm_ambient_deep.mp3` (MiniMax).

## 3. Chưa kiểm được

| Cổng | Lý do |
|---|---|
| G10 nghe mù · G8 (câu #7–#8 `sad` vs #3–#6 neutral) | cần tai người |
| G12 CER < 2 % và G9 F0 cho audio TK2 | chưa chạy (CPU, ~20 phút/3 lượt) |
| Soi nền (H2) | `tk01_brain_desk` có chữ AI vẽ "DSM-5 MANUAL" và chữ nhỏ trên giấy/đơn thuốc; TK1 cũng dùng nền này. Nội dung đúng nhưng vi phạm tinh thần H5 |
| Thẻ overlay | thẻ #1–#2 che phần trên lồng chim (nền `cage`); chấp nhận được, chưa dời |

## 4. Thay đổi script (L8/L9)

`_build_tk01_audio.py`, `_build_tk01_video.py`, `_qc_tk01_clip.py` nay đọc biến `AE_CLIP` (mặc định TK1); hook, thẻ overlay, BGM, SFX lấy từ `SPEC_AUDIO_CLIP_TAP01.json`. **Hồi quy TK1:** audio trộn lại giống bản cũ **từng byte**; hook + thẻ overlay giống manifest cũ. Bản gốc script/spec: `.work/_cu/tk2_20261120/`.

Tái lập: `AE_CLIP=TK2 py -3 .work\_build_tk01_audio.py` → `_build_tk01_video.py` → ghép AAC 256 kbps → `_qc_tk01_clip.py`.
