# HỒ SƠ SẢN XUẤT TẬP 08 · "KHI CÁC THIÊN TÀI BỊ TẨY NÃO"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 08: Khi Các Thiên Tái Bị Tẩy Não** |
| Vụ án | Giáo phái Aum Shinrikyo & Vụ tấn công khí độc tàu điện ngầm Tokyo (Tokyo, Nhật Bản, 1995) |
| Chủ đề | Thao túng tâm lý giáo phái, Sự trống rỗng hiện sinh, Kỹ thuật làm suy kiệt thần kinh, Nghịch lý trí thức tinh hoa |
| Tổng thời lượng | **18 phút 30,8 giây** (1110,8 s) · 5 hồi · 154 câu thoại |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Hành khách Tokyo) · N2 (Bác sĩ Ikuo Hayashi) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D3_SH.wav`, C: `C2_AB03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap08.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap08/xuat_ban/Tap08_master.mp3` & `.work/audio_master_t08.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **$-16.2\text{ LUFS}$** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **$-1.6\text{ dBFS}$** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** **$3.3\text{ LU}$**
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **$124.0\text{ Hz}$** ($n=94$)
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **$86.4\text{ Hz}$** ($n=26$)
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **$208.2\text{ Hz}$** ($n=24$)
- **Nhân chứng ($N1$ · Thỏ tuyết):** F0 trung vị = **$180.8\text{ Hz}$** ($n=6$)
- **Lời khai ($N2$ · Gấu trúc):** F0 trung vị = **$278.3\text{ Hz}$** ($n=4$)
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = 12 \log_2(124.0 / 86.4) = \mathbf{6.26\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = 12 \log_2(208.2 / 124.0) = \mathbf{8.97\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **$9.75\%$** (CER trung bình: $10.98\%$, chủ yếu do từ vựng địa danh tiếng Nhật: *Kasumigaseki*, *Chiyoda*, *Marunouchi*, *Hibiya* và các biến thể dấu thanh của Whisper Base trên tiếng Việt).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **$2.56 / 5.0$** (Dải điểm: $1.51 - 3.44$).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap08/xuat_ban/Tap08_master.mp3`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/Tap08_master.mp3) (25.43 MB)
   - WAV: [`.work/audio_master_t08.wav`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/audio_master_t08.wav) (203.40 MB, 48 kHz 24-bit stereo)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t08.json`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/timeline_s_t08.json) (1110.8 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap08/xuat_ban/Tap08.srt`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/Tap08.srt) (278 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep08_vi.json`](file:///Users/duonganhhai/CodeGit/amber-eyes/.work/quality_qc_utmos_ep08_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md`](file:///Users/duonganhhai/CodeGit/amber-eyes/02_SAN_XUAT/Tap08/xuat_ban/CanNghe_Tap08_higgs.md)
