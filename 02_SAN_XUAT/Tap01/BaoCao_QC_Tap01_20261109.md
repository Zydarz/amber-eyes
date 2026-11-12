# BÁO CÁO QC · TẬP 01 (ẢNH TĨNH 3 NGÔN NGỮ) — 09/11/2026

**Phạm vi:** dựng lại **ảnh tĩnh** (stills) cho Tập 01 sau khi kịch bản được viết lại (205 câu, đồng bộ 1-1 cho VN/EN/JA).
**KHÔNG dựng video** (yêu cầu người dùng) — ảnh tĩnh là cổng QC trước khi dựng video (H18).

| Mục | Giá trị |
|---|---|
| Tiêu chuẩn | `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A) |
| Kịch bản | `01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md` · `.../Tap01_EN/kichban_tap01_EN.md` · `.../Tap01_JA/kichban_tap01_JA.md` |
| Bảng shot | `02_SAN_XUAT/Tap01*/KeHoach_Video_Tap01*.md` mục 6 — **203 dòng** |
| Ảnh tĩnh | `.work/video3/stills/` · `.work/video3_EN/stills/` · `.work/video3_JA/stills/` — **203 ảnh/ngôn ngữ, 1920×1080** |
| Công cụ | `.work/_t01/` (bộ dựng timeline + bảng shot + QC) + `.work/parse_shots.py` + `.work/build_video3.py --stills all` |
| Sao lưu trước khi ghi đè | `.work/_cu/t01_pre_new_20261109/` (timeline, shots, script, edition.py, 3 file kế hoạch) |

---

## 1. NGUỒN MỐC THỜI GIAN (đo thật, không ước lượng)

Master mp3 đã có sẵn (dựng 09/11/2026, khớp kịch bản mới) nên **không tạo TTS mới** (L4: không tốn credit).
Timeline dựng bằng ASR `faster-whisper small` trên chính master mp3, căn chỉnh 205 câu kịch bản vào transcript
bằng **độ phủ ký tự + mốc từ thật** (`.work/_t01/_t01_align4.py`).

| Ngôn ngữ | Thời lượng master | Câu khớp ≥ 0,45 | Cổng G1 (≥97%) | G2 đơn điệu | Câu yếu (nội suy) | G3 (câu cuối) |
|---|---|---|---|---|---|---|
| Tiếng Việt | 1753,36 s (29:13) | **205/205 (100%)** | ✅ | ✅ | 0 | 1743,1 s (còn 10,2 s) |
| Tiếng Anh | 1669,64 s (27:49) | **205/205 (100%)** | ✅ | ✅ | 0 | 1659,4 s (còn 10,3 s) |
| Tiếng Nhật | 1959,46 s (32:39) | **201/205 (98,0%)** | ✅ | ✅ | 4 (`1.13#1`, `2.04#6`, `2.07#8`, `3.08#7`) | 1948,9 s (còn 10,6 s) |

Mốc hồi (tiếng Việt): Hồi 2 · 06:08 · Hồi 3 · 11:53 · Hồi 4 · 16:46 · Hồi 5 · 22:30 — intro 0–22,41 s.

## 2. BẢNG SHOT

| Mục | Số liệu |
|---|---|
| Số dòng | **203** = 198 shot có lời + 4 thẻ chuyển hồi (T10) + 1 thẻ kết |
| Phủ câu | **205/205 câu** (không sót, không lặp) |
| Mẫu | T1 × 186 · T9 (thuật ngữ) × 8 · T10 (chuyển hồi) × 4 · T8 (cờ đỏ) × 4 · T7 (tuyến đường) × 1 |
| Nền | **44 ảnh** `assets/bg/` — **dùng chung tuyệt đối cho cả 3 ngôn ngữ** (H17) |
| Gom câu | 7 nhóm gồm 2 câu (câu < 3 s ở ít nhất 1 ngôn ngữ được gộp khi tổng ≤ 15 s ở cả 3 ngôn ngữ) |

## 3. KẾT QUẢ QC

| Mã | Nội dung | Tiếng Việt | Tiếng Anh | Tiếng Nhật |
|---|---|---|---|---|
| **H6/V3** | Chữ trên hình = **nguyên văn câu kịch bản** | ✅ 0 lỗi | ✅ 0 lỗi | ✅ 0 lỗi |
| **H13** | Khớp 3 chiều ảnh–chữ–lời; thứ tự câu | ✅ 0 mảnh chữ ngoài câu | ✅ | ✅ |
| **H9** | Độ tương phản chữ (>8% nét chữ bị "chìm" ⇒ bật `text_scrim`) | ✅ **0 shot** sau khi bật | ✅ **0 shot** | ✅ **0 shot** |
| **H10 vế 1** | Shot nội dung 3–15 s | ⚠️ xem §4 | ⚠️ xem §4 | ⚠️ xem §4 |
| **H10 vế 2** | Không lặp cùng 1 nền quá 4 shot liền | ✅ max 4 | ✅ max 4 | ✅ max 4 |
| **H12** | Thẻ kết có chữ | ✅ `5-41` 7,0 s — "HỒ SƠ TẬP 01 · ĐÃ ĐÓNG" | ✅ "CASE FILE 01 · CLOSED" | ✅ "事件ファイル 第01話 · 終結" |
| **H17** | Cùng tập nền giữa 3 ngôn ngữ | ✅ | ✅ | ✅ |
| **H18** | Ảnh tĩnh là cổng QC, chưa dựng video | ✅ 609 ảnh | | |
| — | Ảnh tĩnh đủ 1 ảnh/shot, không rỗng | ✅ 203/203 | ✅ 203/203 | ✅ 203/203 |

**H9 — chi tiết:** đo tương phản từng nét chữ trên nền (WCAG) cho 199 shot có chữ × 3 ngôn ngữ.
Lần đo đầu phát hiện chữ chìm; bật `text_scrim` (lớp tối mềm) cho **57 shot** (hợp cả 3 ngôn ngữ) trong `.work/edition.py`;
đo lại ⇒ **0 shot còn chữ chìm**.

## 4. NGOẠI LỆ H10 VẾ 1 (báo cáo trung thực)

Không thể đạt 100% vì luật H10 (shot 3–15 s) xung đột với H6/V3 (chữ phải nguyên văn câu kịch bản):
một câu mà ngôn ngữ nói **> 15 s** thì không thể tách thành 2 shot mà vẫn giữ nguyên văn.

| Ngôn ngữ | TB | Max | Shot > 15 s | Shot < 3 s |
|---|---|---|---|---|
| Tiếng Việt | 8,7 s | 21,4 s | 7 (`1-39` 16,6 · `1-40` 21,4 · `4-08` 17,1 · `4-21` 15,6 · `5-04` 20,2 · `5-35` 17,3 · `5-37` 15,1) | 2 (`1-05` 1,8 · `4-32` 2,5) |
| Tiếng Anh | 8,3 s | 15,7 s | 3 (`1-40` 15,4 · `5-29` 15,7 · `5-35` 15,3) | 0 |
| Tiếng Nhật | 9,8 s | 26,7 s | 15 | 2 (`1-38` 0,4 · `2-12` 0,8) |

Tổng cộng 17 shot vượt 15 s (trong đó nhiều shot chỉ vượt ở **một** ngôn ngữ) và 4 shot dưới 3 s — tất cả đều là
câu khiếu ngôn ngữ nói dài hoặc quá ngắn. Đã xử lý tối đa bằng cách gộp câu ngắn (7 nhóm 2 câu) khi tổng ≤ 15 s ở cả 3 ngôn ngữ.

## 5. VẤN ĐỀ KỸ THUẬT PHÁT HIỆN KHI LÀM (ảnh hưởng bước dựng video sau này)

1. **Master mp3 Tập 01 KHÔNG có khoảng lặng** (đo: khoảng lặng dài nhất 0,96 s; tổng im lặng 6,26 s / 1753 s;
   trung vị nghỉ giữa câu chỉ 0,05 s). Script chuẩn `build_audio3.py` có `GAP_SENT = 0,35 s` và `GAP_ACT = 2,0 s`
   ⇒ master hiện tại **không được dựng bằng script chuẩn** (hoặc đã bỏ pause).
   → Hệ quả: **thẻ hồi T10 không có chỗ trống để nằm** ⇒ 4 thẻ hồi (2,0 s) **chồng lên lời đầu hồi sau**.
   → Việc cần làm trước khi dựng video: dựng lại master có pause (đúng `build_audio3.py`) hoặc cắt bớt lời.
2. **Thẻ kết** kéo dài về `TOTAL − 7,0 s` ⇒ ảnh tĩnh chụp giữa shot **không bị mờ đen** (H12 ✅).
3. Bảng shot cũ (mã `1-04`, `2-13`…) **không còn tồn tại** ⇒ đã xoá `COMBO` / `INSET` / `BG2` / `flag_hold_shots`
   cũ của Tập 01 trong `.work/edition.py`; nền ghi thẳng ở cột *Nền*.
4. **Ảnh tĩnh của shot nhiều đoạn phải chụp SAU khi đoạn cuối hiện xong.** Chụp đúng giữa shot có thể rơi vào
   lúc đoạn sau đang "mờ dần" (fade-in 0,35 s) ⇒ chữ đoạn sau bị mờ trong ảnh (đã thấy ở `2-11`).
   Đã vá `.work/build_video3.py`: `t = max(thời điểm các đoạn) + 0,6 s` (kẹp trong `[start, end−0,15]`) cho shot ≥ 2 đoạn.
   ⇒ ảnh tĩnh luôn có **đủ chữ** của shot.

## 6. SOI TAY (contact sheet)

`.work/qc_final_t01/sheet_vi/` · `sheet_en/` · `sheet_ja/` — 17 tờ/ngôn ngữ, 12 ảnh/tờ (620×349 mỗi ảnh).

## 7. CÒN LẠI TRƯỚC KHI ĐĂNG

- [ ] Dựng video từ bảng shot mới (3 ngôn ngữ) — **cần xử lý khoảng lặng ở §5.1 trước**
- [ ] Sinh lại phụ đề (`.srt`) + mô tả + thumbnail từ timeline mới
- [ ] Điền nguồn cho 9 mã câu trong `need` của `edition.py`
- [ ] Người dùng nghe toàn tập (master mp3 đã đổi theo kịch bản mới)
