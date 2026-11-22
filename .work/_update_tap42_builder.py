# -*- coding: utf-8 -*-
with open('.work/_build_tap42_multilingual.py', 'r', encoding='utf-8') as f:
    s = f.read()

# 1. VN: Line ending comma -> period or semicolon, fix ellipsis
s = s.replace(
    '"Trước khi chuyên gia tâm lý bóc tách từng tầng nhận thức sâu kín nhất của bản ngã con người."',
    '"trước khi chuyên gia tâm lý bóc tách từng tầng nhận thức sâu kín nhất của bản ngã con người."'
)
s = s.replace(
    '"Thế nhưng, chừng nào con người còn biết lắng nghe sự thật, chừng nào cộng đồng còn biết đoàn kết và bảo vệ lẫn nhau,"',
    '"Thế nhưng, chừng nào con người còn biết lắng nghe sự thật, chừng nào cộng đồng còn biết đoàn kết và bảo vệ lẫn nhau;"'
)
s = s.replace(
    '"Tôi xin lỗi những người làm cha, làm mẹ... dù tôi biết hàng ngàn lời xin lỗi cũng vĩnh viễn là không bao giờ đủ."',
    '"Tôi xin lỗi những người làm cha, làm mẹ; dù tôi biết hàng ngàn lời xin lỗi cũng vĩnh viễn là không bao giờ đủ."'
)
s = s.replace(
    '"Hành vi ngoan ngoãn nghe lời hay dạ bảo vâng vâng không phải là sự đồng cảm',
    '"Hành vi ngoan ngoãn nghe lời hay bảo gì nghe nấy không phải là sự đồng cảm'
)

# 2. EN:
s = s.replace(
    '"Before our criminal psychologist dissects the deepest subconscious strata of this fragmented self."',
    '"before our criminal psychologist dissects the deepest subconscious strata of this fragmented self."'
)
s = s.replace(
    '"Yet so long as humanity champions truth, so long as communities unite to shield one another fiercely,"',
    '"Yet so long as humanity champions truth, so long as communities unite to shield one another fiercely;"'
)
s = s.replace(
    '"I beg the forgiveness of those grieving parents... though I know millions of apologies can never suffice."',
    '"I beg the forgiveness of those grieving parents; though I know millions of apologies can never suffice."'
)

# 3. JA:
s = s.replace(
    '"しかし、人間が真実を直視し続け、コミュニティが互いを守るために連帯し続ける限り、"',
    '"しかし、人間が真実を直視し続け、コミュニティが互いを守るために連帯し続ける限りにおいて、"'
)
s = s.replace(
    '"遺族である親御さんたちに心からお詫び申し上げます…何千、何万の謝罪の言葉を重ねようとも、決して許されるはずがないと知りながら。"',
    '"遺族である親御さんたちに心からお詫び申し上げます。何千、何万の謝罪の言葉を重ねようとも、決して許されるはずがないと知りながら。"'
)

with open('.work/_build_tap42_multilingual.py', 'w', encoding='utf-8') as f:
    f.write(s)

print("Updated .work/_build_tap42_multilingual.py successfully.")
