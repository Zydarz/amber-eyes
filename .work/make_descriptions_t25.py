# -*- coding: utf-8 -*-
"""Sinh phần MÔ TẢ (YouTube description) cho TẬP 25 — Yoo Young-chul — ở 4 ngôn ngữ.

Cùng chuẩn với `make_descriptions_t24.py` (tập trước làm mẫu chuẩn):
  • Tiêu đề bản địa hoá + thương hiệu "Amber eyes"
  • Đoạn dẫn lấy nguyên văn từ kịch bản (1.02#1, 3.02#1)
  • "Hệ sinh thái 10 chỉ dấu tâm lý & hành vi" (§A2c / K10) — rút từ Hồi 3 + Hồi 5
  • Mốc chương ĐO THẬT (không phải ước lượng 5 phút/lần)
  • Khối nguồn có tên nguồn + link đã kiểm chứng (không bịa nguồn mới — L2)
  • Đường dây nóng hỗ trợ bản địa hoá + hashtag riêng theo tập
  • Kiểm độ dài ≤ 5000 ký tự (giới hạn YouTube)

MỐC CHƯƠNG (đo từ file thành phẩm, xem `.work/_act_times_t25.py`):
  VN: CanNghe_Tap25_higgs.md (230 câu)  → 00:23 / 07:40 / 13:22 / 21:09 / 28:09
  EN: Tap25_EN.srt                     → 00:25 / 07:25 / 13:07 / 21:40 / 28:49
  JA: Tap25_JA.srt                     → 00:23 / 08:30 / 15:10 / 24:02 / 32:13
  KO: CHƯA CÓ master ⇒ dùng mốc VN (tạm) — phải đo lại khi dựng xong audio KO.

THỨ TỰ BẮT BUỘC (A11 #70): chạy file này SAU cùng. `package.py` và
`generate_all_descriptions.py` sẽ ghi đè `mo_ta.txt` bằng mẫu cũ ⇒ nếu phải
chạy lại pipeline, chạy lại `py -3 .work/make_descriptions_t25.py` sau đó.

KHÔNG ghi đè `nguon_tham_khao*.md` (bảng đối chiếu dữ kiện đã kiểm chứng sẵn).
"""
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
SAN = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham"

# ==============================================================================
# MỐC CHƯƠNG ĐO THẬT
# ==============================================================================
CHAP_VN = [
    ("00:00", "Intro"),
    ("00:23", "Hồi 1 · Cơn ác mộng áo mưa vàng & Những bóng ma sau cánh cửa biệt thự Seoul"),
    ("07:40", "Hồi 2 · Cuộc đào tẩu chớp nhoáng & Sự trơ tráo sau chiếc mặt nạ phán xét"),
    ("13:22", "Hồi 3 · Giải mã tâm lý: Thù hận xã hội (Sociopathic Resentment) & Cơ chế đổ lỗi ngoại hóa"),
    ("21:09", "Hồi 4 · Bản án tử hình & Phán quyết nghiêm minh của công lý"),
    ("28:09", "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện nhân cách thù hận xã hội"),
]
CHAP_EN = [
    ("00:00", "Intro"),
    ("00:25", "Act 1 · The Yellow Raincoat Nightmare & The Shadows Behind Seoul's Mansions"),
    ("07:25", "Act 2 · The Lightning Escape & The Brazen Mask of Vigilantism"),
    ("13:07", "Act 3 · Psychological Decoding: Sociopathic Resentment & Externalization Defenses"),
    ("21:40", "Act 4 · The Death Sentence & The Uncompromising Verdict of Justice"),
    ("28:49", "Act 5 · The Warning Lesson & 4 Red Flags for Detecting Sociopathic Resentment"),
]
CHAP_JA = [
    ("00:00", "オープニング"),
    ("00:23", "第1幕 · 黄色いレインコートの悪夢＆ソウルの豪邸の扉の向こうに潜む影"),
    ("08:30", "第2幕 · 電光石火の脱走＆正義の仮面の裏に隠された厚顔無恥"),
    ("15:10", "第3幕 · 心理解剖：社会憎悪（SOCIOPATHIC RESENTMENT）と責任転嫁の防衛機制"),
    ("24:02", "第4幕 · 死刑判決と法の厳正なる裁き"),
    ("32:13", "第5幕 · 歴史の教訓と社会憎悪パーソナリティを見抜く4つのレッドフラッグ"),
]
CHAP_KO = [
    ("00:00", "오프닝"),
    ("00:23", "제1막 · 노란 우비의 악몽 & 서울 별장 뒤편에 숨어 있던 그림자"),
    ("07:40", "제2막 · 번개처럼 튄 도주 & 도덕적 심판의 가면 뒤에 숨은 능청스러움"),
    ("13:22", "제3막 · 심리 분석: 사회적 분노(Sociopathic Resentment) & 외재화 투사 기제"),
    ("21:09", "제4막 · 사형 판결 & 사법의 준엄한 심판"),
    ("28:09", "제5막 · 각성의 교훈 & 사회 분노형 인격을 식별하는 4가지 위험 신호"),
]


def chap_lines(rows):
    return "\n".join(f"{t} {name}" for t, name in rows)


# ==============================================================================
# KHỐI NGUỒN (chỉ dùng link đã có trong repo — không bịa nguồn mới, L2)
# ==============================================================================
SOURCES_VI = """Toàn bộ sự kiện, hồ sơ xét xử và phân tích động cơ căm thù xã hội đã được đối chiếu với nguồn công khai của cảnh sát và tòa án Hàn Quốc:

▸ Tòa án Quận Trung tâm Seoul & Tòa án Tối cao Hàn Quốc — bản án tử hình Yoo Young-chul (20 nạn nhân; tuyên án 13/12/2004, Tòa án Tối cao giữ nguyên án 06/2005) — https://www.scourt.go.kr/
▸ Cơ quan Cảnh sát Thủ đô Seoul (SMPA) & Đồn Cảnh sát Mapo — điều tra chuyên án và khai quật 11 nạn nhân sau chùa Bongwon — https://www.smpa.go.kr/
▸ Profiler Kwon Il-yong — hồi ký 'Those Who Read Evil Minds' — https://www.chosun.com/ · SBS (Unanswered Questions) — https://www.sbs.co.kr/
▸ Tâm lý học tội phạm: ASPD + NPD; Displaced Aggression, Moral Vigilante Delusion, God Complex, Pathological Self-Pity."""

SOURCES_VI_FILE = """Toàn bộ sự kiện, hồ sơ xét xử và phân tích động cơ căm thù xã hội trong video đã được đối chiếu với các nguồn hồ sơ cảnh sát và tòa án Hàn Quốc:

▸ Hồ sơ tòa án & Cơ quan điều tra
• Tòa án Quận Trung tâm Seoul & Tòa án Tối cao Hàn Quốc — Bản án tử hình xét xử Yoo Young-chul (20 nạn nhân; tuyên án 13/12/2004, Tòa án Tối cao giữ nguyên án 06/2005) — https://www.scourt.go.kr/
• Cơ quan Cảnh sát Thủ đô Seoul (SMPA) & Đồn Cảnh sát Mapo — Nhật trình điều tra chuyên án và khai quật 11 nạn nhân sau chùa Bongwon — https://www.smpa.go.kr/
▸ Báo chí điều tra & Profiling
• Profiler Kwon Il-yong — Hồi ký 'Those Who Read Evil Minds' (Những kẻ đọc tâm lý ác quỷ), bản ghi đối thoại trực tiếp với Yoo — https://www.chosun.com/
• Đài truyền hình SBS (Unanswered Questions) — Kho tư liệu độc quyền về vụ án 'Sát nhân áo mưa' — https://www.sbs.co.kr/
• Netflix Documentary Series — 'The Raincoat Killer: Chasing a Predator in Korea' (2021).
▸ Tâm lý học tội phạm & Khoa học hành vi
• Phân tích Rối loạn nhân cách chống đối xã hội (ASPD) kết hợp Rối loạn nhân cách ái kỷ (NPD).
• Cơ chế Đổ lỗi Ngoại hóa (Displaced Aggression), Ảo tưởng người phán xét đạo đức (Moral Vigilante Delusion), Ảo tưởng Toàn năng (God Complex) & Tự thương hại bệnh lý (Pathological Self-Pity).
▸ Đường dây nóng hỗ trợ
• Tổng đài Quốc gia Bảo vệ Trẻ em 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai — 096 306 1414 — https://duongdaynongngaymai.vn/"""

SOURCES_EN = """Every event, court record and forensic analysis was cross-checked against verified police and court archives:

▸ Seoul Central District Court & Supreme Court of Korea — the death sentence in the Yoo Young-chul case (20 victims; sentenced 13 Dec 2004, upheld by the Supreme Court in June 2005) — https://www.scourt.go.kr/
▸ Seoul Metropolitan Police Agency (SMPA) & Mapo Police Station — the investigation file and the excavation of 11 victims behind Bongwon Temple — https://www.smpa.go.kr/
▸ Profiler Kwon Il-yong — 'Those Who Read Evil Minds' — https://www.chosun.com/ · SBS (Unanswered Questions) — https://www.sbs.co.kr/"""

SOURCES_EN_FILE = """Every event, court record and forensic psychological analysis in this video was cross-checked against verified police and court archives from South Korea:

▸ Court Records & Investigative Agencies
• Seoul Central District Court & Supreme Court of Korea — The death sentence verdict in the Yoo Young-chul case (20 victims; sentenced 13 Dec 2004, upheld by the Supreme Court in June 2005) — https://www.scourt.go.kr/
• Seoul Metropolitan Police Agency (SMPA) & Mapo Police Station — The special-case investigation file and the excavation of 11 victims on the hillside behind Bongwon Temple — https://www.smpa.go.kr/
▸ Investigative Journalism & Profiling
• Profiler Kwon Il-yong — 'Those Who Read Evil Minds', the record of his direct interviews with Yoo — https://www.chosun.com/
• SBS (Unanswered Questions) — The exclusive archive on the 'Raincoat Killer' case — https://www.sbs.co.kr/
• Netflix Documentary Series — 'The Raincoat Killer: Chasing a Predator in Korea' (2021).
▸ Criminal Psychology & Behavioral Science
• Analysis of Antisocial Personality Disorder (ASPD) combined with Narcissistic Personality Disorder (NPD).
• Displaced Aggression, Moral Vigilante Delusion, God Complex & Pathological Self-Pity as the operative mechanisms.
▸ Crisis Helplines & Support
• National Child Helpline 111 (Vietnam, toll-free 24/7) — http://tongdai111.vn/
• Childhelp National Child Abuse Hotline (US/Canada, toll-free 24/7): 1-800-422-4453 — https://www.childhelphotline.org/"""

SOURCES_JA = """本動画の事件経過・裁判記録・行動科学的心理分析は韓国の公式捜査・司法記録と照合検証しています：

▸ 裁判記録と捜査機関
• ソウル中央地方裁判所＆韓国大法院 — Yoo Young-chul 死刑判決（被害者20名、2004年12月13日判決、2005年6月大法院で上告棄却） — https://www.scourt.go.kr/
• ソウル地方警察庁（SMPA）＆麻浦警察署 — 専門捜査の捜査記録および奉恩寺裏山での11体の発掘記録 — https://www.smpa.go.kr/
▸ 捜査報道とプロファイリング
• プロファイラー Kwon Il-yong — 『Those Who Read Evil Minds』（本人との直接対話記録） — https://www.chosun.com/
• SBS『事件Special（それが知りたい）』— 「レインポートキラー」事件の独占アーカイブ — https://www.sbs.co.kr/
• Netflix ドキュメンタリー — 『The Raincoat Killer: Chasing a Predator in Korea』（2021年）。
▸ 犯罪心理学と行動科学
• 反社会的人格障害（ASPD）と自愛型人格障害（NPD）の併存の分析。
• 転移攻撃・道徳的裁判官妄覚・万能感・病的自己憐憫という4つの心理機制。
▸ 相談窓口・支援ホットライン
• 児童相談所虐待対応ダイヤル「189（いちはやく）」（24時間・無料） — http://tongdai111.vn/
• こころの健康相談統一ダイヤル：0570-064-556"""

SOURCES_KO = """본 영상의 사건 경과·재판 기록·행동과학적 심리 분석은 한국의 공식 수사·사법 기록과 대조 검증되었습니다:

▸ 재판 기록 및 수사 기관
• 서울중앙지방법원 & 대법원 — Yoo Young-chul 사건死刑 판결 (피해자 20명, 2004년 12월 13일 판결, 2005년 6월 대법원 상고 기각) — https://www.scourt.go.kr/
• 서울 경찰청(SMPA) & 마포경찰서 — 전문 수사 기록 및 봉원사 뒷산에서 발견된 11점의 피해자 발굴 기록 — https://www.smpa.go.kr/
▸ 수사 보도 및 프로파일링
• 프로파일러 Kwon Il-yong — 『Those Who Read Evil Minds』(본인과의 직접 대화 기록) — https://www.chosun.com/
• SBS 『그것이 알고싶다』 — '우비의 살인자' 사건 독점 아카이브 — https://www.sbs.co.kr/
• Netflix 다큐멘터리 — 『The Raincoat Killer: Chasing a Predator in Korea』(2021).
▸ 범죄심리학 및 행동과학
• 반사회적 인격장애(ASPD)와 자기애상형 인격장애(NPD)의 병존 분석.
• 공격 전이·도덕적 심판 환시·전능감·병적 자기연민이라는 네 가지 심리 기제.
▸ 상담 창구 및 지원 핫라인
• 아동학대 신고전화 112 / 보건복지상담센터 129 (24시간) — http://tongdai111.vn/
• 자살예방 상담전화 109"""

# ==============================================================================
# MÔ TẢ 4 NGÔN NGỮ
# ==============================================================================
DESC_VI = """Tập 25: Sát Nhân Áo Mưa & Cơn Cuồng Nộ Thù Hận Xã Hội — Vỏ Bọc Tự Ti & Tội Ác Đội Lốt Phán Xét (Hồ Sơ Yoo Young-chul) | Tâm lý học tội phạm: Yoo Young-chul & Hệ sinh thái 10 chỉ dấu tâm lý & 4 cảnh báo đỏ sinh tồn | Amber eyes

Vào đầu thập niên 2000, thủ đô Seoul của Hàn Quốc đang trên đà phát triển rực rỡ và trở thành một trong những đô thị thịnh vượng bậc nhất châu Á. Thế nhưng, bên dưới ánh đèn hoa lệ của những tòa nhà chọc trời, một bóng ma tội ác tàn khốc đã bất ngờ xuất hiện. Từ mùa thu năm 2003 đến mùa hè năm 2004, một chuỗi án mạng liên hoàn bí ẩn đã liên tiếp diễn ra tại những khu vực tưởng chừng như an toàn tuyệt đối. Đó là khởi đầu của hồ sơ đen tối mang tên Yoo Young-chul, kẻ sát nhân sau này được biết đến với biệt danh Kẻ sát nhân áo mưa.

Hồ sơ Yoo Young-chul là minh chứng điển hình cho ngành tâm lý học tội phạm quốc tế về sự biến dạng nhân cách do mặc cảm tự ti chuyển hóa thành thù hận xã hội cực đoan. Chuyên gia phác họa tâm lý tội phạm đầu tiên của Hàn Quốc là ông Kwon Il-yong đã đối thoại trực tiếp với hắn nhiều ngày — một cuộc đấu trí tâm lý trong phòng thẩm vấn.

Amber eyes giải phẫu toàn diện hồ sơ này qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (§A2c):
1. ẢNH HƯỞNG XÃ HỘI: 20 nạn nhân trong 10 tháng; "bàng quan tập thể" khi dồn lực lượng vào khu biệt thự; chủ cơ sở nhận ra quy luật số điện thoại đã giúp chặn kẻ sát nhân.
2. VẬT HÓA NẠN NHÂN: gán phẩm chất xấu xa cho nạn nhân để biến họ thành "đáng trừng phạt"; phi nhân tính hóa để tắt lương tâm; luôn chọn người không có khả năng tự vệ.
3. NGƯỜI THÂN & CHIA NGĂN: năm 2002 vợ dẫn con rời đi khi hắn thụ án; ra tù lại bị từ chối tình cảm — hai cú sốc tạo vết thương lòng tự tôn ái kỷ (Narcissistic Injury) và đóng kín cửa hòa nhập.
4. THÁI ĐỘ TRƯỚC BẢN ÁN: trơ tráo, không cúi đầu; cố nhận vơ vụ án Imun-dong để thổi phồng số nạn nhân; thách thức hội đồng xét xử; tự vẽ bản đồ hiện trường như khoe bộ sưu tập.
5. TỰ BÀO CHỮA: Moral Vigilante Delusion + Moral Neutralization + God Complex + Pathological Self-Pity — bốn lớp vỏ bọc để tin mình đang làm công lý.
6. NGÒI NỔ & ĐIỂM GÃY: mắc chứng mù màu phá vỡ giấc mơ nghệ thuật; 14 lần vào tù; năm 2002 ly hôn và bị từ chối tình cảm ngay sau khi ra tù — điểm gãy bùng phát.
7. SIGNATURE VS. MO: MO là đột nhập ban đêm qua cửa sổ hoặc ban công, không lấy tài sản, không để lại vân tay; Signature bất biến là tự khai quật, tự vẽ bản đồ và nuôi hào quang "người phán xét".
8. LEO THANG ẢO TƯỞNG: biệt thự giàu (9/2003) → phụ nữ làm nghề dịch vụ (2004); mỗi đợt chỉ cho chút quyền lực tạm thời rồi lại trống rỗng.
9. HÀO QUANG & ĐIỂM MÙ: dư luận tin "kẻ trừng phạt người giàu", hắn tự phong thẩm phán tối cao và viện dẫn kẻ giết người khác để chứng minh "tỉnh táo"; nạn nhân thực tế là người yếu thế nhất.
10. NẠN NHÂN HỌC & 4 CẢNH BÁO ĐỎ: tôn vinh 20 nạn nhân vô tội; 4 cảnh báo đỏ — đổ lỗi và ganh ghét thành công người khác; phân biệt đối xử với phụ nữ, người yếu thế; nhận dịch vụ ở nơi kín đáo; lời đe dọa mang tính phán xét đạo đức.

⏱ MỐC CHƯƠNG
{chap_vn}

⚠️ LƯU Ý
• Không phù hợp cho trẻ em; mang tính giáo dục, phân tích dưới góc nhìn tâm lý học tội phạm và không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Thông tin dựa trên tư liệu công khai — xem nguồn bên dưới. Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Cú, Sói, Cáo, Cừu, Mèo là nhân vật minh hoạ, không phải người thật; lời thoại của Điều tra viên, Chuyên gia và Người trong cuộc là lời dựng lại dựa trên tư liệu. Giọng đọc, hình ảnh và âm nhạc được tạo cho kênh bằng công cụ AI.

📚 NGUỒN THAM KHẢO & ĐỐI CHIẾU
{src_vi}

🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia bảo vệ trẻ em 111 (Việt Nam, miễn phí 24/7).

#AmberEyes #TrueCrime #CriminalPsychology #YooYoungChul #TheRaincoatKiller #SeoulMurders #SerialKillerProfiling #KwonIlYong #TamLyToiPham #PhamVan #HoiTo"""

DESC_EN = """Ep. 25: The Yellow Raincoat Killer & The Fury of Sociopathic Resentment — The Yoo Young-chul File | Criminal Psychology: Yoo Young-chul & the 10-Indicator Behavioral Ecosystem & 4 Survival Red Flags | Amber eyes

In the early 2000s, Seoul was booming, becoming one of Asia's most prosperous metropolises — yet beneath the glittering skyscrapers a brutal shadow of crime emerged. From autumn 2003 to summer 2004, mysterious serial killings erupted in neighborhoods long considered completely safe. This was the inception of the dark dossier known as Yoo Young-chul — the killer later infamously dubbed The Raincoat Killer.

The case provided international criminal psychology with a classic study on personality deformation stemming from inferiority turning into extreme resentment. South Korea's pioneering profiler, Inspector Kwon Il-yong, engaged in exhaustive direct interviews with him — a psychological chess match inside the interrogation room.

Amber eyes dissects the case through our 10-Indicator Behavioral & Psychological Ecosystem (§A2c):
1. SOCIAL IMPACT: 20 victims in ten months; a dangerous collective illusion after police saturated the wealthy districts; parlor owners who spotted the repeating phone number cracked the case.
2. OBJECTIFICATION OF VICTIMS: Casting victims as greedy and depraved to make them "deserving targets"; dehumanization to silence conscience; only those who could not defend themselves.
3. INTIMATES & CLOSED PATHS: In 2002 his wife left with their son while he was imprisoned; a fresh rejection after his release — a deep narcissistic injury and no way back into society.
4. ATTITUDE BEFORE THE VERDICT: Brazen in the dock, never bowing his head; falsely claiming an unrelated Imun-dong murder to inflate his tally; open defiance; drawing burial-site maps as a trophy.
5. SELF-EXONERATION: Moral Vigilante Delusion + Moral Neutralization + God Complex + Pathological Self-Pity — four layers of armor around a false belief in his own righteousness.
6. TRIGGER & TIPPING POINT: Colour blindness, fourteen prison terms, the 2002 divorce and the rejection that followed — the break point where long-simmering fury detonated.
7. SIGNATURE VS. MO: Night entry through windows and balconies, nothing taken, no fingerprints left; the immutable Signature was self-confession, self-drawn maps, the halo of a self-appointed judge.
8. ESCALATION CYCLE: Affluent elders in mansions (Sept 2003) → service women (2004); each bout a flash of omnipotence, then emptiness pushing him onward.
9. HALO EFFECT & BLIND SPOTS: The public believed a "punisher of the rich"; he called himself a supreme judge and cited another murderer to prove he was "sane" — while his victims were the most defenseless.
10. VICTIMOLOGY & 4 SURVIVAL RED FLAGS: Honoring 20 innocent victims and the families demanding dignity back; 4 red flags — blame-shifting, contempt for women and the weak, services in secluded places without oversight, moralizing threats.

⏱ CHAPTER TIMESTAMPS
{chap_en}

⚠️ PLEASE NOTE
• Not suitable for children. Educational content analyzed from the perspective of criminal psychology; it is not a substitute for medical, psychological or legal advice.
• Based on verified public records — see sources below. The channel has no intent to convict, defame or glorify any individual.
• The Owl, Wolf, Fox, Sheep and Cat are illustrative characters, not real people; dialogue for the Investigator, Expert and the people in the case is reconstructed from documentation. Voices, imagery and music were generated using AI tools.

📚 SOURCES & CROSS-CHECK
{src_en}

🆘 If you know a child is being abused, call the National Child Helpline 111 (Vietnam, toll-free 24/7) or the Childhelp National Child Abuse Hotline (US/Canada): 1-800-422-4453.

#AmberEyes #TrueCrime #CriminalPsychology #YooYoungChul #TheRaincoatKiller #SeoulMurders #SerialKillerProfiling #KwonIlYong #NarcissisticInjury #DisplacedAggression #SurvivalRedFlags"""

DESC_JA = """第25話：黄色いレインコートキラーと反社会的怨恨の狂乱 — Yoo Young-chul 事件ファイル | 犯罪心理学：Yoo Young-chul と10の心理・行動指標エコシステム、4つの生存レッドフラッグ | Amber eyes

2000年代初頭、ソウルは目覚ましい経済発展を遂げ、アジア有数の繁栄する大都市へと成長していました。しかし高層ビルの灯りの下で、凶悪な犯罪の影が突然に現れ、想像も及ばない恐怖を街へと撒き散らしました。2003年秋から2004年の夏にかけて、「安全」とされていた地域で連続殺人が勃発し、雨の夜に潜む黒い影について街中が噂を競い合いました。これが、後に「レインポートキラー」と呼ばれる Yoo Young-chul の、闇に覆われた事件ファイルの始まりです。

Yoo Young-chul の事件記録は、劣等感が極端な反社会性へと転化した人格崩壊の典型例として、犯罪心理学に貴重な研究材料を提供しました。韓国の第一人犯罪プロファイラー Kwon Il-yong 警察官は本人と直接対話を重ね、尋問室での心理的チェスのような決戦。供述の機械的な書き取りではなく、人格の底を暴く戦いの場でもありました。

Amber eyes は本事件を『10の心理・行動指標エコシステム』（§A2c）に基づき徹底解剖します：
1. 社会的波紋と集団的な関心：10ヶ月に満たない間に20名の犠牲者。街を覆った恐怖。富裕層地区に警護力を集中させた結果、「危険は上階級のみ」という危険な集団的錯覚が生まれ、派遣サービス業女性が危険にさらされました。マッサージ店主が同一の電話番号パターンに気づいたことが、捜査の突破口となりました。
2. 被害者の客観化（モノ扱い）：被害者に貪欲・堕落などの悪性を賦課して「処罰すべき存在」に作り替え、良知を眠らせるために人間性を剥奪。常に自己防衛のできない者だけを選定した。
3. 家族・親しい者への認識と分断：2002年、服役中に妻が離婚を申し出て子供と去り、出所直後には再び拒絶された。二重の打撃が深い自愛傷（Narcissistic Injury）を生み、社会復帰への道を塞いだ。
4. 判決前の態度：被告席でも一切頭を下げない蛮横な姿勢。無関係なイムン洞の事件まででっち上げ被害者数を水増し。裁判官への公然たる挑発。埋納現場図を自分で描き、稀少なコレクションを展示するような物言いで語りました。
5. 自己正当化の体系：道徳的裁判官妄覚（Moral Vigilante Delusion）＋道徳的中和＋万能感（God Complex）＋病的自己憐憫 — 正義を執行していると信じさせる4層の装甲。
6. 引き金と行動の転換点：色覚異常による美術学校への夢の崩壊、窃盗と詐欺による14回の服役、2002年の離婚と出所後の拒絶 — 抑圧され続けていた狂気が爆発した点。
7. 心理的署名（シグネチャー）対 手口（MO）：MO は夜間の窓やバルコニーからの侵入で、略奪をせず指紋も残さない。変わらない Signature は自供・自筆の埋納図・「正義の審判者」仮面の維持。
8. ファンタジー依存とエスカレーション：2003年9月、豪邸の高齢富裕層へ → 2004年、派遣サービス業女性へ標的を移す。各局面は全能感の閃光的な錯覚を生むだけ、すぐに消えて次の犯行へと走りました。
9. 後光効果と社会的盲点：世間では「金持ちを罰する者」と信じ、本人は最高裁の裁判者を自称し、別の殺人犯を引いて「正常な理性」を証明。実際の被害者は最も無力な人々でした。
10. 被害者学と4つの生存レッドフラッグ：20名の無実の被害者の尊厳を称え、名誉を取り戻す家族の声を紹介；4つの危険信号 — 常に他責し他人の成功に嫉妬する姿勢；女性や弱者への差別的軽蔑；第三者監視のない閉ざされた場所でサービスを受けること；道徳的裁きを帯びた脅迫。

⏱ チャプター
{chap_ja}

⚠️ ご視聴にあたっての注意事項
• 本動画はお子様向けではありません。
• 本動画は教育目的および犯罪心理学の観点からの分析・解説コンテンツであり、医学的、心理学的、または法的なアドバイスに代わるものではありません。
• 公開記録（裁判資料、警察捜査記録、報道資料等）に基づいて制作されています。特定の個人を告発、中傷、または美化する意図は一切ありません。
• 登場するキャラクター（フクロウ、オオカミ、キツネ、羊、猫）は演出用の架空のキャラクターです。捜査官・心理学者・関係者の発言は公開記録に基づいて構成されたドラマタイズです。
• 音声、画像、音楽はAIツールを活用して制作されています。

📚 参考資料・出典
{src_ja}

🆘 児童虐待を受けている、または虐待の疑いがある子どもに気づいた場合は、児童相談所虐待対応ダイヤル「189（いちはやく）」（24時間・無料）へご連絡ください。

#AmberEyes #TrueCrime #犯罪心理学 #YooYoungChul #レインポートキラー #ソウル連続殺人事件 #プロファイリング #KwonIlYong #10の心理指標 #生存レッドフラッグ"""

DESC_KO = """제25화: 노란 우비의 살인자 & 사회적 분노의 광란 — Yoo Young-chul 사건 파일 | 범죄심리학: Yoo Young-chul과 10대 심리·행동 지표 생태계 & 4가지 생존 레드플래그 | Amber eyes

2000년대 초, 대한민국의 수도 서울은 눈부시게 성장해 아시아에서 가장 번영한 도시 중 하나로 변해가고 있었습니다. 그러나 마천하 늘 보석처럼 빛나는 고층 빌딩 아래에서 잔혹한 범죄의 그림자가 갑자기 나타났습니다. 2003년 가을부터 2004년 여름까지, '안전하다' 여겨졌던 동네에서 연쇄 살인이 터졌고, 비 오는 밤마다 숨어 있는 검은 그림자에 대한 소문이 도시를 가로질렀습니다. 이것이 '노란 우비의 살인자'로 불리게 알려진 Yoo Young-chul의 어두운 사건 파일의 시작이었습니다.

Yoo Young-chul 사건 기록은 열등감이 극단적인 사회적 분노로 변질되어 인격이 파괴된 전형적인 사례로서 국제 범죄심리학계에 귀중한 연구 사례를 제공했습니다. 한국의 최초 범죄 프로파일러인 Kwon Il-yong 경관은 그와 직접 대화를 오래 나누었으며, 자백 기록 수집이 아니라 인격의 심부를 벗겨내는 심리적 체스와의 대결이었습니다.

Amber eyes는 본 사건을 '10대 심리·행동 지표 생태계'(§A2c)를 통해 심층 해부합니다:
1. 사회적 파장 및 집단적 관심: 10개월 만에 20명의 피해자, 서울을 덮은 공포, 부유층 지역에 경력이 집중되면서 '위험은 상류층만을 노린다'는 위험한 집단적 오해를 낳았고 그로 인해 홈서비스 종업원들이 노출되었다; 마사지집 주인이 같은 전화번호 패턴을 눈여겨봤다는 것이 수사의 결정적 단서가 되었다.
2. 피해자의 객체화(사물화): 피해자에게 탐욕과 타락 같은 악질적 속성을 부여해 '처벌할 가치가 있는 존재'로 바꾸고, 양심을 잠재우기 위해 인간성을 박탈; 항상 스스로 방어할 수 없는 사람만 골랐다.
3. 가족·친족에 대한 인식과 단절: 2002년 복역 중 아내가 이혼을 신청하고 아이와 떠났고, 석방 직후 다시 거절당했다. 연타의 충격이 깊은 나르시시즘 상처(Narcissistic Injury)를 만들고 사회 적응의 마지막 길을 닫아버렸다.
4. 판결 전 태도: 피고인석에서도 전혀 고개를 숙이지 않는 뻔뻔한 태도; 무관한 이문동 사건까지 자진해서 주장해 피해자 수를 부풀림; 재판부를 향한 공개적 도전; 매장 장소를 직접 그려 '소장품을 전시하는' 듯한 태도.
5. 자기 합리화 체계: 도덕적 심판 환시(Moral Vigilante Delusion) + 도덕적 중화 + 전능감(God Complex) + 병적 자기연민 — 정의를 이루고 있다고 믿게 하는 네 겹의 갑옷.
6. 촉발 요인과 행동 전환점: 색각 이상으로 미술 학교 진학 꿈이 무너지고, 절도·사기무기로 14차례 복역, 2002년 이혼과 석방 직후의 거절 — 오래 쌓인 분노가 폭발한 지점.
7. 심리적 시그니처 대 범행 수법(MO): MO는 밤 시간의 창문·발코니 침입, 물건을 훔치지 않고 지문도 남기지 않음. 변하지 않는 시그니처는 자백, 직접 그린 매장 지도, 그리고 '정의로운 심판자'라는 후광을 스스로 유지하는 의식.
8. 환상 중독과 에스컬레이션: 2003년 9월 고급주택의 고령 부유층 → 2004년 홈서비스 여성으로 표적 전환. 각 국면은 잠깐의 전능감만 주고 곧 공허함이 채워져 다음 범행으로 몰려갔다.
9. 후광 효과와 사회적 맹점: 사회는 '부자 벌하는 자'를 믿었고, 본인은 최고 심판자이며 다른 살인범을 인용해 '총명한 리얼리티'를 증명하려 했다. 그러나 실제 피해자는 가장 무력한 이들이었다.
10. 피해자학과 4가지 생존 레드플래그: 20명의 무고한 피해자의 존엄을 기리고, 명예를 되찾으려 목소리를 낸 가족들을 조명; 4가지 위험 신호 — 만인의 실패를 남 탓하고 타인의 성공에 시샘하는 태도; 여성과 약자에 대한 차별적 경멸; 제3자 감독 없는 폐쇄된 장소에서 서비스를 받는 일; 도덕적 심단을 내건 협박.

⏱ 챕터(타임라인)
{chap_ko}

⚠️ 시청 전 유의사항
• 본 콘텐츠는 청소년에게 적합하지 않을 수 있습니다.
• 본 영상은 범죄심리학 및 교육적 관점에서의 분석 콘텐츠이며, 의학적·심리학적 또는 법률적 조언을 대신할 수 없습니다.
• 공식 공개 기록(법원 판결문, 수사 기록, 공식 언론 보도)을 바탕으로 제작되었습니다. 특정인을 비방하거나 단죄하려는 의도가 전혀 없습니다.
• 등장하는 올빼미(호스트), 늑대(수사관), 여우(심리학자), 양(증인), 고양이(시청자)는 연출을 위한 가상 캐릭터입니다. 수사관·심리학자·당사자의 발언은 공개 기록에 기반한 드라마타이즈입니다.
• 본 영상의 음성, 시각 자료 및 음악은 AI 기술을 활용하여 제작되었습니다.

📚 참고자료 및 출처
{src_ko}

🆘 아동학대 신고전화 112 / 보건복지상담센터 129 (24시간)

#AmberEyes #TrueCrime #범죄심리학 #YooYoungChul #노란우비의살인자 #서울연쇄살인 #프로파일링 #KwonIlYong #10대심리지표 #생존레드플래그"""

# ==============================================================================
# GHI FILE
# ==============================================================================
DESC_VI = DESC_VI.replace("{chap_vn}", chap_lines(CHAP_VN)).replace("{src_vi}", SOURCES_VI)
DESC_EN = DESC_EN.replace("{chap_en}", chap_lines(CHAP_EN)).replace("{src_en}", SOURCES_EN)
DESC_JA = DESC_JA.replace("{chap_ja}", chap_lines(CHAP_JA)).replace("{src_ja}", SOURCES_JA)
DESC_KO = DESC_KO.replace("{chap_ko}", chap_lines(CHAP_KO)).replace("{src_ko}", SOURCES_KO)

FILES = [
    # VN — không ghi đè nguon_tham_khao.md (bảng đối chiếu đã kiểm chứng)
    (SAN / "Tap25" / "mo_ta.txt", DESC_VI),
    (SAN / "Tap25" / "xuat_ban" / "mo_ta.txt", DESC_VI),
    (SAN / "Tap25" / "nguon_mo_ta.txt", SOURCES_VI_FILE),
    # EN
    (SAN / "Tap25_EN" / "description.txt", DESC_EN),
    (SAN / "Tap25_EN" / "mo_ta.txt", DESC_EN),
    (SAN / "Tap25_EN" / "xuat_ban" / "description.txt", DESC_EN),
    (SAN / "Tap25_EN" / "xuat_ban" / "mo_ta.txt", DESC_EN),
    (SAN / "Tap25_EN" / "nguon_mo_ta_EN.txt", SOURCES_EN_FILE),
    # JA
    (SAN / "Tap25_JA" / "description.txt", DESC_JA),
    (SAN / "Tap25_JA" / "mo_ta.txt", DESC_JA),
    (SAN / "Tap25_JA" / "xuat_ban" / "description.txt", DESC_JA),
    (SAN / "Tap25_JA" / "xuat_ban" / "mo_ta.txt", DESC_JA),
    (SAN / "Tap25_JA" / "nguon_mo_ta_JA.txt", SOURCES_JA),
    # KO
    (SAN / "Tap25_KO" / "description.txt", DESC_KO),
    (SAN / "Tap25_KO" / "mo_ta.txt", DESC_KO),
    (SAN / "Tap25_KO" / "xuat_ban" / "description.txt", DESC_KO),
    (SAN / "Tap25_KO" / "xuat_ban" / "mo_ta.txt", DESC_KO),
    (SAN / "Tap25_KO" / "nguon_mo_ta_KO.txt", SOURCES_KO),
]

if __name__ == "__main__":
    print("=" * 72)
    print("SINH MÔ TẢ TẬP 25 (4 NGÔN NGỮ) — YOO YOUNG-CHUL")
    print("=" * 72)
    for p, content in FILES:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8", newline="")
        print(f"  Ghi: {p.relative_to(ROOT)}  ({len(content)} ký tự)")

    print("\n" + "=" * 72)
    print("KIỂM ĐỘ DAI (GIỚI HẠN YOUTUBE ≤ 5000 KÝ TỰ)")
    print("=" * 72)
    ok = True
    for name, d in (("Tiếng Việt (VN)", DESC_VI), ("Tiếng Anh (EN)", DESC_EN),
                    ("Tiếng Nhật (JA)", DESC_JA), ("Tiếng Hàn (KO)", DESC_KO)):
        good = len(d) <= 5000
        ok = ok and good
        print(f"  {name:16}: {len(d):5d} ký tự — {'PASS' if good else 'FAIL'} "
              f"(dư địa {5000 - len(d)})")
    print("\n>>> ĐẠT" if ok else "\n>>> LỖI: VƯỢT 5000 KÝ TỰ — cần rút gọn")
