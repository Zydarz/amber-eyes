# BÁO CÁO DỰNG TẬP 13 (VI / EN / JA) — 17/11/2026

Người dùng chốt: **hướng B** (không sinh lại audio) và **dựng luôn, không sinh lại ảnh**. Các điểm lệch luật dưới đây là do quyết định đó.

## Số đo (trên mp4 cuối)

| | VI | EN | JA |
|---|---|---|---|
| `timeline.total` | 1989,73 s | 1813,56 s | 2118,34 s |
| `picture.mp4` | 1989,70 s | 1813,53 s | 2118,33 s |
| mp4 cuối | 33:09,70 | 30:13,53 | 35:18,33 |
| LUFS / true peak | −16,3 / −1,8 dBFS | −16,3 / −1,8 | −16,3 / −1,8 |
| Giải mã | 0 lỗi | 0 lỗi | 0 lỗi |
| Khoảng câm > 0,3 s (−60 dB) | 0 | **1 (0,41 s, kết thúc ~161,5 s)** | 0 |
| Phụ đề (cue) | 517 | 516 | 452 |

Cổng sóng giọng H24 (trên stems xấp xỉ): ĐẠT cả 3 ngôn ngữ × 5 vai. Ảnh tĩnh: 645 ảnh render lại, 0 lỗi chữ chìm (H20).

## Điểm lệch luật (cần người dùng biết)

1. **Stems là xấp xỉ**: audio từng câu của Tập 13 không còn trên đĩa. `.work/_make_pseudo_stems_t13.py` cắt master mp3 theo cửa sổ [start,end] của từng vai (lẫn nhạc nền). A14 tầng 2 và `build_audio3.py` **không chạy được**.
2. **H22 ④ TRƯỢT** (EN/JA): `t13_unbound_hands_broken_heart` 30,15 s (EN) / 30,5 s (JA); `t13_tiger_parenting_immigrant_anxiety` 30,15 s (JA).
3. **H2: nền có chữ AI vẽ** trên giấy tờ giả (shot 1-15, 1-27, 1-29, 1-33…); mới soi 16/107 ô montage VI, các nền còn lại chưa soi.
4. **V4 EN**: khoảng câm 0,41 s quanh 161 s nằm sẵn trong master mp3 15/11.
5. **Mux**: `package.py --mux` lỗi vì thiếu `audio_master_*_t13.wav`; ghép thủ công từ master mp3 với `alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1`.
6. **mo_ta.txt VI dài 6.164 ký tự** (> 5.000 của YouTube) — sinh từ 07/11, chưa sửa.
7. Intro: chép `intro_kenh_EN.mov` → `intro_kenh_EN_t13.mov`, `intro_kenh_JA_t11.mov` → `intro_kenh_JA_t13.mov`.

Bản sao lưu trước khi chạy: `.work/_cu/t13_pre_package_20261117/` và `.work/_cu/t13_stills_20261114/`.
