# BÁO CÁO DỰNG TẬP 16 (VI / EN / JA) — 19/11/2026

## Thành phẩm (đã đo trên mp4)
| | VI | EN | JA |
|---|---|---|---|
| File | `Tap16/xuat_ban/Tap16_master.mp4` | `Tap16_EN/xuat_ban/Tap16_EN_master.mp4` | `Tap16_JA/xuat_ban/Tap16_JA_master.mp4` |
| mp4 / `timeline.total` | 42:46,00 / 2566,01 s | 39:44,20 / 2384,21 s | 47:10,10 / 2830,13 s |
| picture.mp4 lệch timeline | −0,01 s | −0,01 s | khớp (3 part 15:43,37) |
| LUFS · true peak | −16,0 · −3,6 dBFS | −16,0 · −1,7 dBFS | −16,0 · −3,3 dBFS |
| Giải mã | 0 lỗi | 0 lỗi | 0 lỗi |
| Thẻ kết | thấy | thấy | thấy (ngắt "第1/6話") |

## Việc đã làm
- Bảng shot sinh bằng `.work/_gen_shots_t16.py` (262 shot/ngôn ngữ: 257 câu + 4 thẻ hồi + thẻ kết), chèn vào mục 6 của 3 file `KeHoach_Video_Tap16*.md`. Bản gốc: `.work/_cu/t16_pre_build_20261118/`. `qc_bg_shared` ĐẠT (95 nền).
- Timeline khớp master (T20 ĐẠT). Nhịp nghỉ trung vị 0,95 s, 0% < 0,4 s. `qc_wave_gate` ĐẠT 5 vai × 3 ngôn ngữ. `qc_voice_gap`: ①② = 0, ③ TRƯỢT vì stems là **xấp xỉ** cắt từ master (`.work/_make_pseudo_stems_t16.py`) — audio gốc từng câu đã mất.
- Ảnh tĩnh 786/786, `qc_contrast_t16.py`: 0 chữ chìm.
- `edition.py` EPISODES["16"]: thêm `mux_af` (limiter −4 dBFS cho VI/JA, −2 dBFS cho EN, đều `latency=1`).
- JA: `part_00.mp4` bị hỏng (NAL không hợp lệ) ⇒ dựng lại đúng part đó (`.work/_rerender_part0_t16_ja.py`), bản hỏng ở `.work/_cu/t16_ja_part00_corrupt/`. Sao `intro_kenh_JA_t15.mov` → `intro_kenh_JA_t16.mov` (các intro JA giống byte).
- Mux chỉ gọi `package.mux()`; **không** chạy `subtitles.py`/CLI `package.py`.

## Lệch luật / người dùng đã chấp nhận ("dựng ngay")
- **Ảnh:** bỏ 31 gradient (24/10) và 22 ảnh phố Westfield lặp (H19) — chưa gỡ khỏi `bg_jobs_tap16.json`/`provenance.json`. Còn 95 nền cho 262 shot.
- **H22 TRƯỢT** cả 3 ngôn ngữ: nhiều nền dùng 3–4 shot, tối đa 46 s (JA, `john_list_a4_12_mansion`).
- **H1/H2:** vẫn dùng ảnh có mặt người thật rõ nét (`a2_c05`, `a2_c08`, `a3_c02`, `a4_c01/c03/c04/c05`, `a5_c02`, tượng sáp Bender) và chữ AI méo (`a2_c08`, `a2_c10`, `a3_c10`, `a4_c08`, `a5_c01`, `a5_c07`, banner 4 cờ, thẻ forensic…).
- **Soi mắt:** chỉ soi 14 shot đặc biệt (thẻ vai, 4 cờ T8, thẻ hồi, thẻ kết) ở VI và JA. **Chưa soi** 140/134/73 shot rủi ro (VI/EN/JA) theo `qc_eyeball_list`; EN mới soi gián tiếp.
- Thẻ hồi 4 JA ngắt "Most Want/ed".
- Mốc thời lượng shot: một số shot > 15 s (VI 17,8 s · EN 16,0 s · JA 20,0 s) — chưa đo H10 bằng script.
- Chưa trích 3 khung liên tiếp từ mp4 để xác nhận sóng badge đổi hình (H24 sau dựng).
- Hồ sơ `KeHoach_Video_Tap16*.md` B1/B2 còn số cũ (2576,1 s, LUFS trống, CER 10,7% / MOS 2,61 dưới ngưỡng).

## Người dùng cần làm
- Nghe duyệt giọng 3 ngôn ngữ (AI chưa nghe được); xem ảnh có mặt/chữ AI nếu muốn sửa trước khi đăng.
- Điền nguồn, kiểm mô tả và thumbnail (chưa chạy `package.py` đầy đủ); chưa commit (media bị `.gitignore`).
