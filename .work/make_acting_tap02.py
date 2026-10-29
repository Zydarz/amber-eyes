#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/acting_tap02.json — diễn xuất từng câu cho bản tiếng Việt Tập 02.

Phản hồi Tập 01: mọi vai đọc đều đều. Đo lại: Sói và Cáo 100% "neutral", cao độ giữa các câu
chỉ lệch ~0,85 nửa cung, tốc độ 3,5–3,8 âm tiết/giây. File này tạo độ tương phản GIỮA các câu:
  1. Tốc độ gốc chậm hơn (mục tiêu ~3,0 âm tiết/giây), câu ngắn chậm hơn nữa để "đóng đinh".
  2. Cảm xúc và cao độ đổi theo nhịp: dẫn chuyện → căng → hé lộ → lắng.
  3. Ngắt nghỉ trong câu bằng thẻ <#s#> (engine không đọc thẻ) và "...".
  4. Nghỉ thêm SAU câu ("_pause_after") để build_audio3 chừa chỗ cho khoảnh khắc và SFX.
Lời đọc riêng chỉ thêm ngắt nghỉ, KHÔNG đổi chữ — phụ đề và chữ trên hình giữ nguyên kịch bản.

Định dạng giống acting_EN.json: id -> [cảm xúc, lệch tốc độ so với tốc độ gốc của vai, cao độ, lời đọc | null]
"""
import json
import re
from pathlib import Path

W = Path(r"D:\TEST\Gax\Audi\.work")
SCRIPT = json.loads((W / "script_tap02.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.06": "N2"}

# Tốc độ gốc trong edition.CAST: H 0.90 · D 0.95 · C 0.92 · N 0.95. Lệch mặc định đưa về ~3,0 âm tiết/giây.
BASE_DELTA = {"H": -0.04, "D": -0.05, "C": -0.04, "N1": -0.03, "N2": -0.02}

# Mặc định theo hồi và vai: (cảm xúc, cao độ)
ACT_MOOD = {
    ("1", "H"): ("neutral", 0), ("1", "N1"): ("happy", 1), ("1", "D"): ("neutral", -1),
    ("2", "H"): ("neutral", -1), ("2", "D"): ("neutral", -1),
    ("3", "H"): ("sad", 0), ("3", "C"): ("neutral", 0),
    ("4", "H"): ("neutral", -1), ("4", "N2"): ("surprised", 1), ("4", "D"): ("neutral", 0), ("4", "C"): ("neutral", -1),
    ("5", "H"): ("neutral", 0), ("5", "C"): ("neutral", 0), ("5", "D"): ("neutral", -1),
}

# Câu then chốt: [cảm xúc, lệch tốc độ, cao độ, lời đọc có ngắt nghỉ | None, nghỉ thêm sau câu (s)]
KEY = {
    # HỒI 1 — mở bằng ánh hào quang, rồi bẻ gãy
    "1.03#1": ["neutral", -0.08, -1, "Tháng 7... <#0.3#> năm 2009.", 0.3],
    "1.03#4": ["happy", -0.04, 1, "Người bước lên bục nhận quyền chỉ huy tối cao là Đại tá David Russell Williams. <#0.4#> Một phi công với bản lý lịch hoàn hảo... <#0.3#> đến mức không thể tìm thấy một vết gợn nhỏ.", 0.2],
    "1.05#1": ["happy", -0.02, 1, None, 0],
    "1.07#4": ["happy", -0.02, 1, "Chúng tôi sẵn sàng theo ông ấy đến bất cứ đâu... <#0.2#> mà không một chút hoài nghi.", 0.4],
    "1.08#1": ["fearful", -0.06, -1, "Thế nhưng... <#0.6#> có ai ngờ rằng người đàn ông khoác trên mình bộ quân phục đính đầy huân chương danh dự ấy, <#0.3#> vào những đêm khuya thanh vắng khi rời khỏi căn cứ quân sự... <#0.3#> lại biến mất vào bóng tối của những thị trấn ngoại ô.", 0],
    "1.08#2": ["fearful", -0.08, -2, "Ở đó... <#0.4#> không còn một vị đại tá oai phong lẫm liệt.", 0],
    "1.08#3": ["fearful", -0.10, -2, "Chỉ còn... <#0.3#> một kẻ rình rập. <#0.4#> Lặng lẽ bước qua những hàng rào tuyết trắng.", 0],
    "1.10#1": ["neutral", -0.08, -1, "Đêm 28 tháng 1... <#0.3#> năm 2010.", 0.2],
    "1.10#2": ["sad", -0.05, -1, "Jessica Lloyd, <#0.2#> một nữ nhân viên 27 tuổi tại thị trấn Belleville, <#0.3#> biến mất khỏi nhà riêng.", 0.5],
    "1.12#1": ["neutral", -0.02, -1, None, 0.2],
    "1.12#3": ["neutral", -0.06, -1, "Mục đích của trạm ấy... <#0.3#> không phải kiểm tra giấy tờ.", 0],
    "1.12#4": ["fearful", 0.0, 0, "Cảnh sát đang săn một dấu vết cụ thể: <#0.35#> một vệt vân lốp xe độc đáo trên nền tuyết gần nhà nạn nhân, <#0.2#> và họ cần tìm chiếc xe có vân lốp giống như vậy.", 0.6],
    "1.14#1": ["neutral", -0.04, 0, None, 0],
    "1.14#3": ["surprised", -0.10, -1, "Người ngồi sau vô-lăng hạ cửa kính xuống... <#0.6#> chính là... <#0.3#> Chỉ huy trưởng căn cứ không quân Trenton.", 0.8],
    "1.14#4": ["fearful", -0.04, -1, None, 0],
    "1.14#5": ["neutral", 0.0, 0, "Nhưng điều đó... <#0.2#> chưa đủ để giữ một người như ông ta lại.", 0],
    "1.14#6": ["neutral", 0.02, 1, None, 0],
    "1.14#7": ["sad", -0.08, -2, "Và ba ngày tiếp theo... <#0.4#> ông ta vẫn là một vị đại tá tự do.", 0.4],
    "1.17#1": ["neutral", -0.02, -1, "Tuyết mới rơi đã lưu lại gần nhà nạn nhân một dấu vết lốp xe vô cùng đặc thù: <#0.35#> một vệt gai lốp xe địa hình khá hiếm gặp, <#0.25#> cùng một dấu giày đi tuyết cỡ lớn.", 0],
    "1.17#3": ["surprised", -0.04, 0, "Nhưng khi rọi đèn pin xuống bánh xe... <#0.4#> anh nhận ra hoa văn lốp rất giống dấu vết tại hiện trường, <#0.25#> đủ để ghi lại và báo về cho nhóm điều tra.", 0.3],
    "1.17#4": ["neutral", -0.08, -2, "Đó là lần đầu tiên... <#0.3#> thế giới của Đại tá Russell Williams chạm vào thế giới của cảnh sát.", 0.4],
    "1.17#7": ["neutral", -0.04, -1, "Và thay vì nhận lệnh triệu tập, <#0.2#> Đại tá Russell Williams nhận được một lời mời bằng điện thoại... <#0.3#> mời đến trụ sở cảnh sát để trao đổi.", 0.8],
    "1.18#1": ["neutral", -0.02, 1, None, 0],
    "1.18#3": ["neutral", -0.04, 0, "Tập này sẽ đi sâu vào hai cơ chế tâm lý đen tối của con người: <#0.35#> Quy luật leo thang hành vi, <#0.25#> và Sự phân mảnh tâm trí. <#0.4#> Để giải mã câu hỏi: <#0.3#> làm thế nào một bộ óc tinh hoa có thể sống hai cuộc đời song song... <#0.3#> ngay phía sau bộ quân phục danh dự?", 0],
    # HỒI 2 — hồ sơ, bốn nấc thang
    "2.02#2": ["fearful", -0.04, -1, "Nhưng những gì được tìm thấy bên trong... <#0.4#> đã vượt qua mọi trí tưởng tượng của những chuyên gia điều tra kỳ cựu nhất.", 0.4],
    "2.04#1": ["neutral", -0.04, -1, "Trong ngôi nhà ở Ottawa, các điều tra viên tìm thấy những ổ cứng... <#0.3#> được giấu trong trần tầng hầm.", 0.2],
    "2.04#3": ["fearful", -0.04, -1, "Và toàn bộ hồ sơ ấy phơi bày một sự thật rợn người: <#0.4#> Russell Williams không phải là một kẻ bộc phát trong một đêm.", 0],
    "2.05#2": ["neutral", -0.10, -2, "Nấc thang thứ nhất: <#0.35#> Nhìn trộm.", 0.2],
    "2.05#4": ["neutral", -0.10, -2, "Nấc thang thứ hai: <#0.35#> Đột nhập lấy đồ riêng tư.", 0.2],
    "2.05#7": ["neutral", -0.02, 0, "Từ tháng 9 năm 2007 đến tháng 11 năm 2009, <#0.3#> hắn thực hiện tổng cộng 82 vụ đột nhập... <#0.2#> và đột nhập bất thành.", 0],
    "2.05#8": ["neutral", -0.04, 0, "Nhưng hắn không lấy tiền bạc... <#0.2#> hay trang sức.", 0],
    "2.05#10": ["disgusted", -0.04, -1, "Nghi thức của hắn lặp lại y hệt ở mọi căn nhà: <#0.35#> chụp ảnh, <#0.2#> lấy đồ, <#0.2#> rồi ghi chép lại.", 0.3],
    "2.05#11": ["neutral", -0.10, -2, "Nấc thang thứ ba: <#0.35#> Xâm nhập khi có người ở nhà.", 0.2],
    "2.05#14": ["sad", -0.12, -3, "Và nấc thang cuối cùng: <#0.6#> Cái chết.", 0.6],
    "2.05#15": ["sad", -0.06, -2, None, 0],
    "2.05#16": ["sad", -0.08, -2, "Và chỉ hai tháng sau đó... <#0.4#> nạn nhân tiếp theo là Jessica Lloyd.", 0.4],
    "2.07#3": ["neutral", -0.04, 0, "Nhưng nghịch lý thay, <#0.2#> một kẻ cẩn trọng đến mức cực đoan như vậy... <#0.3#> lại không thể từ bỏ một thứ. <#0.3#> Thứ mà giới tội phạm học gọi là Chữ ký tâm lý.", 0],
    "2.08#6": ["neutral", -0.04, -1, None, 0],
    "2.08#7": ["fearful", -0.06, -1, None, 0.4],
    # HỒI 3 — giải phẫu tâm lý
    "3.02#2": ["surprised", -0.04, 0, "Tại sao một người đàn ông dường như đã có tất cả mọi thứ: <#0.3#> địa vị, <#0.15#> danh vọng, <#0.15#> một người vợ tài năng, <#0.15#> và sự kính trọng của cả một quốc gia... <#0.4#> lại chấp nhận đánh cược tất cả... <#0.3#> chỉ vì những chiếc đồ lót và những hành vi tàn bạo?", 0],
    "3.04#1": ["neutral", -0.06, -1, "Trước khi phân tích, chúng ta cần nói rõ một điều: <#0.4#> không tồn tại một chẩn đoán lâm sàng công khai nào về Russell Williams.", 0.2],
    "3.05#2": ["neutral", -0.04, 0, "Ngược lại, <#0.2#> Williams hoàn toàn tỉnh táo... <#0.2#> và sở hữu một trí tuệ vượt trội.", 0],
    "3.05#4": ["neutral", -0.08, -1, "Tầng thứ nhất là: <#0.35#> Quy luật leo thang hành vi... <#0.2#> và sự lờn Dopamine.", 0.2],
    "3.05#8": ["neutral", -0.06, -1, "Nhưng não bộ con người... <#0.2#> có cơ chế dung nạp.", 0],
    "3.05#10": ["fearful", -0.02, 0, "Để tìm lại cảm giác ban đầu, hắn nâng dần mức độ rủi ro: <#0.35#> từ nhà trống, <#0.2#> đến đối diện với nạn nhân, <#0.2#> đến khống chế nạn nhân, <#0.3#> và cuối cùng... <#0.3#> là nắm giữ quyền sinh tử của một con người.", 0],
    "3.05#11": ["fearful", -0.08, -2, "Đó là một chiếc dốc... <#0.3#> không đáy. <#0.5#> Ngưỡng thỏa mãn liên tục bị đẩy xa hơn... <#0.3#> cho đến khi dẫn tới án mạng.", 0.6],
    "3.07#3": ["surprised", -0.04, 1, "Làm thế nào một tâm trí chịu đựng được sự đối lập khủng khiếp đó... <#0.3#> mà không bị phát điên?", 0],
    "3.08#1": ["neutral", -0.08, -1, "Đó chính là Tầng thứ hai: <#0.35#> Sự phân mảnh tâm trí tuyệt đối.", 0.2],
    "3.08#6": ["neutral", -0.08, -2, "Khi ở ngăn kéo này... <#0.3#> hắn đóng chặt cánh cửa của ngăn kéo kia.", 0.3],
    "3.08#8": ["neutral", -0.10, -2, None, 0.3],
    "3.08#10": ["sad", -0.06, -1, "Khi thám tử hỏi hắn đã từng nghĩ vì sao mình làm những việc đó chưa, <#0.3#> câu trả lời trong bản ghi thẩm vấn trống rỗng đến lạnh người: <#0.6#> Có. <#0.3#> Nhưng tôi không biết câu trả lời... <#0.3#> và tôi khá chắc là câu trả lời cũng chẳng quan trọng.", 0.8],
    "3.08#11": ["sad", -0.06, -1, None, 0],
    "3.10#1": ["neutral", -0.04, 1, "Và tầng tâm lý thứ ba... <#0.2#> cũng là động cơ cốt lõi thúc đẩy toàn bộ chuỗi hành vi của hắn... <#0.3#> là gì, thưa chuyên gia?", 0],
    "3.11#4": ["fearful", -0.04, -1, "Khi hắn xâm nhập phòng ngủ của những người phụ nữ và cầm chiếc máy ảnh trên tay, <#0.3#> hắn tìm thấy một thứ quyền lực không bị ràng buộc: <#0.35#> quyền định đoạt số phận... <#0.2#> và tước đoạt nhân phẩm của người khác.", 0],
    "3.11#5": ["angry", -0.04, -2, "Những bức ảnh hắn chụp không đơn thuần là sự kích thích, <#0.2#> mà là bằng chứng để nuôi dưỡng cái tôi ái kỷ bệnh hoạn của hắn: <#0.5#> Ta là kẻ đứng trên tất cả. <#0.3#> Ta kiểm soát số phận của các ngươi. <#0.3#> Và không một ai trong các ngươi... <#0.2#> có thể chạm tới ta.", 0.5],
    "3.11#9": ["neutral", -0.04, 0, None, 0],
    "3.11#10": ["neutral", -0.10, -1, None, 0.2],
    "3.11#11": ["sad", -0.06, -2, "Còn ở đây, <#0.3#> mỗi lần vi phạm... <#0.2#> hắn lại được thưởng bằng chính thứ khiến hắn không thể dừng lại.", 0.6],
    # HỒI 4 — phòng thẩm vấn: chậm, nén, rồi vỡ
    "4.03#1": ["neutral", -0.08, -1, "Chủ nhật, <#0.2#> ngày 7 tháng 2 năm 2010.", 0.2],
    "4.03#2": ["neutral", -0.06, -1, "Trụ sở cảnh sát tại Ottawa. <#0.3#> 3 giờ chiều.", 0.3],
    "4.03#5": ["surprised", -0.04, 0, "Và điểm đáng chú ý nhất nằm ở chỗ khác: <#0.4#> vị đại tá tự nguyện đến đây, <#0.2#> sau một cuộc điện thoại mời.", 0],
    "4.03#6": ["neutral", 0.0, 0, "Ông ta được đọc quyền và cảnh báo pháp lý, nhưng vẫn bình thản ngồi lại... <#0.3#> thậm chí còn đùa rằng luật sư duy nhất ông từng thuê là luật sư mua bán nhà.", 0.3],
    "4.06#3": ["surprised", -0.04, 0, None, 0.2],
    "4.06#4": ["fearful", -0.06, 0, None, 0.4],
    "4.08#4": ["happy", 0.0, 1, "Và vị đại tá tự tin đồng ý: <#0.3#> mẫu ADN, <#0.15#> dấu vân tay, <#0.15#> dấu giày.", 0.2],
    "4.08#5": ["neutral", -0.10, -2, "Đó là cái bẫy... <#0.2#> của sự tự tin.", 0.3],
    "4.08#7": ["neutral", -0.04, -1, "Rồi Smyth đặt lên bàn dấu giày đi tuyết thu được gần nhà nạn nhân, <#0.2#> bên cạnh dấu giày của chính Williams, <#0.3#> và nói: <#0.4#> Chúng giống hệt nhau.", 0.5],
    "4.08#9": ["neutral", -0.10, -2, "Và ông nói thẳng: <#0.5#> mọi chuyện đã kết thúc.", 0.6],
    "4.10#1": ["fearful", -0.04, 0, None, 0.3],
    "4.10#2": ["neutral", -0.04, 0, None, 0],
    "4.10#3": ["fearful", -0.06, -1, None, 0.8],
    "4.10#4": ["fearful", -0.10, -2, None, 0.2],
    "4.10#6": ["sad", -0.08, -2, None, 0.5],
    "4.10#7": ["sad", -0.08, -1, None, 0.8],
    "4.10#8": ["neutral", -0.12, -2, None, 1.2],
    "4.10#9": ["sad", -0.06, -1, None, 0.4],
    "4.11#1": ["neutral", -0.08, -1, None, 0.2],
    "4.11#2": ["fearful", -0.04, -1, None, 0],
    "4.11#3": ["neutral", -0.04, 0, None, 0.3],
    "4.11#4": ["sad", -0.06, -1, None, 0.3],
    "4.11#5": ["neutral", -0.04, 0, None, 0.2],
    "4.11#7": ["sad", -0.06, -1, None, 0.4],
    "4.11#8": ["neutral", -0.08, -1, None, 0.2],
    "4.11#9": ["sad", -0.06, -1, None, 0.4],
    "4.12#1": ["sad", -0.08, -2, None, 0.5],
    "4.12#2": ["sad", -0.08, -2, None, 0.3],
    "4.12#3": ["sad", -0.08, -2, None, 0.4],
    "4.12#4": ["neutral", -0.04, 0, None, 0.3],
    "4.12#5": ["surprised", -0.04, 0, None, 0.4],
    "4.12#6": ["sad", -0.08, -2, None, 0.6],
    # HỒI 5 — phán quyết, cảnh báo, lời kết ấm
    "5.02#1": ["neutral", -0.08, -1, "Tháng 10... <#0.2#> năm 2010.", 0.2],
    "5.02#3": ["neutral", -0.04, -1, "Ngày 18 tháng 10, <#0.2#> Russell Williams nhận tội trước toàn bộ 88 cáo buộc.", 0.2],
    "5.02#4": ["neutral", 0.02, 0, "Ba ngày sau, ngày 21, thẩm phán tuyên phạt: <#0.4#> hai mức tù chung thân chạy song song cho hai tội giết người cấp độ một, <#0.2#> thêm 10 năm cho mỗi tội tấn công tình dục, <#0.2#> thêm 10 năm cho mỗi tội giam giữ trái phép, <#0.2#> và 1 năm cho mỗi trong 82 vụ đột nhập, <#0.2#> tất cả cùng chạy song song.", 0],
    "5.02#5": ["neutral", -0.08, -2, "Mức án chung thân... <#0.2#> với 25 năm không được xét ân xá.", 0.3],
    "5.04#1": ["neutral", -0.04, 0, "Nhưng bản án lớn nhất đối với một kẻ ái kỷ như Williams... <#0.3#> là sự sụp đổ hoàn toàn về danh dự.", 0.2],
    "5.04#3": ["neutral", -0.04, -1, "Huân chương bị cắt thành từng mảnh. <#0.3#> Sắc lệnh phong cấp bị hủy bỏ.", 0.3],
    "5.04#5": ["surprised", -0.02, 0, "Quân đội Canada còn làm một việc hiếm thấy: <#0.4#> đốt quân phục và quần áo của hắn tại một cơ sở ở căn cứ Trenton vốn dùng để tiêu hủy tài liệu, <#0.3#> vì trên quần áo có tên hắn.", 0.3],
    "5.04#7": ["neutral", -0.04, 0, "Và đó là lần đầu tiên trong 25 năm phục vụ, <#0.2#> ông thấy một bộ quân phục bị đốt.", 0],
    "5.04#8": ["sad", -0.06, -1, "Nói về việc trục xuất Williams, ông Genest ví nó như một câu văn: <#0.5#> Khi đặt dấu chấm cuối câu, <#0.2#> dấu chấm ấy nhỏ thôi... <#0.3#> nhưng nó mang rất nhiều ý nghĩa.", 0.6],
    "5.06#1": ["neutral", -0.04, 0, "Khép lại tập hồ sơ đen tối này, câu hỏi quan trọng nhất để lại cho xã hội chúng ta là: <#0.4#> Làm thế nào để cộng đồng và mỗi cá nhân có thể nhận diện sớm những kẻ săn mồi... <#0.2#> ẩn mình sau những vỏ bọc hoàn hảo?", 0],
    "5.07#1": ["neutral", -0.06, 0, "Dấu hiệu thứ nhất: <#0.35#> Không bao giờ xem nhẹ các hành vi lệch lạc ranh giới ban đầu.", 0],
    "5.07#4": ["neutral", -0.06, 0, "Dấu hiệu thứ hai: <#0.35#> Sự tách rời cảm xúc bất thường.", 0],
    "5.08#1": ["neutral", -0.06, -1, None, 0],
    "5.08#2": ["neutral", -0.06, -1, None, 0.2],
    "5.08#3": ["neutral", -0.04, 0, None, 0.4],
    "5.10#1": ["sad", -0.06, -1, None, 0.2],
    "5.10#4": ["neutral", -0.06, 0, "Tội ác hiếm khi bắt đầu bằng một phát súng... <#0.2#> hay một nhát dao.", 0],
    "5.10#5": ["sad", -0.04, -1, "Nó bắt đầu từ một bước chân vượt qua lằn ranh đạo đức trong bóng tối, <#0.2#> từ một lần dung túng cho những xung lực lệch lạc nhỏ bé, <#0.3#> để rồi từng bước... <#0.2#> từng bước một... <#0.2#> trượt dài xuống vực thẳm không thể quay đầu.", 0.4],
    "5.10#7": ["sad", -0.08, -1, None, 0],
    "5.10#8": ["sad", -0.08, -1, None, 0],
    "5.10#9": ["sad", -0.04, -1, "Và một cuộc đấu trí kéo dài khoảng mười tiếng đồng hồ... <#0.3#> đủ lâu để một người đàn ông thông minh nhận ra rằng mình không còn giữ được gì nữa.", 0.4],
    "5.10#10": ["neutral", -0.08, -1, "Chúng ta hãy luôn nhớ: <#0.4#> bộ óc tinh hoa... <#0.2#> không bảo vệ được ai cả.", 0.2],
    "5.10#11": ["sad", -0.10, -2, "Nó chỉ làm cho lần sụp đổ ấy đến muộn hơn... <#0.3#> và nặng hơn.", 0.8],
    "5.12#1": ["happy", -0.02, 1, None, 0],
    "5.12#2": ["happy", -0.02, 1, None, 0],
    "5.12#3": ["happy", -0.04, 1, None, 0],
    "5.12#4": ["happy", -0.02, 2, None, 0],
}


def auto_pauses(t):
    """Ngắt nghỉ tự động cho câu không có lời đọc riêng (giống quy tắc bản EN, chữ hoa tiếng Việt)."""
    t = re.sub(r"\.\.\.\s+(?!<#)", "... <#0.45#> ", t)
    t = re.sub(r"\s[–—]\s(?!<#)", ", <#0.2#> ", t)
    t = re.sub(r":\s+(?=[^\W\d_])(?!<#)", lambda m: ": <#0.3#> ", t)
    return t


def soften(raw, alt):
    """Thử giọng 23/10 (2 vòng, chấm bằng mô hình nghe): thẻ ngắt và '...' GIỮA câu làm vụn ngữ điệu
    tiếng Việt (nhịp 3–4/10 so với 6–7 của bản liền mạch). Lời đọc dựng lại từ CÂU GỐC (giữ nguyên dấu câu),
    chỉ thêm một thẻ ngay sau dấu ':' đứng trước câu trích “…”. Kịch tính chuyển sang khoảng lặng GIỮA
    các câu (_pause_after), tắt nhạc và tiếng động."""
    q = raw.find("“")
    if q > 0:
        k = raw.rfind(":", 0, q)
        if k >= 0:
            raw = raw[:k + 1] + " <#0.35#>" + raw[k + 1:]
    s = raw.replace("“", "").replace("”", "").replace('"', "")
    if alt and "(Signature)" not in alt and "(Signature)" in s:      # 2.07#3: không đọc tiếng Anh
        s = s.replace(" (Signature)", "")
    return s


SAFE_EMO = ("neutral", "sad", "fearful", "surprised")


def main():
    acting, pause_after, last = {}, {}, None
    for e in SCRIPT:
        if e["kind"] != "LOI":
            continue
        role = N_ELEMENT.get(e["id"], e["role"])
        act = e["id"].split(".")[0]
        emo0, pitch0 = ACT_MOOD.get((act, role), ("neutral", 0))
        n = len(e["sentences"])
        for k, s in enumerate(e["sentences"], 1):
            sid = s["id"]
            text = s["text"].replace("“", "").replace("”", "").replace('"', "")
            words = len(text.split())
            if sid in KEY:
                emo, dsp, pitch, alt, after = KEY[sid]
                dsp = round(BASE_DELTA[role] + dsp, 2)
                alt = alt if alt else (auto_pauses(text) if auto_pauses(text) != text else None)
            else:
                emo, pitch = emo0, pitch0
                # tương phản theo độ dài: câu ngắn chậm + trầm để "đóng đinh", câu dài trôi nhanh hơn
                dsp = BASE_DELTA[role] + (-0.05 if words <= 8 else 0.02 if words >= 30 else 0.0)
                if words <= 8:
                    pitch -= 1
                if text.rstrip().endswith("?"):
                    emo, pitch = "surprised", pitch + 1
                # câu cuối lượt hạ xuống một bậc để khép ý
                if k == n and n > 1:
                    pitch -= 1
                dsp = round(dsp, 2)
                alt = auto_pauses(text)
                alt = alt if alt != text else None
                after = 0.0
            pitch = max(-4, min(3, pitch))         # tiếng Việt có thanh điệu: giữ cao độ trong ±4
            # BỘ THAM SỐ AN TOÀN (23/10, BaoCao_GiongDoc_Tap02.md): cao độ ≠ 0 hay cảm xúc chưa thử làm giọng
            # đổi "người". Bộ A chỉ được kiểm với neutral · sad · fearful · surprised ở cao độ 0.
            pitch = 0
            if emo not in SAFE_EMO:
                emo = "neutral"
            dsp = max(-0.06, min(0.02, dsp))       # thử 23/10: sad/fearful đã tự chậm lại; lệch thêm > 0,06 nghe kéo lê
            alt = soften(s["text"], alt)
            if alt == text:
                alt = None
            acting[sid] = [emo, dsp, pitch, alt]
            if after:
                pause_after[sid] = after
            last = sid
    out = {"_doc": __doc__.strip().splitlines()[0] + " — xem make_acting_tap02.py",
           "_pause_after": pause_after, **acting}
    (W / "acting_tap02.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    from collections import Counter
    emos = Counter(v[0] for k, v in acting.items())
    print(len(acting), "câu ·", dict(emos), "· lời đọc riêng:", sum(1 for v in acting.values() if v[3]),
          "· nghỉ thêm:", len(pause_after), f"({sum(pause_after.values()):.1f} s)")
    missing = [k for k in KEY if k not in acting]
    if missing:
        raise SystemExit(f"KEY có mã không tồn tại: {missing}")


if __name__ == "__main__":
    main()
