#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo các file mô tả và nguồn tham khảo cho Tập 11 trên 4 ngôn ngữ (VN, EN, JA, KO).
Đảm bảo đầy đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c, K10) và TUYỆT ĐỐI <= 5000 ký tự.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO GỌN CHO FILE NGUỒN TẬP 11
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 11 (PAUL BERNARDO & KARLA HOMOLKA)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp công khai của Tòa án Ontario và Bộ Tư pháp Canada:

1. Hồ sơ tòa án & Phán quyết tư pháp chính thức:
• Tòa Thượng thẩm Ontario (Ontario Superior Court of Justice) — Bản án xét xử Paul Kenneth Bernardo (1995, Thẩm phán Patrick LeSage, tuyên bố Can phạm Nguy hiểm - Dangerous Offender): https://www.canlii.org/
• Viện Kiểm sát Tỉnh bang Ontario — Hồ sơ thỏa thuận nhận tội đặc biệt của Karla Homolka (1993, mức án 12 năm tù): https://www.ontario.ca/
• Tòa Phúc thẩm Ontario (Court of Appeal for Ontario) — Bác đơn kháng cáo bản án chung thân của Paul Bernardo (1997 CanLII 1256): https://www.canlii.org/

2. Báo cáo điều tra tư pháp độc lập & Cải cách hệ thống:
• Cựu Thẩm phán Patrick Galligan (1996) — Báo cáo điều tra độc lập về quy trình ký kết thỏa thuận nhận tội của cơ quan công tố Ontario (Galligan Inquiry).
• Thẩm phán Archie Campbell (1999) — Báo cáo điều tra Campbell (Campbell Inquiry) về sự tắc nghẽn thông tin cảnh sát và cuộc đại cải tổ hệ thống ViCLAS toàn quốc.

3. Tư liệu điều tra báo chí & Chuyên khảo tội phạm học:
• Stephen Williams (Ký giả điều tra) — Tác phẩm tư liệu 'Invisible Darkness: The Strange Case of Paul Bernardo and Karla Homolka': https://www.penguinrandomhouse.ca/
• Nick Pron (Phóng viên Toronto Star) — 'Lethal Marriage: The Unspeakable Crimes of Paul Bernardo and Karla Homolka': https://www.torontostar.com/

4. Tâm lý học hành vi & Khung phân tích chuyên sâu:
• Thang đo Thái nhân cách Robert Hare (Hare Psychopathy Checklist-Revised - PCL-R) áp dụng cho Paul Bernardo: https://www.hare.org/
• Phân tích Hội chứng Điên cuồng đôi (Shared Psychotic Disorder / Folie à Deux), Thao túng đóng vai nạn nhân (Manipulative Victimhood) và Kỹ thuật trung hòa đạo đức (Sykes & Matza).

5. Đường dây nóng hỗ trợ & bảo vệ:
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7): http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414 — https://duongdaynongngaymai.vn/
• Đường dây nóng hỗ trợ phụ nữ bị bạo lực gia đình: 1900 969 680
"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 11 (PAUL BERNARDO & KARLA HOMOLKA)
Amber eyes adheres to multi-source verification using verified public court records and Canadian judicial inquiries:

1. Official Court Transcripts & Judicial Rulings:
• Ontario Superior Court of Justice — R. v. Bernardo (1995, Justice Patrick LeSage presiding; Dangerous Offender designation): https://www.canlii.org/
• Ministry of the Attorney General of Ontario — Karla Homolka Plea Agreement Records (May 1993, 12-year manslaughter sentence): https://www.ontario.ca/
• Court of Appeal for Ontario — Bernardo Conviction Appeal Dismissal (1997 CanLII 1256): https://www.canlii.org/

2. Independent Judicial Inquiries & Systemic Reforms:
• The Honourable Patrick T. Galligan (1996) — Report of the Independent Review into the Prosecutorial Handling of the Bernardo Case (Galligan Report).
• The Honourable Archie Campbell (1999) — The Campbell Report: Inter-agency police communication breakdown and the overhaul of Canada's ViCLAS system.

3. Investigative Journalism & Scholarly Monographs:
• Stephen Williams — 'Invisible Darkness: The Strange Case of Paul Bernardo and Karla Homolka': https://www.penguinrandomhouse.ca/
• Nick Pron — 'Lethal Marriage: The Unspeakable Crimes of Paul Bernardo and Karla Homolka': https://www.torontostar.com/

4. Behavioral Sciences & Criminological Frameworks:
• Dr. Robert D. Hare — The Hare Psychopathy Checklist-Revised (PCL-R) clinical profiles: https://www.hare.org/
• Clinical evaluations of Folie à Deux (Shared Psychotic Disorder), Manipulative Victimhood, and Techniques of Neutralization (Sykes & Matza).

5. Crisis Helplines & Support:
• National Crisis & Mental Health Lifeline (US/Canada): Dial 988 (toll-free 24/7) — https://988lifeline.org/
• Canadian Centre for Child Protection: https://www.protectchildren.ca/
• National Domestic Violence Hotline: 1-800-799-SAFE (7233) — https://www.thehotline.org/
"""

SOURCES_JA = """📚 第11話 参考文献・公式調査資料一覧（ポール・ベルナルドとカーラ・ホモルカ）
Amber eyesは、オンタリオ州高等裁判所の公開裁判記録およびカナダ政府の公式報告書に基づく事実確認を徹底しています：

1. 公式裁判記録および司法判決:
• オンタリオ州高等裁判所 — ポール・ベルナルド公判記録（1995年、パトリック・ルサージュ裁判長、無期限拘禁「危険犯」認定）: https://www.canlii.org/
• オンタリオ州司法長官事務所 — カーラ・ホモルカ司法取引協定書（1993年5月、懲役12年）: https://www.ontario.ca/
• オンタリオ州控訴裁判所 — ベルナルド控訴棄却決定（1997年）: https://www.canlii.org/

2. 独立司法調査報告書および制度改革:
• パトリック・ギャリガン元判事 (1996) — 司法取引検察判断に関する独立調査委員会報告書（ギャリガン・レポート）。
• アーチー・キャンベル判事 (1999) — 警察組織間連携および全国凶悪犯罪連係システム（ViCLAS）刷新調査報告書（キャンベル・レポート）。

3. 調査報道および専門書:
• スティーブン・ウィリアムズ —『Invisible Darkness: The Strange Case of Paul Bernardo and Karla Homolka』: https://www.penguinrandomhouse.ca/
• ニック・プロン —『Lethal Marriage: The Unspeakable Crimes of Paul Bernardo and Karla Homolka』: https://www.torontostar.com/

4. 行動科学および心理学分析枠組み:
• ロバート・ヘア博士 — サイコパシー・チェックリスト改訂版（PCL-R）: https://www.hare.org/
• 感応精神病（フォリー・ドゥ／共有妄想）、被害者面の心理操作、道徳的中和技術の臨床分析。

5. 相談窓口・支援ホットライン:
• こころの健康相談統一ダイヤル（日本）: 0570-064-556
• よりそいホットライン: 0120-279-338 (24時間通話無料) — https://www.thenewjapan.org/
• 児童相談所虐待対応ダイヤル: 189 (いちはやく・無料)
"""

SOURCES_KO = """📚 제11화 참고 문헌 및 공식 수사 기록 (폴 베르나르도와 카를라 호몰카)
Amber eyes는 온타리오주 법원의 공식 공판 기록 및 캐나다 사법부의 공인 문서를 바탕으로 사실 확인을 거쳤습니다:

1. 공식 법원 공판 기록 및 사법 판결:
• 온타리오주 고등법원 — 폴 베르나르도 1심 판결문 (1995년 패트릭 르세이지 판사, 종신형 및 위험한 범죄자 지정): https://www.canlii.org/
• 온타리오주 법무장관실 — 카를라 호몰카 유죄 인정 형량 협상 합의서 (1993년 5월, 징역 12년): https://www.ontario.ca/
• 온타리오주 항소법원 — 베르나르도 항소 기각 판결 (1997 CanLII 1256): https://www.canlii.org/

2. 독립 사법 조사 보고서 및 제도 개혁:
• 패트릭 갤리건 전 판사 (1996) — 검찰 기소 및 협상 과정에 대한 독립 사법 조사 보고서 (갤리건 리포트).
• 아치 캠벨 판사 (1999) — 수사 기관 간 정보 단절 및 전국 연쇄 강력범죄 연계 분석 시스템(ViCLAS) 개혁 보고서 (캠벨 인콰이어리).

3. 탐사 보도 및 범죄학 전문 저술:
• 스티븐 윌리엄스 — 'Invisible Darkness: The Strange Case of Paul Bernardo and Karla Homolka': https://www.penguinrandomhouse.ca/
• 닉 프론 — 'Lethal Marriage: The Unspeakable Crimes of Paul Bernardo and Karla Homolka': https://www.torontostar.com/

4. 행동과학 및 심리학적 분석 틀:
• 로버트 헤어 박사 — 사이코패스 체크리스트(PCL-R) 임상 평가 기준: https://www.hare.org/
• 감응성 정신병(폴리 아 되), 조작적 피해자 코스프레, 도덕적 중화 기술(Sykes & Matza) 분석.

5. 긴급 상담 및 지원 핫라인:
• 자살예방 상담전화 (한국): 109 (24시간 무료)
• 정신건강 상담전화: 1577-0199 / 여성긴급전화: 1366 / 아동학대: 112
"""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Tập 11: Cặp Đôi Ken & Barbie — Thỏa Thuận Với Quỷ Dữ | Tâm lý học tội phạm: Paul Bernardo & Karla Homolka (10 Chỉ Dấu Tâm Lý & 4 Nấc Thang Vực Thẳm) | Amber eyes

Đầu thập niên 1990, tại Port Dalhousie (Ontario, Canada), ngôi nhà sơn hồng số 57 Bayview Drive là tổ ấm kiểu mẫu của Paul Bernardo và Karla Homolka — cặp vợ chồng trẻ xinh đẹp như búp bê Ken & Barbie bước ra đời thực. Thế nhưng phía sau khung cửa sổ màu hồng là một địa ngục kinh hoàng reo rắc nỗi khiếp đảm khắp miền Nam Ontario. Khi Scarborough Rapist sa lưới và bản hợp đồng gây phẫn nộ 'Thỏa thuận với Quỷ dữ' được ký kết, sự thật về 6 cuộn băng video giấu trên trần nhà đã phơi bày điều gì về cơ chế Điên cuồng đôi và nghệ thuật thao túng đóng vai nạn nhân?

Hồ sơ Paul Bernardo & Karla Homolka được Amber eyes giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (§A2c):
1. DƯ CHẤN XÃ HỘI & NỖI HOANG TƯỞNG TẬP THỂ: Scarborough và Niagara chìm trong sợ hãi suốt 5 năm khi phụ nữ sợ ra đường đêm; làn sóng phẫn nộ dữ dội đòi xé bỏ thỏa thuận nhận tội khi 6 cuộn băng rò rỉ; hai cuộc điều tra độc lập Galligan và Campbell dẫn đến đại cải tổ hệ thống ViCLAS toàn Canada.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem nạn nhân là đạo cụ dùng một lần thỏa mãn cơn nghiện quyền lực; Karla giáng cấp em ruột Tammy thành 'vật hiến tế' giữ tình cảm; khuyết tật Thuyết tâm trí biến tiếng van xin thành trở ngại cần loại bỏ.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Khóa chặt ngăn người vợ hiền yêu thú y và ngăn đồng lõa săn mồi; đám cưới xe ngựa cổ tích tại Niagara-on-the-Lake là 'Lá chắn bình thường hóa' giúp Karla tự huyễn hoặc về phẩm giá bản thân.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Karla vào tù với nụ cười kín đáo, mãn hạn 12 năm với sự tự thương hại bệnh lý; Bernardo tại trại Millhaven liên tục xin ân xá trong trạng thái sụp đổ cái tôi ái kỷ kéo dài.
5. HỆ THỐNG TỰ BÀO CHỮA & THAO TÚNG ĐÓNG VAI NẠN NHÂN: Dùng kỹ thuật trung hòa đạo đức ('chỉ làm để chiều chồng'); khoác chiếc mặt nạ 'Hội chứng Người phụ nữ bị Bạo hành' biến tội ác chủ động thành cưỡng ép nhằm trốn án chung thân.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY SINH TỒN: Tháng 1/1993, Paul tấn công Karla bằng đèn pin lớn; bạo lực đánh tan ảo tưởng tình yêu, kích hoạt bản năng sinh tồn khiến Karla trốn khỏi 57 Bayview Drive và chủ động bán đứng Paul để mua quyền miễn tố.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO (đe dọa, thuốc an thần, xi măng giấu xác ở Lake Gibson) liên tục đổi; Signature bất biến là nhu cầu bắt buộc ghi hình video toàn bộ tội ác và ép nạn nhân dùng danh xưng phục tùng.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: 4 nấc thang: (1) Rình rập ngoại ô Scarborough -> (2) Lập cặp đôi và xâm phạm người thân (Tammy, 1990) -> (3) Giam cầm tại 57 Bayview Drive (Leslie, 1991) -> (4) Bắt cóc công khai ban ngày (Kristen, 1992).
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc búp bê vàng, xe mui trần, nhà màu hồng ru ngủ trực giác cộng đồng; định kiến giới khiến cơ quan công tố mặc định phụ nữ trẻ đẹp luôn là nạn nhân, không thể là kẻ chủ mưu.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ SINH TỒN: Tôn vinh phẩm giá và sự kiên cường của Kristen French; 4 cảnh báo đỏ thực tế (The Gift of Fear): Kẻ lạm dụng tổn thương, Bất nhất giữa lời nói và hành vi lén lút, Sự tiếp cận của người có vẻ vô hại, và Nhận diện liên minh cộng sinh độc hại.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Vỏ bọc hoàn hảo của Cặp đôi Ken & Barbie
05:00 Hồi 2 · Hiện trường & Vực thẳm leo thang — 4 nấc thang tội ác
10:00 Hồi 3 · Giải mã liên minh bệnh hoạn — Điên cuồng đôi & Trung hòa đạo đức
15:30 Hồi 4 · Thỏa thuận với Quỷ dữ & Sự sụp đổ của mặt nạ nạn nhân
21:00 Hồi 5 · Phán quyết, di chứng tư pháp & Bài học cảnh báo đỏ

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai của Tòa Thượng thẩm Ontario và các báo cáo điều tra Canada. Kênh không tôn vinh hay bôi nhọ bất kỳ ai.
• Hình tượng Cú, Sói, Cáo, Cừu, Mèo là linh thú nghệ thuật. Giọng đọc, hình ảnh và âm thanh có ứng dụng AI.

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• Bản án xét xử Paul Bernardo (1995, Ontario Court) — https://www.canlii.org/
• Hồ sơ Thỏa thuận nhận tội Karla Homolka (1993) — https://www.ontario.ca/
• Báo cáo điều tra độc lập Patrick Galligan (1996) & Archie Campbell (1999)
• Stephen Williams: 'Invisible Darkness' & Nick Pron: 'Lethal Marriage'
• Thang đo PCL-R của Robert Hare & Phân tích Folie à Deux — https://www.hare.org/

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ & BẢO VỆ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng hỗ trợ phụ nữ bị bạo lực gia đình: 1900 969 680

#AmberEyes #TrueCrime #TamLyToiPham #PaulBernardo #KarlaHomolka #KenAndBarbie #ThoaThuanVoiQuyDu #DienCuongDoi #FolieADeux #10ChiDauTamLy #CanhBaoDo #HoSoToiPham"""

DESC_EN = """Ep. 11: The Ken & Barbie Killers — Deal with the Devil | Criminal Psychology: Paul Bernardo & Karla Homolka (10 Psychological Markers & 4 Escalation Stages) | Amber eyes

In the early 1990s, in Port Dalhousie (Ontario, Canada), an idyllic pink home at 57 Bayview Drive stood as the perfect domestic facade for Paul Bernardo and Karla Homolka — a glamorous young couple appearing like living dolls of Ken and Barbie. Yet behind those pink walls lay a terrifying chamber terrorizing Southern Ontario. When the Scarborough serial predator was unmasked and the controversial 'Deal with the Devil' plea agreement signed, what did the 6 covert videotapes hidden in the ceiling reveal about Folie à Deux and manipulative victimhood?

Amber eyes dissects the case through our 10-Indicator Behavioral & Psychological Ecosystem (§A2c):
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: 5 years of collective paranoia in Scarborough and Niagara; nationwide fury demanding deal cancellation once videotapes leaked; landmark Galligan and Campbell inquiries driving nationwide overhaul of Canada's ViCLAS violent crime system.
2. OBJECTIFICATION OF THE VICTIM: Treating victims as disposable instruments feeding grandiosity and dominance; Karla coldly degrading sister Tammy into a 'sacrificial offering'; crippled Theory of Mind viewing pleas as obstacles to suppress.
3. COGNITIVE COMPARTMENTALIZATION: Strictly walling off the veterinary assistant persona from the cold accomplice; fairytale carriage wedding in Niagara-on-the-Lake acted as a 'Shield of Normalcy' preserving an unblemished self-image.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: Karla entered custody with a subtle smile, serving 12 years steeped in pathological self-pity; inside Millhaven, Bernardo files futile parole bids in chronic narcissistic collapse.
5. TECHNIQUES OF NEUTRALIZATION & MANIPULATIVE VICTIMHOOD: Deploying moral neutralization ('pleasing her husband'); masterfully donning the 'Battered Woman Syndrome' mask to reframe active depravity as helpless coercion, escaping whole-life prison.
6. PSYCHOLOGICAL TRIGGER & SURVIVAL TIPPING POINT: In Jan 1993, Bernardo battered Karla with a heavy flashlight, hospitalizing her; violence shattered illusions, activating survival panic prompting her to flee and preemptively trade evidence.
7. SIGNATURE VS. MODUS OPERANDI (MO): MO (coercion tools, sedatives, concrete disposal in Lake Gibson) evolved; immutable Signature was the compulsive need to document crimes on videotape and force subservient titles.
8. FANTASY ADDICTION & 4 ESCALATION STAGES: (1) Nocturnal ambushes in Scarborough -> (2) Predatory partnership and violating family (Tammy, 1990) -> (3) Confinement at 57 Bayview Drive (Leslie, 1991) -> (4) Brazen daytime abductions (Kristen, 1992).
9. HALO EFFECT & COLLECTIVE BLIND SPOTS: Golden couple aesthetics, convertible car, and pink house blinded the community; prosecutorial gender bias reflexively assumed an attractive blonde woman could only be a victim, never a predator.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Honoring the defiant courage of Kristen French who preserved crucial forensic DNA; 4 pragmatic survival red flags (The Gift of Fear): Weaponizing trauma, Dissonance between rhetoric and conduct, Disarming approaches, and Toxic codependency.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Disclaimer
00:23 Act 1 · The Perfect Facade of Ken & Barbie
05:00 Act 2 · Crime Scene & The Escalation Abyss — 4 Stages of Depravity
10:00 Act 3 · Dissecting the Symbiotic Alliance — Folie à Deux & Neutralization
15:30 Act 4 · The Deal with the Devil & The Collapse of the Victim Mask
21:00 Act 5 · Verdict, Institutional Reckoning & Survival Red Flags

⚠️ LEGAL & SAFETY DISCLAIMER
• Educational and historical documentary on criminal psychology; does not replace medical or legal advice.
• Derived from public transcripts of the Ontario Superior Court and verified Canadian inquiry reports. Does not glorify or defame any individual.
• Narrator animal avatars are artistic motifs. Narration, visuals, and soundscapes are AI-assisted.

📚 VERIFIED HISTORICAL & LEGAL DOSSIER
• R. v. Bernardo (1995, Ontario Court Ruling) — https://www.canlii.org/
• Karla Homolka Plea Agreement Archives (1993) — https://www.ontario.ca/
• Independent Inquiries: Patrick Galligan (1996) & Archie Campbell (1999)
• Books: 'Invisible Darkness' (S. Williams) & 'Lethal Marriage' (N. Pron)
• Dr. Robert Hare: PCL-R Psychopathy Checklist & Folie à Deux Analysis — https://www.hare.org/

🆘 CRISIS HOTLINES & SUPPORT
• 988 Crisis & Mental Health Lifeline (US/Canada, toll-free 24/7): Dial 988 — https://988lifeline.org/
• Canadian Centre for Child Protection: https://www.protectchildren.ca/
• National Domestic Violence Hotline: 1-800-799-SAFE (7233) — https://www.thehotline.org/

#AmberEyes #TrueCrime #CriminalPsychology #PaulBernardo #KarlaHomolka #KenAndBarbie #DealWithTheDevil #FolieADeux #10PsychologicalMarkers #SurvivalRedFlags #CaseFile"""

DESC_JA = """第11話: ケンとバービーの仮面 — 悪魔との取引 | 犯罪心理学: ポール・ベルナルドとカーラ・ホモルカ（10の心理指標と4段階のエスカレーション） | Amber eyes

1990年代初頭、カナダ・オンタリオ州の湖畔の町ポート・ダルハウジー。Bayview Drive 57番地に佇むピンク色の家は、ポール・ベルナルドとカーラ・ホモルカという、まるで現実世界の『ケンとバービー』人形のような美男美女カップルの城でした。しかしピンクの窓枠の奥には、オンタリオ州南部を戦慄させた捕食同盟の地獄が口を開けていたのです。スカーバローの連続暴行魔の正体が暴かれ、『悪魔との取引』と刻まれた前代未聞の司法取引が成立した後、天井裏から発見された6本の隠しビデオテープは何を暴いたのか。

Amber eyesは、本事件を「10の心理・行動指標エコシステム（§A2c）」から深層解剖します：
1. 社会的余波と集団的パラノイア: スカーバローとナイアガラを5年間にわたり襲った夜間外出の恐怖; ビデオテープ流出後に沸騰した協定破棄を求める数十万の怒りの署名; ギャリガン元判事とキャンベル判事の独立調査が促した全国凶悪犯罪連係システム（ViCLAS）の大刷新。
2. 被害者の客体化（モノ扱い）: 支配中毒と誇大妄想を満たすための使い捨ての道具として被害者を認識; カーラが実妹タミーを愛人関係を繋ぎ止める『生贄の供物』として差し出した冷酷さ; 他者の苦痛を慮る『心の理論』の致命的欠如。
3. 心理的区画化（精神の分断）: 動物病院の良妻という人格と冷酷な捕食者の共犯者という人格を完全に別々の引き出しに隔離; おとぎ話のような馬車挙式が自らの無謬性を思い込ませる『正常性の防壁』として機能。
4. 自己愛の崩壊と病的な自己憐憫: 懲役12年の刑期を勝ち取り密かな笑みで収監されたカーラの徹底した自己憐憫; ミルヘイブン刑務所内で他者への責任転嫁と不毛な仮釈放申請を続けるベルナルドの長期自己愛崩壊。
5. 自己正当化と被害者面の心理操作: 「家庭を守り夫を喜ばせるためだった」という道徳的中和技術; 1993年1月の家庭内暴力を利用し『虐待された女性の症候群』の衣を纏って終身刑を逃れた冷徹なサイコパス的欺瞞。
6. 心理的引き金と生存の転換点: 1993年1月、大型懐中電灯によるベルナルドの激しい暴行が引き金となり、生存本能が覚醒; 自宅から脱出したカーラが保身のために夫を売り渡す裏切りの決断。
7. 署名（Signature）対 手口（MO）: 脅迫具、動物用鎮静剤、セメントによる証拠隠滅という手口（MO）の背後に、犯行の全容をビデオテープに記録し屈辱的呼称を強要するという絶対支配の心理的署名（Signature）が不変。
8. 妄想への耽溺と4段階のエスカレーション: (1) 単独での夜間襲撃 -> (2) 共犯ペア結成と身内への侵害（タミー、1990） -> (3) 自宅での長期監禁（レスリー、1991） -> (4) 白昼の教会駐車場からの大胆な拉致（クリステン、1992）。
9. 後光効果（ハロー効果）と社会的盲点: 金髪の美男美女、スポーツカー、ピンクの邸宅が街全体の警戒心を麻痺; 若く魅力的な女性は冷酷な捕食者ではなく被害者であるはずだという捜査陣のジェンダー盲点。
10. 被害者学と4つの生存レッドフラッグ: 自衛の中で爪痕を残しDNA証拠を保持したクリステン・フレンチの類まれなる気高さ; 4つの生存警告（The Gift of Fear）: 過去の傷を武器にする者、言説と陰の行動の乖離、無害に見える人物の接近、有害な共依存同盟。

⏱ タイムスタンプ
00:00 イントロ＆注意事項
00:23 第1幕 · 『ケンとバービー』完璧な仮面の裏側
05:00 第2幕 · 犯行現場と深まるエスカレーション――4段階の凶行の軌跡
10:00 第3幕 · 病的な共生の解剖――共有妄想（フォリー・ドゥ）と道徳の中和
15:30 第4幕 · 悪魔との取引と被害者面の崩壊
21:00 第5幕 · 判決、制度の刷新と生存のための4つの赤い警告

⚠️ 法的留意事項および安全性
• 本動画は犯罪心理学および歴史的資料に基づく教育的コンテンツであり、医学的・心理的・法的助言に代わるものではありません。
• オンタリオ州高等裁判所の公開裁判記録および公式報告書に依拠しています。
• 動物キャラクターは芸術的演出の象徴です。音声、映像、音響はAI技術を活用しています。

📚 公式参考文献・調査資料
• ポール・ベルナルド判決公刊記録 (1995) — https://www.canlii.org/
• カーラ・ホモルカ司法取引協定記録 (1993) — https://www.ontario.ca/
• ギャリガン報告書 (1996) & キャンベル報告書 (1999)
• スティーブン・ウィリアムズ:『Invisible Darkness』& ニック・プロン:『Lethal Marriage』
• ロバート・ヘア博士: PCL-Rチェックリスト — https://www.hare.org/

🆘 相談窓口・支援ホットライン
• こころの健康相談統一ダイヤル: 0570-064-556
• よりそいホットライン (24時間無料): 0120-279-338 — https://www.thenewjapan.org/
• 児童相談所虐待対応ダイヤル: 189 (いちはやく・通話料無料)

#AmberEyes #TrueCrime #犯罪心理学 #ポールベルナルド #カーラホモルカ #ケンとバービー #悪魔との取引 #感応精神病 #フォリードゥ #10の心理的指標 #事件ファイル"""

DESC_KO = """제11화: 켄과 바비 커플의 가면 — 악마와의 거래 | 범죄심리학: 폴 베르나르도와 카를라 호몰카 (10대 핵심 심리 지표 및 4단계 에스컬레이션) | Amber eyes

1990년대 초반, 캐나다 온타리오주 포트 달하우지의 베이뷰 드라이브 57번지. 화사한 분홍빛 주택은 폴 베르나르도와 카를라 호몰카라는, 현실판 ‘켄과 바비’ 인형처럼 완벽해 보이던 신혼부부의 안식처였습니다. 그러나 그 눈부신 가면 뒤에는 남부 온타리오 전역을 공포에 떨게 한 기괴한 연쇄 범죄의 지옥이 똬리를 틀고 있었습니다. 스카버러 연쇄 포식자의 가면이 벗겨지고 ‘악마와의 거래’로 불린 충격적인 형량 거래가 성립된 후, 욕실 천장 속에서 회수된 6개의 은밀한 비디오테이프는 어떤 진실을 폭로했을까요?

Amber eyes는 본 사건을 ‘10대 핵심 심리·행동 지표 생태계(§A2c)’를 통해 정밀 해부합니다:
1. 사회적 파장과 집단적 공포: 5년간 스카버러와 나이아가라 전역을 집어삼킨 밤거리 공포; 비디오 유출 후 분노한 수십만 시민의 형량 거래 파기 청원; 갤리건 전 판사와 캠벨 판사의 독립 조사가 이끌어낸 전국 강력범죄 연계 분석 시스템(ViCLAS)의 대대적 혁신.
2. 피해자의 객체화(사물화): 지배욕과 과대망상을 충족하기 위한 일회성 소품으로 피해자를 취급; 카를라가 애정 결속을 위해 친동생 타미를 ‘제물’로 전락시킨 잔혹성; 타인의 고통을 인지하지 못하는 ‘마음의 이론’ 결핍.
3. 심리적 구획화(정상성의 방패): 자상한 동물병원 직원이라는 서랍과 냉혹한 공범자라는 서랍을 철저히 분리; 나이아가라온더레이크의 동화 같은 마차 결혼식이 스스로를 품위 있는 존재로 착각하게 만든 견고한 ‘정상성의 방패’ 역할.
4. 나르시시즘적 붕괴와 병적 자기연민: 12년 형을 받고 은밀한 미소를 지으며 수감된 카를라의 만성적 자기연민; 밀헤이븐 교도소에서 남 탓만 일삼으며 헛된 가석방을 거듭 신청하는 베르나르도의 나르시시즘적 자아 붕괴.
5. 자기 정당화 및 피해자 코스프레: “남편을 만족시키고 가정을 지키려 했을 뿐”이라는 도덕적 중화 기술; 1993년 1월의 가정폭력을 영악하게 이용하여 ‘매 맞는 여성 증후군’의 가면을 쓰고 종신형을 회피한 냉혹한 심리 조작술.
6. 심리적 방아쇠와 생존의 티핑 포인트: 1993년 1월 대형 손전등을 이용한 남편의 폭행이 계기가 되어 낭만적 착각 붕괴; 생존 본능이 깨어나 베이뷰 드라이브를 탈출한 카를라가 기소 면제를 위해 베르나르도를 전격 배신한 계기.
7. 시그니처(Signature) vs 범행 수법(MO): 도구 사용, 동물 진정제 투여, 시멘트 수중 은닉 등 수법(MO)은 진화했으나, 범행의 전 과정을 비디오테이프로 기록하고 굴종적 호칭을 강요한 것은 절대적 지배를 확인하려는 변치 않는 심리적 시그니처.
8. 환상 중독과 4단계 에스컬레이션: (1) 스카버러 야간 단독 기습 -> (2) 공범 결성 및 친족 침해(타미 호몰카, 1990) -> (3) 자택 장기 감금(레슬리 마하피, 1991) -> (4) 교회 주차장 대낮 공개 납치(크리스틴 프렌치, 1992).
9. 후광 효과(Halo Effect)와 사회적 맹점: 금발의 외모, 컨버터블 스포츠카, 분홍빛 주택이 온 동네의 경계심을 마비; 젊고 매력적인 여성은 잔혹한 포식자가 아니라 피해자일 것이라는 사법 당국의 성별 고정관념 맹점.
10. 피해자학 및 생존을 위한 4가지 레드플래그: 목숨 건 저항으로 가해자의 DNA 증거를 남긴 크리스틴 프렌치의 불굴의 용기 기림; 생존을 위한 4대 적신호(The Gift of Fear): 개인적 상처의 무기화 경계, 도덕적 언행 불일치 식별, 무해해 보이는 사람의 접근 주의, 유해한 공생 관계 단절.

⏱ 챕터 타임스탬프
00:00 인트로 및 안내
00:23 제1막 · 켄과 바비 완벽한 가면의 이면
05:00 제2막 · 현장 분석과 파멸의 에스컬레이션 – 범죄의 4단계 궤적
10:00 제3막 · 병적 공생 관계의 해부 – 감응성 정신병과 도덕적 중화
15:30 제4막 · 악마와의 거래와 산산조각 난 피해자 가면
21:00 제5막 · 사법 판결, 제도의 쇄신과 생존의 적신호

⚠️ 법적 고지 및 안내
• 본 영상은 범죄심리학 및 역사적 자료에 기반한 교육용 콘텐츠이며, 의학적·심리학적·법률적 자문을 대신할 수 없습니다.
• 온타리오주 고등법원 판결문 및 캐나다 공인 조사 보고서에 기반합니다.
• 동물 캐릭터는 예술적 연출을 위한 가상 캐릭터입니다. 내레이션, 이미지, 음향 제작에 AI 기술이 활용되었습니다.

📚 공식 참고 문헌 및 수사 기록
• 폴 베르나르도 유죄 판결 기록 (1995) — https://www.canlii.org/
• 카를라 호몰카 형량 협상 합의 문서 (1993) — https://www.ontario.ca/
• 패트릭 갤리건 보고서 (1996) & 아치 캠벨 보고서 (1999)
• 스티븐 윌리엄스: 'Invisible Darkness' & 닉 프론: 'Lethal Marriage'
• 로버트 헤어 박사: PCL-R 사이코패스 체크리스트 — https://www.hare.org/

🆘 긴급 상담 및 도움 핫라인
• 자살예방 상담전화: 109 (24시간 무료)
• 정신건강 상담전화: 1577-0199 / 여성긴급전화: 1366 / 아동학대: 112

#AmberEyes #TrueCrime #범죄심리학 #폴베르나르도 #카를라호몰카 #켄과바비 #악마와의거래 #감응성정신병 #폴리아되 #10가지심리적지표 #생존레드플래그 #사건파일"""

# ==============================================================================
# HÀM GHI FILE & KIỂM ĐỊNH KÍCH THƯỚC
# ==============================================================================

def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    clean_content = content.strip().replace("\r\n", "\n").replace("\r", "\n")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(clean_content + "\n")


def main():
    print("=== ĐO LƯỜNG ĐỘ DÀI MÔ TẢ TẬP 11 (TRẦN: 5000 KÝ TỰ) ===")
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
        
    print("\n=== TIẾN HÀNH XUẤT BẢN FILE MÔ TẢ & NGUỒN TẬP 11 ===")
    
    files_to_write = [
        # Tiếng Việt
        (ROOT / "02_SAN_XUAT" / "Tap11" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap11" / "xuat_ban" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap11" / "nguon_mo_ta.txt", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap11" / "nguon_tham_khao.md", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap11" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),
        
        # Tiếng Anh
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "xuat_ban" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap11_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),
        
        # Tiếng Nhật
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "xuat_ban" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap11_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),
        
        # Tiếng Hàn
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "xuat_ban" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap11_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
    ]
    
    for path, content in files_to_write:
        write_text(path, content)
        print(f"  -> Đã ghi: {path.relative_to(ROOT)} ({len(content.strip()):,} ký tự)")
        
    print("\n>>> TẤT CẢ FILE MÔ TẢ TẬP 11 ĐÃ ĐƯỢC CẬP NHẬT HOÀN TẤT VÀ ĐẠT CHUẨN! <<<")


if __name__ == "__main__":
    main()
