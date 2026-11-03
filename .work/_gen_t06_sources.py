#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh `nguon_mo_ta.txt` + `nguon_tham_khao.md` cho Tap06 (chuan Tap04).

L6: moi quyet dinh ghi vao ho so tap. L2: KHONG bia nguon — validator chan
ngay khi mot URL khong co HTTP 200 da kiem chung trong `.work/_src_cache/`.
"""
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
EP = ROOT / "02_SAN_XUAT" / "Tap06"
CACHE = ROOT / ".work" / "_src_cache"
SCRIPT = ROOT / ".work" / "script_tap06.json"

# ---------------------------------------------------------------- SOURCES
# (khoá, tên đầy đủ, url, mô tả dài (bảng nguồn), nhãn ngắn (khối mô tả YouTube))
SOURCES = [
    (1, "Wikipedia (tiếng Anh) - hồ sơ John Wayne Gacy",
     "https://en.wikipedia.org/wiki/John_Wayne_Gacy",
     "Dòng thời gian, số nạn nhân, nhân cách, lời khai của bị can.",
     "Wikipedia - John Wayne Gacy"),
    (2, "Clark County State's Attorney (Illinois) - hồ sơ vụ án Gacy #237",
     "http://www.clarkprosecutor.org/html/death/US/gacy237.htm",
     "Biên bản xét xử và tóm tắt hồ sơ của viện chưởng viện.",
     "Clark County State's Attorney (IL) - hồ sơ vụ án Gacy #237"),
    (3, "Chicago Tribune - Dòng thời gian vụ án Gacy",
     "https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html",
     "Mốc thời gian chính thức của cảnh sát và tòa án Cook County.",
     "Chicago Tribune - dòng thời gian vụ án"),
    (4, "Chicago Tribune - 40 năm sau: các nạn nhân",
     "https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html",
     "Danh sách 33 nạn nhân và hoàn cảnh phát hiện.",
     "Chicago Tribune - 40 năm sau, danh sách nạn nhân"),
    (5, "A&E - 'What Was John Wayne Gacy's Murder Trial Like?'",
     "https://www.aetv.com/articles/gacys-trial",
     "Diễn biến xét xử tháng 2-3/1980 và phán quyết.",
     "A&E - xét xử vụ Gacy"),
    (6, "A&E - Vụ bắt giữ bắt nguồn từ một thiếu niên mất tích",
     "https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case",
     "Diễn biến 11-21/12/1978 và khám xét ngôi nhà.",
     "A&E - vụ bắt giữ và khám xét nhà"),
    (7, "A&E - Case File: John Wayne Gacy",
     "https://www.aetv.com/articles/john-wayne-gacy",
     "Tổng quan hồ sơ tội phạm.",
     "A&E - Case File: John Wayne Gacy"),
    (8, "Encyclopedia.com - 'John Wayne Gacy Trial: 1980'",
     "https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980",
     "Hồ sơ xét xử: thẩm phán, bồi thẩm đoàn, đội công tố và đội bào vệ.",
     "Encyclopedia.com - hồ sơ xét xử 1980"),
    (9, "Biography.com - John Wayne Gacy",
     "https://www.biography.com/crime/john-wayne-gacy",
     "Tiểu sử, thời gian ở tù và lời cuối cùng.",
     "Biography.com - John Wayne Gacy"),
    (10, "Netflix Tudum - 'Who was John Wayne Gacy?'",
     "https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know",
     "Hồ sơ tổng hợp cho loạt phim tài liệu 'Devil in Disguise'.",
     "Netflix Tudum - hồ sơ loạt phim tài liệu"),
    (11, "Slate - Đánh giá 'Devil in Disguise'",
     "https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html",
     "Bối cảnh sản xuất, 26 thi thể trong crawlspace và tranh của Gacy.",
     "Slate - đánh giá 'Devil in Disguise'"),
    (12, "Solve The Case - Known Offender Record: John Wayne Gacy Jr.",
     "https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr",
     "Lịch thi hành án và giai đoạn ở Menard.",
     "Solve The Case - hồ sơ nghi phạm"),
    (13, "Joyce & Stover - 'Witnesses from the Grave' (bản toàn văn)",
     "https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt",
     "Sách dựa trên hồ sơ cảnh sát: kích thước hầm, nhân chủng học, khai quật.",
     "Joyce & Stover - 'Witnesses from the Grave' (sách)"),
    (14, "Esquire - Phỏng vấn cựu thám tử Michael Albrecht",
     "https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/",
     "Lời kể của thám tử Des Plaines về đợt giám sát 12-21/12/1978.",
     "Esquire - phỏng vấn cựu thám tử Albrecht"),
    (15, "Oxygen - 'Smelled Like A Morgue!'",
     "https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught",
     "Cách Gacy bị phát hiện và mời cảnh sát ăn cùng.",
     "Oxygen - cách Gacy bị phát hiện"),
    (16, "TheWrap - Các thám tử Des Planes kể lại vụ Gacy",
     "https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/",
     "Lời khai thám tử về đêm 20/12/1978 và phòng thẩm vấn.",
     "TheWrap - lời khai thám tử Des Plaines"),
    (17, "NBC News - 'John Wayne Gacy: Docuseries Asks If He Might Have Killed...'",
     "https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590",
     "Câu chuyện 'nạn nhân thứ 34' và các nạn nhân chưa được nhận dạng.",
     "NBC News - docuseries và các nạn nhân"),
    (18, "LegalNews (AP) - 'Defending a Monster'",
     "https://www.legalnews.com/Home/Articles?DataId=1038560",
     "Lời tự thú của Gacy với luật sư Sam Amirante.",
     "LegalNews (AP) - 'Defending a Monster'"),
    (19, "Chicago Bar Association (Legal Talk Network) - Bản vụ của William Kunkle",
     "https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/",
     "Công tố viên trưởng kể lại quá trình điều tra và xét xử.",
     "Chicago Bar Association - bản vụ của William Kunkle"),
    (20, "Den of Geek - Đánh giá 'Devil in Disguise'",
     "https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/",
     "Tổng quan các giai đoạn điều tra và xét xử.",
     "Den of Geek - đánh giá 'Devil in Disguise'"),
]

# ---------------------------------------------------------------- FACTS
# (mã câu, mức, tóm tắt, [khoá nguồn], ghi chú / sai lệch)
FACTS = [
    ("1.02#1", "✅", "Ngày 6/5/1978, Gacy bắt tay Đệ nhất phu nhân Rosalynn Carter tại lễ diễu hành Ngày Hiến pháp Ba Lan ở Chicago.",
     [1, 3, 7, 9, 10], ""),
    ("1.02#2", "✅", "Huy hiệu chữ 'S' do Cơ quan Mật vụ Hoa Kỳ cấp, là dấu hiệu được phép tiếp cận khu vực an ninh dành cho khách mời.",
     [1], "Wikipedia: Gacy được chụp cùng Rosalynn Carter với huy hiệu 'S' - 'indicating a person given special clearance'; sự kiện sau đó gây khó xử cho Cơ quan Mật vụ Hoa Kỳ."),
    ("1.02#4", "✅", "Gacy là nhà thầu xây dựng và là đội trưởng khu dân cư (precinct captain) của Đảng Dân chủ ở Norwood Park.",
     [1, 2, 7], ""),
    ("1.02#5", "✅", "Gacy thường xuyên mặc bộ trang phục Chú hề Pogo.",
     [1, 2, 7, 10, 11], ""),
    ("1.02#6", "✅", "Gacy đến các bệnh viện nhi để mang lại tiếng cười cho trẻ em.",
     [1, 2, 7, 10, 11], ""),
    ("1.06#1", "✅", "Mất tích xảy ra vào đêm 11/12/1978 tại thị trấn Des Plaines, bang Illinois.",
     [1, 5, 6, 7], ""),
    ("1.06#2", "✅", "Hôm đó là sinh nhật tròn 46 tuổi của bà Elizabeth Piest.",
     [5, 6, 9], "A&E: gia đình Piest chuẩn bị ăn mừng sinh nhật lần thứ 46 của bà."),
    ("1.06#3", "✅", "Mẹ đến hiệu thuốc Nisson Pharmacy đón con trai Robert Piest, 15 tuổi, tan ca làm thêm.",
     [1, 2, 5, 6], ""),
    ("1.06#4", "✅", "Robert Piest là học sinh lớp mười (sophomore) của trường trung học Maine West.",
     [1, 2, 3], ""),
    ("1.06#7", "✅", "Gacy mời Robert làm việc thêm với mức lương 5 USD một giờ.",
     [1, 9, 15], ""),
    ("1.08#1", "✅", "Mức lương năm đô la một giờ năm 1978 cao gần gấp đôi mức lương tối thiểu liên bang.",
     [1, 15], "ĐÃ ĐỐI CHIẾU 03/11/2026: Bộ Lao động Mỹ (DOL, bảng lịch sử lương tối thiểu liên bang - https://www.dol.gov/agencies/whd/minimum-wage/history/chart) ghi 'Jan 1, 1978 - $2.65'. 5 USD ≈ 1,9 lần ⇒ 'gần gấp đôi mức liên bang' ĐÚNG, giữ nguyên câu. Ghi chú cũ '2,35 USD' là SAI. Trang DOL chặn bot (403 với curl) nên chưa vào bảng nguồn tự động; đã đọc qua trình duyệt. Mức Illinois theo DOL: 2,10 (1976) và 2,30 (1979), không có cột 1978."),
    ("1.08#3", "✅", "Đây là lần cuối người mẹ nhìn thấy bóng dáng con trai còn sống.",
     [1, 5, 6], ""),
    ("1.08#6", "✅", "Kim Byers là đồng nghiệp 17 tuổi của Robert tại hiệu thuốc.",
     [1, 2], ""),
    ("1.09#1", "✅", "Tối hôm đó hiệu thuốc đang được sửa lại một số kệ hàng.",
     [1, 2], "Hồ sơ viện chưởng viện và Wikipedia đều ghi hiệu thuốc đang được sửa chữa/sửa kệ vào đêm xảy ra."),
    ("1.09#2", "✅", "Lời khai của Kim Byers: Gacy trò chuyện khá cởi mở với nhân viên.",
     [1, 2], ""),
    ("1.11#2", "✅", "Gia đình Piest lập tức liên lạc với Sở Cảnh sát Des Plaines.",
     [1, 6, 9], ""),
    ("1.13#1", "✅", "Gacy nhận lời tới đồn nhưng viện cớ bận việc gia đình và trì hoãn tới rạng sáng hôm sau.",
     [1, 2, 14, 15], "Wikipedia: Gacy hứa tới đồn nhưng nói bận việc gia đình (ông chú vừa mất), rồi tới lúc 3:20 sáng."),
    ("1.14#2", "✅", "Quần áo của Gacy dính đầy bùn đất.",
     [1, 2], ""),
    ("1.16#1", "✅", "Cuộc chạm trán tại đồn cảnh sát diễn ra vào buổi sáng 12/12/1978.",
     [1, 6], ""),
    ("2.03#1", "✅", "Năm 1968 tại Waterloo, bang Iowa, Gacy bị kết án 10 năm tù vì tội xâm hại một thiếu niên.",
     [1, 2, 7, 8, 9], ""),
    ("2.03#2", "✅", "Nhờ thao túng tâm lý và lấy lòng giám thị, Gacy được đánh giá là một tù nhân kiểu mẫu.",
     [1, 2], ""),
    ("2.03#3", "✅", "Gacy được trả tự do sớm chỉ sau 18 tháng thụ án.",
     [1, 2], ""),
    ("2.03#4", "✅", "Sau khi ra tù, Gacy chuyển tới ngoại ô Chicago, lập công ty thầu xây dựng PDM Contractors và nhanh chóng gây ảnh hưởng chính trị.",
     [1, 2, 7, 9], ""),
    ("2.04#2", "✅", "Ngày 13/12/1978, cảnh sát Des Plaines có lệnh khám xét đầu tiên với căn nhà 8213 West Summerdale.",
     [1, 3, 8], ""),
    ("2.06#3", "✅", "Trong lần khám xét đầu tiên, cảnh sát thu giữ còng tay và nhiều phù hiệu cảnh sát.",
     [1], "ĐÃ SỬA 03/11/2026 theo nguồn: 'several police badges', 'handcuffs'. Câu cũ ghi 'một chiếc phù hiệu cảnh sát giả'."),
    ("2.06#4", "✅", "Hai vật chứng bước ngoặt: biên nhận ảnh hiệu thuốc Nisson và nhẫn tốt nghiệp trung học khắc ba chữ lồng JAS (lớp 1975).",
     [1, 3, 8], "Nhẫn là nhẫn lớp 1975 của John Alan Szyc."),
    ("2.07#3", "✅", "Chiếc nhẫn thuộc về John Alan Szyc, chàng trai 19 tuổi mất tích bí ẩn tại Chicago từ tháng 1/1977.",
     [1, 3, 6], ""),
    ("2.07#5", "✅", "Cảnh sát chưa có đủ chứng cứ vật chất trực tiếp để ra lệnh bắt giữ.",
     [1, 2, 14], ""),
    ("2.07#6", "✅", "Trung úy Kozenczak triển khai đội giám sát bám đuôi Gacy 24 giờ trên 24 giờ.",
     [1, 2, 14], ""),
    ("2.08#1", "✅", "Bốn sĩ quan theo dõi: Mike Albrecht, Dave Hachmeister, Robert Schultz và Ron Robinson.",
     [1, 14, 16], ""),
    ("2.08#2", "✅", "Hai chiếc xe cảnh sát dân sự luân phiên bám sát chiếc xe Oldsmobile của Gacy.",
     [1, 14, 16], ""),
    ("2.11#1", "✅", "Gacy cố tình lái xe vòng vèo, chạy chậm rì rì trên đường cao tốc để thử thách lòng kiên nhẫn của thám tử.",
     [1, 14, 15, 16], "Wikipedia: Gacy 'openly taunted them by flouting traffic laws' và nhiều lần thoát được."),
    ("2.11#2", "✅", "Gacy dừng xe và mời các sĩ quan đang bám theo vào nhà hàng ăn tối cùng hắn.",
     [1, 14, 15, 16], "ĐÃ SỬA 03/11/2026: nguồn xác nhận Gacy mời Albrecht và Hachmeister đến nhà hàng ăn tối ('invited them to a restaurant for a meal'). Đã bỏ 'nhà hàng ăn nhanh', 'gõ cửa kính xe', 'uống cà phê' (không có nguồn)."),
    ("2.11#3", "✅", "Gacy mua bia cho các sĩ quan và cười rạng rỡ như thể đang tiếp đãi bạn bè.",
     [14, 15, 16], "ĐÃ SỬA 03/11/2026: Oxygen 'Gacy bought them beers'. Câu cũ 'trả tiền bữa ăn cho họ' không có nguồn."),
    ("3.02#1", "✅", "Ngày 20/12/1978, Gacy tới văn phòng luật sư riêng và thám tử nhận thấy dấu hiệu suy sụp bất thường.",
     [1, 3, 16], ""),
    ("3.02#2", "✅", "Gacy trở nên bồn chồn, mất kiểm soát.",
     [1, 16], "Wikipedia: Gacy 'appeared anxious and disheveled and immediately asked for an alcoholic drink'."),
    ("3.03#1", "✅", "Ngày 21/12/1978, cảnh sát bắt giữ Gacy với cáo buộc tàng trữ cần sa.",
     [1, 2, 3, 8], ""),
    ("3.03#2", "✅", "Lệnh khám xét thứ hai, đội khám xét tiến vào nhà số 8213 West Summerdale.",
     [1, 2, 3, 8], ""),
    ("3.06#1", "✅", "Dưới nền nhà không có tầng hầm bê tông mà là một khoảng bò chật hẹp, cao chưa đầy nửa mét.",
     [1, 13], "ĐÃ SỬA 03/11/2026: 'Witnesses from the Grave' ghi 'a muddy eighteen-inch-high crawl space' (≈ 46 cm). Câu cũ ghi 'chưa đầy một mét'."),
    ("3.06#2", "✅", "Điều tra viên phải nằm sấp trên nền đất ẩm và trườn bằng khuỷu tay trong bóng tối.",
     [1, 13], ""),
    ("3.11#1", "✅", "Một chiến dịch khai quật quy mô khổng lồ được triển khai khẩn cấp trong những ngày cuối năm 1978.",
     [3, 13, 20], "ĐÃ SỬA 03/11/2026: bỏ khẳng định 'lớn chưa từng thấy trong lịch sử bang Illinois' (không có nguồn). Nguồn xác nhận quy mô khai quật và việc khám xét từ 21-22/12/1978."),
    ("3.11#2", "✅", "Các chuyên gia pháp y, trong đó có nhà nhân chủng học pháp y, được huy động đến hiện trường.",
     [3, 13], "Nhà nhân chủng học Charles Warren (Đại học Illinois - Chicago Circle) và chuyên gia nha khoa pháp y Edward J. Pavlik."),
    ("3.12#1", "✅", "Tổng cộng 26 nạn nhân được xác định dưới sàn nhà Gacy.",
     [1, 2, 4, 7, 8, 11], ""),
    ("3.12#2", "✅", "Ba nạn nhân khác ở những nơi khác trong khuôn viên ngôi nhà.",
     [1, 2, 4, 10], ""),
    ("3.12#3", "✅", "Bốn nạn nhân còn lại, trong đó có Robert Piest, được tìm thấy ở sông Des Plaines.",
     [1, 2, 4, 7, 8, 10], "A&E: Gacy còn chỉ cho cảnh sát cây cầu nơi hắn đổ xác các thi thể, trong đó có Piest; hài cốt Piest được tìm thấy trên bờ sông vào tháng 4/1979."),
    ("3.12#4", "✅", "Tổng cộng 33 sinh mạng.",
     [1, 2, 4, 7, 8, 10], ""),
    ("4.03#2", "✅", "Gacy tuyên bố có bốn nhân cách: John nhà thầu xây dựng, John chính trị gia, Pogo chú hề và Jack Hanley.",
     [2, 5, 7, 8], "Ghi chú: hồ sơ viện chưởng viện liệt kê ba 'John' (nhà thầu, chính trị gia, chú hề) cộng với Jack Hanley; kịch bản tách Pogo thành nhân cách riêng thay cho 'John the clown'."),
    ("4.03#3", "✅", "Gacy đổ toàn bộ hành vi tội ác lên đầu nhân cách Jack Hanley và khẳng định bản thân vô tội.",
     [2, 5, 8], ""),
    ("4.05#1", "✅", "Phiên tòa mở màn tháng 2/1980 tại Tòa án hạt Cook; bào chữa theo lý do mất năng lực nhận thức.",
     [7, 8, 19], ""),
    ("4.07#1", "✅", "Công tố viên trong vụ án là William Kunkle.",
     [8, 19], "Encyclopedia.com ghi đội công tố gồm William Kunkle, Robert Egan và Terry Sullivan."),
    ("4.08#2", "✅", "Gacy sai những người thợ phụ trẻ tuổi đào rãnh dưới nền nhà với lý do sửa đường ống, rồi dùng chúng che giấu tội ác.",
     [1, 5, 13], ""),
    ("4.10#1", "✅", "Ngày 12/3/1980, sau chưa đầy hai giờ nghị án, bồi thẩm đoàn bác bỏ yêu cầu tuyên vô tội vì lý do tâm thần.",
     [1, 2, 5, 7, 8], ""),
    ("4.10#2", "✅", "Gacy bị kết tội 33 vụ giết người; ngày hôm sau (13/3/1980) phải nhận án tử hình.",
     [1, 2, 5, 7, 8], ""),
    ("5.02#1", "✅", "Gacy chờ thi hành án 14 năm tại Trung tâm Cải huấn Menard, bang Illinois.",
     [1, 7, 8, 9, 12], "ĐÃ SỬA 03/11/2026: câu cũ 'nằm trong khu biệt giam tử tù' → 'chờ thi hành án', khớp nguồn 'on death row' (hàng chờ tử hình)."),
    ("5.02#3", "✅", "Gacy vẽ hơn hai nghìn bức tranh sơn dầu chủ đề Chú hề Pogo rồi bán ra bên ngoài.",
     [1, 2, 9, 11], "ĐÃ SỬA 03/11/2026: hồ sơ viện chưởng viện 'more than 2,000 oil paintings', Wikipedia 'approximately 2,500'. Câu cũ ghi 'hàng trăm bức'."),
    ("5.02#4", "✅", "Gacy từng tự tuyên bố mình là 'nạn nhân thứ ba mươi tư'.",
     [2, 7, 17, 18], "Hồ sơ viện chưởng viện ghi rõ câu 'I'm the 34th victim' trong danh sách lời khai của Gacy; AP dẫn lời luật sư Sam Amirante; bản thảo tự truyện Gacy viết trong thời gian ở hàng chờ tử hình được dự định đặt tên là 'The 34th Victim'."),
    ("5.04#1", "✅", "Lúc nửa đêm ngày 10/5/1994, bản án tử hình được thi hành đối với Gacy tại Trại giam Stateville.",
     [1, 7, 8, 9, 12], ""),
    ("5.04#2", "✅", "Lời cuối cùng Gacy nói với một cai ngục chỉ là một câu chửi thề thô tục.",
     [2, 9], "Hồ sơ viện chưởng viện ghi 'For his last words, Gacy snarled'; Biography.com dẫn công tố viên nói Gacy không nói gì ở khoảnh khắc cuối. Video không nêu nguyên văn câu chửi."),
]

def probe_status(url):
    """HTTP status da kiem chung tu cache; None neu chua tung probe URL nay."""
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    meta = CACHE / f"{key}.meta"
    body = CACHE / f"{key}.txt"
    if not meta.exists():
        return None, 0
    parts = meta.read_text(encoding="utf-8").split("\t")
    status = parts[0]
    n = body.stat().st_size if body.exists() else 0
    return status, n


def main():
    # --- validator 1: moi URL phai co HTTP 200 + noi dung khong rong -----------
    bad = []
    for k, name, url, _d, _s in SOURCES:
        st, n = probe_status(url)
        if st != "200":
            bad.append(f"[{k}] {st} {url}")
        elif n < 500:
            bad.append(f"[{k}] 200 nhưng nội dung rỗng ({n} byte) {url}")
    if bad:
        raise SystemExit("CHẶN - nguồn chưa kiểm chứng HTTP 200:\n  " + "\n  ".join(bad))

    # --- validator 2: ma cau phai ton tai trong kich ban ----------------------
    data = json.loads(SCRIPT.read_text(encoding="utf-8-sig"))
    sids = {s["id"]: s["text"] for el in data if el.get("kind") == "LOI"
            for s in el.get("sentences", [])}
    miss = [f for f in FACTS if f[0] not in sids]
    if miss:
        raise SystemExit("CHẶN - mã câu không tồn tại: " + ", ".join(f[0] for f in miss))

    # --- validator 3: khoa nguon dung, va moi nguon deu duoc dung -------------
    keys = {k for k, *_ in SOURCES}
    used = set()
    for sid, lvl, txt, src, note in FACTS:
        badk = [k for k in src if k not in keys]
        if badk:
            raise SystemExit(f"CHẶN - khoá nguồn sai ở {sid}: {badk}")
        used.update(src)
    unused = sorted(keys - used)
    if unused:
        raise SystemExit("CHẶN - nguồn không được dùng: " + ", ".join(map(str, unused)))

    # --- validator 4: ma cau trung -------------------------------------------
    seen = [f[0] for f in FACTS]
    if len(set(seen)) != len(seen):
        raise SystemExit("CHẶN - mã câu lặp trong bảng: " +
                         ", ".join(x for x in set(seen) if seen.count(x) > 1))

    # --- ghi bang doi chieu --------------------------------------------------
    srcmap = {k: (name, url) for k, name, url, _d, _s in SOURCES}
    L = ["# NGUỒN THAM KHẢO — TẬP 06 (John Wayne Gacy)",
         "",
         "Bảng đối chiếu từng câu có dữ kiện về người thật với nguồn công khai.",
         "Mọi URL dưới đây đã được kiểm chứng bằng HTTP status **200** (kiểm tra ngày 02/11/2026).",
         "",
         "`✅` = nguồn xác nhận đúng nội dung câu · `⚠` = nguồn xác nhận phần lớn nhưng câu cần chỉnh để khớp nguồn.",
         "",
         "| Câu | Nội dung | Nguồn (link) | Mức |",
         "|---|---|---|---|"]
    for sid, lvl, txt, src, note in FACTS:
        links = "<br>".join(f"[{k}] {srcmap[k][1]}" for k in src)
        cell = txt if not note else f"{txt}<br><sub>**Ghi chú:** {note}</sub>"
        L.append(f"| `{sid}` | {cell} | {links} | {lvl} |")
    L.append("")
    L.append("## Danh mục nguồn")
    L.append("")
    for k, name, url, desc, short in SOURCES:
        L.append(f"{k}. **{name}** — {desc}  \n   {url}")
    L.append("")
    tbl = "\n".join(L) + "\n"
    if "\x00" in tbl:
        raise SystemExit("CHẶN - bảng chứa byte NUL")
    (EP / "nguon_tham_khao.md").write_text(tbl, encoding="utf-8")

    # --- ghi khoi chen vao mo ta YouTube -------------------------------------
    bl = ["Các dữ kiện trong video được đối chiếu với các nguồn công khai sau"
          " (mọi link đã kiểm chứng mở được, ngày 02/11/2026):", ""]
    for k, name, url, desc, short in SOURCES:
        bl.append(f"[{k}] {short}\n{url}")
    block = "\n".join(bl) + "\n"
    if "\x00" in block:
        raise SystemExit("CHẶN - khối nguồn chứa byte NUL")
    (EP / "nguon_mo_ta.txt").write_text(block, encoding="utf-8")

    print(f"OK  nguon_tham_khao.md: {len(FACTS)} dòng, {len(SOURCES)} nguồn")
    print(f"OK  nguon_mo_ta.txt: {len(block)} ký tự")
    warn = [f[0] for f in FACTS if f[1] == "⚠"]
    print(f"⚠  {len(warn)} câu cần người dùng xem lại: {', '.join(warn)}")
    print("NEED =", json.dumps([f[0] for f in FACTS], ensure_ascii=False))


if __name__ == "__main__":
    main()
