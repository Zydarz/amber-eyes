#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo các file mô tả và nguồn tham khảo cho Tập 14 trên 4 ngôn ngữ (VN, EN, JA, KO).
Đảm bảo đầy đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c, K10) và TUYỆT ĐỐI <= 5000 ký tự.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO CHO TẬP 14
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 14 (HỒ SƠ BETTY BRODERICK)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp chính thức của California và báo chí điều tra Hoa Kỳ:

1. Hồ sơ Tòa án & Phán quyết tư pháp Bang California:
• Tòa Thượng thẩm Bang California Hạt San Diego (San Diego Superior Court) — Hồ sơ xét xử People of the State of California v. Elisabeth Anne Broderick (Case No. CR113886, Thẩm phán Thomas J. Whelan): https://www.sdcourt.ca.gov/
• Văn phòng Biện lý Quận San Diego (San Diego District Attorney's Office) — Bản cáo trạng và chứng cứ xét xử của Công tố viên Kerry Wells: https://www.danewstoday.com/
• Tòa Phúc thẩm California Khu vực 4 (California Court of Appeal, 4th District) — Quyết định bác kháng cáo năm 1994 (Appeal No. D016254).
• Cục Cải huấn & Phục hồi California (CDCR) — Biên bản điều trần bác đơn ân xá các năm 2010 và 2017 đối với phạm nhân W42477: https://www.cdcr.ca.gov/

2. Hồ sơ Điều tra & Cảnh sát thực địa:
• Sở Cảnh sát San Diego (San Diego Police Department - SDPD) — Báo cáo khám nghiệm hiện trường số 1041 Đại lộ Coral Reef ngày 05/11/1989 và biên bản đầu thú của Elisabeth Broderick: https://www.sandiego.gov/police
• Bản ghi âm hộp thư thoại lưu trữ tại SDPD — Hàng trăm cuộc gọi và tin nhắn quấy rối từ Betty gửi tới văn phòng luật và nhà riêng của Daniel Broderick (1985–1989).

3. Báo chí Điều tra & Tác phẩm tài liệu chuyên sâu:
• Bella Stumbo (Ký giả điều tra Los Angeles Times) — Tác phẩm chuyên khảo xuất sắc 'Until the Twelfth of Never: The Deadly Divorce of Dan & Betty Broderick' (Pocket Books, 1993): https://www.latimes.com/
• Los Angeles Times — Lưu trữ trọn vẹn phóng sự hai phiên tòa xét xử chấn động San Diego (1990 & 1991): https://www.latimes.com/archives/
• The New York Times — Bài phân tích xã hội học về phong trào phụ nữ và phản ứng phân cực trước vụ án Betty Broderick: https://www.nytimes.com/
• Tạp chí San Diego Magazine — Hồ sơ tranh chấp tài sản ly hôn triệu đô và cuộc đối đầu pháp lý nội bộ giới luật gia: https://www.sandiegomagazine.com/

4. Tâm lý học Pháp y, Tâm thần học & Hành vi học:
• Bác sĩ Tâm thần học Pháp y Park Dietz — Báo cáo giám định tâm thần pháp y độc lập về nhân cách Betty Broderick.
• Hiệp hội Tâm thần học Hoa Kỳ (APA) — Nghiên cứu chuyên sâu về Hội chứng Thao túng thực tại (Gaslighting), Tổn thương ái kỷ (Narcissistic Injury), Rối loạn nhân cách ranh giới (BPD) và Cơn thịnh nộ ái kỷ (Narcissistic Rage).
• Gavin de Becker — Tác phẩm kinh điển về khoa học trực giác và nhận diện nguy cơ sinh tồn 'The Gift of Fear' (Dell Publishing, 1997).

5. Đường dây nóng hỗ trợ khủng hoảng & phòng chống bạo lực:
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý & trầm cảm): 096 306 1414
• Đường dây nóng Phòng chống Bạo lực Gia đình (Việt Nam): 1900 969 680
• National Domestic Violence Hotline (Hoa Kỳ): 1-800-799-SAFE (7233) — https://www.thehotline.org/"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 14 (BETTY BRODERICK)
Amber eyes adheres to multi-source cross-verification from official California judicial records and investigative journalism:

1. California State Court Archives & Official Judicial Verdicts:
• San Diego County Superior Court — Criminal Trial Record People of the State of California v. Elisabeth Anne Broderick (Case No. CR113886, Hon. Thomas J. Whelan presiding): https://www.sdcourt.ca.gov/
• San Diego District Attorney's Office — Official Indictment and Evidentiary Exhibits by Deputy District Attorney Kerry Wells: https://www.danewstoday.com/
• California Court of Appeal, Fourth Appellate District — Affirmation of Conviction (1994, Appeal No. D016254).
• California Department of Corrections and Rehabilitation (CDCR) — Formal Parole Hearing Decisions denying parole in 2010 and 2017 (Inmate W42477): https://www.cdcr.ca.gov/

2. Law Enforcement & Field Forensic Records:
• San Diego Police Department (SDPD) — Crime Scene Investigation Report for 1041 Coral Reef Avenue (Nov 5, 1989) and voluntary surrender records: https://www.sandiego.gov/police
• SDPD Forensic Audio Evidence Archive — Transcribed telephone answering machine recordings of harassing communications between 1985 and 1989.

3. Investigative Journalism & Primary Biographies:
• Bella Stumbo (Los Angeles Times Investigative Journalist) — Definitive biographical volume 'Until the Twelfth of Never: The Deadly Divorce of Dan & Betty Broderick' (Pocket Books, 1993): https://www.latimes.com/
• Los Angeles Times — Comprehensive trial coverage archives for both San Diego proceedings (1990 & 1991): https://www.latimes.com/archives/
• The New York Times — Socio-legal analyses on gender politics, divorce equity, and societal polarization.
• San Diego Magazine — Investigative features on the high-profile divorce proceedings and legal community tensions: https://www.sandiegomagazine.com/

4. Forensic Psychiatry, Behavioral Science & Victimology:
• Dr. Park Dietz, M.D., Ph.D. (Forensic Psychiatrist) — Expert psychological evaluation and courtroom testimony regarding Betty Broderick.
• American Psychiatric Association (APA) — Clinical frameworks regarding Gaslighting, Narcissistic Injury, Borderline Personality Dynamics, and Pathological Rage.
• Gavin de Becker — Seminal survival and intuitive risk assessment work 'The Gift of Fear' (Dell Publishing, 1997).

5. Crisis Support & Protective Hotlines:
• Child Protective Services / Crisis Response (Vietnam): Hotline 111 (24/7 Free) — http://tongdai111.vn/
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org/"""

SOURCES_JA = """📚 第14話 参考文献・公式調査資料一覧（ベティ・ブロデリック事件）
アンバーアイズ（Amber eyes）は、カリフォルニア州司法省の公式裁判記録および権威ある調査報道資料を厳格に照合しています。

1. カリフォルニア州公式裁判記録および司法判決文書:
• サンディエゴ郡上級裁判所（San Diego Superior Court）— 刑事裁判記録 People v. Elisabeth Anne Broderick (事件番号 CR113886, トーマス・J・ウィーラン裁判長): https://www.sdcourt.ca.gov/
• サンディエゴ地方検察局（San Diego District Attorney's Office）— ケリー・ウェルズ検事による起訴状および法廷証拠資料: https://www.danewstoday.com/
• カリフォルニア州第4控訴裁判所 — 有罪判決維持決定 (1994年, 控訴番号 D016254)。
• カリフォルニア州矯正リハビリテーション局（CDCR）— 2010年および2017年の仮釈放申請却下審問調書（囚人番号 W42477）: https://www.cdcr.ca.gov/

2. 警察実地捜査記録および法医学証拠:
• サンディエゴ市警察（SDPD）— 1989年11月5日 コーラル・リーフ・アベニュー1041番地 現場検証報告書および出頭記録: https://www.sandiego.gov/police
• SDPD 音声証拠アーカイブ — 1985年から1989年にかけて被告が残した数百件に及ぶ脅迫電話・留守番電話録音テープ資料。

3. 調査報道および専門文献:
• ベラ・スタンボ（ロサンゼルス・タイムズ調査報道記者）— 決定版ノンフィクション『Until the Twelfth of Never: The Deadly Divorce of Dan & Betty Broderick』 (Pocket Books, 1993年): https://www.latimes.com/
• ロサンゼルス・タイムズ紙 — サンディエゴを揺るがした2回の公判（1990年・1991年）の全報道アーカイブ: https://www.latimes.com/archives/
• ニューヨーク・タイムズ紙 — 離婚における経済的不公平と世論の極端な分極化に関する社会学的分析。
• サンディエゴ・マガジン — 地元法曹界の対立と巨額財産分与訴訟の舞台裏特集: https://www.sandiegomagazine.com/

4. 法精神医学、行動科学および被害者学:
• パーク・ディーツ博士（法精神医学者）— 法廷におけるベティ・ブロデリックの精神鑑定証言。
• アメリカ精神医学会（APA）— ガスライティング、自己愛性損傷、境界性パーソナリティ傾向および自己愛性憤激の臨床理論。
• ギャヴィン・ド・ベッカー — 直感の危機察知科学の名著『The Gift of Fear』（邦題：『暴力から逃れるための10のレッスン』）。

5. 危機支援・相談ホットライン:
• 全米DVホットライン（USA）: 1-800-799-SAFE (7233) — https://www.thehotline.org/
• 子ども保護ホットライン（ベトナム）: 111 (24時間無料)"""

SOURCES_KO = """📚 제14화 참고 문헌 및 공식 수사 기록 (베티 브로데릭 사건)
앰버 아이즈(Amber eyes)는 캘리포니아주 사법부의 공식 재판 기록과 권위 있는 탐사보도 자료를 엄격하게 교차 검증합니다.

1. 캘리포니아주 법원 공식 재판 기록 및 판결문:
• 샌디에이고 카운티 상급법원 (San Diego Superior Court) — 형사 재판 기록 People v. Elisabeth Anne Broderick (사건번호 CR113886, 토머스 J. 웰런 재판장): https://www.sdcourt.ca.gov/
• 샌디에이고 지방검찰청 (San Diego District Attorney's Office) — 케리 웰스 검사의 공소장 및 법정 증거 목록: https://www.danewstoday.com/
• 캘리포니아주 제4 항소법원 — 1994년 유죄 판결 유지 판결문 (항소번호 D016254).
• 캘리포니아 교정재활국 (CDCR) — 2010년 및 2017년 가석방 기각 심문 의결서 (수형번호 W42477): https://www.cdcr.ca.gov/

2. 경찰 수사 기록 및 현장 감식 자료:
• 샌디에이고 경찰국 (SDPD) — 1989년 11월 5일 코럴 리프 애비뉴 1041번지 사건 현장 감식 보고서 및 자수 기록: https://www.sandiego.gov/police
• SDPD 음성 증거 보존 기록 — 1985년부터 1989년까지 피고인이 남긴 수백 건의 협박 전화 및 자동응답기 녹음 테이프 내역.

3. 탐사보도 및 심층 논픽션:
• 벨라 스텀보 (로스앤젤레스 타임스 탐사전문기자) — 결정판 르포 서적 'Until the Twelfth of Never: The Deadly Divorce of Dan & Betty Broderick' (Pocket Books, 1993): https://www.latimes.com/
• 로스앤젤레스 타임스 (Los Angeles Times) — 샌디에이고를 뒤흔든 두 차례의 법정 공방(1990 & 1991) 아카이브: https://www.latimes.com/archives/
• 뉴욕 타임스 (The New York Times) — 이혼의 경제적 형평성과 사건을 둘러싼 여론 분열 심층 분석.
• 샌디에이고 매거진 (San Diego Magazine) — 백만장자 법조계 이혼 소송의 막전막후: https://www.sandiegomagazine.com/

4. 법정신신의학, 행동과학 및 피해자학:
• 파크 디츠 박사 (법정신의학 전문가) — 베티 브로데릭에 대한 독립적 정신 감정 및 법정 증언.
• 미국정신의학회 (APA) — 가스라이팅(현실왜곡공작), 자기애성 손상, 경계선 성격 성향 및 자기애성 분노의 임상 연구.
• 개빈 드 베커 — 위험 평가와 생존 본능의 고전 'The Gift of Fear' (생존의 선물).

5. 위기 상담 및 피해자 지원 핫라인:
• 미국 가정폭력 핫라인: 1-800-799-SAFE (7233) — https://www.thehotline.org/
• 아동보호 핫라인 (베트남): 111 (24시간 무료)"""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Tập 14: Khi Nạn Nhân Gaslighting Bước Qua Ranh Giới Tội Ác | Tâm lý học tội phạm: Betty Broderick & Bi Kịch Hôn Nhân Triệu Đô (Hệ Sinh Thái 10 Chỉ Dấu Tâm Lý) | Amber eyes

Rạng sáng 05/11/1989, tại khu phố thượng lưu Marston Hills thuộc San Diego, năm phát đạn khô khốc đã kết liễu sinh mệnh luật sư triệu phú Daniel Broderick cùng người vợ mới cưới Linda Kolkena. Thủ phạm là người vợ cũ từng dành trọn 16 năm hy sinh thanh xuân để vun đắp sự nghiệp cho chồng: Elisabeth Anne "Betty" Broderick. Vụ án trở thành một trong những bi kịch hôn nhân gây chia rẽ sâu sắc nhất lịch sử tư pháp nước Mỹ.

Hồ sơ Betty Broderick được Amber eyes giải phẫu toàn diện qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi:
1. DƯ CHẤN XÃ HỘI & SỰ PHÂN CỰC DƯ LUẬN: Gây chia rẽ dữ dội: phong trào phụ nữ đồng cảm với người vợ bị ruồng bỏ sau 16 năm hy sinh vs giới tư pháp lên án bạo lực ái kỷ có toan tính; thúc đẩy cải cách luật ly hôn và quy trình can thiệp bạo lực gia đình.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem Dan và Linda là kẻ cướp đoạt 20 năm thanh xuân và danh vị thượng lưu; khuyết tật thấu cảm phát sinh từ tổn thương ái kỷ biến nỗi đau hôn nhân thành sự thù hận hủy diệt.
3. NGHỊCH LÝ CHIA NGĂN (COMPARTMENTALIZATION): Khóa chặt hai ngăn: "người mẹ hy sinh" vs "dùng con cái làm vũ khí trả thù"; bi kịch của Kim Broderick khi biết mẹ trộm chìa khóa trong túi xách của mình để ra tay.
4. TỰ THƯƠNG HẠI BỆNH LÝ TRƯỚC BẢN ÁN (PATHOLOGICAL SELF-PITY): Suốt phiên tòa và 3 thập kỷ thụ án, Betty không hề khóc thương cho hai nạn nhân, chỉ than khóc cho danh dự cá nhân; hội đồng ân xá 2010 và 2017 bác đơn vì thiếu sự ăn năn chân chính.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC (NEUTRALIZATION): Đổ lỗi cho nạn nhân và tự phong mình là hiện thân của sự công bằng bị lạm dụng quyền lực chà đạp để vô hiệu hóa tiếng nói lương tri trước khi nổ súng.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY (TIPPING POINT): Tòa cưỡng chế bán biệt thự La Jolla sau lưng Betty; đám cưới xa hoa của Dan & Linda kèm vệ sĩ có vũ trang; trát tòa phạt tiền và đe dọa tống giam vì vi phạm lệnh cấm.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO (mua súng .38, trộm chìa khóa con gái, đột nhập lúc 5:30 sáng); Signature bất biến là hành vi giật đứt phựt dây điện thoại đầu giường khi Dan thoi thóp nhằm triệt tiêu cứu viện và thỏa mãn quyền lực tuyệt đối.
8. QUỸ ĐẠO LEO THANG HÀNH VI: Chu kỳ dung nạp kích thích: gọi điện chửi bới đêm khuya -> đột nhập xịt sơn & bôi bánh kem cưới lên giường -> lái xe bán tải đâm sập cửa trước -> mua súng và nổ súng đoạt mạng.
9. HIỆU ƯNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI (HALO EFFECT): Vỏ bọc Chủ tịch Đoàn Luật sư của Dan tạo tấm khiên thể chế khiến giới luật sư từ chối bảo vệ Betty; vỏ bọc phu nhân thượng lưu khiến bạn bè bỏ qua các dấu hiệu tâm lý lệch lạc cực đoan.
10. NẠN NHÂN HỌC & CẢNH BÁO ĐỎ SINH TỒN: Phân định rạch ròi giữa nỗi đau bị Gaslighting với trách nhiệm hình sự; đúc kết bài học từ 'The Gift of Fear' (Gavin de Becker): nhận diện vi tín hiệu thao túng, tỉnh táo trước hào quang xã hội và nghệ thuật buông bỏ thù hận để tự giải thoát.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Người vợ hy sinh và chiếc bẫy thao túng thực tại
05:45 Hồi 2 · Cuộc chiến pháp lý tàn khốc và sự đứt gãy tâm lý
11:30 Hồi 3 · Giải mã tâm lý: Gaslighting, tổn thương ái kỷ & bẫy nạn nhân
17:15 Hồi 4 · Năm phát đạn rạng sáng và phiên tòa chia rẽ nước Mỹ
23:00 Hồi 5 · Bài học đắt giá về rủi ro hôn nhân & Lời cảnh tỉnh

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai của Tòa Thượng thẩm Hạt San Diego và Sở Cảnh sát San Diego (SDPD). Kênh không tôn vinh hay bôi nhọ bất kỳ cá nhân nào.
• Hình tượng Cú, Sói, Cáo, Cừu, Mèo là linh thú nghệ thuật. Giọng đọc, hình ảnh và âm thanh có ứng dụng công nghệ AI.

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• Phán quyết Tòa Thượng thẩm San Diego: People v. Elisabeth Anne Broderick (Case No. CR113886) — https://www.sdcourt.ca.gov/
• Tác phẩm điều tra: 'Until the Twelfth of Never' của Bella Stumbo (1993)
• Giám định tâm thần pháp y: Dr. Park Dietz & Nghiên cứu của APA về Gaslighting & Narcissistic Rage.
• Khoa học hành vi sinh tồn: 'The Gift of Fear' của Gavin de Becker (1997).

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng Phòng chống Bạo lực Gia đình (Việt Nam): 1900 969 680

#AmberEyes #TrueCrime #TamLyToiPham #BettyBroderick #Gaslighting #DeadlyDivorce #NarcissisticInjury #NarcissisticRage #10ChiDauTamLy #TheGiftOfFear #SanDiegoCase"""

DESC_EN = """Ep. 14: When a Gaslighting Victim Crosses the Line | Criminal Psychology: Betty Broderick & The Deadly Divorce (10 Psychological Markers) | Amber eyes

At dawn on November 5, 1989, in the affluent enclave of Marston Hills in San Diego, five fatal gunshots pierced the morning fog, ending the lives of prominent medical malpractice attorney Daniel Broderick and his newly wedded wife Linda Kolkena. The shooter was Daniel's former spouse who had spent 16 years sacrificing her youth to build his fortune: Elisabeth Anne "Betty" Broderick. The case became one of the most polarizing domestic tragedies in American judicial history.

Amber eyes dissects the Betty Broderick dossier through the 10 Psychological & Behavioral Indicators:
1. SOCIAL IMPACT & SOCIETAL POLARIZATION: Fiercely split public opinion: women's advocates sympathized with a wife discarded after 16 years of labor vs. the legal system condemning calculated narcissistic violence; accelerated divorce financial reforms.
2. DEHUMANIZATION & OBJECTIFICATION: Betty perceived Dan and Linda not as sentient humans, but as thieves usurping two decades of her sweat and social status; affective empathy deficit from profound narcissistic injury transformed grief into lethal wrath.
3. COGNITIVE COMPARTMENTALIZATION: Maintained two conflicting mental chambers: the "noble sacrificing mother" vs. weaponizing children to punish her ex-husband; the tragedy of daughter Kim testifying against her mother after realizing her key had been stolen.
4. PATHOLOGICAL SELF-PITY BEFORE THE BENCH: Throughout the trials and 30 years of incarceration, Betty shed no authentic tears for the victims, weeping solely for her lost prestige; led parole boards in 2010 and 2017 to deny release due to absence of remorse.
5. MORAL NEUTRALIZATION: Deployed victim-blaming techniques, framing herself as the ultimate martyr of judicial corruption to systematically silence her conscience before pulling the trigger.
6. THE PSYCHOLOGICAL TRIGGER & FATAL BREAKING POINT: The court-ordered forced sale of the La Jolla family home without Betty's signature; Dan and Linda's lavish wedding guarded by armed security; escalating court fines and threats of jail.
7. PSYCHOLOGICAL SIGNATURE VS. OPERATIONAL MO: Tactical MO (buying a .38 revolver, stealing daughter's key, dawn entry) secured execution; the invariable psychological Signature was yanking the bedside telephone cord from the wall as Dan gasped for life to guarantee total control.
8. BEHAVIORAL ESCALATION TRAJECTORY: Tolerance buildup: obscene late-night answering machine tirades -> spray-painting walls & smearing wedding cake on the bed -> crashing her truck into Dan's front door -> purchasing a gun and executing the fatal shooting.
9. THE HALO EFFECT & COLLECTIVE BLINDSPOTS: Dan's stature as Bar Association President created an institutional shield preventing local attorneys from defending Betty; Betty's high-society matron facade led friends to dismiss early extreme behavioral abnormalities.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Delineating genuine victimhood from criminal responsibility; core survival lessons from Gavin de Becker's 'The Gift of Fear': identifying subtle boundary testing, resisting social status illusions, and liberating one's soul through letting go of toxic grievance.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Advisory
00:23 Act 1 · The Sacrificing Wife and the Gaslighting Trap
05:45 Act 2 · The Brutal Legal War and Psychological Rupture
11:30 Act 3 · Psychological Dissection: Gaslighting, Narcissistic Injury & The Victim Trap
17:15 Act 4 · Five Dawn Shots and the Trial That Split America
23:00 Act 5 · Crucial Lessons in Marital Risk & The Survival Awakening

⚠️ LEGAL & SAFETY ADVISORY
• Educational documentary analyzing criminal psychology; does not substitute professional medical or legal counsel.
• Based on public records of the San Diego County Superior Court and San Diego Police Department. Does not glorify crime.
• Animal avatars are artistic storytellers. Narration, visuals, and audio utilize AI production tools.

📚 OFFICIAL SOURCES
• San Diego Superior Court: People v. Elisabeth Anne Broderick (Case No. CR113886) — https://www.sdcourt.ca.gov/
• Bella Stumbo: 'Until the Twelfth of Never: The Deadly Divorce of Dan & Betty Broderick' (1993)
• Forensic Psychiatric Evaluation by Dr. Park Dietz & APA Research on Gaslighting & Narcissistic Rage.
• Behavioral Science & Threat Assessment: Gavin de Becker's 'The Gift of Fear' (1997).

🆘 CRISIS HOTLINES
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org/
• Child Protection Hotline (Vietnam): 111 (24/7 Free)

#AmberEyes #TrueCrime #CriminalPsychology #BettyBroderick #Gaslighting #DeadlyDivorce #NarcissisticInjury #NarcissisticRage #10PsychologicalMarkers #TheGiftOfFear #CaseFile"""

DESC_JA = """第14話: ガスライティング被害者が一線を越えたとき | 犯罪心理学: ベティ・ブロデリック事件（10の心理的指標エコシステム） | Amber eyes

1989年11月5日の未明、サンディエゴの高級住宅街マーストン・ヒルズで鳴り響いた5発の乾いた銃声が、富豪弁護士ダニエル・ブロデリックと再婚相手リンダ・コルケナの命を奪いました。引き金を引いたのは、夫の立身出世のために16年間の青春と労働を捧げ尽くした元妻、エリザベス・アン・“ベティ”・ブロデリックでした。この事件は、アメリカ司法史において最も世論を二分した泥沼離婚の家庭内惨劇となりました。

アンバーアイズが解剖するベティ・ブロデリック事件の「10の心理的指標」:
1. 社会的余波と世論の極端な分極化: 16年の献身を裏切られた妻に同情する女性権利擁護派 vs 計画的で自己愛的な暴力を断罪する法曹界が激しく激突。カリフォルニア州の離婚法改正および家庭内暴力介入基準の厳罰化を促した。
2. 被害者の非人間化（DEHUMANIZATION）: 元夫と後妻を生きている人間としてではなく、自身の20年間の犠牲と社会的威信を強奪した略奪者とみなす。自己愛性損傷に起因する情緒的共感の麻痺が破壊的復讐心へと転化した。
3. 認知的区画化のパラドックス: 「家庭を守る高潔な母」と「元夫を処罰するために子どもを心理的武器として利用する加害者」という矛盾する二面性を両立。長女キムが法廷で母に不利な証言を迫られた悲劇。
4. 病的自己憐憫（PATHOLOGICAL SELF-PITY）: 公判中も30年以上の服役中も、犠牲者への真の悔悟の涙を一切流さず、自身の不遇な運命のみを嘆き続けた。真摯な反省の欠如により2010年と2017年の仮釈放審問は満場一致で却下された。
5. 道徳的中和技術と責任転嫁: 自分は冷酷な司法制度の最大の犠牲者であるという被害者意識を盾に、凶行の直前まで良心の声を沈黙させた。
6. 心理的引き金と決定的一線: ベティの署名なしで行われたラ・ホヤ旧居の強制売却決定、武装警備員を配置した元夫らの豪華結婚式、度重なる接近禁止命令違反の罰金通知が最後の臨界点を突破させた。
7. 心理的署名 vs. 犯行手口: 手口（38口径拳銃の購入、娘の鍵の盗難、未明の侵入）の裏にある不変の署名。瀕死のダニエルが助けを呼ぼうとした瞬間、ベッド脇の電話線を力任せに引きちぎり、絶対的支配欲を満たした行動。
8. 破壊的エスカレーションの軌道: 深夜の留守番電話への罵詈雑言 -> 旧居への不法侵入と壁へのスプレー塗料噴射 -> トラックによる新居玄関への突入事故 -> 凶器の調達と致命的銃撃へ至る行動の暴走。
9. ハロー効果と社会的盲点: 元弁護士会長としてのダニエルの威光が地元弁護士の受任を拒絶させ、ベティの上流婦人としての外面も周囲が極端な危険信号を見過ごす原因となった。
10. 被害者学と生存のための危険信号: ガスライティング被害の苦痛と刑事責任の峻別。名著『The Gift of Fear』（ギャヴィン・ド・ベッカー）が示す実践的教訓: 初期境界侵犯の見極め、社会的地位の幻想の排除、そして怨恨を手放し魂を解放する生き方。

⏱ チャプター
00:00 イントロ＆注意事項
00:23 第1幕: 献身的な妻とガスライティングの心理的罠
05:45 第2幕: 容赦なき法廷闘争と心理的破綻の連鎖
11:30 第3幕: 心理構造の解剖：ガスライティング、自己愛性損傷、そして被害者の罠
17:15 第4幕: 未明を切り裂く五発の銃声と国を二分した裁判
23:00 第5幕: 婚姻関係の破綻リスクに関する教訓と生存への警鐘

⚠️ 法的案内
• 犯罪心理学および歴史的記録に基づく教育用コンテンツです。
• サンディエゴ郡上級裁判所および警察の公開記録に基づき制作されています。

📚 参考文献
• サンディエゴ郡上級裁判所: People v. Elisabeth Anne Broderick (CR113886)
• ベラ・スタンボ: 『Until the Twelfth of Never: The Deadly Divorce of Dan & Betty Broderick』 (1993)
• パーク・ディーツ博士による法精神医学鑑定報告書
• ギャヴィン・ド・ベッカー: 『The Gift of Fear』 (1997)

#AmberEyes #犯罪心理学 #ベティブロデリック #ガスライティング #泥沼離婚 #自己愛性損傷 #自己愛性憤激 #10の心理的指標 #実録犯罪"""

DESC_KO = """제14화: 가스라이팅 피해자가 선을 넘었을 때 | 범죄심리학: 베티 브로데릭 사건 (10대 핵심 심리 지표 및 샌디에이고 비극) | Amber eyes

1989년 11월 5일 새벽, 샌디에이고 고급 주택가 마스턴 힐스에서 울려 퍼진 다섯 발의 총성이 저명한 의료 과오 전문 변호사 대니얼 브로데릭과 그의 젊은 재혼 아내 린다 콜케나의 목숨을 앗아갔습니다. 방아쇠를 당긴 이는 남편의 성공을 위해 16년간 청춘과 노동을 온전히 바쳤던 전처 엘리자베스 앤 "베티" 브로데릭이었습니다. 이 사건은 미국 사법 역사상 대중을 가장 극렬하게 분열시킨 가정 참극이 되었습니다.

앰버 아이즈가 분석하는 베티 브로데릭 사건의 10대 심리적 지표:
1. 사회적 여파와 여론의 극단적 분열: 16년의 헌신을 배신당한 아내를 지지하는 여성 권익 운동 vs 계획적 자기애성 폭력을 단죄하는 사법 당국의 극렬한 대립; 이혼 재산 분할 제도 및 가정폭력 사법 개혁 촉발.
2. 피해자의 비인간화 및 대상화: 남편과 후처를 존엄한 인간이 아닌, 자신의 20년 희생과 사교계 위상을 강탈한 약탈자로 규정; 자기애성 손상에서 비롯된 정서적 공감 결여가 치명적 복수심으로 변질.
3. 인지적 구획화의 역설: "가정을 지키려는 숭고한 어머니"와 "자녀를 복수의 도구로 무기화하는 가해자"라는 모순된 인격을 분리 유지; 어머니가 자신의 가방에서 열쇠를 훔쳐 범행을 저질렀음을 알게 된 큰딸 킴 브로데릭의 법정 증언 비극.
4. 병적 자기연민과 참회의 결여: 재판과 30년 복역 기간 내내 피해자를 위한 참회의 눈물 대신 자신의 무너진 명예와 불우한 처지만을 비탄; 진정한 뉘우침의 부재로 2010년 및 2017년 가석방 만장일치 기각.
5. 도덕적 중화 기술과 피해자성 악용: 부패한 사법 권력의 궁극적 피해자라는 논리를 방패 삼아 살해 직전까지 양심의 가책을 완벽하게 무력화.
6. 심리적 방아쇠와 치명적 임계점: 베티의 동의 없는 라호야 저택 강제 매각 결정, 무장 경호원을 대동한 화려한 재혼식, 잇따른 접근금지 위반 벌금 통지가 파멸의 도화선에 점화.
7. 심리적 시그니처 vs. 범행 수법(MO): 수법(.38구경 권총 구매, 열쇠 절도, 새벽 침입) 이면에 존재하는 시그니처. 죽어가는 남편이 구조를 요청하려 하자 침대 곁 전화선을 힘껏 쥐어뜯어 버린 절대적 지배 욕구.
8. 행동적 격화의 궤적: 심야 폭언 전화 테러 -> 전남편 저택 벽 페인트 낙서 및 침대 웨딩케이크 훼손 -> 픽업트럭 돌진 사고 -> 권총 구매와 치명적 사격으로 치달은 파멸의 단계.
9. 후광 효과와 제도적 맹점: 전임 변호사협회장이라는 남편의 지위가 지역 법조계를 장악해 아내의 변호를 가로막았고, 상류층 마담이라는 아내의 겉모습 역시 주변인들이 극단적 위험 신호를 간과하게 만듦.
10. 피해자학과 생존을 위한 적색경보: 가스라이팅 피해의 고통과 형사 책임의 명확한 구분; 개빈 드 베커의 명저 'The Gift of Fear'의 핵심 교훈: 조기 경계 침범 식별, 지위의 환상 경계, 그리고 원한을 내려놓고 자아를 해방하는 생존 철학.

⏱ 타임스탬프
00:00 인트로 & 법적 고지
00:23 제1막: 헌신적인 아내와 가스라이팅의 덫
05:45 제2막: 잔혹한 법정 전쟁과 심리적 파탄의 연쇄
11:30 제3막: 심리 구조의 해부: 가스라이팅, 자기애성 손상, 그리고 피해자의 덫
17:15 제4막: 새벽을 가른 다섯 발의 총성과 미국을 분열시킨 재판
23:00 제5막: 혼인 파탄 위험에 관한 교훈과 생존의 각성

⚠️ 법적 고지
• 범죄심리학 및 역사적 기록에 기반한 교육용 다큐멘터리 콘텐츠입니다.
• 샌디에이고 카운티 상급법원 및 경찰국의 공식 공개 기록을 바탕으로 제작되었습니다.

📚 참고 자료
• 샌디에이고 카운티 상급법원: People v. Elisabeth Anne Broderick (CR113886)
• 벨라 스텀보: 'Until the Twelfth of Never: The Deadly Divorce of Dan & Betty Broderick' (1993)
• 파크 디츠 박사의 법정신신의학 감정 보고서
• 개빈 드 베커: 'The Gift of Fear' (1997)

#AmberEyes #범죄심리학 #베티브로데릭 #가스라이팅 #이혼비극 #자기애성손상 #자기애성분노 #10대심리지표 #실제사건"""

def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    clean_content = content.strip().replace("\r\n", "\n")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(clean_content + "\n")

def main():
    print("=== ĐO LƯỜNG ĐỘ DÀI MÔ TẢ TẬP 14 (TRẦN: 5000 KÝ TỰ) ===")
    descs = [
        ("VI", DESC_VI),
        ("EN", DESC_EN),
        ("JA", DESC_JA),
        ("KO", DESC_KO),
    ]
    
    all_valid = True
    for lang, text in descs:
        char_len = len(text.strip())
        lines = len(text.strip().splitlines())
        status = "PASS (<= 5000)" if char_len <= 5000 else "FAIL (> 5000)"
        if char_len > 5000:
            all_valid = False
        print(f"[{lang}] Độ dài: {char_len:,} ký tự | {lines} dòng | Trạng thái: {status}")
    
    if not all_valid:
        print("\n>>> LỖI: Có bản mô tả vượt quá 5000 ký tự! Dừng ghi file. <<<")
        sys.exit(1)
        
    print("\n=== TIẾN HÀNH XUẤT BẢN FILE MÔ TẢ & NGUỒN TẬP 14 ===")
    
    files_to_write = [
        # Tiếng Việt
        (ROOT / "02_SAN_XUAT" / "Tap14" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap14" / "xuat_ban" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap14" / "nguon_mo_ta.txt", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap14" / "nguon_tham_khao.md", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap14" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),
        
        # Tiếng Anh
        (ROOT / "02_SAN_XUAT" / "Tap14_EN" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap14_EN" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap14_EN" / "xuat_ban" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap14_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap14_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap14_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap14_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),
        
        # Tiếng Nhật
        (ROOT / "02_SAN_XUAT" / "Tap14_JA" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap14_JA" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap14_JA" / "xuat_ban" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap14_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap14_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap14_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap14_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),
        
        # Tiếng Hàn
        (ROOT / "02_SAN_XUAT" / "Tap14_KO" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap14_KO" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap14_KO" / "xuat_ban" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap14_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap14_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap14_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap14_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
    ]
    
    for path, content in files_to_write:
        write_text(path, content)
        print(f"  -> Đã ghi: {path.relative_to(ROOT)} ({len(content.strip()):,} ký tự)")
        
    print("\n>>> TẤT CẢ FILE MÔ TẢ TẬP 14 ĐÃ ĐƯỢC CẬP NHẬT HOÀN TẤT VÀ ĐẠT CHUẨN! <<<")


if __name__ == "__main__":
    main()
