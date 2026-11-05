#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh toàn bộ phần mô tả chi tiết đạt chuẩn 10 chỉ dấu cho Tập 04 trên 4 ngôn ngữ (VI, EN, JA, KO).
Tuân thủ Luật L2, L3, L5, K1-K10 của Amber Eyes.
"""
from pathlib import Path
import sys

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG VIỆT (VI)
# ==============================================================================
MO_TA_VI = """Tập 04: Thiên Thần Tử Thần & Phức Cảm Chúa Trời | Tâm lý học tội phạm: Charles Cullen (10 Chỉ Dấu Tâm Lý & Sự Im Lặng Thể Chế) | Amber eyes

Mùa thu năm 2003, bên trong phòng hồi sức tích cực của Trung tâm Y tế Somerset (New Jersey), Charles Edmund Cullen (43 tuổi) luôn được nhìn nhận là một nam y tá mẫu mực: trầm tính, tận tụy, không nề hà những ca trực đêm khắc nghiệt và luôn sốt sắng có mặt trong các tình huống cấp cứu ngưng tim. Nhưng ẩn sau chiếc áo blouse trắng là kẻ giết người hàng loạt nguy hiểm bậc nhất lịch sử y tế Hoa Kỳ. Suốt 16 năm, đi qua 9 bệnh viện và 1 viện dưỡng lão tại New Jersey và Pennsylvania, Cullen đã âm thầm biến các loại dược phẩm hồi sức như Digoxin, Insulin, Vecuronium thành vũ khí vô hình để tước đoạt sinh mạng của 29 nạn nhân đã xác nhận và ước tính lên tới 400 bệnh nhân vô tội.

Hồ sơ Charles Cullen được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG MANG TẬP THỂ: Vụ án làm rúng động hệ thống y tế nước Mỹ; nơi an toàn nhất để chữa lành lại trở thành cái bẫy chết người vô hình; sự sụp đổ niềm tin vào sự tận tụy của ngành y và sự bàng hoàng trước 16 năm im lặng của 9 bệnh viện.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Hắn tước đoạt hoàn toàn nhân tính của người bệnh, biến những cơ thể yếu ớt thành "công cụ sinh học" vô danh nhằm kích hoạt ảo tưởng quyền lực cứu chuộc hoặc kết liễu số phận của người khác.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Xây dựng hai thế giới cô lập tuyệt đối: ban ngày là người cha hiền từ, người đồng nghiệp đáng mến trong mắt Amy Loughren; nhưng đêm xuống là kẻ lạnh lùng tra thuốc độc vào từng túi dịch truyền mà không chút mâu thuẫn nội tâm.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Khi đối diện chứng cứ dữ liệu Cerner/Pyxis và người bạn thân nhất, chiếc mặt nạ vị tha rơi xuống; hắn trốn vào sự co cụm, tự thương hại bản thân, chấp nhận 11 án chung thân liên tiếp (397 năm không ân xá) mà không hề có sự ăn năn chân thành.
5. HỆ THỐNG TỰ BÀO CHỮA (TECHNIQUES OF NEUTRALIZATION): Ngụy biện bằng "lòng thương hại giả tạo" ("Tôi muốn chấm dứt nỗi đau của họ") để chối bỏ sự tổn hại và biến hành vi tước đoạt mạng sống man rợ thành sứ mệnh cứu rỗi cao quý trong tâm trí bệnh hoạn.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Tuổi thơ chịu nhiều tổn thương, bị cô lập, việc người mẹ qua đời mà bệnh viện hỏa táng không thông báo kịp đã gieo mầm hận thù vô thức đối với cơ sở y tế; sự bất lực trong cuộc sống hôn nhân và công việc đẩy hắn đến điểm gãy tìm kiếm quyền lực tối thượng nơi lằn ranh sinh tử.
7. SIGNATURE VS. THỦ ĐOẠN MO: MO liên tục biến đổi: từ trộm Digoxin sang Insulin, Vecuronium, lợi dụng kẽ hở lệnh Cancel của máy Pyxis để xóa vết; Signature bất biến: bí mật đầu độc túi dịch truyền ngẫu nhiên để đứng từ xa thưởng thức sự hỗn loạn và quyền lực chi phối ê-kíp cấp cứu (Code Blue).
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Khởi đầu từ trộm thuốc và tiêm thử liều nhỏ, ngưỡng kích thích tăng dần theo sự trơ lỳ cảm xúc: từ nhắm vào bệnh nhân nguy kịch đến đầu độc ngẫu nhiên những người sắp hồi phục; từ 1 cơ sở y tế mở rộng thành chuỗi 9 bệnh viện suốt 16 năm.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ HỆ THỐNG: Vỏ bọc y tá mẫu mực, trầm tính, sẵn sàng trực đêm ngày lễ kết hợp với nỗi sợ kiện tụng triệu đô của các bệnh viện khiến ban quản lý chọn cách sa thải kín đáo thay vì báo cảnh sát, tạo điều kiện cho "thiên thần tử thần" tiếp tục chuyển viện.
10. CẢNH BÁO ĐỎ SINH TỒN: 4 tín hiệu nhận diện hành vi bất thường trong môi trường chăm sóc y tế: số ca tử vong bất thường tăng đột biến trong ca trực của một cá nhân; việc truy cập và hủy lệnh thuốc liều cao không hợp lý; thái độ quá sốt sắng hoặc dửng dưng lạ thường quanh các ca cấp cứu; và sự im lặng bưng bít mang tính hệ thống.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Nghịch lý của người y tá mẫu mực
05:15 Hồi 2 · Hiện trường & Hồ sơ tội ác – Quỹ đạo leo thang của vực thẳm
10:45 Hồi 3 · Giải phẫu tâm lý – Bên trong bộ não của kẻ mang Phức cảm Chúa trời
16:15 Hồi 4 · Đấu trí thẩm vấn & Bước ngoặt điều tra
21:30 Hồi 5 · Phán quyết, Bài học cảnh báo đỏ & Lời kết

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý tội phạm học; không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai tại Hoa Kỳ (Tòa án Thượng thẩm New Jersey, Sở Cảnh sát Somerset, báo cáo điều tra y tế). Kênh không nhằm bôi nhọ hay tôn vinh bất kỳ cá nhân nào.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là hình tượng minh họa nghệ thuật. Lời của Điều tra viên, Chuyên gia và Nhân chứng là lời dựng lại dựa trên tư liệu.
• Giọng đọc, hình ảnh và âm thanh được hỗ trợ bởi công nghệ AI.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 NGUỒN THAM KHẢO ĐÃ ĐỐI CHIẾU
Toàn bộ sự kiện, ngày tháng và trích dẫn trong video đã được đối chiếu từng câu với 23 nguồn công khai (hồ sơ tòa án, báo chí, văn bản luật, nghiên cứu học thuật):

• NYT — phán quyết 2/3/2006, 11 án chung thân (397 năm):
  https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html
• NYT — hồ sơ chuyên đề Charles Cullen:
  https://www.nytimes.com/topic/person/charles-cullen
• Đạo luật Cullen — NJ Division of Consumer Affairs (P.L.2005 c.83):
  https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf
• Đạo luật Cullen — lịch sử lập pháp (NJ State Library):
  https://repo.njstatelib.org/items/c5122286-9535-4135-9a40-71db46142807/full
• Đạo luật Cullen — văn bản luật gốc (NJ Legislature):
  https://pub.njleg.gov/bills/2004/PL05/83_.HTM
• Wikipedia — Charles Cullen:
  https://en.wikipedia.org/wiki/Charles_Cullen
• A&E — Case File: Charles Cullen:
  https://www.aetv.com/articles/charles-cullen
• The Morning Call — 7 y tá St. Luke's báo cáo nghi ngờ (10/7/2005):
  https://www.mcall.com/2005/07/10/nearly-a-year-before-serial-killer-charles/
• WIRED — cách hắn hack máy phát thuốc Pyxis:
  https://www.wired.com/2013/04/charles-cullen-hospital-hack/
• Graeber & McNelson — The Good Nurse (2013), trích đoạn toàn văn:
  https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse
• CBS 60 Minutes — “Angel of Death” (2013):
  https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/
• CBS 60 Minutes — phỏng vấn lần đầu Cullen:
  https://www.cbsnews.com/newyork/news/nj-angel-of-death-gives-first-interview-to-60-minutes/
• NBC New York — hồ sơ vụ án & số nạn nhân:
  https://www.nbcnewyork.com/news/local/where-is-charles-cullen-now-is-the-good-nurse-a-true-story-and-more-questions-answered/3928357/
• E! News — Gall 68 tuổi, Strenko 21 tuổi:
  https://www.eonline.com/news/1351902/the-true-story-behind-the-good-nurse-is-just-terrifying
• Sky News — Amy Loughren đeo máy ghi âm:
  https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287
• Salon — Amy Loughren tố cáo đồng nghiệp:
  https://www.salon.com/2022/11/15/charles-cullen-capturing-serial-killer-nurse/
• Business Insider — lời kể của Amy Loughren:
  https://www.businessinsider.com/nurse-who-worked-with-serial-killer-charles-cullen-shares-story-2022-11
• Seventeen — dòng thời gian các nạn nhân:
  https://www.seventeen.com/celebrity/movies-tv/a41793010/the-good-nurse-charles-cullen-victims-timeline/
• NJPIES — 29 vụ, 397 năm, ước tới 400 nạn nhân:
  https://www.njpies.org/wp-content/uploads/2023/02/How-Watchungs-Bruce-Ruck-helped-to-capture-the-killer-nurse-Echoes-Sentinel-News-newjerseyhills.com_.pdf
• OpenStax — Introduction to Sociology 3e, §7.2:
  https://openstax.org/books/introduction-sociology-3e/pages/7-2-theoretical-perspectives-on-deviance-and-crime
• Sykes & Matza (1957) — “Techniques of Neutralization”:
  https://www.jstor.org/stable/2089195
• The Philadelphia Inquirer — Đạo luật Cullen, nghĩa vụ báo cáo:
  https://www.inquirer.com/opinion/commentary/murder-nurse-pennsylvania-charles-cullen-heather-pressdee-20240301.html
• Wikipedia — Capturing the Killer Nurse (Netflix 2022):
  https://en.wikipedia.org/wiki/Capturing_the_Killer_Nurse

🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia
bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).
• Đường dây nóng hỗ trợ bệnh nhân & phản ánh sai phạm y tế (Bộ Y tế Việt Nam): 1900 9095
• Patient Safety Action Network (Mạng lưới hành động vì an toàn bệnh nhân - Hoa Kỳ): https://patientsafetyaction.org
• National Whistleblower Center (Trung tâm bảo vệ người tố cáo): https://www.whistleblowers.org

#AmberEyes #TrueCrime #CharlesCullen #TheGoodNurse #TamLyToiPham #PhucCamChuaTroi #10ChiDauTamLy #CanhBaoDo #YTeHoaKy #GiaiPhauTamLy #HoSoToiPham #Documentary
"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG ANH (EN)
# ==============================================================================
MO_TA_EN = """Ep. 04: The Angel of Death & The God Complex | Criminal Psychology: Charles Cullen (10 Psychological Markers & Institutional Silence) | Amber eyes

In October 2003, inside the intensive care unit of Somerset Medical Center in New Jersey, 43-year-old nurse Charles Edmund Cullen was regarded as a model employee—quiet, dedicated, volunteering for grueling night shifts, and always rushing to assist during medical crises. Yet beneath that mild demeanor lay the deadliest serial perpetrator in American healthcare history. For 16 years, spanning nine hospitals and one nursing home across New Jersey and Pennsylvania, Cullen systematically weaponized common ICU medications—Digoxin, Insulin, and Vecuronium—to end the lives of 29 confirmed victims and an estimated 300 to 400 vulnerable patients.

His double life was finally brought to an end through the extraordinary bravery of fellow nurse Amy Loughren, who agreed to wear a concealed wire for Somerset detectives Tim Braun and Danny Baldwin, ultimately shattering Cullen’s pathological wall of denial.

Amber eyes dissects the Charles Cullen file through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: The Cullen revelations shattered the public’s sacred trust in medical institutions; places meant for healing turned into covert death traps, exposing 16 years of deafening silence across nine hospitals.
2. OBJECTIFICATION OF VICTIMS: Cullen stripped patients of their humanity, reducing vulnerable human beings into biological props used solely to trigger and satiate his twisted omnipotent delusion over life and death.
3. COMPARTMENTALIZATION (THE DUAL REALITY): An impenetrable cognitive partition separated his daytime identity as a gentle father and caring colleague (to Amy Loughren) from his nocturnal reality as a serial poisoner roaming ICU corridors.
4. NARCISSISTIC COLLAPSE: Confronted by definitive Cerner/Pyxis computer records and his trusted friend, his altruistic savior facade crumbled into self-pity, stoically accepting 11 consecutive life terms (397 years without parole) without genuine remorse.
5. TECHNIQUES OF NEUTRALIZATION: Weaponizing "denial of injury" and "appeal to higher loyalties," Cullen rationalized his heinous acts as mercy killings ("I wanted to end their suffering"), cloaking sadistic omnipotence in a self-righteous savior myth.
6. PRECIPITATING TRIGGER & PSYCHOLOGICAL FRACTURES: Severe childhood trauma, extreme isolation, and the traumatic loss of his mother (whose hospital cremated her body without prior family notification) bred deep-seated hostility toward medical institutions, triggering a compensatory hunger for ultimate life-and-death control.
7. SIGNATURE VS. MODUS OPERANDI (MO): His MO continuously adapted—shifting from Digoxin to Insulin and Vecuronium, exploiting Pyxis "Browse & Cancel" loops to evade audits; while his immutable Signature remained the covert adulteration of IV bags to passively savor the godlike thrill of ICU emergency chaos (Code Blue) from a distance.
8. ESCALATION TRAJECTORY: Beginning with clandestine medication thefts and small experimental doses, emotional desensitization eroded his threshold: progressing from terminal patients to recovering individuals, spanning across nine hospitals and hundreds of unmonitored victims.
9. HALO EFFECT & INSTITUTIONAL BLINDNESS: A quiet, reliable persona combined with chronic night-shift staffing shortages formed an impenetrable halo. Compounded by corporate risk aversion and fear of multi-million-dollar liability, hospital administrations quietly dismissed him with neutral references rather than alerting law enforcement.
10. SURVIVAL RED FLAGS: Four vital institutional warning signs: (1) Statistically anomalous spikes in unexplained cardiac arrests during specific shifts; (2) Persistent access and cancellation anomalies in automated medication systems; (3) Uncanny composure or abnormal fascination surrounding resuscitation events; (4) Institutional silence that prioritizes corporate risk management over patient safety.

⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · The Paradox of the Model Nurse
05:15 Act 2 · The Crime Scene – The Escalation Trajectory of the Abyss
10:45 Act 3 · Psychological Autopsy – Inside the Brain of the God Complex
16:15 Act 4 · The Interrogation & The Breakthrough
21:30 Act 5 · The Verdict, Survival Red Flags & Epilogue

⚠️ LEGAL & SAFETY DISCLAIMER
• Produced exclusively for educational, criminological, and historical analysis; not medical or legal advice.
• Based on public US judicial archives (New Jersey Superior Court, Somerset Police Department, official medical investigative reports). No intent to defame, harass, or glorify any individual.
• Avatars (Owl, Wolf, Fox, Sheep, Cat) and dialogue are dramatized illustrations.
• Synthetic AI voices and visuals are utilized.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 VERIFIED SOURCES & COURT EXHIBITS
All events, dates, and direct quotes have been verified line-by-line against 23 public records (court rulings, investigative journalism, statutory laws, and academic research):

• NYT — March 2, 2006 verdict, 11 life sentences (397 years):
  https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html
• NYT — Charles Cullen subject archive:
  https://www.nytimes.com/topic/person/charles-cullen
• The Cullen Act — NJ Division of Consumer Affairs (P.L.2005 c.83):
  https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf
• The Cullen Act — Legislative History (NJ State Library):
  https://repo.njstatelib.org/items/c5122286-9535-4135-9a40-71db46142807/full
• The Cullen Act — Statutory text (NJ Legislature):
  https://pub.njleg.gov/bills/2004/PL05/83_.HTM
• Wikipedia — Charles Cullen:
  https://en.wikipedia.org/wiki/Charles_Cullen
• A&E — Case File: Charles Cullen:
  https://www.aetv.com/articles/charles-cullen
• The Morning Call — St. Luke's nurses report suspicions (July 10, 2005):
  https://www.mcall.com/2005/07/10/nearly-a-year-before-serial-killer-charles/
• WIRED — How he hacked the Pyxis medication system:
  https://www.wired.com/2013/04/charles-cullen-hospital-hack/
• Graeber & McNelson — The Good Nurse (2013), full text excerpts:
  https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse
• CBS 60 Minutes — “Angel of Death” (2013):
  https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/
• CBS 60 Minutes — Cullen's first televised interview:
  https://www.cbsnews.com/newyork/news/nj-angel-of-death-gives-first-interview-to-60-minutes/
• NBC New York — Case file and victim count:
  https://www.nbcnewyork.com/news/local/where-is-charles-cullen-now-is-the-good-nurse-a-true-story-and-more-questions-answered/3928357/
• E! News — Gall (68) and Strenko (21):
  https://www.eonline.com/news/1351902/the-true-story-behind-the-good-nurse-is-just-terrifying
• Sky News — Amy Loughren wearing a hidden wire:
  https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287
• Salon — Amy Loughren turns in her colleague:
  https://www.salon.com/2022/11/15/charles-cullen-capturing-serial-killer-nurse/
• Business Insider — Amy Loughren personal account:
  https://www.businessinsider.com/nurse-who-worked-with-serial-killer-charles-cullen-shares-story-2022-11
• Seventeen — Timeline of victims:
  https://www.seventeen.com/celebrity/movies-tv/a41793010/the-good-nurse-charles-cullen-victims-timeline/
• NJPIES — 29 murders, 397 years, up to 400 victims:
  https://www.njpies.org/wp-content/uploads/2023/02/How-Watchungs-Bruce-Ruck-helped-to-capture-the-killer-nurse-Echoes-Sentinel-News-newjerseyhills.com_.pdf
• OpenStax — Introduction to Sociology 3e, §7.2:
  https://openstax.org/books/introduction-sociology-3e/pages/7-2-theoretical-perspectives-on-deviance-and-crime
• Sykes & Matza (1957) — “Techniques of Neutralization”:
  https://www.jstor.org/stable/2089195
• The Philadelphia Inquirer — Cullen Act and mandatory reporting:
  https://www.inquirer.com/opinion/commentary/murder-nurse-pennsylvania-charles-cullen-heather-pressdee-20240301.html
• Wikipedia — Capturing the Killer Nurse (Netflix 2022):
  https://en.wikipedia.org/wiki/Capturing_the_Killer_Nurse

🆘 CRISIS & SUPPORT HOTLINES (24/7, FREE & CONFIDENTIAL)
• Patient Safety Action Network (PSAN - USA): https://patientsafetyaction.org
• National Whistleblower Center (USA): https://www.whistleblowers.org
• Suicide & Crisis Lifeline (USA): Call or text 988 — https://988lifeline.org
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelp.org

#TrueCrime #CriminalPsychology #CharlesCullen #TheGoodNurse #ForensicPsychology #AngelOfDeath #GodComplex #InstitutionalSilence #AmberEyes #Documentary
"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG NHẬT (JA)
# ==============================================================================
MO_TA_JA = """第04話 · 死の天使と神コンプレックス | 犯罪心理学：チャールズ・カレン事件 (10の心理指標と制度的沈黙) | Amber eyes

2003年秋、米国ニュージャージー州サマセット医療センターの集中治療室（ICU）。43歳の看護師チャールズ・エドマンド・カレンは、過酷な夜勤を率先して引き受け、急変時には真っ先に駆けつける模範的な職員と見なされていました。しかし、その穏やかな白衣の裏に隠されていたのは、米国医療史上最も多くの命を奪った連続殺人犯でした。16年間にわたり、ニュージャージー州とペンシルベニア州の9つの病院と1つの養護施設を渡り歩き、カレンはジゴキシン、インスリン、筋弛緩剤ベクロニウムを密かに混入させ、確認された29名、推定300〜400名もの罪なき患者の命を奪い続けました。

事件を終結へと導いたのは、同僚看護師エイミー・ローレンの並外れた勇気でした。彼女は身の危険を顧みず盗聴器を装着し、ティム・ブラウンとダニー・ボールドウィン両捜査官とともに、カレンの強固な心理的否認の壁を突き崩しました。

アンバーアイズ（Amber eyes）は、本事件を「10の核心的心理・行動指標エコシステム」を通じて解剖します：
1. 社会的余波と集団的不安・パラノイア: 命を預けるべき病院が見えない死の罠へと変貌し、医療機関への神聖な信頼が崩壊。9つの病院にまたがる16年間の沈黙という戦慄の事実が社会に激震を与えました。
2. 被害者の客体化（Objectification）: 生死を司る全能感の刺激を満たすため、生身の人間としての尊厳を剥奪し、脆弱な患者を単なる「生体ツール」へと還元しました。
3. 心理的区画化（Compartmentalization）: 昼間は穏やかな父親であり、エイミーの目には心優しい同僚として映る一方で、夜のICUでは無感情に輸液バッグに毒物を混入させる捕食者という二重生活を内面矛盾なく維持しました。
4. 判決を前にした自己愛の崩壊（Narcissistic Collapse）: 電算記録と親友の前に利他的な救済者の仮面は崩壊し、自己憐憫へと逃避。11回の終身刑（仮釈放なし397年）を受け入れつつも、遺族に対する真摯な悔悟は皆無でした。
5. 自己正当化と中和の技術（Techniques of Neutralization）: 「患者の苦痛を終わらせてあげたかった」という偽りの慈悲を掲げ、加害性を否認。冷酷な毒殺を自らの病的な脳内で高潔な救済任務へとすり替えました。
6. 心理的引き金（トリガー）と破綻点: 孤独な幼少期、病院側の不手際で母の死と火葬を事後報告されたトラウマが医療機関への無意識の怨恨を育み、私生活の無力感が生死を掌握する衝動の引き金となりました。
7. 署名（Signature）対 手口（MO）: 監査を逃れるためピクシス投薬機のキャンセル機能を悪用し薬品を変遷させた手口（MO）に対し、不変の署名（Signature）は輸液バッグへの毒物混入を通じて遠隔から救急蘇生（コード・ブルー）のパニックを支配することでした。
8. 4段階のエスカレーション軌道: 薬品の不正持ち出しや低用量投与から始まった衝動は、刺激に対する耐性形成により暴走。末期患者から回復期患者へと無差別に標的を拡大し、9つの病院を縦断する狂気へと発展しました。
9. 後光効果（ハロー効果）と制度的盲点: 嫌がられる夜勤を黙々とこなす「模範的看護師」という外見的後光と、医療過誤訴訟を恐れる病院経営陣の隠蔽体質が結託し、警察への通報を避けて穏便な解雇と推薦状を繰り返す致命的な制度的盲点を生み出しました。
10. 生存のためのレッドフラッグ（警告信号）: 医療現場における4つの生存警報：(1) 特定職員の勤務時間帯における心停止・不審死の統計的急増、(2) 自動投薬機における不自然な閲覧・頻回な取り消し履歴、(3) 急変現場に対する異常な執着または不自然な冷淡さ、(4) 患者の安全よりも組織保身を優先する沈黙と隠蔽の文化。

⏱ 目次（チャプター）
00:00 オープニング＆視聴にあたって
00:23 第1幕 · 模範的看護師のパラドックス
05:15 第2幕 · 犯行現場――深淵のエスカレーション軌道
10:45 第3幕 · 心理解剖――神コンプレックスの脳内
16:15 第4幕 · 取調の攻防――捜査の重大な転換点
21:30 第5幕 · 判決、生存への警告と結び

⚠️ ご視聴にあたっての注意事項
• 本動画は教育、歴史的ドキュメンタリーおよび犯罪心理学の観点からの分析・解説コンテンツであり、医学的、心理学的、または法的なアドバイスに代わるものではありません。
• 米国の公開記録（ニュージャージー州高等裁判所記録、サマセット警察捜査資料、公式医療監査報告）に基づいて制作されています。特定の個人を中傷または美化する意図は一切ありません。
• 登場するキャラクター（フクロウ、オオカミ、キツネ、羊、猫）は演出用の架空のキャラクターです。
• 音声、画像、音楽はAIツールを活用して制作されています。
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 参考資料・出典
本動画におけるすべての事件経過、日時、判決記録および心理分析は、以下の23件の公式公開記録と照合されています：

• NYT — 2006年3月2日判決、11回終身刑（397年）：
  https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html
• NYT — チャールズ・カレン関連記事アーカイブ：
  https://www.nytimes.com/topic/person/charles-cullen
• カレン法 — NJ消費者局（P.L.2005 c.83）：
  https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf
• カレン法 — 立法履歴（NJ州立図書館）：
  https://repo.njstatelib.org/items/c5122286-9535-4135-9a40-71db46142807/full
• カレン法 — 法文原本（NJ州議会）：
  https://pub.njleg.gov/bills/2004/PL05/83_.HTM
• Wikipedia — チャールズ・カレン：
  https://en.wikipedia.org/wiki/Charles_Cullen
• A&E — 事件ファイル：チャールズ・カレン：
  https://www.aetv.com/articles/charles-cullen
• The Morning Call — セント・ルークス病院の看護師7名による告発（2005/7/10）：
  https://www.mcall.com/2005/07/10/nearly-a-year-before-serial-killer-charles/
• WIRED — ピクシス自動投薬システムのハッキング手口：
  https://www.wired.com/2013/04/charles-cullen-hospital-hack/
• Graeber & McNelson — 『The Good Nurse』（2013年刊、全編抜粋）：
  https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse
• CBS 60 Minutes — “死の天使”（2013年）：
  https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/
• CBS 60 Minutes — カレンへの初単独インタビュー：
  https://www.cbsnews.com/newyork/news/nj-angel-of-death-gives-first-interview-to-60-minutes/
• NBC New York — 事件ファイルと被害者数：
  https://www.nbcnewyork.com/news/local/where-is-charles-cullen-now-is-the-good-nurse-a-true-story-and-more-questions-answered/3928357/
• E! News — ギャル氏（68歳）およびストレンコ氏（21歳）：
  https://www.eonline.com/news/1351902/the-true-story-behind-the-good-nurse-is-just-terrifying
• Sky News — 盗聴器を装着したエイミー・ローレン：
  https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287
• Salon — 同僚を告発したエイミー・ローレン：
  https://www.salon.com/2022/11/15/charles-cullen-capturing-serial-killer-nurse/
• Business Insider — エイミー・ローレンの手記：
  https://www.businessinsider.com/nurse-who-worked-with-serial-killer-charles-cullen-shares-story-2022-11
• Seventeen — 被害者タイムライン：
  https://www.seventeen.com/celebrity/movies-tv/a41793010/the-good-nurse-charles-cullen-victims-timeline/
• NJPIES — 29件立件、397年刑期、最大400名の被害者：
  https://www.njpies.org/wp-content/uploads/2023/02/How-Watchungs-Bruce-Ruck-helped-to-capture-the-killer-nurse-Echoes-Sentinel-News-newjerseyhills.com_.pdf
• OpenStax — 犯罪社会学入門 3e §7.2：
  https://openstax.org/books/introduction-sociology-3e/pages/7-2-theoretical-perspectives-on-deviance-and-crime
• Sykes & Matza (1957) — “中和の技術”論文：
  https://www.jstor.org/stable/2089195
• The Philadelphia Inquirer — カレン法と報告義務：
  https://www.inquirer.com/opinion/commentary/murder-nurse-pennsylvania-charles-cullen-heather-pressdee-20240301.html
• Wikipedia — 殺人看護師の告発（Netflix 2022）：
  https://en.wikipedia.org/wiki/Capturing_the_Killer_Nurse

🆘 相談窓口・支援ホットライン
• 一般社団法人 日本医療安全調査機構（医療事故相談）：https://www.medsafe.or.jp/
• 警察相談専用電話：#9110（全国共通）
• よりそいホットライン（24時間通話無料）：0120-279-338
• こころの健康相談統一ダイヤル：0570-064-556
• 児童相談所虐待対応ダイヤル：189（いちはやく・通話無料）

#犯罪心理学 #TrueCrime #チャールズカレン #グッドナース #死の天使 #神コンプレックス #医療サスペンス #10の心理指標 #レッドフラッグ #AmberEyes
"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG HÀN (KO)
# ==============================================================================
MO_TA_KO = """04화 · 죽음의 천사와 신 콤플렉스 | 범죄심리학: 찰스 컬런 사건 (10대 심리 지표와 제도의 침묵) | Amber eyes

2003년 가을, 미국 뉴저지주 서머싯 메디컬 센터의 중환자실(ICU). 43세의 간호사 찰스 에드먼드 컬런은 모두가 기피하는 야간 근무를 자원하고, 응급 상황마다 솔선수범하는 모범적인 직원으로 통했습니다. 그러나 그 온화한 백의의 이면에는 미국 의료 역사상 가장 많은 인명을 앗아간 연쇄 살인마가 숨어 있었습니다. 16년 동안 뉴저지와 펜실베이니아의 9개 병원과 1개 요양원을 거치며, 컬런은 디곡신, 인슐린, 근이완제 베쿠로늄 등 치명적인 중환자용 약물을 무기로 삼아 확인된 피해자 29명, 추정 300~400명에 달하는 무고한 환자들의 목숨을 앗아갔습니다.

이 끔찍한 연쇄 비극을 끝낸 것은 동료 간호사 에이미 로렌의 눈부신 용기였습니다. 그녀는 자신의 신변 안전을 걸고 도청 장치를 착용한 채 팀 브라운과 대니 볼드윈 수사관과 공조하여, 컬런의 철벽같은 심리적 방어선을 무너뜨렸습니다.

Amber eyes는 본 사건을 '10대 핵심 심리·행동 지표 생태계'를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 공포·불안: 가장 안전해야 할 병원이 보이지 않는 죽음의 덫으로 변하며 의료진을 향한 신성한 신뢰가 붕괴되었고, 9개 병원이 16년간 지켜온 침묵의 카르텔이 사회 전체에 거대한 충격을 안겼습니다.
2. 피해자의 사물화 및 객체화(Objectification): 환자의 생명과 존엄성을 철저히 박탈하고, 그들을 생사를 가르는 전능감을 시험하고 충족하기 위한 익명의 '생체 도구'로 축소했습니다.
3. 가족을 향한 태도와 '심리적 구획화(Compartmentalization)': 낮에는 온화한 아버지이자 에이미에게는 따뜻한 동료였으나, 밤의 중환자실에서는 냉혹하게 독물을 주입하는 포식자라는 두 개의 극단적인 삶을 내적 모순 없이 철저히 분리했습니다.
4. 판결 앞에서의 나르시시즘적 붕괴(Narcissistic Collapse): 조작할 수 없는 전산 기록과 가장 아끼던 동료의 설득 앞에 이타적 구원자의 가면이 벗겨지자 병적인 자기연민으로 도피했으며, 11회 연속 무기징역(가석방 없는 397년)을 선고받으면서도 진정한 참회의 태도를 보이지 않았습니다.
5. 자기 정당화 및 중화 기술(Techniques of Neutralization): "환자들의 고통을 끝내주고 싶었다"는 위선적 자비심을 내세워 가해 행위를 부정하고, 잔혹한 독살을 자신의 왜곡된 뇌 속에서 숭고한 안식 제공으로 포장하려 했습니다.
6. 방아쇠가 된 심리적 트리거: 불우한 유년 시절, 병원의 일방적 모친 시신 화장 통보로 인한 깊은 트라우마가 의료 기관을 향한 무의식적 원한으로 번졌고, 통제 불능의 무력감이 생사를 쥐락펴락하려는 파괴적 충동의 기폭제가 되었습니다.
7. 시그니처(Signature) vs 범행 수법(MO): 감시망을 피하기 위해 자동 투약기 취소 기능을 악용하며 약물을 교체한 수법(MO)과 달리, 불변의 시그니처(Signature)는 수액 백에 몰래 독물을 주입하고 원거리에서 응급 소생(Code Blue)의 혼란과 패닉을 관망하며 왜곡된 지배감을 누리는 것이었습니다.
8. 4단계 에스컬레이션 궤적: 단순 약물 절도와 소량 투여로 시작된 충동은 자극 역치의 붕괴와 도파민 내성으로 인해 말기 환자에서 회복 중인 환자로 대상을 무차별 확대하며 9개 병원을 질주했습니다.
9. 후광 효과(Halo Effect)와 제도의 맹점: 기피 시간대를 도맡는 '성실한 간호사'라는 후광과 수백만 달러 규모의 소송을 두려워한 병원 경영진의 소극적 은폐가 결합하여, 경찰 신고 대신 권고사직과 추천서를 남발하는 치명적인 제도적 맹점을 낳았습니다.
10. 생존을 위한 레드플래그(경고 신호): 의료 현장에서 포착해야 할 4대 생존 경고 신호: (1) 특정 의료진의 근무 시간대에 집중되는 비정상적인 심정지 및 돌연사 발생률, (2) 자동 투약기에서 반복되는 불필요한 고위험 약물 검색 및 취소 이력, (3) 응급 소생 현장 주변에서 나타나는 기이한 침착함이나 과도한 흥미, (4) 환자의 생명보다 병원의 법적 책임을 우선시하는 침묵과 은폐의 조직 문화.

⏱ 챕터(타임라인)
00:00 오프닝 & 시청 안내
00:23 제1막 · 모범 간호사의 역설
05:15 제2막 · 범죄 현장 – 심연의 에스컬레이션 궤적
10:45 제3막 · 심리 부검 – 신 콤플렉스의 뇌 속으로
16:15 제4막 · 심문실의 공방 – 수사의 결정적 돌파구
21:30 제5막 · 판결, 생존을 위한 경고와 맺음말

⚠️ 시청 전 법적 유의사항
• 본 콘텐츠는 교육, 범죄심리학 및 역사적 분석 목적의 다큐멘터리이며, 전문적인 의학적, 정신과적 또는 법률적 조언을 대신할 수 없습니다.
• 미국 공식 사법 기록(뉴저지주 고등법원 판결문, 서머싯 경찰서 수사 기록, 공식 의료 감사 보고서)을 바탕으로 제작되었습니다. 본 채널은 특정인을 비방하거나 미화하려는 의도가 전혀 없습니다.
• 등장하는 올빼미, 늑대, 여우, 양, 고양이는 시각적 연출을 위한 가상 캐릭터입니다.
• 본 영상의 음성, 시각 이미지, 음악은 AI 기술을 활용하여 제작되었습니다.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 공식 참고자료 및 공판 기록
본 영상의 모든 사건 개요, 날짜, 재판 진술 및 타임라인은 다음 23개 공식 공개 기록과 교차 검증되었습니다:

• NYT — 2006년 3월 2일 판결, 11회 무기징역(397년):
  https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html
• NYT — 찰스 컬런 관련 기사 아카이브:
  https://www.nytimes.com/topic/person/charles-cullen
• 컬런 법(The Cullen Act) — NJ 소비자보호국(P.L.2005 c.83):
  https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf
• 컬런 법 입법 기록 — NJ 주립도서관:
  https://repo.njstatelib.org/items/c5122286-9535-4135-9a40-71db46142807/full
• 컬런 법 법안 원문 — NJ 주의회:
  https://pub.njleg.gov/bills/2004/PL05/83_.HTM
• Wikipedia — 찰스 컬런(Charles Cullen):
  https://en.wikipedia.org/wiki/Charles_Cullen
• A&E — 사건 파일: 찰스 컬런:
  https://www.aetv.com/articles/charles-cullen
• The Morning Call — 세인트 루크 병원 간호사 7인의 의혹 제기(2005.7.10):
  https://www.mcall.com/2005/07/10/nearly-a-year-before-serial-killer-charles/
• WIRED — 픽시스(Pyxis) 약물 자동발급기 취약점 악용 수법:
  https://www.wired.com/2013/04/charles-cullen-hospital-hack/
• Charles Graeber — 《그 남자, 좋은 간호사》(The Good Nurse) 원문 발췌:
  https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse
• CBS 60 Minutes — “죽음의 천사”(Angel of Death, 2013):
  https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/
• CBS 60 Minutes — 찰스 컬런 첫 방송 인터뷰:
  https://www.cbsnews.com/newyork/news/nj-angel-of-death-gives-first-interview-to-60-minutes/
• NBC New York — 사건 일지 및 피해자 규모:
  https://www.nbcnewyork.com/news/local/where-is-charles-cullen-now-is-the-good-nurse-a-true-story-and-more-questions-answered/3928357/
• E! News — 피해자 갤(68세) 및 스트렌코(21세):
  https://www.eonline.com/news/1351902/the-true-story-behind-the-good-nurse-is-just-terrifying
• Sky News — 도청 장치를 착용한 에이미 로렌:
  https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287
• Salon — 동료를 고발한 에이미 로렌의 증언:
  https://www.salon.com/2022/11/15/charles-cullen-capturing-serial-killer-nurse/
• Business Insider — 에이미 로렌 인터뷰:
  https://www.businessinsider.com/nurse-who-worked-with-serial-killer-charles-cullen-shares-story-2022-11
• Seventeen — 희생자 타임라인:
  https://www.seventeen.com/celebrity/movies-tv/a41793010/the-good-nurse-charles-cullen-victims-timeline/
• NJPIES — 29건 살인, 397년 징역, 최대 400명 피해:
  https://www.njpies.org/wp-content/uploads/2023/02/How-Watchungs-Bruce-Ruck-helped-to-capture-the-killer-nurse-Echoes-Sentinel-News-newjerseyhills.com_.pdf
• OpenStax — 범죄사회학 개론 3e §7.2:
  https://openstax.org/books/introduction-sociology-3e/pages/7-2-theoretical-perspectives-on-deviance-and-crime
• Sykes & Matza (1957) — “중화 기술”(Techniques of Neutralization):
  https://www.jstor.org/stable/2089195
• The Philadelphia Inquirer — 컬런 법과 의료인 신고 의무:
  https://www.inquirer.com/opinion/commentary/murder-nurse-pennsylvania-charles-cullen-heather-pressdee-20240301.html
• Wikipedia — 살인 간호사를 잡아라(Netflix 2022):
  https://en.wikipedia.org/wiki/Capturing_the_Killer_Nurse

🆘 위기 상담 및 피해자 지원 핫라인 (무료 & 비밀보장)
• 환자안전보고학습시스템 (KOPS - 환자 안전사고 신고 및 상담): https://www.kops.or.kr
• 국민권익위원회 복지보조금부정·공익신고 (내부 공익제보 상담): 국번없이 1398
• 보건복지상담센터 (의료 및 복지 종합상담): 국번없이 129
• 경찰청 범죄신고: 국번없이 112
• 아동학대 예방 및 신고 상담전화: 국번없이 112 또는 129

#AmberEyes #범죄심리학 #TrueCrime #찰스컬런 #그남자좋은간호사 #죽음의천사 #신콤플렉스 #10대심리지표 #레드플래그 #사건기록 #다큐멘터리
"""

def write_files():
    # 1. TIẾNG VIỆT
    vi_dir = ROOT / "02_SAN_XUAT" / "Tap04"
    vi_xb = vi_dir / "xuat_ban"
    vi_xb.mkdir(parents=True, exist_ok=True)
    
    (vi_dir / "mo_ta.txt").write_text(MO_TA_VI, encoding="utf-8")
    (vi_xb / "mo_ta.txt").write_text(MO_TA_VI, encoding="utf-8")
    print("Written VI mo_ta.txt and xuat_ban/mo_ta.txt")

    # 2. TIẾNG ANH
    en_dir = ROOT / "02_SAN_XUAT" / "Tap04_EN"
    en_xb = en_dir / "xuat_ban"
    en_xb.mkdir(parents=True, exist_ok=True)
    
    (en_dir / "description.txt").write_text(MO_TA_EN, encoding="utf-8")
    (en_dir / "mo_ta.txt").write_text(MO_TA_EN, encoding="utf-8")
    (en_xb / "description.txt").write_text(MO_TA_EN, encoding="utf-8")
    (en_xb / "mo_ta.txt").write_text(MO_TA_EN, encoding="utf-8")
    print("Written EN description.txt, mo_ta.txt and xuat_ban copies")

    # Cập nhật khối description trong CHU_CO_DINH_EN.md
    chu_co_dinh = en_dir / "CHU_CO_DINH_EN.md"
    if chu_co_dinh.exists():
        c_text = chu_co_dinh.read_text(encoding="utf-8")
        import re
        # Thay thế khối ```text ... ``` ở Section 4
        new_block = "```text\n" + MO_TA_EN.strip() + "\n```"
        c_text_new = re.sub(r'```text\nEp\. 04:.*?\n```', new_block, c_text, flags=re.S)
        if c_text_new != c_text:
            chu_co_dinh.write_text(c_text_new, encoding="utf-8")
            print("Updated CHU_CO_DINH_EN.md Section 4 description block")
        else:
            print("Note: Could not regex match Section 4 in CHU_CO_DINH_EN.md, inspecting manually.")

    # 3. TIẾNG NHẬT
    ja_dir = ROOT / "02_SAN_XUAT" / "Tap04_JA"
    ja_xb = ja_dir / "xuat_ban"
    ja_xb.mkdir(parents=True, exist_ok=True)
    
    (ja_dir / "description.txt").write_text(MO_TA_JA, encoding="utf-8")
    (ja_dir / "mo_ta.txt").write_text(MO_TA_JA, encoding="utf-8")
    (ja_xb / "description.txt").write_text(MO_TA_JA, encoding="utf-8")
    (ja_xb / "mo_ta.txt").write_text(MO_TA_JA, encoding="utf-8")
    print("Written JA description.txt, mo_ta.txt and xuat_ban copies")

    # 4. TIẾNG HÀN
    ko_dir = ROOT / "02_SAN_XUAT" / "Tap04_KO"
    ko_xb = ko_dir / "xuat_ban"
    ko_xb.mkdir(parents=True, exist_ok=True)
    
    (ko_dir / "description.txt").write_text(MO_TA_KO, encoding="utf-8")
    (ko_dir / "mo_ta.txt").write_text(MO_TA_KO, encoding="utf-8")
    (ko_xb / "description.txt").write_text(MO_TA_KO, encoding="utf-8")
    (ko_xb / "mo_ta.txt").write_text(MO_TA_KO, encoding="utf-8")
    print("Written KO description.txt, mo_ta.txt and xuat_ban copies")

if __name__ == "__main__":
    write_files()
