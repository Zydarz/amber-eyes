#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh 3 ban mo ta DAI cho clip TikTok TK2/TK3/TK4 (truong Description, 4.000 ky tu).

Kiem: do dai <= 4.000 · 0 tu cam V9/A9.2 · moi moc deu truy ve
01_KICH_BAN/Ho_So_Toi_Pham/Tap01 + 02_SAN_XUAT/Ho_So_Toi_Pham/Tap01/nguon_tham_khao.md + mo ta tap 01.
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
LINK = "youtu.be/lDVXjeFLn48"

BOI_CANH = """——————
BỐI CẢNH HỒ SƠ
——————
Mùa hè 2015, Springfield (Missouri, Mỹ): Dee Dee Blanchard — biểu tượng người mẹ thánh mẫu đơn thân — được phát hiện qua đời trong căn nhà màu hồng. Con gái Gypsy Rose bị tin là mắc ung thư máu, bại liệt, loạn dưỡng cơ và thiểu năng, biến mất không dấu vết. Chỉ 48 giờ sau, khi cánh cửa phòng thẩm vấn mở ra, sự thật được phơi bày: cô bé tự bước đi bằng đôi chân của chính mình.

Chẩn đoán của tòa: FDIA — Rối loạn giả bệnh áp đặt lên người khác (DSM-5-TR, 300.19). Người mẹ đã giam cầm con gái trong nhà tù y tế nhân tạo và ép con dùng thuốc để giữ bệnh tình "bệnh nhân" — đổi lấy sự thương hại và tôn sùng của cộng đồng."""

CHI_DAU_10 = """——————
HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ (series đầy đủ)
——————
1. Dư chấn xã hội · 2. Vật hóa nạn nhân (objectification) · 3. Cơ chế chia ngăn · 4. Thái độ trước bản án · 5. Hệ thống tự bào chữa (hero complex) · 6. Ngồi nổ & điểm gãy tâm lý · 7. Chữ ký vs thủ đoạn MO · 8. Quỹ đạo leo thang hành vi · 9. Hiệu ứng hào quang · 10. Nạn nhân học & cảnh báo đỏ sinh tồn"""

NGUON = """——————
NGUỒN THAM KHẢO
——————
• Tòa án Hạt Greene: State v. Gypsy Blanchard (No. 1531-CR03746) & State v. Godejohn — courts.mo.gov
• Cảnh sát Hạt Greene: báo cáo hiện trường & họp báo Sheriff Jim Arnott — greenecountymo.gov/sheriff
• Bệnh viện Nhi Mercy (2007): bệnh án nghi vấn FDIA của BS Flasterstein — mercy.net
• APA DSM-5-TR: Rối loạn giả bệnh áp đặt lên người khác (FDIA / 300.19) — psychiatry.org
• Dr. Marc D. Feldman: 'Playing Sick? Untangling Munchausen Syndrome by Proxy' — munchausen.com
• BuzzFeed News: điều tra của Michelle Dean (2016) — buzzfeednews.com
• Springfield News-Leader: dòng thời gian vụ án — news-leader.com
• ABC News 20/20: phỏng vấn độc quyền Gypsy Rose Blanchard — abcnews.go.com
• HBO: 'Mommy Dead and Dearest' (2017) — hbo.com"""

LU_Y = """——————
LƯU Ý
——————
• Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.
• Nội dung không phù hợp cho trẻ em.
• Mang tính giáo dục, phân tích tâm lý tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên tư liệu công khai (hồ sơ tòa án, báo chí điều tra). Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Nhân vật Cú, Sói, Cáo là linh thú minh họa; lời thoại phục dựng dựa trên tư liệu điều tra.
• Hồ sơ có thật, dữ liệu có nguồn.

🆘 Nếu bạn biết một trẻ em đang bị bạo hành hoặc lạm dụng y tế, hãy gọi Tổng đài quốc gia bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7)."""

HEAD = """Tập 01 · Độc dược nhân danh tình mẹ — %s
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút): %s — link trong bio
🔎 %s"""

TK1 = """Cô ấy không ngồi trên xe lăn. Cô ấy bước đi. 👁️

%s

——————
CHỈ DẤU #2: THỦ ĐOẠN ≠ CHỮ KÝ TÂM LÝ
——————
Từ đây, tâm lý học tội phạm tách làm hai khái niệm:
• THỦ ĐOẠN (modus operandi) — những gì kẻ phạm tội làm để thực hiện hành vi và né tránh sự trừng phạt. Ở đây nó liên tục biến đổi: đổi bệnh viện, chuyển chỗ ở ngay khi một bác sĩ bắt đầu nghi ngờ.
• CHỮ KÝ TÂM LÝ (signature) — bất biến, sinh ra để thỏa mãn nhu cầu cảm xúc bệnh lý cốt lõi. Ở đây là tước đoạt tuổi trưởng thành: khai man ngày sinh, biến cô con gái hai mươi tuổi thành một đứa trẻ mười sáu tuổi trên giấy tờ.

Bước ngoặt tâm lý của hồ sơ này: bà ta không chỉ muốn con mình bệnh tật. Bà ta muốn con mình không bao giờ lớn.

%s

%s

%s

%s

#AmberEyes #TamLyToiPham #HosoCoThat #PhanTichTamLy #TrueCrime #MoiTuanMotTap #FDIA #GypsyRoseBlanchard #DeeDeeBlanchard #10ChiDauTamLy""" % (
    HEAD % ("chỉ dấu #2: thủ đoạn và chữ ký tâm lý.", LINK,
            "Chỉ dấu tâm lý · FDIA · hồ sơ có thật"),
    BOI_CANH, CHI_DAU_10, NGUON, LU_Y)

TK2 = """Vì sao cô ấy không bao giờ chạy trốn?

%s

——————
CHỈ DẤU #6: SỰ BẤT LỰC TẬP NHIỄM
——————
Suốt hàng chục năm trời, trước mặt hàng trăm bác sĩ, y tá, cảnh sát và các tình nguyện viên thiện nguyện, cô ấy chưa từng một lần đứng bật dậy khỏi chiếc xe lăn để kêu cứu. Để trả lời, ta phải nhìn vào hai cơ chế giam hãm nhận thức: sự bất lực tập nhiễm và gắn kết chấn thương.

• BẤT LỰC TẬP NHIỄM (learned helplessness) — Năm 1967, nhà tâm lý học Martin Seligman công bố thí nghiệm kinh điển: những kích thích không thể tránh và không thể lùi dạy con vật rằng mọi phản kháng đều vô nghĩa. Kể cả khi người ta mở toang cửa lồng và không còn dòng điện nào cản trở, con vật vẫn nằm im cam chịu. Bộ não bị tổn thương tâm lý sâu sắc sẽ đi đến một kết luận cố định: mọi sự kháng cự đều là vô nghĩa.
• GẮN KẾT CHẤN THƯƠNG — Mỗi lần con gái ngồi trước mặt bác sĩ, bàn tay mẹ luôn nắm chặt. Người ngoài nhìn vào tưởng đó là cái nắm tay chan chứa yêu thương. Với cô bé, đó là tín hiệu đe dọa: nếu cô bé nói sai một lời, bàn tay mẹ sẽ siết chặt hơn nữa. Đó chính là cách một đứa trẻ học được rằng phản kháng là vô ích.

%s

%s

%s
• Seligman, M. E. (1967): thí nghiệm bất lực tập nhiễm — trích trong kịch bản Tập 01 (4.07#3–#8)

%s

#AmberEyes #TamLyToiPham #HosoCoThat #LearnedHelplessness #TraumaBonding #TamLyHoc #FDIA #GypsyRoseBlanchard""" % (
    HEAD % ("chỉ dấu #6: sự bất lực tập nhiễm (Seligman, 1967).", LINK,
            "Chỉ dấu tâm lý · Learned Helplessness · hồ sơ có thật"),
    BOI_CANH, CHI_DAU_10, NGUON, LU_Y)

TK3 = """Bà ta không cần tiền. Bà ta cần sự kính ngợng. 👁️

%s

——————
CHỈ DẤU #3: SỰ CUNG CẤP ÁI KỶ (NARCISSISTIC SUPPLY)
——————
Nhiều người nghĩ bà ta làm tất cả chỉ vì tiền trợ cấp và những chuyến đi Disneyland miễn phí. Nhưng nếu chỉ vì lòng tham tài chính, kẻ phạm tội sẽ chọn cách lừa đảo ít phiền chứ và tốn kém hơn nhiều.

Theo cẩm nang chẩn đoán tâm thần DSM-5-TR, hội chứng FDIA hoàn toàn khác với hành vi giả bệnh trục lợi:
• Kẻ giả bệnh trục lợi sẽ dựng chuyện để kiếm tiền rồi bí mật hưởng thụ trong bóng tối.
• Kẻ mắc hội chứng FDIA thì đói khát một thứ chất gây nghiện tinh vi hơn nhiều: sự cung cấp ái kỷ. Mỗi lời khen ngợi bà là người mẹ vĩ đại nhất là một liều dopamine tiêm thẳng vào não.

Trước khi sinh con, cuộc đời bà ta là một chuỗi thất bại. Nhưng khoảnh khắc bà ta khoác lên mình chiếc áo "người mẹ đơn thân kiên cường nuôi con tàn tật", toàn bộ thế giới bỗng đảo chiều.

——————
CHỈ DẤU #9: ĐIỂM MÙ XÃ HỘI
——————
Chiếc áo "người mẹ thánh mẫu đơn thân vượt khó" tạo ra một tấm khiên hoàn hảo, ru ngủ trực giác nghi ngờ của hàng xóm, bác sĩ và truyền thông suốt 23 năm. Chúng ta đã hoàn toàn tin tưởng rằng bà ấy là một vị thánh sống giữa đời thực — và chính niềm tin ấy làm điểm mù xã hội trở nên vô hình.

%s

%s

%s

%s

#AmberEyes #TamLyToiPham #HosoCoThat #NarcissisticSupply #FDIA #MoiTuanMotTap #GypsyRoseBlanchard #DeeDeeBlanchard""" % (
    HEAD % ("chỉ dấu #3 (sự cung cấp ái kỷ) và #9 (điểm mù xã hội).", LINK,
            "Chỉ dấu tâm lý · FDIA · Narcissistic Supply · hồ sơ có thật"),
    BOI_CANH, CHI_DAU_10, NGUON, LU_Y)

TK4 = """4 dấu hiệu đỏ sinh tồn — lưu lại clip này.

%s

——————
BỘ 4 CẢNH BÁO ĐỎ SINH TỒN
——————
Bốn dấu hiệu đỏ để nhận ra một đứa trẻ đang bị bệnh trong chính ngôi nhà của mình. Dưới góc độ tâm lý và lâm sàng y khoa, cộng đồng cần đặc biệt lưu tâm đến hai chỉ dấu cảnh báo đầu tiên.

① BỆNH SỬ PHỨC TẠP MÂU THUẪN XÉT NGHIỆM — Danh sách bệnh hiểm nghèo kéo dài triều miên, nhưng kết quả kiểm tra khách quan luôn bình thường hoặc trái ngược lời kể của người chăm sóc.
② TRIỆU CHỨNG CHỈ XUẤT HIỆN KHI CÓ MẶT NGƯỜI CHĂM SÓC, và lập tức thuyên giảm khi bệnh nhân được cách ly hoặc nằm trong khu vực có camera giám sát độc lập.
③ ĐỔI BÁC SĨ + NGHIỆN SỰ CHÚ Ý — Người chăm sóc liên tục đổi phòng khám ngay khi bị chất vấn, đồng thời phô trương bệnh tật của con lên mạng xã hội để tìm kiếm sự thương hại.
④ CÔ LẬP TUYỆT ĐỐI KHỎI CỘNG ĐỒNG — Nạn nhân bị cắt đứt khỏi trường học, bạn bè và người thân, dưới chiêu bài "bảo vệ sức khỏe yếu ớt".

Bốn dấu hiệu này không chỉ nằm trong một hồ sơ. Chúng là những gì cộng đồng phải biết để canh giữ trẻ em — và là thứ mỗi người nên nhìn lại trong chính gia đình mình.

%s

%s

%s

%s

#AmberEyes #TamLyToiPham #HosoCoThat #CanhGiuTreEm #LanhDanh #MoiTuanMotTap #FDIA #TamLyHoc""" % (
    HEAD % ("chỉ dấu #10: bộ 4 cảnh báo đỏ sinh tồn.", LINK,
            "Chỉ dấu tâm lý · FDIA · cảnh báo đỏ · hồ sơ có thật"),
    BOI_CANH, CHI_DAU_10, NGUON, LU_Y)

BANNED = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập",
          "đầu độc", "diệt cỏ", "bỏ đói", "móc áo", "hiếp", "cắt đầu",
          "vâng hãm", "hiếp dâm", "lột da", "ngắt tay", "bóp cổ", "trần trụi"]


def check(name, text):
    low = text.lower()
    hits = []
    for w in BANNED:
        if w in low:
            if w == "máu" and low.count("máu") == low.count("ung thư máu"):
                continue
            hits.append(w)
    n = len(text.strip())
    ok = n <= 4000 and not hits
    print("  %s: %d ky tu | tu cam: %s | %s"
          % (name, n, hits if hits else "khong co", "OK" if ok else "LOI"))
    return ok


def main():
    ok = True
    for cid, text in (("TK1", TK1), ("TK2", TK2), ("TK3", TK3), ("TK4", TK4)):
        ok = check(cid, text) and ok
    if not ok:
        print("KHONG ghi file")
        return 1
    for cid, text in (("TK1", TK1), ("TK2", TK2), ("TK3", TK3), ("TK4", TK4)):
        p = D / ("MoTa_Dai_%s.txt" % cid)
        p.write_text(text.strip(), encoding="utf-8")
        print("  -> %s" % p)
    return 0


if __name__ == "__main__":
    sys.exit(main())
