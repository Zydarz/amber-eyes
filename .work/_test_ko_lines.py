# -*- coding: utf-8 -*-
import sys, io, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

for line in [
    "‘The Company’에 대한 공포는 교도소의 그 어떤 쇠창살보다 더 단단한 강철의 현실로 그녀의 마음속에 군림했습니다.",
    "‘The Company’에 대한 공포의 벽은 순식간에 무너져 내렸고, 그녀가 본래 지니고 있던 생존 본능이 되살아났습니다."
]:
    s = line.strip()
    t = re.sub(r'^\*\s+', '', s); t = re.sub(r'^\d+\.\s+', '', t)
    t = t.replace('**', '').replace('*', '')
    t = t.strip().strip('"“”').strip()
    t = re.sub(r"(?<![A-Za-z0-9])'([^']+)'(?![A-Za-z0-9])", r'“\1”', t)
    t = re.sub(r"‘(.*?)’(?![A-Za-z])", r'“\1”', t)
    print("Parsed:", repr(t))
