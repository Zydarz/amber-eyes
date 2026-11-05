# BÁO CÁO QC — TẬP 02 (VI) · RENDER LẠI ẢNH TĨNH THEO KỊCH BẢN VIẾT LẠI 05/11/2026

**Ngày:** 05/11/2026 · **Phạm vi:** bảng shot + timeline + ảnh tĩnh mọi shot (VN) · **Trạng thái:** xong, chờ người dùng duyệt

---

## 1. Vì sao phải làm lại

Kịch bản `01_KICH_BAN/Tap02/kichban_tap02_22102026.md` đã viết lại (bản 10 chỉ dấu tâm lý, 05/11 08:51). So với bản dùng để dựng video cũ (25/10):

| Đo | Cũ | MỚI |
|---|---:|---:|
| Element | 63 | 63 (không đổi) |
| Câu | 203 | 203 (không đổi) |
| Element **đổi số câu** | — | **17** (1.05 · 1.08 · 1.12 · 1.14 · 1.17 · 2.07 · 2.08 · 3.05 · 3.07 · 3.08 · 3.10 · 3.11 · 4.08 · 5.06 · 5.07 · 5.08 · 5.10) |
| Câu **đổi nội dung** (giữ nguyên số câu) | — | **134** câu |
| Bảng shot cũ phủ câu | 203/203 | **15 câu mới không được phủ, 15 câu cũ thừa** ⇒ bảng shot cũ KHÔNG dùng được |

⇒ Bảng shot và timeline phải sinh lại. Không sửa chữ trên hình thì hình sẽ nói sai lời (vi phạm H3/V3).

## 2. Đã làm

1. **Bảng shot (hồ sơ mục 6)** — viết lại 17 khối dòng theo kịch bản mới, sửa 25 dòng chữ trên hình còn cũ, tách 3 shot > 20 s, sửa 3 dòng trỏ nền không tồn tại, đánh lại mã shot (1-01…5-36).
2. **Timeline** — dựng lại theo câu mới (`.work/_build_timeline_t02_new.py`).
3. **Sinh lại `shots_t02.json`** — 161 shot.
4. **QC bảng shot** (`.work/_qc_tap02_shots.py`) — 10/10 cổng xanh.
5. **Render ảnh tĩnh mọi shot** — 161 ảnh, 211 s → `.work/video3_t02/stills/`.
6. **Contact sheet** 18 trang — `.work/qc_t02_20261105/contact_sheet/`.

## 3. Số đo

| Đo | Kết quả |
|---|---|
| Shot | **161** (144 có lời + 17 dòng nghỉ) |
| Câu được phủ | **203/203**, đúng thứ tự, không câu nào thuộc 2 shot |
| Tổng thời lượng | 1411,87 s (23:31) — **giữ nguyên** như bản cũ |
| Thời lượng shot | TB 8,6 s · ngắn nhất 1,3 s · dài nhất 22,6 s (shot `3-15`) |
| Shot > 15 s | 18 (xem mục 5) |
| Shot < 3 s | 24 — gần như toàn bộ là **dòng nghỉ/đổi hồi** (1,3–2,9 s) |
| Chuỗi nền liên tiếp dài nhất | **4 shot** (giới hạn: không > 4) ✅ |
| Mẫu khung dùng | T1×83 · T4×14 · T3×14 · T2×12 · T9×11 · T5×10 · T8×10 · T10×5 · T7×1 · T6×1 |
| Câu theo vai | H=97 · D=53 · C=45 · N1=4 · N2=4 |
| Nền thiếu file | 0 |
| Render ảnh tĩnh | 161/161 · 211 s |

### Cổng QC bảng shot — tất cả xanh

```
[OK] Mọi câu trong timeline có mặt trong bảng shot — thiếu [] · thừa []
[OK] Không câu nào thuộc hai shot
[OK] 203 câu được phủ — 203/203
[OK] Thứ tự shot khớp thứ tự kịch bản
[OK] Cột Vai khớp người nói trong timeline
[OK] Mọi nền dùng trong shot đều có file
[OK] Chữ trích dẫn nguyên văn (lược bằng …) trong câu — V3
[OK] Mọi con số trên hình có trong câu — A9.2
[OK] Không từ cấm / không nhắc hành vi tình dục trên hình
[OK] Shot > 15 s có nhịp hoặc bám V2
[OK] Các shot liền nhau (không hở/chồng)
```

## 4. Lỗi đã phát hiện và sửa trong quá trình làm

| Lỗi | Số | Xử lý |
|---|---:|---|
| Chữ trên hình không còn khớp câu mới (tiêu đề rút gọn) | 23 shot | Sửa lại chữ (VD `2-01` "KHÁM XÉT" → "MỘT VỤ ÁN ĐƠN LẺ"; `4-27` → "MẶT NẠ DANH DỰ VỠ VỤN") |
| Trích dẫn không nguyên văn câu mới | 5 shot | Lấy lại đúng câu (`1-10`, `1-12`, `4-07`, `4-08`, `4-14`) |
| Số trên hình không có trong câu | 2 shot | `3-06` ("3 tầng" → "Các tầng cơ chế"); `5-09` ("25 NĂM" → "HAI MƯƠI LĂM NĂM PHỤC VỤ" — câu đọc bằng chữ) |
| Từ cấm trên hình | 1 shot | `3-15` "MÁU LẠNH" → "MỘT KẺ KHÁC HOÀN TOÀN" |
| Nền `t2_bedroom_intruder` **không tồn tại** | 3 dòng | Sửa thành `bedroom_door` (trước đó âm thầm kế thừa nền shot trước) |
| Shot 33 s | 1 | Tách thành 2 shot (3.11#5 / 3.11#6) |
| Shot 21 s | 2 | Tách (5.10#1–#3 → 2 shot; 5.10#5–#7 → 2 shot) |

## 5. Việc CẦN LÀM để ra video cuối (chưa làm — cần người dùng quyết)

| # | Việc | Vì sao chưa làm |
|---|---|---|
| 1 | **Đọc lại giọng TTS** (Higgs Kaggle hoặc MiniMax) cho 203 câu | Audio VN đã bị xoá sau khi đăng tập (mục 11). 134 câu đổi nội dung ⇒ **không thể dùng lại audio cũ** |
| 2 | **Đo lại timeline** từ audio mới | Timeline trong báo cáo này là **timeline TẠM**: giữ khung thời gian từng element theo audio cũ, chia lại trong element theo số từ. Chưa phải mốc đo thật |
| 3 | **Sinh lại `stems_t02`** | Stem giọng VN đã xoá; bản dùng cho ảnh tĩnh là **file proxy của bản JA** (chỉ sóng âm trang trí trên badge). Video thật bắt buộc dùng stem tiếng Việt |
| 4 | **Sinh lại `.srt`** | `subtitles.py` đọc timeline → chạy lại sau khi có audio mới |
| 5 | Cân nhắc tách tiếp 18 shot > 15 s | Shot dài nhất còn lại `3-15` (22,6 s) là **1 câu** (3.07#1) — kịch bản mới gộp 3 câu cũ thành 1 câu hỏi dài, không tách được nếu không sửa kịch bản |
| 6 | Bản EN / JA / KO | Kịch bản 3 ngôn ngữ kia cũng đã viết lại nhưng **chưa** sửa bảng shot của chúng (hồ sơ riêng: `KeHoach_Video_Tap02_EN.md` / `_JA` / `_KO`) |

## 6. File sinh ra / sửa

| File | Trạng thái |
|---|---|
| `02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md` | **đã sửa** (bảng shot mục 6 + tham chiếu shot-id trong văn bản) |
| `.work/shots_t02.json` | **đã sinh lại** — 161 shot |
| `.work/timeline_s_t02.json` | **đã sinh lại** (timeline tạm — xem mục 5 #2) |
| `.work/video3_t02/stills/shot_*.png` | **161 ảnh** mới |
| `.work/qc_t02_20261105/contact_sheet/sheet_01..18.png` | 18 trang duyệt |
| `.work/_cu/shot_table_t02_20261105_135553/` | backup bảng shot + timeline + script trước khi sửa |
| `.work/_cu/shot_table_fix_t02_20261105_1401*/`, `_cu/shot_table_split_t02_20261105_140322/`, `.work/_cu/timeline_t02_20261105_135648/` | backup từng bước |

## 7. Cách duyệt nhanh

Mở `contact_sheet/sheet_01.png` → `sheet_18.png`: mỗi ô có mã shot, thời lượng, tên nền. Cần soi kỹ thì mở `.work/video3_t02/stills/shot_<mã>.png` (1920×1080).

Ưu tiên soi: **Hồi 1** (1-05 → 1-09 nội dung mới về Trenton/linh cữu/Hiệu ứng Hào quang) · **Hồi 3** (3-06 → 3-12 tầng cơ chế) · **Hồi 5** (5-13 → 5-22).
