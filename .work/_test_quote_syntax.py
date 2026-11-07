# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

line_vn = "Tôi nắm lấy tay Colleen và nói sự thật: 'Cameron không hề thuộc về tổ chức The Company nào cả, tất cả chỉ là lời dối trá của anh ta để giam cầm cô.'"
line_en = "I took Colleen by the hand and told her the truth: ‘Cameron does not belong to any Company, it was all an elaborate lie he invented to keep you captive.’"
line_ko = "저는 Colleen의 손을 잡고 진실을 털어놓았습니다: ‘Cameron은 The Company라는 조직에 속해 있지 않아요, 당신을 가두어 두려고 그가 지어낸 완전한 거짓말이에요.’"

for lang, line in [('VN', line_vn), ('EN', line_en), ('KO', line_ko)]:
    s = line.strip()
    t = re.sub(r'^\*\s+', '', s); t = re.sub(r'^\d+\.\s+', '', t)
    t = t.replace('**', '').replace('*', '')
    t = t.strip().strip('"“”').strip()
    t = re.sub(r"(?<![A-Za-z0-9])'([^']+)'(?![A-Za-z0-9])", r'“\1”', t)
    t = re.sub(r"‘(.*?)’(?![A-Za-z])", r'“\1”', t)
    print(f"[{lang}] parsed text: {repr(t)}")
