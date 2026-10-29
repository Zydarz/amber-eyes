import io
import sys

PATH = r"D:\TEST\Gax\Audi\01_KICH_BAN\Tap03\kichban_tap03_22102026.md"

with io.open(PATH, encoding="utf-8") as f:
    src = f.read()

FIXES = [
    # (a) remove duplicated closing line in Hoi 3 (CHUYEN GIA 3.08)
    (
        "Đó là hình hài của một đứa trẻ bị người mẹ hủy hoại: hắn không thèm giết bà, hắn chỉ muốn khiến bà hiểu rằng mình đã làm điều khủng khiếp.\nVà đây là điểm mấu chốt: **Bộ não của Kemper đã tìm kiếm những nạn nhân thay thế**.\"",
        "Đó là hình hài của một đứa trẻ bị người mẹ hủy hoại: hắn không thèm giết bà, hắn chỉ muốn khiến bà hiểu rằng mình đã làm điều khủng khiếp.\"",
    ),
    # (b) 1.12#6 -> 2 sentences
    (
        "Hắn là ca nghiên cứu đầu tiên của Dự án Nghiên cứu Tính Cách Tội Phạm (Criminal Personality Research Project) của Bộ phận Khoa học Hành vi – và những ghi chép của hắn cùng với hai mươi mấy tù nhân giết người khác đã trở thành nền móng để Cục xây dựng mạng lưới VICAP, nơi lưu trữ và đối chiếu hồ sơ các vụ án giết người hàng loạt.",
        "Hắn là ca nghiên cứu đầu tiên của Dự án Nghiên cứu Tính Cách Tội Phạm (Criminal Personality Research Project) của Bộ phận Khoa học Hành vi.\nNhững ghi chép của hắn cùng với hai mươi mấy tù nhân giết người khác đã trở thành nền móng để Cục xây dựng mạng lưới VICAP, nơi lưu trữ và đối chiếu hồ sơ các vụ án giết người hàng loạt.",
    ),
    # (c) 4.02#4 -> 2 sentences
    (
        "Đó là Đặc vụ John Douglas và Robert Ressler – hai nhà tiên phong thuộc Bộ phận Khoa học Hành vi (Behavioral Science Unit – BSU) của Cục Điều tra Liên bang FBI, một đơn vị mới thành lập được vài năm và đang bắt đầu đi tìm câu trả lời cho câu hỏi lớn nhất của ngành: **Bộ não của chúng thực sự vận hành như thế nào?**",
        "Đó là Đặc vụ John Douglas và Robert Ressler – hai nhà tiên phong thuộc Bộ phận Khoa học Hành vi (Behavioral Science Unit – BSU) của Cục Điều tra Liên bang FBI, một đơn vị mới thành lập được vài năm.\nHọ đang bắt đầu đi tìm câu trả lời cho câu hỏi lớn nhất của ngành: **Bộ não của chúng thực sự vận hành như thế nào?**",
    ),
    # (d) 4.08#4 -> 2 sentences
    (
        "Họ hiểu được rằng hiện trường vụ án không chỉ để lại dấu vết vật lý như máu hay vân tay, mà còn để lại **Chữ ký tâm lý (Behavioral Signature)** của kẻ thủ ác – thứ mà chính Kemper đã thực hiện một cách hoàn hảo, từ việc rút đạn ra khỏi thi thể đến việc chôn đầu nạn nhân trong vườn nhà mẹ.",
        "Họ hiểu được rằng hiện trường vụ án không chỉ để lại dấu vết vật lý như máu hay vân tay, mà còn để lại **Chữ ký tâm lý (Behavioral Signature)** của kẻ thủ ác.\nĐó chính là thứ mà Kemper đã thực hiện một cách hoàn hảo, từ việc rút đạn ra khỏi thi thể đến việc chôn đầu nạn nhân trong vườn nhà mẹ.",
    ),
    # (e) 4.08#5 -> 2 sentences
    (
        "Những tư liệu thu được từ bộ óc IQ 145 của Kemper cùng với hai mươi mấy hồ sơ khác đã trở thành nền móng cho hàng trăm vụ án được phá giải bằng phương pháp phân tích hành vi sau này, và là nguồn cảm hứng bất tận cho các tác phẩm kinh điển như *The Silence of the Lambs (Sự im lặng của bầy cừu)* hay loạt phim *Mindhunter*.",
        "Những tư liệu thu được từ bộ óc IQ 145 của Kemper cùng với hai mươi mấy hồ sơ khác đã trở thành nền móng cho hàng trăm vụ án được phá giải bằng phương pháp phân tích hành vi sau này.\nChúng cũng là nguồn cảm hứng bất tận cho các tác phẩm kinh điển như *The Silence of the Lambs (Sự im lặng của bầy cừu)* hay loạt phim *Mindhunter*.",
    ),
    # (f) 5.02#6 -> 2 sentences
    (
        "Và trong lời nói cuối cùng trước tòa, gã khổng lồ IQ 145 đã đưa ra một yêu cầu chưa từng có trong lịch sử tư pháp: Hắn yêu cầu bồi thẩm đoàn tuyên án tử hình mình bằng hình thức tra tấn đến chết, để trả giá cho những đau đớn mà hắn đã gây ra.",
        "Và trong lời nói cuối cùng trước tòa, gã khổng lồ IQ 145 đã đưa ra một yêu cầu chưa từng có trong lịch sử tư pháp.\nHắn yêu cầu bồi thẩm đoàn tuyên án tử hình mình bằng hình thức tra tấn đến chết, để trả giá cho những đau đớn mà hắn đã gây ra.",
    ),
    # (g) 2.06#1 -> 2 sentences
    (
        "Thi thể của họ sau đó được tìm thấy rải rác dưới những vực sâu hẻo hánh dọc theo dãy núi Santa Cruz, và một thi thể được chôn ngay trong khu vườn sau nhà mẹ Kemper – hắn chôn đầu cô Schall quay lên trời, vì mẹ hắn 'luôn muốn người ta ngước nhìn lên'.",
        "Thi thể của họ sau đó được tìm thấy rải rác dưới những vực sâu hẻo hánh dọc theo dãy núi Santa Cruz.\nMột thi thể được chôn ngay trong khu vườn sau nhà mẹ Kemper – hắn chôn đầu cô Schall quay lên trời, vì mẹ hắn 'luôn muốn người ta ngước nhìn lên'.",
    ),
    # (h) 1.03#6 -> 2 sentences
    (
        "Đó là 'Big Ed' – một gã thanh niên 24 tuổi, cao 2 mét 06 (6 feet 9 inch), nặng khoảng 127 ký (280 pounds), người thường xuyên đến quán rượu The Jury Room ngồi uống bia và trò chuyện thân mật với các sĩ quan cảnh sát sau giờ tuần tra.",
        "Đó là 'Big Ed' – một gã thanh niên 24 tuổi, cao 2 mét 06 (6 feet 9 inch), nặng khoảng 127 ký (280 pounds).\nHắn thường xuyên đến quán rượu The Jury Room ngồi uống bia và trò chuyện thân mật với các sĩ quan cảnh sát sau giờ tuần tra.",
    ),
    # (i) 5.05#3 -> 2 sentences
    (
        "Trong hồ sơ Kemper, chỉ dấu đầu tiên là có thật và rõ ràng: năm 10 tuổi, cậu bé chôn sống một con mèo, đào lên khi nó đã chết, chặt đầu nó và cắm đầu lên một cọc sắt; ba năm sau, cậu lại chặt đầu một con mèo khác và bày trên đĩa.",
        "Trong hồ sơ Kemper, chỉ dấu đầu tiên là có thật và rõ ràng.\nNăm 10 tuổi, cậu bé chôn sống một con mèo, đào lên khi nó đã chết, chặt đầu nó và cắm đầu lên một cọc sắt. Ba năm sau, cậu lại chặt đầu một con mèo khác và bày trên đĩa.",
    ),
]

for i, (old, new) in enumerate(FIXES, 1):
    n = src.count(old)
    if n != 1:
        print(f"FIX {i}: MATCHED {n} TIMES -> ABORT (expected 1)")
        print("  old:", old[:90])
        sys.exit(1)
    src = src.replace(old, new, 1)
    print(f"FIX {i}: ok")

with io.open(PATH, "w", encoding="utf-8", newline="\n") as f:
    f.write(src)
print("written:", PATH)
