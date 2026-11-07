#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo các file mô tả và nguồn tham khảo cho Tập 17 trên 4 ngôn ngữ (VN, EN, JA, KO).
Đảm bảo đầy đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c, K10) và TUYỆT ĐỐI <= 5000 ký tự.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO CHO TẬP 17
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 17 (HỒ SƠ GIA ĐÌNH TURPIN)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp chính thức của California và báo chí điều tra Hoa Kỳ:

1. Hồ sơ Tòa án & Phán quyết tư pháp Bang California:
• Tòa Thượng thẩm Bang California Hạt Riverside (Riverside County Superior Court) — Hồ sơ xét xử People of the State of California v. David Allen Turpin & Louise Ann Turpin (Case No. RIF1800348, Thẩm phán Bernard Schwartz chủ tọa): https://www.riverside.courts.ca.gov/
• Văn phòng Biện lý Hạt Riverside (Riverside County District Attorney's Office) — Bản cáo trạng 14 trọng tội và hồ sơ thỏa thuận nhận tội do Biện lý Michael Hestrin công bố: https://rivcoda.org/
• Cục Cải huấn & Phục hồi Bang California (CDCR) — Quyết định thi hành bản án 25 năm đến chung thân tại các cơ sở an ninh tối đa (Mule Creek State Prison & Central California Women's Facility): https://www.cdcr.ca.gov/

2. Hồ sơ Cảnh sát & Tư liệu thực địa:
• Văn phòng Cảnh sát trưởng Hạt Riverside (Riverside County Sheriff's Department) — Báo cáo hiện trường số 160 đường Muir Woods Road, Perris, California ngày 14/01/2018: https://www.riversidesheriff.org/
• Bản ghi âm cuộc gọi 911 dài 20 phút của Jordan Turpin (17 tuổi) bằng điện thoại di động mất sóng: https://www.cbsnews.com/

3. Báo chí Điều tra & Phỏng vấn độc quyền:
• ABC News 20/20 (Chủ trì: Ký giả Diane Sawyer) — Phỏng vấn độc quyền 'Escape from a House of Horror: The Turpin Sisters Speak' (tháng 11/2021): https://abcnews.go.com/
• Los Angeles Times — Lưu trữ điều tra về lỗ hổng quản lý trường tư thục tại gia (Sandcastle Day School) tại California: https://www.latimes.com/
• The New York Times — Phân tích xã hội học về cơ chế cô lập gia đình khép kín và bi kịch của 13 anh chị em: https://www.nytimes.com/

4. Tâm lý học Pháp y, Tâm thần học & Khoa học Hành vi:
• Khái niệm Kiểm soát cưỡng chế (Coercive Control) theo Giáo sư Evan Stark.
• Hội chứng Điên cuồng đôi (Folie à Deux / Shared Delusional Disorder) và cơ chế Chia ngăn nhận thức (Compartmentalization).
• Gavin de Becker — Tác phẩm kinh điển về nhận diện nguy cơ sinh tồn và bản năng tự vệ 'The Gift of Fear' (Dell Publishing, 1997).
• Khái niệm Tăng trưởng sau sang chấn (Post-Traumatic Growth - PTG) trong tâm lý học lâm sàng.

5. Đường dây nóng hỗ trợ khẩn cấp:
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý & trầm cảm): 096 306 1414
• Childhelp National Child Abuse Hotline (Hoa Kỳ): 1-800-422-4453 — https://www.childhelphotline.org/
• National Domestic Violence Hotline (Hoa Kỳ): 1-800-799-SAFE (7233) — https://www.thehotline.org/"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 17 (THE TURPIN FAMILY CASE)
Amber eyes adheres to multi-source cross-verification from official California judicial records and investigative journalism:

1. California State Court Archives & Judicial Verdicts:
• Riverside County Superior Court — Criminal Proceedings in People of the State of California v. David Allen Turpin & Louise Ann Turpin (Case No. RIF1800348, Hon. Bernard Schwartz presiding): https://www.riverside.courts.ca.gov/
• Riverside County District Attorney's Office — Official 14-count felony indictment and guilty plea disposition by District Attorney Michael Hestrin: https://rivcoda.org/
• California Department of Corrections and Rehabilitation (CDCR) — 25-years-to-life incarceration records (Mule Creek State Prison & CCWF): https://www.cdcr.ca.gov/

2. Law Enforcement Records & Emergency Dispatch:
• Riverside County Sheriff's Department — Crime Scene and Evidence Recovery Reports for 160 Muir Woods Road, Perris, CA (Jan 14, 2018): https://www.riversidesheriff.org/
• 20-minute 911 Emergency Dispatch Audio Recording of Jordan Turpin (aged 17) using a deactivated cell phone: https://www.cbsnews.com/

3. Investigative Journalism & Exclusive In-Depth Interviews:
• ABC News 20/20 (Anchor Diane Sawyer) — Exclusive Documentary 'Escape from a House of Horror: The Turpin Sisters Speak' (Nov 2021): https://abcnews.go.com/
• Los Angeles Times — Investigative series exposing regulatory loopholes in California private homeschools (Sandcastle Day School): https://www.latimes.com/
• The New York Times — Socio-legal analyses of coercive control and domestic captivity.

4. Forensic Psychology, Psychiatry & Behavioral Science:
• Coercive Control Theory by Prof. Evan Stark.
• Shared Delusional Disorder (Folie à Deux) and Cognitive Compartmentalization frameworks.
• Gavin de Becker — Seminal work on survival intuition 'The Gift of Fear' (Dell Publishing, 1997).
• Post-Traumatic Growth (PTG) models in trauma recovery.

5. Crisis Support & Protective Hotlines:
• Child Protective Services / Crisis Response (Vietnam): Hotline 111 (24/7 Free) — http://tongdai111.vn/
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelphotline.org/
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org/"""

SOURCES_JA = """📚 第17話 参考文献・公式調査資料一覧（ターピン一家事件）
アンバーアイズ（Amber eyes）は、カリフォルニア州司法省の公式裁判記録および権威ある調査報道資料を厳格に照合しています。

1. カリフォルニア州公式裁判記録および司法判決文書:
• リバーサイド郡上級裁判所（Riverside County Superior Court）— 刑事裁判記録 People v. David Allen Turpin & Louise Ann Turpin (事件番号 RIF1800348, バーナード・シュワルツ裁判長): https://www.riverside.courts.ca.gov/
• リバーサイド郡地方検察局（Riverside County District Attorney's Office）— マイケル・ヘストリン検事による有罪答弁調書および起訴記録: https://rivcoda.org/
• カリフォルニア州矯正リハビリテーション局（CDCR）— 25年から終身刑の服役記録: https://www.cdcr.ca.gov/

2. 警察実地捜査記録および通報音声:
• リバーサイド郡保安官事務所 — 2018年1月14日 ペリス市ミュア・ウッズ・ロード160番地 現場検証報告書: https://www.riversidesheriff.org/
• ジョーダン・ターピン（当時17歳）による20分間の911緊急通報録音アーカイブ: https://www.cbsnews.com/

3. 調査報道および独占ドキュメンタリー:
• ABCニュース 20/20（ダイアン・ソイヤー記者）— 独占取材『Escape from a House of Horror: The Turpin Sisters Speak』（2021年11月放送）: https://abcnews.go.com/
• ロサンゼルス・タイムズ紙 — カリフォルニア州における私設ホームスクール（サンドキャッスル・デイ・スクール）の監視不備に関する調査報道: https://www.latimes.com/
• ニューヨーク・タイムズ紙 — 密室型家庭内監禁の社会学的・心理学的分析。

4. 法精神医学、行動科学および被害者学:
• エヴァン・スターク教授による「強圧的支配（Coercive Control）」理論。
• 共有精神病（Folie à Deux）および精神の区分化（Compartmentalization）モデル。
• ギャヴィン・ド・ベッカー — 直感の危機管理科学『The Gift of Fear』（邦題：『暴力から逃れるための10のレッスン』）。
• 臨床心理学におけるトラウマ後成長（PTG）理論。

5. 危機支援・相談窓口:
• 全米子ども虐待防止ホットライン（USA）: 1-800-422-4453 — https://www.childhelphotline.org/
• 全米DVホットライン（USA）: 1-800-799-SAFE (7233) — https://www.thehotline.org/
• 子ども保護ホットライン（ベトナム）: 111 (24時間無料)"""

SOURCES_KO = """📚 제17화 참고 문헌 및 공식 수사 기록 (터핀 가족 사건)
앰버 아이즈(Amber eyes)는 캘리포니아주 사법부의 공식 재판 기록과 권위 있는 탐사보도 자료를 엄격하게 교차 검증합니다.

1. 캘리포니아주 법원 공식 재판 기록 및 판결문:
• 리버사이드 카운티 상급법원 (Riverside County Superior Court) — 형사 재판 기록 People v. David Allen Turpin & Louise Ann Turpin (사건번호 RIF1800348, 버나드 슈워츠 재판장): https://www.riverside.courts.ca.gov/
• 리버사이드 카운티 지방검찰청 (Riverside County District Attorney's Office) — 마이클 헤스트린 검사장의 공식 기소장 및 유죄 인정 합의 기록: https://rivcoda.org/
• 캘리포니아 교정재활국 (CDCR) — 25년에서 종신형 복역 수형 기록: https://www.cdcr.ca.gov/

2. 경찰 수사 기록 및 긴급 통화 자료:
• 리버사이드 카운티 보안관실 — 2018년 1월 14일 페리스시 뮤어 우즈 로드 160번지 사건 현장 감식 보고서: https://www.riversidesheriff.org/
• 당시 17세였던 조던 터핀의 20분간 911 긴급 구조 요청 음성 아카이브: https://www.cbsnews.com/

3. 탐사보도 및 독점 다큐멘터리:
• ABC 뉴스 20/20 (다이앤 소여 앵커) — 독점 르포 다큐멘터리 'Escape from a House of Horror: The Turpin Sisters Speak' (2021년 11월): https://abcnews.go.com/
• 로스앤젤레스 타임스 (Los Angeles Times) — 사립 홈스쿨링(샌드캐슬 데이 스쿨) 관리 사각지대 심층 보도: https://www.latimes.com/
• 뉴욕 타임스 (The New York Times) — 밀실 가정 내 강압적 통제와 감금에 대한 사회학적 분석.

4. 법정신의학, 행동과학 및 피해자학:
• 에반 스타크 교수의 '강압적 통제(Coercive Control)' 이론.
• 공유정신병(Folie à Deux) 및 인지적 구획화(Compartmentalization) 임상 모델.
• 개빈 드 베커 — 위험 평가와 생존 본능의 고전 'The Gift of Fear' (생존의 선물).
• 임상심리학의 외상 후 성장(PTG) 회복 이론.

5. 위기 상담 및 피해자 지원 핫라인:
• 미국 전국 아동학대 예방 핫라인: 1-800-422-4453 — https://www.childhelphotline.org/
• 미국 가정폭력 핫라인: 1-800-799-SAFE (7233) — https://www.thehotline.org/
• 아동보호 핫라인 (베트남): 111 (24시간 무료)"""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Tập 17: 13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Kiểm Soát Cưỡng Chế, Ảo Tưởng Điên Cuồng Đôi & Cú Nhảy Sinh Tồn (Hồ Sơ Gia Đình Turpin) | Amber eyes

Rạng sáng 14/01/2018, tại thị trấn Perris thuộc hạt Riverside, California, một thiếu nữ 17 tuổi gầy gò trèo qua bậu cửa sổ, mang theo chiếc điện thoại di động mất sóng gọi 911. Cuộc gọi sinh tử ấy đã giải thoát cho 13 anh chị em khỏi một ngục tù gia đình tàn bạo tồn tại suốt nhiều năm giữa lòng khu dân cư yên bình. Thủ phạm chính là hai bậc cha mẹ có học thức: cựu kỹ sư máy tính David Turpin và người vợ nội trợ Louise Turpin.

Hồ sơ Nhà Turpin được Amber eyes giải phẫu toàn diện qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi:
1. DƯ CHẤN XÃ HỘI & CẢI CÁCH THỂ CHẾ: Cơn hoang tưởng tập thể bao trùm ngoại ô Perris khi tội ác tồn tại sát vách suốt hàng thập kỷ; thúc đẩy các phiên điều trần lập pháp tại California nhằm siết chặt quy trình giám sát các trường tư thục tại gia (homeschooling).
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem 13 người con như "đạo cụ sống" phục vụ ảo tưởng quyền lực của cha mẹ; khuyết tật thấu cảm xúc cảm trầm trọng biến tiếng khóc van xin thành sự kích thích kiểm soát toàn năng.
3. NGHỊCH LÝ CHIA NGĂN (COMPARTMENTALIZATION): Khóa chặt hai thế giới tách biệt: ngăn kéo gia đình mẫu mực mặc đồ đồng bộ rạng rỡ ở Disneyland vs ngăn kéo ngục tù bẩn thỉu sau cánh cửa đóng kín; biến gia đình thành lá chắn bình thường hóa.
4. TỰ THƯƠNG HẠI BỆNH LÝ TRƯỚC BẢN ÁN (PATHOLOGICAL SELF-PITY): Lời xin lỗi và nước mắt của hai bị cáo trước tòa phản ánh sự sụp đổ cái tôi ái kỷ khi mất quyền kiểm soát chứ không phải ăn năn chân chính; Thẩm phán Bernard Schwartz tuyên mức án 25 năm đến chung thân.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC (NEUTRALIZATION): Tự khoác áo thiên thần bảo vệ các con khỏi sự cám dỗ độc hại bên ngoài; đổ lỗi nạn nhân "không vâng lời, rửa tay quá cổ tay" để biện minh cho các đòn trừng phạt xích giữ.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY (TIPPING POINT): Khủng hoảng tài chính nợ nần trầm trọng (hai lần nộp đơn phá sản); sự cô lập địa lý khi chuyển từ Texas sang California và áp lực khi các con lớn bước vào tuổi trưởng thành đòi hỏi tự do.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO thay đổi liên tục (chuyển nhà, lập trường Sandcastle Day School, che rèm, đảo lộn ngày đêm); Signature bất biến là ép con mặc đồng phục chụp ảnh tạo dáng, tra tấn tinh thần bằng cách mua bánh ngọt và đồ chơi để trước mặt nhưng cấm chạm vào.
8. QUỸ ĐẠO LEO THANG HÀNH VI: Chu kỳ dung nạp kích thích: mắng mỏ -> bắt úp mặt vào tường -> nhốt trong phòng -> trói bằng dây thừng -> xích bằng xích sắt và ổ khóa cố định vào giường kéo dài hàng tuần, hàng tháng.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI (HALO EFFECT): Vỏ bọc kỹ sư quốc phòng có học thức cao và những bức ảnh gia đình đông con ngoan ngoãn tạo nên điểm mù nhận thức khiến cộng đồng bỏ qua các dấu hiệu kỳ quặc.
10. NẠN NHÂN HỌC & CẢNH BÁO ĐỎ SINH TỒN: Tôn vinh ý chí sinh tồn phi thường của Jordan Turpin qua nguyên lý 'The Gift of Fear' (Gavin de Becker); đúc kết 4 cảnh báo đỏ thực tế giúp nhận diện bạo hành gia đình khép kín.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Cú nhảy qua cửa sổ rạng sáng và cuộc gọi 911 từ chiếc điện thoại hỏng
05:30 Hồi 2 · Ngục tù ngoại ô và vỏ bọc hoàn hảo của gia đình kiểu mẫu
11:15 Hồi 3 · Giải mã tâm lý: Kiểm soát cưỡng chế, ảo tưởng điên cuồng đôi & sự ấu trĩ hóa nạn nhân
17:00 Hồi 4 · Bản cáo trạng rúng động và phiên tòa đối diện công lý
22:45 Hồi 5 · Hành trình tái sinh từ tro tàn & 4 cảnh báo đỏ về bạo hành gia đình kín

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai của Tòa Thượng thẩm Hạt Riverside và Cảnh sát Hạt Riverside. Kênh không tôn vinh hay bôi nhọ bất kỳ cá nhân nào.
• Hình tượng Cú, Sói, Cáo, Cừu, Mèo là linh thú nghệ thuật. Giọng đọc, hình ảnh và âm thanh có ứng dụng công nghệ AI.

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• Phán quyết Tòa Thượng thẩm Hạt Riverside: People v. David Allen Turpin & Louise Ann Turpin (Case No. RIF1800348) — https://www.riverside.courts.ca.gov/
• Tuyên cáo nhận tội: Riverside County District Attorney Michael Hestrin — https://rivcoda.org/
• Phỏng vấn độc quyền: ABC News 20/20 'Escape from a House of Horror: The Turpin Sisters Speak' (Diane Sawyer).
• Khoa học hành vi sinh tồn: 'The Gift of Fear' của Gavin de Becker (1997).

🆘 ĐƯỜNG DÂY NÓNG BẢO VỆ TRẺ EM
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelphotline.org/

#AmberEyes #TrueCrime #TamLyToiPham #TurpinFamily #HouseOfHorrors #CoerciveControl #JordanTurpin #FolieADeux #TheGiftOfFear #ChildProtection #10ChiDauTamLy"""

DESC_EN = """Ep. 17: 13 Captive Children in a Suburban Dungeon — Coercive Control, Shared Delusional Disorder & The Leap for Survival (The Turpin Family Case) | Amber eyes

At dawn on January 14, 2018, in the quiet suburb of Perris, California, a frail 17-year-old girl slipped through a bedroom window, clutching a deactivated smartphone to dial 911. That life-or-death call rescued 13 siblings from years of systematic domestic captivity right in the heart of an ordinary neighborhood. The perpetrators were their own educated parents: former defense aerospace computer engineer David Turpin and homemaker Louise Turpin.

Amber eyes dissects the Turpin Family dossier through the 10 Psychological & Behavioral Indicators:
1. SOCIAL IMPACT & INSTITUTIONAL REFORM: Collective shock and paranoia gripped suburban Perris upon realizing horrors existed next door for decades; triggered state legislative hearings to close oversight loopholes in California private homeschooling.
2. OBJECTIFICATION & DEHUMANIZATION: The 13 children were viewed not as autonomous humans, but as "living props" serving parental narcissistic fantasies; severe affective empathy deficits turned desperate cries into stimuli for omnipotent control.
3. COGNITIVE COMPARTMENTALIZATION: Strictly locked two worlds: the smiling, matching-outfit model family at Disneyland on Facebook vs. the dark, filthy domestic dungeon; family functioned as a shield of normalization.
4. PATHOLOGICAL SELF-PITY BEFORE THE BENCH: Courtroom tears and apologies reflected Narcissistic Collapse upon losing total dominion, rather than genuine remorse; Judge Bernard Schwartz sentenced both defendants to 25 years to life.
5. MORAL NEUTRALIZATION: Rationalized cruelty through a savior complex, claiming captivity protected offspring from outside corruption; blamed victims for "disobedience" like washing hands past wrists to justify chaining.
6. THE PSYCHOLOGICAL TRIGGER & ESCALATION: Severe debt and two bankruptcy filings; geographic isolation moving from Texas to California, and loss of control as older offspring reached adulthood and yearned for freedom.
7. PSYCHOLOGICAL SIGNATURE VS. OPERATIONAL MO: Tactical MO evolved (relocating, establishing Sandcastle Day School, shuttered windows, nocturnal routine); invariable Signature was identical coordinated outfits and psychological taunting with forbidden pies and toys.
8. BEHAVIORAL ESCALATION TRAJECTORY: Tolerance buildup over years: verbal berating -> standing facing walls -> room isolation -> rope binding -> heavy iron chains and padlocks secured to bedframes for weeks and months.
9. THE HALO EFFECT & COLLECTIVE BLINDSPOTS: David's defense engineer pedigree and churchgoing veneer created an institutional halo effect, blinding neighbors to bizarre underlying anomalies.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Honoring Jordan Turpin's resilience via Gavin de Becker's 'The Gift of Fear'; extracting 4 vital red flags to detect concealed domestic captivity.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Advisory
00:23 Act 1 · The Dawn Window Escape and the 911 Call from a Deactivated Phone
05:30 Act 2 · Suburban Dungeon and the Flawless Facade of a Model Family
11:15 Act 3 · Psychological Autopsy: Coercive Control, Folie à Deux & Infantilization
17:00 Act 4 · The Shocking Indictment and Confronting Justice in Court
22:45 Act 5 · Rebirth from Ashes & 4 Survival Red Flags on Domestic Captivity

⚠️ LEGAL & SAFETY ADVISORY
• Educational documentary analyzing criminal psychology; does not substitute professional medical or legal counsel.
• Based on public records of the Riverside County Superior Court and Riverside County Sheriff's Department. Does not glorify crime.
• Animal avatars are artistic storytellers. Narration, visuals, and audio utilize AI production tools.

📚 OFFICIAL SOURCES
• Riverside County Superior Court: People v. David Allen Turpin & Louise Ann Turpin (Case No. RIF1800348) — https://www.riverside.courts.ca.gov/
• Riverside County District Attorney's Office — Official Indictment Disposition — https://rivcoda.org/
• Exclusive Interview: ABC News 20/20 'Escape from a House of Horror: The Turpin Sisters Speak' (Diane Sawyer).
• Behavioral Survival Science: 'The Gift of Fear' by Gavin de Becker (1997).

🆘 CHILD PROTECTION HOTLINES
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelphotline.org/
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org/
• Child Protective Services (Vietnam): Hotline 111 (24/7 Free) — http://tongdai111.vn/

#AmberEyes #TrueCrime #CriminalPsychology #TurpinFamily #HouseOfHorrors #CoerciveControl #JordanTurpin #FolieADeux #TheGiftOfFear #ChildProtection #10PsychologicalMarkers"""

DESC_JA = """第17話：郊外の暗闇に隠された真実 — 強圧的支配、共有精神病と命懸けの脱出（ターピン一家事件） | Amber eyes

2018年1月14日未明、カリフォルニア州ペリスの静かな住宅街で、小柄な17歳の少女が窓枠を乗り越え、解約された携帯電話から911へ緊急通報を行いました。その決死の通報により、13人の兄弟姉妹が長年にわたる過酷な家庭内監禁から救出されたのです。加害者は、高学歴の元航空宇宙防衛技術者の父親デイヴィッドと、専業主婦の母親ルイーズでした。

アンバーアイズは、ターピン一家事件を「10の心理・行動指標体系」を通じて解剖します：
1. 社会的余波と制度改革：平穏な郊外住宅街に数十年潜んでいた地獄に地域社会は震撼；カリフォルニア州における私設ホームスクール（サンドキャッスル・デイ・スクール）の監視体制の不備が浮き彫りとなり、法改正の議論を促進。
2. 被害者の客体化（Objectification）：13人の実子を人格ではなく親の全能感を満たす「生きた小道具」として扱い、極端な共感性欠如により嘆願の声を支配の刺激として消費。
3. 精神の区分化（Compartmentalization）：SNS上の「ディズニーランドで揃いの服を着た幸福な模範家族」と密室の「不衛生な監禁部屋」を完全に分断し、家庭を正常化の盾として利用。
4. 判決前の病的な自己憐憫：法廷での涙と謝罪は支配権力を喪失したことによる「自己愛の完全崩壊」であり、真の悔悟ではないと看破；シュワルツ判事は25年から終身刑を宣告。
5. 道徳的中和技術：子供を世間の悪から守る聖なる使命と信じ込み、「手首より上を洗った」等の些細な不服従を理由に鎖による拘束を自己正当化。
6. 心理的引き金と暴走：莫大なカード負債と二度の破産申告；テキサスからカリフォルニアへの移住による地理的孤立と、成長した子供たちが自由を希求し始めたことによる統制喪失の危機。
7. 手口（MO）と心理的刻印（Signature）：引越しや遮光カーテン、昼夜逆転という変化する手口に対し、揃いの衣服での写真撮影や、ケーキや玩具を目の前に置きながら触れることを禁じる精神的拷問が不変の心理的刻印。
8. 行動のエスカレーション：叱責から暗室閉じ込め、ロープ拘束を経て、重い鉄の鎖と南京錠による数週間から数か月に及ぶ長期緊縛へと過激化。
9. 後光効果（ハロー効果）と社会の死角：元防衛産業技術者という高学歴な肩書と、従順な大家族の仮面が地域社会の警戒心を麻痺させた。
10. 被害者学と生存レッドフラッグ：ジョーダンの直感と勇気を『The Gift of Fear』の原理で称賛；密室型家庭内虐待を見抜く4つの重要指標を提示。

⏱ タイムスタンプ
00:00 イントロ＆注意事項
00:23 第1幕 · 夜明けの窓からの脱出と解約携帯による911通報
05:30 第2幕 · 郊外の要塞と理想的家族の完璧な仮面
11:15 第3幕 · 心理解剖：強圧的支配、共有精神病および被害者の幼態化
17:00 第4幕 · 激震の起訴状と司法の正義との対峙
22:45 第5幕 · 灰燼からの再生と密室虐待を見抜く4つのレッドフラッグ

⚠️ 免責事項・安全基準
• 本動画は犯罪心理学の教育的分析を目的としており、専門的な助言に代わるものではありません。
• リバーサイド郡上級裁判所および保安官事務所の公式記録に基づいています。
• キャラクターは芸術的表現です。音声、映像にはAI技術を活用しています。

📚 公式参考文献
• リバーサイド郡上級裁判所判決録: People v. David Allen Turpin & Louise Ann Turpin (Case No. RIF1800348)
• ABCニュース 20/20 独占取材『Escape from a House of Horror: The Turpin Sisters Speak』
• 生存心理学：ギャヴィン・ド・ベッカー『The Gift of Fear』（1997年）

🆘 緊急相談窓口
• 全米子ども虐待ホットライン（USA）: 1-800-422-4453 — https://www.childhelphotline.org/
• 子ども保護ホットライン（ベトナム）: 111 (24時間無料)

#AmberEyes #犯罪心理学 #ターピン一家 #恐怖の館 #強圧的支配 #ジョーダンターピン #共有精神病 #児童保護 #10の心理指標"""

DESC_KO = """제17화: 교외의 감옥에 갇힌 13남매 — 강압적 통제, 공유정신병과 생존을 향한 도약 (Turpin 가족 사건) | Amber eyes

2018년 1월 14일 새벽, 캘리포니아주 페리스의 평온한 교외 주택가에서 야윈 17세 소녀가 창틀을 뛰어넘어 서비스가 해지된 휴대전화로 911에 전화를 걸었습니다. 그 필사의 통화는 평범한 이웃들 사이에서 수년간 지속되던 끔찍한 가정 내 감옥으로부터 13명의 형제자매를 구출해 냈습니다. 가해자는 전직 방위산업 항공우주 컴퓨터 엔지니어 아버지 데이비드 터핀과 전업주부 어머니 루이즈 터핀이었습니다.

앰버 아이즈는 터핀 가족 사건을 '10가지 심리 및 행동 지표 체계'를 통해 종합 해부합니다:
1. 사회적 파장 및 제도 개혁: 평온한 교외 한가운데서 수십 년간 참상이 방치되었다는 사실에 집단적 충격; 캘리포니아주 사립 홈스쿨링(샌드캐슬 데이 스쿨) 관리 사각지대를 개선하기 위한 입법 청문회 촉발.
2. 피해자의 객체화(Objectification): 13명의 친자녀를 독립된 인격체가 아닌 부모의 나르시시즘을 채우는 '살아있는 소품'으로 전락시켰으며, 극단적인 공감 결여로 울부짖음을 전능한 지배의 자극으로 소비.
3. 인지적 구획화(Compartmentalization): SNS상의 '디즈니랜드에서 같은 옷을 맞춰 입은 화목한 모범 가족'과 밀실의 '더러운 감옥'을 완벽히 분리하여 가정을 정상화의 방패로 악용.
4. 판결 앞의 병적인 자기연민: 법정에서 보인 눈물과 사과는 진정한 참회가 아닌 지배 권력을 잃은 데서 온 '자기애적 붕괴'임을 간파; 슈워츠 판사는 25년에서 종신형을 선고.
5. 도덕적 중화 기술: 세상의 유혹으로부터 아이들의 순결을 지킨다는 구원자 콤플렉스를 주입하고, '손목 위로 손을 씻었다'는 식의 사소한 불복종을 구실로 결박 학대를 정당화.
6. 심리적 기폭제와 폭주: 막대한 신용카드 부채와 두 차례의 파산 신청; 텍사스에서 캘리포니아로의 이주에 따른 지리적 고립과 성장한 자녀들의 자유 갈망으로 인한 통제 상실의 위기.
7. 수법(MO)과 심리적 각인(Signature): 잦은 이사, 암막 커튼, 주야 역전 등 변화하는 수법과 달리, 동일한 단체복 촬영과 케이크나 장난감을 눈앞에 두고 만지지 못하게 하는 정신적 고문이 불변의 심리적 각인.
8. 행동 에스컬레이션 궤적: 잔소리에서 벽 보고 서 있기, 독방 감금, 밧줄 결박을 거쳐 무거운 쇠사슬과 자물쇠를 이용한 수주일에서 수개월간의 장기 침대 결박으로 폭주.
9. 후광 효과(Halo Effect)와 사회적 사각지대: 전직 방위산업 엔지니어라는 고학력 배경과 순종적인 대가족의 가면이 지역사회의 의구심을 완전히 잠재웠음.
10. 피해자학 및 생존 레드플래그: 개빈 드 베커의 'The Gift of Fear' 원리를 통해 조던 터핀의 회복 탄력성을 조명; 밀실형 가정 학대를 조기에 감지하는 4가지 생존 레드플래그 제시.

⏱ 챕터 타임스탬프
00:00 인트로 및 안내
00:23 제1막 · 새벽의 창문 탈출과 해지된 전화기를 통한 911 긴급 통화
05:30 제2막 · 교외의 감옥과 완벽한 모범 가정의 가면
11:15 제3막 · 심리 해부: 강압적 통제, 공유정신병 및 피해자의 유아화
17:00 제4막 · 충격적인 기소장과 정의의 법정에 선 가해자들
22:45 제5막 · 잿더미에서의 부활과 밀실 학대를 감지하는 4가지 레드플래그

⚠️ 법적 고지 및 콘텐츠 안내
• 본 영상은 범죄심리학적 분석을 위한 교육용 콘텐츠이며 전문적인 법률·의학 자문을 대신하지 않습니다.
• 리버사이드 카운티 상급법원 및 보안관실의 공개 기록을 바탕으로 제작되었습니다.
• 캐릭터는 예술적 상징입니다. 음성과 시각 요소에는 AI 제작 도구가 활용되었습니다.

📚 공식 참고 문헌
• 리버사이드 카운티 상급법원 판결문: People v. David Allen Turpin & Louise Ann Turpin (Case No. RIF1800348)
• ABC 뉴스 20/20 독점 다큐멘터리 'Escape from a House of Horror: The Turpin Sisters Speak'
• 생존심리학: 개빈 드 베커 저 'The Gift of Fear' (1997)

🆘 아동 보호 긴급 지원 핫라인
• 미국 전국 아동학대 예방 핫라인: 1-800-422-4453 — https://www.childhelphotline.org/
• 아동보호 핫라인 (베트남): 111 (24시간 무료)

#AmberEyes #범죄심리학 #터핀가족사건 #공포의집 #강압적통제 #조던터핀 #공유정신병 #아동보호 #10가지심리지표"""


def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")


def main():
    print("=== KIỂM ĐỊNH ĐỘ DÀI MÔ TẢ TẬP 17 (TRẦN <= 5000 KÝ TỰ) ===")
    
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
        
    print("\n=== TIẾN HÀNH XUẤT BẢN FILE MÔ TẢ & NGUỒN TẬP 17 ===")
    
    files_to_write = [
        # Tiếng Việt
        (ROOT / "02_SAN_XUAT" / "Tap17" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap17" / "xuat_ban" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap17" / "nguon_mo_ta.txt", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap17" / "nguon_tham_khao.md", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap17" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),
        
        # Tiếng Anh
        (ROOT / "02_SAN_XUAT" / "Tap17_EN" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap17_EN" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap17_EN" / "xuat_ban" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap17_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap17_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap17_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap17_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),
        
        # Tiếng Nhật
        (ROOT / "02_SAN_XUAT" / "Tap17_JA" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap17_JA" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap17_JA" / "xuat_ban" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap17_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap17_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap17_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap17_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),
        
        # Tiếng Hàn
        (ROOT / "02_SAN_XUAT" / "Tap17_KO" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap17_KO" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap17_KO" / "xuat_ban" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap17_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap17_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap17_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap17_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
    ]
    
    for path, content in files_to_write:
        write_text(path, content)
        print(f"  -> Đã ghi: {path.relative_to(ROOT)} ({len(content.strip()):,} ký tự)")
        
    print("\n>>> TẤT CẢ FILE MÔ TẢ TẬP 17 ĐÃ ĐƯỢC CẬP NHẬT HOÀN TẤT VÀ ĐẠT CHUẨN! <<<")


if __name__ == "__main__":
    main()
