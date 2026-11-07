#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo và cập nhật mô tả video đạt chuẩn Hệ sinh thái 10 chỉ dấu tâm lý & hành vi
cho Tập 07 trên cả 4 ngôn ngữ (VI, EN, JA, KO).
TUYỆT ĐỐI TUÂN THỦ TRẦN YOUTUBE <= 5,000 KÝ TỰ (Rule L3).
"""

import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"d:\TEST\Gax\amber-eyes")

# ==============================================================================
# 1. NGUỒN ĐẦY ĐỦ 21 MỤC CHO CÁC TÀI LIỆU LƯU TRỮ (NGUON_MO_TA.TXT)
# ==============================================================================
SOURCES_VI_FULL = """▸ Hồ sơ vụ án & bản án tư pháp:
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
• [20] Scamwatch (ACCC) — Cơ chế leo thang cam kết:
  https://www.scamwatch.gov.au/stop-check-protect/help-someone-whos-being-scammed/understanding-how-scammers-manipulate-your-loved-one
• [21] National Library of Medicine (NCBI / StatPearls) — Munchausen by Internet:
  https://www.ncbi.nlm.nih.gov/books/NBK518999/"""

SOURCES_EN_FULL = """▸ Official Court Records & Legal Documents:
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
• [20] Australian Competition & Consumer Commission (Scamwatch) — Escalation of Commitment:
  https://www.scamwatch.gov.au/stop-check-protect/help-someone-whos-being-scammed/understanding-how-scammers-manipulate-your-loved-one
• [21] National Library of Medicine (NCBI / StatPearls) — Munchausen by Internet:
  https://www.ncbi.nlm.nih.gov/books/NBK518999/"""

SOURCES_JA_FULL = """▸ 公的司法記録および公式裁判資料:
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

SOURCES_KO_FULL = """▸ 공식 사법 기록 및 법원 판결문:
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
• [20] 호주 경쟁소비자위원회(Scamwatch) — 몰입의 점진적 심화 이론:
  https://www.scamwatch.gov.au/stop-check-protect/help-someone-whos-being-scammed/understanding-how-scammers-manipulate-your-loved-one
• [21] 미국 국립의학도서관(StatPearls / NCBI) — 인터넷 뮌하우젠 증후군:
  https://www.ncbi.nlm.nih.gov/books/NBK518999/"""

# ==============================================================================
# 2. BẢN MÔ TẢ ĐẦY ĐỦ TIẾNG VIỆT (TỐI ƯU HOÁ STRICTLY <= 5,000 KÝ TỰ)
# ==============================================================================
DESC_VI = """Tập 07: Bản Án Giết Người Bằng Tin Nhắn | Tâm lý học tội phạm: Michelle Carter & Conrad Roy (Hệ Sinh Thái 10 Chỉ Dấu Tâm Lý & Thao Túng Không Gian Số) | Amber eyes

Sáng 13/7/2014, tại bãi đỗ xe Kmart (Fairhaven, Massachusetts), cảnh sát phát hiện Conrad Roy III (18 tuổi) tử vong trong xe bán tải Ford F-250. Dù vừa nhận bằng thuyền trưởng tàu kéo danh giá, Conrad luôn phải vật lộn với những cơn trầm cảm nặng nề. Khi trích xuất điện thoại, thám tử phát hiện hơn 20.000 tin nhắn từ bạn gái Michelle Carter (17 tuổi, ở Plainville). Thay vì cứu giúp, Michelle đã biến nỗi đau của bạn trai thành một sân khấu ảo để thỏa mãn cơn khát bệnh lý được chú ý. Đêm 12/7/2014, khi Conrad hoảng sợ bước ra khỏi xe để tìm đường sống, Michelle đã lạnh lùng ra lệnh qua điện thoại cách xa 50 km: "Hãy quay trở lại xe đi". Bản án ngộ sát không tự nguyện lịch sử của Thẩm phán Lawrence Moniz đã trở thành tiền lệ kinh điển thời đại số.

Hồ sơ Michelle Carter & Conrad Roy được Amber eyes giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi (§A2c):
1. DƯ CHẤN XÃ HỘI & NỖI HOANG MANG TẬP THỂ: Phán quyết lịch sử kết án kẻ thao túng từ xa 50 km; phá vỡ ảo tưởng ngôn từ mạng vô hại, dấy lên nỗi bất an của phụ huynh và thúc đẩy Đạo luật Conrad (Conrad's Law) hình sự hóa ép buộc tự hại.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem Conrad là "đạo cụ sống" trong kịch bản bi kịch tự đạo diễn; khuyết tật thấu cảm (Affective Empathy Deficit) khiến Carter dửng dưng trước nỗi sợ của nạn nhân để chiếm spotlight ảo.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Hai mặt song song: ban ngày là nữ sinh ngoan nấp sau "lá chắn bình thường hóa" của gia đình; ban đêm là kẻ săn mồi kỹ thuật số bẻ gãy bản năng sống của bạn trai.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Dữ liệu số phơi bày, vỏ bọc vị tha vỡ vụn; Carter sụp đổ ái kỷ cùng sự tự thương hại bệnh lý (Pathological Self-Pity), không hề ăn năn mà kiên quyết kháng cáo lên Tối cao Pháp viện.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA: Áp dụng kỹ thuật trung hòa: "đổ lỗi cho nạn nhân", "ngụy biện thiên thần cứu rỗi" (Hero Complex — huyễn hoặc đang giải thoát bạn trai), và "ngoại hóa trách nhiệm" (đổ cho thuốc Celexa).
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Đầu tháng 7/2014, nỗi cô đơn bị bạn bè cô lập cùng sự do dự của Conrad tạo điểm gãy; sợ bị lật tẩy nói dối khi đã tung tin trước đó, Carter quyết định thúc ép nạn nhân để giữ thể diện ảo.
7. CHỮ KÝ SIGNATURE VS. THỦ ĐOẠN MO: MO (nhắn tin, xóa lịch sử) thay đổi linh hoạt; Signature bất biến là khao khát đóng vai "góa phụ bi thương" — sao chép thoại phim Glee (Rachel Berry) và tổ chức bóng mềm "Homers for Conrad".
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Quen nhờn cảm xúc dẫn tới "đói ảo tưởng"; leo thang từ an ủi sang gợi ý phương thức, ấn định thời gian, khiêu khích tự trọng và kết thúc bằng mệnh lệnh điện thoại tước đoạt sự sống của nạn nhân.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc thiếu nữ da trắng ngoại ô ngoan hiền tạo hào quang ru ngủ trực giác cộng đồng; nhà trường và phụ huynh đều mắc kẹt trong định kiến, không ngờ kẻ thao túng lại ẩn sau gương mặt thơ ngây.
10. NẠN NHÂN HỌC & CẢNH BÁO ĐỎ SINH TỒN: Tôn vinh Conrad Roy III; 4 cảnh báo đỏ (The Gift of Fear): (1) Bị cô lập khỏi gia đình/y tế; (2) Bị khiêu khích tự trọng để tự hại; (3) Bị dùng nỗi đau làm mồi câu chú ý; (4) Tin trực giác, lập tức cắt liên lạc và tìm trợ giúp.

⏱ MỐC CHƯƠNG
00:00 Khuyến cáo
00:23 Hồi 1 · Buổi sáng định mệnh tại bãi đỗ xe Kmart
04:10 Hồi 2 · Mê cung hai mươi nghìn dòng tin nhắn
07:41 Hồi 3 · Vở kịch cô bạn gái đau khổ & bộ não ái kỷ
11:06 Hồi 4 · Dòng tin nhắn tội lỗi và bản án lịch sử
14:54 Hồi 5 · Đạo đức không gian số & Đạo luật Conrad

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Tư liệu lịch sử & phân tích tâm lý tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên hồ sơ công khai của Tòa án Massachusetts. Không bôi nhọ hay tôn vinh bất kỳ ai.
• Hình tượng động vật là nghệ thuật. Giọng đọc & âm thanh hỗ trợ bởi AI (Higgs Audio).

📚 NGUỒN THAM KHẢO CHÍNH THỨC
• Tòa Tối cao Massachusetts — Commonwealth v. Michelle Carter: https://www.supremecourt.gov/
• Phán quyết Thẩm phán Moniz (Tòa Bristol): https://www.masslive.com/
• Quốc hội Massachusetts — Dự luật Conrad (S.1032): https://malegislature.gov/
• Nghiên cứu Munchausen by Internet (NCBI): https://www.ncbi.nlm.nih.gov/books/NBK518999/
• Jesse Barron: 'The Girl From Plainville' (Esquire) & Báo cáo Thám tử Scott Gordon.
* Toàn bộ 21 nguồn và biên bản 56 dữ kiện lưu tại: 02_SAN_XUAT/Tap07/nguon_tham_khao.md

🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ 24/7 (MIỄN PHÍ)
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (Việt Nam) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Hỗ trợ tâm lý): 096 306 1414
• 988 Suicide & Crisis Lifeline (Mỹ): Gọi/nhắn 988 — https://988lifeline.org
• Childhelp National Child Abuse Hotline: 1-800-422-4453

#AmberEyes #TrueCrime #TamLyHocToiPham #MichelleCarter #ConradRoy #ConradsLaw #10ChiDauTamLy #CanhBaoDo #ThaoTungTamLy #TextingCase #InvoluntaryManslaughter #HoSoToiPham #Glee"""

# ==============================================================================
# 3. BẢN MÔ TẢ ĐẦY ĐỦ TIẾNG ANH (TỐI ƯU HOÁ STRICTLY <= 5,000 KÝ TỰ)
# ==============================================================================
DESC_EN = """Ep. 07: The Landmark Texting Manslaughter Case | Criminal Psychology: Michelle Carter & Conrad Roy (10 Psychological Markers & Digital Coercion) | Amber eyes

On July 13, 2014, in a Kmart parking lot in Fairhaven, Massachusetts, police found Conrad Roy III (18) dead inside a Ford F-250. Conrad had graduated with honors and earned a tugboat captain's license, yet fought severe depression. Forensics recovered over 20,000 texts from girlfriend Michelle Carter (17, in Plainville). Rather than helping, Carter turned his pain into a digital stage to feed her craving for attention. When survival instinct drove Conrad to escape the fume-filled cab, Carter coldly commanded him by phone from 50 km away: "Get back in." Judge Lawrence Moniz's historic manslaughter ruling—upheld by the Massachusetts Supreme Judicial Court—became a digital legal milestone.

Amber eyes dissects the case through our 10-Indicator Behavioral & Psychological Ecosystem (§A2c):
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: Historic conviction of a remote manipulator 50 km away; shattered the myth of harmless cyber words, sparked parental anxiety, and spurred Conrad's Law to criminalize coercion to self-harm.
2. OBJECTIFICATION OF THE VICTIM: Reducing Conrad to a "living prop" in her drama; severe affective empathy deficit rendered Carter indifferent to his mortal terror, using his death to seize the digital spotlight.
3. COGNITIVE COMPARTMENTALIZATION: Parallel lives: by day, an active athlete at King Philip High shielded by a "shield of normalcy"; by night, a digital predator systematically dismantling her boyfriend's will to live.
4. NARCISSISTIC COLLAPSE & SELF-PITY: When digital proof emerged, her benevolent mask shattered; Carter fell into pathological self-pity without remorse, appealing all the way to the US Supreme Court.
5. TECHNIQUES OF NEUTRALIZATION: Neutralization tactics: "victim blaming" (berating Conrad for hesitating), a twisted "Hero Complex" (rationalizing she freed him into heaven), and blaming Celexa medication.
6. PSYCHOLOGICAL TRIGGER & TIPPING POINT: In July 2014, peer isolation collided with Conrad's hesitation; fearing her prior claims would be exposed as attention-seeking, Carter aggressively coerced him to preserve face.
7. SIGNATURE VS. MODUS OPERANDI (MO): MO (rapid texting, deleting logs) evolved; immutable Signature was her need to play the "grieving widow" — quoting Glee (Rachel Berry) and hosting the "Homers for Conrad" softball tournament.
8. FANTASY ADDICTION & ESCALATION: Tolerance buildup fueled "fantasy starvation"; escalating from sympathy to suggesting methods, setting deadlines, attacking his ego, and the fatal phone command ending his life.
9. HALO EFFECT & COLLECTIVE BLIND SPOTS: Her persona as a smiling suburban schoolgirl created a halo effect; teachers and parents succumbed to blind spots, unable to perceive the predator behind her innocent face.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Honoring Conrad Roy III; 4 survival red flags (The Gift of Fear): (1) Isolation from family/doctors; (2) Baiting ego to prove worth via self-harm; (3) Weaponizing pain for clout; (4) Trust intuition and seek help.

⏱ CHAPTER TIMESTAMPS
00:00 Advisory & Intro
00:23 Act 1 · The Fateful Morning in the Kmart Parking Lot
04:10 Act 2 · The Labyrinth of Twenty Thousand Text Messages
07:41 Act 3 · Grieving Girlfriend Drama & Histrionic Mind
11:06 Act 4 · The Confession Text & Historic Verdict
14:54 Act 5 · Cyberspace Ethics & Conrad’s Law

⚠️ LEGAL & SAFETY DISCLAIMER
• Educational documentary on criminal psychology; not medical or legal advice.
• Derived from public records of Massachusetts courts. Does not glorify or defame anyone.
• Narrator avatars are artistic motifs. Audio and visuals are AI-assisted (Higgs Audio).

📚 VERIFIED HISTORICAL & LEGAL DOSSIER
• Mass. Supreme Judicial Court — Commonwealth v. Michelle Carter: https://www.supremecourt.gov/
• Bristol Juvenile Court — Judge Lawrence Moniz Ruling: https://www.masslive.com/
• Mass. General Court — Senate Bill S.1032 (Conrad's Law): https://malegislature.gov/
• National Library of Medicine (NCBI) — Munchausen by Internet: https://www.ncbi.nlm.nih.gov/books/NBK518999/
• Jesse Barron: 'The Girl From Plainville' (Esquire) & Det. Scott Gordon Report.
* Full 21-source catalogue & 56 verified facts: 02_SAN_XUAT/Tap07/nguon_tham_khao.md

🆘 24/7 CRISIS & MENTAL HEALTH HOTLINES (FREE & CONFIDENTIAL)
• 988 Suicide & Crisis Lifeline (US & Canada): Call/text 988 — https://988lifeline.org
• Crisis Text Line: Text HOME to 741741 — https://www.crisistextline.org
• Childhelp National Child Abuse Hotline: 1-800-422-4453
• National Child Helpline 111 (Vietnam, toll-free 24/7) — http://tongdai111.vn/

#AmberEyes #TrueCrime #CriminalPsychology #MichelleCarter #ConradRoy #ConradsLaw #10PsychologicalMarkers #SurvivalRedFlags #DigitalCoercion #TextingCase #InvoluntaryManslaughter #ForensicPsychology #Documentary"""

# ==============================================================================
# 4. BẢN MÔ TẢ ĐẦY ĐỦ TIẾNG NHẬT (TỐI ƯU HOÁ STRICTLY <= 5,000 KÝ TỰ)
# ==============================================================================
DESC_JA = """第07話 · メッセージによる殺人――デジタル空間の心理操作 | 犯罪心理学：ミシェル・カーターとコンラッド・ロイ事件 (10の心理指標と自己愛の演劇) | Amber eyes

2014年7月13日の朝、マサチューセッツ州フェアヘイブンのKマート駐車場にて、警察は停車中のフォードF-250ピックアップトラック内で息を引き取っていた18歳の青年コンラッド・ロイ3世を発見しました。コンラッドは優秀な成績で高校を卒業し、一家の伝統であるタグボート船長免許を取得したばかりでしたが、思春期の深刻なうつ状態と闘っていました。押収した携帯電話を解析した捜査官は、50キロ離れたプレインビルに住む17歳の交際相手、ミシェル・カーターとの2万通を超えるテキストを発見。彼女は救助を求める代わりに、青年の心の傷を「悲劇のヒロイン」を演じるための舞台装置へと利用していたのです。

そして運命の2014年7月12日夜から13日未明、生存本能から車外へと脱出したコンラッドに対し、ミシェルは47分間の通話越しに冷酷にも命じました――「車の中に戻りなさい」。ローレンス・モニズ判事による歴史的な過失致死罪有罪判決と最高裁による支持は、デジタル時代の遠隔心理操作を断罪する画期的な先例となりました。

アンバーアイズ（Amber eyes）は、本事件を「10の核心的心理・行動指標エコシステム」を通じて解剖します：
1. 社会的余波と集団的パラノイア: 現場にいなかった人物が50km離れた場所からのテキストと通話のみで過失致死罪に問われた史上初の判決。メッセージは無害であるという幻想を打ち砕き、青少年の心理操作に対する親の不安を顕在化させ、「コンラッド法（Conrad's Law）」制定運動を巻き起こしました。
2. 被害者の客体化（Objectification）: コンラッドを尊厳ある人間ではなく、自らが脚本・演出する悲劇の「生体プロップ（小道具）」として扱いました。感情的共感の致命的欠如により、青年の死を自らにスポットライトを当てる道具へと矮小化しました。
3. 心理的区画化（Compartmentalization）: 昼はスポーツに励む模範的な生徒として「正常の盾」を誇る家庭に守られ、夜は画面越しに青年の生存本能を解体する捕食者という、二極化した現実を平然と両立させました。
4. 自己愛の崩壊（Narcissistic Collapse）: デジタル証拠が法廷で暴かれ有罪を告げられた瞬間、慈善的ヒロインの仮面は崩壊。遺族への真の悔悟を示すことなく病的な自己憐憫に逃げ込み、連邦最高裁へ言論の自由を口実に上告を続けました。
5. 自己正当化と中和の技術: 「被害者非難」（行動を起こさない相手を責める）、「救済者妄想（Hero Complex）」（天国へ送るという歪んだ利他主義）、そして「責任の転嫁」（抗うつ薬セレクサによる酩酊を主張）という中和技術を駆使しました。
6. 心理的引き金と破綻点: 2014年7月初旬、学校での孤立感と相手の躊躇が交錯。コンラッドが生き続ければ自分は注目されず、友人に語っていた物語が嘘と暴かれる恐怖が引き金となり、執拗な煽動者へと変貌しました。
7. 署名（Signature）対 手口（MO）: 手口（大量SMS、深夜通話、履歴消去指示）は変化する一方、不変の署名は「悲劇のヒロイン」への病的な渇望：ドラマ『Glee』の台詞盗用、事前の失踪予告、死後の慈善ソフトボール大会「Homers for Conrad」主催など。
8. 妄想耽溺とエスカレーション: 相談相手から始まり、耐性形成により刺激に飢えたカーターは、共感から方法提示、日時催促、自尊心を傷つける挑発へと激化し、車外に逃げ出した彼を死へと連れ戻す通話命令に至りました。
9. 後光効果と社会的盲点: 郊外の中産階級、笑顔の少女という属性がハロー効果を形成。「無邪気な少女が遠隔で人を死に追いやるはずがない」という認知の盲点により、捜査が進むまで誰も見抜けませんでした。
10. 被害者学と生存レッドフラッグ: コンラッド・ロイ3世の名誉を回復するとともに、『The Gift of Fear』に基づく4つの生存警告を提示：(1) 家族や医療から孤立させる関係、(2) 自傷的な証明を迫る挑発、(3) 個人の苦悩を注目集めの道具にする行為、(4) 違和感を覚えたら直感に従い直ちに連絡を絶ち専門家に相談すること。

⏱ 目次（チャプター）
00:00 オープニング＆視聴にあたって
00:23 第1幕 · Kマート駐車場での運命の朝
04:10 第2幕 · 2万通のテキストメッセージの迷宮
07:41 第3幕 · 悲劇のヒロイン劇と自己愛性パーソナリティ
11:06 第4幕 · 自白テキストと歴史的有罪判決
14:54 第5幕 · デジタル空間の倫理とコンラッド法

⚠️ ご視聴にあたっての注意事項
• 本動画は教育、歴史的ドキュメンタリーおよび犯罪心理学の観点からの分析であり、医療・法的な助言ではありません。
• 米国マサチューセッツ州最高司法裁判所および少年裁判所の公開記録に基づいています。
• キャラクター（フクロウ、オオカミ、キツネ等）は演出用の架空の表現です。音声・映像・音楽にAI技術（Higgs Audio等）を活用しています。

📚 公式参考資料・判決記録
• マサチューセッツ州最高司法裁判所 — Commonwealth v. Michelle Carter 事件記録: https://www.supremecourt.gov/
• ブリストル郡少年裁判所 — ローレンス・モニズ判事による判決文: https://www.masslive.com/
• マサチューセッツ州議会 — 上院法案 S.1032（コンラッド法）: https://malegislature.gov/
• 米国立衛生研究所（NCBI / StatPearls） — インターネット・ミュンヒハウゼン症候群: https://www.ncbi.nlm.nih.gov/books/NBK518999/
• ジェシー・バロン: 『プレインビルから来た少女』(Esquire) およびゴードン捜査官報告書。
* 全21件の公的資料および56件の事実対照表は以下に保存：02_SAN_XUAT/Tap07/nguon_tham_khao.md

🆘 相談窓口・支援ホットライン（24時間無料）
• よりそいホットライン：0120-279-338（24時間対応・多言語対応）
• こころの健康相談統一ダイヤル：0570-064-556
• 児童相談所虐待対応ダイヤル：189（いちはやく）
• 警察相談専用電話：#9110

#犯罪心理学 #TrueCrime #ミシェルカーター #コンラッドロイ #10の心理指標 #レッドフラッグ #マインドコントロール #自己愛性パーソナリティ #ドキュメンタリー #AmberEyes #コンラッド法"""

# ==============================================================================
# 5. BẢN MÔ TẢ ĐẦY ĐỦ TIẾNG HÀN (TỐI ƯU HOÁ STRICTLY <= 5,000 KÝ TỰ)
# ==============================================================================
DESC_KO = """07화 · 문자로 내린 살인 판결――디지털 조작의 덫 | 범죄심리학: 미셸 카터 & 콘래드 로이 사건 (10대 심리 지표와 가상공간의 비극) | Amber eyes

2014년 7월 13일 아침, 미국 매사추세츠주 페어헤이븐의 케이마트(Kmart) 주차장. 출동한 경찰은 주차장 구석에 세워진 녹색 포드 F-250 픽업트럭 내부에서 18세 청년 콘래드 로이 3세의 시신을 발견했습니다. 콘래드는 우수한 성적으로 고등학교를 졸업하고 가문의 전통인 예인선 선장 면허를 취득한 성실한 청년이었으나, 극심한 우울감에 시달리고 있었습니다. 경찰이 휴대전화를 디지털 포렌식 복구하자, 50km 떨어진 플레인빌에 사는 17세 여자친구 미셸 카터와 주고받은 2만 건이 넘는 문자가 드러났습니다. 미셸은 치료를 권하는 대신, 피해자의 고통을 '비련의 여주인공' 연극의 무대 장치로 악용하고 있었습니다.

2014년 7월 12일 밤부터 13일 새벽, 생존 본능으로 차량 밖으로 탈출한 콘래드에게 미셸 카터는 47분간의 통화 속에서 차갑게 명령했습니다――"다시 차 안으로 들어가." 로런스 모니즈 판사의 역사적인 과실치사 유죄 판결과 매사추세츠주 대법원의 판결 확정은, 가상공간에서 벌어지는 원격 심리 조작의 치명적 폭력을 입증한 사법적 이정표가 되었습니다.

Amber eyes는 본 사건을 '10대 핵심 심리·행동 지표 생태계'를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 파라노이아: 범죄 현장에 없던 인물이 50km 떨어진 곳에서 전송한 문자와 통화만으로 유죄를 선고받은 최초의 판결. 온라인상의 언어 폭력의 파괴력을 입증하며 학부모들에게 큰 충격을 안겼고, 원격 자해 강요를 처벌하는 '콘래드 법(Conrad's Law)' 제정을 촉발했습니다.
2. 피해자의 사물화(Objectification): 콘래드를 한 인간이 아닌, 자신이 기획한 비극적 드라마를 위한 '살아있는 소품'으로 취급했습니다. 정서적 공감 결핍으로 인해 피해자의 공포를 느끼지 못하고, 그의 죽음을 자신을 향한 조명으로 삼았습니다.
3. 인지적 구획화(Compartmentalization): 낮에는 운동에 전념하고 화목한 가정이라는 '정상성의 방패' 뒤에 숨은 학생, 밤에는 휴대폰을 통해 취약한 피해자의 생존 본능을 파괴하는 포식자라는 두 삶을 완벽하게 분리했습니다.
4. 나르시시즘적 붕괴와 병적 자기연민: 포렌식 증거로 법정에서 유죄가 선고되자 선량한 가면은 산산조각 났습니다. 유족에 대한 참회 대신 병적인 자기연민에 빠져들었으며, 미국 연방대법원까지 상고를 거듭하며 책임을 회피했습니다.
5. 자기 정당화 및 중화 기술: '피해자 비난'(망설이는 콘래드를 질책), '영웅 콤플렉스'(천국으로 보내준다는 왜곡된 이타주의), 그리고 '책임의 외재화'(항우울제 셀렉사 복용으로 인한 취약 상태 주장)를 통해 죄책감을 무력화했습니다.
6. 심리적 방아쇠와 티핑 포인트: 2014년 7월 초, 교내에서의 소외감과 콘래드의 계속되는 망설임이 맞물린 순간. 콘래드가 행동하지 않으면 자신이 거짓말쟁이로 드러날 것이라는 공포가 방아쇠가 되어 행동 강요자로 폭주했습니다.
7. 시그니처 vs 범행 수법(MO): 수법(연속 SMS, 심야 통화, 메시지 삭제 지시)은 진화한 반면, 불변의 시그니처는 '비련의 여주인공'을 향한 집착: 드라마 《Glee》 대사 모방, 사망 전 실종 예고, 사후 추모 소프트볼 대회 'Homers for Conrad' 주최 등.
8. 환상 중독과 에스컬레이션: 상담에서 시작된 관계는 자극 내성 형성으로 심화되었습니다. 공감에서 수단 제시, 일정 독촉, 자존심을 짓밟는 도발("행동하지 않으면 넌 말뿐이야")로 수위를 높였으며, 결국 차 밖으로 도망친 피해자를 죽음으로 밀어 넣는 명령에 도달했습니다.
9. 후광 효과와 제도의 맹점: 중산층, 밝은 미소의 소녀라는 외적 조건이 완벽한 후광 효과를 형성했습니다. 학교와 교사들은 순진한 소녀가 누군가를 조작할 리 없다는 편견의 맹점에 갇혀 실체를 인지하지 못했습니다.
10. 피해자학 및 생존 레드플래그: 콘래드 로이 3세의 명예와 존엄을 회복하고, 《The Gift of Fear》에 기반한 4대 생존 경고를 제시: (1) 가족 및 전문 의료기관과의 단절을 유도하는 관계, (2) 자존심을 건드리며 자해적 행동을 증명하라고 압박하는 행위, (3) 타인의 고통을 SNS 관심 도구로 삼는 태도, (4) 위험을 감지했을 때 직관을 믿고 즉시 관계를 차단하며 전문기관에 도움을 요청할 것.

⏱ 챕터(타임라인)
00:00 오프닝 & 시청 안내
00:23 제1막 · 케이마트 주차장의 운명적인 아침
04:10 제2막 · 2만 통의 문자 메시지 미로
07:41 제3막 · 비련의 여주인공 연극과 연극성 심리
11:06 제4막 · 자백 문자 메시지와 역사적 유죄 판결
14:54 제5막 · 사이버 공간의 윤리와 콘래드 법

⚠️ 시청 전 법적 유의사항
• 본 콘텐츠는 교육, 범죄심리학 및 역사적 분석 목적의 다큐멘터리이며, 의학적 또는 법률적 조언을 대신할 수 없습니다.
• 미국 매사추세츠주 대법원 및 브리스톨 카운티 소년법원의 공판 기록을 바탕으로 제작되었습니다.
• 등장하는 동물 캐릭터는 예술적 연출이며, 음성·시각·음악에 AI 기술(Higgs Audio 등)이 활용되었습니다.

📚 공식 참고자료 및 공판 기록
• 매사추세츠주 대법원 — Commonwealth v. Michelle Carter 판결문: https://www.supremecourt.gov/
• 브리스톨 소년법원 — 로런스 모니즈 판사의 유죄 판결문: https://www.masslive.com/
• 매사추세츠주 의회 — 상원 법안 S.1032 (콘래드 법): https://malegislature.gov/
• 미국 국립의학도서관(NCBI / StatPearls) — 인터넷 뮌하우젠 증후군: https://www.ncbi.nlm.nih.gov/books/NBK518999/
• 제시 배런: 《플레인빌에서 온 소녀》(Esquire) 및 스콧 고든 수사관 보고서.
* 21개 공식 출처 및 56개 사실 대조표는 다음 파일에 보관: 02_SAN_XUAT/Tap07/nguon_tham_khao.md

🆘 위기 상담 및 피해자 지원 핫라인 (24시간 무료)
• 정신건강 위기상담전화: 1577-0199 (24시간)
• 청소년 상담전화: 국번없이 1388 (24시간)
• 아동학대 예방 및 신고 상담전화: 국번없이 112 또는 129
• 여성긴급전화: 국번없이 1366

#AmberEyes #범죄심리학 #TrueCrime #미셸카터 #콘래드로이 #10대심리지표 #레드플래그 #디지털조작 #연극성성격장애 #다큐멘터리 #콘래드법"""

# ==============================================================================
# 6. ĐO ĐẠC ĐỘ DÀI VÀ KIỂM ĐỊNH TRẦN 5000 KÝ TỰ (RULE L3)
# ==============================================================================
descs = {
    "VI": DESC_VI,
    "EN": DESC_EN,
    "JA": DESC_JA,
    "KO": DESC_KO,
}

print("=== KIỂM ĐỊNH ĐỘ DÀI MÔ TẢ TẬP 07 (TRẦN YOUTUBE <= 5,000 KÝ TỰ) ===")
all_pass = True
for lang, content in descs.items():
    cnt = len(content)
    is_ok = cnt <= 5000
    status = f"PASS ({cnt:,} / 5,000 ký tự)" if is_ok else f"FAIL (> 5,000: {cnt:,})"
    print(f"[{lang}] Độ dài mô tả: {status}")
    if not is_ok:
        all_pass = False

if not all_pass:
    print("\n>>> CẢNH BÁO: CÓ BẢN MÔ TẢ VƯỢT QUÁ 5,000 KÝ TỰ! DỪNG LẠI. <<<")
    sys.exit(1)

print("\n>>> TẤT CẢ 4 BẢN MÔ TẢ ĐÃ ĐẠT CHUẨN ĐẦY ĐỦ 10 CHỈ DẤU VÀ STRICTLY <= 5,000 KÝ TỰ! <<<\n")

# ==============================================================================
# 7. GHI FILE TOÀN BỘ 18 ĐÍCH
# ==============================================================================
files_to_write = [
    # 1. TIẾNG VIỆT
    (ROOT / "02_SAN_XUAT" / "Tap07" / "nguon_mo_ta.txt", SOURCES_VI_FULL),
    (ROOT / "02_SAN_XUAT" / "Tap07" / "mo_ta.txt", DESC_VI),
    (ROOT / "02_SAN_XUAT" / "Tap07" / "xuat_ban" / "mo_ta.txt", DESC_VI),

    # 2. TIẾNG ANH
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN_FULL),
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "mo_ta.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "xuat_ban" / "description.txt", DESC_EN),
    (ROOT / "02_SAN_XUAT" / "Tap07_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),

    # 3. TIẾNG NHẬT
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA_FULL),
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "mo_ta.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "xuat_ban" / "description.txt", DESC_JA),
    (ROOT / "02_SAN_XUAT" / "Tap07_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),

    # 4. TIẾNG HÀN
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO_FULL),
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "mo_ta.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "xuat_ban" / "description.txt", DESC_KO),
    (ROOT / "02_SAN_XUAT" / "Tap07_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
]

written = 0
for path, text in files_to_write:
    path.parent.mkdir(parents=True, exist_ok=True)
    clean_text = text.strip() + "\n"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(clean_text)
    raw_bytes = path.read_bytes()
    assert b"\r\r\n" not in raw_bytes, f"LỖI T19: phát hiện \\r\\r\\n trong {path}"
    written += 1
    print(f"[{written:02d}/18] Đã ghi thành công: {path.relative_to(ROOT)} ({len(clean_text):,} ký tự)")

print(f"\nHoàn tất ghi toàn bộ 18 file mô tả & hồ sơ nguồn cho Tập 07!")
