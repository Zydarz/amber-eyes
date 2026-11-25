# HỒ SƠ SẢN XUẤT TẬP 32 · "TRƯƠNG TỬ CƯỜNG" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap32/kichban_tap32_22112026.md`
**File kịch bản phân rã:** `.work/script_tap32.json`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Ho_So_Toi_Pham/Tap32/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 32: Hồ Sơ Trương Tử Cường — Tướng Cướp Thế Kỷ & Tâm Lý Con Bạc Bệnh Lý Hồng Kông |
| **Đề tài** | Chuỗi vụ án cướp xe bọc thép chở tiền tại sân bay Khải Đức và bắt cóc tống tiền con trai Lý Gia Thành (Lý Trạch Cự), Quách Bính Tương thu về gần 2 tỷ HKD do Trương Tử Cường (Cheung Tsz-keung) thực hiện; bị bắt và thi hành án tử hình tại Quảng Đông năm 1998 |
| **Trọng tâm tâm lý (K10)** | Tâm lý Con bạc bệnh lý (Pathological Gambling), Sự thèm khát Adrenaline & Ảo tưởng quyền lực tối thượng (God Complex), Chiến thuật tâm lý đối đầu hệ thống pháp luật và Điểm mù tư pháp xuyên biên giới. |
| **Số câu kịch bản** | **240 câu** (Đo lường chính xác bằng `parse_kichban.py`) |
| **Phân bổ theo vai** | Host (Cú): 85 câu · Điều tra viên (Sói): 77 câu · Chuyên gia tâm lý (Cáo): 62 câu · Người bình thường (N): 16 câu |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Cận vệ / Nhân chứng (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung toàn diện vào đấu trí tâm lý, phân tích động cơ hành vi và bài học an ninh bảo vệ). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1 (61 câu):** Tướng cướp thế kỷ Trương Tử Cường, xuất thân Du Ma Địa, vụ cướp sân bay Khải Đức năm 1991 và màn kháng cáo đòi bồi thường 8 triệu HKD chấn động.
* **Hồi 2 (51 câu):** Đòn cân não đàm phán một mình mang thuốc nổ vào dinh thự tỷ phú Lý Gia Thành và vụ bắt cóc thế kỷ thu 1,38 tỷ HKD.
* **Hồi 3 (49 câu):** Cơn nghiện adrenaline và sòng bạc không đáy tại Ma Cao, vòng xoáy tự hủy diệt của kẻ khát bạc bệnh lý, vụ bắt cóc Quách Bính Tương.
* **Hồi 4 (39 câu):** Kế hoạch mua hơn 800 kg thuốc nổ, bẫy lưới chuyên án 9810 tại Quảng Đông, sự sụp đổ của ảo tưởng quyền lực và giới hạn tư pháp xuyên biên giới.
* **Hồi 5 (40 câu):** Phán quyết tử hình tại Quảng Châu, bác bỏ dẫn độ và Hệ thống 3 bài học cảnh báo sâu sắc về kiểm soát lòng tham và an ninh cá nhân.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Ho_So_Toi_Pham/Tap32/kichban_tap32_22112026.md`) — 240 câu, 0 lỗi chính tả/dấu câu
- [x] Tách câu kịch bản chuẩn hóa (`.work/script_tap32.json`)
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Ho_So_Toi_Pham/Tap32_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Ho_So_Toi_Pham/Tap32_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Ho_So_Toi_Pham/Tap32_KO/`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
