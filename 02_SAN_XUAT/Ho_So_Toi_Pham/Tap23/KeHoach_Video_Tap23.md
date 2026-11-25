# HỒ SƠ SẢN XUẤT TẬP 20 · "KẺ TƯỚC ĐOẠT MẠNG SỐNG CẢ GIA ĐÌNH ĐỂ 'ĐƯA HỌ LÊN THIÊN ĐÀNG' — JOHN LIST"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 23: Nước Mắt Cá Sấu Của Kẻ Thuê Sát Thủ Giết Chồng (Hồ Sơ Richard Ramirez)** |
| Vụ án | Vụ án dàn cảnh thuê sát thủ tại Los Angeles & San Francisco (California, Hoa Kỳ, 1984–1989) |
| Chủ đề | Hội chứng say mê tội phạm (Hybristophilia), Dấu ấn Signature vs MO, Chấn thương đầu tuổi thơ & Vết gãy tâm lý |
| Tổng thời lượng | **2407.4 s (~40 phút 07 giây)** · 5 hồi · **245 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (N1 Cư dân Đông Los Angeles) · N2 (N2 Nhà báo theo dõi phiên tòa) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap22.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap23/xuat_ban/Tap23_master.mp3` & `02_SAN_XUAT/Tap23/xuat_ban/Tap23_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-20 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2398.4 s, kết thúc audio tại 2407.4 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **120.9 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **86.2 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **206.0 Hz**
- **Cư dân Đông Los Angeles ($N1$ · Cừu):** F0 trung vị = **181.8 Hz**
- **Nhà báo theo dõi phiên tòa ($N2$ · Mèo):** F0 trung vị = **282.4 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.86\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.23\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `faster-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.37%** (CER trung bình: **10.82%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.62 / 5.0** (Dải điểm: 1.94 – 3.64). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap23/xuat_ban/CanNghe_Tap23_higgs.md`](xuat_ban/CanNghe_Tap23_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap23/xuat_ban/Tap23_master.mp3`](xuat_ban/Tap23_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap23/xuat_ban/Tap23_master.wav`](xuat_ban/Tap23_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t23.json`](../../.work/timeline_s_t23.json) (2407.4 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap23/xuat_ban/Tap23.srt`](xuat_ban/Tap23.srt) (245 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep23_vi.json`](../../.work/quality_qc_utmos_ep23_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap23/xuat_ban/CanNghe_Tap23_higgs.md`](xuat_ban/CanNghe_Tap23_higgs.md)
