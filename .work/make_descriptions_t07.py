#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo và cập nhật mô tả video đạt chuẩn Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cho Tập 07 trên cả 4 ngôn ngữ (VI, EN, JA, KO)."""

import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# 1. NGUỒN TIẾNG VIỆT
# ==============================================================================
SOURCES_VI = """▸ Hồ sơ vụ án & bản án tư pháp:
• [1] Tòa Tối cao Massachusetts — hồ sơ phúc thẩm vụ án Commonwealth v. Michelle Carter (nguyên văn trích xuất tin nhắn số):
  https://www.supremecourt.gov/DocketPDF/19/19-62/107409/20190708155645613_Michelle%20Carter%20Appendix%20July%208%202019%20EFile.pdf
• [2] Wikipedia — Toàn cảnh vụ án cái chết của Conrad Roy III:
  https://en.wikipedia.org/wiki/Death_of_Conrad_Roy
• [3] Associated Press (AP) — Tòa án Tối cao Massachusetts giữ nguyên phán quyết có tội (2019):
  https://apnews.com/abd449bd66274f698e9ff4d4c2247a8e

▸ Báo chí & điều tra chuyên sâu:
• [4] CBS News — 'Death by Text': hồ sơ điều tra chi tiết và nguyên văn đối thoại:
  https://www.cbsnews.com/news/death-by-text-the-case-against-michelle-carter/
• [5] Courthouse News Service — Mức án và lập luận pháp lý của Thẩm phán Lawrence Moniz:
  https://www.courthousenews.com/woman-convicted-urging-boyfriends-suicide-gets-2-%C2%BD-years/
• [6] Esquire — 'The Girl From Plainville' (phóng sự điều tra tâm lý chuyên sâu của Jesse Barron):
  https://www.esquire.com/news-politics/a57125/michelle-carter-trial/
• [7] MassLive — Tuyên án Michelle Carter phạm tội ngộ sát không tự nguyện:
  https://www.masslive.com/news/index.ssf/2017/06/michelle_carter_found_guilty_i.html
• [8] MassLive — Trích xuất tin nhắn tự thú gửi bạn học Samantha Boardman:
  https://www.masslive.com/news/2017/06/michelle_carter_trial_breakout.html
• [9] NBC News — Phán quyết bước ngoặt và chiếc xe bán tải Ford F-250:
  https://www.nbcnews.com/news/us-news/michelle-carter-found-guilty-encouraging-boyfriend-s-suicide-text-messages-n773306
• [10] The New York Times — Bản án ngày 16/06/2017 và tiền lệ pháp lý không gian số:
  https://www.nytimes.com/2017/06/16/us/suicide-texting-trial-michelle-carter-conrad-roy.html
• [11] People Magazine — Lời khai của bác sĩ tâm thần Peter Breggin về thuốc Celexa:
  https://people.com/crime/teen-accused-of-urging-boyfriends-suicide-took-meds-that-hurt-her-ability-to-empathize-psychiatrist/
• [12] The Standard-Times (SouthCoast Today) — Báo cáo điều tra hiện trường của Thám tử Scott Gordon:
  https://www.southcoasttoday.com/story/news/crime/2015/02/27/police-teen-coaxed-friend-to/35089861007/
• [13] Boston.com — Tổng quan hồ sơ Michelle Carter & Conrad Roy:
  https://www.boston.com/culture/entertainment/2022/03/29/the-girl-from-plainville-hulu-series-michelle-carter/
• [14] CNN — Phán quyết lịch sử kết tội Michelle Carter (16/06/2017):
  https://www.cnn.com/2017/06/16/us/michelle-carter-texting-case/index.html
• [15] CNN — Phiên tòa tuyên mức án và lệnh thi hành (03/08/2017):
  https://www.cnn.com/2017/08/03/us/michelle-carter-texting-suicide-sentencing/index.html

▸ Đạo luật Conrad & cải cách pháp chế:
• [16] Boston.com — Chiến dịch khởi xướng Đạo luật Conrad (24/07/2019):
  https://www.boston.com/news/politics/2019/07/25/conrads-law/
• [17] Quốc hội Bang Massachusetts (The 192nd General Court) — Toàn văn dự luật Thượng viện S.1032:
  https://malegislature.gov/Bills/192/S1032.pdf
• [18] WBUR News — Phiên điều trần Ủy ban Tư pháp về luật hình sự hóa xúi giục tự hại:
  https://www.wbur.org/news/2019/11/12/massachusetts-legislation-suicide-text-case
• [19] CBS Boston — Bà Lynn Roy và nỗ lực bảo vệ thanh thiếu niên qua Đạo luật Conrad:
  https://www.cbsnews.com/boston/news/conrad-roy-bill-law-suicide-michelle-carter/

▸ Nghiên cứu tâm lý học & thao túng hành vi:
• [20] Scamwatch (Ủy ban Cạnh tranh và Người tiêu dùng Úc ACCC) — Cơ chế leo thang cam kết (Escalation of Commitment):
  https://www.scamwatch.gov.au/stop-check-protect/help-someone-whos-being-scammed/understanding-how-scammers-manipulate-your-loved-one
• [21] National Library of Medicine (StatPearls / NCBI) — Munchausen by Internet và hội chứng tạo bệnh giả trực tuyến:
  https://www.ncbi.nlm.nih.gov/books/NBK518999/"""

# ==============================================================================
# 2. NGUỒN TIẾNG ANH
# ==============================================================================
SOURCES_EN = """▸ Official Court Records & Legal Documents:
• [1] Supreme Judicial Court of Massachusetts — Commonwealth v. Michelle Carter (Official Forensic Appendix & Text Transcripts):
  https://www.supremecourt.gov/DocketPDF/19/19-62/107409/20190708155645613_Michelle%20Carter%20Appendix%20July%208%202019%20EFile.pdf
• [2] Wikipedia — Death of Conrad Roy III (Case Overview & Timeline):
  https://en.wikipedia.org/wiki/Death_of_Conrad_Roy
• [3] Associated Press (AP) — Massachusetts Highest Court Upholds Involuntary Manslaughter Conviction (2019):
  https://apnews.com/abd449bd66274f698e9ff4d4c2247a8e

▸ Investigative Journalism & News Coverage:
• [4] CBS News — 'Death by Text': Complete Investigative Docket & Transcript Archive:
  https://www.cbsnews.com/news/death-by-text-the-case-against-michelle-carter/
• [5] Courthouse News Service — Sentencing Proceedings & Judge Lawrence Moniz's Ruling:
  https://www.courthousenews.com/woman-convicted-urging-boyfriends-suicide-gets-2-%C2%BD-years/
• [6] Esquire — 'The Girl From Plainville' (Definitive Psychological Investigation by Jesse Barron):
  https://www.esquire.com/news-politics/a57125/michelle-carter-trial/
• [7] MassLive — Michelle Carter Found Guilty of Involuntary Manslaughter:
  https://www.masslive.com/news/index.ssf/2017/06/michelle_carter_found_guilty_i.html
• [8] MassLive — Forensic Text Extractions & Confession Messages to Samantha Boardman:
  https://www.masslive.com/news/2017/06/michelle_carter_trial_breakout.html
• [9] NBC News — The Landmark Verdict and the Ford F-250 Crime Scene:
  https://www.nbcnews.com/news/us-news/michelle-carter-found-guilty-encouraging-boyfriend-s-suicide-text-messages-n773306
• [10] The New York Times — Verdict Analysis (June 16, 2017) & The Digital Precedent:
  https://www.nytimes.com/2017/06/16/us/suicide-texting-trial-michelle-carter-conrad-roy.html
• [11] People Magazine — Psychiatric Testimony of Dr. Peter Breggin on Celexa Medication:
  https://people.com/crime/teen-accused-of-urging-boyfriends-suicide-took-meds-that-hurt-her-ability-to-empathize-psychiatrist/
• [12] The Standard-Times (SouthCoast Today) — Lead Detective Scott Gordon's Investigative Report:
  https://www.southcoasttoday.com/story/news/crime/2015/02/27/police-teen-coaxed-friend-to/35089861007/
• [13] Boston.com — Case Archive: Michelle Carter and the Conrad Roy Tragedy:
  https://www.boston.com/culture/entertainment/2022/03/29/the-girl-from-plainville-hulu-series-michelle-carter/
• [14] CNN — Historic Conviction of Michelle Carter in Groundbreaking Trial (June 16, 2017):
  https://www.cnn.com/2017/06/16/us/michelle-carter-texting-case/index.html
• [15] CNN — Sentencing Hearing and Incarceration Order (August 3, 2017):
  https://www.cnn.com/2017/08/03/us/michelle-carter-texting-suicide-sentencing/index.html

▸ Legislative Reform & Conrad's Law:
• [16] Boston.com — The Legislative Initiative Behind Conrad's Law (July 24, 2019):
  https://www.boston.com/news/politics/2019/07/25/conrads-law/
• [17] The 192nd General Court of Massachusetts — Official Text of Senate Bill S.1032:
  https://malegislature.gov/Bills/192/S1032.pdf
• [18] WBUR News — Judiciary Committee Hearings on Digital Coercion Legislation:
  https://www.wbur.org/news/2019/11/12/massachusetts-legislation-suicide-text-case
• [19] CBS Boston — Lynn Roy's Advocacy for Youth Protection via Conrad's Law:
  https://www.cbsnews.com/boston/news/conrad-roy-bill-law-suicide-michelle-carter/

▸ Behavioral Psychology & Coercive Control:
• [20] Australian Competition & Consumer Commission (Scamwatch) — Escalation of Commitment Mechanisms:
  https://www.scamwatch.gov.au/stop-check-protect/help-someone-whos-being-scammed/understanding-how-scammers-manipulate-your-loved-one
• [21] National Library of Medicine (StatPearls / NCBI) — Munchausen by Internet & Factitious Virtual Attention Seeking:
  https://www.ncbi.nlm.nih.gov/books/NBK518999/"""

# ==============================================================================
# 3. NGUỒN TIẾNG NHẬT
# ==============================================================================
SOURCES_JA = """▸ 公的司法記録および公式裁判資料:
• [1] マサチューセッツ州最高司法裁判所 — マサチューセッツ州対ミシェル・カーター事件（公式押収テキスト記録付録）：
  https://www.supremecourt.gov/DocketPDF/19/19-62/107409/20190708155645613_Michelle%20Carter%20Appendix%20July%208%202019%20EFile.pdf
• [2] Wikipedia — コンラッド・ロイ3世事件（概要と年表）：
  https://en.wikipedia.org/wiki/Death_of_Conrad_Roy
• [3] AP通信 — マサチューセッツ州最高裁が過失致死罪の有罪判決を支持（2019年）：
  https://apnews.com/abd449bd66274f698e9ff4d4c2247a8e

▸ 報道機関および深層調査記録:
• [4] CBS News — 『Death by Text（テキストによる死）』捜査記録およびメッセージ全文：
  https://www.cbsnews.com/news/death-by-text-the-case-against-michelle-carter/
• [5] Courthouse News Service — 量刑公判およびローレンス・モニズ判事による判決理由：
  https://www.courthousenews.com/woman-convicted-urging-boyfriends-suicide-gets-2-%C2%BD-years/
• [6] Esquire — 『プレインビルから来た少女』（ジェシー・バロンによる深層心理ルポルタージュ）：
  https://www.esquire.com/news-politics/a57125/michelle-carter-trial/
• [7] MassLive — ミシェル・カーターに対する過失致死罪有罪判決の詳報：
  https://www.masslive.com/news/index.ssf/2017/06/michelle_carter_found_guilty_i.html
• [8] MassLive — 友人サマンサ・ボードマンへ送信された自白テキスト記録：
  https://www.masslive.com/news/2017/06/michelle_carter_trial_breakout.html
• [9] NBC News — 画期的な有罪判決とフォードF-250の現場検証：
  https://www.nbcnews.com/news/us-news/michelle-carter-found-guilty-encouraging-boyfriend-s-suicide-text-messages-n773306
• [10] ニューヨーク・タイムズ — 2017年6月16日の判決とサイバー空間における司法的先例：
  https://www.nytimes.com/2017/06/16/us/suicide-texting-trial-michelle-carter-conrad-roy.html
• [11] ピープル誌 — ピーター・ブレギン精神科医による抗うつ薬セレクサに関する法廷証言：
  https://people.com/crime/teen-accused-of-urging-boyfriends-suicide-took-meds-that-hurt-her-ability-to-empathize-psychiatrist/
• [12] The Standard-Times — スコット・ゴードン主任捜査官による事件捜査報告書：
  https://www.southcoasttoday.com/story/news/crime/2015/02/27/police-teen-coaxed-friend-to/35089861007/
• [13] Boston.com — ミシェル・カーターとコンラッド・ロイ事件の全貌：
  https://www.boston.com/culture/entertainment/2022/03/29/the-girl-from-plainville-hulu-series-michelle-carter/
• [14] CNN — 歴史的有罪判決の速報（2017年6月16日）：
  https://www.cnn.com/2017/06/16/us/michelle-carter-texting-case/index.html
• [15] CNN — 量刑言渡公判と収監決定（2017年8月3日）：
  https://www.cnn.com/2017/08/03/us/michelle-carter-texting-suicide-sentencing/index.html

▸ 立法改革およびコンラッド法:
• [16] Boston.com — コンラッド法制定に向けた立法キャンペーン（2019年7月24日）：
  https://www.boston.com/news/politics/2019/07/25/conrads-law/
• [17] マサチューセッツ州議会 — 上院法案 S.1032 正式条文：
  https://malegislature.gov/Bills/192/S1032.pdf
• [18] WBUR News — 遠隔煽動・心理的強要を犯罪化する法案に関する司法委員会公聴会：
  https://www.wbur.org/news/2019/11/12/massachusetts-legislation-suicide-text-case
• [19] CBS Boston — リン・ロイ氏によるコンラッド法推進運動：
  https://www.cbsnews.com/boston/news/conrad-roy-bill-law-suicide-michelle-carter/

▸ 行動心理学および心理操作メカニズム:
• [20] オーストラリア競争・消費者委員会（Scamwatch） — コミットメントのエスカレーション理論：
  https://www.scamwatch.gov.au/stop-check-protect/help-someone-whos-being-scammed/understanding-how-scammers-manipulate-your-loved-one
• [21] 米国立衛生研究所（StatPearls / NCBI） — インターネット・ミュンヒハウゼン症候群：
  https://www.ncbi.nlm.nih.gov/books/NBK518999/"""

# ==============================================================================
# 4. NGUỒN TIẾNG HÀN
# ==============================================================================
SOURCES_KO = """▸ 공식 사법 기록 및 법원 판결문:
• [1] 매사추세츠주 대법원 — 매사추세츠주 대 미셸 카터 사건 (공식 디지털 포렌식 부록 및 문자 녹취록):
  https://www.supremecourt.gov/DocketPDF/19/19-62/107409/20190708155645613_Michelle%20Carter%20Appendix%20July%208%202019%20EFile.pdf
• [2] Wikipedia — 콘래드 로이 3세 사망 사건 개요 및 타임라인:
  https://en.wikipedia.org/wiki/Death_of_Conrad_Roy
• [3] AP통신 — 매사추세츠주 최고법원, 과실치사 유죄 판결 최종 확정 (2019년):
  https://apnews.com/abd449bd66274f698e9ff4d4c2247a8e

▸ 언론 심층 탐사 보도 및 인터뷰:
• [4] CBS News — 'Death by Text': 사건 종합 수사 기록 및 메시지 전문 아카이브:
  https://www.cbsnews.com/news/death-by-text-the-case-against-michelle-carter/
• [5] Courthouse News Service — 선고 공판 및 로런스 모니즈 판사의 법리적 판결 이유:
  https://www.courthousenews.com/woman-convicted-urging-boyfriends-suicide-gets-2-%C2%BD-years/
• [6] 에스콰이어 — 《플레인빌에서 온 소녀》(제시 배런 기자의 심층 심리 탐사 보도):
  https://www.esquire.com/news-politics/a57125/michelle-carter-trial/
• [7] MassLive — 미셸 카터 과실치사 유죄 판결 상세 분석:
  https://www.masslive.com/news/index.ssf/2017/06/michelle_carter_found_guilty_i.html
• [8] MassLive — 친구 서맨사 보드먼에게 보낸 자백 문자 메시지 포렌식 기록:
  https://www.masslive.com/news/2017/06/michelle_carter_trial_breakout.html
• [9] NBC News — 기념비적 판결과 포드 F-250 픽업트럭 현장 수사:
  https://www.nbcnews.com/news/us-news/michelle-carter-found-guilty-encouraging-boyfriend-s-suicide-text-messages-n773306
• [10] 뉴욕타임스 — 2017년 6월 16일 유죄 판결과 사이버 시대의 사법 선례:
  https://www.nytimes.com/2017/06/16/us/suicide-texting-trial-michelle-carter-conrad-roy.html
• [11] 피플지 — 피터 브레긴 정신과 전문의의 항우울제 셀렉사 관련 법정 증언:
  https://people.com/crime/teen-accused-of-urging-boyfriends-suicide-took-meds-that-hurt-her-ability-to-empathize-psychiatrist/
• [12] The Standard-Times — 스콧 고든 주임 수사관의 현장 수사 보고서:
  https://www.southcoasttoday.com/story/news/crime/2015/02/27/police-teen-coaxed-friend-to/35089861007/
• [13] Boston.com — 미셸 카터와 콘래드 로이 사건 종합 파일:
  https://www.boston.com/culture/entertainment/2022/03/29/the-girl-from-plainville-hulu-series-michelle-carter/
• [14] CNN — 미셸 카터 역사적 유죄 선고 생중계 보도 (2017년 6월 16일):
  https://www.cnn.com/2017/06/16/us/michelle-carter-texting-case/index.html
• [15] CNN — 양형 선고 공판 및 수감 명령 집행 (2017년 8월 3일):
  https://www.cnn.com/2017/08/03/us/michelle-carter-texting-suicide-sentencing/index.html

▸ 입법 개혁 및 콘래드 법:
• [16] Boston.com — 콘래드 법(Conrad's Law) 제정 발의 캠페인 (2019년 7월 24일):
  https://www.boston.com/news/politics/2019/07/25/conrads-law/
• [17] 매사추세츠주 의회 — 상원 법안 S.1032 공식 법률 조문:
  https://malegislature.gov/Bills/192/S1032.pdf
• [18] WBUR News — 원격 자해 강요 범죄화 법안에 대한 사법위원회 청문회:
  https://www.wbur.org/news/2019/11/12/massachusetts-legislation-suicide-text-case
• [19] CBS Boston — 린 로이 여사의 청소년 보호를 위한 콘래드 법 입법 운동:
  https://www.cbsnews.com/boston/news/conrad-roy-bill-law-suicide-michelle-carter/

▸ 행동심리학 및 가상공간 조작 분석:
• [20] 호주 경쟁소비자위원회(Scamwatch) — 몰입의 점진적 심화(Escalation of Commitment) 이론:
  https://www.scamwatch.gov.au/stop-check-protect/help-someone-whos-being-scammed/understanding-how-scammers-manipulate-your-loved-one
• [21] 미국 국립의학도서관(StatPearls / NCBI) — 인터넷 뮌하우젠 증후군 연구:
  https://www.ncbi.nlm.nih.gov/books/NBK518999/"""

# ==============================================================================
# 5. MÔ TẢ ĐẦY ĐỦ TIẾNG VIỆT
# ==============================================================================
DESC_VI = f"""Tập 07: Bản Án Giết Người Bằng Tin Nhắn | Tâm lý học tội phạm: Michelle Carter & Conrad Roy (Hệ Sinh Thái 10 Chỉ Dấu Tâm Lý & Thao Túng Không Gian Số) | Amber eyes

Vào sáng ngày 13 tháng 7 năm 2014, tại góc bãi đỗ xe của siêu thị Kmart thuộc thị trấn ven biển Fairhaven, bang Massachusetts, cảnh sát địa phương phát hiện chiếc xe bán tải Ford F-250 màu xanh lục sẫm. Bên trong cabin kín, chàng thanh niên 18 tuổi Conrad Roy III đã ra đi mãi mãi. Conrad vừa xuất sắc tốt nghiệp trung học, vừa nhận được tấm bằng danh giá thuyền trưởng tàu kéo (tugboat captain) theo truyền thống gia đình ba đời làm nghề sông nước. Trong mắt người thân và bạn bè, Conrad là một chàng trai lương thiện, hiền lành nhưng lại mang trong mình vết thương tâm lý sâu sắc — những cơn trầm cảm và nỗi bất an tuổi mới lớn mà cậu luôn nỗ lực vượt qua.

Thế nhưng, khi các thám tử thu giữ chiếc điện thoại của Conrad và tiến hành trích xuất dữ liệu số, họ không hề tìm thấy một bi kịch đơn độc. Ẩn sâu trong bộ nhớ là hơn hai mươi nghìn dòng tin nhắn qua lại giữa Conrad và cô bạn gái cách xa gần 50 km tại Plainville — Michelle Carter (17 tuổi). Michelle là một nữ sinh trung học bề ngoài ngoan hiền, ưa nhìn nhưng bên trong luôn dằn vặt bởi sự cô lập xã hội, chứng rối loạn ăn uống và cơn khát khao bệnh lý được bạn bè chú ý. Khi phát hiện những tổn thương tinh thần của Conrad, thay vì tìm kiếm sự trợ giúp y tế hay thông báo cho gia đình cậu, Michelle đã từng bước biến nỗi đau của người bạn trai thành một sân khấu bi kịch ảo, nơi cô ta có thể sắm vai chính: "người bạn gái đau khổ tận tụy".

Đỉnh điểm kinh hoàng xảy ra vào đêm ngày 12 rạng sáng ngày 13 tháng 7 năm 2014: trong khoảnh khắc sinh tử khi bản năng sinh tồn trỗi dậy, Conrad đã hoảng sợ mở cửa bước ra khỏi cabin ngột ngạt để tìm đường sống. Nhưng qua đường dây điện thoại kéo dài 47 phút xuyên màn đêm cách xa 50 km, Michelle Carter đã lạnh lùng ra lệnh cho cậu: "Hãy quay trở lại xe đi". Bản án lịch sử của Thẩm phán Lawrence Moniz kết tội Michelle ngộ sát không tự nguyện (involuntary manslaughter) — được Tòa án Tối cao Massachusetts giữ nguyên — đã trở thành một dấu mốc pháp lý kinh điển của thời đại số, phơi bày quyền lực hủy diệt của sự thao túng tâm lý qua màn hình điện thoại.

Hồ sơ Michelle Carter & Conrad Roy được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG MANG TẬP THỂ: Vụ án gây chấn động toàn cầu khi lần đầu tiên một cá nhân bị kết án tù vì những dòng tin nhắn và cuộc gọi cách xa 50 km mà không hề có mặt tại hiện trường; cú sốc xã hội làm dấy lên nỗi hoang mang tột độ trong các bậc phụ huynh thời đại số, phá vỡ ảo tưởng về sự vô hại của thế giới mạng và thúc đẩy làn sóng vận động Đạo luật Conrad (Conrad's Law) nhằm hình sự hóa hành vi ép buộc tự hủy hoại bản thân.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Michelle Carter không hề xem Conrad Roy như một sinh mệnh con người có cảm xúc, gia đình và tương lai, mà biến cậu thành "đạo cụ sống" trong một kịch bản bi kịch do chính mình đạo diễn; sự thiếu hụt thấu cảm cảm xúc (affective empathy deficit) khiến cô ta dửng dưng trước nỗi sợ hãi của nạn nhân, coi việc cậu biến mất là phương tiện kích hoạt ánh đèn sân khấu hướng về bản thân.
3. CƠ CHẾ CHIA NGĂN NHẬN THỨC (COMPARTMENTALIZATION): Xây dựng hai ngăn thực tại hoàn toàn cách biệt mà không chút cắn rứt lương tâm: ban ngày là nữ sinh ngoan ngoãn, chơi thể thao năng nổ tại trường King Philip, được gia đình nề nếp bao bọc như một "lá chắn bình thường hóa"; nhưng ban đêm qua màn hình điện thoại là kẻ săn mồi tâm lý kiên nhẫn bẻ gãy mọi rào cản đạo đức và bản năng sống của bạn trai.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Khi búa tòa giáng xuống và bằng chứng trích xuất số bộc lộ toàn bộ sự thật, chiếc mặt nạ vị tha vỡ vụn; Carter rơi vào trạng thái sụp đổ cái tôi ái kỷ kết hợp với nỗi tự thương hại bản thân bệnh lý (pathological self-pity), không một giọt nước mắt hối hận chân thành cho nạn nhân hay gia đình Roy, mà chỉ tập trung nại cớ tự do ngôn luận và kháng cáo lên tận Tòa án Tối cao Hoa Kỳ để trốn tránh tội lỗi.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC (TECHNIQUES OF NEUTRALIZATION): Triệt để áp dụng kỹ thuật "đổ lỗi cho nạn nhân" (trách móc Conrad chần chừ, không giữ lời hứa), "ngụy biện thiên thần cứu rỗi" (Hero Complex — tự huyễn hoặc mình đang giúp Conrad giải thoát sang một thế giới tốt đẹp hơn), và "ngoại hóa trách nhiệm" (đổ lỗi cho tác dụng phụ say thuốc chống trầm cảm Celexa) để vô hiệu hóa sự trừng phạt của tòa án lương tâm.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Đầu tháng 7 năm 2014, nỗi cô đơn tột cùng vì bị nhóm bạn cùng trường cô lập kết hợp với cảm giác thất vọng khi thấy Conrad nhiều lần do dự đã tạo nên điểm gãy tâm lý; Carter nhận ra nếu Conrad không thực sự ra đi, cô ta sẽ mãi mãi là kẻ vô hình và những lời than khóc trước đó với bạn bè sẽ bị bóc trần là dối trá, kích hoạt quyết định thúc ép nạn nhân đến cùng.
7. CHỮ KÝ SIGNATURE VS. THỦ ĐOẠN MO: Thủ đoạn (MO) liên tục thay đổi theo hoàn cảnh kỹ thuật: nhắn tin dồn dập, gọi điện thoại ban đêm, hướng dẫn xóa lịch sử cuộc gọi để qua mặt cảnh sát; Chữ ký tâm lý (Signature) bất biến: nhu cầu bệnh lý đóng vai "góa phụ bi kịch" — sao chép nguyên văn lời thoại nhân vật Rachel Berry (phim Glee), tung tin đồn Conrad mất tích trước khi vụ việc xảy ra, và tự đứng ra tổ chức giải bóng mềm từ thiện "Homers for Conrad" để bước lên bục vinh quang dưới danh nghĩa tình yêu.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Khởi đầu từ việc lắng nghe tâm sự để tìm kiếm sự kết nối, nhưng khi cơ chế dung nạp kích thích (tolerance buildup) bị lờn, Carter rơi vào trạng thái "đói ảo tưởng"; cô ta leo thang từ an ủi sang gợi ý phương thức, thúc giục thời gian, thách thức lòng tự trọng ("nếu cậu không làm thì cậu chỉ toàn nói suông"), và cuối cùng là mệnh lệnh lạnh lùng qua điện thoại tước đoạt cơ hội sống sót duy nhất của nạn nhân.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc một thiếu nữ da trắng ngoại ô xinh xắn, gia đình khá giả, luôn mỉm cười và tham gia hoạt động từ thiện đã tạo nên chiếc khiên tàng hình hoàn hảo; các thầy cô, bạn bè và phụ huynh xung quanh đều mắc kẹt trong điểm mù định kiến, không ai có thể ngờ một bộ não thao túng nguy hiểm lại đang ẩn mình sau gương mặt thơ ngây ấy.
10. NẠN NHÂN HỌC & CẢNH BÁO ĐỎ SINH TỒN: Trả lại danh dự và nhân phẩm trọn vẹn cho Conrad Roy — một chàng thanh niên tài năng, nhân hậu; đồng thời đúc kết 4 cảnh báo đỏ sống còn giúp thanh thiếu niên nhận diện và thoát khỏi kẻ thao túng: (1) Mối quan hệ độc hại cách ly bạn khỏi gia đình và các nguồn hỗ trợ y tế chuyên nghiệp; (2) Hành vi khiêu khích tự trọng, thách thức bạn chứng minh bản thân bằng những hành động gây tổn hại; (3) Kẻ luôn biến nỗi đau của bạn thành công cụ để thu hút sự chú ý trên mạng xã hội; (4) Khi trực giác báo động sự nguy hiểm, hãy dứt khoát cắt đứt liên lạc và tìm kiếm sự trợ giúp từ người thân, chuyên gia hoặc các đường dây nóng 24/7.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Buổi sáng định mệnh tại bãi đỗ xe Kmart
04:10 Hồi 2 · Mê cung hàng nghìn dòng tin nhắn
07:41 Hồi 3 · Vở kịch cô bạn gái đau khổ & bộ não ái kỷ kịch tính
11:06 Hồi 4 · Dòng tin nhắn tự thú và bản án lịch sử
14:54 Hồi 5 · Đạo đức không gian số & Đạo luật Conrad

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai tại Hoa Kỳ (Tòa án Tối cao Massachusetts, Tòa án Thiếu niên Hạt Bristol, Sở Cảnh sát Fairhaven). Kênh không nhằm bôi nhọ hay tôn vinh bất kỳ cá nhân nào.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là hình tượng minh họa nghệ thuật. Lời của Điều tra viên, Chuyên gia và Nhân chứng là lời dựng lại dựa trên tư liệu lịch sử.
• Giọng đọc, hình ảnh và âm thanh được hỗ trợ bởi công nghệ AI.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 NGUỒN THAM KHẢO ĐÃ ĐỐI CHIẾU
Toàn bộ sự kiện, ngày tháng và trích dẫn trong video đã được đối chiếu từng câu với 21 nguồn công khai (hồ sơ tòa án, báo chí, văn bản luật, nghiên cứu học thuật):

{SOURCES_VI}

Lưu ý: “Đạo luật Conrad” là dự luật do bà Lynn Roy cùng các nhà lập pháp Massachusetts vận động khởi xướng nhằm hình sự hóa hành vi ép buộc tự hủy hoại bản thân trong không gian số.
Danh mục nguồn chi tiết kèm biên bản đối chiếu 56 dữ kiện lịch sử được lưu trữ tại: 02_SAN_XUAT/Tap07/nguon_tham_khao.md

🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).
• Đường dây nóng hỗ trợ tâm lý Ngày Mai: 096 306 1414
• Viện Sức khỏe Tâm thần – Bệnh viện Bạch Mai: 024 3869 3731
• Đường dây nóng can thiệp & phòng chống bạo lực: 1900 969 680
• 988 Mental Health & Crisis Lifeline (Hoa Kỳ): Gọi hoặc nhắn tin 988 — https://988lifeline.org
• Childhelp National Child Abuse Hotline (Hoa Kỳ): 1-800-422-4453 — https://www.childhelp.org

#AmberEyes #TrueCrime #CriminalPsychology #MichelleCarter #ConradRoy #ConradsLaw #10ChiDauTamLy #CanhBaoDo #ThaoTungTamLy #TextingCase #InvoluntaryManslaughter #Glee #HoSoToiPham #Documentary"""

# ==============================================================================
# 6. MÔ TẢ ĐẦY ĐỦ TIẾNG ANH
# ==============================================================================
DESC_EN = f"""Ep. 07: The Landmark Texting Manslaughter Case | Criminal Psychology: Michelle Carter & Conrad Roy (10 Psychological Markers & Digital Coercion) | Amber eyes

On the morning of July 13, 2014, in a quiet corner of a Kmart parking lot in Fairhaven, Massachusetts, local police discovered a dark green Ford F-250 pickup truck. Inside the sealed cabin, 18-year-old Conrad Roy III was found deceased. Conrad had just graduated high school with honors and earned his tugboat captain's license—following in the proud maritime tradition of three generations of his family. To those who loved him, Conrad was a gentle, hardworking, and deeply sensitive young man who was fighting courageously against waves of clinical depression and adolescent anxiety.

However, when investigators seized Conrad's cell phone and performed digital forensic extraction, they did not find a solitary tragedy. Buried within the device were more than twenty thousand text messages exchanged between Conrad and his 17-year-old girlfriend living fifty kilometers away in Plainville: Michelle Carter. Michelle was an attractive suburban high school student whose polished appearance masked severe emotional turbulence, an eating disorder, and a desperate, pathological craving for social validation. Rather than alerting Conrad's family or seeking professional psychiatric intervention, Carter systematically transformed her boyfriend's vulnerability into a twisted digital theater where she cast herself as the grieving, devoted heroine.

The tragic culmination occurred on the night of July 12 into the early hours of July 13, 2014. In that terrifying moment when human survival instinct took over, Conrad climbed out of the fumes filling his truck cab to seek air and safety. Yet over a forty-seven-minute phone call across fifty kilometers of darkness, Michelle Carter issued a chilling, lethal directive: "Get back in." Judge Lawrence Moniz's historic decision convicting Carter of involuntary manslaughter—subsequently affirmed by the Massachusetts Supreme Judicial Court—established a monumental legal precedent for the digital age, exposing the devastating reality of remote psychological coercion.

Amber eyes dissects the Michelle Carter & Conrad Roy case through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: The case sent shockwaves across the globe as the first historic conviction for remote manslaughter perpetrated entirely through digital communication across 50 km; it shattered the cultural assumption that cyberspace messages are harmless, sparked widespread collective paranoia among parents in the smartphone era, and mobilized a persistent legislative campaign for Conrad’s Law to criminalize remote coercion to self-harm.
2. OBJECTIFICATION OF THE VICTIM: Carter completely dehumanized Conrad Roy, stripping him of his personal agency, aspirations, and family bonds to reduce him into a "living prop" for her narcissistic drama; her profound affective empathy deficit rendered her blind to his mortal terror, viewing his demise merely as the necessary plot device to illuminate herself in the digital spotlight.
3. COGNITIVE COMPARTMENTALIZATION: Maintaining two irreconcilable realities without internal friction: by day, an accomplished student athlete at King Philip Regional High School shielded by a protective suburban family acting as a "shield of normalcy"; by night, an obsessive digital predator calculatingly dismantling her vulnerable boyfriend's moral defenses and biological will to live.
4. NARCISSISTIC COLLAPSE & PATHOLOGICAL SELF-PITY: When confronted by undeniable forensic extractions and the weight of the courtroom verdict, Carter's benevolent facade disintegrated; she plummeted into narcissistic collapse accompanied by profound pathological self-pity, exhibiting zero genuine remorse for Conrad or the Roy family while pursuing constitutional First Amendment appeals all the way to the US Supreme Court to evade accountability.
5. TECHNIQUES OF NEUTRALIZATION & HERO COMPLEX: Weaponizing classic psychological neutralization strategies: "condemnation of the victim" (berating Conrad for hesitating and not following through), a twisted "Hero Complex" (rationalizing that she was altruistically releasing him from earthly torment into paradise), and "displacement of responsibility" (hiring defense psychiatrists to blame involuntary antidepressant Celexa toxicity).
6. PSYCHOLOGICAL TRIGGER & TIPPING POINT: In early July 2014, Carter's acute social alienation among her high school peer group collided with Conrad's repeated hesitation; realizing that if Conrad did not follow through she would remain socially invisible and her prior dramatic disclosures to friends would be unmasked as fraudulent attention-seeking, she crossed an irreversible psychological threshold from passive listener to aggressive instigator.
7. SIGNATURE VS. MODUS OPERANDI (MO): Her MO adapted dynamically to digital logistics: thousands of rapid SMS exchanges, late-night phone calls, and instructing Conrad to delete message logs to evade detection; Her immutable psychological Signature was the pathological compulsion to inhabit a tragic melodrama: plagiarizing verbatim dialogue from Lea Michele in the television series Glee, issuing premature false missing-person alerts to commandeer attention, and organizing the "Homers for Conrad" charity softball tournament to position herself at the center of public sympathy.
8. FANTASY ADDICTION & ESCALATION TRAJECTORY: Beginning with standard sympathetic listening, Carter gradually experienced tolerance buildup as casual validation lost its emotional charge; to satisfy her fantasy starvation, she escalated from reassurance to proposing methods, establishing deadlines, challenging his masculinity ("if you don't do it, you're just talking"), and ultimately issuing the fatal telephone command that extinguished his final opportunity for rescue.
9. HALO EFFECT & COLLECTIVE BLIND SPOTS: Her outward demographic persona as a pleasant, clean-cut, Caucasian suburban schoolgirl from a respectable household created an impenetrable halo effect; teachers, friends, and parents succumbed to systemic cognitive blind spots, incapable of imagining that severe predatory control could operate behind such an innocent facade until forensic phone records laid bare the digital reality.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Honoring the true memory, kindness, and industrious dignity of Conrad Roy III; and outlining four vital survival red flags from The Gift of Fear to identify digital manipulation: (1) Toxic isolation separating you from family and professional psychiatric care; (2) Passive-aggressive baiting and challenges demanding you prove your worth through self-destructive acts; (3) Narcissistic dramatization that exploits your private suffering for social media status; (4) Trusting visceral survival intuition to immediately sever contact and seek professional help from trusted loved ones or 24/7 crisis hotlines.

⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · The Fateful Morning in the Kmart Parking Lot
04:10 Act 2 · The Labyrinth of Thousands of Text Messages
07:41 Act 3 · The Grieving Girlfriend Drama & The Histrionic Narcissistic Mind
11:06 Act 4 · The Confession Text Message & The Historic Verdict
14:54 Act 5 · Cyberspace Ethics & Conrad’s Law

⚠️ LEGAL & SAFETY DISCLAIMER
• Produced exclusively for educational, criminological, and historical analysis; not medical or legal advice.
• Based on public US judicial archives (Supreme Judicial Court of Massachusetts, Bristol County Juvenile Court, Fairhaven Police Department). No intent to defame, harass, or glorify any individual.
• Avatars (Owl, Wolf, Fox, Sheep, Cat) and dialogue are dramatized illustrations based on archival transcripts.
• Synthetic AI voices, visuals, and audio are utilized.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 VERIFIED SOURCES & COURT EXHIBITS
All events, dates, and direct quotes have been verified line-by-line against 21 public archival sources (court transcripts, police files, investigative books, and academic studies):

{SOURCES_EN}

Note: "Conrad's Law" represents the landmark legislative initiative spearheaded by Lynn Roy and Massachusetts lawmakers to criminalize digital coercion to self-harm.
Complete source catalogue and historical cross-referencing ledger available at: 02_SAN_XUAT/Tap07/nguon_tham_khao.md

🆘 24/7 CRISIS & MENTAL HEALTH SUPPORT HOTLINES (FREE & CONFIDENTIAL)
If you or someone you know is going through emotional distress or crisis, please reach out to trusted professionals:
• 988 Mental Health & Crisis Lifeline (US & Canada): Call or text 988 — https://988lifeline.org
• Crisis Text Line: Text HOME to 741741 — https://www.crisistextline.org
• The Trevor Project: 1-866-488-7386 — https://www.thetrevorproject.org
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelphotline.org
• National Child Helpline 111 (Vietnam, toll-free 24/7) — http://tongdai111.vn

#AmberEyes #TrueCrime #CriminalPsychology #MichelleCarter #ConradRoy #ConradsLaw #10PsychologicalMarkers #SurvivalRedFlags #DigitalCoercion #TextingCase #InvoluntaryManslaughter #ForensicPsychology #Documentary"""

# ==============================================================================
# 7. MÔ TẢ ĐẦY ĐỦ TIẾNG NHẬT
# ==============================================================================
DESC_JA = f"""第07話 · メッセージによる殺人――デジタル空間の心理操作 | 犯罪心理学：ミシェル・カーターとコンラッド・ロイ事件 (10の心理指標と自己愛の演劇) | Amber eyes

2014年7月13日の朝、マサチューセッツ州フェアヘイブンの静かなKマート駐車場。地元警察は、人目につかない場所に停車していた濃い緑色のフォードF-250ピックアップトラックを発見しました。密閉された車内の中で、18歳の青年コンラッド・ロイ3世は息を引き取っていました。コンラッドは優秀な成績で高校を卒業したばかりで、3代続く一家の伝統を受け継ぎタグボート船長免許を取得した将来有望な若者でした。周囲の人々にとって、コンラッドは心優しく誠実でありながら、思春期の重い不安やうつ状態と懸命に向き合い続けていた青年でした。

しかし、捜査官がコンラッドの携帯電話を押収しデジタル鑑識解析を行った際、そこに浮かび上がったのは孤独な悲劇ではありませんでした。端末の奥底に記録されていたのは、50キロ離れたプレインビルに住む17歳の交際相手、ミシェル・カーターとの間で交わされた2万通を超えるテキストメッセージでした。ミシェルは清楚で裕福な家庭に育ちながら、激しい対人関係の孤立、摂食障害、そして周囲の関心を渇望する病的な自己愛に苛まれていました。コンラッドの心の傷を知った彼女は、専門機関への相談や家族への連絡を促す代わりに、その苦悩を自身の「悲劇の献身的なヒロイン」という舞台装置として悪用し始めたのです。

そして2014年7月12日夜から13日未明にかけて、恐るべき臨界点が訪れました。死の恐怖と生存本能から、コンラッドは充満する煙に耐えかねてトラックのドアを開け、外の空気を吸うために車外へ脱出しました。しかし、50キロの距離を隔てた47分間の通話の中で、ミシェル・カーターは冷酷にもこう命じたのです――「車の中に戻りなさい」。ローレンス・モニズ判事による歴史的な過失致死罪有罪判決と、マサチューセッツ州最高裁判所による判決維持は、デジタル空間における遠隔心理操作の破壊的脅威を世界に告発する画期的な司法の先例となりました。

アンバーアイズ（Amber eyes）は、本事件を「10の核心的心理・行動指標エコシステム」を通じて解剖します：
1. 社会的余波と集団的パラノイア: 現場にいなかった加害者が、50キロ離れた場所からのテキストと通話のみで過失致死罪に問われた史上初の判決。デジタル空間のメッセージは無害であるという幻想を完全に打ち砕き、スマートフォン時代における青少年の心理操作と集団的不安を顕在化させ、「コンラッド法（Conrad's Law）」制定への立法運動を巻き起こしました。
2. 被害者の客体化（Objectification）: カーターはコンラッドを尊厳ある人間としてではなく、自らが脚本・演出する悲劇の「生体プロップ（小道具）」として扱いました。感情的共感の致命的な欠如（Affective Empathy Deficit）により、青年の命の恐怖を意に介さず、彼の消滅を自らにスポットライトを当てるための手段へと矮小化しました。
3. 心理的区画化（Compartmentalization）: 昼はキング・フィリップ高校で活発にスポーツに励む模範的な生徒として「正常の盾（Shield of Normalcy）」を誇る家庭に守られ、夜は携帯電話の画面越しに青年の生存本能と倫理的防壁を執拗に解体する冷酷な捕食者という、完全に二極化した現実を平然と両立させました。
4. 自己愛の崩壊（Narcissistic Collapse）: デジタル鑑識の動かぬ証拠が白日の下に晒され、法廷で有罪を告げられた瞬間、慈善的ヒロインの仮面は砕け散りました。真の反省や遺族への悔悟を示すことなく、病的な自己憐憫（Pathological Self-Pity）に逃げ込み、連邦最高裁への言論の自由を口実にした上告を続けることで自らの道徳的責任を否定し続けました。
5. 自己正当化と中和の技術（Techniques of Neutralization）: 「被害者非難」（行動を起こさないコンラッドを責める）、「救済者妄想（Hero Complex）」（苦痛から解放して天国へ送るという歪んだ利他主義）、そして「責任の転嫁」（抗うつ薬セレクサによる非自発的酩酊を主張）という中和技術を駆使し、内なる良心の呵責を無力化しました。
6. 心理的引き金（トリガー）と破綻点: 2014年7月初旬、学校内での孤立感とコンラッドの度重なる躊躇が交錯した瞬間。コンラッドが生き続ければ自分は誰の注目も浴びず、友人たちに語っていた悲劇の物語が「嘘」として暴かれるという恐怖がトリガーとなり、受動的な聞き役から能動的かつ執拗な煽動者へと変貌しました。
7. 署名（Signature）対 手口（MO）: 手口（MO）は状況に応じて変化：連日の大量SMS送信、深夜の通話、履歴の削除指示。一方、不変の署名（Signature）は「悲劇のヒロイン」を演じる病的な渇望：人気ドラマ『Glee』のリア・ミシェル（レイチェル役）の台詞をそのまま盗用、コンラッドの失踪予告を事前に友人に流して同情を集め、死後には慈善ソフトボール大会「Homers for Conrad」を自ら主催して注目の的となりました。
8. 妄想への耽溺とエスカレーション軌道: 単なる相談相手から始まった関係は、刺激に対する耐性の形成（Tolerance Buildup）により深刻化。より強烈な注目を求める「妄想飢餓」に陥り、共感から方法の提示、日時の催促、自尊心を傷つける挑発（「行動しないなら口先だけ」）へと段階的に激化し、車外に逃げ出した彼を死へと連れ戻す致命的な通話命令へと至りました。
9. 後光効果（ハロー効果）と社会的盲点: 郊外の中産階級、笑顔の可愛らしい少女、ボランティア活動という属性が完璧なハロー効果を形成。学校や周囲の大人たちは「あのような無邪気な少女が遠隔で人を死に追いやるはずがない」という認知の盲点に囚われ、端末の全記録が押収されるまで何一つ見抜くことができませんでした。
10. 被害者学と生存のためのレッドフラッグ: 心優しく勤勉だったコンラッド・ロイ3世の名誉と尊厳を回復するとともに、『The Gift of Fear』に基づく4つの生存レッドフラッグを提示：(1) 家族や医療機関から孤立させようとする関係、(2) 自尊心を挑発し自傷的な行動を証明させようとする煽り、(3) 個人の苦悩をSNS等で自身の注目集めの道具にする行為、(4) 違和感や恐怖を覚えた時は直感に従い直ちに連絡を絶ち、信頼できる専門窓口に相談すること。

⏱ 目次（チャプター）
00:00 オープニング＆視聴にあたって
00:23 第1幕 · Kマート駐車場での運命の朝
04:10 第2幕 · 数千通のテキストメッセージの迷宮
07:41 第3幕 · 悲劇のヒロイン劇と自己愛性パーソナリティ
11:06 第4幕 · 自白テキストと歴史的有罪判決
14:54 第5幕 · デジタル空間の倫理とコンラッド法

⚠️ ご視聴にあたっての注意事項
• 本動画は教育、歴史的ドキュメンタリーおよび犯罪心理学の観点からの分析・解説コンテンツであり、医学的、心理学的、または法的なアドバイスに代わるものではありません。
• 米国の公開記録（マサチューセッツ州最高司法裁判所記録、ブリストル郡少年裁判所記録、フェアヘイブン警察捜査記録）に基づいて制作されています。特定の個人を中傷または美化する意図は一切ありません。
• 登場するキャラクター（フクロウ、オオカミ、キツネ、羊、猫）は演出用の架空のキャラクターです。
• 音声、画像、音楽はAIツールを活用して制作されています。
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 参考資料・出典
本動画におけるすべての事件経過、日時、判決記録および心理分析は、以下の21件の公式公開記録と照合されています：

{SOURCES_JA}

注記：「コンラッド法（Conrad's Law）」は、オンライン空間における遠隔煽動・強要行為を犯罪化するためにリン・ロイ氏とマサチューセッツ州議会議員が主導する法案です。
全56件の歴史的事実対照記録を含む完全な出典一覧は、以下のファイルに保存されています：02_SAN_XUAT/Tap07/nguon_tham_khao.md

🆘 相談窓口・支援ホットライン（通話無料・24時間受付）
悩みや不安を抱えているときは、決してひとりで抱え込まず、専門の相談窓口にご相談ください：
• こころの健康相談統一ダイヤル：0570-064-556（対応時間は自治体により異なります）
• よりそいホットライン：0120-279-338（通話無料・24時間対応・多言語対応）
• 児童相談所虐待対応ダイヤル：189（いちはやく・通話無料・24時間対応）
• 性犯罪・性暴力被害者のためのワンストップ支援センター：#8891（短縮ダイヤル）
• 警察相談専用電話：#9110（全国共通）

#犯罪心理学 #TrueCrime #ミシェルカーター #コンラッドロイ #10の心理指標 #レッドフラッグ #マインドコントロール #デジタル空間の罠 #自己愛性パーソナリティ #ドキュメンタリー #AmberEyes #コンラッド法"""

# ==============================================================================
# 8. MÔ TẢ ĐẦY ĐỦ TIẾNG HÀN
# ==============================================================================
DESC_KO = f"""07화 · 문자로 내린 살인 판결――디지털 조작의 덫 | 범죄심리학: 미셸 카터 & 콘래드 로이 사건 (10대 심리 지표와 가상공간의 비극) | Amber eyes

2014년 7월 13일 아침, 미국 매사추세츠주 페어헤이븐의 한적한 케이마트(Kmart) 주차장. 현장에 출동한 경찰은 주차장 구석에 세워진 짙은 녹색 포드 F-250 픽업트럭을 발견했습니다. 밀폐된 차량 내부에서 18세 청년 콘래드 로이 3세가 싸늘한 주검으로 발견되었습니다. 콘래드는 우수한 성적으로 고등학교를 갓 졸업하고, 3대째 바다를 지켜온 가문의 전통을 이어 예인선 선장 면허까지 취득한 성실하고 유망한 청년이었습니다. 가족과 지인들의 기억 속 콘래드는 다정하고 배려심 깊은 청년이었으나, 청소년기 특유의 극심한 불안과 우울감 속에서 고통스럽게 싸우고 있었습니다.

그러나 경찰 수사관들이 콘래드의 휴대전화를 압수하여 디지털 포렌식 복구를 진행했을 때, 드러난 것은 단순한 고립된 비극이 아니었습니다. 전화기 속에는 50킬로미터 떨어진 플레인빌에 사는 17세의 여자친구 미셸 카터와 주고받은 2만 건이 넘는 문자 메시지가 고스란히 남아 있었습니다. 겉보기에는 단정하고 모범적인 학생이었던 미셸 카터는 내면에 극단적인 사회적 소외감, 섭식 장애, 그리고 타인의 관심을 갈망하는 병적인 연극성·자기애적 성격을 품고 있었습니다. 콘래드의 정신적 고통을 알게 된 미셸은 전문적인 치료나 가족에게 도움을 요청하는 대신, 그의 고통을 자신이 주연을 맡을 '비련의 헌신적인 여주인공' 연극의 무대 장치로 철저히 악용하기 시작했습니다.

그리고 2014년 7월 12일 밤부터 13일 새벽, 참혹한 임계점이 찾아왔습니다. 일산화탄소의 고통과 본능적인 생존에 대한 갈망으로 콘래드는 공포에 질려 차량 문을 열고 밖으로 뛰쳐나왔습니다. 그러나 50킬로미터 떨어진 곳에서 이어진 47분간의 통화 속에서, 미셸 카터는 차갑게 명령했습니다――"다시 차 안으로 들어가." 로런스 모니즈 판사의 역사적인 과실치사(involuntary manslaughter) 유죄 판결과 매사추세츠주 대법원의 판결 확정은, 가상공간에서 벌어지는 원격 심리 조작의 치명적인 폭력성을 전 세계에 폭로한 디지털 시대의 중대한 사법적 이정표가 되었습니다.

Amber eyes는 본 사건을 '10대 핵심 심리·행동 지표 생태계'를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 불안·파라노이아: 범죄 현장에 물리적으로 존재하지 않았던 인물이 50km 떨어진 곳에서 전송한 문자 메시지와 전화 통화만으로 과실치사 유죄 판결을 받은 사법 역사상 최초의 판결. 온라인상의 언어 폭력과 심리 조작이 치명적인 결과를 낳을 수 있음을 입증하며 스마트폰 시대 학부모들에게 거대한 충격을 안겼고, 원격 자해 강요 행위를 처벌하는 '콘래드 법(Conrad's Law)' 제정 운동을 촉발했습니다.
2. 피해자의 사물화 및 객체화(Objectification): 카터는 콘래드를 인격과 고통을 지닌 한 인간으로 보지 않고, 자신이 기획한 비극적 드라마를 완성하기 위한 '살아있는 소품(living prop)'으로 취급했습니다. 정서적 공감 결핍(Affective Empathy Deficit)으로 인해 피해자의 공포를 전혀 느끼지 못했으며, 그의 죽음을 자신에게 스포트라이트를 비추기 위한 도구로 전락시켰습니다.
3. 인지적 구획화(Compartmentalization): 낮에는 킹 필립 고등학교에서 운동에 전념하고 평화로운 가정이라는 '정상성의 방패(Shield of Normalcy)' 뒤에 숨은 모범적인 학생, 밤에는 휴대폰 화면을 통해 취약한 피해자의 생존 본능과 도덕적 방벽을 파괴하는 포식자라는 두 극단의 삶을 양심의 가책 없이 완벽하게 분리·영위했습니다.
4. 나르시시즘적 붕괴와 병적 자기연민: 포렌식 증거가 낱낱이 공개되고 유죄 판결이 확정되자 자선적이고 순결했던 가면은 산산조각 났습니다. 카터는 진정한 참회나 유족에 대한 사죄 대신 극단적인 자기연민(Pathological Self-Pity)에 빠져들었으며, 미국 연방대법원까지 표현의 자유를 주장하며 상고를 거듭해 법적·도덕적 책임을 끝까지 회피하려 했습니다.
5. 자기 정당화 및 중화 기술(Techniques of Neutralization): '피해자 비난'(약속을 지키지 않고 망설이는 콘래드를 질책), '영웅 콤플렉스(Hero Complex)'(고통스러운 세상에서 벗어나 천국으로 보내주는 것이라는 왜곡된 이타주의), 그리고 '책임의 외재화'(항우울제 셀렉사 복용으로 인한 비자발적 약물 취약 상태 주장)를 통해 내면의 죄책감을 무력화했습니다.
6. 심리적 방아쇠와 티핑 포인트: 2014년 7월 초, 교내에서의 극심한 고립감과 콘래드의 계속되는 망설임이 맞물린 순간. 콘래드가 행동하지 않는다면 자신은 영원히 투명인간으로 남게 되고, 친구들에게 미리 흘려둔 비극의 서사가 거짓으로 탄로 날 것이라는 공포가 방아쇠가 되어, 위로자를 가장한 청취자에서 잔혹한 행동 강요자로 폭주했습니다.
7. 시그니처(Signature) vs 범행 수법(MO): 수법(MO)은 상황에 따라 진화: 수천 건의 연속 SMS, 심야 통화, 수사관을 피하기 위한 메시지 삭제 지시. 반면 불변의 시그니처(Signature)는 '비련의 여주인공'을 향한 병적인 집착: 드라마 《글리(Glee)》 속 레이첼 베리(리아 미셸 분)의 대사를 그대로 모방, 사망 전 미리 친구들에게 실종 소식을 알리며 동정심 유발, 사후에는 추모 자선 소프트볼 대회 'Homers for Conrad'를 직접 주최해 관심의 정점에 서려 했습니다.
8. 환상 중독과 에스컬레이션 궤적: 단순한 고민 상담에서 시작된 관계는 자극 내성 형성(Tolerance Buildup)으로 점차 심화되었습니다. 더 강렬한 인정을 갈망하는 '환상 기아' 상태에 빠진 카터는 공감에서 수단 제시, 일정 독촉, 자존심을 짓밟는 도발("행동하지 않으면 넌 그냥 말뿐인 사람이야")로 수위를 높였으며, 결국 차 밖으로 도망친 피해자를 죽음으로 밀어 넣는 전화 통화 명령에 도달했습니다.
9. 후광 효과(Halo Effect)와 제도의 맹점: 교외 중산층, 밝은 미소를 지닌 백인 소녀, 자선 활동이라는 외적 조건이 완벽한 후광 효과를 형성했습니다. 학교, 교사, 주변 어른들은 '저런 순진한 소녀가 누군가를 원격으로 조작할 리 없다'는 편견의 맹점에 갇혀, 디지털 포렌식 데이터가 복구될 때까지 끔찍한 조작의 실체를 전혀 인지하지 못했습니다.
10. 피해자학 및 생존을 위한 레드플래그: 따뜻하고 유능했던 콘래드 로이 3세의 명예와 존엄을 회복하고, 《The Gift of Fear》에 기반한 4대 생존 경고 신호를 제시: (1) 가족 및 전문 의료기관과의 단절을 유도하는 관계, (2) 자존심을 건드리며 자해적 행동으로 자신을 증명하라고 압박하는 행위, (3) 타인의 고통을 자신의 SNS 관심 유발 도구로 삼는 태도, (4) 불안과 위험을 감지했을 때 본능적인 직관을 믿고 즉시 관계를 차단하며 전문 상담 핫라인에 도움을 요청할 것.

⏱ 챕터(타임라인)
00:00 오프닝 & 시청 안내
00:23 제1막 · 케이마트 주차장의 운명적인 아침
04:10 제2막 · 수천 통의 문자 메시지 미로
07:41 제3막 · 비련의 여주인공 연극과 연극성·자기애적 심리
11:06 제4막 · 자백 문자 메시지와 역사적 유죄 판결
14:54 제5막 · 사이버 공간의 윤리와 콘래드 법

⚠️ 시청 전 법적 유의사항
• 본 콘텐츠는 교육, 범죄심리학 및 역사적 분석 목적의 다큐멘터리이며, 전문적인 의학적, 정신과적 또는 법률적 조언을 대신할 수 없습니다.
• 미국 공식 사법 기록(매사추세츠주 대법원 판결문, 브리스톨 카운티 소년법원 기록, 페어헤이븐 경찰서 수사 기록)을 바탕으로 제작되었습니다. 본 채널은 특정인을 비방하거나 미화하려는 의도가 전혀 없습니다.
• 등장하는 올빼미, 늑대, 여우, 양, 고양이는 시각적 연출을 위한 가상 캐릭터입니다.
• 본 영상의 음성, 시각 이미지, 음악은 AI 기술을 활용하여 제작되었습니다.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 공식 참고자료 및 공판 기록
본 영상의 모든 사건 개요, 날짜, 재판 진술 및 타임라인은 다음 21개 공식 공개 기록과 교차 검증되었습니다:

{SOURCES_KO}

참고: '콘래드 법(Conrad's Law)'은 린 로이 여사와 매사추세츠주 의회가 주도하여 원격 자해 강요 및 조작 행위를 처벌하기 위해 발의한 주요 법안입니다.
56개 역사적 사실 대조표를 포함한 전체 출처 목록은 다음 파일에 보관되어 있습니다: 02_SAN_XUAT/Tap07/nguon_tham_khao.md

🆘 위기 상담 및 피해자 지원 핫라인 (24시간 무료 & 비밀보장)
마음의 고통이나 극심한 위기 상황에 처해 있다면 혼자 견디지 마시고 언제든 도움을 요청하세요:
• 정신건강 위기상담전화: 1577-0199 (24시간)
• 청소년 상담전화: 국번없이 1388 (24시간)
• 아동학대 예방 및 신고 상담전화: 국번없이 112 또는 129
• 여성긴급전화 (가정폭력·성폭력 상담): 국번없이 1366
• 보건복지상담센터: 국번없이 129

#AmberEyes #범죄심리학 #TrueCrime #미셸카터 #콘래드로이 #10대심리지표 #레드플래그 #가스라이팅 #디지털조작 #연극성성격장애 #다큐멘터리 #콘래드법"""

# ==============================================================================
# 9. GHI FILE TOÀN BỘ 18 ĐÍCH
# ==============================================================================
files_to_write = [
    # 1. TIẾNG VIỆT
    (ROOT / "02_SAN_XUAT" / "Tap07" / "nguon_mo_ta.txt", SOURCES_VI),
    (ROOT / "02_SAN_XUAT" / "Tap07" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "mo_ta.txt", DESC_VI),

    # 2. TIẾNG ANH
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN),
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "xuat_ban" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),

    # 3. TIẾNG NHẬT
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "xuat_ban" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),

    # 4. TIẾNG HÀN
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "xuat_ban" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
]

written_count = 0
for path, content in files_to_write:
    path.parent.mkdir(parents=True, exist_ok=True)
    # Ghi bằng open với newline='' để tránh nhân đôi CRLF (\r\r\n) theo Luật T19 / Lesson #119
    clean_text = content.strip() + "\n"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(clean_text)
    
    # Kiểm tra ngay lập tức byte raw không có \r\r\n
    raw_bytes = path.read_bytes()
    assert b"\r\r\n" not in raw_bytes, f"LỖI T19: phát hiện \\r\\r\\n trong {path}"
    written_count += 1
    print(f"[{written_count:02d}/18] Đã ghi thành công: {path.relative_to(ROOT)} ({len(clean_text)} ký tự)")

print(f"\nHoàn tất tạo và cập nhật 18 file mô tả & nguồn đạt chuẩn 10 chỉ dấu cho Tập 07!")
