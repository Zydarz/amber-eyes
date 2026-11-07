# -*- coding: utf-8 -*-
"""Generate comprehensive descriptions and source files for Episode 20 across 4 languages.
Ensures full coverage of 10 Psychological Indicators (§A2c) and strictly <= 5000 characters.
"""

import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# 1. SOURCES DATA
# ==============================================================================

SOURCES_VI = """▸ Hồ sơ tòa án & Phán quyết tư pháp chính thức:
• [1] Tòa Thượng thẩm Hạt Bibb (Macon, Georgia) — Bản án xét xử State of Georgia v. Stephen Mark McDaniel (Case No. 12-CR-0062, Thẩm phán Howard Simms; án chung thân tối thiểu 30 năm): https://www.maconbibb.us/
• [2] Văn phòng Biện lý Hạt Bibb (District Attorney) — Hồ sơ thỏa thuận nhận tội và bản thừa nhận chi tiết của bị cáo (tháng 4/2014): https://da.maconbibb.us/
• [3] Wikipedia — Vụ án mạng Lauren Giddings và diễn biến tư pháp: https://en.wikipedia.org/wiki/Murder_of_Lauren_Giddings

▸ Cơ quan điều tra, tư liệu truyền hình & Báo chí hiện trường:
• [4] Sở Cảnh sát Macon & Cục Điều tra Georgia (GBI) — Báo cáo khám nghiệm hiện trường, giám định chìa khóa vạn năng và phân tích dấu vết kỹ thuật số: https://gbi.georgia.gov/
• [5] WGXA News — Bản ghi hình trực tiếp cuộc phỏng vấn định mệnh ngày 30/06/2011 (khoảnh khắc sụp đổ tâm lý và phản ứng bất động): https://wgxa.tv/
• [6] CBS News / 48 Hours — Phim tài liệu điều tra 'The Lauren Giddings Murder': https://www.cbsnews.com/news/georgia-man-pleads-guilty-to-strangling-dismembering-woman/
• [7] The Telegraph (Macon) — Kho lưu trữ tài liệu điều tra, phản ứng dư luận và lời chứng của bạn bè Trường Luật Mercer: https://www.macon.com/

▸ Khoa học hành vi & Tâm lý học tội phạm:
• [8] Gavin de Becker — Tác phẩm 'The Gift of Fear' (Nhận diện nguy cơ rình rập và lắng nghe trực giác sinh tồn): https://gavindebecker.com/resources/the_gift_of_fear/
• [9] FBI Behavioral Analysis Unit (BAU) — Chuyên khảo về Kẻ rình rập săn mồi (Predatory Stalking) và Thị dâm săn mồi (Predatory Voyeurism).
• [10] Phân tích thần kinh học về Phản ứng đóng băng (Freeze Response / Tonic Immobility) và Vi biểu cảm khi đối mặt cú sốc bại lộ tội lỗi."""

SOURCES_EN = """▸ Official Judicial Records & Court Transcripts:
• [1] Bibb County Superior Court (Macon, Georgia) — State of Georgia v. Stephen Mark McDaniel (Case No. 12-CR-0062, Judge Howard Simms; Life sentence with 30-year mandatory minimum): https://www.maconbibb.us/
• [2] Bibb County District Attorney's Office — Negotiated Plea Agreement and Factual Proffer (April 2014): https://da.maconbibb.us/
• [3] Wikipedia — Murder of Lauren Giddings & Judicial Disposition: https://en.wikipedia.org/wiki/Murder_of_Lauren_Giddings

▸ Investigative Records, Broadcast Archives & Journalism:
• [4] Macon Police Department & Georgia Bureau of Investigation (GBI) — Crime scene reports, master key toolmark analysis, and digital forensics: https://gbi.georgia.gov/
• [5] WGXA News — Live broadcast footage of June 30, 2011 interview (the on-camera breakdown and cognitive freeze): https://wgxa.tv/
• [6] CBS News / 48 Hours — Investigative documentary on the Lauren Giddings murder: https://www.cbsnews.com/news/georgia-man-pleads-guilty-to-strangling-dismembering-woman/
• [7] The Telegraph (Macon) — Archival coverage of the Mercer Law School community impact and investigation: https://www.macon.com/

▸ Behavioral Sciences & Forensic Psychology:
• [8] Gavin de Becker — 'The Gift of Fear: Survival Signals That Protect Us from Violence': https://gavindebecker.com/resources/the_gift_of_fear/
• [9] FBI Behavioral Analysis Unit (BAU) — Research monographs on Predatory Stalking, Voyeurism, and Covert Narcissism.
• [10] Neurobiological research on the Freeze Response (Tonic Immobility) and micro-expression leakage during acute cognitive shock."""

SOURCES_JA = """▸ 公式司法記録および法廷文書:
• [1] ジョージア州ビブ郡上級裁判所 — ジョージア州対スティーブン・マーク・マクダニエル刑事判決（事件番号: 12-CR-0062、ハワード・シムズ裁判長、仮釈放資格まで最低30年の終身刑）: https://www.maconbibb.us/
• [2] ビブ郡地方検察局 — 有罪答弁司法取引合意書および事実認定自白調書（2014年4月）: https://da.maconbibb.us/
• [3] ウィキペディア — ローレン・ギディングス殺害事件および司法手続き記録: https://en.wikipedia.org/wiki/Murder_of_Lauren_Giddings

▸ 捜査機関資料、報道映像アーカイブおよび報道記事:
• [4] メーコン警察局およびジョージア州捜査局（GBI） — 現場鑑識報告書、マスターキー工具痕鑑定およびデジタルフォレンジック記録: https://gbi.georgia.gov/
• [5] WGXAニュース — 2011年6月30日生中継インタビュー映像（生放送中の崩壊劇と凍結反応）: https://wgxa.tv/
• [6] CBSニュース / 48アワーズ — ローレン・ギディングス事件特別捜査ドキュメンタリー: https://www.cbsnews.com/news/georgia-man-pleads-guilty-to-strangling-dismembering-woman/
• [7] ザ・テレグラフ（メーコン） — マーサー大学ロースクールの証言と事件報道アーカイブ: https://www.macon.com/

▸ 行動科学および犯罪心理学の専門文献:
• [8] ギャビン・ド・ベッカー — 『ギフト・オブ・フィアー：危険を察知する生存の知恵』: https://gavindebecker.com/resources/the_gift_of_fear/
• [9] FBI行動分析課（BAU） — 捕食的ストーキング、覗き見行動（捕食的観察行動）および隠れ自己愛性パーソナリティに関する研究文献。
• [10] 神経生物学における凍結反応（緊張病性不活動）および認知的過負荷時における微表情の漏出に関する臨床研究。"""

SOURCES_KO = """▸ 공식 사법 기록 및 법원 판결 공문서:
• [1] 조지아주 비브 카운티 상급법원 — 조지아주 대 Stephen Mark McDaniel 형사재판 확정 판결 (사건번호: 12-CR-0062, Howard Simms 판사, 최소 30년 복역 조건부 종신형): https://www.maconbibb.us/
• [2] 비브 카운티 지방검찰청 — 유죄 협상 합의서 및 사실 인정 자백 공소 기록 (2014년 4월): https://da.maconbibb.us/
• [3] 위키백과 — Lauren Giddings 살인 사건 및 사법 절차 상세 아카이브: https://en.wikipedia.org/wiki/Murder_of_Lauren_Giddings

▸ 수사기관 공문, 방송 보도 영상 및 심층 르포:
• [4] 메이컨 경찰국 및 조지아 수사국(GBI) — 범죄 현장 감식 보고서, 마스터키 공구 흔적 분석 및 디지털 포렌식 기록: https://gbi.georgia.gov/
• [5] WGXA 뉴스 — 2011년 6월 30일 생방송 인터뷰 영상 원본 (카메라 앞 심리적 붕괴와 동결 반응 포착): https://wgxa.tv/
• [6] CBS 뉴스 / 48 Hours — Lauren Giddings 사건 심층 다큐멘터리: https://www.cbsnews.com/news/georgia-man-pleads-guilty-to-strangling-dismembering-woman/
• [7] 더 텔레그래프(메이컨) — 머서 로스쿨 동기들의 증언 및 사건 종합 탐사 보도: https://www.macon.com/

▸ 행동과학 및 범죄심리학 전문 연구:
• [8] Gavin de Becker — 저서 'The Gift of Fear' (인간의 생존 직관과 스토킹 조기 경보 체계): https://gavindebecker.com/resources/the_gift_of_fear/
• [9] FBI 행동분석팀(BAU) — 포식적 스토킹, 관음증적 침해 행동 및 내현적 자기애성 인격에 관한 연구 보고서.
• [10] 급격한 범행 탄로 시 발생하는 생리적 동결 반응(Freeze Response / Tonic Immobility)과 미세 표정 신경생물학 연구."""


# ==============================================================================
# 2. FULL DESCRIPTIONS (STRICTLY <= 5000 CHARACTERS)
# ==============================================================================

DESC_VI = """Khoảnh Khắc Sụp Đổ Trước Ống Kính — Ám Ảnh Rình Rập & Phản Ứng Đóng Băng Kỳ Dị (Hồ Sơ Stephen McDaniel) | Tâm lý học tội phạm | Amber eyes

Cuối tháng 6/2011, Trường Luật Mercer (Georgia) rúng động khi Lauren Giddings, 27 tuổi, nữ cử nhân luật ưu tú, mất tích bí ẩn tại chung cư Barristers Hall không dấu vết cạy phá. Giữa lúc truyền thông đổ dồn về hiện trường, người hàng xóm đối diện và là bạn cùng lớp — Stephen McDaniel (25 tuổi) — đã chủ động bước ra trước ống kính đài truyền hình WGXA, đóng vai người bạn tận tụy đầy đồng cảm.

Ngay trong lúc ghi hình trực tiếp, phóng viên bất ngờ nhận tin báo: một phát hiện đau lòng vừa được tìm thấy ngoài chung cư. Ống kính bắt trọn khoảnh khắc McDaniel biến sắc hoàn toàn, lặp từ trong hoảng loạn và khuỵu xuống lề đường. Tại phòng thẩm vấn, hắn ngồi bất động như tượng đá suốt nhiều giờ — phản ứng đóng băng (Freeze Response) kỳ dị nhằm triệt tiêu mọi vi biểu cảm trước camera.

Hồ sơ Stephen McDaniel được Amber eyes giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi (§A2c):
1. DƯ CHẤN XÃ HỘI & HOANG TƯỞNG TẬP THỂ: Phá vỡ an toàn tại Trường Luật Mercer; sinh viên khóa chặt cửa trong đêm hè; thúc đẩy cải cách toàn quốc về quản lý chìa khóa vạn năng và nhân sự chung cư sinh viên.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem Lauren như 'đạo cụ' phục vụ khoái cảm ái kỷ; khuyết tật thấu cảm cảm xúc; thị dâm săn mồi (Predatory Voyeurism) quay lén qua cửa sổ để tìm quyền lực ngầm.
3. NGHỊCH LÝ CHIA NGĂN NHẬN THỨC (COMPARTMENTALIZATION): Khóa chặt hai thế giới: sinh viên luật cần mẫn ban ngày và kẻ rình rập săn mồi ban đêm; cú sốc niềm tin tan vỡ của bạn bè và gia đình.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Đối lập giữa ăn năn chân chính và tự thương hại bệnh lý (Pathological Self-Pity); McDaniel chỉ tiếc tương lai cá nhân tan tành; nhận tội để tránh án tử hình.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC: Đóng vai nạn nhân bị hắt hủi, đổ lỗi cho sự cự tuyệt của phụ nữ, tự cho mình quyền trừng phạt người từ chối mình.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY (TRIGGER): Lauren tốt nghiệp chuẩn bị dọn về Atlanta; thùng đồ đóng gói báo trước mất quyền kiểm soát; tổn thương ái kỷ dữ dội kích hoạt hành vi đột nhập.
7. CHỮ KÝ SIGNATURE VS. THỦ ĐOẠN MO: MO (trộm chìa vạn năng, đột nhập rạng sáng khi nạn nhân ngủ) toan tính thực dụng; Chữ ký (Signature) bất biến là rình rập quay lén nhiều tháng và giữ chiến lợi phẩm số.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Dung nạp kích thích: Nhìn trộm qua cửa sổ -> tìm cách bẻ khóa -> quay video đêm qua ban công -> dùng chìa vạn năng đột nhập khi nạn nhân ngủ.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc sinh viên trường luật nhút nhát ('bạn lập dị vô hại') tạo nên thiên kiến bình thường hóa (Normalcy Bias) che mắt cộng đồng xung quanh.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ SINH TỒN: Tôn vinh phẩm giá và tài năng của Lauren Giddings; 4 cảnh báo đỏ (The Gift of Fear): (1) Trùng hợp quá mức và xâm phạm không gian riêng; (2) Tò mò bệnh hoạn về đời tư; (3) Dấu vết bất thường quanh nơi ở và ổ khóa; (4) Cảm xúc thất thường và hận thù phụ nữ ngầm.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Cuộc phỏng vấn định mệnh & tin báo bất ngờ từ thùng rác
05:30 Hồi 2 · Bức tượng đá trong phòng hỏi cung & cú sốc nhận thức
10:30 Hồi 3 · Giải mã tâm lý: Kẻ rình rập ngầm & phản ứng đóng băng kỳ dị
16:00 Hồi 4 · Phán quyết chung thân & sự trừng phạt của công lý
21:30 Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa kẻ rình rập ngầm

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai Tòa Thượng thẩm Hạt Bibb (Georgia) và báo cáo điều tra Cảnh sát Macon / FBI. Kênh không bôi nhọ hay tôn vinh bất kỳ cá nhân nào.
• Nhân vật dẫn chuyện là hình tượng nghệ thuật. Lời thoại phục dựng dựa trên hồ sơ tư pháp.
• Giọng đọc, hình ảnh và âm thanh được hỗ trợ bởi công nghệ AI.

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• Bản án State of Georgia v. Stephen Mark McDaniel (Thẩm phán Howard Simms, 2014) — Tòa Thượng thẩm Hạt Bibb
• Báo cáo khám nghiệm hiện trường và kỹ thuật số Macon Police Department & GBI
• Băng ghi hình phỏng vấn trực tiếp đài truyền hình WGXA News (30/06/2011)
• Khung phân tích Predatory Stalking, Voyeurism & The Gift of Fear (Gavin de Becker)

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ & BẢO VỆ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng phòng chống bạo lực gia đình: 1900 969 680

#AmberEyes #TrueCrime #TamLyToiPham #StephenMcDaniel #LaurenGiddings #FreezeResponse #PredatoryStalker #MercerLaw #10ChiDauTamLy #CanhBaoDo #TheGiftOfFear #HoSoToiPham"""

DESC_EN = """Stephen McDaniel Case: The On-Camera Collapse & The Eerie Freeze Response | Criminal Psychology Documentary | Amber eyes

In late June 2011, dread gripped Mercer University School of Law in Macon, Georgia. Lauren Giddings, 27, a gifted law graduate preparing for the bar exam, vanished from her Barristers Hall apartment with zero signs of forced entry. As news of her disappearance broke, across-the-hall classmate Stephen McDaniel (25) stepped before WGXA news cameras, staging the role of a devoted, concerned friend.

Yet while the live broadcast rolled, the reporter received breaking news: human remains had just been discovered outside the building. The camera captured an unforgettable collapse: McDaniel's face went blank, his voice rasped in panic, and he crumpled onto the curb. In police interrogation, he sat motionless for hours like a stone statue — an eerie artificial manifestation of the biological Freeze Response (Tonic Immobility) deployed to suppress micro-expressions.

Amber eyes dissects this case through our 10-Indicator Behavioral Ecosystem (§A2c):
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: Shattered safety across Mercer Law; students deadbolted doors in summer heat; spurred nationwide student housing reforms regarding master key custody and access audits.
2. OBJECTIFICATION & DEHUMANIZATION: Lauren was treated as an object for narcissistic supply; affective empathy deficit; predatory voyeurism through window filming seeking covert power.
3. COGNITIVE COMPARTMENTALIZATION: Rigidly partitioned the studious bar candidate by day from the nocturnal stalker by night; trust collapse experienced by classmates and family.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: Remorse vs. pathological self-pity; McDaniel's tears mourned the ruin of his own grandiosity; his guilty plea was a calculation to escape execution.
5. TECHNIQUES OF NEUTRALIZATION: Moral disengagement framing himself as a misunderstood outsider, blaming female rejection, and rationalizing his entitlement to punish.
6. PRECIPITATING STRESSOR & TIPPING POINT: Lauren's graduation and move to Atlanta; packing boxes signaled the end of his secret surveillance; acute narcissistic injury triggered lethal intrusion.
7. PSYCHOLOGICAL SIGNATURE VS. MO: MO (stealing master passkey, predawn entry, dumpster disposal) evolved pragmatically; immutable Signature was months of voyeuristic recording and digital trophy archiving.
8. FANTASY ESCALATION TRAJECTORY: Stimulus tolerance buildup: Peeping -> lock-picking queries -> nocturnal balcony video filming -> master key midnight residential breach.
9. HALO EFFECT & SOCIAL BLIND SPOTS: Awkward student persona ('harmless nerdy peer') established a normalcy bias that blinded classmates to his predatory menace.
10. VICTIMOLOGY & 4 SURVIVAL RED FLAGS: Honoring Lauren Giddings' bright life; 4 classic survival red flags (The Gift of Fear): (1) Manufactured coincidence & spatial intrusion; (2) Boundary-crossing curiosity; (3) Lock tampering around dwelling; (4) Misogyny beneath awkwardness.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Disclaimer
00:23 Act 1 · The Fateful Interview & The Unexpected Discovery
05:30 Act 2 · The Stone Statue in the Interrogation Room & Cognitive Shock
10:30 Act 3 · Psychological Dissection: The Predatory Stalker & Tonic Immobility
16:00 Act 4 · The Life Verdict & Retribution of Justice
21:30 Act 5 · Awakening Lessons & 4 Red Flags Against Covert Stalking

⚠️ LEGAL & SAFETY DISCLAIMER
• Educational and historical documentary on criminal psychology; does not replace medical or legal advice.
• Derived from public transcripts of the Bibb County Superior Court and verified Macon Police / FBI records.
• Animal narrator avatars are artistic motifs. Narration, visuals, and audio are AI-assisted.

📚 VERIFIED OFFICIAL SOURCES
• State of Georgia v. Stephen Mark McDaniel (Case No. 12-CR-0062, Judge Howard Simms, 2014) — Bibb County Superior Court
• Macon Police Department & Georgia Bureau of Investigation (GBI) Forensic Reports
• WGXA News Live Television Broadcast Archive (June 30, 2011)
• Analytical Frameworks: Predatory Stalking, Voyeurism & The Gift of Fear (Gavin de Becker)

🆘 CRISIS HOTLINES & SUPPORT
• 988 Suicide & Crisis Lifeline (US/Canada, toll-free 24/7): Dial 988 — https://988lifeline.org/
• National Domestic Violence Hotline: 1-800-799-SAFE (7233) — https://www.thehotline.org/
• National Sexual Assault Hotline (RAINN): 1-800-656-4673 — https://www.rainn.org/

#AmberEyes #TrueCrime #CriminalPsychology #StephenMcDaniel #LaurenGiddings #FreezeResponse #PredatoryStalker #MercerLaw #10PsychologicalMarkers #SurvivalRedFlags #TheGiftOfFear #CaseDossier"""

DESC_JA = """スティーブン・マクダニエル事件：生中継の崩壊劇と取調室の奇怪な凍結反応 | 犯罪心理学ドキュメンタリー | Amber eyes

2011年6月下旬、ジョージア州メーコンのマーサー大学ロースクールのキャンパスは、不気味で重苦しい不安に包まれていました。優秀な成績で卒業し、司法試験の準備に励んでいた27歳の女性ローレン・ギディングスが突如として不可解な失踪を遂げたのです。彼女が暮らしていた集合住宅バリスターズ・ホールの部屋には侵入の形跡が一切ありませんでした。失踪事件が大きく報じられる中、真向かいの部屋に住むロースクールの同期生、25歳のスティーブン・マクダニエルが自ら地元テレビ局WGXAのカメラの前に進み出て、友人の身を案じる誠実な隣人を演じました。

しかし生中継の最中、女性記者は警察からの速報を受け取ります。アパート敷地内のゴミ収集容器から遺留品が発見されたという一報でした。カメラはその瞬間、マクダニエルの顔から血の気が完全に引き、動揺して路肩にへたり込む生々しい心理的崩壊を捉えました。さらに警察の取調室で、彼は何時間もの間、まるで冷たい石像のように微動だにせず座り続けました。これは微表情を抹消し罪悪感を隠蔽しようとする生理的凍結反応（フリーズ・レスポンス）の特異な発露でした。

Amber eyesは、本事件を「10の心理・行動指標エコシステム（§A2c）」から深層解剖します：
1. 社会的余波と集団的パラノイア: マーサー大学の学生コミュニティを震撼させ、真夏の夜に学生たちが扉を固く閉ざして疑心暗鬼に陥る恐怖を生み出し、全米の学生住宅におけるマスターキー管理基準の法制化を促進。
2. 被害者の客体化と脱人間化: ローレンを意思ある人間としてではなく、自らの自己愛を満たすための「道具」として見なす認識; 共感能力の致命的欠如と、覗き見によって権力感情を得る捕食的観察行動。
3. 認知的区分化（コンパートメント化）の逆説: 勤勉な法学生としての昼の顔と、夜の捕食的ストーカーとしての暗黒面を完全に遮断; 真実を知った友人や遺族が味わった深い裏切りの衝撃。
4. 自己愛性崩壊と病理的自己憐憫: 真の反省ではなく、自らの輝かしい知性と未来が瓦解したことへの惨めな自己憐憫; 死刑を免れるために計算された保身の有罪答弁。
5. 自己正当化と道徳の中和技術: 社会に拒絶された不遇の被害者像を自作自演し、女性の拒絶を身勝手に責め立てて犯行を正当化。
6. 心理的引き金と限界点（トリガー）: ローレンが卒業しアトランタへ引っ越す準備を進めていた現実が、秘密の監視権を永久に奪われる恐怖を刺激し、自己愛性怒涛と凶行を誘発。
7. 署名（SIGNATURE）対 手口（MO）: 合鍵を用いた未明の侵入手口（MO）に対し、数ヶ月にわたる盗撮とデジタル記録の蓄積という不変の心理的署名（Signature）。
8. 妄想のエスカレーション軌跡: 覗き見 -> 鍵開け技術の検索 -> ベランダからの夜間動画撮影 -> 合鍵による就寝中の侵入へのエスカレーション。
9. 後光効果（ハロー効果）と社会的盲点: 「変わり者だが無害なオタク学生」という正常性バイアスが周囲の目を曇らせ、危険性を察知できない社会的盲点を形成。
10. 被害者学と4つの生存レッドフラッグ: ローレン・ギディングスの高潔な魂を追悼; 生存のための4つの警報（The Gift of Fear）: (1) 偶然の一致の連発と私的空間への侵犯; (2) 交友関係への執拗な詮索; (3) 居室周囲の不審な痕跡と鍵の異変; (4) 内気な態度の裏に潜む女性蔑視。

⏱ タイムスタンプ
00:00 イントロ＆注意事項
00:23 第1幕 · 運命の生中継インタビューと予期せぬ衝撃の一報
05:30 第2幕 · 取調室の石像と認知的ショックの深層
10:30 第3幕 · 深層心理の解剖：観察型ストーカーと凍結反応の力学
16:00 第4幕 · 終身刑の判決と司法の厳正なる断罪
21:30 第5幕 · 覚醒の教訓と捕食的ストーカーを防ぐ4つの危険兆候

⚠️ 免責事項および安全基準
• 犯罪心理学に関する教育・歴史的ドキュメンタリーであり、専門的な法的・医学的助言に代わるものではありません。
• ビブ郡上級裁判所の公開司法記録および捜査当局の公式資料に基づいています。
• 登場する動物キャラクターは芸術的モチーフです。音声・画像にはAI技術を活用しています。

📚 公式参考文献一覧
• ジョージア州対スティーブン・マクダニエル事件判決（ハワード・シムズ裁判長、2014年） — ビブ郡上級裁判所
• メーコン警察局およびジョージア州捜査局（GBI）鑑識報告書
• WGXAニュース 生中継取材アーカイブ（2011年6月30日）
• 行動科学理論：捕食的ストーキング、覗き見行動および『ギフト・オブ・フィアー』（ギャビン・ド・ベッカー）

🆘 緊急相談窓口・支援ホットライン
• こころの健康相談統一ダイヤル: 0570-064-556
• よりそいホットライン: 0120-279-338（24時間無料通話）
• 性犯罪・性暴力被害者のためのワンストップ支援センター: #8891
• 警察相談専用電話: #9110

#AmberEyes #TrueCrime #犯罪心理学 #スティーブンマクダニエル #ローレンギディングス #フリーズレスポンス #ストーカー対策 #10の心理指標 #レッドフラッグ #事件記録"""

DESC_KO = """Stephen McDaniel 사건: 생방송 카메라 앞의 붕괴와 취조실의 기이한 동결 반응 | 범죄심리학 다큐멘터리 | Amber eyes

2011년 6월 말, 조지아주 메이컨에 위치한 머서대학교 로스쿨 캠퍼스는 음산한 긴장감에 휩싸였습니다. 우수한 성적으로 졸업하고 변호사 시험을 준비하던 스물일곱 살의 Lauren Giddings가 흔적도 없이 사라졌습니다. 그녀가 살던 Barristers Hall 아파트 문에는 침입 흔적이 전혀 없었습니다. 실종 소식이 전국을 뒤흔들자, 맞은편 방에 살던 로스쿨 동기 Stephen McDaniel(25세)이 WGXA 방송 카메라 앞에 자청하여 나서서 사려 깊은 친구를 연기했습니다.

그러나 생방송 인터뷰 도중 기자가 경찰로부터 긴급 속보를 전달받았습니다. 아파트 외부 대형 쓰레기통에서 비극적인 유류 흔적이 발견되었다는 소식이었습니다. 방송 카메라는 McDaniel의 안색이 하얗게 질리며 다리가 풀려 길가에 주저앉는 심리적 방어선의 붕괴를 고스란히 포착했습니다. 이후 경찰 취조실에서 그는 몇 시간 동안 석상처럼 미동도 없이 굳어 앉아 있었는데, 이는 미세 표정을 지우기 위해 신체를 마비시킨 기이한 동결 반응(Freeze Response)이었습니다.

Amber eyes는 본 사건을 10대 심리·행동 분석 생태계(§A2c)로 심층 해부합니다:
1. 사회적 충격과 집단적 공포: 머서 로스쿨 커뮤니티의 일상적 안전을 파괴하고 한여름 밤 문을 걸어 잠그게 만든 집단 공포; 미국 전역의 학생 주거 시설 마스터키 관리 및 인력 검증 시스템 개혁 촉발.
2. 피해자의 도구화 및 비인간화: Lauren을 독립된 인격체가 아닌 자기애적 만족을 위한 도구로 취급; 정서적 공감 결여와 관음적 관찰을 통한 왜곡된 권력감 획득.
3. 인지적 격실화(구획화)의 역설: 주간의 성실한 법학도와 야간의 포식적 스토커라는 두 자아를 철저히 분리; 진실을 마주한 동기들과 유족들의 뼈아픈 배신감.
4. 자기애성 붕괴와 병리적 자기연민: 진정한 참회가 아닌 자신의 지적 명성과 미래가 파멸한 것에 대한 비열한 슬픔; 사형을 피하기 위한 유죄 협상.
5. 도덕적 중화 기술: 소외된 피해자 행세를 하며 여성의 거절을 비난하고 범행 권리를 스스로 부여하는 합리화.
6. 심리적 방아쇠와 임계점(트리거): Lauren의 애틀랜타 이주 준비가 은밀한 관찰 기회의 영구 박탈을 의미하자 폭발한 자기애적 분노.
7. 시그니처 대 MO: 마스터키 야간 침입이라는 수단(MO)과 수개월간의 불법 촬영 및 디지털 기록 보관이라는 불변의 심리적 서명(Signature).
8. 망상의 에스컬레이션 궤적: 자극 역치 증가: 창문 훔쳐보기 -> 자물쇠 해체 검색 -> 베란다 야간 동영상 촬영 -> 마스터키 새벽 침입.
9. 후광 효과와 사회적 맹점: '괴짜지만 무해한 동기'라는 정상성 편향이 이웃들의 경계심을 무력화시킨 맹점.
10. 피해자학 및 4대 생존 위험 징후: Lauren Giddings의 빛나는 리더십과 따뜻한 영혼을 기림; 4대 생존 레드 플래그(The Gift of Fear): (1) 작위적 우연과 사적 영역 침범; (2) 교우·연애 관계에 대한 병적 집착; (3) 거처 주변의 미세한 침입 흔적과 열쇠 이상; (4) 내성적 외면 뒤에 숨겨진 여성 혐오.

⏱ 챕터 타임스탬프
00:00 인트로 및 안내
00:23 제1막 · 운명의 생방송 인터뷰와 쓰레기통의 비극적 발견
05:30 제2막 · 취조실의 석상과 인지적 충격의 실체
10:30 제3막 · 범죄 심리 해부: 포식적 스토커와 기이한 동결 반응
16:00 제4막 · 종신형 선고와 준엄한 사법적 단죄
21:30 제5막 · 각성의 교훈과 은밀한 스토킹을 막는 4대 위험 징후

⚠️ 법적 고지 및 안전 안내
• 본 영상은 범죄심리학 및 역사적 기록에 기반한 교육적 다큐멘터리이며 법적·의학적 조언을 대신하지 않습니다.
• 비브 카운티 상급법원의 공개 판결 및 메이컨 경찰국/GBI의 공식 수사 기록을 바탕으로 제작되었습니다.
• 등장하는 동물 캐릭터는 예술적 모티브이며, 음성과 시각 자료에는 AI 기술이 활용되었습니다.

📚 공식 참고 자료 목록
• 조지아주 대 Stephen Mark McDaniel 형사재판 판결 (Howard Simms 판사, 2014) — 비브 카운티 상급법원
• 메이컨 경찰국 및 조지아 수사국(GBI) 과학 수사 감식 보고서
• WGXA 뉴스 생방송 취재 영상 아카이브 (2011년 6월 30일)
• 행동과학 이론: 포식적 스토킹, 관음증 및 《The Gift of Fear》(Gavin de Becker)

🆘 위기 상담 전화 및 지원 안내
• 한국 생명의 전화: 1588-9191 (24시간 상담)
• 정신건강위기상담전화: 1577-0199
• 여성긴급전화: 1366
• 경찰청 범죄 신고: 112

#AmberEyes #TrueCrime #범죄심리학 #StephenMcDaniel #LaurenGiddings #동결반응 #스토킹경보 #10대심리지표 #레드플래그 #TheGiftOfFear #사건파일"""


def main():
    print("=" * 70)
    print("GENERATING TAP 20 DESCRIPTIONS ACROSS 4 LANGUAGES (<= 5000 CHARS)")
    print("=" * 70)
    
    descs = {
        "VN": DESC_VI.strip(),
        "EN": DESC_EN.strip(),
        "JA": DESC_JA.strip(),
        "KO": DESC_KO.strip(),
    }
    
    sources = {
        "VN": SOURCES_VI.strip(),
        "EN": SOURCES_EN.strip(),
        "JA": SOURCES_JA.strip(),
        "KO": SOURCES_KO.strip(),
    }
    
    # 1. Check lengths
    all_ok = True
    for lang, text in descs.items():
        char_len = len(text)
        print(f"[{lang}] Description character length: {char_len} / 5000")
        if char_len > 5000:
            print(f"ERROR: {lang} description exceeds 5000 characters by {char_len - 5000} chars!")
            all_ok = False
        else:
            print(f"  -> SAFE: {5000 - char_len} chars remaining below YouTube limit.")

    if not all_ok:
        sys.exit(1)

    # 2. Paths to write
    destinations = {
        "VN": {
            "mo_ta": [
                ROOT / "02_SAN_XUAT" / "Tap20" / "mo_ta.txt",
                ROOT / "02_SAN_XUAT" / "Tap20" / "xuat_ban" / "mo_ta.txt",
            ],
            "sources": [
                ROOT / "02_SAN_XUAT" / "Tap20" / "nguon_mo_ta.txt",
                ROOT / "02_SAN_XUAT" / "Tap20" / "nguon_tham_khao.md",
                ROOT / "02_SAN_XUAT" / "Tap20" / "xuat_ban" / "nguon_tham_khao.md",
            ],
        },
        "EN": {
            "mo_ta": [
                ROOT / "02_SAN_XUAT" / "Tap20_EN" / "description.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_EN" / "mo_ta.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_EN" / "xuat_ban" / "description.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_EN" / "xuat_ban" / "mo_ta.txt",
            ],
            "sources": [
                ROOT / "02_SAN_XUAT" / "Tap20_EN" / "nguon_tham_khao_EN.md",
                ROOT / "02_SAN_XUAT" / "Tap20_EN" / "xuat_ban" / "nguon_tham_khao_EN.md",
            ],
        },
        "JA": {
            "mo_ta": [
                ROOT / "02_SAN_XUAT" / "Tap20_JA" / "description.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_JA" / "mo_ta.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_JA" / "xuat_ban" / "description.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_JA" / "xuat_ban" / "mo_ta.txt",
            ],
            "sources": [
                ROOT / "02_SAN_XUAT" / "Tap20_JA" / "nguon_tham_khao_JA.md",
                ROOT / "02_SAN_XUAT" / "Tap20_JA" / "xuat_ban" / "nguon_tham_khao_JA.md",
            ],
        },
        "KO": {
            "mo_ta": [
                ROOT / "02_SAN_XUAT" / "Tap20_KO" / "description.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_KO" / "mo_ta.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_KO" / "xuat_ban" / "description.txt",
                ROOT / "02_SAN_XUAT" / "Tap20_KO" / "xuat_ban" / "mo_ta.txt",
            ],
            "sources": [
                ROOT / "02_SAN_XUAT" / "Tap20_KO" / "nguon_tham_khao_KO.md",
                ROOT / "02_SAN_XUAT" / "Tap20_KO" / "xuat_ban" / "nguon_tham_khao_KO.md",
            ],
        },
    }

    # Write files
    for lang in ["VN", "EN", "JA", "KO"]:
        d_text = descs[lang] + "\n"
        s_text = sources[lang] + "\n"
        
        for p in destinations[lang]["mo_ta"]:
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(d_text)
            print(f"Written description: {p.relative_to(ROOT)}")
            
        for p in destinations[lang]["sources"]:
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(s_text)
            print(f"Written sources: {p.relative_to(ROOT)}")

    print("\n>>> ALL DESCRIPTION FILES SUCCESSFULLY GENERATED AND VERIFIED <= 5000 CHARACTERS! <<<")


if __name__ == "__main__":
    main()
