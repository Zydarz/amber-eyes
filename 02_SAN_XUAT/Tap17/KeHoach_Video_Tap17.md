# HỒ SƠ SẢN XUẤT TẬP 17 · "13 ĐỨA TRẺ TRONG NGỤC TÙ NGOẠI Ô — KIỂM SOÁT CƯỠNG CHẾ & CÚ NHẢY SINH TỒN"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 17: 13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Kiểm Soát Cưỡng Chế & Cú Nhảy Sinh Tồn (Hồ Sơ Gia Đình Turpin)** |
| Vụ án | Thảm kịch giam cầm và bạo hành 13 người con — Biệt thự ngoại ô Perris, California (14/01/2018) |
| Chủ đề | Kiểm soát cưỡng chế (Coercive Control), Hội chứng Điên cuồng đôi (Folie à Deux), Sự ấu trĩ hóa có chủ đích (Deliberate Infantilization) & Bản năng sinh tồn |
| Tổng thời lượng | **2035.0 s (~33 phút 54 giây)** · 5 hồi · **226 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Tổng đài viên 911 Hạt Riverside) · N2 (Đại diện y tế Bệnh viện Riverside) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap17.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap17/xuat_ban/Tap17_master.mp3` & `02_SAN_XUAT/Tap17/xuat_ban/Tap17_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2026.0 s, kết thúc audio tại 2035.0 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **121.1 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **87.6 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **206.5 Hz**
- **Tổng đài viên 911 ($N1$ · Cừu):** F0 trung vị = **180.5 Hz**
- **Đại diện y tế ($N2$ · Mèo):** F0 trung vị = **284.1 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.60\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.24\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `faster-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.77%** (CER trung bình: **10.96%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.57 / 5.0** (Dải điểm: 1.64 – 3.52). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap17/xuat_ban/CanNghe_Tap17_higgs.md`](xuat_ban/CanNghe_Tap17_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap17/xuat_ban/Tap17_master.mp3`](xuat_ban/Tap17_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap17/xuat_ban/Tap17_master.wav`](xuat_ban/Tap17_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t17.json`](../../.work/timeline_s_t17.json) (2035.0 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap17/xuat_ban/Tap17.srt`](xuat_ban/Tap17.srt) (226 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep17_vi.json`](../../.work/quality_qc_utmos_ep17_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap17/xuat_ban/CanNghe_Tap17_higgs.md`](xuat_ban/CanNghe_Tap17_higgs.md)
