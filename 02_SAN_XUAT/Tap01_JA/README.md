# TẬP 01 · BẢN TIẾNG NHẬT · HỒ SƠ SẢN XUẤT
# 第01話「母の愛という名の毒薬」日本語版制作ファイル

**Phương án:** Dựng lại toàn bộ bằng tiếng Nhật chuẩn phát thanh tài liệu (giọng đọc AI tiếng Nhật, chữ trên màn hình tiếng Nhật, intro tiếng Nhật, phụ đề Nhật, gói xuất bản). Hình nền, linh thú, nhạc và cấu trúc 122 shot đồng bộ 100% với bản chuẩn.

---

## 1. Trạng thái tiến độ & Đo đạc thực tế (Hoàn thành 100%)

| Bước | Hạng mục | Trạng thái | Số đo & Chi tiết kỹ thuật |
|---|---|---|---|
| 1 | Kịch bản tiếng Nhật | ✅ **ĐẠT** | `01_KICH_BAN/Tap01_JA/kichban_tap01_JA.md` (128 câu, 33 lượt nói, 5 hồi; passed `_qc_ja.py 01`) |
| 2 | Tách câu JSON | ✅ **ĐẠT** | `.work/script_tap01_JA.json` (61 element, 128 câu, khớp 100% mã câu VN) |
| 3 | Diễn xuất từng câu | ✅ **ĐẠT** | `.work/acting_tap01_JA.json` (kế thừa cảm xúc, pitch = 0 theo G5, speed clamp G4) |
| 4 | Chữ cố định & Intro | ✅ **ĐẠT** | `CHU_CO_DINH_JA.md`, font Yu Gothic (`YuGothB.ttc`/`YuGothM.ttc`), `assets/brand/intro_kenh_JA_t01.mov` (22.4s) |
| 5 | Bảng shot 122 cảnh | ✅ **ĐẠT** | `KeHoach_Video_Tap01_JA.md` (122/122 shot, 21 cụm beat khớp 100% câu thoại) |
| 6 | Thử giọng & Duyệt vai | ✅ **ĐẠT** | Đã duyệt bộ 5 giọng: H (`GentleButler`), D (`SeriousCommander`), C (`DependableWoman`), N1 (`KindLady`), N2 (`DecisivePrincess`) |
| 7 | Đọc TTS toàn tập | ✅ **ĐẠT** | 128/128 câu đã tạo thành công trong `.work/audio_s_JA/` |
| 8 | Kiểm vai (G10 Check) | ✅ **ĐẠT** | 5/5 vai = 1 người duy nhất (`SPEAKERS: 1`). Xen kẽ 3 vai đạt 10/10 tách bạch (`thu_giong_kiem_vai/report.md`) |
| 9 | Dựng âm thanh Master | ✅ **ĐẠT** | Thời lượng 1368.7s (22m48.7s). **-16.0 LUFS** (đạt -16 ± 1), **True Peak -2.93 dBFS** (đạt ≤ -1.5). 0 khoảng câm > 0.3s. File: `xuat_ban/Tap01_JA_master.mp3` |
| 10 | Dựng hình video | ✅ **ĐẠT** | `build_video3.py --workers 6` dựng đủ 41.061 khung hình (1920x1080 @ 30fps), 0 lỗi |
| 11 | Phụ đề & Đóng gói | ✅ **ĐẠT** | `Tap01_JA.srt` (145 cues, tự ngắt dòng 24 ký tự theo kinsoku shori), `thumbnail.png` (1280x720), `description.txt` / `mo_ta.txt` (đầy đủ mốc chương, lưu ý pháp lý, nguồn đối chiếu, đường dây nóng 189) |
| 12 | Đóng gói MP4 Master | ✅ **ĐẠT** | `Tap01_JA_master.mp4` (477.79 MB, 1368.667s, độ lệch A/V: **0.0053s**, quét lỗi giải mã: **0 lỗi**) |

---

## 2. Bảng phân vai chính thức (Bộ 5 giọng tiếng Nhật)

| Vai | Giọng AI MiniMax | Tốc độ | F0 trung vị | Đặc điểm âm sắc |
|---|---|---:|---:|---|
| **Host (Cú)** | `Japanese_GentleButler` | 0.95 | 109 Hz | Trầm ấm, điềm đạm, giọng kể podcast ban đêm. |
| **Điều tra viên (Sói)** | `Japanese_SeriousCommander` | 0.97 | 172 Hz | Lạnh lùng, nghiêm nghị, sắc bén (cách Host 7.8 nửa cung). |
| **Chuyên gia (Cáo)** | `Japanese_DependableWoman` | 0.95 | 213 Hz | Nữ trí tuệ, tự tin, nhấn nhá rõ ràng, phong cách chuyên gia tâm lý. |
| **N1 (Cừu)** | `Japanese_KindLady` | 0.95 | 225 Hz | Nữ ấm áp, cảm xúc, đại diện hàng xóm Springfield. |
| **N2 (Mèo)** | `Japanese_DecisivePrincess` | 0.95 | 235 Hz | Trẻ trung, linh hoạt, góc nhìn khán giả theo dõi vụ án. |

---

## 3. Các thành phẩm xuất bản (`02_SAN_XUAT/Tap01_JA/xuat_ban/`)

1. **`Tap01_JA_master.mp4`** (477.79 MB): Video hoàn chỉnh độ phân giải 1080p30 (H.264 + AAC 192kbps). Thời lượng 22m48.7s. Đồng bộ hình - tiếng lệch chỉ 0.0053s. 0 lỗi decode.
2. **`Tap01_JA_master.mp3`** (32.85 MB): Master audio chuẩn truyền hình (-16.0 LUFS, TP -2.93 dBFS).
3. **`Tap01_JA.srt`** (25.66 KB): Phụ đề tiếng Nhật chuẩn phát thanh (145 cue).
4. **`thumbnail.png`** (1.34 MB): Ảnh đại diện 1280x720 phong cách Graphic Novel Noir với tiêu đề tiếng Nhật: 「母の愛という名の / 毒薬」.
5. **`description.txt` / `mo_ta.txt`**: Nội dung mô tả video YouTube với mốc chương (chapters), lưu ý pháp lý/giáo dục, 19 nguồn tra cứu đã xác minh (✅) và đường dây nóng bảo vệ trẻ em 189 tại Nhật Bản.
6. **`nguon_tham_khao_JA.md`**: Danh mục chi tiết 19 nguồn công khai đối chiếu theo từng câu thoại.
