# BÁO CÁO DỰNG LẠI TẬP 15 (VI / EN / JA) — 25/11/2026

Dựng theo H26 (khung không chữ, trừ thẻ kết và số T5), dùng bộ 150 ảnh nền mới (sinh 23/11), audio master cũ (16–17/11, không sinh lại giọng).

## Số đo (trên mp4)
| | VI | EN | JA |
|---|---|---|---|
| `Tap15*_master.mp4` | 731,8 MB | 716,2 MB | 846,8 MB |
| Thời lượng mp4 / `timeline.total` | 30:51,37 / 1851,37 s | 30:15,87 / 1815,89 s | 35:42,90 / 2142,91 s |
| LUFS · đỉnh | −16,0 · −1,9 dBFS | −16,0 · −1,7 dBFS | −16,0 · −1,6 dBFS |
| Giải mã | 0 lỗi | 0 lỗi | 0 lỗi |
| Dựng hình (`--workers 6`) | 63 phút | 37 phút | 46 phút |

- T20: master mp3 so `timeline.total` lệch 0,04 / 0,05 / 0,03 s (ĐẠT ≤ 0,05).
- Stems xấp xỉ (cắt từ master, `_make_pseudo_stems_t15.py`); `qc_wave_gate` ĐẠT 5 vai × 3 ngôn ngữ (chạm trần 1,8–3,4 %).
- Hash trước mux (T17): timeline VI a44a5342bcb6 · EN d219ea7afe3f · JA 6ea63dbf3a08 (18/11 14:47); shots VI 9eddcbb9bbc1 · EN 0a29c8fd8e29 · JA ef23141acdd3 (24/11 08:15).
- Log dựng: `.work/_t15/logs/build_all.log`. Khung QC: `.work/_t15/qc/`.

## Lệch luật / chưa đạt
- **H22:** VI trượt 1 nền (`t15_bystander_guilt_whispers_livingroom` 31 s), JA trượt 2 (34 s; `t15_jodi_arias_a3_09_rental_car` 31 s). EN đạt. Người dùng chấp nhận (24/11).
- **H27 `qc_bg_mapping.py 15` TRƯỢT:** M5 câu chưa phủ 220/220 · M4 prompt riêng 75/150. Người dùng chốt dùng bộ 150 ảnh. Mọi mã nền đều có file (M1 0/150 sai).
- **H26(a):** nền thẻ kết `t15_amber_eyes_closing_dossier_arias` có chữ AI vẽ méo ("AMBER CAES EYES DOSER") trên bìa sổ — VI/EN/JA dùng chung nền. Khung giữa VI (600 s) còn chữ AI méo trên chip nhớ và máy in. **Chưa soi hết 150 ảnh.**
- Đã bỏ qua bước 8 (ảnh tĩnh) theo yêu cầu người dùng 24/11; render ảnh tĩnh dừng giữa chừng (VI 225, EN 12, JA 0).
- Thẻ kết hiện đủ (khung ở 5 s sau đầu shot cuối: "HỒ SƠ TẬP 15 · ĐÃ ĐÓNG" + AMBER EYES + khẩu hiệu). Khung `total − 2 s` đã fade về đen, chỉ còn logo — đúng thiết kế fade của shot cuối, nhưng khác cách kiểm A11 #55. Chỉ soi VI, EN/JA chưa mở khung thẻ kết.

## Chưa làm
- Nghe duyệt giọng 3 ngôn ngữ; soi mắt video; bổ sung `nguon_tham_khao`; chưa chạy `subtitles.py`/`package.py` mô tả/thumbnail (tránh ghi đè SRT/mô tả).
- Chưa commit (media bị `.gitignore`).
