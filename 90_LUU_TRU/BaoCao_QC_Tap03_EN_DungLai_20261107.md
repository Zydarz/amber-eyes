# BÁO CÁO QC — TẬP 03 EN DỰNG LẠI THEO KỊCH BẢN + MASTER MỚI · 07/11/2026

**Thành phẩm:** `02_SAN_XUAT/Tap03_EN/xuat_ban/Tap03_EN_master.mp4` (568,1 MB)
**Nguồn:** `Tap03_EN_master.mp3` (06/11 07:15, 1648,80 s) · `timeline_s_EN_t03.json` (sha 12 ký tự `f383ec36d0ba`) · `shots_EN_t03.json` (`af70bb7e7580`) · `build_video3.py` `800698eaad64` · `edition.py` `057b07863bfc`

## Số đo (trên mp4 cuối)
| Mục | Giá trị | Chuẩn | |
|---|---|---|---|
| Thời lượng mp4 / mp3 / timeline.total | 1648,800 / 1648,800 / 1648,8 s | ± 0,05 | ✅ |
| Khung hình | 49.464 = `int(1648,8×30)` (chunk 16.470 + 16.470 + 16.524) | khớp | ✅ |
| LUFS | −16,4 | −16 ± 1 | ✅ |
| True peak | **−2,6 dBFS** | ≤ −1,5 | ✅ (xem lỗi 3) |
| Khoảng lặng > 0,3 s @ −60 dB | 0 | 0 | ✅ |
| Lệch A/V (FFT, 4 cửa sổ) | 0,0 ms | ≤ 20 ms | ✅ |
| Giải mã | 0 lỗi | 0 | ✅ |
| Lời đọc ↔ mốc câu timeline | 218/218 câu có onset đúng (bước nhảy mức TB 26 dB) · 0 câu câm bên trong | — | ✅ |
| Bảng shot | 110 shot · phủ 218/218 câu · đúng thứ tự · liền mạch · cuối = 1648,8 s | — | ✅ |
| Ảnh tĩnh ↔ khung trong mp4 | 110/110 · MAE TB 4,04/4,10/3,46 · max 5,47 | < 15 | ✅ |
| Ảnh tĩnh soi bằng mắt | 110/110 (13 contact sheet) + 6 shot danh sách T8 tại cuối shot | — | ✅ |
| Thẻ kết (1644 s) | có `CASE FILE 03 · CLOSED / AMBER EYES / khẩu hiệu` | H12 | ✅ |
| Phụ đề | 469 cue · cue cuối 1639,8 s · 0 chồng · 0 > 6 s | — | ✅ |

## Lỗi tìm ra và sửa
1. **Bảng shot lệch thời gian (H14):** dựng cho audio 1646,62 s, master mới 1648,8 s ⇒ lệch tới 7,3 s. Chạy lại `parse_shots` (chỉ mốc thời gian đổi, 0 khác biệt nội dung).
2. **5 shot chữ ≠ lời đọc** do kịch bản đổi câu (cổng số/phủ câu không bắt được): `1-23`, `2-07` (+ đổi nền `t3_backyard_garden` → `t3_car_door`), `2-15`, `4-07`, `5-09`. Sửa ở `KeHoach_Video_Tap03_EN.md` + `.work/shots_text_tap03_EN.json`.
3. **Đè chữ ở mục danh sách T8** `2-05`, `2-06`, `3-12` (mục dài xuống dòng). Rút ngắn; kiểm lại ở `end − 0,6 s`: sạch.
4. **True peak −0,7 dBFS:** đỉnh duy nhất ở 1640,84 s (tiếng "cạch" cassette); thêm `asoftclip=hard:0.63` sau `alimiter` ⇒ −2,6 dBFS. Chuỗi mux dùng: `alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1,asoftclip=type=hard:threshold=0.63` (chạy ffmpeg trực tiếp, **chưa khai vào `edition.py`**).
5. `audio_master_EN_t03.wav` đã bị dọn ⇒ giải mã lại từ mp3 (48 kHz s16).

## Việc người dùng phải làm
- Nghe duyệt audio + xem video (chưa có ai xem video này).
- **`mo_ta.txt`/`description.txt` hiện 8.478 ký tự > giới hạn YouTube 5.000.** Tôi giữ bản đã commit (nội dung 10 chỉ dấu), chỉ vá 4 mốc chương (05:33 / 10:51 / 16:31 / 22:04). Bản `package.py` sinh ra (4.935 ký tự, 24/24 link, không có 10 chỉ dấu) cất ở `.work/_cu/en_t03_rebuild_20261107/mo_ta_package_generated_4935.txt`. Cần quyết định rút gọn hay dùng bản sinh.
- Quyết định có khai chuỗi limiter mới vào `edition.py` không (đụng file dùng chung).

## Sao lưu (L5)
`.work/_cu/en_t03_rebuild_20261107/`: shots/timeline/KeHoach trước sửa · srt/mo_ta/description/thumbnail cũ · `Tap03_EN_master_peak-0.7_fail.mp4` · ảnh tĩnh cũ.
