# Báo cáo QC clip TikTok TK3 (Tập 01) — 20/11/2026

> Thành phẩm: `02_SAN_XUAT/TIKTOK/Tap01/clip03_TK3.mp4` (media → không commit, L10). Đo thật trên mp4 cuối.

## 0. Tóm tắt

| Hạng mục | Kết quả |
|---|---|
| File | 1080×1920 · 30 fps · H.264 + AAC · **26,71 MB** · **63,52 s** |
| Cổng QC | **14/14 ĐẠT** |
| Âm lượng | **−16,0 LUFS** · true peak **−4,2 dBFS** (đo trên mp4) |
| Khoảng câm / lệch AV / giải mã | 0 / 0,0000 s / 0 lỗi |
| Safe zone / tương phản | 0 vi phạm / thấp nhất 7,56 : 1 |
| V9 / G6 / H6 | 0 từ cấm / phụ đề khớp 10/10 câu / hook là trích nguyên văn `TK3.01#1` |

## 1. Quyết định đã tự chọn (có thể đổi)

- **Hook:** spec ghi *"Bà ta không cần tiền. Bà ta cần sự kính ngợng."* — câu này không có trong lời đọc ⇒ vi phạm H6. Dùng trích nguyên văn `TK3.01#1`: *"bà ta làm tất cả chỉ vì tiền trợ cấp"* (khoá `hook_render`/`hook_line`).
- **SFX:** nền phòng + **tiếng lật giấy tự tổng hợp** đặt đầu câu `TK3.01#4` (khoá `sfx_kind`/`sfx_at`). BGM `bgm_cello_sad.mp3` (MiniMax).

## 2. Soi nền (H1/H2)

- `tk01_spotlight_deedee`: có hình một người phụ nữ (nhân vật người thật) — **mặt chìm hoàn toàn** khi phóng to (đạt H1). Không vẽ nạn nhân.
- `tk01_records`, `tk01_house_night`, `tk01_brain_desk`: không thấy chữ đọc được ở khung phim (riêng `brain_desk` vẫn có chữ "DSM-5" trên sách — xem báo cáo TK2 mục 3).
- Nền `records` dùng 5/10 câu (không liền nhau); chấp nhận cho clip ngắn.

## 3. Lỗi chính tả trong kế hoạch/caption — cần người dùng xác nhận

"**kính ngợng**" xuất hiện trong `KE_HOACH_CLIP_TAP01.md` (dòng 40, 99, 288) và `MoTa_Dai_TK3.txt` dòng 1 — nhiều khả năng là "**kính ngưỡng**". Chưa sửa vì file người dùng đã duyệt; sửa trước khi đăng.

## 4. Chưa kiểm được

G10 nghe mù · G8 (câu #6 `sad`, #9 vai N1 `sad`) · **G12 CER < 2 % và G9 F0 cho audio TK3** (chưa chạy).

## 5. Script (L8/L9)

Thêm hàm `paper_flip` và khoá SPEC `sfx_kind`/`sfx_at` cho `_build_tk01_audio.py`. **Hồi quy:** audio TK2 trộn lại giống bản cũ từng byte (TK1 đã kiểm ở lượt trước, hàm TK1 không đổi). Bản sao lưu: `.work/_cu/tk3_20261120/`.

Tái lập: `AE_CLIP=TK3 py -3 .work\_build_tk01_audio.py` → `_build_tk01_video.py` → ghép AAC 256 kbps → `_qc_tk01_clip.py`.
