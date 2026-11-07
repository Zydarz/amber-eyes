# BÁO CÁO QC — TẬP 03 JA DỰNG LẠI THEO MASTER MỚI · 07/11/2026

**Thành phẩm:** `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp4` (644,3 MB)
**Nguồn:** `Tap03_JA_master.mp3` (06/11 07:16, 1929,43 s) · `timeline_s_JA_t03.json` sha `f4b7153e4f63` · `shots_JA_t03.json` sha `65d2c81219f5`

## Số đo (trên mp4 cuối)
| Mục | Giá trị | Chuẩn | |
|---|---|---|---|
| Thời lượng mp4 / timeline.total | 1929,400 / 1929,43 s (= `int(total×30)/30`, 57.882 khung) | ± 0,05 | ✅ |
| LUFS · true peak | −16,3 · **−2,7 dBFS** | −16 ± 1 · ≤ −1,5 | ✅ |
| Khoảng lặng > 0,3 s @ −60 dB · lỗi giải mã | 0 · 0 | 0 | ✅ |
| Lệch A/V (4 cửa sổ) | 0,0 ms | ≤ 20 ms | ✅ |
| Ảnh tĩnh ↔ khung trong mp4 | 110/110 · MAE TB 3,87 · max 5,42 | < 15 | ✅ |
| Mốc câu ↔ audio | ASR whisper small, 44 đoạn rải khắp tập: đầu câu lệch 0,0–0,2 s, đúng thứ tự · năng lượng: 207/218 onset ≥ 6 dB, 0 câu câm | — | ✅ |
| Bảng shot | 110 shot · 218/218 câu · liền mạch · cuối = 1929,43 s | — | ✅ |
| Ảnh tĩnh soi bằng mắt | 110/110 + 7 shot danh sách tại cuối shot | — | ✅ |
| Thẻ kết (1925 s) | có đủ chữ (事件ファイル 第03話 · 終結 / AMBER EYES / khẩu hiệu) | H12 | ✅ |
| Phụ đề | 436 cue · cue cuối 1920,43 s · 0 chồng | — | ✅ |

## Lỗi tìm ra và sửa
1. **Bảng shot lệch audio mới** (H14): lệch tới 2,4 s ⇒ `parse_shots` lại (0 khác biệt nội dung).
2. **Chữ trên hình ≠ lời đọc:** `2-07` (còn chữ của kịch bản cũ "海へ逃げた/庭に遺体を埋めた" ⇒ đổi chữ + nền `t3_car_door`), `4-07` (câu hiện trước lời), `2-02` ("道を尋ねる" sai nghĩa), lỗi chữ Trung `自行` `多次の` `渴`.
3. **Chữ dài xuống dòng:** `2-05` đè mục sau; `2-15`, `2-17` chữ mồ côi ⇒ rút ngắn, kiểm ở cuối shot.
4. Mux dùng `alimiter=0.63:latency=1,asoftclip=hard:0.63` (A11 #134) chạy ffmpeg trực tiếp.

## Cần người dùng quyết
- **Mô tả YouTube JA:** `xuat_ban/mo_ta.txt` và `description.txt` đã bị một tiến trình/session khác ghi lúc 12:15 và 12:57 (3.411 ký tự, **0/24 link nguồn** có trong mô tả; bản gốc tôi sao lưu 4.889 ký tự ở `.work/_cu/ja_t03_rebuild_20261107/`). Tôi chỉ đổi mốc chương `12:24 → 12:22`; bản `02_SAN_XUAT/Tap03_JA/mo_ta.txt` (thư mục cha) vẫn ghi `12:24`.
- **Lời đọc có lỗi dịch** (không sửa được nếu không đọc lại giọng): địa danh サンタ・クラルズ/クリアズ/クルーズ; chữ Trung "遇到的困難"; "フィルター" cho tem dán xe; "11年生"; "6英尺9インチ".
- Nghe duyệt audio, xem video.
- `edition.py` bị sửa lúc 12:21 trong khi đang render (chunk C khởi động sau đó); kết quả 110/110 khớp ảnh tĩnh cho thấy không ảnh hưởng hình, nhưng nên kiểm hash (T17).
