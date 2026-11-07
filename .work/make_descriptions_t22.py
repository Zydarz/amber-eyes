# -*- coding: utf-8 -*-
"""Generate comprehensive descriptions and source files for Tap 22 across 4 languages.
Ensures full coverage of 10 Psychological Indicators (§A2c) and strictly <= 5000 characters.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO GỌN CHO FILE NGUỒN TẬP 22
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 22 (DALIA DIPPOLITO)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ tư pháp công khai của Tòa án Hạt Palm Beach và Sở Cảnh sát Boynton Beach:

1. Hồ sơ tòa án & Phán quyết tư pháp chính thức:
• Tòa án Tư pháp Khu vực 15 (Hạt Palm Beach, Florida) — Hồ sơ vụ án State of Florida v. Dalia Dippolito (Case No. 50-2009-CF-011566-AXXX-MB).
• Bản án kết tội và tuyên phạt 16 năm tù giam (Thẩm phán Glenn D. Kelley, 7/2017).
• Tòa Phúc thẩm Khu vực 4 Florida & Tòa án Tối cao Florida — Quyết định bác đơn kháng cáo (2018-2019).

2. Báo cáo điều tra thực địa & Bằng chứng kỹ thuật số:
• Sở Cảnh sát Boynton Beach — Báo cáo chiến dịch giăng bẫy nghiệp vụ (Sting Operation) và hồ sơ lời khai đối chất (8/2009).
• Video nghiệp vụ cảnh sát chìm Widy Jean ghi hình bí mật cuộc gặp gỡ trong xe hơi màu đỏ (1/8/2009).
• Băng ghi hình hiện trường giả lập và đối chất phòng hỏi cung (Chương trình Cops/Fox & Đội Điều tra Hạt Palm Beach).

3. Tư liệu điều tra báo chí & Chuyên khảo truyền hình:
• Dateline NBC — Chuyên đề điều tra đặc biệt 'On Camera: The Dalia Dippolito Case'.
• 20/20 (ABC News) — Loạt phóng sự phân tích tâm lý và phỏng vấn trực tiếp Michael Dippolito.

4. Tâm lý học hành vi:
• Rối loạn nhân cách ái kỷ ác tính (Malignant Narcissism), Cơ chế Chia ngăn nhận thức (Compartmentalization) & The Gift of Fear (Gavin de Becker).

5. Đường dây nóng hỗ trợ & bảo vệ:
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7): http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng phòng chống bạo lực gia đình: 1900 969 680
"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 22 (DALIA DIPPOLITO)
Amber eyes adheres to multi-source verification using verified public court records and official filings:

1. Official Court Transcripts & Judicial Rulings:
• 15th Judicial Circuit Court of Florida (Palm Beach County) — State of Florida v. Dalia Dippolito (Case No. 50-2009-CF-011566-AXXX-MB).
• Sentencing Order (Judge Glenn D. Kelley; 16 years hard incarceration, July 2017).
• Florida 4th District Court of Appeal & Florida Supreme Court — Appellate affirmation and certiorari denial orders.

2. Law Enforcement & Digital Forensic Records:
• Boynton Beach Police Department — Covert sting operation tactical reports, evidence custody, and interview transcripts (Aug 2009).
• Undercover surveillance footage inside red vehicle with Officer Widy Jean (August 1, 2009).
• Staged simulated crime scene and confrontation video recordings (Boynton Beach PD & Cops production).

3. Investigative Journalism & Documentaries:
• Dateline NBC — Investigative documentary: 'On Camera: The Dalia Dippolito Case'.
• 20/20 (ABC News) — In-depth forensic coverage and interviews with Michael Dippolito.

4. Crisis Helplines & Support:
• 988 Suicide & Crisis Lifeline (US/Canada, toll-free 24/7): Dial 988 — https://988lifeline.org/
• National Domestic Violence Hotline: 1-800-799-SAFE (7233) — https://www.thehotline.org/
"""

SOURCES_JA = """📚 第22話 参考文献・公式調査資料一覧（ダリア・ディッポリト事件）
Amber eyesは、パームビーチ郡裁判所の公開裁判記録およびボイントンビーチ警察の公式捜査記録に基づく事実確認を徹底しています：

1. 公式裁判記録および司法判決:
• フロリダ州第15司法地区巡回裁判所（パームビーチ郡） — ダリア・ディッポリト公判記録（事件番号 50-2009-CF-011566-AXXX-MB）。
• 有罪判決および禁錮16年実刑宣告記録（グレン・ケリー裁判長、2017年7月）。
• フロリダ州第4地区控訴裁判所およびフロリダ州最高裁判所 — 上告棄却決定記録（2018〜2019年）。

2. 法科学捜査報告書および電子的証拠:
• ボイントンビーチ警察署 — おとり捜査作戦報告書および取調べ記録（2009年8月）。
• 潜入捜査官ウィディ・ジーンによる赤い車内での極秘監視録画映像（2009年8月1日）。
• 模擬事件現場および取調室対面記録映像（ボイントンビーチ警察署およびドキュメンタリー番組『Cops』）。

3. 相談窓口・支援ホットライン:
• こころの健康相談統一ダイヤル: 0570-064-556 / よりそいホットライン: 0120-279-338 / 配偶者暴力相談支援センター: 0570-0-55210
"""

SOURCES_KO = """📚 제22화 참고 문헌 및 공식 수사 기록 (달리아 디폴리토 사건)
Amber eyes는 팜비치 카운티 법원의 공식 공판 기록 및 보인턴비치 경찰국의 공인 수사 문서를 바탕으로 사실 확인을 거쳤습니다:

1. 공식 법원 공판 기록 및 사법 판결:
• 플로리다주 제15사법순회법원 (팜비치 카운티) — 달리아 디폴리토 사건 공판 기록 (사건번호 50-2009-CF-011566-AXXX-MB).
• 유죄 판결 및 징역 16년 실형 선고서 (글렌 켈리 판사, 2017년 7월).
• 플로리다주 제4지구 항소법원 및 플로리다주 대법원 — 상고 기각 결정문 (2018-2019).

2. 수사기관 보고서 및 디지털 영상 증거:
• 보인턴비치 경찰국 — 비밀 함정 수사 작전 보고서 및 취조 녹취록 (2009년 8월).
• 위장 수사관 위디 진과 빨간색 차량 내부에서 은밀히 촬영된 잠입 감시 영상 (2009년 8월 1일).
• 모의 살인 현장 및 취조실 대면 공식 비디오 기록 (보인턴비치 경찰국 및 콥스 제작진).

3. 긴급 상담 및 지원 핫라인:
• 자살예방 상담전화: 109 / 정신건강: 1577-0199 / 여성긴급전화: 1366 / 경찰청: 112
"""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Nước Mắt Cá Sấu Của Kẻ Thuê Sát Thủ Giết Chồng — Thao Túng Trơ Trẽn & Màn Kịch Trước Máy Quay (Hồ Sơ Dalia Dippolito) | Tâm lý học tội phạm | Amber eyes

Buổi sáng ngày 5/8/2009 tại thị trấn biển Boynton Beach, Florida, một khu phố ngoại ô bỗng chốc bị phong tỏa bởi hàng chục xe cảnh sát và ống kính của chương trình truyền hình thực tế Cops. Người phụ nữ bước xuống xe là Dalia Dippolito, 26 tuổi, một người vợ trẻ mới cưới 6 tháng. Khi được sĩ quan cảnh sát báo tin chồng mình đã qua đời, một màn diễn xuất xứng tầm điện ảnh bùng nổ: Dalia ôm mặt khóc nức nở, gục đầu vào vai cảnh sát và khóc nấc từng hồi.

Thế nhưng người đàn bà ấy không ngờ rằng toàn bộ hiện trường chỉ là một cái bẫy giăng sẵn. Người chồng Michael Dippolito vẫn sống nguyên vẹn dưới sự bảo vệ của cảnh sát. Và kẻ chủ mưu thuê sát thủ lấy mạng anh chính là người vợ đang khóc lóc thảm thiết ngoài kia, với câu nói chắc nịch trong băng ghi âm bí mật: "Tôi chắc chắn khoảng năm nghìn phần trăm."

Hồ sơ Dalia Dippolito được Amber eyes giải phẫu toàn diện qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (§A2c):
1. DƯ CHẤN XÃ HỘI & TRUYỀN THÔNG: Cơn sốt truyền thông toàn cầu từ Cops, Dateline NBC; nỗi bàng hoàng của cộng đồng ngoại ô khi nhận ra tội ác tày trời ẩn náu ngay sát vách; thúc đẩy tiền lệ pháp lý về chuẩn mực giám sát chiến dịch giăng bẫy.
2. VẬT HÓA & PHI NHÂN HÓA: Michael bị giáng cấp thành "đạo cụ tài chính", vật cản pháp lý ngăn Dalia độc chiếm căn nhà 250.000$; khuyết tật thấu cảm (Affective Empathy Deficit); tiếng khóc van xin chỉ kích thích sự hưng phấn quyền lực (power arousal).
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Bộ não hai mặt khóa chặt ngăn gia đình bình thường (con gái hiếu thảo, vợ đảm đang) và ngăn bóng tối săn mồi (ngã giá với sát thủ); gia đình là tấm khiên bình thường hóa để ru ngủ lương tri; bi kịch sụp đổ danh tính của mẹ và người thân trước tòa.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Dalia bật khóc khi lãnh án 16 năm tù, nhưng đó không phải nước mắt ăn năn cho Michael mà là Sự tự thương hại bệnh lý (Pathological Self-Pity) khi mất sạch quyền kiểm soát và tự do; bản án tâm lý phơi bày sự trống rỗng đạo đức vĩnh viễn.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC: Đổ lỗi cho nạn nhân (Michael từng mang tiền án nên không xứng đáng hưởng tài sản); ngoại hóa trách nhiệm (đổ lỗi người tình cũ ép buộc, tố cảnh sát gài bẫy); ngụy biện các cuộc gặp chỉ là diễn kịch giải trí.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Biến cố kích hoạt là khi Michael ký sang tên nhà; điểm gãy xuất hiện khi Michael nghi ngờ các vụ gài bẫy trước đó và sắp hết hạn quản chế; nguy cơ bị ly hôn và hủy hợp đồng chuyển nhượng thúc đẩy Dalia hành động cấp bách.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO là thuê người ngoài, tạo ngoại phạm ở phòng gym, dùng sim rác, yêu cầu tạo hiện trường cướp; Signature bất biến là nhu cầu kiểm soát tối thượng qua phát ngôn "Tôi chắc chắn năm nghìn phần trăm" và thái độ trơ trẽn gaslighting không bao giờ nhận lỗi.
8. QUỸ ĐẠO LEO THANG: 4 nấc thang độc hại: Thao túng tình cảm -> Thúc ép sang tên nhà -> Bỏ chất lạ vào ly trà -> Gài chất cấm vào xe tống chồng vào tù -> Thuê sát thủ thủ tiêu sinh mạng.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc người vợ trẻ trung, duyên dáng, mới cưới 6 tháng khóc nức nở gục vào vai cảnh sát tạo tấm khiên tàng hình hoàn hảo, ru ngủ sự cảnh giác của xã hội suốt nhiều tháng.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ: Tôn vinh phẩm giá và sự kiên cường của Michael Dippolito; 4 cảnh báo đỏ sinh tồn (The Gift of Fear): (1) Hôn nhân chớp nhoáng gắn liền đòi hỏi tài sản; (2) Thao túng thực tại trơ trẽn (Gaslighting); (3) Cảm xúc thái quá mang tính trình diễn và thiếu thấu cảm sâu sắc; (4) Những sự cố nguy hiểm bất thường liên tục lặp lại xung quanh nạn nhân.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Màn kịch hiện trường giả & nước mắt người vợ mới cưới
06:15 Hồi 2 · Ván bài lật ngửa & nghệ thuật thao túng trơ trẽn (Gaslighting)
12:30 Hồi 3 · Giải mã tâm lý: Sự thao túng trơ trẽn & nhân cách ái kỷ ác tính
19:00 Hồi 4 · Cuộc chiến pháp lý 8 năm & bản án 16 năm tù giam
25:30 Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện kẻ thao túng trục lợi

⚠️ LƯU Ý
• Nội dung mang tính giáo dục, phân tích dưới góc nhìn tâm lý học tội phạm và pháp y hành vi; không thay thế tư vấn y khoa hay pháp lý.
• Thông tin dựa trên hồ sơ tòa án Hạt Palm Beach và báo cáo điều tra của Sở Cảnh sát Boynton Beach.

📚 NGUỒN THAM KHẢO CHÍNH
• Tòa án Hạt Palm Beach (Florida) — Hồ sơ State v. Dalia Dippolito (Case No. 50-2009-CF-011566).
• Sở Cảnh sát Boynton Beach — Báo cáo nghiệp vụ trinh sát giăng bẫy & Băng ghi hình Cops (8/2009).
• Gavin de Becker — Tác phẩm 'The Gift of Fear' về trực giác sinh tồn.

📞 TỔNG ĐÀI HỖ TRỢ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (miễn phí 24/7)
• Đường dây nóng Ngày Mai (Khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng Bạo lực gia đình: 1900 969 680

#DaliaDippolito #TamLyHocToiPham #AmberEyes #HoSoVuAn #Gaslighting #MalignantNarcissism #StingOperation #CanhBaoDoSinhTon
"""

DESC_EN = """The Crocodile Tears of a Contract Hit Mastermind — Extreme Gaslighting & The On-Camera Charade (Dalia Dippolito Case) | Forensic Psychology | Amber eyes

On the morning of August 5, 2009, in the coastal town of Boynton Beach, Florida, a quiet suburban neighborhood was suddenly swarmed by dozens of police cruisers and yellow crime tape. The eyes of neighbors and cameras from reality TV show Cops were fixed upon an approaching vehicle. Twenty-six-year-old newlywed Dalia Dippolito stepped out. When informed by an officer that her husband of six months was dead, an Oscar-worthy performance erupted: Dalia buried her face in her hands, hyperventilating and weeping uncontrollably on an officer's shoulder.

Yet she never suspected that the entire scene was a meticulously orchestrated police sting operation. Her husband, Michael Dippolito, was very much alive and entirely safe. And the mastermind who had solicited an undercover hitman to extinguish his life was none other than the grieving bride herself, caught on tape declaring: "I am about five thousand percent sure."

The Dalia Dippolito dossier is clinically examined through the 10 Psychological & Behavioral Dimensions (§A2c):
1. SOCIETAL IMPACT & MEDIA FRENZY: Global media sensation fueled by Cops, Dateline NBC, and 20/20; suburban terror at realization that deadly malice dwelt next door; establishing judicial precedents on sting operation video oversight.
2. OBJECTIFICATION & DEHUMANIZATION: Michael reduced to a financial prop and legal hurdle blocking sole ownership of a $250,000 townhouse; total affective empathy deficit; victim's pleas only stoked predatory power arousal.
3. COGNITIVE COMPARTMENTALIZATION: Double-faced cognition isolating domestic life (dutiful daughter, devoted bride) from predatory underworld dealings; family weaponized as a shield of normalcy; devastating identity collapse of her mother and relatives.
4. NARCISSISTIC COLLAPSE: Convulsive tears upon receiving a 16-year sentence reflected pathological self-pity over lost freedom rather than genuine remorse for Michael; psychological verdict exposing eternal moral emptiness.
5. TECHNIQUES OF NEUTRALIZATION: Victim blaming (exploiting Michael's past fraud conviction as moral justification); displacement of responsibility (blaming ex-lover and alleging police entrapment); minimizing murder plot as mere reality TV scripting.
6. PRECIPITATING STRESSOR & TIPPING POINT: Real estate deed transfer as the catalyst; tipping point triggered when Michael grew suspicious and approached end of probation, threatening asset revocation via divorce.
7. SIGNATURE VS. MODUS OPERANDI: MO included gym alibi, burner phones, staged burglary; behavioral signature was pathological need for absolute dominance embodied in "5000% sure" and brazen gaslighting.
8. ESCALATION TRAJECTORY: 4 toxic stages: Emotional manipulation -> Townhouse title seizure -> Spiked iced tea -> Planting illicit narcotics to revoke probation -> Hiring hitman for termination.
9. HALO EFFECT & SOCIAL BLINDSPOTS: Youthful, glamorous bride persona projecting innocence, blinding neighbors and community to lethal malice for months.
10. VICTIMOLOGY & 4 RED FLAGS: Honoring Michael Dippolito's resilience; 4 survival red flags (The Gift of Fear): (1) Rushed marriage coupled with asset pursuit; (2) Brazen gaslighting when confronted; (3) Performative emotional outbursts lacking empathy; (4) Recurring bizarre hazards clustering around victim.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Advisory
00:23 Act 1 · The Staged Crime Scene & The Newlywed's Theatrical Tears
06:15 Act 2 · Cards on the Table & Extreme Gaslighting Psychology
12:30 Act 3 · Psychological Dissection: Malignant Narcissism & Predatory Exploitation
19:00 Act 4 · The 8-Year Legal War & The 16-Year Prison Sentence
25:30 Act 5 · Awakening Lessons & 4 Red Flags Against Romantic Predation

⚠️ ADVISORY
• Educational content analyzed through forensic behavioral science; does not replace legal or medical counsel.
• Based on public court transcripts from Palm Beach County and Boynton Beach Police Department files.

📚 PRIMARY SOURCES
• 15th Judicial Circuit of Florida — State v. Dalia Dippolito (Case No. 50-2009-CF-011566).
• Boynton Beach Police Department — Tactical sting reports and undercover recordings (Aug 2009).
• Gavin de Becker — 'The Gift of Fear' (Intuitive Survival Frameworks).

📞 CRISIS HELPLINES
• 988 Suicide & Crisis Lifeline (US/Canada): Dial 988
• National Domestic Violence Hotline: 1-800-799-SAFE (7233)

#DaliaDippolito #ForensicPsychology #AmberEyes #TrueCrime #Gaslighting #MalignantNarcissism #StingOperation #PerformativeGrief #TheGiftOfFear #SurvivalRedFlags
"""

DESC_JA = """夫殺害を企てた女の偽りの涙とカメラの前での大茶番 — 極限の現実操作と悪性自己愛の解剖（ダリア・ディッポリト事件）| 犯罪心理学 | Amber eyes

2009年8月5日の朝、フロリダ州ボイントンビーチの静かな郊外住宅街が突如数十台のパトカーと黄色い規制線で封鎖されました。住民たちの注視と人気番組『Cops』のカメラが1台の車に集中します。降りてきたのは結婚6か月の26歳の新妻ダリア・ディッポリト。警官から夫が命を落としたと告げられた瞬間、映画の主演女優賞に値する大号泣劇が始まりました。

しかし彼女は知る由もありませんでした。現場全体が警察の周到なおとり捜査であり、夫マイケルは無事に保護されていることを。そして殺し屋を雇った黒幕こそが、目の前で泣き崩れる妻本人であり、「5000パーセント確信している」と言い放っていたことを。

Amber eyesは本事件を「10の犯罪心理・行動分析指標（§A2c）」を通じて完全解剖します：
1. 社会的激震とメディア熱狂: 全米を巻き込んだメディア現象；平穏な隣人の仮面の下に潜む悪意への集団的不安；おとり捜査の映像記録に関する法的基準の確立。
2. 客観化と脱人間化: 夫を25万ドルの不動産を独占するための法的障害とみなす冷酷さ；情緒的共感の完全な欠如；被害者の嘆願が捕食的支配欲を刺激する力学。
3. 認知的区画化: 家庭人としての顔と冷酷な暗殺首謀者の顔を完全に隔離する脳内防壁；家族を正常性の盾として利用；家族のアイデンティティ崩壊の悲劇。
4. 自己愛性崩壊: 禁錮16年の実刑判決を受けた際の涙は夫への悔悟ではなく自由を失った病的な自己憐憫；心理的判決が露わにした永遠の倫理的空虚。
5. 道徳的中和技術: 被害者非難（夫の前科を口実に正当化）；責任転嫁（元恋人の強要や警察の罠を主張）；悪ふざけの演技だったとする矮小化。
6. 心理的引き金と限界点: 不動産名義変更が契機；過去の工作に夫が疑念を抱き離婚による資産喪失を恐れたことが凶行への決定打。
7. シグネチャーと手口（MO）: アリバイ工作や外注手口に対し、「5000パーセント確信」と豪語し一切非を認めない極度の支配欲が不変の心理的署名。
8. エスカレーション軌道: 感情操作 -> 不動産強奪 -> お茶への異物混入 -> 車両への違法薬物偽装 -> 殺害依頼へと暴走した4段階の悪意。
9. ハロー効果と社会的盲点: 若く可憐な花嫁という外面が完璧な目くらましとなり、周囲の警戒心を長期間麻痺させた認知バイアス。
10. 被害者学と4つの危険兆候: 被害者の尊厳と回復力；生存のための4大危険兆候（The Gift of Fear）：(1) 資産獲得を伴う異常に性急な婚姻；(2) 厚顔無恥なガスライティング；(3) 共感を欠いた過剰な演技的感情表現；(4) 身の回りで不自然に繰り返される危険事故。

⏱ チャプター
00:00 イントロ＆留意事項
00:23 第1幕 · 偽装殺人現場と新妻の劇的な号泣劇
06:15 第2幕 · 白日の下に晒された真相と極限のガスライティング
12:30 第3幕 · 深層心理の解剖：悪性自己愛と経済的捕食の力学
19:00 第4幕 · 8年に及ぶ過酷な法廷闘争と禁錮16年の断罪
25:30 第5幕 · 覚醒の教訓と捕食的搾取を見抜く4つの危険兆候

⚠️ ご案内
• 本動画は司法行動科学および犯罪心理学に基づく教育的分析であり、法的・医学的助言に代わるものではありません。
• パームビーチ郡裁判所およびボイントンビーチ警察署の公開記録に基づき制作されています。

📚 主な参考文献
• パームビーチ郡巡回裁判所 — State v. Dalia Dippolito 公判記録
• ボイントンビーチ警察署 — おとり捜査報告書および極秘録画記録（2009）
• ギャビン・デ・ベッカー著『The Gift of Fear』

📞 相談ホットライン
• よりそいホットライン: 0120-279-338
• 配偶者暴力相談支援センター: 0570-0-55210

#ダリアディッポリト #犯罪心理学 #AmberEyes #事件解説 #ガスライティング #自己愛性パーソナリティ障害 #おとり捜査 #法医学 #危険兆候
"""

DESC_KO = """남편 청부살인범의 악어의 눈물과 카메라 앞의 희대의 연극 — 극한의 가스라이팅과 악성 자기애 해부 (Dalia Dippolito 사건) | 범죄심리학 | Amber eyes

2009년 8월 5일 아침, 플로리다주 해안 도시 보인턴비치의 평온한 교외 주택가가 수십 대의 경찰차와 노란 통제선으로 봉쇄되었습니다. 이웃 주민들의 시선과 인기 리얼리티 프로그램 콥스의 카메라가 급히 달려온 차량으로 쏠렸습니다. 내린 사람은 결혼한 지 6개월 된 스물여섯 살의 젊은 아내 달리아 디폴리토. 남편이 목숨을 잃었다는 경찰의 비보를 듣자마자 아카데미상급 오열 연극이 폭발했습니다.

하지만 그 여인은 꿈에도 몰랐습니다. 현장 전체가 경찰의 치밀한 함정 수사였으며 남편 마이클은 안전하게 살아있다는 사실을. 그리고 남편을 살해하기 위해 위장 경찰관을 고용한 주모자가 바로 밖에서 비통하게 울부짖던 아내 자신이었으며, 녹음 테이프 속에서 "약 오천 퍼센트 확신한다"고 호언장담했다는 사실을.

Amber eyes는 본 사건을 '10대 범죄 심리·행동 분석 지표(§A2c)'로 심층 해부합니다:
1. 사회적 파장과 미디어 열풍: 콥스, 데이트라인 NBC, 20/20을 통한 세계적 미디어 이슈; 평온한 이웃의 얼굴 뒤에 도사린 악의에 대한 교외 공동체의 전율; 함정 수사 영상 감시에 관한 사법적 기준 확립.
2. 사물화와 비인간화: 남편을 25만 달러 타운하우스를 가로채기 위한 법적 장애물로 격하시킨 냉혹함; 정서적 공감의 완전한 결여; 피해자의 호소가 가해자의 권력 도취감만을 자극하는 역학.
3. 인지적 구획화: 가정적인 아내의 모습과 냉혹한 살인 청부업자의 영역을 완벽히 차단한 뇌내 방화벽; 가족을 정상성의 방패로 악용; 법정에서 어머니와 친족들이 겪은 참혹한 정체성 붕괴.
4. 자기애적 붕괴: 16년 실형을 선고받았을 때의 오열은 남편을 향한 참회가 아닌 자유를 잃은 병적인 자기 연민; 진실 앞에서 패배한 영혼의 영원한 도덕적 공허.
5. 도덕적 중화 기법: 피해자 탓하기(남편의 과거 전과를 빌미로 정당화); 책임의 외부화(전 연인의 강요와 경찰의 함정 주장); 단순한 연기였다는 파렴치한 축소 변명.
6. 심리적 방아쇠와 임계점: 부동산 명의 이전이 기폭제; 남편이 의구심을 품고 보호관찰 종료가 다가오자 이혼으로 인한 재산 박탈 공포가 범행을 촉발.
7. 시그니처와 범행 수법(MO): 헬스클럽 알리바이와 청부 수법 대비, "오천 퍼센트 확신" 발언과 잘못을 절대 인정하지 않는 오만한 가스라이팅이 불변의 심리적 서명.
8. 에스컬레이션 궤적: 정서적 조작 -> 주택 명의 강탈 -> 아이스티 이물질 투입 -> 차량 마약 누명 조작 -> 청부살인 사주로 폭주한 4단계 악의.
9. 후광 효과와 사회적 맹점: 젊고 매력적인 신부라는 외적 껍데기가 사회적 경계심을 수개월간 완벽히 잠재운 인지적 편향.
10. 피해자학과 4대 위험 징후: 피해자의 고결한 인품과 회복력; 생존을 위한 4대 위험 징후(The Gift of Fear): (1) 재산권을 노린 성급한 결혼; (2) 파렴치한 가스라이팅; (3) 공감을 결여한 연극적 감정 분출; (4) 주변에서 거듭되는 기이한 위험 사고.

⏱ 챕터 타임라인
00:00 인트로 및 안내
00:23 막 1 · 모의 살인 현장 연출과 새댁의 극적인 오열
06:15 막 2 · 백일하에 드러난 진실과 극한의 가스라이팅
12:30 막 3 · 범죄 심리 해부: 악성 자기애와 약탈적 착취의 메커니즘
19:00 막 4 · 8년에 걸친 법정 전쟁과 징역 16년의 준엄한 단죄
25:30 막 5 · 각성의 교훈과 약탈적 심리 조작을 막는 4대 위험 징후

⚠️ 유의 사항
• 본 콘텐츠는 법행동과학 및 범죄심리학 분석에 기반한 교육적 영상이며 법적·의학적 조언을 대신하지 않습니다.
• 팜비치 카운티 법원 및 보인턴비치 경찰국의 공개 사법 기록을 토대로 제작되었습니다.

📚 주요 참고 문헌
• 플로리다 팜비치 카운티 법원 — State v. Dalia Dippolito 공판 기록
• 보인턴비치 경찰국 — 비밀 함정 수사 작전 보고서 및 영상 (2009)
• 개빈 드 베커 — 'The Gift of Fear' (직관적 생존 과학)

📞 긴급 상담 핫라인
• 자살예방 상담전화: 109 / 여성긴급전화: 1366 / 경찰청: 112

#달리아디폴리토 #범죄심리학 #AmberEyes #사건파일 #가스라이팅 #악성자기애 #함정수사 #악어의눈물 #생존위험징후 #법정드라마
"""

TARGETS = [
    # Tiếng Việt
    (ROOT / "02_SAN_XUAT" / "Tap22" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap22" / "xuat_ban" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap22" / "nguon_tham_khao.md", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap22" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap22" / "nguon_mo_ta.txt", SOURCES_VI),
    
    # Tiếng Anh
    (ROOT / "02_SAN_XUAT" / "Tap22_EN" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap22_EN" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap22_EN" / "xuat_ban" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap22_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap22_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap22_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap22_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),

    # Tiếng Nhật
    (ROOT / "02_SAN_XUAT" / "Tap22_JA" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap22_JA" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap22_JA" / "xuat_ban" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap22_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap22_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap22_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap22_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),

    # Tiếng Hàn
    (ROOT / "02_SAN_XUAT" / "Tap22_KO" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap22_KO" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap22_KO" / "xuat_ban" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap22_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap22_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap22_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap22_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
]

print("=" * 70)
print(">>> KIỂM TRA VÀ GHI TẤT CẢ FILE MÔ TẢ TẬP 22 (4 NGÔN NGỮ) <<<")
print("=" * 70)
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
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text.strip() + "\n")
    print(f"  Saved: {path.relative_to(ROOT)} ({len(text)} chars)")

if all_passed:
    print("\n>>> TẤT CẢ CÁC BẢN MÔ TẢ ĐÃ ĐƯỢC TẠO HOÀN HẢO VÀ ĐỀU DƯỚI 5000 KÝ TỰ! <<<")
else:
    print("\n>>> CẢNH BÁO: CÓ BẢN MÔ TẢ VƯỢT QUÁ 5000 KÝ TỰ! <<<")
print("=" * 70)
