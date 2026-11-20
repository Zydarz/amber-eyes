# -*- coding: utf-8 -*-
with open('.work/build_tap31_216.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
text = re.sub(r'chấp nhận\s+nhận\s+[^,;\'\"]*', 'thừa nhận toàn bộ 16 cáo buộc đánh bom', text)

with open('.work/build_tap31_216.py', 'w', encoding='utf-8') as f:
    f.write(text)

print('Cleaned in python file.')
