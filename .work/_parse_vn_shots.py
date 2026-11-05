# -*- coding: utf-8 -*-
import sys, json, re
sys.stdout.reconfigure(encoding='utf-8')

content = open('02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md', encoding='utf-8').read()
rows = []
for line in content.splitlines():
    m = re.match(r'^\|\s*([1-5]-\d{2})\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|', line)
    if m:
        rows.append([g.strip() for g in m.groups()])

print(f"Total shots parsed: {len(rows)}")
for r in rows:
    sid, cau, vai, mau, nen, chu, sfx, nv = r
    print(f"{sid} | cau: {cau} | vai: {vai} | mau: {mau} | nen: {nen}")
