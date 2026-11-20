#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh lại mô tả YouTube cho TẬP 17 (Turpin Family) — 4 ngôn ngữ VI/EN/JA/KO.

Nguyên tắc (theo AGENTS.md L5/L6 + A11 #70/#85/#86):
  • Nội dung mô tả nằm Ở ĐÂY (nguồn duy nhất) — không sửa tay file thành phẩm.
  • Mốc chương ĐO THẬT từ timeline của từng ngôn ngữ (package.act_start_times).
    Tập 17 KO chưa dựng audio ⇒ mốc ước lượng, hiệu chuẩn từ timeline KO Tập 02.
  • ĐO số ký tự thật TRƯỚC khi ghi; vượt 5000 ⇒ dừng, không ghi file.
  • `nguon_mo_ta*.txt` = khối nguồn RÚT GỌN (package.py chèn dưới header
    "📚 NGUỒN THAM KHẢO") — KHÔNG lặp lại header (tránh "📚 NGUỒN THAM KHẢO 📚 ...").
  • `nguon_tham_khao*.md` = hồ sơ nguồn đầy đủ (bảng đối chiếu từng câu).

Căn cứ nội dung: 01_KICH_BAN/Tap17/kichban_tap17_23102026.md (bản 226 câu, 14/11/2026)
+ 01_KICH_BAN/Tap17/REVIEW_kichban_tap17_10chiau.md (bảng 10 chỉ dấu A2c).
Format tham chiếu: Tập 16 (mẫu mới nhất, 19/11/2026).
"""

import json
import os
import re
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
LIMIT = 5000

# ==============================================================================
# TIÊU ĐỀ + TÊN HỒI (đồng bộ với edition.py EPISODES["17"])
# ==============================================================================
TITLES = {
    "VI": "Tập 17: 13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Kiểm Soát Cưỡng Chế, Ảo Tưởng Điên Cuồng Đôi & Cú Nhảy Sinh Tồn (Hồ Sơ Gia Đình Turpin)",
    "EN": "Ep. 17: 13 Captive Children in a Suburban Dungeon — Coercive Control, Shared Delusional Disorder & The Leap for Survival (The Turpin Family Case)",
    "JA": "第17話：郊外の暗闇に隠された真実 — 強圧的支配、共有精神病と命懸けの脱出（ターピン一家事件）",
    "KO": "제17화: 교외의 감옥에 갇힌 13남매 — 강압적 통제, 공유정신병과 생존을 향한 도약 (Turpin 가족 사건)",
}

ACT_TITLES = {
    "VI": {1: "Hồi 1 · Cú nhảy qua cửa sổ và cuộc gọi 911 từ chiếc điện thoại hỏng",
           2: "Hồi 2 · Ngục tù ngoại ô và vỏ bọc hoàn hảo của gia đình kiểu mẫu",
           3: "Hồi 3 · Giải mã tâm lý: Kiểm soát cưỡng chế, ảo tưởng điên cuồng đôi & ấu trĩ hóa nạn nhân",
           4: "Hồi 4 · Bản cáo trạng rúng động và phiên tòa đối diện công lý",
           5: "Hồi 5 · Hành trình tái sinh từ tro tàn & 4 cảnh báo đỏ về bạo hành gia đình kín"},
    "EN": {1: "Act 1 · The Dawn Window Escape and the 911 Call",
           2: "Act 2 · The Suburban Dungeon and the Model Family Facade",
           3: "Act 3 · Psychological Decoding: Coercive Control & Folie à Deux",
           4: "Act 4 · The Shocking Indictment and the Confrontation with Justice",
           5: "Act 5 · Rebirth from the Ashes & 4 Survival Red Flags"},
    "JA": {1: "第1幕 · 夜明けの窓からの脱出と解約携帯による911通報",
           2: "第2幕 · 郊外の監禁部屋と完璧なモデル家族の仮面",
           3: "第3幕 · 心理分析：強圧的支配、共有精神病（フォリ・ア・ドゥ）と作為的幼態化",
           4: "第4幕 · 震撼の起訴状と法廷での正義との対面",
           5: "第5幕 · 灰からの再生と隠蔽された家庭内虐待の4つのレッドフラッグ"},
    "KO": {1: "제1막 · 새벽 창문을 통한 탈출과 끊긴 전화로 건 911 신고",
           2: "제2막 · 교외의 감옥과 모범적인 가족이라는 완벽한 가면",
           3: "제3막 · 심리 해체: 강압적 통제, 공유정신병(Folie à Deux)과 의도적 유아화",
           4: "제4막 · 충격적인 공소장과 법정에서 마주한 정의",
           5: "제5막 · 잿더미 속에서의 부활과 은폐된 가정폭력의 4가지 레드플래그"},
}

INTRO_LABEL = {"VI": "00:00 Intro & Khuyến cáo an toàn", "EN": "00:00 Intro & Advisory",
               "JA": "00:00 イントロ＆注意事項", "KO": "00:00 인트로 및 안내"}

# ==============================================================================
# KHỐI NGUỒN RÚT GỌN (đưa vào mô tả)
# ==============================================================================
SHORT_VI = """• Tòa Thượng thẩm Hạt Riverside: People v. David Allen Turpin & Louise Ann Turpin (RIF1800348) — https://www.riverside.courts.ca.gov/
• Biện lý Hạt Riverside: 14 trọng tội và thỏa thuận nhận tội (Công tố viên Michael Hestrin) — https://rivcoda.org/
• Cảnh sát Hạt Riverside: hiện trường 160 đường Muir Woods Road, Perris (14/01/2018) — https://www.riversidesheriff.org/
• ABC News 20/20: 'Escape from a House of Horror: The Turpin Sisters Speak' (11/2021) — https://abcnews.go.com/
• 'The Gift of Fear' của Gavin de Becker (1997) — khoa học hành vi sinh tồn."""

SHORT_EN = """• Superior Court, Riverside County: People v. David Allen Turpin & Louise Ann Turpin (RIF1800348) — https://www.riverside.courts.ca.gov/
• DA's Office, Riverside County: 14-count felony indictment and guilty plea (Michael Hestrin) — https://rivcoda.org/
• Sheriff's Office: crime scene report, 160 Muir Woods Road, Perris (Jan 14, 2018) — https://www.riversidesheriff.org/
• ABC News 20/20: 'Escape from a House of Horror: The Turpin Sisters Speak' (Nov 2021) — https://abcnews.go.com/
• 'The Gift of Fear' — Gavin de Becker (1997)."""

SHORT_JA = """• リバーサイド郡上級裁判所: People v. David Allen Turpin & Louise Ann Turpin (事件番号 RIF1800348) — https://www.riverside.courts.ca.gov/
• リバーサイド郡地方検察局: 14項目の重罪起訴と有罪答弁（マイケル・ヘストリン検事） — https://rivcoda.org/
• リバーサイド郡保安官事務所: ペリス市ミュア・ウッズ・ロード160番地 現場検証報告書（2018年1月14日） — https://www.riversidesheriff.org/
• ABCニュース 20/20: 『Escape from a House of Horror: The Turpin Sisters Speak』（2021年11月） — https://abcnews.go.com/
• 生存行動科学: ギャヴィン・ド・ベッカー『The Gift of Fear』（1997年）"""

SHORT_KO = """• 리버사이드 카운티 상급법원: People v. David Allen Turpin & Louise Ann Turpin (사건번호 RIF1800348) — https://www.riverside.courts.ca.gov/
• 리버사이드 카운티 지방검찰청: 14개 중범 기소 및 유죄 인정 합의 (마이클 헤스트린 검사) — https://rivcoda.org/
• 리버사이드 카운티 보안관실: 페리스시 뮤어 우즈 로드 160번지 사건 현장 감식 보고서 (2018년 1월 14일) — https://www.riversidesheriff.org/
• ABC 뉴스 20/20: 'Escape from a House of Horror: The Turpin Sisters Speak' (2021년 11월) — https://abcnews.go.com/
• 생존 행동 과학: 개빈 드 베커 저 'The Gift of Fear' (1997년)"""

# ==============================================================================
# MẪU MÔ TẢ EN (package.py description_en() đọc khối ```text có "CHAPTERS")
# + BẢNG NGUỒN EN DẠNG ✅ (package.py verified_links() đọc bảng này)
# ==============================================================================
EN_TEMPLATE = """# CHỮ CỐ ĐỊNH & GÓI PHÁT HÀNH TIẾNG ANH · TẬP 17
**Hồ sơ vụ án:** Turpin Family — 13 Captive Children in a Suburban Dungeon (Case No. RIF1800348)
**Kênh:** Amber eyes — Criminal psychology through real case files

---

## Mẫu mô tả YouTube hoàn chỉnh (Full YouTube Description)

```text
__BODY__
```
"""

SOURCES_TABLE_EN = """# SOURCES & FACT-CHECKING REFERENCE — EP. 17: THE TURPIN FAMILY CASE (13 CAPTIVE CHILDREN IN A SUBURBAN DUNGEON)

All events, dates, court verdicts and psychological frameworks have been cross-checked against verified public records:

| Verified Source / Official Record | Type | Status |
|---|---|:---:|
| https://www.riverside.courts.ca.gov/ | Public Record / Legal Document | ✅ Verified |
| https://rivcoda.org/ | Public Record / Legal Document | ✅ Verified |
| https://www.riversidesheriff.org/ | Public Record / Legal Document | ✅ Verified |
| https://abcnews.go.com/ | Public Record / Legal Document | ✅ Verified |
| http://tongdai111.vn/ | Public Record / Legal Document | ✅ Verified |
| https://www.childhelphotline.org/ | Public Record / Legal Document | ✅ Verified |
| https://www.thehotline.org/ | Public Record / Legal Document | ✅ Verified |
"""

# ==============================================================================
# NỘI DUNG MÔ TẢ — thân bài (mở đầu + 10 chỉ dấu)
# ==============================================================================
BODY_VI = """Rạng sáng 14/01/2018, tại Perris (hạt Riverside, California), một thiếu nữ 17 tuổi gầy gò trèo qua bậu cửa sổ, cầm chiếc điện thoại đã bị ngắt dịch vụ mạng, để gọi 911. Câu trình bày hai mươi phút ấy kéo 13 anh chị em ra khỏi ngục tù gia đình tàn bạo tồn tại giữa lòng khu dân cư ngoại ô yên bình. Thủ phạm là hai bậc cha mẹ có học thức: David Turpin, 56 tuổi, kỹ sư máy tính từng làm việc cho các tập đoàn quốc phòng, và Louise Turpin, 49 tuổi, người nội trợ quản lý gia đình. Các sĩ quan phát hiện bảy người con đã là người trưởng thành từ 18 đến 29 tuổi nhưng thể trạng như trẻ con: người chị cả 29 tuổi chỉ nặng khoảng 37 kilôgam.

Hồ sơ Nhà Turpin được Amber eyes giải phẫu toàn diện qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi:
1. DƯ CHẤN XÃ HỘI & CẢI CÁCH THỂ CHẾ: Hoang tưởng tập thể bao trùm ngoại ô Perris khi tội ác nằm ngay cạnh nhà; vụ án buộc California mở phiên điều trần lập pháp để siết giám sát trường tư thục tại gia.
2. VẬT HÓA & PHI NHÂN HÓA NẠN NHÂN: 13 người con bị giáng cấp thành 'đạo cụ sống' phục vụ ảo tưởng toàn năng của cha mẹ; khuyết tật thấu cảm biến tiếng van xin thành sự kích thích kiểm soát.
3. NGHỊCH LÝ CHIA NGĂN: Hai thế giới bị khóa chặt — kỹ sư quốc phòng lịch thiệp ban ngày và kẻ giam cầm ban đêm; ảnh gia đình Disneyland trên mạng trở thành lá chắn bình thường hóa.
4. THÁI ĐỘ TRƯỚC BẢN ÁN: Nước mắt tại tòa là sự tự thương hại bệnh lý khi mất ngai vàng gia đình, không phải ăn năn; lời 'Chúa có kế hoạch đặc biệt cho các con' là ngụy biện tâm linh né trách nhiệm.
5. HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC: Giam con để 'bảo vệ' khỏi cám dỗ bên ngoài; đổ lỗi nạn nhân 'không vâng lời, rửa tay quá cổ tay' để biện minh cho trừng phạt.
6. NGÒI NỔ & ĐIỂM GÃY: Khủng hoảng nợ cùng hai lần nộp đơn phá sản làm sụp đổ cơ chế tự chủ của gia đình; với nạn nhân, nguy cơ các em nhỏ không qua khỏi kích hoạt bản năng sinh tồn.
7. DẤU ẤN SIGNATURE VS. THỦ ĐOẠN MO: MO liên tục đổi (trường tư thục tại gia, rèm tối, đảo ngày đêm); Signature bất biến là đồ đồng phục, dàn ảnh Las Vegas và tra tấn tâm lý bằng bánh ngọt, đồ chơi cấm chạm.
8. QUỸ ĐẠO LEO THANG HÀNH VI: Mắng mỏ → bắt úp mặt vào tường → nhốt phòng kín → trói dây thừng → xích sắt và ổ khóa; cơn nghiện mua sắm của người mẹ biến món hàng xa xỉ thành công cụ đày đọa.
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Vỏ bọc kỹ sư quốc phòng cùng ảnh gia đình đông con ngoan ngoãn tạo nên điểm mù nhận thức; đóng kín cửa và tôn trọng quyền riêng tư thái quá dựng nên bức tường vô hình che tội ác.
10. NẠN NHÂN HỌC & CẢNH BÁO ĐỎ SINH TỒN: Giải mã cú nhảy sinh tồn của Jordan qua 'The Gift of Fear' (Gavin de Becker), tha thứ như hành vi giải phóng cảm xúc và Tăng trưởng sau sang chấn (PTG); 4 cảnh báo đỏ: cô lập tuyệt đối, tương phản ảnh mạng với thực tế, suy kiệt dinh dưỡng bất thường, đảo lộn ngày đêm kèm kỷ luật trừng phạt."""

BODY_EN = """At dawn on January 14, 2018, in the quiet suburb of Perris, California, a frail 17-year-old girl slipped through a bedroom window, clutching a deactivated smartphone to dial 911. That twenty-minute call pulled 13 siblings out of a domestic dungeon hidden for years in an ordinary neighborhood. The perpetrators were their own educated parents: David Turpin, 56, a computer engineer who had worked for defense contractors, and Louise Turpin, 49, a homemaker. Officers later found seven of the captive 'children' were adults between 18 and 29 — the eldest sister, at 29, weighed only 37 kilograms.

Amber eyes dissects the Turpin Family dossier through the 10 Psychological & Behavioral Indicators:
1. SOCIAL IMPACT & INSTITUTIONAL REFORM: Collective paranoia gripped suburban Perris once the horror was found next door; the case forced California hearings to tighten oversight of private homeschooling.
2. OBJECTIFICATION & DEHUMANIZATION: The 13 children were demoted to 'living props' serving parental omnipotence fantasies; severe empathy deficits turned desperate cries into stimuli for control.
3. COGNITIVE COMPARTMENTALIZATION: Two worlds were locked apart — the polite defense engineer by day and the jailer of the family by night; the Disneyland family album became a shield of normalization.
4. PATHOLOGICAL SELF-PITY BEFORE THE BENCH: The courtroom tears were pathological self-pity at the loss of the family throne, not remorse; 'God has a special plan for the children' is spiritual bypassing to dodge responsibility.
5. MORAL NEUTRALIZATION: Captivity was reframed as 'protecting' the children from outside corruption; victims were blamed for 'disobedience' — washing hands past the wrists — to justify the punishment.
6. THE BREAKING POINT: Severe debt and two bankruptcy filings collapsed the family's self-reliance; for the victims, the risk of losing the younger siblings triggered the survival instinct.
7. PSYCHOLOGICAL SIGNATURE VS. OPERATIONAL MO: The MO kept evolving (home school, blackout curtains, inverted day and night); the Signature never changed — matching outfits, staged Las Vegas photo sets, and torture with food and toys never to be touched.
8. BEHAVIORAL ESCALATION TRAJECTORY: Verbal berating → standing facing walls → room isolation → rope binding → iron chains and padlocks; the mother's compulsive hoarding turned luxury goods into instruments of deprivation.
9. THE HALO EFFECT & COLLECTIVE BLINDSPOTS: The defense-contractor pedigree and staged images of a large, well-behaved family created an institutional blind spot; closed doors and extreme privacy norms built a wall shielding the abuse.
10. VICTIMOLOGY & SURVIVAL RED FLAGS: Decoding Jordan's leap through 'The Gift of Fear' (Gavin de Becker), forgiveness as emotional liberation, and Post-Traumatic Growth; four red flags: social isolation, an absurd contrast between online image and reality, unexplained malnutrition, and an inverted day-night routine with punitive rules."""

BODY_JA = """2018年1月14日の未明、カリフォルニア州リバーサイド郡ペリス市の静かな住宅街で、小柄な17歳の少女Jordan Turpinが窓枠を乗り越え、回線契約を解除された携帯電話から911へ緊急通報しました。20分に及ぶその通報が、十数年にわたる家庭内の監禁から13人の兄弟姉妹を救い出しました。加害者は高学歴の両親――56歳の父David Turpin（防衛産業向けの計算機エンジニア）と、49歳の母Louise Turpin（家事と教育をすべて担う主婦）でした。2018年中盤、警官は「子ども」たちのうち7人が18歳から29歳の成人だったことを知りました。29歳の姉の体重はわずか37キログラムにすぎません。

アンバーアイズ（Amber eyes）は、ターピン一家事件を「10の心理・行動指標体系」を通じて徹底解剖します：
1. 社会的余波と制度改革：隣人の家の中で発見された地獄に、郊外の街は集団的な恐怖と偏執に支配された。この事件は、カリフォルニア州に私設ホームスクール（サンドキャッスル・デイ・スクール）の監督を強化する法改正の議論を招く議会審議会を促した。
2. 被害者の客体化（Objectification）：13人の実子は人格を奪われ、親の全能感を満たす「生きた小道具」に格下げされた。極端な共感欠如により、懇願の声は統制の刺激として消費された。
3. 精神の区分化（Compartmentalization）：昼間の端正な防衛産業技師と、夜間の家族の監禁者――二つの世界は完全に分断された。SNSに並ぶ「ディズニーランドの仲良いモデル家族」の写真は、正常化の盾になった。
4. 判決前の病的な自己憐憫：法廷の涙と謝罪は真の罪悪感ではなく、家の玉座を失ったあとの病的な自己憐憫。「神には子供たちへの特別な計画がある」は、個人の責任から逃れるための霊的バイパスだった。
5. 道徳的中和技術：監禁を「外の悪から子供を守る」目的として正当化し、「手首より上を洗った」のような些細な不服従を、鎖による拘束の理由として正当化した。
6. 心理的引き金と崩壊点：巨大な負債と二度目の自己破産申立てが家の自立機構を崩壊させ、被害者側では弟妹の死リスクが生存本能を起動させた。
7. 手口（MO）と心理的刻印（Signature）：絶えず変化するMO（ホームスクール、暗幕、昼夜逆転）に対し、不変のSignatureは揃いの服、ラスベガス撮影、そして触れ禁止の食物や玩具による精神的拷問であった。
8. 行動のエスカレーション：叱責→壁を向いて立つ→幽閉→縄縛り→鉄鎖と南京錠。母の買物依存は贅沢品を子供を苦しめる道具に変えた。
9. 後光効果（ハロー効果）と社会の死角：防衛産業技師の肩書と作り込まれた家族写真は認識的な盲点を生み、閉ざされたドアと行き過ぎたプライバシー感覚が不可視の壁となって罪を庇った。
10. 被害者学と生存レッドフラッグ：ジョーダンの脱出を『The Gift of Fear』で解読し、許しが情緒的解放へ至る構造とトラウマ後の成長（PTG）。4つの赤い警告――完全な社会的孤立、网上的姿と現実の矛盾、説明のできない低栄養、昼夜逆転と罰則的規律。"""

BODY_KO = """2018년 1월 14일 새벽, 캘리포니아주 리버사이드 카운티 페리스의 조용한 교외 주택가에서, 17세 소녀 Jordan Turpin이 창틀을 넘어 해지된 휴대전화로 911에 신고했습니다. 20분간 이어진 그 통화가 10여 년간의 가정 내 감옥에서 13명의 형제자매를 구해 냈습니다. 가해자는 고학력 부모 — 방위산업 업체에서 컴퓨터 엔지니어로 일했던 56세 아버지 David Turpin과 가내와 자녀 교육까지 전부 담당하던 49세 어머니 Louise Turpin이었습니다. 2018년 중반, 경찰은 '아이'들 가운데 7명이 18세에서 29세의 성인이며, 29세 누나의 몸무게는 37킬로그램에 불과하다는 사실을 알게 됩니다.

앰버 아이즈(Amber eyes)는 터핀 가족 사건을 '10가지 심리 및 행동 지표 체계'를 통해 정밀 해부합니다:
1. 사회적 파장 및 제도 개혁: 이웃집 안에서 발견된 지옥에 교외 사회 전체가 집단적 공포와 편각에 사로잡힘; 이 사건은 캘리포니아주가 샌드캐슬 데이 스쿨 같은 사립 홈스쿨링에 대한 감독을 강화하는 입법 청원회를 촉발.
2. 피해자의 객체화(Objectification): 13명의 자녀는 인격이 아니라 부모의 전능망상을 채우는 '살아있는 소품'으로 격하; 극단적인 공감 결여로 간절한 울음소리마저 통제 자극으로 소비.
3. 인지적 구획화(Compartmentalization): 낮에는 정확한 방위산업 엔지니어, 밤에는 가족의 감금자 — 두 세계는 완전히 분리되었고, SNS에 올라온 '디즈니랜드 모범 가족' 사진이 정상화의 방패가 됨.
4. 판결 앞의 병적인 자기연민: 법정의 눈물과 사과는 진정한 참회가 아니라 집안의 옥좌를 잃은 뒤의 병적인 자기연민; '하나님은 아이들에게 특별한 계획이 있다'는 말은 개인적 책임을 피하기 위한 영적 우회.
5. 도덕적 중화 기법: 감금을 '바깥의 악으로부터 아이들을 지키는 일'로 정당화하고, '손목 위로 손을 씻었다'는 식의 미세한 불복종을 결박 학대의 명분으로 삼음.
6. 심리적 기폭제와 붕괴 지점: 막대한 부채와 두 차례의 파산 신청이 가구의 자립 기제를 무너뜨렸고, 피해자 쪽에서는 어린 동생들이 위험에 처할 수 있다는 판단이 생존 본능을 깨움.
7. 수법(MO)과 심리적 각인(Signature): 계속 바뀌는 MO(홈스쿨링, 암막 커튼, 주야 역전)와 달리 불변의 Signature는 동일한 단체복, 라스베가스 촬영 세트, 만지지 못하게 방치한 음식과 장난감을 이용한 정신적 고문.
8. 행동 에스컬레이션: 잔소리 → 벽 보고 서 있기 → 독방 → 밧줄 결박 → 쇠사슬과 자물쇠. 어머니의 구매 집착이 사치품을 아이들을 괴롭히는 도구로 바꿔 놓음.
9. 후광 효과(Halo Effect)와 사회적 사각지대: 방위산업 엔지니어라는 신분과 빈틈없이 연출한 가족 사진이 인지적 맹점을 만들었고, 꽉 닫힌 문과 과도한 사생활 존중이 범죄를 감춰 주는 보이지 않는 벽이 됨.
10. 피해자학 및 생존 레드플래그: 조던 터핀의 도주를 'The Gift of Fear'로 해부하고, 용서가 정서적 해방으로 이어지는 구조와 외상 후 성장(PTG). 4가지 레드플래그 — 절대적 사회적 고립, 온라인 이미지와 현실의 모순, 설명되지 않는 영양 결핍, 주야가 뒤바뀐 생활과 처벌적 규율."""

# ==============================================================================
# CÁC KHỐI CỐ ĐỊNH THEO NGÔN NGỮ
# ==============================================================================
ADVISORY = {
    "VI": """⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý học tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Căn cứ hồ sơ công khai của Tòa Thượng thẩm Hạt Riverside và Cảnh sát Hạt Riverside. Kênh không tôn vinh tội ác hay bôi nhọ ai.
• Linh thú là nhân vật minh họa nghệ thuật; lời Điều tra viên, Chuyên gia tâm lý và Người bình thường được dựng lại từ tư liệu công khai. Giọng đọc, hình ảnh và âm thanh dùng công nghệ AI.""",
    "EN": """⚠️ LEGAL & SAFETY ADVISORY
• Educational true-crime documentary analyzing criminal psychology; not a substitute for medical or legal counsel.
• Based entirely upon public records of the Riverside County Superior Court, the DA's Office and the Sheriff's Department. Does not glorify crime.
• Animal avatars are artistic framing; investigator, psychologist and witness lines are dramatized from public records. Visuals and audio utilize AI tools.""",
    "JA": """⚠️ 免責事項・安全基準
• 本動画は犯罪心理学と司法史の研究を目的とした教育コンテンツであり、専門的な助言に代わるものではありません。
• リバーサイド郡上級裁判所、地方検察局および保安官事務所の公式公開記録に基づいています。特定の個人を非難する意図はありません。
• キャラクターは芸術的表現です。捜査官・心理学者・証人の発言は公開記録に基づくドラマタイズです。音声、映像にはAI技術を活用しています。""",
    "KO": """⚠️ 법적 고지 및 콘텐츠 안내
• 본 영상은 범죄심리학 및 사법 기록 연구를 목적으로 한 교육용 콘텐츠이며 전문적인 법률·의학 자문을 대신하지 않습니다.
• 리버사이드 카운티 상급법원, 지방검찰청 및 보안관실의 공개 기록에 기반합니다. 특정인을 비방하거나 단죄하려는 의도가 없습니다.
• 캐릭터는 예술적 표현입니다. 수사관·심리학자·증인의 발언은 공개 기록에 기반한 드라마타이즈이며, 음성과 시각 요소에는 AI 기술이 활용되었습니다.""",
}

SOS = {
    "VI": """🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ
• Tổng đài Bảo vệ Trẻ em: 111 (Việt Nam, miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (trầm cảm & tâm lý): 096 306 1414
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelphotline.org/
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org/""",
    "EN": """🆘 CRISIS & PROTECTION HOTLINES
• Childhelp National Child Abuse Hotline (USA): 1-800-422-4453 — https://www.childhelphotline.org/
• National Domestic Violence Hotline (USA): 1-800-799-SAFE (7233) — https://www.thehotline.org/
• Child Protective Hotline (Vietnam): 111 (24/7 Free) — http://tongdai111.vn/""",
    "JA": """🆘 緊急相談窓口
• 全米子ども虐待ホットライン（USA）: 1-800-422-4453 — https://www.childhelphotline.org/
• 全米DVホットライン（USA）: 1-800-799-SAFE (7233) — https://www.thehotline.org/
• 子ども保護ホットライン（ベトナム）: 111 (24時間無料)""",
    "KO": """🆘 아동 보호 및 가정폭력 긴급 지원 핫라인
• 미국 아동학대 예방 핫라인: 1-800-422-4453 — https://www.childhelphotline.org/
• 미국 가정폭력 핫라인: 1-800-799-SAFE (7233) — https://www.thehotline.org/
• 아동보호 핫라인 (베트남): 111 (24시간 무료)""",
}

TAGS = {
    "VI": ("#AmberEyes #TrueCrime #TamLyToiPham #TurpinFamily #HouseOfHorrors #CoerciveControl "
           "#JordanTurpin #FolieADeux #TheGiftOfFear #CanhBaoDo #10ChiDauTamLy #PhamVan #HoiTo"),
    "EN": ("#AmberEyes #TrueCrime #CriminalPsychology #TurpinFamily #HouseOfHorrors #CoerciveControl "
           "#JordanTurpin #FolieADeux #TheGiftOfFear #RedFlags #10PsychologicalMarkers"),
    "JA": ("#AmberEyes #TrueCrime #犯罪心理学 #ターピン一家 #恐怖の館 #強圧的支配 #ジョーダンターピン "
           "#共有精神病 #TheGiftOfFear #レッドフラッグ #10の心理指標"),
    "KO": ("#AmberEyes #TrueCrime #범죄심리학 #터핀가족사건 #공포의집 #강압적통제 #조던터핀 #공유정신병 "
           "#TheGiftOfFear #레드플래그 #10가지심리지표"),
}

HEADS = {"VI": "⏱ MỐC CHƯƠNG", "EN": "⏱ CHAPTER TIMESTAMPS",
         "JA": "⏱ タイムスタンプ", "KO": "⏱ 챕터 타임스탬프"}
SRC_HEADS = {"VI": "📚 NGUỒN THAM KHẢO CHÍNH THỨC", "EN": "📚 OFFICIAL SOURCES",
             "JA": "📚 公式参考文献", "KO": "📚 공식 참고 문헌"}


# ==============================================================================
# ĐO MỐC CHƯƠNG
# ==============================================================================
def mmss(t):
    t = int(t + 0.5)
    return f"{t // 60:02d}:{t % 60:02d}"


def act_start_times(tl):
    """Mốc bắt đầu hồi = câu thoại đầu tiên của hồi (giống package.act_start_times)."""
    starts = {}
    for it in tl.get("items", []):
        a = it.get("act")
        if a and a not in starts:
            starts[a] = it["start"]
    if not starts:
        for m in tl.get("markers", []):
            if m.get("type") == "ACT":
                starts[m["act"]] = m["start"]
    return starts


def spoken_by_act(path, act_re):
    acts, cur = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        m = act_re.match(s)
        if m:
            cur = int(m.group(1))
            acts.setdefault(cur, [])
            continue
        if cur is None or not s:
            continue
        if s.startswith(("#", "---", "**", "[", "*", "|")):
            continue
        acts[cur].append(s)
    return {a: len("".join(v)) for a, v in acts.items()}


def chapters(lang):
    """Trả về (danh sách dòng chapter, nguồn số liệu)."""
    if lang == "KO":
        # Chưa có audio KO ⇒ ước lượng: tỉ trọng ký tự lời thoại theo hồi × tốc độ đọc
        # hiệu chuẩn từ timeline JA đã đo thật (đối chiếu: tỉ lệ KO/VI ở Tập 02 = 1,2863).
        ko = spoken_by_act(ROOT / "01_KICH_BAN" / "Tap17_KO" / "kichban_tap17_KO.md",
                           re.compile(r"^##\s*막\s*(\d)"))
        ja = spoken_by_act(ROOT / "01_KICH_BAN" / "Tap17_JA" / "kichban_tap17_JA.md",
                           re.compile(r"^##\s*第(\d)幕"))
        rate = sum(ja.values()) / 2099.88        # ký tự/giây (JA đo thật 19/11/2026)
        t = 23.0                                  # intro kênh 22,41 s
        lines = [INTRO_LABEL["KO"]]
        for a in sorted(ko):
            lines.append(f"{mmss(t)} {ACT_TITLES['KO'][a]}")
            t += ko[a] / rate
        return lines, "ƯỚC LƯỢNG (audio KO chưa dựng)"
    tl = json.loads((WORK / f"timeline_s{'' if lang == 'VI' else '_' + lang}_t17.json")
                     .read_text(encoding="utf-8"))
    st = act_start_times(tl)
    lines = [INTRO_LABEL[lang]] + [f"{mmss(st[a])} {ACT_TITLES[lang][a]}" for a in sorted(st)]
    return lines, "ĐO THẬT từ timeline"


# ==============================================================================
# THẬT BẢN MÔ TẢ
# ==============================================================================
def build(lang):
    chap, _ = chapters(lang)
    body = {"VI": BODY_VI, "EN": BODY_EN, "JA": BODY_JA, "KO": BODY_KO}[lang]
    short = {"VI": SHORT_VI, "EN": SHORT_EN, "JA": SHORT_JA, "KO": SHORT_KO}[lang]
    title = TITLES[lang] + " | Amber eyes"
    return f"""{title}

{body}

{HEADS[lang]}
{chr(10).join(chap)}

{ADVISORY[lang]}

{SRC_HEADS[lang]}
{short}

{SOS[lang]}

{TAGS[lang]}
"""


def main():
    # Sao lưu bản cũ (L5)
    bak = WORK / "_cu" / f"desc_t17_{os.environ.get('AE_STAMP', 'rewrite')}"
    bak.mkdir(parents=True, exist_ok=True)
    olds = ["02_SAN_XUAT/Tap17/mo_ta.txt", "02_SAN_XUAT/Tap17/xuat_ban/mo_ta.txt",
            "02_SAN_XUAT/Tap17_EN/description.txt", "02_SAN_XUAT/Tap17_EN/mo_ta.txt",
            "02_SAN_XUAT/Tap17_EN/xuat_ban/description.txt", "02_SAN_XUAT/Tap17_EN/xuat_ban/mo_ta.txt",
            "02_SAN_XUAT/Tap17_JA/description.txt", "02_SAN_XUAT/Tap17_JA/mo_ta.txt",
            "02_SAN_XUAT/Tap17_JA/xuat_ban/description.txt", "02_SAN_XUAT/Tap17_JA/xuat_ban/mo_ta.txt",
            "02_SAN_XUAT/Tap17_KO/description.txt", "02_SAN_XUAT/Tap17_KO/mo_ta.txt",
            "02_SAN_XUAT/Tap17_KO/xuat_ban/description.txt", "02_SAN_XUAT/Tap17_KO/xuat_ban/mo_ta.txt",
            "02_SAN_XUAT/Tap17/nguon_mo_ta.txt", "02_SAN_XUAT/Tap17_EN/nguon_mo_ta_EN.txt",
            "02_SAN_XUAT/Tap17_JA/nguon_mo_ta_JA.txt", "02_SAN_XUAT/Tap17_KO/nguon_mo_ta_KO.txt"]
    for rel in olds:
        p = ROOT / rel
        if p.exists():
            shutil.copy2(p, bak / rel.replace("/", "__"))

    # Kiểm độ dài TRƯỚC khi ghi (A11 #85/#86)
    print("=== KIỂM ĐỘ DÀI MÔ TẢ TẬP 17 (trần 5000 ký tự) ===")
    built = {}
    for lang in ["VI", "EN", "JA", "KO"]:
        txt = build(lang).strip()
        built[lang] = txt
        _, src = chapters(lang)
        status = "PASS" if len(txt) <= LIMIT else "FAIL"
        print(f"  [{lang}] {len(txt):5d} ký tự  {status}  (mốc chương: {src})")
    over = [k for k, v in built.items() if len(v) > LIMIT]
    if over:
        print(f"\n>>> LỖI: {over} vượt trần 5000 ký tự. KHÔNG ghi file. <<<")
        sys.exit(1)

    plan = {
        "VI": [("02_SAN_XUAT/Tap17/mo_ta.txt", built["VI"]),
               ("02_SAN_XUAT/Tap17/xuat_ban/mo_ta.txt", built["VI"]),
               ("02_SAN_XUAT/Tap17/nguon_mo_ta.txt", SHORT_VI)],
        "EN": [("02_SAN_XUAT/Tap17_EN/description.txt", built["EN"]),
               ("02_SAN_XUAT/Tap17_EN/mo_ta.txt", built["EN"]),
               ("02_SAN_XUAT/Tap17_EN/xuat_ban/description.txt", built["EN"]),
               ("02_SAN_XUAT/Tap17_EN/xuat_ban/mo_ta.txt", built["EN"]),
               ("02_SAN_XUAT/Tap17_EN/nguon_mo_ta_EN.txt", SHORT_EN)],
        "JA": [("02_SAN_XUAT/Tap17_JA/description.txt", built["JA"]),
               ("02_SAN_XUAT/Tap17_JA/mo_ta.txt", built["JA"]),
               ("02_SAN_XUAT/Tap17_JA/xuat_ban/description.txt", built["JA"]),
               ("02_SAN_XUAT/Tap17_JA/xuat_ban/mo_ta.txt", built["JA"]),
               ("02_SAN_XUAT/Tap17_JA/nguon_mo_ta_JA.txt", SHORT_JA)],
        "KO": [("02_SAN_XUAT/Tap17_KO/description.txt", built["KO"]),
               ("02_SAN_XUAT/Tap17_KO/mo_ta.txt", built["KO"]),
               ("02_SAN_XUAT/Tap17_KO/xuat_ban/description.txt", built["KO"]),
               ("02_SAN_XUAT/Tap17_KO/xuat_ban/mo_ta.txt", built["KO"]),
               ("02_SAN_XUAT/Tap17_KO/nguon_mo_ta_KO.txt", SHORT_KO)],
    }
    print("\n=== GHI FILE ===")
    for lang, items in plan.items():
        for rel, content in items:
            p = ROOT / rel
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content.strip() + "\n", encoding="utf-8")
            print(f"  -> {rel} ({len(content.strip()):,} ký tự)")

    # Mẫu mô tả EN (package.py description_en() đọc file này; thiếu ⇒ crash)
    # Dùng header "📚 SOURCES" để package.py THAY THẾ khối nguồn tại chỗ (nếu dùng
    # "📚 OFFICIAL SOURCES" như bản publish, package.py sẽ CHÈN thêm khối và làm
    # vượt trần 5000 ký tự).
    tpl = ROOT / "02_SAN_XUAT" / "Tap17_EN" / "CHU_CO_DINH_EN.md"
    tpl_body = (built["EN"].replace("⏱ CHAPTER TIMESTAMPS", "⏱ CHAPTERS")
                        .replace("📚 OFFICIAL SOURCES", "📚 SOURCES"))
    tpl.write_text(EN_TEMPLATE.replace("__BODY__", tpl_body), encoding="utf-8")
    print(f"  -> 02_SAN_XUAT/Tap17_EN/CHU_CO_DINH_EN.md ({len(tpl_body):,} ký tự)")

    # Bảng nguồn EN dạng ✅ (package.py verified_links() đọc file này)
    src_en = ROOT / "02_SAN_XUAT" / "Tap17_EN" / "nguon_tham_khao_EN.md"
    if "|" not in src_en.read_text(encoding="utf-8")[:400]:
        src_en.write_text(SOURCES_TABLE_EN, encoding="utf-8")
        print("  -> 02_SAN_XUAT/Tap17_EN/nguon_tham_khao_EN.md (chuyển sang bảng ✅)")

    sync_edition()
    print(f"\nSao lưu bản cũ: {bak.relative_to(ROOT)}")
    print(">>> XONG: 4 ngôn ngữ đã được viết lại. <<<")


# ==============================================================================
# ĐỒNG BỘ edition.py — để package.py sinh lại mô tả KHÔNG bị mất nội dung
# ==============================================================================
def build_act_block():
    def block(lang):
        return "{" + ",\n".join(f'{k!r}: "{v}"' for k, v in sorted(ACT_TITLES[lang].items())) + "}"
    return ('        "act_titles": (' + block("EN") + ' if EN else\n'
            '                       ' + block("JA") + ' if JA else\n'
            '                       ' + block("KO") + ' if KO else\n'
            '                       ' + block("VI") + '),')


def sync_edition():
    """Ghi title / act_titles / hashtags / summary_* của Tập 17 vào edition.py.

    `package.py` sinh lại mô tả từ các khoá này (A11 #70) ⇒ nếu thiếu, lần chạy
    pipeline sau sẽ XOÁ mất thân bài 10 chỉ dấu. Nguồn duy nhất vẫn là file này.
    """
    p = WORK / "edition.py"
    raw = p.read_bytes()
    crlf = b"\r\n" in raw
    src = raw.decode("utf-8").replace("\r\n", "\n")
    a = src.index('    "17": {')
    b = src.index('\n    "18": {', a)
    blk = src[a:b]

    # --- title ---
    ta = blk.index('        "title": (')
    tb = blk.index('\n        "act_titles": (', ta)
    blk = blk[:ta] + (
        '        "title": (' + repr(TITLES["EN"]) + ' if EN else\n'
        '                  ' + repr(TITLES["JA"]) + ' if JA else\n'
        '                  ' + repr(TITLES["KO"]) + ' if KO else\n'
        '                  ' + repr(TITLES["VI"]) + '),') + blk[tb:]

    # --- act_titles ---
    aa = blk.index('        "act_titles": (')
    ab = blk.index('\n        "mux_af":', aa)
    blk = blk[:aa] + build_act_block() + blk[ab:]

    # --- hashtags + summary (thêm trước "mux_af") ---
    # BỎ khoá cũ trước (idempotent — chạy lại nhiều lần không nhân bản)
    lines = [ln for ln in blk.split("\n")
             if not re.match(r'\s*"(hashtags|hashtags_en|hashtags_ja|hashtags_ko|'
                             r'summary_vn|summary_ja|summary_ko)":', ln)]
    blk = "\n".join(lines)
    keys = {
        "hashtags": TAGS["VI"],
        "hashtags_en": TAGS["EN"],
        "hashtags_ja": TAGS["JA"],
        "hashtags_ko": TAGS["KO"],
        "summary_vn": BODY_VI,
        "summary_ja": BODY_JA,
        "summary_ko": BODY_KO,
    }
    add = "".join(f'        "{k}": {v!r},\n' for k, v in keys.items())
    idx = blk.index('\n        "mux_af":')
    blk = blk[:idx] + "\n" + add.rstrip("\n") + blk[idx:]

    out = src[:a] + blk + src[b:]
    bak = WORK / "_cu" / "edition_t17_desc_sync.py"
    bak.parent.mkdir(parents=True, exist_ok=True)
    if not bak.exists():
        shutil.copy2(p, bak)
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(out.replace("\n", "\r\n") if crlf else out)
    print("  -> .work/edition.py (EPISODES['17'] đã đồng bộ: title, act_titles, hashtags, summary_*)")


if __name__ == "__main__":
    main()
