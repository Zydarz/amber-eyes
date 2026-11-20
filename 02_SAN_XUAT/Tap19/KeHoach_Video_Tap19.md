# HỒ SƠ SẢN XUẤT TẬP 19 · "13 ĐỨA TRẺ TRONG NGỤC TÙ NGOẠI Ô — KIỂM SOÁT CƯỠNG CHẾ & CÚ NHẢY SINH TỒN"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 19: Màn Kịch 'Con Quỷ Trong Đầu' — Giả Bệnh Tâm Thần & Sự Thật Trước Máy Quay (Hồ Sơ Nikolas Cruz)** |
| Vụ án | Vụ xả súng Trường Trung học Marjory Stoneman Douglas, Parkland, Florida (14/02/2018) |
| Chủ đề | Giả bệnh tâm thần (Malingering), Loạn thần thực sự vs. Rối loạn nhân cách chống đối xã hội, Hối hận công cụ vs. Tự thương hại bệnh lý |
| Tổng thời lượng | **2214.0 s (~36 phút 53 giây)** · 5 hồi · **241 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Học sinh sống sót Parkland) · N2 (Bồi thẩm viên) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap19.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap19/xuat_ban/Tap19_master.mp3` & `02_SAN_XUAT/Tap19/xuat_ban/Tap19_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2205.0 s, kết thúc audio tại 2214.0 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **119.9 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **87.6 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **208.7 Hz**
- **Tổng đài viên 911 ($N1$ · Cừu):** F0 trung vị = **177.8 Hz**
- **Đại diện y tế ($N2$ · Mèo):** F0 trung vị = **292.7 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.43\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.60\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `faster-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.32%** (CER trung bình: **10.44%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.59 / 5.0** (Dải điểm: 1.74 – 3.53). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap19/xuat_ban/CanNghe_Tap19_higgs.md`](xuat_ban/CanNghe_Tap19_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap19/xuat_ban/Tap19_master.mp3`](xuat_ban/Tap19_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap19/xuat_ban/Tap19_master.wav`](xuat_ban/Tap19_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t19.json`](../../.work/timeline_s_t19.json) (2214.0 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap19/xuat_ban/Tap19.srt`](xuat_ban/Tap19.srt) (241 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep19_vi.json`](../../.work/quality_qc_utmos_ep19_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap19/xuat_ban/CanNghe_Tap19_higgs.md`](xuat_ban/CanNghe_Tap19_higgs.md)
