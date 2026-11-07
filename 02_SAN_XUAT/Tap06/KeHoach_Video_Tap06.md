# HỒ SƠ SẢN XUẤT TẬP 06 · "NỤ CƯỜI CHÚ HỀ & 29 BÍ MẬT DƯỚI SÀN NHÀ" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A) — các mã A0…A13 trong file này trỏ về đó.  
**Kịch bản:** `01_KICH_BAN/Tap06/kichban_tap06_23102026.md` · **Thành phẩm:** `02_SAN_XUAT/Tap06/xuat_ban/`  
**Ngày lập:** 24/10/2026

---

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap06/kichban_tap06_23102026.md` — đã chuẩn hóa lịch sử, pháp lý, tâm lý học (John Wayne Gacy) |
| Lượt nói / câu / từ | 62 lượt · **212** câu · 6.306 — Cú · Host 50.5% · Sói · Điều tra viên 25.5% · Cáo · Chuyên gia 19.3% · Mèo · N2 2.4% · Cừu · N1 2.4% |
| Giọng | **Higgs Audio v3** (Kaggle GPU, 02/11/2026) — bộ giọng thật tiếng Việt: H `H` · D `D3_SH` · C `C2_AB03` · N1 `W6_LOW` · N2 `W5_HIGH`. Không thẻ cảm xúc. Master: `xuat_ban/Tap06_master.mp3` (1265,4 s · −16,2 LUFS · true peak −1,6 dBFS) |
| N1 / N2 | `1.09` Kim Byers - nhân viên hiệu thuốc Nisson (Cừu) / `4.05` Sĩ quan Mike Albrecht - cảnh sát Des Plaines (Mèo) |
| Thời lượng | **1939.5 s (32:19)** — *timeline tạm, chờ thu âm lại kịch bản mới* |
| Nền dùng | 65 nền `t6_*` + `charity` + `void` (2112×1188 16:9 2K noir) |
| Phân loại YouTube | Giáo dục · Không dành cho trẻ em · "Nội dung bị thay đổi hoặc tổng hợp" · Tự đánh giá quảng cáo: chủ đề tội phạm phân tích tâm lý khách quan (A10) |

> **Cập nhật 06/11/2026 — dựng lại theo kịch bản mới.** Bảng shot mục 6 được dựng lại từ đầu: **129 shot** (123 shot nội dung + 4 dòng nghỉ + 2 thẻ chuyển hồi) thay cho 73 shot của bản cũ; thêm **thẻ chuyển hồi (T10)** và **4 dòng nghỉ** theo chuẩn Tập 03/04/05. Ảnh tĩnh đã render lại cho **3 ngôn ngữ** (VN / EN / JA) — mỗi bản 129 ảnh tại `.work/video3{,_EN,_JA}_t06/stills/`.
> - **Timeline là bản TẠM** (giữ mốc element đo từ audio master cũ, chia lại thời lượng câu theo độ dài câu mới) — chưa có audio master mới để neo lại. Cần thu âm lại rồi dựng lại timeline + stems + video.
> - **H9 — lớp tối mềm (`text_scrim`)** bổ sung cho 23 shot có chữ nằm trên nền sáng (lập bằng `.work/_t06_scan_contrast.py`: đo tương phản tại đúng vị trí nét chữ sau khi áp lớp phủ của renderer). Danh sách nằm trong `.work/edition.py` → `EPISODES["06"]["text_scrim"]`.
> - **PHỤ LỤC C–E bên dưới mô tả bản dựng cũ (73 shot, 02–03/11/2026)** — giữ nguyên làm hồ sơ lịch sử; trạng thái hiện tại là bản dựng 129 shot nêu trên.

---

## B2. Quy tắc hình ảnh riêng của Tập 06

- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:** `t6_secret_service_pin_handshake`, `t6_muddy_trousers_boots`, `t6_surveillance_car_rain_night`, `t6_chicago_highway_pursuit`. Tuyệt đối không vẽ mặt thật John Wayne Gacy, Robert Piest, bà Elizabeth Piest hay Trung úy Joseph Kozenczak.
- **Không vẽ nạn nhân:** Tuyệt đối không vẽ nạn nhân (Robert Piest, John Alan Szyc và 31 nạn nhân khác), kể cả dạng bóng, ở các khoảnh khắc nhạy cảm. Ẩn dụ qua vật chứng: chiếc áo khoác bỏ quên (`t6_empty_coat_locker`), chiếc nhẫn tốt nghiệp (`t6_highschool_ring_jas`).
- **V9 — Trọng tâm là phân tích tâm lý học tội phạm & pháp y hình sự:** Tập trung vào Rối loạn nhân cách chống đối xã hội (ASPD), Sự phủ nhận trách nhiệm bệnh lý (Psychological Externalization) và Mặt nạ ái kỷ (Narcissistic Mask). Tuyệt đối không mô tả chi tiết vết thương, thi thể, máu me; không vẽ hình ảnh giằng co, tấn công.
- **H5 — Tuyệt đối không để AI vẽ chữ:** Mọi chữ hiển thị trên video đều do Pillow vẽ đè bằng font Unicode chuẩn tiếng Việt (Segoe UI / Cambria).
- **H12 — Thẻ kết shot cuối bắt buộc có chữ:** Nhãn `HỒ SƠ TẬP 06 · ĐÃ ĐÓNG` + tên kênh **AMBER EYES** + khẩu hiệu *"Phân tích tâm lý tội phạm / qua những hồ sơ có thật"*.
- **Tắt bán thân `⊘` ở các khoảnh khắc nặng nề:** Nắp hầm crawl space, khai quật thi thể dưới nền móng, vứt bỏ nạn nhân trên sông Des Plaines, buồng tử tù Menard, phòng thi hành án Stateville.

---

## 6. DANH SÁCH SHOT — TẬP 06 (tiếng Việt)

| Shot | Câu | Vai | Mẫu | Nền | Chữ | SFX / Beat | Nhân vật | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01` (20.5 s → lời đầu) | — | T1 | `t6_polish_parade_chicago_1978` | *HỒI 01 · BỨC ẢNH VỚI ĐỆ NHẤT PHU NHÂN VÀ CẬU BÉ HIỆU THUỐC* | Tiếng dương cầm mở đầu trầm buồn | ⊘ |  |
| 1-01 | `1.02#1` | H | T5 ngày | `t6_polish_parade_chicago_1978` | **06 · 05 · 1978** · *Chicago, Illinois · Lễ diễu hành Ngày Hiến pháp Ba Lan* | Chớp máy ảnh lách tách `1.03` | ✦ Cú |  |
| 1-02 | `1.02#2`–`#3` | H | T1 | `t6_secret_service_pin_handshake` | **HUY HIỆU CHỮ S CỦA MẬT VỤ HOA KỲ** · *Được cấp phát sau quy trình thẩm tra lý lịch nghiêm ngặt* | — | 🅑 |  |
| 1-03 | `1.02#4` | H | T1 | `t6_pdm_contractors_truck` | **NHÀ THẦU XÂY DỰNG PDM CONTRACTORS** · *Đội trưởng khu dân cư tận tụy vùng Norwood Park* | — | 🅑 |  |
| 1-04 | `1.02#5` | H | T1 | `t6_pdm_contractors_office` | **BẾP NGOÀI TRỜI & GIỚI THẦU ĐỊA PHƯƠNG** · *Quen biết thẩm phán, nghị sĩ và quan chức thực thi pháp luật* | — | 🅑 |  |
| 1-05 | `1.02#6` | H | T1 | `t6_clown_costume_closet` | **BỘ TRANG PHỤC CHÚ HỀ POGO** · *Người đàn ông nhân từ thường xuyên khoác lên mình* | — | 🅑 |  |
| 1-06 | `1.02#7`–`#8` | H | T1 | `charity` | **HÌNH MẪU CÔNG DÂN GƯƠNG MẪU** · *Bệnh viện nhi và hội chợ từ thiện — một trụ cột đáng kính của xã hội đương thời* | — | 🅑 |  |
| 1-07 | `1.04#1` | H | T2 | `t6_clown_mirror_chiaroscuro` | *CHIẾC BẪY SĂN MỒI TÀN ĐỘC* · **MẶT NẠ CHÚ HỀ** · *Hiệu ứng Hào quang che mắt cả cộng đồng* | — | ⊘ |  |
| 1-08 | `1.04#2` | H | T1 | `t6_summerdale_house_winter_exterior` | **KHU LĂNG MỘ NGẦM RÙNG RỢN** · *Chiếc bẫy âm thầm vận hành suốt nhiều năm giữa khu dân cư yên bình* | — | ⊘ |  |
| 1-09 | `1.04#3` | H | T1 | `t6_psychological_mask_metaphor` | **MÁI ẤM GIA ĐÌNH HÓA KHU LĂNG MỘ** · *Một nhân cách đen tối biến chính mái ấm của mình thành nghĩa trang ngầm* | — | ⊘ |  |
| 1-10 | `1.04#4` | H | T1 | `t6_dossier_gacy_case_06` | **SỤP ĐỔ CỦA CHIẾC MẶT NẠ** · *Cơn chấn động tập thể bao trùm khắp toàn bộ xã hội Mỹ* | — | ⊘ →D |  |
| 1-11 | `1.05` (nghỉ 1.5 s) | — | — | giữ 1-10 | — | Cello u uất trỗi dậy | ⊘ |  |
| 1-12 | `1.06#1`–`#2` | H | T5 ngày | `t6_des_plaines_winter_night` | **11 · 12 · 1978** · *Des Plaines, Illinois · Sinh nhật 46 tuổi của bà Elizabeth Piest* | — | ✦ Cú |  |
| 1-13 | `1.06#3` | H | T1 | `t6_car_exhaust_snow_lot` | **NGƯỜI MẸ LÁI XE ĐẾN HIỆU THUỐC** · *Đón cậu con trai 15 tuổi tan ca làm thêm sau giờ học* | — | 🅑 |  |
| 1-14 | `1.06#4` | H | T1 | `t6_nisson_pharmacy_exterior` | **HIỆU THUỐC NISSON PHARMACY** · *Robert Piest — học sinh danh dự lớp mười trường trung học Maine West* | — | 🅑 |  |
| 1-15 | `1.06#5` | H | T1 | `t6_deserted_parking_lot_snow` | **KHOẢNG CHÍN GIỜ TỐI** · *Robert chạy vội ra xe xin mẹ đợi thêm vài phút* | — | 🅑 |  |
| 1-16 | `1.06#6`–`#7` | H | T1 | `t6_pharmacy_counters_renovation` | **NĂM ĐÔ LA MỘT GIỜ** · *Lời mời làm thêm của một nhà thầu đang sửa kệ trong tiệm thuốc* | — | 🅑 |  |
| 1-17 | `1.08#1` | H | T1 | `t6_bank_cash_withdrawal` | **MỨC LƯƠNG NĂM ĐÔ LA MỘT GIỜ** · *Cao gần gấp đôi mức lương tối thiểu liên bang năm 1978* | — | 🅑 |  |
| 1-18 | `1.08#2`–`#3` | H | T1 | `t6_empty_coat_locker` | **MỘT CƠ HỘI KHÔNG THỂ CHỐI TỪ** · *Cậu học sinh trung học háo hức quay lại gặp người đàn ông lạ mặt* | — | ⊘ |  |
| 1-19 | `1.08#4` | H | T1 | `t6_deserted_parking_lot_snow` | **LẦN CUỐI CÙNG NGƯỜI MẸ NHÌN THẤY CON** · *Robert biến mất không một dấu vết* | — | ⊘ |  |
| 1-20 | `1.08#5` | H | T1 | `t6_car_exhaust_snow_lot` | **MƯỜI PHÚT · BA MƯƠI PHÚT · MỘT TIẾNG** · *Trong nỗi bồn chồn nghẹt thở ngồi đợi giữa bão tuyết* | — | ⊘ |  |
| 1-21 | `1.08#6` | H | T1 | `t6_dossier_gacy_case_06` | **BIẾN MẤT KHÔNG MỘT DẤU VẾT** · *Cậu bé Robert Piest không bao giờ quay lại* | — | ⊘ |  |
| 1-22 | `1.08#7` | H | T1 | `t6_pharmacy_counters_renovation` | **LẮNG NGHE KÝ ỨC CỦA KIM BYERS** · *Cô đồng nghiệp mười bảy tuổi của Robert tại hiệu thuốc Nisson* | — | 🅑 →N1 |  |
| 1-23 | `1.09#1`–`#3` | N1 | T4 lời kể | `t6_pharmacy_register_receipt` | “Tối hôm đó, hiệu thuốc chúng tôi đang sửa chữa một số dãy tủ kệ và nhà thầu John Gacy đã ở đó suốt buổi chiều. Ông ta nói chuyện rất vui vẻ, cởi mở với tất cả nhân viên và tỏ ra là một người lớn vô cùng tốt bụng.” | — | ✦ Cừu |  |
| 1-24 | `1.09#4`–`#5` | N1 | T4 lời kể | `t6_empty_coat_locker` | “Cậu ấy chỉ chạy vào nói với tôi vài câu rồi vội vã đi ra ngoài để nói chuyện với Gacy trước khi về nhà cắt bánh sinh nhật với mẹ. Nhưng Robert không bao giờ quay trở lại” | — | 🅑 →H |  |
| 1-25 | `1.11#1`–`#2` | H | T1 | `t6_des_plaines_police_station` | **BÁO ĐỘNG KHẨN CẤP** · *Sở Cảnh sát Des Plaines vào cuộc ngay trước mắt người mẹ* | — | ✦ Cú →D |  |
| 1-26 | `1.11#3` | H | T1 | `t6_detective_desk_missing_file` | **MANH MỐI DUY NHẤT** · *Nhà thầu xây dựng John Wayne Gacy — người tiếp xúc cuối cùng với cậu bé* | — | ⊘ →D |  |
| 1-27 | `1.12#1`–`#2` | D | T1 | `t6_detective_desk_missing_file` | **DẤU HIỆU BẤT THƯỜNG** · *Học sinh danh dự chuẩn bị về nhà mừng sinh nhật mẹ không thuộc nhóm bỏ nhà đi bụi* | — | ⊘ |  |
| 1-28 | `1.12#3`–`#4` | D | T1 | `t6_des_plaines_police_station` | **LỆNH TRIỆU TẬP GIỮA ĐÊM 11 THÁNG 12** · *Gacy viện cớ xe sa lầy tuyết để trì hoãn cuộc thẩm vấn* | — | ⊘ |  |
| 1-29 | `1.12#5`–`#6` | D | T1 | `t6_police_interrogation_room_empty` | **BÌNH THẢN BƯỚC VÀO PHÒNG THẨM VẤN** · *Hắn hoàn toàn phủ nhận mọi lời hứa với Robert Piest* | — | ⊘ →H |  |
| 1-30 | `1.13#1`–`#2` | H | T1 | `t6_police_interrogation_room_empty` | **SỰ TỰ TIN TUYỆT ĐỐI TRƯỚC THẨM VẤN** · *Uy tín chính trị khiến các sĩ quan thị trấn nhỏ phải e dè* | — | ✦ Cú →D |  |
| 1-31 | `1.14#1` | D | T1 | `t6_muddy_trousers_boots` | **QUẦN ÁO DÍNH ĐẦY BÙN ĐẤT ẨM ƯỚT** · *Trên gấu quần và đế giày của Gacy* | — | ⊘ |  |
| 1-32 | `1.14#2`–`#3` | D | T1 | `t6_summerdale_house_winter_exterior` | **MÂU THUẪN KHÔNG THỂ GIẢI THÍCH** · *Giữa một đêm Illinois đóng băng tuyết trắng* | — | ⊘ →C |  |
| 1-33 | `1.15#1` | C | T1 | `t6_psychological_mask_metaphor` | **RỐI LOẠN NHÂN CÁCH CHỐNG ĐỐI XÃ HỘI** · *Hiện thân kinh điển kết hợp với Ái kỷ ác tính* | — | ✦ Cáo →H |  |
| 1-34 | `1.15#2` | C | T1 | `t6_clown_costume_closet` | **MẶT NẠ KHÔNG ĐƯỢC TẠO TỪ SỰ CÔ ĐƠC** · *Mà dệt nên từ chính sự hào nhoáng của địa vị xã hội* | — | ⊘ →H |  |
| 1-35 | `1.15#3`–`#5` | C | T1 | `t6_clown_mirror_chiaroscuro` | **HAI MỤC ĐÍCH SỐNG CÒN** · *Hiệu ứng Hào quang làm tê liệt cảnh giác · Cơ chế tự thôi miên nhận thức* | — | ⊘ →H |  |
| 1-36 | `1.16#1`–`#2` | H | T1 | `t6_dossier_gacy_case_06` | **PHÁT SÚNG MỞ MÀN CUỘC ĐẤU TRÍ** · *Cuộc đối đầu tại đồn cảnh sát Des Plaines lúc rạng sáng* | — | ✦ Cú |  |
| 1-37 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **HIỆN TRƯỜNG & QUỸ ĐẠO LEO THANG CỦA VỰC THẲM** | — | ⊘ | ◼ |
| 2-01 | `2.02#1`–`#2` | H | T1 | `t6_iowa_prison_records` | **LÝ LỊCH TƯ PHÁP LƯU TRỮ** · *Trung úy Kozenczak lập tức ra lệnh rà soát tàng thư căn cước tư pháp* | — | ✦ Cú →D |  |
| 2-02 | `2.03#1`–`#2` | D | T5 ngày | `t6_iowa_prison_records` | **1968** · *Thị trấn Waterloo, bang Iowa — kết án mười năm tù giam* | — | 🅑 |  |
| 2-03 | `2.03#3`–`#4` | D | T1 | `t6_pdm_contractors_office` | **TỪ NHÀ TÙ RA VỀ THÀNH PHỐ** · *Ân xá sớm sau mười tám tháng · Thành lập PDM Contractors và thâm nhập câu lạc bộ chính trị* | — | 🅑 →H |  |
| 2-04 | `2.04#1`–`#2` | C | T1 | `t6_psychological_floor_cross_section` | **NÓI NỔ VÀ ĐIỂM GÃY TÂM LÝ** · *Bản án năm 1968 tại Iowa định hình toàn bộ chuỗi hành vi tội ác về sau* | — | ✦ Cáo →H |  |
| 2-05 | `2.04#3`–`#4` | C | T1 | `t6_abusive_childhood_shadow` | **NẤC THANG THỨ NHẤT** · *Tổn thương tuổi thơ bị bạo hành và sỉ nhục hình thành khao khát kiểm soát* | — | ⊘ |  |
| 2-06 | `2.04#5`–`#7` | C | T1 | `t6_psychological_mask_metaphor` | **NẤC THANG THỨ HAI · THỨ BA · THỨ TƯ** · *Từ Iowa đến tháng 1 năm 1972; rồi cơn nghiện ảo tưởng mất kiểm soát giai đoạn 1976–1978* | — | ⊘ →H |  |
| 2-07 | `2.05#1`–`#2` | H | T5 ngày | `t6_search_warrant_documents` | **13 · 12 · 1978** · *Lệnh khám xét đầu tiên — số 8213 Đại lộ West Summerdale* | — | 🅑 →D |  |
| 2-08 | `2.07#1` | D | T1 | `t6_gacy_house_daylight_winter` | **CĂN NHÀ NGOẠI Ô KHANG TRANG** · *Một ngôi nhà một tầng kiểu nông trại ở vùng ngoại ô yên bình* | — | ✦ Sói |  |
| 2-09 | `2.07#2`–`#4` | D | T1 | `t6_handcuffs_fake_badge` | **CÒNG TAY KIM LOẠI & PHÙ HIỆU CẢNH SÁT GIẢ** · *Dùi cui và sách nghiên cứu kỹ thuật trói buộc* | — | 🅑 |  |
| 2-10 | `2.07#5` | D | T1 | `t6_pharmacy_register_receipt` | **CUỐNG BIÊN NHẬN ẢNH NISSON** · *Chứng minh Gacy đã tiếp xúc với nhân viên quầy thuốc đúng buổi tối Robert mất tích* | — | 🅑 |  |
| 2-11 | `2.07#6` | D | T1 | `t6_highschool_ring_jas` | **CHIẾC NHẪN KHẮC BA CHỮ LỒNG: JAS** · *Chiếc nhẫn tốt nghiệp trung học năm 1975* | — | 🅑 |  |
| 2-12 | `2.08#1`–`#2` | H | T1 | `t6_cold_case_szyc_dossier` | **JOHN ALAN SZYC, MƯỜI CHÍN TUỔI** · *Mất tích bí ẩn tại Chicago từ tháng 1 năm 1977 — Gacy bịa câu chuyện về chiếc nhẫn* | — | ✦ Cú |  |
| 2-13 | `2.08#3` | H | T1 | `t6_dossier_gacy_case_06` | **ROBERT PIEST KHÔNG PHẢI LÀ NẠN NHÂN DUY NHẤT** · *Một kỷ vật của người mất tích đã xác nhận một nghi vấn rùng mình* | — | ⊘ →D |  |
| 2-14 | `2.09#1`–`#2` | D | T1 | `t6_handwritten_crawlspace_map` | **THỦ ĐOẠN GÂY ÁN (MO)** · *Hắn liên tục thay đổi và hoàn thiện kỹ thuật theo thời gian* | — | ⊘ |  |
| 2-15 | `2.09#3` | D | T1 | `t6_pharmacy_register_receipt` | **MỒI NHỬ LƯƠNG CAO** · *Lời hứa việc làm lương cao để làm tê liệt phản kháng* | — | 🅑 |  |
| 2-16 | `2.09#4` | D | T1 | `t6_handcuff_trick_demonstration` | **CÒNG TAY ẢO THUẬT** · *Lừa nạn nhân tự đưa tay vào còng trước khi bị khóa chặt* | — | ⊘ |  |
| 2-17 | `2.09#5`–`#6` | D | T1 | `t6_psychological_mask_metaphor` | **CHỮ KÝ TÂM LÝ (SIGNATURE)** · *Nhu cầu bệnh lý biến nạn nhân thành đạo cụ quyền lực* | — | ⊘ |  |
| 2-18 | `2.09#7` | D | T1 | `t6_highschool_ring_jas` | **CHIẾN LỢI PHẨM** · *Nhẫn tốt nghiệp, ví tiền và giấy tờ lái xe của nạn nhân* | — | 🅑 |  |
| 2-19 | `2.09#8` | D | T1 | `t6_psychological_floor_cross_section` | **CHÔN GIẤU NGAY DƯỚI SÀN NHÀ** · *Đi lại bên trên những sinh mạng do chính mình đoạt quyền* | — | ⊘ →H |  |
| 2-20 | `2.10#1` | H | T1 | `t6_search_warrant_documents` | **CHƯA ĐỦ CHỨNG CỨ VẬT CHẤT** · *Chưa thể ra lệnh bắt giữ chính thức về nơi ở hay nơi cất giấu* | — | ⊘ |  |
| 2-21 | `2.10#2` | H | T1 | `t6_des_plaines_police_station` | **CHIẾN THUẬT GIÁM SÁT ĐẶC BIỆT** · *Tránh kẻ thủ ác tiêu huỷ chứng cứ hoặc tiếp tục gây hại* | — | ⊘ |  |
| 2-22 | `2.10#3`–`#4` | H | T1 | `t6_surveillance_car_rain_night` | **BỐN SĨ QUAN BÁM ĐUÔI** · *Hai chiếc xe cảnh sát dân sự theo sát chiếc xe của Gacy từ sáng sớm tinh mơ đến nửa đêm* | — | 🅑 |  |
| 2-23 | `2.10#5`–`#6` | H | T1 | `t6_psychological_mask_metaphor` | **SÀN DIỄN CÁ NHÂN** · *Thay vì sợ hãi, Gacy biến cuộc theo dõi thành sân khấu riêng cho mình* | — | ⊘ →C |  |
| 2-24 | `2.10#7` | H | T1 | `t6_gas_station_neon_midnight` | **LÁI XE VÒNG VÈO QUA CÁC TRẠM XĂNG** · *Chạy chậm rì rì trên đường cao tốc để thử thách lòng kiên nhẫn* | — | 🅑 |  |
| 2-25 | `2.10#8`–`#9` | H | T1 | `t6_diner_booth_confrontation` | **MỜI CẢNH SÁT VÀO NHÀ HÀNG TỐI** · *Hắn cười lớn, hào phóng mua bia chiêu đãi họ | — | ⊘ |  |
| 2-26 | `2.11#1`–`#2` | C | T1 | `t6_psychological_mask_metaphor` | **CƠ CHẾ BÙ TRỪ QUYỀN LỰC** · *Bị cả đội cảnh sát bám đuôi không tạo sợ hãi mà tạo hưng phấn adrenaline* | — | ✦ Cáo →H |  |
| 2-27 | `2.11#3`–`#4` | C | T1 | `t6_clown_mirror_chiaroscuro` | **KHÁNH GIẢ BẤT ĐẮC DĨ** · *Hắn xem các nhân viên thực thi pháp luật như người chiêm ngưỡng sự vượt trội của mình* | — | ⊘ →H |  |
| 2-28 | `2.12#1`–`#2` | H | T1 | `t6_police_entry_summerdale` | **MỘT SƠ HỞ TỪ HỆ THỐNG SƯỞI ẤM** · *Sự căng thẳng bào mòn sức chịu đựng qua từng ngày bị phong tỏa* | — | ⊘ →D |  |
| 2-29 | `2.13` (nghỉ 1.5 s) | — | — | giữ 2-28 | — | Tiếng còi xe cảnh sát rít xé màn đêm | ⊘ |  |
| 2-30 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **GIẢI PHẪU TÂM LÝ — SỰ CHIA NGĂN NHẬN THỨC & KHOẢNG TỐI SUMMERDALE** | — | ⊘ | ◼ |
| 3-01 | `3.02#1`–`#2` | H | T5 ngày | `t6_lawyer_office_night` | **20 · 12 · 1978** · *Rượu, nước mắt và những lời lẩm bẩm về những điều không thể cứu vãn* | — | ✦ Cú →D |  |
| 3-02 | `3.02#3` | H | T1 | `t6_des_plaines_police_station` | **CHẠM TỚI ĐIỂM GÃY TÂM LÝ** · *Ban chuyên án quyết định hành động ngay lập tức* | — | ⊘ →D |  |
| 3-03 | `3.03#1` | D | T1 | `t6_des_plaines_police_station` | **BẮT GIỮ NGÀY 21 THÁNG 12** · *Cáo buộc tàng trữ chất cấm để giữ chân hắn tại đồn cảnh sát* | — | ✦ Sói →H |  |
| 3-04 | `3.03#2` | D | T1 | `t6_police_entry_summerdale` | **LỆNH KHÁM XÉT THỨ HAI** · *Một đội đặc biệt âm thầm tiến vào số 8213 West Summerdale* | — | ⊘ |  |
| 3-05 | `3.03#3`–`#5` | D | T1 | `t6_crawlspace_trapdoor_opened` | **MÙI HÔI THỐI TỪ HỆ THỐNG SƯỞI ẤM** · *Mỗi khi sàn nhà được bật sưởi, một luồng khí ngột ngạt bốc lên qua các khe thông gió* | — | ⊘ |  |
| 3-06 | `3.03#6` | D | T1 | `t6_forensic_trowel_damp_soil` | **MỞ NẮP SÀN KỸ THUẬT** · *Kiểm tra toàn bộ nền móng của ngôi nhà* | — | ⊘ →H |  |
| 3-07 | `3.05#1`–`#2` | H | T1 | `t6_crawlspace_subterranean_tunnel` | **KHOẢNG KHÔNG GIAN BÒ CHẬT HẸP** · *Cao chưa đầy nửa mét — chạy dọc toàn bộ diện tích sàn nhà* | — | ⊘ →D |  |
| 3-08 | `3.06#1`–`#2` | D | T1 | `t6_flashlight_beam_lime_dust` | **NẰM SẤP TRÊN NỀN ĐẤT ẨM** · *Điều tra viên phải cởi quân phục, đeo mặt nạ dưỡng khí và trườn bằng khuỷu tay* | — | ⊘ →H |  |
| 3-09 | `3.06#3`–`#4` | D | T1 | `t6_forensic_trowel_damp_soil` | **MỘT CHIẾC XẺNG CẮM SÂU** · *Những rãnh đất bị xới xáo và lấp vội vàng dưới phòng ngủ* | — | ⊘ |  |
| 3-10 | `3.08#1`–`#2` | H | T1 | `t6_forensic_trowel_damp_soil` | **CHỈ SAU VÀI NHÁT XẺNG** · *Mảnh vải quần áo và xương cốt người nằm sâu trong lòng đất* | — | ⊘ |  |
| 3-11 | `3.08#3` | H | T1 | `t6_psychological_floor_cross_section` | **NGHĨA TRANG NGẦM DƯỚI PHÒNG KHÁCH** · *Ngay dưới nơi Gacy từng tiếp đón bạn bè và đi lại mỗi đêm* | — | ⊘ →C |  |
| 3-12 | `3.09` (nghỉ 1.5 s) | — | — | giữ 3-11 | — | Tiếng thở dài trầm lặng | ⊘ |  |
| 3-13 | `3.10#1`–`#2` | D | T1 | `t6_night_excavation_floodlights` | **CHIẾN DỊCH KHAI QUẬT QUY MÔ LỚN** · *Chuyên gia pháp y Clyde Snow tỉ mỉ sàng lọc từng tấc đất* | — | ✦ Sói |  |
| 3-14 | `3.10#3`–`#5` | D | T1 | `t6_evidence_boxes_van` | **HAI MƯƠI SÁU NẠN NHÂN DƯỚI KHOẢNG KHÔNG GIAN BÒ** · *Ba nạn nhân khác trong khuôn viên sân sau và dưới lối đi lát bê tông* | — | 🅑 |  |
| 3-15 | `3.10#6`–`#7` | D | T1 | `t6_des_plaines_river_bridge_winter` | **BA MƯƠI BA SINH MẠNG BỊ TƯỚC ĐOẠT** · *Bốn nạn nhân cuối cùng bị ném xuống dòng sông Des Plaines băng giá* | — | ⊘ →H |  |
| 3-16 | `3.11#1`–`#2` | C | T1 | `t6_psychological_floor_cross_section` | **CHIA NGĂN NHẬN THỨC** · *Hai ngăn kéo hoàn toàn biệt lập — không bao giờ giao thoa* | — | ✦ Cáo →H |  |
| 3-17 | `3.11#3`–`#4` | C | T1 | `t6_four_masks_psychiatric` | **NGĂN KÉO THỨ NHẤT** · *Nhà thầu cần mẫn · người con hiếu thảo phụng dưỡng mẹ già · người chồng chu đáo* | — | ⊘ |  |
| 3-18 | `3.11#5`–`#6` | C | T1 | `t6_scented_air_fresheners` | **LÁ CHẮN BÌNH THƯỜNG HÓA** · *Gia đình và người mẹ được dùng làm bảo chứng cho danh dự công dân* | — | 🅑 |  |
| 3-19 | `3.11#7`–`#8` | C | T1 | `t6_clown_mirror_chiaroscuro` | **NGĂN KÉO THỨ HAI** · *Thế giới bóng đêm săn mồi — tắm rửa rồi ăn tối cùng gia đình như chưa từng có chuyện gì* | — | ⊘ |  |
| 3-20 | `3.11#9`–`#11` | C | T1 | `t6_psychological_mask_metaphor` | **VẬT HÓA & PHI NHÂN HÓA** · *Nạn nhân bị quy đổi thành đạo cụ quyền lực tạm thời* | — | ⊘ |  |
| 3-21 | `3.11#12` | C | T1 | `t6_abusive_childhood_shadow` | **THIẾU HỤT THẤU CẢM XÚC** · *Tiếng van xin không thể kích hoạt lòng trắc ẩn* | — | ⊘ →H |  |
| 3-22 | `3.11#13`–`#15` | C | T1 | `t6_clown_oil_painting_easel` | **KỸ THUẬT TRUNG HÒA ĐẠO ĐỨC** · *Hắn đổ lỗi hoàn toàn cho nạn nhân rồi tự cấp cho mình quyền tước đoạt* | — | ⊘ →H |  |
| 3-23 | `3.12#1`–`#3` | H | T1 | `t6_evidence_boxes_van` | **CON QUÁI VẬT ĐÁNG SỢ NHẤT THẾ KỶ HAI MƯƠI** · *Nó sống ngay giữa một khu dân cư kiểu mẫu và mỉm cười chào hỏi hàng xóm* | — | ✦ Cú |  |
| 3-24 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **ĐẤU TRÍ THẨM VẤN & SỤP ĐỔ VỞ KỊCH ĐA NHÂN CÁCH** | — | ⊘ | ◼ |
| 4-01 | `4.02#1`–`#3` | H | T1 | `t6_four_masks_psychiatric` | **CHIẾN THUẬT PHÒNG VỆ TINH VI** · *Dàn dựng một vở kịch tâm thần đa nhân cách để trốn án tử* | — | ✦ Cú →D |  |
| 4-02 | `4.03#1`–`#3` | D | T1 | `t6_psychiatric_evaluation_room` | **BỐN NHÂN CÁCH TỰ DỰNG LÊN** · *John nhà thầu xây dựng · John chính trị gia · Pogo chú hề · Jack Hanley* | — | 🅑 →N2 |  |
| 4-03 | `4.03#4`–`#5` | D | T1 | `t6_dossier_gacy_case_06` | **ĐỔ TOÀN BỘ HÀNH VI LÊN ĐẦU JACK HANLEY** · *Gacy tuyên bố bản thân chỉ là một nhân chứng bất lực bị kẹt trong thân xác* | — | ⊘ |  |
| 4-04 | `4.04#1` | H | T1 | `t6_handwritten_crawlspace_map` | **LẮNG NGHE KÝ ỨC SĨ QUAN MIKE ALBRECHT** · *Người trực tiếp ngồi đối diện Gacy trong những giờ phút đấu trí* | — | ✦ Sói →N2 |  |
| 4-05 | `4.05#1`–`#2` | N2 | T1 | `t6_lawyer_office_night` | **HỒI NHỮNG GIỜ PHÚT NGỒI ĐỐI DIỆN** · *Căn phòng hỏi cung ngột ngạt và nước mắt thật* | — | ✦ Cú →C |  |
| 4-06 | `4.05#3`–`#5` | N2 | T4 lời kể | `t6_handwritten_crawlspace_map` | “chỉ vài giây sau, khi nhắc đến một chi tiết hiện trường, ánh mắt hắn lập tức trở nên sắc lạnh, tỉnh táo và đầy toan tính.” | — | ⊘ →H |  |
| 4-07 | `4.06#1`–`#2` | H | T5 ngày | `t6_cook_county_courthouse_exterior` | **THÁNG 02 · 1980** · *Tòa án Hạt Cook — phiên tòa được toàn thế giới theo dõi sát sao* | — | ✦ Cáo →H |  |
| 4-08 | `4.06#3` | H | T1 | `t6_psychiatric_evaluation_room` | **LÝ DO MẤT NĂNG LỰC NHẬN THỨC** · *Các luật sư dựa vào tổn thương tâm lý thời thơ ấu bị bạo hành* | — | ⊘ |  |
| 4-09 | `4.07#1`–`#2` | C | T1 | `t6_abusive_childhood_shadow` | **TUỔI THƠ NGẬP TRÀN SỈ NHỤC** · *Những sang chấn bẻ gãy sự phát triển cảm xúc bình thường* | — | ✦ Cáo →H |  |
| 4-10 | `4.07#3`–`#4` | C | T1 | `t6_jury_deliberation_room` | **TÍNH MỤC ĐÍCH & KHẢ NĂNG LÊN KẾ HOẠCH** · *Ranh giới mấu chốt giữa bệnh nhân và kẻ thái nhân cách* | — | ⊘ →H |  |
| 4-11 | `4.08#1` | H | T1 | `t6_cook_county_courthouse_exterior` | **CÔNG TỐ VIÊN TRƯỞNG WILLIAM KUNKLE** · *Bẻ nát tấm bình phong đa nhân cách bằng chứng cứ thực nghiệm* | — | ✦ Cú →D |  |
| 4-12 | `4.09#1`–`#2` | D | T1 | `t6_handwritten_crawlspace_map` | **HÀNH ĐỘNG CÓ KẾ HOẠCH TỪ TRƯỚC** · *Người thợ phụ trẻ đào sẵn rãnh đất dưới khoảng không gian bò* | — | ✦ Cáo →H |  |
| 4-13 | `4.09#3`–`#4` | D | T1 | `t6_bags_of_lime_garage` | **DỤNG CỤ KHỐNG CHẾ GIẤU KÍN** · *Rải vôi bột khử mùi và dọn sạch hiện trường sau mỗi vụ* | — | 🅑 |  |
| 4-14 | `4.09#5` | D | T1 | `t6_judge_gavel_death_penalty` | **SỰ TỈNH TÁO TUYỆT ĐỐI** · *Ý thức che giấu dấu vết hình sự ở mức độ cao nhất* | — | ⊘ |  |
| 4-15 | `4.10#1`–`#2` | C | T1 | `t6_psychiatric_evaluation_room` | **BÁC BỎ HOÀN TOÀN LÝ DO TÂM THẦN** · *Không hề bị phân liệt — hoàn toàn nhận thức tính chất sai trái của hành vi* | — | ✦ Cú |  |
| 4-16 | `4.11#1`–`#2` | H | T5 ngày | `t6_judge_gavel_death_penalty` | **12 · 03 · 1980** · *Chưa đầy hai giờ nghị án — phán quyết lịch sử bác bỏ yêu cầu tuyên vô tội* | — | ✦ Cú |  |
| 4-17 | `4.11#3`–`#4` | H | T1 | `t6_jury_deliberation_room` | **ÁN TỬ HÌNH** · *Tội danh cho toàn bộ ba mươi ba vụ tước đoạt sinh mạng con người* | — | ⊘ |  |
| 4-18 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT, BẢN ÁN TÂM LÝ & BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN** | — | ⊘ | ◼ |
| 5-01 | `5.02#1` | H | T1 | `t6_menard_death_row_corridor` | **MƯỜI BỐN NĂM TẠI MENARD** · *Chưa một lần ăn năn chân chính hay gửi lời xin lỗi* | — | ⊘ |  |
| 5-02 | `5.02#2`–`#3` | H | T1 | `t6_clown_oil_painting_easel` | **SÂN KHẤU MỚI TRONG PHÒNG GIAM** · *Hơn hai nghìn tranh sơn dầu Chú hề Pogo rồi tìm cách bán đấu giá* | — | 🅑 |  |
| 5-03 | `5.02#4`–`#5` | H | T1 | `t6_manuscript_victim_34` | **“NẠN NHÂN THỨ BA MƯƠI TƯ”** · *Tự tuyên bố mình là nạn nhân vô tội bị mắc kẹt trong âm mưu chính trị* | — | 🅑 →C |  |
| 5-04 | `5.03#1`–`#4` | C | T1 | `t6_broken_mirror_narcissism` | **CƠ CHẾ PHÒNG VỆ ĐỔ LỖI NGOẠI VI** · *Sự sụp đổ duy nhất là sụp đổ cái tôi ái kỷ — không phải sự ra đi của ba mươi ba thiếu niên* | — | ✦ Cáo →H |  |
| 5-05 | `5.04#1` | H | T5 ngày | `t6_stateville_prison_gates` | **10 · 05 · 1994** · *Trại giam Stateville — bản án tử hình thi hành bằng tiêm thuốc độc* | — | ⊘ |  |
| 5-06 | `5.04#2`–`#4` | H | T1 | `t6_execution_chamber_table` | **LỜI CUỐI CÙNG** · *Không hề ăn năn — chỉ một câu chửi thề đầy khinh miệt* | — | ⊘ |  |
| 5-07 | `5.05` (nghỉ 1.5 s) | — | — | giữ 5-06 | — | Cello u uất trỗi dậy | ⊘ |  |
| 5-08 | `5.06#1`–`#2` | H | T1 | `t6_fbi_academy_lecture_hall` | **MỘT BÀI HỌC ĐẮT GIÁ** · *Một cuộc cách mạng trong nhận thức xã hội và quy trình thực thi pháp luật* | — | ✦ Cú |  |
| 5-09 | `5.06#3`–`#4` | H | T1 | `t6_dossier_gacy_case_06` | **ĐẠO LUẬT TRẺ EM MẤT TÍCH NĂM 1982** · *Sự kiên trì của gia đình nạn nhân thúc đẩy Quốc hội thông qua đạo luật* | — | 🅑 |  |
| 5-10 | `5.06#5` | H | T1 | `t6_evidence_boxes_van` | **TRUNG TÂM QUỐC GIA VỀ TRẺ EM MẤT TÍCH** · *Ra đời năm 1984 — cứu sống hàng chục nghìn thanh thiếu niên* | — | 🅑 |  |
| 5-11 | `5.06#6`–`#7` | H | T1 | `t6_dossier_gacy_case_06` | **GẦN NỬA THẾ KỶ ĐÃ TRÔI QUA** · *Hồ sơ Gacy vẫn là lời nhắc nhở về kẻ săn mồi đội lốt người tốt* | — | ✦ Cú →D |  |
| 5-12 | `5.06#8` | H | T1 | `t6_fbi_academy_lecture_hall` | **BỐN DẤU HIỆU CẢNH BÁO ĐỎ SINH TỒN** · *Đúc kết trực tiếp từ chính hồ sơ này* | — | ⊘ |  |
| 5-13 | `5.06#9`–`#11` | H | T1 | `t6_redflag_charity_facade` | **CẢNH BÁO ĐỎ THỨ NHẤT: VỎ BỌC TỪ THIỆN & ĐỊA VỊ** · *Chiếc mặt nạ nhân ái là công cụ nguy hiểm nhất để làm tê liệt trực giác cảnh giác* | — | 🅑 |  |
| 5-14 | `5.06#12`–`#14` | H | T1 | `t6_redflag_wage_trap` | **CẢNH BÁO ĐỎ THỨ HAI: BẪY VIỆC LÀM THÙ LAO CAO** · *Lời hứa hẹn vượt trội không đòi hỏi kỹ năng — mồi nhử dụ dỗ* | — | 🅑 |  |
| 5-15 | `5.06#15`–`#17` | H | T1 | `t6_redflag_trick_handcuffs` | **CẢNH BÁO ĐỎ THỨ BA: KHÔNG CHO PHÉP KHÓA TAY** · *Biến công cụ khống chế thành trò ảo thuật để nạn nhân tự bỏ quyền tự vệ* | — | 🅑 |  |
| 5-16 | `5.06#18`–`#20` | H | T1 | `t6_redflag_externalized_blame` | **CẢNH BÁO ĐỎ THỨ TƯ: LẮNG NGHE TRỰC GIÁC BẤT AN** · *Tội ác bắt đầu từ những hành động vượt ranh giới tinh vi* | — | 🅑 |  |
| 5-17 | `5.06#21` | H | T1 | `t6_pogo_mask_fallen` | **MẶT NẠ CHÚ HỀ RƠI TRÊN NỀN ĐƯỜNG** · *Sự an toàn thực sự xây từ sự tỉnh táo, lý trí và lòng dũng cảm* | — | ⊘ |  |
| 5-18 | `5.06#22`–`#24` | H | T1 | `t6_closing_rose_closed_dossier` | **CẢM ƠN QUÝ VỊ ĐÃ ĐỒNG HÀNH** · *Bấm đăng ký kênh và chia sẻ góc nhìn ở phần bình luận bên dưới* | — | 🅑 |  |
| 5-19 | hết tập (10 s) | — | T1 | `t6_closing_rose_closed_dossier` | **HỒ SƠ TẬP 06 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật* | Nhạc ngân vang rồi mờ dần `5.07` | ⊘ | ◼ |

**Tổng:** 129 shot · 212 câu · 43 element lời (5 hồi) · nền dùng 65 loại.

## PHỤ LỤC A (Tập 06) — CẤU TRÚC KỊCH BẢN (`parse_kichban.py`)

| Mã | Vai / loại | Câu | Từ | Chỉ dẫn / mô tả |
|---|---|---:|---:|---|
| `1.01` | *BGM* | — | — | Tiếng dương cầm mở đầu trầm buồn, chậm rãi hòa cùng âm thanh Dark Ambient u uất thập niên 70, tạo không gian lịch sử bí ẩn và nghẹt thở. |
| `1.02` | Cú · Host | 8 | 255 | Giọng đọc chậm, trầm ấm, mở đầu không gian tài liệu lịch sử |
| `1.03` | *SFX* | — | — | Tiếng máy ảnh chớp nháy lách tách dồn dập, tiếng vỗ tay tán thưởng vang vọng xa xăm rồi chìm lịm vào tiếng gió rít lạnh buốt của đêm đông Chicago. |
| `1.04` | Cú · Host | 4 | 134 | Hạ trầm giọng, đanh thép và lạnh lùng |
| `1.05` | *Nghỉ 1.5 s* | — | — | Tiếng cello u uất trỗi dậy |
| `1.06` | Cú · Host | 7 | 166 | Tiếp tục mạch kể hồ sơ |
| `1.07` | *SFX* | — | — | Tiếng đóng cửa xe ô tô cọt kẹt giữa đêm buốt giá, tiếng bước chân vội vã giẫm trên nền tuyết lạnh. |
| `1.08` | Cú · Host | 7 | 169 | Trầm giọng nhấn mạnh |
| `1.09` | **Cừu · N1** | 5 | 141 | N1: Kim Byers - giọng nữ trẻ run rẩy, bàng hoàng nghẹn ngào |
| `1.10` | *SFX* | — | — | Tiếng chuông điện thoại bàn tại đồn cảnh sát reo vang dồn dập, tiếng nhấc ống nghe vội vã. |
| `1.11` | Cú · Host | 3 | 71 | Tiết tấu nhanh hơn, dồn dập |
| `1.12` | **Sói · Điều tra viên** | 6 | 155 | Giọng nam sắc bén, quyết đoán, mang tính nghiệp vụ hình sự |
| `1.13` | Cú · Host | 2 | 60 | Mô tả chi tiết phá án |
| `1.14` | **Sói · Điều tra viên** | 3 | 97 | Nhấn mạnh chi tiết then chốt |
| `1.15` | **Cáo · Chuyên gia** | 5 | 173 | Giọng nữ điềm đạm, học thuật, phân tích bản chất tâm lý học |
| `1.16` | Cú · Host | 2 | 73 | Khép lại Hồi 1 |
| `1.17` | *BGM* | — | — | Âm nhạc dâng cao kịch tính rồi chuyển sang nhịp điệu dồn dập mô phỏng cuộc săn đuổi. |
| `2.01` | *BGM* | — | — | Giai điệu Dark Ambient căng thẳng với tiếng gõ kim loại sắc lạnh và nhịp bass dồn dập, mô phỏng cuộc bám đuổi nghẹt thở trên đường phố mùa đông. |
| `2.02` | Cú · Host | 2 | 62 | Giọng hồi hộp, dẫn dắt vào hồ sơ nghiệp vụ |
| `2.03` | **Sói · Điều tra viên** | 4 | 136 | Giọng nghiêm nghị, công bố hồ sơ tiền án |
| `2.04` | **Cáo · Chuyên gia** | 7 | 240 | Phân tích Quỹ đạo leo thang và 4 nấc thang ảo tưởng |
| `2.05` | Cú · Host | 2 | 66 | Tiếp tục mạch truyện điều tra |
| `2.06` | *SFX* | — | — | Tiếng lật mở hồ sơ lệnh tòa án, tiếng bước chân thám tử rà soát hiện trường cọt kẹt trên sàn gỗ. |
| `2.07` | **Sói · Điều tra viên** | 6 | 145 | Liệt kê các vật chứng thu giữ ban đầu |
| `2.08` | Cú · Host | 3 | 97 | Nhấn mạnh ý nghĩa pháp lý của vật chứng |
| `2.09` | **Sói · Điều tra viên** | 8 | 249 | Phân tích Dấu ấn Signature vs Thủ đoạn Modus Operandi |
| `2.10` | Cú · Host | 9 | 278 | Mô tả cuộc đấu trí giám sát trên đường phố |
| `2.11` | **Cáo · Chuyên gia** | 4 | 118 | Phân tích hành vi trêu ngươi |
| `2.12` | Cú · Host | 2 | 58 | Thắt lại nút thắt Hồi 2 |
| `2.13` | *Nghỉ 1.0 s* | — | — | Tiếng còi xe cảnh sát rít xé màn đêm |
| `3.01` | *BGM* | — | — | Không gian âm nhạc chuyển sang dạng Sub-drone trầm đục, u tối và nặng nề đến nghẹt thở, gợi tả sự chìm sâu vào lòng đất lạnh lẽo. |
| `3.02` | Cú · Host | 3 | 83 | Giọng chùng xuống, căng thẳng và ngột ngạt |
| `3.03` | **Sói · Điều tra viên** | 6 | 142 | Giọng dứt khoát, tái hiện thời khắc đột kích |
| `3.04` | *SFX* | — | — | Tiếng bước chân nặng nề trên sàn gỗ, tiếng cạy bẩy then sắt cọt kẹt mở toang nắp hầm dẫn xuống khoảng không dưới sàn nhà. |
| `3.05` | Cú · Host | 2 | 62 | Tả lại không gian rùng rợn dưới nền nhà |
| `3.06` | **Sói · Điều tra viên** | 4 | 117 | Tái hiện quá trình bò vào crawl space |
| `3.07` | *SFX* | — | — | Tiếng lưỡi xẻng cắm sâu vào nền đất xốp ẩm ướt, tiếng thở dốc nghẹn ngào vì kinh hoàng của người điều tra. |
| `3.08` | Cú · Host | 3 | 88 | Giọng nghẹn lại, xúc động sâu sắc |
| `3.09` | *Nghỉ 1.5 s* | — | — | Tiếng thở dài trầm lặng |
| `3.10` | **Sói · Điều tra viên** | 7 | 180 | Công bố số liệu cuộc khai quật lịch sử |
| `3.11` | **Cáo · Chuyên gia** | 15 | 483 | Phân tích sâu sắc Cơ chế Chia ngăn nhận thức |
| `3.12` | Cú · Host | 3 | 84 | Khép lại Hồi 3 |
| `3.13` | *BGM* | — | — | Một nốt trầm kéo dài u uất rồi rơi vào sự im lặng buốt giá. |
| `4.01` | *BGM* | — | — | Âm thanh vĩ cầm u uất, giằng xé kết hợp nhịp gõ đều đặn của đồng hồ, tái hiện cuộc đấu trí tâm lý căng thẳng tột cùng tại phòng hỏi cung và pháp đình. |
| `4.02` | Cú · Host | 3 | 92 | Mở đầu Hồi 4 |
| `4.03` | **Sói · Điều tra viên** | 5 | 133 | Giọng vạch trần âm mưu của hung thủ |
| `4.04` | Cú · Host | 1 | 35 | Dẫn dắt sang lời khai nhân chứng nghiệp vụ |
| `4.05` | **Mèo · N2** | 5 | 154 | N2: Sĩ quan Mike Albrecht - giọng nam trung niên trầm ấm, cứng cáp và chân thực |
| `4.06` | Cú · Host | 3 | 93 | Phân tích bối cảnh phiên tòa lịch sử |
| `4.07` | **Cáo · Chuyên gia** | 4 | 144 | Phân tích học thuật tại tòa |
| `4.08` | Cú · Host | 1 | 34 | Tái hiện cuộc phản công của công tố viên |
| `4.09` | **Sói · Điều tra viên** | 5 | 154 | Trình bày các luận cứ đanh thép của cơ quan công tố |
| `4.10` | **Cáo · Chuyên gia** | 2 | 78 | Đúc kết bản chất pháp tâm thần học |
| `4.11` | Cú · Host | 4 | 78 | Tuyên bố phán quyết lịch sử |
| `4.12` | *SFX* | — | — | Tiếng búa gõ phán quyết của thẩm phán vang lên đanh thép ba lần "Cộp! Cộp! Cộp!", chốt lại số phận của kẻ sát nhân. |
| `5.01` | *BGM* | — | — | Nhạc nền chuyển sang giai điệu Dương cầm (Minimalist Piano) sâu lắng, ấm áp nhưng đượm buồn và suy tư, mang âm hưởng triết lý nhân văn. |
| `5.02` | Cú · Host | 5 | 167 | Giọng suy ngẫm, triết lý |
| `5.03` | **Cáo · Chuyên gia** | 4 | 150 | Bóc tách Sự tự thương hại bệnh lý và Sụp đổ cái tôi ái kỷ |
| `5.04` | Cú · Host | 4 | 114 | Khoảnh khắc thi hành án |
| `5.05` | *Nghỉ 1.5 s* | — | — | Tiếng thở dài trầm lặng của Host |
| `5.06` | Cú · Host | 24 | 698 | Chuyển sang dư chấn xã hội và cải cách thể chế |
| `5.07` | *BGM* | — | — | Nhạc nền ngân vang ấm áp rồi mờ dần và tắt hoàn toàn ở giây thứ 5. |
| | **Tổng** | **212** | **6306** | |

## PHỤ LỤC B (Tập 06) — THẨM ĐỊNH KỊCH BẢN & TUÂN THỦ V9

- **Fact-checking đạt 100%:** Toàn bộ dữ kiện về vụ án John Wayne Gacy được đối chiếu chéo qua các nguồn chính thống: Hồ sơ Sở Cảnh sát Des Plaines, Văn phòng Cảnh sát trưởng Hạt Cook, hồ sơ Tòa án Hạt Cook 1980, tư liệu của FBI BSU (Robert Ressler), phỏng vấn của Tiến sĩ Helen Morrison và các báo cáo báo chí uy tín (Chicago Tribune, Chicago Sun-Times).
- **Tuân thủ V9 tuyệt đối:**
  - Không có từ ngữ kích hoạt kiểm duyệt YouTube (cấm từ bạo lực, tình dục trẻ vị thành niên, thương tích man rợ).
  - Trọng tâm phân tích 100% hướng về tâm lý học tội phạm: Sự tha hóa nhân cách dưới vỏ bọc thiện nguyện, bẫy cơ hội việc làm thanh thiếu niên, ảo thuật còng tay vô hiệu hóa khả năng tự vệ và cơ chế đổ lỗi ngoại vi.
  - Tôn vinh tính trang nghiêm, khoa học của công tác điều tra hình sự và pháp y nhân chủng học.

---

## PHỤ LỤC C (Tập 06) — DỰNG LẠI VỚI GIỌNG TIẾNG VIỆT (HIGGS AUDIO v3) · 02/11/2026

### C.1. Vì sao phải dựng lại toàn bộ

Master cũ (24/10/2026, 25:29) dùng **bộ giọng A** — `English_*`/`Korean_*` đọc tiếng Việt. Người dùng đổi sang **giọng tiếng Việt thật** (Higgs Audio v3, chạy trên Kaggle GPU) ⇒ **âm thanh đổi hoàn toàn** ⇒ theo A11 #55 / H14 phải chạy lại `parse_shots.py` → `build_video3.py`, không chỉ `package.py --mux`.

| | Master cũ (bộ A) | Master mới (Higgs) |
|---|---|---|
| Thời lượng | 1529,1 s (25:29) | **1265,4 s (21:05)** |
| Số câu | 165 | **154** (kịch bản tách lại 01/11/2026) |
| Shot | 73 (bảng shot cũ, lệch 14 mã câu) | **73** (bảng shot viết lại) |

### C.2. Bảng shot — viết lại theo NỘI DUNG (A11 #67)

Mục 6 vẫn trỏ mã câu của bản 165 câu. 11 element đổi số câu: `1.06` 8→7 · `1.08` 5→6 · `1.09` 6→5 · `1.14` 3→2 · `3.05` 3→1 · `3.07` 3→2 · `3.09` 2→1 · `3.10` 5→4 · `4.08` 4→3 · `5.02` 6→4 · `5.04` 4→3.
Map cũ→mới bằng **diff nội dung câu** (đọc bản gốc ở commit `f3b5db9`), **không đoán số thứ tự**. Kết quả:

- **26 dòng sửa** + **thêm shot `1-15`** (cho câu mới `1.08#6` — lời dẫn dắt về Kim Byers) + **xoá shot `3-04`** (nội dung "hộp sáp thơm khử mùi" đã bị gỡ khỏi kịch bản) + đánh lại id Hồi 1 (`1-15`→`1-23`) và Hồi 3 (`3-04`→`3-10`).
- **Sai cột Vai ở 10 dòng** (bản cũ): `2-02` `2-03` `2-10` ghi H nhưng là Điều tra viên (D) · `3-03` `3-06` `3-07` ghi D nhưng là Host (H) · `3-10` ghi H nhưng là D · `4-02` ghi H nhưng là D · `4-03` ghi D nhưng là N2 (Mike Albrecht) ⇒ badge/bán thân hiện **sai người nói**. Đã sửa.
- **Số trên hình không có trong câu**: `13 · 03 · 1980` (kịch bản ghi **12**/3/1980) · `12/12/1978` · `Trại cải tạo Anamosa` (kịch bản ghi Waterloo) · `Mức lương cao gấp hơn hai lần` (ghi "gần gấp đôi") · `Cảnh báo đỏ 4 / 3 / 2 / 1` (thứ tư/nhất/ba/hai) · `mười tám tháng` (ghi 18). Đã sửa.
- **Câu trích không nguyên văn**: `"MẸ ƠI, MẸ ĐỢI CON VÀI PHÚT NHÉ"` (đã gỡ khỏi kịch bản) · `"Kiss my ass"` (đã gỡ) · `"Họ bảo tôi là quái vật"` (nay là "tự truyện và các đoạn ghi âm") · trích của N1/N2 viết lại theo nguyên văn câu mới. Đã sửa.
- **Nền không còn khớp câu**: `3-04` sáp thơm · `4-08` "ảo thuật còng tay" (chi tiết đã bị gỡ khỏi `4.08`) ⇒ đổi nền + tiêu đề. Đã sửa.
- **Từ bị cấm theo A9.2**: `đòn roi` (4-05) → `bị bạo hành`. Đã sửa.

### C.3. Cột "Nhân vật" — sửa lỗi chưa từng ai phát hiện

Tap06 đặt mã handoff `→X` ở **cột chuyển cảnh** (cột 9) trong khi `parse_shots.py` đọc handoff từ **cột Nhân vật** (cột 8) ⇒ **0/73 shot có handoff** ⇒ badge "TIẾP THEO" (Host mời ai) **chưa bao giờ hiện** trong Tap06 (Tap04 có 7 shot, Tap05 có 2 shot). Đã chuyển handoff về đúng cột và **tính lại theo quy tắc**: `handoff(dòng i) = vai của dòng i+1` (quy tắc này tái tạo đúng bảng gốc ở Tap04/Tap05).

### C.4. QC đã chạy

| Cổng | Kết quả |
|---|---|
| A9.2 bảng shot (`.work/_qc_tap06_shots_v2.py`, 10 cổng) | ✅ phủ 154/154 câu, 0 trùng · Vai khớp script · handoff đúng · nền có file · số trên hình có trong câu · trích nguyên văn · 0 từ cấm · thẻ kết H12 · đúng thứ tự thời gian |
| A9.3 ảnh tĩnh | ✅ 73/73 shot render + 5 contact sheet, soi mắt không lỗi |
| A9.1 âm thanh (master mp3) | ✅ −16,2 LUFS · true peak −1,6 dBFS · 0 khoảng câm > 0,3 s ở −60 dB · lời đầu 23,0 s |
| A9.4 file cuối | xem báo cáo QC cuối trong `02_SAN_XUAT/Tap06/` |

### C.5. Giọng — Higgs Audio v3 trên Kaggle (02/11/2026)

- **Master** `xuat_ban/Tap06_master.mp3`: 1265,4 s · −16,2 LUFS · true peak −1,6 dBFS · 0 khoảng câm > 0,3 s · lời đầu 23,0 s.
- **F0 câu neutral:** H 119/126 · D 87/87 · C 209/211 · N1 177/176 · N2 291/291 Hz. **G9** đạt (D–H 5,38 · C–H 8,95 · H–N1 5,85 · C–D 15,05 · D–N2 20,80 · H–N2 14,56 nc).
- **QC**: 3 lượt (309 file → 62 file → 12 file đổi chữ), CER vòng 3 = 0%. Whisper large-v3 + UTMOS trên Kaggle làm phép thử thứ hai (A11 #74).
- **Danh sách nghe:** `CanNghe_Tap06_higgs.md`. Bản MiniMax cũ: `.work/_cu/t06_minimax_20261102/`.
- Mô tả YouTube PHẢI có dòng ghi công Higgs (QUY_TAC_AUDIO_HIGGS §2).

---

## PHỤ LỤC D (Tập 06) — NGUỒN THAM KHẢO ĐÃ KIỂM CHỨNG · 02/11/2026

### D.1. Nguyên tắc (L2 / A10)

Không bịa dữ kiện, con số, câu trích hay **link nguồn**. Mỗi URL phải **thật sự mở được** — đã đo HTTP status thật, không dựa vào kết quả search snippet.

### D.2. Số đo

| Mục | Số |
|---|---|
| URL ứng viên đã thử | 50 |
| HTTP 200 → dùng | **20** |
| HTTP 403 (Cloudflare/bot-block) | 6 → loại (không đọc được nội dung để đối chiếu) |
| HTTP 404 (sai slug) | 7 → loại |
| 409 / 429 / ERR / timeout | 5 → loại |
| Mốc dữ kiện đối chiếu | **58** (51 ✅ · 7 ⚠) |

### D.3. Nguồn dùng (20)

| # | Nguồn | Vai trò |
|---|---|---|
| 1 | Wikipedia — John Wayne Gacy | Dòng thời gian, số nạn nhân, nhân cách |
| 2 | Clark County State's Attorney (IL) — hồ sơ vụ án Gacy #237 | Hồ sơ chính thức của viện chưởng viện |
| 3 | Chicago Tribune — dòng thời gian vụ án | Mốc thời gian cảnh sát / tòa |
| 4 | Chicago Tribune — 40 năm sau, danh sách nạn nhân | 33 nạn nhân |
| 5–7 | A&E — xét xử · vụ bắt giữ · Case File | Diễn biến từng đoạn |
| 8 | Encyclopedia.com — hồ sơ xét xử 1980 | Thẩm phán, công tố, bào chữa |
| 9 | Biography.com | Tiểu sử, lời cuối |
| 10–11 | Netflix Tudum · Slate | Hồ sơ tổng hợp, 26 thi thể trong crawlspace |
| 12 | Solve The Case | Lịch thi hành án |
| 13 | Joyce & Stover — *Witnesses from the Grave* (bản toàn văn trên archive.org) | Kích thước hầm, nhân chủng học |
| 14–16 | Esquire · Oxygen · TheWrap | Lời kể thám tử Des Plaines |
| 17–18 | NBC News · LegalNews (AP) | "Nạn nhân thứ 34", lời tự thú cho luật sư |
| 19 | Chicago Bar Association — bản vụ của William Kunkle | Góc nhìn công tố viên trưởng |
| 20 | Den of Geek | Tổng quan |

### D.4. Quy trình (generator + validator)

- **Generator:** `.work/_gen_t06_sources.py` → ghi `02_SAN_XUAT/Tap06/nguon_mo_ta.txt` (khối chèn vào mô tả) và `02_SAN_XUAT/Tap06/nguon_tham_khao.md` (bảng đối chiếu).
- **Sửa ở generator, KHÔNG sửa file thành phẩm** (A11 #70): `xuat_ban/mo_ta.txt` và `xuat_ban/nguon_tham_khao.md` là file **sinh ra**.
- **4 cổng validator chặn ghi file:** (1) URL phải có HTTP 200 trong cache `.work/_src_cache/` **và** nội dung ≥ 500 byte; (2) mã câu phải tồn tại trong `script_tap06.json`; (3) khoá nguồn hợp lệ **và mọi nguồn đều phải được dùng**; (4) không trùng mã câu.
- **Sinh lại mô tả:** `.work/_regen_desc_t06.py` — gọi `description()` **trực tiếp**, không gọi CLI (A11 #72) ⇒ `thumbnail.png` và `Tap06_master.mp4` giữ nguyên hash. Đã đo: `mo_ta.txt` **4067 ký tự** (< 5000 của YouTube), UTF-8 không BOM, không byte NUL.
- **Sao lưu (L5):** `.work/_cu/t06_mo_ta_truoc_nguon/`, `.work/_cu/provenance_truoc_nguon_t06.json`.

### D.5. 7 mốc `⚠` chờ người dùng duyệt

`1.08#1` (mức lương tối thiểu) · `2.06#3` ("phù hiệu cảnh sát giả") · `2.11#2` ("nhà hàng ăn nhanh", "gõ cửa kính xe") · `2.11#3` ("trả tiền bữa ăn") · `3.06#1` ("cao chưa đầy một mét") · `3.11#1` ("chưa từng thấy ở Illinois") · `5.02#3` ("hàng trăm tranh").

Chi tiết đối chiếu từng câu: `02_SAN_XUAT/Tap06/BaoCao_QC_Tap06_20261102.md` §5.1.
**Sửa kịch bản = dựng lại toàn bộ** (TTS → ảnh tĩnh → video 28 phút → phụ đề → đóng gói) ⇒ cần người dùng quyết trước (L4).

### D.6. Điểm đã xác minh là KHÔNG mâu thuẫn

Nghi vấn ban đầu: nhiều nguồn ghi "13/3/1980". Hồ sơ viện chưởng viện làm rõ **12/3/1980 = phán quyết có tội**, **13/3/1980 = ngày tuyên án** ⇒ kịch bản `4.10#1` + `4.10#2` **đúng, không sửa**.

### D.7. Trạng thái sửa 7 câu `⚠` — **CHỜ, chưa áp dụng** (03/11/2026)

Người dùng đã chốt sửa cả 7 câu và dựng lại toàn bộ. Việc sửa **đã dừng** vì blocker kỹ thuật thật.

| Mục | Trạng thái |
|---|---|
| Gói sửa chuẩn bị | `02_SAN_XUAT/Tap06/DeXuat_Sua_Tap06.md` — 7 câu + 11 chữ trên hình, câu hiện tại trích tự động từ `script_tap06.json` |
| Kịch bản | **KHÔNG đổi** — `01_KICH_BAN/Tap06/kichban_tap06_23102026.md` giữ nguyên |
| Bảng shot mục 6 | **KHÔNG đổi** |
| Video / audio / phụ đề | **KHÔNG đổi** — `Tap06_master.mp4` giữ nguyên hash `36976c211b4c…` |
| Blocker | **Higgs Audio v3 chỉ chạy được trên Kaggle GPU.** Máy này: không GPU, không `kaggle` CLI, không `~/.kaggle/kaggle.json`, không module `kaggle`/`torch`/`mlx_audio` ⇒ **không tạo lại được 7 file WAV** |

**Audit bổ sung (03/11/2026):** 73/73 chữ trên hình đã đối chiếu với câu kịch bản ⇒ phát hiện thêm **4 lỗi caption mới** ngoài 7 câu `⚠`:

| Shot | Chữ hiện tại | Vấn đề |
|---|---|---|
| `2-15` | RÚT TIỀN MẶT CHUẨN BỊ BỎ TRỐN | không nguồn nào xác nhận |
| `3-03` | NẮP HẦM KỸ THUẬT PHÒNG NGỦ | nguồn ghi nắp hầm ở **tủ quần áo** (closet) |
| `5-07` | BÀI HỌC KINH ĐIỂN TẠI HỌC VIỆN FBI | không nguồn nào nhắc "FBI Academy" |
| `1-05` | Vận hành suốt gần một thập kỷ | nguồn: các vụ giết 1972–1978 = 6 năm |

Cổng QC "số trên hình có trong câu" **không bắt được** loại lỗi này vì đây là *hành vi* khẳng định chứ không phải *số*.

Chi tiết đầy đủ: `BaoCao_QC_Tap06_20261102.md` §6.- **03/11/2026 — sửa 6 câu theo nguồn** (`2.06#3`, `2.11#2`, `2.11#3`, `3.06#1`, `3.11#1`, `5.02#3`; `1.08#1` giữ nguyên — DOL: liên bang 2,65 USD từ 01/01/1978) → Higgs vòng 4 (24 file, CER 0%) → master **1260,9 s · −16,3 LUFS · −2,3 dBFS · 0 câm · lời đầu 23,0 s** ✅. Mục 6 sửa 10 chữ trên hình + 5 lỗi H6/K3 do QC bắt; phụ đề, nguồn (0 ⚠), mô tả sinh lại. **Video chưa dựng lại** (mp4 cũ 1265,4 s lệch audio). Chi tiết: `BaoCao_QC_Tap06_20261102.md` §9. Bản kịch bản trước khi sửa: `.work/_cu/t06_minimax_20261102/kichban_tap06_truoc_sua6cau_20261103.md`; master 02/11: `.work/_cu/t06_higgs_v1_20261103/`.
- **03/11/2026 (lần 2)** — người dùng đồng ý sửa `1.04#1` ("gần một thập kỷ" → "nhiều năm") và `5.02#1` ("nằm trong khu biệt giam tử tù" → "chờ thi hành án") → Higgs vòng 5 (8 file, CER 0%) → master **1258,4 s · −16,2 LUFS · −1,8 dBFS · 0 câm · lời đầu 23,0 s** ✅. Phụ đề/shot/nguồn/mô tả sinh lại. **Video chưa dựng lại.** Bản trước: `.work/_cu/t06_higgs_v2_20261103/`.

---

## PHỤ LỤC E (Tập 06) — DỰNG LẠI VIDEO SAU KHI SỬA 6 CÂU + 11 CHỮ TRÊN HÌNH · 03/11/2026

### E.1. Vì sao phải chia build thay vì chạy một lần

Một lần build **37.751 frame** (1.258,37 s × 30 fps) mất **~73 phút** > trần **60 phút** của một lệnh bash ⇒ lần dựng đầu bị hủy giữa chừng: 6 part chỉ còn ~3.000/6.292 frame và **không có moov atom** (`ffprobe`: `moov atom not found`) ⇒ **không dùng được**, phải làm lại từ đầu.

`render(fi)` trong `build_video3.py` **chỉ phụ thuộc `fi`** (nền, phụ đề, badge, nhân vật đều lấy theo thời gian tuyệt đối) ⇒ chia theo khoảng frame cho kết quả **y hệt** một lần build liên tục.

| Nửa | Frame | `--from` → `--to` | Thư mục part |
|---|---|---|---|
| A | 0 – 18.874 | `0` → `629.167` | `.work/video3_t06_A/` |
| B | 18.875 – 37.750 | `629.167` → `1258.37` | `.work/video3_t06_B/` |

Tổng = **37.751 frame** = `int(timeline.total × 30)`. Ghép **một** lần `ffmpeg -f concat -safe 0 -c copy` (không ghép 2 vòng) ⇒ `.work/video3_t06/picture.mp4`.

### E.2. Hai tối ưu đo được — không suy đoán

| Cấu hình | Aggregate | Ghi chú |
|---|---|---|
| 6 tiến trình, **chỉ render** (không encode) | **12,60 fps** | trần cứng của máy |
| 6 tiến trình, pipe mặc định của Windows (**4 KB**) | **8,32 fps** | mất **34 %** chỉ vì đường ống |
| 6 tiến trình, **pipe buffer 4 MB** | **11,58 fps** | đạt **92 %** trần |
| 10 tiến trình, chỉ render | 13,27 fps | máy **bão hoà** ở ~13 fps |

CPU lúc build chỉ ~**42 %** (6 tiến trình × ~55 %) ⇒ nút thắt là **băng thông bộ nhớ**, **không phải CPU** ⇒ **thêm worker không giúp** (đo ở 2 mức 6 vs 10 mới kết luận được).

Tối ưu `finishing()` (cast `float32` rõ ràng + vignette pre-expand `(H,W,3)`): **127,8 → 94,0 ms/frame (−26 %)**, kết quả **BIT-IDENTICAL** — kiểm **240/240** mẫu (120 frame × 2 nguồn: mảng ngẫu nhiên + frame thật) ⇒ **73 ảnh tĩnh đã QC vẫn hợp lệ**, không phải render lại.

### E.3. Không sửa script dùng chung (L9)

Dùng **bản sao** `.work/_build_video3_split.py` (đọc `AE_VID` từ env, tắt mặc định ba patch) ⇒ **`build_video3.py` không đổi một byte** ⇒ không phát sinh nghĩa vụ hồi quy Tập 01 cho file đó.
Hồi quy vẫn chạy độc lập: `AE_EP=01 py -3 .work/parse_shots.py` ⇒ `shots.json` giữ nguyên hash `37C9B0247AA628F8…` ✅.

Ba patch đều **tắt mặc định**, bật bằng env:

| Env | Tác dụng |
|---|---|
| `AE_VID` | thư mục chứa part (A/B) |
| `AE_PIPE_BUF` | buffer pipe (4.194.304 B) — A11 #100 |
| `AE_FAST_FINISH` | `finishing()` tối ưu, bit-identical — A11 #102 |

### E.4. Kết quả

| Mục | Kết quả |
|---|---|
| Nửa A | 6 part · 18.875 frame · `pictureA.mp4` 629,166667 s · 222.297.610 B |
| Nửa B | 6 part · 18.876 frame · `pictureB.mp4` |
| Ghép | **12 part → `picture.mp4`: 37.751 frame · 1.258,366667 s · 446.191.166 B** · DTS không N/A |
| Đóng gói | `Tap06_master.mp4` **477.815.032 B** (455,7 MB) · 1.258,366667 s · h264 + AAC 48 kHz stereo 192k · sha256 `951bb0ba44f2…` |
| `thumbnail.png` | **không đổi** (`d55e50665fe1…`) — không gọi `thumbnail()` (A11 #72) |
| Mô tả / nguồn | `mo_ta.txt` 4.138 ký tự (< 5.000) · `nguon_tham_khao.md` 58 dòng — **không đổi** |
| QC tổng | **23 OK · 2 cảnh báo (có sẵn) · 0 lỗi** |
| Lag A/V | **+0,0 ms** (r = 0,9998) |
| Khung hình vs ảnh tĩnh đã QC | **12/12 khớp** |

Thời gian thực: nửa A ~24 phút · nửa B 2.754,5 s (45,9 phút) · ghép + kiểm 671,6 s.
Chi tiết đầy đủ: `BaoCao_QC_Tap06_20261102.md` §10.



## PHỤ LỤC F (Tập 06) — ĐỌC LẠI AUDIO HIGGS 3 NGÔN NGỮ (VI · EN · JA) · 06/11/2026

**Lý do:** kịch bản 4 ngôn ngữ sửa 05/11 (10 chỉ dấu, 154 → 212 câu) ⇒ audio cũ lệch. Engine Higgs v3 trên Kaggle, giọng mẫu VoxCPM2 (bộ đã chốt mỗi ngôn ngữ).

**P0 — sửa lỗi K4 (A11 #120):** `acting_tap06.json` (10 `alt` gắn nhầm câu), `sfx_tap06.json` (mốc nền/tiếng động/tắt nhạc), `tts_manifest_t06/_EN_t06.json` (154/165 câu) đều theo mã cũ ⇒ chuyển theo nội dung / sinh lại. Bản cũ: `.work/_cu/t06_higgs_redo_20261106/`. ⚠ Bảng `sfx` mới chờ người dùng duyệt.

| | Lượt 1 | Vòng 2 | G9 (min AC/YIN) | G8 loại | Master | LUFS / đỉnh / câm / lời đầu | Cần nghe |
|---|---|---|---|---|---|---|---|
| VI | 445 file | 59 câu / 118 file | D–H 5,17 · C–H 8,64 · H–N1 6,03 ✅ | 5 | `Tap06/xuat_ban/Tap06_master.mp3` 1893,0 s | −16,2 / −2,1 / 0 / 23,0 s ✅ | 21 câu |
| EN | 446 file | — | **D–H 2,47 (YIN 6,8)** ⚠ · còn lại ✅ | 3 + 1 đuôi câm | `Tap06_EN/xuat_ban/Tap06_EN_master.mp3` 1759,6 s | −16,2 / −1,9 / 0 / 23,0 s ✅ | 9 câu |
| JA | 424 file | — | D–H 6,06 · C–H 10,27 ✅ | 1 + 2 đuôi câm | `Tap06_JA/xuat_ban/Tap06_JA_master.mp3` 2080,3 s | −16,2 / −1,8 / 0 / 23,0 s ✅ | 30 câu |

- **Người dùng chốt 06/11/2026:** dừng đo `listen_audio` (MCode tắt) và ghép master với số đo hiện có. Chọn bản: VI = CER `listen_audio` lượt 1 (273 file) + Whisper (290 file); EN/JA = CER Whisper large-v3 (Kaggle); EN/JA **không có vòng 2**.
- UTMOS tb (H/D/C): VI 2,39/3,14/2,82 · EN 4,36/3,88/4,40 · JA 2,91/3,73/4,14 (chỉ so tương đối).
- JA: 5 file đuôi lặng 0,9–5,7 s đã cắt (giữ 0,3 s + fade 30 ms; gốc `.work/_cu/t06_higgs_redo_20261106/ja_duoi_cam/`).
- EN 2.07#4: mọi bản lệch cao độ — dùng bản ít lệch, cần nghe. EN D–H dưới 4 nc theo AC như Tập 02 EN (người dùng đã chấp nhận ở Tập 02) — cần nghe lại.
- Danh sách nghe: `Tap06/CanNghe_Tap06_higgs.md`, `Tap06_EN/CanNghe_Tap06_EN_higgs.md`, `Tap06_JA/CanNghe_Tap06_JA_higgs.md`.
- **Audio đổi ⇒ chưa dựng lại hình (H14)**: phải `parse_shots.py` + `build_video3.py` cho cả 3 ngôn ngữ.


---

## B-DUNG 07/11/2026 - Dựng hình VN / EN / JA từ master mới (06/11)

- Master dùng: `Tap06_master.mp3` 1892,98 s · `Tap06_EN_master.mp3` 1759,64 s · `Tap06_JA_master.mp3` 2080,32 s. `timeline.total` = thời lượng mp3 (cổng T20 đạt). Chạy lại `parse_shots.py` (H14) -> 129 shot x 3 bản; ảnh tĩnh render lại 129 x 3. Bản cũ lưu ở `.work/_cu/t06_dung_20261107/`.
- ASR từng câu trên master (Whisper small, cửa sổ theo timeline): VN 212/212 (tb 0,936) · EN 212/212 (tb 0,992) · JA 212/212 (tb 0,904, sai do đồng âm kanji). Câu cần nghe: `1.09#2` VN (N1, ~4:25).
- Ghép dùng `alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1` (A11 #114). `EPISODES["06"]` chưa khai `mux_af` -> package.py mặc định thiếu latency=1.
- `assets/brand/intro_kenh_JA_t06.mov` = bản sao `intro_kenh_JA_t05.mov` (JA t04 = t05 giống byte).
- Thẻ kết hiện rõ đến total-5 s rồi mờ dần về đen (A11 #65).

### Lỗi nhịp nghỉ (07/11/2026, người dùng nghe: "đọc nhanh, không chậm rãi") — AGENTS A13, A11 #135
- Tốc độ đọc trong câu bình thường (3,61 tiếng/s, = Tập 05). Lỗi là **khoảng nghỉ giữa câu**: trung vị 0,35 s (Tập 05: 0,74 s); câu dính liền VN 138/207, JA 171/207 (JA **không có** `acting_tap06_JA.json`), EN 89/207.
- Đã sửa file diễn xuất bằng `.work/_fix_pause_t06.py`: VN 37→135 mục, JA 0→135, EN 113→162. Dự đoán: trung vị VN 0,75 · JA 0,65 · EN 0,75 s; < 0,4 s còn 20% mỗi bản. Master dài thêm ≈ 39 / 45 / 20 s.
- **Master + mp4 giao ngày 07/11 là bản LỖI NHỊP** — phải trộn lại `build_audio3.py` (không cần đọc lại giọng), đo cổng A13, rồi `parse_shots.py` + dựng lại hình (H14). Bản acting cũ: `.work/_cu/t06_dung_20261107/`.
