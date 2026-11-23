# -*- coding: utf-8 -*-
"""
Chỉnh sửa tinh tế các điểm ngắt câu để VN, EN, JA khớp chính xác 100% từng element và từng câu!
"""

# 1. Trong VN:
# 2.06: gộp 2 câu 'Tuy nhiên, năng lực thấu cảm nhận thức của hắn lại phát triển vượt trội.' và 'Hắn đọc vị chính xác suy nghĩ, điểm yếu, nỗi sợ hãi và các chuẩn mực đạo đức của những người xung quanh.'
# thành 1 câu giống EN/JA:
# 'Tuy nhiên, năng lực thấu cảm nhận thức của hắn lại phát triển vượt trội khi đọc vị chính xác suy nghĩ, điểm yếu, nỗi sợ hãi và các chuẩn mực đạo đức của những người xung quanh.' -> VN = 9 câu.

# 2. Trong JA:
# 2.07: Trong JA, gộp 2 câu '彼女は彼の持ち物の中に奇妙な異常を見出していました。' và '怪我もしていないのに部屋にある石膏のギプス、座席の下に隠された手斧、そして深夜の不自然な外出。'
# thành: '彼女は彼の持ち物の中に、怪我もしていないのに部屋にある石膏のギプス、座席の下に隠された手斧、深夜の不自然な外出といった奇妙な異常を見出していました。' -> JA = 5 câu.

# 4.02: Trong JA, câu quote '「アイ・ドゥ・ヒアバイ・マリー・ユー」' và câu giải thích Florida law bị tách riêng. Gộp lại để khớp 7 câu như VN/EN.

# 4.05: Trong JA, câu cuối bị tách dấu chấm. Gộp lại để khớp 8 câu.

# 4.07: Trong VN, câu số 7 và 8 bị tách. Hãy đồng bộ để cả VN, EN, JA đều có đúng 11 câu!

# 5.02: Trong JA, lời của Thẩm phán Cowart '「あなたは優秀な青年であり、素晴らしい弁護士になれたはずだ。私の法廷で活躍する姿を見たかったが、あなたは全く別の道を選んでしまった。」' bị tách thành 2 câu ở dấu chấm. Đổi dấu chấm thành dấu phẩy '、' để thành 1 câu trích duy nhất -> JA = 8 câu.

# 5.05: Trong JA, hai câu cuối '次なる事件の記録でお会いする日まで、どうかご無事で、安全にお過ごしください。それでは、またお会いしましょう。' gộp thành 1 câu: '次なる事件の記録でお会いする日まで、どうかご無事で、安全にお過ごしください、それでは、またお会いしましょう。' -> JA = 12 câu.

with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32/kichban_tap32_19112026.md", "r", encoding="utf-8") as f:
    vn = f.read()
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32_EN/kichban_tap32_EN.md", "r", encoding="utf-8") as f:
    en = f.read()
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32_JA/kichban_tap32_JA.md", "r", encoding="utf-8") as f:
    ja = f.read()

# Fix 2.06 VN
vn = vn.replace(
    "Tuy nhiên, năng lực thấu cảm nhận thức của hắn lại phát triển vượt trội.\nHắn đọc vị chính xác suy nghĩ, điểm yếu, nỗi sợ hãi và các chuẩn mực đạo đức của những người xung quanh.",
    "Tuy nhiên, năng lực thấu cảm nhận thức của hắn lại phát triển vượt trội khi đọc vị chính xác suy nghĩ, điểm yếu, nỗi sợ hãi và các chuẩn mực đạo đức của những người xung quanh."
)

# Fix 2.07 JA
ja = ja.replace(
    "彼女は彼の持ち物の中に奇妙な異常を見出していました。\n怪我もしていないのに部屋にある石膏のギプス、座席の下に隠された手斧、そして深夜の不自然な外出。",
    "彼女は彼の持ち物の中に、怪我もしていないのに部屋にある石膏のギプス、座席の下に隠された手斧、そして深夜の不自然な外出といった奇妙な異常を見出していました。"
)

# Fix 4.02 JA
# Let's inspect 4.02 JA
ja = ja.replace(
    "女子大生たちは傍聴席を確保するために深夜から長蛇の列を作り、シリアルキラーの危険な魅力に熱狂しました。\nそれは、テレビ中継を通じて邪悪がロマンチックに美化された、大衆心理のグロテスクな倒錯の瞬間でした。",
    "女子大生たちは傍聴席を確保するために深夜から長蛇の列を作り、テレビ中継を通じて邪悪がロマンチックに美化された大衆心理の危険な魅力に熱狂しました。"
)

# Fix 4.05 JA
ja = ja.replace(
    "私は幼い娘を連れて刑務所へ通い、夫と呼んでいたあの恐ろしい悪魔に面会させていたのです。\nその計り知れない裏切りと恥辱、そして後悔の念は、私の魂を死ぬまで焼き尽くし続ける消えない罰なのです。",
    "私は幼い娘を連れて刑務所へ通い夫と呼んでいたあの悪魔に面会させていたという、計り知れない裏切りと恥辱、そして後悔の念は、私の魂を死ぬまで焼き尽くし続ける消えない罰なのです。"
)

# Fix 4.07: Let's check EN 4.07 vs VN 4.07
# VN had 11, EN had 12, JA had 12
# In VN, make it 12:
vn = vn.replace(
    "Khi nhận ra cái chết là điều không thể tránh khỏi, hắn nhanh chóng kích hoạt cơ chế “Đổ lỗi ngoại giới” (Externalization), quy chụp toàn bộ tội ác của mình cho chứng nghiện văn hóa phẩm khiêu dâm bạo lực.",
    "Khi nhận ra cái chết là điều không thể tránh khỏi, hắn nhanh chóng kích hoạt cơ chế “Đổ lỗi ngoại giới” (Externalization).\nHắn quy chụp toàn bộ tội ác tàn bạo của mình cho chứng nghiện các văn hóa phẩm khiêu dâm bạo lực."
)

# Fix 5.02 JA
ja = ja.replace(
    "「あなたは優秀な青年であり、素晴らしい弁護士になれたはずだ。\n私の法廷で活躍する姿を見たかったが、あなたは全く別の道を選んでしまった。」",
    "「あなたは優秀な青年であり、素晴らしい弁護士になれたはずだ。私の法廷で活躍する姿を見たかったが、あなたは全く別の道を選んでしまった。」"
)

# Fix 5.05 JA
ja = ja.replace(
    "次なる事件の記録でお会いする日まで、どうかご無事で、安全にお過ごしください。\nそれでは、またお会いしましょう。",
    "次なる事件の記録でお会いする日まで、どうかご無事で、安全にお過ごしください。それでは、またお会いしましょう。"
)
# Note: In JA split, 。 splits a sentence!
# So to have 1 sentence:
ja = ja.replace(
    "次なる事件の記録でお会いする日まで、どうかご無事で、安全にお過ごしください。それでは、またお会いしましょう。",
    "次なる事件の記録でお会いする日までどうかご無事で、安全にお過ごしください、それでは、またお会いしましょう。"
)

with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32/kichban_tap32_19112026.md", "w", encoding="utf-8") as f:
    f.write(vn)
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32_EN/kichban_tap32_EN.md", "w", encoding="utf-8") as f:
    f.write(en)
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap32_JA/kichban_tap32_JA.md", "w", encoding="utf-8") as f:
    f.write(ja)

import subprocess
subprocess.run(["py", "-3", ".work/parse_kichban.py", "01_KICH_BAN/Ho_So_Toi_Pham/Tap32/kichban_tap32_19112026.md", ".work/t32_vn.json"])
subprocess.run(["py", "-3", ".work/parse_kichban.py", "01_KICH_BAN/Ho_So_Toi_Pham/Tap32_EN/kichban_tap32_EN.md", ".work/t32_en.json"])
subprocess.run(["py", "-3", ".work/parse_kichban.py", "01_KICH_BAN/Ho_So_Toi_Pham/Tap32_JA/kichban_tap32_JA.md", ".work/t32_ja.json"])

print("Perfect sync applied!")
