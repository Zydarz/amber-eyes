import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "02_SAN_XUAT" / "Tap02" / "KeHoach_Video_Tap02.md"
lines = PLAN.read_text(encoding="utf-8").splitlines()

replacements = {
    # Hồi 2: 2.04
    "| 2-04 | `2.04#2` | H | T8 | `t2_folder_tree`, `pan` | *Hàng nghìn bức ảnh và video · Đóng dấu ngày giờ · Hệ thống thư mục phức tạp · Ghi chép về từng lần phạm tội* | Mỗi mục ở cụm từ | | |":
    "| 2-04 | `2.04#1`–`#2` | H | T1 | `t2_escalation_stairs` | *Kẻ bắt cóc không xuất hiện từ hư không* · **BÓNG MA TRONG BÓNG TỐI** | — | | |",

    "| 2-05 | `2.04#3`–`#4` | H | T1 | `t2_escalation_stairs` | **KHÔNG PHẢI MỘT KẺ BỘC PHÁT TRONG MỘT ĐÊM** → `#4`: *Đỉnh chóp của một tảng băng chìm* · **4 NẤC THANG LEO THANG HÀNH VI** | — | | |":
    "| 2-05 | `2.04#3` | H | T1 | `t2_escalation_stairs` | *Đỉnh chóp của một tảng băng chìm* · **4 NẤC THANG LEO THANG HÀNH VI** | — | | |",

    "| 2-06 | `2.04#5` | H | T1 | `pinboard` mờ, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN PHÂN TÍCH PHƯƠNG THỨC HOẠT ĐỘNG** | — | →D | |":
    "| 2-06 | `2.04#4` | H | T1 | `pinboard` mờ, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN PHÂN TÍCH PHƯƠNG THỨC HOẠT ĐỘNG** | — | →D | |",

    # Hồi 2: 2.08
    "| 2-22 | `2.08#7` | D | T5 | `t2_folder_tree` | **82** · *Vụ đột nhập* → *Khoảng 1.400 món đồ bị lấy đi* | Số đếm; dòng phụ ở \"1.400\" | | |":
    "| 2-22 | `2.08#6` | D | T1 | `t2_suv_stop` | *VÂN LỐP VÀ DẤU GIÀY TRÊN TUYẾT* · **DẤU VẾT HIỆN TRƯỜNG** | — | | |",

    "| 2-23 | `2.08#8`–`#9` | D | T1 | `t2_house_missing_dawn` | *THỊ TRẤN TWEED* · **KHÔNG MỘT VỤ NÀO TỪNG ĐƯỢC TRÌNH BÁO** → `#9`: *Cho đến khi cảnh sát gõ cửa* | — | | |":
    "| 2-23 | `2.08#7` | D | T1 | `t2_house_missing_dawn` | *CHIẾC CHÌA KHÓA DUY NHẤT* · **KHO BẰNG CHỨNG BÍ MẬT** | — | | |",

    # Hồi 4: 4.05
    "| 4-05 | `4.05#1`–`#2` | H | T1 | `t2_tape_recorder`, `push` | **MỘT TRONG NHỮNG CUỘC THẨM VẤN KINH ĐIỂN NHẤT** → `#2`: *LẮNG NGHE:* **MỘT NGƯỜI THEO DÕI VỤ ÁN** | — | →N2 | |":
    "| 4-05 | `4.05#1` | H | T1 | `t2_tape_recorder`, `push` | **MỘT TRONG NHỮNG CUỘC THẨM VẤN KINH ĐIỂN NHẤT** · *LẮNG NGHE:* **KÝ ỨC CỦA NGƯỜI DÂN** | — | →N2 | |",

    # Hồi 4: 4.06
    "| 4-06 | `4.06#1` | N2 | T4 lời kể | `t2_interrogation_empty` | “…một sĩ quan cấp cao như Đại tá Williams hẳn phải biết rõ quyền của mình.” | — | ✦ Mèo | |":
    "| 4-06 | `4.06#1`–`#2` | N2 | T4 lời kể | `t2_house_missing_dawn` | “…thị trấn nhỏ Tweed của chúng tôi sống trong một nỗi bất an mơ hồ…” | — | ✦ Mèo | |",

    "| 4-07 | `4.06#2`–`#3` | N2 | T4 lời kể | `t2_interrogation_early` | “…tự miệng thú nhận toàn bộ chỉ sau vài tiếng đồng hồ?” | — | ✦ Mèo | |":
    "| 4-07 | `4.06#3`–`#4` | N2 | T4 lời kể | `t2_bedroom_intruder` | “…kẻ đội lốt sĩ quan đứng ngay trong bóng tối, nhìn chằm chằm vào bạn.” | — | ✦ Mèo | |",

    # Hồi 4: 4.10
    "| 4-20 | `4.10#9` | D | T4 `hero` | `t2_forest_map` | “Có bản đồ không?” | — | ⊘ | ✂ |":
    "| 4-20 | `4.10#8` | D | T4 `hero` | `t2_forest_map` | “Có bản đồ không?” | — | ⊘ | ✂ |",

    "| 4-21 | `4.10#10` | D | T1 | `t2_interrogation_early` | *Gần sáu tiếng tiếp theo* · **TỪNG VỤ MỘT** | — | | |":
    "| 4-21 | `4.10#9` | D | T1 | `t2_interrogation_early` | *Gần sáu tiếng tiếp theo* · **TỪNG VỤ MỘT** | — | | |",

    # Hồi 4: 4.11
    "| 4-25 | `4.11#8`–`#9` | C | T3 so sánh | `void` | *NHỮNG NỖI LO HẮN NÓI RA* · *Vợ mình · Tác động lên căn cứ* → `#9`: *KHÔNG PHẢI* · **NHỮNG NGƯỜI PHỤ NỮ ĐÃ BỊ HẮN LÀM HẠI** | Cột phải ở `#9` | ⊘ | |":
    "| 4-25 | `4.11#6`–`#7` | C | T3 so sánh | `void` | *NỖI LO VỢ MÌNH VÀ CĂN CỨ* → *KHÔNG PHẢI NỖI ĐAU CỦA NẠN NHÂN* | — | ⊘ | |",

    "| 4-26 | `4.11#10`–`#11` | C | T3 so sánh | `void` | **KHÔNG PHẢI SỰ HỐI HẬN** → `#11`: **LÀ SỰ SỢ HÃI** · *Sợ mất đi hình tượng* | Cột phải ở `#11` | | |":
    "| 4-26 | `4.11#8` | C | T1 | `void` | **KHÔNG PHẢI SỰ ĂN NĂN HỐI LỖI** | — | | |",

    "| 4-27 | `4.11#12` | C | T1 | `t2_head_down` | **MỘT NGƯỜI ĐÀN ÔNG DUY NHẤT** · *Phải đối diện với tất cả những gì mình đã làm* | — | 🅑 | |":
    "| 4-27 | `4.11#9` | C | T1 | `t2_head_down` | **CHIẾC MẶT NẠ DANH DỰ ĐÃ BỊ LỘT BỎ** | — | 🅑 | |",

    # Hồi 4: 4.12
    "| 4-31 | `4.12#5` | H | T1 | `t2_interrogation_early` | *Sau khoảng mười tiếng đồng hồ* · **VỎ BỌC HOÀN HẢO ĐÃ SỤP ĐỔ** | — | | |":
    "| 4-31 | `4.12#4` | H | T1 | `t2_folder_tree` | *Kho dữ liệu trong ổ cứng* · **82 VỤ ĐỘT NHẬP BÍ MẬT** | — | | |",

    "| 4-32 | `4.12#6`–`#7` | H | T1 | `t2_folder_tree` | **CÂU CHUYỆN CHƯA KẾT THÚC** → `#7`: *Kho ảnh và ghi chép hắn tự lưu giữ* | — | | |":
    "| 4-32 | `4.12#5` | H | T5 | `pinboard` | **88** · *88 Cáo buộc hình sự · Một người đàn ông duy nhất* | Số đếm 0 → 88 | | |",

    "| 4-33 | `4.12#8` | H | T5 | `pinboard` | **88** · *82 cáo buộc đột nhập · Tổng cộng 88 cáo buộc · Một người đàn ông duy nhất* | Số đếm 0 → 88 (T5 chỉ hiện một số lớn) | | |":
    "| 4-33 | `4.12#6` | H | T1 | `t2_head_down` | **VỎ BỌC HOÀN MỸ ĐÃ TAN THÀNH MÂY KHÓI** | — | | |",

    # Hồi 5: 5.08
    "| 5-17 | `5.08#1`–`#3` | D | T8 cờ | cờ 3 | *03* · **BÍ MẬT CỰC ĐOAN · THÓI QUEN GIỮ KỶ VẬT** → `#3`: *Một hệ thống ghi chép · Một kho ảnh phân cấp · Những món đồ được cất giấu* | — | hai badge · Sói sáng | |":
    "| 5-17 | `5.08#1` | D | T1 | `t2_folder_tree` | *TÍNH KỶ LUẬT VÀ GHI CHÉP* · **TỰ VIẾT BẢN ÁN CHO CHÍNH MÌNH** | — | | |",

    "| 5-18 | `5.08#4`–`#5` | D | T8 cờ | cờ 4 | *04* · **VỎ BỌC ĐẠO ĐỨC QUÁ HOÀN MỸ** | — | hai badge | |":
    "| 5-18 | `5.08#2` | D | T1 | `void` | **SỰ KIÊU HÃNH CỦA KẺ ÁI KỶ LUÔN ĐỂ LẠI DẤU VẾT** | — | | |",

    "| 5-19 | `5.08#6`–`#7` | D | T8 cờ | đủ 4 cờ | *Sự cầu toàn không phải là dấu hiệu tội phạm* → `#7`: *Đáng chú ý khi đi kèm sự bí mật cực đoan và sự thiếu đồng cảm* | Cờ 4 viền mảnh lại ở `#6` (cân bằng, tránh định kiến) | hai badge | |":
    "| 5-19 | `5.08#3` | D | T1 | `t2_suv_stop` | **KHÔNG MỘT VỎ BỌC NÀO ĐỨNG TRÊN BẰNG CHỨNG HIỆN TRƯỜNG** | — | | |",
}

new_lines = []
replaced = 0
for line in lines:
    matched = False
    for old_row, new_row in replacements.items():
        if line.strip() == old_row.strip():
            new_lines.append(new_row)
            replaced += 1
            matched = True
            break
    if not matched:
        new_lines.append(line)

print(f"Replaced {replaced}/{len(replacements)} shot rows.")
PLAN.write_text("\n".join(new_lines), encoding="utf-8")
