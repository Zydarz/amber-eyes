import os

episodes_info = [
    (30, 'Chris Watts', 'CHRIS WATTS', 'Chiếc Mặt Nạ Người Chồng Mẫu Mực & Hội Chứng Hủy Diệt Gia Đình',
     'Vụ thảm án gia đình Watts tại Frederick, Colorado (Tháng 8/2018)',
     'Hội chứng Kẻ hủy diệt gia đình (Self-Preserving Annihilator), Ái kỷ kín đáo, Phân ngăn tâm trí bệnh lý.'),
    (31, 'Ted Kaczynski (Unabomber)', 'TED KACZYNSKI', 'Cơn Cuồng Nộ Trí Thức & Bước Đột Phá Của Giám Định Ngôn Ngữ Học Pháp Y',
     'Giáo sư toán học Harvard sống ẩn dật gửi 16 bom thư phản đối văn minh công nghệ (1978-1995)',
     'Giám định ngôn ngữ học pháp y (Forensic Linguistics), Hoang tưởng cứu thế, Sự tự cô lập cực đoan.'),
    (32, 'Ted Bundy', 'TED BUNDY', 'Cái Bẫy Của Lòng Trắc Ẩn & Ảo Tưởng Kiểm Soát Tuyệt Đối',
     'Sát nhân hàng loạt điển trai sát hại hơn 30 phụ nữ khắp nước Mỹ thập niên 1970',
     'Hiệu ứng hào quang (Halo Effect), Khai thác lòng trắc ẩn, Ảo tưởng chiếm đoạt tuyệt đối.'),
    (33, 'Aileen Wuornos', 'AILEEN WUORNOS', 'Chấn Thương Gắn Bó Sâu Sắc & Vòng Xoáy Bạo Lực Phòng Vệ',
     'Nữ sát nhân hàng loạt hạ sát 7 người đàn ông dọc các tuyến quốc lộ Florida (1989-1990)',
     'Rối loạn nhân cách ranh giới (BPD), Sang chấn gắn bó tuổi thơ, Cơ chế phòng vệ quá khích.'),
    (34, 'Nguyễn Đức Nghĩa', 'NGUYỄN ĐỨC NGHĨA', 'Vỏ Bọc Sinh Viên Ưu Tú & Sự Tê Liệt Cảm Xúc Sau Chiếc Kính Cận',
     'Án mạng tại chung cư G4 Trung Hòa - Cầu Giấy, Hà Nội gây rúng động năm 2010',
     'Hiệu ứng hào quang tri thức, Cơ chế phân ngăn tâm trí, Che giấu nhận dạng có tính toán.'),
    (35, 'Nguyễn Đức Anh', 'NGUYỄN ĐỨC ANH', 'Tâm Lý Học Cuồng Yêu Hóa Sát Nhân & Cơn Cuồng Nộ Chuyển Hướng',
     'Thảm án tại xã Bình Minh, Đồng Nai rạng sáng 3/9/2026 sau khi bị bạn gái chia tay',
     'Tổn thương ái kỷ (Narcissistic Injury), Hung hăng chuyển hướng (Displaced Aggression).'),
    (36, 'Kip Kinkel', 'KIP KINKEL', 'Tiếng Nói Trong Tâm Trí & Bi Kịch Ảo Giác Tuổi Vị Thành Niên',
     'Thiếu niên 15 tuổi sát hại cha mẹ rồi xả súng tại trường trung học Springfield, Oregon năm 1998',
     'Khởi phát tâm thần phân liệt sớm, Ảo giác thính giác mệnh lệnh, Điểm mù gia đình.'),
    (37, 'Dr. Harold Shipman', 'DR. HAROLD SHIPMAN', 'Thiên Thần Tử Thần & Phức Cảm Thượng Đế Y Khoa',
     'Bác sĩ gia đình uy tín tại Anh sát hại hơn 215 bệnh nhân lớn tuổi suốt 24 năm',
     'Phức cảm Thượng đế (God Complex), Lạm dụng lòng tin áo trắng, Kiểm toán hồ sơ bệnh án.'),
    (38, 'Natascha Kampusch & Přiklopil', 'NATASCHA KAMPUSCH', '3.096 Ngày Dưới Lòng Đất & Ý Chí Sinh Tồn Đánh Bại Thao Túng',
     'Cô bé 10 tuổi bị bắt cóc giam cầm 8 năm dưới hầm ngầm ngoại ô Vienna, Áo (1998-2006)',
     'Giải mã Hội chứng Stockholm, Liên kết sang chấn (Traumatic Bonding), Ý chí sinh tồn.'),
    (39, 'Joanna Dennehy', 'JOANNA DENNEHY', 'Nữ Sát Nhân Peterborough & Cơn Nghiện Bạo Lực Thuần Túy',
     'Nữ sát nhân psychopathy sát hại 3 người đàn ông trong 10 ngày để giải tỏa buồn chán',
     'Psychopathy nữ, Bạo dâm (Sadomasochism), Đảo ngược vai trò giới trong bạo lực săn mồi.'),
    (40, 'Patrice Alègre', 'PATRICE ALÈGRE', 'Bóng Đen Toulouse & Cuộc Cách Mạng Hồ Sơ Hành Vi Tại Pháp',
     'Chuỗi tội ác kéo dài cả thập kỷ tại Toulouse thúc đẩy thành lập đơn vị BAU của Hiến binh Pháp',
     'Chuyển dịch phương thức hành động (MO), Sự ra đời của Đơn vị phân tích hành vi.'),
    (41, 'Quái Vật Florence', 'QUÁI VẬT FLORENCE', 'Cơn Ác Mộng Đồi Tuscany & Phân Tích Địa Lý Hành Vi',
     '8 vụ sát hại các cặp tình nhân nơi vắng vẻ quanh vùng Florence, Ý suốt 17 năm (1968-1985)',
     'Định vị địa lý hành vi (Geographic Profiling), Chữ ký đêm không trăng, Mặc cảm bất lực.'),
    (42, 'Marc Dutroux', 'MARC DUTROUX', 'Ngôi Nhà Nỗi Sợ Marcinelle & Sự Phản Kháng Của Lương Tri Xã Hội',
     'Vụ án chấn động nước Bỉ dẫn tới cuộc diễu hành Bạch hành của 300.000 người dân',
     'Kiểm soát độc hại vợ chồng, Thức tỉnh lương tri xã hội trước lỗ hổng tư pháp.'),
    (43, 'Peter Kürten', 'PETER KÜRTEN', 'Thời Kỳ Weimar & Nguồn Cội Phân Tâm Học Tội Phạm',
     'Quái vật Düsseldorf năm 1929 tại Đức, đối tượng nghiên cứu kinh điển của tâm thần học',
     'Nguồn cội phân tâm học tội phạm, Thỏa mãn từ nỗi sợ đám đông, Nghiên cứu Carl Jung.'),
    (44, 'Bóng Ma Heilbronn', 'BÓNG MA HEILBRONN', 'Hồ Sơ Sát Nhân Vô Hình & Bài Học Về Ô Nhiễm Mẫu ADN',
     'Cuộc truy lùng nữ sát thủ vô hình để lại ADN tại 40 hiện trường ở Đức, Áo, Pháp',
     'Thiên kiến xác nhận (Confirmation Bias) trong điều tra, Bài học ô nhiễm vật chứng pháp y.'),
    (45, 'Moses Sithole', 'MOSES SITHOLE', 'Cái Bẫy Tuyển Dụng Hậu Apartheid & Nữ Profiler Tiên Phong',
     'Sát nhân ABC sát hại 37 phụ nữ tìm việc làm tại Nam Phi năm 1994-1995',
     'Đấu trí với Tiến sĩ Micki Pistorius (nữ profiler đầu tiên của Nam Phi).'),
    (46, 'Rosemary Ndlovu', 'ROSEMARY NDLOVU', 'NỮ CẢNH SÁT LÒNG THAM & BẢN HỢP ĐỒNG BẢO HIỂM ĐẪM MÁU',
     'Nữ cảnh sát tại Tembisa sát hại người thân trục lợi tiền bảo hiểm nhân thọ',
     'Tha hóa quyền lực hành pháp, Coi người thân là công cụ tài chính, Diễn xuất vô cảm.'),
    (47, 'Cedric Maake', 'CEDRIC MAAKE', 'Hội Chứng Tắc Kè Hoa & Bước Chuyển Phương Thức Hành Động',
     'Sát nhân Wemmer Pan tại Johannesburg liên tục thay đổi hung khí và đối tượng',
     'Phân biệt giữa Phương thức hành động (MO) biến đổi và Chữ ký tâm lý (Signature).'),
    (48, 'Suzane von Richthofen', 'SUZANE VON RICHTHOFEN', 'Nghịch Tử Dinh Thự Sao Paulo & Màn Kịch Đẫm Nước Mắt',
     'Nữ sinh luật 18 tuổi cùng bạn trai sát hại cha mẹ ruột để chiếm đoạt gia tài thừa kế',
     'Nổi loạn ái kỷ thượng lưu, Màn kịch giả vờ đau đớn tại đám tang, Thao túng đồng phạm.'),
    (49, 'Pedro López', 'PEDRO LÓPEZ', 'Vết Rạn Thời Kỳ La Violencia & Sự Thao Túng Biên Giới',
     'Quái vật Andes gây tội ác xuyên quốc gia tại Colombia, Peru và Ecuador',
     'Chấn thương tâm lý từ thời kỳ nội chiến, Khai thác điểm mù của các bộ tộc bản địa.'),
    (50, 'Bộ Ba Garanhuns', 'BỘ BA GARANHUNS', 'Ảo Tưởng Tẩy Rửa Dân Số & Thảm Kịch Cuồng Giáo Gia Đình',
     'Giáo phái thanh trừng thu nhỏ gồm 3 người tại Brazil thao túng và sát hại nạn nhân',
     'Loạn thần chia sẻ 3 người (Folie à Trois), Ảo tưởng cứu rỗi dị giáo, Thao túng nội bộ.'),
    (51, 'Juana Barraza', 'JUANA BARRAZA', 'Nữ Đấu Sĩ Lucha Libre & Mối Thù Oán Với Người Mẹ',
     'Nữ đô vật tại Mexico City đóng giả nhân viên y tế sát hại hàng chục cụ bà neo đơn',
     'Phóng chiếu (Projection) mối hận thù người mẹ nghiện ngập lên các phụ nữ cao tuổi.'),
    (52, 'Gia Đình Setagaya', 'GIA ĐÌNH SETAGAYA', 'Bí Ẩn Đêm Giao Thừa & Hành Vi Kỳ Dị Của Kẻ Xâm Nhập',
     '4 thành viên gia đình Miyazawa bị sát hại tại Tokyo đêm 30/12/2000',
     'Hành vi lưu trú tại hiện trường (Resident Behavior), Đóng băng cảm xúc, Kỳ án bế tắc.'),
    (53, 'Tsutomu Miyazaki', 'TSUTOMU MIYAZAKI', 'Căn Phòng 5.000 Cuốn Băng & Vực Thẳm Tách Rời Thực Tại',
     'Sát nhân Otaku bắt cóc 4 bé gái gây chấn động dư luận Nhật Bản năm 1988-1989',
     'Mặc cảm khiếm khuyết cơ thể, Hikikomori thoái lui xã hội, Ranh giới thực - ảo.'),
    (54, 'Thùng Xi Măng Tân Trang', 'THÙNG XI MĂNG TÂN TRANG', 'Thù Hận Tích Tụ Dưới Mái Nhà & Ngôi Mộ Trong Phòng Ngủ',
     'Mâu thuẫn nhà ở thừa kế tại Đài Loan năm 2018, chị dâu sát hại em chồng đắp xi măng',
     'Bùng nổ hung hăng thụ động (Passive-Aggressive), Cơ chế chối bỏ thực tại (Denial).'),
    (55, 'Adrian Lim', 'ADRIAN LIM', 'Gã Thầy Pháp Toa Payoh & Vi Mô Cuồng Giáo Giữa Chung Cư HDB',
     'Thầy trừ tà thao túng hai người vợ gây tội ác tại khu nhà ở xã hội Singapore năm 1981',
     'Cấu trúc vi mô cuồng giáo (Micro-Cult Dynamics), Tẩy não bằng sợ hãi và niềm tin lệch lạc.'),
    (56, 'Mona Fandey', 'MONA FANDEY', 'Nụ Cười Bí Ẩn Dưới Giá Treo Cổ & Vở Kịch Quyền Lực Đen Tối',
     'Cựu ca sĩ pop chuyển sang làm phù thủy sát hại chính khách bang Pahang, Malaysia năm 1993',
     'Ái kỷ kịch nghệ (Histrionic Narcissism), Lợi dụng bùa chú thao túng chính trị gia.'),
    (57, 'Charles Sobhraj', 'CHARLES SOBHRAJ', 'Bóng Ma Tuyến Đường Hippie Trail & Bậc Thầy Thao Túng',
     'Kẻ sát nhân chuốc thuốc cướp tài sản của du khách dọc Đông Nam Á thập niên 1970',
     'Nhân cách chống đối xã hội thể ký sinh (Parasitic Psychopathy), Thao túng lòng tin.'),
    (58, 'Thảm Án Snowtown', 'THẢM ÁN SNOWTOWN', 'Những Chiếc Thùng Axit & Kẻ Thao Túng Lòng Thù Hận',
     'Vụ án giết người giấu trong hầm ngân hàng bỏ hoang tại Nam Úc thập niên 1990',
     'Thủ lĩnh độc tài thao túng tâm lý, Loạn thần chia sẻ (Folie à Plusieurs), Ngụy biện.'),
    (59, 'David Bain', 'DAVID BAIN', 'Giai Điệu Buổi Bình Minh Đẫm Máu & Cuộc Chiến Pháp Đình Lịch Sử',
     '5 thành viên gia đình Bain tại Dunedin, New Zealand bị sát hại sáng sớm năm 1994',
     'Hiện trường nội bộ gia đình, Chứng mất trí nhớ phân ly (Dissociative Amnesia).')
]

for ep, name, short_name, title, brief, psy in episodes_info:
    dir_vn = f'02_SAN_XUAT/Ho_So_Toi_Pham/Tap{ep:02d}'
    os.makedirs(f'{dir_vn}/xuat_ban', exist_ok=True)
    
    kh_content = f"""# HỒ SƠ SẢN XUẤT TẬP {ep:02d} · "{short_name}" (PHẦN B)

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A).
**Kịch bản gốc:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap{ep:02d}/kichban_tap{ep:02d}_19112026.md`
**Thành phẩm xuất bản:** `02_SAN_XUAT/Ho_So_Toi_Pham/Tap{ep:02d}/xuat_ban/`

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| **Tên tập** | Tập {ep:02d}: Hồ Sơ {name} — {title} |
| **Đề tài** | {brief} |
| **Trọng tâm tâm lý (K10)** | {psy} |
| **Thời lượng dự kiến** | 24:00 – 27:00 (~1.500 giây) |
| **Giọng đọc phân bổ** | Host (Cú) · Điều tra viên (Sói) · Chuyên gia tâm lý (Cáo) · Người trong cuộc (N) |
| **Quy tắc kiểm duyệt** | 100% YouTube Safe theo Tiêu chuẩn V9 (Không mô tả bạo lực ghê rợn, tập trung tâm lý học và hành vi). |

## B2. Kế hoạch sản xuất chi tiết 5 Hồi

* **Hồi 1:** Khởi nguồn vụ việc, tín hiệu cảnh báo ban đầu và sự vào cuộc của cơ quan chức năng.
* **Hồi 2:** Bóc tách vỏ bọc ngụy trang, cuộc sống đời thường và cơ chế phân ngăn tâm trí bệnh lý.
* **Hồi 3:** Cuộc đấu trí trong phòng thẩm vấn, phân tích vi biểu cảm và sự sụp đổ của các lời khai ngụy biện.
* **Hồi 4:** Khoa học hình sự, phân tích dấu vết vi mô, dữ liệu công nghệ và bước ngoặt phá án.
* **Hồi 5:** Bản án nghiêm minh của tòa án và 3 bài học cảnh báo đỏ sinh tồn đắt giá cho cộng đồng.

## B3. Trạng thái các bước kỹ thuật (Checklist)

- [x] Kịch bản Tiếng Việt (01_KICH_BAN/Ho_So_Toi_Pham/Tap{ep:02d}/)
- [x] Kịch bản Tiếng Anh (01_KICH_BAN/Ho_So_Toi_Pham/Tap{ep:02d}_EN/)
- [x] Kịch bản Tiếng Nhật (01_KICH_BAN/Ho_So_Toi_Pham/Tap{ep:02d}_JA/)
- [x] Kịch bản Tiếng Hàn (01_KICH_BAN/Ho_So_Toi_Pham/Tap{ep:02d}_KO/)
- [ ] Tách câu (`parse_kichban.py`)
- [ ] Diễn xuất & sinh audio TTS (`tts_sentences.py`)
- [ ] QC âm thanh, nhịp nghỉ, LUFS (`qc_pause_gate.py`, `build_audio3.py`)
- [ ] Bảng shot hình ảnh (`parse_shots.py`)
- [ ] Render video hoàn thiện (`build_video3.py`)
- [ ] Đóng gói xuất bản (`package.py --mux`)
"""
    with open(f'{dir_vn}/KeHoach_Video_Tap{ep:02d}.md', 'w', encoding='utf-8') as f:
        f.write(kh_content)
        
    mota_content = f"""HỒ SƠ TÂM LÝ TỘI PHẠM — TẬP {ep:02d}: {name.upper()}
{title}

📌 Nội dung tập phim:
{brief}
Phân tích chuyên sâu dưới lăng kính tâm lý học tội phạm & khoa học hành vi:
- {psy}

⏱️ Mốc thời gian (Timestamps):
00:00 - Hồi 1: Khởi nguồn cơn ác mộng & Tiếng chuông báo động
05:30 - Hồi 2: Vỏ bọc ngụy trang & Dấu vết hành vi ngầm
10:30 - Hồi 3: Cuộc đấu trí trong phòng thẩm vấn
16:00 - Hồi 4: Khoa học hình sự & Ánh sáng công lý
21:00 - Hồi 5: Bản án cuối cùng & Bài học cảnh báo đỏ sinh tồn

🔔 Đăng ký kênh Amber Eyes để theo dõi những hồ sơ tâm lý học tội phạm kinh điển được giải mã khoa học và sâu sắc nhất!
#AmberEyes #TamLyHocToiPham #HoSoVuAn #{short_name.replace(" ", "")}
"""
    with open(f'{dir_vn}/mo_ta.txt', 'w', encoding='utf-8') as f:
        f.write(mota_content)

    for lang in ['EN', 'JA', 'KO']:
        dir_lang = f'02_SAN_XUAT/Ho_So_Toi_Pham/Tap{ep:02d}_{lang}'
        os.makedirs(f'{dir_lang}/xuat_ban', exist_ok=True)
        with open(f'{dir_lang}/Production_Plan_Tap{ep:02d}_{lang}.md', 'w', encoding='utf-8') as f:
            f.write(f"# PRODUCTION PLAN EPISODE {ep:02d} ({lang})\n\nCase: {name}\nStandard: Amber Eyes 4-Language Pipeline\nStatus: Script Ready -> Pending Audio Synthesis & Video Assembly.\n")
        with open(f'{dir_lang}/description_{lang}.txt', 'w', encoding='utf-8') as f:
            f.write(f"AMBER EYES CASE FILE {ep:02d} [{lang}] — {name}\n\nForensic and behavioral psychology documentary.\n")

print("Finished generating dossiers for all 30 episodes in 02_SAN_XUAT.")
