# HỒ SƠ SẢN XUẤT TẬP 14 · "BI KỊCH BETTY BRODERICK"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 14: Khi Nạn Nhân Gaslighting Bước Qua Ranh Giới Tội Ác — Sự Thao Túng Thực Tại & Cơn Thịnh Nộ Hủy Diệt (Hồ Sơ Betty Broderick)** |
| Vụ án | Elisabeth 'Betty' Broderick, Daniel Broderick & Linda Kolkena — La Jolla & Marston Hills, San Diego, California, Hoa Kỳ (05/11/1989) |
| Chủ đề | Thao túng thực tại (Gaslighting), Tổn thương ái kỷ (Narcissistic Injury), Phản ứng đứt gãy, Bẫy phục tùng & Hệ sinh thái 10 chỉ dấu tâm lý |
| Tổng thời lượng | **2206.6 s (~36 phút 46 giây)** · 5 hồi · **210 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Bạn thân La Jolla) · N2 (Kim Broderick - Con gái lớn) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap14.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap14/xuat_ban/Tap14_master.mp3` & `02_SAN_XUAT/Tap14/xuat_ban/Tap14_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **-16.2 LUFS** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **-2.2 dBFS** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** **3.3 LU**
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2197.6 s, kết thúc audio tại 2206.6 s với đuôi nhạc ấm fade out (ĐẠT ✅)
- **Nhịp nghỉ giữa câu (Rule A13):** Trung vị nghỉ 0.75 s ($\ge 0.60\text{ s}$), tỷ lệ khoảng nghỉ $< 0.40\text{ s}$: 0% ($\le 25\%$) — ĐẠT ✅

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **119.1 Hz** (n=128)
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **86.6 Hz** (n=35)
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **205.1 Hz** (n=35)
- **Bạn thân ($N1$ · Cừu):** F0 trung vị = **183.2 Hz** (n=6)
- **Kim Broderick ($N2$ · Mèo):** F0 trung vị = **287.4 Hz** (n=6)
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.51\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.41\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **9.96%** (CER trung bình: **10.33%** — chủ yếu do tên riêng tiếng Anh: Broderick, La Jolla, Kolkena, Daniel).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.58 / 5.0** (Dải điểm: 1.81 – 3.38).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap14/xuat_ban/CanNghe_Tap14_higgs.md`](xuat_ban/CanNghe_Tap14_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap14/xuat_ban/Tap14_master.mp3`](xuat_ban/Tap14_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap14/xuat_ban/Tap14_master.wav`](xuat_ban/Tap14_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t14.json`](../../.work/timeline_s_t14.json) (2206.6 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap14/xuat_ban/Tap14.srt`](xuat_ban/Tap14.srt) (551 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep14_vi.json`](../../.work/quality_qc_utmos_ep14_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap14/xuat_ban/CanNghe_Tap14_higgs.md`](xuat_ban/CanNghe_Tap14_higgs.md)
