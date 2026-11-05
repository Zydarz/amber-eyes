# BÁO CÁO SẢN XUẤT VÀ KIỂM ĐỊNH CHẤT LƯỢNG — TẬP 06 (ENGLISH EDITION)

> **Hồ sơ vụ án:** The Killer Clown — John Wayne Gacy (Chicago, Illinois, 1978)  
> **Ngôn ngữ:** Tiếng Anh (English)  
> **Ngày hoàn thành:** 04/11/2026  
> **Người thực hiện:** Antigravity Pairing AI  
> **Tuân thủ quy chuẩn:** `AGENTS.md` (L1–L10, H1–H14, A1–A12, G1–G13) & `TIEU_CHUAN_DUNG_VIDEO.md`  

---

## 1. TỔNG QUAN THÀNH PHẨM SẢN XUẤT

| Thành phẩm | Đường dẫn | Thông số kỹ thuật | Trạng thái |
|---|---|---|---|
| **Video Master** | `02_SAN_XUAT/Tap06_EN/xuat_ban/Tap06_EN_master.mp4` | 1920x1080 @ 30 fps · 38.506 frames · 453.63 MB · H.264/AAC | **HOÀN THÀNH** |
| **Audio Master** | `02_SAN_XUAT/Tap06_EN/xuat_ban/Tap06_EN_master.mp3` | 1283.54 s · 48 kHz stereo · 192 kbps · Higgs Audio v3 | **HOÀN THÀNH** |
| **Phụ đề SRT** | `02_SAN_XUAT/Tap06_EN/xuat_ban/Tap06_EN.srt` | 365 cues · Phủ 100% 165 câu thoại có Speaker Tag | **HOÀN THÀNH** |
| **Thumbnail** | `02_SAN_XUAT/Tap06_EN/xuat_ban/thumbnail.png` | 1280x720 · PNG 1.17 MB · Chuẩn nhận diện Amber Eyes | **HOÀN THÀNH** |
| **Bảng Shot** | `02_SAN_XUAT/Tap06_EN/KeHoach_Video_Tap06_EN.md` | 73 shot chuẩn · 5 hồi · Phủ 165 câu tuần tự | **HOÀN THÀNH** |

---

## 2. BẢNG SỐ ĐO THỰC TẾ (TUÂN THỦ LUẬT L3 & QC A9.1–A9.4)

Mọi tiêu chí kỹ thuật đều được đo đạc trực tiếp trên file thành phẩm cuối:

| Tiêu chuẩn / Hạng mục | Ngưỡng yêu cầu | Số đo thực tế | Kết luận |
|---|---|---|---|
| **Thời lượng Video vs Timeline** | Lệch $\le \pm 0.05\text{ s}$ | $1283.533\text{ s}$ vs $1283.540\text{ s}$ (lệch **$0.0067\text{ s}$**) | **ĐẠT (PASS)** |
| **Độ lệch Hình / Tiếng (A/V Sync)** | Lệch $\le \pm 0.05\text{ s}$ | $1283.533\text{ s}$ vs $1283.520\text{ s}$ (lệch **$0.0133\text{ s}$**) | **ĐẠT (PASS)** |
| **Độ nguyên vẹn giải mã (Decode)** | 0 lỗi frame | **0 errors** / 38.506 frames (`ffprobe/ffmpeg -f null`) | **ĐẠT (PASS)** |
| **Độ lớn tích lũy (Loudness)** | $-16 \pm 1.0\text{ LUFS}$ | **$-16.39\text{ LUFS}$** | **ĐẠT (PASS)** |
| **Đỉnh thật âm thanh (True Peak)** | $\le -1.5\text{ dBFS}$ | **$-3.39\text{ dBFS}$** | **ĐẠT (PASS)** |
| **Dải động âm thanh (LRA)** | $\le 11\text{ LU}$ | **$3.60\text{ LU}$** | **ĐẠT (PASS)** |
| **Khoảng lặng âm thanh (Silence)** | 0 đoạn câm $> 0.3\text{ s}$ @ $-60\text{ dBFS}$ | **0 đoạn câm** | **ĐẠT (PASS)** |
| **Phủ câu thoại (H14)** | Phủ 100% câu đúng thứ tự | **165/165 câu** ($1.02\#1 \to 5.06\#19$) | **ĐẠT (PASS)** |
| **Khớp chữ & câu thoại (H6, V3)** | Chữ trích từ câu đang đọc | **100% khớp** chính xác từng shot | **ĐẠT (PASS)** |
| **Thẻ kết hồ sơ (H12)** | Có nhãn đóng hồ sơ + AMBER EYES | **Đạt** (Shot 5-14 hiển thị thẻ kết thương hiệu) | **ĐẠT (PASS)** |

---

## 3. CÁC QUYẾT ĐỊNH KỸ THUẬT QUAN TRỌNG

1. **Forced Alignment đa luồng bất đồng bộ trên Windows Speech Recognition:**
   - Xử lý nhận diện và căn chỉnh mốc thời gian tuyệt đối của 165 câu thoại tiếng Anh từ master audio trong thời gian 42.6 s, sai số định vị $< 0.02\text{ s}$.
2. **Audio Stems cho Avatar Badge:**
   - Trích xuất waveform từ audio master thành các stem riêng biệt theo vai (`H`, `D`, `C`, `N1`, `N2`) để hiển thị avatar badge mấp máy chân thực đúng lúc từng nhân vật cất tiếng.
3. **Muxing với Limiter có bù trễ (`latency=1`):**
   - Áp dụng chuỗi lọc `alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1` để kiểm soát True Peak của AAC không vượt quá $-1.5\text{ dBFS}$ (kết quả đạt $-3.39\text{ dBFS}$) mà không gây lệch 5 ms giữa hình và tiếng.
4. **Tách vai khách mời:**
   - Phân định rõ `N1` (Kim Byers - Đồng nghiệp hiệu thuốc) và `N2` (Mike Albrecht - Điều tra viên giám sát) trong kịch bản và timeline, kích hoạt chuẩn avatar và bảng tên khách mời.
