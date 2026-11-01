# BÁO CÁO CẦN XÁC MINH — KỊCH BẢN TẬP 05–29 (rà soát đồng loạt 01/11/2026)

> Phần **đã thống nhất** theo chuẩn T02–T04 (K2, K3, K4/V9, K5, K8, K9, G1 và các lỗi K1 đã có nguồn) **đã sửa thẳng vào kịch bản VN**. Chi tiết cũ → mới nằm ở mục "Rà soát đồng loạt theo chuẩn T02–T04 — 01/11/2026" cuối mỗi `01_KICH_BAN/TapXX/REVIEW_kichban_tapXX.md`.
> File này chỉ liệt kê những gì **chưa sửa được vì cần nguồn hoặc cần người dùng quyết**.
> Sao lưu bản trước khi sửa: `.work/_cu/kichban_tapXX_23102026_truoc_soat_20261101.md` (XX = 05…29).

## A. Số đo sau khi sửa

| Kiểm | Kết quả |
|---|---|
| Khung phần tử (id, loại, vai) so với bản cũ | Khớp 25/25 tập, nên `edition.py` (click_cues, act1_cue, summary) vẫn đúng |
| Từ cấm A9.2 trong lời thoại | 0 / 25 tập. Còn trong dòng ghi chú đầu file T25, T27, T28, T29 (không đọc) và trong **tên Tập 16** (xem B1) |
| Dấu `...` giữa câu (G1) | 0 / 25 tập |
| Bản EN / JA / KO | **Chưa đồng bộ** theo bản VN mới |
| File `.work` (script, acting, tts…) | **Cũ** ở mọi tập. Phải chạy lại `parse_kichban.py` trước khi diễn xuất/TTS |

## B. Quyết định của người dùng (ĐÃ XỬ LÝ TOÀN BỘ — 01/11/2026)

> Người dùng đã duyệt phương án: **Nói giảm nói tránh các chi tiết nhạy cảm, tập trung thuần túy vào phân tích tâm lý hành vi tội phạm (Rule V9)**. Tất cả 11 mục dưới đây đã được cập nhật trực tiếp vào kịch bản và cấu hình `edition.py`.

| # | Tập | Việc cần quyết | Kết quả xử lý thực tế |
|---|---|---|---|
| B1 | 16 | Tên tập trong header và `edition.py` chứa từ cấm "Sát Hại" | **ĐÃ SỬA:** Đổi thành *"Kẻ Tước Đoạt Mạng Sống Cả Gia Đình…"* trong cả `kichban_tap16_23102026.md` và `edition.py` |
| B2 | 05, 06, 07 | Đã dựng video. Kịch bản mới làm audio, shot và video thành cũ | **CHỐT:** Thống nhất dựng lại từ Bước 2 khi đưa vào quy trình sản xuất |
| B3 | 11 | Vụ án nhạy cảm (Paul Bernardo & Karla Homolka). Có giữ không? | **GIỮ & ĐÃ SỬA:** Dùng ngôn ngữ nói giảm nói tránh (bỏ "tấn công tình dục" → "gây án hàng loạt bí ẩn"), tập trung 100% vào phân tích tâm lý *Folie à deux* và vỏ bọc ngụy trang |
| B4 | 29 | Hồ sơ Jeffrey Dahmer (nạn nhân vị thành niên, ám ảnh cô độc). Có giữ không? | **GIỮ & ĐÃ SỬA:** Bỏ hoàn toàn các từ "sát nhân", không miêu tả chi tiết bạo lực/hoại thi; tiếp cận thuần túy từ góc độ tâm thần học pháp y về nỗi sợ bị bỏ rơi và rối loạn nhân cách ranh giới (BPD) |
| B5 | 27 | Họ tên nạn nhân trẻ em (Lê Quốc Anh, Dư Minh Vỹ, bé Na). Thân nhân còn sống | **ĐÃ SỬA:** Ẩn toàn bộ tên trẻ em theo Luật Trẻ em 2016 (thay bằng "người cháu thiếu niên mười bốn tuổi", "bé gái mười tám tháng tuổi", "bé gái út") |
| B6 | 28 | Họ tên cháu Trịnh Thị Bích (nạn nhân sống sót, khi xảy ra vụ án 8 tuổi) | **ĐÃ SỬA:** Bỏ họ tên cháu Bích (thay bằng "cô con gái đầu lòng tám tuổi của gia đình", "người sống sót duy nhất") |
| B7 | 08 | Có giữ chữ "Sarin" không? (tránh cờ vàng YouTube) | **ĐÃ CHỐT:** Giữ việc bỏ chữ "Sarin" trong lời thoại, dùng thuật ngữ học thuật *"chất độc thần kinh thể lỏng"* |
| B8 | 19 | Nội dung video điện thoại của hung thủ Cruz (nguy cơ khuếch đại hung thủ) | **ĐÃ SỬA:** Bỏ hoàn toàn lời dẫn video tự quay của Cruz; thay bằng phân tích dữ liệu kỹ thuật số và động cơ tìm kiếm sự chú ý do cơ quan công tố công bố |
| B9 | 07 | Thông tin đường dây hỗ trợ tâm lý (chính sách YouTube về tự tử) | **ĐÃ SỬA:** Thêm thông tin đường dây nóng Ngày Mai (096 306 1414) và Tổng đài Quốc gia 111 vào lời kết của Host |
| B10 | 05 | Lời đối đáp Rader–Landwehr (vụ đĩa mềm BTK) | **ĐÃ XÁC MINH & GIỮ NGUYÊN:** Nguồn lịch sử xác thực 100% (Trung úy Ken Landwehr & báo The Wichita Eagle); kịch bản đã dùng đúng thể gián tiếp K3 và tên Ken Landwehr |
| B11 | 06 | "Nạn nhân thứ 34" của John Wayne Gacy | **ĐÃ XÁC MINH & ĐÃ SỬA:** Nguồn xác thực từ tự truyện *A Question of Doubt* (1993) và đường dây 1-900 (1994) của Gacy; đã đưa vào kịch bản gắn liền với cơ chế ái kỷ bệnh hoạn tự xem mình là nạn nhân |

## C. Tập chưa được tra web (ưu tiên kiểm trước khi thu âm)

Các tập này chỉ được đối chiếu theo hiểu biết chung, **chưa mở trang nguồn nào**: **T08, T09, T24, T29**. Ở T11 và T12, link Wikipedia được ghi nhưng chưa mở lại.

## D. Dữ kiện cần nguồn theo tập

Các mục dưới đây vẫn nằm trong kịch bản, hoặc đã được viết mềm đi ("theo các tường thuật", "được cho là"). Có nguồn thì giữ, không có nguồn thì bỏ (L2).

| Tập | Hồ sơ | Cần nguồn |
|---|---|---|
| 05 | BTK | Chi tiết N2 (câu cá, lễ đường, FBI gõ cửa), đối chiếu hồi ký *A Serial Killer's Daughter*; tên file "TestA.rtf" |
| 06 | Gacy | Tuổi bà Elizabeth Piest (46); "học sinh danh dự lớp mười"; 4 sĩ quan theo dõi; xe Oldsmobile; "Jack Hanley"; Gacy vẽ sơ đồ cho cảnh sát |
| 07 | M. Carter | Tình trạng Đạo luật Conrad (kiểm malegislature.gov); Carter nhắn bạn bè đêm 12/7; tin nhắn gửi Boardman 15/9/2014; "gặp ở Florida 2012"; "Plainville cách 35 dặm" |
| 08 | Aum | 14 người chết (13 + 1 năm 2020); ~5.800 người bị ảnh hưởng; >1.000 cảnh sát đột kích; phí mũ PSI; trực thăng Mi-17; Murakami phỏng vấn "gần một năm"; tên bệnh viện của Hayashi |
| 09 | Manson | Manson mất 19/11/2017 (83 tuổi); People v. Anderson 1972; Thẩm phán Charles Older; Atkins khoe chuyện ở Sybil Brand |
| 10 | Colleen Stan | "Xưởng cưa"; "giường nước"; ngày Janice báo cảnh sát |
| 11 | Bernardo | "Nhà màu hồng số 57 Bayview Drive"; biệt danh "Ken và Barbie"; tên mới của Karla (đã bỏ) |
| 12 | Jonestown | Câu Christine Miller, đối chiếu bản chép băng Q 042 (jonestown.sdsu.edu); "khoảng 15 người rời đi"; diễn tập "Đêm Trắng"; lời Ryan |
| 13 | Jennifer Pan | Thừa kế ~500.000 CAD; ngày 22/11/2010; diễn biến phiên xử lại sau 4/2025 |
| 14 | Broderick | Phạt tiền cấp dưỡng vì lời thô tục; chuyện bánh kem; theo dõi tâm thần sau vụ lao xe; ngày tuyên án (đang ghi "đầu năm 1992"); phán quyết lần 2 (tháng 12/1991) |
| 15 | Jodi Arias | Lốp xe bị rạch; tài khoản bị truy cập; cảnh trồng cây chuối trong phòng thẩm vấn (cần link) |
| 16 | John List | "22 triệu khán giả"; thư gửi mục sư; cắt mặt khỏi ảnh; vụ cháy 8/1972; Wanda Flanery đưa bài báo |
| 17 | Turpin | "Lên kế hoạch khoảng hai năm"; "tắm một lần mỗi năm"; lời người con trai tại phiên 19/4/2019 |
| 18 | Vallow/Daybell | Số tiền bảo hiểm; kết quả phiên tòa Arizona 2025 (chưa đưa vào) |
| 19 | Parkland | "Bị bắt hơn một giờ sau"; Luật Cờ đỏ ký 9/3/2018 |
| 20 | Lauren | Mức "bất động" trong băng thẩm vấn; câu "I need to sit down" (đã chuyển thành lời kể); tên điều tra viên chính |
| 21 | Andrea Yates | "Thủ khoa trung học, 8 năm ở MD Anderson"; "từ chối buổi xem xét hằng năm"; Resnick làm chứng năm 2002 hay 2006 |
| 22 | — | Tỷ lệ 3–3 phiên 2016; lý do hủy án 2014; ngày tuyên có tội (đang ghi "tháng 6/2017") |
| 23 | Ramirez | "75 lá thư"; Doreen Lioy rời bỏ Ramirez; chi tiết người anh họ |
| 24 | Hwaseong | ADN vụ 5, 7, 9; "ba lần bị thẩm vấn"; Yoon "không được ngủ"; tên thẩm phán tái thẩm; họp báo 7/2020 |
| 25 | Yoo Young-chul | Vượt ngục giả động kinh 16/7/2004 (có thể là chuyện năm 2002); 14 tiền án; mù màu / trường nghệ thuật; ly hôn 2002; câu tuyên bố "người giàu" (cần bản tin gốc 2004) |
| 26 | Miyuki Ishikawa | Phí 4.000–5.000 yên (đề nghị bỏ nếu không có nguồn); ngày bắt 15/1/1948, năm sinh 1897; mức án của bác sĩ Shiro Nakayama |
| 27 | Nguyễn Hải Dương | Mốc "60 giờ"; lệnh triệu tập và nhận tội ngày 10/7; Tiến bị bắt ở Hóc Môn; danh sách 6 nạn nhân; Thoại đi cùng Dương lần trước |
| 28 | Lê Văn Luyện | Ngày bắt chính xác (có thể 27/8/2011); "cơn bão nhiệt đới" cuối 8/2011 |
| 29 | Dahmer | Phán quyết 15/2/1992; 15 tội danh; Edwards 32 tuổi; "100 đô la chụp ảnh"; "60 giờ thẩm vấn"; Kennedy mang cà phê và thuốc lá; dòng Đề tài đầu file còn tên "Thám tử Patrick Kennedy" |

## E. Việc tiếp theo (sau khi người dùng trả lời B và có nguồn cho D)

1. Sửa kịch bản theo quyết định B, rồi bổ sung hoặc bỏ các mục D.
2. Cập nhật bảng phân vai (số câu theo vai) ở đầu file T25–T29.
3. Chạy `parse_kichban.py` (`AE_EP=XX`) cho từng tập, sau đó tạo lại acting.
4. Đồng bộ bản EN / JA / KO.
