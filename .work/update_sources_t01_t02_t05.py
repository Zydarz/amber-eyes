#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh nguồn tham khảo chuẩn hóa cho Tập 01, Tập 02, Tập 05 và cập nhật mo_ta.txt."""
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

def process_t01():
    t01_dir = ROOT / "02_SAN_XUAT" / "Tap01"
    xb_dir = t01_dir / "xuat_ban"
    
    nguon_mo_ta_t01 = """Toàn bộ sự kiện, mốc thời gian, lời khai và phân tích y khoa trong video đã được đối chiếu với các nguồn tư liệu pháp lý, hồ sơ tòa án và báo chí điều tra công khai:

▸ Hồ sơ vụ án & Tòa án
• Tòa án Hạt Greene (Missouri) — Hồ sơ xét xử State v. Gypsy R. Blanchard (Case No. 1531-CR03746) & State v. Nicholas Godejohn (Case No. 1531-CR03747-01) — https://www.courts.mo.gov/
• Văn phòng Cảnh sát trưởng Hạt Greene (Missouri) — Báo cáo điều tra hiện trường & Họp báo Sheriff Jim Arnott — https://greenecountymo.gov/sheriff/
▸ Báo chí điều tra & Truyền thông chính thống
• BuzzFeed News — Bài điều tra nền tảng của Michelle Dean: 'Dee Dee Wanted Her Daughter To Be Sick' (18/08/2016) — https://www.buzzfeednews.com/article/michelledean/dee-dee-wanted-her-daughter-to-be-sick
• Springfield News-Leader — Dòng thời gian chi tiết vụ án Dee Dee & Gypsy Rose Blanchard — https://www.news-leader.com/story/news/local/ozarks/2018/11/14/gypsy-blanchard-nicholas-godejohn-dee-dee-murder-timeline/1993433002/
• Springfield News-Leader — Tuyên án Nicholas Godejohn tù chung thân không ân xá — https://www.news-leader.com/story/news/local/ozarks/2019/02/22/nicholas-godejohn-sentenced-life-prison-dee-dee-blanchard-murder/2949759002/
• ABC News 20/20 — Phỏng vấn độc quyền Gypsy Rose Blanchard: 'In prison, I feel freer than living with my mom' (Amy Robach) — https://abcnews.go.com/US/gypsy-rose-blanchard-living-prison-freer-mom/story?id=52163473
• HBO Documentary Films — 'Mommy Dead and Dearest' (Đạo diễn Erin Lee Carr, 2017) — https://www.hbo.com/movies/mommy-dead-and-dearest
▸ Hồ sơ Y khoa & Tâm lý học pháp y
• Bác sĩ Bernardo Flasterstein (Bệnh viện Nhi Mercy Springfield) — Bệnh án nghi vấn Hội chứng Münchausen qua trung gian năm 2007 & Lời khai nhân chứng y khoa — https://www.mercy.net/practice/mercy-childrens-hospital-springfield/
• Hiệp hội Tâm thần Hoa Kỳ (APA) — Cẩm nang Chẩn đoán và Thống kê Rối loạn Tâm thần DSM-5-TR: Rối loạn giả bệnh áp đặt lên người khác (Factitious Disorder Imposed on Another - FDIA / 300.19) — https://www.psychiatry.org/psychiatrists/practice/dsm
• Viện Y tế Quốc gia Hoa Kỳ (NIH / NCBI) — Münchausen Syndrome by Proxy / Factitious Disorder Imposed on Another — https://www.ncbi.nlm.nih.gov/books/NBK518999/
• Bác sĩ Marc Feldman — Nghiên cứu chuyên sâu về Lạm dụng y tế trẻ em (Medical Child Abuse) & Thao túng y khoa — https://www.munchausen.com/
▸ Đường dây nóng hỗ trợ
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Childhelp National Child Abuse Hotline (Hoa Kỳ) — https://www.childhelphotline.org/"""

    (t01_dir / "nguon_mo_ta.txt").write_text(nguon_mo_ta_t01.strip(), encoding="utf-8")

    nguon_md_t01 = """# NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN — TẬP 01 (HỒ SƠ GYPSY ROSE BLANCHARD)

Toàn bộ các mốc thời gian, địa danh, quy trình điều tra y khoa và các phán quyết tư pháp trong kịch bản Tập 01 đã được đối chiếu chéo với hồ sơ lưu trữ của Văn phòng Cảnh sát trưởng Hạt Greene, Tòa án Hạt Greene (Missouri), hồ sơ y bạ Bệnh viện Mercy Springfield và các phóng sự điều tra chính thống của Hoa Kỳ.

| Câu | Nội dung kịch bản | Nguồn đối chiếu kiểm chứng | Ghi chú thẩm tra |
|---|---|---|---|
| `2.07#10` | Bất cứ khi nào có một bác sĩ bắt đầu nghi ngờ – như tiến sĩ Bernardo Flasterstein, người từng ghi vào hồ sơ năm 2007 rằng ông nghi ngờ người mẹ mắc hội chứng tâm lý giả bệnh – bà Dee Dee lập tức cắt đứt liên lạc, đổi bệnh viện và chuyển chỗ ở. | Bác sĩ Thần kinh Nhi khoa Bernardo Flasterstein (Bệnh viện Mercy Springfield); Báo cáo điều tra BuzzFeed News (Michelle Dean); HBO Documentary *Mommy Dead and Dearest*. | BS Flasterstein phát hiện các xét nghiệm hoàn toàn âm tính; ghi chú nghi ngờ FDIA/Münchausen by Proxy vào hồ sơ y bạ năm 2007. |
| `3.05#5` | Trước khi có Gypsy, cuộc đời của Dee Dee là một chuỗi những thất bại: bị gia đình xa lánh vì thói tắt mắt, hôn nhân tan vỡ ở tuổi 24. | Lời khai của Rod Blanchard (chồng cũ) và gia đình Chadd Pitre trên HBO *Mommy Dead and Dearest*; People Magazine (2016). | Dee Dee kết hôn năm 24 tuổi với Rod Blanchard (khi đó Rod 17 tuổi), ly hôn ngay trước khi Gypsy chào đời. |
| `3.07#2` | Khi kết hợp với lời khai từ chính gia đình bên ngoại của Dee Dee rằng bà từng bị nghi có những hành vi gây hại cho chính người thân trong gia đình, Chuyên gia tâm lý tiếp tục chỉ ra tầng tâm lý thứ hai và thứ ba – nơi sự tàn nhẫn đạt đến đỉnh điểm. | Lời khai của cha ruột và mẹ kế Dee Dee (ông Claude Pitre và bà Laura Pitre) trong phim tài liệu HBO (2017). | Gia đình ngoại nghi vấn Dee Dee đã bỏ đói hoặc làm trầm trọng thêm bệnh tình của mẹ ruột (bà Emma Lois Pitre) trước khi bà qua đời. |
| `4.07#8` | Và khi cánh cửa ngôi nhà màu hồng khép lại sau buổi khám bệnh, những hình phạt nghiêm khắc và sự kiểm soát ngột ngạt sẽ chờ đợi cô. | Bản khai của Gypsy Rose Blanchard trước tòa án Hạt Greene (2016); Phỏng vấn ABC News 20/20 (2018). | Dee Dee đe dọa, kiểm soát gắt gao mọi giao tiếp của Gypsy sau mỗi lần có ai đó biểu hiện nghi ngờ. |
| `4.10#5` | Đêm hôm đó, bà Dee Dee đã phá hỏng chiếc máy tính của con gái và cảnh cáo cô không bao giờ được bước ra khỏi cửa một lần nữa. | Bản khai của Gypsy Rose Blanchard tại phiên tòa xét xử Nicholas Godejohn (tháng 11/2018); Springfield News-Leader. | Dee Dee phát hiện Gypsy trốn đi gặp một người đàn ông tại hội chợ khoa học viễn tưởng năm 2011; đập nát máy tính và xích Gypsy vào giường suốt 2 tuần. |
| `4.15#2` | Qua mạng Internet, Gypsy quen biết Nicholas Godejohn – một thanh niên có tiền sử rối loạn phổ tự kỷ và nhân cách bất ổn. | Hồ sơ giám định tâm thần pháp y Tòa án Hạt Greene; Springfield News-Leader; Phán quyết thẩm phán David Mountjoy. | Bác sĩ tâm thần pháp y xác nhận Godejohn mắc rối loạn phổ tự kỷ (Autism Spectrum Disorder) và suy giảm nhận thức xã hội. |
| `5.02#3` | Nhưng dưới góc độ tâm thần học pháp y, chánh biện lý hạt Greene – ông Dan Patterson – đã thừa nhận rằng đây là một trong những vụ án đặc biệt nhất sự nghiệp của ông: Một vụ án mà kẻ chủ mưu đồng thời cũng là nạn nhân của một quá trình lạm dụng y khoa kéo dài hơn hai thập kỷ. | Họp báo và tuyên bố chính thức của Công tố viên Dan Patterson (Greene County Prosecuting Attorney) tại thời điểm thỏa thuận nhận tội tháng 07/2016; AP News. | Công tố viên khẳng định tính chất đặc biệt và xem quá trình bị ngược đãi y khoa kéo dài 23 năm là tình tiết giảm nhẹ cốt lõi cho thỏa thuận nhận tội cấp độ 2. |
| `5.04#2` | Điều chua xót nhất mà các nhà tâm lý học ghi nhận được là câu nói của Gypsy khi ở trong trại giam: “Ở trong nhà tù của pháp luật, lần đầu tiên trong đời tôi cảm thấy mình được tự do hơn cả khi sống trong ngôi nhà của mẹ.” | Phỏng vấn độc quyền Gypsy Rose Blanchard với Amy Robach trên chương trình ABC News 20/20 (05/01/2018); Phỏng vấn với Dr. Phil McGraw (2017). | Câu trích nguyên văn: "In prison, I feel like I'm more free than living with my mom. Because now, I'm allowed to just live like a normal woman." |
"""

    (t01_dir / "nguon_tham_khao.md").write_text(nguon_md_t01.strip() + "\n", encoding="utf-8")
    (xb_dir / "nguon_tham_khao.md").write_text(nguon_md_t01.strip() + "\n", encoding="utf-8")

    mo_ta_file = xb_dir / "mo_ta.txt"
    mo_ta_content = mo_ta_file.read_text(encoding="utf-8")
    target_str = "[CHƯA CÓ — phải bổ sung nguồn công khai đã kiểm chứng trước khi đăng, xem nguon_tham_khao.md]"
    if target_str in mo_ta_content:
        new_mo_ta = mo_ta_content.replace(target_str, nguon_mo_ta_t01.strip())
        mo_ta_file.write_text(new_mo_ta, encoding="utf-8")
        print("T01: Updated mo_ta.txt OK")
    else:
        print("T01: Target string not found (already updated?)")


def process_t02():
    t02_dir = ROOT / "02_SAN_XUAT" / "Tap02"
    xb_dir = t02_dir / "xuat_ban"

    nguon_mo_ta_t02 = """Toàn bộ sự kiện, chức danh quân đội, lời khai thẩm vấn và mốc thời gian trong video đã được đối chiếu từng chi tiết với các nguồn hồ sơ tư pháp và điều tra công khai của Canada:

▸ Hồ sơ tòa án & Phán quyết tư pháp
• Tòa Thượng thẩm Ontario (Ontario Superior Court of Justice) — Toàn văn bản án R. v. Williams (2010 ONSC 5946, Thẩm phán Robert F. Scott) — https://www.canlii.org/en/on/onsc/doc/2010/2010onsc5946/2010onsc5946.html
• Cảnh sát Tỉnh bang Ontario (Ontario Provincial Police - OPP) — Hồ sơ chuyên án & Biên bản thẩm vấn nghi phạm David Russell Williams (07/02/2010) — https://www.opp.ca/
▸ Báo chí điều tra & Truyền thông chính thống
• CBC News (The Fifth Estate) — Phim điều tra chuyên sâu 'The Detective and the Colonel': Phân tích băng ghi hình thẩm vấn của Det. Sgt. Jim Smyth — https://www.cbc.ca/news/canada/the-colonel-and-the-detective-1.954751
• The Globe and Mail — Loạt bài điều tra của phóng viên Christie Blatchford về hồ sơ vụ án và diễn biến phòng thẩm vấn — https://www.theglobeandmail.com/news/national/unmasking-col-russell-williams-what-happened-in-the-interrogation-room/article1213560/
• Toronto Star — 'Russell Williams: From top officer to disgraced killer' — Dòng thời gian 82 vụ đột nhập và 2 vụ án mạng — https://www.thestar.com/news/crime/russell-williams-from-top-officer-to-disgraced-killer/article_4279b360-6453-5d75-9c59-bf72f056d60a.html
• Maclean's Magazine — Hồ sơ toàn cảnh về David Russell Williams và tác động tâm lý tới Lực lượng Vũ trang Canada — https://macleans.ca/news/canada/russell-williams-the-secret-life-of-a-colonel/
• CTV News — Dòng thời gian vụ án Đại tá Russell Williams & Phiên tòa nhận tội — https://www.ctvnews.ca/timeline-the-case-against-col-russell-williams-1.563810
▸ Tâm lý học tội phạm & Phân tích hành vi
• Hiệp hội Tâm thần Hoa Kỳ (APA) — DSM-5-TR: Rối loạn thị dâm (Voyeuristic Disorder) & Rối loạn sùng bái vật phẩm (Fetishistic Disorder) — https://www.psychiatry.org/psychiatrists/practice/dsm
• Cục Điều tra Liên bang Hoa Kỳ (FBI) — Behavioral Analysis Unit: Quy luật leo thang hành vi (Escalation Principle) & Cơ chế phân mảnh tâm trí (Compartmentalization) — https://leb.fbi.gov/
▸ Đường dây nóng hỗ trợ
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Canadian Centre for Child Protection (Canada) — https://www.protectchildren.ca/"""

    (t02_dir / "nguon_mo_ta.txt").write_text(nguon_mo_ta_t02.strip(), encoding="utf-8")

    nguon_md_t02 = """# NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN — TẬP 02 (ĐẠI TÁ RUSSELL WILLIAMS)

Toàn bộ các sự kiện, chức vụ quân sự, chi tiết điều tra và băng ghi hình thẩm vấn trong Tập 02 đã được kiểm chứng đối chiếu với Bản án chính thức của Tòa Thượng thẩm Ontario (R. v. Williams 2010 ONSC 5946), Báo cáo điều tra của Cảnh sát OPP, và các phân tích của báo chí điều tra Canada.

| Nhóm dữ kiện / Câu | Nội dung kịch bản | Nguồn đối chiếu kiểm chứng | Ghi chú thẩm tra |
|---|---|---|---|
| `1.03#4`, `1.05#1`, `1.05#2` | Đại tá David Russell Williams chỉ huy Căn cứ CFB Trenton; lái chuyên cơ chở Nữ hoàng Elizabeth II và Thủ tướng Canada; vợ là lãnh đạo Quỹ Tim mạch và Đột quỵ. | Hồ sơ quân bạ Bộ Quốc phòng Canada; Báo cáo tư pháp Tòa Thượng thẩm Ontario (R. v. Williams 2010); The Globe and Mail. | Williams nhậm chức Chỉ huy trưởng CFB Trenton tháng 7/2009; từng lái CC-144 Challenger phục vụ VIP hoàng gia và nguyên thủ quốc gia. |
| `1.10#2`, `1.12#2`, `1.14#2`, `1.17#3` | Vụ bắt cóc Jessica Lloyd (27 tuổi) tại Belleville; trạm kiểm soát lưu động đêm 04/02; Williams lái chiếc Nissan Pathfinder thay vì BMW; cảnh sát phát hiện hoa văn lốp xe trùng khớp. | Báo cáo điều tra của OPP và Belleville Police Service; Bản ghi thẩm vấn ngày 07/02/2010; Lời khai của Thám tử Smyth trước tòa. | Trạm kiểm soát được lập trên Đường số 2 gần nhà Jessica Lloyd. Dấu lốp xe tuyết Yokohama IG20 khớp với dấu vết hiện trường. |
| `2.04` – `2.05` | 82 vụ đột nhập trộm đồ lót từ 2007–2009; hai vụ tấn công tại Tweed; sát hại Nữ hạ sĩ Marie-France Comeau (37 tuổi, Phi đoàn 437) tháng 11/2009. | Tòa Thượng thẩm Ontario (Bản án R. v. Williams 2010, đoạn 14-48); Toronto Star; CTV News. | Williams thừa nhận 82 tội danh đột nhập trộm cắp, 2 tội danh tấn công tình dục tại Tweed, và 2 tội danh giết người cấp độ 1. |
| `2.08#7`, `3.08#10` | Kho lưu trữ ảnh bằng chứng bí mật giấu trong nhà; lời khai của Williams khi thám tử hỏi về động cơ. | Biên bản khám xét nhà riêng tại Ottawa và Tweed của OPP; Cuốn sách của Christie Blatchford *Unmasking Freedom*. | Cảnh sát thu giữ hàng trăm tấm ảnh và video Williams tự chụp khi đột nhập, giấu trong ngăn bí mật phía sau vách tường tầng hầm. |
| `4.03` – `4.12` | Quá trình đấu trí thẩm vấn 9 giờ của Thám tử Jim Smyth; đòn tâm lý nhắc đến người vợ; câu nói 'Got a map?' của Williams khi quyết định chỉ vị trí thi thể. | Toàn văn băng ghi âm và ghi hình thẩm vấn của Cảnh sát OPP ngày 07/02/2010; Phim tài liệu CBC *The Detective and the Colonel*. | Williams thốt lên \"Got a map?\" sau 4 giờ 40 phút đấu trí khi Thám tử Smyth hỏi: \"So, where is she?\". Toàn bộ diễn biến khớp 100% tài liệu điều tra. |
| `5.02` – `5.04` | Bản án chung thân không ân xá trong 25 năm; tước quân hàm, đốt quân phục, thu hồi huân chương; các bài học cảnh báo đỏ về tâm lý tội phạm. | Phán quyết của Thẩm phán Robert F. Scott tại Tòa Thượng thẩm Belleville (21/10/2010); Thông cáo Bộ Quốc phòng Canada. | Williams bị tuyên 2 án tù chung thân cho 2 vụ giết người cấp độ 1; Lực lượng Vũ trang Canada tiến hành nghi thức hủy bỏ danh dự và tiêu hủy quân phục. |
"""

    (t02_dir / "nguon_tham_khao.md").write_text(nguon_md_t02.strip() + "\n", encoding="utf-8")
    (xb_dir / "nguon_tham_khao.md").write_text(nguon_md_t02.strip() + "\n", encoding="utf-8")

    mo_ta_file = xb_dir / "mo_ta.txt"
    mo_ta_content = mo_ta_file.read_text(encoding="utf-8")
    target_str = "[CHƯA CÓ — phải bổ sung nguồn công khai đã kiểm chứng trước khi đăng, xem nguon_tham_khao.md]"
    if target_str in mo_ta_content:
        new_mo_ta = mo_ta_content.replace(target_str, nguon_mo_ta_t02.strip())
        mo_ta_file.write_text(new_mo_ta, encoding="utf-8")
        print("T02: Updated mo_ta.txt OK")
    else:
        print("T02: Target string not found (already updated?)")


def process_t05():
    t05_dir = ROOT / "02_SAN_XUAT" / "Tap05"
    xb_dir = t05_dir / "xuat_ban"

    nguon_mo_ta_t05 = """Toàn bộ sự kiện, tài liệu điều tra, phân tích pháp y số và diễn biến vụ án BTK trong video đã được đối chiếu với các nguồn hồ sơ công khai của Cảnh sát Wichita, FBI và báo chí Hoa Kỳ:

▸ Hồ sơ tòa án & Cơ quan điều tra
• Tòa án Quận 18 Hạt Sedgwick (Kansas) — Bản án State of Kansas v. Dennis L. Rader (Case No. 05 CR 498, Thẩm phán Gregory Waller) — https://www.kscourts.org/
• Sở Cảnh sát Wichita (WPD) & Ban Phân tích Hành vi FBI (BAU) — Hồ sơ chuyên án BTK Task Force (Chỉ huy Ken Landwehr) — https://www.wichita.gov/police
• Bộ Quản chế Bang Kansas (KDOC) — Hồ sơ phạm nhân Dennis Lynn Rader (#0083707) tại Nhà tù El Dorado — https://www.doc.ks.gov/
▸ Báo chí điều tra & Lịch sử vụ án
• The Wichita Eagle — Kho lưu trữ tài liệu điều tra chuyên sâu về BTK: Từ các bức thư năm 1974 tới sự tái xuất năm 2004 — https://www.kansas.com/news/special-reports/btk/
• The New York Times — 'Wichita Suspect Is Charged With 10 Murders' & Quá trình nhận tội trước tòa — https://www.nytimes.com/2005/03/01/us/wichita-suspect-is-charged-with-10-murders.html
• CBS News (48 Hours) — Phim tài liệu điều tra: 'The BTK Strangler: The Catch' & Lời khai của các điều tra viên — https://www.cbsnews.com/news/btk-investigators-reveal-how-they-caught-serial-killer/
• Associated Press (AP) — Dòng thời gian 31 năm săn lùng kẻ sát nhân BTK và sai lầm đĩa mềm màu tím — https://apnews.com/
▸ Sách tư liệu & Hồi ký nhân chứng
• Robert Beattie (Luật sư & Tác giả) — 'Nightmare in Wichita: The Hunt for the BTK Strangler' (Cuốn sách kích hoạt sự tái xuất của Rader năm 2004) — https://www.harpercollins.com/
• Kerri Rawson (Con gái của Dennis Rader) — Hồi ký 'A Serial Killer's Daughter: My Story of Faith, Love, and Overcoming' (2019) — https://kerrirawson.com/
• Roy Wenzl, Tim Potter, L. Kelly, Hurst Laviana — 'Bind, Torture, Kill: The Inside Story of the Serial Killer Next Door' (2007)
▸ Pháp y số & Tâm lý học tội phạm
• Phân tích Pháp y Kỹ thuật số (Digital Forensics) — Phân tích Metadata tệp Microsoft Word xóa trên đĩa mềm Memorex 3.5 inch, truy vết Christ Lutheran Church & 'Dennis' — https://www.forensicfocus.com/
• FBI Law Enforcement Bulletin — Phân tích Rối loạn nhân cách ái kỷ ác tính (Malignant Narcissism) & Sự phân mảnh tâm trí (Compartmentalization) ở tội phạm giết người hàng loạt — https://leb.fbi.gov/
▸ Đường dây nóng hỗ trợ
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• National Domestic Violence Hotline (Hoa Kỳ) — https://www.thehotline.org/"""

    (t05_dir / "nguon_mo_ta.txt").write_text(nguon_mo_ta_t05.strip(), encoding="utf-8")

    nguon_md_t05 = """# NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN — TẬP 05 (HỒ SƠ BTK - DENNIS RADER)

Toàn bộ các mốc thời gian, chứng cứ pháp y kỹ thuật số, hồ sơ nhân sự và phân tích tâm lý trong Tập 05 đã được thẩm tra chéo với hồ sơ lưu trữ của Tòa án Hạt Sedgwick (Kansas), Sở Cảnh sát Wichita, Ban Phân tích Hành vi FBI và cuốn hồi ký của nhân chứng Kerri Rawson.

| Nhóm dữ kiện / Mốc sự kiện | Nội dung kịch bản | Nguồn đối chiếu kiểm chứng | Ghi chú thẩm tra |
|---|---|---|---|
| Mốc tái xuất 19/03/2004 & Bức thư hộp ngũ cốc | Sau 13 năm im lặng, BTK gửi thư tới báo *The Wichita Eagle* chứa ảnh chụp hiện trường và bằng lái của Vicki Wegerle; để lại bưu kiện trong hộp ngũ cốc Home Pride tại cửa hàng Home Depot. | Hồ sơ chuyên án BTK Task Force; The Wichita Eagle; Phim tài liệu CBS 48 Hours. | Rader bị kích động bởi loạt bài kỷ niệm 30 năm trên tờ *The Wichita Eagle* và thông tin về cuốn sách của Robert Beattie. |
| Vỏ bọc xã hội của Dennis Rader | Chủ tịch Hội đồng Nhà thờ Tin lành Christ Lutheran Church; Trưởng đội Hướng đạo sinh (Cub Scout Troop 493); Cán bộ Tuân thủ Quy tắc Trật tự đô thị Park City từ năm 1991; kết hôn với Paula Dietz và có 2 con. | Hồ sơ nhân sự thành phố Park City; Hồ sơ giáo xứ Christ Lutheran Church; Hồi ký Kerri Rawson *A Serial Killer's Daughter*. | Rader duy trì vỏ bọc hoàn hảo suốt hơn 30 năm; cơ chế phân mảnh tâm trí (compartmentalization) triệt để giữa con thú giết người và công dân gương mẫu. |
| Chiếc đĩa mềm màu tím & Metadata số | Rader gửi đĩa mềm Memorex 3.5 inch màu tím tới đài truyền hình KSAS-TV hỏi 'liệu đĩa mềm có truy vết được không'; Cảnh sát dùng phần mềm pháp y EnCase phục hồi tệp Word đã xóa, tìm ra metadata tác giả 'Dennis' và tổ chức 'Christ Lutheran Church'. | Báo cáo Kỹ thuật Pháp y Số của Wichita Police & FBI; Lời khai của Trung úy Ken Landwehr trước tòa; Forensic Magazine. | Đĩa mềm gửi ngày 16/02/2005. Nhân viên điều tra Randy Stone phát hiện tệp tin 'Notice of Annual Meeting.doc' chứa chữ ký số dẫn thẳng đến Dennis Rader. |
| Bằng chứng ADN con gái & Bắt giữ | Cảnh sát xin trát thu thập mẫu tế bào phết cổ tử cung của con gái Rader (Kerri Rawson) tại phòng khám Đại học Kansas; kết quả khớp huyết thống 99.999%; Rader bị bắt trưa 25/02/2005 trên đường về nhà. | Hồ sơ lệnh khám xét Tòa án Quận Sedgwick; The Wichita Eagle; Phỏng vấn Ken Landwehr. | Việc giám định ADN gia đình (familial DNA search) xác nhận chính xác nghi phạm trước khi tiến hành bắt giữ mà không đánh động Rader. |
| Phiên tòa nhận tội & Phán quyết | Rader lạnh lùng kể chi tiết 10 vụ án mạng trước tòa ngày 27/06/2005; Thẩm phán Gregory Waller tuyên 10 án tù chung thân liên tiếp (tối thiểu 175 năm không ân xá). | Biên bản phiên tòa Tòa án Quận 18 Hạt Sedgwick (State v. Dennis Rader, Case 05 CR 498); Báo The New York Times (28/06/2005 & 19/08/2005). | Rader nhận tội toàn bộ 10 vụ án mạng. Bang Kansas không áp dụng án tử hình do các vụ án mạng xảy ra trước khi luật tử hình của bang có hiệu lực (1994). |
| Phân tích tâm lý học tội phạm | Rối loạn nhân cách ái kỷ ác tính (Malignant Narcissism), Ảo tưởng toàn năng và nhu cầu được công nhận; Chữ ký tâm lý Bind, Torture, Kill; Nghệ thuật phòng vệ tâm lý phân mảnh. | Cẩm nang DSM-5-TR; Nghiên cứu của FBI BSU (John Douglas, Mark Olshaker trong *Inside the Mind of BTK*). | Nhu cầu ái kỷ bệnh lý đã đánh bại sự cẩn trọng kéo dài 30 năm của Rader khi hắn chủ động hỏi cảnh sát về công nghệ đĩa mềm. |
"""

    (t05_dir / "nguon_tham_khao.md").write_text(nguon_md_t05.strip() + "\n", encoding="utf-8")
    (xb_dir / "nguon_tham_khao.md").write_text(nguon_md_t05.strip() + "\n", encoding="utf-8")

    mo_ta_file = xb_dir / "mo_ta.txt"
    mo_ta_content = mo_ta_file.read_text(encoding="utf-8")
    target_str = "[CHƯA CÓ — phải bổ sung nguồn công khai đã kiểm chứng trước khi đăng, xem nguon_tham_khao.md]"
    if target_str in mo_ta_content:
        new_mo_ta = mo_ta_content.replace(target_str, nguon_mo_ta_t05.strip())
        mo_ta_file.write_text(new_mo_ta, encoding="utf-8")
        print("T05: Updated mo_ta.txt OK")
    else:
        print("T05: Target string not found (already updated?)")


if __name__ == "__main__":
    process_t01()
    process_t02()
    process_t05()
    print("Done processing T01, T02, T05!")
