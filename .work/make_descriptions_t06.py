#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tạo và cập nhật mô tả video đạt chuẩn 10 chỉ dấu tâm lý cho Tập 06 trên cả 4 ngôn ngữ (VI, EN, JA, KO)."""

import os
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# 1. NGUỒN TIẾNG VIỆT
SOURCES_VI = """• [1] Wikipedia — John Wayne Gacy:
  https://en.wikipedia.org/wiki/John_Wayne_Gacy
• [2] Clark County State's Attorney (IL) — hồ sơ vụ án Gacy #237:
  http://www.clarkprosecutor.org/html/death/US/gacy237.htm
• [3] Chicago Tribune — dòng thời gian vụ án:
  https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html
• [4] Chicago Tribune — 40 năm sau, danh sách nạn nhân:
  https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html
• [5] A&E — xét xử vụ Gacy:
  https://www.aetv.com/articles/gacys-trial
• [6] A&E — vụ bắt giữ và khám xét nhà:
  https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case
• [7] A&E — Case File: John Wayne Gacy:
  https://www.aetv.com/articles/john-wayne-gacy
• [8] Encyclopedia.com — hồ sơ xét xử 1980:
  https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980
• [9] Biography.com — John Wayne Gacy:
  https://www.biography.com/crime/john-wayne-gacy
• [10] Netflix Tudum — hồ sơ loạt phim tài liệu:
  https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know
• [11] Slate — đánh giá 'Devil in Disguise':
  https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html
• [12] Solve The Case — hồ sơ nghi phạm:
  https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr
• [13] Joyce & Stover — 'Witnesses from the Grave' (sách):
  https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt
• [14] Esquire — phỏng vấn cựu thám tử Albrecht:
  https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/
• [15] Oxygen — cách Gacy bị phát hiện:
  https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught
• [16] TheWrap — lời khai thám tử Des Plaines:
  https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/
• [17] NBC News — docuseries và các nạn nhân:
  https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590
• [18] LegalNews (AP) — 'Defending a Monster':
  https://www.legalnews.com/Home/Articles?DataId=1038560
• [19] Chicago Bar Association — bản vụ của William Kunkle:
  https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/
• [20] Den of Geek — đánh giá 'Devil in Disguise':
  https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/"""

# 2. NGUỒN TIẾNG ANH
SOURCES_EN = """• [1] Wikipedia — John Wayne Gacy:
  https://en.wikipedia.org/wiki/John_Wayne_Gacy
• [2] Clark County State's Attorney (IL) — Case File #237:
  http://www.clarkprosecutor.org/html/death/US/gacy237.htm
• [3] Chicago Tribune — Complete Case Timeline:
  https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html
• [4] Chicago Tribune — 40 Years Later, Victims Roster:
  https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html
• [5] A&E — The Trial of John Wayne Gacy:
  https://www.aetv.com/articles/gacys-trial
• [6] A&E — Capture and Search of the Summerdale Residence:
  https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case
• [7] A&E — Case File: John Wayne Gacy:
  https://www.aetv.com/articles/john-wayne-gacy
• [8] Encyclopedia.com — 1980 Trial Record:
  https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980
• [9] Biography.com — John Wayne Gacy Biography:
  https://www.biography.com/crime/john-wayne-gacy
• [10] Netflix Tudum — Documentary Profile:
  https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know
• [11] Slate — Peacock Documentary 'Devil in Disguise' Review:
  https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html
• [12] Solve The Case — Offender Profile:
  https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr
• [13] Joyce & Stover — 'Witnesses from the Grave' (Archived Forensic Text):
  https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt
• [14] Esquire — Interview with Former Detective Mike Albrecht:
  https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/
• [15] Oxygen — The Brazen Way Serial Killer Gacy Got Caught:
  https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught
• [16] TheWrap — Des Plaines Detectives Interview:
  https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/
• [17] NBC News — Gacy Docuseries and the Victims:
  https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590
• [18] LegalNews (AP) — 'Defending a Monster':
  https://www.legalnews.com/Home/Articles?DataId=1038560
• [19] Chicago Bar Association — The Prosecution of John Wayne Gacy (William Kunkle):
  https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/
• [20] Den of Geek — Review of 'Devil in Disguise':
  https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/"""

# 3. NGUỒN TIẾNG NHẬT
SOURCES_JA = """• [1] Wikipedia — ジョン・ウェイン・ゲイシー（John Wayne Gacy）：
  https://en.wikipedia.org/wiki/John_Wayne_Gacy
• [2] クラーク郡検察局（イリノイ州）— ゲイシー事件記録 #237：
  http://www.clarkprosecutor.org/html/death/US/gacy237.htm
• [3] シカゴ・トリビューン — 事件完全タイムライン：
  https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html
• [4] シカゴ・トリビューン — 40年後の検証・犠牲者名簿：
  https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html
• [5] A&E — ジョン・ウェイン・ゲイシーの裁判記録：
  https://www.aetv.com/articles/gacys-trial
• [6] A&E — サマーデール通りの捜索と逮捕の経緯：
  https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case
• [7] A&E — 事件ファイル：ジョン・ウェイン・ゲイシー：
  https://www.aetv.com/articles/john-wayne-gacy
• [8] Encyclopedia.com — 1980年公判記録：
  https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980
• [9] Biography.com — ジョン・ウェイン・ゲイシーの生涯と犯罪：
  https://www.biography.com/crime/john-wayne-gacy
• [10] Netflix Tudum — ドキュメンタリー特集・ゲイシーの素顔：
  https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know
• [11] Slate — Peacockドキュメンタリー『仮面を被った悪魔』批評：
  https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html
• [12] Solve The Case — 犯人プロファイル記録：
  https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr
• [13] ジョイス＆ストーバー — 『墓場からの証人』（法医人類学アーカイブ）：
  https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt
• [14] エスクァイア — 元捜査官マイク・アルブレヒト単独インタビュー：
  https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/
• [15] Oxygen — 連続殺人犯ゲイシーが自滅した大胆な手口：
  https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught
• [16] TheWrap — デス・プレーンズ警察捜査官インタビュー：
  https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/
• [17] NBC News — ドキュメンタリーシリーズと犠牲者たちの記録：
  https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590
• [18] LegalNews (AP) — 『怪物弁護記（Defending a Monster）』：
  https://www.legalnews.com/Home/Articles?DataId=1038560
• [19] シカゴ弁護士会 — ウィリアム・カンクル検事による公判記録：
  https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/
• [20] Den of Geek — 『仮面を被った悪魔』作品レビュー：
  https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/"""

# 4. NGUỒN TIẾNG HÀN
SOURCES_KO = """• [1] Wikipedia — 존 웨인 게이시 (John Wayne Gacy):
  https://en.wikipedia.org/wiki/John_Wayne_Gacy
• [2] 클라크 카운티 검찰청 (일리노이주) — 사건 파일 #237:
  http://www.clarkprosecutor.org/html/death/US/gacy237.htm
• [3] 시카고 트리뷴 — 사건 종합 타임라인:
  https://graphics.chicagotribune.com/john-wayne-gacy-new-timeline/blurb.html
• [4] 시카고 트리뷴 — 40년 후 재조명, 희생자 명단:
  https://graphics.chicagotribune.com/john-wayne-gacy-murders-40-years-later/index.html
• [5] A&E — 존 웨인 게이시의 공판 기록:
  https://www.aetv.com/articles/gacys-trial
• [6] A&E — 서머데일 주택 압수수색 및 체포 과정:
  https://www.aetv.com/articles/john-wayne-gacy-capture-missing-teen-case
• [7] A&E — 사건 파일: 존 웨인 게이시:
  https://www.aetv.com/articles/john-wayne-gacy
• [8] Encyclopedia.com — 1980년 재판 공식 기록:
  https://www.encyclopedia.com/law/law-magazines/john-wayne-gacy-trial-1980
• [9] Biography.com — 존 웨인 게이시 전기 및 범죄 분석:
  https://www.biography.com/crime/john-wayne-gacy
• [10] Netflix Tudum — 다큐멘터리 프로파일:
  https://www.netflix.com/tudum/articles/who-was-john-wayne-gacy-everything-to-know
• [11] Slate — Peacock 다큐멘터리 '가면을 쓴 악마' 리뷰:
  https://slate.com/culture/2021/03/john-wayne-gacy-devil-in-disguise-documentary-peacock.html
• [12] Solve The Case — 가해자 프로파일:
  https://www.solvethecase.org/offender/2026-071/john-wayne-gacy-jr
• [13] 조이스 & 스토버 — 《무덤에서 온 증인들》(법의인류학 아카이브):
  https://archive.org/stream/B-001-016-569/B-001-016-569_djvu.txt
• [14] 에스콰이어 — 전직 수사관 마이크 알브레히트 단독 인터뷰:
  https://www.esquire.com/entertainment/tv/a35927993/michael-albrecht-john-wayne-gacy-interview-confession-additional-bodies-accomplices/
• [15] Oxygen — 연쇄 살인마 게이시가 덜미를 잡힌 대담한 행적:
  https://www.oxygen.com/true-crime-buzz/the-brazen-way-that-serical-killer-john-wayne-gacy-got-caught
• [16] TheWrap — 데스플레인스 수사관 인터뷰:
  https://www.thewrap.com/john-wayne-gacy-devil-in-disguise-detectives-interview/
• [17] NBC News — 게이시 다큐시리즈와 희생자들:
  https://www.nbcnews.com/news/us-news/john-wayne-gacy-docuseries-asks-if-he-might-have-killed-n1261590
• [18] LegalNews (AP) — 《괴물을 변호하다 (Defending a Monster)》:
  https://www.legalnews.com/Home/Articles?DataId=1038560
• [19] 시카고 변호사협회 — 윌리엄 쿤클 검사의 공판 회고:
  https://legaltalknetwork.com/podcasts/chicago-bar/2019/02/the-killer-clown-edition-the-prosecution-of-john-wayne-gacy/
• [20] Den of Geek — '가면을 쓴 악마' 작품 분석:
  https://www.denofgeek.com/tv/john-wayne-gacy-devil-in-disguise-review/"""

# TOÀN BỘ MÔ TẢ TIẾNG VIỆT
DESC_VI = f"""Tập 06: Nụ Cười Chú Hề & 29 Bí Mật Dưới Sàn Nhà | Tâm lý học tội phạm: John Wayne Gacy (10 Chỉ Dấu Tâm Lý & Chiếc Mặt Nạ Ái Kỷ) | Amber eyes

Vào ngày 6 tháng 5 năm 1978, tại buổi lễ diễu hành mừng Ngày Hiến pháp Ba Lan ở thành phố Chicago, một người đàn ông trung niên bảnh bao, mỉm cười tự tin bắt tay Đệ nhất phu nhân Hoa Kỳ Rosalynn Carter. Trên ngực áo vest của người đàn ông là chiếc huy hiệu mang chữ "S" do Cơ quan Mật vụ Hoa Kỳ cấp — dấu hiệu chứng nhận quyền tiếp cận khu vực an ninh đặc biệt. Người đàn ông đó là John Wayne Gacy (36 tuổi): một chủ thầu xây dựng thành đạt của công ty PDM Contractors, một đội trưởng khu dân cư năng nổ của Đảng Dân chủ tại Norwood Park, và là người thường xuyên khoác lên mình bộ trang phục rực rỡ mang tên "Chú hề Pogo" để đem lại tiếng cười miễn phí cho các bệnh nhi tại các bệnh viện địa phương. Trong mắt cộng đồng ngoại ô Chicago, Gacy là hiện thân trọn vẹn của "giấc mơ Mỹ" — một công dân gương mẫu, nhiệt thành và đầy lòng nhân ái.

Thế nhưng, đằng sau lớp phấn trắng, nụ cười chú hề vẽ vụng và chiếc mặt nạ công dân hoàn hảo ấy là một trong những kẻ săn mồi tàn độc nhất lịch sử tội phạm hiện đại. Chỉ 7 tháng sau bức ảnh chụp cùng Đệ nhất phu nhân, vào đêm ngày 11 tháng 12 năm 1978, cậu thiếu niên 15 tuổi Robert Piest — một học sinh lớp 10 gương mẫu đang làm thêm tại hiệu thuốc Nisson — đã biến mất không dấu vết sau khi bước ra ngoài nói chuyện với Gacy về lời hứa công việc phụ việc xây dựng với mức thù lao 5 USD một giờ. Cuộc điều tra kiên trì và cuộc bám đuôi nghẹt thở suốt 24/7 của các thám tử Sở Cảnh sát Des Plaines cuối cùng đã dẫn họ bước vào căn nhà gạch số 8213 West Summerdale Avenue.

Tại đây, bên dưới khoảng bò chật hẹp chỉ cao 46 cm ngập trong bùn đất ẩm ướt và lớp vôi sống, các điều tra viên đã bàng hoàng phát hiện ra một hố chôn tập thể kinh hoàng: thi thể của 29 thanh thiếu niên bị siết cổ bằng dây thừng garrote và giấu kín ngay dưới sàn nhà nơi Gacy sinh hoạt mỗi ngày, cùng 4 nạn nhân khác bị ném xuống dòng sông Des Plaines khi khoảng tối dưới sàn đã không còn chỗ trống. Tổng cộng 33 sinh mạng thanh xuân đã bị chôn vùi dưới nụ cười của một kẻ mang chứng rối loạn nhân cách chống đối xã hội và ái kỷ ác tính.

Hồ sơ John Wayne Gacy được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG MANG TẬP THỂ: Vụ án làm sụp đổ hoàn toàn niềm tin vào cộng đồng ngoại ô bình yên của nước Mỹ thập niên 1970; một nhân vật uy tín của Đảng Dân chủ địa phương, chủ thầu xây dựng thành đạt, người hóa trang "chú hề Pogo" đem nụ cười đến các bệnh viện nhi lại là kẻ săn mồi sát hại 33 thanh thiếu niên; cú sốc xã hội làm dấy lên nỗi sợ hãi kéo dài và thay đổi vĩnh viễn hệ thống giám sát người từng có tiền án xâm hại.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Hắn tước đoạt toàn bộ nhân tính của những chàng trai trẻ, biến họ thành công cụ sinh học vô danh nhằm kích hoạt ảo tưởng kiểm soát tối thượng và nhục dục bệnh hoạn; coi họ là những vật thể tiêu hao có thể tùy ý giam giữ, bóp nghẹt và vứt bỏ dưới lòng đất như rác thải xây dựng.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Xây dựng hai thực tại hoàn toàn cách biệt mà không chút mâu thuẫn nội tâm: ban ngày là nhà thầu PDM năng nổ, người hàng xóm hào phóng tổ chức tiệc nướng, nhân vật chính trị đeo huy hiệu an ninh Mật vụ chụp ảnh cùng Đệ nhất phu nhân; nhưng đêm xuống là kẻ săn mồi lạnh lùng siết chặt sợi dây thừng quanh cổ nạn nhân ngay trong chính ngôi nhà của mình.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Khi đối diện chứng cứ vật chất không thể chối cãi (biên nhận ảnh hiệu thuốc, chiếc nhẫn khắc chữ JAS của nạn nhân John Szyc) và vòng vây giám sát 24/7 của cảnh sát Des Plaines, chiếc mặt nạ vị tha và ngạo mạn rơi xuống; hắn trốn vào chiêu bài "đa nhân cách Jack Hanley", tự nhận "Tôi là nạn nhân thứ 34", bám víu vào sự thương hại bản thân và từ chối mọi sự ăn năn chân thành cho đến khi bị hành quyết năm 1994.
5. HỆ THỐNG TỰ BÀO CHỮA (TECHNIQUES OF NEUTRALIZATION): Triệt để sử dụng kỹ thuật "đổ lỗi cho nạn nhân" và "chối bỏ trách nhiệm": ngụy biện rằng các chàng trai trẻ tự nguyện vào nhà hắn vì tiền hoặc ma túy, tự chuốc lấy kết cục bi thảm; tự đóng vai nạn nhân bị hoàn cảnh ép buộc để xoa dịu lương tâm méo mó.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Tuổi thơ bị bạo hành tàn bạo cả thể xác lẫn tinh thần bởi người cha nghiện rượu (liên tục bị sỉ nhục là "kẻ ẻo lả, vô tích sự"), căn bệnh tim bẩm sinh và chấn thương đầu năm 11 tuổi đã gieo mầm mặc cảm bất lực cùng cực; điểm gãy bùng phát khi bản án 10 năm tù tại Iowa (1968) phá nát vỏ bọc danh dự, biến khát khao bù trừ ái kỷ thành sự cuồng loạn kiểm soát sự sống chết của người khác.
7. SIGNATURE VS. THỦ ĐOẠN MO: MO liên tục thay đổi: từ dụ dỗ làm việc thêm lương 5 USD/giờ (cao gấp đôi mức tối thiểu), giả danh cảnh sát đến trò ảo thuật còng tay ("rope trick / handcuffs") để vô hiệu hóa phản kháng; Signature bất biến: ép buộc nạn nhân vào trạng thái hoàn toàn bất lực để tận hưởng cảm giác thống trị tuyệt đối, siết cổ bằng cây gậy xoắn (garrote) và chôn cất thi thể ngay dưới không gian sinh hoạt của chính mình.
8. QUỸ ĐẠO LEO THANG ẢO TƯỞNG: Bắt đầu từ xâm hại tình dục đơn lẻ ở Iowa, sau khi ra tù hắn nhanh chóng leo thang sang giết người hàng loạt; tần suất tăng vọt từ năm 1972 đến 1978 (riêng giai đoạn 1976–1977 chôn hàng chục thi thể dưới sàn nhà), ngưỡng kích thích tăng dần theo sự trơ lỳ cảm xúc cho đến khi khoảng bò 46 cm dưới nền nhà hết chỗ và phải ném 4 xác xuống sông Des Plaines.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc "chú hề Pogo" từ thiện, tấm huy hiệu "S" của Mật vụ Mỹ chụp cùng Đệ nhất phu nhân Rosalynn Carter, cùng vị thế chủ thầu xây dựng tạo nên hào quang công dân gương mẫu hoàn hảo; các cơ quan thực thi pháp luật và cộng đồng đã phớt lờ nhiều đơn trình báo và lời khai trốn thoát của các nạn nhân trong nhiều năm.
10. CẢNH BÁO ĐỎ SINH TỒN: 4 tín hiệu nhận diện kẻ săn mồi đội lốt người tốt: (1) Những lời mời làm việc với mức thù lao bất thường cao ngoài giờ dành cho thiếu niên; (2) Yêu cầu tham gia các trò chơi ảo thuật trói buộc hoặc cho phép đeo còng tay thử; (3) Mùi xú khí bất thường trong nhà bị ngụy trang bằng vôi sống hoặc hóa chất khử mùi nồng nặc; (4) Vẻ quyến rũ bề ngoài quá mức (superficial charm) kết hợp với thái độ kiểm soát áp đặt và tiền án giấu kín trong quá khứ.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Bức ảnh với Đệ nhất phu nhân và cậu bé hiệu thuốc
05:10 Hồi 2 · Hiện trường & Quỹ đạo leo thang của vực thẳm
10:45 Hồi 3 · Giải phẫu tâm lý — Sự chia ngăn nhận thức & Khoảng tối Summerdale
16:30 Hồi 4 · Đấu trí thẩm vấn & Sụp đổ vở kịch đa nhân cách
21:50 Hồi 5 · Phán quyết, bản án tâm lý & bài học cảnh báo đỏ sinh tồn

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai tại Hoa Kỳ (Tòa án Thượng thẩm Quận Cook, Sở Cảnh sát Des Plaines, Văn phòng Công tố Bang Illinois). Kênh không nhằm bôi nhọ hay tôn vinh bất kỳ cá nhân nào.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là hình tượng minh họa nghệ thuật. Lời của Điều tra viên, Chuyên gia và Nhân chứng là lời dựng lại dựa trên tư liệu lịch sử.
• Giọng đọc, hình ảnh và âm thanh được hỗ trợ bởi công nghệ AI.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 NGUỒN THAM KHẢO ĐÃ ĐỐI CHIẾU
Toàn bộ sự kiện, ngày tháng và trích dẫn trong video đã được đối chiếu từng câu với 20 nguồn công khai (hồ sơ tòa án, báo chí, văn bản luật, nghiên cứu học thuật):

{SOURCES_VI}

🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).
• Đường dây nóng can thiệp & phòng chống bạo lực gia đình: 1900 969 680
• National Center for Missing & Exploited Children (NCMEC - Hoa Kỳ): 1-800-843-5678 — https://www.missingkids.org
• National Sexual Assault Hotline (RAINN - Hoa Kỳ): 1-800-656-4673 — https://www.rainn.org
• Childhelp National Child Abuse Hotline (Hoa Kỳ): 1-800-422-4453 — https://www.childhelp.org

#AmberEyes #TrueCrime #CriminalPsychology #JohnWayneGacy #TheKillerClown #ChuHeSatNhan #TamLyToiPham #10ChiDauTamLy #CanhBaoDo #GiaiPhauTamLy #HoSoToiPham #Documentary"""

# TOÀN BỘ MÔ TẢ TIẾNG ANH
DESC_EN = f"""Ep. 06: The Killer Clown & 29 Secrets Under the Floor | Criminal Psychology: John Wayne Gacy (10 Psychological Markers & The Narcissistic Mask) | Amber eyes

On May 6, 1978, at the Polish Constitution Day parade in Chicago, a well-groomed, self-assured middle-aged man warmly shook hands with First Lady of the United States Rosalynn Carter. Pinned to the lapel of his tailored suit was an "S" clearance badge issued by the United States Secret Service—signifying special access to maximum security VIP areas. That man was 36-year-old John Wayne Gacy: a successful contractor heading PDM Contractors, an energetic Democratic precinct captain in Norwood Park, and a beloved local figure who regularly donned colorful costumes as "Pogo the Clown" to bring free entertainment and joy to sick children in pediatric hospital wards. To suburban Chicago, Gacy personified the quintessential American Dream—an industrious civic pillar, an outgoing neighbor, and a generous philanthropist.

Yet behind that thick greasepaint, the clumsy painted smile, and the flawless mask of civic virtue lurked one of the deadliest human predators in modern history. Just seven months after that famous photograph with the First Lady, on the freezing evening of December 11, 1978, 15-year-old Robert Piest—a conscientious sophomore working part-time at Nisson Pharmacy—vanished without a trace after stepping outside to speak with Gacy regarding a promised $5.00/hour construction job. The relentless investigation and grueling 24/7 mobile surveillance by detectives of the Des Plaines Police Department eventually breached the perimeter of his suburban brick ranch house at 8213 West Summerdale Avenue.

There, beneath an eighteen-inch-high crawl space submerged in damp mud, lime powder, and darkness, investigators unearthed an unimaginable mass grave: the remains of 29 young men and adolescent boys systematically garroted and concealed beneath the floorboards where Gacy entertained guests and slept every night, alongside four additional victims dumped into the Des Plaines River when the crawl space had reached maximum capacity. In total, 33 vibrant young lives were extinguished beneath the toxic smile of an antisocial and malignant narcissistic predator.

Amber eyes dissects the John Wayne Gacy case through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: The case utterly shattered the post-war American illusion of suburban safety; a respected local Democratic precinct captain, successful contractor, and beloved hospital volunteer clown was unmasked as a predatory serial killer of 33 young boys and men, sparking lasting nationwide dread and permanently reforming juvenile protection protocols.
2. OBJECTIFICATION OF VICTIMS: Gacy stripped his young victims of every shred of humanity, reducing them into disposable biological objects designed solely to stimulate and satisfy his perverse appetite for absolute dominance, before burying them like building debris beneath his floorboards.
3. COMPARTMENTALIZATION (THE DUAL REALITY): He maintained two completely partitioned existences without cognitive dissonance: by day, an energetic PDM contractor, a friendly neighbor hosting neighborhood pig roasts, and a politically connected figure shaking hands with First Lady Rosalynn Carter; by night, a cold-blooded predator tightening a tourniquet garrote in his secluded residence.
4. NARCISSISTIC COLLAPSE: When confronted by overwhelming physical evidence (the pharmacy photo receipt, the engraved JAS high school ring of John Szyc) and relentless 24/7 surveillance by Des Plaines detectives, his benevolent mask collapsed; he retreated into a fabricated "Jack Hanley multiple personality" defense, claimed "I am victim number 34," wallowing in pathological self-pity without remorse until his 1994 execution.
5. TECHNIQUES OF NEUTRALIZATION: He weaponized "denial of responsibility" and "condemnation of the condemners," arguing that runaway youths voluntarily entered his home for quick cash or substances, thus blaming the victims for their own demise while portraying himself as an unfairly targeted victim of societal malice.
6. PRECIPITATING TRIGGER & PSYCHOLOGICAL FRACTURES: Brutal physical and psychological abuse by an alcoholic father (who constantly belittled him as weak and worthless), a congenital heart defect, and childhood head trauma sowed deep seeds of inadequacy; his psychological breaking point occurred when his 1968 Iowa prison sentence destroyed his social facade, turning compensatory narcissistic rage into an uncontrollable obsession with lethal control.
7. SIGNATURE VS. MODUS OPERANDI (MO): His MO adapted dynamically—luring teens with promises of $5/hour construction work (nearly double the federal minimum wage), flashing badges, and using the "handcuff trick" to disarm resistance; his immutable Signature remained the psychological subjugation of helpless victims, tightening a garrote to experience total godlike dominion, and entombing their remains directly beneath his living space.
8. ESCALATION TRAJECTORY: Evolving from isolated sexual assaults in Iowa to mass homicide in Norwood Park; between 1972 and 1978, his killing frequency accelerated rapidly (concentrating dozens of burials between 1976 and 1977) as emotional desensitization raised his arousal threshold, until the 18-inch crawl space filled up, forcing him to dump his final four victims into the Des Plaines River.
9. HALO EFFECT & SOCIAL BLIND SPOTS: His public persona as "Pogo the Clown," the Secret Service "S" clearance pin worn beside First Lady Rosalynn Carter, and active civic involvement formed an impenetrable halo effect, causing local authorities and community members to overlook prior survivor complaints for years.
10. SURVIVAL RED FLAGS: Four vital warning signs to identify predatory exploitation: (1) Off-the-books job offers boasting unusually inflated wages targeted at vulnerable youth; (2) Coercive requests to demonstrate restraint devices, rope tricks, or handcuffs; (3) Pervasive putrid odors masked by lime powder or heavy industrial deodorizers; (4) Superficial charm masking sudden explosive outbursts of control and concealed criminal histories.

⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · The Photo with the First Lady and the Pharmacy Boy
05:10 Act 2 · The Crime Scene & The Escalation Trajectory of the Abyss
10:45 Act 3 · Psychological Autopsy — Cognitive Compartmentalization & The Summerdale Darkness
16:30 Act 4 · The Interrogation Duel & The Collapse of the Multiple Personality Masquerade
21:50 Act 5 · The Verdict, Psychological Sentence & Survival Red Flags

⚠️ LEGAL & SAFETY DISCLAIMER
• Produced exclusively for educational, criminological, and historical analysis; not medical or legal advice.
• Based on public US judicial archives (Cook County Circuit Court, Des Plaines Police Department, Illinois Attorney General's Office). No intent to defame, harass, or glorify any individual.
• Avatars (Owl, Wolf, Fox, Sheep, Cat) and dialogue are dramatized illustrations based on archival transcripts.
• Synthetic AI voices, visuals, and audio are utilized.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 VERIFIED SOURCES & COURT EXHIBITS
All events, dates, and direct quotes have been verified line-by-line against 20 public archival sources (court transcripts, police files, investigative books, and academic studies):

{SOURCES_EN}

🆘 CRISIS & CHILD PROTECTION HOTLINES (24/7, FREE & CONFIDENTIAL)
• National Center for Missing & Exploited Children (NCMEC - USA): 1-800-843-5678 — https://www.missingkids.org
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelp.org
• National Sexual Assault Hotline (RAINN - USA): 1-800-656-4673 — https://www.rainn.org
• Suicide & Crisis Lifeline (USA): Call or text 988 — https://988lifeline.org
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org

#AmberEyes #TrueCrime #CriminalPsychology #JohnWayneGacy #TheKillerClown #ForensicPsychology #PogoTheClown #10PsychologicalMarkers #SurvivalRedFlags #Documentary #AbyssTrajectory"""

# TOÀN BỘ MÔ TẢ TIẾNG NHẬT
DESC_JA = f"""第06話 · 殺人ピエロの笑顔と床下の29の秘密 | 犯罪心理学：ジョン・ウェイン・ゲイシー事件 (10の心理指標と自己愛の仮面) | Amber eyes

1978年5月6日、シカゴで開催されたポーランド憲法記念日パレード。仕立てのよいスーツを着こなした自信に満ちた中年男性が、米国のファーストレディ、ロザリン・カーター大統領夫人と温かい握手を交わしました。男性の胸元には、米シークレットサービス（特務警護部）が発行した「S」のバッジが光っていました。それはVIP専用警戒区域への無制限の出入りを許可された特別な人物であることを証明する証票でした。その男の名はジョン・ウェイン・ゲイシー（36歳）。建築会社PDMコントラクターズの成功した経営者であり、ノーウッド・パーク地区の民主党熱心な幹部、そして小児病棟の入院中の子どもたちに笑顔を届けるため、カラフルなピエロ「ポゴ」に扮して無償で慰問活動を続ける「町の誇る慈善家」でした。シカゴ郊外の市民たちの目には、ゲイシーは誠実で温かく、アメリカン・ドリームを体現した模範的市民に映っていました。

しかし、その分厚い白塗りメイクとぎこちなく描かれたピエロの笑顔の裏側には、近代犯罪史上最も凶悪かつ冷酷な連続殺人鬼の牙が隠されていました。大統領夫人との栄光の写真からわずか7か月後の1978年12月11日の凍てつく夜、ニッソン薬局でアルバイトをしていた15歳の真面目な少年ロバート・ピーストが、時給5ドル（当時の連邦最低賃金の約2倍）の建設アルバイトの勧誘を受け、ゲイシーと店外で言葉を交わしたのを最後に消息を絶ちました。デス・プレーンズ警察の捜査官たちによる執念の24時間密着追跡の末、捜査員たちはサマーデール通り8213番地のゲイシーの自宅へと突入しました。

そこで捜査官たちが目の当たりにしたのは、人間の想像を絶する光景でした。ゲイシーが毎夜眠り、友人を招いてバーベキューを楽しんでいた生活空間の真下、わずか46cmの湿った泥と消石灰に覆われた床下から、止血棒（ガロット）で絞殺された29名もの少年たちの遺体が発見されたのです。さらに、床下が満杯になった後に近隣のデス・プレーンズ川へ投げ捨てられた4名を合わせ、計33名もの尊い若者たちの未来が、自己愛性パーソナリティ障害と反社会的人格の怪物の手によって闇に葬られていました。

アンバーアイズ（Amber eyes）は、本事件を「10の核心的心理・行動指標エコシステム」を通じて解剖します：
1. 社会的余波と集団的不安・パラノイア: 1970年代米国の平穏な郊外神話を根本から覆した戦慄の事件。地域政界の信望を集める実業家であり、小児病棟を慰問する慈善ピエロ「ポゴ」の正体が、33名の少年を屠った冷酷な捕食者であったという事実は、全米に深いトラウマを刻み、未成年者保護体制を恒久的に変革しました。
2. 被害者の客体化（Objectification）: 犠牲となった若者たちから人間としての尊厳と人格を完全に剥奪し、絶対的な支配欲と病的な性的嗜癖を満たすためだけの「生体ツール」へと還元。遺体を建築廃材のように床下へと埋め捨てました。
3. 心理的区画化（Compartmentalization）: 昼は活動的な建設業者であり、近隣住民を招いてバーベキューを振る舞い、大統領夫人と握手を交わす「良き市民」、夜は自宅で冷酷に絞殺用のロープを締め上げる「捕食者」という2つの極端な世界を、一切の心理的葛藤なく完全に分離・維持しました。
4. 自己愛の崩壊（Narcissistic Collapse）: 写真の預かり証や犠牲者ジョン・シクのイニシャル入り指輪という動かぬ物的証拠、そして警察の24時間監視に直面した時、尊大な仮面は剥がれ落ちました。多重人格（ジャック・ハンリー）の狂言に逃げ込み、「私こそが34人目の犠牲者だ」と自己憐憫に浸り、1994年の死刑執行に至るまで真の悔悟を示すことはありませんでした。
5. 自己正当化と中和の技術（Techniques of Neutralization）: 「被害者非難（Victim Blaming）」と「責任の否認」を駆使し、若者たちが金や薬物目当てで自ら招いた事態であると強弁。自らを不当な偏見と司法の犠牲者として演出することで、内なる良心の呵責を無力化しました。
6. 心理的引き金（トリガー）と破綻点: アルコール依存症の父による日常的な家庭内暴力と人格否定（「軟弱者」「役立たず」という罵倒）、先天性の心臓疾患、11歳での頭部外傷が極度の劣等感を形成。1968年のアイオワ州での服役が社会的地位を打ち砕いたことを契機に、自己愛の代償欲求が生死を支配する暴走衝動へと転落しました。
7. 署名（Signature）対 手口（MO）: 手口（MO）は時給5ドルの好待遇（当時の連邦最低賃金の約2倍）での勧誘、警察バッジの提示、「手錠のマジック」など状況に応じて洗練。一方、不変の署名（Signature）は、完全に無力化した被害者の生死を手中に収める全能感の享受、止血棒を用いた絞殺、そして生活空間の直下への埋葬でした。
8. エスカレーション軌道: アイオワでの単独の性的加害から、出所後は連続殺人へと急速にエスカレート。1972年から1978年にかけて殺害頻度は加速し（1976〜1977年に集中埋葬）、刺激に対する耐性と感覚の麻痺により、床下の高さ46cmのスペースが埋まり尽くすとデス・プレーンズ川への遺棄へと発展しました。
9. 後光効果（ハロー効果）と社会的盲点: チャリティピエロ活動、シークレットサービスの特別許可ピンを胸に大統領夫人と並んだ写真、地域政界とのパイプが完璧な「後光」を形成。過去の脱出被害者の証言や通報が長年にわたり軽視・放置される致命的な盲点を生み出しました。
10. 生存のためのレッドフラッグ（警告信号）: 善人の仮面を被った捕食者を見破る4つの危険兆候：(1) 青少年に対する相場を著しく超えた高額バイトの勧誘、(2) 手錠や拘束具を用いた「手品」「脱出ゲーム」への誘い、(3) 消石灰や工業用消臭剤で覆いきれない室内の不自然な異臭、(4) 過剰な人当たりの良さ（表層的魅力）の裏に見え隠れする支配欲と隠蔽された前科。

⏱ 目次（チャプター）
00:00 オープニング＆視聴にあたって
00:23 第1幕 · ファーストレディとの写真と薬局の少年
05:10 第2幕 · 犯行現場と深淵のエスカレーション軌道
10:45 第3幕 · 徹底心理解剖――認知的区画化とサマーデールの暗闇
16:30 第4幕 · 取調の攻防と多重人格劇の崩壊
21:50 第5幕 · 判決、深層心理の代償と生存のためのレッドフラッグ

⚠️ ご視聴にあたっての注意事項
• 本動画は教育、歴史的ドキュメンタリーおよび犯罪心理学の観点からの分析・解説コンテンツであり、医学的、心理学的、または法的なアドバイスに代わるものではありません。
• 米国の公開記録（クック郡巡回裁判所記録、デス・プレーンズ警察捜査記録、イリノイ州司法長官記録）に基づいて制作されています。特定の個人を中傷または美化する意図は一切ありません。
• 登場するキャラクター（フクロウ、オオカミ、キツネ、羊、猫）は演出用の架空のキャラクターです。
• 音声、画像、音楽はAIツールを活用して制作されています。
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 参考資料・出典
本動画におけるすべての事件経過、日時、判決記録および心理分析は、以下の20件の公式公開記録と照合されています：

{SOURCES_JA}

🆘 相談窓口・支援ホットライン（通話無料・24時間受付）
• 児童相談所虐待対応ダイヤル：189（いちはやく・通話無料）
• 性犯罪・性暴力被害者のためのワンストップ支援センター：#8891（短縮ダイヤル）
• 警察相談専用電話：#9110（全国共通）
• よりそいホットライン（通話無料・多言語対応）：0120-279-338
• 米国・全米行方不明・被搾取児童センター（NCMEC）：1-800-843-5678 — https://www.missingkids.org

#犯罪心理学 #TrueCrime #ジョンウェインゲイシー #キラークラウン #殺人ピエロ #10の心理指標 #レッドフラッグ #心理解剖 #ドキュメンタリー #AmberEyes"""

# TOÀN BỘ MÔ TẢ TIẾNG HÀN
DESC_KO = f"""06화 · 살인 광대의 미소와 마루 밑 29개의 비밀 | 범죄심리학: 존 웨인 게이시 사건 (10대 심리 지표와 나르시시즘의 가면) | Amber eyes

1978년 5월 6일, 미국 시카고에서 열린 폴란드 헌법의 날 기념 퍼레이드. 말끔한 정장을 차려입은 자신감 넘치는 중년 남성이 미국의 퍼스트레이디 로절린 카터 여사와 환한 미소로 악수를 나누었습니다. 남성의 양복 깃에는 미국 비밀경호국(Secret Service)이 발급한 특별 보안 배지 'S' 핀이 빛나고 있었습니다. 이는 최고 등급의 VIP 경호 구역을 자유롭게 출입할 수 있는 특별 승인자임을 증명하는 표식이었습니다. 그 남자의 이름은 36세의 존 웨인 게이시. 번창하는 건설회사 PDM의 대표이자, 노우드 파크 지역 민주당 간부였으며, 어린이 병원의 아픈 아이들에게 웃음을 선물하기 위해 화려한 의상을 입고 광대 '포고'로 변신해 무보수 자선 활동을 펼치던 '모범 시민'이었습니다. 시카고 교외 주민들의 눈에 게이시는 성공과 온정을 겸비한 아메리칸 드림의 이상적인 표상이었습니다.

그러나 두터운 분장과 어색하게 그려진 광대의 미소 이면에는 현대 범죄 역사상 가장 잔혹한 포식자의 이빨이 숨겨져 있었습니다. 영부인과의 기념사진 촬영 후 불과 7개월이 지난 1978년 12월 11일 혹한의 밤, 니슨 약국에서 성실히 아르바이트를 하던 15세의 고교생 로버트 피스트가 시간당 5달러(당시 연방 최저임금의 약 2배)의 건축 보조 일자리를 제안받고 게이시와 대화를 나눈 뒤 흔적도 없이 사라졌습니다. 데스플레인스 경찰서 수사관들의 끈질긴 24시간 밀착 잠복 감시 끝에, 수사팀은 서머데일 8213번지 게이시의 주택에 대한 압수수색을 단행했습니다.

그곳에서 수사관들이 마주한 것은 인간의 상식을 아득히 뛰어넘는 참상이었습니다. 게이시가 매일 밤 잠을 자고 이웃들을 초대해 바비큐 파티를 열던 거실 바로 밑, 높이 46cm에 불과한 축축한 진흙과 소석회로 뒤덮인 마루 밑 기폐 공간(crawl space)에서 지혈봉(garrote)으로 목이 졸려 살해된 29구의 청소년 시신이 쏟아져 나온 것입니다. 마루 밑이 가득 차자 인근 데스플레인스 강에 내던져진 4명을 포함해, 총 33명의 찬란한 젊음이 악성 나르시시즘과 반사회성 성격장애를 지닌 괴물의 뒤틀린 미소 아래 암매장되어 있었습니다.

Amber eyes는 본 사건을 '10대 핵심 심리·행동 지표 생태계'를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 공포·불안: 1970년대 미국 교외 중산층 사회의 안전 신화를 송두리째 무너뜨린 충격적 비극. 지역 정계의 유력 인사, 성공한 건축업자, 어린이 병원을 찾던 자선 광대 '포고'의 정체가 33명의 소년과 청년을 사냥한 연쇄 살인마였다는 사실은 전미에 지울 수 없는 공포를 남겼으며, 청소년 보호 체계를 영구히 개혁시켰습니다.
2. 피해자의 사물화 및 객체화(Objectification): 무고한 청년들에게서 생명과 인격을 완전히 박탈하고, 자신의 왜곡된 지배욕과 병적인 성적 통제감을 충족하기 위한 일회용 '생체 도구'로 전락시켰으며, 살해 후에는 건축 폐기물처럼 자신의 마루 밑에 파묻었습니다.
3. 심리적 구획화(Compartmentalization): 낮에는 성실한 건설업체 대표이자 이웃을 초대해 바비큐 파티를 열고 영부인과 악수하는 '모범 시민', 밤에는 집 안에서 잔혹하게 올가미를 조이는 '포식자'라는 양극단의 삶을 내적 갈등이나 양심의 가책 없이 철저하게 분리·영위했습니다.
4. 나르시시즘적 붕괴(Narcissistic Collapse): 결정적인 현상 영수증과 피해자 존 시크의 이니셜(JAS)이 새겨진 졸업 반지, 그리고 경찰의 24시간 밀착 감시망 앞에 오만한 가면이 벗겨지자, 그는 가공의 '다중인격 잭 핸리'를 내세우며 "나야말로 34번째 피해자"라는 비열한 자기연민 뒤로 숨었으며, 1994년 사형 집행 순간까지 진정한 참회를 거부했습니다.
5. 자기 정당화 및 중화 기술(Techniques of Neutralization): '피해자 비난'과 '책임 부정'의 중화 기술을 극단적으로 악용하여, 돈이나 호기심 때문에 스스로 집을 찾아온 소년들의 탓으로 책임을 전가하고, 자신을 불공정한 사회와 사법 제도의 희생양으로 규정하며 죄책감을 지워버렸습니다.
6. 방아쇠가 된 심리적 트리거: 알코올 중독자 아버지의 일상적인 폭력과 모욕("나약하고 쓸모없는 놈"), 선천성 심장 질환과 11세 때의 뇌 손상이 뿌리 깊은 무력감과 결핍을 낳았습니다. 1968년 아이오와 교도소 복역으로 첫 사회적 가면이 파괴되자, 결핍된 자기애를 보상받으려는 충동이 타인의 생사를 통제하려는 파괴적 광기로 폭발했습니다.
7. 시그니처(Signature) vs 범행 수법(MO): 수법(MO)은 시간당 5달러의 파격적인 일자리 제안(당시 최저임금의 2배), 경찰 배지 사칭, '수갑 마술' 등 상황에 맞춰 진화한 반면, 불변의 시그니처(Signature)는 완전히 무력화된 피해자를 상대로 절대적 권력을 만끽하고, 지혈봉(garrote)을 조여 살해한 뒤 자신의 일상 생활공간 바로 아래 묻어두는 것이었습니다.
8. 에스컬레이션 궤적: 아이오와에서의 성범죄에서 출소 후 연쇄 살인으로 폭주. 1972년부터 1978년까지 살해 빈도는 기하급수적으로 증가했으며(1976~1977년 집중 매장), 자극 역치 붕괴로 인해 마루 밑 46cm 공간이 포화 상태에 이르자 데스플레인스 강으로 유기 장소를 넓혔습니다.
9. 후광 효과(Halo Effect)와 제도의 맹점: '광대 포고'라는 자선 활동, 비밀경호국 보안 배지를 달고 영부인과 찍은 사진, 지역 민주당 간부라는 직함이 완벽한 후광을 형성하여, 수년간 접수된 피해자들의 탈출 증언과 신고가 사법 당국과 사회에 의해 철저히 묵살당하는 치명적인 맹점을 초래했습니다.
10. 생존을 위한 레드플래그(경고 신호): 선한 가면을 쓴 포식자를 식별하는 4대 경고 신호: (1) 청소년을 대상으로 하는 비정상적으로 높은 보수의 비공식 아르바이트 제안, (2) 수갑이나 밧줄을 이용한 '마술 게임' 또는 신체 구속 요구, (3) 소석회나 방향제로도 감춰지지 않는 실내의 썩은 냄새, (4) 과도한 사교성과 표격적 매력 이면에 숨겨진 병적인 통제욕과 은폐된 범죄 전력.

⏱ 챕터(타임라인)
00:00 오프닝 & 시청 안내
00:23 제1막 · 영부인과의 사진과 약국 소년의 실종
05:10 제2막 · 범죄 현장과 심연의 에스컬레이션 궤적
10:45 제3막 · 심층 심리 분석 — 인지적 구획화와 서머데일의 어둠
16:30 제4막 · 심문실의 심리전과 다중인격극의 붕괴
21:50 제5막 · 판결, 심리적 심판과 생존을 위한 레드플래그

⚠️ 시청 전 법적 유의사항
• 본 콘텐츠는 교육, 범죄심리학 및 역사적 분석 목적의 다큐멘터리이며, 전문적인 의학적, 정신과적 또는 법률적 조언을 대신할 수 없습니다.
• 미국 공식 사법 기록(쿡 카운티 순회법원 판결문, 데스플레인스 경찰서 수사 기록, 일리노이주 법무장관 기록)을 바탕으로 제작되었습니다. 본 채널은 특정인을 비방하거나 미화하려는 의도가 전혀 없습니다.
• 등장하는 올빼미, 늑대, 여우, 양, 고양이는 시각적 연출을 위한 가상 캐릭터입니다.
• 본 영상의 음성, 시각 이미지, 음악은 AI 기술을 활용하여 제작되었습니다.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 공식 참고자료 및 공판 기록
본 영상의 모든 사건 개요, 날짜, 재판 진술 및 타임라인은 다음 20개 공식 공개 기록과 교차 검증되었습니다:

{SOURCES_KO}

🆘 위기 상담 및 피해자 지원 핫라인 (24시간 무료 & 비밀보장)
• 아동학대 예방 및 신고 상담전화: 국번없이 112 또는 129
• 여성긴급전화 (가정폭력·성폭력 상담): 국번없이 1366
• 경찰청 범죄신고: 국번없이 112
• 보건복지상담센터: 국번없이 129
• 청소년 전화 및 사이버상담: 국번없이 1388
• 미국 실종학대아동방지센터 (NCMEC): 1-800-843-5678 — https://www.missingkids.org

#AmberEyes #범죄심리학 #TrueCrime #존웨인게이시 #살인광대 #광대포고 #10대심리지표 #레드플래그 #사건기록 #다큐멘터리"""

# GHI FILE
files_to_write = [
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

for path, content in files_to_write:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print(f"Đã ghi: {path.relative_to(ROOT)} ({len(content)} ký tự)")

print("\nHoàn tất ghi toàn bộ 17 file mô tả & nguồn cho Tập 06!")
