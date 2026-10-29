# HỒ SƠ SẢN XUẤT TẬP 01 · "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A) — các mã A0…A13 trong file này trỏ về đó.
**Kịch bản:** `01_KICH_BAN/Tap01/` · **Thành phẩm:** `02_SAN_XUAT/Tap01/xuat_ban/`
**Dùng làm mẫu:** tập mới sao chép file này thành `02_SAN_XUAT/TapXX/KeHoach_Video_TapXX.md` rồi thay nội dung.

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md` (bản giảm bạo lực của `kichban_tap01_22102026.md`, 23 chỗ sửa — Phụ lục B) |
| Lượt nói / câu / từ | 33 / **128** / 3.545 — Host 50% · Chuyên gia 24% · Điều tra viên 20% · Người dân 5% |
| N1 / N2 | `1.07` Hàng xóm (Cừu) / `4.03` Khán giả (Mèo) |
| Thời lượng đo | **1.133,5 s (18:53)** — intro 0–22,41 s |
| Mốc hồi | Hồi 1 · 00:20 · Hồi 2 · 03:28 · Hồi 3 · 06:51 · Hồi 4 · 10:54 · Hồi 5 · 15:43 |
| Bảng shot | 122 dòng = 104 shot có lời + 18 dòng không lời |
| Nền dùng | 45 ảnh `assets/bg/` (5 nền người dùng tạo + 2 cảnh bóng người dùng tạo + 41 nền connector + `void` tự vẽ) |

## B2. Kết quả và việc còn lại

| Hạng mục | Kết quả |
|---|---|
| TTS | 128/128, 5 giọng CER 0% |
| Âm thanh | 0 đoạn câm tuyệt đối; −16,2 LUFS; true peak −4,3 dBFS; lời đầu 23,0 s; 14 hiệu ứng (3 tiếng "Tách" + 11 file SFX) |
| Chữ | 128/128 câu phủ đúng; 0 số/trích sai; 0 từ bạo lực |
| File | `xuat_ban/Tap01_master.mp4` 419 MB; hình 1133,47 s = tiếng 1133,46 s; giải mã 0 lỗi |
| **Còn lại trước khi đăng** | ① Điền nguồn trong `nguon_tham_khao.md` · ② Kiểm tra điều khoản thương mại (57 dòng `provenance.json`), cho biết công cụ đã tạo 5 linh thú và 5 nền chủ đạo · ③ Người dùng nghe toàn tập |
| **Làm đơn giản hơn thiết kế** (có thể bổ sung) | Chưa có tư thế P2; chưa vẽ đường nhịp Dopamine, lưới biểu tượng bác sĩ, vòng hào quang, song sắt ghép từ lọ thuốc, bong bóng bình luận; 5 vòng màu cuối intro là hình tạm |

## B3. Ánh xạ riêng của Tập 01 (trong `parse_shots.py`)

| Biến | Giá trị |
|---|---|
| `COMBO` (cảnh ghép sẵn) | 1-04 `crowd_house` · 1-07 `deedee_room` · 1-17 `interrogation_gypsy` · 1-19 `bedroom_door_gypsy` · 2-02, 3-20 `wheelchair_gypsy` · 2-13…2-15 `pinboard` · 3-02, 3-10 `fog_deedee` · 3-11, 3-12 `spotlight_deedee` · 4-04 `wheelchair_spot` · 4-06 `glass_box_gypsy` · 4-10 `cage` · 4-19 `night_street_gypsy` · 4-21 `house_return` · 4-22 `night_screen` · 4-24 `crowd_away` · 4-30 `godejohn_screen` · 4-31 `two_shadows` · 5-16 `house_free` · 5-17 `cage_open` |
| `BG2` (đổi nền trong shot) | 4-10 `cage` → `cage_open` · 4-22 `night_screen` → `screen_off` |
| `INSET` | 2-14 ảnh `storm` ghim trên bảng |
| Prompt nền | `.work/bg_jobs.json`, `bg_jobs2.json`, `bg_jobs3.json` |

## 6. DANH SÁCH SHOT — TẬP 01 (bảng mẫu, viết theo A7)

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X (hiện badge chờ) · `✦` = lần đầu xuất hiện (thẻ giới thiệu) · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` (chỉ hình, shot I-01 → I-04, chi tiết ở A5.7) ở 0,00 s. Không câu thoại nào thuộc intro.

### HỒI 1 — KHOẢNH KHẮC ĐỨT GÃY NIỀM TIN · nền chủ đạo `house_night`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s, chồng lên phần đen cuối intro) | — | T1 | `house_police` hiện dần từ đen, `push` | *HỒI 01 · KHOẢNH KHẮC ĐỨT GÃY NIỀM TIN* | Đèn cảnh sát quét; drone dâng | ⊘ | |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `house_night` mờ | **14 · 06 · 2015** · *Springfield, Missouri* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T11 | `phone_dark` | *TRANG MẠNG XÃ HỘI CHUNG CỦA HAI MẸ CON* → **MỘT DÒNG TRẠNG THÁI KHIẾN CẢ KHU PHỐ CHẾT LẶNG** | Bài đăng hiện dạng các dòng mờ, không đọc được chữ, ở "đầy hằn học" | | |
| 1-03 | `1.04` (nghỉ 2 s) | — | — | giữ 1-02, ánh đỏ nhấp nháy | — | — | | |
| 1-04 | `1.05#1` | H | T1 | `house_police` + `crowd` | **NGÔI NHÀ NHỎ SƠN MÀU HỒNG PHẤN** · *Springfield, Missouri* (không hiện số nhà — nhà riêng, có thể đang có người ở) | — | | |
| 1-05 | `1.05#2` | H | T1 | `house_night`, `pull` | *LẮNG NGHE:* **MỘT NGƯỜI DÂN CÙNG KHU PHỐ** | — | →N1 | |
| 1-06 | `1.07#1` | N1 | T4 lời kể | `house_night` ấm, mờ | “Biểu tượng của tình mẫu tử thiêng liêng” | — | ✦ Cừu | |
| 1-07 | `1.07#2` | N1 | T8 | `wheelchair_room` + `deedee_wheelchair` | *NHỮNG GÌ CẢ KHU PHỐ TIN* · *Bại liệt từ thắt lưng trở xuống · Ung thư máu · Loạn dưỡng cơ · Động kinh nặng · Trí tuệ ngang trẻ lên bảy* | Mỗi mục tại cụm từ | | |
| 1-08 | `1.07#3` | N1 | T4 lời kể | `house_night` ấm | “Ai trong thị trấn này cũng rơi nước mắt cảm phục” | — | 🅑 | |
| 1-09 | `1.08#1` | H | T1 | `bedroom_door` | **NGƯỜI MẸ ĐÃ QUA ĐỜI** | — | | |
| 1-10 | `1.08#2` | H | T1 | `empty_room`, `still` | **GYPSY ROSE ĐÃ BIẾN MẤT** | — | ⊘ | ✂ |
| 1-11 | `1.08#3`–`#4` | H | T1 | `wheelchair_room` | **XE LĂN · BÌNH OXY · HÀNG CHỤC LỌ THUỐC** | `#3` sáng xe lăn, `#4` sáng kệ | | |
| 1-12 | `1.08#5` | H | T3 | `wheelchair_room` tối + dấu `?` lớn | *CẢ NƯỚC MỸ HỎI* · **AI ĐÃ GÂY RA CÁI CHẾT CỦA NGƯỜI MẸ?** | — | | |
| 1-13 | `1.08#6` | H | T1 | `interrogation`, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN THỤ LÝ HỒ SƠ** | — | →D | |
| 1-14 | `1.09`–`1.10` (nghỉ 2 s) | — | — | giữ 1-13, nhiễu bộ đàm `cold` | — | — | ⊘ | |
| 1-15 | `1.11#1` | D | T2 | `pinboard` | **LỆNH TRUY TÌM TOÀN QUỐC** | Dấu mộc ở "phát lệnh truy tìm" | ✦ Sói | |
| 1-16 | `1.11#2` | D | T7 | `route_night` | **48 GIỜ SAU** · *Bang Wisconsin — cách hàng trăm dặm* | Đường tự vẽ, số đếm | | |
| 1-17 | `1.11#3`–`#4` | D | T1 | `interrogation` + `gypsy_stand` | **CÔ TA TỰ BƯỚC ĐI** | Đèn treo sáng ở `#4` | | |
| 1-18 | `1.11#5`–`#7` | D | T8 gạch bỏ | giấy hồ sơ trên `records` | *Ung thư máu · Loạn dưỡng cơ · Tổn thương não* | Mỗi câu gạch một mục | | ✂ |
| 1-19 | `1.11#8` | D | T1 `hero` | `bedroom_door` + `gypsy_stand`, tối dần | **CÔ CON GÁI BÉ BỎNG CỦA BÀ** | Tiêu đề ở "không ai khác" | 🅑 P2 | |
| 1-20 | `1.13#1` | H | T1 | `podcast_desk`, cassette quay | **HỒ SƠ PHÂN TÍCH TÂM LÝ HỌC TỘI PHẠM** | "Tách" ở đầu | 🅑 | |
| 1-21 | `1.13#2` | H | T9 → T10 | `house_night` | **HỘI CHỨNG MÜNCHAUSEN QUA TRUNG GIAN** → *TẬP 01 · ĐỘC DƯỢC NHÂN DANH TÌNH MẸ* | Thuật ngữ ở "Hội chứng"; tên tập cuối câu | | |
| 1-22 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **23 NĂM TRONG NHÀ TÙ Y KHOA** | — | ⊘ | ◼ |

### HỒI 2 — HIỆN TRƯỜNG & HỒ SƠ BỆNH ÁN · nền chủ đạo `wheelchair_room`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#2` | H | T1 | `bedroom_door` | **KHÔNG PHẢI CĂN PHÒNG NGỦ** · *Tháng 6 năm 2015* | Tiêu đề ở `#2` | | |
| 2-02 | `2.02#3` | H | T5 | `wheelchair_room` + `gypsy_wheelchair` | *HIỆN TRƯỜNG THỰC SỰ* · **23 NĂM** | Số đếm | | |
| 2-03 | `2.04#1`–`#5` | H | T6 | `records`, `pan` | *1991 · Sinh ra khỏe mạnh* → *3 tháng tuổi · Ngưng thở khi ngủ* → *Danh sách bệnh án bắt đầu* → *7 tuổi · Tổn thương tủy sống · Xe lăn* → *Cạo trọc đầu · Hoá trị ung thư máu* | Mỗi câu một mốc | ⊘ | |
| 2-04 | `2.06#1` | H | T1 | `clinical` | **KHÔNG CHỈ LÀ LỜI NÓI DỐI** | — | 🅑 | |
| 2-05 | `2.06#2` | H | T2 | `records` | **HÀNG NGÀN TRANG BỆNH ÁN** · *Can thiệp y khoa trực tiếp lên cơ thể Gypsy* | — | | |
| 2-06 | `2.06#3` | H | T1 | `pinboard` mờ, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN CÔNG BỐ HỒ SƠ** | — | →D | |
| 2-07 | `2.07#1` | D | T2 | `pinboard` | **BA DẤU VẾT TRONG HỒ SƠ Y TẾ** | Bộ đếm `0/3` | | |
| 2-08 | `2.07#2` | D | T3 `1/3` | `wheelchair_room` cận kệ thuốc | **THUỐC CHỐNG ĐỘNG KINH LIỀU CAO** · *Dù cô không hề bị động kinh* | Phụ ở "dù cô không hề" | | |
| 2-09 | `2.07#3` | D | T3 `2/3` | `clinical` | **ỐNG NUÔI ĂN QUA DẠ DÀY** | — | | |
| 2-10 | `2.07#4` | D | T3 `3/3` | `clinical` tối | **PHẪU THUẬT KHÔNG CẦN THIẾT** · *Từ những triệu chứng giả trước mắt bác sĩ* | — | | |
| 2-11 | `2.07#5` | D | T5 | `clinical` + lưới ~100 biểu tượng bác sĩ (Pillow) | **HÀNG TRĂM BÁC SĨ** · *Không ai phát hiện ra?* | Biểu tượng hiện dần | | |
| 2-12 | `2.07#6` | D | T9 | `pinboard`, `pull` | **PHƯƠNG THỨC HÀNH ĐỘNG** *(Modus Operandi)* | 3 thẻ trống ghim lên | 🅑 | |
| 2-13 | `2.07#7` | D | T2 trên bảng ghim | camera dời tới thẻ 1 | *01* · **TỪNG LÀM HỘ LÝ** · *Nắm rõ thuật ngữ y khoa* | — | | |
| 2-14 | `2.07#8`–`#9` | D | T2 trên bảng ghim | thẻ 2 có ảnh `storm` thu nhỏ | *02 · 2005* · **BÃO KATRINA** → `#9`: *Mọi lịch sử y tế chỉ qua lời bà Dee Dee* | Dây đỏ nối ở `#9` | | |
| 2-15 | `2.07#10` | D | T2 trên bảng ghim | thẻ 3 + ghi chú Consolas | *03* · **AI NGHI NGỜ → ĐỔI BỆNH VIỆN, CHUYỂN NHÀ** · *BS. Bernardo Flasterstein · 2007* (chỉ chữ, V5) | Kéo ra thấy cả bảng | | |
| 2-16 | `2.09#1`–`#2` | H | T1 | `house_closed` | **CỬA SỔ LUÔN ĐÓNG KÍN** · *Không được đi học* | Tiếng khoá cửa ở đầu | | |
| 2-17 | `2.09#3` | H | T5 | `house_closed` mờ | **−4 TUỔI** · *Khai gian để mãi là trẻ vị thành niên* | — | | |
| 2-18 | `2.09#4` | H | T1 | `house_night` + bóng song sắt ghép từ lọ thuốc, ống truyền (Pillow) | **MỘT NHÀ TÙ KHÔNG CHẤN SONG** | Song sắt ở "được xây bằng" | | |
| 2-19 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **BÊN TRONG BỘ NÃO CỦA KẺ MẮC FDIA** | — | ⊘ | ◼ |

### HỒI 3 — GIẢI PHẪU TÂM LÝ · nền chủ đạo `brain_desk`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` | H | T5 | `void`, `still` | *CÂU HỎI LỚN NHẤT* · **TẠI SAO?** | Đúng ở "Tại sao" | ⊘ | ✂ |
| 3-02 | `3.02#2` | H | T1 | `fog` + `deedee_wheelchair` | **HƠN HAI THẬP KỶ** | — | | |
| 3-03 | `3.02#3`–`#4` | H | T3 | `charity` | **TRỤC LỢI TỪ THIỆN?** → `#4`: **TIỀN CHỈ LÀ PHẦN THƯỞNG PHỤ** | Đồng xu mờ ở `#4` | | |
| 3-04 | `3.02#5` | H | T9 | `brain_desk` | **HỘI CHỨNG MÜNCHAUSEN QUA TRUNG GIAN** *(Münchausen Syndrome by Proxy)* · *DSM-5-TR: Rối loạn giả bệnh áp đặt lên người khác — FDIA* | Dòng DSM ở "DSM-5-TR" | | |
| 3-05 | `3.03` (nghỉ) | — | — | giữ 3-04 | — | — | | |
| 3-06 | `3.04#1`–`#2` | H | T1 | `brain_desk`, `push` | *LẮNG NGHE:* **CHUYÊN GIA TÂM LÝ HỌC TỘI PHẠM** → *3 tầng tâm lý* | — | →C | |
| 3-07 | `3.05#1` | C | T9 | `brain_desk` + sơ đồ `brain3` | **3 TẦNG ĐỘNG CƠ** · *Vô thức và ý thức* | 3 vòng sáng lần lượt | ✦ Cáo | |
| 3-08 | `3.05#2` | C | T4 | `brain_desk` tối, tầng 1 sáng + `halo` | *TẦNG 01 · CƠN NGHIỆN HÀO QUANG* · “Vị thánh tử đạo” | — | | |
| 3-09 | `3.05#3`–`#4` | C | T3 so sánh | `brain_desk` mờ | **MALINGERING** *(Giả bệnh trục lợi) → tiền* · `#4`: **MÜNCHAUSEN** *→ sự chú ý, thương cảm, tôn sùng* | Cột phải ở `#4` | | |
| 3-10 | `3.05#5`–`#6` | C | T1 | `fog` + `deedee_wheelchair` mờ | *Gia đình xa lánh · Hôn nhân tan vỡ ở tuổi 24* → **MỘT CÁI BÓNG MỜ NHẠT** | Tiêu đề ở `#6` | | |
| 3-11 | `3.05#7` | C | T1 | `spotlight` + `deedee_wheelchair` | **TRUNG TÂM CỦA VŨ TRỤ** | Đèn bật ở "bỗng nhiên" | | ✂ |
| 3-12 | `3.05#8` | C | T1 | `spotlight` + biểu tượng bác sĩ, hàng xóm, tờ báo | **VỊ THÁNH SỐNG** | Mỗi biểu tượng ở cụm từ | | |
| 3-13 | `3.05#9` | C | T5 | `void` + đường nhịp tăng vọt | **DOPAMINE** · *Mỗi lần Gypsy nhập viện cấp cứu* | Nhịp nhấp nháy | 🅑 P2 | |
| 3-14 | `3.06` (nghỉ) | — | — | tối dần | — | — | | |
| 3-15 | `3.07#1` | H | T1 | `brain_desk` | **MỚI CHỈ LÀ BỀ NỔI** | — | | |
| 3-16 | `3.07#2` | H | T2 | `records` | *LỜI KHAI GIA ĐÌNH BÊN NGOẠI* · **BỊ NGHI GÂY HẠI CHO NGƯỜI THÂN** | — | →C | |
| 3-17 | `3.08#1` | C | T9 | `brain_desk`, tầng 2 sáng | *TẦNG 02* · **NỖI SỢ BỊ BỎ RƠI · NHU CẦU KIỂM SOÁT** | — | | |
| 3-18 | `3.08#2`–`#4` | C | T3 | `hands` | **MỘT VẬT SỞ HỮU DUY NHẤT** → `#3`: *Đi học → bạn bè → yêu đương → rời xa mẹ* → `#4`: **GIỮ MỘT CON NGƯỜI MÃI MÃI?** | 3 beat | | |
| 3-19 | `3.08#5` | C | T1 `hero` | `void`, tối dần | **HÃY KHIẾN CON BÉ TIN RẰNG MÌNH BỆNH TẬT** | Tiêu đề ở "Hãy khiến" | ⊘ | |
| 3-20 | `3.08#6` | C | T3 | `wheelchair_room` + `gypsy_wheelchair` | **NGƯỜI DUY NHẤT NẮM GIỮ CUỘC SỐNG CỦA CON GÁI** | — | | |
| 3-21 | `3.09` (nghỉ) | — | — | giữ 3-20 | — | — | | |
| 3-22 | `3.10#1` | C | T9 | `brain_desk`, tầng 3 sáng | *TẦNG 03* · **DẤU ẤN XOÁ BỎ NHÂN DẠNG** *(Signature)* | — | | |
| 3-23 | `3.10#2` | C | T3 | `dress_hanger` | **CẠO TRỌC ĐẦU · VÁY CÔNG CHÚA** · *Ngay cả khi cô đã hơn 20 tuổi* | — | | |
| 3-24 | `3.10#3`–`#4` | C | T9 | `dress_hanger` mờ | *Không chỉ là giả bệnh ung thư* → **TƯỚC ĐOẠT SỰ TRƯỞNG THÀNH** *(Infantilization)* | Thuật ngữ ở `#4` | 🅑 | |
| 3-25 | `3.10#5`–`#6` | C | T1 | `doll` | **CON BÚP BÊ SỨ 7 TUỔI** | Tiêu đề ở "búp bê sứ" | | |
| 3-26 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **TẠI SAO GYPSY KHÔNG ĐỨNG DẬY?** | — | ⊘ | ◼ |

### HỒI 4 — GÓC NHÌN NẠN NHÂN · nền chủ đạo `locked_door`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` | H | T1 | `night_screen` + bong bóng bình luận mờ (Pillow, không tên) | **CÂU HỎI ĐẦY HOÀI NGHI** · *Dành cho chính Gypsy Rose* | — | | |
| 4-02 | `4.02#2` | H | T1 | `night_screen`, `push` | *LẮNG NGHE:* **MỘT KHÁN GIẢ THEO DÕI VỤ ÁN** | — | →N2 | |
| 4-03 | `4.03#1` | N2 | T4 lời kể | `night_screen` | “Cô ấy biết rõ đôi chân mình không hề bị liệt.” | — | ✦ Mèo | |
| 4-04 | `4.03#2`–`#3` | N2 | T4 lời kể | `wheelchair_room` tối, xe lăn trống dưới đèn rọi | “Mỗi tối… cô ấy vẫn tự đứng dậy đi lại bình thường.” → “Vậy tại sao… Gypsy không một lần đứng phắt dậy khỏi chiếc xe lăn để tố cáo mẹ mình?” | Mỗi câu một dòng | 🅑 ở `#3` | |
| 4-05 | `4.04` (nghỉ) | — | — | tối dần | — | — | | |
| 4-06 | `4.05#1` | H | T1 | `glass_box` + `gypsy_wheelchair` nhỏ | **LỚN LÊN TRONG LỒNG KÍNH** | — | | |
| 4-07 | `4.05#2` | H | T3 | `locked_door` · 2 thẻ thuật ngữ | **BẤT LỰC TẬP NHIỄM** *(Learned Helplessness)* · **GẮN KẾT CHẤN THƯƠNG** *(Trauma Bonding)* | Mỗi thẻ ở cụm từ | →C | |
| 4-08 | `4.07#1` | C | T9 | `cage` đóng | **SỰ BẤT LỰC TẬP NHIỄM** · *Martin Seligman · 1967* | Tiếng xích ở đầu | | |
| 4-09 | `4.07#2` | C | T4 `hero` | `cage` đóng, tối dần | “Mọi sự vùng vẫy đều vô nghĩa” | Câu trích ở cụm từ | | |
| 4-10 | `4.07#3` | C | T1 | `cage` đóng → mở (hoà tan 2 nền cùng seed) | **CỬA LỒNG ĐÃ MỞ TOANG** · *…nhưng không bao giờ bước ra nữa* | Cửa mở ở "cánh cửa lồng" | | |
| 4-11 | `4.07#4` | C | T1 | `locked_door` | **THẾ GIỚI QUAN CỦA GYPSY** | — | 🅑 P2 | |
| 4-12 | `4.07#5`–`#6` | C | T3 | `hands` | **BÀ LUÔN NẮM CHẶT TAY GYPSY** · `#6`: *Với người ngoài: cử chỉ âu yếm* | — | | |
| 4-13 | `4.07#7` | C | T3 | `hands`, ánh `cold` | *Với Gypsy: một mật lệnh đe dọa* · **MỘT LỜI CẢNH CÁO KHÔNG THÀNH TIẾNG** | Hai bàn tay khép chặt hơn ở "siết chặt" | | |
| 4-14 | `4.07#8` | C | T2 | `locked_door` | *SAU BUỔI KHÁM BỆNH* · **HÌNH PHẠT NGHIÊM KHẮC · KIỂM SOÁT NGỘT NGẠT** | Khe sáng tắt ở "khép lại" | | |
| 4-15 | `4.08` (nghỉ) | — | — | tối dần | — | — | | |
| 4-16 | `4.09#1` | H | T1 | `locked_door`, khe sáng dưới cửa | **GYPSY TỪNG CỐ GẮNG TỰ CỨU MÌNH** | — | | ✂ |
| 4-17 | `4.09#2` | H | T2 | `records` | *BIÊN BẢN THẨM VẤN* · **BIẾN CỐ NĂM 2011** | — | | |
| 4-18 | `4.09#3` | H | T1 | `pinboard` mờ | *LẮNG NGHE:* **HỒ SƠ SỰ VIỆC TỪ ĐIỀU TRA VIÊN** | — | →D | |
| 4-19 | `4.10#1` | D | T6 | `night_street` + `gypsy_stand` | *2011 · 19 tuổi* · **TRỐN KHỎI NHÀ ĐỂ CẦU CỨU** | — | | |
| 4-20 | `4.10#2`–`#3` | D | T2 | `pinboard`, tập giấy tờ, dấu `GIẢ MẠO` | **VÀI GIỜ SAU, BÀ LẦN RA DẤU VẾT** → `#3`: *Giấy tờ giả mạo: vị thành niên · thiểu năng trí tuệ · mất năng lực hành vi dân sự* | Dấu mộc ở "giả mạo" | | |
| 4-21 | `4.10#4` | D | T1 | `house_night` + `gypsy_walk` đi về nhà | **TRAO TRẢ VỀ NGÔI NHÀ MÀU HỒNG** | — | | |
| 4-22 | `4.10#5` | D | T1 | `screen_off` | **ĐÊM HÔM ĐÓ** · *Không bao giờ được bước ra khỏi cửa* | Màn hình tắt dần ở "phá hỏng" | 🅑 P2 | |
| 4-23 | `4.11` (nghỉ) | — | — | tối dần | — | — | | |
| 4-24 | `4.12#1` | H | T1 | `night_street` + `crowd` quay lưng | **XÃ HỘI CHỈ TIN NGƯỜI MẸ** · *Cú sốc năm 2011* | — | | |
| 4-25 | `4.12#2` | H | T1 | `locked_door` + một sợi chỉ mảnh (Pillow) | *LẮNG NGHE:* **SỢI DÂY VÔ HÌNH** | — | →C | |
| 4-26 | `4.13#1` | C | T9 | `hands` mờ | **GẮN KẾT CHẤN THƯƠNG** *(Trauma Bonding)* | — | | |
| 4-27 | `4.13#2` | C | T4 | `dress_hanger` tối | *Người gây ra bệnh tật — cũng là người duy nhất ôm ấp cô* → “thiên thần nhỏ của mẹ” | Câu trích ở cụm từ | | |
| 4-28 | `4.13#3` | C | T3 | `void` + đường ranh giới tan dần (Pillow) | **TÊ LIỆT KHẢ NĂNG PHÂN ĐỊNH RANH GIỚI** | Đường tan trong câu | | |
| 4-29 | `4.15#1` | H | T1 | `corridor` | **MỌI LỐI THOÁT HỢP PHÁP BỊ BỊT KÍN** | Tiếng bàn phím ở đầu | | |
| 4-30 | `4.15#2` | H | T1 | `night_screen` + `godejohn_screen` | **NICHOLAS GODEJOHN** · *Quen qua mạng Internet* | — | | |
| 4-31 | `4.15#3` | H | T9 | `void` + 2 bóng người, bóng đổ hoà làm một | **FOLIE À DEUX** *(Điên cuồng đôi)* | Bóng nhập ở "trượt vào" | | |
| 4-32 | `4.15#4`–`#5` | H | T1 `hero` | `house_night`, cửa mở, ánh sáng tràn | *Chỉ khi mẹ cô biến mất…* → **THÁNG 6 · 2015** | Cửa sáng ở "mở cửa" | ⊘ | |
| 4-33 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT PHÁP Y & LỜI KẾT** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT, DẤU HIỆU NHẬN DIỆN & LỜI KẾT · nền chủ đạo `court_dawn`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` | H | T1 | `court_dawn` | **TÒA ÁN BANG MISSOURI** | Búa gõ ở đầu câu | | |
| 5-02 | `5.02#2` | H | T2 | `court_dawn` mờ | *VỀ MẶT LUẬT PHÁP* · **MỘT TRỌNG TỘI KHÔNG THỂ CHỐI CÃI** | — | | |
| 5-03 | `5.02#3` | H | T2 | `court_dawn` mờ + bảng tên trên bàn (Pillow) | *Dan Patterson · Chánh biện lý hạt Greene* (chỉ chữ, V5) · **KẺ CHỦ MƯU — ĐỒNG THỜI LÀ NẠN NHÂN** | Tiêu đề ở "kẻ chủ mưu" | | |
| 5-04 | `5.03` (nghỉ) | — | — | giữ 5-03 | — | — | | |
| 5-05 | `5.04#1` | H | T5 | `court_dawn` | *2016 · Giết người cấp độ hai* · **10 NĂM** · *Mức án thấp nhất có thể* | Số đếm 0 → 10 | | |
| 5-06 | `5.04#2` | H | T4 `hero` | `prison_window` | *LỜI GYPSY TRONG TRẠI GIAM* → “Ở trong nhà tù của pháp luật, lần đầu tiên trong đời tôi cảm thấy mình được tự do hơn cả khi sống trong ngôi nhà của mẹ.” | Câu trích từng dòng từ dấu `:` | ⊘ | |
| 5-07 | `5.04#3` | H | T5 | `prison_window`, nắng sáng dần | *12 · 2023* · **85%** · *Chính thức được trả tự do* | Thanh tiến trình | | |
| 5-08 | `5.05` (nghỉ) | — | — | sáng dần | — | — | | |
| 5-09 | `5.06#1` | H | T1 | `court_dawn`, `pull` | **4 DẤU HIỆU CẢNH BÁO ĐỎ** *(Red Flags)* · *Chuyên gia tâm lý & Điều tra viên* | — | →C+D | |
| 5-10 | `5.07#1` | C | T8 cờ | `void` đỏ sẫm, 4 ô cờ | *01* · **BỆNH SỬ DÀY ĐẶC — XÉT NGHIỆM LUÔN MÂU THUẪN** | Cờ 1 tô đầy | hai badge | |
| 5-11 | `5.07#2` | C | T8 cờ | cờ 2 | *02* · **TRIỆU CHỨNG CHỈ CÓ KHI NGƯỜI CHĂM SÓC CÓ MẶT** | — | hai badge | |
| 5-12 | `5.08#1` | D | T8 cờ | cờ 3 | *03* · **HÀO HỨNG VỚI THỦ THUẬT · PHÔ TRƯƠNG BỆNH · ĐỔI BÁC SĨ** | 3 cụm theo cụm từ | hai badge · Sói sáng | |
| 5-13 | `5.08#2` | D | T8 cờ | cờ 4 | *04* · **CÔ LẬP KHỎI TRƯỜNG HỌC, BẠN BÈ, NGƯỜI THÂN** + dấu mộc “bảo vệ sức khỏe” | Dấu mộc ở cụm từ | hai badge | |
| 5-14 | `5.09` (nghỉ 2,5 s) | — | T8 | đủ 4 cờ, `still` | 4 dòng tóm tắt | — | ⊘ | |
| 5-15 | `5.10#1` | H | T1 | `podcast_desk`, đèn ấm dần | **HỒ SƠ KHÉP LẠI** | — | | |
| 5-16 | `5.10#2` | H | T1 `hero` | `house_dawn` + `gypsy_walk`, xe lăn bỏ lại | **TỰ BƯỚC ĐI TRÊN ĐÔI CHÂN CỦA MÌNH** | Trời sáng dần | ⊘ | |
| 5-17 | `5.10#3` | H | T1 | `cage` mở, nắng | **THỨ KHOÁC ÁO THIÊN THẦN** | Tiêu đề ở "khoác áo thiên thần" | | |
| 5-18 | `5.11` (nghỉ) | — | — | giữ 5-17 | — | — | | |
| 5-19 | `5.12#1` | H | T1 | `podcast_desk` | **CẢM ƠN CÁC KHÁCH MỜI** · *Nhân vật minh hoạ · giọng đọc AI* | Dàn khách mời: 5 ảnh P0 sáng lần lượt | dàn khách mời | |
| 5-20 | `5.12#2` | H | T10 | `podcast_desk` mờ | **HẸN GẶP LẠI Ở TẬP TIẾP THEO** · *Để lại góc nhìn của bạn ở phần bình luận* | — | 🅑 | |
| 5-21 | `5.13`–`5.14` | — | T2 | `podcast_desk`, bìa hồ sơ gập (Pillow), cassette dừng | — | Bìa gập ở "Bụp"; mờ ra đen | ⊘ | ◼ |

**Tổng: 122 dòng = 104 shot có lời + 18 dòng không lời.** Phủ 128/128 câu, đúng thứ tự, cột Vai khớp người nói (kiểm tra bằng script ngày 22/10; `validate_shots.py` phải lặp lại).

**Xuất hiện của linh thú (ước tính):**

| Nhân vật | Lượt nói | Bán thân (câu đầu lượt + `🅑`) | Lần được mời (`→`) |
|---|---:|---:|---:|
| Cú · Host | 21 | ~22 (21 đầu lượt + 3 `🅑` − 2 đầu lượt bị `⊘`) | — |
| Sói · Điều tra viên | 4 | 7 | 4 |
| Cáo · Chuyên gia | 6 | 9 | 5 |
| Cừu · N1 | 1 | 2 | 1 |
| Mèo · N2 | 1 | 2 | 1 |

Badge hiện **suốt** mọi lượt của cả 5 nhân vật.

---

---

## PHỤ LỤC A (Tập 01) — CẤU TRÚC KỊCH BẢN (`parse_kichban.py` trên `kichban_tap01_22102026_v2.md`, 22/10/2026)

B1 phải sinh ra **đúng bảng này**; khác là dừng và báo.

| Mã | Vai / loại | Câu | Từ | Chỉ dẫn / mô tả |
|---|---|---:|---:|---|
| `1.01` | *BGM* | — | — | Hộp nhạc lên dây cót, bị drone bóp nghẹt |
| `1.02` | *SFX* | — | — | Còi cảnh sát xa, gõ cửa dồn dập |
| `1.03` | Cú · Host | 3 | 70 | Chậm, trầm, giữ khoảng cách khách quan |
| `1.04` | *Nghỉ 2,0 s* | — | — | |
| `1.05` | Cú · Host | 2 | 66 | (kế thừa) |
| `1.06` | *SFX* | — | — | Băng ghi âm "Tách" |
| `1.07` | **Cừu · N1** | 3 | 105 | Xúc động, chân thật như trả lời phỏng vấn |
| `1.08` | Cú · Host | 6 | 151 | Đẩy nhanh nhịp độ |
| `1.09` | *Nghỉ 2,0 s* | — | — | Nhạc dừng đột ngột (giữ drone −40 dB) |
| `1.10` | *SFX* | — | — | Bộ đàm rè, mở cửa phòng thẩm vấn |
| `1.11` | **Sói · Điều tra viên** | 8 | 143 | Hạ trầm, sắc lạnh, dứt khoát |
| `1.12` | *SFX* | — | — | "Tách", cello vào |
| `1.13` | Cú · Host | 2 | 60 | — |
| `2.01` | *BGM* | — | — | Máy đo nhịp tim + piano |
| `2.02` | Cú · Host | 3 | 68 | Đều đặn, dẫn dắt |
| `2.03` | *SFX* | — | — | Lật giấy hồ sơ |
| `2.04` | Cú · Host | 5 | 131 | (kế thừa) |
| `2.05` | *Nghỉ 1,5 s* | — | — | |
| `2.06` | Cú · Host | 3 | 57 | (kế thừa) |
| `2.07` | **Sói · Điều tra viên** | 10 | 348 | Đanh thép, nhấn từng chứng cứ |
| `2.08` | *SFX* | — | — | Khoá cửa sắt "Cạch" |
| `2.09` | Cú · Host | 4 | 91 | Trầm lắng |
| `3.01` | *BGM* | — | — | Ambient sâu, học thuật |
| `3.02` | Cú · Host | 5 | 159 | — |
| `3.03` | *Nghỉ 2,0 s* | — | — | |
| `3.04` | Cú · Host | 2 | 43 | — |
| `3.05` | **Cáo · Chuyên gia** | 9 | 239 | Phân tích chuyên môn, rõ ràng |
| `3.06` | *Nghỉ 1,5 s* | — | — | |
| `3.07` | Cú · Host | 2 | 69 | — |
| `3.08` | **Cáo · Chuyên gia** | 6 | 147 | Hạ giọng trầm, chậm rãi hơn |
| `3.09` | *Nghỉ 2,0 s* | — | — | |
| `3.10` | **Cáo · Chuyên gia** | 6 | 122 | (kế thừa) |
| `4.01` | *BGM* | — | — | Nhịp tim chậm + violin |
| `4.02` | Cú · Host | 2 | 55 | Trăn trở |
| `4.03` | **Mèo · N2** | 3 | 74 | Băn khoăn, hoài nghi |
| `4.04` | *Nghỉ 2,0 s* | — | — | |
| `4.05` | Cú · Host | 2 | 72 | — |
| `4.06` | *SFX* | — | — | Xiềng xích, kim loại |
| `4.07` | **Cáo · Chuyên gia** | 8 | 207 | — |
| `4.08` | *Nghỉ 1,5 s* | — | — | |
| `4.09` | Cú · Host | 3 | 61 | — |
| `4.10` | **Sói · Điều tra viên** | 5 | 135 | Trầm, thuật lại hồ sơ |
| `4.11` | *Nghỉ 2,0 s* | — | — | Host lắng xuống |
| `4.12` | Cú · Host | 2 | 66 | — |
| `4.13` | **Cáo · Chuyên gia** | 3 | 70 | — |
| `4.14` | *SFX* | — | — | Bàn phím gõ trong đêm |
| `4.15` | Cú · Host | 5 | 116 | — |
| `5.01` | *BGM* | — | — | Búa tòa án → piano ấm |
| `5.02` | Cú · Host | 3 | 116 | Điềm đạm, tổng kết |
| `5.03` | *Nghỉ 1,5 s* | — | — | |
| `5.04` | Cú · Host | 3 | 107 | (kế thừa) |
| `5.05` | *Nghỉ 2,0 s* | — | — | |
| `5.06` | Cú · Host | 1 | 60 | (kế thừa) |
| `5.07` | **Cáo · Chuyên gia** | 2 | 77 | Nhấn mạnh từng ý, góc lâm sàng |
| `5.08` | **Sói · Điều tra viên** | 2 | 82 | Tiếp lời, góc hành vi xã hội |
| `5.09` | *Nghỉ 2,5 s* | — | — | Piano dâng nhẹ |
| `5.10` | Cú · Host | 3 | 114 | Trầm ấm, truyền cảm |
| `5.11` | *Nghỉ 1,5 s* | — | — | |
| `5.12` | Cú · Host | 2 | 64 | (kế thừa) |
| `5.13` | *SFX* | — | — | Gấp hồ sơ "Bụp", tắt máy ghi âm "Tách" |
| `5.14` | *BGM* | — | — | Piano ngân 5 s rồi tắt |
| | **Tổng** | **128** | **3.545** | |

### B4.1 SFX đã có trong master (22/10/2026)

Ngoài tiếng "Tách" (tổng hợp bằng code trong `build_audio3.py`), tập đã có **11 file SFX** tự tổng hợp bằng `.work/make_sfx.py` (không tải file ngoài → không vướng bản quyền). Đặt theo bảng `SFX_CUES` trong `build_audio3.py`; `offset` âm = đặt **trước** mốc để tiếng nối vào câu thoại kế tiếp.

| File | Mốc | Offset | Mức | Mô tả |
|---|---|---:|---:|---|
| `police_siren_distant.wav` | `1.02` | −2,80 s | −3 dB | Còi xe cảnh sát vọng xa |
| `door_knock.wav` | `1.02` | −0,90 s | −2 dB | Gõ cửa dồn dập trong đêm |
| `radio_chatter.wav` | `1.10` | −3,00 s | −6 dB | Bộ đàm rè + tiếng mở cửa phòng thẩm vấn |
| `heart_beep.wav` | `2.01` | −5,03 s | −18 dB | Máy đo nhịp tim "Bíp… Bíp…" |
| `paper_rustle.wav` | `2.03` | −1,00 s | −8 dB | Lật giấy hồ sơ sột soạt |
| `lock_door.wav` | `2.08` | −1,10 s | −2 dB | Khoá cửa sắt "Cạch" |
| `heartbeat_slow.wav` | `4.01` | −4,97 s | −18 dB | Nhịp tim đập chậm (Hồi 4) |
| `chains.wav` | `4.06` | −2,50 s | −5 dB | Xiềng xích, kim loại va nhẹ |
| `keyboard_night.wav` | `4.14` | −2,20 s | −12 dB | Bàn phím gõ trong đêm |
| `gavel.wav` | `5.01` | −1,10 s | +1 dB | Búa tòa án gõ "Cốp" |
| `folder_close.wav` | `5.13` | −0,47 s | −8 dB | Gấp hồ sơ giấy "Bụp" |

Mức tính theo RMS lời, hiệu chuẩn bằng cách nghe thật trong bản thành phẩm (mốc tham chiếu: tiếng "Tách" ở −6 dB). Ba tiếng "Tách" (mã `1.06`, `1.12`, `5.13`) vẫn do `build_audio3.py` tổng hợp trực tiếp, không cần file.

**Kiểm chứng**
- Có mặt đúng chỗ: tương quan chéo với stem SFX lossless → **14/14** (NCC = 1,000).
- Có thật trong bản xuất: so năng lượng dải tần đặc trưng giữa master mới và master cũ (chưa có SFX) → **11/11 tăng 22–47 dB**.
- Nghe rõ: nghe thử trên bản thành phẩm (nhạc nền + lời đọc) → **11/11 CLEAR**, khớp đúng nghĩa.
- Loudness sau khi thêm SFX: **−16,2 LUFS**, true peak −4,3 dBFS (chuẩn: −16 LUFS / ≤ −1,5 dBFS).
- Luồng hình của MP4 **không đổi** (MD5 giống hệt bản cũ — chỉ thay lớp âm thanh).

---

## PHỤ LỤC B (Tập 01) — 23 CHỖ GIẢM BẠO LỰC (`kichban_tap01_22102026.md` → `_v2.md`)

Nguyên tắc: **giữ dữ kiện và luận điểm tâm lý, bỏ chi tiết thể xác**. Không thêm dữ kiện mới. Số câu và mã câu không đổi.

| Câu | Bản gốc | Bản v2 |
|---|---|---|
| `1.03#3` | …khiến cả khu phố chết lặng: *"Con khốn đó chết rồi."* | …một dòng trạng thái ngắn ngủi, đầy hằn học, thông báo rằng bà Dee Dee đã qua đời – khiến cả khu phố chết lặng |
| `1.08#1` | họ tìm thấy thi thể của người mẹ… | họ phát hiện người mẹ… đã qua đời trong phòng ngủ |
| `1.08#5` | Kẻ máu lạnh nào đã sát hại người mẹ tận tụy ấy, rồi bắt cóc… | Ai đã gây ra cái chết của người mẹ tận tụy ấy, rồi đưa đi… |
| `1.11#8` | kế hoạch đoạt mạng bà mẹ "thánh thiện" | kế hoạch dẫn đến cái chết của bà mẹ "thánh thiện" |
| `2.02#1` | chọn cách kết liễu mẹ ruột | đi đến một lựa chọn cực đoan với chính mẹ ruột |
| `2.02#2` | căn phòng ngủ đẫm máu | căn phòng ngủ |
| `2.07#1` | trực tiếp hủy hoại cơ thể con gái | trực tiếp tác động lên sức khỏe con gái |
| `2.07#2` | hàm răng bị mục ruỗng và phải nhổ bỏ toàn bộ răng cửa | sức khỏe răng miệng của cô bé bị tổn hại nghiêm trọng |
| `2.07#3` | phẫu thuật đặt ống truyền thức ăn trực tiếp qua thành bụng vào dạ dày | đặt ống nuôi ăn qua dạ dày |
| `2.07#4` | bôi thuốc gây tê vào nướu để nước bọt chảy ròng ròng… cắt bỏ tuyến nước bọt | tạo ra những triệu chứng giả trước mắt bác sĩ… một ca phẫu thuật tuyến nước bọt không cần thiết |
| `3.02#2` | biến đứa con… thành một phế nhân đau đớn | khiến đứa con… phải sống như một người bệnh |
| `3.07#2` | bị nghi bỏ thuốc diệt cỏ vào thức ăn của mẹ kế và bỏ đói mẹ ruột… | bị nghi có những hành vi gây hại cho chính người thân trong gia đình |
| `3.08#5` | Hãy làm cho con bé tàn tật và phụ thuộc hoàn toàn vào mình | Hãy khiến con bé tin rằng mình bệnh tật và phụ thuộc hoàn toàn vào mẹ |
| `3.08#6` | không thể tự ăn uống mà phải truyền qua ống thông dạ dày… vị Chúa tể duy nhất nắm giữ sự sống | tin rằng mình… không thể tự chăm sóc bản thân… người duy nhất nắm giữ cuộc sống |
| `3.10#6` | yếu ớt, vô tính và… | yếu ớt và… |
| `4.07#2` | chịu đựng sự đau đớn lặp đi lặp lại | chịu đựng những áp lực tiêu cực lặp đi lặp lại |
| `4.07#7` | siết chặt lại đến mức bầm tím | siết chặt lại như một lời cảnh cáo không thành tiếng |
| `4.07#8` | những trận đòn bằng móc áo, bị bỏ đói và bị trói vào thành giường suốt hai tuần | những hình phạt nghiêm khắc và sự kiểm soát ngột ngạt |
| `4.10#5` | dùng búa đập nát chiếc máy tính… đe doạ đập nát các ngón tay | phá hỏng chiếc máy tính… cảnh cáo cô không bao giờ được bước ra khỏi cửa |
| `4.13#2` | người đầu độc Gypsy | người gây ra bệnh tật cho Gypsy |
| `4.13#3` | bạo hành thể xác | kiểm soát hà khắc |
| `5.02#2` | lên kế hoạch sát hại mẹ ruột | lên kế hoạch dẫn đến cái chết của mẹ ruột |
| `5.02#3` | bạo hành y khoa | lạm dụng y khoa |
| `5.08#1` | thủ thuật y khoa đau đớn | thủ thuật y khoa xâm lấn |

**Giữ nguyên có chủ đích:** "ung thư máu" (tên bệnh) · "giết người cấp độ hai" ở `5.04#1` (tên tội danh trong bản án — đổi sẽ sai sự thật) · "cạo trọc đầu", "váy công chúa" ở `2.04#5`, `3.10#2` (cốt lõi của luận điểm *tước đoạt sự trưởng thành*, không mang tính bạo lực).

---

---

*Bản sao v9 trước khi chuyển thành tiêu chuẩn: `90_LUU_TRU/ke_hoach_cu/KeHoach_LamLai_Video_Tap01_v9.md`. Không file nguồn nào bị sửa.*
