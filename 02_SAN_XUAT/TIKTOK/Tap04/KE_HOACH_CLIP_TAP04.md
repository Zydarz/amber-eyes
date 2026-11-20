# KẾ HOẠCH CLIP TIKTOK — TẬP 04 · "THIÊN THẦN TỬ THẦN & PHỨC CẢM CHÚA TRỜI"
*Ngày: 20/11/2026 · Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*
*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap04/SPEC_AUDIO_CLIP_TAP04.json`*
*Nguồn duy nhất của mọi dữ kiện: `02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md` · `.work/timeline_s_t04.json` (212 câu) · `02_SAN_XUAT/Tap04/nguon_tham_khao.md`*

---

## 0. Tóm tắt chốt

| Hạng mục | Giá trị |
|---|---|
| Số clip | **5 clip** (TK1–TK4 chính + TK5 bài học sinh tồn) |
| Tổng câu đọc | **48 câu** đọc giọng (chuẩn hóa đo lường ASR) |
| Độ dài đo thực tế | Ước lượng 63.2 – 82.3 s/clip (mục tiêu 60–90 s · cổng QC 45–95 s) |
| Chủ đề | Mỗi clip = **1–2 chỉ dấu tâm lý cốt lõi** của Tập 04 (K10) |
| Ngôn ngữ | Tiếng Việt · vai Host (H), Điều tra viên (D), Chuyên gia (C), Y tá Somerset (N1), Y tá Amy (N2) |
| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** (bộ giọng chuẩn Tập 04) |
| Hình ảnh | Nền dọc 9:16 crop/pad từ 51 nền noir 2K gốc của Tập 04 |
| Chi phí | **0 đồng** (Kaggle GPU có sẵn) |

---

## 1. Năm clip và chỉ dấu tâm lý tương ứng (K10)

| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng thời lượng |
|---|---|---|---|---|
| **TK1** | #6 · #7 | Kẽ hở công nghệ máy phát thuốc Pyxis & Quỹ đạo leo thang của Thiên thần Tử thần | *"Nhập lệnh lấy thuốc độc. Rồi nhấn hủy chỉ sau một giây."* | 63.2 s · 9 câu |
| **TK2** | #9 · #1 | Hiệu ứng hào quang (Halo Effect) & Điểm mù xã hội trước kẻ săn mồi hiền lành | *"Người y tá hiền lành nhất bệnh viện. Lại là kẻ sát nhân tàn khốc nhất."* | 77.9 s · 11 câu |
| **TK3** | #6 · #4 | Điểm gãy tâm lý & Cuộc đối đầu sinh tử của Amy Loughren tại quán ăn | *"Chiếc micro dưới áo khoác mùa đông. Và cuộc hẹn sinh tử tại quán ăn."* | 82.3 s · 10 câu |
| **TK4** | #9 · #3 | Sự thờ ơ thể chế (Institutional Bystander Effect) & 400 nạn nhân trong bóng tối | *"Chín bệnh viện biết hắn có vấn đề. Nhưng tất cả đều chọn im lặng."* | 71.7 s · 9 câu |
| **TK5** | #10 | Nạn nhân học & Bài học sinh tồn: Dũng cảm phá vỡ sự im lặng | *"Bài học sinh tồn lớn nhất: Đừng bao giờ im lặng trước cái ác."* | 75.7 s · 9 câu |

**Thứ tự đăng đề xuất:** TK2 → TK1 → TK3 → TK4 → TK5

---

## 2. Diễn xuất và đặc tả chi tiết từng clip

### TK1 — "Nấc thang hủy lệnh Pyxis và lỗ hổng chết người"

*Thời lượng: 63.2 s (9 câu) · BGM: `bgm_ambient_tension.mp3` (Hồi 2 — bed tập: bgm_ambient_tension.mp3)*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK1.01#1` | H | neutral | -0.02 | 0.5 | `t4_pyxis_station` | still | Nhập lệnh lấy thuốc độc. Rồi nhấn hủy chỉ sau một giây. | `hook — không phải dữ kiện kịch bản` |
| `TK1.01#2` | D | neutral | -0.03 | 0.6 | `t4_pyxis_station` | pull | Vào đầu những năm 2000, các bệnh viện bắt đầu sử dụng tủ cấp phát thuốc tự động Pyxis MedStation để quản lý dược phẩm chặt chẽ hơn. | `2.06#1` |
| `TK1.01#3` | D | neutral | -0.03 | 0.6 | `t4_pyxis_station` | pan | Tuy nhiên, Charles Cullen đã phát hiện ra một lỗ hổng nghiêm trọng trong thiết kế phần mềm của hệ thống này. | `2.06#3` |
| `TK1.01#4` | D | neutral | -0.03 | 0.6 | `t4_pyxis_drawer_ajar` | push | Hắn nhập lệnh yêu cầu lấy những loại thuốc độc bảng A như Digoxin, Insulin hay Norepinephrine, nhưng ngay khi ngăn kéo máy vừa mở ra, hắn lập tức nhấn nút hủy lệnh. | `2.06#4` |
| `TK1.01#5` | D | neutral | -0.03 | 0.7 | `t4_pyxis_drawer_ajar` | still | Hệ thống máy tính ghi nhận giao dịch đã bị hủy và không trừ thuốc vào tài khoản bệnh nhân, nhưng trên thực tế, viên thuốc độc đã nằm gọn trong túi áo của Cullen. | `2.06#5` |
| `TK1.01#6` | D | neutral | -0.03 | 0.7 | `t4_pyxis_printout` | push | Tại bệnh viện Somerset, hắn mất hoàn toàn khả năng kiềm chế, sát hại cả những bệnh nhân trẻ tuổi đang bình phục khỏe mạnh. | `2.06#14` |
| `TK1.01#7` | C | neutral | -0.02 | 0.7 | `t4_neutral_letter` | pull | Ngược lại, chữ ký tâm lý Signature – thứ nhu cầu cảm xúc bất biến thúc đẩy hắn gây án – chính là “Phức cảm Chúa trời”. | `2.08#5` |
| `TK1.01#8` | C | neutral | -0.02 | 0.7 | `t4_institutional_bystander` | still | Hắn cảm thấy bản thân mình trở nên vĩ đại, đứng trên cả y học và số phận khi có quyền quyết định ai được thở và ai phải dừng lại. | `2.11#7` |
| `TK1.01#9` | H | neutral | -0.02 | 0.0 | `t4_closing_desk` | still | Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | `CTA — không phải dữ kiện kịch bản` |

**Lớp phủ chữ trên hình (Text Overlays):**
- `TK1.01#1`: **"MÁY PHÁT THUỐC TỰ ĐỘNG PYXIS MEDSTATION"** (3.0 s)
- `TK1.01#4`: **"LỖ HỔNG HỦY LỆNH: DIGOXIN & INSULIN BIẾN MẤT"** (2.5 s)
- `TK1.01#6`: **"GIAI ĐOẠN 4: MẤT KIỂM SOÁT HOÀN TOÀN"** (2.5 s)
- `TK1.01#7`: **"CHỮ KÝ TÂM LÝ: “PHỨC CẢM CHÚA TRỜI”"** (2.5 s)
- `TK1.01#8`: **"ẢO TƯỞNG TOÀN NĂNG ĐỨNG TRÊN SỐ PHẬN"** (3.0 s)

### TK2 — "Người đồng nghiệp mẫu mực và hiệu ứng hào quang chiếc áo blouse"

*Thời lượng: 77.9 s (11 câu) · BGM: `bgm_jazz_noir.mp3` (Hồi 1 — bed tập: bgm_jazz_noir.mp3)*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK2.01#1` | H | neutral | -0.02 | 0.5 | `t4_nurse_station` | still | Người y tá hiền lành nhất bệnh viện. Lại là kẻ sát nhân tàn khốc nhất. | `hook — không phải dữ kiện kịch bản` |
| `TK2.01#2` | H | neutral | -0.02 | 0.5 | `t4_somerset_exterior` | pan | Mùa thu năm 2003. | `1.03#1` |
| `TK2.01#3` | H | neutral | -0.02 | 0.6 | `t4_somerset_exterior` | pull | Tại Trung tâm Y tế Somerset thuộc thị trấn Somerville, bang New Jersey, nước Mỹ. | `1.03#2` |
| `TK2.01#4` | H | neutral | -0.02 | 0.6 | `t4_icu_night` | still | Người đàn ông 43 tuổi ấy có dáng người gầy gò, giọng nói nhỏ nhẹ, luôn xuất hiện với nụ cười hiền lành và sẵn sàng nhận làm thay ca trực cho bất kỳ đồng nghiệp nào đang kiệt sức. | `1.03#4` |
| `TK2.01#5` | H | neutral | -0.02 | 0.6 | `t4_cullen_silhouette` | push | Thế nhưng, chính chiếc áo blouse trắng tinh tươm ấy đã tạo nên một “Hiệu ứng Hào quang” hoàn hảo, che giấu một vực thẳm tâm lý đen tối suốt 16 năm ròng rã. | `1.03#6` |
| `TK2.01#6` | H | neutral | -0.02 | 0.6 | `t4_code_blue_aftermath` | pan | Hắn luôn là người đầu tiên chạy đến phụ giúp khi có bệnh nhân trở nặng, và lặng lẽ ở lại dọn dẹp phòng bệnh sau những ca cấp cứu thất bại. | `1.05#2` |
| `TK2.01#7` | N1 | neutral | -0.02 | 0.6 | `t4_breakroom_night` | still | Trong mắt tất cả y tá chúng tôi tại bệnh viện Somerset, Charlie là một người bạn tuyệt vời. | `1.07#1` |
| `TK2.01#8` | N1 | neutral | -0.02 | 0.6 | `t4_breakroom_night` | push | Anh ấy chu đáo, không bao giờ cáu gắt và luôn chăm sóc người bệnh vô cùng ân cần. | `1.07#2` |
| `TK2.01#9` | N1 | sad | -0.04 | 0.7 | `t4_corridor_shadow` | pull | Cho đến khi sự thật vỡ lở, tất cả chúng tôi đều lạnh sống lưng vì nhận ra mình đã cùng làm việc bên cạnh một kẻ sát nhân hàng loạt nguy hiểm nhất. | `1.07#5` |
| `TK2.01#10` | C | neutral | -0.02 | 0.7 | `t4_institutional_bystander` | still | Dưới góc độ tâm lý học hành vi, Charles Cullen biểu hiện một cơ chế “Vật hóa” và phi nhân hóa nạn nhân vô cùng điển hình. | `2.11#1` |
| `TK2.01#11` | H | neutral | -0.02 | 0.0 | `t4_closing_desk` | still | Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | `CTA — không phải dữ kiện kịch bản` |

**Lớp phủ chữ trên hình (Text Overlays):**
- `TK2.01#1`: **"TRUNG TÂM Y TẾ SOMERSET · MÙA THU 2003"** (3.0 s)
- `TK2.01#5`: **"CHIẾC ÁO BLOUSE TRẮNG: HIỆU ỨNG HÀO QUANG"** (2.5 s)
- `TK2.01#7`: **"“CHARLIE LÀ NGƯỜI BẠN TUYỆT VỜI NHẤT”"** (2.5 s)
- `TK2.01#9`: **"LẠNH SỐNG LƯNG: LÀM VIỆC CẠNH ÁC QUỶ"** (2.5 s)
- `TK2.01#10`: **"CƠ CHẾ PHI NHÂN HÓA VÀ VẬT HÓA NẠN NHÂN"** (3.0 s)

### TK3 — "Nữ y tá mang máy nghe lén đối đầu bạn thân"

*Thời lượng: 82.3 s (10 câu) · BGM: `bgm_sub_drone.mp3` (Hồi 4 — bed tập: bgm_sub_drone.mp3)*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK3.01#1` | H | neutral | -0.02 | 0.5 | `t4_diner_exterior` | still | Chiếc micro dưới áo khoác mùa đông. Và cuộc hẹn sinh tử tại quán ăn. | `hook — không phải dữ kiện kịch bản` |
| `TK3.01#2` | H | neutral | -0.02 | 0.6 | `t4_diner_exterior` | pull | Và họ đã tìm đến Amy Loughren – nữ y tá ca đêm tài năng, người đồng thời là bạn thân nhất của Charles Cullen. | `4.02#7` |
| `TK3.01#3` | D | neutral | -0.03 | 0.6 | `t4_diner_booth` | pan | Khi chúng tôi bí mật tiếp cận Amy Loughren tại một quán ăn nhỏ ngoài giờ trực và trải ra trước mặt cô ấy bản in nhật ký máy Pyxis, Amy đã chết lặng. | `4.04#1` |
| `TK3.01#4` | D | neutral | -0.03 | 0.6 | `t4_amy_scrubs` | still | Điều khiến tình thế trở nên sinh tử là lúc bấy giờ, Amy đang một mình nuôi hai con nhỏ và mang trong mình căn bệnh cơ tim nguy hiểm có thể đe dọa tính mạng bất cứ lúc nào. | `4.04#6` |
| `TK3.01#5` | N2 | fearful | -0.04 | 0.7 | `t4_amy_scrubs` | push | Dù vô cùng sợ hãi cho mạng sống của bản thân và tương lai của các con, tôi biết mình không có quyền im lặng để tội ác tiếp tục diễn ra. | `4.06#6` |
| `TK3.01#6` | H | neutral | -0.02 | 0.6 | `t4_wire_closeup` | push | Amy Loughren bước vào quán ăn với chiếc micro bí mật được các điều tra viên gắn khéo léo dưới lớp áo khoác mùa đông. | `4.08#3` |
| `TK3.01#7` | H | neutral | -0.02 | 0.7 | `t4_diner_booth` | still | Bằng sự khéo léo và thấu hiểu tâm lý, Amy nhẹ nhàng gợi mở về những bất thường tại bệnh viện và đề nghị giúp đỡ hắn tìm kiếm sự giải thoát. | `4.08#6` |
| `TK3.01#8` | H | sad | -0.03 | 0.7 | `t4_diner_booth` | pull | Hắn cúi gục đầu xuống bàn, giọng run rẩy thốt lên những lời thì thầm được máy ghi âm ghi lại nguyên văn: “Tôi muốn dừng lại, tôi muốn mọi chuyện kết thúc.” | `4.08#8` |
| `TK3.01#9` | D | neutral | -0.03 | 0.7 | `t4_interrogation_room` | still | Hắn thừa nhận đã dùng Digoxin và Insulin sát hại linh mục Florian Gall, bệnh nhân Michael Strenko và hàng chục nạn nhân khác qua nhiều năm. | `4.12#5` |
| `TK3.01#10` | H | neutral | -0.02 | 0.0 | `t4_closing_desk` | still | Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | `CTA — không phải dữ kiện kịch bản` |

**Lớp phủ chữ trên hình (Text Overlays):**
- `TK3.01#1`: **"CHIẾC MICRO DƯỚI ÁO KHOÁC MÙA ĐÔNG"** (3.0 s)
- `TK3.01#4`: **"MẸ ĐƠN THÂN VÀ CĂN BỆNH CƠ TIM NGUY HIỂM"** (2.5 s)
- `TK3.01#5`: **"“TÔI KHÔNG CÓ QUYỀN IM LẶNG TRƯỚC TỘI ÁC”"** (2.5 s)
- `TK3.01#8`: **"“TÔI MUỐN DỪNG LẠI, MUỐN MỌI CHUYỆN KẾT THÚC”"** (2.5 s)
- `TK3.01#9`: **"LỜI THỪA NHẬN SÁT HẠI HÀNG CHỤC NẠN NHÂN"** (3.0 s)

### TK4 — "Mười sáu năm im lặng của chín bệnh viện"

*Thời lượng: 71.7 s (9 câu) · BGM: `bgm_ambient_deep.mp3` (Hồi 1/5 — bed tập: bgm_ambient_deep.mp3)*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK4.01#1` | H | neutral | -0.02 | 0.5 | `t4_ten_hospitals_map` | still | Chín bệnh viện biết hắn có vấn đề. Nhưng tất cả đều chọn im lặng. | `hook — không phải dữ kiện kịch bản` |
| `TK4.01#2` | D | neutral | -0.03 | 0.6 | `t4_somerset_exterior` | pan | Trung tâm Y tế Somerset hoàn toàn không phải là hiện trường đầu tiên. | `1.14#2` |
| `TK4.01#3` | D | neutral | -0.03 | 0.6 | `t4_ten_hospitals_map` | pull | Trong suốt 16 năm, từ năm 1988 đến năm 2003, Charles Cullen đã làm việc qua 9 bệnh viện và 1 viện dưỡng lão khác nhau trên khắp hai bang New Jersey và Pennsylvania. | `1.14#3` |
| `TK4.01#4` | D | neutral | -0.03 | 0.6 | `t4_ten_hospitals_map` | push | Ở bất cứ nơi nào hắn đặt chân đến, tỷ lệ bệnh nhân tử vong vì ngưng tim đột ngột vào ca trực đêm đều tăng vọt theo một đồ thị bất thường. | `1.14#4` |
| `TK4.01#5` | D | neutral | -0.03 | 0.7 | `t4_neutral_letter` | still | Hắn bị nghi ngờ ở nơi này, liền bị buộc thôi việc trong im lặng, rồi lại dễ dàng cầm thư giới thiệu chuyển sang một bệnh viện khác để tiếp tục hành vi săn mồi. | `1.14#5` |
| `TK4.01#6` | D | neutral | -0.03 | 0.7 | `t4_case_file_open` | push | Tuy nhiên, dựa trên hồ sơ theo dõi dịch tễ và lượng thuốc mất tích bí ẩn, các chuyên gia điều tra nhận định con số thực tế có thể lên tới 400 nạn nhân. | `1.14#7` |
| `TK4.01#7` | C | neutral | -0.02 | 0.7 | `t4_institutional_bystander` | still | Sự im lặng có hệ thống của các nhà quản lý đã biến chính những cơ sở chữa bệnh thành nơi đồng lõa cho cái ác tiếp diễn suốt 16 năm. | `5.05#6` |
| `TK4.01#8` | D | neutral | -0.03 | 0.7 | `t4_courtroom_bench` | still | Năm 2004, Thống đốc bang New Jersey đã ký ban hành “Đạo luật Cullen” nhằm bẻ gãy vĩnh viễn sự im lặng thể chế nguy hiểm này. | `5.06#2` |
| `TK4.01#9` | H | neutral | -0.02 | 0.0 | `t4_closing_desk` | still | Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | `CTA — không phải dữ kiện kịch bản` |

**Lớp phủ chữ trên hình (Text Overlays):**
- `TK4.01#1`: **"16 NĂM · 9 BỆNH VIỆN VÀ 1 VIỆN DƯỠNG LÃO"** (3.0 s)
- `TK4.01#5`: **"BUỘC THÔI VIỆC TRONG IM LẶNG: BẢO VỆ DANH TIẾNG"** (2.5 s)
- `TK4.01#6`: **"ƯỚC TÍNH THỰC TẾ CÓ THỂ LÊN TỚI 400 NẠN NHÂN"** (2.5 s)
- `TK4.01#7`: **"SỰ IM LẶNG ĐỒNG LÕA CỦA CÁC NHÀ QUẢN LÝ"** (2.5 s)
- `TK4.01#8`: **"ĐẠO LUẬT CULLEN 2004: CHẤM DỨT SỰ IM LẶNG"** (3.0 s)

### TK5 — "Bài học sinh tồn từ lòng dũng cảm của Amy Loughren"

*Thời lượng: 75.7 s (9 câu) · BGM: `bgm_piano_warm.mp3` (Hồi 5 — bed tập: bgm_piano_warm.mp3)*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK5.01#1` | H | neutral | -0.02 | 0.5 | `t4_somerset_courtroom` | still | Bài học sinh tồn lớn nhất: Đừng bao giờ im lặng trước cái ác. | `hook — không phải dữ kiện kịch bản` |
| `TK5.01#2` | H | neutral | -0.02 | 0.6 | `t4_boardroom_empty` | pan | Đồng thời, chúng ta sẽ bóc trần sự thật cay đắng hơn cả tội ác của hắn: sự im lặng đồng lõa của chín bệnh viện vì nỗi sợ kiện tụng và trách nhiệm pháp lý. | `1.16#4` |
| `TK5.01#3` | H | neutral | -0.02 | 0.7 | `t4_somerset_exterior` | pull | Đó là bài học đắt giá về sự bất an tập thể và cái giá phải trả khi xã hội nhắm mắt trước những tín hiệu cảnh báo đỏ sinh tồn. | `1.16#5` |
| `TK5.01#4` | D | neutral | -0.03 | 0.6 | `t4_courtroom_bench` | still | Năm 2004, Thống đốc bang New Jersey đã ký ban hành “Đạo luật Cullen” nhằm bẻ gãy vĩnh viễn sự im lặng thể chế nguy hiểm này. | `5.06#2` |
| `TK5.01#5` | D | neutral | -0.03 | 0.6 | `t4_pyxis_station` | pan | Quy trình vận hành máy phát thuốc tự động Pyxis cũng được tái thiết kế trên toàn quốc, xóa bỏ hoàn toàn lỗ hổng hủy lệnh và siết chặt theo dõi từng liều độc dược. | `5.06#5` |
| `TK5.01#6` | H | neutral | -0.02 | 0.7 | `t4_nurse_station` | still | Bài học sinh tồn lớn nhất mà vụ án này để lại chính là: “Hãy luôn biết lắng nghe và tin tưởng vào trực giác của chính mình.” | `5.08#4` |
| `TK5.01#7` | H | neutral | -0.02 | 0.7 | `t4_amy_scrubs` | push | Lòng dũng cảm của nữ y tá Amy Loughren đã chứng minh rằng: Một cá nhân dám bước qua nỗi sợ hãi để lên tiếng có thể cứu sống hàng trăm sinh mệnh khác. | `5.08#6` |
| `TK5.01#8` | H | neutral | -0.02 | 0.8 | `t4_closing_desk` | pull | Sự im lặng trước cái ác không bao giờ mang lại sự bình yên, mà chỉ tiếp tay cho vực thẳm nuốt chửng những người vô tội. | `5.08#7` |
| `TK5.01#9` | H | neutral | -0.02 | 0.0 | `t4_closing_desk` | still | Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | `CTA — không phải dữ kiện kịch bản` |

**Lớp phủ chữ trên hình (Text Overlays):**
- `TK5.01#1`: **"BÀI HỌC SINH TỒN VÀ TRÁCH NHIỆM XÃ HỘI"** (3.0 s)
- `TK5.01#3`: **"CẢNH BÁO ĐỎ SINH TỒN: SỰ BẤT AN TẬP THỂ"** (2.5 s)
- `TK5.01#5`: **"TÁI THIẾT KẾ QUY TRÌNH QUẢN LÝ DƯỢC TOÀN QUỐC"** (2.5 s)
- `TK5.01#7`: **"LÒNG DŨNG CẢM CỦA NỮ Y TÁ AMY LOUGHREN"** (2.5 s)
- `TK5.01#8`: **"LẮNG NGHE VÀ TIN TƯỞNG VÀO TRỰC GIÁC"** (3.0 s)

