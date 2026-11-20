# Báo cáo QC clip TikTok TK4 (Tập 01) — 20/11/2026

> Thành phẩm: `02_SAN_XUAT/TIKTOK/Tap01/clip04_TK4.mp4` (media → không commit, L10). Đo thật trên mp4 cuối.

## 0. Tóm tắt

| Hạng mục | Kết quả |
|---|---|
| File | 1080×1920 · 30 fps · H.264 + AAC · **~26,9 MB** · **69,63 s** |
| Cổng QC | **14/14 ĐẠT** (+ cổng mới 11b: thiếu glyph = 0) |
| Âm lượng | **−16,1 LUFS** · true peak **−3,8 dBFS** (đo trên mp4) |
| Khoảng câm / lệch AV / giải mã | 0 / 0,0000 s / 0 lỗi |
| Safe zone / tương phản | 0 vi phạm / thấp nhất 7,52 : 1 |
| V9 / G6 / H6 | 0 từ cấm / phụ đề khớp 8/8 câu / hook là trích nguyên văn `TK4.01#1` |

## 1. LỖI ĐÃ BẮT VÀ SỬA — ký tự ①②③④ hiện thành ô vuông

Bản dựng đầu tiên của TK4 đạt 14/14 cổng nhưng **cả 4 thẻ overlay hiện "▯" thay cho ①②③④**. Nguyên nhân: font Segoe UI Bold **không có glyph** U+2460–2463 (đo: render trùng ô `.notdef`); Pillow không báo lỗi. Cổng QC cũ đo chữ trên mask nên **không phát hiện** — chỉ lộ khi soi khung hình bằng mắt.

- **Sửa:** `_build_tk01_video.py` vẽ ký tự khoanh tròn đầu dòng bằng `seguisym.ttf` (có glyph), phần chữ còn lại giữ Bold.
- **Cổng mới 11b** trong `_qc_tk01_clip.py`: mọi ký tự trên hình phải có glyph thật trong font dùng để vẽ. Đã chạy lại cho cả 4 clip: **0 ký tự thiếu glyph** (TK1 có "≠", TK2 có “ ”, TK3 có "≠" — đều có glyph).
- Bản lỗi lưu ở `.work/_cu/tk4_20261120/clip04_TK4_tofu_OLD.mp4` (L5).
- **Bài học:** cổng xanh không thay được soi mắt các thẻ có ký tự đặc biệt (H7/H20).

## 2. Quyết định đã tự chọn (có thể đổi)

- **Hook:** spec ghi *"4 dấu hiệu đỏ sinh tồn — lưu lại clip này."* không có trong lời đọc ⇒ vi phạm H6. Dùng trích `TK4.01#1`: *"Bốn dấu hiệu đỏ để nhận ra một đứa trẻ đang bị bệnh"*.
- **SFX:** nền phòng + **tiếng gõ cửa tự tổng hợp** (3 cú) đầu câu `TK4.01#6` (khoá `sfx_kind`=`knock`, `sfx_at`). BGM `bgm_piano_minimal.mp3` (MiniMax).
- Thẻ ② dài 3 dòng, nằm trong khung thẻ và safe zone.

## 3. Soi nền (H1/H2)

6 nền soi ở khung phim: không thấy chữ đọc được (bảng ghim `pinboard` chỉ có giấy ghi chú không chữ). `two_shadows` và `crowd_away` là bóng người, không lộ mặt. Không có nạn nhân.

## 4. Chưa kiểm được

G10 nghe mù · G8 · **G12 CER < 2 % và G9 F0 cho audio TK4** (chưa chạy).

## 5. Script (L8/L9)

Thêm `door_knock` + khoá SPEC; sửa font số khoanh tròn; thêm cổng 11b; QC đọc được manifest TK1 cũ. **Hồi quy:** audio TK2 và TK3 trộn lại giống bản cũ từng byte; TK1 hook + thẻ overlay giống manifest cũ; **TK1 QC chạy lại 14/14 với số đo trùng báo cáo cũ** (7,11 : 1; −1,6 dBFS; 12/12 câu). Bản sao lưu: `.work/_cu/tk4_20261120/`.

Tái lập: `AE_CLIP=TK4 py -3 .work\_build_tk01_audio.py` → `_build_tk01_video.py` → ghép AAC 256 kbps → `_qc_tk01_clip.py`.
