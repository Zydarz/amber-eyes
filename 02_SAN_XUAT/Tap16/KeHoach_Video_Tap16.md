# HỒ SƠ SẢN XUẤT TẬP 16 · "KẺ TƯỚC ĐOẠT MẠNG SỐNG CẢ GIA ĐÌNH ĐỂ 'ĐƯA HỌ LÊN THIÊN ĐÀNG' — JOHN LIST"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 16: Kẻ Tước Đoạt Mạng Sống Cả Gia Đình Để 'Đưa Họ Lên Thiên Đàng' (Hồ Sơ John List)** |
| Vụ án | Thảm kịch gia đình John List — Biệt thự Breeze Knoll, Westfield, New Jersey (09/11/1971) |
| Chủ đề | Rối loạn nhân cách ám ảnh cưỡng chế (OCPD), Bẫy ngụy biện đạo đức, Cuộc trốn chạy 18 năm dưới danh tính Robert Clark & Bức tượng sáp Frank Bender |
| Tổng thời lượng | **2576.1 s (~42 phút 56 giây)** · 5 hồi · **257 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Jean Phillips - Giáo viên kịch) · N2 (Wanda Flanery - Hàng xóm Colorado) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap16.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap16/xuat_ban/Tap16_master.mp3` & `02_SAN_XUAT/Tap16/xuat_ban/Tap16_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2567.1 s, kết thúc audio tại 2576.1 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **120.0 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **87.0 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **205.1 Hz**
- **Jean Phillips ($N1$ · Cừu):** F0 trung vị = **183.2 Hz**
- **Wanda Flanery ($N2$ · Mèo):** F0 trung vị = **282.4 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.56\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.28\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.74%** (CER trung bình: **11.25%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.61 / 5.0** (Dải điểm: 1.65 – 3.48). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap16/xuat_ban/CanNghe_Tap16_higgs.md`](xuat_ban/CanNghe_Tap16_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap16/xuat_ban/Tap16_master.mp3`](xuat_ban/Tap16_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap16/xuat_ban/Tap16_master.wav`](xuat_ban/Tap16_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t16.json`](../../.work/timeline_s_t16.json) (2576.1 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap16/xuat_ban/Tap16.srt`](xuat_ban/Tap16.srt) (257 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep16_vi.json`](../../.work/quality_qc_utmos_ep16_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap16/xuat_ban/CanNghe_Tap16_higgs.md`](xuat_ban/CanNghe_Tap16_higgs.md)
