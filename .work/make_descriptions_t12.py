#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo các file mô tả và nguồn tham khảo cho Tập 12 trên 4 ngôn ngữ (VN, EN, JA, KO).
Đảm bảo đầy đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c, K10) và TUYỆT ĐỐI <= 5000 ký tự.
"""

import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NGUỒN THAM KHẢO GỌN CHO FILE NGUỒN
# ==============================================================================

SOURCES_VI = """📚 TỔNG HỢP NGUỒN THAM KHẢO HỒ SƠ TẬP 12 (JONESTOWN & JIM JONES)
Amber eyes tuân thủ nguyên tắc đối chiếu đa nguồn từ hồ sơ giải mật chính thức của Quốc hội Hoa Kỳ và FBI:

1. Hồ sơ chính thức & Báo cáo điều tra:
• House Foreign Affairs Committee (1979) — Báo cáo điều tra chính thức vụ ám sát Dân biểu Leo Ryan và Thảm kịch Jonestown (House Report No. 96-223): https://www.congress.gov/
• FBI Vault RYMUR (Ryan Murder / Jonestown) — Hơn 48.000 trang hồ sơ giải mật: https://vault.fbi.gov/jonestown
• Băng ghi âm hiện trường 'The Death Tape' (FBI Audio File Q 042, ngày 18/11/1978 tại Jonestown, Guyana): https://archive.org/details/ptc1978-11-18.flac16

2. Cơ sở tư liệu học thuật & Báo cáo chuyên sâu:
• San Diego State University (SDSU) — Dự án Lưu trữ Tư liệu Toàn cảnh Jonestown: https://jonestown.sdsu.edu/
• Julia Scheeres — Tác phẩm tư liệu 'A Thousand Lives: The Untold Story of Jonestown': https://www.simonandschuster.com/
• Tim Reiterman (Ký giả bị thương tại sân bay Port Kaituma) — 'Raven: The Untold Story of the Rev. Jim Jones and His People': https://www.penguinrandomhouse.com/

3. Tâm lý học thao túng đám đông & Tự sát cưỡng chế:
• GS. Philip Zimbardo — Nghiên cứu Sự tuân phục hủy diệt và Thao túng tâm lý có hệ thống.
• Phân tích Tự sát cưỡng chế (Coerced Collective Suicide / Mass Murder) dưới áp lực vũ lực và tẩy não.

4. Đường dây nóng hỗ trợ & bảo vệ:
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7): http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414 — https://duongdaynongngaymai.vn/
"""

SOURCES_EN = """📚 PRIMARY SOURCES & INVESTIGATIVE DOSSIER — EPISODE 12 (JONESTOWN & JIM JONES)
Amber eyes adheres to multi-source verification using declassified US government and academic archives:

1. Official Government & Investigative Records:
• House Foreign Affairs Committee (1979) — The Assassination of Representative Leo J. Ryan and the Jonestown, Guyana Tragedy (House Report No. 96-223): https://www.congress.gov/
• FBI Records Vault: RYMUR (Ryan Murder / Jonestown) — Over 48,000 pages of declassified files: https://vault.fbi.gov/jonestown
• FBI Audio Tape File Q 042 ('The Death Tape', recorded Nov 18, 1978 at Jonestown, Guyana): https://archive.org/details/ptc1978-11-18.flac16

2. Academic Archives & Investigative Journalism:
• San Diego State University (SDSU) — Alternative Considerations of Jonestown & Peoples Temple: https://jonestown.sdsu.edu/
• Julia Scheeres — 'A Thousand Lives: The Untold Story of Jonestown': https://www.simonandschuster.com/
• Tim Reiterman — 'Raven: The Untold Story of the Rev. Jim Jones and His People': https://www.penguinrandomhouse.com/

3. Social Psychology & Mass Coercion Research:
• Prof. Philip Zimbardo — Destructive Obedience and Systemic Coercive Persuasion.
• Analysis of Coerced Collective Suicide and Mass Murder under armed coercion and groupthink.

4. Crisis Helplines & Support:
• National Crisis & Mental Health Lifeline (US): Dial 988 (toll-free 24/7) — https://988lifeline.org/
• National Child Abuse Hotline (US): 1-800-422-4453 — https://www.childhelp.org/
"""

SOURCES_JA = """📚 第12話 参考文献・公式調査資料一覧（ジョーンズタウンとジム・ジョーンズ）
Amber eyesは、米国連邦政府およびFBIの公式機密解除文書に基づく多角的な事実確認を徹底しています：

1. 公式政府記録および調査報告書:
• 米国下院外交委員会 (1979) — レオ・ライアン下院議員暗殺およびジョーンズタウン惨劇に関する公式調査報告書 (House Report No. 96-223): https://www.congress.gov/
• FBI機密解除公文書 Vault: RYMUR (ライアン殺害事件／ジョーンズタウン、48,000頁超): https://vault.fbi.gov/jonestown
• 現地録音テープ「The Death Tape」(FBI Audio File Q 042、1978年11月18日録音): https://archive.org/details/ptc1978-11-18.flac16

2. 学術アーカイブ・調査報道:
• サンディエゴ州立大学 (SDSU) — ジョーンズタウン総合記録資料プロジェクト: https://jonestown.sdsu.edu/
• ジュリア・シーレス —『A Thousand Lives: The Untold Story of Jonestown』: https://www.simonandschuster.com/
• ティム・ライターマン —『Raven: The Untold Story of the Rev. Jim Jones and His People』: https://www.penguinrandomhouse.com/

3. 社会心理学およびマインドコントロール研究:
• フィリップ・ジンバルドー教授 — 破壊的服従と体系的心理操作の研究。
• 武力威嚇と集団浅慮下における強要された集団自決（Mass Murder）の分析。

4. 相談窓口・支援ホットライン:
• こころの健康相談統一ダイヤル（日本）: 0570-064-556
• よりそいホットライン: 0120-279-338 (24時間通話無料) — https://www.thenewjapan.org/
"""

SOURCES_KO = """📚 제12화 참고 문헌 및 공식 수사 기록 (존스타운과 짐 존스)
Amber eyes는 미국 의회 및 FBI의 공식 기밀 해제 문서를 바탕으로 다각적 사실 확인을 거쳤습니다:

1. 공식 정부 기록 및 수사 보고서:
• 미 하원 외교위원회 (1979) — 레오 라이언 의원 암살 및 존스타운 참사 공식 수사 보고서 (House Report No. 96-223): https://www.congress.gov/
• FBI 기밀 해제 문서 RYMUR (라이언 의원 살해 및 존스타운 수사, 48,000쪽 이상): https://vault.fbi.gov/jonestown
• 현장 녹음 테이프 'The Death Tape' (FBI Audio File Q 042, 1978년 11월 18일 녹음): https://archive.org/details/ptc1978-11-18.flac16

2. 학술 기록물 및 탐사 보도:
• 샌디에이고 주립대학교 (SDSU) — 존스타운 종합 아카이브 프로젝트: https://jonestown.sdsu.edu/
• 줄리아 시어스 — 'A Thousand Lives: The Untold Story of Jonestown': https://www.simonandschuster.com/
• 팀 라이터먼 — 'Raven: The Untold Story of the Rev. Jim Jones and His People': https://www.penguinrandomhouse.com/

3. 사회심리학 및 집단 세뇌 연구:
• 필립 짐바르도 교수 — 파괴적 복종과 체계적 심리 조작 연구.
• 무력 위협과 집단사고 하에서 발생한 강요된 집단 살해(Mass Murder) 분석.

4. 긴급 상담 및 지원 핫라인:
• 자살예방 상담전화 (한국): 109 (24시간 무료)
• 보건복지상담센터: 129
"""

# ==============================================================================
# BẢN MÔ TẢ ĐẦY ĐỦ CHO TỪNG NGÔN NGỮ (STRICTLY <= 5000 KÝ TỰ)
# ==============================================================================

DESC_VI = """Tập 12: Thảm Kịch Jonestown — Khi 918 Con Người Cùng Bước Vào Chỗ Chết | Tâm lý học tội phạm: Jim Jones & Peoples Temple (Hệ Sinh Thái 10 Chỉ Dấu Tâm Lý) | Amber eyes

Ngày 18/11/1978, tại vùng rừng sâu Guyana, 918 sinh mạng vô tội — gồm hơn 300 trẻ em cùng Dân biểu Quốc hội Mỹ Leo Ryan — đã ngã xuống trong sự kiện 'Cái chết cách mạng' dưới sự chỉ huy của Jim Jones và Peoples Temple. Từng khởi đầu bằng khẩu hiệu bình đẳng xã hội và bác ái, làm sao hàng trăm con người lương thiện lại bị biến thành cỗ máy tự hủy diệt tập thể? Cuộn băng tử thần Q 042 hé lộ điều gì về cơ chế thao túng tâm lý tàn khốc nhất lịch sử?

Hồ sơ Jim Jones & Thảm kịch Jonestown được Amber eyes giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG TƯỞNG TẬP THỂ: 918 sinh mạng mất đi là tổn thất dân sự Mỹ lớn nhất trước 11/9/2001; thành ngữ 'Drinking the Kool-Aid' thành vết sẹo cảnh tỉnh sự phục tùng mù quáng; thúc đẩy Quốc hội Mỹ điều trần và cải tổ quy trình bảo hộ công dân ở nước ngoài.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem hơn 900 tín đồ là 'đạo cụ sống' phục vụ ảo tưởng quyền lực toàn năng (God Complex); sự thiếu hụt thấu cảm biến tiếng khóc trẻ em trong băng Q 042 thành công cụ cưỡng chế thống trị tột cùng.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Dựng 'Gia đình Cầu vồng' làm lá chắn đạo đức nhưng triệt tiêu tình mẫu tử; ép trẻ gọi Jones là Cha và tố cáo cha mẹ; bi kịch nhóm Thân nhân Quan ngại mòn mỏi kêu cứu trong tuyệt vọng.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Khi tội ác bị lộ sau vụ phục kích, Jones ép tập thể tự hủy để giữ ảo tưởng 'kẻ tử vì đạo'; sự hèn nhát bệnh lý lộ rõ khi ép nạn nhân uống độc nhưng tự chọn bắn súng để tránh đau đớn thể xác.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC: Đánh tráo sự hủy diệt thành 'cái chết cách mạng' để giữ phẩm giá ảo; đổ lỗi cho xã hội ('kẻ thù đã ép chúng ta'); ngoại hóa trách nhiệm thành nạn nhân của âm mưu chính trị.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Ngòi nổ là phóng sự New West (1977); Điểm gãy bùng phát chiều 18/11/1978 khi 15 tín đồ công khai theo Dân biểu Ryan về Mỹ, chọc thủng chiếc bong bóng quyền lực toàn năng.
7. CHỮ KÝ SIGNATURE VS. THỦ ĐOẠN MO: MO (biệt lập rừng sâu, tịch thu hộ chiếu, vũ trang, phục kích) liên tục đổi; Signature bất biến là kiểm soát tâm trí: loa phóng thanh 24/7, diễn tập 'Đêm Trắng' và băng ghi âm Q 042.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Bẫy chi phí chìm qua 4 nấc: (1) Bếp ăn từ thiện, phép lạ giả -> (2) Tham chính California, ép dâng tài sản, sỉ nhục tập thể -> (3) Giam lỏng tại Jonestown, diễn tập Đêm Trắng -> (4) Phục kích và hủy diệt hàng loạt.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc nhà từ thiện và quan hệ chính trị tạo khiên tàng hình khiến giới chức và báo chí ngần ngại điều tra vì sợ định kiến tôn giáo.
10. NẠN NHÂN HỌC & CẢNH BÁO ĐỎ SINH TỒN: Tôn vinh phẩm giá nạn nhân; ca ngợi Christine Miller (chất vấn Jones trong băng Q 042), Leslie Wagner-Wilson và Dân biểu Ryan; 4 cảnh báo đỏ sinh tồn nhận diện các nhóm thao túng độc hại.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Lời hứa thiên đường và bóng ma nơi rừng sâu
06:05 Hồi 2 · Cuộc phục kích đường băng và tiếng còi báo động định mệnh
11:50 Hồi 3 · Giải mã cơ chế tâm lý: Từ phục tùng đến tư duy tập thể
17:55 Hồi 4 · Cuộn băng tử thần Q 042 và tiếng nói phản kháng cô đơn
23:50 Hồi 5 · Bài học đắt giá về tâm lý bầy đàn & Cảnh báo đỏ sinh tồn

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai của Quốc hội Mỹ (House Report 96-223) và FBI Vault RYMUR. Kênh không tôn vinh hay bôi nhọ bất kỳ ai.
• Hình tượng Cú, Sói, Cáo, Cừu, Mèo là linh thú nghệ thuật. Giọng đọc, hình ảnh và âm thanh có ứng dụng công nghệ AI.

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• House Report No. 96-223: Báo cáo điều tra vụ ám sát Dân biểu Leo Ryan — https://www.congress.gov/
• FBI Vault RYMUR: Hồ sơ giải mật vụ án Jonestown — https://vault.fbi.gov/jonestown
• Băng ghi âm hiện trường FBI File Q 042 ('The Death Tape') — https://archive.org/details/ptc1978-11-18.flac16
• SDSU Jonestown Archive — https://jonestown.sdsu.edu/
• Tác phẩm: 'A Thousand Lives' (J. Scheeres) & 'Raven' (T. Reiterman)
• GS. Philip Zimbardo: Nghiên cứu Sự tuân phục hủy diệt và Thao túng tâm lý.

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ & BẢO VỆ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ khủng hoảng tâm lý): 096 306 1414
• Đường dây nóng hỗ trợ phụ nữ bị bạo lực: 1900 969 680

#AmberEyes #TrueCrime #TamLyToiPham #Jonestown #JimJones #PeoplesTemple #ThaoTungTamLy #TuDuyTapThe #10ChiDauTamLy #CanhBaoDo #HoSoToiPham"""

DESC_EN = """Ep. 12: The Jonestown Tragedy — When 918 Lives Followed a False Prophet | Criminal Psychology: Jim Jones & Peoples Temple (10 Psychological Markers) | Amber eyes

On Nov 18, 1978, in remote Guyana, 918 human beings — including over 300 children and U.S. Congressman Leo Ryan — died in what Jim Jones called a 'revolutionary death.' What began as a movement promoting racial integration degenerated into collective self-destruction. How did hundreds of decent people surrender their minds to absolute tyranny? What does the chilling 44-minute 'Death Tape' (FBI File Q 042) reveal about coercive persuasion, obedience, and groupthink?

Amber eyes dissects the case through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: 918 casualties was the largest intentional loss of American civilian life prior to 9/11; 'Drinking the Kool-Aid' became a cultural warning against blind obedience; spurred Congressional hearings and diplomatic citizen protection reforms.
2. OBJECTIFICATION OF THE VICTIM: Jones viewed 900+ followers as living props for his God Complex; profound empathy deficit meant children's cries in Tape Q 042 only triggered intense coercive domineering aggression.
3. COGNITIVE COMPARTMENTALIZATION: Used multiracial adoptees as a moral shield while destroying authentic family ties; forced children to call him Father and denounce parents; exposed the heartbreak of Concerned Relatives.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: Facing exposure after the airstrip ambush, Jones experienced narcissistic collapse; coerced mass destruction to preserve his delusion, yet chose a gunshot to avoid the agony of poison.
5. TECHNIQUES OF NEUTRALIZATION & HERO COMPLEX: Rebranded mass annihilation as a 'revolutionary death' to protect his ego; condemned condemners ('enemies forced our hand'); cast himself as a martyr resisting cosmic conspiracies.
6. PSYCHOLOGICAL TRIGGER & TIPPING POINT: Precipitating trigger was the 1977 New West exposé; tipping point was Nov 18, 1978, when 15 defectors joined Rep. Ryan's truck, shattering Jones's omnipotent control.
7. SIGNATURE VS. MODUS OPERANDI (MO): MO (jungle isolation, armed guards, airstrip ambush) evolved; Signature was immutable: total mind control via 24/7 loudspeakers, 'White Night' rehearsals, and Tape Q 042.
8. FANTASY ADDICTION & ESCALATION TRAJECTORY: Sunk cost escalation: (1) Free kitchens, fake healings in Indiana -> (2) California politics, forced asset surrender -> (3) Jonestown labor camp, loyalty rehearsals -> (4) Armed ambush and mass death.
9. HALO EFFECT & COLLECTIVE BLIND SPOTS: Humanitarian facade and civic ties created a blind spot, causing officials to avoid investigating for fear of religious bias claims.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Honoring honest victims, Christine Miller (who challenged Jones in Tape Q 042), Leslie Wagner-Wilson, and Rep. Leo Ryan; 4 survival red flags (The Gift of Fear) to identify destructive cults.

⏱ CHAPTER TIMESTAMPS
00:00 Intro & Disclaimer
00:23 Act 1 · The Promised Paradise & The Jungle Specter
06:05 Act 2 · The Airstrip Ambush & The Fatal Siren
11:50 Act 3 · Deconstructing the Mind: From Obedience to Groupthink
17:55 Act 4 · The Death Tape Q 042 & The Solitary Voice of Defiance
23:50 Act 5 · Hard Lessons on Herd Mentality & Survival Red Flags

⚠️ LEGAL & SAFETY DISCLAIMER
• Educational and historical documentary on criminal psychology; does not replace medical or legal advice.
• Derived from public archives of the U.S. Congress (House Report 96-223) and FBI Vault RYMUR. Does not glorify or defame any individual or group.
• Narrator animal avatars are artistic motifs. Narration, visuals, and soundscapes are AI-assisted.

📚 VERIFIED HISTORICAL & ACADEMIC DOSSIER
• House Report No. 96-223: Rep. Leo Ryan Investigation — https://www.congress.gov/
• FBI Vault RYMUR: Jonestown Declassified Files — https://vault.fbi.gov/jonestown
• FBI Audio File Q 042 ('The Death Tape') — https://archive.org/details/ptc1978-11-18.flac16
• SDSU Jonestown Archive — https://jonestown.sdsu.edu/
• Books: 'A Thousand Lives' (J. Scheeres) & 'Raven' (T. Reiterman)
• Prof. Philip Zimbardo: Research on Destructive Obedience & Systemic Coercion.

🆘 CRISIS HOTLINES & SUPPORT
• 988 Crisis & Mental Health Lifeline (US, toll-free 24/7): Dial 988 — https://988lifeline.org/
• National Domestic Violence Hotline (US): 1-800-799-SAFE — https://www.thehotline.org/
• Childhelp National Child Abuse Hotline: 1-800-422-4453 — https://www.childhelp.org/

#AmberEyes #TrueCrime #CriminalPsychology #Jonestown #JimJones #PeoplesTemple #CoercivePersuasion #Groupthink #10PsychologicalMarkers #SurvivalRedFlags #CaseFile"""

DESC_JA = """第12話: ジョーンズタウンの惨劇 — 918人が従った偽りの楽園 | 犯罪心理学: ジム・ジョーンズと人民寺院（10の心理的指標） | Amber eyes

1978年11月18日、南米ガイアナの孤立した密林で、現代史上例を見ない集団的悲劇が発生しました。300名を超える無垢な子どもたちや現職の米国下院議員を含む918名もの尊い命が、指導者ジム・ジョーンズが主導した「革命的死」によって失われたのです。人種融和、社会正義、平等を掲げて始まった信徒コミュニティは、いかにして集団浅慮と破壊的服従の牢獄へと堕ちていったのか。最後の44分間を克明に記録したFBI公文書テープ Q 042（Death Tape）から、人間心理の暗部を徹底解剖します。

Amber eyesは、ジム・ジョーンズとジョーンズタウンの惨劇を「10の心理・行動指標」を通じて深層分析します：
1. 社会的余波と集団的パラノイア: 918名の犠牲は9.11以前の米国市民の故意による被害として史上最大規模であり、「Drinking the Kool-Aid」という成句は盲従への警鐘として定着。米下院調査委員会および在外公館の保護制度の大改革を促しました。
2. 被害者の客体化（モノ扱い）: 900名以上の信徒を自身の全能感（神コンプレックス）を満たす「生きた小道具」として扱い、離脱希望者を裏切り者と断罪。共感性の著しい欠如と猜疑性パーソナリティが、テープQ 042における児童への無慈悲な強制へと直結しました。
3. 心理的区画化（家族の解体）: 多人種の養子を迎えた「虹の家族」を道徳的隠れ蓑とする一方、教団内部では親子の絆を徹底的に破壊。子どもに自身を「父」と呼ばせ親を告発させる非情な支配と、家族奪還に奔走した「憂慮する親族の会」の悲劇。
4. 自己愛の崩壊と病的な自己憐憫: ライアン議員銃撃後に米国の法廷で裁かれる恐怖に直面し、自己愛が崩壊。信徒には苦痛を伴う服毒を強要しながら、自らは肉体的苦痛を逃れるために銃撃による自決を選択した卑劣な本質。
5. 自己正当化と中和の技術: 集団自滅を「尊厳を守る革命的死」へとすり替え、責任を「外部の敵による陰謀」へと転嫁する道徳的中和技術。
6. 心理的引き金と転換点（ティッピングポイント）: 1977年のNew West誌による告発報道が密林移住の引き金となり、1978年11月18日に15名の信徒が公然と帰国を希望した瞬間、全能感のバブルが弾け暴力の引き金となりました。
7. 署名（Signature）対 手口（MO）: 密林隔離や武装警備、飛行場襲撃などの手口（MO）の背後に、24時間の拡声器放送、模擬演習「白い夜（White Nights）」、記録テープQ 042という絶対支配の心理的署名（Signature）が存在。
8. 妄想への耽溺とエスカレーション軌道: サンクコスト効果による4段階の上昇: (1) 慈善給食と偽りの奇跡治療 -> (2) 政界進出と財産没収、公開批判集会 -> (3) 密林の監禁所での過酷労働と白い夜の演習 -> (4) 下院議員暗殺と強要された集団自決。
9. 後光効果（ハロー効果）と社会的盲点: 人種差別撤廃と慈善活動の看板が完璧な隠れ蓑となり、政界有力者との親交が司法やメディアの追及を長年阻む社会的盲点を形成。
10. 被害者学と生存のためのレッドフラッグ: クリスティン・ミラー（テープQ 042でジョーンズに異を唱えた勇敢な女性）、子どもを背負い30マイルの密林を脱出したレスリー、そしてレオ・ライアン議員の勇気を称え、破壊的カルトを見抜く4つの生存警告（The Gift of Fear）を提示。

⏱ タイムスタンプ
00:00 イントロ＆注意事項
00:23 第1幕 · 約束された楽園と密林の暗影
06:05 第2幕 · 滑走路の待ち伏せと運命の警報
11:50 第3幕 · 心理メカニズムの解剖: 服従から集団浅慮へ
17:55 第4幕 · 死のテープQ 042と孤高の抵抗
23:50 第5幕 · 群集心理の痛恨の教訓＆生存のレッドフラッグ

⚠️ 法的留意事項および安全性
• 本動画は犯罪心理学および歴史的資料に基づく教育的コンテンツであり、医学的・心理的・法的助言に代わるものではありません。
• 米国議会公式報告書 (House Report 96-223) およびFBI機密解除資料 (RYMUR) に依拠しています。いかなる個人・団体の誹謗中傷や美化を意図するものではありません。
• フクロウ、オオカミ、キツネ等の動物キャラクターは芸術的演出の象徴です。音声、映像、音響はAI技術を活用して制作されています。

📚 公式参考文献・調査資料
• 米国下院外交委員会: House Report No. 96-223 (1979) — https://www.congress.gov/
• FBI Records Vault: RYMUR Files (Jonestown, 48,000頁超) — https://vault.fbi.gov/jonestown
• 現地録音テープ FBI Audio File Q 042 ('The Death Tape') — https://archive.org/details/ptc1978-11-18.flac16
• サンディエゴ州立大学 (SDSU) ジョーンズタウン資料館 — https://jonestown.sdsu.edu/
• ジュリア・シーレス: 『A Thousand Lives: The Untold Story of Jonestown』
• ティム・ライターマン: 『Raven: The Untold Story of Rev. Jim Jones』
• フィリップ・ジンバルドー教授: 破壊的服従と集団圧力の研究。

🆘 相談窓口・支援ホットライン
• こころの健康相談統一ダイヤル: 0570-064-556
• よりそいホットライン (24時間無料): 0120-279-338 — https://www.thenewjapan.org/
• 児童相談所虐待対応ダイヤル: 189 (いちはやく・通話料無料)

#AmberEyes #TrueCrime #犯罪心理学 #ジョーンズタウン #ジムジョーンズ #人民寺院 #マインドコントロール #集団浅慮 #10の心理的指標 #事件ファイル"""

DESC_KO = """제12화: 존스타운의 비극 — 918명의 생명을 앗아간 거짓 낙원 | 범죄심리학: 짐 존스와 인민사원 (10가지 심리적 지표) | Amber eyes

1978년 11월 18일, 남아메리카 가이아나의 외딴 밀림 속에서 현대 인류 역사상 유례없는 참혹한 집단 비극이 발생했습니다. 300명이 넘는 무고한 어린이들과 현직 미국 연방 하원의원을 포함한 918명의 소중한 생명이, 사이비 교주 짐 존스가 주도한 이른바 '혁명적 죽음'에 의해 희생되었습니다. 인종 평등, 사회 정의, 인도주의를 표방하며 시작된 공동체가 어떻게 집단적 맹종과 자멸의 도가니로 전락했는가? 최후의 44분을 생생히 담은 FBI 비밀 녹음 테이프 Q 042(Death Tape)를 통해 가스라이팅과 집단사고의 치명적인 심리 메커니즘을 심층 해부합니다.

Amber eyes는 짐 존스와 존스타운 참사를 '10가지 핵심 심리·행동 지표'를 통해 입체적으로 분석합니다:
1. 사회적 파장과 집단적 불안·파라노이아: 918명의 희생은 9·11 테러 이전 미국 민간인이 고의로 희생된 단일 사건 중 최대 규모였으며, 'Drinking the Kool-Aid'는 맹목적 추종에 대한 사회적 경고로 남았습니다. 미 의회 청문회 및 외교부 재외국민 긴급 보호 체계의 전면적 개혁을 촉발했습니다.
2. 피해자의 사물화 및 객체화: 존스는 900여 명의 신도를 자신의 전능감(God Complex)을 충족시키는 '살아있는 소품'으로 취급했으며, 탈출 희망자를 용서받을 수 없는 배신자로 규정했습니다. 심각한 정서적 공감 결여로 인해 테이프 Q 042 속 어린이들의 울음소리조차 잔혹한 지배 본능을 자극하는 도구에 불과했습니다.
3. 인지적 구획화와 가족 해체: 다인종 입양아들로 구성된 '무지개 가족'을 도덕적 방패로 삼았으나, 내부적으로는 부모와 자식 간의 유대를 철저히 파괴했습니다. 아이들이 존스를 '아버지'라 부르고 친부모를 집단 비판하게 만들었으며, 가족을 구하려던 '우려하는 친척 모임'의 비극을 낳았습니다.
4. 나르시시즘적 붕괴와 병적 자기연민: 라이언 의원 일행 기습 이후 미 사법 당국의 법정에 설 위기에 직면하자 나르시시즘적 자아가 붕괴되었습니다. 메시아적 망상을 지키기 위해 집단 자멸을 강요하면서도, 정작 자신은 신체적 고통을 피하려 총기 자결을 택한 비열한 본성이 드러났습니다.
5. 자기 정당화 및 중화 기술: 집단 파멸을 존엄을 지키는 '혁명적 죽음'으로 미화하고, '외부의 적이 우리를 궁지로 몰았다'며 피해자와 사회를 비난하는 도덕적 중화 기술을 구사했습니다.
6. 심리적 방아쇠와 티핑 포인트: 1977년 New West 지의 폭로 보도가 밀림 도피의 방아쇠가 되었으며, 1978년 11월 18일 오후 15명의 신도가 라이언 의원의 귀국 트럭에 탑승한 순간 존스의 전능감 풍선이 터지며 무자비한 집단 파멸 명령으로 이어졌습니다.
7. 시그니처(Signature) vs 범행 수법(MO): 밀림 격리, 여권 압수, 무장 경비 등 수법(MO)은 환경에 따라 진화했으나, 24시간 확성기 세뇌 방송, 모의 훈련인 '화이트 나이트(White Nights)', 최후의 순간을 기록한 Q 042 테이프는 절대적 정신 지배라는 변치 않는 심리적 시그니처였습니다.
8. 환상 중독과 에스컬레이션 궤적: 매몰비용 오류를 이용한 4단계 상승: (1) 인디애나 시절 무료 급식소와 가짜 기적 치유 -> (2) 캘리포니아 정계 유착, 재산 강탈, 집단 모욕 집회 -> (3) 존스타운 감금소 노역과 화이트 나이트 모의 훈련 -> (4) 하원의원 암살 및 강요된 대규모 자멸.
9. 후광 효과(Halo Effect)와 제도의 맹점: 사회 운동가라는 대외적 명망과 유력 정치인들과의 유착이 완벽한 투명 망토 역할을 하여, 사법 당국과 언론이 종교 탄압 논란을 우려해 장기간 수사를 회피하는 제도의 맹점을 형성했습니다.
10. 피해자학 및 생존을 위한 레드플래그: 무고한 피해자들의 인간적 존엄을 복원하며, 테이프 Q 042에서 교주에게 당당히 맞선 크리스틴 밀러, 아이를 안고 30마일 밀림을 탈출한 레슬리, 그리고 목숨을 바친 레오 라이언 의원의 용기를 기립니다. 파괴적 사이비 집단을 식별하는 4가지 생존 레드플래그(The Gift of Fear)를 제시합니다.

⏱ 챕터 타임스탬프
00:00 인트로 및 안내
00:23 제1막 · 약속의 낙원과 밀림의 유령
06:05 제2막 · 활주로의 매복과 운명의 사이렌
11:50 제3막 · 심리 메커니즘 해부: 복종에서 집단사고까지
17:55 제4막 · 죽음의 테이프 Q 042와 고독한 저항
23:50 제5막 · 군중심리의 뼈아픈 교훈 & 생존을 위한 레드플래그

⚠️ 법적 고지 및 안내
• 본 영상은 범죄심리학 및 역사적 자료에 기반한 교육용 콘텐츠이며, 의학적·심리학적·법률적 자문을 대신할 수 없습니다.
• 미국 의회 공식 보고서 (House Report 96-223) 및 FBI 기밀 해제 문서 (RYMUR)에 기반합니다. 특정 개인이나 단체를 찬양하거나 비방할 목적이 없습니다.
• 부엉이, 늑대, 여우 등의 동물 캐릭터는 예술적 연출을 위한 가상 캐릭터입니다. 내레이션, 이미지, 음향 제작에 AI 기술이 활용되었습니다.

📚 공식 참고 문헌 및 수사 기록
• 미 하원 외교위원회: House Report No. 96-223 (1979) — https://www.congress.gov/
• FBI Records Vault: RYMUR Files (존스타운 수사, 48,000쪽 이상) — https://vault.fbi.gov/jonestown
• 현장 녹음 테이프 FBI Audio File Q 042 ('The Death Tape') — https://archive.org/details/ptc1978-11-18.flac16
• 샌디에이고 주립대 (SDSU) 존스타운 아카이브 — https://jonestown.sdsu.edu/
• 줄리아 시어스: 'A Thousand Lives: The Untold Story of Jonestown'
• 팀 라이터먼: 'Raven: The Untold Story of Rev. Jim Jones'
• 필립 짐바르도 교수: 파괴적 복종 및 체계적 세뇌 연구.

🆘 긴급 상담 및 도움 핫라인
• 자살예방 상담전화: 109 (24시간 무료)
• 정신건강 상담전화: 1577-0199
• 여성긴급전화: 1366
• 아동학대 신고전화: 112

#AmberEyes #TrueCrime #범죄심리학 #존스타운 #짐존스 #인민사원 #가스라이팅 #집단사고 #10가지심리적지표 #생존레드플래그 #사건파일"""

# ==============================================================================
# HÀM GHI FILE & KIỂM ĐỊNH KÍCH THƯỚC
# ==============================================================================

def write_text(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    clean_content = content.strip().replace("\r\n", "\n").replace("\r", "\n")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(clean_content + "\n")


def main():
    print("=== ĐO LƯỜNG ĐỘ DÀI MÔ TẢ TẬP 12 (TRẦN: 5000 KÝ TỰ) ===")
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
        
    print("\n=== TIẾN HÀNH XUẤT BẢN FILE MÔ TẢ & NGUỒN TẬP 12 ===")
    
    files_to_write = [
        # Tiếng Việt
        (ROOT / "02_SAN_XUAT" / "Tap12" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap12" / "xuat_ban" / "mo_ta.txt", DESC_VI),
        (ROOT / "02_SAN_XUAT" / "Tap12" / "nguon_mo_ta.txt", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap12" / "nguon_tham_khao.md", SOURCES_VI),
        (ROOT / "02_SAN_XUAT" / "Tap12" / "xuat_ban" / "nguon_tham_khao.md", SOURCES_VI),
        
        # Tiếng Anh
        (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "xuat_ban" / "description.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
        (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "nguon_tham_khao_EN.md", SOURCES_EN),
        (ROOT / "02_SAN_XUAT" / "Tap12_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", SOURCES_EN),
        
        # Tiếng Nhật
        (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "xuat_ban" / "description.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
        (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "nguon_tham_khao_JA.md", SOURCES_JA),
        (ROOT / "02_SAN_XUAT" / "Tap12_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", SOURCES_JA),
        
        # Tiếng Hàn
        (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "xuat_ban" / "description.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
        (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "nguon_tham_khao_KO.md", SOURCES_KO),
        (ROOT / "02_SAN_XUAT" / "Tap12_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", SOURCES_KO),
    ]
    
    for path, content in files_to_write:
        write_text(path, content)
        print(f"  -> Đã ghi: {path.relative_to(ROOT)} ({len(content.strip()):,} ký tự)")
        
    print("\n>>> TẤT CẢ FILE MÔ TẢ TẬP 12 ĐÃ ĐƯỢC CẬP NHẬT HOÀN TẤT VÀ ĐẠT CHUẨN! <<<")


if __name__ == "__main__":
    main()
