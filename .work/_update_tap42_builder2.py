# -*- coding: utf-8 -*-
with open('.work/_build_tap42_multilingual.py', 'r', encoding='utf-8') as f:
    s = f.read()

# VN:
s = s.replace(
    '"Để trả lời câu hỏi nhức nhối này, chúng ta cần lắng nghe chính lời khai đầy giằng xé của người trong cuộc,"',
    '"Để trả lời câu hỏi nhức nhối này, chúng ta cần lắng nghe chính lời khai đầy giằng xé của người trong cuộc;"'
)
s = s.replace(
    'hồ sơ Marc Dutroux mãi mãi là một bài học xương máu',
    'hồ sơ Marc Dutroux mãi là một bài học xương máu'
)

# EN:
s = s.replace(
    '"To answer this agonizing question, we must first hear the conflicted testimony of the accomplice herself,"',
    '"To answer this agonizing question, we must first hear the conflicted testimony of the accomplice herself;"'
)

# JA:
s = s.replace(
    '"しかし、人間が真実を直視し続け、コミュニティが互いを守るために連帯し続ける限りにおいて、"',
    '"しかし、人間が真実を直視し続け、コミュニティが互いを守るために連帯し続ける限りにおいて、光は決して消え去りません。"'
)
s = s.replace(
    '"Thì bóng tối sẽ không bao giờ có thể chiến thắng được ánh sáng của công lý."',
    '"Bóng tối sẽ không bao giờ có thể chiến thắng được ánh sáng của công lý."'
)
s = s.replace(
    '"The shadows will never extinguish the resilient dawn of justice."',
    '"Shadows will never extinguish the resilient dawn of justice."'
)
s = s.replace(
    '"いかなる暗黒も正義の黎明の光を永久に呑み込むことはできません。"',
    '"いかなる暗黒も、正義の黎明の光を永久に呑み込むことはできないのです。"'
)

with open('.work/_build_tap42_multilingual.py', 'w', encoding='utf-8') as f:
    f.write(s)

print("Updated .work/_build_tap42_multilingual.py (pass 2).")
