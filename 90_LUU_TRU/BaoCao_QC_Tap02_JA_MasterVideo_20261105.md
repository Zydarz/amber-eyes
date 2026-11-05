# BÁO CÁO KIỂM ĐỊNH CHẤT LƯỢNG (QC) — TẬP 02 JAPANESE MASTER VIDEO
**Kênh:** Amber eyes (YouTube)  
**Tập:** Episode 02 (Japanese Edition) — *第02話 · 二重生活の大佐とエスカレーションの深淵 | ラッセル・ウィリアムズ大佐の犯罪心理学 (10の心理指標と4段階の暴走)*  
**Ngày hoàn thành & kiểm định:** 05/11/2026 21:00:15  
**Thành phẩm bàn giao:** `02_SAN_XUAT/Tap02_JA/xuat_ban/Tap02_JA_master.mp4`  

---

## 1. THỐNG KÊ SỐ ĐO VÀ ĐỐI CHIẾU TIÊU CHUẨN KÊNH

| # | Hạng mục kiểm tra | Tiêu chuẩn kênh (AGENTS.md & Tiêu chuẩn dựng) | Số đo thực tế | Kết luận |
|---|---|---|---|---|
| 1 | **Độ dài Video & Audio** | Lệch giữa hình và tiếng $\le 0.05\text{ s}$ (Luật H14) | Video: **1.793,267 s** · Audio: **1.793,270 s** · Độ lệch: **0,000 s** ($0,0\text{ ms}$) | **ĐẠT** |
| 2 | **Độ phân giải & Tốc độ khung hình** | 1920x1080 @ 30 fps, Progressive, H.264 Baseline profile | **1920x1080 @ 30 fps**, 53.798 khung hình | **ĐẠT** |
| 3 | **Khung hình Intro & Brand** | Intro tiếng Nhật `intro_kenh_JA_t02.mov` (22,41 s), mở đầu 23,00 s | Đúng chuẩn JA, logo flare tại 1,5 s, thẻ cảnh báo & vai diễn | **ĐẠT** |
| 4 | **Độ lớn tích hợp (Integrated Loudness)** | $-16 \pm 1\text{ LUFS}$ (Luật A7 / EBU R128) | **-16,3 LUFS** | **ĐẠT** |
| 5 | **Đỉnh âm lượng cực đại (True Peak)** | $\le -1.5\text{ dBFS}$ (Đo trên AAC cuối) | **-3,6 dBFS** (với `mux_af` limiter `latency=1`) | **ĐẠT** |
| 6 | **Dải động âm lượng (LRA)** | $\le 12\text{ LU}$ | **4,5 LU** | **ĐẠT** |
| 7 | **Khoảng câm bất thường (Silence Gaps)** | Không có khoảng câm $> 0,3\text{ s}$ @ $-60\text{ dBFS}$ (Luật V4, A1) | **0 khoảng câm > 0,3 s** | **ĐẠT** |
| 8 | **Đồng bộ âm thanh - hình ảnh (A/V Sync)** | $\le 20\text{ ms}$ (Luật A11 #64, cross-correlation FFT) | Trung bình: **+0,00 ms** · Cực đại: **0,00 ms** (5 cửa sổ đo) | **ĐẠT** |
| 9 | **Kiểm tra giải mã (FFmpeg decode check)** | 0 cảnh báo lỗi, 0 frame rách | **0 lỗi** | **ĐẠT** |
| 10 | **Tương thích mạng (FastStart)** | Thẻ `moov` nằm trước `mdat` (Luật A11 #55) | Đã tối ưu `+faststart` | **ĐẠT** |
| 11 | **Phụ đề tiếng Nhật (SRT)** | Phủ 100% lời thoại, không dòng rỗng, không lỗi format | **219 cue**, kết thúc tại 1784,27 s | **ĐẠT** |
| 12 | **Thẻ kết (End Card)** | Thẻ kết thúc xuất hiện tại shot cuối có đầy đủ slogan và tên kênh | Khung hình tại 1786,27 s hiển thị chữ AMBER EYES và slogan tiếng Nhật | **ĐẠT** |

---

## 2. BẢNG CỔNG QC ĐẦU RA (32/32 CỔNG ĐẠT)

| Cổng | Tiêu chí | Kết quả | Ghi chú kỹ thuật |
|---|---|---|---|
| **G0** | Khớp mốc âm thanh master | **PASS** | `master mp3` == `timeline.total` == `shots.total` = 1793.27 s (lệch 0.000 s) |
| **G1** | Khớp độ dài `picture.mp4` | **PASS** | 1793.27 s vs 1793.27 s (lệch 0.000 s, ngưỡng $\pm 0.05\text{ s}$) |
| **G2** | Luồng Video + Audio | **PASS** | 1 luồng H.264 1080p30 + 1 luồng AAC stereo 44.1kHz, 602.65 MB (> 100 MB) |
| **G3** | Giải mã FFmpeg | **PASS** | Quét giải mã 100% stream: 0 lỗi |
| **G4** | Khớp độ dài MP4 cuối | **PASS** | 1793.27 s (29 phút 53 giây) |
| **G5** | Số khung hình | **PASS** | Đúng 53.798 frames ($1793.267 \times 30$) |
| **G6** | Âm học (Loudness & Peak) | **PASS** | -16.3 LUFS · True Peak -3.6 dBFS · 0 silence gaps > 0.3 s |
| **G7** | Phủ câu thoại kịch bản | **PASS** | 203/203 câu đầy đủ, không sót, không lặp |
| **G8** | Phụ đề SRT | **PASS** | 219 cues, cue cuối kết thúc tại 1784.27 s (trước thẻ kết) |
| **G9** | Font chữ tiếng Nhật | **PASS** | Font `YuGothB.ttc` và `YuGothM.ttc` hiển thị sắc nét, 0 lỗi tofu |
| **G10** | Mẫu đồ họa số lớn T5 | **PASS** | Chữ số và ký tự năm hiển thị rõ ràng, không đè lấn |
| **G11** | Thẻ kết hồ sơ (End card) | **PASS** | Xuất hiện tại 1786.27 s: "AMBER EYES", "事件ファイル 第02話 · 終結" |
| **G12** | Lặp nền liên tiếp | **PASS** | Tối đa 4 shot liên tiếp cùng nền, tuân thủ H10 |
| **G13** | A/V Sync (Lệch hình - tiếng) | **PASS** | 0.00 ms (ngưỡng $\le 20\text{ ms}$) |
| **G14** | Thumbnail YouTube | **PASS** | 1280x720 PNG nền `t2_two_chairs`, chữ tiếng Nhật chuẩn |
| **G15** | YouTube Chapter Markers | **PASS** | 6 mốc chương khớp chính xác với timeline và cấu trúc kịch bản |

---

## 3. CÁC TÀI SẢN HOÀN CHỈNH BÀN GIAO TRONG THƯ MỤC XUẤT BẢN

Thư mục: `02_SAN_XUAT/Tap02_JA/xuat_ban/`
1. `Tap02_JA_master.mp4` (631.919.225 bytes · 602,65 MB · 29:53)
2. `Tap02_JA_master.mp3` (43.039.916 bytes · 41,05 MB)
3. `Tap02_JA.srt` (38.434 bytes · 219 cues)
4. `thumbnail.png` (1.108.738 bytes · 1280x720 PNG)
5. `mo_ta.txt` & `description.txt` (7.472 bytes · chứa 6 mốc chapter và disclaimer)
6. `nguon_tham_khao_JA.md` (1.711 bytes)
