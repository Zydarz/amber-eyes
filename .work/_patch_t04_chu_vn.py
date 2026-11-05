#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Bản vá cột Chữ VN Tập 04 — sửa các mảnh không liên tục trong câu."""
from pathlib import Path

P = Path(__file__).resolve().parent / "_t04_chu_vn.py"
src = P.read_text(encoding="utf-8")

FIX = [
    ("RƠI VÀO CƠN LOẠN NHỊP KỊP PHÁT RỒI TRỤY TIM", "RƠI VÀO CƠN LOẠN NHỊP KỊCH PHÁT RỒI TRỤY TIM"),
    ("**CULLEN THỪA NHẬN SÁT HẠI** · *Tòa xác nhận 29 nạn nhân*",
     "**CULLEN THỪA NHẬN** · *Sát hại khoảng 40 bệnh nhân* · *Cơ quan công tố xác nhận 29 nạn nhân*"),
    ("**KHAI THÁC KẼ HỞ QUẢN LÝ KỸ THUẬT SỐ** · *Chiếc máy cấp phát thuốc tự động*",
     "**KHAI THÁC TRIỆT ĐỂ NHỮNG KẼ HỞ** · *Quản lý kỹ thuật số thời kỳ đầu* · *Chiếc máy cấp phát thuốc tự động*"),
    ("*Mỗi y tá đăng nhập bằng mã số cá nhân*", "*Mỗi y tá phải dùng mã số cá nhân để đăng nhập*"),
    ("*Thuốc độc bảng A: Digoxin, Insulin hay Norepinephrine*", "*Thuốc độc bảng A* · *Digoxin, Insulin hay Norepinephrine*"),
    ("**VIÊN THUỐC ĐỘC NẰM GỌN TRONG TÚI ÁO**", "**VIÊN THUỐC ĐỘC** · *Nằm gọn trong túi áo của Cullen*"),
    ("*Sinh mệnh yếu ớt nhất, gắn chặt vào dây truyền dịch*", "*Sinh mệnh yếu ớt nhất, bị gắn chặt vào dây truyền dịch*"),
    ("*Biến bệnh nhân vô tội thành công cụ thỏa mãn bản năng*", "*Biến những bệnh nhân vô tội thành công cụ thỏa mãn bản năng*"),
    ("*Bệnh nhân bị giáng cấp thành “đạo cụ sống”*", "*Bệnh nhân bị giáng cấp thành những “đạo cụ sống”*"),
    ("*Quyền quyết định ai được thở, ai phải dừng lại*", "*Quyền quyết định ai được thở và ai phải dừng lại*"),
    ("*Công cụ hợp thức hóa sự tha hóa nhân cách*", "*Công cụ để hợp thức hóa sự tha hóa nhân cách*"),
    ("*Chuyên gia tâm lý giải phẫu sang chấn nguồn cội*", "*Chuyên gia tâm lý giải phẫu những sang chấn nguồn cội*"),
    ("*Bệnh viện đã tự ý hỏa táng*", "*Đã tự ý hỏa táng mà không hề thông báo*"),
    ("**MỐI THÙ HẰN ÂM Ỉ VỚI CÁC THỂ CHẾ Y TẾ**", "**MỐI THÙ HẰN ÂM Ỉ ĐỐI VỚI CÁC THỂ CHẾ Y TẾ**"),
    ("*Không phải tìm kiếm sự cứu rỗi*", "*Không phải là con đường tìm kiếm sự cứu rỗi*"),
    ("*Nhận ra dấu hiệu tâm thần bất ổn*", "*Nhận ra những dấu hiệu tâm thần bất ổn*"),
    ("*Thám tử Tim Braun và Danny Baldwin*", "*Hai thám tử kỳ cựu Tim Braun và Danny Baldwin*"),
    ("*Bệnh viện trì hoãn giao nộp tài liệu*", "*Bệnh viện tìm cách trì hoãn giao nộp tài liệu*"),
    ("*Nữ y tá ca đêm tài năng, bạn thân nhất của Charles Cullen*", "*Nữ y tá ca đêm tài năng* · *Bạn thân nhất của Charles Cullen*"),
    ("*Một mình nuôi hai con nhỏ và mang bệnh cơ tim*", "*Một mình nuôi hai con nhỏ* · *Mang trong mình căn bệnh cơ tim*"),
    ("**LỚP MẶT NẠ ĐIỀM TĨNH BẮT ĐẦU RẠN NỨT**", "**LỚP MẶT NẠ ĐIỀM TĨNH** · *Bắt đầu rạn nứt*"),
    ("**KHAI THÁC ẢO TƯỞNG VỀ LÒNG NHÂN TỪ**", "**KHAI THÁC CHÍNH ẢO TƯỞNG VỀ LÒNG NHÂN TỪ**"),
    ("**CULLEN KHÓC NẤC LÊN VÀ SUY SỤP HOÀN TOÀN**", "**KHÓC NẤC LÊN VÀ SUY SỤP HOÀN TOÀN**"),
    ("**GIỌT NƯỚC MẮT TRONG PHÒNG HỎI CUNG** · *Không dành cho các nạn nhân xấu số*",
     "**GIỌT NƯỚC MẮT** · *Trong phòng hỏi cung* · *Không hề dành cho các nạn nhân xấu số*"),
    ("*Không một tia trắc ẩn nào cho những người đã khuất*", "*Không hề có một tia trắc ẩn nào cho những người đã khuất*"),
    ("*Ghi nhận những bất thường, phát hiện thuốc mất tích*", "*Ghi nhận những bất thường* · *Từng phát hiện thuốc mất tích*"),
    ("**KY NHỮNG LÁ THƯ GIỚI THIỆU TÍCH CỰC**", "**KÝ NHỮNG LÁ THƯ GIỚI THIỆU TÍCH CỰC**"),
    ("*Biến cơ sở chữa bệnh thành nơi đồng lõa*", "*Biến chính những cơ sở chữa bệnh thành nơi đồng lõa*"),
    ("**SỰ AN TOÀN BỊ XẾP SAU DANH TIẾNG VÀ TIỀN BẠC**", "**SỰ AN TOÀN CỦA CON NGƯỜI BỊ XẾP SAU DANH TIẾNG VÀ TIỀN BẠC**"),
    ("**MIỄN TRỪ TRÁCH NHIỆM PHÁP LÝ CHO CƠ SỞ Y TẾ**", "**MIỄN TRỪ TRÁCH NHIỆM PHÁP LÝ CHO CÁC CƠ SỞ Y TẾ**"),
    ("*Tái thiết kế toàn quốc*", "*Tái thiết kế trên toàn quốc*"),
]

miss = []
for old, new in FIX:
    if old not in src:
        miss.append(old)
    else:
        src = src.replace(old, new, 1)
P.write_text(src, encoding="utf-8", newline="\n")
print("đã vá:", len(FIX) - len(miss), "· không tìm thấy:", len(miss))
for m in miss:
    print("  ✗", m[:80])
