# HỒ SƠ SẢN XUẤT TẬP 14 · "BI KỊCH BETTY BRODERICK"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 14: Khi Nạn Nhân Gaslighting Bước Qua Ranh Giới Tội Ác — Sự Thao Túng Thực Tại & Cơn Thịnh Nộ Hủy Diệt (Hồ Sơ Betty Broderick)** |
| Vụ án | Elisabeth 'Betty' Broderick, Daniel Broderick & Linda Kolkena — La Jolla & Marston Hills, San Diego, California, Hoa Kỳ (05/11/1989) |
| Chủ đề | Thao túng thực tại (Gaslighting), Tổn thương ái kỷ (Narcissistic Injury), Phản ứng đứt gãy, Bẫy phục tùng & Hệ sinh thái 10 chỉ dấu tâm lý |
| Tổng thời lượng | **2214.5 s (~36 phút 54 giây)** · 5 hồi · **210 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Bạn thân La Jolla) · N2 (Kim Broderick - Con gái lớn) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap14.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap14/xuat_ban/Tap14_master.mp3` & `02_SAN_XUAT/Tap14/xuat_ban/Tap14_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2205.5 s, kết thúc audio tại 2214.5 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **119.1 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **86.6 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **205.1 Hz**
- **Bạn thân ($N1$ · Cừu):** F0 trung vị = **183.2 Hz**
- **Kim Broderick ($N2$ · Mèo):** F0 trung vị = **287.4 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.51\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.41\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **9.82%** (CER trung bình: **10.24%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.57 / 5.0** (Dải điểm: 1.62 – 3.49). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap14/xuat_ban/CanNghe_Tap14_higgs.md`](xuat_ban/CanNghe_Tap14_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap14/xuat_ban/Tap14_master.mp3`](xuat_ban/Tap14_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap14/xuat_ban/Tap14_master.wav`](xuat_ban/Tap14_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t14.json`](../../.work/timeline_s_t14.json) (2214.5 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap14/xuat_ban/Tap14.srt`](xuat_ban/Tap14.srt) (210 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep14_vi.json`](../../.work/quality_qc_utmos_ep14_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap14/xuat_ban/CanNghe_Tap14_higgs.md`](xuat_ban/CanNghe_Tap14_higgs.md)
