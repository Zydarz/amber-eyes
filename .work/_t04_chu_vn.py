#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — CHỮ TRÊN HÌNH bản tiếng Việt cho bảng shot mới (kịch bản v4).

Mỗi mục: shot_id -> chuỗi cột "Chữ".
Quy ước (giữ nguyên với pipeline):
  * **đậm** = tiêu đề lớn   ·  *nghiêng* = phụ đề   ·  “trích dẫn” = nguyên văn
  * `→ `#N`: ...`  = đổi khối chữ khi shot tới câu #N của ELEMENT (N là số thứ tự câu
    trong element, KHÔNG phải trong shot — renderer tìm id kết thúc bằng "#N")
  * Mọi mảnh chữ phải là chuỗi từ LIÊN TÚC có trong câu đang đọc của shot (H6/V3)
  * Mọi con số trên hình phải có trong câu (H6/V3)
"""
import json

CHU_VN = {
    # ---------------- HỒI 1
    "1-01": "**MÙA THU NĂM 2003** · *Trung tâm Y tế Somerset* → `#2`: *Thị trấn Somerville · Bang New Jersey*",
    "1-02": "**NGƯỜI ĐÀN ÔNG 43 TUỔI** · *Dáng người gầy gò · Giọng nói nhỏ nhẹ* → *Sẵn sàng nhận làm thay ca trực*",
    "1-03": "**CHIẾC ÁO BLOUSE TRẮNG TINH TƯƠM** · *Tạo nên một “Hiệu ứng Hào quang”* → *Che giấu một vực thẳm tâm lý đen tối*",
    "1-05": "*MÔI TRƯỜNG Y TẾ ĐẦY ÁP LỰC* · **RANH GIỚI GIỮA SỰ SỐNG VÀ SỰ RA ĐI** · *Một chỗ dựa đáng tin cậy*",
    "1-06": "**NGƯỜI ĐẦU TIÊN CHẠY ĐẾN PHỤ GIÚP** · *Lặng lẽ ở lại dọn dẹp phòng bệnh* → `#3`: *Một người bạn hiền lành · Một người cha trầm lặng*",
    "1-07": "“Trong mắt tất cả y tá chúng tôi tại bệnh viện Somerset, Charlie là một người bạn tuyệt vời.” → `#2`: “Anh ấy chu đáo, không bao giờ cáu gắt và luôn chăm sóc người bệnh vô cùng ân cần.”",
    "1-08": "“Không một ai trong bệnh viện có thể mảy may nghi ngờ một người đồng nghiệp hiền lành và tận tụy đến như thế.” → `#5`: “Cho đến khi sự thật vỡ lở, tất cả chúng tôi đều lạnh sống lưng vì nhận ra mình đã cùng làm việc bên cạnh một kẻ sát nhân hàng loạt nguy hiểm nhất.”",
    "1-09": "**MỘT BÓNG MA TỬ THẦN** · *Gieo rắc bi kịch qua từng hành lang bệnh viện* → `#2`: *Linh mục Florian Gall · 68 tuổi*",
    "1-10": "**TIẾN TRIỂN RẤT KHẢ QUAN** → `#4`: **RƠI VÀO CƠN LOẠN NHỊP KỊCH PHÁT RỒI TRỤY TIM** → `#5`: *Chiến đấu suốt nhiều giờ nhưng không thể đảo ngược tình thế*",
    "1-11": "**MỘT SỰ RA ĐI ĐẦY BẤT THƯỜNG** · *Gia đình và các đồng nghiệp bàng hoàng nghi vấn*",
    "1-12": "*XÉT NGHIỆM ĐỘC CHẤT HỌC PHÁP Y* · **NỒNG ĐỘ DIGOXIN CỰC CAO** · *Cao gấp hàng chục lần ngưỡng an toàn cho phép*",
    "1-13": "**BỊ BÓP NGHẸT BỞI MỘT LIỀU ĐỘC DƯỢC NHÂN TẠO** → `#4`: **CẢNH BÁO KHẨN CẤP TỚI BAN GIÁM ĐỐC BỆNH VIỆN** → `#5`: *Chọn cách trì hoãn và giữ kín sự việc*",
    "1-15": "*QUY MÔ CHẤN ĐỘNG* · **ĐIỀU TRA VIÊN CHUYÊN ÁN** → `#2`: *Những con số nằm sâu trong bóng tối*",
    "1-16": "**LỊCH SỬ CÔNG TÁC CỦA CHARLES CULLEN** · *Một bức tranh kinh hoàng* → `#2`: *Không phải là hiện trường đầu tiên*",
    "1-17": "*16 NĂM* · *9 BỆNH VIỆN VÀ 1 VIỆN DƯỠNG LÃO* → `#4`: *Ngưng tim đột ngột vào ca trực đêm đều tăng vọt*",
    "1-18": "**CULLEN THỪA NHẬN** · *Khoảng 40 bệnh nhân* · *Cơ quan công tố xác nhận 29 nạn nhân* → `#7`: **CON SỐ THỰC TẾ CÓ THỂ LÊN TỚI 400 NẠN NHÂN** → `#8`: *Kẻ giết người hàng loạt tàn khốc nhất*",
    "1-19": "**THIÊN THẦN TỬ THẦN** · *“Phức cảm Chúa trời”* · *Kỹ thuật trung hòa đạo đức*",
    "1-20": "**SỰ IM LẶNG ĐỒNG LÕA CỦA CHÍN BỆNH VIỆN** · *Sợ kiện tụng và trách nhiệm pháp lý* → `#5`: *Bài học đắt giá về sự bất an tập thể*",
    # ---------------- HỒI 2
    "2-01": "**HIỆN TRƯỜNG CỦA CHARLES CULLEN** · *Những căn phòng điều trị vô trùng* → `#3`: **CHÍNH NHỮNG ỐNG THUỐC CỨU NGƯỜI**",
    "2-02": "*MỘT TẤM BÌNH PHONG CHE MẮT* · **HỆ THỐNG GIÁM SÁT SUỐT 16 NĂM**",
    "2-04": "**KHAI THÁC TRIỆT ĐỂ NHỮNG KẼ HỞ** · *Quản lý kỹ thuật số thời kỳ đầu* · *Chiếc máy cấp phát thuốc tự động* → `#3`: *Quỹ đạo leo thang hành vi của kẻ thủ ác*",
    "2-05": "**TỦ CẤP PHÁT THUỐC TỰ ĐỘNG PYXIS MEDSTATION** · *Mỗi y tá phải dùng mã số cá nhân để đăng nhập* → `#3`: **MỘT LỖ HỔNG NGHIÊM TRỌNG TRONG THIẾT KẾ PHẦN MỀM**",
    "2-06": "**NHẬP LỆNH YÊU CẦU** · *Thuốc độc bảng A* · *Digoxin, Insulin hay Norepinephrine* → `#5`: **VIÊN THUỐC ĐỘC** · *Nằm gọn trong túi áo của Cullen* → `#6`: *Bốn nấc thang leo thang hành vi điển hình*",
    "2-07": "**NẤC THANG THỨ NHẤT** · *Khủng hoảng nội tâm và trộm thuốc*",
    "2-08": "*Trầm cảm nặng nề · Tự hủy hoại bản thân* → `#9`: **NẤC THANG THỨ HAI** · *Bệnh nhân hấp hối* → `#10`: *Năm 1988 tại Trung tâm Y tế Saint Barnabas*",
    "2-09": "**NẤC THANG THỨ BA** · *Ngẫu nhiên các túi dịch truyền*",
    "2-10": "*Lén tiêm Insulin và Digoxin vào các túi nước muối sinh lý* → `#13`: **NẤC THANG THỨ TƯ: GIẾT NGƯỜI HÀNG LOẠT MẤT KIỂM SOÁT** → `#14`: *Cả những bệnh nhân trẻ tuổi đang bình phục khỏe mạnh*",
    "2-11": "**MỘT CỖ MÁY HỦY DIỆT KHÔNG THỂ DỪNG LẠI**",
    "2-12": "**MỘT SỰ BẤT ĐỐI XỨNG QUYỀN LỰC** · *Sinh mệnh yếu ớt nhất, bị gắn chặt vào dây truyền dịch* → `#3`: *Tin tưởng tuyệt đối vào người y tá đứng bên cạnh*",
    "2-13": "**LINH MỤC FLORIAN GALL** · *Michael Strenko mới 21 tuổi* → `#5`: **SỰ PHẢN BỘI NIỀM TIN Y ĐỨC KINH HOÀNG NHẤT**",
    "2-14": "*KHOA HỌC HÀNH VI* · **PHƯƠNG THỨC GÂY ÁN** · *Chữ ký tâm lý của Charles Cullen*",
    "2-15": "*Tinh vi hóa qua từng năm tháng để thích ứng với quy chế kiểm tra* → `#5`: **CHỮ KÝ TÂM LÝ** · *“Phức cảm Chúa trời”* → `#6`: *Không lấy cắp thuốc để bán kiếm tiền*",
    "2-16": "**BÁO ĐỘNG KHẨN CẤP CODE BLUE** · *Tận hưởng cảm giác toàn năng*",
    "2-17": "**CHIẾC BẪY TÂM LÝ NGUY HIỂM NHẤT** · *Biến những bệnh nhân vô tội thành công cụ thỏa mãn bản năng* → `#3`: *Cơ chế vật hóa nạn nhân và sự tê liệt cảm xúc*",
    "2-18": "*TÂM LÝ HỌC HÀNH VI* · **CƠ CHẾ “VẬT HÓA” VÀ PHI NHÂN HÓA NẠN NHÂN** · *Bệnh nhân bị giáng cấp thành những “đạo cụ sống”*",
    "2-19": "**KHIẾM KHUYẾT NGHIÊM TRỌNG VỀ THẤU CẢM CẢM XÚC** · *Trơ lỳ trước nỗi đau đớn* → `#6`: **MỘT CƠN KHOÁI CẢM QUYỀN LỰC CỰC KỲ ĐỘC HẠI**",
    "2-20": "**ĐỨNG TRÊN CẢ Y HỌC VÀ SỐ PHẬN** · *Quyền quyết định ai được thở và ai phải dừng lại* → `#8`: *Tìm kiếm những nạn nhân mới*",
    "2-21": "**CHIẾC ÁO BLOUSE TRẮNG** · *Công cụ để hợp thức hóa sự tha hóa nhân cách* → `#10`: **MỘT VŨ KHÍ HỦY DIỆT LẠNH LÙNG NHẤT**",
    # ---------------- HỒI 3
    "3-01": "**TẦNG SÂU U TỐI NHẤT TRONG BỘ NÃO** · *Một thiếu niên nhút nhát* → `#3`: *Hắn ra tay vì lòng thương cảm*",
    "3-02": "**CHÂN DUNG CỦA MỘT VỊ THIÊN THẦN** · *Ban phát cái chết êm dịu* → `#5`: **BẰNG CHỨNG KHÁCH QUAN** · *Vạch trần một sự thật hoàn toàn trái ngược* → `#6`: *Chuyên gia tâm lý giải phẫu những sang chấn nguồn cội*",
    "3-03": "**MỘT TUỔI THƠ NGẬP TRÀN BÓNG TỐI** · *Hồ sơ tâm lý pháp y* → `#2`: *Mồ côi cha khi mới chỉ được bảy tháng tuổi* → `#3`: *Bị bạn bè bắt nạt tàn nhẫn*",
    "3-04": "**BIẾN CỐ MANG TÍNH BƯỚC NGOẶT** · *Năm hắn 17 tuổi* · *Người mẹ thân yêu qua đời trong một vụ tai nạn giao thông* → `#5`: *Đã tự ý hỏa táng mà không hề thông báo*",
    "3-05": "**MỐI THÙ HẰN ÂM Ỉ ĐỐI VỚI CÁC THỂ CHẾ Y TẾ** · *Tước đi điểm tựa tình cảm duy nhất* → `#7`: *Trầm cảm nặng và nhiều lần mưu toan tự sát bất thành* → `#8`: *Không phải là con đường tìm kiếm sự cứu rỗi*",
    "3-07": "**MỘT NGƯỜI MANG ĐẦY NHỮNG TỔN THƯƠNG TÂM LÝ** · *Hắn kết hôn, có hai người con gái, hiến thận cứu người* → `#3`: *Cơ chế phân mảnh tâm trí* · *Che giấu con quái vật bên trong mình*",
    "3-08": "**CƠ CHẾ PHÒNG VỆ CỰC ĐOAN** · *“Chia ngăn tâm lý”* → `#2`: *Hai ngăn kéo hoàn toàn độc lập* → `#3`: *Một người cha dịu dàng, một người bạn tận tụy*",
    "3-09": "**“LÁ CHẮN BÌNH THƯỜNG HÓA”** · *Hành vi thiện nguyện và sự tận tụy ban ngày* → `#5`: **MỞ KHÓA BẢN NĂNG HỦY DIỆT** → `#6`: *Không thể che giấu được những người ở cự ly gần nhất*",
    "3-10": "**ADRIENNE BAUM** · *Vợ cũ của hắn* · *Nhận ra những dấu hiệu tâm thần bất ổn* → `#8`: *Xin lệnh cách ly và ly hôn vào năm 1993*",
    "3-11": "**SỰ RẠN NỨT SÂU SẮC TRONG NHÂN CÁCH** · *Một kẻ sát nhân có học thức* → `#2`: *Vô hiệu hóa cảm giác tội lỗi và ngủ ngon sau mỗi ca trực* → `#3`: *Kỹ thuật trung hòa đạo đức trong hành vi phạm tội*",
    "3-12": "*LÝ THUYẾT CỦA SYKES VÀ MATZA* · **KỸ THUẬT TRUNG HÒA ĐẠO ĐỨC** → `#2`: **“PHỦ NHẬN TỔN HẠI”** → `#3`: *“Ngoại hóa trách nhiệm”*",
    "3-13": "*ĐỔ LỖI CHO BAN GIÁM ĐỐC BỆNH VIỆN* → `#5`: **“KẾT ÁN NHỮNG KẺ KẾT ÁN”** · *Chỉ trích hệ thống y tế là đạo đức giả*",
    "3-14": "**BIẾN MÌNH THÀNH NẠN NHÂN CỦA HOÀN CẢNH** · *Cơ chế phán xét đạo đức bên trong tâm trí* → `#8`: **SỰ SỤP ĐỔ TOÀN DIỆN CỦA NHÂN TÍNH**",
    "3-15": "**CON QUỶ DỮ TRONG HẮN SUỐT 16 NĂM**",
    "3-16": "**MỘT HỆ THỐNG TỰ BÀO CHỮA HOÀN HẢO** · *Quyền quyết định số phận của đồng loại* → `#3`: **LÒNG DŨNG CẢM CỦA MỘT NGƯỜI PHỤ NỮ**",
    # ---------------- HỒI 4
    "4-01": "**THÁNG 10 NĂM 2003** · *Văn phòng Công tố Quận Somerset* → `#3`: *Hai thám tử kỳ cựu Tim Braun và Danny Baldwin*",
    "4-02": "**BỨC TƯỜNG IM LẶNG KIÊN CỐ** · *Từ phía ban giám đốc Trung tâm Y tế Somerset* → `#5`: *Bệnh viện tìm cách trì hoãn giao nộp tài liệu* → `#6`: *Chìa khóa duy nhất để phá vỡ bế tắc*",
    "4-03": "**HỌ ĐÃ TÌM ĐẾN AMY LOUGHREN** · *Nữ y tá ca đêm tài năng* · *Bạn thân nhất của Charles Cullen*",
    "4-04": "**BẢN IN NHẬT KÝ MÁY PYXIS** · *Amy đã chết lặng* → `#3`: **RÚT THUỐC CỦA HÀNG CHỤC BỆNH NHÂN**",
    "4-05": "**THUỐC ĐỘC CỰC MẠNH** · *Làm ngừng tim chỉ sau vài phút*",
    "4-06": "**DẤU VẾT CỦA NHỮNG VỤ ÁM SÁT HÀNG LOẠT CÓ TÍNH TOÁN** → `#6`: *Một mình nuôi hai con nhỏ* · *Mang trong mình căn bệnh cơ tim* → `#7`: **DẤN THÂN VÀO MỘT CUỘC ĐẤU TRÍ CÂN NÃO**",
    "4-07": "“Charlie từng là người bạn thân thiết nhất của tôi trong những đêm trực lạnh lẽo tại khoa hồi sức.” → `#2`: “Anh ấy biết bệnh tim của tôi, luôn nhận làm giúp tôi những phần việc nặng” → `#3`: “Tôi đã từng yêu quý và tin tưởng anh ấy như một người anh em ruột thịt trong gia đình.”",
    "4-08": "*Những trang nhật ký máy tính ghi lại các loại thuốc độc* · *Trái tim tôi như tan nát*",
    "4-09": "“Tôi nhận ra người đàn ông hiền lành ngồi ăn khuya cùng tôi bấy lâu nay lại là một kẻ gieo rắc cái chết trong bóng tối.” → `#6`: “Dù vô cùng sợ hãi cho mạng sống của bản thân và tương lai của các con, tôi biết mình không có quyền im lặng để tội ác tiếp tục diễn ra.”",
    "4-10": "**NGÀY 6 THÁNG 12 NĂM 2003** · *Một cuộc gặp gỡ lịch sử* · *Tại một quán ăn địa phương ở thị trấn Somerville* → `#3`: *Chiếc micro bí mật* · *Gắn khéo léo dưới lớp áo khoác mùa đông*",
    "4-11": "**BÊN NGOÀI BÃI ĐỖ XE** · *Theo dõi từng cử động qua thiết bị thu âm tầm xa*",
    "4-12": "**ĐỐI DIỆN VỚI AMY** · *Dáng vẻ gầy gò và ánh mắt ngây thơ quen thuộc* → `#6`: *Amy nhẹ nhàng gợi mở về những bất thường* → `#7`: **LỚP MẶT NẠ ĐIỀM TĨNH** · *Bắt đầu rạn nứt*",
    "4-13": "“Tôi muốn dừng lại, tôi muốn mọi chuyện kết thúc.” → `#9`: **MẮT XÍCH QUYẾT ĐỊNH** · *Ra lệnh bắt giữ khẩn cấp kẻ thủ ác*",
    "4-15": "**NGÀY 12 THÁNG 12 NĂM 2003** · *Bị tra tay vào còng số tám ngay tại bãi đỗ xe bệnh viện* → `#2`: *Một cuộc thẩm vấn kéo dài suốt bảy tiếng đồng hồ* → `#3`: **BỨC TƯỜNG TÂM LÝ** · *Đã sụp đổ hoàn toàn*",
    "4-16": "**CUỘC ĐẤU TRÍ QUYẾT ĐỊNH** · *Trong căn phòng thẩm vấn định mệnh*",
    "4-17": "**KHÔNG BAO GIỜ TẤN CÔNG HAY PHÁN XÉT NHÂN CÁCH** → `#2`: *Dồn một kẻ ái kỷ vào chân tường* · *Cơ chế phòng vệ và im lặng tuyệt đối* → `#3`: **KHAI THÁC CHÍNH ẢO TƯỞNG VỀ LÒNG NHÂN TỪ**",
    "4-18": "**KHÓC NẤC LÊN VÀ SUY SỤP HOÀN TOÀN**",
    "4-19": "**DIGOXIN VÀ INSULIN** → `#6`: **GIỌT NƯỚC MẮT** · *Trong phòng hỏi cung* · *Không hề dành cho các nạn nhân xấu số* → `#7`: *Sự “Tự thương hại bệnh lý” của một kẻ ái kỷ*",
    "4-20": "**HẮN KHÓC VÌ THƯƠNG BẢN THÂN PHẢI VÀO TÙ** · *Không hề có một tia trắc ẩn nào cho những người đã khuất* → `#9`: *Vô cảm về cách thức tiêm thuốc* → `#10`: **HÀNH TRÌNH LẨN TRỐN SUỐT 16 NĂM**",
    "4-21": "**CÁNH CỬA PHÒNG TẠM GIAM ĐÓNG LẠI** → `#12`: **HỆ THỐNG Y TẾ PHẢI ĐỐI DIỆN** · *Trách nhiệm của chính mình*",
    # ---------------- HỒI 5
    "5-01": "**THÁNG 3 NĂM 2006** · *Tòa án Thượng thẩm Quận Somerset, bang New Jersey*",
    "5-02": "**11 BẢN ÁN TÙ CHUNG THÂN** · *Thời gian thụ án tối thiểu 397 năm*",
    "5-03": "**THÊM BẢY BẢN ÁN CHUNG THÂN** · *Tổng mức án lên 18 bản án tù chung thân* → `#7`: *Chôn vùi toàn bộ phần đời còn lại* → `#8`: **BẢN ÁN NGHIÊM KHẮC** · *Khép lại chuỗi ngày săn mồi kinh hoàng*",
    "5-05": "**BẢN CHẤT ÁI KỶ MÉO MÓ** · *Vẫn tiếp tục bộc lộ một cách trơ tráo* → `#2`: *Từ chối bước ra đối diện với gia đình các nạn nhân* → `#3`: **“THƯA QUÝ TÒA, NGÀI CẦN PHẢI TỪ CHỨC.”**",
    "5-06": "*Suốt hàng giờ đồng hồ* · **THẨM PHÁN WILLIAM PLATT** · *Ra lệnh dùng băng dính bịt miệng hắn lại*",
    "5-07": "**SỰ SỤP ĐỔ THẢM HẠI CỦA MỘT BẢN NGÃ ÁI KỶ** · *Bị tước đoạt toàn bộ quyền lực và sự chú ý* → `#7`: **CHỨ NHẤT QUYẾT KHÔNG CHỊU CÚI ĐẦU NHẬN TỘI**",
    "5-08": "**“SỰ PHẢN BỘI THỂ CHẾ”** · *Điểm mù tập thể của một hệ thống y tế bị chi phối bởi lợi ích kinh tế* → `#3`: *Ghi nhận những bất thường* · *Từng phát hiện thuốc mất tích*",
    "5-09": "*SỢ BỊ KIỆN TỤNG BỒI THƯỜNG HÀNG TRIỆU ĐÔ LA* → `#5`: **KÝ NHỮNG LÁ THƯ GIỚI THIỆU TÍCH CỰC** → `#6`: *Sự im lặng có hệ thống* · *Biến chính những cơ sở chữa bệnh thành nơi đồng lõa*",
    "5-10": "**SỰ AN TOÀN CỦA CON NGƯỜI BỊ XẾP SAU DANH TIẾNG VÀ TIỀN BẠC** · *Thảm kịch chắc chắn sẽ xảy ra*",
    "5-11": "**MỘT CUỘC ĐẠI CẢI TỔ MANG TÍNH LỊCH SỬ** → `#2`: **“ĐẠO LUẬT CULLEN”** · *Năm 2004* → `#3`: *Báo cáo mọi hành vi sai phạm nghiêm trọng*",
    "5-12": "**MIỄN TRỪ TRÁCH NHIỆM PHÁP LÝ CHO CÁC CƠ SỞ Y TẾ** → `#5`: *Tái thiết kế trên toàn quốc* · *Xóa bỏ hoàn toàn lỗ hổng hủy lệnh* → `#6`: **MỘT HÀNG RÀO BẢO VỆ VỮNG CHẮC**",
    "5-14": "**MỘT LỜI CẢNH TỈNH LẠNH LÙNG** · *Về bản chất phức tạp của lòng tin con người* → `#2`: *Chiếc áo blouse trắng* · *Không bao giờ là sự bảo chứng tuyệt đối cho đạo đức của một tâm hồn* → `#3`: **TỘI ÁC TINH VI NHẤT** · *Luôn ẩn mình hoàn hảo phía sau những vỏ bọc mẫu mực*",
    "5-15": "**“HÃY LUÔN BIẾT LẮNG NGHE VÀ TIN TƯỞNG VÀO TRỰC GIÁC CỦA CHÍNH MÌNH”** → `#5`: *Đừng bao giờ để sự tự trấn an* → `#6`: **LÒNG DŨNG CẢM** · *Cứu sống hàng trăm sinh mệnh khác*",
    "5-16": "**SỰ IM LẶNG TRƯỚC CÁI ÁC** · *Chỉ tiếp tay cho vực thẳm nuốt chửng những người vô tội*",
    "5-18": "*Cảm ơn các khách mời chuyên gia đã cùng đồng hành* → `#2`: *Cảm ơn bạn đã lắng nghe đến những phút cuối cùng* → `#3`: **HÃY LUÔN GIỮ CHO MÌNH MỘT CÁI NHÌN TỈNH TÁO**",
    "5-19": "*Xin chào và hẹn gặp lại các bạn* · **HỒ SƠ TÂM LÝ TIẾP THEO CỦA KÊNH AMBER EYES**",
}

if __name__ == "__main__":
    import sys
    from pathlib import Path
    out = Path(__file__).resolve().parent / "_t04_chu_vn.json"
    out.write_text(json.dumps(CHU_VN, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")
    print(f"{len(CHU_VN)} shot -> {out}")
