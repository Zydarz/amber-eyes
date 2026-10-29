import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace Hồi 1 shots
old_h1 = """| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t5_wichita_skyline_dusk` | **19 · 03 · 2004** · *Wichita, Kansas · Nước Mỹ* → `#2`: *Tòa soạn báo The Wichita Eagle nhận phong bì màu vàng không người gửi* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T1 | `t5_eagle_newsroom_night` | **BẢN SAO BẰNG LÁI VICKI WEGERLE** · *Cùng ba tấm ảnh hiện trường vụ án xưa cũ* | — | 🅑 | |
| 1-03 | `1.03#4` | H | T2 | `t5_manila_envelope_polaroids` | *CƠN ÁC MỘNG KINH HOÀNG* · **KÝ TÊN B-T-K** · *Vùng Trung Tây nước Mỹ suốt nhiều thập kỷ* | Dấu mộc ở "B-T-K" | 🅑 | |
| 1-04 | `1.03#5` | H | T1 | `t5_btk_signature_letter` | **BA CHỮ CÁI VIẾT TẮT: B-T-K** · *Bind · Torture · Kill* | — | ⊘ | |"""

new_h1 = """| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `t5_wichita_skyline_dusk` | **19 · 03 · 2004** · *Wichita, Kansas · Nước Mỹ* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T1 | `t5_eagle_newsroom_night` | **TÒA SOẠN BÁO THE WICHITA EAGLE** · *Nhận phong bì thư màu vàng không người gửi* | — | 🅑 | |
| 1-03 | `1.03#4` | H | T1 | `t5_manila_envelope_polaroids` | **BẢN SAO BẰNG LÁI VICKI WEGERLE** · *Cùng ba tấm ảnh chụp hiện trường vụ án xưa cũ* | — | 🅑 | |
| 1-04 | `1.03#5` | H | T2 | `t5_btk_signature_letter` | *CƠN ÁC MỘNG VÙNG TRUNG TÂY* · **KÝ TÊN B-T-K** · *Bind · Torture · Kill* | Dấu mộc ở "B-T-K" | ⊘ | |"""

# Replace Hồi 2 shots
old_h2 = """| 2-03 | `2.04#1`–`#3` | D | T8 | `t5_btk_signature_metaphor`, `still` | *KHOA HỌC HÀNH VI FBI · CHỮ KÝ TÂM LÝ ĐẶC TRƯNG* · *Thứ nhất: Nhu cầu áp chế tuyệt đối* · *Dùng dây trói khống chế, tận hưởng nỗi sợ hãi tột cùng* | Lật ảnh hiện trường `2.03` | ✦ Sói | |
| 2-04 | `2.04#4`–`#6` | D | T1 | `t5_trophy_lockbox` | **THỨ HAI: NHU CẦU LƯU GIỮ CHIẾN LỢI PHẨM** · *Lấy đi bằng lái, đồng hồ, trang sức để kích hoạt cảm xúc thống trị* | — | 🅑 | |
| 2-05 | `2.04#7`–`#8` | D | T1 | `t5_public_library_bookshelves` | **THỨ BA: TRUYỀN THÔNG TRÊU NGƯƠI** · *Để lại bưu kiện trong thư viện công cộng, dán dưới gầm bàn* | — | | |
| 2-06 | `2.04#9`–`#10` | D | T1 | `t5_park_trashcan_drop` | **THÙNG RÁC CÔNG VIÊN MÙA ĐÔNG** · *Chứa bài thơ tự sáng tác và câu đố chữ gửi cảnh sát* | — | ⊘ | →H |
| 2-07 | `2.05#1`–`#4` | H | T1 | `t5_gloves_forensic_desk` | **MỘT KẺ SĂN MỒI TỈ MỈ VÀ CỰC KỲ KIÊN NHẪN** · *Nắm rõ kỹ thuật trinh sát, luôn đeo găng tay* → `#3`: *Danh tính thực sự phía sau chiếc mặt nạ* | — | ✦ Cú | →D |
| 2-08 | `2.06#1`–`#2` | D | T1 | `t5_air_force_service_era` | **DENNIS RADER · SINH NĂM 1945** · *Bốn năm Không quân Mỹ · Tốt nghiệp Quản trị tư pháp* | — | ✦ Sói | |
| 2-09 | `2.06#3` | D | T1 | `t5_rader_house_park_city` | **NGÔI NHÀ 6220 INDEPENDENCE TẠI PARK CITY** · *Người vợ hơn 30 năm và hai đứa con ngoan ngoãn* | — | | |
| 2-10 | `2.06#4` | D | T1 | `t5_lutheran_church_exterior` | **CHỦ TỊCH HỘI ĐỒNG NHÀ THỜ LUTHERAN CHÚA KITÔ** · *Tín đồ gương mẫu, thu tiền công đức và tổ chức thiện nguyện* | — | | |
| 2-11 | `2.06#5` | D | T1 | `t5_church_council_altar` | **NGƯỜI ĐỨNG TRƯỚC BỤC GIẢNG NHÀ THỜ** · *Được cả cộng đồng tín hữu kính trọng* | — | | |
| 2-12 | `2.06#6` | D | T1 | `t5_scout_camp_campfire` | **ĐỘI TRƯỞNG HƯỚNG ĐẠO SINH CUB SCOUT** · *Dạy trẻ em thắt dây thừng, dựng lều và rèn luyện trung thực* | — | ⊘ | |
| 2-13 | `2.06#7` | D | T1 | `t5_compliance_measuring_tape`, `push` | **NHÂN VIÊN KIỂM TRA TRẬT TỰ ĐÔ THỊ PARK CITY** · *Cầm thước đo từng bãi cỏ · Nghiêm khắc đến mức hà khắc* | Tiếng thước dây đo cỏ | ⊘ | →H |"""

new_h2 = """| 2-03 | `2.04#1`–`#3` | D | T8 | `t5_btk_signature_metaphor`, `still` | *KHOA HỌC HÀNH VI FBI · CHỮ KÝ TÂM LÝ ĐẶC TRƯNG* · *Thứ nhất: Nhu cầu áp chế tuyệt đối* · *Dùng dây trói khống chế, biến nạn nhân bất lực* | Lật ảnh hiện trường `2.03` | ✦ Sói | |
| 2-04 | `2.04#4`–`#5` | D | T1 | `t5_darkened_house_exterior`, `push` | **ĐỘT NHẬP CẮT DÂY ĐIỆN THOẠI & KHỐNG CHẾ** · *Tận hưởng nỗi sợ hãi tột cùng trong bóng tối* | — | 🅑 | |
| 2-05 | `2.04#6`–`#8` | D | T1 | `t5_trophy_lockbox` | **THỨ HAI: NHU CẦU LƯU GIỮ CHIẾN LỢI PHẨM** · *Lấy đi bằng lái, đồng hồ, trang sức để kích hoạt cảm xúc thống trị* | — | | |
| 2-06 | `2.04#9`–`#10` | D | T1 | `t5_public_library_bookshelves` | **THỨ BA: TRUYỀN THÔNG TRÊU NGƯƠI** · *Bưu kiện giấu trong thư viện công cộng và thùng rác công viên* | — | ⊘ | →H |
| 2-07 | `2.05#1`–`#4` | H | T1 | `t5_gloves_forensic_desk` | **MỘT KẺ SĂN MỒI TỈ MỈ VÀ CỰC KỲ KIÊN NHẪN** · *Nắm rõ kỹ thuật trinh sát, luôn đeo găng tay* → `#3`: *Danh tính thực sự phía sau chiếc mặt nạ* | — | ✦ Cú | →D |
| 2-08 | `2.06#1` | D | T1 | `t5_air_force_service_era` | **DENNIS RADER · SINH NĂM 1945** · *Bốn năm Không quân Mỹ · Tốt nghiệp Quản trị tư pháp* | — | ✦ Sói | |
| 2-09 | `2.06#2` | D | T1 | `t5_rader_house_park_city` | **NGÔI NHÀ 6220 INDEPENDENCE TẠI PARK CITY** · *Người vợ hơn 30 năm và hai đứa con ngoan ngoãn* | — | | |
| 2-10 | `2.06#3` | D | T1 | `t5_lutheran_church_exterior` | **CHỦ TỊCH HỘI ĐỒNG NHÀ THỜ LUTHERAN CHÚA KITÔ** · *Đứng trước bục giảng chào đón tín đồ và làm thiện nguyện* | — | | |
| 2-11 | `2.06#4` | D | T1 | `t5_scout_camp_campfire` | **ĐỘI TRƯỞNG HƯỚNG ĐẠO SINH CUB SCOUT** · *Dạy trẻ em thắt dây thừng, dựng lều và rèn luyện trung thực* | — | ⊘ | |
| 2-12 | `2.06#5`–`#6` | D | T1 | `t5_compliance_truck_street` | **NHÂN VIÊN KIỂM TRA TRẬT TỰ ĐÔ THỊ TỪ NĂM 1991** · *Lái xe bán tải đi đo chiều cao từng bãi cỏ, bắt giữ chó mèo chạy rông* | — | ⊘ | |
| 2-13 | `2.06#7` | D | T1 | `t5_compliance_measuring_tape`, `push` | **TỈ MỈ ĐẾN MỨC BỆNH HOẠN, HÀ KHẮC** · *Không ai ngờ người đàn ông luôn cầm thước đo cỏ lại là con quái vật BTK* | Tiếng thước dây đo cỏ | ⊘ | →H |"""

c_norm = c.replace('\r\n', '\n')
old_h1_norm = old_h1.replace('\r\n', '\n')
new_h1_norm = new_h1.replace('\r\n', '\n')
old_h2_norm = old_h2.replace('\r\n', '\n')
new_h2_norm = new_h2.replace('\r\n', '\n')

if old_h1_norm not in c_norm:
    print("ERROR: old_h1_norm not found!")
    sys.exit(1)
if old_h2_norm not in c_norm:
    print("ERROR: old_h2_norm not found!")
    sys.exit(1)

c_norm = c_norm.replace(old_h1_norm, new_h1_norm).replace(old_h2_norm, new_h2_norm)

with open('02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md', 'w', encoding='utf-8') as f:
    f.write(c_norm)

print("SUCCESS: Updated KeHoach_Video_Tap05.md with corrected shots!")
