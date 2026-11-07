#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo các file mô tả và nguồn tham khảo cho Tập 15 trên 4 ngôn ngữ (VN, EN, JA, KO).
Đảm bảo đầy đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c, K10) và TUYỆT ĐỐI <= 5000 ký tự.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO GỌN CHO FILE NGUỒN TẬP 15
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 15 (JODI ARIAS & TRAVIS ALEXANDER)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp công khai của Tòa án Bang Arizona và Sở Cảnh sát Mesa:

1. Hồ sơ tòa án & Phán quyết tư pháp chính thức:
• Tòa Thượng thẩm Bang Arizona Hạt Maricopa — Toàn văn hồ sơ vụ án State of Arizona v. Jodi Ann Arias (Case No. CR2008-031021, Thẩm phán Sherry Stephens): https://www.clerkofcourt.maricopa.gov/
• Văn phòng Công tố Hạt Maricopa — Báo cáo xét xử và luận tội của Công tố viên Juan Martinez: https://www.maricopacountyattorney.org/
• Tòa Phúc thẩm Bang Arizona — Phán quyết bác đơn kháng cáo của Jodi Arias (2020): https://www.azcourts.gov/

2. Cơ quan điều tra thực địa & Báo chí chính thống:
• Sở Cảnh sát Mesa (Mesa Police Department) — Báo cáo khám nghiệm hiện trường vụ án ngày 04/06/2008, lời khai nhân chứng và biên bản bắt giữ Jodi Arias ngày 15/07/2008: https://www.mesaaz.gov/residents/police
• Juan Martinez (Chánh công tố) — Cuốn hồi ký tư liệu 'Conviction: The Untold Story of Putting Jodi Arias Behind Bars': https://www.harpercollins.com/
• Arizona Republic & CNN/HLN — Kho tư liệu phát thanh truyền hình trực tiếp toàn bộ phiên tòa 2013–2015: https://www.azcentral.com/

3. Giám định tâm thần học pháp y & Nghiên cứu hành vi:
• Tiến sĩ Tâm lý học Lâm sàng Janeen DeMarte — Lời khai nhân chứng chuyên môn của công tố về Rối loạn nhân cách ranh giới (BPD) và Nét ái kỷ ác tính (Malignant Narcissism).
• Hiệp hội Tâm thần học Hoa Kỳ (APA DSM-5-TR) — Tiêu chuẩn chẩn đoán Rối loạn nhân cách ranh giới, Cơn cuồng nộ ranh giới (Borderline Rage) và Nỗi sợ bị ruồng bỏ (Fear of Abandonment).
• Gavin de Becker — Tác phẩm 'The Gift of Fear: Survival Signals That Protect Us from Violence': https://gavindebecker.com/

4. Đường dây nóng hỗ trợ khủng hoảng & bảo vệ nạn nhân:
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7): http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ trầm cảm & khủng hoảng tâm lý): 096 306 1414 — https://duongdaynongngaymai.vn/
• Đường dây nóng hỗ trợ phòng chống bạo lực gia đình: 1900 969 680
"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 15 (JODI ARIAS CASE)
Amber eyes adheres to multi-source verification using verified public court records and forensic transcripts:

1. Official Court Transcripts & Judicial Rulings:
• Maricopa County Superior Court of Arizona — State of Arizona v. Jodi Ann Arias (Case No. CR2008-031021, Judge Sherry Stephens presiding): https://www.clerkofcourt.maricopa.gov/
• Maricopa County Attorney’s Office — Trial prosecution records by Prosecutor Juan Martinez: https://www.maricopacountyattorney.org/
• Arizona Court of Appeals — Ruling affirming Jodi Arias's conviction and life sentence (2020): https://www.azcourts.gov/

2. Law Enforcement Records & Investigative Archives:
• Mesa Police Department — Crime scene forensic reports (June 4, 2008), latent print analysis, and arrest warrant execution (July 15, 2008): https://www.mesaaz.gov/residents/police
• Juan Martinez — 'Conviction: The Untold Story of Putting Jodi Arias Behind Bars': https://www.harpercollins.com/
• The Arizona Republic & CNN/HLN — Complete gavel-to-gavel televised trial broadcast archives (2013–2015): https://www.azcentral.com/

3. Forensic Psychology & Behavioral Science Literature:
• Dr. Janeen DeMarte — Expert psychiatric testimony on Borderline Personality Disorder (BPD) and Malignant Narcissism.
• American Psychiatric Association (APA DSM-5-TR) — Clinical criteria for Borderline Rage, Splitting mechanisms, and Abandonment Trauma.
• Gavin de Becker — 'The Gift of Fear: Survival Signals That Protect Us from Violence': https://gavindebecker.com/

4. Crisis Helplines & Support:
• National Domestic Violence Hotline (US): 1-800-799-SAFE (7233) / Text "START" to 88788 — https://www.thehotline.org/
• National Suicide & Crisis Lifeline: Dial 988 (toll-free 24/7) — https://988lifeline.org/
• Childhelp National Child Abuse Hotline: 1-800-422-4453 — https://www.childhelp.org/
"""

SOURCES_JA = """📚 第15話 参考文献・公式捜査資料一覧（ジョディ・アリアス事件）
Amber eyesは、アリゾナ州裁判所の公開公判記録およびメサ市警察の公式文書に基づく厳格な事実確認を行っています：

1. 公式裁判記録および司法判決:
• アリゾナ州マリコパ郡上級裁判所 — アリゾナ州対ジョディ・アン・アリアス公判記録（事件番号 CR2008-031021、シェリー・スティーブンス裁判長）: https://www.clerkofcourt.maricopa.gov/
• マリコパ郡検察局 — フアン・マルティネス検事による論告および起訴記録: https://www.maricopacountyattorney.org/
• アリゾナ州控訴裁判所 — 有罪判決および仮釈放なし終身刑支持決定（2020年）: https://www.azcourts.gov/

2. 捜査機関記録および公式アーカイブ:
• メサ市警察（Mesa Police Department） — 2008年6月4日事件現場鑑識報告書、デジタル復元記録、2008年7月15日逮捕状執行記録: https://www.mesaaz.gov/residents/police
• フアン・マルティネス検事 — 著書『Conviction: The Untold Story of Putting Jodi Arias Behind Bars』: https://www.harpercollins.com/
• アリゾナ・リパブリック紙およびCNN/HLN — 2013年〜2015年全米生中継公判記録アーカイブ: https://www.azcentral.com/

3. 法精神医学および行動科学文献:
• ジャニーン・デマルテ臨床心理学博士（Dr. Janeen DeMarte） — 境界性パーソナリティ障害（BPD）および悪性自己愛に関する検察側専門家証言。
• ギャビン・デ・ベッカー著『ギフト・オブ・フィアー（恐怖という贈り物）』: https://gavindebecker.com/

4. 相談窓口・支援ホットライン:
• DV相談ナビ（日本・全国共通）: #8008 / DV相談プラス: 0120-279-889（24時間対応・通話無料）
• よりそいホットライン: 0120-279-338 (24時間通話無料) — https://www.thenewjapan.org/
• 警察相談専用電話: #9110
"""

SOURCES_KO = """📚 제15화 참고 문헌 및 공식 수사 기록 (조디 아리아스 사건)
Amber eyes는 애리조나주 법원의 공식 공판 기록 및 메사 경찰국의 공인 수사 문서를 바탕으로 철저한 검증을 거쳤습니다:

1. 공식 법원 공판 기록 및 사법 판결:
• 애리조나주 마리코파 카운티 상급법원 — 애리조나주 대 조디 앤 아리아스 공판 기록 (사건번호 CR2008-031021, 셰리 스티븐스 판사): https://www.clerkofcourt.maricopa.gov/
• 마리코파 카운티 검찰청 — 후안 마르티네스 검사의 기소 및 논고 기록: https://www.maricopacountyattorney.org/
• 애리조나주 항소법원 — 유죄 판결 및 가석방 없는 종신형 확정 판결 (2020년): https://www.azcourts.gov/

2. 수사 기관 기록 및 탐사 보도:
• 메사 경찰국(Mesa Police Department) — 2008년 6월 4일 사건 현장 감식 보고서, 디지털 포렌식 증거 기록, 2008년 7월 15일 체포 영장 집행 기록: https://www.mesaaz.gov/residents/police
• 후안 마르티네스 검사 — 수사 회고록 'Conviction: The Untold Story of Putting Jodi Arias Behind Bars': https://www.harpercollins.com/
• 애리조나 리퍼블릭 및 CNN/HLN — 2013~2015년 전미 생중계 재판 아카이브: https://www.azcentral.com/

3. 법심리학 및 행동과학 연구 문헌:
• 자닌 데마르테 임상심리학 박사(Dr. Janeen DeMarte) — 경계선 성격장애(BPD) 및 악성 자기애에 대한 검찰 측 전문 증인 증언.
• 개빈 드 베커 — 저서 '공포라는 선물(The Gift of Fear)': https://gavindebecker.com/

4. 긴급 상담 및 피해자 지원 핫라인:
• 여성긴급전화 (한국): 1366 (24시간 교제폭력·스토킹 상담 및 긴급 피신)
• 경찰청 범죄신고: 112 / 정부민원안내: 110
• 정신건강 상담전화: 1577-0199 / 자살예방 상담: 109
"""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (TỐI ƯU CÔ ĐỌNG, STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Tập 15: Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới | Tâm lý học tội phạm: Jodi Arias, Nỗi Sợ Bị Ruồng Bỏ & Thảm Kịch Phòng Tắm (10 Chỉ Dấu Tâm Lý & Bẫy Thao Túng) | Amber eyes

Ngày 9 tháng 6 năm 2008, tại Mesa, Arizona, Travis Alexander — một diễn giả truyền cảm hứng 30 tuổi — được phát hiện đã bị tước đoạt mạng sống trong buồng tắm. Hung thủ đã ném máy ảnh vào máy giặt cùng quần áo ướt nhằm tiêu hủy dữ liệu số. Tuy nhiên, sự kiên định của đội ngũ pháp y và cuộc đấu trí gần 7 năm tại Tòa Thượng thẩm Maricopa đã bóc trần chiếc mặt nạ của Jodi Arias — một phụ nữ mang vẻ ngoài trí thức nhưng che giấu cấu trúc nhân cách ranh giới nguy hiểm khi ảo tưởng sở hữu bị sụp đổ.

Hồ sơ Jodi Arias được Amber eyes giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi (§A2c):
1. DƯ CHẤN XÃ HỘI & RẠN NỨT NIỀM TIN: Thảm kịch gây rúng động Mesa; phiên tòa truyền hình 2013 thu hút hàng chục triệu người xem tạo 'rạp xiếc truyền thông' (media circus); thúc đẩy cải cách quy định ghi hình tại tòa án hình sự.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem nạn nhân là 'vật thể cảm xúc' khỏa lấp lỗ hổng căn tính; khiếm khuyết Thuyết tâm trí biến mạng sống đối phương thành công cụ thống trị; sự từ chối bị coi là xúc phạm cái tôi ái kỷ.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Phân lập 2 ngăn kéo: cháu gái hiền lành ở California vs. kẻ săn mồi chuẩn bị 3 can xăng; ngay sau vụ án, lái xe đến Utah gặp người đàn ông khác và gửi thư thoại ngọt ngào cho nạn nhân.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Khi bồi thẩm đoàn tuyên có tội Giết người cấp 1, mặt nạ tự mãn tan vỡ; Jodi rơi vào khủng hoảng bản ngã, chuyển sang tự thương hại bệnh lý (Pathological Self-Pity), xin nhận án tử hình rồi lại kháng cáo.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC: 3 tầng dối trá (Sykes & Matza): (1) Phủ nhận hiện diện -> (2) Bịa 2 kẻ đột nhập -> (3) Bôi nhọ nạn nhân bằng kịch bản bạo hành và mất trí nhớ giả mạo để sắm vai nạn nhân tự vệ trốn án phạt.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Cuối tháng 5/2008, khi biết tin Travis dứt khoát vạch ranh giới và chuẩn bị cùng đồng nghiệp đi Cancun; kích hoạt nỗi sợ bị ruồng bỏ cực độ và chuyển hóa thành kế hoạch đoạt mạng có chuẩn bị.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO (thuê xe xa, nhuộm tóc, tắt điện thoại, mang 3 can xăng tránh quẹt thẻ, giấu máy ảnh vào máy giặt) liên tục đổi; Signature bất biến là nhu cầu chụp ảnh cuối trong buồng tắm và mức độ dồn dập phản ánh Borderline Rage.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: 4 giai đoạn leo thang: (1) Thần tượng hóa & cải đạo Mormon -> (2) Lấn ranh giới & hack tài khoản cá nhân -> (3) Phá hoại tài sản & rạch lốp xe -> (4) Cơn cuồng nộ hủy diệt khi bị từ chối sở hữu độc tôn.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vẻ ngoài nữ tính, mảnh mai, học thức tạo chiếc khiên 'Hào quang ngược' khiến người xung quanh mất cảnh giác, tin rằng cô ta chỉ là người yêu cũ phiền toái chứ không gây nguy hiểm tính mạng.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ SINH TỒN: Tôn vinh phẩm giá của Travis Alexander; 4 cảnh báo đỏ (The Gift of Fear - Gavin de Becker): Gắn kết quá nhanh kết hợp tắc kè hoa, Xâm phạm ranh giới cá nhân, Tư duy phân tách trắng đen, và Leo thang hung hãn khi chia tay.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Ám ảnh độc hại và thảm kịch trong buồng tắm
05:15 Hồi 2 · Dấu vết kỹ thuật số và chiếc bình xăng bí mật
10:45 Hồi 3 · Giải mã tâm lý: Rối loạn nhân cách ranh giới (BPD) & Cơn cuồng nộ ruồng bỏ
16:30 Hồi 4 · Trò ảo thuật phòng thẩm vấn và phiên tòa truyền hình
21:45 Hồi 5 · Phán quyết chung thân & 4 cảnh báo đỏ của mối quan hệ ám ảnh

⚠️ LƯU Ý PHÁP LÝ & CÔNG NGHỆ AI
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai Tòa Thượng thẩm Arizona (CR2008-031021) và Sở Cảnh sát Mesa; không nhằm bôi nhọ bất kỳ ai.
• Linh thú Cú, Sói, Cáo, Cừu, Mèo là nhân vật minh họa. Lời thoại dựng lại dựa trên biên bản lời khai và hồ sơ tố tụng.
• Giọng đọc AI Boson AI Higgs Audio v3; đồ họa noir độc quyền của kênh.

📚 NGUỒN KIỂM CHỨNG CHÍNH THỨC
• Tòa Thượng thẩm Bang Arizona Hạt Maricopa: https://www.clerkofcourt.maricopa.gov/
• Sở Cảnh sát Mesa (Mesa PD): https://www.mesaaz.gov/residents/police
• Hồi ký 'Conviction' của Công tố viên Juan Martinez: https://www.harpercollins.com/
• Lời khai giám định pháp y của TS. Janeen DeMarte về BPD & Ái kỷ.
• Tác phẩm 'The Gift of Fear' của Gavin de Becker: https://gavindebecker.com/

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ BẢO VỆ 24/7
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7): http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng phòng chống bạo lực gia đình: 1900 969 680

#AmberEyes #TrueCrime #TamLyToiPham #JodiArias #TravisAlexander #BPD #BorderlineRage #10ChiDauTamLy #CanhBaoDo #HoSoToiPham #DigitalForensics"""

DESC_EN = """Ep. 15: Borderline Rage & Fatal Obsession | Criminal Psychology: Jodi Arias, Fear of Abandonment & The Bathroom Tragedy (10 Psychological Markers & Manipulation Trap) | Amber eyes

On June 9, 2008, in Mesa, Arizona, 30-year-old motivational speaker Travis Alexander was found deceased in his master bathroom. The assailant submersed a digital camera in the washing machine to destroy digital evidence with water. However, forensic data recovery and a seven-year legal battle at Maricopa County Superior Court unmasked Jodi Arias — an articulate woman whose demure exterior concealed a lethal borderline personality structure that erupted into volcanic fury when her fantasy of possessive control shattered.

The Jodi Arias Case is deconstructed through Amber eyes' 10 Core Psychological Markers & Behavioral Framework (§A2c):
1. SOCIAL IMPACT & COLLECTIVE TRAUMA: The tragedy shook Mesa; the 2013 televised trial drew tens of millions of viewers creating an unprecedented 'media circus'; public polarization catalyzed reforms restricting broadcast cameras in capital cases.
2. OBJECTIFICATION & EMPATHY DEFICIT: Arias degraded Alexander into an emotional possession to patch her internal void; deficits in Theory of Mind led her to treat life as an instrumental prop; rejection triggered narcissistic rage requiring punitive destruction.
3. COGNITIVE COMPARTMENTALIZATION: Mental partitioning into 2 drawers: polite granddaughter in California vs. calculating predator preparing 3 fuel cans; post-crime, she traveled to Utah to socialize cheerfully, leaving affectionate voicemails for Travis.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: The first-degree murder verdict shattered her victim persona; plunging into ego collapse, Arias shifted from defying the jury to desperate self-pity, requesting capital punishment before appealing.
5. TECHNIQUES OF NEUTRALIZATION & MANIPULATIVE VICTIMHOOD: 3-tiered fabrications (Sykes & Matza): (1) Denying presence -> (2) Fabricating 2 masked intruders -> (3) Slandering the victim via false abuse claims and fake amnesia to stage self-defense.
6. PSYCHOLOGICAL TRIGGER & TIPPING POINT: Late May 2008, learning Travis severed ties and planned a Cancun trip with another woman; this mortification detonated her fear of abandonment, transmuting stalking into planned annihilation.
7. SIGNATURE VS. MODUS OPERANDI: MO evolved for evasion (car rental, hair dye, phone off, 3 fuel cans, submersing camera); invariable Signature was taking final bathroom photos and explosive overkill reflecting Borderline Rage.
8. FANTASY ADDICTION & 4-STAGE ESCALATION: 4-stage trajectory: (1) Rapid idealization & conversion -> (2) Boundary encroachment & hacking accounts -> (3) Property vandalism & tire slashing -> (4) Annihilation rage upon total rejection.
9. HALO EFFECT & SOCIAL BLINDSPOTS: Demure, studious appearance created a reverse halo effect; societal biases led people to misjudge her as an eccentric ex-partner rather than a calculating predator.
10. VICTIMOLOGY & 4 SURVIVAL RED FLAGS: Honoring Travis Alexander's dignity; 4 survival signals (The Gift of Fear - Gavin de Becker): Accelerated chameleon mimicry, Boundary encroachment, Polarized splitting, and Retaliatory escalation.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Advisory
00:23 Act 1 · Toxic Obsession & The Tragedy in the Bathroom
05:15 Act 2 · Digital Traces & The Secret Fuel Cans
10:45 Act 3 · Psychological Deconstruction: BPD & Abandonment Rage
16:30 Act 4 · The Interrogation Illusion & The Televised Trial
21:45 Act 5 · Natural Life Verdict & 4 Red Flags of Obsessive Relationships

⚠️ LEGAL DISCLAIMER & AI DISCLOSURE
• Produced for educational and forensic analysis; not clinical or legal advice.
• Based on public trial exhibits of Maricopa County Superior Court (CR2008-031021) and Mesa Police Department.
• Character avatars are stylized representations; dialogues reconstructed from verified court testimony.
• Synthesized using Boson AI Higgs Audio v3 technology; graphic novel noir visual aesthetic.

📚 OFFICIAL SOURCES & TRIAL EXHIBITS
• Maricopa County Superior Court Public Case Records: https://www.clerkofcourt.maricopa.gov/
• Mesa Police Department Homicide Investigation Records: https://www.mesaaz.gov/residents/police
• Prosecutor Juan Martinez's trial memoir 'Conviction': https://www.harpercollins.com/
• Dr. Janeen DeMarte's expert testimony on BPD & Malignant Narcissism.
• Gavin de Becker's 'The Gift of Fear': https://gavindebecker.com/

🆘 24/7 CRISIS HELPLINES
• National Domestic Violence Hotline (US): 1-800-799-SAFE (7233) / Text "START" to 88788 — https://www.thehotline.org/
• 988 Suicide & Crisis Lifeline: Call or text 988 (toll-free 24/7, US & Canada) — https://988lifeline.org/
• Childhelp National Child Abuse Hotline: 1-800-422-4453 — https://www.childhelp.org/

#AmberEyes #TrueCrime #CriminalPsychology #JodiArias #TravisAlexander #BPD #BorderlineRage #10PsychologicalMarkers #RedFlags #ForensicFiles #DigitalForensics"""

DESC_JA = """第15話：境界性パーソナリティ障害の狂気の嫉妬 | 犯罪心理学：ジョディ・アリアス、見捨てられ不安と浴室の悲劇（10の心理指標エコシステムと操作の罠） | Amber eyes

2008年6月9日、アリゾナ州メサで30歳の講演家Travis Alexanderが自宅浴室で命を奪われました。犯人は浸水により電子的記録を破壊しようとデジタルカメラを洗濯機へ投入していましたが、鑑識班の執念のデータ復元とマリコパ郡上級裁判所での7年に及ぶ法廷闘争が、ジョディ・アリアス（Jodi Arias）の仮面を剥ぎ取りました。清楚な外見の奥底には、支配の幻想が砕けた際に破壊的激怒を爆発させる重度の境界性パーソナリティ構造が潜んでいたのです。

本エピソードでは、Amber eyes独自の「10大核心心理指標エコシステム（§A2c）」を通じて事件を徹底解剖します：
1. 社会的余波と集団的トラウマ：メサを揺るがした恐怖；2013年全米生中継裁判が空前の「メディアサーカス」を現出；世論過熱を受け重大刑事裁判での法廷カメラ規制の法改正が進展。
2. 被害者の客体化（Objectification）と共感の欠如：自己の慢性的な空虚感を埋める感情的道具として被害者を所有物扱い；心の理論の欠如により他者の苦痛や命を支配欲求を満たす小道具へと貶め、命乞いを自己愛への冒涜と見なして処罰。
3. 心理的区画化（Compartmentalization）：祖父母と暮らす従順な孫娘の引き出しと、予備燃料缶3個を用意し追跡する冷酷な捕食者の引き出しを完全分離；犯行直後にもユタ州で別の男性と笑顔で歓談し、何事もなかったかのように被害者へ留守電を残す二重生活。
4. 自己愛の崩壊（Narcissistic Collapse）と病的な自己憐憫：第1級殺人罪の有罪評決により尊大な優越感が崩壊；陪審員を嘲笑していた傲慢さから同情を引く自己憐憫へ急旋回し、死刑を要求するも即座に減刑を求めて控訴する自己防衛の醜態。
5. 自己正当化と道徳的中和技術（Techniques of Neutralization）：3段階の変遷を辿る虚偽（アリゾナ滞在否定 -> 覆面強盗犯の捏造 -> 虚偽のDV被害と偽装記憶喪失による正当防衛劇）；自らを被害者と位置づけて責任を完全に回避。
6. 心理的引き金（Trigger）と臨界点：2008年5月下旬、Travisが境界線を明確にして別の女性とのカンクン旅行を決定した事実；耐え難い自己愛の傷つきと見捨てられ不安の極限が、水面下のストーカー行為を計画的殺害計画へと一挙に暴発させた契機。
7. 署名（Signature）対犯行手口（MO）の進化：追跡を逃れるMO（遠隔レンタカー、髪の染色、携帯電源切断、カード痕跡を消す燃料缶3個、カメラの洗濯機隠蔽）；不変のシグネチャーは浴室で最後の写真を撮影し続けた病的な支配欲求と過剰破壊（Overkill）に表れた境界性の激怒（Borderline Rage）。
8. 妄想への耽溺と4段階のエスカレーション：(1) 理想化と同化（改宗） -> (2) 境界侵犯とアカウント不正侵入 -> (3) 器物損壊とタイヤ切り裂き -> (4) 独占拒絶に伴う破滅的激怒の爆発。
9. 後光効果（Halo Effect）と集団的盲点：清楚で知的な佇まいが強力な「逆ハロー効果」を生み、周囲も被害者自身も彼女を「少し厄介な元恋人」と見くびり生命の危機を感知できなかった心理的死角。
10. 被害者学と4大生存レッドフラグ：Travis Alexanderの名誉と人間性を追悼；ギャビン・デ・ベッカー著『ギフト・オブ・フィアー』に基づく4大生存警告（急速すぎる同化、献身を装った境界侵蝕、白黒思考のスプリッティング、別れ際の脅迫・損壊のエスカレーション）。

⏱ タイムスタンプ
00:00 オープニング・注意事項
00:23 第1幕 · 毒された執着と浴室の悲劇
05:15 第2幕 · デジタルの痕跡と秘密の燃料缶
10:45 第3幕 · 心理分析：BPDと見捨てられの激怒
16:30 第4幕 · 取調室のイリュージョンと中継された法廷劇
21:45 第5幕 · 終身刑判決と執着関係の4大レッドフラグ

⚠️ 法的事項およびAI制作についての免責事項
• 本動画は教育、歴史的検証、犯罪心理学分析を目的として制作されており、医学的・法的助言を提供するものではありません。
• アリゾナ州マリコパ郡上級裁判所の公開公判記録（State v. Arias, CR2008-031021）およびメサ市警察の公式捜査記録に基づいています。
• キャラクター（フクロウ、オオカミ等）は象徴的アバターです。音声はBoson AI Higgs Audio v3を用いて生成され、映像はノワール調グラフィックノベルスタイルで演出されています。

📚 公式参考文献・出典資料
• マリコパ郡上級裁判所 公開記録: https://www.clerkofcourt.maricopa.gov/
• メサ市警察 殺人捜査記録: https://www.mesaaz.gov/residents/police
• フアン・マルティネス検事 著書『Conviction』: https://www.harpercollins.com/
• ジャニーン・デマルテ博士（Dr. Janeen DeMarte）による精神医学鑑定記録。
• ギャビン・デ・ベッカー著『ギフト・オブ・フィアー』: https://gavindebecker.com/

🆘 相談窓口・支援ホットライン
• DV相談ナビ: #8008 / DV相談プラス: 0120-279-889（24時間対応・通話無料）
• よりそいホットライン: 0120-279-338 (24時間通話無料) — https://www.thenewjapan.org/
• こころの健康相談統一ダイヤル: 0570-064-556

#AmberEyes #犯罪心理学 #ジョディ・アリアス #境界性パーソナリティ障害 #BPD #トラヴィス・アレクサンダー #心理分析 #取調室 #プロファイリング #未解決事件 #実話事件 #レッドフラグ"""

DESC_KO = """제15화: 경계선 성격장애의 광기 어린 질투 | 범죄심리학: 조디 아리아스, 유기 불안과 욕실의 비극 (10대 핵심 심리 지표 및 가스라이팅의 덫) | Amber eyes

2008년 6월 9일, 미국 애리조나주 메사에서 30세의 동기부여 강사 Travis Alexander가 자택 욕실에서 참혹하게 생명을 빼앗긴 채 발견되었습니다. 가해자는 물로 전자 데이터를 파괴하기 위해 디지털카메라를 세탁기에 넣어 돌려놓았으나, 디지털 포렌식 복원과 마리코파 카운티 법원에서 7년간 이어진 법정 공방은 조디 아리아스(Jodi Arias)의 가면을 벗겨냈습니다. 지적이고 단정한 외모 뒤에는 자신의 독점적 통제와 소유 환상이 무너지는 순간 잔혹한 파괴 충동으로 돌변한 중증 경계선 성격장애가 숨어 있었습니다.

Amber eyes는 '10대 핵심 심리 지표 및 행동과학 프레임워크(§A2c)'를 통해 조디 아리아스 사건의 심연을 정밀 해부합니다:
1. 사회적 파장과 제도의 변화: 지역 사회를 뒤흔든 충격; 2013년 재판 전미 생중계가 수천만 명의 시청자를 끌어모으며 유례없는 '미디어 서커스' 현상을 촉발; 대중의 과열된 반응으로 인해 중범죄 재판 시 법정 내 카메라 중계를 엄격히 제한하는 사법 개혁으로 이어짐.
2. 피해자의 객체화(Objectification)와 공감 결여: 내면의 만성적인 정체성 공허감을 메우기 위해 연인을 소유물인 감정적 도구로 격하; 타인의 마음에 대한 이해와 공감 능력 결여로 인해 상대의 고통과 인격을 통제 욕구의 수단으로 취급하고, 거절과 애원을 자기애에 대한 모욕으로 받아들여 처벌.
3. 심리적 구획화(Compartmentalization): 조부모를 돌보는 얌전한 손녀의 서랍과 보조 연료통 3개를 챙겨 피해자를 미행하는 냉혹한 포식자의 서랍을 완벽히 분리; 범행 직후 유타주로 이동해 다른 남성과 밝은 미소로 어울리며 태연하게 다정한 음성 메시지를 남기는 이중생활의 극치.
4. 나르시시즘적 붕괴(Narcissistic Collapse)와 병적인 자기연민: 배심원단의 1급 살인 유죄 평결로 우월한 자아상이 산산조각 나며 심각한 자아 붕괴에 직면; 배심원을 조롱하던 오만함에서 동정을 유발하기 위한 극단적 자기연민으로 돌변하여 사형을 탄원하다가도 종신형 선고 앞에서는 즉각 감형 항소를 제기하는 모순.
5. 자기 정당화와 도덕적 중화 기술(Techniques of Neutralization): 3단계에 걸친 거짓 진술의 변천(애리조나 방문 전면 부인 -> 복면 괴한 침입설 날조 -> 피해자를 가해자로 둔갑시킨 조작된 가정폭력 및 기억상실 주장의 정당방위 연극); 철저한 피해자 코스프레를 통한 책임 회피.
6. 심리적 방아쇠(Trigger)와 한계점: 2008년 5월 말, Travis가 단호히 선을 긋고 다른 여성과의 칸쿤 여행을 확정한 사실; 견딜 수 없는 자기애적 모욕감과 극단적 유기 불안이 폭발하며 음성적 스토킹을 치밀한 계획 범행으로 전환시킨 결정적 계기.
7. 시그니처(Signature) 대 범행 수법(MO)의 진화: 추적을 피하기 위한 MO(원거리 렌터카, 짙은 갈색 염색, 휴대전화 전원 차단, 카드 결제 흔적을 지우기 위한 연료통 3개 적재, 카메라 세탁기 은닉); 결코 포기하지 않은 시그니처는 욕실에서 마지막 순간들을 집요하게 촬영한 병적인 통제 욕구와 과잉 살상(Overkill)에 드러난 경계선 분노(Borderline Rage).
8. 환상 중독과 4단계 에스컬레이션: (1) 우상화 및 종교 개종을 통한 인격 동화 -> (2) 경계 침해 및 계정 해킹 스토킹 -> (3) 타이어 손괴 및 협박 -> (4) 거절에 직면한 파멸적 파괴 충동 분출.
9. 후광 효과(Halo Effect)와 집단적 맹점: 단정하고 왜소하며 지적인 여성의 외모가 형성한 '역후광 효과'로 인해 주변인들과 피해자조차 그녀를 단순한 귀찮은 전 연인으로 오판하여 치명적 위험 신호를 간과한 사회적 편견.
10. 피해자학 및 4대 생존 레드플래그: Travis Alexander의 고결한 인품과 삶을 추모; 개빈 드 베커의 '공포라는 선물'에 기반한 4대 생존 경고(카멜레온 모방과 급속한 밀착, 헌신으로 위장된 미세 통제, 흑백논리 스플리팅, 결별 국면에서의 보복 협박 및 손괴).

⏱ 챕터 타임스탬프
00:00 인트로 및 주의사항
00:23 막 1 · 유독한 집착과 욕실에서 벌어진 비극
05:15 막 2 · 디지털 흔적과 비밀의 연료통
10:45 막 3 · 심리 분석: 경계선 성격장애(BPD)와 유기 분노의 폭발
16:30 막 4 · 취조실의 환상과 중계된 법정 드라마
21:45 막 5 · 종신형 판결과 집착적 관계의 4대 레드플래그

⚠️ 법적 고지 및 AI 기술 안내
• 본 영상은 범죄심리학적 분석, 역사적 기록 및 공익적 교육을 목적으로 제작되었으며, 의학적 또는 법적 조언을 대신하지 않습니다.
• 애리조나주 마리코파 카운티 상급법원 공개 공판 기록(State v. Arias, CR2008-031021) 및 메사 경찰국 수사 문서를 바탕으로 엄정하게 구성되었습니다.
• 동물 캐릭터들(부엉이, 늑대 등)은 상징적 아바타입니다. 음성은 Boson AI Higgs Audio v3 기술로 합성되었으며, 비주얼은 느와르 그래픽 노블 양식으로 연출되었습니다.

📚 공식 참고 문헌 및 공판 출처
• 애리조나주 마리코파 카운티 법원 공개 기록: https://www.clerkofcourt.maricopa.gov/
• 메사 경찰국 수사 기록 보고서: https://www.mesaaz.gov/residents/police
• 후안 마르티네스 검사 수사 회고록 'Conviction': https://www.harpercollins.com/
• 자닌 데마르테 박사(Dr. Janeen DeMarte) 임상 법심리학 감정 증언 기록.
• 개빈 드 베커 저서 '공포라는 선물(The Gift of Fear)': https://gavindebecker.com/

🆘 긴급 상담 및 피해자 지원 핫라인
• 여성긴급전화 (한국): 1366 (24시간 교제폭력·스토킹 상담 및 긴급 피신)
• 경찰청 범죄신고: 112 / 정부민원안내: 110
• 정신건강 상담전화: 1577-0199 / 자살예방 상담: 109

#AmberEyes #범죄심리학 #조디아리아스 #경계선성격장애 #BPD #트래비스알렉산더 #프로파일링 #심리분석 #취조실 #실화사건 #레드플래그 #디지털포렌식"""


def write_file_lf(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    # Normalize to pure LF (\n)
    normalized = content.replace("\r\n", "\n").replace("\r", "\n")
    path.write_bytes(normalized.encode("utf-8"))


def main():
    print("=== BẮT ĐẦU TẠO CÁC FILE MÔ TẢ TẬP 15 (4 NGÔN NGỮ) ===")
    
    # 1. Đo ký tự
    desc_dict = {
        "VI": DESC_VI,
        "EN": DESC_EN,
        "JA": DESC_JA,
        "KO": DESC_KO,
    }
    
    for lang, text in desc_dict.items():
        cnt = len(text.strip())
        print(f"[{lang}] Dung lượng ký tự: {cnt:,} / 5,000 ký tự (Đạt: {cnt <= 5000})")
        if cnt > 5000:
            print(f"LỖI: {lang} vượt quá 5000 ký tự!")
            sys.exit(1)

    # 2. Ghi các file Tiếng Việt
    dir_vi = ROOT / "02_SAN_XUAT" / "Tap15"
    write_file_lf(dir_vi / "mo_ta.txt", DESC_VI)
    write_file_lf(dir_vi / "xuat_ban" / "mo_ta.txt", DESC_VI)
    write_file_lf(dir_vi / "nguon_mo_ta.txt", SOURCES_VI)
    write_file_lf(dir_vi / "nguon_tham_khao.md", SOURCES_VI)
    write_file_lf(dir_vi / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI)
    print("-> Đã ghi xong các file Tiếng Việt (Tap15)")

    # 3. Ghi các file Tiếng Anh
    dir_en = ROOT / "02_SAN_XUAT" / "Tap15_EN"
    write_file_lf(dir_en / "description.txt", DESC_EN)
    write_file_lf(dir_en / "mo_ta.txt", DESC_EN)
    write_file_lf(dir_en / "xuat_ban" / "description.txt", DESC_EN)
    write_file_lf(dir_en / "xuat_ban" / "mo_ta.txt", DESC_EN)
    write_file_lf(dir_en / "nguon_mo_ta_EN.txt", SOURCES_EN)
    write_file_lf(dir_en / "nguon_tham_khao_EN.md", SOURCES_EN)
    write_file_lf(dir_en / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN)
    print("-> Đã ghi xong các file Tiếng Anh (Tap15_EN)")

    # 4. Ghi các file Tiếng Nhật
    dir_ja = ROOT / "02_SAN_XUAT" / "Tap15_JA"
    write_file_lf(dir_ja / "description.txt", DESC_JA)
    write_file_lf(dir_ja / "mo_ta.txt", DESC_JA)
    write_file_lf(dir_ja / "xuat_ban" / "description.txt", DESC_JA)
    write_file_lf(dir_ja / "xuat_ban" / "mo_ta.txt", DESC_JA)
    write_file_lf(dir_ja / "nguon_mo_ta_JA.txt", SOURCES_JA)
    write_file_lf(dir_ja / "nguon_tham_khao_JA.md", SOURCES_JA)
    write_file_lf(dir_ja / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA)
    print("-> Đã ghi xong các file Tiếng Nhật (Tap15_JA)")

    # 5. Ghi các file Tiếng Hàn
    dir_ko = ROOT / "02_SAN_XUAT" / "Tap15_KO"
    write_file_lf(dir_ko / "description.txt", DESC_KO)
    write_file_lf(dir_ko / "mo_ta.txt", DESC_KO)
    write_file_lf(dir_ko / "xuat_ban" / "description.txt", DESC_KO)
    write_file_lf(dir_ko / "xuat_ban" / "mo_ta.txt", DESC_KO)
    write_file_lf(dir_ko / "nguon_mo_ta_KO.txt", SOURCES_KO)
    write_file_lf(dir_ko / "nguon_tham_khao_KO.md", SOURCES_KO)
    write_file_lf(dir_ko / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO)
    print("-> Đã ghi xong các file Tiếng Hàn (Tap15_KO)")

    print("\n=== HOÀN TẤT TẠO TOÀN BỘ FILE MÔ TẢ TẬP 15 ===")


if __name__ == "__main__":
    main()
