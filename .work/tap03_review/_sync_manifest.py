import io
import sys

PATH = r"D:\TEST\Gax\Audi\02_SAN_XUAT\Tap03\Danh_Sach_Anh_Tap03.md"

with io.open(PATH, encoding="utf-8") as f:
    src = f.read()

R = [
    # ---- header ----
    (
        "*Vụ án Edmund Kemper. Ngày 23/10/2026.*",
        "*Vụ án Edmund Kemper. Ngày 23/10/2026.*\n"
        "\n"
        "> **⚠️ ĐÃ ĐỒNG BỘ LẠI 23/10/2026 sau review sự thật của kịch bản.**\n"
        "> Kịch bản đã được viết lại (xem `01_KICH_BAN/Tap03/REVIEW_kichban_tap03.md`): 21 lỗi fact + 4 trích dẫn không có nguồn đã sửa.\n"
        "> Hệ quả trực tiếp lên file này: **mọi mốc câu đã dịch lại** (bảng B2), 4 mô tả ảnh đã sửa nội dung (địa chỉ hiện trường, số án, Rorschach, phiên ân xá), và 1 ảnh (`t3_car_door`) mất mốc vì chi tiết tương ứng đã bị loại khỏi kịch bản.",
    ),
    (
        "**29 lượt · 143 câu · 3 539 từ** — vai H 18 lượt, D 5, C 4, N 2.",
        "**31 lượt · 215 câu · 5 106 từ** — vai H 20 lượt, D 5, C 4, N 2. *(Cập nhật sau review)*",
    ),
    # ---- note 1 & 2 ----
    (
        "1. **Không vẽ súng/dao/còng tay trong xe.** Kịch bản 2.05#4 kể rõ Kemper giấu còng tay, dao găm, súng ngắn và túi nilông dưới gầm ghế. V9 cấm minh hoạ cách gây hại → `t3_under_seat` chỉ vẽ **khoang trống** (compartment rỗng), `t3_car_door` chỉ vẽ **hai lỗ trống** sau khi tháo tay nắm. Lời đọc vẫn đủ, hình không vi phạm.",
        "1. **Không vẽ súng/dao/còng tay trong xe.** Kịch bản 2.07#6 kể rõ Kemper lưu trong **cốp xe** túi nilông, dao găm, chăn và còng tay. V9 cấm minh hoạ cách gây hại → `t3_under_seat` chỉ vẽ **khoang trống** (compartment rỗng). Lời đọc vẫn đủ, hình không vi phạm.\n"
        "   **Sau review:** chi tiết *\"tháo bỏ tay nắm mở cửa ở ghế phụ và chốt khóa an toàn\"* đã **bị loại khỏi kịch bản** (không tìm thấy nguồn nào) → ảnh `t3_car_door` **không còn mốc câu**, không dùng trong bảng shot.",
    ),
    (
        "2. **Kỷ niệm/thưởng vật chất.** 4.07#3 nói về \"chiến lợi phẩm\" → `t3_trophy_box` là **hộp gỗ đậy kín**, không có đồ vật của nạn nhân.",
        "2. **Kỷ niệm/thưởng vật chất.** 4.07#6 nói về \"chiến lợi phẩm\" → `t3_trophy_box` là **hộp gỗ đậy kín**, không có đồ vật của nạn nhân.",
    ),
    # ---- HOI 1 ----
    ("| `t3_dispatch_desk` | Trực ban đêm Santa Cruz, chuông điện thoại reo phá vỡ tĩnh mịch | `1.03#2`–`#4` |",
     "| `t3_dispatch_desk` | Trực ban đêm Santa Cruz, chuông điện thoại reo phá vỡ tĩnh mịch | `1.03#3`–`#5` |"),
    ("| `t3_phone_booth` | Bốt điện thoại ven đường ở Pueblo, Colorado — 1.500 km | `1.03#4` |",
     "| `t3_phone_booth` | Bốt điện thoại ven đường ở Pueblo, Colorado — hơn 1.600 km | `1.03#2`, `#5` |"),
    ("| `t3_tape_start` | Tiếng băng ghi âm bật nhẹ \"Tách\" | `1.06` |",
     "| `t3_tape_start` | Tiếng băng ghi âm bật nhẹ \"Tách\" | `1.08` |"),
    ("| `t3_apartos_house` | Hiện trường số 609 đường Aptos Creek | `1.08#1` |",
     "| `t3_apartos_house` | ⚠️ Hiện trường số **609A đường Ord Drive**, thị xã Aptos *(địa chỉ \"Aptos Creek\" là SAI — đã sửa)* | `1.10#1` |"),
    ("| `t3_bedroom_door` | Phòng ngủ — cánh cửa đóng, khe sáng dưới cửa | `1.08#2` |",
     "| `t3_bedroom_door` | Phòng ngủ — cánh cửa đóng, khe sáng dưới cửa | `1.10#2` |"),
    ("| `t3_prison_corridor` | Hành lang nhà tù — tiếng bước chân vang vọng | `1.09` |",
     "| `t3_prison_corridor` | Hành lang nhà tù — tiếng bước chân vang vọng | `1.11` |"),
    ("| `t3_gate_slam` | Cánh cửa sắt trại giam kéo lê rồi đóng sập \"Rầm\" | `1.10` |",
     "| `t3_gate_slam` | Cánh cửa sắt trại giam kéo lê rồi đóng sập \"Rầm\" | `1.12` |"),
    ("| `t3_fbi_corridor` | Chuyển sang góc nhìn Đặc vụ FBI — bê tông nền cho mở đầu chương trình | `1.11`, `1.13#2` |",
     "| `t3_fbi_corridor` | Chuyển sang góc nhìn Đặc vụ FBI — bê tông nền cho mở đầu chương trình | `1.13`, `1.15#2` |"),
    # ---- HOI 2 ----
    ("| `t3_ravine` | Vực sâu hẻo lánh dọc dãy núi Santa Cruz — hiện trường bị xóa sạch | `2.04#2`–`#3` |",
     "| `t3_ravine` | Vực sâu hẻo lánh dọc dãy núi Santa Cruz — hiện trường bị xóa sạch | `2.06#1`–`#3` |"),
    ("| `t3_galaxie` | Ford Galaxie màu vàng nhạt — mẫu xe cực kỳ phổ biến, không gây chú ý | `2.05#2` |",
     "| `t3_galaxie` | Ford Galaxie màu vàng năm 1969 — mẫu xe cực kỳ phổ biến, không gây chú ý | `2.07#2` |"),
    ("| `t3_car_door` | Tay nắm mở cửa ở ghế phụ bị tháo ra → chiếc lồng giam di động | `2.05#3` |",
     "| `t3_car_door` | ❌ **KHÔNG DÙNG** — chi tiết tháo tay nắm đã bị loại khỏi kịch bản (không có nguồn) | — |"),
    ("| `t3_under_seat` | Dưới gầm ghế — khoang giấu bí mật | `2.05#4` |",
     "| `t3_under_seat` | Khoang giấu trong cốp xe | `2.07#6` |"),
    ("| `t3_courthouse_exterior` | Tòa án hạt Santa Cruz nằm ngay đối diện quán rượu | `2.08#1` |",
     "| `t3_courthouse_exterior` | Tòa án Quận Santa Cruz nằm ngay đối diện quán rượu | `2.09#1` |"),
    ("| `t3_bar_jury_room` | Quán rượu The Jury Room — nơi lui tới của thám tử, cảnh sát, luật sư | `2.08#1`–`#3` |",
     "| `t3_bar_jury_room` | Quán rượu The Jury Room — nơi lui tới của thám tử, cảnh sát, luật sư | `2.09#1`–`#3` |"),
    ("| `t3_bar_stool_shadow` | \"Big Ed\" ngồi ở góc quầy bar uống bia, gật gù phân tích vụ án đang truy lùng chính mình | `2.08#2`–`#6` |",
     "| `t3_bar_stool_shadow` | \"Big Ed\" ngồi ở góc quầy bar uống bia, gật gù phân tích vụ án đang truy lùng chính mình | `2.09#2`–`#9` |"),
    # ---- HOI 3 ----
    ("| `t3_coal_furnace` | Tầng 1 — lò sưởi than suốt nhiều năm, chuột bọ, ẩm ướt | `3.05#4` |",
     "| `t3_coal_furnace` | Tầng 1 — lò sưởi than suốt nhiều năm, chuột bọ, ẩm ướt | `3.05#6` |"),
    ("| `t3_small_bed` | Tầng 1 — đứa trẻ 8 tuổi ngủ dưới tầng hầm | `3.05#3` |",
     "| `t3_small_bed` | Tầng 1 — đứa trẻ 8 tuổi ngủ dưới tầng hầm (có cửa bẩy dưới bàn ăn) | `3.05#6`–`#7` |"),
    ("| `t3_atascadero` | Tầng 2 — Bệnh viện Tâm thần Bang Atascadero (vào năm 15 tuổi, ra năm 21 tuổi) | `3.08#2`, `3.11#3` |",
     "| `t3_atascadero` | Tầng 2 — Bệnh viện Tâm thần Bang Atascadero (vào năm 15 tuổi, thả đúng ngày 21 tuổi) | `3.08#2`–`#5` |"),
    ("| `t3_mother_shadow` | Tầng 2 — cơ chế **phóng chiếu**: bóng người mẹ bị dồn nén | `3.08#4`–`#6` |",
     "| `t3_mother_shadow` | Tầng 2 — cơ chế **phóng chiếu**: bóng người mẹ bị dồn nén | `3.08#7`–`#11` |"),
    ("| `t3_textbooks` | Tầng 3 — học thuộc MMPI, Rorschach, thao túng hội đồng y khoa | `3.11#3` |",
     "| `t3_textbooks` | Tầng 2 — học thuộc MMPI, tự phát triển thang đo của riêng mình, thao túng hội đồng y khoa *(đã bỏ Rorschach — không có nguồn)* | `3.08#3`–`#4` |"),
    ("| `t3_self_observation` | Tầng 3 — tách rời cảm xúc, quan sát cơn khát máu của mình như nhà khoa học theo dõi thí nghiệm | `3.11#1`, `#4`–`#6` |",
     "| `t3_self_observation` | Tầng 3 — tách rời cảm xúc, quan sát cơn khát máu của mình như nhà khoa học theo dõi thí nghiệm | `3.11#1`, `#4`–`#6` |"),
    ("| `t3_brain_mirror` | **\"Chiếc Gương Giải Phẫu Tâm Trí\"** — tự mổ xẻ tâm trí với độ chính xác của bác sĩ giải phẫu thần kinh | `1.11#4`, `3.11#1` |",
     "| `t3_brain_mirror` | **\"Chiếc Gương Giải Phẫu Tâm Trí\"** — tự mổ xẻ tâm trí với độ chính xác của bác sĩ giải phẫu thần kinh | `1.13#5`, `3.11#1` |"),
    # ---- HOI 4 ----
    ("| `t3_vacaville_1978` | Mùa hè 1978, Nhà tù Bang California, Vacaville | `4.02#1`–`#2` |",
     "| `t3_vacaville_1978` | Năm 1978, Cơ sở Y tế Bang California (California Medical Facility), Vacaville | `4.02#1`–`#2` |"),
    ("| `t3_giant_doorway` | \"Kemper khổng lồ như một ngọn núi, lấp kín cả khung cửa\" | `4.05#1` |",
     "| `t3_giant_doorway` | \"Kemper khổng lồ như một ngọn núi, lấp kín cả khung cửa\" | `4.05#1`–`#2` |"),
    ("| `t3_interview_room` | Hắn kéo ghế ngồi xuống, mỉm cười lịch sự như giáo sư đại học | `4.05#2` |",
     "| `t3_interview_room` | Hắn kéo ghế ngồi xuống, mỉm cười lịch sự như giáo sư đại học | `4.05#3` |"),
    ("| `t3_fantasy_spiral` | **Quy luật hình thành của Ảo tưởng tình dục bạo lực** — vòng xoáy không đáy | `4.07#2` |",
     "| `t3_fantasy_spiral` | **Vòng lặp Ảo tưởng Bạo lực (Violent Fantasy Cycle)** — vòng xoáy không đáy | `4.07#2`–`#5` |"),
    ("| `t3_trophy_box` | Khái niệm **Chiến lợi phẩm (Trophies/Souvenirs)** | `4.07#3` |",
     "| `t3_trophy_box` | Khái niệm **Chiến lợi phẩm (Trophies/Souvenirs)** | `4.07#6`–`#7` |"),
    ("| `t3_organized_split` | Hệ thống phân loại: Kẻ giết người **có tổ chức** và **vô tổ chức** | `4.08#1` |",
     "| `t3_organized_split` | Hệ thống phân loại: Kẻ giết người **có tổ chức** và **vô tổ chức** | `4.08#1`–`#3` |"),
    ("| `t3_signature_trace` | **Chữ ký tâm lý (Behavioral Signature)** hiện trường vụ án | `4.08#2` |",
     "| `t3_signature_trace` | **Chữ ký tâm lý (Behavioral Signature)** hiện trường vụ án | `4.08#4`–`#5` |"),
    # ---- HOI 5 ----
    ("| `t3_courtroom_1973` | Phiên tòa Santa Cruz, tháng 11/1973 — 8 án chung thân liên tiếp | `5.02#1`–`#2` |",
     "| `t3_courtroom_1973` | Phiên tòa Santa Cruz (mở 23/10/1973, tuyên án 08/11/1973) — 8 án chung thân **thi hành đồng thời** | `5.02#1`–`#5` |"),
    ("| `t3_life_sentence` | Thụ án suốt đời tại Vacaville; từ chối mọi buổi đều trần xin ân xá | `5.02#4`, `#6` |",
     "| `t3_life_sentence` | Thụ án suốt đời tại Cơ sở Y tế Bang California, Vacaville; hồ sơ bị bác hơn 10 lần, kế tiếp 2031 | `5.02#8`–`#11` |"),
    ("| `t3_gift_drowned` | \"Món quà bị nhúng vào bể chứa của sự ngược đãi\" — ẩn dụ lời kết | `5.08#3` |",
     "| `t3_gift_drowned` | \"Món quà bị nhúng vào bể chứa của sự ngược đãi\" — ẩn dụ lời kết | `5.08#6`–`#7` |"),
    # ---- QC table ----
    ("| Bạo lực / máu / thi thể / vũ khí (vi phạm V9) | **0** — `t3_under_seat` là khoang **rỗng**, `t3_car_door` là **hai lỗ trống**, `t3_trophy_box` là **hộp đậy kín** |",
     "| Bạo lực / máu / thi thể / vũ khí (vi phạm V9) | **0** — `t3_under_seat` là khoang **rỗng**, `t3_trophy_box` là **hộp đậy kín** |"),
    ("| `t3_small_bed` | Có song song chắn → đọc như **phòng giam** hơn là tầng hầm Montana 1950s | Dùng cho `3.05#3` vẫn đúng ý \"giam cầm\". Nếu cần đúng \"tầng hầm\" thì đổi sang `t3_coal_furnace` |",
     "| `t3_small_bed` | Có song song chắn → đọc như **phòng giam** hơn là tầng hầm Montana 1950s | Dùng cho `3.05#6`–`#7` vẫn đúng ý \"giam cầm\". Nếu cần đúng \"tầng hầm\" thì đổi sang `t3_coal_furnace` |"),
    ("| `t3_under_seat` | Đọc như **ghế gỗ / hộp gỗ** hơn là khoang dưới ghế xe | Vẫn là \"khoang giấu bí mật\". Nếu chữ trên hình nói *\"dưới gầm ghế\"*, đặt câu đó cạnh `t3_car_door` |",
     "| `t3_under_seat` | Đọc như **ghế gỗ / hộp gỗ** hơn là khoang cốp xe | Vẫn là \"khoang giấu bí mật\". Câu 2.07#6 nói **cốp xe** — nếu chữ trên hình ghi \"cốp xe\" thì khớp |"),
    # ---- B4 ----
    ("| 4 | `.work/tts_sentences.py` → `N_ELEMENT` | Tap03 có 2 lượt vai N: `1.07` và `2.08` → cần `{... \"1.07\": \"N1\", \"2.08\": \"N2\"}` |",
     "| 4 | `edition.py` → `N_ELEMENT` | Tap03 có 2 lượt vai N: **`1.09`** (trực ban Santa Cruz) và **`2.09`** (cảnh sát quán rượu) → cần `{... \"1.09\": \"N1\", \"2.09\": \"N2\"}`. Lưu ý nhãn `N2` mặc định là \"KHÁN GIẢ\" — Tập 03 không có vai khán giả, phải đổi nhãn |"),
    ("| 5 | Đo lại thời lượng sau khi có audio TTS | Xem B5 — kịch bản hiện **thiếu ~5–6 phút** so với brief |",
     "| 5 | Đo lại thời lượng sau khi có audio TTS | Xem B5 — **đã đạt** ~25,8 phút sau khi bổ sung nội dung có nguồn |"),
    ("| 6 | Bảng nguồn tham khảo theo từng câu (A10) | `02_SAN_XUAT/Tap03/xuat_ban/nguon_tham_khao.md` |",
     "| 6 | Bảng nguồn tham khảo theo từng câu (A10) | ✅ `02_SAN_XUAT/Tap03/xuat_ban/nguon_tham_khao.md` — đã tạo, 19 câu + phụ lục nguyên văn tiếng Anh; **cần người dùng điền link** |"),
    # ---- B5 ----
    ("| Số từ | 4 721 | **3 539** (75% của Tap02) |",
     "| Số từ | 4 721 | **5 106** (108% của Tap02) |"),
    ("| Phần lời | 1 452,8 s | ~1 089 s |",
     "| Phần lời | 1 452,8 s | ~1 547 s |"),
    ("| Phụ lục (gap + intro + nền) | 163,4 s | ~83,5 s |",
     "| Phụ lục (gap + intro + nền) | 163,4 s | ~119 s |"),
    ("| **Tổng** | **1 616,3 s = 26:56** | **~1 173 s = 19:32** (theo hệ số tổng: 20:11) |",
     "| **Tổng** | **1 616,3 s = 26:56** | **~1 666 s = 27:46** *(ước lượng)* |"),
    ("| Brief | 25–27 phút | 25–27 phút ⇒ **KHÔNG ĐẠT, thiếu ~5–6 phút** |",
     "| Brief | 25–27 phút | 25–27 phút ⇒ **ĐẠT** (ước ~25,8 phút theo hệ số phần lời; cần đo lại khi có audio TTS thật) |"),
    ("⇒ Để đạt 25–27 phút, kịch bản cần **+1 300 từ (≈ +26%)**. Bộ 45 ảnh này vẫn hợp lý ở cả hai mốc:\n"
     "45 ảnh / 25,5 phút = **1 ảnh ≈ 34 s** (Tap02: 37 ảnh / 26,9 phút ≈ 44 s) — nhịp chuyển cảnh hơi nhanh hơn Tập 02 nhưng vẫn trong vùng dùng được.",
     "⇒ Sau review, kịch bản đã **+1 567 từ** (bổ sung nội dung có nguồn: danh sách 6 nạn nhân, lịch sử CPRP/VICAP, chẩn đoán 1984, phiên tòa, thẩm phán Brauer, đặc vụ Colomy) và đạt khung 25–27 phút.\n"
     "Bộ 45 ảnh này vẫn hợp lý: 45 ảnh / 25,8 phút = **1 ảnh ≈ 34 s** (Tap02: 37 ảnh / 26,9 phút ≈ 44 s) — nhịp chuyển cảnh hơi nhanh hơn Tập 02 nhưng vẫn trong vùng dùng được.\n"
     "**Lưu ý:** `t3_car_door` không còn mốc câu (chi tiết đã bị loại khỏi kịch bản) → nếu dùng đủ 45 ảnh thì cần **giảm nhịp hoặc tái neo ảnh này** cho một câu khác; còn 44 ảnh thì không vấn đề."),
]

for i, (old, new) in enumerate(R, 1):
    n = src.count(old)
    if n != 1:
        print(f"REPL {i}: MATCHED {n} TIMES -> ABORT")
        print("  old:", old[:120])
        sys.exit(1)
    src = src.replace(old, new, 1)
    print(f"REPL {i}: ok")

with io.open(PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(src)
print("manifest updated")
