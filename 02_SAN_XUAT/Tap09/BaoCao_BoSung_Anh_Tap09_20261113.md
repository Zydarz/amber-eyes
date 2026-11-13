# BÁO CÁO BỔ SUNG ẢNH GỐC — TẬP 09 · 13/11/2026

**Tập 09:** "Nghệ Thuật Xóa Bỏ Bản Ngã" (Charles Manson & Thảm kịch Gia đình Manson, Los Angeles, 1969)  
**Phạm vi lượt này:** **CHỈ sinh ảnh gốc (nền)** + cập nhật bảng ánh xạ nền. **KHÔNG render chữ, KHÔNG đụng audio/timeline** (theo quyết định của người dùng 13/11/2026).  
**Quy chuẩn áp dụng:** `AGENTS.md` (L1–L10, H1–H20, A1–A13), `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (A11 #156–#158).

---

## 1. Điều tra: kịch bản đã thay đổi thế nào

| Nguồn | Số câu | Ghi chú |
|---|---|---|
| Kịch bản VN `01_KICH_BAN/Tap09/kichban_tap09_23102026.md` (sửa 13/11 07:55) | **207** | commit `4f390af` lúc 08:07 — đã vào HEAD |
| Bản trước đó (`HEAD~1`, bản đã dựng video 11/11) | 199 | master mp3 + timeline + 196 ảnh tĩnh đều theo bản này |
| Kịch bản EN `01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md` | **199** | chưa cập nhật — người dùng sẽ tự sửa |
| Kịch bản JA `01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md` | **199** | chưa cập nhật — người dùng sẽ tự sửa |
| Timeline VN `timeline_s_t09.json` | 199 mục | thiếu 9 mã câu mới, thừa 1 mã |

**Bảng mã câu thay đổi (OLD `HEAD~1` → NEW `HEAD`), khớp theo văn bản nguyên văn:**

| Element | Câu cũ | Câu mới | Câu mới thêm / viết lại |
|---|---|---|---|
| 1.02 | 5 | 8 | +3 — niềm tin mù quáng · truyền thông ca ngợi tự do · kẽ hở cho kẻ săn mồi |
| 1.04 | 7 | 7 | #6 viết lại (“xinh đẹp” → “tài hoa”) |
| 1.12 | 4 | 4 | #1 viết lại (“Amber Eyes” → “Amber eyes”) |
| 2.06 | 13 | 14 | +1 ở #8 (ngưỡng dung nạp), #13 gộp 2 câu, +1 ở #14 (Linda Kasabian) |
| 3.08 | 10 | 11 | #3–#5 bỏ ngoặc tiếng Anh, +2 câu (#7–#8), #9–#10 gộp |
| 4.05 | 7 | 8 | +3 câu lời kể Kasabian (#5–#7), #8 gộp |
| 4.09 | 7 | 9 | viết lại toàn bộ: phiên tòa 1970 · chữ X · cách ly xà lim · Chấn thương Đạo đức |
| 5.04 | 5 | 6 | +3 câu Doris Tate / Quyền Nạn nhân (#2–#4), #5 gộp |
| 5.05 | 8 | 7 | #3–#4 viết lại, #5 cũ bị bỏ |
| 5.07 | 10 | 10 | #1 viết lại |

**Hệ quả trực tiếp:** `BG_FIX` gắn nền theo **mã câu** ⇒ chỉ cần chèn 3 câu ở đầu 1.02 là mọi mã câu phía sau trong hồi 1 trở đi lệch ⇒ bảng nền cũ rơi sang sai câu.

---

## 2. Việc đã làm

### 2.1 Sinh 3 ảnh nền mới cho đoạn Doris Tate / Quyền Nạn nhân (5.04)

| Tên file | Nội dung cảnh (H19 — cảnh cụ thể) | Gán cho câu | Trạng thái |
|---|---|---|---|
| `t9_doris_tate_public_podium` | Bà cụ đứng sau bụi diễn đàn, ngược sáng thành bóng, đèn chiếu xuyên sương mù, ghế trống chìm trong tối | `5.04#2` | **CHỜ CREDIT** |
| `t9_blank_paper_pile_stamp_desk` | Bàn gỗ chất đống giấy trắng trơn, hộp dấu cao su + mực đỏ, bút máy, ánh sáng cửa sổ xiên | `5.04#3` | **CHỜ CREDIT** |
| `t9_victim_family_testimony_chair` | Phòng xét ân xá gỗ tối, một ghế nhân chứng rỗng trong vũng sáng, micro đứng, ghế hàng bóng tối | `5.04#4` | **CHỜ CREDIT** |

Prompt viết theo H5 — **không nhắc tên riêng, không nhắc nhãn, không nhắc con số** (chỉ mô tả bề mặt trưng + "completely blank and unmarked"), kèm NEG mạnh cho nhóm có giấy/bìa. Ba nền này thuộc `STRONG` trong `_t09_gen_bg_minimax.py`.

### 2.2 Cập nhật bảng ánh xạ nền `BG_FIX` → 207 mục

| Kiểm tra | Kết quả |
|---|---|
| Số mục `BG_FIX` | **207/207** câu đều có nền |
| Nền cũ trên đĩa được gán ≥ 1 lần | **65/65** ✅ (không nền nào bị bỏ mồ côi) |
| Nền được gán nhưng chưa có file | 3 (đúng 3 nền mới đang chờ sinh) |
| H10 vế 2 — đoạn lặp nền dài nhất (xấp xỉ trần trên "1 câu = 1 shot") | **3 shot** ≤ 4 ✅ |

Sao lưu trước khi sửa: `.work/_cu/t09_bgfix_20261113/_t09_gen_table.py`.

### 2.3 Ghi bài học vào tiêu chuẩn (L6)

Đã thêm **#156–#158** vào bảng A11 (`00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md`): kịch bản sửa sau khi xuất bản ⇒ mã câu dịch chuyển · kịch bản đang sửa dở thì chỉ sinh ảnh gốc · MiniMax hết credit khi sinh nền mới cho tập đã có checkpoint. `_check_md_tables3.py` → **ERROR 0**.

---

## 3. Trạng thái 3 ảnh nền mới — ĐANG CHỜ NẠP CREDIT

MiniMax trả lỗi: `image generation needs at least 100 credits ... available before it starts` ⇒ số dư credit hiện tại < 100 credit.

Đã bật **supervisor nền**: `.work/_t09/_t09_gen_supervisor.py` (nghỉ 180 s/vòng, tối đa 8 giờ). Người dùng chỉ cần **nạp credit là 3 ảnh tự sinh**, không phải canh.

| Vòng | Thời điểm | Kết quả |
|---|---|---|
| 0 | 08:14 | lỗi thiếu credit |
| 1 | 08:17 | lỗi thiếu credit |
| 2 | 08:20 | lỗi thiếu credit (đang retry) |

> **Còn 1 bước bắt buộc sau khi có ảnh: soi bằng mắt (H2/H5/H19).** Cổng grep prompt báo XANH không đủ — MiniMax vẫn có thể vẽ chữ lên giấy/dấu. Có 1 tờ montage 900 px là đủ soi 3 ảnh này.

---

## 4. Việc còn lại (KHÔNG thuộc lượt này — chờ người dùng)

Sau khi kịch bản EN và JA đủ 207 câu:

1. Dựng lại audio 3 ngôn ngữ (master mp3) cho phần đổi → đo lại timeline (9 mã câu mới VN + tương ứng EN/JA).
2. Chạy `_t09_gen_table.py` (self-test đã sửa `199` → `N_CAU = 207`) → sinh bảng shot 3 ngôn ngữ.
3. `parse_shots.py` → `shots_t09 / shots_EN_t09 / shots_JA_t09`.
4. Render ảnh tĩnh 3 ngôn ngữ (mã shot dịch ⇒ phải render lại, không render được bản vá lẻ).
5. QC: H9 (đo lại toàn bộ vì nền MiniMax sáng hơn), H10, A9.2, T25, soi mắt.
6. Cập nhật `provenance.json` cho 3 nền mới (script tự ghi khi sinh) + báo cáo cuối.

**Lưu ý lịch sử:** video Tập 09 đã xuất bản 11/11 từ bản 199 câu (`Tap09.mp4` 549,4 MB · `Tap09_EN.mp4` 519,2 MB · `Tap09_JA.mp4` 623,2 MB) ⇒ **thành phẩm hiện tại không khớp kịch bản 207 câu**; cần dựng lại khi kịch bản 3 ngôn ngữ chốt.

---

## 5. Danh mục file đã đụng

| File | Trạng thái |
|---|---|
| `.work/_t09/bg_jobs_t09.json` | M — thêm 3 job nền mới (68 job) |
| `.work/_t09/_t09_gen_bg_minimax.py` | M — thêm 3 tên vào nhóm `STRONG` (NEG mạnh) |
| `.work/_t09/_t09_gen_table.py` | M — `BG_FIX` 199 → 207 mục; self-test `199` → `N_CAU` |
| `.work/_t09/_t09_add_bg_jobs_t09_b.py` | Mới — thêm job nền (có backup trước) |
| `.work/_t09/_t09_gen_supervisor.py` | Mới — supervisor chờ nạp credit |
| `.work/_t09/_t09_patch_bgfix_207.py` | Mới — dựng lại khối `BG_FIX` |
| `.work/_t09/_t09_check_h10_207.py` | Mới — đo H10 + sửa self-test |
| `.work/_t09/_t09_map_old_new.py` | Mới — bảng ánh xạ OLD → NEW |
| `.work/_t09/_t09_diff_state.py` | Mới — đối chiếu md / JSON / HEAD / timeline |
| `.work/_t09/_t09_check_sync.py` | Mới — đối chiếu script vs timeline |
| `.work/_t09/_t09_show_new_elements.py` | Mới — in cấu trúc câu theo element |
| `.work/_t09/_t09_add_lessons_156.py` | Mới — thêm #156–#158 vào A11 |
| `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` | M — thêm #156–#158 |

**Sao lưu:** `.work/_cu/t09_bg_jobs_20261113/` · `.work/_cu/t09_bgfix_20261113/` · `.work/_cu/t09_lessons_20261113/` · `.work/_cu/t09_bg_20261113/`
