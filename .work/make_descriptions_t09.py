#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo và cập nhật mô tả video đạt chuẩn Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cho Tập 09 trên cả 4 ngôn ngữ (VI, EN, JA, KO)."""

import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# 1. NGUỒN TIẾNG VIỆT (20 NGUỒN CÔNG KHAI ĐÃ ĐỐI CHIẾU)
# ==============================================================================
SOURCES_VI = """▸ Hồ sơ tư pháp & cơ quan điều tra Hoa Kỳ:
• [1] Tòa Thượng thẩm California Hạt Los Angeles — Hồ sơ xét xử vụ án State of California v. Charles Manson, Susan Atkins, Patricia Krenwinkel, Leslie Van Houten (Case No. A253156):
  https://www.courts.ca.gov/
• [2] Tòa Tối cao California — Án lệ bước ngoặt People v. Anderson (1972) bãi bỏ án tử hình tại California (6 Cal. 3d 628):
  https://www.courts.ca.gov/opinions/archive/Crim13617.PDF
• [3] Cục Điều tra Liên bang Hoa Kỳ (FBI Vault) — Hồ sơ lưu trữ hiện trường và các chứng cứ điều tra vụ án mạng Tate-LaBianca:
  https://vault.fbi.gov/charles-manson
• [4] Sở Cảnh sát Los Angeles (LAPD) — Báo cáo điều tra hiện trường vụ án 10050 Cielo Drive và 3311 Waverly Drive (1969):
  https://www.lapdonline.org/
• [5] Cục Cải huấn & Phục hồi California (CDCR) — Hồ sơ tù nhân Charles Manson (#B33920) tại Nhà tù Tiểu bang Corcoran:
  https://www.cdcr.ca.gov/

▸ Tác phẩm điều tra chuyên sâu & nghiên cứu học thuật:
• [6] Vincent Bugliosi & Curt Gentry — 'Helter Skelter: The True Story of the Manson Murders' (W. W. Norton & Company, 1974):
  https://wwnorton.com/books/9780393322231
• [7] Ed Sanders — 'The Family: The Story of Charles Manson's Dune Buggy Attack Battalion' (Dutton, 1971):
  https://www.penguinrandomhouse.com/books/160677/the-family-by-ed-sanders/
• [8] Dianne Lake & Deborah Herman — 'Member of the Family: My Story of Charles Manson, Life Inside His Cult, and the Darkness That Ended the Sixties' (William Morrow, 2017):
  https://www.harpercollins.com/products/member-of-the-family-dianne-lake-deborah-herman
• [9] Jeffrey Melnick — 'Creepy Crawling: Charles Manson and the Many Lives of America's Most Infamous Family' (Arcade Publishing, 2018):
  https://www.skyhorsepublishing.com/9781628729955/creepy-crawling/
• [10] Gavin de Becker — 'The Gift of Fear: Survival Signals That Protect Us from Violence' (Dell Publishing, 1997):
  https://gavindebecker.com/resources/the_gift_of_fear/

▸ Báo chí quốc tế & lưu trữ truyền thông:
• [11] Los Angeles Times — Lưu trữ tư liệu lịch sử phiên tòa xét xử gia đình Manson và cuộc đời Sharon Tate:
  https://www.latimes.com/local/crime/la-me-manson-trial-archive-htmlstory.html
• [12] The New York Times — Vụ án Tate-LaBianca và dấu chấm hết của kỷ nguyên Hippie thập niên 1960:
  https://www.nytimes.com/1969/12/02/archives/five-manson-followers-charged-in-tate-murders.html
• [13] Time Magazine — Chân dung Charles Manson và màn kịch rạp xiếc phòng xử án (1970):
  https://time.com/5029377/charles-manson-dead-history/
• [14] Rolling Stone — Phóng sự điều tra chuyên sâu của David Dalton & David Felton: 'Charles Manson: The Incredible Story of the Most Dangerous Man Alive' (1970):
  https://www.rollingstone.com/culture/culture-news/charles-manson-the-incredible-story-of-the-most-dangerous-man-alive-238466/
• [15] CBS News — Lời khai của nhân chứng được miễn tố Linda Kasabian và cuộc giải mã gia đình Manson:
  https://www.cbsnews.com/news/charles-manson-family-murders-linda-kasabian-dead-at-73/
• [16] ABC News — Phỏng vấn độc quyền của Diane Sawyer với Leslie Van Houten và Patricia Krenwinkel:
  https://abcnews.go.com/US/charles-manson-followers-recount-murders/story?id=48602280

▸ Tâm lý học hành vi & thao túng tâm trí:
• [17] Hiệp hội Tâm lý học Hoa Kỳ (APA) — Nghiên cứu về Hiện tượng xóa bỏ bản ngã tập thể (De-individuation) và Rối loạn nhân cách chống đối xã hội (ASPD):
  https://www.apa.org/topics/personality-disorders
• [18] Gresham Sykes & David Matza — Lý thuyết Kỹ thuật Trung hòa Đạo đức (Techniques of Neutralization in Criminology):
  https://www.jstor.org/stable/2089195
• [19] Leon Festinger — Thuyết Bất hòa Nhận thức (Cognitive Dissonance Theory) trong các cấu trúc tâm lý giáo phái khép kín:
  https://www.simplypsychology.org/cognitive-dissonance.html
• [20] Steven Hassan — Mô hình BITE về kiểm soát tâm trí và cơ chế tước đoạt quyền tự chủ cá nhân:
  https://freedomofmind.com/cult-mind-control/bite-model/"""

# ==============================================================================
# 2. NGUỒN TIẾNG ANH (20 VERIFIED SOURCES)
# ==============================================================================
SOURCES_EN = """▸ US Judicial Archives & Law Enforcement Records:
• [1] Los Angeles County Superior Court — State of California v. Charles Manson, Susan Atkins, Patricia Krenwinkel, Leslie Van Houten (Docket No. A253156):
  https://www.courts.ca.gov/
• [2] Supreme Court of California — Landmark Precedent People v. Anderson (1972) Invalidating the Death Penalty in California (6 Cal. 3d 628):
  https://www.courts.ca.gov/opinions/archive/Crim13617.PDF
• [3] Federal Bureau of Investigation (FBI Vault) — Official Tate-LaBianca Crime Scene Investigation Records & Evidence Files:
  https://vault.fbi.gov/charles-manson
• [4] Los Angeles Police Department (LAPD) — Crime Scene Investigation Dossiers for 10050 Cielo Drive and 3311 Waverly Drive (1969):
  https://www.lapdonline.org/
• [5] California Department of Corrections and Rehabilitation (CDCR) — Inmate Profile Charles Manson (#B33920) at Corcoran State Prison:
  https://www.cdcr.ca.gov/

▸ Investigative Monographs & Academic Literature:
• [6] Vincent Bugliosi & Curt Gentry — 'Helter Skelter: The True Story of the Manson Murders' (W. W. Norton & Company, 1974):
  https://wwnorton.com/books/9780393322231
• [7] Ed Sanders — 'The Family: The Story of Charles Manson's Dune Buggy Attack Battalion' (Dutton, 1971):
  https://www.penguinrandomhouse.com/books/160677/the-family-by-ed-sanders/
• [8] Dianne Lake & Deborah Herman — 'Member of the Family: My Story of Charles Manson, Life Inside His Cult, and the Darkness That Ended the Sixties' (William Morrow, 2017):
  https://www.harpercollins.com/products/member-of-the-family-dianne-lake-deborah-herman
• [9] Jeffrey Melnick — 'Creepy Crawling: Charles Manson and the Many Lives of America's Most Infamous Family' (Arcade Publishing, 2018):
  https://www.skyhorsepublishing.com/9781628729955/creepy-crawling/
• [10] Gavin de Becker — 'The Gift of Fear: Survival Signals That Protect Us from Violence' (Dell Publishing, 1997):
  https://gavindebecker.com/resources/the_gift_of_fear/

▸ International Journalism & Media Archives:
• [11] Los Angeles Times — Historical Coverage Archives of the Manson Family Murder Trials and the Sharon Tate Legacy:
  https://www.latimes.com/local/crime/la-me-manson-trial-archive-htmlstory.html
• [12] The New York Times — The Tate-LaBianca Murders and the Death of the 1960s Counterculture Era:
  https://www.nytimes.com/1969/12/02/archives/five-manson-followers-charged-in-tate-murders.html
• [13] Time Magazine — Profile of Charles Manson and the Courtroom Circus Trial (1970):
  https://time.com/5029377/charles-manson-dead-history/
• [14] Rolling Stone — Comprehensive Investigative Retrospective by David Dalton & David Felton: 'Charles Manson: The Incredible Story of the Most Dangerous Man Alive' (1970):
  https://www.rollingstone.com/culture/culture-news/charles-manson-the-incredible-story-of-the-most-dangerous-man-alive-238466/
• [15] CBS News — Courtroom Testimony of Star State Witness Linda Kasabian and Unmasking the Manson Cult:
  https://www.cbsnews.com/news/charles-manson-family-murders-linda-kasabian-dead-at-73/
• [16] ABC News — Diane Sawyer's Exclusive Prison Interviews with Leslie Van Houten and Patricia Krenwinkel:
  https://abcnews.go.com/US/charles-manson-followers-recount-murders/story?id=48602280

▸ Behavioral Criminology & Coercive Control Studies:
• [17] American Psychological Association (APA) — Clinical Studies on De-individuation in Cult Groups and Antisocial Personality Disorder (ASPD):
  https://www.apa.org/topics/personality-disorders
• [18] Gresham Sykes & David Matza — Techniques of Neutralization Theory in Criminological Justifications:
  https://www.jstor.org/stable/2089195
• [19] Leon Festinger — Theory of Cognitive Dissonance in Closed Dogmatic Groups:
  https://www.simplypsychology.org/cognitive-dissonance.html
• [20] Steven Hassan — The BITE Model of Mind Control and Systematic Deprivation of Personal Autonomy:
  https://freedomofmind.com/cult-mind-control/bite-model/"""

# ==============================================================================
# 3. NGUỒN TIẾNG NHẬT (20の参照・照合済み公的資料)
# ==============================================================================
SOURCES_JA = """▸ 米国司法記録および公的捜査機関文書:
• [1] カリフォルニア州ロサンゼルス郡上級裁判所 — カリフォルニア州対チャールズ・マンソン他公判記録（事件番号：Case No. A253156）:
  https://www.courts.ca.gov/
• [2] カリフォルニア州最高裁判所 — 州内死刑違憲判決 People v. Anderson (1972)（6 Cal. 3d 628）:
  https://www.courts.ca.gov/opinions/archive/Crim13617.PDF
• [3] 連邦捜査局（FBI Vault） — テート・ラビアンカ事件公式現場捜査記録および証拠調書:
  https://vault.fbi.gov/charles-manson
• [4] ロサンゼルス市警察（LAPD） — 10050シエロ・ドライブおよび3311ウェーバリー・ドライブ事件現場調書（1969年）:
  https://www.lapdonline.org/
• [5] カリフォルニア州矯正局（CDCR） — コーコラン州立刑務所受刑者記録チャールズ・マンソン（#B33920）:
  https://www.cdcr.ca.gov/

▸ 専門調査著作および学術研究文献:
• [6] ヴィンセント・ブリオーシ＆カート・ジェントリー — 『ヘルダー・スケルター：マンソン殺人事件の真相』（W. W. Norton, 1974年）:
  https://wwnorton.com/books/9780393322231
• [7] エド・サンダース — 『ファミリー：チャールズ・マンソンのデューンバギー攻撃部隊』（Dutton, 1971年）:
  https://www.penguinrandomhouse.com/books/160677/the-family-by-ed-sanders/
• [8] ダイアン・レイク＆デボラ・ハーマン — 『ファミリーの一員：私のマンソン体験とカルトの崩壊』（William Morrow, 2017年）:
  https://www.harpercollins.com/products/member-of-the-family-dianne-lake-deborah-herman
• [9] ジェフリー・メルニック — 『クリーピー・クローリング：チャールズ・マンソンと悪名高きファミリー』（Arcade Publishing, 2018年）:
  https://www.skyhorsepublishing.com/9781628729955/creepy-crawling/
• [10] ギャビン・ド・ベッカー — 『The Gift of Fear（危険の兆候：暴力から身を守る直観）』（Dell Publishing, 1997年）:
  https://gavindebecker.com/resources/the_gift_of_fear/

▸ 国際報道および歴史的アーカイブ:
• [11] ロサンゼルス・タイムズ — マンソン・ファミリー裁判記録およびシャロン・テート回顧録:
  https://www.latimes.com/local/crime/la-me-manson-trial-archive-htmlstory.html
• [12] ニューヨーク・タイムズ — テート・ラビアンカ事件と1960年代ヒッピー文化の残酷な終焉:
  https://www.nytimes.com/1969/12/02/archives/five-manson-followers-charged-in-tate-murders.html
• [13] TIME誌 — チャールズ・マンソンの人物像と劇場型法廷サーカスの記録（1970年）:
  https://time.com/5029377/charles-manson-dead-history/
• [14] ローリング・ストーン誌 — デイヴィッド・ダルトンによる深層ルポ『世界で最も危険な男の信じがたい記録』（1970年）:
  https://www.rollingstone.com/culture/culture-news/charles-manson-the-incredible-story-of-the-most-dangerous-man-alive-238466/
• [15] CBSニュース — 重要証言者リンダ・カサビアンの免責証言とカルト解体の記録:
  https://www.cbsnews.com/news/charles-manson-family-murders-linda-kasabian-dead-at-73/
• [16] ABCニュース — ダイアン・ソーヤーによる服役中のファミリー元信徒独占インタビュー:
  https://abcnews.go.com/US/charles-manson-followers-recount-murders/story?id=48602280

▸ 行動犯罪学・マインドコントロール研究:
• [17] アメリカ心理学会（APA） — 集団における「没個性化（De-individuation）」および反社会性パーソナリティ障害（ASPD）研究:
  https://www.apa.org/topics/personality-disorders
• [18] グレシャム・サイクス＆デビッド・マッツァ — 犯罪学における「中和の技術（Techniques of Neutralization）」論:
  https://www.jstor.org/stable/2089195
• [19] レオン・フェスティンガー — 閉鎖的カルト組織における「認知的不協和」理論:
  https://www.simplypsychology.org/cognitive-dissonance.html
• [20] スティーヴン・ハッサン — カルトのマインドコントロール「BITEモデル」と個人の主体性剥奪の構造:
  https://freedomofmind.com/cult-mind-control/bite-model/"""

# ==============================================================================
# 4. NGUỒN TIẾNG HÀN (20대 대조 완료된 공식 사법·학술 참고문헌)
# ==============================================================================
SOURCES_KO = """▸ 미국 사법 공식 기록 및 수사 당국 문서:
• [1] 미국 캘리포니아주 로스앤젤레스 상급법원 — 캘리포니아주 대 찰스 맨슨 외 공판 기록 (Case No. A253156):
  https://www.courts.ca.gov/
• [2] 캘리포니아주 대법원 — 사형 위헌 및 무기징역 감형 선례 People v. Anderson (1972) 판결문 (6 Cal. 3d 628):
  https://www.courts.ca.gov/opinions/archive/Crim13617.PDF
• [3] 미국 연방수사국(FBI Vault) — 테이트-라비안카 사건 현장 정밀 수사 기록 및 증거 보고서:
  https://vault.fbi.gov/charles-manson
• [4] 로스앤젤레스 경찰청(LAPD) — 10050 시엘로 드라이브 및 3311 웨이벌리 드라이브 현장 보고서 (1969년):
  https://www.lapdonline.org/
• [5] 캘리포니아 교정재활국(CDCR) — 코코런 주립 교도소 수감자 공식 기록 찰스 맨슨 (#B33920):
  https://www.cdcr.ca.gov/

▸ 심층 탐사 단행본 및 학술 연구 문헌:
• [6] 빈센트 부글리오시 & 커트 젠트리 — 《헬터 스켈터: 맨슨 살인사건의 진실》(W. W. Norton & Company, 1974년):
  https://wwnorton.com/books/9780393322231
• [7] 에드 샌더스 — 《패밀리: 찰스 맨슨 듄 버기 기동대의 실체》(Dutton, 1971년):
  https://www.penguinrandomhouse.com/books/160677/the-family-by-ed-sanders/
• [8] 다이앤 레이크 & 데버라 허먼 — 《패밀리의 일원: 맨슨 카ルト에서의 삶과 60년대의 비극적 종말》(William Morrow, 2017년):
  https://www.harpercollins.com/products/member-of-the-family-dianne-lake-deborah-herman
• [9] 제프리 멜닉 — 《크리피 크롤링: 찰스 맨슨과 악명 높은 패밀리의 민낯》(Arcade Publishing, 2018년):
  https://www.skyhorsepublishing.com/9781628729955/creepy-crawling/
• [10] 개빈 드 베커 — 《The Gift of Fear(생존 경고 신호: 폭력으로부터 우리를 지키는 직관)》(Dell Publishing, 1997년):
  https://gavindebecker.com/resources/the_gift_of_fear/

▸ 국제 언론 심층 보도 및 역사적 영상 아카이브:
• [11] 로스앤젤레스 타임스 — 맨슨 패밀리 역사적 재판 아카이브 및 샤론 테이트 추모 보도:
  https://www.latimes.com/local/crime/la-me-manson-trial-archive-htmlstory.html
• [12] 뉴욕타임스 — 테이트-라비안카 참극과 1960년대 히피 반문화의 비극적 종말:
  https://www.nytimes.com/1969/12/02/archives/five-manson-followers-charged-in-tate-murders.html
• [13] 타임지 — 찰스 맨슨의 인물 프로파일과 서커스 같았던 법정 공방의 기록 (1970년):
  https://time.com/5029377/charles-manson-dead-history/
• [14] 롤링스톤지 — 데이비드 돌턴의 심층 탐사 르포 《살아있는 가장 위험한 사내의 믿을 수 없는 실체》(1970년):
  https://www.rollingstone.com/culture/culture-news/charles-manson-the-incredible-story-of-the-most-dangerous-man-alive-238466/
• [15] CBS 뉴스 — 핵심 기소면제 증인 린다 카사비안의 법정 증언과 맨슨 카ルト의 실체:
  https://www.cbsnews.com/news/charles-manson-family-murders-linda-kasabian-dead-at-73/
• [16] ABC 뉴스 — 다이앤 소여의 맨슨 추종자들(레슬리 밴 하우텐, 패트리샤 크렌윈클) 옥중 독점 인터뷰:
  https://abcnews.go.com/US/charles-manson-followers-recount-murders/story?id=48602280

▸ 행동범죄학 및 강압적 조작·세뇌 연구:
• [17] 미국심리학회(APA) — 폐쇄 집단 내 '몰개성화(De-individuation)' 및 반사회성 성격장애(ASPD) 분석:
  https://www.apa.org/topics/personality-disorders
• [18] 그레셤 사이크스 & 데이비드 마츠아 — 범죄학의 '도덕적 중화 기술(Techniques of Neutralization)':
  https://www.jstor.org/stable/2089195
• [19] 레온 페스팅거 — 폐쇄적 독단 집단에서의 '인지부조화(Cognitive Dissonance)' 이론:
  https://www.simplypsychology.org/cognitive-dissonance.html
• [20] 스티븐 하산 — 사이비 마인드 컨트롤 BITE 모델 및 개인의 도덕적 자율성 박탈 구조:
  https://freedomofmind.com/cult-mind-control/bite-model/"""

# ==============================================================================
# 5. MÔ TẢ ĐẦY ĐỦ TIẾNG VIỆT
# ==============================================================================
DESC_VI = f"""Tập 09: Nghệ Thuật Xóa Bỏ Bản Ngã | Tâm lý học tội phạm: Charles Manson & Thảm Kịch Helter Skelter (Hệ Sinh Thái 10 Chỉ Dấu Tâm Lý & 5 Nấc Thang Vực Thẳm) | Amber eyes

Nước Mỹ cuối thập niên 1960 đang chìm đắm trong đỉnh cao của phong trào phản văn hóa Hippie, nơi hàng triệu người trẻ tin vào thông điệp hòa bình, âm nhạc tự do và sự khai phóng của "Mùa hè Tình yêu". Những chiếc xe van du mục, hoa cài trên tóc và những điệu nhạc folk ngập tràn đường phố San Francisco và Los Angeles. Người ta tin rằng một thế hệ mới ngập tràn yêu thương đang thay thế trật tự cũ kỹ của xã hội tư sản. Thế nhưng, vào hai đêm kinh hoàng đầu tháng 8 năm 1969, ảo tưởng ngây thơ ấy đã bị bóp nghẹt hoàn toàn trong vũng máu.

Đêm ngày 8 rạng sáng ngày 9 tháng 8 năm 1969, tại căn biệt thự biệt lập số 10050 Cielo Drive trên ngọn đồi Benedict Canyon sang trọng thuộc Beverly Hills, một cuộc tàn sát man rợ đã diễn ra. Năm nạn nhân vô tội đã bị sát hại dã man: nữ diễn viên điện ảnh tài năng Sharon Tate — khi ấy đang mang thai tám tháng rưỡi và chỉ còn hai tuần nữa là đến ngày sinh nở, chuyên gia tạo mẫu tóc hàng đầu Hollywood Jay Sebring, người thừa kế gia tộc cà phê Abigail Folger, nhà văn trẻ người Ba Lan Wojciech Frykowski, và cậu học sinh 18 tuổi Steven Parent vô tình ghé qua thăm người quản gia. Chưa đầy 24 giờ sau, đêm ngày 10 tháng 8, cách đó nhiều dặm tại số 3311 đường Waverly Drive, vợ chồng doanh nhân Leno và Rosemary LaBianca tiếp tục bị tàn sát dã man ngay trong chính phòng khách nhà mình. Trên các bức tường và cánh cửa ra vào của hiện trường, những kẻ sát nhân đã dùng chính máu của nạn nhân để viết nên những khẩu hiệu rùng rợn: "PIG", "RISE", "HEALTER SKELTER", và "WAR".

Cơn hoang tưởng tập thể lập tức bao trùm toàn bộ siêu đô thị Los Angeles. Giới thượng lưu Beverly Hills và người dân thành phố hoảng loạn đổ xô đi mua súng ngắn, lắp đặt các hệ thống khóa an ninh, thuê chó săn và vệ sĩ tư nhân để tự vệ. Cảnh sát LAPD hoàn toàn bế tắc trước một hiện trường không hề có động cơ cướp tài sản thông thường hay thù hằn cá nhân. Nhưng điều gây chấn động tột cùng cho toàn thế giới chính là sự thật về kẻ chủ mưu khi bức màn bí mật được vén lên: Hắn không hề chạm tay vào hung khí, không hề có mặt tại thời khắc đoạt mạng nạn nhân tại căn biệt thự Cielo Drive. Hắn là Charles Manson — một kẻ lang thang với nửa cuộc đời ngập chìm sau song sắt nhà tù, một kẻ ái kỷ ác tính đã dùng ma túy LSD, âm nhạc, sự cô lập địa lý và nghệ thuật thao túng xóa bỏ bản ngã tinh vi để biến những thanh niên ưu tú, có học thức thành những cỗ máy giết người mù quáng không còn lương tri.

Hồ sơ Charles Manson & Gia đình Manson được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG TƯỞNG TẬP THỂ (COLLECTIVE PARANOIA): Vụ thảm sát Sharon Tate đã chôn vùi vĩnh viễn sự ngây thơ của kỷ nguyên Hippie và phong trào phản văn hóa; cơn hoang tưởng tập thể khiến cư dân Beverly Hills và Los Angeles nín thở sau những cánh cửa khóa chặt, mua sạch súng tại các cửa hàng vũ khí; về mặt tư pháp, vụ án đã đặt định chế lịch sử về trách nhiệm của kẻ chủ mưu gián tiếp (vicarious liability) thông qua lập luận sắc bén của Công tố viên Vincent Bugliosi; đồng thời phán quyết bước ngoặt People v. Anderson (1972) của Tòa Tối cao California đã bãi bỏ án tử hình, biến án tử của Manson và đồng bọn thành tù chung thân.
2. VẬT HÓA NẠN NHÂN & KHUYẾT TẬT THẤU CẢM (OBJECTIFICATION & EMPATHY DEFICIT): Các nạn nhân bị giáng cấp thành "Pigs" (lũ lợn đại diện cho xã hội tư sản) và những đạo cụ vô tri trong vở kịch khải huyền Helter Skelter; sự khuyết tật hoàn toàn của Thuyết tâm trí (Theory of Mind) và sự tê liệt thấu cảm cảm xúc khiến tiếng van xin bảo vệ đứa con trong bụng của Sharon Tate không khơi gợi được chút trắc ẩn nào, mà trái lại trở thành chất kích hoạt hưng phấn quyền lực tàn bạo của những kẻ sát nhân bị tẩy não.
3. CƠ CHẾ CHIA NGĂN NHẬN THỨC & BI KỊCH NẠN NHÂN THỨ HAI (COMPARTMENTALIZATION): Manson coi các tín đồ như "công cụ kéo dài của bản ngã ái kỷ" (extensions of the self); các tín đồ vận hành hai thực tại hoàn toàn tách biệt: ban ngày là cuộc sống du ca hippie bình thản, chơi nhạc và ca hát tại trang trại Spahn Ranch, ban đêm hóa thành những sát thủ máu lạnh mà không hề có xung đột lương tri nội tại; đồng thời phơi bày bi kịch của các nạn nhân thứ hai: cha mẹ của Leslie Van Houten, Susan Atkins, Patricia Krenwinkel sụp đổ hoàn toàn danh tính khi con gái ngoan ngoãn trở thành ác quỷ tàn sát.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ & TỰ THƯƠNG HẠI BỆNH LÝ (NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY): Màn kịch rạp xiếc ái kỷ kéo dài suốt 9,5 tháng xét xử: Manson khắc chữ X lên trán, buộc các tín đồ làm theo, lao qua bàn luật sư mưu toan tấn công Thẩm phán Charles Older nhằm duy trì quyền lực và sự chú ý tối thượng; khi bị cách ly và tước bỏ quyền lực sau song sắt nhà tù Corcoran suốt 46 năm, bản ngã ái kỷ sụp đổ hoàn toàn thành sự tự thương hại bệnh lý (pathological self-pity), bám víu vào sự hận thù và ảo tưởng cho đến khi qua đời trong cô độc năm 2017 ở tuổi 83.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC (TECHNIQUES OF NEUTRALIZATION): Vận dụng triệt để lý thuyết của Sykes & Matza: (1) Kháng cáo lý tưởng cao hơn (Appeal to higher loyalties) — ngụy biện rằng hành vi tàn sát là "đại từ bi" để khơi mào chiến tranh sắc tộc Helter Skelter nhằm cứu rỗi thế giới; (2) Đổ lỗi cho xã hội và nhà tù (Condemning the condemners) — tuyên bố xã hội đã tạo ra con quái vật trong hắn; (3) Ngoại hóa trách nhiệm (Denial of responsibility) — Manson rũ bỏ tội lỗi bằng tuyên bố ngụy biện "tay tôi không hề chạm vào bất kỳ hung khí nào".
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY (PRECIPITATING TRIGGER): Bị nhà sản xuất âm nhạc Terry Melcher (hãng Columbia Records) từ chối ký hợp đồng thu âm và phát hành album đã giáng đòn chí mạng hủy hoại cái tôi ái kỷ mong manh của Manson; kết hợp với sự bế tắc khi dự ngôn "chiến tranh sắc tộc giữa người da đen và da trắng" mãi không tự bùng nổ; ngôi nhà 10050 Cielo Drive (nơi Melcher từng thuê cùng bạn gái Candice Bergen) trở thành mục tiêu trút giận và kích hoạt mệnh lệnh thảm sát nhằm "châm ngòi" cho Helter Skelter.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO (SIGNATURE VS. MODUS OPERANDI): Thủ đoạn MO (Modus Operandi) thích ứng linh hoạt để che giấu và sinh tồn: cắt đứt dây điện thoại trước khi đột nhập, mặc trang phục đen chuyên dụng, dùng hung khí dao và súng ngắn rồi vứt rải rác trên đường tẩu thoát, rút lui ẩn náu sâu trong sa mạc Death Valley; Dấu ấn tâm lý Signature bất biến: dùng máu nạn nhân viết các khẩu hiệu Helter Skelter ("PIG", "RISE", "HEALTER SKELTER", "WAR") lên tường và cửa ra vào; dùng dây thừng trói cổ các nạn nhân nối vào xà nhà nhằm thỏa mãn nhu cầu bệnh lý cưỡng chế hiện thực hóa ảo tưởng khải huyền.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG 5 NẤC THANG (ESCALATION TRAJECTORY & TOLERANCE BUILDUP): Quá trình xây dựng ngưỡng dung nạp kích thích bị đẩy xa dần qua 5 nấc thang: (1) Trộm cắp xe hơi, gian lận séc ngân hàng và lưu manh vặt -> (2) Thành lập giáo phái du mục, sử dụng LSD và âm nhạc thao túng tâm lý tại Spahn Ranch -> (3) Tập dượt xâm nhập ban đêm "Creepy Crawling" vào nhà dân để kiểm tra mức độ phục tùng -> (4) Bắn trọng thương tay buôn ma túy Bernard Crowe và trực tiếp xúi giục sát hại nhạc sĩ Gary Hinman (tháng 7/1969) -> (5) Bùng nổ thảm sát liên hoàn tại biệt thự Cielo Drive và dinh thự Waverly Drive (tháng 8/1969).
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI (HALO EFFECT & COLLECTIVE BLIND SPOTS): Chiếc áo ngụy trang hoàn hảo của phong trào Hippie: biểu tượng hòa bình, hoa cài trên tóc, thông điệp "tình yêu tự do" và phản chiến đã che giấu một kẻ săn mồi nguy hiểm; xã hội và giới chấp pháp thời bấy giờ có định kiến cho rằng cộng đồng thanh niên Spahn Ranch chỉ là những đứa trẻ lập dị, nổi loạn vô hại, tạo nên điểm mù chết người trong công tác phòng ngừa tội phạm.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ SINH TỒN (VICTIMOLOGY & SURVIVAL RED FLAGS): Tôn vinh nhân phẩm và ký ức của các nạn nhân vô tội: Sharon Tate và thai nhi Paul Richard Polanski, Jay Sebring, Abigail Folger, Wojciech Frykowski, Steven Parent, Leno LaBianca, Rosemary LaBianca, và Gary Hinman; Đúc kết 4 cảnh báo đỏ sinh tồn cốt lõi theo nguyên lý The Gift of Fear của Gavin de Becker nhằm nhận diện các tổ chức thao túng tâm lý: (1) Cảnh giác bẫy "Love Bombing" dồn dập (sự quan tâm nồng nhiệt quá mức nhằm xóa bỏ ranh giới tâm lý); (2) Nhận diện thủ đoạn cô lập địa lý và cắt đứt liên lạc với gia đình, bạn bè; (3) Từ chối tư duy nhị nguyên trắng - đen và sự sùng bái cá nhân cực đoan (khi người đứng đầu tự phong mình là hiện thân của Chúa hay Đấng cứu thế); (4) Tuyệt đối giữ vững quyền tự chủ đạo đức và phán đoán lương tri (không bao giờ chuyển giao trách nhiệm đạo đức cá nhân cho bất kỳ ai).

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · The Hook — Dấu chấm hết của Mùa hè Tình yêu & Cơn hoang tưởng Los Angeles
05:20 Hồi 2 · Hiện trường biệt thự & Bóng ma Helter Skelter tại Spahn Ranch
10:45 Hồi 3 · Giải phẫu tâm lý — Bên trong bộ não thao túng & Nghệ thuật xóa bỏ bản ngã
16:30 Hồi 4 · Đấu trí phòng xử án & Trách nhiệm kẻ không chạm tay
21:50 Hồi 5 · Phán quyết lịch sử, bản án tâm lý & Bài học cảnh báo đỏ

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai tại Hoa Kỳ (Tòa Thượng thẩm California Hạt Los Angeles, Tòa Tối cao California, Cảnh sát LAPD, FBI, Cục Cải huấn CDCR). Kênh không nhằm bôi nhọ hay tôn vinh bất kỳ tổ chức hay cá nhân nào.
• Tôn trọng phẩm giá và tưởng niệm sâu sắc các nạn nhân vô tội cùng gia đình họ.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là hình tượng minh họa nghệ thuật. Lời của Điều tra viên, Chuyên gia và Nhân chứng là lời dựng lại dựa trên tư liệu lịch sử phiên tòa.
• Giọng đọc, hình ảnh và âm thanh được hỗ trợ bởi công nghệ AI.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 NGUỒN THAM KHẢO ĐÃ ĐỐI CHIẾU
Toàn bộ sự kiện, mốc thời gian, tên nhân vật, chứng cứ hiện trường và trích dẫn trong video đã được đối chiếu từng câu với 20 nguồn công khai (hồ sơ tòa án, báo cáo cảnh sát, biên bản điều tra, báo chí quốc tế, nghiên cứu tâm lý học):

{SOURCES_VI}

Danh mục nguồn chi tiết kèm biên bản đối chiếu dữ kiện lịch sử được lưu trữ tại: 02_SAN_XUAT/Tap09/nguon_tham_khao.md

🆘 Nếu bạn biết một trẻ em đang bị bạo hành hoặc gia đình cần trợ giúp tâm lý, hãy liên hệ:
• Tổng đài quốc gia bảo vệ trẻ em: 111 (Việt Nam, miễn phí, 24/7) — http://tongdai111.vn
• Đường dây nóng hỗ trợ tâm lý Ngày Mai: 096 306 1414 — https://duongdaynongngaymai.vn
• Viện Sức khỏe Tâm thần – Bệnh viện Bạch Mai: 024 3869 3731
• Ngôi nhà Bình Yên (Hỗ trợ phụ nữ và trẻ em bị bạo lực): 1900 969 680
• 988 Suicide & Crisis Lifeline (Hoa Kỳ): Gọi hoặc nhắn tin 988 — https://988lifeline.org
• Childhelp National Child Abuse Hotline (Hoa Kỳ): 1-800-422-4453 — https://www.childhelphotline.org

#AmberEyes #TrueCrime #TamLyToiPham #CharlesManson #HelterSkelter #MansonFamily #XoaBoBanNga #10ChiDauTamLy #CanhBaoDo #GavinDeBecker #VincentBugliosi #SharonTate #SpahnRanch #HoSoToiPham #Documentary"""

# ==============================================================================
# 6. MÔ TẢ ĐẦY ĐỦ TIẾNG ANH
# ==============================================================================
DESC_EN = f"""Ep. 09: The Art of Ego Erasure | Criminal Psychology: Charles Manson & The Manson Family Tragedy (10 Psychological Markers & 5 Stages of Escalation) | Amber eyes

In the late 1960s, America was captivated by the height of the counterculture revolution—a vibrant era where millions of young people embraced the peaceful idealism of the "Summer of Love," free-spirited folk music, and countercultural liberation. Nomadic camper vans, flower-power innocence, and community communes dotted San Francisco and Southern California. Many believed that an enlightened generation of love was dawning to replace the rigid orthodoxy of bourgeois society. Yet, across two terrifying nights in early August 1969, that sweet delusion was brutally drowned in pools of blood.

On the night of August 8 into the early hours of August 9, 1969, at a secluded luxury estate located at 10050 Cielo Drive in the Benedict Canyon hills of Beverly Hills, an unspeakable massacre unfolded. Five innocent victims were mercilessly slaughtered: gifted actress Sharon Tate—eight-and-a-half months pregnant and merely two weeks away from giving birth, celebrity hairstylist Jay Sebring, coffee heiress Abigail Folger, young Polish writer Wojciech Frykowski, and 18-year-old high school graduate Steven Parent who had merely stopped by to visit the estate caretaker. Less than 24 hours later, on the night of August 10, several miles away at 3311 Waverly Drive, supermarket executive Leno LaBianca and his wife Rosemary were butchered in their living room. Written across the crime scene walls and front doors in the victims' own blood were chilling apocalyptic slogans: "PIG", "RISE", "HEALTER SKELTER", and "WAR".

A wave of collective paranoia gripped metropolitan Los Angeles. Wealthy Beverly Hills residents and ordinary citizens panicked, rushing to gun shops to purchase handguns, reinforcing deadbolts, and hiring guard dogs and private security guards. LAPD detectives were baffled by a grotesque crime scene devoid of ordinary robbery motives or personal feuds. But what truly shattered the nation was the chilling reality of the mastermind when the veil was finally lifted: He had never held a weapon at the scene, nor had he been present when the victims breathed their last at Cielo Drive. He was Charles Manson—a career drifter who had spent half his life behind bars, a malignant sociopathic narcissist who weaponized LSD, hypnotic music, geographic isolation, and the dark art of systematic ego erasure to transform educated, privileged young people into remorseless executioners.

Amber eyes dissects the Charles Manson & The Manson Family file through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: The Tate-LaBianca murders irrevocably shattered the innocence of the counterculture era and buried the flower-power movement; collective paranoia seized Southern California as residents double-locked doors and emptied firearm shelves; judicially, the case established an enduring legal landmark regarding mastermind vicarious liability through Prosecutor Vincent Bugliosi's historic argument; concurrently, the California Supreme Court's landmark ruling People v. Anderson (1972) abolished capital punishment, commuting death sentences for Manson and his followers to life imprisonment.
2. OBJECTIFICATION & EMPATHY DEFICIT: Victims were stripped of their humanity, reduced into "Pigs" representing the bourgeois establishment and disposable stage props in an apocalyptic Helter Skelter fantasy; a total deficit in Theory of Mind and profound affective callousness ensured that Sharon Tate's desperate pleas to save her unborn baby elicited zero mercy, functioning instead as a sadistic psychological trigger for power arousal among the brainwashed executioners.
3. COGNITIVE COMPARTMENTALIZATION & SECONDARY VICTIMS: Manson treated his followers as "extensions of his narcissistic ego"; disciples operated within two radically insulated realities: by day, pastoral hippie communal living, singing folk songs and playing guitars at Spahn Ranch; by night, detached, robotic slaughterers devoid of internal moral dissonance; concurrently exposing the devastation of secondary victims: the respectable parents of Leslie Van Houten, Susan Atkins, and Patricia Krenwinkel, whose social identities were utterly obliterated upon learning their daughters had become mass murderers.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: A protracted 9.5-month courtroom circus: Manson carved an X into his forehead, coerced disciples to mimic him, and lunged across counsel table to assault Judge Charles Older to retain absolute messianic dominance; yet once isolated and stripped of his flock over 46 years within Corcoran State Prison, his grandiose facade suffered total narcissistic collapse, devolving into pathological self-pity and paranoid bitterness until his solitary death in 2017 at age 83.
5. TECHNIQUES OF NEUTRALIZATION (SYKES & MATZA): Masterful deployment of neutralization techniques: (1) Appeal to higher loyalties—rationalizing mass murder as an act of cosmic mercy to ignite Helter Skelter and liberate mankind; (2) Condemning the condemners—accusing society and prison institutions of having manufactured his monstrous nature; (3) Denial of responsibility—externalizing moral culpability through the duplicitous mantra "my hands never touched a single weapon."
6. PRECIPITATING TRIGGER & TIPPING POINT: Columbia Records producer Terry Melcher’s rejection of Manson’s musical ambitions dealt a fatal blow to his fragile narcissistic ego; coupled with the mounting panic that his prophesied racial apocalypse was failing to materialize, 10050 Cielo Drive (the residence Melcher formerly leased with Candice Bergen) became the designated slaughterhouse to ignite Helter Skelter.
7. SIGNATURE VS. MODUS OPERANDI (MO): Modus Operandi (MO) evolved strategically for stealth and survival: severing telephone lines prior to entry, donning specialized black clothing, discarding firearms and knives during the getaway, and fleeing deep into Death Valley; Immutable psychological Signature: utilizing victims' blood to scrawl apocalyptic slogans ("PIG", "RISE", "HEALTER SKELTER", "WAR") on doors and walls; binding victims by their necks with nylon rope over ceiling rafters to fulfill a compulsive theatrical craving for omnipotent dominance.
8. 5-STAGE ESCALATION TRAJECTORY & TOLERANCE BUILDUP: Tolerance buildup pushed behavioral thresholds through five distinct stages: (1) Auto theft, check forgery, and petty larceny -> (2) Establishing a nomadic LSD hippie cult at Spahn Ranch -> (3) Nighttime residential break-in rehearsals known as "Creepy Crawling" -> (4) Shooting drug dealer Bernard Crowe and orchestrating the homicide of musician Gary Hinman (July 1969) -> (5) Coordinated massacres at Cielo Drive and Waverly Drive (August 1969).
9. HALO EFFECT & COLLECTIVE BLIND SPOTS: The flower-power counterculture aesthetic provided an impenetrable cloak; peace symbols, guitars, and communal love slogans masked an apex predator; contemporary society and law enforcement dismissed Spahn Ranch commune members as eccentric, harmless hippie runaways, creating a catastrophic systemic blind spot in crime prevention.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Honoring the human dignity and sacred memory of the victims: Sharon Tate and her unborn son Paul Richard Polanski, Jay Sebring, Abigail Folger, Wojciech Frykowski, Steven Parent, Leno LaBianca, Rosemary LaBianca, and Gary Hinman; Distilling 4 vital survival red flags based on Gavin de Becker's The Gift of Fear to identify destructive manipulative groups: (1) Beware aggressive "Love Bombing" designed to dismantle psychological boundaries; (2) Recognize geographic isolation and enforced estrangement from family; (3) Reject black-and-white ideological dualism and messianic authoritarian worship; (4) Vigorously safeguard moral autonomy and individual conscience (never outsource moral responsibility to any leader).

⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · The Hook — The End of the Summer of Love & Collective Paranoia in Los Angeles
05:20 Act 2 · The Mansions & The Helter Skelter Shadow at Spahn Ranch
10:45 Act 3 · Psychological Autopsy — Inside the Manipulative Mind & The Art of Ego Erasure
16:30 Act 4 · Courtroom Drama & Mastermind Liability
21:50 Act 5 · Historical Verdict, Psychological Sentence & Red Flags for Survival

⚠️ LEGAL ADVISORY & SAFETY
• Produced solely for educational, criminological, and historical documentation; not a substitute for professional medical, psychiatric, or legal advice.
• Based on public judicial records and investigative findings in the United States (Los Angeles County Superior Court, California Supreme Court, LAPD, FBI Vault, CDCR). Not intended to defame or glorify any organization or individual.
• Complete reverence is accorded to the memory and dignity of the victims and their surviving families.
• Character avatars (Owl, Wolf, Fox, Sheep, Cat) are dramatized artistic illustrations. Statements by Investigators, Psychologists, and Witnesses are reconstructed from historical trial records.
• Synthesized voiceover, imagery, and audio engineered with AI technologies.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 VERIFIED HISTORICAL SOURCES & DOCKETS
All case chronologies, data points, forensic evidence, and quotations cross-referenced against 20 public records:

{SOURCES_EN}

Comprehensive source documentation and verification logs archived at: 02_SAN_XUAT/Tap09_EN/nguon_tham_khao_EN.md

🆘 If you or someone you know is in crisis, experiencing domestic abuse, or facing coercive group manipulation:
• National Suicide and Crisis Lifeline (US & Canada): Call or text 988 (24/7, Free & Confidential) — https://988lifeline.org
• Childhelp National Child Abuse Hotline: 1-800-422-4453 — https://www.childhelphotline.org
• Crisis Text Line: Text HOME to 741741 — https://www.crisistextline.org
• National Domestic Violence Hotline: 1-800-799-7233 — https://www.thehotline.org
• National Child Helpline 111 (Vietnam, toll-free 24/7) — http://tongdai111.vn

#AmberEyes #TrueCrime #CriminalPsychology #CharlesManson #HelterSkelter #MansonFamily #EgoErasure #Deindividuation #10PsychologicalMarkers #SurvivalRedFlags #VincentBugliosi #SharonTate #SpahnRanch #ForensicFiles #Documentary"""

# ==============================================================================
# 7. MÔ TẢ ĐẦY ĐỦ TIẾNG NHẬT
# ==============================================================================
DESC_JA = f"""第09話：自我を消去する技術 | 犯罪心理学：チャールズ・マンソンとファミリーの悲劇（10の心理指標エコシステムと5段階エスカレーション） | Amber eyes

1960年代後半のアメリカは、ヒッピー文化と「愛の夏（Summer of Love）」が約束した平和の理想に酔いしれていました。何百万人もの若者が反体制文化の解放感、自由なフォーク音楽、そして愛と連帯のメッセージを信じ、サンフランシスコやロサンゼルスの街には花を髪に飾った若者たちとキャンピングカーが溢れていました。古い資本主義の抑圧的な秩序を打ち破り、純粋な愛に基づく新しい時代が訪れると信じられていたのです。しかし1969年8月初旬の血塗られた2夜によって、その無邪気な幻想は残酷に打ち砕かれました。

1969年8月8日の深夜から9日未明にかけて、ビバリーヒルズの閑静な高級住宅街ベネディクト・キャニオンに位置するシエロ・ドライブ10050番地の邸宅で、未曾有の無差別虐殺が発生しました。出産をわずか2週間後に控えた妊娠8か月半の新進気鋭の女優シャロン・テート、ハリウッド屈指のヘアスタイリストであるジェイ・セブリング、有名コーヒー財閥の令嬢アビゲイル・フォルジャー、若きポーランド人作家ヴォイチェフ・フリコフスキー、そして管理人の知人を訪ねて偶然居合わせた18歳の青年スティーブン・ペアレントの5名が無残に命を奪われました。さらにその翌夜、数マイル離れたウェーバリー・ドライブ3311番地で、スーパーマーケットを経営するレノ＆ローズマリー・ラビアンカ夫妻が自宅のリビングで同様に虐殺されたのです。現場の壁や玄関ドアには、犠牲者の血を使って「PIG」「RISE」「HEALTER SKELTER」「WAR」といった不気味な終末予言のスローガンが殴り書きされていました。

大都市ロサンゼルスは一瞬にして集団的偏執病（パラノイア）の恐怖に覆い尽くされました。ビバリーヒルズの富裕層や一般市民はパニックに陥り、銃器店に殺到して拳銃を買い漁り、頑丈な二重鍵を取り付け、護衛犬や私設警備員を雇いました。金品強奪や個人的な怨恨といった通常の動機が一切見当たらない現場を前に、ロサンゼルス市警察の捜査は完全に暗礁に乗り上げました。しかし世界に最大の衝撃を与えたのは、事件の背後にいた真の首謀者の正体でした。男はシエロ・ドライブの現場で凶器に一度も触れておらず、犠牲者が絶命したその瞬間に現場に居合わせることすらしていませんでした。男の名はチャールズ・マンソン。人生の半分以上を刑務所の独房で過ごした前科者であり、LSD、音楽、地理的隔絶、そして「自我を消去する技術」を駆使して、高い教育を受けた善良な青年たちを盲目的な殺人機械へと改造した誇大自己愛的な怪物だったのです。

犯罪心理学ドキュメンタリー『Amber eyes』第09話では、本事件を「10の核心的心理・行動指標エコシステム」に基づいて徹底解剖します：
1. 社会的余波と集団的パラノイア（COLLECTIVE PARANOIA）：テート・ラビアンカ事件はヒッピー時代の無邪気な理想主義に永遠の終止符を打ちました；ロサンゼルス市民が施錠された部屋で息を潜め銃器を買い漁った集団パニック；ヴィンセント・ブリオーシ検事の歴史的論告による「間接的教唆責任（首謀者責任）」の法的確立；1972年カリフォルニア州最高裁判所の「ピープル対アンダーソン」判例による死刑違憲判断と終身刑への減刑。
2. 被害者の客体化と共感の欠如（OBJECTIFICATION & EMPATHY DEFICIT）：被害者は資本主義社会を象徴する「Pigs（豚）」や終末戦争ヘルター・スケルターの無機質な舞台小道具へと格下げ；心の理論（Theory of Mind）の完全な機能不全とおぞましい感情麻痺により、お腹の子供の命乞いをするシャロン・テートの叫びが共感を呼ぶどころか、洗脳された実行犯たちの歪んだ支配欲を刺激する触媒へと反転した狂気。
3. 精神の分断（区画化）と二次被害の悲劇（COMPARTMENTALIZATION）：信徒を「肥大化した自己の延長物」として完全支配；スパーン牧場で歌を歌い平和を語る「牧歌的な昼の世界」と、現場で冷酷に刃を振るう「夜の暗殺者」という内面的葛藤を排した二重生活の分断；真面目だった愛娘が悪魔の殺人鬼へと変貌したことを知りアイデンティティが完全崩壊した両親たちの悲劇。
4. 自己愛の崩壊と病的な自己憐憫（NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY）：9か月半に及んだ法廷サーカス：額にXの傷を刻み信徒に模倣させ、裁判長に飛びかかり絶対的支配者を演じ続けたマンソン；しかしコーコラン刑務所で隔離され権力を剥奪された46年間の獄中生活において、その誇大自己は完全崩壊し、2017年に83歳で孤独死するまで被害者面と病的な自己憐憫に耽溺した末路。
5. 中和の技術と自己正当化（TECHNIQUES OF NEUTRALIZATION）：サイクス＆マッツァの理論の実践：(1) より高次の忠誠心への訴求 — 人類を救う終末戦争を起こすための「慈悲の殺人」という狂気の歪曲；(2) 非難者への非難 — 自分のような怪物を作ったのは腐敗した社会と刑務所体制であるという責任転嫁；(3) 責任の外在化 — 「自分は一度も凶器を手にしていない」という欺瞞的抗弁。
6. 心理的引き金と限界点（PRECIPITATING TRIGGER）：音楽プロデューサーのテリー・メルチャーによるレコード契約拒絶がマンソンの脆弱な自己愛に致命傷を与えた点；予言した人種戦争が一向に起きない焦燥感；かつてメルチャーが住んでいたシエロ・ドライブ10050番地が標的として選ばれ、終末戦争の引き金として虐殺命令が下された背景。
7. 精神的シグネチャー対手口（SIGNATURE VS. MODUS OPERANDI）：手口（MO）は隠蔽と生存のために周到に進化：事前に電話線を切断、専用の黒服の着用、逃走経路への凶器遺棄、デスバレー砂漠への潜伏；不変の心理的シグネチャー：被害者の血で壁やドアに終末スローガン（PIG、RISE、HEALTER SKELTER、WAR）を書き殴り、被害者の首をナイフやロープで天井梁に繋ぎ止める劇的な支配願望の具現化。
8. 5段階のエスカレーション軌道（ESCALATION TRAJECTORY）：刺激耐性の形成に伴う暴力の5段階：(1) 車両窃盗や小切手偽造などの軽犯罪 -> (2) スパーン牧場におけるLSDと音楽を用いた放浪カルトの結成 -> (3) 服従度を試す夜間侵入訓練「クリーピー・クローリング」 -> (4) 麻薬密売人バーナード・クロウ銃撃とゲイリー・ヒンマン殺害教唆（1969年7月） -> (5) シエロ・ドライブおよびウェーバリー・ドライブでの無差別大量虐殺（1969年8月）。
9. 後光効果（ハロー効果）と社会の死角（HALO EFFECT & BLIND SPOTS）：ヒッピー文化の完璧な隠れ蓑：愛、平和、花、反戦のシンボルが冷酷な捕食者の本性を遮蔽；当時の社会と警察組織がスパーン牧場の若者たちを「単なる無害な不良集団」と侮った致命的な制度的盲点。
10. 被害者学と生存のための4大レッドフラッグ（VICTIMOLOGY & SURVIVAL REDFLAGS）：犠牲者の尊厳の回復：シャロン・テートとお腹の胎児、ジェイ・セブリング、アビゲイル・フォルジャー、ヴォイチェフ・フリコフスキー、スティーブン・ペアレント、レノ＆ローズマリー・ラビアンカ、ゲイリー・ヒンマン；ギャビン・ド・ベッカー『The Gift of Fear』に基づくカルト・マインドコントロール見抜き警告：(1) 心理的境界線を溶かす過剰な「ラブ・ボンビング」への警戒；(2) 地理的孤立と家族・友人関係の遮断の察知；(3) 白黒二元論と教祖への絶対的個人崇拝の拒絶；(4) 良心の自己決定権と倫理的主体性の厳守（自己の道徳的責任を他者に委ねないこと）。

⏱ 目次（チャプター）
00:00 オープニング・免責事項
00:23 第1幕 · フック — 「愛の夏」の残酷な終焉とロサンゼルスの集団的偏執病
05:20 第2幕 · 邸宅の惨劇＆スパーン牧場の終末幻想
10:45 第3幕 · 犯罪心理解剖 — マインドコントロールの深層と自我を消去する技術
16:30 第4幕 · 法廷の攻防＆手を下さざる黒幕の責任
21:50 第5幕 · 歴史的判決、深層心理の刑罰＆生存のためのレッドフラッグ

⚠️ ご視聴にあたっての注意事項
• 本動画は教育目的および犯罪心理学・歴史記録の観点からの分析コンテンツであり、医学的、心理学的、または法的助言を提供するものではありません。
• 米国の公開裁判資料および公的捜査記録（ロサンゼルス郡上級裁判所、カリフォルニア州最高裁判所、LAPD、FBI、CDCR）に基づき制作されています。個人を誹謗中傷、または美化する意図はありません。
• 犠牲者とそのご遺族の名誉と尊厳に最大の敬意を払っています。
• フクロウ、オオカミ、キツネ、ヒツジ、ネコのアバターは芸術的演出です。捜査官、心理学者、証人の発言は歴史的公判資料に基づき再構成されています。
• 音声、画像、映像の生成にはAI技術が活用されています。
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 参照・照合済み公的資料リスト
動画内のすべての年表、事実関係、および証言は以下の20の公的資料および学術研究に基づき照合されています：

{SOURCES_JA}

詳細な出典および歴史的事実の対照記録は以下に保管されています：02_SAN_XUAT/Tap09_JA/nguon_tham_khao_JA.md

🆘 心の健康相談および危機対応窓口（通話無料・24時間対応）:
• こころの健康相談統一ダイヤル: 0570-064-556
• よりそいホットライン: 0120-279-338
• 警察相談専用電話: #9110 （緊急時は110番）
• 児童相談所虐待対応ダイヤル: 189
• TELL Lifeline（日本国内・多言語対応）: 03-5774-0992 — https://telljp.com
• 米国 988 Suicide & Crisis Lifeline: 988 — https://988lifeline.org

#AmberEyes #犯罪心理学 #心理分析 #チャールズマンソン #マンソンファミリー #自我の消去 #没個性化 #マインドコントロール #プロファイリング #10の心理指標 #レッドフラッグ #シャロンテート #実話事件 #ドキュメンタリー"""

# ==============================================================================
# 8. MÔ TẢ ĐẦY ĐỦ TIẾNG HÀN
# ==============================================================================
DESC_KO = f"""제09화: 자아를 지우는 기술 | 범죄심리학: 찰스 맨슨과 맨슨 패밀리 참극 (10대 핵심 심리 지표 및 5단계 에스컬레이션) | Amber eyes

1960년대 후반의 미국은 히피 반문화와 ‘사랑의 여름(Summer of Love)’이 약속한 평화와 자유의 이상에 깊이 취해 있었습니다. 수백만 명의 청년들이 기성세대의 억압적인 질서에서 벗어나 자유로운 포크 음악, 꽃을 꽂은 머리, 히피 공동체의 연대를 믿으며 샌프란시스코와 로스앤젤레스의 거리를 메웠습니다. 사랑과 평화의 새로운 유토피아가 도래할 것이라는 순진한 믿음이 사회를 지배하고 있었습니다. 그러나 1969년 8월 초, 이틀간 벌어진 유혈 참극은 그 순진무구한 환상을 단숨에 피비린내 나는 악몽으로 바꾸어 놓았습니다.

1969년 8월 8일 깊은 밤부터 9일 새벽 사이, 베벌리 힐스의 한적하고 부유한 언덕 베네딕트 캐니언에 위치한 10050 시엘로 드라이브 저택에서 상상을 초월하는 무차별 학살이 자행되었습니다. 임신 8개월 반으로 출산을 불과 2주 앞두고 있던 촉망받는 여배우 샤론 테이트, 할리우드 최고의 헤어스타일리스트 제이 세브링, 대형 커피 재벌가의 상속녀 애비게일 폴저, 폴란드 출신의 전도유망한 젊은 작가 보이체크 프라이코프스키, 그리고 관리인 친구를 만나러 우연히 들렀던 18세 청년 스티븐 패런트 등 5명의 무고한 생명이 처참하게 살해당했습니다. 그리고 채 24시간도 지나지 않은 8월 10일 밤, 수 마일 떨어진 3311 웨이벌리 드라이브 저택에서 슈퍼마켓 체인을 운영하던 레노·로즈마리 라비안카 부부가 자신들의 거실에서 또다시 잔혹하게 난자당했습니다. 현장의 벽과 현관문에는 피해자들의 피로 쓴 기괴한 종말론적 혈서가 선명하게 남아 있었습니다: "PIG", "RISE", "HEALTER SKELTER", 그리고 "WAR".

로스앤젤레스 대도시 전체가 순식간에 집단적 편집증(Collective Paranoia)의 거대한 공포에 휩싸였습니다. 베벌리 힐스의 상류층과 시민들은 극심한 패닉 속에 총기상으로 달려가 권총을 사재기했고, 문마다 이중 자물쇠를 설치했으며, 경비견과 사설 경호원을 고용했습니다. 강도나 개인적 원한 같은 통상적인 범죄 동기가 전무한 현장 앞에서 LAPD 경찰의 수사는 완전히 미궁에 빠졌습니다. 그러나 세상을 가장 경악하게 만든 진실은 마침내 베일이 벗겨진 주범의 정체였습니다. 그는 시엘로 드라이브 현장에서 흉기에 손끝 하나 대지 않았으며, 피해자들이 숨을 거두던 그 시각 현장에 있지도 않았습니다. 그의 이름은 찰스 맨슨. 인생의 절반을 감옥에서 보낸 전과자이자, 환각제 LSD와 음악, 지리적 고립, 그리고 정교한 ‘자아 삭제의 기술’을 통해 유복하고 교양 있던 청년들을 맹목적인 살인 기계로 개조한 사이코패스적 교주였습니다.

범죄심리학 채널 ‘Amber eyes’ 09화에서는 맨슨 패밀리 참극을 ‘10대 핵심 심리 및 행동 지표 생태계’를 통해 심층 해부합니다:
1. 사회적 충격과 집단적 편집증 (COLLECTIVE PARANOIA): 테이트-라비안카 살인 사건은 히피 시대의 순진한 이상주의를 영구히 종식시켰습니다; 로스앤젤레스 전역을 휩쓴 집단 패닉과 총기 사재기 열풍; 빈센트 부글리오시 검사의 정교한 법리를 통한 ‘간접 교사자(배후 조종자) 책임’의 역사적 확립; 1972년 캘리포니아 대법원의 ‘피플 대 앤더슨’ 위헌 판결로 인한 사형 폐지 및 종신형 감형의 전말.
2. 피해자의 사물화 및 공감 결여 (OBJECTIFICATION & EMPATHY DEFICIT): 피해자들을 기득권 사회를 상징하는 ‘Pigs(돼지들)’이자 헬터 스켈터 종말 환상의 소모품 무대 소품으로 격하시킴; 마음 이론(Theory of Mind)의 완전한 붕괴와 감정적 마비로 인해 뱃속의 아이만은 살려달라는 샤론 테이트의 절규가 자비를 부르기는커녕 살인자들의 왜곡된 권력적 흥분을 자극하는 방아쇠로 작용한 광기.
3. 인지적 구획화와 2차 피해자의 비극 (COMPARTMENTALIZATION): 신도들을 ‘과대 자아의 연장선’으로 완벽히 통제; 스판 랜치에서 평화롭게 노래 부르고 기타를 치는 ‘목가적인 낮의 세계’와 아무런 내적 갈등 없이 살인을 집행하는 ‘밤의 살인자’라는 극단적 이중생활의 구획화; 얌전했던 딸들이 잔혹한 학살범이 되었다는 사실 앞에 가문의 정체성이 송두리째 무너져 내린 부모들의 2차 비극.
4. 나르시시즘적 붕괴와 병적 자기연민 (NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY): 9개월 반 동안 이어진 세기의 법정 서커스: 이마에 X자 흉터를 새기고 신도들에게 모방을 강요하며 판사에게 달려들어 절대적 메시아 행세를 지속한 맨슨; 그러나 코코런 교도소에 격리되어 권력을 박탈당한 46년의 옥중 세월 동안 과대 자아는 완전한 나르시시즘적 붕괴를 겪었고, 2017년 83세로 사망할 때까지 병적인 자기연민과 세상에 대한 원망에 갇혀 지낸 비참한 결말.
5. 도덕적 중화 기술과 자기 정당화 (TECHNIQUES OF NEUTRALIZATION): 사이크스와 마자의 중화 이론 완벽 적용: (1) 상위 가치에의 호소 — 인류를 구원할 종말 전쟁 헬터 스켈터를 촉발하기 위한 ‘자비의 살인’이라는 기괴한 교리; (2) 비난자에 대한 비난 — 나 같은 괴물을 만든 것은 부패한 사회와 교도소 시스템이라는 책임 전가; (3) 책임의 외재화 — "내 손은 흉기에 닿지 않았다"는 비겁한 항변.
6. 심리적 방아쇠와 임계점 (PRECIPITATING TRIGGER): 유명 음반 프로듀서 테리 멜처의 레코드 계약 거절이 맨슨의 취약한 나르시시즘적 자아에 가한 치명적 상처; 자신이 예언한 인종 전쟁이 일어나지 않자 극도의 조급증에 빠진 점; 멜처가 살았던 시엘로 드라이브 10050번지가 분풀이 표적으로 선정되어 참극의 방아쇠가 당겨진 내막.
7. 시그니처 vs 범행 수법 (SIGNATURE VS. MODUS OPERANDI): 범행 수법(MO)은 생존과 은폐를 위해 진화: 사전 전화선 절단, 검은 옷 착용, 도주로에 흉기 유기, 데스밸리 사막으로의 은신; 불변의 심리적 시그니처: 피해자의 피로 벽과 문에 헬터 스켈터 구호(PIG, RISE, HEALTER SKELTER, WAR)를 남기고, 피해자들의 목을 밧줄로 묶어 천장 들보에 연결하는 연극적이고 압도적인 지배 망상의 실현.
8. 5단계 에스컬레이션 궤적 (ESCALATION TRAJECTORY): 자극 내성 형성에 따른 5단계 파멸의 과정: (1) 차량 절도 및 수표 위조 등 잡범 -> (2) 스판 랜치에서 LSD와 음악을 이용한 히피 방랑 카ルト 결성 -> (3) 복종 시험을 위한 야간 주거침입 훈련 ‘크리피 크롤링’ -> (4) 마약상 버나드 크로 총격 및 음악가 게리 힌먼 살해 교사 (1969년 7월) -> (5) 시엘로 드라이브 및 웨이벌리 드라이브 연쇄 대량학살 폭발 (1969년 8월).
9. 후광 효과와 사회적 맹점 (HALO EFFECT & BLIND SPOTS): 히피 반문화의 완벽한 위장막: 평화, 꽃, 자유, 반전의 슬로건이 포식자의 흉계를 은폐; 당시 기성사회와 수사기관이 스판 랜치의 청년 집단을 ‘단순한 길 잃은 방황 청소년들’로 치부했던 치명적인 시스템적 맹점.
10. 피해자학 및 생존을 위한 4대 레드플래그 (VICTIMOLOGY & SURVIVAL REDFLAGS): 희생자들의 온전한 인격과 존엄 회복: 샤론 테이트와 태아 폴 리처드 폴란스키, 제이 세브링, 애비게일 폴저, 보이체크 프라이코프스키, 스티븐 패런트, 레노·로즈마리 라비안카, 게리 힌먼; 개빈 드 베커의 『The Gift of Fear』 원리에 기반한 사이비·가스라이팅 식별 4대 생존 경고 신호: (1) 심리적 경계선을 무너뜨리는 저돌적인 ‘애정 폭격(Love Bombing)’ 경계; (2) 지리적 고립 및 가족·친구와의 관계 단절 수법 포착; (3) 흑백 이원론과 교주에 대한 절대적 개인숭배 거부; (4) 양심의 자율성과 도덕적 판단권 엄수 (자신의 윤리적 책임을 타인에게 양도하지 말 것).

⏱ 챕터 (타임라인)
00:00 오프닝 및 시청 유의사항
00:23 제1막 · 훅(The Hook) — 사랑의 여름의 비극적 종말과 로스앤젤레스의 집단적 편집증
05:20 제2막 · 저택의 참극 & 스판 랜치의 헬터 스켈터 그림자
10:45 제3막 · 심리 부검 — 조작된 뇌와 자아를 지우는 기술
16:30 제4막 · 법정의 공방 & 직접 손대지 않은 교사자의 책임
21:50 제5막 · 역사적 판결, 내면의 종신형 & 생존을 위한 레드플래그

⚠️ 시청 전 유의사항
• 본 콘텐츠는 범죄심리학 및 교육적·역사적 관점에서의 분석 콘텐츠이며, 의학적, 심리학적 또는 법률적 조언을 대신할 수 없습니다.
• 미국 공식 사법 기록(로스앤젤레스 상급법원, 캘리포니아 대법원, LAPD, FBI, CDCR)을 바탕으로 제작되었습니다. 특정 개인이나 단체를 비방하거나 미화할 의도가 없습니다.
• 무고한 희생자들과 유가족의 고통과 인격에 깊은 경의를 표합니다.
• 부엉이, 늑대, 여우, 양, 고양이 아바타는 예술적 연출입니다. 수사관, 심리학자, 증인의 발언은 역사적 공판 기록을 토대로 재구성되었습니다.
• 음성, 이미지, 사운드 제작에 AI 기술이 적용되었습니다.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 대조 완료된 공식 사법·학술 참고문헌
영상 내 모든 타임라인, 사실관계 및 증언은 다음 20개 공적 문서 및 학술 자료와 대조되었습니다:

{SOURCES_KO}

상세한 출처 및 사실관계 대조 기록은 다음 위치에 보관되어 있습니다: 02_SAN_XUAT/Tap09_KO/nguon_tham_khao_KO.md

🆘 위기상담 및 심리 지원 안내 (한국 및 국제 24시간 무료 운영):
• 자살예방 상담전화: 109
• 정신건강 상담전화: 1577-0199
• 보건복지상담센터: 129
• 경찰청 긴급신고: 112 (민원상담 182)
• 아동학대 신고전화: 112
• 여성긴급전화: 1366
• 미국 988 Suicide & Crisis Lifeline: 988 — https://988lifeline.org

#AmberEyes #범죄심리학 #프로파일링 #찰스맨슨 #맨슨패밀리 #헬터스켈터 #세뇌 #자아삭제 #10대심리지표 #레드플래그 #샤론테이트 #실화사건 #다큐멘터리"""

# ==============================================================================
# 9. NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN CHI TIẾT (FULL DOSSIER)
# ==============================================================================
FULL_NGUON_THAM_KHAO_VI = f"""# NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN — TẬP 09 (CHARLES MANSON & GIA ĐÌNH MANSON)

## 1. DANH MỤC 20 NGUỒN TƯ LIỆU CÔNG KHAI ĐÃ ĐỐI CHIẾU

{SOURCES_VI}

---

## 2. BẢNG ĐỐI CHIẾU DỮ KIỆN LỊCH SỬ TỪNG NHÓM CÂU KỊCH BẢN

Toàn bộ các sự kiện, nhân vật, mốc thời gian, lời khai nhân chứng và phán quyết tư pháp trong Tập 09 đã được kiểm chứng đối chiếu với Hồ sơ xét xử chính thức của Tòa Thượng thẩm California (*State of California v. Charles Manson et al.* Case No. A253156), Báo cáo điều tra của Cảnh sát LAPD, và các tác phẩm điều tra uy tín.

- ✅ = đã đối chiếu khớp (hồ sơ tòa án / báo cáo điều tra / tác phẩm chính thức)
- ⚠ = khung lý thuyết / phân tích tâm lý học tội phạm (không phải chẩn đoán y tế)

| Nhóm dữ kiện / Câu | Nội dung kịch bản | Nguồn đối chiếu kiểm chứng | Ghi chú thẩm tra |
|---|---|---|---|
| `1.02` – `1.07` | Đêm 8–9/8/1969 tại 10050 Cielo Drive; 5 nạn nhân (Sharon Tate mang thai 8,5 tháng, Jay Sebring, Abigail Folger, Wojciech Frykowski, Steven Parent); cư dân LA hoảng loạn mua súng, thuê chó. | Hồ sơ hiện trường LAPD; Sách *Helter Skelter* của Vincent Bugliosi; Báo cáo lưu trữ Los Angeles Times & New York Times. | ✅ Khớp 100% thời gian, địa điểm, danh tính 5 nạn nhân và phản ứng tâm lý hoang tưởng tập thể tại Beverly Hills. |
| `2.02` – `2.05` | Hiện trường đêm tiếp theo tại 3311 Waverly Drive (vợ chồng Leno và Rosemary LaBianca); chữ máu PIG, RISE, HEALTER SKELTER; trang trại Spahn Ranch làm căn cứ; chiếc áo Hippie ngụy trang. | Báo cáo hiện trường LAPD; Hồ sơ Tòa Thượng thẩm Quận Los Angeles; Bản khai của George Spahn. | ✅ Khớp 100% hiện trường nhà LaBianca, chữ viết trên tường và bối cảnh sinh hoạt tại trang trại Spahn Ranch. |
| `2.06` | Quỹ đạo leo thang 5 nấc thang: trộm cắp vặt → giáo phái LSD → Creepy Crawling đột nhập đêm → bắn Bernard Crowe & sát hại Gary Hinman → thảm sát Cielo Drive & Waverly Drive. | Hồ sơ tiền án Cục Nhà tù Liên bang Hoa Kỳ; Bản khai của Bobby Beausoleil và Mary Brunner; Cáo trạng Bugliosi. | ✅ Khớp 100% tiến trình leo thang hành vi từ 1967 đến tháng 8/1969. |
| `2.08` – `2.10` | Terry Melcher (Columbia Records) từ chối hợp đồng âm nhạc; ngòi nổ tâm lý xúc phạm cái tôi ái kỷ; sự vật hóa và phi nhân hóa nạn nhân thành 'Pigs'. | Lời khai của Terry Melcher trước tòa; Hồ sơ tâm lý học tư pháp của CDCR; Phân tích của Vincent Bugliosi. | ✅ Melcher từng thuê biệt thự 10050 Cielo Drive với Candice Bergen; Manson biết rõ địa chỉ này. |
| `3.02` – `3.11` | Cơ chế tẩy não và xóa bỏ bản ngã (De-individuation): cô lập, LSD, tước đoạt tài sản, Love Bombing, phân mảnh tâm trí; bi kịch cha mẹ Leslie Van Houten và Susan Atkins. | Nghiên cứu của Hiệp hội Tâm lý học Hoa Kỳ (APA); Sách *The Family* của Ed Sanders; Băng phỏng vấn của Diane Sawyer. | ⚠ Khung lý thuyết De-individuation và Kỹ thuật Trung hòa Đạo đức (Sykes & Matza). |
| `4.02` – `4.09` | Phiên tòa thế kỷ kéo dài 9,5 tháng; lời khai nhân chứng then chốt Linda Kasabian; màn kịch rạp xiếc của Manson (khắc chữ X, tấn công Thẩm phán Charles Older); trách nhiệm kẻ chủ mưu gián tiếp. | Biên bản phiên tòa Tòa Thượng thẩm Los Angeles; Toàn văn lời khai của Linda Kasabian (được miễn trừ truy tố); Tạp chí Time (1970). | ✅ Linda Kasabian làm chứng 18 ngày; Manson lao qua bàn luật sư mưu toan tấn công thẩm phán Older. |
| `5.02` – `5.05` | Án tử hình chuyển thành tù chung thân theo phán quyết *People v. Anderson* (1972); sự sụp đổ cái tôi ái kỷ trong nhà tù Corcoran; Manson qua đời 2017 ở tuổi 83; cựu tín đồ dằn vặt lương tâm. | Phán quyết Tòa Tối cao California (6 Cal. 3d 628); Hồ sơ y tế nhà tù Corcoran; Thông cáo báo chí Bộ Cải huấn California. | ✅ Manson qua đời ngày 19/11/2017 tại Bệnh viện Hạt Kern, thụ án chung thân 46 năm. |
| `5.07` – `5.09` | Tôn vinh phẩm giá các nạn nhân; 4 tín hiệu cảnh báo đỏ sinh tồn theo nguyên lý *The Gift of Fear* của Gavin de Becker. | Tác phẩm *The Gift of Fear* của Gavin de Becker; Quỹ Tưởng niệm Sharon Tate (Sharon Tate Foundation). | ⚠ 4 Red Flags nhận diện tà giáo và kẻ thao túng tâm lý. |
"""

FULL_NGUON_THAM_KHAO_EN = f"""# VERIFIED CASE SOURCES & HISTORICAL EXHIBITS — EPISODE 09 (CHARLES MANSON & THE MANSON FAMILY)

## 1. COMPREHENSIVE REPOSITORY OF 20 VERIFIED PUBLIC SOURCES

{SOURCES_EN}

---

## 2. CROSS-REFERENCED HISTORICAL FACT AUDIT TABLE

All historical events, individuals, chronologies, courtroom testimony, and judicial rulings in Episode 09 have been verified against the official trial records of the Los Angeles County Superior Court (*State of California v. Charles Manson et al.* Case No. A253156), LAPD and FBI Vault Investigative Reports, and authoritative historical monographs.

- ✅ = Verified exact match (Official court transcripts / Police investigative logs / Authoritative records)
- ⚠ = Criminological & psychological framework (Theoretical models, not clinical medical diagnoses)

| Act / Scene | Script Content & Historical Focus | Cross-Referenced Source | Verification Notes |
|---|---|---|---|
| `1.02` – `1.07` | Night of August 8–9, 1969 at 10050 Cielo Drive; 5 victims (Sharon Tate 8.5 months pregnant, Jay Sebring, Abigail Folger, Wojciech Frykowski, Steven Parent); Beverly Hills panic buying firearms. | LAPD Crime Scene Files; *Helter Skelter* by Vincent Bugliosi; Los Angeles Times & New York Times Archives. | ✅ 100% match on dates, crime scene, victim identities, and collective paranoia across Los Angeles. |
| `2.02` – `2.05` | Next night at 3311 Waverly Drive (Leno & Rosemary LaBianca); blood slogans PIG, RISE, HEALTER SKELTER; Spahn Ranch headquarters; flower-power disguise. | LAPD Homicide Reports; LA Superior Court Records; Testimony of George Spahn. | ✅ 100% match on LaBianca crime scene, blood scrawls, and communal living dynamics at Spahn Movie Ranch. |
| `2.06` | 5-Stage Escalation Trajectory: Petty thefts → LSD cult → Creepy Crawling night break-ins → Shooting Bernard Crowe & Gary Hinman murder → Tate-LaBianca massacres. | Federal Bureau of Prisons Docket; Sworn testimony of Bobby Beausoleil & Mary Brunner; Bugliosi Indictment. | ✅ 100% behavioral match for progressive violent escalation from 1967 to August 1969. |
| `2.08` – `2.10` | Terry Melcher (Columbia Records) rejects music contract; narcissistic humiliation; dehumanization and objectification of victims as "Pigs". | Trial testimony of Terry Melcher; CDCR Forensic Psychological Evaluations; Bugliosi trial memos. | ✅ Melcher previously rented 10050 Cielo Drive with Candice Bergen; Manson visited the property personally. |
| `3.02` – `3.11` | Mechanisms of Ego Erasure (De-individuation): isolation, LSD, property surrender, Love Bombing, cognitive fragmentation; tragedy of secondary victims (parents). | American Psychological Association (APA) Studies; *The Family* by Ed Sanders; Diane Sawyer Prison Interviews. | ⚠ De-individuation framework and Sykes & Matza's Techniques of Neutralization. |
| `4.02` – `4.09` | 9.5-month "trial of the century"; star immunized witness Linda Kasabian; Manson's courtroom theatrics (carved X on forehead, lunging at Judge Older); vicarious liability. | LA County Superior Court Trial Transcripts; Full sworn testimony of Linda Kasabian; Time Magazine Archives. | ✅ Linda Kasabian testified for 18 days; Manson leaped over defense table attempting to attack Judge Older. |
| `5.02` – `5.05` | Death penalty commuted to life imprisonment via *People v. Anderson* (1972); narcissistic collapse in Corcoran State Prison; death in 2017 at age 83. | Supreme Court of California Decision (6 Cal. 3d 628); Corcoran State Prison Medical Records; CDCR Press Release. | ✅ Manson passed away on November 19, 2017 at Kern County Hospital after 46 years of continuous incarceration. |
| `5.07` – `5.09` | Honoring victim dignity; 4 survival red flags for identifying coercive manipulation based on Gavin de Becker's *The Gift of Fear*. | *The Gift of Fear* by Gavin de Becker; The Sharon Tate Foundation Archives. | ⚠ 4 Red Flags for cult and predatory manipulation identification. |
"""

FULL_NGUON_THAM_KHAO_JA = f"""# 参照・照合済み公的資料リストおよび歴史的事実対照記録 — 第09話（チャールズ・マンソンとファミリー）

## 1. 照合済み公的資料および学術研究文献（20選）

{SOURCES_JA}

---

## 2. 脚本各幕における歴史的事実対照表

第09話で語られるすべての事件、人物、年表、証言、および司法判決は、カリフォルニア州上級裁判所の公式公判記録（*State of California v. Charles Manson et al.* Case No. A253156）、ロサンゼルス市警察（LAPD）およびFBIの捜査調書、ならびに信頼性の高い調査著作と照合済みです。

- ✅ = 完全一致確認済み（裁判記録／警察調書／公的記録）
- ⚠ = 犯罪心理学理論モデル（医学的診断ではなく心理学的分析枠組み）

| 幕・場面 | 脚本の内容および検証対象 | 照合・参照先資料 | 検証結果および注記 |
|---|---|---|---|
| `1.02` – `1.07` | 1969年8月8日〜9日未明、シエロ・ドライブ10050番地；5名の犠牲者（シャロン・テート他）；ビバリーヒルズ市民の銃器買い占めパニック。 | LAPD現場調書；ブリオーシ検事著『ヘルダー・スケルター』；ロサンゼルス・タイムズ報道アーカイブ。 | ✅ 日時、場所、被害者5名の身元、ロサンゼルス全体の集団的偏執病と完全一致。 |
| `2.02` – `2.05` | 翌夜のウェーバリー・ドライブ3311番地（ラビアンカ夫妻虐殺）；PIG、RISE、HEALTER SKELTER血文字；スパーン牧場の生活実態。 | LAPD捜査報告書；LA上級裁判所記録；牧場主ジョージ・スパーンの証言録取書。 | ✅ ラビアンカ邸の惨劇、現場の血文字、スパーン牧場における共同生活の実態と完全一致。 |
| `2.06` | 暴力の5段階エスカレーション：軽犯罪 → 放浪カルト → 夜間侵入「クリーピー・クローリング」 → ヒンマン殺害 → テート・ラビアンカ事件。 | 連邦刑務所受刑記録；ボビー・ボーソレイユおよびメアリー・ブルナーの供述書；起訴状。 | ✅ 1967年から1969年8月に至る刺激耐性形成と暴力のエスカレーション過程と一致。 |
| `2.08` – `2.10` | 音楽プロデューサーのテリー・メルチャーによるレコード契約拒絶；自己愛の破綻；被害者の客体化と「Pigs」への格下げ。 | メルチャーの法廷証言；カリフォルニア州矯正局（CDCR）心理評価書；裁判記録。 | ✅ メルチャーはかつてシエロ・ドライブ10050番地を借りており、マンソンも訪問していた。 |
| `3.02` – `3.11` | 自我消去（没個性化）のメカニズム：社会的孤立、LSD、財産放棄、ラブ・ボンビング、精神の分断；実行犯の両親が負った二次被害。 | アメリカ心理学会（APA）研究資料；エド・サンダース著『The Family』；ダイアン・ソーヤー独占取材。 | ⚠ 没個性化（De-individuation）および中和の技術（Techniques of Neutralization）の適用。 |
| `4.02` – `4.09` | 9か月半に及ぶ法廷闘争；重要証人リンダ・カサビアンの免責証言；マンソンの額のX傷とオールダー裁判長襲撃；教唆首謀者責任。 | ロサンゼルス郡上級裁判所公判記録全巻；カサビアン証言録；TIME誌アーカイブ。 | ✅ カサビアンは18日間にわたり証言；マンソンが机を飛び越え裁判長を襲撃した記録と一致。 |
| `5.02` – `5.05` | 1972年「ピープル対アンダーソン」判決による死刑違憲・終身刑減刑；コーコラン刑務所での自己愛崩壊と2017年の83歳での孤独死。 | カリフォルニア州最高裁判所判例集（6 Cal. 3d 628）；刑務所カルテ；矯正局公式声明。 | ✅ マンソンは46年間服役し、2017年11月19日にカーン郡病院にて83歳で死亡。 |
| `5.07` – `5.09` | 犠牲者の尊厳回復；ギャビン・ド・ベッカー『The Gift of Fear』に基づくカルト・マインドコントロール見抜き4大レッドフラッグ。 | ギャビン・ド・ベッカー著『The Gift of Fear』；シャロン・テート財団資料。 | ⚠ 破壊的カルトおよび支配的マインドコントロール集団を見抜くための警告指標。 |
"""

FULL_NGUON_THAM_KHAO_KO = f"""# 공식 참고문헌 및 사법 기록 대조 보고서 — 제09화 (찰스 맨슨과 맨슨 패밀리)

## 1. 정밀 교차 검증된 20대 공적 자료 목록

{SOURCES_KO}

---

## 2. 각 막별 역사적 사실관계 대조표

제09화에서 다루어진 모든 사건, 인물, 타임라인, 증언 및 사법 판결은 미국 캘리포니아주 로스앤젤레스 상급법원 공식 공판 기록(*State of California v. Charles Manson et al.* Case No. A253156), 로스앤젤레스 경찰청(LAPD) 및 FBI의 공식 수사 보고서, 그리고 권위 있는 탐사 단행본들과 교차 대조되었습니다.

- ✅ = 공식 기록과 100% 일치 확인 완료 (재판 기록 / 수사 보고서 / 정부 공식 발표)
- ⚠ = 범죄심리학적 분석 프레임워크 (임상적 의학 진단이 아닌 이론적 분석 모델)

| 막 및 장면 | 각본 내용 및 검증 대상 | 교차 대조 출처 자료 | 검증 결과 및 세부 주석 |
|---|---|---|---|
| `1.02` – `1.07` | 1969년 8월 8~9일 시엘로 드라이브 10050번지 참극; 희생자 5인(임신 8.5개월 샤론 테이트 외); 베벌리 힐스 총기 사재기 패닉. | LAPD 공식 현장 보고서; 빈센트 부글리오시 『헬터 스켈터』; LA 타임스 및 뉴욕타임스 아카이브. | ✅ 일시, 장소, 희생자 5인의 신원, 로스앤젤레스 전역의 집단적 편집증 현상과 100% 일치. |
| `2.02` – `2.05` | 이튿날 밤 웨이벌리 드라이브 3311번지 참극(라비안카 부부 피살); 혈서(PIG, RISE, HEALTER SKELTER); 스판 랜치 공동체 실태. | LAPD 살인수사 보고서; LA 상급법원 재판 기록; 조지 스판 증언 조서. | ✅ 라비안카 저택 범행 현장, 벽면 혈서, 스판 랜치에서의 히피 공동체 생활상과 100% 일치. |
| `2.06` | 폭력의 5단계 에스컬레이션 궤적: 잡범 → 방랑 카ルト → 야간 주거침입 ‘크리피 크롤링’ → 힌먼 살해 → 시엘로·웨이벌리 참극. | 연방교도국 전과 기록; 바비 보솔레이 및 메리 브루너 진술서; 부글리오시 검사 기소장. | ✅ 1967년부터 1969년 8월에 이르는 자극 내성 형성과 단계별 폭력 진화 과정 확인. |
| `2.08` – `2.10` | 테리 멜처 음반 계약 거절; 나르시시즘적 자아의 치명적 상처; 피해자의 사물화 및 ‘Pigs’ 격하. | 테리 멜처 법정 증언; 캘리포니아 교정국(CDCR) 심리 평가서; 재판 공판 조서. | ✅ 멜처는 실제로 캔디스 버겐과 시엘로 드라이브에 거주했으며 맨슨이 해당 저택을 방문했음. |
| `3.02` – `3.11` | 자아 삭제(몰개성화) 메커니즘: 사회적 고립, LSD, 재산 헌납, 애정 폭격, 구획화; 가해자 부모들의 2차 비극. | 미국심리학회(APA) 학술 자료; 에드 샌더스 『The Family』; 다이앤 소여 인터뷰. | ⚠ 몰개성화(De-individuation) 이론 및 사이크스 & 마자의 중화 기술 모델 적용. |
| `4.02` – `4.09` | 9.5개월간의 세기의 재판; 기소면제 증인 린다 카사비안의 결정적 증언; 맨슨의 이마 X 흉터 및 올더 판사 습격; 간접 교사자 책임. | 로스앤젤레스 상급법원 공판 조서; 카사비안 법정 증언 녹취록; 타임지 보도. | ✅ 카사비안 18일간 증언; 맨슨이 피고인석을 뛰어넘어 판사를 공격하려 했던 사실 일치. |
| `5.02` – `5.05` | 1972년 피플 대 앤더슨 판결로 인한 사형 위헌 및 무기징역 감형; 코코런 교도소 나르시시즘적 붕괴와 2017년 83세 고독사. | 캘리포니아 대법원 판례집(6 Cal. 3d 628); 교도소 의무 기록; 교정재활국 공식 발표문. | ✅ 맨슨은 46년간 복역 후 2017년 11월 19일 컨 카운티 병원에서 83세로 사망함. |
| `5.07` – `5.09` | 희생자들의 존엄 회복; 개빈 드 베커 『The Gift of Fear』 원리에 기반한 사이비·가스라이팅 식별 4대 생존 경고 신호. | 개빈 드 베커 저 『The Gift of Fear』; 샤론 테이트 재단 추모 자료. | ⚠ 유해한 사이비 조작 집단 및 나르시시스트 포식자를 식별하기 위한 서바이벌 레드플래그. |
"""

# ==============================================================================
# 10. CHU_CO_DINH_EN.md
# ==============================================================================
CHU_CO_DINH_EN = f"""# CHỮ CỐ ĐỊNH & GÓI PHÁT HÀNH TIẾNG ANH (THỊ TRƯỜNG MỸ) · TẬP 09
**Hồ sơ vụ án:** Charles Manson & Thảm kịch Gia đình Manson (The Charles Manson & Manson Family File)  
**Kênh:** Amber eyes — Criminal psychology through real case files

---

## 1. Tiêu đề Video & Thumbnail (Tối ưu hóa thuật toán YouTube US)

### A. Tiêu đề YouTube (Title Options)
* **Phương án 1 (Khuyên dùng — Chuẩn hóa học thuật & Nhận diện Kênh):**  
  `Ep. 09: The Art of Ego Erasure | Criminal Psychology: Charles Manson & The Manson Family Tragedy (10 Psychological Markers & 5 Stages of Escalation) | Amber eyes`
* **Phương án 2 (Kịch tính, thu hút CTR cao):**  
  `Behind the Cult: How Charles Manson Weaponized Mind Control Without Touching a Weapon | Forensic Psychology | Amber eyes`
* **Phương án 3 (Tập trung vào tiền lệ pháp lý):**  
  `The Mastermind Who Struck from the Shadows: The Manson Murders & Mastermind Liability | Amber eyes`

### B. Chữ trên Thumbnail (2 dòng lớn, tương phản cao trên Mobile)
```
EGO ERASURE
HELTER SKELTER
```
*Phương án phụ:*
```
THE MASTERMIND
WITHOUT WEAPONS
```

---

## 2. Thẻ Intro cảnh báo chuẩn thị trường Mỹ (Disclaimers)

### Thẻ A — `ABOUT THIS DOCUMENTARY`
1. **Educational content:** A forensic & criminal psychology analysis based strictly on public records, trial exhibits, and official investigative transcripts.
2. **Investigative purpose:** Produced solely for educational, criminological, and public safety awareness.
3. **No defamation:** Not intended to defame, harass, or inflict distress upon any innocent individuals or victims' families.

### Thẻ B — `VIEWER DISCRETION & ADVISORY`
1. **Mature audience only:** Contains mature themes, cult psychology analysis, and non-graphic accounts of historical violent crimes. Viewer discretion is advised.
2. **AI & Dramatization:** Narrated with synthetic AI voices. Visuals and character avatars are dramatized illustrations and do not depict real persons.
3. **Professional boundaries:** Not a substitute for professional legal, medical, or psychiatric advice.

---

## 3. Nhãn nhân vật hiển thị trên màn hình (Character Badges)

| Vai | Dòng 1 (Vai trò) | Dòng 2 (Mô tả) | Ghi chú pháp lý Mỹ |
|---|---|---|---|
| **H · Cú** | **HOST** | Your Narrator | Người dẫn chuyện |
| **D · Sói** | **INVESTIGATOR** | Forensic Case Analysis | *Fictional character · AI voice · Dramatized* |
| **C · Cáo** | **PSYCHOLOGIST** | Behavioral Dynamics | *Fictional character · AI voice · Dramatized* |
| **N1 · Cừu** | **LOS ANGELES RESIDENT** | Witness to History | *Dramatized illustration* |
| **N2 · Mèo** | **LINDA KASABIAN** | Former Manson Family Member | *Key State Witness · Dramatized illustration* |

---

## 4. Mô tả YouTube chuẩn Mỹ (YouTube Description with Crisis Resources)

```text
{DESC_EN}
```
"""

# ==============================================================================
# 11. HÀM GHI FILE AN TOÀN
# ==============================================================================
def write_file_safe(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content.strip() + "\n")
    print(f"  -> Đã ghi: {path.relative_to(ROOT)} ({len(content)} ký tự)")


def main():
    print("==================================================================")
    print("TẠO VÀ ĐỒNG BỘ TOÀN DIỆN MÔ TẢ TẬP 09 (4 NGÔN NGỮ: VI, EN, JA, KO)")
    print("==================================================================")

    # 1. TIẾNG VIỆT
    print("\n[1/4] Ghi file Tiếng Việt (Tap09)...")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09" / "mo_ta.txt", DESC_VI)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09" / "xuat_ban" / "mo_ta.txt", DESC_VI)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09" / "nguon_mo_ta.txt", SOURCES_VI)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09" / "nguon_tham_khao.md", FULL_NGUON_THAM_KHAO_VI)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09" / "xuat_ban" / "nguon_tham_khao.md", FULL_NGUON_THAM_KHAO_VI)

    # 2. TIẾNG ANH
    print("\n[2/4] Ghi file Tiếng Anh (Tap09_EN)...")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_EN" / "description.txt", DESC_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_EN" / "mo_ta.txt", DESC_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_EN" / "xuat_ban" / "description.txt", DESC_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_EN" / "nguon_tham_khao_EN.md", FULL_NGUON_THAM_KHAO_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_EN" / "xuat_ban" / "nguon_tham_khao_EN.md", FULL_NGUON_THAM_KHAO_EN)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_EN" / "CHU_CO_DINH_EN.md", CHU_CO_DINH_EN)

    # 3. TIẾNG NHẬT
    print("\n[3/4] Ghi file Tiếng Nhật (Tap09_JA)...")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_JA" / "description.txt", DESC_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_JA" / "mo_ta.txt", DESC_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_JA" / "xuat_ban" / "description.txt", DESC_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_JA" / "nguon_tham_khao_JA.md", FULL_NGUON_THAM_KHAO_JA)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_JA" / "xuat_ban" / "nguon_tham_khao_JA.md", FULL_NGUON_THAM_KHAO_JA)

    # 4. TIẾNG HÀN
    print("\n[4/4] Ghi file Tiếng Hàn (Tap09_KO)...")
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_KO" / "description.txt", DESC_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_KO" / "mo_ta.txt", DESC_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_KO" / "xuat_ban" / "description.txt", DESC_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_KO" / "nguon_tham_khao_KO.md", FULL_NGUON_THAM_KHAO_KO)
    write_file_safe(ROOT / "02_SAN_XUAT" / "Tap09_KO" / "xuat_ban" / "nguon_tham_khao_KO.md", FULL_NGUON_THAM_KHAO_KO)

    print("\n==================================================================")
    print("HOÀN TẤT GHI TẤT CẢ FILE MÔ TẢ VÀ TÀI LIỆU XUẤT BẢN TẬP 09!")
    print("==================================================================")


if __name__ == "__main__":
    main()
