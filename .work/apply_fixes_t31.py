# -*- coding: utf-8 -*-
with open('.work/build_tap31_216.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. VN fixes:
# 'sự hy sinh sinh mạng' -> 'sự hy sinh mạng sống'
text = text.replace('sự hy sinh sinh mạng của một vài cá nhân', 'sự hy sinh mạng sống của một vài cá nhân')

# 'thiếu hụt hoàn toàn của thấu cảm cảm xúc' -> 'thiếu hụt hoàn toàn của năng lực thấu cảm'
text = text.replace('thiếu hụt hoàn toàn của thấu cảm cảm xúc', 'thiếu hụt hoàn toàn của năng lực thấu cảm')

# 'chấp nhận nhận tội' -> 'chấp nhận nhận toàn bộ tội danh'
text = text.replace('chấp nhận nhận tội toàn bộ 16 vụ đánh bom', 'chấp nhận nhận toàn bộ tội danh trong 16 vụ đánh bom')

# 2. EN fixes (apostrophes):
text = text.replace('The attacker targets shifted relentlessly', "The attacker's targets shifted relentlessly")
text = text.replace('from the perpetrator primary targets', "from the perpetrator's primary targets")
text = text.replace('The perpetrator lethality escalated', "The perpetrator's lethality escalated")
text = text.replace('the Unabomber first homicide', "the Unabomber's first homicide")
text = text.replace('into every scholar mind', "into every scholar's mind")
text = text.replace('Please spare my brother life', "Please spare my brother's life")
text = text.replace('Ted 1971 23-page essay was laid upon Fitzgerald analytical desk', "Ted's 1971 23-page essay was laid upon Fitzgerald's analytical desk")
text = text.replace('Armed with Fitzgerald 50-page forensic linguistic affidavit', "Armed with Fitzgerald's 50-page forensic linguistic affidavit")
text = text.replace('pierced the Unabomber secretive universe', "pierced the Unabomber's secretive universe")
text = text.replace('families of Ted bombings', "families of Ted's bombings")
text = text.replace('maimed by Ted bomb in Salt Lake City', "maimed by Ted's bomb in Salt Lake City")
text = text.replace('Entering the 1990s, the Unabomber rage escalated', "Entering the 1990s, the Unabomber's rage escalated")

with open('.work/build_tap31_216.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated build_tap31_216.py successfully.')
