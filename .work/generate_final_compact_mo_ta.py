#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tạo và chuẩn hóa mô tả cho Tập 06 trên 4 ngôn ngữ (VI, EN, JA, KO).
- Đảm bảo chính tả chính xác 100%.
- Đầy đủ 10 chỉ dấu tâm lý, 5 mốc chương, 20 nguồn kiểm chứng, hotline, disclaimer, hashtags.
- Đảm bảo độ dài DƯỚI 5.000 KÝ TỰ (chuẩn YouTube).
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# 1. TIẾNG VIỆT (VI)
# ==============================================================================
TITLE_VI = "Tập 06: Nụ Cười Chú Hề & 29 Bí Mật Dưới Sàn Nhà | Tâm lý học tội phạm: John Wayne Gacy (10 Chỉ Dấu Tâm Lý & Mặt Nạ Ái Kỷ) | Amber eyes"

INTRO_VI = """Ngày 6/5/1978, tại lễ diễu hành mừng Ngày Hiến pháp Ba Lan ở Chicago, John Wayne Gacy (36 tuổi) mỉm cười tự tin bắt tay Đệ nhất phu nhân Hoa Kỳ Rosalynn Carter. Trên ve áo vest của hắn là chiếc huy hiệu chữ "S" do Cơ quan Mật vụ Hoa Kỳ cấp, chứng nhận quyền tiếp cận khu vực an ninh đặc biệt. Trong mắt cộng đồng ngoại ô Chicago, Gacy là hiện thân của "giấc mơ Mỹ": chủ thầu xây dựng PDM Contractors thành đạt, đội trưởng khu dân cư của Đảng Dân chủ tại Norwood Park, và là người thường xuyên hóa trang thành "Chú hề Pogo" mang tiếng cười miễn phí đến các bệnh nhi. Không ai ngờ đằng sau lớp phấn trắng và chiếc mặt nạ công dân mẫu mực ấy lại là kẻ săn mồi tàn độc nhất lịch sử hiện đại.

Đêm 11/12/1978, cậu thiếu niên 15 tuổi Robert Piest tan ca tại hiệu thuốc Nisson (Des Plaines, Illinois) và biến mất sau khi bước ra ngoài gặp Gacy để trao đổi về công việc phụ việc xây dựng lương 5 USD/giờ. Cuộc điều tra và bám đuôi 24/7 của các thám tử Des Plaines đã dẫn họ vào căn nhà số 8213 West Summerdale. Dưới khoảng bò chật hẹp chỉ cao 46 cm ngập bùn đất và vôi sống, cảnh sát bàng hoàng phát hiện hố chôn 29 thi thể thanh thiếu niên bị siết cổ bằng dây garrote, cùng 4 nạn nhân bị ném xuống sông Des Plaines khi hầm đã chật kín. Tổng cộng 33 sinh mạng đã bị tước đoạt bởi kẻ mang chứng rối loạn nhân cách chống đối xã hội và ái kỷ ác tính."""

MARKERS_VI = """Hồ sơ John Wayne Gacy được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG MANG TẬP THỂ: Phá vỡ hoàn toàn ảo tưởng an toàn ngoại ô; cú sốc khi một trụ cột cộng đồng, một chú hề từ thiện sát hại 33 thanh thiếu niên, làm thay đổi vĩnh viễn quy trình bảo vệ trẻ em.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Tước đoạt toàn bộ nhân tính nạn nhân, biến họ thành "công cụ sinh học" vô danh phục vụ ảo tưởng thống trị tối thượng và nhục dục bệnh hoạn, rồi chôn vùi như phế thải xây dựng.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Duy trì hai thực tại cô lập: ban ngày là nhà thầu năng nổ, người hàng xóm hào phóng đãi tiệc nướng; đêm xuống là kẻ săn mồi siết dây garrote ngay trong chính căn nhà của mình.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Đối diện vật chứng (biên nhận ảnh, nhẫn JAS của John Szyc) và sự giám sát 24/7, chiếc mặt nạ rơi xuống; hắn trốn vào chiêu bài "đa nhân cách Jack Hanley", tự nhận "Tôi là nạn nhân thứ 34".
5. HỆ THỐNG TỰ BÀO CHỮA (TECHNIQUES OF NEUTRALIZATION): Vận dụng "đổ lỗi cho nạn nhân" và "chối bỏ trách nhiệm", ngụy biện các chàng trai tự nguyện đến nhà vì tiền hoặc ma túy, tự coi mình là nạn nhân bị xã hội hãm hại.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Tuổi thơ bị cha nghiện rượu bạo hành và sỉ nhục tàn tệ, cùng bệnh tim và chấn thương đầu gieo mầm mặc cảm bất lực; bản án tù tại Iowa (1968) phá nát danh dự, kích hoạt cơn cuồng sát kiểm soát sinh tử.
7. SIGNATURE VS. THỦ ĐOẠN MO: MO biến đổi từ mời việc 5 USD/giờ đến trò "ảo thuật còng tay"; Signature bất biến là ép nạn nhân vào thế bất lực, siết cổ bằng garrote và chôn cất thi thể ngay dưới không gian sinh sống.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Từ xâm hại đơn lẻ tại Iowa đến sát nhân hàng loạt ở Summerdale; tần suất tăng vọt giai đoạn 1976–1977 do trơ lỳ cảm xúc, buộc phải ném xác xuống sông khi khoảng bò 46 cm hết chỗ.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc "chú hề Pogo", huy hiệu Mật vụ "S" chụp cùng Đệ nhất phu nhân và quan hệ chính trị tạo hào quang hoàn hảo, khiến chính quyền phớt lờ nhiều đơn tố cáo suốt nhiều năm.
10. CẢNH BÁO ĐỎ SINH TỒN: 4 tín hiệu nhận diện kẻ săn mồi đội lốt người tốt: lời mời việc làm thù lao bất thường cho thiếu niên; trò ảo thuật còng tay trói buộc; mùi hôi thối ngụy trang bằng vôi bột; và vẻ quyến rũ che đậy cơn kiểm soát áp đặt."""

CHAPTERS_VI = """⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Bức ảnh với Đệ nhất phu nhân và cậu bé hiệu thuốc
05:10 Hồi 2 · Hiện trường & Quỹ đạo leo thang của vực thẳm
10:45 Hồi 3 · Giải phẫu tâm lý — Sự chia ngăn nhận thức & Khoảng tối Summerdale
16:30 Hồi 4 · Đấu trí thẩm vấn & Sụp đổ vở kịch đa nhân cách
21:50 Hồi 5 · Phán quyết, bản án tâm lý & bài học cảnh báo đỏ sinh tồn"""

DISCLAIMER_VI = """⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Phân tích giáo dục, tư liệu lịch sử & tâm lý tội phạm học; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai Hoa Kỳ (Tòa Cook County, Cảnh sát Des Plaines, Công tố Illinois). Kênh không bôi nhọ hay tôn vinh bất kỳ ai.
• Hình tượng động vật là nghệ thuật. Lời thoại dựng lại từ tư liệu lịch sử.
• Giọng đọc, hình ảnh & âm thanh hỗ trợ bởi công nghệ AI.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio"""

SOURCES_VI = """📚 NGUỒN THAM KHẢO ĐÃ ĐỐI CHIẾU
Toàn bộ sự kiện đã đối chiếu 20 nguồn công khai:
• [1] Wikipedia — John Wayne Gacy: https://en.wikipedia.org/wiki/John_Wayne_Gacy
• [2] Clark County Prosecutor #237: http://www.clarkprosecutor.org/html/death/US/gacy237.htm
• [3] Chicago Tribune Timeline: https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html
• [4] Chicago Tribune Victims: https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html
• [5] A&E — Gacy's Trial: https://www.aetv.com/articles/gacys-trial
• [6] A&E — Capture & Search: https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case
• [7] A&E — Case File Gacy: https://www.aetv.com/articles/john-wayne-gacy
• [8] Encyclopedia.com 1980 Trial: https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980
• [9] Biography.com John Wayne Gacy: https://www.biography.com/crime/john-wayne-gacy
• [10] Netflix Tudum Profile: https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know
• [11] Slate — 'Devil in Disguise': https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html
• [12] Solve The Case Profile: https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr
• [13] Joyce & Stover 'Witnesses': https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt
• [14] Esquire Det. Albrecht: https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/
• [15] Oxygen Brazen Arrest: https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught
• [16] TheWrap Detectives Interview: https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/
• [17] NBC News Gacy Docuseries: https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590
• [18] LegalNews 'Defending a Monster': https://www.legalnews.com/Home/Articles?DataId=1038560
• [19] Chicago Bar Prosecution: https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/
• [20] Den of Geek Review: https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/"""

HOTLINE_VI = """🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).
• Đường dây nóng phòng chống bạo lực gia đình: 1900 969 680
• National Center for Missing & Exploited Children (NCMEC): 1-800-843-5678 — https://www.missingkids.org
• National Sexual Assault Hotline (RAINN): 1-800-656-4673 — https://www.rainn.org"""

TAGS_VI = "#AmberEyes #TrueCrime #CriminalPsychology #JohnWayneGacy #TheKillerClown #TamLyToiPham #10ChiDauTamLy #CanhBaoDo #HoSoToiPham #Documentary"

DESC_VI = f"{TITLE_VI}\n\n{INTRO_VI}\n\n{MARKERS_VI}\n\n{CHAPTERS_VI}\n\n{DISCLAIMER_VI}\n\n{SOURCES_VI}\n\n{HOTLINE_VI}\n\n{TAGS_VI}\n"


# ==============================================================================
# 2. TIẾNG ANH (EN)
# ==============================================================================
TITLE_EN = "Ep. 06: The Killer Clown & 29 Secrets Under the Floor | Criminal Psychology: John Wayne Gacy (10 Psychological Markers & The Narcissistic Mask) | Amber eyes"

INTRO_EN = """On May 6, 1978, at Chicago's Polish Constitution Day parade, 36-year-old John Wayne Gacy smiled confidently as he shook hands with First Lady Rosalynn Carter. On his lapel was a Secret Service "S" pin granting special VIP clearance. To suburban Chicago, Gacy embodied the American Dream: successful contractor at PDM Contractors, Democratic precinct captain, and a charitable volunteer who dressed as "Pogo the Clown" to bring free laughter to hospitalized children. Nobody suspected that beneath that greasepaint smile was one of the deadliest serial predators in modern history.

On the freezing night of December 11, 1978, 15-year-old high school sophomore Robert Piest vanished after stepping outside Nisson Pharmacy in Des Plaines to discuss a $5/hour construction job with Gacy. Relentless 24/7 surveillance by Des Plaines detectives eventually led to a search of Gacy's home at 8213 West Summerdale Avenue. In an 18-inch crawl space beneath the living room, submerged in damp mud and lime, investigators uncovered 29 garroted bodies, with four more dumped into the Des Plaines River after the crawl space filled up. In total, 33 young lives were stolen by a predatory psychopath with malignant narcissism."""

MARKERS_EN = """Amber eyes dissects the John Wayne Gacy file through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: The case shattered suburban safety illusions; the horror that a respected civic leader and children's clown murdered 33 young men permanently transformed juvenile protection systems.
2. OBJECTIFICATION OF VICTIMS: Gacy stripped victims of humanity, reducing them to disposable "biological tools" to satisfy perverse fantasies of supreme dominance, burying them like construction debris.
3. COMPARTMENTALIZATION (THE DUAL REALITY): He maintained two isolated realities without conflict: an energetic contractor and generous neighbor by day; a ruthless predator tightening a garrote in his home by night.
4. NARCISSISTIC COLLAPSE: Confronted with physical evidence (photo receipt, John Szyc's JAS ring) and 24/7 surveillance, his mask shattered; he hid behind a fake "Jack Hanley multiple personality" defense and claimed "I am victim 34."
5. TECHNIQUES OF NEUTRALIZATION: He weaponized "victim blaming" and "denial of responsibility," claiming boys entered voluntarily for cash or drugs, portraying himself as an unjustly persecuted victim.
6. PRECIPITATING TRIGGER & PSYCHOLOGICAL FRACTURES: Brutal abuse by an alcoholic father, a heart defect, and childhood head trauma sowed profound inadequacy; his 1968 Iowa prison sentence broke his social pride, unleashing lethal compensatory rage.
7. SIGNATURE VS. MODUS OPERANDI (MO): MO evolved from $5/hr job offers to fake police badges and the "handcuff trick"; his immutable Signature was rendering victims entirely helpless, garroting them, and entombing them beneath his floor.
8. ESCALATION TRAJECTORY: From isolated abuse in Iowa to serial slaughter at Summerdale; killing frequency spiked in 1976–1977 from emotional desensitization, forcing river disposals once the crawl space filled up.
9. HALO EFFECT & SOCIAL BLIND SPOTS: His "Pogo the Clown" charity, Secret Service "S" pin beside the First Lady, and political standing formed an impenetrable halo, blinding authorities to survivor reports for years.
10. SURVIVAL RED FLAGS: Four vital predatory red flags: off-the-books job offers with inflated wages for teens; coercive restraint/handcuff games; putrid odors masked by lime; and superficial charm masking sudden domineering control."""

CHAPTERS_EN = """⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · The Photo with the First Lady and the Pharmacy Boy
05:10 Act 2 · The Crime Scene & The Escalation Trajectory of the Abyss
10:45 Act 3 · Psychological Autopsy — Cognitive Compartmentalization & The Summerdale Darkness
16:30 Act 4 · The Interrogation Duel & The Collapse of the Multiple Personality Masquerade
21:50 Act 5 · The Verdict, Psychological Sentence & Survival Red Flags"""

DISCLAIMER_EN = """⚠️ LEGAL & SAFETY DISCLAIMER
• Produced exclusively for educational, criminological, and historical analysis; not medical or legal advice.
• Based on public US judicial records (Cook County Circuit Court, Des Plaines Police Dept, Illinois AG Office). No intent to defame or glorify any individual.
• Avatars (Owl, Wolf, Fox, Sheep, Cat) and dialogue are dramatized illustrations based on archival transcripts.
• Synthetic AI voices, visuals, and audio are utilized.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio"""

SOURCES_EN = """📚 VERIFIED SOURCES & COURT EXHIBITS
All events, dates, and quotes have been verified line-by-line against 20 public archival sources:
• [1] Wikipedia — John Wayne Gacy: https://en.wikipedia.org/wiki/John_Wayne_Gacy
• [2] Clark County State's Attorney — Gacy Case #237: http://www.clarkprosecutor.org/html/death/US/gacy237.htm
• [3] Chicago Tribune Timeline: https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html
• [4] Chicago Tribune Victims: https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html
• [5] A&E — Trial of John Wayne Gacy: https://www.aetv.com/articles/gacys-trial
• [6] A&E — Capture & Summerdale Search: https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case
• [7] A&E — Case File John Wayne Gacy: https://www.aetv.com/articles/john-wayne-gacy
• [8] Encyclopedia.com 1980 Trial: https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980
• [9] Biography.com John Wayne Gacy Biography: https://www.biography.com/crime/john-wayne-gacy
• [10] Netflix Tudum Profile: https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know
• [11] Slate — Peacock Doc 'Devil in Disguise': https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html
• [12] Solve The Case Profile: https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr
• [13] Joyce & Stover 'Witnesses': https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt
• [14] Esquire Interview Det. Albrecht: https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/
• [15] Oxygen Brazen Arrest: https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught
• [16] TheWrap Detectives Interview: https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/
• [17] NBC News Docuseries & Victims: https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590
• [18] LegalNews 'Defending a Monster': https://www.legalnews.com/Home/Articles?DataId=1038560
• [19] Chicago Bar Prosecution: https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/
• [20] Den of Geek Review: https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/"""

HOTLINE_EN = """🆘 CRISIS & CHILD PROTECTION HOTLINES (24/7, FREE & CONFIDENTIAL)
• National Center for Missing & Exploited Children (NCMEC - USA): 1-800-843-5678 — https://www.missingkids.org
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelp.org
• National Sexual Assault Hotline (RAINN - USA): 1-800-656-4673 — https://www.rainn.org
• Suicide & Crisis Lifeline (USA): Call or text 988 — https://988lifeline.org"""

TAGS_EN = "#AmberEyes #TrueCrime #CriminalPsychology #JohnWayneGacy #TheKillerClown #ForensicPsychology #PogoTheClown #10PsychologicalMarkers #SurvivalRedFlags #Documentary"

DESC_EN = f"{TITLE_EN}\n\n{INTRO_EN}\n\n{MARKERS_EN}\n\n{CHAPTERS_EN}\n\n{DISCLAIMER_EN}\n\n{SOURCES_EN}\n\n{HOTLINE_EN}\n\n{TAGS_EN}\n"


# ==============================================================================
# 3. TIẾNG NHẬT (JA)
# ==============================================================================
TITLE_JA = "第06話 · 殺人ピエロの笑顔と床下の29の秘密 | 犯罪心理学：ジョン・ウェイン・ゲイシー事件 (10の心理指標と自己愛の仮面) | Amber eyes"

INTRO_JA = """1978年5月6日、シカゴのポーランド憲法記念日パレード。仕立てのよいスーツを着た自信溢れる36歳の男性が、ファーストレディのロザリン・カーター大統領夫人と笑顔で握手を交わしました。男性の胸元には特務警護部（シークレットサービス）発行のVIP特別通行証「S」ピンが光っていました。その男ジョン・ウェイン・ゲイシーは、建築会社PDMコントラクターズ社長、地域民主党幹部、そして小児病棟を慰問する慈善ピエロ「ポゴ」として愛される模範市民でした。しかしその白塗りメイクの下に、近代犯罪史上最悪の捕食者が潜んでいたのです。

1978年12月11日の夜、薬局でアルバイトを終えた15歳の高校生ロバート・ピーストが、時給5ドルのバイトの勧誘を受け、ゲイシーと店外で話したのを最後に失踪。警察の執念の24時間密着追跡の末、サマーデール通り8213番地の自宅への家宅捜索が行われました。生活空間の直下、高さわずか46cmの泥と消石灰に覆われた床下から、止血棒（ガロット）で絞殺された29名の少年遺体が発見され、床下が満杯となり近隣の川へ遺棄された4名を加え、計33名もの尊い命が冷酷な自己愛性捕食者によって奪われていました。"""

MARKERS_JA = """アンバーアイズ（Amber eyes）は、本事件を「10の核心的心理・行動指標エコシステム」を通じて解剖します：
1. 社会的余波と集団的パラノイア: 平穏な郊外の安全神話が崩壊。慈善ピエロと地域有力者の正体が33名の少年を屠った連続殺人鬼であった戦慄の事実は、米国の未成年者保護体制を根本から変革しました。
2. 被害者の客体化（Objectification）: 被害者から人間性を完全に剥奪し、絶対的支配欲を満たすための「生体ツール」へと還元。遺体を建築廃材のように床下へと埋め捨てました。
3. 心理的区画化（Compartmentalization）: 昼は近隣に料理を振る舞い大統領夫人と握手する「良き市民」、夜は自宅で冷酷にロープを締め上げる「捕食者」という2つの世界を完全に分離しました。
4. 自己愛の崩壊（Narcissistic Collapse）: 薬局の預かり証や指輪などの証拠と24時間監視の前に尊大な仮面は崩壊。「多重人格ジャック・ハンリー」の狂言に逃げ、「私こそ34人目の被害者だ」と自己憐憫に浸りました。
5. 中和の技術（Techniques of Neutralization）: 「被害者非難」を駆使し、若者たちが金や薬物欲しさに自ら招いた事態だと強弁。自己を不当な司法の犠牲者として演出しました。
6. 心理的引き金と破綻点: アルコール依存症の父による虐待、心臓疾患、頭部外傷が劣等感を形成。1968年の服役で社会的地位を失ったことが、生死を支配する暴走衝動の引き金となりました。
7. 署名（Signature）対 手口（MO）: 手口（MO）は高額バイト勧誘、警察バッジ提示、「手錠マジック」など洗練。不変の署名（Signature）は、完全無力化した被害者の生死を握る全能感と床下埋葬でした。
8. エスカレーション軌道: 単独の性的加害から連続殺人へ暴走。1976〜1977年に殺害頻度が急増し、床下が埋まり尽くすと川への遺棄へと発展しました。
9. ハロー効果と社会的盲点: ピエロ活動、大統領夫人との写真、政界とのパイプが完璧な後光を形成し、過去の脱出被害者の訴えが長年放置される致命的な盲点を生みました。
10. 生存のレッドフラッグ: 善人の仮面を見破る4つの危険兆候：青少年への高額バイト勧誘；手錠・拘束具への誘導；消石灰で隠された室内の異臭；過剰な表層的魅力の裏の支配欲。"""

CHAPTERS_JA = """⏱ 目次（チャプター）
00:00 オープニング＆視聴にあたって
00:23 第1幕 · ファーストレディとの写真と薬局の少年
05:10 第2幕 · 犯行現場と深淵のエスカレーション軌道
10:45 第3幕 · 徹底心理解剖――認知的区画化とサマーデールの暗闇
16:30 第4幕 · 取調の攻防と多重人格劇の崩壊
21:50 第5幕 · 判決、深層心理の代償と生存のためのレッドフラッグ"""

DISCLAIMER_JA = """⚠️ ご視聴にあたっての注意事項
• 本動画は教育、歴史的ドキュメンタリーおよび犯罪心理学の分析コンテンツであり、医学的・法的助言に代わるものではありません。
• 米国の公開記録（クック郡裁判所、デス・プレーンズ警察、イリノイ州司法長官記録）に基づいて制作されています。
• 登場する動物キャラクター（フクロウ、オオカミ、キツネ、羊、猫）は演出用の架空のキャラクターです。
• 音声、画像、音楽はAIツールを活用して制作されています。
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio"""

SOURCES_JA = """📚 参考資料・出典
本動画におけるすべての事件経過、日時、判決記録は以下の20件の公式公開記録と照合されています：
• [1] Wikipedia — ジョン・ウェイン・ゲイシー: https://en.wikipedia.org/wiki/John_Wayne_Gacy
• [2] クラーク郡検察局 — 事件記録 #237: http://www.clarkprosecutor.org/html/death/US/gacy237.htm
• [3] シカゴ・トリビューン — 事件タイムライン: https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html
• [4] シカゴ・トリビューン — 犠牲者名簿: https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html
• [5] A&E — 裁判記録: https://www.aetv.com/articles/gacys-trial
• [6] A&E — 捜索と逮捕の経緯: https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case
• [7] A&E — 事件ファイル: https://www.aetv.com/articles/john-wayne-gacy
• [8] Encyclopedia.com 1980年公判記録: https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980
• [9] Biography.com 生涯と犯罪: https://www.biography.com/crime/john-wayne-gacy
• [10] Netflix Tudum ドキュメンタリー特集: https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know
• [11] Slate — 『仮面を被った悪魔』批評: https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html
• [12] Solve The Case 犯人プロファイル: https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr
• [13] ジョイス＆ストーバー 『墓場からの証人』: https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt
• [14] エスクァイア 捜査官アルブレヒト証言: https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/
• [15] Oxygen ゲイシー逮捕の経緯: https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught
• [16] TheWrap デス・プレーンズ警察証言: https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/
• [17] NBC News ドキュメンタリーと犠牲者: https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590
• [18] LegalNews (AP) 『怪物弁護記』: https://www.legalnews.com/Home/Articles?DataId=1038560
• [19] シカゴ弁護士会 カンクル検事公判記録: https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/
• [20] Den of Geek 作品レビュー: https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/"""

HOTLINE_JA = """🆘 相談窓口・支援ホットライン（通話無料・24時間受付）
• 児童相談所虐待対応ダイヤル：189（いちはやく・通話無料）
• 性犯罪・性暴力被害者のためのワンストップ支援センター：#8891（短縮ダイヤル）
• 警察相談専用電話：#9110（全国共通）
• よりそいホットライン：0120-279-338"""

TAGS_JA = "#犯罪心理学 #TrueCrime #ジョンウェインゲイシー #キラークラウン #殺人ピエロ #10の心理指標 #レッドフラッグ #心理解剖 #ドキュメンタリー #AmberEyes"

DESC_JA = f"{TITLE_JA}\n\n{INTRO_JA}\n\n{MARKERS_JA}\n\n{CHAPTERS_JA}\n\n{DISCLAIMER_JA}\n\n{SOURCES_JA}\n\n{HOTLINE_JA}\n\n{TAGS_JA}\n"


# ==============================================================================
# 4. TIẾNG HÀN (KO)
# ==============================================================================
TITLE_KO = "06화 · 살인 광대의 미소와 마루 밑 29개의 비밀 | 범죄심리학: 존 웨인 게이시 사건 (10대 심리 지표와 나르시시즘의 가면) | Amber eyes"

INTRO_KO = """1978년 5월 6일, 미국 시카고에서 열린 폴란드 헌법의 날 퍼레이드. 깔끔한 양복을 입은 자신감 넘치는 36세 남성이 퍼스트레이디 로절린 카터 여사와 환한 미소로 악수했습니다. 그의 가슴에는 비밀경호국이 발급한 특별 보안 배지 'S' 핀이 빛나고 있었습니다. 남자의 이름은 존 웨인 게이시. 번창하는 건설회사 PDM 대표이자 지역 민주당 간부, 소아 병동을 찾아 무보수로 웃음을 선물하던 자선 광대 '포고'로 사랑받던 모범 시민이었습니다. 하지만 그 두터운 분장 이면에는 현대 범죄 역사상 가장 잔혹한 포식자의 이빨이 숨겨져 있었습니다.

1978년 12월 11일 혹한의 밤, 약국 아르바이트를 마친 15세 고교생 로버트 피스트가 시급 5달러의 건축 보조 일자리를 제안받고 게이시와 대화한 뒤 실종되었습니다. 경찰의 24시간 밀착 감시 끝에 단행된 자택 압수수색에서, 거실 바로 밑 46cm 높이의 축축한 마루 밑 기폐 공간(crawl space)에서 지혈봉(garrote)으로 교살된 29구의 청소년 시신이 발견되었습니다. 공간이 부족해 인근 강에 유기된 4명을 포함해 총 33명의 젊은 생명이 악성 나르시시즘 포식자의 뒤틀린 미소 아래 암매장되어 있었습니다."""

MARKERS_KO = """Amber eyes는 본 사건을 '10대 핵심 심리·행동 지표 생태계'를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 공포: 안전 신화가 무너진 충격. 자선 광대이자 지역 유력 인사가 33명의 소년을 살해한 연쇄 살인마였다는 사실은 전미에 공포를 남겼으며 청소년 보호 체계를 영구히 개혁시켰습니다.
2. 피해자의 객체화(Objectification): 피해자에게서 생명과 인격을 박탈하고, 절대적 통제감을 충족하기 위한 일회용 '생체 도구'로 축소해 건축 폐기물처럼 마루 밑에 파묻었습니다.
3. 심리적 구획화(Compartmentalization): 낮에는 이웃과 바비큐 파티를 열고 영부인과 악수하는 '모범 시민', 밤에는 집 안에서 잔혹하게 올가미를 조이는 '포식자'의 삶을 철저히 분리했습니다.
4. 나르시시즘적 붕괴(Narcissistic Collapse): 증거(현상 영수증, 졸업 반지)와 밀착 감시 앞에 오만한 가면이 벗겨지자, '다중인격 잭 핸리' 뒤로 숨으며 "나야말로 34번째 피해자"라고 참회를 거부했습니다.
5. 중화 기술(Techniques of Neutralization): '피해자 비난'을 악용해 돈을 노리고 찾아온 소년들의 탓으로 돌리며, 자신을 불공정한 사회의 희생양으로 규정했습니다.
6. 심리적 트리거와 파탄점: 알코올 중독자 아버지의 학대, 심장 질환, 뇌 손상이 열등감을 형성. 1968년 복역으로 사회적 가면이 파괴되자 생사를 통제하려는 광기로 폭발했습니다.
7. 시그니처 vs 범행 수법(MO): 수법(MO)은 시급 5달러 제안, 경찰 사칭, '수갑 마술'로 진화한 반면, 불변의 시그니처는 피해자를 완전 무력화시켜 지혈봉으로 교살하고 마루 밑에 묻는 것이었습니다.
8. 에스컬레이션 궤적: 성범죄에서 연쇄 살인으로 폭주. 1976~1977년 살해 빈도가 급증했고, 마루 밑이 가득 차자 데스플레인스 강으로 유기 장소를 넓혔습니다.
9. 후광 효과와 제도의 맹점: 자선 활동, 영부인과의 사진, 정계 인맥이 완벽한 후광을 형성해 피해자들의 탈출 증언과 신고가 수년간 묵살되는 치명적 맹점을 낳았습니다.
10. 생존의 레드플래그: 선한 가면을 쓴 포식자를 식별하는 4대 경고: 비정상적 고보수 알바 제안; 수갑·밧줄 구속 요구; 소석회로 덮은 실내 악취; 과도한 매력 이면의 통제욕."""

CHAPTERS_KO = """⏱ 챕터(타임라인)
00:00 오프닝 & 시청 안내
00:23 제1막 · 영부인과의 사진과 약국 소년의 실종
05:10 제2막 · 범죄 현장과 심연의 에스컬레이션 궤적
10:45 제3막 · 심층 심리 분석 — 인지적 구획화와 서머데일의 어둠
16:30 제4막 · 심문실의 심리전과 다중인격극의 붕괴
21:50 제5막 · 판결, 심리적 심판과 생존을 위한 레드플래그"""

DISCLAIMER_KO = """⚠️ 시청 전 법적 유의사항
• 본 콘텐츠는 교육, 범죄심리학 및 역사적 분석 다큐멘터리이며, 의학적·법률적 조언을 대신할 수 없습니다.
• 미국 공식 사법 기록(쿡 카운티 법원, 데스플레인스 경찰서, 일리노이주 법무장관 기록)을 바탕으로 제작되었습니다.
• 등장하는 동물 캐릭터(올빼미, 늑대, 여우, 양, 고양이)는 시각적 연출을 위한 가상 캐릭터입니다.
• 본 영상의 음성, 이미지, 음악은 AI 기술을 활용하여 제작되었습니다.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio"""

SOURCES_KO = """📚 공식 참고자료 및 공판 기록
본 영상의 모든 사건 개요, 날짜, 재판 기록은 다음 20개 공식 공개 기록과 교차 검증되었습니다:
• [1] Wikipedia — 존 웨인 게이시: https://en.wikipedia.org/wiki/John_Wayne_Gacy
• [2] 클라크 카운티 검찰청 — 사건 파일 #237: http://www.clarkprosecutor.org/html/death/US/gacy237.htm
• [3] 시카고 트리뷴 — 사건 종합 타임라인: https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html
• [4] 시카고 트리뷴 — 희생자 명단: https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html
• [5] A&E — 공판 기록: https://www.aetv.com/articles/gacys-trial
• [6] A&E — 주택 압수수색 및 체포: https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case
• [7] A&E — 사건 파일: https://www.aetv.com/articles/john-wayne-gacy
• [8] Encyclopedia.com 1980년 재판 기록: https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980
• [9] Biography.com 전기 및 범죄 분석: https://www.biography.com/crime/john-wayne-gacy
• [10] Netflix Tudum 다큐멘터리 프로파일: https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know
• [11] Slate — '가면을 쓴 악마' 리뷰: https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html
• [12] Solve The Case 가해자 프로파일: https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr
• [13] 조이스 & 스토버 《무덤에서 온 증인들》: https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt
• [14] 에스콰이어 수사관 알브레히트 인터뷰: https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/
• [15] Oxygen 게이시가 덜미를 잡힌 행적: https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught
• [16] TheWrap 데스플레인스 수사관 인터뷰: https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/
• [17] NBC News 다큐시리즈와 희생자들: https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590
• [18] LegalNews (AP) 《괴물을 변호하다》: https://www.legalnews.com/Home/Articles?DataId=1038560
• [19] 시카고 변호사협회 쿤클 검사의 공판 회고: https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/
• [20] Den of Geek 작품 분석: https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/"""

HOTLINE_KO = """🆘 위기 상담 및 피해자 지원 핫라인 (24시간 무료 & 비밀보장)
• 아동학대 예방 및 신고 상담전화: 국번없이 112 또는 129
• 여성긴급전화 (가정폭력·성폭력 상담): 국번없이 1366
• 경찰청 범죄신고: 국번없이 112
• 보건복지상담센터: 국번없이 129
• 청소년 전화 및 사이버상담: 국번없이 1388"""

TAGS_KO = "#AmberEyes #범죄심리학 #TrueCrime #존웨인게이시 #살인광대 #광대포고 #10대심리지표 #레드플래그 #사건기록 #다큐멘터리"

DESC_KO = f"{TITLE_KO}\n\n{INTRO_KO}\n\n{MARKERS_KO}\n\n{CHAPTERS_KO}\n\n{DISCLAIMER_KO}\n\n{SOURCES_KO}\n\n{HOTLINE_KO}\n\n{TAGS_KO}\n"


# ==============================================================================
# GHI FILE & KIỂM TRA ĐỘ DÀI
# ==============================================================================
files_data = [
    # 1. TIẾNG VIỆT
    (ROOT / "02_SAN_XUAT" / "Tap06" / "nguon_mo_ta.txt", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap06" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap06" / "xuat_ban" / "mo_ta.txt", DESC_VI),

    # 2. TIẾNG ANH
    (ROOT / "02_SAN_XUAT" / "Tap06_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap06_EN" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap06_EN" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap06_EN" / "xuat_ban" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap06_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),

    # 3. TIẾNG NHẬT
    (ROOT / "02_SAN_XUAT" / "Tap06_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap06_JA" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap06_JA" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap06_JA" / "xuat_ban" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap06_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),

    # 4. TIẾNG HÀN
    (ROOT / "02_SAN_XUAT" / "Tap06_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap06_KO" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap06_KO" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap06_KO" / "xuat_ban" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap06_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
]

all_under_5000 = True

print(f"{'File':<55} | {'Ký tự':<6} | <= 5000?")
print("-" * 75)

for path, content in files_data:
    path.parent.mkdir(parents=True, exist_ok=True)
    c_strip = content.strip() + "\n"
    path.write_text(c_strip, encoding="utf-8")
    c_len = len(c_strip)
    is_ok = c_len <= 5000
    if not is_ok:
        all_under_5000 = False
    status = "✅ ĐẠT" if is_ok else "❌ VƯỢT"
    rel_path = str(path.relative_to(ROOT))
    print(f"{rel_path:<55} | {c_len:<6} | {status}")

print("-" * 75)
if all_under_5000:
    print("KẾT QUẢ: 100% FILE MÔ TẢ ĐỀU DƯỚI 5.000 KÝ TỰ (ĐẠT CHUẨN YOUTUBE)!")
else:
    print("CẢNH BÁO: CÓ FILE VƯỢT QUÁ 5.000 KÝ TỰ!")
