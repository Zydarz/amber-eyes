# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

line = 'Tôi nắm lấy tay Colleen và nói sự thật: “Cameron không hề thuộc về tổ chức The Company nào cả, tất cả chỉ là lời dối trá của anh ta để giam cầm cô.”\n'
s = line.strip()
t = re.sub(r'^\*\s+', '', s); t = re.sub(r'^\d+\.\s+', '', t)
t = t.replace('**', '').replace('*', '')
print('t after replace:', repr(t))
t = t.strip().strip('"“”').strip()
print('t after strip:', repr(t))

# Now let's see vn_quotes and LATIN_SPLIT
paras = [t]
# check what parse_lines does:
# LATIN_SPLIT
LATIN_SPLIT = r'(?:(?<=[.?!…])|(?<=[.?!…]”))\s+(?=[A-ZÀ-ỸĐ가-힣“(])'
parts = re.split(LATIN_SPLIT, t)
print('parts:', parts)
