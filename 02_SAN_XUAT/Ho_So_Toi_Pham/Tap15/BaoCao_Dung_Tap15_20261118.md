# BÁO CÁO DỰNG TẬP 15 (VI / EN / JA) — 18/11/2026

## Thành phẩm (đã đo trên mp4)
| | VI | EN | JA |
|---|---|---|---|
| File | `Tap15/xuat_ban/Tap15_master.mp4` | `Tap15_EN/xuat_ban/Tap15_EN_master.mp4` | `Tap15_JA/xuat_ban/Tap15_JA_master.mp4` |
| Thời lượng mp4 / `timeline.total` | 30:51,37 / 1851,37 s | 30:15,87 / 1815,89 s | 35:42,90 / 2142,91 s |
| LUFS · đỉnh | −16,0 · −1,9 dBFS | −16,0 · −1,7 dBFS | −16,0 · −1,6 dBFS |
| Giải mã | 0 lỗi | 0 lỗi | 0 lỗi |
| Thẻ vai / thẻ kết | thấy | thấy | thấy |

## Việc đã làm
- **T20 (timeline ước lượng):** `timeline_s*_t15.json` cũ lệch master −34,8 / +16,7 / +20,3 s. Dựng lại từ SRT của master (`.work/_rebuild_timeline_t15.py`): 0 câu lệch chữ, `total` = thời lượng master. Bản cũ ở `.work/_cu/t15_pre_build_20261118/`.
- **Audio gốc từng câu và stems đã mất** ⇒ stems là **xấp xỉ**, cắt từ master theo timeline (`.work/_make_pseudo_stems_t15.py`, như Tập 13/14). Chỉ ảnh hưởng thanh sóng badge. Cổng đo trên master: nhịp nghỉ trung vị 0,75 s, 0% < 0,4 s (ĐẠT) · `qc_voice_gap` ĐẠT · `qc_wave_gate` ĐẠT 5 vai × 3 ngôn ngữ · V4: VI còn 1 khoảng câm 0,34 s ở 601,6 s (giữa 2.07#5 và 2.07#6).
- **Ảnh:** đưa 67 ảnh `t15_bNN_*` vào bảng shot cả 3 ngôn ngữ (85 shot đổi nền). H22: VI trượt 1 nền (31 s), JA trượt 2 nền (31 s, 34 s), EN đạt. `qc_bg_shared` ĐẠT. Chữ chìm 0/675 ảnh. Soi mắt VI 60 · EN 67 · JA 39 shot.
- **Sửa bảng shot:** số cờ T8 lệch một bậc ⇒ 5-22→01, 5-25→02, 5-29→03, 5-31→04, 5-18 về T1; tắt bán thân ở shot T8; hoán nền 5-18 ↔ 5-22.
- **Sửa renderer cấu hình T15:** `intro_card_pos [960, 90]` (thẻ giới thiệu vai đè chữ T1 ở shot 1-01, A11 #142). Phải dựng lại cả 3 ngôn ngữ.
- Mux chỉ gọi `package.mux()`; **không** chạy `subtitles.py`/CLI `package.py` (tránh ghi đè SRT, thumbnail, mô tả).

## Lệch luật / người dùng đã chấp nhận
- **H2/H1:** người dùng duyệt dùng ảnh hiện tại dù còn: chữ AI méo (b13 bảng trắng `4-38`, b45/b47 bản đồ `2-34/2-38`, b44 tờ báo, b53 biển đỏ, b26 nhãn), b67 mặt người rõ nét (`3-09/3-10`), b47 hình người nằm dưới sàn (`2-34`). Nghi chữ/biển: b25, b29, b43, b64, b65 (chưa mở full-res).
- Caption `4-39`, `4-44`, `4-45` bị cán cân che một phần; JA thẻ kết ngắt dòng "第1 / 5話".
- Cổng H22 còn trượt VI/JA như trên (vượt 1–4 s).

## Chưa làm / người dùng cần làm
- Nghe duyệt giọng 3 ngôn ngữ (AI chưa nghe được); bổ sung `nguon_tham_khao`; kiểm thumbnail và mô tả.
- Chưa chạy `package.py` cho mô tả/thumbnail; chưa commit (media đã bị `.gitignore`).

## Thumbnail (19/11/2026)
- Khai `thumb_bg` = `t15_b01_two_guilt_polarities_scales` trong `edition.py` (trước đó tập 15 rơi về nền Tập 01 `house_police`, lỗi H11). Chữ: VI "CƠN CUỒNG GHEN / RANH GIỚI" · EN "BORDERLINE RAGE / FATAL OBSESSION" · JA "境界の狂気 / 執着の果て".
- Sinh bằng `package.thumbnail()` trực tiếp (không chạy CLI để khỏi ghi đè mô tả/nguồn): `Tap15*/xuat_ban/thumbnail.png`, 1280x720. Chưa kiểm bằng trình đăng YouTube.
