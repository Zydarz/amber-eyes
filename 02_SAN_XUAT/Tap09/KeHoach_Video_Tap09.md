# HỒ SƠ SẢN XUẤT TẬP 09 · "NGHỆ THUẬT XÓA BỎ BẢN NGÃ"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 09: Nghệ Thuật Xóa BỎ Bản Ngã** |
| Vụ án | Hồ sơ Charles Manson & Thảm kịch Gia đình Manson (Los Angeles, California, Hoa Kỳ, 1969) |
| Chủ đề | Cơ chế tẩy não 3 giai đoạn (Unfreezing – Changing – Refreezing), Bộ ba Đen tối (Dark Triad) & Thao túng tâm lý bầy đàn |
| Tổng thời lượng | **1530.2 s (~25 phút 30 giây)** · 5 hồi · **199 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Cư dân Los Angeles) · N2 (Linda Kasabian) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap09.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp3` & `02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 1521.2 s, kết thúc audio tại 1530.2 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **121.2 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **86.8 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **208.7 Hz**
- **Nhân chứng ($N1$ · Cư dân):** F0 trung vị = **177.8 Hz**
- **Lời khai ($N2$ · Linda Kasabian):** F0 trung vị = **289.2 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.78\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.41\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **11.54%** (CER trung bình: **12.85%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.68 / 5.0** (Dải điểm: 1.72 – 3.58). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap09/xuat_ban/CanNghe_Tap09_higgs.md`](CanNghe_Tap09_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp3`](xuat_ban/Tap09_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.wav`](xuat_ban/Tap09_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t09.json`](../../.work/timeline_s_t09.json) (1530.2 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09.srt`](xuat_ban/Tap09.srt) (199 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep09_vi.json`](../../.work/quality_qc_utmos_ep09_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap09/xuat_ban/CanNghe_Tap09_higgs.md`](xuat_ban/CanNghe_Tap09_higgs.md)
