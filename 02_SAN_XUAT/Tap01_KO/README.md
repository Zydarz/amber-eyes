# TẬP 01 · BẢN TIẾNG HÀN · HỒ SƠ SẢN XUẤT
# 제01화 「엄마의 사랑이라는 이름의 독약」 한국어판 제작 파일

**Phương án:** Dựng lại toàn bộ bằng tiếng Hàn chuẩn phát thanh tài liệu (giọng đọc AI tiếng Hàn, chữ trên màn hình tiếng Hàn font Malgun Gothic, intro tiếng Hàn, phụ đề Hàn, gói xuất bản). Hình nền, linh thú, nhạc và cấu trúc 122 shot đồng bộ 100% với bản chuẩn.

---

## 1. Trạng thái tiến độ & Đo đạc thực tế (Hoàn thành 100%)

| Bước | Hạng mục | Trạng thái | Số đo & Chi tiết kỹ thuật |
|---|---|---|---|
| 1 | Kịch bản tiếng Hàn | ✅ **ĐẠT** | `01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md` (128 câu, 33 lượt nói, 5 hồi; passed `_qc_ko_parity.py`) |
| 2 | Tách câu JSON | ✅ **ĐẠT** | `.work/script_tap01_KO.json` (61 element, 128 câu, khớp 100% mã câu VN) |
| 3 | Diễn xuất từng câu | ✅ **ĐẠT** | `.work/acting_tap01_KO.json` (kế thừa cảm xúc, pitch = 0 theo G5, speed clamp G4) |
| 4 | Chữ cố định & Intro | ✅ **ĐẠT** | `00_TIEU_CHUAN/CHU_CO_DINH_KO.md`, font Malgun Gothic (`malgun.ttf`/`malgunbd.ttf`), `assets/brand/intro_kenh_KO_t01.mov` (22.41s) |
| 5 | Bảng shot 122 cảnh | ✅ **ĐẠT** | `KeHoach_Video_Tap01_KO.md` (122/122 shot, khớp 100% câu thoại và trigger renderer) |
| 6 | Thử giọng & Duyệt vai | ✅ **ĐẠT** | Đã duyệt bộ 5 giọng: H (`Korean_CalmGentleman`), D (`Korean_ColdYoungMan`), C (`Korean_DecisiveQueen`), N1 (`Korean_GentleWoman`), N2 (`Korean_SweetGirl`) |
| 7 | Đọc TTS toàn tập | ✅ **ĐẠT** | 128/128 câu đã tạo thành công trong `.work/audio_s_KO/` |
| 8 | Kiểm vai (G10 Check) | ✅ **ĐẠT** | 5/5 vai = 1 người duy nhất (`SPEAKERS: 1`). Xen kẽ 3 vai đạt 10/10 tách bạch (`thu_giong_kiem_vai/report.md`) |
| 9 | Dựng âm thanh Master | ✅ **ĐẠT** | Thời lượng 1194.3s (19m54.3s). **-16.3 LUFS** (đạt -16 ± 1), **True Peak -4.5 dBTP** (đạt ≤ -1.5). 0 khoảng câm > 0.3s. File: `xuat_ban/Tap01_KO_master.mp3` |
| 10 | Dựng hình video | ✅ **ĐẠT** | `build_video3.py --workers 6` dựng đủ 35.829 khung hình (1920x1080 @ 30fps), 0 lỗi |
| 11 | Phụ đề & Đóng gói | ✅ **ĐẠT** | `Tap01_KO.srt` (162 cues), `thumbnail.png` (1280x720), `description.txt` / `mo_ta.txt` (đầy đủ mốc chương, lưu ý pháp lý, nguồn đối chiếu, đường dây nóng 112/129) |
| 12 | Đóng gói MP4 Master | ✅ **ĐẠT** | `Tap01_KO_master.mp4` (420.54 MB, 1194.300s, độ lệch A/V: **0.0173s**, quét lỗi giải mã: **0 lỗi**) |

---

## 2. Bảng phân vai chính thức (Bộ 5 giọng tiếng Hàn)

| Vai | Giọng AI MiniMax | Tốc độ | F0 trung vị | Đặc điểm âm sắc |
|---|---|---:|---:|---|
| **Host (Cú)** | `Korean_CalmGentleman` | 0.95 | 107 Hz | Trầm ấm, điềm đạm, giọng kể podcast ban đêm. |
| **Điều tra viên (Sói)** | `Korean_ColdYoungMan` | 0.95 | 143 Hz | Lạnh lùng, nghiêm nghị, sắc bén (cách Host 5.0 nửa cung). |
| **Chuyên gia (Cáo)** | `Korean_DecisiveQueen` | 0.92 | 258 Hz | Nữ trí tuệ, tự tin, dứt khoát, phong cách chuyên gia tâm lý. |
| **N1 (Cừu)** | `Korean_GentleWoman` | 0.95 | 276 Hz | Nữ ấm áp, cảm xúc, đại diện hàng xóm Springfield. |
| **N2 (Mèo)** | `Korean_SweetGirl` | 0.95 | 193 Hz | Trẻ trung, tự nhiên, góc nhìn khán giả theo dõi vụ án (phân tách rõ với C & N1). |

---

## 3. Các thành phẩm xuất bản (`02_SAN_XUAT/Tap01_KO/xuat_ban/`)

1. **`Tap01_KO_master.mp4`** (420.54 MB): Video hoàn chỉnh độ phân giải 1080p30 (H.264 + AAC 192kbps). Thời lượng 19m54.3s. Đồng bộ hình - tiếng lệch chỉ 0.0173s. 0 lỗi decode.
2. **`Tap01_KO_master.mp3`** (27.34 MB): Master audio chuẩn truyền hình (-16.3 LUFS, TP -4.5 dBTP).
3. **`Tap01_KO.srt`** (24.65 KB): Phụ đề tiếng Hàn chuẩn phát thanh (162 cue).
4. **`thumbnail.png`** (1.26 MB): Ảnh đại diện 1280x720 phong cách Graphic Novel Noir với tiêu đề tiếng Hàn: 「엄마의 사랑이라는 / 이름의 독약」.
5. **`description.txt` / `mo_ta.txt`**: Nội dung mô tả video YouTube với mốc chương (chapters), lưu ý pháp lý/giáo dục, 19 nguồn tra cứu đã xác minh (✅) và đường dây nóng bảo vệ trẻ em 112 / 129 tại Hàn Quốc.
6. **`nguon_tham_khao_KO.md`**: Danh mục chi tiết 19 nguồn công khai đối chiếu theo từng câu thoại.
