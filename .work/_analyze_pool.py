import json, os, re

report = json.load(open('.work/_accurate_final_report.json', encoding='utf-8'))
pool = report[28:] # 40 episodes: Tap 29 to Tap 68

# Group by theme/geography
# 1. Châu Á & Việt Nam:
# VN: 34 (Nguyễn Đức Nghĩa), 35 (Nguyễn Đức Anh)
# TQ & HK: 60, 61, 62, 63, 64, 65, 66, 67, 68
# Nhật Bản: 53 (Tsutomu Miyazaki), 58 (Miyazawa)
# ĐNÁ & Đài Loan: 54 (Đài Loan), 55 (Singapore), 56 (Malaysia), 57 (Charles Sobhraj)
# 2. Châu Mỹ (Mỹ & Latin):
# Mỹ: 29 (Dahmer), 30 (Chris Watts), 31 (Unabomber), 32 (Alcala), 33 (Aileen Wuornos), 36 (Kip Kinkel), 52 (Turpin), 59 (David Parker Ray)
# Latin: 48 (Richthofen), 49 (Pedro Lopez), 50 (Garanhuns), 51 (Juana Barraza)
# 3. Châu Âu & Nam Phi:
# Châu Âu: 37 (Harold Shipman), 38 (Natascha Kampusch), 39 (Joanna Dennehy), 40 (Patrice Alegre), 41 (Florence), 42 (Marc Dutroux), 43 (Peter Kurten), 44 (Heilbronn)
# Nam Phi: 45 (Moses Sithole), 46 (Rosemary Ndlovu), 47 (Cedric Maake)

print(f"Total pool to shuffle: {len(pool)} episodes")
