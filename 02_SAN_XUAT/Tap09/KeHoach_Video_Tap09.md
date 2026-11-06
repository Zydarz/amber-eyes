# HỒ SƠ SẢN XUẤT TẬP 09 · "NGHỆ THUẬT XÓA BỎ BẢN NGÃ"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 09: Nghệ Thuật Xóa Bỏ Bản Ngã** |
| Vụ án | Hồ sơ Charles Manson & Thảm kịch Gia đình Manson (Los Angeles, California, Hoa Kỳ, 1969) |
| Chủ đề | Cơ chế tẩy não 3 giai đoạn (Unfreezing – Changing – Refreezing), Bộ ba Đen tối (Dark Triad) & Thao túng tâm lý bầy đàn |
| Tổng thời lượng | **20 phút 28,5 giây** (1228,5 s) · 5 hồi · 159 câu thoại |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Cư dân Los Angeles) · N2 (Linda Kasabian) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D3_SH.wav`, C: `C2_AB03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap09.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp3` & `.work/audio_master_t09.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **$-16.2\text{ LUFS}$** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **$-1.5\text{ dBFS}$** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** **$3.7\text{ LU}$**
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** $23.0\text{ s}$ (sau đoạn Intro $22.41\text{ s}$ — ĐẠT ✅)
- **Thời lượng lời cuối:** $1219.5\text{ s}$, kết thúc audio tại $1228.5\text{ s}$ với đuôi nhạc ấm fade out $7.8\text{ s}$ (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **$124.0\text{ Hz}$** ($n=94$)
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **$86.5\text{ Hz}$** ($n=25$)
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **$206.9\text{ Hz}$** ($n=29$)
- **Nhân chứng ($N1$ · Thỏ tuyết):** F0 trung vị = **$176.1\text{ Hz}$** ($n=8$)
- **Lời khai ($N2$ · Gấu trúc):** F0 trung vị = **$282.4\text{ Hz}$** ($n=3$)
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = 12 \log_2(124.0 / 86.5) = \mathbf{6.24\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = 12 \log_2(206.9 / 124.0) = \mathbf{8.86\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **$10.83\%$** (CER trung bình: $11.90\%$, chủ yếu do từ vựng tên riêng, địa danh tiếng Anh: *Charles Manson*, *Sharon Tate*, *Spahn Ranch*, *Cielo Drive*, *Beverly Hills*, *Helter Skelter*, *Terry Melcher*, *Vincent Bugliosi* và các biến thể dấu thanh của Whisper Base trên tiếng Việt).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER $> 2\%$ và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **$2.60 / 5.0$** (Dải điểm: $1.47 - 3.49$).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap09/xuat_ban/CanNghe_Tap09_higgs.md`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap09/xuat_ban/CanNghe_Tap09_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp3`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap09/xuat_ban/Tap09_master.mp3) (28.12 MB)
   - WAV: [`.work/audio_master_t09.wav`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/audio_master_t09.wav) (224.94 MB, 48 kHz 24-bit stereo)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t09.json`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/timeline_s_t09.json) (1228.5 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap09/xuat_ban/Tap09.srt`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap09/xuat_ban/Tap09.srt) (310 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep09_vi.json`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/quality_qc_utmos_ep09_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap09/xuat_ban/CanNghe_Tap09_higgs.md`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap09/xuat_ban/CanNghe_Tap09_higgs.md)
