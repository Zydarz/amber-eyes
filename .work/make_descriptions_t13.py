#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo các file mô tả và nguồn tham khảo cho Tập 13 trên 4 ngôn ngữ (VN, EN, JA, KO).
Đảm bảo đầy đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c, K10) và TUYỆT ĐỐI <= 5000 ký tự.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO CHO TẬP 13
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 13 (HỒ SƠ JENNIFER PAN)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp chính thức của Canada và báo chí điều tra:

1. Hồ sơ Tòa án & Phán quyết tư pháp Canada:
• Tòa Thượng thẩm Ontario (Ontario Superior Court of Justice) — Bản án xét xử R. v. Pan et al. (2014 ONSC, Thẩm phán Cary Boswell): https://www.canlii.org/
• Tòa Phúc thẩm Ontario (Court of Appeal for Ontario) — Phán quyết phúc thẩm năm 2023 (2023 ONCA 362): https://www.ontariocourts.ca/coa/
• Tòa án Tối cao Canada (Supreme Court of Canada) — Hồ sơ kháng cáo liên quan: https://www.scc-csc.ca/

2. Hồ sơ Điều tra & Cơ quan Cảnh sát:
• Cảnh sát Khu vực York (York Regional Police - YRP) — Băng ghi âm cuộc gọi 911 và video thẩm vấn nghi phạm Jennifer Pan của Thám tử William "Bill" Goetz: https://www.yrp.ca/
• Biên bản giám định kỹ thuật số viễn thông trích xuất dữ liệu điện thoại giữa Jennifer Pan và Daniel Wong.

3. Báo chí Điều tra & Phóng sự chuyên sâu:
• Karen K. Ho (Ký giả điều tra, bạn học cũ) — Phóng sự chuyên sâu 'Jennifer Pan's Revenge' trên tạp chí Toronto Life (2015): https://torontolife.com/city/crime/jennifer-pan-revenge/
• The Globe and Mail — Dòng thời gian vụ án mạng tại Markham và bi kịch gia đình nhập cư: https://www.theglobeandmail.com/
• CBC News — Diễn biến phiên tòa kéo dài 10 tháng và các phán quyết tư pháp: https://www.cbc.ca/news/

4. Tâm lý học Gia đình & Khoa học Hành vi:
• Amy Chua — Khái niệm Kỷ luật Cha mẹ Hổ (Tiger Parenting) và áp lực thành tích học đường cực đoan.
• Phân tích Tâm lý học Hành vi — Hội chứng Nói dối bệnh lý (Mythomania / Pathological Lying), Cơ chế Chia ngăn nhận thức (Cognitive Compartmentalization) và Bẫy chi phí chìm (Sunk Cost Fallacy).

5. Đường dây nóng hỗ trợ & bảo vệ:
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng hỗ trợ phụ nữ bị bạo lực: 1900 969 680"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 13 (JENNIFER PAN)
Amber eyes adheres to multi-source cross-verification from official Canadian judicial records and investigative journalism:

1. Canadian Judicial Records & Court Rulings:
• Ontario Superior Court of Justice — Criminal Trial Ruling R. v. Pan et al. (2014 ONSC, Justice Cary Boswell): https://www.canlii.org/
• Court of Appeal for Ontario — Appellate Court Ruling (2023 ONCA 362): https://www.ontariocourts.ca/coa/
• Supreme Court of Canada — Appellate proceedings and rulings: https://www.scc-csc.ca/

2. Law Enforcement & Police Interrogation Archives:
• York Regional Police (YRP) — 911 Emergency Audio Recording & Forensic Video Interrogation of Jennifer Pan by Detective William Goetz: https://www.yrp.ca/
• Telecommunications Forensic Extraction Reports — Thousands of text messages between Jennifer Pan and Daniel Wong.

3. Investigative Journalism & In-depth Reporting:
• Karen K. Ho (Investigative Journalist & Former High School Classmate) — 'Jennifer Pan's Revenge' published in Toronto Life (2015): https://torontolife.com/city/crime/jennifer-pan-revenge/
• The Globe and Mail — Chronology of the Markham Home Invasion and immigrant family dynamics: https://www.theglobeandmail.com/
• CBC News — Comprehensive coverage of the 10-month murder trial and judicial verdicts: https://www.cbc.ca/news/

4. Behavioral Psychology & Familial Dynamics:
• Tiger Parenting Model — Analysis of authoritarian parental discipline, conditional love, and achievement pressure.
• Clinical Behavioral Analysis — Pathological Lying (Mythomania / Pseudologia Fantastica), Cognitive Compartmentalization, and the Sunk Cost Trap.

5. Support & Crisis Hotlines:
• Child Protective Services / Crisis Response (Vietnam): Hotline 111 (24/7 Free)
• Mental Health Support Hotline: 096 306 1414"""

SOURCES_JA = """📚 第13話 参考文献・公式調査資料一覧（ジェニファー・パン事件）
アンバーアイズ（Amber eyes）は、カナダ司法省の公式裁判記録および調査報道資料を厳格に照合しています。

1. カナダ公式裁判記録・判決文書:
• オンタリオ州高等裁判所（Ontario Superior Court of Justice）— 第一審判決 R. v. Pan et al. (2014 ONSC, ケイリー・ボズウェル裁判長): https://www.canlii.org/
• オンタリオ州控訴裁判所（Court of Appeal for Ontario）— 控訴審判決 (2023 ONCA 362): https://www.ontariocourts.ca/coa/
• カナダ最高裁判所（Supreme Court of Canada）— 上告審記録: https://www.scc-csc.ca/

2. 警察捜査記録および尋問アーカイブ:
• ヨーク地域警察（York Regional Police - YRP）— 911緊急通報録音音声およびウィリアム・ゲーツ刑事による尋問映像: https://www.yrp.ca/
• デジタル通信フォレンジック解析報告書 — 被告間の数千件に及ぶテキストメッセージ記録。

3. 調査報道および専門文献:
• カレン・K・ホー（調査報道記者、高校時代の同級生）— 専門ルポ『ジェニファー・パンの復讐』（Toronto Life 誌、2015年）: https://torontolife.com/city/crime/jennifer-pan-revenge/
• グローブ・アンド・メール紙（The Globe and Mail）— マーカム事件の時系列記録と移民家庭の深層分析: https://www.theglobeandmail.com/
• CBCニュース — 10ヶ月に及ぶ公判記録と司法判決報道: https://www.cbc.ca/news/

4. 犯罪心理学および家族行動科学:
• タイガー・ペアレンティング（過干渉・条件付きの愛）の心理的影響分析。
• 空想虚言症（病的虚言癖）、認知的区画化（二重生活の維持）、および埋没費用の罠に関する臨床考察。"""

SOURCES_KO = """📚 제13화 참고 문헌 및 공식 수사 기록 (제니퍼 판 사건)
앰버 아이즈(Amber eyes)는 캐나다 사법부의 공식 재판 기록과 권위 있는 탐사보도 자료를 교차 검증합니다.

1. 캐나다 법원 공식 재판 기록 및 판결문:
• 온타리오주 고등법원 (Ontario Superior Court of Justice) — 1심 판결 R. v. Pan et al. (2014 ONSC, 캐리 보스웰 재판장): https://www.canlii.org/
• 온타리오주 항소법원 (Court of Appeal for Ontario) — 항소심 판결 (2023 ONCA 362): https://www.ontariocourts.ca/coa/
• 캐나다 연방대법원 (Supreme Court of Canada) — 상고심 관련 사법 기록: https://www.scc-csc.ca/

2. 경찰 수사 기록 및 심문 자료:
• 요크 지역 경찰청 (York Regional Police - YRP) — 911 긴급 신고 통화 녹음 및 윌리엄 게츠 형사의 피의자 심문 녹화 영상: https://www.yrp.ca/
• 디지털 포렌식 통신 분석 보고서 — 피고인들 간의 수천 건의 문자메시지 복원 내역.

3. 탐사보도 및 심층 기사:
• 카렌 K. 호 (탐사보도 기자, 고등학교 동창) — 토론토 라이프 심층 르포 '제니퍼 판의 복수' (Toronto Life, 2015): https://torontolife.com/city/crime/jennifer-pan-revenge/
• 글로브 앤드 메일 (The Globe and Mail) — 마컴 주택 침입 사건 타임라인과 이민자 가정의 비극 분석: https://www.theglobeandmail.com/
• CBC 뉴스 — 10개월간의 법정 공방 및 배심원 평결 심층 보도: https://www.cbc.ca/news/

4. 가족 심리학 및 범죄 행동과학:
• 타이거 패런팅 (극단적 훈육과 조건부 애정)의 파괴적 영향 분석.
• 병적 허언증 (공상허언증), 인지적 구획화 (이중생활 유지 기제) 및 매몰비용의 함정 연구."""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Tập 13: Vỏ Bọc 'Con Nhà Người Ta' & Lời Nói Dối 10 Năm | Tâm lý học tội phạm: Jennifer Pan & Vụ Án Markham (Hệ Sinh Thái 10 Chỉ Dấu Tâm Lý) | Amber eyes

Đêm 08/11/2010, tại Markham, Ontario, Canada, vụ nổ súng kinh hoàng tại căn nhà số 238 Đại lộ Helen đã phơi bày bi kịch gia đình chấn động toàn cầu. Đằng sau vỏ bọc "con nhà người ta" ngoan ngoãn và tài năng, cô con gái cưng Jennifer Pan đã che giấu một tòa tháp dối trá suốt gần 10 năm và lập mưu tước đoạt mạng sống của chính đấng sinh thành.

Hồ sơ Jennifer Pan được Amber eyes giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi:
1. DƯ CHẤN XÃ HỘI & SỰ RẠN NỨT HUYỀN THOẠI: Làm rung chuyển cộng đồng gốc Á tại Bắc Mỹ; châm ngòi tranh luận toàn cầu về mặt trái tàn khốc của phương pháp giáo dục độc đoán "Tiger Parenting" và áp lực thành tích cực đoan.
2. PHI NHÂN HÓA NẠN NHÂN (DEHUMANIZATION): Giáng cấp cha mẹ thành "cai ngục" và "chướng ngại vật" cản trở tự do; xem cha mẹ là công cụ tài chính để chiếm đoạt tài sản thừa kế và bảo hiểm ~500.000 CAD; sự thiếu hụt thấu cảm tột cùng khi đứng nghe tiếng súng mà không hề can ngăn.
3. NGHỊCH LÝ CHIA NGĂN (COMPARTMENTALIZATION): Vận hành hai thế giới độc lập suốt 10 năm: ban ngày là sinh viên gương mẫu đàn piano, ban đêm làm giả giấy tờ và đồng lõa với giang hồ; bi kịch người cha sống sót hồi tỉnh sau hôn mê đối diện sự thật con gái mở cửa cho kẻ thủ ác.
4. THAO TÚNG ÁI KỶ TRƯỚC BẢN ÁN (PERPETUAL VICTIMHOOD): Đóng vai nạn nhân vô tội, liên tục rơi nước mắt tìm sự thương cảm; lạnh lùng đón nhận án chung thân không ân xá trong 25 năm; kháng cáo phúc thẩm năm 2023 nhằm né tránh trách nhiệm đạo đức cao nhất.
5. HỆ THỐNG TỰ BÀO CHỮA & GIẢM TRỪ TỘI LỖI (MINIMIZATION): Khi bị dồn vào chân tường, Jennifer bịa chuyện thuê người để kết thúc mạng sống chính mình vì bế tắc; đổ lỗi ngược cho sự hà khắc của cha mẹ đã đẩy cô vào bước đường cùng.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY (TIPPING POINT): Ngòi nổ ban đầu là trượt môn Giải tích lớp 12 và chấn thương đầu gối mất cơ hội Olympic; Điểm gãy bùng phát mùa xuân 2010 khi cha phát hiện toàn bộ bằng cấp là giả, tịch thu điện thoại, giam lỏng tại gia và ép chia tay bạn trai.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO (mở chốt cửa từ bên trong, dàn dựng cướp nhà ngẫu nhiên, thuê sát thủ) thay đổi; Signature bất biến là nhu cầu ái kỷ muốn thành "nạn nhân vô tội đáng thương nhất": cố tình buộc lỏng tay vào lan can để bấm 911 diễn kịch la hét tạo chứng cứ ngoại phạm.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG (SUNK COST TRAP): Bẫy chi phí chìm: Làm giả học bạ cấp ba -> giả trúng tuyển Ryerson -> bịa chuyện học Dược ĐH Toronto -> làm giả bằng tốt nghiệp -> bịa việc làm SickKids -> thuê người thanh trừng cha mẹ để bảo vệ mặt nạ danh dự.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI (HALO EFFECT): Vỏ bọc "Nữ sinh tài năng, gia đình kiểu mẫu" (giải trượt băng, piano, lễ phép) tạo tấm khiên tàng hình; cha mẹ vì quá tự hào nên mắc thành kiến bình thường hóa (Normalcy Bias), bỏ qua vô số sơ hở suốt nhiều năm.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ SINH TỒN: Tôn vinh sự hy sinh cần cù của cha mẹ; đúc kết 4 cảnh báo đỏ nhận diện rạn nứt gia đình: (1) Tình yêu có điều kiện; (2) Chiếc mạng nhện dối trá leo thang; (3) Kiểm soát toàn diện triệt tiêu tự quyết; (4) Đứt gãy giao tiếp & sự im lặng độc hại.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Vỏ bọc 'Con nhà người ta' và tòa tháp dối lừa mười năm
06:10 Hồi 2 · Đêm kinh hoàng tại đại lộ Helen và cuộc gọi 911
12:00 Hồi 3 · Giải mã tâm lý: Từ 'Cha mẹ hổ' đến hội chứng nói dối bệnh lý
18:15 Hồi 4 · Đấu trí phòng thẩm vấn & Sự thức tỉnh của người cha
24:20 Hồi 5 · Bản án lương tâm & Lời cảnh tỉnh

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai của Tòa Thượng thẩm Ontario (R. v. Pan) và Cảnh sát Khu vực York. Kênh không tôn vinh hay bôi nhọ bất kỳ cá nhân nào.
• Hình tượng Cú, Sói, Cáo, Cừu, Mèo là linh thú nghệ thuật. Giọng đọc, hình ảnh và âm thanh có ứng dụng công nghệ AI.

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• Phán quyết Tòa Thượng thẩm Ontario: R. v. Pan et al. (2014 ONSC) — https://www.canlii.org/
• Phán quyết Tòa Phúc thẩm Ontario: 2023 ONCA 362 — https://www.ontariocourts.ca/coa/
• Băng ghi âm 911 & video thẩm vấn của Cảnh sát Khu vực York (YRP) — https://www.yrp.ca/
• Phóng sự chuyên sâu 'Jennifer Pan's Revenge' của Karen K. Ho (Toronto Life, 2015)
• Khái niệm Kỷ luật Cha mẹ Hổ (Amy Chua) & Phân tích Tâm lý học Hành vi.

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ & BẢO VỆ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng hỗ trợ phụ nữ bị bạo lực: 1900 969 680

#AmberEyes #TrueCrime #TamLyToiPham #JenniferPan #TigerParenting #MarkhamCase #PathologicalLying #Mythomania #10ChiDauTamLy #CanhBaoDo #HoSoToiPham"""

DESC_EN = """Ep. 13: The Golden Child Facade & A 10-Year Web of Lies | Criminal Psychology: Jennifer Pan & The Markham Case (10 Psychological Markers) | Amber eyes

In Markham, Ontario, Canada, the family of Huei Hann Pan and Bich Ha Pan was revered as an immigrant success story. But on the night of November 8, 2010, fatal gunfire inside 238 Helen Avenue shattered that illusion, revealing a devastating family tragedy. Behind her facade as an obedient, talented daughter, Jennifer Pan had concealed a decade-long tower of deceit, culminating in a cold-blooded conspiracy against her own parents.

Amber eyes dissects the Jennifer Pan dossier through the 10 Psychological & Behavioral Markers:
1. SOCIAL TRAUMA & MODEL MINORITY SHATTERING: Shook the Asian diaspora across North America; ignited international debate on the dark side of authoritarian "Tiger Parenting" and academic pressure.
2. DEHUMANIZATION OF VICTIMS: Parents reduced from loving caregivers to "cruel wardens" and "obstacles" to freedom; objectified as financial tools to access an estimated $500,000 estate and insurance payout; total affective empathy deficit while listening to gunfire.
3. COGNITIVE COMPARTMENTALIZATION: Maintained two completely isolated mental compartments for nearly a decade: the dutiful daughter playing piano by day, and the forged-transcript dropout collaborating with hitmen by night; the agony of the surviving father awakening from a coma to identify his daughter as an accomplice.
4. PERPETUAL VICTIMHOOD & NARCISSISTIC DEFENSE: Portrayed herself as a helpless damsel in distress; wept theatrical tears in court; showed callous detachment upon receiving life imprisonment with no parole for 25 years; pursued procedural appeals in 2023 to avoid moral guilt.
5. MINIMIZATION & RATIONALIZATION: When cornered during interrogation, Jennifer floated a preposterous defense claiming she hired hitmen to end her own life due to despair, blaming the intruders for going rogue; projected culpability onto parental strictness.
6. PRECIPITATING STRESSOR & TIPPING POINT: Initial trigger was failing 12th-grade calculus and knee injury ending Olympic dreams; final tipping point in spring 2010 when her father discovered the academic fraud, impounded her phone, and enforced domestic confinement.
7. PSYCHOLOGICAL SIGNATURE VS. MODUS OPERANDI: Modus Operandi (unlocked front door, staged home invasion, outsourced gunmen) evolved; Signature was the narcissistic urge to be seen as the ultimate innocent victim: hands deliberately bound loosely to allow a dramatic 911 performance as an alibi.
8. ESCALATION CYCLE & SUNK COST TRAP: Trapped by sunk costs: high school report card forgery -> fake Ryerson acceptance -> invented University of Toronto pharmacology studies -> fake graduation -> fabricated SickKids hospital job -> hiring assassins to prevent ego collapse.
9. HALO EFFECT & SOCIAL BLINDSPOTS: Pristine exterior (piano awards, figure skating medals, polite demeanor) served as an invisible cloak; parents fell prey to Normalcy Bias, ignoring numerous red flags for years.
10. VICTIMOLOGY & 4 SURVIVAL RED FLAGS: Honors the immigrant sacrifice of the parents; outlines 4 survival warning signs: (1) Conditional love & punitive discipline; (2) Escalating web of deceit & dual lifestyles; (3) Total control & suppressed autonomy; (4) Emotional detachment & toxic domestic silence.

⏱ TIMESTAMPS
00:00 Intro & Advisory
00:23 Act 1 · The Golden Child Facade and a Decade-Long Tower of Deceit
06:10 Act 2 · A Night of Terror on Helen Avenue and the 911 Call
12:00 Act 3 · Psychological Autopsy: From 'Tiger Parenting' to Pathological Lying
18:15 Act 4 · The Interrogation Room Duel and a Father's Awakening
24:20 Act 5 · The Verdict of Conscience and Moral Warnings

⚠️ LEGAL & SAFETY ADVISORY
• Educational documentary analyzing criminal psychology; does not substitute professional medical or legal counsel.
• Based on public judicial records of the Ontario Superior Court of Justice and York Regional Police. Does not glorify crime.
• Animal avatars are artistic storytellers. Narration, visuals, and audio utilize AI production tools.

📚 OFFICIAL SOURCES
• Ontario Superior Court of Justice: R. v. Pan et al. (2014 ONSC) — https://www.canlii.org/
• Court of Appeal for Ontario: 2023 ONCA 362 — https://www.ontariocourts.ca/coa/
• York Regional Police (YRP) 911 Emergency Audio & Forensic Interrogation Tapes — https://www.yrp.ca/
• Karen K. Ho: 'Jennifer Pan's Revenge' (Toronto Life, 2015)

#AmberEyes #TrueCrime #CriminalPsychology #JenniferPan #TigerParenting #MarkhamCase #PathologicalLying #Mythomania #10PsychologicalMarkers #CaseFile"""

DESC_JA = """第13話: 完璧な優等生の仮面と10年間の嘘 | 犯罪心理学: ジェニファー・パン事件（10の心理的指標） | Amber eyes

カナダ・オンタリオ州マーカムにおいて、フエイ・ハン・パンとビック・ハ・パン夫妻の家庭は、アジア系移民の模範的な成功家庭として称賛されていました。しかし2010年11月8日の夜、ヘレン・アベニュー238番地で鳴り響いた凶弾がその美しい虚飾を引き裂き、世界中を震撼させる悲劇を白日の下に晒しました。「完璧な優等生」の仮面の裏で、長女ジェニファー・パンは10年近くに及ぶ壮大な嘘を隠蔽し、自らの両親を標的とする凶行を企てていたのです。

アンバーアイズが解剖するジェニファー・パン事件の「10の心理的指標」:
1. 社会的余波と模範的移民神話の崩壊: 北米のアジア系社会に激震を与え、「タイガー・ペアレンティング（極端な権威主義的教育）」と学歴至上主義の暗部に関する世界的議論を巻き起こした。
2. 被害者の非人間化（DEHUMANIZATION）: 親を慈愛の養育者から自由を阻む「冷酷な看守」「障害物」へと格下げ。約50万カナダドルの遺産と生命保険金を狙う経済的道具と見なし、銃声を平然と聞き届ける情緒的共感の麻痺。
3. 認知的区画化のパラドックス: 10年間にわたり2つの完全に孤立した人格を作動。昼はピアノを弾く従順な娘、夜は偽造と犯罪者に手を染める逸脱者。生還した父親が娘の共謀を証言する悲劇。
4. 自己愛性被害者意識（PERPETUAL VICTIMHOOD）: 取調室や法廷で涙を流し哀れな無実の被害者を熱演。仮釈放なし25年の終身刑にも冷淡さを見せ、控訴を通じて道徳的責任を回避し続ける。
5. 責任の最小化と自己正当化: 追いつめられた際、「絶望して自らの命を絶つために男たちを雇った」と弁明し、両親の被害は予想外だったと責任を転嫁。
6. 心理的引き金と転落の分岐点: 高校の微積分学落第と膝の負傷による五輪断念が最初の契機。2010年春、嘘が発覚し外出禁止と携帯没収を受けたことで破滅的な凶行への導火線に点火。
7. 心理的署名 vs. 犯行手口: 手口（解錠、強盗偽装、外部への犯行委託）の裏にある不変の署名。それは「最も哀れな被害者」として見られたいという強迫観念。緩く縛られた手で911通報を演じたアリバイ工作。
8. 虚飾のエスカレーション（サンクコストの罠）: 成績表偽造から大学合格詐称、卒業式捏造、名門小児病院勤務の嘘へと膨張。もはや真実を明かせなくなり、両親排除の凶行へ突入。
9. ハロー効果と社会的盲点: フィギュア大会受賞やピアノ認定の栄誉が完璧な隠れ蓑となり、親も正常性バイアスにより数々の矛盾を長年見落とした。
10. 被害者学と4つの生存危険信号: 両親の勤勉な犠牲を記憶し、現代家庭へ警鐘を鳴らす: (1) 条件付きの愛と過酷な懲罰、(2) 拡大する嘘と二重生活、(3) 過剰監視と自律性の剥奪、(4) 情緒的対話の断絶と有害な沈黙。

⏱ チャプター
00:00 イントロ＆注意事項
00:23 第1幕: 完璧な優等生の仮面と十年間に及ぶ虚飾の楼閣
06:10 第2幕: ヘレン・アベニューの惨劇と911通報の波紋
12:00 第3幕: 心理解剖: 「タイガー・ペアレンティング」から病的虚言へ
18:15 第4幕: 取調室の心理戦と生還した父親の証言
24:20 第5幕: 良心の審判と現代への警鐘

⚠️ 法的留意事項
• 犯罪心理学および歴史的資料に基づく教育的コンテンツです。
• カナダ高等裁判所およびヨーク地域警察の公式記録に基づきます。

#AmberEyes #犯罪心理学 #ジェニファーパン #タイガーペアレンティング #マーカム事件 #病的虚言癖 #10の心理的指標"""

DESC_KO = """제13화: 완벽한 모범생의 가면과 10년의 거짓말 | 범죄심리학: 제니퍼 판 사건 (10가지 심리적 지표) | Amber eyes

캐나다 온타리오주 마컴에서 후이 한 판과 빅 하 판 부부의 가정은 아시아계 이민자 사회에서 가장 모범적인 성공 신화로 손꼽혔습니다. 그러나 2010년 11월 8일 밤, 헬렌 애비뉴 238번지에서 울려 퍼진 총성은 화려한 장막을 찢어발기며 전 세계를 충격에 빠뜨린 비극을 드러냈습니다. 착하고 순종적인 '완벽한 모범생' 가면 뒤에서, 장녀 제니퍼 판은 10년 가까이 거대한 기만의 성채를 쌓아 올렸고 끝내 친부모의 목숨을 노린 잔혹한 음모를 꾸몄습니다.

앰버 아이즈가 해부하는 제니퍼 판 사건의 '10대 심리 및 행동 지표':
1. 사회적 파장과 모범 이민자 신화의 붕괴: 북미 아시아계 사회를 뒤흔들고, '타이거 패런팅(극단적 권위주의 훈육)'과 학벌 지상주의의 파괴적 이면에 대한 전 세계적 논쟁 촉발.
2. 피해자의 비인간화 (DEHUMANIZATION): 헌신적인 부모를 자유를 가로막는 '잔인한 교도관'이자 '장애물'로 격하; 약 50만 캐나다 달러의 유산과 보험금을 노린 경제적 수단으로 전락시켰으며, 총성을 들으면서도 애원조차 하지 않은 정서적 공감 결여.
3. 인지적 구획화의 역설: 10년 동안 완벽히 격리된 두 인격을 가동: 낮에는 피아노를 치는 순종적인 딸, 밤에는 위조와 범죄자들과 결탁한 일탈자. 기적적으로 깨어난 아버지가 딸의 공모를 증언하는 비극.
4. 자기애적 피해자 코스프레 (PERPETUAL VICTIMHOOD): 취조실과 법정에서 눈물을 쏟으며 가련한 무고한 피해자 행세; 가석방 없는 25년 종신형에도 냉담함을 보였으며, 항소를 통해 도덕적 책임을 끊임없이 회피.
5. 책임의 최소화와 자기정당화: 취조실에서 덜미가 잡히자 '절망에 빠져 스스로 생을 마감하려 괴한들을 고용했다'는 궤변을 늘어놓으며, 부모의 엄격함이 자신을 벼랑 끝으로 몰았다고 원망.
6. 심리적 방아쇠와 티핑 포인트: 고교 미적분학 낙제와 무릎 부상으로 인한 올림픽 좌절이 첫 뇌관; 2010년 봄 학력 위조가 발각되어 외출 금지와 휴대폰 압수를 당하자 억압된 분노가 파괴적 범행으로 폭발.
7. 심리적 서명 vs. 범행 수법: 수법(문 열어두기, 강도 위장, 청부 살해) 너머의 불변의 서명. 그것은 '가장 불쌍한 피해자'로 인정받으려는 강박. 손이 묶인 척 연출하며 911 신고극을 펼친 알리바이 공작.
8. 에스컬레이션 궤적 (매몰비용의 함정): 성적표 위조에서 명문대 합격 사기, 졸업식 조작, 아동병원 취업 거짓말로 눈덩이처럼 확대. 진실을 밝힐 수 없어 부모 제거라는 극단적 선택으로 돌진.
9. 후광 효과와 사회적 맹점: 피겨스케이팅 메달과 피아노 자격증, 온순한 태도가 완벽한 투명 망토가 되었으며, 부모 역시 정상성 편향으로 수년간 수많은 모순을 간과함.
10. 피해자학과 4가지 생존 적색경보: 부모의 성실한 희생을 기리고 현대 가정에 경종을 울림: (1) 조건부 사랑과 가혹한 징벌, (2) 확대되는 거짓말과 이중생활, (3) 과도한 감시와 자율성 박탈, (4) 정서적 단절과 유독한 침묵.

⏱ 타임스탬프
00:00 인트로 & 안내
00:23 제1막: 모범생의 가면과 10년 동안 쌓아 올린 거짓의 성채
06:10 제2막: 헬렌 애비뉴의 참극과 911 신고 전화의 파문
12:00 제3막: 심리 부검: '타이거 패런팅'에서 병적 허언증으로
18:15 제4막: 취조실의 심리전과 깨어난 아버지의 증언
24:20 제5막: 양심의 판결과 현대사회를 향한 경종

⚠️ 법적 안내
• 범죄심리학 및 역사적 기록에 기반한 교육용 콘텐츠입니다.
• 온타리오주 고등법원 및 요크 지역 경찰청의 공개 기록을 바탕으로 제작되었습니다.

#AmberEyes #범죄심리학 #제니퍼판 #타이거패런팅 #마컴사건 #병적허언증 #10대심리지표"""

def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    clean_content = content.strip().replace("\r\n", "\n")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(clean_content + "\n")

def main():
    print("=== ĐO LƯỜNG ĐỘ DÀI MÔ TẢ TẬP 13 (TRẦN: 5000 KÝ TỰ) ===")
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
        
    print("\n=== TIẾN HÀNH XUẤT BẢN FILE MÔ TẢ & NGUỒN TẬP 13 ===")
    
    files_to_write = [
        # Tiếng Việt
        (ROOT / "02_SAN_XUAT" / "Tap13" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap13" / "xuat_ban" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap13" / "nguon_mo_ta.txt", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap13" / "nguon_tham_khao.md", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap13" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),
        
        # Tiếng Anh
        (ROOT / "02_SAN_XUAT" / "Tap13_EN" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap13_EN" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap13_EN" / "xuat_ban" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap13_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap13_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap13_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap13_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),
        
        # Tiếng Nhật
        (ROOT / "02_SAN_XUAT" / "Tap13_JA" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap13_JA" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap13_JA" / "xuat_ban" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap13_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap13_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap13_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap13_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),
        
        # Tiếng Hàn
        (ROOT / "02_SAN_XUAT" / "Tap13_KO" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap13_KO" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap13_KO" / "xuat_ban" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap13_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap13_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap13_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap13_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
    ]
    
    for path, content in files_to_write:
        write_text(path, content)
        print(f"  -> Đã ghi: {path.relative_to(ROOT)} ({len(content.strip()):,} ký tự)")
        
    print("\n>>> TẤT CẢ FILE MÔ TẢ TẬP 13 ĐÃ ĐƯỢC CẬP NHẬT HOÀN TẤT VÀ ĐẠT CHUẨN! <<<")


if __name__ == "__main__":
    main()
