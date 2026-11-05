# -*- coding: utf-8 -*-
"""Generate complete, rich, 10-indicator descriptions for Tap 05 in 4 languages (VI, EN, JA, KO).
Writes to all target locations in 02_SAN_XUAT/Tap05*
"""
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG VIỆT (VI)
# ==============================================================================
MO_TA_VI = """Tập 05: Chiếc Đĩa Mềm Màu Tím & Cơn Nghiện Ái Kỷ | Tâm lý học tội phạm: Dennis Rader (Hệ Sinh Thái 10 Chỉ Dấu Tâm Lý & Sự Sụp Đổ Của Vỏ Bọc 30 Năm) | Amber eyes

Suốt hơn 30 năm (1974–2005), Dennis Lynn Rader đã dựng nên một chiếc mặt nạ công dân hoàn hảo đến kinh ngạc tại thị trấn Park City, bang Kansas: cựu binh Không quân Mỹ, người chồng mẫu mực 34 năm, người cha chu đáo, Chủ tịch Hội đồng Nhà thờ Lutheran Chúa Kitô, Đội trưởng Hướng đạo sinh Cub Scout, và nhân viên trật tự đô thị mẫn cán. Nhưng ẩn sau vỏ bọc tôn nghiêm ấy là "BTK" (Bind, Torture, Kill) — kẻ sát nhân hàng loạt reo rắc cơn ác mộng kinh hoàng cho cả miền Trung Tây nước Mỹ, tước đoạt sinh mạng của 10 nạn nhân vô tội. Sau 13 năm ngủ đông an toàn tuyệt đối (1991–2004), sự kiêu ngạo ái kỷ và cơn nghiện danh tiếng đã thúc đẩy Rader phá vỡ sự im lặng. Một câu hỏi ngây thơ gửi tới cảnh sát và một chiếc đĩa mềm Memorex 1.44MB màu tím gửi tới đài truyền hình KSAS-TV đã kích hoạt chiếc bẫy pháp y số lịch sử của Trung úy Ken Landwehr, vĩnh viễn khóa chặt cánh cửa tự do của kẻ săn mồi hai mặt.

Hồ sơ Dennis Rader được giải phẫu toàn diện qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & CƠN HOANG TƯỞNG TẬP THỂ: Vụ án gây chấn động nước Mỹ suốt ba thập kỷ; khi bức thư tái xuất xuất hiện vào tháng 3/2004, người dân Wichita lại nín thở trong kinh hoàng, mua súng, thay khóa cửa, nghi kỵ lẫn nhau; sự sụp đổ niềm tin tột cùng của cộng đồng khi phát hiện kẻ thủ ác là chủ tịch hội đồng nhà thờ; vụ án trở thành bước ngoặt lịch sử thúc đẩy sự phát triển của ngành Giám định Pháp y Kỹ thuật số (Digital Forensics) và trích xuất Siêu dữ liệu (Metadata).
2. VẬT HÓA & PHI NHÂN HÓA NẠN NHÂN (OBJECTIFICATION): Rader gọi các nạn nhân là những "dự án" (projects), coi họ như "đạo cụ sống" (living props) phục vụ kịch bản ảo tưởng bệnh hoạn; sự kết hợp giữa Ái kỷ ác tính và Rối loạn nhân cách chống đối xã hội triệt tiêu hoàn toàn sự thấu cảm; tiếng van xin của nạn nhân chỉ kích hoạt hưng phấn quyền lực toàn năng (power arousal).
3. CƠ CHẾ CHIA NGĂN NHẬN THỨC (COMPARTMENTALIZATION): Khả năng đóng chặt các ngăn kéo tâm trí độc lập: ngăn 1 là người chồng gương mẫu 34 năm của Paula, người cha tận tụy dạy con gái đi xe đạp, chủ tịch nhà thờ; ngăn 2 là con thú săn mồi bóng đêm; gia đình bị biến thành "Lá chắn bình thường hóa" (Shield of Normalization) che mắt xã hội; bi kịch hủy hoại người thân và cuộc khủng hoảng danh tính kéo dài suốt đời của con gái Kerri Rawson.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Khi đối chất trong phòng thẩm vấn, Rader bối rối như một đứa trẻ bị lừa vì cảnh sát nói dối về chiếc đĩa mềm; sau đó rơi vào trạng thái sụp đổ cái tôi ái kỷ và thao thao bất tuyệt thú nhận 10 vụ án đầy tự hào như giáo sư giảng bài; trước tòa chỉ thể hiện sự Tự thương hại bản thân bệnh hoạn (Pathological Self-Pity), hoàn toàn không có sự ăn năn chân chính.
5. HỆ THỐNG TỰ BÀO CHỮA & "NHÂN TỐ X" (FACTOR X & NEUTRALIZATION): Ứng dụng lý thuyết Kỹ thuật Trung hòa Đạo đức: Rader tự tạo ra khái niệm hoang tưởng "Nhân tố X" (Factor X), coi xung lực ác tính là một thực thể ký sinh bên ngoài ép buộc hắn ra tay để rũ bỏ trách nhiệm cá nhân ("không phải tôi muốn làm điều đó, mà chính Nhân tố X bên trong ép tôi phải làm"), giúp hắn vừa gây tội ác vừa có thể về nhà mỉm cười ăn tối cùng gia đình.
6. NGÒI NỔ TÂM LÝ & TỔN THƯƠNG ÁI KỶ (PRECIPITATING TRIGGER): Đầu năm 2004, tờ báo The Wichita Eagle đăng loạt bài kỷ niệm 30 năm vụ án BTK và nhắc đến cuốn sách của Robert Beattie với giả thuyết BTK đã chết hoặc bị lãng quên; cú đâm chí mạng vào lòng tự tôn ái kỷ khiến Rader không chịu nổi sự lãng quên, trở thành ngòi nổ kích hoạt sự tái xuất sau 13 năm ngủ đông.
7. CHỮ KÝ SIGNATURE VS. THỦ ĐOẠN MO: MO liên tục thay đổi để tẩu thoát (cắt dây điện thoại, đeo găng tay, chọn thời điểm đêm tối, ngụy trang); Signature bất biến để thỏa mãn nhu cầu cảm xúc bệnh lý nội tại (trói áp chế tuyệt đối, lưu giữ chiến lợi phẩm Trophies như bằng lái và trang sức để kích hoạt hồi tưởng, gửi thơ và câu đố chữ trêu ngươi truyền thông).
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG 4 NẤC THANG: Khởi đầu từ thời niên thiếu bạo hành súc vật nhỏ và nhìn trộm qua cửa sổ ban đêm -> đột nhập lén lút trộm đồ riêng tư phụ nữ làm kỷ vật -> xâm nhập gia cư khống chế trực diện nạn nhân -> tước đoạt sinh mạng kết hợp chụp ảnh bệnh hoạn; cơn đói ảo tưởng liên tục đòi hỏi liều kích thích mạnh hơn nếu không có sự can thiệp từ bên ngoài.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI (HALO EFFECT & NORMALCY BIAS): Chiếc mặt nạ đạo mạo hoàn hảo (cựu binh Không quân, Chủ tịch Hội đồng Nhà thờ Lutheran, Đội trưởng Hướng đạo sinh Cub Scout, nhân viên trật tự đô thị đo cỏ) tạo ra thành kiến bình thường hóa khiến người dân chỉ coi sự hà khắc là "nguyên tắc quân đội", tạo điểm mù che mắt cả thị trấn suốt ba thập kỷ.
10. CẢNH BÁO ĐỎ SINH TỒN & NẠN NHÂN HỌC: Bóc trần việc lạm dụng vị trí lắp đặt báo động an ninh ADT và quản lý trật tự đô thị để tiếp cận con mồi; đúc kết 4 Dấu hiệu cảnh báo đỏ sinh tồn: (1) Sự ám ảnh kiểm soát quy tắc cực đoan; (2) Sự tách biệt cảm xúc đằng sau vẻ ngoài nhiệt thành (Shallow Affect); (3) Thói quen bí mật lưu trữ vật dụng riêng tư của người khác như chiến lợi phẩm; (4) Cơn khát khao ái kỷ được công nhận bằng mọi giá. Lời khuyên: "Hãy luôn tin vào trực giác và bảo vệ ranh giới an toàn của cuộc sống".

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Bức thư tái xuất sau 13 năm lặng căm
05:15 Hồi 2 · Hiện trường & Hồ sơ tội ác – Chữ ký tâm lý & Quỹ đạo leo thang
10:30 Hồi 3 · Giải phẫu tâm lý – Bên trong bộ não ái kỷ ác tính & Nghịch lý chia ngăn
16:45 Hồi 4 · Đấu trí thẩm vấn & Bẫy công nghệ đĩa mềm
21:45 Hồi 5 · Phán quyết, Bài học cảnh báo đỏ & Lời kết

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý tội phạm học; không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai tại Hoa Kỳ (Tòa án Quận Sedgwick, Sở Cảnh sát Wichita, Bộ Quản chế Bang Kansas). Kênh không nhằm bôi nhọ, phỉ báng hay cổ xúy bất kỳ hành vi phạm tội nào.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là hình tượng minh họa nghệ thuật. Lời của Điều tra viên, Chuyên gia và Nhân chứng là lời dựng lại dựa trên tư liệu.
• Giọng đọc, hình ảnh và âm thanh được hỗ trợ bởi công nghệ AI.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 NGUỒN THAM KHẢO ĐÃ ĐỐI CHIẾU
Toàn bộ sự kiện, ngày tháng, tài liệu điều tra, phân tích pháp y số và diễn biến vụ án BTK trong video đã được đối chiếu từng câu với các nguồn hồ sơ công khai của Cảnh sát Wichita, FBI và báo chí Hoa Kỳ:

▸ Hồ sơ tòa án & Cơ quan điều tra:
• Tòa án Quận 18 Hạt Sedgwick (Kansas) — Bản án State of Kansas v. Dennis L. Rader (Case No. 05 CR 498, Thẩm phán Gregory Waller) — https://www.kscourts.org/
• Sở Cảnh sát Wichita (WPD) & Ban Phân tích Hành vi FBI (BAU) — Hồ sơ chuyên án BTK Task Force (Chỉ huy Ken Landwehr) — https://www.wichita.gov/police
• Bộ Quản chế Bang Kansas (KDOC) — Hồ sơ phạm nhân Dennis Lynn Rader (#0083707) tại Nhà tù El Dorado — https://www.doc.ks.gov/
▸ Báo chí điều tra & Lịch sử vụ án:
• The Wichita Eagle — Kho lưu trữ tài liệu điều tra chuyên sâu về BTK: Từ các bức thư năm 1974 tới sự tái xuất năm 2004 — https://www.kansas.com/news/special-reports/btk/
• The New York Times — 'Wichita Suspect Is Charged With 10 Murders' & Quá trình nhận tội trước tòa — https://www.nytimes.com/2005/03/01/us/wichita-suspect-is-charged-with-10-murders.html
• CBS News (48 Hours) — Phim tài liệu điều tra: 'The BTK Strangler: The Catch' & Lời khai của các điều tra viên — https://www.cbsnews.com/news/btk-investigators-reveal-how-they-caught-serial-killer/
• Associated Press (AP) — Dòng thời gian 31 năm săn lùng kẻ sát nhân BTK và sai lầm đĩa mềm màu tím — https://apnews.com/
▸ Sách tư liệu & Hồi ký nhân chứng:
• Robert Beattie (Luật sư & Tác giả) — 'Nightmare in Wichita: The Hunt for the BTK Strangler' (Cuốn sách kích hoạt sự tái xuất của Rader năm 2004) — https://www.harpercollins.com/
• Kerri Rawson (Con gái của Dennis Rader) — Hồi ký 'A Serial Killer's Daughter: My Story of Faith, Love, and Overcoming' (2019) — https://kerrirawson.com/
• Roy Wenzl, Tim Potter, L. Kelly, Hurst Laviana — 'Bind, Torture, Kill: The Inside Story of the Serial Killer Next Door' (2007)
▸ Pháp y số & Tâm lý học tội phạm:
• Phân tích Pháp y Kỹ thuật số (Digital Forensics) — Phân tích Metadata tệp Microsoft Word xóa trên đĩa mềm Memorex 3.5 inch, truy vết Christ Lutheran Church & 'Dennis' — https://www.forensicfocus.com/
• FBI Law Enforcement Bulletin — Phân tích Rối loạn nhân cách ái kỷ ác tính (Malignant Narcissism) & Sự phân mảnh tâm trí (Compartmentalization) ở tội phạm giết người hàng loạt — https://leb.fbi.gov/

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ & BẢO VỆ (24/7, MIỄN PHÍ)
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng hỗ trợ bệnh nhân & phản ánh sai phạm y tế (Bộ Y tế Việt Nam): 1900 9095
• National Domestic Violence Hotline (Hoa Kỳ): 1-800-799-SAFE (7233) — https://www.thehotline.org
• Childhelp National Child Abuse Hotline (Hoa Kỳ): 1-800-422-4453 — https://www.childhelp.org
• Suicide & Crisis Lifeline (Hoa Kỳ): Gọi hoặc nhắn tin 988 — https://988lifeline.org

#AmberEyes #TrueCrime #CriminalPsychology #BTK #DennisRader #ForensicFiles #DigitalForensics #TamLyToiPham #PhamVan #HoiTo #PhanManhTamTri #AiKyAcTinh #10ChiDauTamLy #CanhBaoDo #Documentary
"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG ANH (EN)
# ==============================================================================
MO_TA_EN = """Episode 05: The Purple Floppy Disk & Narcissistic Addiction | Criminal Psychology: Dennis Rader (The 10 Psychological Indicators & The Collapse of a 30-Year Masquerade) | Amber eyes

For more than thirty years (1974–2005), Dennis Lynn Rader maintained an astonishingly pristine civic facade in Park City, Kansas: a US Air Force veteran, devoted husband of 34 years, loving father, Council President of Christ Lutheran Church, Cub Scout leader, and diligent municipal compliance officer. Yet behind that pious masquerade lurked "BTK" (Bind, Torture, Kill)—the phantom serial predator who terrorized the American Midwest, claiming the lives of ten innocent victims. After thirteen full years of absolute hibernation (1991–2004), narcissistic arrogance and an unquenchable addiction to notoriety drove Rader to shatter his own silence. A naive inquiry to detectives and a purple Memorex 1.44MB floppy disk sent to KSAS-TV sprang Lieutenant Ken Landwehr's historic digital forensic trap, sealing the fate of the two-faced monster forever.

Amber eyes dissects the Dennis Rader dossier through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: The BTK terror paralyzed Kansas for three decades; when his resurgence letter arrived in March 2004, the heartland held its breath in dread, rushing to buy firearms, bolt windows, and eye neighbors with suspicion; total community betrayal upon discovering the monster was their church council president; landmark milestone catalyzing modern Digital Forensics and Metadata extraction.
2. OBJECTIFICATION & DEHUMANIZATION OF VICTIMS: Rader coldly termed his victims "projects," reducing living human beings into "living props" to enact bizarre sadistic fantasies; the toxic fusion of Malignant Narcissism and Antisocial Personality Disorder eradicated affective empathy; victims' desperate pleas only served as sensory triggers intensifying his sensation of omnipotent power.
3. COMPARTMENTALIZATION (THE DUAL REALITY): An airtight psychological partition divided his cognitive drawers: Drawer One as Paula's faithful husband, a father teaching his daughter to ride a bike, and church elder; Drawer Two as the nocturnal predator; his family functioned as a "Shield of Normalization" hiding his dark reality; the devastating psychological aftermath for his daughter Kerri Rawson.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: In the interrogation room, Rader displayed petulant confusion when learning detectives had lied about floppy disk traceability; once trapped, he plummeted into Narcissistic Collapse, launching into a marathon confession delivered with academic pride; before the court, he exhibited pathetic Pathological Self-Pity devoid of genuine remorse.
5. TECHNIQUES OF NEUTRALIZATION ("FACTOR X"): Utilizing Sykes & Matza's neutralization theory, Rader invented the delusional concept of "Factor X"—an external parasite he claimed compelled his dark impulses ("it was not that I wanted to do it, but Factor X forced my hand"), thereby shedding moral accountability and allowing him to return home to dine innocently with his family.
6. PRECIPITATING TRIGGER & NARCISSISTIC INJURY: In early 2004, The Wichita Eagle ran a 30-year retrospective citing Robert Beattie's upcoming book and theorizing BTK was dead or forgotten; this inflicted a catastrophic narcissistic injury on Rader's fragile ego, compelling him to break thirteen years of safe hibernation to reassert his notoriety.
7. SIGNATURE VS. MODUS OPERANDI (MO): His MO continuously adapted for practical evasion (cutting phone cords, wearing gloves, hunting under darkness); while his immutable Signature served internal psychological compulsions (absolute binding control, hoarding driver's licenses and jewelry as Trophies, and planting taunting poems and puzzles in public libraries and park trash cans).
8. FANTASY ESCALATION TRAJECTORY: Evolving across four dangerous stages: childhood animal cruelty and nocturnal voyeurism -> residential prowling and collecting private garments as souvenirs -> purposeful home invasions confronting victims -> lethal destruction and staging bizarre photographs; predatory fantasy hunger inevitably demands escalating stimulation.
9. HALO EFFECT & SOCIAL BLIND SPOTS: An impeccable civic disguise (Air Force veteran, Lutheran council president, Cub Scout master, meticulous municipal code officer) generated a powerful normalcy bias; neighbors dismissed his extreme rigidity as mere military discipline, creating a three-decade blind spot.
10. SURVIVAL RED FLAGS & VICTIMOLOGY: Weaponizing his positions at ADT Security Systems and municipal code enforcement to stalk vulnerable households; four vital survival red flags: (1) Extreme control obsession and administrative rigidity; (2) Shallow affect masked behind civic warmth; (3) Covert accumulation of others' personal belongings as trophies; (4) Insatiable narcissistic demand for acclaim. Core takeaway: "Always trust your inner intuition when encountering unsettling behavior."

⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · Resurgence After Thirteen Years of Silence
05:15 Act 2 · Crime Scene & Forensic Dossier – Signature & Escalation Trajectory
10:30 Act 3 · Psychological Autopsy – Inside Malignant Narcissism & Compartmentalization
16:45 Act 4 · Interrogation & The Floppy Disk Forensic Trap
21:45 Act 5 · Verdict, Survival Red Flags & Epilogue

⚠️ LEGAL & SAFETY DISCLAIMER
• Produced exclusively for educational, criminological, and historical documentary purposes; not professional medical or legal advice.
• Based on public US judicial archives (Sedgwick County District Court, Wichita Police Department, Kansas Department of Corrections). No intent to defame, harass, or glorify criminal conduct.
• Avatars (Owl, Wolf, Fox, Sheep, Cat) and dialogue are dramatized artistic illustrations based on public records.
• Synthetic AI voices, visuals, and audio are utilized.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 VERIFIED SOURCES & COURT EXHIBITS
All events, dates, investigative files, digital forensic findings, and trial proceedings have been verified line-by-line against official public records:

▸ Judicial Records & Investigative Files:
• 18th Judicial District Court of Sedgwick County, Kansas — State of Kansas v. Dennis L. Rader (Case No. 05 CR 498, Judge Gregory Waller) — https://www.kscourts.org/
• Wichita Police Department (WPD) & FBI Behavioral Analysis Unit (BAU) — BTK Task Force Case Dossier (Commander Ken Landwehr) — https://www.wichita.gov/police
• Kansas Department of Corrections (KDOC) — Inmate Profile: Dennis Lynn Rader (#0083707), El Dorado Correctional Facility — https://www.doc.ks.gov/
▸ Investigative Journalism & Historical Archives:
• The Wichita Eagle — Investigative Archive on BTK: From the 1974 communiqués to the 2004 resurgence — https://www.kansas.com/news/special-reports/btk/
• The New York Times — 'Wichita Suspect Is Charged With 10 Murders' & Courtroom Confession — https://www.nytimes.com/2005/03/01/us/wichita-suspect-is-charged-with-10-murders.html
• CBS News (48 Hours) — Documentary Special: 'The BTK Strangler: The Catch' — https://www.cbsnews.com/news/btk-investigators-reveal-how-they-caught-serial-killer/
• Associated Press (AP) — 31-Year Timeline of the BTK Manhunt and the Purple Floppy Disk Blunder — https://apnews.com/
▸ Biographical Memoirs & Literature:
• Robert Beattie — 'Nightmare in Wichita: The Hunt for the BTK Strangler' (The catalyst book that triggered Rader's resurgence in 2004) — https://www.harpercollins.com/
• Kerri Rawson — Memoir: 'A Serial Killer's Daughter: My Story of Faith, Love, and Overcoming' (2019) — https://kerrirawson.com/
• Roy Wenzl, Tim Potter, L. Kelly, Hurst Laviana — 'Bind, Torture, Kill: The Inside Story of the Serial Killer Next Door' (2007)
▸ Digital Forensics & Behavioral Psychiatry:
• Digital Forensics Analysis — Forensic recovery of deleted Word metadata from Memorex 3.5-inch floppy disk identifying Christ Lutheran Church and 'Dennis' — https://www.forensicfocus.com/
• FBI Law Enforcement Bulletin — Malignant Narcissism and Compartmentalization in Serial Homicide Offenders — https://leb.fbi.gov/

🆘 CRISIS & SUPPORT HOTLINES (24/7, FREE & CONFIDENTIAL)
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelp.org
• Suicide & Crisis Lifeline (USA): Call or text 988 — https://988lifeline.org
• National Child Helpline 111 (Vietnam, toll-free 24/7) — http://tongdai111.vn/

#AmberEyes #TrueCrime #CriminalPsychology #BTK #DennisRader #ForensicFiles #DigitalForensics #MalignantNarcissism #Compartmentalization #10PsychologicalMarkers #SurvivalRedFlags #Documentary
"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG NHẬT (JA)
# ==============================================================================
MO_TA_JA = """第05話：紫色のフロッピーディスクと自己愛の渇望 | 犯罪心理学：Dennis Rader（10の心理的指標＆30年間に及ぶ仮面の崩壊） | Amber eyes

30年以上にわたり（1974年〜2005年）、Dennis Lynn Raderは米カンザス州パークシティにおいて、息をのむほど完璧な模範市民の仮面を維持し続けました。空軍退役軍人、34年間連れ添った良き夫、献身的な父親、キリスト・ルーテル教会の教会評議会議長、カブスカウトの隊長、そして真面目な市役所の規則遵守指導員。しかしその敬虔な素顔の裏に潜んでいたのは、無辜の市民10名の命を奪い、アメリカ中西部を震え上がらせた連続殺人鬼「BTK（Bind, Torture, Kill）」でした。13年間にわたる完全な冬眠（1991年〜2004年）の後、肥大化した自己愛と悪名への渇望が彼に沈黙を破らせました。警察への無知な問いかけと、地元テレビ局KSAS-TVへ送りつけた一枚の紫色Memorex製フロッピーディスクが、ケン・ランドウェアー警部率いる捜査班のデジタル鑑識の罠を作動させ、二重生活を送った怪物は永遠の断罪へと追い込まれました。

アンバーアイズ（Amber eyes）は、Dennis Rader事件を「10の核心的心理・行動指標エコシステム」を通じて徹底解剖します：
1. 社会的余波と集団的偏執病（パラノイア）: BTKの恐怖は30年間にわたりカンザス州を麻痺させました。2004年3月に再出現の手紙が届いたとき、市民は息をのみ、銃を買い足し、鍵を取り替え、隣人同士で疑心暗鬼に陥りました。犯人が自らの教会の会長であったという事実は地域社会に計り知れない打撃を与え、本事件は現代のデジタル鑑識とメタデータ抽出技術の歴史的転換点となりました。
2. 被害者の客体化（物扱い）と非人間化: Raderは被害者たちを「プロジェクト」と呼び、異様な加虐妄想を演じるための「生きた小道具」へと格下げしました。悪性自己愛と反社会性人格障害の結合が共感能力を完全に喪失させ、被害者の懇願は全能の権力支配感を刺激する燃料として消費されました。
3. 精神の分断（コンパートメンタライゼーション）と正常性の防壁: 認知的引き出しを完全に分離する能力：引き出し1は良き夫、愛娘に自転車を教える父親、教会議長；引き出し2は夜の冷酷な捕食者。家庭は社会の目を欺く「正常性の防壁」として利用され、逮捕後に娘Kerri Rawsonが背負うこととなった深刻な魂の傷跡を描きます。
4. 自己愛の崩壊（Narcissistic Collapse）と病的な自己憐憫: 取調室でフロッピーの追跡可能性について警察が嘘をついたと知った際、子供のように動揺。罠に落ちたことを悟ると自己愛の完全崩壊を起こし、大学教授が講義するかのように10件の凶行を誇らしげに自供。法廷では遺族への悔悟ではなく、哀れな自己憐憫に終始しました。
5. 道徳的合理化技術と「要因X」（Factor X）: サイクスとマッツァの中和理論を実践：自らの邪悪な衝動を「要因X」という外部寄生体に責任転嫁し（「自分が望んだのではなく内なる要因Xに強いられた」）、個人の道徳的責任を放棄することで、残虐な犯行後も平然と家族と食卓を囲むことを可能にしました。
6. 心理的引き金と自己愛の傷（Precipitating Trigger）: 2004年初頭、The Wichita Eagle紙が30周年特集を組み、Robert Beattieの著作に触れて「BTKは死亡したか忘れ去られた」と報じたことが、病的な誇大自己愛に致命的な一撃を与え、13年の沈黙を破る決定的な引き金となりました。
7. 署名（Signature）対 手口（MO）: 逃走のために柔軟に変遷した犯行手口（電話線切断、手袋、夜間侵入）に対し、内面的な感情を満たす不変の署名（絶対的な拘束支配、興奮を反芻するための運転免許証や装飾品などの戦利品「Trophies」の保管、警察やメディアを挑発する詩やパズルの送付）。
8. 4段階の妄想エスカレーション軌道: 少年時代の小動物虐待と夜間の覗き行為 -> 女性の私的な衣服の窃盗と収集 -> 標的への直接的住居侵入と拘束 -> 人命の破壊と異様な写真撮影。捕食者の歪んだ妄想は、外部からの強制制止がない限り際限なくエスカレートします。
9. ハロー効果と集団的正常性バイアス: 完璧な社会的肩書（元空軍、教会評議会議長、カブスカウト隊長、市の指導員）が強固なハロー効果を生み出し、息が詰まるほどの偏執的な性格も「元軍人の厳格な規律」として受け入れられ、30年間にわたり町全体に巨大な死角を形成しました。
10. 被害者学と生存のための赤い警告（Red Flags）: 警備会社ADTや市役所指導員の特権を悪用した獲物の物色手口を告発。4つの生存警報：(1) 極端なルール統制への執着とマイクロマネジメント；(2) 社交的な外面の裏にある感情的な断絶（浅薄な情動）；(3) 他人の私物を戦利品として密かに収集する習癖；(4) 世間からの承認と賞賛への病的な渇望。「違和感を覚えたら、自らの直感を常に信じること」。

⏱ 目次（チャプター）
00:00 オープニング＆視聴にあたって
00:23 第1幕 · 13年の沈黙を破る再出現の書簡
05:15 第2幕 · 現場検証と事件調書 – 心理的署名とエスカレーション
10:30 第3幕 · 心理解剖 – 悪性ナルシシズムの内面と分断の逆説
16:45 第4幕 · 尋問と対決 – フロッピーディスクのデジタル鑑識の罠
21:45 第5幕 · 断罪と警告 – 生存のための危険信号と結び

⚠️ ご視聴にあたっての注意事項
• 本動画は教育、歴史的ドキュメンタリーおよび犯罪心理学の観点からの分析・解説コンテンツであり、医学的、心理学的、または法的なアドバイスに代わるものではありません。
• 米国の公開記録（セジウィック郡地方裁判所、ウィチタ警察、カンザス州矯正局）に基づいて制作されています。犯罪行為を中傷、名誉毀損、または賛美する意図は一切ありません。
• 登場するキャラクター（フクロウ、オオカミ、キツネ、羊、猫）は演出用の架空のキャラクターです。
• 音声、画像、音楽はAIツールを活用して制作されています。
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 参考資料・公式出典
本動画におけるすべての事件経過、日時、鑑識記録および心理分析は、以下の公式公開記録と照合されています：

▸ 裁判記録および捜査公文書:
• カンザス州セジウィック郡第18司法管轄区地方裁判所 — State of Kansas v. Dennis L. Rader (Case No. 05 CR 498, Gregory Waller判事) — https://www.kscourts.org/
• ウィチタ警察署 (WPD) & FBI行動分析課 (BAU) — BTK特捜班捜査ファイル (Ken Landwehr指揮官) — https://www.wichita.gov/police
• カンザス州矯正局 (KDOC) — 収容者記録: Dennis Lynn Rader (#0083707), エルドラド刑務所 — https://www.doc.ks.gov/
▸ 調査報道および歴史的アーカイブ:
• The Wichita Eagle — BTK調査報道アーカイブ: 1974年の書簡から2004年の再出現まで — https://www.kansas.com/news/special-reports/btk/
• The New York Times — 'Wichita Suspect Is Charged With 10 Murders' & 法廷自供記録 — https://www.nytimes.com/2005/03/01/us/wichita-suspect-is-charged-with-10-murders.html
• CBS News (48 Hours) — 特集ドキュメンタリー: 'The BTK Strangler: The Catch' — https://www.cbsnews.com/news/btk-investigators-reveal-how-they-caught-serial-killer/
• Associated Press (AP) — BTK追跡31年のタイムラインと紫色フロッピーディスクの失策 — https://apnews.com/
▸ 関連書籍および関係者回想録:
• Robert Beattie — 'Nightmare in Wichita: The Hunt for the BTK Strangler' (2004年の再出現の引き金となった書) — https://www.harpercollins.com/
• Kerri Rawson — 回想録: 'A Serial Killer's Daughter: My Story of Faith, Love, and Overcoming' (2019) — https://kerrirawson.com/
• Roy Wenzl, Tim Potter, L. Kelly, Hurst Laviana — 'Bind, Torture, Kill: The Inside Story of the Serial Killer Next Door' (2007)
▸ デジタル鑑識および行動精神医学:
• デジタルフォレンジック分析 — 3.5インチMemorexフロッピーから復元されたWordメタデータ（Christ Lutheran ChurchおよびDennis）の解析 — https://www.forensicfocus.com/
• FBI Law Enforcement Bulletin — 連続殺人犯における悪性ナルシシズムと認知の分断に関する研究 — https://leb.fbi.gov/

🆘 相談窓口および緊急連絡先（日本国内・24時間対応）
• 警察相談専用電話：#9110（事件事故に至る前のストーカー・嫌がらせ・犯罪被害等の相談窓口）
• 児童相談所虐待対応ダイヤル：189（いちはやく・通話料無料）
• こころの健康相談統一ダイヤル：0570-064-556
• よりそいホットライン：0120-279-338（通話料無料）
• 緊急の場合は110番（警察）または119番（救急・消防）

#AmberEyes #TrueCrime #犯罪心理学 #心理分析 #BTK #DennisRader #デニスレイダー #実録犯罪 #未解決事件 #プロファイリング #精神の分断 #自己愛性パーソナリティ障害 #10の心理指標 #ドキュメンタリー
"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG HÀN (KO)
# ==============================================================================
MO_TA_KO = """제05화: 보라색 플로피 디스크와 자기애적 중독 | 범죄심리학: Dennis Rader (10가지 심리적 지표 생태계 & 30년 가면의 붕괴) | Amber eyes

30년 넘는 세월 동안(1974~2005), Dennis Lynn Rader는 미국 캔자스주 파크시티에서 경악스러울 만큼 완벽한 모범 시민의 가면을 쓰고 살았습니다. 4년간 복무한 미 공군 퇴역 군인, 34년간 해로한 성실한 남편, 다정한 아버지, 그리스도 루터교회 평신도 의회 회장, 보이스카우트 컵스카우트 대장, 그리고 매일 잔디 길이를 단속하던 헌신적인 시청 공무원. 그러나 그 독실한 외면 뒤에 숨겨진 정체는 10명의 무고한 생명을 앗아가며 미국 중서부를 공포로 마비시킨 연쇄 살인마 'BTK(Bind, Torture, Kill)'였습니다. 13년간의 완벽한 동면(1991~2004) 끝에, 병적인 자기애와 악명에 대한 갈증은 그로 하여금 스스로 침묵을 깨게 만들었습니다. 경찰을 향한 어처구니없는 질문과 방송국 KSAS-TV로 보낸 한 장의 보라색 1.44MB Memorex 플로피 디스크는 켄 랜드웨어 경위가 설계한 역사적인 디지털 포렌식 덫을 발동시켰고, 두 얼굴의 괴물은 마침내 영원히 쇠창살 뒤로 격리되었습니다.

Amber eyes는 본 사건을 '10대 핵심 심리·행동 지표 생태계'를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 편집증: 30년 동안 캔자스주를 마비시킨 BTK의 공포; 2004년 3월 재등장 서한이 날아들었을 때 주민들은 숨을 죽이고 총기를 구입하며 창문을 걸어 잠그고 서로를 의심했습니다; 연쇄 살인마가 다름 아닌 교회 의회 회장이었다는 사실이 안긴 충격과 배신감; 현대 디지털 포렌식 및 메타데이터 추출 수사의 역사적 분수령이 된 사건.
2. 피해자의 사물화 및 객체화(Objectification): Rader는 피해자들을 '프로젝트(projects)'라 부르며 왜곡된 가학 환상을 연출하기 위한 '살아있는 소품'으로 축소했습니다; 악성 자기애와 반사회적 인격장애의 결합으로 공감 능력이 완전히 상실되었으며, 피해자의 눈물과 애원은 가해자의 전능한 권력 통제감을 극대화하는 자극제로 악용되었습니다.
3. 인지적 구획화(Compartmentalization)와 정상성의 방패: 서로 다른 삶을 완벽히 분리해 닫아두는 능력: 서랍 1은 아내의 성실한 남편이자 딸에게 자전거를 가르쳐준 다정한 아버지, 교회 지도자; 서랍 2는 밤의 냉혹한 사냥꾼; 가족은 사회의 의심을 막아내는 '정상성의 방패(Shield of Normalization)'로 이용되었으며, 딸 Kerri Rawson이 겪어야 했던 평생의 영혼의 상처.
4. 나르시시즘적 붕괴(Narcissistic Collapse)와 병적인 자기연민: 심문실에서 플로피 디스크 추적에 대해 경찰이 거짓말을 했다는 사실에 어린아이처럼 억울해하다가, 정체가 폭로되자 급격한 자기애적 붕괴에 빠져 대학교수가 연구 성과를 발표하듯 10건의 살인을 거침없이 자백; 법정에서는 유가족을 향한 참회 대신 병적인 자기연민(Pathological Self-Pity)만을 드러냈습니다.
5. 도덕적 중화 기술과 '요인 X'(Factor X & Neutralization): 사이크스와 마츠의 중화 이론 적용: Rader는 폭력적 충동을 외부에서 침입한 기생체인 '요인 X'로 규정하고 책임을 전가함으로써("내가 원해서 한 것이 아니라 내 안의 요인 X가 강요한 것이다") 도덕적 가책을 털어내고 태연하게 가정으로 돌아가 식사할 수 있었습니다.
6. 심리적 방아쇠와 자기애적 상처(Precipitating Trigger): 2004년 초, The Wichita Eagle 신문이 사건 30주년 특집을 보도하며 Robert Beattie의 책을 인용해 'BTK는 이미 사망했거나 잊혀졌을 것'이라는 가설을 제기하자, 병적인 자존심에 치명적인 상처를 입고 13년 만에 재등장 편지를 보내는 기폭제가 되었습니다.
7. 시그니처(Signature) vs 범행 수법(MO): 수사망을 피하기 위해 지속적으로 바뀐 범행 수법(전화선 절단, 장갑 착용, 야간 침입, 위장)과 달리, 내면의 감정적 만족을 위해 불변했던 심리적 시그니처(결박을 통한 절대적 통제, 혼자만의 흥분을 위해 운전면허증과 보석을 전리품 Trophies로 보관, 언론과 경찰을 도발하는 시와 암호 퍼즐 발송).
8. 4단계 환상 격상 궤적(Fantasy Escalation Trajectory): 소년 시절 작은 동물 학대 및 야간 관음증 -> 민가 침입 및 여성 사적 의류 절도 -> 표적 주거지 침입 및 직접적 결박 -> 살인 및 기괴한 사진 연출; 외부의 강제적 개입이 없는 한 왜곡된 환상은 끊임없이 더 강력한 자극을 요구합니다.
9. 후광 효과(Halo Effect)와 집단적 정상성 편향: 완벽한 사회적 스펙(공군 참전, 루터교회 의장, 컵스카우트 대장, 시청 공무원)이 강력한 후광을 형성하여 그의 병적인 깐깐함조차 '군인 출신의 철저한 원칙'으로 미화되었고, 30년간 온 마을의 눈을 가린 거대한 사각지대를 만들었습니다.
10. 피해자학 및 생존을 위한 위험 신호(Survival Red Flags): ADT 보안 회사 및 시청 단속원의 직업적 특권을 악용하여 취약 가구를 사냥감으로 물색한 수법; 4대 생존 위험 신호: (1) 극단적인 규칙 통제 집착 및 완고함; (2) 사교적 외면 뒤의 정서적 단절(Shallow Affect); (3) 타인의 사적 물품을 전리품처럼 은밀히 수집하는 버릇; (4) 인정과 칭송에 대한 병적인 자기애적 갈망. 핵심 교훈: "이상한 징후를 마주할 때 자신의 직관을 절대적으로 신뢰하라."

⏱ 챕터(타임라인)
00:00 오프닝 & 시청 안내
00:23 제1막 · 13년 침묵을 깨고 날아든 서한
05:15 제2막 · 현장 분석 & 범죄 파일 – 심리적 서명과 환상의 격상
10:30 제3막 · 심리 해부 – 악성 자기애의 내면과 구획화의 역설
16:45 제4막 · 심문과 대결 – 플로피 디스크의 디지털 포렌식 덫
21:45 제5막 · 단죄와 경고 – 생존의 위험 신호와 결언

⚠️ 시청 전 법적 유의사항
• 본 콘텐츠는 교육, 범죄심리학 및 역사적 분석 목적의 다큐멘터리이며, 전문적인 의학적, 정신과적 또는 법률적 조언을 대신할 수 없습니다.
• 미국 공식 사법 기록(세지윅 카운티 지방법원, 위치타 경찰서, 캔자스주 교정국)을 바탕으로 제작되었습니다. 범죄 행위를 비방하거나 미화하려는 의도가 전혀 없습니다.
• 등장하는 올빼미, 늑대, 여우, 양, 고양이는 시각적 연출을 위한 가상 캐릭터입니다.
• 본 영상의 음성, 시각 이미지, 음악은 AI 기술을 활용하여 제작되었습니다.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 공식 참고자료 및 공판 기록
본 영상의 모든 사건 개요, 날짜, 수사 기록, 디지털 포렌식 분석 및 재판 과정은 다음 공식 공개 기록과 교차 검증되었습니다:

▸ 사법 기록 및 수사 공문서:
• 캔자스주 세지윅 카운티 제18사법관할구 지방법원 — State of Kansas v. Dennis L. Rader (Case No. 05 CR 498, Gregory Waller 판사) — https://www.kscourts.org/
• 위치타 경찰국 (WPD) & FBI 행동분석과 (BAU) — BTK 전담반 수사 파일 (Ken Landwehr 총괄 지휘관) — https://www.wichita.gov/police
• 캔자스주 교정국 (KDOC) — 수감자 기록: Dennis Lynn Rader (#0083707), 엘도라도 교도소 — https://www.doc.ks.gov/
▸ 탐사 보도 및 역사적 아카이브:
• The Wichita Eagle — BTK 심층 탐사 아카이브: 1974년 첫 편지부터 2004년 재등장까지 — https://www.kansas.com/news/special-reports/btk/
• The New York Times — 'Wichita Suspect Is Charged With 10 Murders' & 법정 자백 기록 — https://www.nytimes.com/2005/03/01/us/wichita-suspect-is-charged-with-10-murders.html
• CBS News (48 Hours) — 특집 다큐멘터리: 'The BTK Strangler: The Catch' — https://www.cbsnews.com/news/btk-investigators-reveal-how-they-caught-serial-killer/
• Associated Press (AP) — BTK 31년 추적 연표와 보라색 플로피 디스크의 치명적 실수 — https://apnews.com/
▸ 관련 도서 및 관계자 회고록:
• Robert Beattie — 'Nightmare in Wichita: The Hunt for the BTK Strangler' (2004년 Rader의 재등장을 촉발한 도서) — https://www.harpercollins.com/
• Kerri Rawson — 회고록: 'A Serial Killer's Daughter: My Story of Faith, Love, and Overcoming' (2019) — https://kerrirawson.com/
• Roy Wenzl, Tim Potter, L. Kelly, Hurst Laviana — 'Bind, Torture, Kill: The Inside Story of the Serial Killer Next Door' (2007)
▸ 디지털 포렌식 및 행동정신의학:
• 디지털 포렌식 분석 — 3.5인치 Memorex 플로피 디스크에서 복원된 Word 메타데이터(Christ Lutheran Church 및 Dennis) 분석 — https://www.forensicfocus.com/
• FBI Law Enforcement Bulletin — 연쇄 살인범의 악성 자기애 및 인지적 구획화 연구 — https://leb.fbi.gov/

🆘 긴급 위기 상담 및 피해자 지원 전화 (24시간, 무료)
• 아동학대 신고전화: 112 (경찰청)
• 보건복지상담센터: 129
• 자살예방 상담전화: 109 (24시간 운영)
• 여성긴급전화: 1366
• 미국 전국 가정폭력 핫라인: 1-800-799-SAFE (7233) — https://www.thehotline.org

#AmberEyes #TrueCrime #범죄심리학 #프로파일링 #BTK #DennisRader #데니스레이더 #실제사건 #사건파일 #심리분석 #구획화 #악성자기애 #10대심리지표 #위험신호 #다큐멘터리
"""

# ==============================================================================
# GHI VÀO CÁC TỆP TIẾNG VIỆT
# ==============================================================================
targets_vi = [
    ROOT / "02_SAN_XUAT" / "Tap05" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap05" / "xuat_ban" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap05" / "nguon_mo_ta.txt",
]
for p in targets_vi:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(MO_TA_VI, encoding="utf-8")
    print(f"Wrote VI: {p}")

# Ghi nguon_tham_khao.md
nguon_md_vi = ROOT / "02_SAN_XUAT" / "Tap05" / "nguon_tham_khao.md"
nguon_md_vi_xb = ROOT / "02_SAN_XUAT" / "Tap05" / "xuat_ban" / "nguon_tham_khao.md"
nguon_content_vi = "# TÀI LIỆU THAM KHẢO ĐÃ ĐỐI CHIẾU — TẬP 05\n\n" + MO_TA_VI[MO_TA_VI.find("📚 NGUỒN THAM KHẢO ĐÃ ĐỐI CHIẾU"):]
for p in [nguon_md_vi, nguon_md_vi_xb]:
    p.write_text(nguon_content_vi, encoding="utf-8")
    print(f"Wrote VI refs: {p}")

# ==============================================================================
# GHI VÀO CÁC TỆP TIẾNG ANH (EN)
# ==============================================================================
targets_en = [
    ROOT / "02_SAN_XUAT" / "Tap05_EN" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_EN" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_EN" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_EN" / "xuat_ban" / "mo_ta.txt",
]
for p in targets_en:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(MO_TA_EN, encoding="utf-8")
    print(f"Wrote EN: {p}")

nguon_md_en = ROOT / "02_SAN_XUAT" / "Tap05_EN" / "nguon_tham_khao_EN.md"
nguon_md_en_xb = ROOT / "02_SAN_XUAT" / "Tap05_EN" / "xuat_ban" / "nguon_tham_khao_EN.md"
nguon_content_en = "# VERIFIED SOURCES & COURT EXHIBITS — EPISODE 05\n\n" + MO_TA_EN[MO_TA_EN.find("📚 VERIFIED SOURCES & COURT EXHIBITS"):]
for p in [nguon_md_en, nguon_md_en_xb]:
    p.write_text(nguon_content_en, encoding="utf-8")
    print(f"Wrote EN refs: {p}")

# ==============================================================================
# GHI VÀO CÁC TỆP TIẾNG NHẬT (JA)
# ==============================================================================
targets_ja = [
    ROOT / "02_SAN_XUAT" / "Tap05_JA" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_JA" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_JA" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_JA" / "xuat_ban" / "mo_ta.txt",
]
for p in targets_ja:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(MO_TA_JA, encoding="utf-8")
    print(f"Wrote JA: {p}")

nguon_md_ja = ROOT / "02_SAN_XUAT" / "Tap05_JA" / "nguon_tham_khao_JA.md"
nguon_md_ja_xb = ROOT / "02_SAN_XUAT" / "Tap05_JA" / "xuat_ban" / "nguon_tham_khao_JA.md"
nguon_content_ja = "# 参考資料・公式出典 — 第05話\n\n" + MO_TA_JA[MO_TA_JA.find("📚 参考資料・公式出典"):]
for p in [nguon_md_ja, nguon_md_ja_xb]:
    p.write_text(nguon_content_ja, encoding="utf-8")
    print(f"Wrote JA refs: {p}")

# ==============================================================================
# GHI VÀO CÁC TỆP TIẾNG HÀN (KO)
# ==============================================================================
targets_ko = [
    ROOT / "02_SAN_XUAT" / "Tap05_KO" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_KO" / "mo_ta.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_KO" / "xuat_ban" / "description.txt",
    ROOT / "02_SAN_XUAT" / "Tap05_KO" / "xuat_ban" / "mo_ta.txt",
]
for p in targets_ko:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(MO_TA_KO, encoding="utf-8")
    print(f"Wrote KO: {p}")

nguon_md_ko = ROOT / "02_SAN_XUAT" / "Tap05_KO" / "nguon_tham_khao_KO.md"
nguon_md_ko_xb = ROOT / "02_SAN_XUAT" / "Tap05_KO" / "xuat_ban" / "nguon_tham_khao_KO.md"
nguon_content_ko = "# 공식 참고자료 및 공판 기록 — 제05화\n\n" + MO_TA_KO[MO_TA_KO.find("📚 공식 참고자료 및 공판 기록"):]
for p in [nguon_md_ko, nguon_md_ko_xb]:
    p.write_text(nguon_content_ko, encoding="utf-8")
    print(f"Wrote KO refs: {p}")

print("\nAll description files successfully generated and written!")
