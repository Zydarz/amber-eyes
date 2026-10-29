# HỒ SƠ SẢN XUẤT TẬP 01 · BẢN TIẾNG HÀN · 「엄마의 사랑이라는 이름의 독약」 (PHẦN B)

> **TRẠNG THÁI: CHỜ DUYỆT GIỌNG ĐỌC & DỰNG**

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản:** `01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md` · **Chữ cố định:** `00_TIEU_CHUAN/CHU_CO_DINH_KO.md` · **Thành phẩm:** `02_SAN_XUAT/Tap01_KO/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md`. Bảng shot giữ nguyên các cột Câu, Vai, Mẫu, Nền, Nhân vật và mô tả beat; chỉ thay:
- cột **Chữ** sang tiếng Hàn chuẩn phát thanh tài liệu (Pillow vẽ chữ với `malgun.ttf` / `malgunbd.ttf`);
- các cụm `ở "…"` trong cột **Beat** sang cụm tiếng Hàn **có thật** trong câu KO tương ứng.

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap01_KO/kichban_tap01_KO.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_KO.md`, 128 câu, 33 lượt nói, passed `_qc_ko_parity.py`) |
| Lượt nói / câu | 33 / **128**. Host 50% · Chuyên gia 24% · Điều tra viên 20% · Người bình thường 5%. Mã câu trùng 100% bản VN (`script_tap01_KO.json`) |
| N1 / N2 | `1.07` 증인 (Cừu) / `4.03` 시청자 (Mèo) |
| Bảng shot | 122 dòng = 104 shot có lời + 18 dòng không lời |
| Nền dùng | 45 ảnh `assets/bg/` (dùng lại 100% của bản VN/EN/JA) |
| Giọng dự kiến | H `Korean_CalmGentleman` 0.95 · D `Korean_ColdYoungMan` 0.95 · C `Korean_DecisiveQueen` 0.92 · N1 `Korean_GentleWoman` 0.95 · N2 `Korean_SweetGirl` 0.95 |

## B3. Ánh xạ riêng (trong `parse_shots.py`)

Giống hệt bản VN (`COMBO`, `BG2`, `INSET`), vì số hiệu shot và nền không đổi.

## 6. DANH SÁCH SHOT — TẬP 01 BẢN TIẾNG HÀN

**Đọc bảng:** *Vai* = người đang nói (H 호스트 · D 수사관 · C 심리학자 · N1 증인 · N2 시청자).

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X (hiện badge chờ) · `✦` = lần đầu xuất hiện (thẻ giới thiệu) · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` (chỉ hình, shot I-01 → I-04, chi tiết ở A5.7) ở 0,00 s. Không câu thoại nào thuộc intro.

### 제1막 — 신뢰가 무너지는 순간 · nền chủ đạo `house_night`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s, chồng lên phần đen cuối intro) | — | T1 | `house_police` hiện dần từ đen, `push` | *제1막 · 신뢰가 무너지는 순간* | Đèn cảnh sát quét; drone dâng | ⊘ | |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `house_night` mờ | **2015년 6월 14일** · *Missouri 주 Springfield* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T11 | `phone_dark` | *모녀의 공동 SNS 계정* → **온 마을을 침묵에 빠뜨린 한 줄의 상태 글** | Bài đăng hiện dạng các dòng mờ, không đọc được chữ, ở "짧고 쓴 듯한" | | |
| 1-03 | `1.04` (nghỉ 2 s) | — | — | giữ 1-02, ánh đỏ nhấp nháy | — | — | | |
| 1-04 | `1.05#1` | H | T1 | `house_police` + `crowd` | **파스텔 핑크빛의 작은 집** · *Missouri 주 Springfield* (번지는 화면에 표시하지 않음 — 개인 주택) | — | | |
| 1-05 | `1.05#2` | H | T1 | `house_night`, `pull` | *다음 순서:* **같은 골목에 사는 주민** | — | →N1 | |
| 1-06 | `1.07#1` | N1 | T4 lời kể | `house_night` ấm, mờ | “성스러운 모성애의 상징” | — | ✦ Cừu | |
| 1-07 | `1.07#2` | N1 | T8 | `wheelchair_room` + `deedee_wheelchair` | *온 마을이 믿었던 사실* · *하반신 마비 · 백혈병 · 근이영양증 · 중증 뇌전증 · 7세 수준의 지능* | Mỗi mục tại cụm từ | | |
| 1-08 | `1.07#3` | N1 | T4 lời kể | `house_night` ấm | “온 동네 사람들이 감동과 칭송의 눈물을 흘렸다” | — | 🅑 | |
| 1-09 | `1.08#1` | H | T1 | `bedroom_door` | **어머니는 사망했다** | — | | |
| 1-10 | `1.08#2` | H | T1 | `empty_room`, `still` | **GYPSY ROSE는 흔적도 없이 사라졌다** | — | ⊘ | ✂ |
| 1-11 | `1.08#3`–`#4` | H | T1 | `wheelchair_room` | **휠체어 · 산소통 · 수십 개의 약병** | `#3` sáng xe lăn, `#4` sáng kệ | | |
| 1-12 | `1.08#5` | H | T3 | `wheelchair_room` tối + dấu `?` lớn | *전미가 묻는다* · **어머니를 죽음으로 몰고 간 자는 대체 누구인가?** | — | | |
| 1-13 | `1.08#6` | H | T1 | `interrogation`, `push` | *다음 순서:* **사건 담당 수사관** | — | →D | |
| 1-14 | `1.09`–`1.10` (nghỉ 2 s) | — | — | giữ 1-13, nhiễu bộ đàm `cold` | — | — | ⊘ | |
| 1-15 | `1.11#1` | D | T2 | `pinboard` | **전국 지명수배 및 수색영장** | Dấu mộc ở "전국 지명수배" | ✦ Sói | |
| 1-16 | `1.11#2` | D | T7 | `route_night` | **그 다음 날** · *Wisconsin 주 — 수백 마일 밖* | Đường tự vẽ, số đếm | | |
| 1-17 | `1.11#3`–`#4` | D | T1 | `interrogation` + `gypsy_stand` | **그녀는 두 발로 온전히 서서 걷고 있었다** | `#4` sáng đèn treo | | |
| 1-18 | `1.11#5`–`#7` | D | T8 gạch bỏ | giấy hồ sơ trên `records` | *백혈병 · 근이영양증 · 뇌 손상* | Mỗi câu gạch một mục | | ✂ |
| 1-19 | `1.11#8` | D | T1 `hero` | `bedroom_door` + `gypsy_stand`, tối dần | **그녀의 작은 사랑스러운 딸** | Tiêu đề ở "작은 사랑스러운 딸" | 🅑 P2 | |
| 1-20 | `1.13#1` | H | T1 | `podcast_desk`, cassette quay | **범죄심리 프로파일링 사건 기록** | "Tách" ở đầu | 🅑 | |
| 1-21 | `1.13#2` | H | T9 → T10 | `house_night` | **대리 뮌하우젠 증후군** → *제01화 · 엄마의 사랑이라는 이름의 독약* | Thuật ngữ ở "대리 뮌하우젠 증후군"; tên tập cuối câu | | |
| 1-22 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *제2막* · **의료 감옥에서의 23년** | — | ⊘ | ◼ |

### 제2막 — 범죄 현장 & 진료 기록 · nền chủ đạo `wheelchair_room`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#2` | H | T1 | `bedroom_door` | **단순한 침실이 아니다** · *2015년 6월* | Tiêu đề ở `#2` | | |
| 2-02 | `2.02#3` | H | T5 | `wheelchair_room` + `gypsy_wheelchair` | *진짜 범죄 현장* · **23년** | Số đếm | | |
| 2-03 | `2.04#1`–`#5` | H | T6 | `records`, `pan` | *1991년 · 건강한 출생* → *생후 3개월 · 수면무호흡증 주장* → *조작된 병력의 시작* → *7세 · 척수 손상 · 휠체어* → *삭발한 머리 · 백혈병 항암치료* | 1 câu 1 mốc | ⊘ | |
| 2-04 | `2.06#1` | H | T1 | `clinical` | **단순한 거짓말에 그치지 않는다** | — | 🅑 | |
| 2-05 | `2.06#2` | H | T2 | `records` | **수천 페이지의 진료 기록** · *Gypsy의 신체에 대한 직접적인 의료 개입* | — | | |
| 2-06 | `2.06#3` | H | T1 | `pinboard` mờ, `push` | *다음 순서:* **수사관의 기록 공개** | — | →D | |
| 2-07 | `2.07#1` | D | T2 | `pinboard` | **의료 기록에 남겨진 3가지 증거** | Bộ đếm `0/3` | | |
| 2-08 | `2.07#2` | D | T3 `1/3` | `wheelchair_room` cận kệ thuốc | **고용량 항뇌전증제 투여** · *뇌전증이 아님에도 불구하고* | Phụ ở "뇌전증이 아님에도" | | |
| 2-09 | `2.07#3` | D | T3 `2/3` | `clinical` | **위 영양관(위루관) 삽입** | — | | |
| 2-10 | `2.07#4` | D | T3 `3/3` | `clinical` tối | **불필요한 수술** · *의사들 앞에서 연출된 거짓 증상에 기반* | — | | |
| 2-11 | `2.07#5` | D | T5 | `clinical` + lưới ~100 biểu tượng bác sĩ (Pillow) | **수백 명의 의사들** · *왜 아무도 알아채지 못했는가?* | Biểu tượng bác sĩ hiện dần | | |
| 2-12 | `2.07#6` | D | T9 | `pinboard`, `pull` | **행동 양식** *(Modus Operandi)* | 3 thẻ trống ghim lên | 🅑 | |
| 2-13 | `2.07#7` | D | T2 trên bảng ghim | camera dời tới thẻ 1 | *01* · **간호조무사 출신** · *전문 의료 용어에 정통했다* | — | | |
| 2-14 | `2.07#8`–`#9` | D | T2 trên bảng ghim | thẻ 2 có ảnh `storm` thu nhỏ | *02 · 2005년* · **허리케인 Katrina** → `#9`: *모든 병력은 Dee Dee의 구두 진술에 의존했다* | `#9` nối dây đỏ | | |
| 2-15 | `2.07#10` | D | T2 trên bảng ghim | thẻ 3 + ghi chú Consolas | *03* · **의심을 받으면 → 병원을 바꾸고 이사했다** · *Dr. Bernardo Flasterstein · 2007년* (문자만, V5) | Kéo ra thấy cả bảng | | |
| 2-16 | `2.09#1`–`#2` | H | T1 | `house_closed` | **창문은 언제나 굳게 닫혀 있었다** · *학교 교육은 철저히 차단되었다* | Tiếng khóa cửa ở đầu | | |
| 2-17 | `2.09#3` | H | T5 | `house_closed` mờ | **−4세** · *영원히 미성년자로 묶어두기 위한 나이 조작* | — | | |
| 2-18 | `2.09#4` | H | T1 | `house_night` + bóng song sắt ghép từ lọ thuốc, ống truyền (Pillow) | **창살 없는 감옥** | Dấu mộc ở "처방전" | | |
| 2-19 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *제3막* · **FDIA 가해자의 뇌 속** | — | ⊘ | ◼ |

### 제3막 — 심리해부――FDIA 가해자의 뇌 속 · nền chủ đạo `clinical`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` | H | T5 | `void`, `still` | *모든 것의 밑바탕에 깔린 질문* · **왜?** | Tiêu đề ở "왜?" | ⊘ | ✂ |
| 3-02 | `3.02#2` | H | T1 | `fog` + `deedee_wheelchair` | **후원 기금 · 자선 주택 · 무료 여행** | Hiện dần các mục | | |
| 3-03 | `3.02#3`–`#4` | H | T3 | `charity` | **금전은 2차적인 부수익에 불과했다** | — | | |
| 3-04 | `3.02#5` | H | T9 | `brain_desk` | **대리 뮌하우젠 증후군** · *DSM-5-TR: 타인에게 강요된 사기성장애 (FDIA)* | Tiêu đề ở "DSM-5-TR" | | |
| 3-05 | `3.03` (nghỉ) | — | — | giữ 3-04 | *다음 순서:* **범죄심리학 전문가** | — | | |
| 3-06 | `3.04#1`–`#2` | H | T1 | `brain_desk`, `push` | **꾀병 (Malingering)** · *이익 추구 및 책임 회피 목적* → **사기성장애 (Factitious Disorder)** · *환자 역할을 원하는 심리적 동기* | So sánh 2 cột | →C | |
| 3-07 | `3.05#1` | C | T9 | `brain_desk` + sơ đồ `brain3` | **관심 · 동정 · 정서적 숭배** | 3 từ căn giữa | ✦ Cáo | |
| 3-08 | `3.05#2` | C | T4 | `brain_desk` tối, tầng 1 sáng + `halo` | **내적 보상** *(Internal Incentive)* | — | | |
| 3-09 | `3.05#3`–`#4` | C | T3 so sánh | `brain_desk` mờ | **3단계의 심리적 심연** | 3 vạch đo | | |
| 3-10 | `3.05#5`–`#6` | C | T1 | `fog` + `deedee_wheelchair` mờ | *제1층* · **악성 자기애 (Malignant Narcissism)** · *‘완벽한 희생적 어머니’라는 가면* | — | | |
| 3-11 | `3.05#7` | C | T1 | `spotlight` + `deedee_wheelchair` | **돌연 우주의 중심이 되었다** | Sáng đèn ở "돌연" | | ✂ |
| 3-12 | `3.05#8` | C | T1 | `spotlight` + biểu tượng bác sĩ, hàng xóm, tờ báo | **중독적인 찬사에 대한 갈망** | — | | |
| 3-13 | `3.05#9` | C | T5 | `void` + đường nhịp tăng vọt | *제2층* · **버림받는 것에 대한 병적 공포** · *절대적 통제에 대한 집착* | — | 🅑 P2 | |
| 3-14 | `3.06` (nghỉ) | — | — | tối dần | **아이는 자라나고, 언젠가 떠난다** | — | | |
| 3-15 | `3.07#1` | H | T1 | `brain_desk` | **아이를 영원히 곁에 묶어둘 방법은 무엇인가?** | — | | |
| 3-16 | `3.07#2` | H | T2 | `records` | **‘아프고, 어머니에게 완전히 의존한다’고 믿게 만드는 것** | — | →C | |
| 3-17 | `3.08#1` | C | T9 | `brain_desk`, tầng 2 sáng | **딸의 생명을 완전히 장악한 유일한 지배자** | — | | |
| 3-18 | `3.08#2`–`#4` | C | T3 | `hands` | — | — | | |
| 3-19 | `3.08#5` | C | T1 `hero` | `void`, tối dần | *제3층* · **인격 지우기의 심리적 서명** *(Signature)* | Tiêu đề ở "인격 지우기" | ⊘ | |
| 3-20 | `3.08#6` | C | T3 | `wheelchair_room` + `gypsy_wheelchair` | **삭발한 머리 · 어린아이의 드레스** · *20세가 넘어서도* | — | | |
| 3-21 | `3.09` (nghỉ) | — | — | giữ 3-20 | **어른이 되는 권리의 박탈** *(Infantilization)* | — | | |
| 3-22 | `3.10#1` | C | T9 | `brain_desk`, tầng 3 sáng | **여성으로서의 성장을 일체 거부당했다** | — | | |
| 3-23 | `3.10#2` | C | T3 | `dress_hanger` | **영원히 7살에 멈춘 인형** | — | | |
| 3-24 | `3.10#3`–`#4` | C | T9 | `dress_hanger` mờ | **극도의 지능 · 치밀한 수완 · 뛰어난 설득력** | 3 từ hiện lần lượt | 🅑 | |
| 3-25 | `3.10#5`–`#6` | C | T1 | `doll` | **완벽한 사랑의 가면** | Tiêu đề ở "사랑의 가면" | | |
| 3-26 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *제4막* · **심문과 전환점――왜 GYPSY는 도망치지 못했는가?** | — | ⊘ | ◼ |

### 제4막 — 심문 & 전환점――왜 GYPSY는 도망치지 못했는가? · nền chủ đạo `interrogation`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` | H | T1 | `night_screen` + bong bóng bình luận mờ (Pillow, không tên) | *사회의 가장 큰 의문* · **왜 일어서서 도망치지 못했는가?** | — | | |
| 4-02 | `4.02#2` | H | T1 | `night_screen`, `push` | **온전히 걸을 수 있었다** · *창살 없는 집* | — | →N2 | |
| 4-03 | `4.03#1` | N2 | T4 lời kể | `night_screen` | *다음 순서:* **사건을 지켜본 시청자의 시선** | — | ✦ Mèo | |
| 4-04 | `4.03#2`–`#3` | N2 | T4 lời kể | `wheelchair_room` tối, xe lăn trống dưới đèn rọi | “왜 휠체어에서 일어나 사람들에게 도움을 청하지 못했는가?” | — | 🅑 ở `#3` | |
| 4-05 | `4.04` (nghỉ) | — | — | tối dần | *다음 순서:* **심리학 전문가의 답변** | — | | |
| 4-06 | `4.05#1` | H | T1 | `glass_box` + `gypsy_wheelchair` nhỏ | **20세기 심리학에서 가장 잔혹한 개념 중 하나** | — | | |
| 4-07 | `4.05#2` | H | T3 | `locked_door` · 2 thẻ thuật ngữ | **학습된 무력감** *(Learned Helplessness)* · *Martin Seligman · 1967년* | — | →C | |
| 4-08 | `4.07#1` | C | T9 | `cage` đóng | **도망칠 수 없는 환경에 오랜 시간 갇힌 생명체** | — | | |
| 4-09 | `4.07#2` | C | T4 `hero` | `cage` đóng, tối dần | **전기 충격 · 반복되는 고통** | — | | |
| 4-10 | `4.07#3` | C | T1 | `cage` đóng → mở (hoà tan 2 nền cùng seed) | **우리의 문이 열려 있어도, 도망치려 하지 않는다** | Cửa mở ở "우리의 문" | | |
| 4-11 | `4.07#4` | C | T1 | `locked_door` | **‘내가 무엇을 해도 무력하다’고 뇌가 학습해버렸다** | — | 🅑 P2 | |
| 4-12 | `4.07#5`–`#6` | C | T3 | `hands` | **딸의 손을 으스러지도록 꽉 쥐는 어머니의 손** | — | | |
| 4-13 | `4.07#7` | C | T3 | `hands`, ánh `cold` | **침묵을 강요하는 경고** | Bàn tay siết chặt ở "더욱 강해졌다" | | |
| 4-14 | `4.07#8` | C | T2 | `locked_door` | **문이 닫히면 가혹한 처벌이 기다렸다** | Cửa đóng ở "닫히면" | | |
| 4-15 | `4.08` (nghỉ) | — | — | tối dần | **23년 동안 저항을 전혀 시도하지 않은 것은 아니다** | — | | |
| 4-16 | `4.09#1` | H | T1 | `locked_door`, khe sáng dưới cửa | **2011년** · *SF 컨벤션 행사 · 남성 지인* | — | | ✂ |
| 4-17 | `4.09#2` | H | T2 | `records` | **탈출 시도** · *모텔* | — | | |
| 4-18 | `4.09#3` | H | T1 | `pinboard` mờ | **불과 몇 시간 만에** | — | →D | |
| 4-19 | `4.10#1` | D | T6 | `night_street` + `gypsy_stand` | **Dee Dee는 즉시 추적해 강제로 끌고 왔다** | — | | |
| 4-20 | `4.10#2`–`#3` | D | T2 | `pinboard`, tập giấy tờ, dấu `GIẢ MẠO` | **‘지적 장애를 가진 미성년자’라는 위조 서류** | Dấu mộc ở "위조 서류" | | |
| 4-21 | `4.10#4` | D | T1 | `house_night` + `gypsy_walk` đi về nhà | **침대에 묶인 채 굶주림의 처벌을 받았다** | — | | |
| 4-22 | `4.10#5` | D | T1 | `screen_off` | **컴퓨터 파괴 · 외부와의 완벽한 단절** | Màn hình tắt ở "부수고" | 🅑 P2 | |
| 4-23 | `4.11` (nghỉ) | — | — | tối dần | **모든 구조의 길이 차단되었다** | — | | |
| 4-24 | `4.12#1` | H | T1 | `night_street` + `crowd` quay lưng | **출구 없는 심리적 덫** | — | | |
| 4-25 | `4.12#2` | H | T1 | `locked_door` + một sợi chỉ mảnh (Pillow) | **유일한 숨구멍: 은밀한 인터넷** | — | →C | |
| 4-26 | `4.13#1` | C | T9 | `hands` mờ | **온라인 데이팅 사이트** · *2012년* | — | | |
| 4-27 | `4.13#2` | C | T4 | `dress_hanger` tối | **Nicholas Godejohn** · *고립된 남성* | — | | |
| 4-28 | `4.13#3` | C | T3 | `void` + đường ranh giới tan dần (Pillow) | **수천 통의 심야 메시지** | — | | |
| 4-29 | `4.15#1` | H | T1 | `corridor` | **어두운 망상의 공유** | — | | |
| 4-30 | `4.15#2` | H | T1 | `night_screen` + `godejohn_screen` | **‘어머니가 사라져야만 내가 구원받을 수 있다’는 확신** | — | | |
| 4-31 | `4.15#3` | H | T9 | `void` + 2 bóng người, bóng đổ hoà làm một | **감응성 정신병 (FOLIE À DEUX)** *(두 사람의 광기)* | Hai bóng người lồng vào nhau ở "광기" | | |
| 4-32 | `4.15#4`–`#5` | H | T1 `hero` | `house_night`, cửa mở, ánh sáng tràn | *어머니가 사라져야만 비로소…* → **2015년 6월** | Cửa sáng ở "문을 열고" | ⊘ | |
| 4-33 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *제5막* · **사법적 단죄와 레드플래그, 그리고 교훈** | — | ⊘ | ◼ |

### 제5막 — 사법적 단죄, 레드플래그 & 교훈 · nền chủ đạo `court_dawn`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` | H | T1 | `court_dawn` | **Missouri 주 법정** | — | | |
| 5-02 | `5.02#2` | H | T2 | `court_dawn` mờ | *법적으로는* · **명백한 중범죄** | — | | |
| 5-03 | `5.02#3` | H | T2 | `court_dawn` mờ + bảng tên trên bàn (Pillow) | *Dan Patterson · Greene 카운티 검사* (문자만, V5) · **주동자인 동시에 가혹한 학대의 피해자** | Tiêu đề ở "주동자" | | |
| 5-04 | `5.03` (nghỉ) | — | — | giữ 5-03 | — | — | | |
| 5-05 | `5.04#1` | H | T5 | `court_dawn` | *2016년 · 유죄 인정 협상 · 2급 살인* · **징역 10년** · *동일 범죄의 법정 최저형* | — | | |
| 5-06 | `5.04#2` | H | T4 `hero` | `prison_window` | *가석방 후 GYPSY의 고백* → “감옥 안에서 평생 처음으로 어머니의 집에 살 때보다 더 큰 자유를 느꼈습니다.” | — | ⊘ | |
| 5-07 | `5.04#3` | H | T5 | `prison_window`, nắng sáng dần | *2023년 12월* · **형기의 85% 복역** · *가석방 출소* | — | | |
| 5-08 | `5.05` (nghỉ) | — | — | sáng dần | — | — | | |
| 5-09 | `5.06#1` | H | T1 | `court_dawn`, `pull` | **경계해야 할 4가지 레드플래그** *(Red Flags)* · *심리학자 & 수사관* | — | →C+D | |
| 5-10 | `5.07#1` | C | T8 cờ | `void` đỏ sẫm, 4 ô cờ | *01* · **비정상적으로 긴 병력 — 검사 결과와의 끊임없는 모순** | — | hai badge | |
| 5-11 | `5.07#2` | C | T8 cờ | cờ 2 | *02* · **증상이 보호자가 동석했을 때만 발생한다** | — | hai badge | |
| 5-12 | `5.08#1` | D | T8 cờ | cờ 3 | *03* · **치료에 대한 기이한 열광 · 질병 과시 · 잦은 병원 변경** | — | hai badge · Sói sáng | |
| 5-13 | `5.08#2` | D | T8 cờ | cờ 4 | *04* · **학교, 친구, 친척들로부터의 완전한 격리** + dấu mộc “보호라는 구실” | — | hai badge | |
| 5-14 | `5.09` (nghỉ 2,5 s) | — | T8 | đủ 4 cờ, `still` | 4가지 레드플래그 요약 | — | ⊘ | |
| 5-15 | `5.10#1` | H | T1 | `podcast_desk`, đèn ấm dần | **사건 기록은 종결되었다** | — | | |
| 5-16 | `5.10#2` | H | T1 `hero` | `house_dawn` + `gypsy_walk`, xe lăn bỏ lại | **자신의 두 다리로 일어서기 시작했다** | — | ⊘ | |
| 5-17 | `5.10#3` | H | T1 | `cage` mở, nắng | **천사의 옷을 입은 악마** | Tiêu đề ở "천사의 옷" | | |
| 5-18 | `5.11` (nghỉ) | — | — | giữ 5-17 | — | — | | |
| 5-19 | `5.12#1` | H | T1 | `podcast_desk` | **출연해주신 게스트 여러분께 감사드립니다** · *가상 인물 · AI 음성* | — | dàn khách mời | |
| 5-20 | `5.12#2` | H | T10 | `podcast_desk` mờ | **다음 사건 파일에서 다시 뵙겠습니다** · *댓글로 여러분의 생각을 남겨주세요* | — | 🅑 | |
| 5-21 | `5.13`–`5.14` | — | T2 | `podcast_desk`, bìa hồ sơ gập (Pillow), cassette dừng | *사건 기록 제01화 · 종결* · **AMBER EYES** · *범죄심리학 — 실사 사건 기록으로 읽는 인간 심리* | Đóng tệp ở "Bụp"; tối đen | ⊘ | ◼ |

**Tổng: 122 dòng = 104 shot có lời + 18 dòng không lời.** Phủ 128/128 câu, đúng thứ tự, cột Vai khớp người nói (kiểm tra bằng script ngày 22/10; `validate_shots.py` phải lặp lại).