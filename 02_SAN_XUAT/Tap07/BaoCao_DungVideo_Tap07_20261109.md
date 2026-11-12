# Báo cáo dựng video Tập 07 (VI · EN · JA) — 09/11/2026

Kịch bản **219 câu** (người dùng xác nhận). Âm thanh: master mp3 mới 09/11/2026 08:05. Timeline **đo bằng ASR** từ chính master (không dùng bản ước lượng cũ, T20). Bản ước lượng cũ lưu ở `.work/_cu/t07_tl_est_20261109/`; shots cũ ở `.work/_cu/t07_shots_est_20261109/`; mô tả/nguồn cũ ở `.work/_cu/t07_pkg_20261109/`.

## Số đo

| | VI | EN | JA |
|---|---|---|---|
| Master mp3 = timeline.total = picture.mp4 (s) | 1874,40 | 1731,38 / 1731,37 | 2035,97 |
| Mp4 thành phẩm | 31:14,40 | 28:51,37 | 33:55,97 |
| Giải mã lỗi | 0 | 0 | 0 |
| LUFS (mp4) | −16,2 | −16,3 | −16,3 |
| True peak (dBFS) | −1,6 | −1,7 | −1,9 |
| Khoảng câm > 0,3 s @ −60 dB | 0 | 0 | 0 |
| Câu 219/219 nằm đúng shot đang hiện (giữa câu) | 219 | 219 | 219 |
| Hở giữa shot / shot phủ 100% không lặp | 0 / đạt | 0 / đạt | 0 / đạt |
| Phụ đề (cue) · chồng lấn · vượt total | 497 · 0 · 0 | 492 · 0 · 0 | 444 · 0 · 0 |
| Lời đầu | 23,0 s | 23,0 s | 23,0 s |

Soi mắt 12 khung/ngôn ngữ trích từ mp4 thành phẩm: chữ trên hình = câu đang đọc, thẻ vai đúng, nền đúng cảnh.

## Lệch tiêu chuẩn / chưa đạt (nói thẳng)

1. **Thẻ kết mờ về đen từ ~`total−9 s`, đen hẳn ở `total−6 s`** (renderer fade từ start+4 s). Cổng H14 theo chữ ("thấy thẻ kết ở total−2 s") **không đạt**; thẻ hiện rõ ở `total−12 s`. Cần người dùng quyết: chấp nhận hay sửa renderer (script dùng chung, L8/L9).
2. **Mô tả VI `xuat_ban/mo_ta.txt` dài 5232 ký tự > 5000** (T15) — phải rút gọn `02_SAN_XUAT/Tap07/nguon_mo_ta.txt`.
3. **EN: chưa sinh lại mô tả** vì thiếu `02_SAN_XUAT/Tap07_EN/CHU_CO_DINH_EN.md` (mô tả EN cũ 07/11 vẫn là bản 147 câu). Mux/thumbnail EN đã xong.
4. `nguon_tham_khao.md` + mô tả còn viết cho bản cũ ở thư mục tập → người dùng rà lại nguồn.
5. Shot VI `5-33` 15,12 s (> 15 s, H10); EN `1-01` 1,26 s (< 3 s).
6. Khung `3.06#7` (cả 3 ngôn ngữ) có nhãn "HOST" mờ chồng góc phải bên cạnh thẻ vai đang nói — chưa tra nguyên nhân (nghi hiệu ứng handoff của shot).
7. **Script dùng chung bị session khác sửa giữa chừng**: `build_video3.py` (21:32) và `edition.py` (21:40) mới hơn lần dựng VI (18:54–19:31); EN/JA dựng sau đó. Chưa kiểm hồi quy VI↔EN/JA; khung lấy mẫu của 3 ngôn ngữ giống nhau về bố cục.
8. Render EN/JA bị chết 3 lần (20:07, 20:44, 20:55); hai script chạy nền bị đổi tên `.disabled` bởi tác nhân ngoài; chưa rõ nguyên nhân. Lượt cuối chạy bằng python tuyệt đối thành công.
9. Mux dùng WAV tạo từ chính master mp3 (`.work/audio_master_*_t07.wav`, 48 kHz) vì `package.py` đòi file wav.

## Hash lúc mux (T17)

| File | SHA-256 (12) | mtime |
|---|---|---|
| .work/timeline_s_t07.json | 87b676bc0b7c | 11-09 18:48 |
| .work/timeline_s_EN_t07.json | a22a4b132a0a | 11-09 18:48 |
| .work/timeline_s_JA_t07.json | ac2104714820 | 11-09 18:49 |
| .work/shots_t07.json | 5c65dde04657 | 11-09 18:49 |
| .work/shots_EN_t07.json | a3c71522bde6 | 11-09 18:49 |
| .work/shots_JA_t07.json | acdcfd8df64d | 11-09 18:49 |
| .work/build_video3.py | 1ff6f364e5c3 | 11-09 21:32 |
| .work/edition.py | 3c9bf6a27448 | 11-09 21:40 |
| .work/package.py | 2ce3932d56ca | 11-05 14:04 |
| .work/subtitles.py | 3d8a1b9146aa | 11-06 17:36 |

## Việc người dùng cần làm
- Nghe duyệt 3 bản (giọng, nhịp, khớp hình).
- Quyết định thẻ kết (mục 1) và rút gọn mô tả VI (mục 2).
- Cung cấp/xác nhận template `CHU_CO_DINH_EN.md` cho EN (mục 3).
- Rà `nguon_tham_khao` theo bản 219 câu (mục 4).
- Không commit media (L10).
