#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo các file mô tả và nguồn tham khảo cho Tập 19 trên 4 ngôn ngữ (VN, EN, JA, KO).
Đảm bảo đầy đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c, K10) và TUYỆT ĐỐI <= 5000 ký tự.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO CHI TIẾT CHO TẬP 19 (LƯU TRỮ ĐỘC LẬP)
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 19 (HỒ SƠ NIKOLAS CRUZ)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp chính thức của Florida và báo chí điều tra Hoa Kỳ:

1. Hồ sơ Tòa án & Phán quyết tư pháp Bang Florida:
• Tòa án Quận 17 Bang Florida Hạt Broward (Broward County 17th Judicial Circuit Court) — Hồ sơ xét xử State of Florida v. Nikolas Jacob Cruz (Case No. 18-001958CF10A, Thẩm phán Elizabeth Scherer tuyên 34 bản án chung thân không ân xá): https://www.browardclerk.org/
• Văn phòng Biện lý Hạt Broward (Broward State Attorney's Office) — Bản cáo trạng, luận tội và bằng chứng thực nghiệm của Công tố viên Michael Satz: https://browardsao.com/
• Bang Florida (Florida Legislature) — Đạo luật An toàn Công cộng Trường Trung học Marjory Stoneman Douglas (SB 7026, ban hành tháng 3/2018) và Luật cải cách tuyên án tử hình (HB 537, ban hành năm 2023).

2. Hồ sơ Điều tra & Cơ quan Cảnh sát:
• Văn phòng Cảnh sát trưởng Hạt Broward (Broward Sheriff's Office - BSO) — Toàn văn băng ghi âm và video hỏi cung do Thám tử John Curcio thực hiện ngày 14/02/2018: https://www.sheriff.org/
• Ủy ban An toàn Công cộng Marjory Stoneman Douglas (MSD Public Safety Commission) — Báo cáo điều tra toàn diện hơn 400 trang về tiến trình vụ án, các điểm mù thể chế và lỗ hổng an ninh: https://www.fdle.state.fl.us/MSD-Commission
• Cục Điều tra Liên bang Hoa Kỳ (FBI) — Báo cáo kiểm điểm nội bộ về việc tiếp nhận và bỏ sót tin báo đường dây nóng ngày 05/01/2018: https://www.fbi.gov/

3. Báo chí Điều tra & Báo cáo Tư liệu Chuyên sâu:
• Miami Herald — Tuyển tập hồ sơ điều tra chuyên sâu và dòng thời gian tương tác vụ xả súng Parkland: https://www.miamiherald.com/
• South Florida Sun Sentinel — Loạt phóng sự đoạt giải Pulitzer về những sai phạm và điểm mù trong công tác an ninh học đường Parkland: https://www.sun-sentinel.com/
• The New York Times — Phân tích xã hội học về phong trào March for Our Lives và thế hệ học sinh Parkland: https://www.nytimes.com/

4. Tâm lý học Pháp y, Tâm thần học & Hành vi học:
• Bác sĩ Tâm thần học Pháp y Charles Scott, M.D. (Đại học California, Davis) — Báo cáo giám định tâm thần pháp y kết luận Cruz giả bệnh (Malingering) và hoàn toàn kiểm soát nhận thức.
• Hiệp hội Tâm thần học Hoa Kỳ (APA) — Cẩm nang Chẩn đoán và Thống kê Rối loạn Tâm thần DSM-5-TR: Tiêu chuẩn chẩn đoán Malingering (Z76.5) và Rối loạn nhân cách chống đối xã hội (ASPD).
• Gavin de Becker — Tác phẩm kinh điển về nhận diện nguy cơ và đánh giá đe dọa hành vi 'The Gift of Fear' (Dell Publishing, 1997).

5. Đường dây nóng bảo vệ & Hỗ trợ phòng chống bạo lực:
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý & trầm cảm): 096 306 1414
• Đường dây nóng Phòng chống Bạo lực Gia đình (Việt Nam): 1900 969 680
• National Suicide Prevention Lifeline & Crisis Helpline (Hoa Kỳ): 988 hoặc 1-800-273-TALK — https://988lifeline.org/"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 19 (NIKOLAS CRUZ)
Amber eyes adheres to multi-source cross-verification from official Florida judicial records and investigative journalism:

1. Florida State Court Archives & Official Judicial Verdicts:
• 17th Judicial Circuit Court of Florida (Broward County) — Criminal Trial Record State of Florida v. Nikolas Jacob Cruz (Case No. 18-001958CF10A, Hon. Elizabeth Scherer presiding, sentencing defendant to 34 consecutive life terms without parole): https://www.browardclerk.org/
• Broward County State Attorney's Office — Official Indictment, Trial Exhibits, and Aggravating Factors by Lead Prosecutor Michael J. Satz: https://browardsao.com/
• Florida State Legislature — Marjory Stoneman Douglas High School Public Safety Act (SB 7026, March 2018) and Florida Capital Sentencing Reform (HB 537, 2023).

2. Law Enforcement & Investigative Field Records:
• Broward Sheriff's Office (BSO) — Unredacted interrogation video recordings and transcripts conducted by Lead Detective John Curcio on February 14, 2018: https://www.sheriff.org/
• Marjory Stoneman Douglas High School Public Safety Commission — Definitive 400+ page investigative report examining the shooting, institutional blindspots, and security failures: https://www.fdle.state.fl.us/MSD-Commission
• Federal Bureau of Investigation (FBI) — Internal Oversight Review regarding the unforwarded Public Access Line tip on January 5, 2018: https://www.fbi.gov/

3. Investigative Journalism & Primary Archives:
• Miami Herald — In-depth investigative reporting archives and digital timeline on the Parkland tragedy: https://www.miamiherald.com/
• South Florida Sun Sentinel — Pulitzer Prize-winning investigative coverage detailing institutional lapses in school safety: https://www.sun-sentinel.com/
• The New York Times — Socio-legal features on the March for Our Lives movement and student-led activism: https://www.nytimes.com/

4. Forensic Psychiatry, Behavioral Science & Threat Assessment:
• Dr. Charles L. Scott, M.D. (Forensic Psychiatrist, UC Davis) — Expert clinical evaluation establishing forensic evidence of Malingering and intact cognitive capacity.
• American Psychiatric Association (APA) — Diagnostic and Statistical Manual of Mental Disorders DSM-5-TR: Diagnostic criteria for Malingering (Z76.5) and Antisocial Personality Disorder (ASPD).
• Gavin de Becker — Seminal survival intuition and threat assessment treatise 'The Gift of Fear' (Dell Publishing, 1997).

5. Crisis Support & Safety Hotlines:
• Child Protective Services / Crisis Response (Vietnam): Hotline 111 (24/7 Free) — http://tongdai111.vn/
• 988 Suicide & Crisis Lifeline (USA): Dial 988 or 1-800-273-8255 — https://988lifeline.org/
• National School Safety Center (USA): https://www.schoolsafety.us/"""

SOURCES_JA = """📚 第19話 参照資料・公式捜査記録一覧（ニコラス・クルーズ事件）
Amber eyesは、フロリダ州の公的司法記録および米国調査報道機関の一次資料に基づき多角検証を実施しています。

1. フロリダ州公的裁判記録および司法判決：
• フロリダ州第17司法巡回裁判所（ブロワード郡） — 刑事公判記録 State of Florida v. Nikolas Jacob Cruz（事件番号 18-001958CF10A、エリザベス・シェアラー判事による34回連続終身刑宣告）: https://www.browardclerk.org/
• ブロワード郡検察局 — マイケル・サッツ主任検察官による起訴状および証拠提出記録: https://browardsao.com/
• フロリダ州議会 — マージョリー・ストーンマン・ダグラス高校公共安全法（SB 7026、2018年3月成立）および死刑量刑基準改正法（HB 537、2023年成立）。

2. 警察捜査記録および公的報告書：
• ブロワード郡保安官事務所（BSO） — 2018年2月14日、ジョン・クルシオ刑事による完全取調映像および供述調書記録: https://www.sheriff.org/
• マージョリー・ストーンマン・ダグラス高校公共安全委員会（MSD Commission） — 組織的見落としと学校警備の欠陥を総括した400頁超の公式調査報告書: https://www.fdle.state.fl.us/MSD-Commission
• 連邦捜査局（FBI） — 2018年1月5日に受付窓口に寄せられた情報が現場へ伝達されなかった事案に関する内部調査報告: https://www.fbi.gov/

3. 調査報道および学術記録：
• マイアミ・ヘラルド紙 — パークランド高校事件に関する深層調査報道アーカイブ: https://www.miamiherald.com/
• サン・センティネル紙 — 学校警備体制の機能不全を暴きピュリッツァー賞を受賞した連載報道記録: https://www.sun-sentinel.com/
• ニューヨーク・タイムズ紙 — 生徒主導の「命のための行進」運動と銃規制論争に関する社会学的分析。

4. 司法精神医学および行動脅威アセスメント：
• チャールズ・L・スコット医学博士（UC Davis 司法精神医学） — クルーズの詐病（メリンガリング）および十全な責任能力を立証した精神鑑定報告書。
• 米国精神医学会（APA） — 精神疾患の診断・統計マニュアル DSM-5-TR：詐病（Z76.5）および反社会性パーソナリティ障害（ASPD）の診断基準。
• ギャビン・ド・ベッカー — 直感による危険察知と生存のための脅威評価論『The Gift of Fear』。

5. 相談窓口および通報機関：
• 全米危機支援ホットライン: 988 — https://988lifeline.org/
• 児童虐待・緊急通報窓口（ベトナム）: 111（24時間無料）"""

SOURCES_KO = """📚 제19화 공식 참조 자료 및 수사 기록 목록 (니콜라스 크루즈 사건)
Amber eyes는 플로리다주 사법 공식 기록 및 미국 주요 탐사 보도 자료에 입각하여 다각 검증을 수행합니다.

1. 플로리다주 법원 공식 사법 기록 및 판결문:
• 플로리다주 제17사법순회법원 (브로워드 카운티) — 형사 재판 기록 State of Florida v. Nikolas Jacob Cruz (사건번호 18-001958CF10A, 엘리자베스 셰러 판사의 34회 연속 종신형 선고): https://www.browardclerk.org/
• 브로워드 카운티 검찰청 — 마이클 색츠 수석검사의 기소장 및 법정 증거 목록: https://browardsao.com/
• 플로리다주 의회 — 마조리 스톤맨 더글러스 고교 공공안전법 (SB 7026, 2018년 3월) 및 사형 양형 기준 개정법 (HB 537, 2023년).

2. 경찰 수사 기록 및 공식 조사 보고서:
• 브로워드 카운티 보안관실 (BSO) — 2018년 2월 14일 존 커시오 수사관의 취조 녹화 영상 및 공식 신문조서: https://www.sheriff.org/
• 마조리 스톤맨 더글러스 고교 공공안전위원회 (MSD Commission) — 제도적 맹점과 학교 경비 결함을 전면 조사한 400여 쪽의 공식 보고서: https://www.fdle.state.fl.us/MSD-Commission
• 연방수사국 (FBI) — 2018년 1월 5일 제보 전화 접수 후 현장 마이애미 지부로 미전달된 과오에 관한 내부 감사 보고서: https://www.fbi.gov/

3. 탐사 보도 및 학술 기록:
• 마이애미 헤럴드 — 파클랜드 참사 타임라인 및 심층 탐사 취재 아카이브: https://www.miamiherald.com/
• 사우스 플로리다 선 센티널 — 공공기관 맹점을 파헤쳐 퓰리처상을 수상한 심층 탐사 보도: https://www.sun-sentinel.com/
• 뉴욕 타임스 — '우리의 생명을 위한 행진' 운동과 총기 규제 청소년 연대 분석.

4. 사법정신의학 및 행동 위협 평가:
• 찰스 L. 스콧 의학박사 (UC 데이비스 사법정신의학) — 크루즈의 꾀병(메링거링) 및 온전한 사물 변별 능력을 입증한 법정 감정 보고서.
• 미국정신의학회 (APA) — 정신질환 진단 및 통계 편람 DSM-5-TR: 꾀병(Z76.5) 및 반사회성 성격장애(ASPD) 진단 기준.
• 개빈 드 베커 — 생존을 위한 위험 감지와 행동 위협 평가의 고전 『The Gift of Fear』.

5. 위기 상담 및 지원 핫라인:
• 미국 위기 상담 핫라인: 988 — https://988lifeline.org/
• 아동 보호 및 위기 대응 핫라인 (베트남): 111 (24시간 무료)"""

# ==============================================================================
# MÔ TẢ YOUTUBE CHUẨN HOÁ (<= 5000 ký tự)
# ==============================================================================

DESC_VI = """Màn Kịch 'Con Quỷ Trong Đầu' — Giả Bệnh Tâm Thần & Sự Thật Trước Máy Quay (Hồ Sơ Nikolas Cruz) | Amber eyes

Chiều ngày 14/02/2018, tại Trường Trung học Marjory Stoneman Douglas (Parkland, Florida), một cựu học sinh 19 tuổi đã gây ra thảm kịch xả súng chấn động toàn cầu, cướp đi 17 sinh mạng vô tội. Khi bị bắt và đối diện với Thám tử kỳ cựu John Curcio, Nikolas Cruz xuất hiện trong bộ áo bệnh viện, co ro run rẩy và thì thào rằng trong đầu mình có một 'con quỷ' thúc ép 'Đốt, Giết, Phá hủy'. Nhưng ống kính máy quay không chớp mắt trong phòng hỏi cung bí mật và cuộc đấu trí tâm lý xuất sắc của điều tra viên đã bóc trần sự thật: Một màn kịch giả bệnh tâm thần (Malingering) được toan tính lạnh lùng nhằm trốn tránh án phạt cao nhất.

Hồ sơ Nikolas Cruz được Amber eyes giải phẫu toàn diện qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & PHONG TRÀO CẢI CÁCH: Thảm kịch làm rúng động toàn cầu, thổi bùng phong trào March for Our Lives do học sinh Parkland dẫn đầu; thúc đẩy Đạo luật An toàn Học đường Marjory Stoneman Douglas và cải cách luật bồi thẩm đoàn Florida từ 12-0 sang 8-4.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Coi bạn bè và thầy cô như những 'chướng ngại vật' và 'con số thống kê' phục vụ mưu cầu khét tiếng; triệt tiêu thấu cảm nhằm thỏa mãn bản ngã ái kỷ tiêu cực.
3. NGHỊCH LÝ CHIA NGĂN (COMPARTMENTALIZATION): Khóc lóc đóng vai kẻ yếu trước em trai Zachary Cruz trong phòng hỏi cung; mỏ neo kiềm chế sụp đổ khi mẹ nuôi Lynda Cruz qua đời vì viêm phổi cuối năm 2017.
4. BẢN NGÃ SỤP ĐỔ & TỰ THƯƠNG HẠI BỆNH LÝ: Cúi gằm mặt duy trì vỏ bọc suy sụp; lời xin lỗi chiếu lệ nhằm xin tha án tử; nhận 34 bản án chung thân không ân xá, ảo tưởng về sự khét tiếng tan vỡ trước thực tế bị cô lập vĩnh viễn trong bóng tối.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC: Ngoại hóa trách nhiệm về 'con quỷ' để ru ngủ lương tri; bị Curcio bẻ gãy khi thừa nhận hoàn toàn có thể từ chối giọng nói đó khi đi mua sắm và ăn uống.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY BÙNG PHÁT: Bị đuổi học khỏi trường cũ kết hợp với cái chết đột ngột của mẹ nuôi tước đi mỏ neo kiểm soát cuối cùng, kích hoạt kế hoạch trả thù tích tụ.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO (áo gi-lê chiến thuật, súng giấu trong bao đàn guitar, kéo chuông báo cháy, vứt trang bị tẩu thoát); Signature là khao khát được cả thế giới biết tên (tự quay 3 video tuyên ngôn chết chóc).
8. QUỸ ĐẠO LEO THANG HÀNH VI 4 GIAI ĐOẠN: Ngược đãi động vật nhỏ -> Bạo lực học đường & đe dọa trực tuyến -> Mua sắm vũ khí hợp pháp & tích trữ đạn dược -> Tấn công thực tế vào ngày lễ tình nhân.
9. ĐIỂM MÙ THỂ CHẾ & HIỆU ỨNG HÀO QUANG NGƯỢC: Hơn 30 cuộc gọi cảnh báo bị cảnh sát địa phương xử lý rời rạc; đường dây nóng FBI nhận tin báo trực tiếp về nguy cơ xả súng vào đầu năm 2018 nhưng bị bỏ quên do tắc trách hành chính.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ SINH TỒN (BTAM): Tôn vinh phẩm giá và lòng dũng cảm của thầy Aaron Feis, thầy Scott Beigel; đúc kết 4 Cảnh báo đỏ: (1) Rò rỉ ý định (Leakage); (2) Ám ảnh vũ khí & bạo lực (Fixation); (3) Mất mỏ neo kiểm soát (Anchor Loss); (4) Chuẩn bị chiến thuật (Tactical Preparation).

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Căn phòng hỏi cung và lời nói dối về 'con quỷ'
05:45 Hồi 2 · Chiếc máy quay không chớp mắt và khoảnh khắc chiếc mặt nạ rơi xuống
11:30 Hồi 3 · Giải mã tâm lý: Giả bệnh tâm thần (Malingering) vs. Loạn thần thực sự
17:15 Hồi 4 · Bản án 34 án chung thân và sự phán xét của công lý
23:00 Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa bạo lực học đường

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Nội dung mang tính giáo dục, nghiên cứu hành vi học và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ tư pháp công khai của Tòa án Hạt Broward, biên bản hỏi cung BSO và lời khai của TS. Charles Scott. Kênh không nhằm mục đích bôi nhọ hay cổ xúy bạo lực.
• Các nhân vật linh thú là minh họa cách điệu. Lời thoại là lời dựng lại dựa trên tư liệu. Giọng đọc tạo bằng công cụ AI.

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• Phán quyết Tòa án Hạt Broward: State of Florida v. Nikolas Jacob Cruz (Case No. 18-001958CF10A, 34 bản án chung thân không ân xá)
• Băng ghi hình hỏi cung của Thám tử John Curcio (Văn phòng Cảnh sát trưởng Hạt Broward - BSO)
• Giám định tâm thần học pháp y: TS. Charles Scott & Tiêu chuẩn Malingering trong DSM-5-TR
• Báo cáo Ủy ban An toàn Công cộng Marjory Stoneman Douglas (MSD Commission Report)
• Khoa học hành vi sinh tồn: 'The Gift of Fear' của Gavin de Becker

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• 988 Suicide & Crisis Lifeline (Hoa Kỳ): Gọi 988 — https://988lifeline.org/

#AmberEyes #TrueCrime #TamLyToiPham #NikolasCruz #ParklandShooting #Malingering #InterrogationTechniques #BTAM #RedFlags #10ChiDauTamLy #HoSoToiPham"""

DESC_EN = """The 'Demon in the Head' Charade — Malingering & Truth on Camera (The Nikolas Cruz Dossier) | Amber eyes

On February 14, 2018, Marjory Stoneman Douglas High School in Parkland, Florida, was struck by a devastating mass shooting that claimed seventeen innocent lives. When apprehended and seated opposite veteran Detective John Curcio, nineteen-year-old Nikolas Cruz trembled in a hospital gown, whispering that an evil voice commanded him to 'Burn, Kill, Destroy.' However, the unblinking lens of the covert interrogation camera and Curcio's brilliant behavioral tests shattered the illusion: A cold, calculated performance of malingering designed to escape capital punishment.

The Nikolas Cruz dossier is comprehensively analyzed through the 10 Core Psychological & Behavioral Indicators:
1. SOCIAL IMPACT & LEGISLATIVE REFORM: Sparked global shock and the historic youth-led March for Our Lives movement; spurred the Marjory Stoneman Douglas High School Public Safety Act and Florida's capital sentencing reform from 12-0 to 8-4.
2. VICTIM OBJECTIFICATION & EMPATHY DEFICIT: Reduced classmates and educators to mere obstacles and statistics in a quest for negative notoriety; total shutdown of empathy driven by malignant narcissism.
3. COMPARTMENTALIZATION & FAMILY ANCHOR LOSS: Sobbed in an emotional performance before younger brother Zachary Cruz in interrogation; behavioral control collapsed following the sudden death of adoptive mother Lynda Cruz in late 2017.
4. PATHOLOGICAL SELF-PITY & NARCISSISTIC COLLAPSE: Maintained a downcast posture to simulate despair; offered a superficial apology to evade the death penalty; sentenced to 34 consecutive life terms, confronting permanent isolation instead of infamy.
5. NEUTRALIZATION & MALINGERING CHARADE: Externalized blame onto a 'demon' to suppress conscience; completely unraveled when Curcio demonstrated he freely disobeyed the voice during shopping and eating.
6. PSYCHOLOGICAL TRIGGER & BREAKING POINT: Disciplinary expulsion from school combined with the sudden death of his adoptive mother extinguished his final social anchor, triggering long-cultivated vengeance.
7. SIGNATURE VS. MODUS OPERANDI (MO): MO included tactical vest, concealed rifle in guitar case, and pulling the fire alarm; immutable Signature was notoriety-seeking (pre-recording 3 manifesto videos proclaiming his deadly ambition).
8. FOUR-STAGE BEHAVIORAL ESCALATION: Cruelty toward small animals -> Schoolyard violence and online tactical threats -> Legal firearm acquisition and ammunition stockpiling -> Tactical execution of mass assault.
9. INSTITUTIONAL BLINDSPOTS & INVERTED HALO: Over 30 law enforcement warnings mishandled in isolation; direct FBI tip-line warning in January 2018 unforwarded to Miami field office due to administrative lapses.
10. VICTIMOLOGY & 4 SURVIVAL RED FLAGS (BTAM): Honoring the selfless heroism of Aaron Feis and Scott Beigel; synthesizing 4 Critical Red Flags: (1) Intent Leakage; (2) Morbid Fixation; (3) Anchor Loss; (4) Tactical Preparation.

⏱ TIMESTAMPS
00:00 Introduction & Advisory
00:23 Act 1 · The Interrogation Room and the 'Demon' Alibi
05:45 Act 2 · The Unblinking Lens and the Falling Mask
11:30 Act 3 · Psychological Decoding: Malingering vs. True Psychosis
17:15 Act 4 · Thirty-Four Life Sentences and the Verdict of Justice
23:00 Act 5 · The Wake-Up Call & 4 Red Flags for School Violence Prevention

⚠️ VIEWER DISCRETION & LEGAL ADVISORY
• Educational content produced strictly for criminological, behavioral, and school safety analysis; not a substitute for legal or psychiatric counsel.
• Grounded strictly in official judicial exhibits of Broward County Circuit Court, BSO interrogation footage, and Dr. Charles Scott's psychiatric evaluation. Does not promote or glorify violence.
• Animal avatars are stylized illustrations. Spoken dialogue represents evidentiary dramatization. Narrated with synthetic AI voices.

📚 OFFICIAL JUDICIAL SOURCES
• Broward County 17th Judicial Circuit Court — State of Florida v. Nikolas Jacob Cruz (Case No. 18-001958CF10A, 34 consecutive life terms)
• Broward Sheriff's Office (BSO) — Detective John Curcio Interrogation Video (Feb 14, 2018)
• Dr. Charles L. Scott, M.D. — Forensic Psychiatric Evaluation on Malingering
• Marjory Stoneman Douglas High School Public Safety Commission Report (400+ pages)
• DSM-5-TR Diagnostic Criteria for Malingering (Z76.5) & ASPD
• Gavin de Becker — 'The Gift of Fear' (Behavioral Threat Assessment)

🆘 CRISIS HOTLINES & RESOURCES
• 988 Suicide & Crisis Lifeline (USA): Dial 988 — https://988lifeline.org/
• Child Protective Services Hotline 111 (Vietnam, 24/7 Free) — http://tongdai111.vn/

#AmberEyes #TrueCrime #CriminalPsychology #NikolasCruz #ParklandShooting #Malingering #InterrogationTechniques #BTAM #ForensicPsychiatry #RedFlags #Documentary"""

DESC_JA = """第19話：『頭の中の悪魔』という仮面 — 精神疾患の偽装とカメラが暴いた真実 | 犯罪心理学：ニコラス・クルーズ事件（10の心理的指標＆4大レッドフラグ） | Amber eyes

2018年2月14日、フロリダ州パークランドのマージョリー・ストーンマン・ダグラス高校で、17名の尊い命を奪った痛ましい銃乱射事件が発生しました。逮捕されベテランのジョン・クルシオ刑事と対峙した19歳のニコラス・クルーズは、病棟着に身を包んで震えながら、頭の中の悪魔が「燃やせ、殺せ、破壊せよ」と命じたのだと囁きました。しかし、取調室に設置された監視カメラと熟練捜査官の行動テストによって、その欺瞞は完全に暴かれました。それは極刑を逃れるために冷徹に計算された「詐病（メリンガリング）」の演技だったのです。

本事件をAmber eyesが10の心理的・行動的指標を通じて徹底解剖します：
1. 社会的余波と法改正運動：全米に広がった生徒主導の「命のための行進」運動とフロリダ州死刑量刑基準の法改正（12対0から8対4へ）。
2. 被害者の物体化と共感性の欠落：悪名を轟かせる目的のために犠牲者を単なる障害物や統計上の数字として冷酷に扱った歪んだ心理。
3. 心理的区画化と家庭的錨の喪失：取調室で実弟と対面した際にのみ泣き崩れる作為的二面性と、養母リンダの急死による最後の抑止力の崩壊。
4. 病的自己愛の崩壊と自己憐憫：法廷でうつむき続けた空虚な演技と、34回の終身刑宣告による完全な忘却と孤立。
5. 道徳的中和技術と詐病工作：悪魔のせいにすることで良心の呵責を麻痺させようとしたが、日常行動での矛盾を突かれ自壊。
6. 心理的トリガーと行動破綻点：学校からの退学処分と養母の死去が重なり、長年蓄積された復讐心が臨界点に到達。
7. シグネチャーと犯行手口（MO）：火災報知器を用いた計画的手口と、世界に名を残すため事前に犯行予告動画を撮影した名声欲（シグネチャー）。
8. 4段階のエスカレーション軌道：小動物虐待 -> 学校暴力とネット威嚇 -> 合法銃器購入と弾薬備蓄 -> 無差別襲撃の実行。
9. 組織的盲点とハロー効果の反転：30回以上に及ぶ事前通報の放置と、FBI受付窓口における情報共有の致命的断絶。
10. 被害者の尊厳と4大生存レッドフラグ（BTAM）：生徒を守り殉職した教員の勇気と、4大危険兆候（意図の漏洩、異常な執着、錨の喪失、戦術的準備）。

⏱ タイムスタンプ
00:00 導入および視聴上の注意
00:23 第1幕 · 密室の取調室と「悪魔」という虚飾の弁解
05:45 第2幕 · 瞬きしない監視レンズと剥ぎ取られた仮面
11:30 第3幕 · 心理構造の解剖：虚病（メリンガリング）vs 真性の精神病
17:15 第4幕 · 34回の終身刑と司法の厳粛なる審判
23:00 第5幕 · 生存の教訓と学校暴力防止の4大レッドフラグ

⚠️ 視聴上の注意および免責事項
• 犯罪心理学および学校安全研究を目的とした教育コンテンツであり、医学的・法的助言に代わるものではありません。
• ブロワード郡巡回裁判所の公判記録、捜査調書、精神鑑定証言に基づき構成されています。
• 登場する動物アバターは擬人化表現です。AI合成音声によりナレーションが生成されています。

📚 公式参照記録
• フロリダ州第17司法巡回裁判所 — State of Florida v. Nikolas Jacob Cruz（事件番号 18-001958CF10A）
• ブロワード郡保安官事務所（BSO） — ジョン・クルシオ刑事取調映像記録
• チャールズ・スコット医学博士 — 詐病精神鑑定報告書
• マージョリー・ストーンマン・ダグラス高校公共安全委員会報告書
• DSM-5-TR 詐病（Z76.5）および反社会性パーソナリティ障害診断基準
• 全米危機支援ホットライン: 988 — https://988lifeline.org/

#AmberEyes #犯罪心理学 #プロファイリング #ニコラスクルーズ #パークランド高校銃乱射事件 #取調室の心理戦 #詐病 #実話事件 #レッドフラグ"""

DESC_KO = """제19화: '머릿속의 악마'라는 가면 — 정신질환 위장과 카메라가 밝혀낸 진실 | 범죄심리학: 니콜라스 크루즈 사건 (10대 심리 지표 & 4대 생존 레드플래그) | Amber eyes

2018년 2월 14일, 플로리다주 파클랜드의 마조리 스톤맨 더글러스 고등학교에서 17명의 무고한 목숨을 앗아간 충격적인 총기 난사 참극이 일어났습니다. 체포된 후 베테랑 존 커시오 수사관과 마주 앉은 19세의 니콜라스 크루즈는 환자복을 입고 몸을 떨며 머릿속 악마가 "불태우고, 죽이고, 파괴하라"고 명령했다고 속삭였습니다. 하지만 밀폐된 취조실의 무인 감시 카메라와 노련한 수사관의 날카로운 행동 검증은 그 거짓말을 완전히 해체했습니다. 사형을 피하기 위해 치밀하게 연기된 '꾀병(메링거링)'의 민낯이 드러난 것입니다.

본 사건을 Amber eyes가 10대 핵심 심리·행동 지표를 통해 심층 해부합니다:
1. 사회적 충격과 사법 개혁 운동: 청소년 주도의 '우리의 생명을 위한 행진' 운동 촉발 및 플로리다주 사형 양형 기준 개정(12-0에서 8-4로 완화).
2. 피해자의 사물화와 공감 결여: 악명을 떨치겠다는 이기적 목적을 위해 동급생과 교사들을 단순한 장애물과 숫자로 취급한 잔혹한 심리.
3. 심리적 구획화와 가정 닻의 붕괴: 취조실에서 친동생을 만났을 때만 눈물을 흘리는 이중성과, 양모 린다의 급사로 인한 통제 기제의 완전 붕괴.
4. 병적 자기애의 붕괴와 자기연민: 법정에서 고개를 떨군 채 유지한 허식의 가면과 34회 연속 종신형 선고로 인한 영구적 고립.
5. 도덕적 중화 기술과 꾀병 위장: 악마 탓을 하며 양심의 소리를 무력화하려 했으나, 일상 행동에서의 논리적 모순이 드러나며 붕괴.
6. 심리적 트리거와 행동 파탄점: 학교 퇴학 처분과 양모의 사망이 겹치며 수년간 축적된 복수 망상이 통제 불능 상태로 폭발.
7. 시그니처 vs 범행 수법(MO): 화재경보기를 악용한 계획적 수법과, 전 세계에 이름을 알리기 위해 범행 예고 영상을 직접 촬영한 시그니처.
8. 4단계 행동 에스컬레이션: 소동물 학대 -> 교내 폭력 및 온라인 협박 -> 합법적 총기 구매 및 탄약 비축 -> 무차별 난사 실행.
9. 제도적 맹점과 후광 효과의 반전: 30회 이상의 사전 위험 신고 묵살 및 FBI 제보 핫라인 정보의 관료적 전달 누락.
10. 피해자 존엄성과 4대 생존 레드플래그(BTAM): 목숨 바쳐 학생을 구한 교사들의 숭고한 용기와 4대 행동 경고 신호(의도 누출, 병적 집착, 닻 상실, 전술 준비).

⏱ 타임스탬프
00:00 인트로 및 안내
00:23 막 1 · 밀폐된 취조실과 '악마'라는 거짓된 변명
05:45 막 2 · 깜빡이지 않는 감시 렌즈와 벗겨진 가면
11:30 막 3 · 심리 구조의 해부: 꾀병(메링거링) vs 진성 정신증
17:15 막 4 · 34회의 종신형과 사법정의의 준엄한 심판
23:00 막 5 · 생존의 교훈과 학교폭력 예방을 위한 4대 레드플래그

⚠️ 법적 고지 및 시청 안내
• 범죄심리학 및 학교 안전 교육을 목적으로 제작되었으며, 의학적·법적 조언을 대신하지 않습니다.
• 브로워드 카운티 순회법원 공판 기록, 수사관 신문조서, 정신감정 증언 등 공식 기록에 근거합니다.
• 등장하는 동물 아바타는 상징적 캐릭터입니다. 음성은 인공지능(AI) 도구로 생성되었습니다.

📚 공식 사법 기록 및 출처
• 플로리다주 제17사법순회법원 — State of Florida v. Nikolas Jacob Cruz (사건번호 18-001958CF10A)
• 브로워드 카운티 보안관실 (BSO) — 존 커시오 수사관 취조 영상 기록
• 찰스 스콧 박사 — 꾀병(메링거링) 법정 감정 보고서
• 마조리 스톤맨 더글러스 고교 공공안전위원회 보고서
• 미국정신의학회 DSM-5-TR 꾀병(Z76.5) 및 반사회성 성격장애 진단 기준
• 미국 위기 지원 핫라인: 988 — https://988lifeline.org/

#AmberEyes #범죄심리학 #프로파일링 #니콜라스크루즈 #파클랜드총기난사 #취조실심리전 #메링거링 #실화사건 #레드플래그"""

# ==============================================================================
# GHI FILE VÀ KIỂM TRA ĐỘ DÀI
# ==============================================================================

files_to_write = [
    # Tiếng Việt
    (ROOT / "02_SAN_XUAT" / "Tap19" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap19" / "xuat_ban" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap19" / "nguon_mo_ta.txt", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap19" / "nguon_tham_khao.md", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap19" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),

    # Tiếng Anh
    (ROOT / "02_SAN_XUAT" / "Tap19_EN" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap19_EN" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap19_EN" / "xuat_ban" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap19_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap19_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap19_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap19_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),

    # Tiếng Nhật
    (ROOT / "02_SAN_XUAT" / "Tap19_JA" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap19_JA" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap19_JA" / "xuat_ban" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap19_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap19_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap19_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap19_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),

    # Tiếng Hàn
    (ROOT / "02_SAN_XUAT" / "Tap19_KO" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap19_KO" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap19_KO" / "xuat_ban" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap19_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap19_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap19_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap19_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
]

all_pass = True
print("================================================================")
print("TIẾN TRÌNH TẠO MÔ TẢ VÀ NGUỒN THAM KHẢO TẬP 19 (4 NGÔN NGỮ)")
print("================================================================")

for p, text in files_to_write:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.strip() + "\n", encoding="utf-8")
    char_len = len(text.strip())
    is_desc = p.name in ["mo_ta.txt", "description.txt"]
    if is_desc:
        status = "PASS" if char_len <= 5000 else "FAIL (> 5000)"
        if char_len > 5000:
            all_pass = False
        print(f"[{status}] Ghi file mô tả: {p.relative_to(ROOT)} -> {char_len:,} ký tự")
    else:
        print(f"[DONE] Ghi file nguồn: {p.relative_to(ROOT)} -> {char_len:,} ký tự")

print("================================================================")
print(f"KẾT QUẢ: {'ALL GREEN - ĐẠT TIÊU CHUẨN <= 5000 KÝ TỰ' if all_pass else 'FAILED'}")
print("================================================================")
