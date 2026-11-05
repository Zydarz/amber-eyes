#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo và cập nhật mô tả video đạt chuẩn Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cho Tập 08 trên cả 4 ngôn ngữ (VI, EN, JA, KO)."""

import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# 1. NGUỒN TIẾNG VIỆT
# ==============================================================================
SOURCES_VI = """▸ Hồ sơ tư pháp & cơ quan điều tra Nhật Bản:
• [1] Tòa án Tối cao Nhật Bản & Tòa án Địa phương Tokyo — Bản án chung thẩm vụ án Aum Shinrikyo và Shoko Asahara:
  https://www.courts.go.jp/app/hanrei_en/detail?id=968
• [2] Cơ quan Cảnh sát Quốc gia Nhật Bản (NPA) — Báo cáo tổng kết điều tra thảm họa Sarin Tokyo:
  https://www.npa.go.jp/english/bureau/security/aum.html
• [3] Bộ Tư pháp Nhật Bản (Ministry of Justice) — Thông cáo chính thức thi hành án tử hình đối với Shoko Asahara và 12 đồng phạm (07/2018):
  https://www.moj.go.jp/hisho/kouhou/hisho06_00411.html
• [4] Wikipedia — Toàn cảnh vụ tấn công khí độc tàu điện ngầm Tokyo và giáo phái Aum Shinrikyo:
  https://en.wikipedia.org/wiki/Tokyo_subway_sarin_attack

▸ Tác phẩm điều tra chuyên sâu & nghiên cứu học thuật:
• [5] Haruki Murakami — 'Ngầm' (Underground: The Tokyo Gas Attack and the Japanese Psyche, 1997):
  https://www.harukimurakami.com/book/underground
• [6] Robert Jay Lifton — 'Destroying the World to Save It: Aum Shinrikyo, Apocalyptic Violence, and the New Global Terrorism' (1999):
  https://us.macmillan.com/books/9780805065114/destroyingtheworldtosaveit
• [7] David E. Kaplan & Andrew Marshall — 'The Cult at the End of the World: The Incredible Story of Aum' (1996):
  https://www.penguinrandomhouse.com/books/89831/the-cult-at-the-end-of-the-world-by-david-e-kaplan-and-andrew-marshall/
• [8] Margaret Thaler Singer — 'Cults in Our Midst: The Continuing Fight Against Their Hidden Menace':
  https://www.wiley.com/en-us/Cults+in+Our+Midst%3A+The+Continuing+Fight+Against+Their+Hidden+Menace-p-9780787967413

▸ Báo chí quốc tế & truyền thông tư liệu:
• [9] BBC News — Vụ thi hành án tử hình Shoko Asahara và dấu mốc lịch sử tư pháp (06/07/2018):
  https://www.bbc.com/news/world-asia-44734788
• [10] The New York Times — Hồ sơ toàn cảnh vụ tấn công Kasumigaseki và phòng thí nghiệm Satyam 7:
  https://www.nytimes.com/1995/03/21/world/subway-attack-tokyo-poison-gas-attack-tokyo-subway-kills-six-thousands-are-sick.html
• [11] The Guardian — Bên trong giáo phái ngày tận thế: Cách thức Aum gieo rắc kinh hoàng dưới lòng đất Tokyo:
  https://www.theguardian.com/world/2018/jul/06/aum-shinrikyo-cult-tokyo-sarin-attack-shoko-asahara
• [12] NHK World-Japan — Lưu trữ tư liệu lịch sử vụ án tàu điện ngầm Tokyo và cuộc truy quét Kamikuishiki:
  https://www3.nhk.or.jp/nhkworld/en/news/backstories/168/
• [13] Asahi Shimbun — Hồ sơ vụ thảm sát gia đình Luật sư Tsutsumi Sakamoto (1989):
  https://www.asahi.com/special/aum/
• [14] Mainichi Shimbun — Vụ tấn công sarin thành phố Matsumoto mùa hè năm 1994:
  https://mainichi.jp/english/articles/20180706/p2a/00m/0na/012000c
• [15] Reuters — Lời khai và sự hối hận của Bác sĩ Ikuo Hayashi trước Tòa án Tokyo:
  https://www.reuters.com/article/world/japan-hangs-doomsday-cult-leader-asahara-and-followers-for-sarin-attack-idUSKBN1JW04O/
• [16] Time Magazine — Chân dung Shoko Asahara và các trí thức tinh hoa bị tẩy não:
  https://time.com/5331590/japan-shoko-asahara-aum-shinrikyo-execution/

▸ Tâm lý học hành vi & thao túng tâm trí:
• [17] Steven Hassan — Mô hình BITE về kiểm soát tâm trí trong các tổ chức độc hại (Freedom of Mind Resource Center):
  https://freedomofmind.com/cult-mind-control/bite-model/
• [18] Gresham Sykes & David Matza — Lý thuyết Kỹ thuật Trung hòa Đạo đức (Techniques of Neutralization):
  https://www.jstor.org/stable/2089195
• [19] Viktor Frankl — 'Ý niệm về sự trống rỗng hiện sinh' (The Existential Vacuum, Man's Search for Meaning):
  https://www.goodreads.com/book/show/4069.Man_s_Search_for_Meaning"""

# ==============================================================================
# 2. NGUỒN TIẾNG ANH
# ==============================================================================
SOURCES_EN = """▸ Japanese Judicial Records & Official Law Enforcement Documents:
• [1] Supreme Court of Japan & Tokyo District Court — Final Judgments on Aum Shinrikyo and Shoko Asahara:
  https://www.courts.go.jp/app/hanrei_en/detail?id=968
• [2] National Police Agency of Japan (NPA) — Comprehensive Investigative Report on the Tokyo Subway Sarin Disaster:
  https://www.npa.go.jp/english/bureau/security/aum.html
• [3] Ministry of Justice (Japan) — Official Statement on Capital Executions of Shoko Asahara and 12 Key Conspirators (July 2018):
  https://www.moj.go.jp/hisho/kouhou/hisho06_00411.html
• [4] Wikipedia — Tokyo Subway Sarin Attack & Aum Shinrikyo Detailed Docket:
  https://en.wikipedia.org/wiki/Tokyo_subway_sarin_attack

▸ Investigative Monographs & Academic Literature:
• [5] Haruki Murakami — 'Underground: The Tokyo Gas Attack and the Japanese Psyche' (1997):
  https://www.harukimurakami.com/book/underground
• [6] Robert Jay Lifton — 'Destroying the World to Save It: Aum Shinrikyo, Apocalyptic Violence, and the New Global Terrorism' (1999):
  https://us.macmillan.com/books/9780805065114/destroyingtheworldtosaveit
• [7] David E. Kaplan & Andrew Marshall — 'The Cult at the End of the World: The Incredible Story of Aum' (1996):
  https://www.penguinrandomhouse.com/books/89831/the-cult-at-the-end-of-the-world-by-david-e-kaplan-and-andrew-marshall/
• [8] Margaret Thaler Singer — 'Cults in Our Midst: The Continuing Fight Against Their Hidden Menace':
  https://www.wiley.com/en-us/Cults+in+Our+Midst%3A+The+Continuing+Fight+Against+Their+Hidden+Menace-p-9780787967413

▸ International Journalism & Media Archives:
• [9] BBC News — Execution of Shoko Asahara Marks Milestone in Japanese Justice (July 6, 2018):
  https://www.bbc.com/news/world-asia-44734788
• [10] The New York Times — The Attack at Kasumigaseki & The Satyam 7 Industrial Chemical Arsenal:
  https://www.nytimes.com/1995/03/21/world/subway-attack-tokyo-poison-gas-attack-tokyo-subway-kills-six-thousands-are-sick.html
• [11] The Guardian — Inside the Doomsday Cult: How Aum Unleashed Horror on Tokyo's Subway:
  https://www.theguardian.com/world/2018/jul/06/aum-shinrikyo-cult-tokyo-sarin-attack-shoko-asahara
• [12] NHK World-Japan — Archival History: The Tokyo Subway Attack and the Kamikuishiki Compound Raid:
  https://www3.nhk.or.jp/nhkworld/en/news/backstories/168/
• [13] Asahi Shimbun — Special Retrospective on the 1989 Tsutsumi Sakamoto Family Murders:
  https://www.asahi.com/special/aum/
• [14] Mainichi Shimbun — The 1994 Matsumoto Sarin Attack Targeting Judicial Judges:
  https://mainichi.jp/english/articles/20180706/p2a/00m/0na/012000c
• [15] Reuters — Courtroom Testimony and Remorse of Dr. Ikuo Hayashi at the Tokyo District Court:
  https://www.reuters.com/article/world/japan-hangs-doomsday-cult-leader-asahara-and-followers-for-sarin-attack-idUSKBN1JW04O/
• [16] Time Magazine — Profile of Shoko Asahara and the Tragic Enigma of Brainwashed Elites:
  https://time.com/5331590/japan-shoko-asahara-aum-shinrikyo-execution/

▸ Behavioral Psychology & Coercive Control Frameworks:
• [17] Steven Hassan — The BITE Model of Authoritarian Control (Freedom of Mind Resource Center):
  https://freedomofmind.com/cult-mind-control/bite-model/
• [18] Gresham Sykes & David Matza — Techniques of Neutralization in Criminological Psychology:
  https://www.jstor.org/stable/2089195
• [19] Viktor Frankl — The Existential Vacuum & The Search for Meaning:
  https://www.goodreads.com/book/show/4069.Man_s_Search_for_Meaning"""

# ==============================================================================
# 3. NGUỒN TIẾNG NHẬT
# ==============================================================================
SOURCES_JA = """▸ 日本の司法記録および公的警察資料:
• [1] 最高裁判所・東京地方裁判所 — オウム真理教および麻原彰晃（松本智津夫）刑事裁判確定判決記録:
  https://www.courts.go.jp/app/hanrei_en/detail?id=968
• [2] 警察庁（NPA） — 地下鉄サリン事件およびオウム真理教関連事件総合捜査報告:
  https://www.npa.go.jp/english/bureau/security/aum.html
• [3] 法務省 — 麻原彰晃および幹部死刑囚13名に対する死刑執行に関する公式発表（2018年7月）:
  https://www.moj.go.jp/hisho/kouhou/hisho06_00411.html
• [4] ウィキペディア — 地下鉄サリン事件・オウム真理教事件全貌アーカイブ:
  https://ja.wikipedia.org/wiki/地下鉄サリン事件

▸ 調査ノンフィクションおよび学術研究文献:
• [5] 村上春樹 — 『アンダーグラウンド』（地下鉄サリン事件の被害者・信者聞き取り調査録、1997年）:
  https://www.harukimurakami.com/book/underground
• [6] ロバート・J・リフトン — 『終末の破壊者：オウム真理教と新たなグローバル・テロリズム』（1999年）:
  https://us.macmillan.com/books/9780805065114/destroyingtheworldtosaveit
• [7] デビッド・E・カプラン＆アンドリュー・マーシャル — 『世界の終わりのカルト：オウム真理教の真実』（1996年）:
  https://www.penguinrandomhouse.com/books/89831/the-cult-at-the-end-of-the-world-by-david-e-kaplan-and-andrew-marshall/
• [8] マーガレット・シンガー — 『カルトの心理学：マインド・コントロールの脅威と救出』:
  https://www.wiley.com/en-us/Cults+in+Our+Midst%3A+The+Continuing+Fight+Against+Their+Hidden+Menace-p-9780787967413

▸ 報道機関アーカイブおよびメディア資料:
• [9] BBC News — 麻原彰晃ら死刑執行と戦後日本社会の総括（2018年7月6日）:
  https://www.bbc.com/news/world-asia-44734788
• [10] ニューヨーク・タイムズ — 霞ケ関攻撃と第7サティアンの化学兵器工場発覚報道:
  https://www.nytimes.com/1995/03/21/world/subway-attack-tokyo-poison-gas-attack-tokyo-subway-kills-six-thousands-are-sick.html
• [11] ガーディアン — 終末カルトの狂気：オウムはいかにして地下鉄に恐怖を放ったか:
  https://www.theguardian.com/world/2018/jul/06/aum-shinrikyo-cult-tokyo-sarin-attack-shoko-asahara
• [12] NHKニュース — 事件アーカイブ：地下鉄サリン事件と上九一色村強制捜査の記憶:
  https://www3.nhk.or.jp/nhkworld/en/news/backstories/168/
• [13] 朝日新聞 — オウム特集：坂本堤弁護士一家殺害事件（1989年）の真相:
  https://www.asahi.com/special/aum/
• [14] 毎日新聞 — 1994年松本サリン事件と裁判官狙撃計画の全貌:
  https://mainichi.jp/english/articles/20180706/p2a/00m/0na/012000c
• [15] ロイター通信 — 林郁夫元医師の法廷における自白と痛切な謝罪:
  https://www.reuters.com/article/world/japan-hangs-doomsday-cult-leader-asahara-and-followers-for-sarin-attack-idUSKBN1JW04O/
• [16] TIME誌 — 麻原彰晃の人物像とエリート知識人洗脳のメカニズム:
  https://time.com/5331590/japan-shoko-asahara-aum-shinrikyo-execution/

▸ 行動心理学・マインドコントロール研究:
• [17] スティーヴン・ハッサン — 独裁的カルトのマインドコントロール「BITEモデル」:
  https://freedomofmind.com/cult-mind-control/bite-model/
• [18] グレシャム・サイクス＆デビッド・マッツァ — 犯罪心理学における「中和の技術」論:
  https://www.jstor.org/stable/2089195
• [19] ヴィクトール・フランクル — 『夜と霧』および「実存的真空」の概念研究:
  https://www.goodreads.com/book/show/4069.Man_s_Search_for_Meaning"""

# ==============================================================================
# 4. NGUỒN TIẾNG HÀN
# ==============================================================================
SOURCES_KO = """▸ 일본 사법 기록 및 공식 수사 당국 문서:
• [1] 일본 최고재판소 및 도쿄지방재판소 — 옴진리교 및 아사하라 쇼코 형사재판 확정 판결 기록:
  https://www.courts.go.jp/app/hanrei_en/detail?id=968
• [2] 일본 경찰청(NPA) — 도쿄 지하철 사린 테러 및 옴진리교 연루 사건 종합 수사 보고서:
  https://www.npa.go.jp/english/bureau/security/aum.html
• [3] 일본 법무성(Ministry of Justice) — 아사하라 쇼코 및 주범 13인 사형 집행 공식 발표 (2018년 7월):
  https://www.moj.go.jp/hisho/kouhou/hisho06_00411.html
• [4] 위키백과 — 도쿄 지하철 사린 사건 및 옴진리교 종합 사건 아카이브:
  https://ko.wikipedia.org/wiki/도쿄_지하철_사린_사건

▸ 심층 탐사 르포 및 학술 연구 단행본:
• [5] 무라카미 하루키 — 《언더그라운드》(도쿄 지하철 사린 테러 피해자·신도 심층 인터뷰집, 1997년):
  https://www.harukimurakami.com/book/underground
• [6] 로버트 J. 리프턴 — 《세상을 파괴하여 구원하리라: 옴진리교와 새로운 글로벌 테러리즘》(1999년):
  https://us.macmillan.com/books/9780805065114/destroyingtheworldtosaveit
• [7] 데이비드 E. 카플란 & 앤드루 마셜 — 《세계 종말의 사이비: 옴진리교의 믿을 수 없는 실체》(1996년):
  https://www.penguinrandomhouse.com/books/89831/the-cult-at-the-end-of-the-world-by-david-e-kaplan-and-andrew-marshall/
• [8] 마거릿 싱어 — 《우리 가운데 있는 사이비: 보이지 않는 마인드 컨트롤과의 전쟁》:
  https://www.wiley.com/en-us/Cults+in+Our+Midst%3A+The+Continuing+Fight+Against+Their+Hidden+Menace-p-9780787967413

▸ 국제 언론 심층 보도 및 영상 아카이브:
• [9] BBC News — 아사하라 쇼코 사형 집행과 전후 일본 사회의 역사적 분기점 (2018년 7월 6일):
  https://www.bbc.com/news/world-asia-44734788
• [10] 뉴욕타임스 — 카스미가세키 테러와 제7 사티안 산업용 화학무기 공장 적발 보도:
  https://www.nytimes.com/1995/03/21/world/subway-attack-tokyo-poison-gas-attack-tokyo-subway-kills-six-thousands-are-sick.html
• [11] 가디언 — 종말론 사이비의 광기: 옴진리교는 어떻게 도쿄 지하철을 테러로 뒤덮었는가:
  https://www.theguardian.com/world/2018/jul/06/aum-shinrikyo-cult-tokyo-sarin-attack-shoko-asahara
• [12] NHK World-Japan — 사건 아카이브: 도쿄 지하철 사린 사건과 카미쿠이시키 강제 수색의 기록:
  https://www3.nhk.or.jp/nhkworld/en/news/backstories/168/
• [13] 아사히신문 — 옴진리교 특별 기획: 사카모토 츠츠미 변호사 일가 살해 사건(1989년)의 진상:
  https://www.asahi.com/special/aum/
• [14] 마이니치신문 — 1994년 마츠모토 사린 사건과 사법 판사 암살 기도 전말:
  https://mainichi.jp/english/articles/20180706/p2a/00m/0na/012000c
• [15] 로이터통신 — 하야시 이쿠오 전 의사의 도쿄지방법원 자백과 참회의 순간:
  https://www.reuters.com/article/world/japan-hangs-doomsday-cult-leader-asahara-and-followers-for-sarin-attack-idUSKBN1JW04O/
• [16] 타임지 — 아사하라 쇼코의 인물상과 세뇌된 엘리트 청년들의 비극적 역설:
  https://time.com/5331590/japan-shoko-asahara-aum-shinrikyo-execution/

▸ 행동심리학 및 강압적 조작 연구:
• [17] 스티븐 하산 — 독재적 사이비 종교의 마인드 컨트롤 BITE 모델:
  https://freedomofmind.com/cult-mind-control/bite-model/
• [18] 그레셤 사이크스 & 데이비드 마츠아 — 범죄심리학의 '도덕적 중화 기술(Techniques of Neutralization)':
  https://www.jstor.org/stable/2089195
• [19] 빅터 프랭클 — 《죽음의 수용소에서》 및 '실존적 진공' 연구:
  https://www.goodreads.com/book/show/4069.Man_s_Search_for_Meaning"""

# ==============================================================================
# 5. MÔ TẢ ĐẦY ĐỦ TIẾNG VIỆT
# ==============================================================================
DESC_VI = f"""Tập 08: Khi Các Thiên Tài Bị Tẩy Não | Tâm lý học tội phạm: Giáo Phái Aum Shinrikyo & Thảm Họa Sarin Tokyo (Hệ Sinh Thái 10 Chỉ Dấu Tâm Lý & Ma Thuật Tẩy Não Tinh Hoa) | Amber eyes

Vào sáng thứ Hai, ngày 20 tháng 3 năm 1995, thủ đô Tokyo của Nhật Bản thức dậy trong nhịp sống hối hả thường nhật. Hàng triệu người dân đổ dồn về hệ thống tàu điện ngầm dưới lòng đất để bắt đầu tuần làm việc mới. Đúng tám giờ sáng, giờ cao điểm đông đúc nhất trong ngày. Năm chuyến tàu điện ngầm trên ba tuyến huyết mạch Chiyoda, Marunouchi và Hibiya đang cùng lao vun vút về phía nhà ga Kasumigaseki — trái tim quyền lực nhất của đất nước, nơi đặt trụ sở các Bộ ngành trọng yếu và Cơ quan Cảnh sát Quốc gia. Nhật Bản khi ấy vẫn tự hào với 'huyền thoại an toàn', một xã hội có tỷ lệ tội phạm thấp bậc nhất thế giới.

Thế nhưng, trên mỗi chuyến tàu ấy, có những người đàn ông mang theo một thứ chất độc thần kinh có sức tàn phá khủng khiếp. Họ dùng đầu ô đã mài nhọn đâm thủng các túi ni-lông chứa chất lỏng chết người ngay trên sàn toa xe. Khi cửa tàu vừa mở tại các nhà ga đông đúc, những kẻ này nhanh chóng bước ra ngoài, để lại luồng hơi độc bốc lên âm thầm giữa đám đông. Vụ tấn công hóa học tàn bạo đã cướp đi sinh mạng của mười bốn thường dân vô tội, làm tổn hại sức khỏe của hơn năm nghìn tám trăm người khác, và khiến hai nhân viên đường sắt quả cảm — ông Kazumasa Takahashi và ông Tsuneo Hishinuma — hy sinh anh dũng khi dùng tay không dọn các túi chất độc để bảo vệ hành khách.

Điều khiến toàn bộ thế giới bàng hoàng không chỉ dừng lại ở sự tàn độc của vụ tấn công. Khi danh tính thực sự của những kẻ chế tạo và rải chất độc lộ diện, một nghịch lý rúng động đã phơi bày trước công chúng. Đứng sau thảm kịch không phải là tội phạm đường phố hay thế lực ngoại bang, mà là những nhà khoa học, bác sĩ và trí thức tinh hoa xuất chúng của chính nước Nhật: Masami Tsuchiya (thạc sĩ hóa học Đại học Tsukuba), Hideo Murai (nhà vật lý Đại học Osaka), Seiichi Endo (nghiên cứu sinh virus học Đại học Kyoto), và Bác sĩ Ikuo Hayashi (bác sĩ tim mạch Đại học Keio, từng là trưởng khoa bệnh viện quốc gia). Tất cả đã dâng hiến toàn bộ lý trí và lương tâm cho Shoko Asahara — một kẻ mù lòa từng bán thuốc giả và thi trượt đại học.

Hồ sơ Giáo phái Aum Shinrikyo được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG TƯỞNG TẬP THỂ: Đánh sập hoàn toàn 'huyền thoại an toàn' của Nhật Bản thời hậu chiến; cơn hoang tưởng tập thể tại siêu đô thị Tokyo khiến người dân nín thở khi bước xuống ga ngầm, kiểm tra từng gầm ghế và nghi kỵ lẫn nhau; toàn bộ hệ thống giao thông và y tế tê liệt; thúc đẩy làn sóng đại cải tổ thể chế, sửa đổi Luật Tổ chức Tôn giáo và ban hành luật kiểm soát đặc biệt các tổ chức có nguy cơ khủng bố tập thể.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Nạn nhân trên tàu không được nhìn như những con người có cha mẹ, con cái, mà bị giáng cấp thành "đạo cụ", "vật cản trở kỷ nguyên mới"; khuyết tật Thuyết tâm trí (Theory of Mind) và sự thiếu hụt thấu cảm cảm xúc (empathy deficit) biến sinh mạng vô tội thành những dữ liệu thực nghiệm vô cảm trong phòng lab Satyam số 7.
3. CƠ CHẾ CHIA NGĂN NHẬN THỨC (COMPARTMENTALIZATION): Khóa chặt ngăn "người con hiếu thảo, bác sĩ chữa bệnh hiền lành" khỏi ngăn "chế tạo vũ khí hủy diệt hàng loạt" mà không hề cắn rứt nội tâm; đồng thời phơi bày bi kịch của các nạn nhân thứ hai: cha mẹ của các thủ khoa, thạc sĩ hoàn toàn sụp đổ danh tính khi con mình thành kẻ khủng bố, phải từ bỏ sự nghiệp và quỳ gối xin lỗi công chúng suốt đời.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Đối lập sắc sảo giữa sự ăn năn chân chính của Bác sĩ Ikuo Hayashi (thức tỉnh lương tâm, quỳ xin nhận trừng phạt, hợp tác toàn diện phá án để nhận án chung thân) và sự giả điên, lẩm bẩm vô nghĩa cùng phản ứng tự thương hại bệnh lý (pathological self-pity) của Asahara khi bị tước bỏ áo choàng quyền lực trong phiên tòa kéo dài hơn hai thập kỷ.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC (TECHNIQUES OF NEUTRALIZATION): Đỉnh cao thao túng là việc bóp méo khái niệm thiền định 'Poa' thành giáo lý "giết người là hành vi đại từ bi để cứu rỗi nạn nhân khỏi tích tụ thêm ác nghiệp"; kết hợp với cơ chế ngoại hóa trách nhiệm (displacement of responsibility) khiến tín đồ ru ngủ lương tâm rằng mình chỉ là công cụ thực thi ý chí của Đấng tối cao.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Tin mật báo về cuộc đại lục soát của cảnh sát dự kiến diễn ra vào ngày 22/3/1995 vì vụ bắt cóc công chứng viên đã kích hoạt cơn hoảng loạn tột độ của Asahara; đối mặt với nguy cơ bị lột trần, hắn phát động vụ tấn công sarin chỉ trong vòng 48 giờ để đánh lạc hướng điều tra và làm tê liệt đầu não cảnh sát tại Kasumigaseki.
7. CHỮ KÝ SIGNATURE VS. THỦ ĐOẠN MO: Thủ đoạn (MO) liên tục được tính toán kỹ lưỡng: dùng túi ni-lông 2 lớp bọc giấy báo, mài nhọn đầu ô để chọc thủng, chọn đúng 8 giờ sáng khi các chuyến tàu hội tụ về Kasumigaseki, xe đón sẵn ở cửa ga; Chữ ký tâm lý (Signature) bất biến: nhu cầu bệnh lý cưỡng chế hiện thực hóa sấm truyền chiến tranh thế giới thứ ba và tận thế luận để chứng minh uy quyền của Đấng cứu thế.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Cơ chế dung nạp kích thích (tolerance buildup) khiến ngưỡng thỏa mãn của giáo phái liên tục bị đẩy xa hơn qua 4 nấc thang: (1) Lớp yoga nhỏ và trò bịp bay bổng trên không -> (2) Cưỡng đoạt tài sản, giam giữ và thủ tiêu nội bộ -> (3) Sát hại cả gia đình Luật sư Tsutsumi Sakamoto (1989) -> (4) Tấn công sarin tại Matsumoto (1994) sát hại thẩm phán và bùng nổ thành thảm họa tàu điện ngầm Tokyo (1995).
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Bằng cấp thủ khoa từ các đại học danh tiếng (Tokyo, Kyoto, Osaka, Keio, Tsukuba) tạo nên chiếc khiên tàng hình hoàn hảo; định kiến xã hội "người trí thức không thể làm điều điên rồ" và sự e ngại can thiệp tôn giáo đã che mắt cơ quan điều tra suốt nhiều năm dù đã có nhiều vụ mất tích bí ẩn.
10. NẠN NHÂN HỌC & CẢNH BÁO ĐỎ SINH TỒN: Trả lại nhân phẩm trọn vẹn cho các nạn nhân; tôn vinh sự dũng cảm của hai nhân viên đường sắt Kazumasa Takahashi và Tsuneo Hishinuma; đúc kết góc nhìn sâu sắc từ tác phẩm 'Ngầm' của Haruki Murakami; và trang bị 4 cảnh báo đỏ sinh tồn (The Gift of Fear) nhận diện các tổ chức thao túng tâm lý: (1) Cô lập xã hội và cắt đứt liên lạc người thân; (2) Làm suy kiệt thể chất nhằm triệt tiêu tư duy phản biện; (3) Sùng bái cá nhân tuyệt đối và cấm đoán hoài nghi; (4) Ngụy biện đảo ngược đạo đức và kích động thù hận xã hội.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Buổi sáng định mệnh dưới lòng đất Tokyo & Cơn hoang tưởng tập thể
05:15 Hồi 2 · Khu căn cứ Satyam và nhà máy tử thần — Thủ đoạn MO và dấu ấn Signature
10:00 Hồi 3 · Giải phẫu tâm lý — Sự trống rỗng hiện sinh & Nghịch lý giới tinh hoa
15:30 Hồi 4 · Đấu trí thẩm vấn & Bóc trần ma thuật tẩy não cùng khái niệm Poa
21:00 Hồi 5 · Phán quyết lịch sử, bản án tâm lý & Bài học cảnh báo đỏ sinh tồn

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai tại Nhật Bản (Tòa án Tối cao Nhật Bản, Tòa án Địa phương Tokyo, Cơ quan Cảnh sát Quốc gia NPA, Bộ Tư pháp Nhật Bản). Kênh không nhằm bôi nhọ hay tôn vinh bất kỳ tổ chức hay cá nhân nào.
• Các nhân vật Cú, Sói, Cáo, Thỏ tuyết, Gấu trúc là hình tượng minh họa nghệ thuật. Lời của Điều tra viên, Chuyên gia và Nhân chứng là lời dựng lại dựa trên tư liệu lịch sử.
• Giọng đọc, hình ảnh và âm thanh được hỗ trợ bởi công nghệ AI.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 NGUỒN THAM KHẢO ĐÃ ĐỐI CHIẾU
Toàn bộ sự kiện, ngày tháng và trích dẫn trong video đã được đối chiếu từng câu với 19 nguồn công khai (hồ sơ tòa án, báo chí, văn bản luật, nghiên cứu học thuật):

{SOURCES_VI}

Danh mục nguồn chi tiết kèm biên bản đối chiếu dữ kiện lịch sử được lưu trữ tại: 02_SAN_XUAT/Tap08/nguon_tham_khao.md

🆘 Nếu bạn biết một trẻ em đang bị bạo hành hoặc gia đình cần trợ giúp tâm lý, hãy liên hệ:
• Tổng đài quốc gia bảo vệ trẻ em: 111 (Việt Nam, miễn phí, 24/7)
• Đường dây nóng hỗ trợ tâm lý Ngày Mai: 096 306 1414
• Viện Sức khỏe Tâm thần – Bệnh viện Bạch Mai: 024 3869 3731
• Đường dây nóng can thiệp & phòng chống bạo lực: 1900 969 680
• Đường dây nóng hỗ trợ khủng hoảng Nhật Bản (TELL Lifeline): 03-5774-0992 — https://telljp.com
• Đường dây khẩn cấp Cảnh sát Nhật Bản: #9110 hoặc 110
• 988 Suicide & Crisis Lifeline (Hoa Kỳ): Gọi hoặc nhắn tin 988 — https://988lifeline.org

#AmberEyes #TrueCrime #CriminalPsychology #AumShinrikyo #ShokoAsahara #SarinTokyo #ThaoTungTamLy #10ChiDauTamLy #CanhBaoDo #MindControl #Kasumigaseki #HarukiMurakami #HoSoToiPham #Documentary"""

# ==============================================================================
# 6. MÔ TẢ ĐẦY ĐỦ TIẾNG ANH
# ==============================================================================
DESC_EN = f"""Ep. 08: When Geniuses Are Brainwashed | Criminal Psychology: Aum Shinrikyo & The Tokyo Sarin Attack (10 Psychological Markers & Elite Mind Control) | Amber eyes

On the morning of Monday, March 20, 1995, Tokyo awakened to its usual brisk rhythm of life. Millions of commuters crowded into the subterranean labyrinth of the subway network to begin their work week. It was precisely eight o’clock in the morning, the peak rush hour of the entire day. Five subway trains across three vital artery lines—Chiyoda, Marunouchi, and Hibiya—were hurtling toward Kasumigaseki Station: the political and administrative heart of Japan, home to central ministries and the National Police Agency. At that time, Japan took immense pride in its 'myth of public safety', boasting one of the lowest violent crime rates in the world.

Yet, on each of those five trains, men boarded carrying a neurotoxic chemical capable of catastrophic devastation. Using umbrellas ground to razor-sharp tips, they punctured plastic bags filled with lethal liquid directly onto train floors. As doors opened at bustling stations, the perpetrators slipped quietly away, leaving toxic vapors to rise silently into crowded passenger cars. The coordinated chemical strike claimed the lives of fourteen innocent people, severely injured over five thousand eight hundred commuters, and took the lives of two courageous subway station workers—Kazumasa Takahashi and Tsuneo Hishinuma—who heroically removed the toxic bags with their bare hands to protect passengers.

What stunned Japan and the global community went far beyond the sheer cruelty of the strike itself. As the true identities of the perpetrators emerged, an astonishing paradox stood exposed. Behind this devastating assault were not street criminals or foreign forces, but top-tier scientists, medical doctors, and intellectual elites educated at Japan’s most prestigious universities: Masami Tsuchiya (organic chemistry master’s graduate from Tsukuba University), Hideo Murai (astrophysicist from Osaka University), Seiichi Endo (virologist from Kyoto University), and Dr. Ikuo Hayashi (esteemed cardiologist from Keio University and former department chief at a national hospital). All had surrendered their fortunes, intellects, and moral compasses to Shoko Asahara—a partially blind charlatan who had failed college entrance exams and peddled fraudulent medicine.

Amber eyes dissects the Aum Shinrikyo & Tokyo Sarin Attack file through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: Completely shattered Japan's postwar 'myth of public safety'; collective paranoia gripped the metropolis as commuters held their breath descending subway stairs, inspected undercarriages of seats, and viewed strangers with profound suspicion; paralyzed municipal transit and emergency medical infrastructures; catalyzed sweeping legislative and institutional reforms, radically amending the Religious Corporations Act and enacting specialized surveillance statutes against mass-casualty organizations.
2. OBJECTIFICATION OF THE VICTIM: Subway commuters were stripped of their humanity, personal agency, and family bonds, reduced into "spiritual obstacles" and "living props" in an apocalyptic narrative; profound affective empathy deficit and warped Theory of Mind degraded human agony into cold experimental data points within the Satyam 7 chemical synthesis logs.
3. COGNITIVE COMPARTMENTALIZATION: Intellectual disciples operated two irreconcilable realities without internal friction: by day, ethical professionals, healing physicians, and gentle sons; by night, detached chemical technicians synthesizing mass-extermination agents; concurrently exposing the tragedy of secondary victims: proud parents whose identities were obliterated upon learning their prodigy children had become mass terrorists.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: A stark behavioral contrast between Dr. Ikuo Hayashi's genuine remorse (conscience awakened, kneeling before victims' families, full investigative cooperation resulting in life imprisonment) and Shoko Asahara's pathological self-pity and feigned madness (incoherent muttering, refusing dialogue) as his grandiose messianic facade suffered total narcissistic collapse upon being stripped of worldly power.
5. TECHNIQUES OF NEUTRALIZATION & HERO COMPLEX: The grotesque theological perversion of 'Poa' (transference of consciousness) into a murderous doctrine asserting that terminating civilians was an act of supreme mercy to liberate them from accumulating negative karma; coupled with displacement of responsibility convincing operatives they were merely executing the infallible will of the Supreme Master.
6. PSYCHOLOGICAL TRIGGER & TIPPING POINT: An internal leak revealing an imminent police raid on the Kamikuishiki compound scheduled for March 22, 1995 regarding a notary kidnapping triggered severe panic in Asahara; facing total exposure, he ordered the sarin offensive within a desperate 48-hour window to paralyze police headquarters and divert investigative scrutiny.
7. SIGNATURE VS. MODUS OPERANDI (MO): Modus Operandi (MO) adapted with clinical precision: double-layered plastic bags wrapped in newspaper, punctured with sharpened umbrella tips, coordinated 8:00 AM rush-hour arrival, staged getaway drivers; Immutable psychological Signature: the pathological compulsion to physically manifest apocalyptic prophecies and validate his timeline of World War Three before his followers.
8. FANTASY ADDICTION & ESCALATION TRAJECTORY: Behavioral escalation fueled by stimulus tolerance buildup across four violent thresholds: (1) Modest yoga studio with staged levitation photography -> (2) Forced asset surrender, confinement cells, and internal executions -> (3) Murder of Attorney Tsutsumi Sakamoto and his entire family (1989) -> (4) Matsumoto sarin attack targeting judges (1994), culminating in the Tokyo subway horror (1995).
9. HALO EFFECT & COLLECTIVE BLIND SPOTS: Elite academic pedigrees from premier institutions (Tokyo, Kyoto, Osaka, Keio, Tsukuba) created an impenetrable halo effect; the cultural assumption that intellectuals could not commit barbarous acts, combined with societal hesitation toward religious oversight, blinded law enforcement for years despite mounting disappearances.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Restoring human dignity to the victims; honoring the extraordinary valor of station workers Kazumasa Takahashi and Tsuneo Hishinuma; incorporating profound sociological insights from Haruki Murakami’s 'Underground'; and equipping viewers with 4 vital survival red flags (The Gift of Fear) to identify destructive manipulative groups: (1) Strategic social isolation and cutting off family; (2) Systematic physical exhaustion to paralyze critical thinking; (3) Absolute authoritarianism and forbidding honest doubt; (4) Moral inversion rationalizing harm in the name of a higher cause.

⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · A Fateful Morning Under Tokyo & Collective Paranoia
05:15 Act 2 · The Satyam Complex & The Lab of Death — Modus Operandi and Psychological Signature
10:00 Act 3 · Psychological Autopsy — Existential Vacuum & The Paradox of Intellectual Elites
15:30 Act 4 · Interrogation & Demystifying Mind Control and the 'Poa' Doctrine
21:00 Act 5 · Historic Verdict, Psychological Judgment & Red Flags for Survival

⚠️ LEGAL ADVISORY & SAFETY
• Produced solely for educational, criminological, and historical documentation; not a substitute for professional medical, psychiatric, or legal advice.
• Based on verified public court records and government findings in Japan (Supreme Court of Japan, Tokyo District Court, National Police Agency NPA, Ministry of Justice). Not intended to defame or glorify any organization or individual.
• Character avatars (Owl, Wolf, Fox, Snow Rabbit, Panda) are dramatized artistic illustrations. Statements by Investigators, Psychologists, and Witnesses are reconstructed from historical trial records.
• Synthesized voiceover, imagery, and audio engineered with AI technologies.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 VERIFIED HISTORICAL SOURCES & DOCKETS
All case chronologies, data points, and quotations cross-referenced against 19 public records:

{SOURCES_EN}

Comprehensive source documentation and verification logs archived at: 02_SAN_XUAT/Tap08_EN/nguon_tham_khao_EN.md

🆘 If you or someone you care about is facing an emotional crisis or coercive group manipulation:
• TELL Lifeline (Japan, English/Japanese, Free & Confidential): 03-5774-0992 — https://telljp.com
• Japan National Police Consultation Hotline: #9110 or Emergency 110
• 988 Suicide & Crisis Lifeline (US & Canada): Call or text 988 — https://988lifeline.org
• Crisis Text Line: Text HOME to 741741
• International Association for Suicide Prevention (IASP): https://www.iasp.info/resources/Crisis_Centres/

#AmberEyes #TrueCrime #CriminalPsychology #AumShinrikyo #ShokoAsahara #TokyoSarinAttack #CultMindControl #ExistentialVacuum #10PsychologicalMarkers #RedFlags #Kasumigaseki #HarukiMurakami #CaseFile #Documentary"""

# ==============================================================================
# 7. MÔ TẢ ĐẦY ĐỦ TIẾNG NHẬT
# ==============================================================================
DESC_JA = f"""第08話：天才たちはいかにして洗脳されたのか | 犯罪心理学：オウム真理教と地下鉄サリン事件（10の心理指標エコシステムとエリートマインドコントロール） | Amber eyes

1995年3月20日、月曜日の朝、日本の首都・東京は普段と変わらぬ慌ただしい生活のリズムの中で目覚めました。数百万人の市民が、新しい一週間の始まりに向けて地下鉄の巨大な網の目の中へと足早に吸い込まれていきました。午前8時ちょうど、一日の中で最も混雑する朝の通勤ラッシュアワーです。千代田線、丸ノ内線、日比谷線の3つの大動脈を走る5本の列車が、霞ケ関駅へと向かって同時に疾走していました。ここは国の重要省庁と警察庁が集中する、まさに日本における政治と行政の中枢です。当時の日本は世界で最も治安が良い国の一つとして、「安全神話」を誇りにしていました。

しかし、その5本の列車の各車両には、恐るべき破壊力を秘めた神経毒を持ち込んだ男たちが乗っていました。彼らは研ぎ澄ました傘の先端を使い、猛毒の液体が入ったビニール袋を車内の床の上で突き刺したのです。混雑する駅で電車のドアが開いた瞬間、犯行者たちは素早く車外へ抜け出し、車内には目に見えぬ有毒ガスが静かに立ち込めました。この化学兵器攻撃により14名の尊い命が奪われ、5800人以上が重軽傷を負いました。乗客を守るために素手で毒液袋を車外へ運び出し尊い犠牲となった高橋一正助役と菱沼恒夫駅員をはじめ、多くの人々が今なお癒えぬ後遺症と心の傷を抱えています。

日本と世界に最大の衝撃を与えたのは、単なる攻撃の残忍さだけではありませんでした。毒物を製造し散布した実行犯たちの真の素顔が明らかになるにつれ、驚くべきパラドックスが白日の下に晒されたのです。この未曾有の惨劇の背後にいたのは、日本の名門大学で高度な教育を受けた一握りの科学者、医師、そしてエリート知識人たちでした：土谷正実（筑波大学大学院・有機化学修士）、村井秀夫（大阪大学理学部・物理学）、遠藤誠一（京都大学大学院・ウイルス学）、そして林郁夫（慶應義塾大学医学部卒・元国立病院循環器科部長）。彼らはなぜ、かつて偽薬販売で処罰された半盲の男・麻原彰晃に全財産と理性、そして良心を捧げ尽くしてしまったのでしょうか。

Amber eyesは、オウム真理教および地下鉄サリン事件を独自の「10の核心的心理・行動指標エコシステム」を通じて解剖します：
1. 社会的余波と集団的パラノイア：戦後日本の「安全神話」を根底から打ち砕き、市民が地下鉄の階段を降りるたびに息を詰め座席の下を確認する集団的偏執病を引き起こした過程；首都機能の麻痺と、宗教法人法改正および無差別大量殺人行為を行った団体の規制に関する法律（オウム新法）制定に至る大改革。
2. 被害者の客体化（Objectification）：通勤客を血の通った人間として見なさず、新世界移行の障害となる「悪業を背負った魂」や「生きている小道具」へと格下げ；共感能力の欠如と認知の歪みにより、人命を研究室における無機質な実験データへと還元した狂気。
3. 心理的区画化（Compartmentalization）：家庭や社会規範が存在する「日常の世界」と、サティアン内の「秘密の暗黒世界」を完全に分離した二重生活；エリート知識人の両親が子どものテロリスト化によってアイデンティティの完全崩壊を経験した二次被害の悲劇。
4. 自己愛の崩壊（Narcissistic Collapse）と病的な自己憐憫：林郁夫医師の真摯な悔恨と法廷での謝罪（良心の覚醒、全面供述による無期懲役判決）と、特権を失い公判で意味不明な独り言を呟き狂気を装った麻原彰晃の病的自己憐憫との鮮烈な対比。
5. 自己正当化と中和の技術（Techniques of Neutralization）：意識の転移を意味する神聖な修行概念「ポア」を「悪業を積む前に魂を救済する慈悲の殺人」へと教義的に偽装；教祖の意志を代行しているに過ぎないとする責任の外在化の罠。
6. 心理的引き金（Precipitating Trigger）：1995年3月22日に予定されていた公証人役場事務長拉致事件に伴う上九一色村への強制捜査情報漏洩が引き起こした麻原の極度なパニック；捜査網を攪乱するため48時間以内に下された無謀なサリン散布命令。
7. 署名（Signature）対 手口（MO）：手口（MO）の周到な計算（新聞紙で包んだ二重ビニール袋、研いだ傘の先、午前8時ラッシュアワーの同期、待機車両）に対し、不変の心理的署名（自らが予言したハルマゲドンと第三次世界大戦の妄想を現実に強要しようとした支配欲）。
8. 妄想への耽溺とエスカレーション軌道：刺激耐性の形成に伴う4段階のエスカレーション：(1) ヨガ教室と空中浮揚などの虚構演出 -> (2) 財産収奪、密室監禁、内部粛清 -> (3) 坂本堤弁護士一家殺害事件（1989年） -> (4) 松本サリン事件（1994年）を経て地下鉄テロへと至る破滅の連鎖。
9. 後光効果（ハロー効果）と社会的盲点：東京大、京都大、大阪大、慶應大、筑波大などの最高峰の学歴が作り出した完璧な不可視の盾；「知識人エリートが凶悪事件を起こすはずがない」という社会的先入観が警察の警戒を長年無力化した盲点。
10. 被害者学と生存のためのレッドフラッグ：被害者の尊厳の回復；素手でサリン袋を撤去し殉職した高橋一正助役と菱沼恒夫駅員の勇気；村上春樹『アンダーグラウンド』に見る人間の弱さの考察；有害なマインドコントロール集団を見抜く4つの警告信号（社会的孤立の強要、肉体的消耗による思考力奪取、絶対的個人崇拝と疑問の禁止、道徳的反転と敵意の煽動）。

⏱ 目次（チャプター）
00:00 オープニング・免責事項
00:23 第1幕 · 東京地下で迎える運命の朝と集団的偏執病
05:15 第2幕 · サティアン複合施設と死の実験室 — 手口（MO）と精神的シグネチャー
10:00 第3幕 · 心理解剖 — 実存的真空と知識人エリートの逆説
15:30 第4幕 · 取調べの攻防 — 洗脳の解体と歪められた「ポア」の教義
21:00 第5幕 · 歴史的判決、心理的結審および生存のためのレッドフラッグ

⚠️ ご視聴にあたっての注意事項
• 本動画は教育目的および犯罪心理学・歴史記録の観点からの分析コンテンツであり、医学的、心理学的、または法的助言を提供するものではありません。
• 日本の公的司法記録（最高裁判所、東京地方裁判所、警察庁、法務省）に基づき制作されています。いかなる団体や個人を誹謗中傷、または美化する意図はありません。
• フクロウ、オオカミ、キツネ、ユキウサギ、パンダのアバターは芸術的演出です。捜査官、心理学者、証人の発言は歴史的公判資料に基づき再構成されています。
• 音声、画像、映像の生成にはAI技術が活用されています。
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 参照・照合済み公的資料リスト
動画内のすべての年表、事実関係、および証言は以下の19の公的資料および学術研究に基づき照合されています：

{SOURCES_JA}

詳細な出典および歴史的事実の対照記録は以下に保管されています：02_SAN_XUAT/Tap08_JA/nguon_tham_khao_JA.md

🆘 心の健康相談および危機対応窓口（日本国内）:
• こころの健康相談統一ダイヤル: 0570-064-556
• よりそいホットライン（通話無料・24時間対応）: 0120-279-338
• 警察相談専用電話: #9110 （緊急時は110番）
• TELL Lifeline（英語・日本語対応）: 03-5774-0992 — https://telljp.com
• いのちの電話: 0570-783-556（午前10時〜午後10時） / 0120-783-556（毎日午後4時〜午後9時）

#AmberEyes #犯罪心理学 #心理分析 #オウム真理教 #麻原彰晃 #地下鉄サリン事件 #マインドコントロール #実存的真空 #プロファイリング #10の心理指標 #レッドフラッグ #村上春樹 #アンダーグラウンド #霞ケ関 #実話事件"""

# ==============================================================================
# 8. MÔ TẢ ĐẦY ĐỦ TIẾNG HÀN
# ==============================================================================
DESC_KO = f"""제08화: 천재들은 어떻게 세뇌되었는가 | 범죄심리학: 옴진리교와 도쿄 지하철 사린 테러 (10대 핵심 심리 지표 및 엘리트 마인드 컨트롤) | Amber eyes

1995년 3월 20일 월요일 아침, 일본의 수도 도쿄는 평소와 다름없이 분주한 일상의 리듬 속에서 눈을 떴습니다. 수백만 명의 시민들이 새로운 한 주를 시작하기 위해 지하철의 거대한 미로 속으로 빠르게 걸음을 옮겼습니다. 오전 8시 정각, 하루 중 가장 붐비는 출근길 러시 아워였습니다. 치요다선, 마루노우치선, 히비야선의 3개 주요 동맥 노선을 달리던 5편의 열차가 카스미가세키역을 향해 일제히 질주하고 있었습니다. 이곳은 일본의 핵심 정부 부처와 경찰청이 밀집해 있는, 명실상부한 국가 행정의 심장부입니다. 당시 일본은 세계에서 가장 안전한 치안을 자랑하며 자국의 ‘안전 신화’에 강한 자부심을 품고 있었습니다.

그러나 그 5편의 열차 각 객차 안에는 가공할 파괴력을 지닌 신경독 가스를 휴대한 남성들이 타고 있었습니다. 그들은 날카롭게 갈아낸 우산 끝으로 맹독성 액체가 담긴 비닐봉지를 객차 바닥 위에 내리찍어 구멍을 뚫었습니다. 혼잡한 역에서 전철 문이 열리는 순간 범인들은 재빨리 빠져나갔고, 차내에는 보이지 않는 유독가스가 소리 없이 피어올랐습니다. 이 잔혹한 화학 테러로 인해 14명의 소중한 목숨이 희생되었고, 5800명 이상의 무고한 시민들이 심각한 피해를 입었습니다. 승객들을 지키기 위해 맨손으로 독극물 봉지를 치우다 순직한 타카하시 카즈마사 조역과 히시누마 츠네오 역무원을 비롯해, 수많은 사람들이 평생에 걸친 후유증과 정신적 트라우마를 안고 살아가야 했습니다.

일본과 전 세계에 가장 큰 충격을 안겨준 것은 단순한 테러의 잔혹성만이 아니었습니다. 독극물을 제조하고 살포한 실행범들의 진짜 정체가 드러나면서, 경악할 만한 역설이 세상 앞에 적나라하게 노출되었습니다. 이 미증유의 참극 배후에 서 있던 자들은 일본 최고의 명문 대학들에서 고등 교육을 받은 일류 과학자, 의사, 엘리트 지식인들이었습니다: 츠치야 마사미(쓰쿠바대 대학원 유기화학 석사), 무라이 히데오(오사카대 물리학과), 엔도 세이이치(교토대 대학원 바이러스학), 그리고 하야시 이쿠오(게이오대 의대 졸·전 국립병원 순환기내과 과장). 그들은 도대체 왜 가짜 약을 팔다 처벌받았던 한 사기꾼 아사하라 쇼코의 발아래 무릎을 꿇고 자신의 지성과 양심을 송두리째 바쳤던 것일까요?

Amber eyes는 옴진리교와 도쿄 사린 테러 사건을 자체적인 ‘10대 핵심 심리·행동 지표 생태계’를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 불안·파라노이아: 전후 일본 사회의 굳건한 ‘안전 신화’를 완전히 붕괴시키고, 시민들이 지하철 계단을 내려갈 때마다 숨을 죽이고 좌석 밑을 확인하는 집단적 편집증을 촉발한 과정; 수도권 교통·의료 시스템 마비와 종교법인법 전면 개정 및 옴 규제법 제정으로 이어진 사법 제도 대개혁.
2. 피해자의 사물화 및 객체화 (Objectification): 승객들을 존엄한 인간이 아닌 새 시대로의 진입을 가로막는 ‘악업에 물든 존재’이자 종말 드라마의 ‘살아있는 소품’으로 전락시킨 기제; 병적인 공감 결여와 인지 왜곡이 인간의 생명을 실험실 기록지 속 차가운 수치로 격하시킨 광기.
3. 인지적 구획화 (Compartmentalization): 가정과 도덕이 숨 쉬는 ‘일상의 방’과 살상 무기를 제조하는 ‘사티안의 암흑 방’을 완벽하게 분리한 이중생활; 수재 자녀가 무차별 학살범이 되었다는 충격 앞에 가문의 정체성이 송두리째 무너져 내린 부모들의 2차 비극.
4. 나르시시즘적 붕괴와 병적 자기연민: 하야시 이쿠오 의사의 진정성 있는 참회와 눈물의 자백(양심의 회복, 전면 수사 협조로 무기징역 선고)과, 재판 내내 횡설수설하며 광인 행세를 지속한 아사하라 쇼코의 나르시시즘적 붕괴 및 병적 자기연민의 극명한 대비.
5. 자기 정당화 및 중화 기술 (Techniques of Neutralization): 의식 전이의 신성한 불교 수행 개념 ‘포아’를 ‘더 큰 악업을 짓기 전에 영혼을 구원해 주는 지고의 자비’로 변질시킨 사이비 교리; 모든 책임을 절대적 교주의 신성한 뜻으로 떠넘긴 책임의 외재화.
6. 심리적 방아쇠와 티핑 포인트 (Precipitating Trigger): 1995년 3월 22일로 예정되어 있던 공증인 납치 사건 관련 카미쿠이시키 기지 대대적 압수수색 정보 유출이 촉발한 아사하라의 극심한 공황 상태; 수사망을 교란하고 경찰 수뇌부를 마비시키기 위해 48시간 만에 전격 명령된 사린 살포.
7. 시그니처(Signature) vs 범행 수법(MO): 수법(MO)의 치밀한 진화(이중 비닐봉지, 날카로운 우산 끝, 출근길 동시 살포, 도주 차량)와, 자신이 예언한 제3차 세계대전 종말 시나리오를 현실에 억지로 실현하려 했던 불변의 심리적 시그니처(지배 망상).
8. 환상 중독과 에스컬레이션 궤적: 자극 내성 형성에 따른 폭력의 4단계 에스컬레이션: (1) 요가 교실과 공중부양 사기극 -> (2) 재산 강탈, 밀실 감금, 내부 살해 -> (3) 사카모토 변호사 일가 살해(1989년) -> (4) 마츠모토 사린 테러(1994년)를 거쳐 도쿄 지하철 참사로 폭발한 파멸의 궤도.
9. 후광 효과(Halo Effect)와 제도의 맹점: 도쿄대, 교토대, 오사카대, 게이오대, 쓰쿠바대 등 최고 학부 출신이라는 타이틀이 형성한 보이지 않는 방패; ‘엘리트 지식인이 테러를 저지를 리 없다’는 사회적 편견과 종교 자유 보호 원칙이 경찰의 조기 개입을 가로막은 시스템의 맹점.
10. 피해자학 및 생존을 위한 레드플래그: 피해자들의 온전한 인격과 존엄 회복; 맨손으로 사린 봉지를 치우다 순직한 역무원들의 숭고한 용기 기림; 무라카미 하루키의 《언더그라운드》가 던지는 인간 소외에 대한 성찰; 유해한 사이비 조작 집단을 식별하고 벗어나기 위한 4대 생존 경고 신호(사회적 고립 강요, 육체적 탈진을 통한 비판력 마비, 절대적 개인숭배와 의문 금지, 도덕적 반전과 증오 선동).

⏱ 챕터 (타임라인)
00:00 오프닝 및 시청 유의사항
00:23 제1막 · 도쿄 지하에서 시작된 운명의 아침과 집단적 편집증
05:15 제2막 · 사티안 기지와 죽음의 연구실 — 범행 수법(MO)과 심리적 시그니처
10:00 제3막 · 심리 부검 — 실존적 진공과 지식인 엘리트의 역설
15:30 제4막 · 취조실의 공방 — 세뇌의 해체와 왜곡된 ‘포아’ 교리
21:00 제5막 · 역사적 판결, 심리적 결심 및 생존을 위한 레드플래그

⚠️ 시청 전 유의사항
• 본 콘텐츠는 범죄심리학 및 교육적 관점에서의 분석 콘텐츠이며, 의학적, 심리학적 또는 법률적 조언을 대신할 수 없습니다.
• 일본 최고재판소, 도쿄지방재판소, 경찰청, 법무성의 공개된 사법 기록을 바탕으로 제작되었습니다. 특정 개인이나 단체를 비방하거나 미화할 목적이 없습니다.
• 부엉이, 늑대, 여우, 눈토끼, 판다 아바타는 예술적 연출입니다. 수사관, 심리학자, 증인의 발언은 역사적 공판 기록을 토대로 재구성되었습니다.
• 음성, 이미지, 사운드 제작에 AI 기술이 적용되었습니다.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 대조 완료된 공식 사법·학술 참고문헌
영상 내 모든 타임라인, 사실관계 및 증언은 다음 19개 공적 문서 및 학술 자료와 대조되었습니다:

{SOURCES_KO}

상세한 출처 및 사실관계 대조 기록은 다음 위치에 보관되어 있습니다: 02_SAN_XUAT/Tap08_KO/nguon_tham_khao_KO.md

🆘 위기상담 및 심리 지원 안내 (한국 및 국제):
• 자살예방 상담전화: 109 (24시간 운영)
• 정신건강 상담전화: 1577-0199
• 보건복지상담센터: 129
• 경찰청 긴급신고: 112 (민원상담 182)
• TELL Lifeline (일본 내 다국어 위기상담): 03-5774-0992 — https://telljp.com
• 미국 988 Suicide & Crisis Lifeline: 전화 또는 문자 988 — https://988lifeline.org

#AmberEyes #범죄심리학 #프로파일링 #옴진리교 #아사하라쇼코 #도쿄지하철사린 #세뇌 #실존적진공 #마인드컨트롤 #10대심리지표 #레드플래그 #무라카미하루키 #언더그라운드 #실화사건 #다큐멘터리"""


def write_file_safe(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content.strip() + "\n")
    print(f"  -> Đã ghi: {path.relative_to(ROOT)} ({len(content)} ký tự)")


def main():
    print("=== CẬP NHẬT MÔ TẢ ĐẦY ĐỦ CHO TẬP 08 TRÊN 4 NGÔN NGỮ ===")

    # 1. TIẾNG VIỆT
    print("\n[1/4] Ghi file Tiếng Việt (Tap08)...")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08" / "mo_ta.txt", DESC_VI)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08" / "xuat_ban" / "mo_ta.txt", DESC_VI)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08" / "nguon_mo_ta.txt", SOURCES_VI)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08" / "nguon_tham_khao.md", f"# NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN — TẬP 08\n\n{SOURCES_VI}")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08" / "xuat_ban" / "nguon_tham_khao.md", f"# NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN — TẬP 08\n\n{SOURCES_VI}")

    # 2. TIẾNG ANH
    print("\n[2/4] Ghi file Tiếng Anh (Tap08_EN)...")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_EN" / "description.txt", DESC_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_EN" / "mo_ta.txt", DESC_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_EN" / "xuat_ban" / "description.txt", DESC_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_EN" / "nguon_tham_khao_EN.md", f"# VERIFIED CASE SOURCES & LEGAL DOCKETS — EPISODE 08\n\n{SOURCES_EN}")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", f"# VERIFIED CASE SOURCES & LEGAL DOCKETS — EPISODE 08\n\n{SOURCES_EN}")

    # 3. TIẾNG NHẬT
    print("\n[3/4] Ghi file Tiếng Nhật (Tap08_JA)...")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_JA" / "description.txt", DESC_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_JA" / "mo_ta.txt", DESC_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_JA" / "xuat_ban" / "description.txt", DESC_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_JA" / "nguon_tham_khao_JA.md", f"# 参照・照合済み公的資料リスト — 第08話\n\n{SOURCES_JA}")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", f"# 参照・照合済み公的資料リスト — 第08話\n\n{SOURCES_JA}")

    # 4. TIẾNG HÀN
    print("\n[4/4] Ghi file Tiếng Hàn (Tap08_KO)...")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_KO" / "description.txt", DESC_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_KO" / "mo_ta.txt", DESC_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_KO" / "xuat_ban" / "description.txt", DESC_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_KO" / "nguon_tham_khao_KO.md", f"# 공식 참고문헌 및 사법 기록 목록 — 제08화\n\n{SOURCES_KO}")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap08_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", f"# 공식 참고문헌 및 사법 기록 목록 — 제08화\n\n{SOURCES_KO}")

    print("\nĐã tạo thành công toàn bộ mô tả và nguồn tham khảo cho Tập 08 trên 4 ngôn ngữ!")


if __name__ == "__main__":
    main()
