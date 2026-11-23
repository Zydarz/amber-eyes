import json, os, re

def detect_country(ep, title, topic, plan_txt):
    full_text = (title + " " + topic + " " + plan_txt).lower()
    
    # Specific known cases:
    if ep == 1: # Dee Dee Blanchard, Springfield, Missouri
        return "Mỹ"
    if ep == 2: # Russell Williams, CFB Trenton, Ontario
        return "Canada"
    if ep == 3: # Ed Kemper, Santa Cruz, California
        return "Mỹ"
    if ep == 4: # Charles Cullen, New Jersey
        return "Mỹ"
    if ep == 5: # BTK Dennis Rader, Wichita, Kansas
        return "Mỹ"
    if ep == 6: # John Wayne Gacy, Chicago, Illinois
        return "Mỹ"
    if ep == 7: # Michelle Carter, Massachusetts
        return "Mỹ"
    if ep == 8: # Aum Shinrikyo, Tokyo
        return "Nhật Bản"
    if ep == 9: # Charles Manson, Los Angeles, California
        return "Mỹ"
    if ep == 10: # Cameron Hooker / Colleen Stan, Red Bluff, California
        return "Mỹ"
    if ep == 11: # Paul Bernardo & Karla Homolka, Ontario
        return "Canada"
    if ep == 12: # Jonestown / Jim Jones (Guyana / nguồn gốc giáo phái Mỹ)
        return "Mỹ / Guyana"
    if ep == 13: # Jennifer Pan, Markham, Ontario
        return "Canada"
    if ep == 14: # Betty Broderick, San Diego, California
        return "Mỹ"
    if ep == 15: # Jodi Arias, Mesa, Arizona
        return "Mỹ"
    if ep == 16: # Ted Bundy, Washington / Florida
        return "Mỹ"
    if ep == 17: # Richard Ramirez (Night Stalker), California
        return "Mỹ"
    if ep == 18: # Andrei Chikatilo, Rostov
        return "Nga (Liên Xô)"
    if ep == 19: # Gary Ridgway (Green River Killer), Washington
        return "Mỹ"
    if ep == 20: # Hwaseong Serial Murders (Lee Chun-jae), Gyeonggi
        return "Hàn Quốc"
    if ep == 21: # Josef Fritzl, Amstetten
        return "Áo"
    if ep == 22: # Tsutomu Miyazaki (Otaku Murderer), Tokyo / Saitama
        return "Nhật Bản"
    if ep == 23: # Bạch Ngân (Gao Chengyong), Cam Túc
        return "Trung Quốc"
    if ep == 24: # Harold Shipman, Hyde, Greater Manchester
        return "Anh"
    if ep == 25: # Yoo Young-chul, Seoul
        return "Hàn Quốc"
    if ep == 26: # Miyuki Ishikawa, Tokyo
        return "Nhật Bản"
    if ep == 27: # Nguyễn Hải Dương, Bình Phước
        return "Việt Nam"
    if ep == 28: # Lê Văn Luyện, Bắc Giang
        return "Việt Nam"
    if ep == 29: # Jeffrey Dahmer, Milwaukee, Wisconsin
        return "Mỹ"
    if ep == 30: # Chris Watts, Frederick, Colorado
        return "Mỹ"
    if ep == 31: # Unabomber Ted Kaczynski, Montana / Illinois
        return "Mỹ"
    if ep == 32: # Rodney Alcala (Dating Game Killer), California
        return "Mỹ"
    if ep == 33: # Thảm sát Port Arthur (Martin Bryant), Tasmania
        return "Úc"
    if ep == 34: # Issei Sagawa, Paris / Nhật Bản
        return "Nhật Bản / Pháp"
    if ep == 35: # David Berkowitz (Son of Sam), New York
        return "Mỹ"
    if ep == 36: # Lâm Quá Vân (The Jars Murderer), Hồng Kông
        return "Hồng Kông"
    if ep == 37: # Golden State Killer (Joseph DeAngelo), California
        return "Mỹ"
    if ep == 38: # Aileen Wuornos, Florida
        return "Mỹ"
    if ep == 39: # Giáo phái Đền Thái Dương (Order of the Solar Temple)
        return "Thụy Sĩ / Pháp / Canada"
    if ep == 40: # Thảm sát Columbine (Eric Harris & Dylan Klebold), Colorado
        return "Mỹ"
    if ep == 41: # Fred & Rose West, Gloucester
        return "Anh"
    if ep == 42: # Alexander Pichushkin (Cờ vua), Moscow
        return "Nga"
    if ep == 43: # Marc Dutroux, Bỉ
        return "Bỉ"
    if ep == 44: # Thảm kịch Waco (David Koresh), Texas
        return "Mỹ"
    if ep == 45: # Edmund Kemper (nếu có lặp) hoặc vụ khác
        pass

    # Generic keywords matching
    if any(k in full_text for k in ['hàn quốc', 'korea', 'seoul', 'hwaseong']): return "Hàn Quốc"
    if any(k in full_text for k in ['nhật bản', 'japan', 'tokyo', 'kyoto', 'osaka']): return "Nhật Bản"
    if any(k in full_text for k in ['hồng kông', 'hong kong']): return "Hồng Kông"
    if any(k in full_text for k in ['trung quốc', 'china', 'quảng đông', 'bắc kinh', 'cam túc', 'bạch ngân']): return "Trung Quốc"
    if any(k in full_text for k in ['việt nam', 'bình phước', 'bắc giang', 'nguyễn hải dương', 'lê văn luyện']): return "Việt Nam"
    if any(k in full_text for k in ['canada', 'ontario', 'toronto']): return "Canada"
    if any(k in full_text for k in ['anh quốc', 'vương quốc anh', 'nước anh', 'london', 'manchester', 'england', 'uk']): return "Anh"
    if any(k in full_text for k in ['áo', 'austria', 'vienna', 'amstetten']): return "Áo"
    if any(k in full_text for k in ['úc', 'australia', 'tasmania', 'port arthur']): return "Úc"
    if any(k in full_text for k in ['nga', 'russia', 'moscow', 'liên xô']): return "Nga"
    if any(k in full_text for k in ['pháp', 'france', 'paris']): return "Pháp"
    if any(k in full_text for k in ['đức', 'germany']): return "Đức"
    if any(k in full_text for k in ['bỉ', 'belgium']): return "Bỉ"
    if any(k in full_text for k in ['hoa kỳ', 'mỹ', 'usa', 'fbi', 'california', 'texas', 'florida', 'colorado', 'ohio', 'new york', 'massachusetts', 'illinois', 'kansas', 'missouri', 'oregon', 'washington', 'connecticut', 'georgia', 'indiana', 'alaska', 'nebraska', 'utah', 'wisconsin', 'arizona']): return "Mỹ"
    return "Mỹ"

data = json.load(open('.work/_episodes_data_final.json', encoding='utf-8'))
for row in data:
    ep = row['ep']
    p = f"02_SAN_XUAT/Ho_So_Toi_Pham/Tap{ep:02d}/KeHoach_Video_Tap{ep:02d}.md"
    txt = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    row['country'] = detect_country(ep, row['title'], row['topic'], txt[:2000])

open('.work/_episodes_data_final.json', 'w', encoding='utf-8').write(json.dumps(data, ensure_ascii=False, indent=2))
print("Countries updated accurately!")
