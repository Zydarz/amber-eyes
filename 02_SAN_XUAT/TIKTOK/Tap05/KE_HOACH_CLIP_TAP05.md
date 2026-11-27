# KẾ HOẠCH CLIP TIKTOK — TẬP 05 · "CHIẾC ĐĨA MỀM MÀU TÍM & CƠN NGHIỆN ÁI KỶ"

*Ngày cập nhật: 27/11/2026 · Trạng thái: **kịch bản viết lại (bản 2 — súc tích, kịch tính, liền mạch), chờ duyệt trước khi đọc giọng** (L4)*
*Bản sao lưu cũ: `.work/_cu/KE_HOACH_CLIP_TAP05_cu_20261127.md`*
*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap05/SPEC_AUDIO_CLIP_TAP05.json`*
*Nguồn dữ liệu chuẩn: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap05/KeHoach_Video_Tap05.md` · `01_KICH_BAN/Ho_So_Toi_Pham/Tap05/kichban_tap05.md`*

---

## 0. Tóm tắt chốt

| Hạng mục | Giá trị |
|---|---|
| Số clip | **5 clip** (Part 1–5: mỗi clip 1 câu chuyện trọn vẹn, liên kết thành series) |
| Tổng câu thoại | **50 câu** đọc giọng (10 câu/clip — nhịp nhanh, súc tích) |
| Thời lượng mục tiêu | ~50–65 s/clip (chuẩn TikTok giữ chân người xem) |
| Hệ sinh thái K10 | Đủ 10 chỉ dấu tâm lý & hành vi cốt lõi của Tập 05 |
| Ngôn ngữ | Tiếng Việt · Cast: Host (H), Điều tra viên (D), Chuyên gia (C), Kerri Rawson (N2) |
| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** |
| Hình ảnh nền | Tái sử dụng **34 nền dọc 9:16** `assets/bg/tk05_*.png` đã có (Q5: video không chèn chữ burn-in) |

---

## 1. Cấu trúc 5 clip — Mạch kể chuyện liền mạch (Series 5 phần)

| Clip | Chỉ dấu | Góc tiếp cận sáng tạo | Hook (0–3 s) | Số câu |
|---|---|---|---|---|
| **TK1** | #4 · #8 | **Ván cờ đĩa mềm**: Hỏi thẳng cảnh sát có bị truy vết không và cái bẫy trên mặt báo | *"Một tên sát nhân gửi thư hỏi thẳng cảnh sát: dùng đĩa mềm có bị bắt không?"* | 10 |
| **TK2** | #6 · #5 | **Nghịch lý 13 năm im lặng**: Thoát tội hoàn hảo, lại tự chui đầu ra chỉ vì một bài báo | *"Thoát tội suốt ba mươi năm, tại sao kẻ sát nhân lại tự viết thư khiêu khích cảnh sát?"* | 10 |
| **TK3** | #9 · #3 | **Người hàng xóm hoàn hảo**: Dạy hướng đạo sinh, giữ chìa khóa nhà thờ, đo từng bãi cỏ | *"Người đàn ông này dạy con bạn sinh tồn, giữ chìa khóa nhà thờ, và đo từng ngọn cỏ."* | 10 |
| **TK4** | #3 · #1 | **Cú sốc ngày cưới**: Người cha dắt tay vào lễ đường hóa ra là bóng ma BTK | *"Người cha dắt tay bạn vào lễ đường ngày cưới, hóa ra là kẻ sát nhân bị truy nã ba mươi năm."* | 10 |
| **TK5** | #4 · #10 | **Hình phạt đáng sợ hơn cái chết**: Kẻ nghiện được chú ý bị nhốt vào sự im lặng tuyệt đối | *"Với một kẻ nghiện được cả thế giới sợ hãi, hình phạt nào đáng sợ hơn cả cái chết?"* | 10 |

---

## 2. Diễn xuất từng clip (lời đọc + hình + âm)

### TK1 — "Ván cờ đĩa mềm" (Part 1)

*BGM: `bgm_ambient_tension.mp3` · Mạch: Câu hỏi ngây thơ khó tin → Cái bẫy trên báo → 2 dòng metadata → Cú sốc hỏi cung → Kéo về YouTube.*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK1.01#1` | H | neutral | -0.02 | 0.4 | `tk05_handwritten_note_floppy` | push | Một tên sát nhân gửi thư hỏi thẳng cảnh sát: dùng đĩa mềm có bị bắt không? | `hook` |
| `TK1.01#2` | D | neutral | -0.02 | 0.5 | `tk05_handwritten_note_floppy` | pan | Nghe như chuyện đùa, nhưng đó là câu hỏi thật của BTK sau ba mươi năm lẩn trốn. | `4.02#6` |
| `TK1.01#3` | D | neutral | -0.02 | 0.5 | `tk05_newspaper_classified_494` | still | Cảnh sát lập tức giăng bẫy trên mục rao vặt báo: “Rex, mọi chuyện sẽ ổn để gửi nó”. | `4.04#5` |
| `TK1.01#4` | H | neutral | -0.02 | 0.5 | `tk05_purple_floppy_disk` | pull | Tin lời kẻ thù, hắn gửi ngay một chiếc đĩa mềm Memorex màu tím. | `4.04#8` |
| `TK1.01#5` | H | neutral | -0.02 | 0.5 | `tk05_digital_forensics_lab` | pan | Hắn không ngờ mọi file Word đều lưu lại dấu vết ẩn bên trong. | `4.06#1` |
| `TK1.01#6` | H | neutral | -0.02 | 0.5 | `tk05_metadata_screen` | push | Chỉ vài phút kiểm tra, hai dòng chữ hiện lên: “Sửa đổi lần cuối bởi: Dennis”. | `4.06#6` |
| `TK1.01#7` | H | neutral | -0.02 | 0.5 | `tk05_church_website_search` | still | Và tổ chức đăng ký: “Nhà thờ Lutheran Chúa Kitô”. | `4.06#7` |
| `TK1.01#8` | D | neutral | -0.02 | 0.6 | `tk05_interrogation_confrontation` | push | Bị bắt, hắn ngơ ngác hỏi Trung úy Landwehr: “Tại sao các anh lại nói dối tôi?” | `4.12#2` |
| `TK1.01#9` | D | neutral | -0.03 | 0.7 | `tk05_interrogation_confrontation` | still | Trung úy đáp gọn: “Vì chúng tôi tìm cách bắt ông.” | `4.12#3` |
| `TK1.01#10` | H | neutral | -0.02 | 0.0 | `tk05_amber_eyes_dossier_05` | still | Nhưng hắn đã qua mặt FBI suốt 30 năm bằng cách nào? Xem bản đầy đủ ở link trong bio. | `CTA` |

---

### TK2 — "Nghịch lý 13 năm im lặng" (Part 2)

*BGM: `bgm_sub_drone.mp3` · Mạch: Tình huống giả định kéo người xem nhập vai → Bài báo 2004 → Cú đâm tự ái → Nhân tố X → Kéo về YouTube.*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK2.01#1` | H | neutral | -0.02 | 0.4 | `tk05_fear_of_oblivion` | push | Thoát tội suốt ba mươi năm, tại sao kẻ sát nhân lại tự viết thư khiêu khích cảnh sát? | `hook` |
| `TK2.01#2` | D | neutral | -0.02 | 0.5 | `tk05_detective_war_room` | pan | Đáng lẽ hắn chỉ cần im lặng là có thể sống yên ổn đến cuối đời. | `1.14#1` |
| `TK2.01#3` | D | neutral | -0.02 | 0.5 | `tk05_book_manuscript_desk` | still | Nhưng đầu năm 2004, báo chí đăng bài kỷ niệm, nhận định BTK có lẽ đã chết. | `1.14#3-4` |
| `TK2.01#4` | C | neutral | -0.02 | 0.5 | `tk05_narcissist_mirror_shadow` | push | Với một kẻ ái kỷ ác tính, bị lãng quên còn đau đớn hơn cả ngồi tù. | `1.14#5` |
| `TK2.01#5` | C | neutral | -0.02 | 0.5 | `tk05_narcissist_mirror_shadow` | still | Hắn phát điên vì thế giới sắp quên mất nỗi khiếp sợ do chính mình tạo ra. | `1.14#6` |
| `TK2.01#6` | D | neutral | -0.02 | 0.5 | `tk05_btk_signature_letter` | pull | Cơn nghiện được chú ý buộc hắn tự phá vỡ vỏ bọc, gửi thư báo mình vẫn còn sống. | `1.14#7` |
| `TK2.01#7` | C | neutral | -0.02 | 0.5 | `tk05_factor_x_shadow` | push | Trong tâm trí, hắn tự bịa ra một khái niệm mang tên “Nhân tố X” để đổ mọi tội lỗi. | `3.02#7` |
| `TK2.01#8` | C | neutral | -0.02 | 0.6 | `tk05_projection_mask` | still | Nhờ vậy, hắn vừa phạm tội ác, vừa tin mình là một công dân hoàn toàn vô can. | `3.04#3` |
| `TK2.01#9` | H | neutral | -0.02 | 0.6 | `tk05_two_faces_silhouette` | pull | Chính cơn nghiện được nhớ tên đã đẩy hắn thẳng vào cái bẫy của chính mình. | `3.04#3` |
| `TK2.01#10` | H | neutral | -0.02 | 0.0 | `tk05_amber_eyes_dossier_05` | still | Giải mã trọn vẹn tâm lý “Nhân tố X” trong Tập năm trên YouTube, link trong bio. | `CTA` |

---

### TK3 — "Người hàng xóm hoàn hảo ở Park City" (Part 3)

*BGM: `bgm_jazz_noir.mp3` · Mạch: Hook rợn người về người hàng xóm → 3 vai trò đáng kính → Hiệu ứng Hào quang → Bức tường tâm trí → Kéo về YouTube.*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK3.01#1` | H | neutral | -0.02 | 0.4 | `tk05_two_faces_silhouette` | push | Người đàn ông này dạy con bạn sinh tồn, giữ chìa khóa nhà thờ, và đo từng ngọn cỏ. | `hook` |
| `TK3.01#2` | D | neutral | -0.02 | 0.5 | `tk05_lutheran_church_exterior` | pan | Dennis Rader là Chủ tịch Hội đồng Nhà thờ Lutheran, được cả giáo đoàn tuyệt đối tin cậy. | `2.06#4` |
| `TK3.01#3` | D | neutral | -0.02 | 0.5 | `tk05_scout_camp_campfire` | still | Hắn là Đội trưởng Hướng đạo sinh, tận tình rèn luyện đạo đức cho trẻ nhỏ mỗi cuối tuần. | `2.06#5` |
| `TK3.01#4` | D | neutral | -0.02 | 0.5 | `tk05_compliance_truck_street` | push | Làm Nhân viên Trật tự Đô thị, hắn khắt khe đến mức đo từng bãi cỏ của hàng xóm. | `2.06#6` |
| `TK3.01#5` | D | neutral | -0.02 | 0.5 | `tk05_compliance_measuring_tape` | still | Nhưng mọi người chỉ cười xòa, nghĩ đó là tác phong kỷ luật của một cựu quân nhân. | `2.06#7` |
| `TK3.01#6` | C | neutral | -0.02 | 0.5 | `tk05_rader_house_park_city` | pull | Đó là “Hiệu ứng Hào quang”: khi ai đó khoác áo đạo đức, ta tự động mù quáng trước cái ác. | `2.06#8` |
| `TK3.01#7` | C | neutral | -0.02 | 0.5 | `tk05_concrete_wall_divide` | push | Trong đầu hắn có một bức tường bê tông ngăn đôi thế giới gia đình và thế giới săn mồi. | `3.02#3` |
| `TK3.01#8` | C | neutral | -0.02 | 0.6 | `tk05_family_dinner_warmth` | still | Vợ con và nhà thờ chính là tấm khiên hoàn hảo che mắt cả thị trấn suốt ba mươi năm. | `3.02#6` |
| `TK3.01#9` | H | neutral | -0.02 | 0.6 | `tk05_shattered_mask_confession` | pull | Không một ai hay biết, cho đến ngày chiếc mặt nạ vỡ vụn trước mắt người thân. | `4.14#1` |
| `TK3.01#10` | H | neutral | -0.02 | 0.0 | `tk05_amber_eyes_dossier_05` | still | Xem toàn bộ hồ sơ giải phẫu tâm lý Dennis Rader tại link trong bio. | `CTA` |

---

### TK4 — "Cú sốc ngày cưới của con gái BTK" (Part 4)

*BGM: `bgm_piano_warm.mp3` · Mạch: Hook đặt người xem vào vị trí nạn nhân tinh thần → Ký ức đẹp → FBI gõ cửa → Nỗi đau phản bội → Kéo về YouTube.*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK4.01#1` | H | neutral | -0.02 | 0.4 | `tk05_kerri_rawson_tears` | still | Người cha dắt tay bạn vào lễ đường ngày cưới, hóa ra là kẻ sát nhân bị truy nã ba mươi năm. | `hook` |
| `TK4.01#2` | H | sad | -0.03 | 0.5 | `tk05_rader_house_park_city` | pan | Đằng sau sự tự mãn của kẻ thủ ác là bi kịch giáng xuống đầu những người thân vô tội. | `4.14#1` |
| `TK4.01#3` | H | sad | -0.03 | 0.5 | `tk05_kerri_rawson_tears` | push | Hãy nghe lời tâm sự của Kerri Rawson, con gái ruột của Dennis Rader. | `4.14#3` |
| `TK4.01#4` | N2 | sad | -0.03 | 0.5 | `tk05_family_dinner_warmth` | still | Cả thế giới thấy ông ấy là quái vật, nhưng với tôi, ông từng là người cha mẫu mực nhất. | `4.15#1` |
| `TK4.01#5` | N2 | neutral | -0.02 | 0.5 | `tk05_family_dinner_warmth` | pan | Ông dạy tôi đi xe đạp, đưa tôi đi câu cá và tự hào dắt tay tôi bước vào lễ đường. | `4.15#2` |
| `TK4.01#6` | N2 | sad | -0.03 | 0.6 | `tk05_highway_takedown_arrest` | push | Khi FBI gõ cửa báo tin cha tôi là sát nhân BTK, mặt đất dưới chân tôi như sụp đổ. | `4.15#3` |
| `TK4.01#7` | N2 | sad | -0.03 | 0.6 | `tk05_shattered_mask_confession` | pull | Nỗi đau lớn nhất không phải sự sợ hãi, mà là cảm giác bị phản bội niềm tin tột cùng. | `4.15#4` |
| `TK4.01#8` | N2 | sad | -0.03 | 0.6 | `tk05_narcissistic_throne` | still | Làm sao tôi chấp nhận được người chúc tôi ngủ ngon mỗi đêm lại hủy hoại hàng chục gia đình? | `4.15#5` |
| `TK4.01#9` | N2 | sad | -0.03 | 0.7 | `tk05_darkened_house_exterior` | push | Đó là vết thương tâm hồn sẽ không bao giờ lành trong suốt phần đời còn lại của tôi. | `4.15#6` |
| `TK4.01#10` | H | neutral | -0.02 | 0.0 | `tk05_amber_eyes_dossier_05` | still | Câu chuyện đầy đủ phía sau cánh cửa nhà Rader có trong Tập năm, link ở bio. | `CTA` |

---

### TK5 — "Hình phạt đáng sợ hơn cả cái chết" (Part 5)

*BGM: `bgm_piano_warm.mp3` · Mạch: Câu đố tâm lý → 10 bản án chung thân → Thái độ trước tòa → Biệt giam im lặng ở El Dorado → Kéo về YouTube.*

| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |
|---|---|---|---|---|---|---|---|---|
| `TK5.01#1` | H | neutral | -0.02 | 0.4 | `tk05_solitary_confinement_cell` | push | Với một kẻ nghiện được cả thế giới sợ hãi, hình phạt nào đáng sợ hơn cả cái chết? | `hook` |
| `TK5.01#2` | D | neutral | -0.02 | 0.5 | `tk05_shattered_mask_confession` | pan | Ngày 18 tháng 8 năm 2005, tại tòa án thành phố Wichita. | `5.01#1` |
| `TK5.01#3` | D | neutral | -0.02 | 0.5 | `tk05_narcissistic_throne` | still | Dennis Rader nhận 10 bản án tù chung thân liên tiếp, tối thiểu 175 năm không ân xá. | `5.01#2` |
| `TK5.01#4` | C | neutral | -0.02 | 0.5 | `tk05_projection_mask` | push | Trước vành móng ngựa, hắn không hề ăn năn mà chỉ liên tục tự thương hại bản thân. | `5.01#4` |
| `TK5.01#5` | H | neutral | -0.02 | 0.5 | `tk05_solitary_confinement_cell` | pull | Hiện tại, ở tuổi ngoài tám mươi, hắn bị giam trong buồng biệt lập tại nhà tù El Dorado. | `5.02#1` |
| `TK5.01#6` | H | neutral | -0.02 | 0.5 | `tk05_darkened_house_exterior` | still | Không còn báo chí, không còn ánh đèn sân khấu, bị cách ly hoàn toàn với thế giới. | `5.02#2` |
| `TK5.01#7` | C | neutral | -0.02 | 0.5 | `tk05_fear_of_oblivion` | push | Với kẻ cả đời khát khao được chú ý, sự im lặng tuyệt đối chính là địa ngục tàn nhẫn nhất. | `5.02#3` |
| `TK5.01#8` | H | neutral | -0.02 | 0.6 | `tk05_closing_desk` | still | Hắn đánh lừa được hàng xóm, gia đình và cảnh sát suốt ba mươi năm. | `5.08#3` |
| `TK5.01#9` | H | neutral | -0.02 | 0.7 | `tk05_closing_desk` | pull | Nhưng lại không thể thắng nổi con quái vật ái kỷ bên trong chính mình. | `5.08#3` |
| `TK5.01#10` | H | neutral | -0.02 | 0.0 | `tk05_amber_eyes_dossier_05` | still | Xem trọn vẹn hồ sơ 30 năm truy lùng BTK trên kênh YouTube Amber Eyes, link trong bio. | `CTA` |

---

## 3. Mô tả & Hashtag đăng TikTok (Caption)

> Lưu ý: Bật toggle **"AI-generated content"** khi đăng theo quy định mục 2.2 của `KE_HOACH_TIKTOK.md`.

### TK1 — Ván cờ đĩa mềm
> Một tên sát nhân lẩn trốn 30 năm lại gửi thư hỏi thẳng cảnh sát: dùng đĩa mềm có bị truy vết không? Và cái kết không ai ngờ tới.
> Xem bản phân tích đầy đủ Tập 05 (Dennis Rader / BTK) trên YouTube **Amber Eyes** — link ở bio.
> *(Nội dung có sử dụng giọng đọc và hình ảnh minh họa AI)*
> `#AmberEyes #TamLyToiPham #HoSoToiPham #BTK #TrueCrimeVN`

### TK2 — Nghịch lý 13 năm im lặng
> Đáng lẽ chỉ cần im lặng là thoát tội suốt đời, tại sao kẻ sát nhân lại tự viết thư khiêu khích cảnh sát sau 13 năm biến mất? Giải mã cơn nghiện được nhớ tên và cơ chế "Nhân tố X".
> Xem trọn bộ Tập 05 trên YouTube **Amber Eyes** — link ở bio.
> *(Nội dung có sử dụng giọng đọc và hình ảnh minh họa AI)*
> `#AmberEyes #TamLyHoc #BTK #HoSoToiPham #TrueCrimeVN`

### TK3 — Người hàng xóm hoàn hảo ở Park City
> Ban ngày là Chủ tịch hội đồng nhà thờ, Đội trưởng Hướng đạo sinh, nhân viên trật tự đô thị mẫu mực. Tại sao cả thị trấn không một ai nghi ngờ suốt 30 năm?
> Xem giải phẫu tâm lý Dennis Rader bản đầy đủ trên YouTube **Amber Eyes** — link ở bio.
> *(Nội dung có sử dụng giọng đọc và hình ảnh minh họa AI)*
> `#AmberEyes #HieuUngHaoQuang #TamLyToiPham #BTK #TrueCrimeVN`

### TK4 — Cú sốc ngày cưới của con gái BTK
> Người cha từng dạy bạn đi xe đạp, dắt tay bạn vào lễ đường ngày cưới... hóa ra là kẻ sát nhân bị FBI truy nã suốt 3 thập kỷ. Lời tâm sự xé lòng của Kerri Rawson.
> Xem câu chuyện đầy đủ phía sau cánh cửa nhà Rader trên YouTube **Amber Eyes** — link ở bio.
> *(Nội dung có sử dụng giọng đọc và hình ảnh minh họa AI)*
> `#AmberEyes #KerriRawson #BTK #HoSoToiPham #TrueCrimeVN`

### TK5 — Hình phạt đáng sợ hơn cả cái chết
> 10 bản án chung thân liên tiếp, tối thiểu 175 năm không ân xá. Nhưng với kẻ nghiện được cả thế giới chú ý, sự im lặng tuyệt đối trong buồng biệt giam mới là địa ngục thực sự.
> Xem trọn vẹn hồ sơ 30 năm truy lùng BTK trên YouTube **Amber Eyes** — link ở bio.
> *(Nội dung có sử dụng giọng đọc và hình ảnh minh họa AI)*
> `#AmberEyes #DennisRader #BTK #TamLyToiPham #TrueCrimeVN`
