# HỒ SƠ SẢN XUẤT TẬP 68 · "TRƯƠNG TỬ CƯỜNG" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Tap68/kichban_tap68_22112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Tap68/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 68: Hồ Sơ Trương Tử Cường — Tướng Cướp Thế Kỷ & Tâm Lý Con Bạc Bệnh Lý Hồng Kông |
| **Đề tài** | Chuỗi vụ án cướp xe bọc thép chở tiền tại sân bay Khải Đức và bắt cóc tống tiền con trai Lý Gia Thành, Walter Kwok thu về gần 2 tỷ HKD do Trương Tử Cường (Cheung Tsz-keung) thực hiện; bị bắt và thi hành án tử hình tại Quảng Đông năm 1998 |
| **Trọng tâm tâm lý (K10)** | Tâm lý Con bạc bệnh lý (Pathological Gambling), Sự thèm khát Adrenaline & Ảo tưởng quyền lực tối thượng (God Complex), Chiến thuật tâm lý đối đầu hệ thống pháp luật và Điểm mù tư pháp xuyên biên giới. |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Vệ sĩ / Nhân chứng (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung toàn diện vào đấu trí tâm lý, phân tích động cơ hành vi và bài học an ninh bảo vệ). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Tướng cướp thế kỷ Trương Tử Cường, vụ cướp sân bay Khải Đức năm 1991 và màn kháng cáo đòi bồi thường 8 triệu HKD chấn động.
* **Hồi 2:** Đòn cân não đàm phán một mình mang thuốc nổ vào dinh thự tỷ phú Lý Gia Thành và vụ bắt cóc thế kỷ thu 1,38 tỷ HKD.
* **Hồi 3:** Cơn nghiện adrenaline và sòng bạc không đáy tại Ma Cao, vòng xoáy tự hủy diệt của kẻ khát bạc bệnh lý.
* **Hồi 4:** Bẫy lưới chuyên án 9810 tại Quảng Đông, sự sụp đổ của ảo tưởng quyền lực và giới hạn tư pháp xuyên biên giới.
* **Hồi 5:** Phán quyết tử hình tại Quảng Châu và Hệ thống 3 bài học cảnh báo sâu sắc về kiểm soát lòng tham và an ninh cá nhân.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (`01_KICH_BAN/Tap68/kichban_tap68_22112026.md`)
- [ ] Kịch bản Tiếng Anh (`01_KICH_BAN/Tap68_EN/`)
- [ ] Kịch bản Tiếng Nhật (`01_KICH_BAN/Tap68_JA/`)
- [ ] Kịch bản Tiếng Hàn (`01_KICH_BAN/Tap68_KO/`)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
