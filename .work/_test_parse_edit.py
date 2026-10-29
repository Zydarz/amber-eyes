import sys, json, re
sys.stdout.reconfigure(encoding="utf-8")

# Let's test the edit on memory and parse it using parse_kichban logic
from pathlib import Path
sys.path.append(".work")
import parse_kichban

# Read original file
orig_text = Path("01_KICH_BAN/Tap07/kichban_tap07_23102026.md").read_text(encoding="utf-8")

# Apply replacements
mod_text = orig_text.replace(
    'Bên trong cabin xe là thi thể của chàng trai trẻ mười tám tuổi Conrad Henri Roy Đệ Tam.',
    'Bên trong cabin xe, chàng trai trẻ mười tám tuổi Conrad Henri Roy Đệ Tam nằm bất động.'
).replace(
    'Cậu vừa trút hơi thở cuối cùng trong một không gian ngập tràn chất khí độc hại được tạo ra từ một chiếc máy bơm nước chạy bằng xăng.',
    'Cậu vừa trút hơi thở cuối cùng trong không gian ngột ngạt ngập tràn khí thải nguy hại.'
).replace(
    'Michelle viết cho Conrad: Anh lúc nào cũng nói sẽ làm, nhưng anh chẳng bao giờ làm cả. Em cá là tối nay anh lại tìm cớ trì hoãn cho mà xem. Thời điểm chín muồi rồi, anh đã sẵn sàng, anh chỉ cần làm ngay thôi. Không còn chần chừ gì nữa. Hãy làm đi.',
    'Michelle viết cho Conrad: “Anh lúc nào cũng nói sẽ làm, nhưng anh chẳng bao giờ làm cả. Em cá là tối nay anh lại tìm cớ trì hoãn cho mà xem. Thời điểm chín muồi rồi, anh đã sẵn sàng, anh chỉ cần làm ngay thôi. Không còn chần chừ gì nữa. Hãy làm đi.”'
).replace(
    'Cô ta nhắn tin: Bố mẹ anh sẽ hiểu cho anh thôi. Họ sẽ đau buồn một thời gian, nhưng sau đó họ sẽ biết rằng anh đang ở một nơi thanh thản hơn. Bố mẹ anh rồi sẽ chấp nhận sự thật và sống tiếp.',
    'Cô ta nhắn tin: “Bố mẹ anh sẽ hiểu cho anh thôi. Họ sẽ đau buồn một thời gian, nhưng sau đó họ sẽ biết rằng anh đang ở một nơi thanh thản hơn. Bố mẹ anh rồi sẽ chấp nhận sự thật và sống tiếp.”'
).replace(
    'Thay vào đó, cô ta ra lệnh dứt khoát qua điện thoại: Hãy trèo trở lại vào trong xe ngay lập tức.',
    'Thay vào đó, cô ta ra lệnh dứt khoát qua điện thoại: “Hãy trèo trở lại vào trong xe ngay lập tức.”'
).replace(
    'Michelle nhắn cho tôi nguyên văn rằng: Cái chết của Conrad là lỗi của tớ. Thật sự tớ đã có thể ngăn anh ấy lại. Tớ đã nói chuyện điện thoại với anh ấy, và khi khí bắt đầu ngập xe, anh ấy sợ hãi trèo ra ngoài. Nhưng tớ đã bảo anh ấy hãy trèo trở lại vào trong xe.',
    'Michelle nhắn cho tôi nguyên văn rằng: “Cái chết của Conrad là lỗi của tớ. Thật sự tớ đã có thể ngăn anh ấy lại. Tớ đã nói chuyện điện thoại với anh ấy, và khi khí bắt đầu ngập xe, anh ấy sợ hãi trèo ra ngoài. Nhưng tớ đã bảo anh ấy hãy trèo trở lại vào trong xe.”'
).replace(
    'Thẩm phán Moniz nhận định: Khi Conrad Roy bước chân ra khỏi cabin chiếc xe tải vì ngạt thở, đó là khoảnh khắc chàng trai trẻ đã lựa chọn sự sống. Hành vi của nạn nhân đã tạm dừng chuỗi tự hủy hoại. Nhưng chính vào thời điểm sinh tử đó, Michelle Carter đã ra lệnh cho cậu phải trèo trở lại vào trong xe. Việc ép buộc nạn nhân cùng với việc hoàn toàn không gọi trợ giúp dù có đầy đủ phương tiện trong tay đã cấu thành một hành vi liều lĩnh, vô lương tâm và nguy hiểm nghiêm trọng. Hành động đó đã trực tiếp tước đoạt cơ hội sống sót duy nhất của nạn nhân.',
    'Thẩm phán Moniz nhận định: “Khi Conrad Roy bước chân ra khỏi cabin chiếc xe tải vì ngạt thở, đó là khoảnh khắc chàng trai trẻ đã lựa chọn sự sống. Hành vi của nạn nhân đã tạm dừng chuỗi tự hủy hoại. Nhưng chính vào thời điểm sinh tử đó, Michelle Carter đã ra lệnh cho cậu phải trèo trở lại vào trong xe. Việc ép buộc nạn nhân cùng với việc hoàn toàn không gọi trợ giúp dù có đầy đủ phương tiện trong tay đã cấu thành một hành vi liều lĩnh, vô lương tâm và nguy hiểm nghiêm trọng. Hành động đó đã trực tiếp tước đoạt cơ hội sống sót duy nhất của nạn nhân.”'
)

# Test parse
tmp_path = Path(".work/_temp_kichban_test.md")
tmp_path.write_text(mod_text, encoding="utf-8")
tmp_json = Path(".work/_temp_script_test.json")

# Run parse_kichban
import subprocess
res = subprocess.run([sys.executable, ".work/parse_kichban.py", str(tmp_path), str(tmp_json)], capture_output=True, text=True)
print("Parse output:", res.stdout, res.stderr)

parsed = json.loads(tmp_json.read_text(encoding="utf-8"))
total_sents = sum(len(el.get("sentences", [])) for el in parsed if el.get("kind") == "LOI")
print(f"Total elements: {len(parsed)}, Total sentences: {total_sents}")

# Compare sentence count per element
with open(".work/script_tap07.json", "r", encoding="utf-8") as f:
    orig_parsed = json.load(f)

orig_sents = [s["id"] for el in orig_parsed if el.get("kind") == "LOI" for s in el.get("sentences", [])]
new_sents = [s["id"] for el in parsed if el.get("kind") == "LOI" for s in el.get("sentences", [])]

print(f"Original sentences: {len(orig_sents)}, New sentences: {len(new_sents)}")
if orig_sents == new_sents:
    print("EXACT SENTENCE ID MATCH 100%!")
else:
    print("MISMATCH!")
