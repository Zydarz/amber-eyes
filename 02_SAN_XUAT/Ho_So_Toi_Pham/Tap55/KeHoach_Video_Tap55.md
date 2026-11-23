# HỒ SƠ SẢN XUẤT TẬP 55 · "PETER KÜRTEN" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap55/kichban_tap55_19112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Ho_So_Toi_Pham/Tap55/xuat_ban/`
**Cập nhật:** 22/11/2026 — Bổ sung tư liệu lịch sử từ internet lên chuẩn **242 câu thoại** (Hệ sinh thái 10 chỉ dấu tâm lý & Phân tâm học tội phạm Weimar).

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập 55: Hồ Sơ Peter Kürten — Thời Kỳ Weimar & Nguồn Cội Phân Tâm Học Tội Phạm |
| **Đề tài** | Quái vật Düsseldorf năm 1929 tại Đức, đối tượng nghiên cứu kinh điển của tâm thần học |
| **Kịch bản** | `01_KICH_BAN/Ho_So_Toi_Pham/Tap55/kichban_tap55_19112026.md` (242 câu thoại · 25 lượt nói · 6.983 từ · chuẩn A2c/K10) |
| **Trọng tâm tâm lý (K10)** | Nguồn cội phân tâm học tội phạm, Thỏa mãn từ nỗi sợ đám đông, Nghiên cứu Carl Gustav Jung (Bóng tối Archetype), Công trình *Der Sadist* của Tiến sĩ Karl Berg. |
| **Thời lượng dự kiến** | 26:00 – 30:00 (~1.600 – 1.800 giây) |
| **Giọng đọc phân bổ** | Host (Cú, 123 câu ~50.8%) · Điều tra viên (Sói, 46 câu ~19.0%) · Chuyên gia tâm lý (Cáo, 51 câu ~21.1%) · N1 (Maria Budlick, 11 câu) · N2 (Auguste Scharf Kürten, 11 câu) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung tâm lý học và hành vi). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1 (56 câu):** Nỗi kinh hoàng trên đường phố Düsseldorf và cơn cuồng loạn tập thể. Dư chấn xã hội Weimar, hơn 12.000 thư tố cáo và 200 thư nhận tội giả, sự xuất hiện của Ernst Gennat cùng chiếc xe điều tra lưu động huyền thoại *Mordauto*.
* **Hồi 2 (52 câu):** Chiếc mặt nạ hoàn hảo và cơ chế chia ngăn tâm trí. Cuộc sống mẫu mực tại chung cư số 71 phố Mettmanner, hệ thống hồ sơ án mạng tập trung *Zentrale Mordkartei*, tuổi thơ bị bạo hành và cơ chế phân ly tâm lý bệnh hoạn.
* **Hồi 3 (45 câu):** Khoảnh khắc thoát cửa tử và bức thư định mệnh của nạn nhân. Bước ngoặt ngày 14/05/1930 với Maria Budlick tại rừng Grafenberg, phản ứng "thích ứng phục tùng" đánh lừa ảo tưởng quyền năng của Kürten, lá thư gửi nhầm địa chỉ.
* **Hồi 4 (51 câu):** Điểm gãy tâm lý của người vợ và cạm bẫy tại Nhà thờ Thánh Rochus. Lời thú tội lạnh lùng của hung thủ, toan tính ái kỷ về tiền thưởng, sự thức tỉnh lương tri của Auguste Scharf và chiến dịch giăng bẫy bắt sống Peter Kürten ngày 24/05/1930.
* **Hồi 5 (38 câu):** Phân tâm học vạch trần bản ngã ái kỷ và bản án lịch sử. Tiến sĩ Karl Berg và công trình kinh điển *Der Sadist*, câu hỏi cuối cùng trước máy chém Klingelpütz ngày 02/07/1931, di sản khoa học hình sự và 3 bài học cảnh báo đỏ sinh tồn.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt chuẩn 242 câu (`01_KICH_BAN/Ho_So_Toi_Pham/Tap55/kichban_tap55_19112026.md`)
- [ ] Đồng bộ bổ sung kịch bản Tiếng Anh (`01_KICH_BAN/Ho_So_Toi_Pham/Tap55_EN/`)
- [ ] Đồng bộ bổ sung kịch bản Tiếng Nhật (`01_KICH_BAN/Ho_So_Toi_Pham/Tap55_JA/`)
- [ ] Đồng bộ bổ sung kịch bản Tiếng Hàn (`01_KICH_BAN/Ho_So_Toi_Pham/Tap55_KO/`)
- [x] Kiểm tra tách câu (`.work/parse_kichban.py`: 242 câu đạt chuẩn)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
