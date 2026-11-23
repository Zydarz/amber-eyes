# HỒ SƠ SẢN XUẤT TẬP 15 · "CƠN CUỒNG GHEN RANH GIỚI — JODI ARIAS"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 15: Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới — Nỗi Sợ Bị Ruồng Bỏ & Thảm Kịch Phòng Tắm (Hồ Sơ Jodi Arias)** |
| Vụ án | Jodi Arias & Travis Alexander — Mesa, Arizona, Hoa Kỳ (09/06/2008) |
| Chủ đề | Rối loạn nhân cách ranh giới (BPD), Cơn cuồng nộ ruồng bỏ (Abandonment Rage), Ám ảnh độc hại, Trò ảo thuật phòng thẩm vấn & Hệ sinh thái 10 chỉ dấu tâm lý |
| Tổng thời lượng | **1859.9 s (~30 phút 59 giây)** · 5 hồi · **220 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Bạn thân Mesa) · N2 (Bồi thẩm đoàn Hạt Maricopa) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap15.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap15/xuat_ban/Tap15_master.mp3` & `02_SAN_XUAT/Ho_So_Toi_Pham/Tap15/xuat_ban/Tap15_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 1850.9 s, kết thúc audio tại 1859.9 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **118.2 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **87.1 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **206.9 Hz**
- **Bạn thân ($N1$ · Cừu):** F0 trung vị = **180.5 Hz**
- **Kim Broderick ($N2$ · Mèo):** F0 trung vị = **281.6 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.29\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.69\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **11.59%** (CER trung bình: **11.58%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.59 / 5.0** (Dải điểm: 1.48 – 3.39). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap15/xuat_ban/CanNghe_Tap15_higgs.md`](xuat_ban/CanNghe_Tap15_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap15/xuat_ban/Tap15_master.mp3`](xuat_ban/Tap15_master.mp3)
   - WAV: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap15/xuat_ban/Tap15_master.wav`](xuat_ban/Tap15_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t15.json`](../../.work/timeline_s_t15.json) (1859.9 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap15/xuat_ban/Tap15.srt`](xuat_ban/Tap15.srt) (220 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep15_vi.json`](../../.work/quality_qc_utmos_ep15_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Ho_So_Toi_Pham/Tap15/xuat_ban/CanNghe_Tap15_higgs.md`](xuat_ban/CanNghe_Tap15_higgs.md)
