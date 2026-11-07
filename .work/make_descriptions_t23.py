# -*- coding: utf-8 -*-
"""Generate comprehensive descriptions and source files for Tap 23 across 4 languages.
Ensures full coverage of 10 Psychological Indicators (§A2c) and strictly <= 5000 characters.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO GỌN CHO FILE NGUỒN TẬP 23
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 23 (RICHARD RAMIREZ — NIGHT STALKER)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp công khai của Tòa Thượng thẩm California và các cơ quan điều tra:

1. Hồ sơ tòa án & Phán quyết tư pháp chính thức:
• Tòa Thượng thẩm Bang California (Hạt Los Angeles) — Hồ sơ vụ án People of the State of California v. Richard Ramirez (Case No. A704401).
• Biên bản tuyên án tử hình (Thẩm phán Michael Tynan, 11/1989) kết tội 43 tội danh (13 tội giết người, 5 tội âm mưu giết người, 11 tội tấn công bạo lực, 14 tội trộm cắp).
• Cục Quản lý Cải huấn và Phạm nhân Bang California (CDCR) — Hồ sơ tử tù Richard Ramirez (#E35200) tại Nhà tù Bang San Quentin và Giấy chứng tử Bệnh viện Đa khoa Marin (7/6/2013).

2. Báo cáo điều tra thực địa & Bằng chứng kỹ thuật số:
• Sở Cảnh sát Hạt Los Angeles (LASD - Homicide Bureau) & Sở Cảnh sát Los Angeles (LAPD) — Báo cáo chuyên án điều tra Night Stalker Task Force (Thám tử Gil Carrillo & Thám tử Frank Salerno).
• Báo cáo vận hành công nghệ nhận dạng vân tay tự động (AFIS) của Bang California khớp dấu vân tay trên xe Toyota station wagon (8/1985).
• Báo cáo bắt giữ chính thức tại Phố Hubbard, Đông Los Angeles (31/8/1985) và hồ sơ lời khai nhân chứng cộng đồng.

3. Tư liệu điều tra báo chí & Tác phẩm chuyên khảo:
• Philip Carlo — Tác phẩm tư liệu điều tra kinh điển 'The Night Stalker: The Life and Crimes of Richard Ramirez' (Kensington/Citadel Press).
• Los Angeles Times & San Francisco Chronicle — Kho tư liệu báo chí điều tra hiện trường và phóng sự phòng xử án giai đoạn 1984–1989.

4. Tâm lý học hành vi & Pháp y:
• Hội chứng Say mê Tội phạm (Hybristophilia / Bonnie & Clyde Syndrome) — Nghiên cứu tâm thần học pháp y của John Money & Sheila Isenberg ('Women Who Love Men Who Kill').
• Khái niệm Tội phạm hỗn hợp (Mixed Offender), Tổn thương não bộ thời thơ ấu (Frontal & Temporal Lobe Damage), Cơ chế Chia ngăn nhận thức (Compartmentalization) & 'The Gift of Fear' (Gavin de Becker).

5. Đường dây nóng hỗ trợ & bảo vệ:
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7): http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng phòng chống bạo lực gia đình: 1900 969 680
"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 23 (RICHARD RAMIREZ — NIGHT STALKER)
Amber eyes adheres to multi-source verification using verified public court records and official filings:

1. Official Court Transcripts & Judicial Rulings:
• Superior Court of California (County of Los Angeles) — State of California v. Richard Ramirez (Case No. A704401).
• Formal Death Penalty Sentencing Order (Judge Michael Tynan, Nov 1989) convicting on 43 counts (13 murders, 5 attempted murders, 11 sexual assaults, 14 burglaries).
• California Department of Corrections and Rehabilitation (CDCR) — Death row inmate record for Richard Ramirez (#E35200) at San Quentin State Prison and Marin General Hospital Certificate of Death (June 7, 2013).

2. Law Enforcement & Forensic Records:
• Los Angeles County Sheriff's Department (LASD Homicide Bureau) & LAPD — Official Night Stalker Task Force reports (Detectives Gil Carrillo and Frank Salerno).
• State of California Automated Fingerprint Identification System (AFIS) match report on stolen orange Toyota station wagon (August 1985).
• Official East Los Angeles arrest incident log and citizen apprehension records on Hubbard Street (August 31, 1985).

3. Investigative Journalism & Criminology Literature:
• Philip Carlo — Definitive biographical dossier: 'The Night Stalker: The Life and Crimes of Richard Ramirez' (Citadel Press).
• Los Angeles Times & San Francisco Chronicle — Comprehensive investigative archives and courtroom coverage (1984–1989).

4. Behavioral Sciences:
• Hybristophilia & Bonnie and Clyde Syndrome in forensic psychiatry — Studies by John Money and Sheila Isenberg ('Women Who Love Men Who Kill').
• Mixed Offender dynamics, childhood organic trauma, cognitive compartmentalization, and intuitive threat detection ('The Gift of Fear' by Gavin de Becker).

5. Crisis Helplines & Support:
• 988 Suicide & Crisis Lifeline (US/Canada, toll-free 24/7): Dial 988 — https://988lifeline.org/
• National Domestic Violence Hotline: 1-800-799-SAFE (7233) — https://www.thehotline.org/
"""

SOURCES_JA = """📚 第23話 参考文献・公式調査資料一覧（リチャード・ラミレス事件）
Amber eyesは、カリフォルニア州上級裁判所の公開公判記録および警察当局の公式捜査記録に基づく事実確認を徹底しています：

1. 公式裁判記録および司法判決:
• カリフォルニア州上級裁判所（ロサンゼルス郡） — カリフォルニア州対リチャード・ラミレス公判記録（事件番号 A704401）。
• 死刑宣告判決文（マイケル・タイナン裁判長、1989年11月）：殺人13件を含む起訴43件すべてにおける有罪宣告。
• カリフォルニア州矯正リハビリテーション局（CDCR） — サン・クエンティン州立刑務所における死刑囚記録（#E35200）およびマリン総合病院死亡診断書（2013年6月7日）。

2. 法科学捜査報告書および電子的証拠:
• ロサンゼルス郡保安官事務所（LASD殺人課）およびロサンゼルス市警察（LAPD） — ナイト・ストーカー専従捜査班公式記録（ギル・カリーロ刑事、フランク・サレルノ刑事）。
• カリフォルニア州自動指紋照合システム（AFIS）による盗難トヨタ・ステーションワゴンの指紋照合報告書（1985年8月）。
• イースト・ロサンゼルス・ハバード通りにおける市民逮捕・警察護送記録（1985年8月31日）。

3. 調査報道および学術文献:
• フィリップ・カーロ著『The Night Stalker: The Life and Crimes of Richard Ramirez』。
• ロサンゼルス・タイムズ紙およびサンフランシスコ・クロニクル紙の事件・法廷報道アーカイブ（1984〜1989年）。
• 法精神医学における犯罪者愛好症（ヒブリストフィリア / ボニー＆クライド症候群）およびギャビン・デ・ベッカー著『The Gift of Fear』。

4. 相談窓口・支援ホットライン:
• こころの健康相談統一ダイヤル: 0570-064-556 / よりそいホットライン: 0120-279-338 / 配偶者暴力相談支援センター: 0570-0-55210
"""

SOURCES_KO = """📚 제23화 참고 문헌 및 공식 수사 기록 (리처드 라미레즈 사건)
Amber eyes는 캘리포니아주 상급법원의 공개 공판 기록 및 사법 당국의 공인 수사 문서를 바탕으로 사실 확인을 거쳤습니다:

1. 공식 법원 공판 기록 및 사법 판결:
• 캘리포니아주 상급법원 (로스앤젤레스 카운티) — 캘리포니아주 대 리처드 라미레즈 공판 기록 (사건번호 A704401).
• 사형 선고 판결문 (마이클 타이난 판사, 1989년 11월): 13건의 살인을 포함한 43건의 기소 혐의 전원 유죄 판결.
• 캘리포니아 교정재활국 (CDCR) — 샌  Quentin 주립 교도소 사형수 수감 기록 (#E35200) 및 마린 종합병원 사망진단서 (2013년 6월 7일).

2. 수사기관 보고서 및 과학수사 증거:
• 로스앤젤레스 카운티 보안관국 (LASD) 및 LA 경찰청 (LAPD) — 나이트 스토커 전담 수사본부 공식 수사 보고서 (길 카릴로 형사, 프랭크 살레르노 형사).
• 캘리포니아주 자동 지문 식별 시스템 (AFIS) 도난 토요타 왜건 지문 일치 감식 보고서 (1985년 8월).
• 이스트 로스앤젤레스 허버드 거리 시민 체포 및 경찰 인계 공식 기록 (1985년 8월 31일).

3. 탐사 보도 및 학술 전문 서적:
• 필립 카를로 — 탐사 평전 'The Night Stalker: The Life and Crimes of Richard Ramirez'.
• 로스앤젤레스 타임스 및 샌프란시스코 크로니클 법정 취재 아카이브 (1984–1989).
• 법정신의학 범죄자 매혹 증후군 (Hybristophilia) 및 개빈 드 베커 저서 'The Gift of Fear'.

4. 긴급 상담 및 지원 핫라인:
• 자살예방 상담전화: 109 / 정신건강: 1577-0199 / 여성긴급전화: 1366 / 경찰청: 112
"""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Ám Ảnh 'Night Stalker' & Bí Ẩn Hội Chứng Say Mê Tội Phạm — Tội Ác Ngẫu Nhiên, Đấu Trí AFIS & Ảo Tưởng Người Giải Cứu (Hồ Sơ Richard Ramirez) | Tâm lý học tội phạm | Amber eyes

Mùa hè năm 1985, một đợt nắng nóng kỷ lục thiêu đốt bang California, nhưng cư dân Los Angeles lại run rẩy trong nỗi sợ hãi tột cùng. Một bóng ma vô hình đột nhập vào nhà dân lúc nửa đêm, tấn công không theo bất kỳ quy luật nào và để lại biểu tượng ngôi sao năm cánh ngược kỳ dị. Cả thành phố rơi vào cơn hoang tưởng tập thể: hàng triệu gia đình đóng chặt cửa sổ, thức trắng đêm và vũ trang để tự vệ.

Bước đột phá xuất hiện khi công nghệ nhận dạng vân tay tự động AFIS lần đầu tiên trong lịch sử phá án khớp một dấu vân tay duy nhất trên chiếc xe Toyota bị đánh cắp với cái tên: Richard Ramirez. Sáng 31/8/1985, khi ảnh chân dung xuất hiện trên trang nhất tất cả các báo lớn, kẻ sát nhân đã bị chính những người dân quả cảm tại khu phố Đông Los Angeles truy đuổi và khống chế trên vỉa hè. Nhưng khi phiên tòa mở màn, một nghịch lý gây sốc nổ ra: hàng trăm phụ nữ trẻ mặc đồ đen, chen lấn dự tòa và gửi hàng nghìn thư tình cho kẻ ác — khởi đầu của cơn sốt tâm lý bệnh hoạn mang tên Hội chứng say mê tội phạm (Hybristophilia).

Hồ sơ Richard Ramirez được Amber eyes giải phẫu toàn diện qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (§A2c):
1. DƯ CHẤN XÃ HỘI & HOANG TƯỞNG TẬP THỂ: Cơn hoang tưởng tập thể bao trùm California hè 1985; sức mạnh quả cảm của cộng đồng Đông Los Angeles bắt giữ kẻ thủ ác; bước ngoặt lịch sử của công nghệ nhận dạng vân tay AFIS.
2. VẬT HÓA & PHI NHÂN HÓA: Tấn công ngẫu nhiên mọi lứa tuổi, coi nạn nhân là đạo cụ thỏa mãn bản năng quyền lực; khuyết tật Thuyết tâm trí (Theory of Mind) và thiếu hụt thấu cảm cảm xúc sâu sắc.
3. CƠ CHẾ CHIA NGĂN NHẬN THỨC: Quá khứ El Paso trốn đòn roi ra ngủ nghĩa trang; bi kịch danh dự của gia đình Ramirez; sự tan vỡ ảo tưởng của Doreen Lioy khi ADN năm 2009 vạch trần sự thật.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ: Sự trơ tráo trước tòa với câu nói ngông cuồng "Hẹn gặp ở Disneyland"; bản án tâm lý trần trụi khi chết trong bệnh tật và cô độc tại San Quentin năm 2013.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC: Mượn vỏ bọc tà giáo Satan để ru ngủ lương tri, ngoại hóa trách nhiệm và đổ lỗi cho thế giới thối nát.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Hai tai nạn chấn thương não thời thơ ấu gây động kinh thùy thái dương, người cha bạo hành và cú sốc năm 13 tuổi chứng kiến anh họ Miguel bắn chết vợ.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO (giày Avia 11.5, cắt dây điện thoại, đột nhập đêm) vs. Signature bất biến (ngôi sao năm cánh Pentagram, lục tủ lạnh, ép nạn nhân thề thốt để khẳng định quyền lực).
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Dung nạp kích thích từ nhìn trộm qua cửa sổ -> trộm vặt -> đột nhập nhà có người -> bạo lực giết người hàng loạt.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Hiệu ứng hào quang ngược gán ghép vẻ ngoài góc cạnh với chiều sâu nội tâm; truyền thông giật gân tạo điểm mù đạo đức nguy hiểm.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ: Tôn vinh các nạn nhân và cộng đồng; giải mã Hội chứng Hybristophilia & Ảo tưởng người giải cứu (Can-Fix-Him Syndrome); đúc kết 4 cảnh báo đỏ nhận diện và phòng ngừa độc hại.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Mùa hè rực lửa 1985 & cơn ác mộng rình rập ban đêm
06:15 Hồi 2 · Phiên tòa cuồng loạn & những người hâm mộ kẻ sát nhân
12:30 Hồi 3 · Giải mã tâm lý: Chấn thương não bộ & hội chứng say mê tội phạm (Hybristophilia)
19:15 Hồi 4 · Di sản tư pháp & sự sụp đổ của một ảo tượng
25:45 Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện hội chứng say mê độc hại

⚠️ LƯU Ý
• Nội dung mang tính giáo dục, phân tích dưới góc nhìn tâm lý học tội phạm và pháp y hành vi; không thay thế tư vấn y khoa hay pháp lý.
• Thông tin dựa trên hồ sơ Tòa Thượng thẩm California và báo cáo chuyên án của LASD & LAPD.

📚 NGUỒN THAM KHẢO CHÍNH
• Tòa Thượng thẩm Bang California (Hạt Los Angeles) — Hồ sơ State v. Richard Ramirez (Case No. A704401).
• LASD & LAPD — Báo cáo chuyên án Night Stalker Task Force & AFIS match report (1985).
• Philip Carlo — 'The Night Stalker: The Life and Crimes of Richard Ramirez'.
• Gavin de Becker — Tác phẩm 'The Gift of Fear' về trực giác sinh tồn.

🆘 Nếu bạn biết một trẻ em đang bị bạo hành hoặc cần hỗ trợ khẩn cấp, hãy gọi Tổng đài quốc gia
bảo vệ trẻ em 111 (Việt Nam, miễn phí 24/7).
• Đường dây nóng Ngày Mai (Khủng hoảng tâm lý & hỗ trợ trầm cảm): 096 306 1414
• Đường dây nóng Ngôi nhà Bình Yên (Phòng chống bạo lực gia đình): 1900 969 680
• National Domestic Violence Hotline (US): 1-800-799-SAFE (7233)
• National Center for Victims of Crime: https://victimsofcrime.org

#RichardRamirez #NightStalker #TamLyHocToiPham #AmberEyes #HoSoVuAn #Hybristophilia #CanFixHim #AFIS #CanhBaoDoSinhTon
"""

DESC_EN = """The 'Night Stalker' Terror & The Enigma of Hybristophilia — Random Atrocities, AFIS Breakthrough & The Savior Delusion (The Richard Ramirez Dossier) | Forensic Psychology | Amber eyes

In the scorching summer of 1985, a record-breaking heatwave gripped California, yet the residents of Los Angeles shivered in bone-chilling terror. An elusive phantom invaded homes in the dead of night without pattern or boundary, leaving bizarre inverted pentagrams at crime scenes. The city descended into collective paranoia: millions of families bolted windows, endured sleepless nights, and armed themselves in desperate self-defense.

The historic breakthrough arrived when California's newly deployed Automated Fingerprint Identification System (AFIS) achieved a technological triumph, matching a single print on a stolen Toyota station wagon to twenty-five-year-old Richard Ramirez. On August 31, 1985, when his mugshot dominated front pages statewide, the predator was chased down and restrained on the sidewalk by courageous East Los Angeles citizens. Yet when the courtroom proceedings opened, a grotesque spectacle erupted: scores of young women dressed in black queued for seats, showering the killer with adoring love letters — igniting a chilling manifestation of Hybristophilia (Bonnie and Clyde Syndrome).

The Richard Ramirez dossier is clinically examined through the 10 Psychological & Behavioral Dimensions (§A2c):
1. SOCIETAL IMPACT & COLLECTIVE PARANOIA: The 1985 summer terror in California; heroic community apprehension on Hubbard Street; the historic forensic milestone of automated fingerprint technology (AFIS).
2. OBJECTIFICATION & DEHUMANIZATION: Indiscriminate targeting treating victims as props for predatory dominance; profound Theory of Mind deficit and complete lack of affective empathy.
3. COGNITIVE COMPARTMENTALIZATION: El Paso childhood fleeing domestic beatings to sleep in cemeteries; the honor tragedy of the Ramirez family; Doreen Lioy's marriage unraveling when 2009 DNA evidence exposed the truth.
4. NARCISSISTIC COLLAPSE: Courtroom insolence epitomized by the infamous "See you in Disneyland" parting shot; the stark psychological verdict of dying diseased and completely abandoned at San Quentin in 2013.
5. TECHNIQUES OF NEUTRALIZATION: Weaponizing occult satanic delusions to anesthetize conscience, displacing responsibility, and rationalizing atrocities as mirrors of a corrupt world.
6. PRECIPITATING STRESSOR & TIPPING POINT: Severe childhood head trauma causing temporal lobe epilepsy, parental abuse, and the foundational trauma at age 13 witnessing his cousin Miguel murder his wife.
7. SIGNATURE VS. MODUS OPERANDI: Evolving MO (Avia size 11.5 sneakers, cutting phone lines, nocturnal burglary) vs. constant psychological signature (inverted pentagrams, looting refrigerators, forcing oaths of allegiance).
8. FANTASY ESCALATION TRAJECTORY: Behavioral tolerance buildup progressing from voyeurism to petty burglary, hot prowls, and serial lethal violence.
9. HALO EFFECT & SOCIAL BLINDSPOTS: The reverse halo effect where angular features were blindly conflated with brooding charisma; media sensationalism creating dangerous moral blindspots.
10. VICTIMOLOGY & 4 RED FLAGS: Honoring victim resilience and community heroes; deconstructing Hybristophilia and the Can-Fix-Him syndrome; distilling 4 actionable survival red flags.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Advisory
00:23 Act 1 · The Scorching Summer of 1985 & The Prowling Nightmare
06:15 Act 2 · Courtroom Sensationalism & The Killer's Devotees
12:30 Act 3 · Psychological Deconstruction: Brain Trauma & Hybristophilia
19:15 Act 4 · Judicial Legacy & The Collapse of an Illusion
25:45 Act 5 · Solemn Reflection & 4 Vital Red Flags of Toxic Attraction

⚠️ ADVISORY
• Educational content analyzed through forensic behavioral science; does not replace legal or medical counsel.
• Based on public court transcripts from Los Angeles County Superior Court and official LASD/LAPD files.

📚 PRIMARY SOURCES
• California Superior Court (Los Angeles County) — State v. Richard Ramirez (Case No. A704401).
• LASD & LAPD — Official Night Stalker Task Force reports and AFIS records (1985).
• Philip Carlo — 'The Night Stalker: The Life and Crimes of Richard Ramirez'.
• Gavin de Becker — 'The Gift of Fear' (Intuitive Survival Frameworks).

📞 CRISIS HELPLINES
• 988 Suicide & Crisis Lifeline (US/Canada): Dial 988
• National Domestic Violence Hotline: 1-800-799-SAFE (7233)

#RichardRamirez #NightStalker #ForensicPsychology #AmberEyes #TrueCrime #Hybristophilia #CanFixHimSyndrome #AFIS #TheGiftOfFear #SurvivalRedFlags
"""

DESC_JA = """ナイト・ストーカーの悪夢と犯罪者愛好症の深淵 — 無差別侵入、AFIS指紋捜査と救済者妄想の崩壊（リチャード・ラミレス事件）| 犯罪心理学 | Amber eyes

1985年の夏、記録的な猛暑がカリフォルニアを襲う中、ロサンゼルスの住民たちは骨の髄まで凍りつく恐怖に震えていました。真夜中に何の規則もなく民家に侵入し、逆五芒星の印を残していく正体不明の怪異。街全体が集団的パラノイアに包まれ、何百万もの家庭が窓を閉ざし、銃を手に眠れぬ夜を過ごしました。

事件が動いたのは、カリフォルニア州に導入されたばかりの自動指紋照合システムAFISが、盗難車に残された指紋から25歳のリチャード・ラミレスを特定した瞬間でした。1985年8月31日の朝、顔写真が新聞1面を飾ると、逃走する殺人犯はイースト・ロサンゼルスの勇敢な住民たちによって歩道上で制圧されました。しかし法廷が開かれると、異様な光景が展開します。黒い服を着た若い女性たちが傍聴席に押し寄せ、熱烈なファンレターを送り始めたのです。犯罪者愛好症（ヒブリストフィリア）の病理が露わになりました。

Amber eyesは本事件を「10の犯罪心理・行動分析指標（§A2c）」を通じて完全解剖します：
1. 社会的激震と集団的パラノイア: 1985年カリフォルニアの集団的パニック；イースト・ロサンゼルス住民による勇気ある犯人逮捕；指紋自動識別システム（AFIS）の歴史的快挙。
2. 客観化と脱人間化: 無差別に標的を選び被害者を権力欲の道具へと貶める冷酷さ；心の理論（Theory of Mind）の障害と情緒的共感の欠如。
3. 認知的区画化: 父親の暴力から逃れ墓地で夜を明かしたエルパソの過去；ラミレス家の名誉の悲劇；2009年のDNA鑑定によりドリーン・リオイの幻想が完全に崩壊した真相。
4. 自己愛性崩壊: 「ディズニーランドで会おう」と言い放った法廷での傲慢さ；2013年サン・クエンティンで病気と絶対的孤独の中で息絶えた冷厳な心理的判決。
5. 道徳的中和技術: 良心を麻痺させ責任を外部化するためオカルト的な悪魔崇拝を口実として利用した自己正当化。
6. 心理的引き金と限界点: 幼少期の2度の頭部外傷による側頭葉てんかん、家庭内暴力、13歳で従兄が妻を射殺する現場を目撃した決定打。
7. シグネチャーと手口（MO）: 変容するMO（アビア11.5スニーカー、電話線切断、深夜侵入）対不変の署名（逆五芒星、冷蔵庫の物色、忠誠の誓いの強制）。
8. 妄想のエスカレーション軌道: 覗き見から空き巣、住居侵入、そして連続殺人へと暴走した刺激への耐性形成。
9. ハロー効果と社会的盲点: 鋭角的な顔立ちを男らしい魅力と盲信した逆ハロー効果；メディアの扇情報道が生んだ危険な倫理的盲点。
10. 被害者学と4つの赤い警告: 被害者と地域社会の勇気の顕彰；ヒブリストフィリアと救済者妄想（Can-Fix-Him）の解剖；危険な関係を見抜く4大危険兆候。

⏱ チャプター
00:00 イントロ＆留意事項
00:23 第1幕 · 1985年の猛暑と夜の恐怖
06:15 第2幕 · 熱狂の法廷と殺人鬼に魅せられた人々
12:30 第3幕 · 心理解剖: 脳損傷と犯罪者愛好症
19:15 第4幕 · 司法の遺産と幻影の崩壊
25:45 第5幕 · 警鐘のメッセージと危険な魅惑を見抜く4つの赤い警告

⚠️ ご案内
• 本動画は司法行動科学および犯罪心理学に基づく教育的分析であり、法的・医学的助言に代わるものではありません。
• ロサンゼルス郡上級裁判所および警察当局の公式公開記録に基づき制作されています。

📚 主な参考文献
• カリフォルニア州上級裁判所 — State v. Richard Ramirez 公判記録
• LASDおよびLAPD — ナイト・ストーカー専従班報告書およびAFIS鑑識記録（1985）
• フィリップ・カーロ著『The Night Stalker: The Life and Crimes of Richard Ramirez』
• ギャビン・デ・ベッカー著『The Gift of Fear』

📞 相談ホットライン
• こころの健康相談統一ダイヤル: 0570-064-556 / よりそいホットライン: 0120-279-338 / 配偶者暴力相談支援センター: 0570-0-55210

#リチャードラミレス #ナイトストーカー #犯罪心理学 #AmberEyes #事件解説 #ヒブリストフィリア #救済者妄想 #AFIS #危険兆候 #法科学
"""

DESC_KO = """'Night Stalker'의 악몽과 범죄자 매혹 증후군의 심연 — 무차별 침입, AFIS 지문 수사와 구원자 망상의 파멸 (리처드 라미레즈 사건) | 범죄심리학 | Amber eyes

1985년 여름, 기록적인 폭염이 캘리포니아를 덮쳤지만 로스앤젤레스 시민들은 뼛속까지 시린 공포에 떨었습니다. 한밤중에 규칙도 경계도 없이 침입해 기괴한 역오망성 기호를 남기는 정체불명의 살인마. 도시 전체가 집단적 편집증에 휩싸였고, 수백만 가구가 창문을 굳게 걸어 잠근 채 총기를 들고 뜬눈으로 밤을 지새웠습니다.

사건의 결정적 돌파구는 캘리포니아주에 갓 도입된 컴퓨터 자동 지문 식별 시스템 AFIS가 도난 차량에 남겨진 단 하나의 지문으로부터 스물다섯 살의 리처드 라미레즈를 특정하면서 찾아왔습니다. 1985년 8월 31일 아침, 얼굴 사진이 신문 1면을 장식하자 도주하던 살인마는 이스트 로스앤젤레스의 용감한 시민들에게 포위되어 보도 위에서 제압되었습니다. 하지만 법정이 열리자 충격적인 역설이 벌어졌습니다. 검은 옷을 입은 젊은 여성들이 방청석을 메우고 수백 통의 연애편지를 보내기 시작한 것입니다. 바로 범죄자 매혹 증후군(Hybristophilia)의 출현이었습니다.

Amber eyes는 본 사건을 '10대 범죄 심리·행동 분석 지표(§A2c)'로 심층 해부합니다:
1. 사회적 파장과 집단적 편집증: 1985년 캘리포니아를 휩쓴 집단 공포; 이스트 로스앤젤레스 시민들의 용기 있는 범인 검거; 자동 지문 식별 시스템(AFIS)의 역사적 승리.
2. 사물화와 비인간화: 피해자를 권력욕과 폭력성을 충족하기 위한 도구로 취급한 무차별 범행; 마음 이론(Theory of Mind)의 결함과 정서적 공감의 완전한 결여.
3. 인지적 구획화: 아버지의 학대를 피해 묘지에서 밤을 지새우던 엘파소 시절의 상처; 라미레즈 가족의 명예 붕괴; 2009년 DNA 감식으로 도린 리오이의 환상이 완전히 깨진 비극.
4. 자기애적 붕괴: 법정에서 "디즈니랜드에서 다시 만나자"고 지껄인 오만함; 2013년 샌 퀜틴 교도소에서 질병과 완전한 고독 속에 숨진 냉혹한 심리적 단죄.
5. 도덕적 중화 기법: 양심을 마비시키고 책임을 외부화하기 위해 오컬트 사탄 숭배를 핑계로 삼아 흉악 범죄를 정당화한 기제.
6. 심리적 방아쇠와 임계점: 유년기 두 차례 뇌진탕으로 인한 측두엽 뇌전증, 가정 폭력, 13세 때 사촌 형 미겔이 아내를 총격 살해하는 현장을 목격한 충격.
7. 시그니처와 범행 수법(MO): 진화하는 MO(아비아 11.5 운동화, 전화선 절단, 야간 침입) 대 불변의 서명(역오망성, 냉장고 뒤지기, 충성 맹세 강요).
8. 망상 에스컬레이션 궤적: 훔쳐보기에서 절도, 주거 침입, 연쇄 살인으로 폭주한 자극에 대한 내성 형성 과정.
9. 후광 효과와 사회적 맹점: 날카로운 외모를 남성적 매력으로 맹목적으로 오인한 역후광 효과; 미디어의 황색 저널리즘이 낳은 도덕적 맹점.
10. 피해자학과 4대 위험 징후: 피해자와 시민 영웅들의 연대 기림; 범죄자 매혹 증후군과 구원자 망상(Can-Fix-Him) 해부; 유해한 관계를 막는 4대 생존 레드 플래그.

⏱ 챕터 타임라인
00:00 인트로 및 안내
00:23 막 1 · 1985년의 뜨거운 여름과 밤의 침입자
06:15 막 2 · 광란의 법정과 살인자를 숭배하는 팬들
12:30 막 3 · 심리 해부: 뇌 손상과 범죄자 매혹 증후군
19:15 막 4 · 사법적 유산과 환상의 붕괴
25:45 막 5 · 경종의 메시지와 유해한 매혹을 분별하는 4대 레드 플래그

⚠️ 유의 사항
• 본 콘텐츠는 법행동과학 및 범죄심리학 분석에 기반한 교육적 영상이며 법적·의학적 조언을 대신하지 않습니다.
• 로스앤젤레스 카운티 법원 및 경찰 당국의 공개 사법 기록을 토대로 제작되었습니다.

📚 주요 참고 문헌
• 캘리포니아주 상급법원 — State v. Richard Ramirez 공판 기록
• LASD 및 LAPD — 나이트 스토커 전담반 공식 수사 보고서 및 AFIS 기록 (1985)
• 필립 카를로 — 'The Night Stalker: The Life and Crimes of Richard Ramirez'
• 개빈 드 베커 — 'The Gift of Fear' (직관적 생존 과학)

📞 긴급 상담 핫라인
• 자살예방 상담전화: 109 / 여성긴급전화: 1366 / 경찰청: 112

#리처드라미레즈 #나이트스토커 #범죄심리학 #AmberEyes #사건파일 #히브리토필리아 #구원자망상 #AFIS #생존위험징후 #법정드라마
"""

TARGETS = [
    # Tiếng Việt
    (ROOT / "02_SAN_XUAT" / "Tap23" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap23" / "xuat_ban" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap23" / "nguon_tham_khao.md", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap23" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap23" / "nguon_mo_ta.txt", SOURCES_VI),
    
    # Tiếng Anh
    (ROOT / "02_SAN_XUAT" / "Tap23_EN" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap23_EN" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap23_EN" / "xuat_ban" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap23_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap23_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap23_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap23_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),

    # Tiếng Nhật
    (ROOT / "02_SAN_XUAT" / "Tap23_JA" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap23_JA" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap23_JA" / "xuat_ban" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap23_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap23_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap23_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap23_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),

    # Tiếng Hàn
    (ROOT / "02_SAN_XUAT" / "Tap23_KO" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap23_KO" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap23_KO" / "xuat_ban" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap23_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap23_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap23_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap23_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
]

print("=" * 70)
print(">>> KIỂM TRA ĐỘ DÀI VÀ GHI FILE MÔ TẢ TẬP 23 (4 NGÔN NGỮ) <<<")
print("=" * 70)

all_passed = True

desc_lengths = {
    "VN": len(DESC_VI),
    "EN": len(DESC_EN),
    "JA": len(DESC_JA),
    "KO": len(DESC_KO),
}

for lang, length in desc_lengths.items():
    status = "PASS (<= 5000 ký tự)" if length <= 5000 else "FAIL (> 5000 ký tự)"
    if length > 5000:
        all_passed = False
    print(f"  {lang} Description: {length} ký tự -> {status}")

for path, text in TARGETS:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.strip() + "\n")
    print(f"  Saved: {path.relative_to(ROOT)} ({len(text)} chars)")

if all_passed:
    print("\n>>> TẤT CẢ 4 BẢN MÔ TẢ ĐỀU ĐẠT CHUẨN HOÀN TOÀN VÀ ĐỀU DƯỚI 5000 KÝ TỰ! <<<")
else:
    print("\n>>> CẢNH BÁO: CÓ BẢN MÔ TẢ VƯỢT QUÁ 5000 KÝ TỰ! <<<")
print("=" * 70)
