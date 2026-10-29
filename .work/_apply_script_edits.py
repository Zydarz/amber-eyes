import sys, subprocess
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

kb_path = Path("01_KICH_BAN/Tap07/kichban_tap07_23102026.md")
text = kb_path.read_text(encoding="utf-8")

# Replacements
replacements = [
    (
        'Bên trong cabin xe là thi thể của chàng trai trẻ mười tám tuổi Conrad Henri Roy Đệ Tam.',
        'Bên trong cabin xe, chàng trai trẻ mười tám tuổi Conrad Henri Roy Đệ Tam nằm bất động.'
    ),
    (
        'Cậu vừa trút hơi thở cuối cùng trong một không gian ngập tràn chất khí độc hại được tạo ra từ một chiếc máy bơm nước chạy bằng xăng.',
        'Cậu vừa trút hơi thở cuối cùng trong không gian ngột ngạt ngập tràn khí thải nguy hại.'
    ),
    (
        'Michelle viết cho Conrad: Anh lúc nào cũng nói sẽ làm, nhưng anh chẳng bao giờ làm cả. Em cá là tối nay anh lại tìm cớ trì hoãn cho mà xem. Thời điểm chín muồi rồi, anh đã sẵn sàng, anh chỉ cần làm ngay thôi. Không còn chần chừ gì nữa. Hãy làm đi.',
        'Michelle viết cho Conrad: “Anh lúc nào cũng nói sẽ làm, nhưng anh chẳng bao giờ làm cả. Em cá là tối nay anh lại tìm cớ trì hoãn cho mà xem. Thời điểm chín muồi rồi, anh đã sẵn sàng, anh chỉ cần làm ngay thôi. Không còn chần chừ gì nữa. Hãy làm đi.”'
    ),
    (
        'Cô ta nhắn tin: Bố mẹ anh sẽ hiểu cho anh thôi. Họ sẽ đau buồn một thời gian, nhưng sau đó họ sẽ biết rằng anh đang ở một nơi thanh thản hơn. Bố mẹ anh rồi sẽ chấp nhận sự thật và sống tiếp.',
        'Cô ta nhắn tin: “Bố mẹ anh sẽ hiểu cho anh thôi. Họ sẽ đau buồn một thời gian, nhưng sau đó họ sẽ biết rằng anh đang ở một nơi thanh thản hơn. Bố mẹ anh rồi sẽ chấp nhận sự thật và sống tiếp.”'
    ),
    (
        'Thay vào đó, cô ta ra lệnh dứt khoát qua điện thoại: Hãy trèo trở lại vào trong xe ngay lập tức.',
        'Thay vào đó, cô ta ra lệnh dứt khoát qua điện thoại: “Hãy trèo trở lại vào trong xe ngay lập tức.”'
    ),
    (
        'Michelle nhắn cho tôi nguyên văn rằng: Cái chết của Conrad là lỗi của tớ. Thật sự tớ đã có thể ngăn anh ấy lại. Tớ đã nói chuyện điện thoại với anh ấy, và khi khí bắt đầu ngập xe, anh ấy sợ hãi trèo ra ngoài. Nhưng tớ đã bảo anh ấy hãy trèo trở lại vào trong xe.',
        'Michelle nhắn cho tôi nguyên văn rằng: “Cái chết của Conrad là lỗi của tớ. Thật sự tớ đã có thể ngăn anh ấy lại. Tớ đã nói chuyện điện thoại với anh ấy, và khi khí bắt đầu ngập xe, anh ấy sợ hãi trèo ra ngoài. Nhưng tớ đã bảo anh ấy hãy trèo trở lại vào trong xe.”'
    ),
    (
        'Thẩm phán Moniz nhận định: Khi Conrad Roy bước chân ra khỏi cabin chiếc xe tải vì ngạt thở, đó là khoảnh khắc chàng trai trẻ đã lựa chọn sự sống. Hành vi của nạn nhân đã tạm dừng chuỗi tự hủy hoại. Nhưng chính vào thời điểm sinh tử đó, Michelle Carter đã ra lệnh cho cậu phải trèo trở lại vào trong xe. Việc ép buộc nạn nhân cùng với việc hoàn toàn không gọi trợ giúp dù có đầy đủ phương tiện trong tay đã cấu thành một hành vi liều lĩnh, vô lương tâm và nguy hiểm nghiêm trọng. Hành động đó đã trực tiếp tước đoạt cơ hội sống sót duy nhất của nạn nhân.',
        'Thẩm phán Moniz nhận định: “Khi Conrad Roy bước chân ra khỏi cabin chiếc xe tải vì ngạt thở, đó là khoảnh khắc chàng trai trẻ đã lựa chọn sự sống. Hành vi của nạn nhân đã tạm dừng chuỗi tự hủy hoại. Nhưng chính vào thời điểm sinh tử đó, Michelle Carter đã ra lệnh cho cậu phải trèo trở lại vào trong xe. Việc ép buộc nạn nhân cùng với việc hoàn toàn không gọi trợ giúp dù có đầy đủ phương tiện trong tay đã cấu thành một hành vi liều lĩnh, vô lương tâm và nguy hiểm nghiêm trọng. Hành động đó đã trực tiếp tước đoạt cơ hội sống sót duy nhất của nạn nhân.”'
    )
]

for old, new in replacements:
    if old in text:
        text = text.replace(old, new, 1)
    else:
        print(f"Warning: pattern not found: {old[:40]}...")

kb_path.write_text(text, encoding="utf-8")
print(f"Updated {kb_path} successfully!")

# Parse to script_tap07.json
res = subprocess.run([sys.executable, ".work/parse_kichban.py", str(kb_path), ".work/script_tap07.json"], capture_output=True, text=True)
print("Parse stdout:", res.stdout)
print("Parse stderr:", res.stderr)
