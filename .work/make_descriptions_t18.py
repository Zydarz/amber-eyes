# -*- coding: utf-8 -*-
"""Generate comprehensive descriptions and source files for Tap 18 across 4 languages.
Ensures full coverage of 10 Psychological Indicators (§A2c) and strictly <= 5000 characters.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO GỌN CHO FILE NGUỒN TẬP 18
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 18 (LORI VALLOW & CHAD DAYBELL)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp công khai của Tòa án Hạt Ada và FBI:

1. Hồ sơ tòa án & Phán quyết tư pháp chính thức:
• Tòa án Hạt Ada (Boise, Idaho) — Bản án xét xử Lori Vallow Daybell (7/2023, Thẩm phán Steven Boyce; 3 án chung thân liên tiếp không ân xá): https://coi.isc.idaho.gov/
• Tòa án Hạt Ada (Boise, Idaho) — Bản án tử hình Chad Guy Daybell (6/2024, Thẩm phán Steven Boyce): https://coi.isc.idaho.gov/
• Hồ sơ truy tố đại bồi thẩm đoàn Hạt Fremont & Hạt Madison (Idaho, 2020-2021).

2. Báo cáo điều tra thực địa & Giám định pháp y:
• Sở Cảnh sát Rexburg — Báo cáo kiểm tra an sinh và khám xét căn hộ Rexburg (11/2019).
• Cục Điều tra Liên bang (FBI) — Báo cáo hiện trường khai quật trang trại Salem và phân tích kỹ thuật số vệ tinh (6/2020).
• Văn phòng Giám định Y khoa Hạt Ada — Báo cáo khám nghiệm pháp y tử thi Tylee Ryan, JJ Vallow và Tammy Daybell.

3. Tư liệu điều tra báo chí & Chuyên khảo tội phạm học:
• Nate Eaton (East Idaho News) — Chuỗi phóng sự điều tra hiện trường và phỏng vấn tại Kauai, Hawaii.
• Leah Sottile — Tác phẩm tư liệu 'When the Moon Turns to Blood: Lori Vallow, Chad Daybell, and a Story of Murder, Faith, and End Times'.

4. Tâm lý học hành vi:
• Rối loạn hoang tưởng chia sẻ (Folie à Deux), Cơ chế Phi nhân tính hóa (Dehumanization) & The Gift of Fear (Gavin de Becker).

5. Đường dây nóng hỗ trợ & bảo vệ:
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7): http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng phòng chống bạo lực gia đình: 1900 969 680
"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 18 (LORI VALLOW & CHAD DAYBELL)
Amber eyes adheres to multi-source verification using verified public court records and official filings:

1. Official Court Transcripts & Judicial Rulings:
• District Court of the Seventh Judicial District (Ada County, Idaho) — State of Idaho v. Lori Norene Vallow (Judge Steven W. Boyce; consecutive life sentences): https://coi.isc.idaho.gov/
• District Court of the Seventh Judicial District (Ada County, Idaho) — State of Idaho v. Chad Guy Daybell (Judge Steven W. Boyce; Judgment of Death, June 2024): https://coi.isc.idaho.gov/

2. Forensic Pathology & Law Enforcement Reports:
• Rexburg Police Department — Emergency welfare check records and search warrants (Nov 2019).
• FBI Evidence Response Team — Excavation records and cellular geofence data (Salem property, June 2020).
• Ada County Coroner Office — Forensic autopsy reports for Tylee Ryan, JJ Vallow, and Tamara Daybell.

3. Investigative Journalism & Monographs:
• Nate Eaton (East Idaho News) — Comprehensive investigative reporting and field interviews.
• Leah Sottile — 'When the Moon Turns to Blood: Lori Vallow, Chad Daybell, and a Story of Murder, Faith, and End Times'.

4. Behavioral Sciences Frameworks:
• Shared Delusional Disorder (Folie à Deux), Dehumanization dynamics, and Gavin de Becker's 'The Gift of Fear'.

5. Crisis Helplines & Support:
• 988 Suicide & Crisis Lifeline (US/Canada, toll-free 24/7): Dial 988 — https://988lifeline.org/
• National Center for Missing & Exploited Children: 1-800-843-5678 — https://www.missingkids.org/
• National Domestic Violence Hotline: 1-800-799-SAFE (7233) — https://www.thehotline.org/
"""

SOURCES_JA = """📚 第18話 参考文献・公式調査資料一覧（ロリ・ヴァロウとチャド・デイベル）
Amber eyesは、アイダホ州裁判所の公開裁判記録およびFBIの公認資料に基づく事実確認を徹底しています：

1. 公式裁判記録および司法判決:
• アイダホ州エイダ郡裁判所 — ロリ・ヴァロウ公判記録（2023年7月、仮釈放なき終身刑）: https://coi.isc.idaho.gov/
• アイダホ州エイダ郡裁判所 — チャド・デイベル死刑判決宣告記録（2024年6月）: https://coi.isc.idaho.gov/

2. 法科学捜査報告書および検視記録:
• レックスバーグ警察署 — 緊急安否確認および家宅捜索報告書（2019年11月）。
• 連邦捜査局（FBI） — セイラム農場発掘調査およびGPS基地局分析記録（2020年6月）。
• エイダ郡検視局 — タイリー、JJ、タミーの法医学解剖鑑定書。

3. 調査報道および専門書:
• ネイト・イートン（East Idaho News） — 現場追跡報道記録。
• リア・ソッティーレ —『When the Moon Turns to Blood』。

4. 相談窓口・支援ホットライン:
• こころの健康相談統一ダイヤル: 0570-064-556 / よりそいホットライン: 0120-279-338 / 児童相談所: 189
"""

SOURCES_KO = """📚 제18화 참고 문헌 및 공식 수사 기록 (로리 밸로우와 채드 데이벨)
Amber eyes는 아이다호주 법원의 공식 공판 기록 및 FBI 공인 문서를 바탕으로 사실 확인을 거쳤습니다:

1. 공식 법원 공판 기록 및 사법 판결:
• 아이다호주 에이다 카운티 법원 — 로리 밸로우 판결문 (2023년 7월, 가석방 없는 종신형): https://coi.isc.idaho.gov/
• 아이다호주 에이다 카운티 법원 — 채드 데이벨 사형 선고 판결문 (2024년 6월): https://coi.isc.idaho.gov/

2. 법의학 검시 및 수사기관 보고서:
• 렉스버그 경찰국 — 긴급 복지 점검 및 압수수색 영장 집행 기록 (2019년 11월).
• 연방수사국(FBI) — 세일럼 농장 발굴 수사 보고서 (2020년 6월).
• 에이다 카운티 검시소 — 타일리, JJ, 태미 공식 부검 감정서.

3. 긴급 상담 및 지원 핫라인:
• 자살예방 상담전화: 109 / 정신건강: 1577-0199 / 여성긴급: 1366 / 아동학대: 112
"""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Tập 18: Lời Tiên Tri Ngày Tận Thế & Ảo Tưởng Ma Quỷ — Hoang Tưởng Tôn Giáo Chia Sẻ & Bi Kịch Rexburg (Hồ Sơ Lori Vallow & Chad Daybell) | Tâm lý học tội phạm | Amber eyes

Đầu tháng 11/2019, trên bãi biển Kauai (Hawaii), một đám cưới lộng lẫy được tổ chức. Cô dâu Lori Vallow và chú rể Chad Daybell tươi cười trao nhau lời thề nguyền. Nhưng đằng sau bức tranh hạnh phúc ấy là sự thật rùng mình: người vợ 30 năm của Chad vừa qua đời đột ngột trước đó 2 tuần, và hai con của Lori — Tylee Ryan (16 tuổi) cùng cậu bé tự kỷ JJ Vallow (7 tuổi) — đã mất tích bí ẩn suốt hơn 2 tháng.

Điều gì đã biến một cựu hoa hậu quý bà và tác giả sách tôn giáo đạo mạo thành những kẻ nhúng tay vào cái chết của chính người thân? Khi hai đứa trẻ bị gán nhãn là 'Zombie' và cuộc đào tẩu sang Hawaii bị cảnh sát lột trần, sự thật dưới mảnh đất nông trại tại Salem, Idaho đã phơi bày điều gì về cơ chế Điên cuồng đôi (Folie à Deux) và sự sụp đổ của cái tôi ái kỷ ác tính?

Hồ sơ Lori Vallow & Chad Daybell được Amber eyes giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (§A2c):
1. DƯ CHẤN XÃ HỘI: Cơn chấn động khắp nước Mỹ trước hình ảnh cưới ở Hawaii đối lập với hai đứa trẻ mất tích; sự phẫn nộ thúc đẩy bang Idaho đại cải tổ quy trình kiểm tra an sinh khẩn cấp (welfare check).
2. VẬT HÓA & PHI NHÂN TÍNH HÓA (DEHUMANIZATION): Nạn nhân bị dán nhãn 'Zombie' bị quỷ chiếm giữ; khuyết tật thấu cảm biến tiếng van xin thành sự kháng cự của ác quỷ cần tiêu diệt để 'giải thoát linh hồn'.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Lori khóa chặt ngăn người mẹ mẫu mực và ngăn sát thủ vào hai thế giới riêng; Chad bình thản ăn tối cùng con ruột trên mảnh đất chôn cất nạn nhân; bi kịch sụp đổ danh tính của con trai cả Colby Ryan.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Lori trơ trẽn tuyên bố trước tòa: 'Chúa Giê-su biết không ai bị hại oan ức cả...'; Chad hèn nhát đổ tội cho người tình; nước mắt chỉ là Sự tự thương hại bệnh lý (Pathological Self-Pity) khi mất sạch danh vọng và tự do.
5. HỆ THỐNG TỰ BÀO CHỮA: Thang đo Ánh sáng và Bóng tối tự trao quyền phán xét; bóp méo giáo lý thành vũ khí thanh trừng; tự khoác áo cứu thế 144.000 người được chọn để ru ngủ lương tri và chiếm đoạt tiền bảo hiểm.
6. NGÒI NỔ TÂM LÝ & ÁP LỰC THỜI GIAN: Cuộc gặp năm 2018 tại 'Preparing a People' và mốc tận thế tự bịa (tháng 7/2020) là ngòi nổ kích hoạt chuỗi án mạng liên hoàn để dọn sạch chướng ngại và gom tiền trợ cấp.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO (dùng Alex Cox, tắt định vị, thuê kho) liên tục thay đổi; Signature bất biến là các nghi thức cầu nguyện thanh tẩy trục xuất quỷ dữ và cơn đói quyền năng tâm linh.
8. QUỸ ĐẠO LEO THANG: 4 nấc thang bạo lực: (1) Viết sách hoang tưởng -> (2) Nổ súng sát hại Charles Vallow chiếm bảo hiểm -> (3) Đoạt mạng Tylee và JJ -> (4) Đoạt mạng Tammy Daybell để tự do kết hôn.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc hoa hậu quý bà của Lori và tác giả sách tôn giáo của Chad ru ngủ trực giác cộng đồng; điểm mù khiến cảnh sát ban đầu phớt lờ lời cầu cứu của Charles Vallow.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ: Tôn vinh phẩm giá Tylee Ryan và bé JJ Vallow; 4 cảnh báo đỏ sinh tồn (The Gift of Fear): (1) Giáo chủ tự xưng vượt luật pháp; (2) Cô lập và ma quỷ hóa người thân; (3) Gieo rắc nỗi sợ tận thế để thao túng; (4) Trục lợi tài chính núp bóng tâm linh.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Bãi biển Hawaii và bí ẩn hai đứa trẻ biến mất
06:15 Hồi 2 · Khu đất nông trại và chữ ký tâm lý bệnh hoạn
12:30 Hồi 3 · Giải mã tâm lý: Folie à Deux và cơ chế phi nhân tính hóa
19:00 Hồi 4 · Đấu trí tư pháp, bản án trần thế và sự sụp đổ ái kỷ
25:30 Hồi 5 · Phán quyết lịch sử và 4 cảnh báo đỏ về tà giáo cuồng tín

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích khoa học hành vi tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai của Tòa án Hạt Ada (Idaho) và các báo cáo điều tra của FBI.
• Hình tượng Cú, Sói, Cáo, Cừu, Mèo là linh thú nghệ thuật. Giọng đọc, hình ảnh và âm thanh có ứng dụng AI.

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• Bản án Lori Vallow Daybell (2023, Thẩm phán Steven Boyce) — Tòa án Hạt Ada, Idaho
• Bản án tử hình Chad Daybell (2024, Thẩm phán Steven Boyce) — Tòa án Hạt Ada, Idaho
• Báo cáo điều tra hiện trường Rexburg Police Department & FBI
• Khung phân tích Folie à Deux, Dehumanization & The Gift of Fear (Gavin de Becker)

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ & BẢO VỆ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng phòng chống bạo lực gia đình: 1900 969 680

#AmberEyes #TrueCrime #TamLyToiPham #LoriVallow #ChadDaybell #DoomsdayMom #RexburgIdaho #FolieADeux #10ChiDauTamLy #CanhBaoDo #HoSoToiPham"""

DESC_EN = """Ep. 18: Doomsday Prophecy & Demonic Delusions — Shared Psychosis & The Tragedy of Two Children (The Lori Vallow & Chad Daybell Case) | Criminal Psychology | Amber eyes

In early November 2019, on a sun-drenched beach in Kauai, Hawaii, a picturesque wedding took place. Lori Vallow and Chad Daybell exchanged wedding rings and vows. Yet behind that romantic facade lay a horrifying reality: Chad wife of 30 years, Tammy Daybell, had died unexpectedly 2 weeks earlier, and Lori two children — 16-year-old Tylee Ryan and 7-year-old special needs son JJ Vallow — had been missing for over 2 months.

What transformed a charismatic former beauty pageant contestant and a religious author into killers of their own children? When the children were branded as 'Zombies' and their tropical escape unravelled, what did the discoveries beneath Chad Salem property reveal about Shared Delusional Disorder (Folie à Deux) and Malignant Narcissistic Collapse?

Amber eyes dissects the case through our 10-Indicator Behavioral Ecosystem (§A2c):
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: Worldwide outrage over Hawaii wedding while children vanished; exposed welfare check vulnerabilities, driving Idaho statutory reforms.
2. OBJECTIFICATION & DEHUMANIZATION: Victims labeled 'Zombies' possessed by demons; empathy deficit framing innocent pleas as demonic defiance requiring eradication to 'liberate the soul'.
3. COGNITIVE COMPARTMENTALIZATION: Lori rigidly separated devoted mother persona from cold perpetrator; Chad dined casually with children over burial grounds; identity collapse of son Colby Ryan.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: Lori unrepentantly claimed: 'Jesus knows no one was murdered...'; Chad blamed Lori and deceased brother; tears reflected self-pity over lost status.
5. TECHNIQUES OF NEUTRALIZATION: Light and Dark scale used for arbitrary condemnation; twisting scripture into murder justification; claiming 144,000 elect status to rationalize greed.
6. PRECIPITATING STRESSOR & TIME PRESSURE: 2018 'Preparing a People' meeting and manufactured July 2020 doomsday deadline acted as a catalyst for rapid homicidal purges.
7. PSYCHOLOGICAL SIGNATURE VS. MO: MO (using Alex Cox, disabling geolocations, storage units) evolved; immutable Signature was casting out rituals and compulsive spiritual supremacy.
8. FANTASY ADDICTION & 4 ESCALATION STAGES: (1) Apocalyptic writing -> (2) Charles Vallow shooting for insurance -> (3) Murder of children Tylee and JJ -> (4) Murder of Tammy Daybell.
9. HALO EFFECT & SOCIAL BLIND SPOTS: Lori pageant charm and Chad pious community standing deceived neighbors; authorities dismissed early warnings from Charles Vallow.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Honoring Tylee Ryan and JJ Vallow; 4 survival red flags (The Gift of Fear): (1) Leaders claiming exemption from law; (2) Demonizing and isolating kin; (3) Doomsday panic for obedience; (4) Financial exploitation disguised as faith.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Disclaimer
00:23 Act 1 · Hawaiian Beach and the Mystery of Two Missing Children
06:15 Act 2 · Rural Property and Forensic Discovery
12:30 Act 3 · Psychological Profiling: Folie à Deux and Dehumanization
19:00 Act 4 · Courtroom Showdown, Verdict, and Narcissistic Collapse
25:30 Act 5 · Historic Verdict and 4 Survival Red Flags

⚠️ LEGAL & SAFETY DISCLAIMER
• Educational and historical documentary on criminal psychology; does not replace medical or legal advice.
• Derived from public transcripts of Ada County District Court and verified FBI investigative records.
• Narrator animal avatars are artistic motifs. Narration, visuals, and soundscapes are AI-assisted.

📚 VERIFIED HISTORICAL & LEGAL DOSSIER
• State of Idaho v. Lori Vallow (2023, Judge Steven Boyce) — Ada County District Court
• State of Idaho v. Chad Daybell (2024, Judge Steven Boyce) — Death Penalty Ruling
• Rexburg Police Department & FBI Evidence Response Team Forensic Records
• Analytical Frameworks: Folie à Deux, Dehumanization & The Gift of Fear (G. de Becker)

🆘 CRISIS HOTLINES & SUPPORT
• 988 Suicide & Crisis Lifeline (US/Canada, toll-free 24/7): Dial 988 — https://988lifeline.org/
• National Center for Missing & Exploited Children: 1-800-843-5678 — https://www.missingkids.org/
• National Domestic Violence Hotline: 1-800-799-SAFE (7233) — https://www.thehotline.org/

#AmberEyes #TrueCrime #CriminalPsychology #LoriVallow #ChadDaybell #DoomsdayMom #RexburgIdaho #FolieADeux #10PsychologicalMarkers #SurvivalRedFlags #CaseFile"""

DESC_JA = """第18話: 終末の予言と悪霊の妄想 — 共有精神病と二人の子供の悲劇（ロリ・ヴァロウ＆チャド・デイベル事件） | 犯罪心理学 | Amber eyes

2019年11月初旬、ハワイのカウアイ島にある陽光あふれるビーチで、華やかな結婚式が執り行われました。花嫁のロリ・ヴァロウと花婿のチャド・デイベルは、満面の笑みを浮かべて指輪を交わし、永遠の愛を誓い合いました。しかし、その甘美で幸福な光景の裏には恐ろしい真実が隠されていました。チャドの約30年連れ添った妻タミーがそのわずか2週間前に急死し、ロリの二人の子供たち――16歳の娘タイリー・ライアンと自閉症を抱える7歳の養子JJ・ヴァロウ――はすでに2か月以上も消息を絶っていたのです。

かつて献身的な母であった元美人コンテスト出場者と、敬虔な宗教書の著者を、我が子の命を奪う凶行へと駆り立てたものは何だったのか。子供たちを「ゾンビ」と呼び、ハワイへの逃避行の末に逮捕された後、アイダホ州セイラムの農場の地下から暴かれた真実は、共有精神病（フォリアドゥ）と悪性自己愛の崩壊について何を物語るのか。

Amber eyesは、本事件を「10の心理・行動指標エコシステム（§A2c）」から深層解剖します：
1. 社会的余波と集団的パラノイア: ハワイ挙式と子供たちの失踪のコントラストが全米の怒りに火をつけ、脆弱な子供に対する緊急安否確認制度の法改正を促進。
2. 被害者の客体化と脱人間化（DEHUMANIZATION）: 被害者を悪霊に乗っ取られた「ゾンビ」と決めつけ、共感能力を麻痺させ、命を奪う行為を「魂の救済」と正当化。
3. 心理的区画化（精神の分断）: 慈愛に満ちた母親としての自己と冷酷な殺人者としての自己を完全に分断; チャドは遺体が埋まる庭の家で実子と平然と生活; 長男コルビーのアイデンティティ崩壊の悲劇。
4. 自己愛の崩壊と病的な自己憐憫: ロリは法廷で「イエス様は誰も殺されていないことを知っている」と開き直り、チャドは責任をなすりつけ逃亡を図る; 涙は犠牲者への追悼ではなく特権喪失への自己憐憫。
5. 自己正当化と道徳の中和技術: 「光と闇の精神スケール」による恣意的な格付け; 終末を導く14万4000人の選民思想により良心の呵責を無効化し保険金詐欺を正当化。
6. 心理的引き金と時間の切迫: 2018年の出会いと自作自演の「2020年7月終末予言」がタイムリミットとなり、邪魔者の排除と資金集めの連続殺害へと暴走。
7. 署名（SIGNATURE）対 手口（MO）: アレックス・コックスの利用、GPS遮断などの手口（MO）の背後に、悪霊祓いの清めの祈りという不変の心理的署名（Signature）が存在。
8. 妄想への耽溺と4段階のエスカレーション: (1) 終末小説執筆 -> (2) 保険金目的のチャールズ射殺 -> (3) タイリーとJJの殺害 -> (4) 結婚を急ぐための妻タミー殺害。
9. 後光効果（ハロー効果）と社会的盲点: 元ミス・コンテストの魅力的な母と敬虔な作家という仮面が地域社会を欺き、チャールズの生前の必死の警告を警察が見過ごす盲点を形成。
10. 被害者学と4つの生存レッドフラッグ: 弟を守り抜いたタイリーと無垢なJJの尊厳を追悼; 4つの生存警告（The Gift of Fear）: (1) 法の上に立つと称する指導者; (2) 家族の悪魔化と孤立化; (3) 終末恐怖による服従; (4) 信仰を隠れ蓑にした金銭的搾取。

⏱ タイムスタンプ
00:00 イントロ＆注意事項
00:23 第1幕 · ハワイのビーチと姿を消した二人の子供の謎
06:15 第2幕 · 農場と病的な心理的刻印
12:30 第3幕 · 心理解剖：フォリアドゥと脱人間化のメカニズム
19:00 第4幕 · 司法の攻防、現世の判決と自己愛の崩壊
25:30 第5幕 · 歴史的判決とカルトを見抜く4つの警報

⚠️ 法的留意事項および安全性
• 本動画は犯罪心理学および歴史的資料に基づく教育的コンテンツであり、医学的・心理的・法的助言に代わるものではありません。
• アイダホ州エイダ郡裁判所の公開裁判記録およびFBI公式報告書に依拠しています。
• 動物キャラクターは芸術的演出の象徴です。音声、映像、音響はAI技術を活用しています。

📚 公式参考文献・調査資料
• ロリ・ヴァロウ判決記録 (2023, スティーブン・ボイス裁判長) — エイダ郡裁判所
• チャド・デイベル死刑判決記録 (2024, スティーブン・ボイス裁判長)
• レックスバーグ警察署およびFBI科学捜査チーム公式調査報告書
• 犯罪心理学分析枠組み: フォリアドゥ、脱人間化、『The Gift of Fear』(G. de Becker)

🆘 相談窓口・支援ホットライン
• こころの健康相談統一ダイヤル: 0570-064-556
• よりそいホットライン (24時間無料): 0120-279-338 — https://www.thenewjapan.org/
• 児童相談所虐待対応ダイヤル: 189 (いちはやく・通話料無料)

#AmberEyes #TrueCrime #犯罪心理学 #心理分析 #ロリヴァロウ #チャドデイベル #カルト #終末予言 #フォリアドゥ #共有精神病 #10の心理指標"""

DESC_KO = """제18화: 종말의 예언과 악령의 망상 — 공유정신병과 두 아이의 비극 (로리 밸로우 및 채드 데이벨 사건) | 범죄심리학 | Amber eyes

2019년 11월 초, 하와이 카우아이섬의 눈부신 햇살이 쏟아지는 해변에서 화려한 결혼식이 열렸습니다. 신부 로리 밸로우와 신랑 채드 데이벨은 환한 미소를 지으며 반지를 교환하고 영원한 사랑을 맹세했습니다. 그러나 그 달콤하고 행복해 보이는 장면 뒤에는 끔찍한 진실이 숨어 있었습니다. 채드와 30년간 함께 살아온 아내 태미가 불과 2주 전 자택에서 돌연 숨졌고, 로리의 두 자녀인 16세 딸 타일리 라이언과 자폐를 앓던 7세 입양아들 JJ 밸로우는 이미 두 달 이상 흔적도 없이 사라진 상태였습니다.

한때 자식을 헌신적으로 사랑하던 미인대회 출신 어머니와 독실한 종교 서적 작가를 친자식들의 생명을 앗아가는 괴물로 변모시킨 것은 무엇이었을까요. 두 아이를 ‘좀비’라 부르며 하와이로 도피했던 이들이 체포된 후, 아이다호주 세일럼 농장의 차가운 흙 아래에서 드러난 진실은 공유정신병(폴리아두)과 악성 자기애적 붕괴에 대해 무엇을 증언하고 있을까요.

Amber eyes는 본 사건을 ‘10대 심리·행동 지표 생태계(§A2c)’를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 공포: 하와이 해변 결혼식과 두 아이 실종의 충격적 대비가 미국 전역을 뒤흔들었으며, 아동 긴급 복지 점검 제도의 법적 개혁을 촉발.
2. 피해자 대상화 및 비인간화 (DEHUMANIZATION): 피해자를 악령에 사로잡힌 ‘좀비’로 격하시켜 공감 능력을 마비시키고, 살해 행위를 ‘영혼을 해방하는 구원’으로 합리화.
3. 인지적 구획화 (COMPARTMENTALIZATION): 과거 다정했던 어머니로서의 자아와 냉혹한 살인자 자아를 완전히 분리; 채드는 희생자가 묻힌 마당의 집에서 친자식들과 태연히 식사; 장남 콜비 라이언의 참혹한 정체성 붕괴.
4. 자기애적 붕괴와 병적인 자기연민: 로리는 법정에서 ‘예수님은 아무도 살해당하지 않았음을 아신다’고 강변하고, 채드는 책임을 떠넘기며 감형을 시도; 눈물은 피해자에 대한 애도가 아닌 자신의 몰락에 대한 병적인 자기연민.
5. 도덕적 정당화 및 중화 기술: ‘빛과 어둠의 영적 척도’로 주변인을 자의적으로 단죄; 14만 4천 명의 선택받은 지도자라는 선민의식으로 양심을 마비시키고 보험금 갈취를 정당화.
6. 심리적 방아쇠와 시간의 압박: 2018년 첫 만남과 자작 ‘2020년 7월 종말론’이 시한폭탄 역할을 하여 방해물 제거와 보험금·연금 착복을 위한 연속 살인으로 폭주.
7. 심리적 서명 (SIGNATURE) 대 범행 수법 (MO): 알렉스 콕스 이용, 위치 추적 차단 등 수법(MO) 뒤에, 악령을 쫓는 정화의 기도와 영적 권능에 대한 갈망이라는 불변의 심리적 서명(Signature) 각인.
8. 망상 중독과 4단계 에스컬레이션: (1) 종말론 소설 집필 -> (2) 보험금을 노린 찰스 밸로우 사살 -> (3) 타일리와 JJ 살해 -> (4) 재혼을 위한 아내 태미 살해.
9. 후광 효과 (HALO EFFECT)와 사회적 맹점: 매력적인 어머니와 독실한 작가라는 외양이 이웃과 사법기관을 속여, 생전 찰스 밸로우의 절박한 구원 요청이 묵살되는 치명적 맹점 형성.
10. 피해자학 및 4대 생존 위험 신호: 동생을 지킨 타일리와 순진한 JJ의 존엄을 추모; 4대 생존 경고 신호 (The Gift of Fear): (1) 법 위에 군림하려는 교주; (2) 가족 악마화 및 고립; (3) 종말 공포를 통한 복종 강요; (4) 영성을 빙자한 재정적 착취.

⏱ 타임스탬프
00:00 인트로 & 안내사항
00:23 막 1 · 하와이 해변과 사라진 두 아이의 미스터리
06:15 막 2 · 농장 부지와 병적인 심리적 서명
12:30 막 3 · 심리 해부: 공유정신병과 비인간화 메커니즘
19:00 막 4 · 사법 공방, 현세의 판결과 자기애의 붕괴
25:30 막 5 · 역사적 판결과 사이비 집단 4대 생존 경고

⚠️ 법적 유의사항 및 안전 안내
• 본 영상은 범죄심리학 및 역사적 자료에 기반한 교육적 다큐멘터리이며 의학적, 심리학적, 법적 자문을 대체하지 않습니다.
• 아이다호주 에이다 카운티 법원의 공판 기록 및 FBI 공식 수사 보고서를 바탕으로 제작되었습니다.
• 동물 캐릭터는 예술적 연출입니다. 음성, 영상, 음향에 AI 기술이 적용되었습니다.

📚 공식 참고 문헌 및 수사 기록
• 로리 밸로우 판결문 (2023, 스티븐 보이스 판사) — 에이다 카운티 법원
• 채드 데이벨 사형 선고 판결문 (2024, 스티븐 보이스 판사)
• 렉스버그 경찰국 및 FBI 과학수사 전담반 공식 보고서
• 범죄심리학 분석 틀: 폴리아두(공유정신병), 비인간화, The Gift of Fear (G. de Becker)

🆘 긴급 상담 및 지원 핫라인
• 자살예방 상담전화: 109 (24시간 무료)
• 정신건강 상담전화: 1577-0199 / 여성긴급전화: 1366 / 아동학대 신고: 112

#AmberEyes #TrueCrime #범죄심리학 #심리분석 #로리밸로우 #채드데이벨 #사이비종교 #종말론 #폴리아두 #공유정신병 #10대심리지표"""

# ==============================================================================
# GHI FILE VÀ ĐỐI SOÁT ĐỘ DÀI KÝ TỰ (STRICTLY <= 5000 CHARS)
# ==============================================================================

TARGETS = [
    # Tiếng Việt
    (ROOT / "02_SAN_XUAT" / "Tap18" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap18" / "xuat_ban" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap18" / "nguon_tham_khao.md", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap18" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap18" / "nguon_mo_ta.txt", SOURCES_VI),
    
    # Tiếng Anh
    (ROOT / "02_SAN_XUAT" / "Tap18_EN" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap18_EN" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap18_EN" / "xuat_ban" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap18_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap18_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap18_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap18_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
    
    # Tiếng Nhật
    (ROOT / "02_SAN_XUAT" / "Tap18_JA" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap18_JA" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap18_JA" / "xuat_ban" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap18_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap18_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap18_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap18_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
    
    # Tiếng Hàn
    (ROOT / "02_SAN_XUAT" / "Tap18_KO" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap18_KO" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap18_KO" / "xuat_ban" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap18_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap18_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap18_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap18_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
]

print(">>> VIẾT VÀ KIỂM TRA ĐỘ DÀI TẤT CẢ FILE MÔ TẢ TẬP 18 <<<")
all_passed = True

desc_lengths = {
    "VN": len(DESC_VI),
    "EN": len(DESC_EN),
    "JA": len(DESC_JA),
    "KO": len(DESC_KO),
}

for lang, length in desc_lengths.items():
    status = "PASS (<= 5000)" if length <= 5000 else "FAIL (> 5000)"
    if length > 5000:
        all_passed = False
    print(f"  {lang} Description: {length} ký tự -> {status}")

for path, text in TARGETS:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text.strip() + "\n")
    print(f"  Saved: {path.relative_to(ROOT)} ({len(text)} chars)")

if all_passed:
    print("\n>>> TẤT CẢ CÁC BẢN MÔ TẢ ĐÃ ĐƯỢC TẠO HOÀN HẢO VÀ ĐỀU DƯỚI 5000 KÝ TỰ! <<<")
else:
    print("\n>>> CẢNH BÁO: CÓ BẢN MÔ TẢ VƯỢT QUÁ 5000 KÝ TỰ! <<<")
