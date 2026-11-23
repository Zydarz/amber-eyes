# -*- coding: utf-8 -*-
"""
Expand Episode 34 script from 205 sentences to exactly 240 sentences across VN, EN, and JA.
Includes factual corrections:
- Sông Cầm (Đông Triều, Quảng Ninh)
- Bố hung thủ tử nạn giao thông ngày 30/10/2010
- Đơn xin ân xá gửi Chủ tịch nước (bác đơn năm 2012), không phải đơn xin thi hành án sớm.
- Bổ sung 35 câu thoại chia đều 5 hồi chuẩn K10, V1-V9.
"""
import os, re, json

# Read original scripts
vn_file = '01_KICH_BAN/Ho_So_Toi_Pham/Tap34/kichban_tap34_19112026.md'
en_file = '01_KICH_BAN/Ho_So_Toi_Pham/Tap34_EN/kichban_tap34_EN.md'
ja_file = '01_KICH_BAN/Ho_So_Toi_Pham/Tap34_JA/kichban_tap34_JA.md'

vn_paras = open(vn_file, encoding='utf-8').read().split('\n\n')
en_paras = open(en_file, encoding='utf-8').read().split('\n\n')
ja_paras = open(ja_file, encoding='utf-8').read().split('\n\n')

print(f"Original: VN {len(vn_paras)}, EN {len(en_paras)}, JA {len(ja_paras)} paragraphs")
