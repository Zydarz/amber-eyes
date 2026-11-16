# HỒ SƠ SẢN XUẤT TẬP 11 · "CẶP ĐÔI KEN & BARBIE"

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 11: Cặp Đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi & Thỏa Thuận Với Quỷ Dữ (Hồ Sơ Paul Bernardo & Karla Homolka)** |
| Vụ án | Paul Bernardo & Karla Homolka — Vụ án mạng Scarborough Rapist & Ken and Barbie Killers (Ontario, Canada) |
| Chủ đề | Hội chứng Điên cuồng đôi (Folie à Deux), Trung hòa đạo đức (Moral Neutralization), Mặt nạ nạn nhân (Victim Mask), Thỏa thuận với Quỷ dữ & Hệ sinh thái 10 chỉ dấu tâm lý |
| Tổng thời lượng | **2374.2 s (~39 phút 34 giây)** · 5 hồi · **272 câu thoại** |
| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Người hàng xóm Port Dalhousie) · N2 (Công tố viên phụ trách vụ án) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) trên Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (H: `H.wav`, D: `D_NEW_subbass-husky_t02.wav`, C: `C_NEW_alto-brisk_t03.wav`, N1: `W6_LOW.wav`, N2: `W5_HIGH.wav`) |
| Âm thanh | Stereo 3 lớp: BGM 5 Hồi + Ambience liên tục + SFX tiếng động (`.work/sfx_tap11.json`) |
| Thành phẩm Master | `02_SAN_XUAT/Tap11/xuat_ban/Tap11_master.mp3` & `02_SAN_XUAT/Tap11/xuat_ban/Tap11_master.wav` |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($I$):** **** (Tiêu chuẩn: $-16 \pm 1\text{ LUFS}$ — ĐẠT ✅)
- **True Peak ($TP$):** **** (Tiêu chuẩn: $\le -1.5\text{ dBFS}$ — ĐẠT ✅)
- **Loudness Range ($LRA$):** ****
- **Khoảng câm tuyệt đối ($> 0.3\text{ s}$ ở $-60\text{ dBFS}$):** **0 lỗi** (ĐẠT ✅ Rule A1 / V4)
- **Thời lượng lời đầu:** 23.0 s (sau đoạn Intro 22.41 s — ĐẠT ✅)
- **Thời lượng lời cuối:** 2365.2 s, kết thúc audio tại 2374.2 s với đuôi nhạc ấm fade out (ĐẠT ✅)

### 2. Tách bạch Cao độ & Nhận diện Vai (Quy tắc G9)
- **Host ($H$ · Cú):** F0 trung vị = **122.4 Hz**
- **Điều tra viên ($D$ · Sói):** F0 trung vị = **87.0 Hz**
- **Chuyên gia ($C$ · Cáo):** F0 trung vị = **207.8 Hz**
- **Người hàng xóm ($N1$ · Cừu):** F0 trung vị = **176.7 Hz**
- **Công tố viên ($N2$ · Mèo):** F0 trung vị = **282.4 Hz**
- **Khoảng cách cao độ:**
  - $\Delta_{D \to H} = \mathbf{5.93\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)
  - $\Delta_{H \to C} = \mathbf{9.16\text{ nửa cung}}$ (Ngưỡng $\ge 4.0\text{ nc}$ — ĐẠT ✅)

### 3. Giám sát Độ chính xác (Whisper Base CER) & Tự nhiên (UTMOSv2 MOS)
- **Engine ASR:** `openai-whisper` (`base` model, CPU) qua chuẩn hóa `vi_cer`.
- **CER Trung vị:** **10.02%** (CER trung bình: **11.05%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 với seed mới cho toàn bộ các câu có CER > 2% và chọn take tối ưu.
- **Điểm tự nhiên UTMOSv2 MOS:** Trung bình **2.60 / 5.0** (Dải điểm: 1.65 – 3.42). Đạt chuẩn (>= 3.0 / 5.0).
- **Báo cáo câu cần nghe kiểm tra:** [`02_SAN_XUAT/Tap11/xuat_ban/CanNghe_Tap11_higgs.md`](xuat_ban/CanNghe_Tap11_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap11/xuat_ban/Tap11_master.mp3`](xuat_ban/Tap11_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap11/xuat_ban/Tap11_master.wav`](xuat_ban/Tap11_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [`.work/timeline_s_t11.json`](../../.work/timeline_s_t11.json) (2374.2 s)
   - Phụ đề SRT: [`02_SAN_XUAT/Tap11/xuat_ban/Tap11.srt`](xuat_ban/Tap11.srt) (272 cues)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [`.work/quality_qc_utmos_ep11_vi.json`](../../.work/quality_qc_utmos_ep11_vi.json)
   - Bảng câu nghe duyệt: [`02_SAN_XUAT/Tap11/xuat_ban/CanNghe_Tap11_higgs.md`](xuat_ban/CanNghe_Tap11_higgs.md)
