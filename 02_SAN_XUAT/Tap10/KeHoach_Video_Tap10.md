# HỒ SƠ SẢN XUẤT TẬP 10 · "CHIẾC HỘP GỖ DƯỚI GẦM GIƯỜNG"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 10: Chiếc Hộp Gỗ Dưới Gầm Giường — Sự Bất Lực Tập Nhiễm & Bóng Ma 'The Company' (Hồ Sơ Colleen Stan)** |
| Vụ án | Cameron & Janice Hooker — Vụ bắt cóc, giam cầm 7 năm Colleen Stan (19/05/1977 – 10/08/1984, Red Bluff, California) |
| Chủ đề | Sự bất lực tập nhiễm (Learned Helplessness), Gắn kết chấn thương (Trauma Bonding), Bóng ma 'The Company', Tước đoạt cảm giác cực hạn & Hệ sinh thái 10 chỉ dấu tâm lý |
| Tổng thời lượng | **2040.5 s (~34 phút 00 giây)** · 5 hồi · **240 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Bạn của Colleen) · N2 (Janice Hooker - Đồng phạm kiêm người giải cứu) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap10.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap10/xuat_ban/Tap10_master.mp3` & `02_SAN_XUAT/Tap10/xuat_ban/Tap10_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2031.5 s, kết thúc audio tại 2040.5 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **121.1 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **86.4 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **205.1 Hz**
- **Bạn của Colleen ($N1$ · Cừu):** F0 trung vị = **175.2 Hz**
- **Janice Hooker ($N2$ · Mèo):** F0 trung vị = **285.7 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.84\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.13\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.91%** (CER trung bình: **11.23%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.58 / 5.0** (Dải điểm: 1.71 – 3.42). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap10/xuat_ban/CanNghe_Tap10_higgs.md`](xuat_ban/CanNghe_Tap10_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap10/xuat_ban/Tap10_master.mp3`](xuat_ban/Tap10_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap10/xuat_ban/Tap10_master.wav`](xuat_ban/Tap10_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t10.json`](../../.work/timeline_s_t10.json) (2040.5 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap10/xuat_ban/Tap10.srt`](xuat_ban/Tap10.srt) (240 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep10_vi.json`](../../.work/quality_qc_utmos_ep10_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap10/xuat_ban/CanNghe_Tap10_higgs.md`](xuat_ban/CanNghe_Tap10_higgs.md)
