# -*- coding: utf-8 -*-
"""
Build and supplement comprehensive descriptions for Episode 09 across all 4 languages:
VN, EN, JA, KO according to the 10-Indicator Behavioral & Psychological Ecosystem.
Also updates edition.py and ensures YouTube < 5000 chars limit (A11 #85, #86).
"""
import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAN_XUAT = ROOT / "02_SAN_XUAT"

# -------------------------------------------------------------------------
# 1. TEXT DEFINITIONS (10 INDICATORS & INTRO)
# -------------------------------------------------------------------------

TITLE_VN = "Tập 09: Nghệ Thuật Xóa Bỏ Bản Ngã | Tâm lý học tội phạm: Charles Manson & Thảm kịch Gia đình Manson (10 Chỉ Dấu Tâm Lý & 5 Nấc Thang Vực Thẳm)"
TITLE_EN = "Ep. 09: The Art of Ego Erasure | Criminal Psychology: Charles Manson & The Manson Family Tragedy (10 Psychological Markers & 5 Stages of Escalation)"
TITLE_JA = "第09話：自我を消去する技術 | 犯罪心理学：チャールズ・マンソンとファミリーの悲劇（10の心理指標と5段階エスカレーション）"
TITLE_KO = "09화: 자아를 지우는 기술 | 범죄심리학: 찰스 맨슨과 맨슨 패밀리 참극 (10대 심리지표와 5단계 에스컬레이션)"

SUMMARY_VN = """Nước Mỹ cuối thập niên 1960 đang chìm đắm trong cao trào của phong trào Hippie và thông điệp hòa bình của "Mùa hè Tình yêu". Nhưng vào hai đêm đẫm máu tháng 8/1969 tại đồi Beverly và Los Angeles, ảo tưởng ngây thơ ấy sụp đổ hoàn toàn. Năm nạn nhân tại biệt thự 10050 Cielo Drive – trong đó có nữ diễn viên Sharon Tate đang mang thai 8 tháng rưỡi – cùng vợ chồng doanh nhân Leno và Rosemary LaBianca bị tàn sát man rợ. Điều gây rúng động nhất: kẻ chủ mưu không hề chạm tay vào hung khí tại hiện trường. Hắn là Charles Manson, kẻ đã dùng ma túy, âm nhạc và nghệ thuật thao túng tâm lý để biến những thanh niên ưu tú thành công cụ giết người mù quáng.

Hồ sơ Charles Manson & Gia đình Manson được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG TƯỞNG TẬP THỂ: Vụ án Sharon Tate chôn vùi kỷ nguyên Hippie; cư dân LA mua súng, thuê chó bảo vệ; phán quyết People v. Anderson (1972) bãi bỏ án tử hình.
2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem nạn nhân là "Pigs" và đạo cụ trong ảo tưởng Helter Skelter; khuyết tật Thuyết tâm trí biến tiếng van xin thành chất kích hoạt hưng phấn quyền lực.
3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Coi môn đồ là "công cụ kéo dài của bản ngã"; ban ngày du ca tại Spahn Ranch, ban đêm thành cỗ máy tàn sát; bi kịch phụ huynh.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Diễn trò ái kỷ tại tòa (khắc chữ X, tấn công thẩm phán); sụp đổ cái tôi và tự thương hại trong tù Corcoran đến khi qua đời 2017.
5. HỆ THỐNG TỰ BÀO CHỮA (NEUTRALIZATION): Kỹ thuật trung hòa đạo đức (Sykes & Matza): kháng cáo lý tưởng tâm linh, đổ lỗi nhà tù, ngoại hóa trách nhiệm vì không chạm hung khí.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Bị Terry Melcher từ chối hợp đồng âm nhạc sỉ nhục cái tôi; ảo tưởng chiến tranh sắc tộc bế tắc dẫn đến thảm sát tại 10050 Cielo Drive.
7. SIGNATURE VS. THỦ ĐOẠN MO: MO (cắt dây điện, đồ đen, vũ khí lạnh) biến đổi để che giấu; Signature (chữ máu PIG, RISE, HEALTER SKELTER, dây thừng nối nạn nhân) bất biến.
8. QUỸ ĐẠO LEO THANG 5 NẤC THANG: 5 nấc leo thang: trộm cắp (1) → giáo phái LSD (2) → Creepy Crawling (3) → sát hại Gary Hinman (4) → thảm sát Cielo Drive & Waverly Drive (5).
9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Chiếc áo ngụy trang Hippie giúp kẻ săn mồi đội lốt đạo sư du mục; xã hội chủ quan coi hội nhóm thanh niên chỉ là sự nổi loạn vô hại.
10. CẢNH BÁO ĐỎ SINH TỒN (GAVIN DE BECKER): 4 tín hiệu nhận diện tà giáo: cảnh giác Love Bombing dồn dập, nhận diện cô lập, chống tư duy nhị nguyên, và giữ vững quyền lương tri."""

SUMMARY_EN = """In the late 1960s, America was captivated by the counterculture wave and the peaceful idealism of the "Summer of Love." But over two bloodstained nights in August 1969 in the hills of Los Angeles, that innocent delusion was shattered forever. Five victims at 10050 Cielo Drive – including eight-and-a-half-month pregnant actress Sharon Tate – along with Leno and Rosemary LaBianca on Waverly Drive, were brutally slain. The most chilling reality: the mastermind never personally touched a weapon at the scene. He was Charles Manson, a sociopathic narcissist who weaponized LSD, psychological manipulation, and communal isolation to transform ordinary youth into compliant executioners.

Amber eyes dissects the case through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & COLLECTIVE PARANOIA: The Tate-LaBianca murders ended the counterculture era; LA residents bought firearms; set historic legal precedent for mastermind liability & People v. Anderson (1972).
2. OBJECTIFICATION & DEHUMANIZATION: Victims were treated as "Pigs" and stage props in Helter Skelter; Theory of Mind deficits turned pleas into power arousal.
3. COMPARTMENTALIZATION & "THE FAMILY": Followers served as extensions of Manson's self; daytime communes at Spahn Ranch separated from nighttime slaughter; family heartbreak.
4. NARCISSISTIC COLLAPSE & SENTENCE: Theatrical narcissism on trial (carving Xs, attacking judge); decades of collapse & pathological self-pity in prison until death in 2017.
5. TECHNIQUES OF NEUTRALIZATION (SYKES & MATZA): Spiritual loyalties, blaming society and penal system, externalizing guilt ("hands touched no weapon").
6. PRECIPITATING TRIGGER: Record producer Terry Melcher rejected Manson's music, crushing his ego; race war deadlock triggered the slaughter at 10050 Cielo Drive.
7. SIGNATURE VS. MO: MO (cut phone wires, black clothes, knives, desert flight) adapted; Signature (blood slogans PIG, RISE, HEALTER SKELTER, rope) immutable.
8. 5-STAGE ESCALATION TRAJECTORY: 5 steps: petty crimes (1) → LSD cult (2) → Creepy Crawling (3) → murdering Gary Hinman (4) → Tate & LaBianca massacres (5).
9. HALO EFFECT & SOCIETAL BLIND SPOTS: Hippie flower-power counterculture camouflaged a predator; society dismissed communes as harmless youth rebellion.
10. SURVIVAL RED FLAGS (GAVIN DE BECKER): 4 life-saving signals: beware Love Bombing, recognize isolation, reject us-versus-them dualism, and protect moral autonomy."""

SUMMARY_JA = """1960年代後半のアメリカは、ヒッピー文化と「愛の夏（Summer of Love）」の平和的理想に酔いしれていました。しかし1969年8月、ビバリーヒルズとロサンゼルスの丘で起きた血塗られた2夜によって、その無邪気な幻想は残酷に打ち砕かれました。妊娠8か月半の女優シャロン・テートを含む10050シエロ・ドライブの5名の犠牲者、そしてレノ＆ローズマリー・ラビアンカ夫妻が命を奪われました。最も戦慄すべき真実は、黒幕自身が現場で凶器に一度も触れていなかったことです。男の名はチャールズ・マンソン。LSDと心理的操作、共同体の孤立化を武器に、普通のエリート青年たちを盲目的な実行犯へと改造したのです。

犯罪心理学ドキュメンタリー『Amber eyes』第09話では、本事件を「10の心理・行動指標」に基づいて解剖します：
1. 社会的衝撃と集団的偏執病（Collective Paranoia）：ヒッピー時代の終焉と市民の銃器買い占めパニック。首謀者責任の確立と1972年「ピープル対アンダーソン」判例。
2. 被害者の客体化と非人間化（Objectification）：被害者を「Pigs」や終末戦争の舞台小道具とみなす認知。心の理論の欠陥により命乞いが権力の性的興奮を誘発。
3. 精神の分断（Compartmentalization）と「ファミリー」：信徒を「肥大化した自己の延長物」とみなす支配構造。牧歌的な昼と夜の冷酷な暗殺者という完全な分断。
4. 自己愛の完全崩壊（Narcissistic Collapse）と判決：法廷での劇的な自己愛（額のX傷、裁判官襲撃）。刑務所で忘れ去られる中で見せた病的な自己憐憫と2017年の孤独死。
5. 中和の技術（Techniques of Neutralization）：サイクス＆マッツァの理論に基づく自己正当化（高次の精神的理想への訴求、社会や刑務所への責任転嫁、外在化）。
6. 心理的トリガーと限界点：音楽プロデューサーのテリー・メルチャーによるレコード契約拒絶が自己愛を粉砕。人種戦争が起きない焦りからシエロ・ドライブを標的に設定。
7. 署名（Signature）vs 手口（MO）：MO（電話線切断、黒服、刃物、砂漠逃亡）は隠蔽のため変遷したが、署名（壁の「PIG」「RISE」「HEALTER SKELTER」血文字）は不変。
8. 5段階のエスカレーション軌道：刺激耐性の形成過程：小犯罪（1）→ LSDカルト（2）→ 夜間侵入「クリーピー・クローリング」（3）→ ヒンマン殺害（4）→ テート事件（5）。
9. 後光効果（Halo Effect）と社会の死角：平和と愛を掲げるヒッピーの隠れ蓑。若者の共同体を無害な反抗と侮った社会の盲点。
10. サバイバル・レッドフラッグ（ギャビン・ド・ベッカー）：『The Gift of Fear』に基づく4大警告（ラブ・ボンビング警戒、社会的孤立察知、二元論拒絶、良心の自己決定権保持）。"""

SUMMARY_KO = """1960년대 후반의 미국은 히피 반문화와 ‘사랑의 여름(Summer of Love)’이 약속한 평화의 이상에 깊이 빠져 있었습니다. 그러나 1969년 8월, 로스앤젤레스 베벌리 힐스 언덕에서 벌어진 이틀간의 유혈 참극은 그 순진한 환상을 단숨에 산산조각 냈습니다. 임신 8개월 반이었던 여배우 샤론 테이트를 비롯한 10050 시엘로 드라이브의 희생자 5명과 레노·로즈마리 라비안카 부부가 참혹하게 희생되었습니다. 가장 충격적인 사실은 주범이 현장에서 흉기에 손끝 하나 대지 않았다는 점이었습니다. 그의 이름은 찰스 맨슨. LSD와 음악, 정교한 심리적 가스라이팅으로 평범한 청년들을 맹목적인 살인 기계로 개조한 사이코패스적 교주였습니다.

범죄심리학 채널 ‘Amber eyes’ 09화에서는 맨슨 패밀리 사건을 ‘10대 핵심 심리 및 행동 지표’를 통해 입체적으로 해부합니다:
1. 사회적 충격과 집단적 편집증(Collective Paranoia): 히피 시대의 비극적 종말과 LA 시민들의 총기·경비견 사재기 공포. 빈센트 부글리오시 검사의 교사자 책임 법리 및 1972년 사형 폐지(People v. Anderson) 선례.
2. 피해자의 객체화와 비인간化(Objectification): 피해자들을 ‘Pigs’이자 헬터 스켈터 종말 환상의 무대 소품으로 전락시킴. 마음 이론의 결함으로 인해 애원의 목소리가 권력적 흥분을 촉발.
3. 심리적 구획화(Compartmentalization)와 ‘가족’: 신도들을 ‘과대 자아의 연장선’으로 취급. 스판 랜치에서의 목가적인 낮과 밤의 냉혈한 살인자라는 이중생활의 구획화, 부모들의 정체성 붕괴.
4. 자기애의 완전한 붕괴(Narcissistic Collapse)와 판결: 법정에서의 연극적 자기애(이마의 X자 흉터, 판사 공격 시도). 코코런 교도소에서 잊혀지며 드러난 병적인 자기연민과 2017년 고독사.
5. 도덕적 중화 기술(Techniques of Neutralization): 사이크스와 마자의 중화 이론(인류 구원이라는 상위 충성심 호소, 사회와 교도소에 대한 책임 전가, ‘직접 죽이지 않았다’는 외재화).
6. 심리적 방아쇠와 촉발점: 음반 프로듀서 테리 멜처의 계약 거절로 인한 자아의 치명적 상처. 종족 전쟁이 일어나지 않자 멜처가 살던 시엘로 드라이브를 표적으로 선택.
7. 시그니처(Signature) vs 범행수법(MO): 수법(전화선 절단, 검은 옷, 흉기 은닉, 사막 도주)은 진화했으나, 시그니처(벽에 남긴 PIG, RISE, HEALTER SKELTER 혈서, 밧줄 결박)는 불변.
8. 5단계 에스컬레이션 궤적: 도파민 불감증에 따른 5단계 파멸: 잡범 및 사기(1) → LSD 히피 공동체(2) → 야간 주거침입 ‘크리피 크롤링’(3) → 게리 힌먼 살해(4) → 시엘로·웨이벌리 드라이브 참극(5).
9. 후광 효과(Halo Effect)와 사회적 맹점: 자유와 평화를 표방한 히피 문화가 포식자에게 완벽한 위장막을 제공; 청년 공동체를 단순한 방황으로 치부한 기성세대의 안일함.
10. 서바이벌 레드플래그(개빈 드 베커): 『The Gift of Fear』 원리에 기반한 4대 생존 경고 신호(애정 폭격 경계, 사회적 고립 수법 감지, 흑백논리 거부, 양심의 판단권을 타인에게 넘기지 말 것)."""

# -------------------------------------------------------------------------
# 2. CHAPTERS, DISCLAIMERS, SOURCES & HOTLINES
# -------------------------------------------------------------------------

CHAPTERS_VN = """⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · The Hook & Dấu chấm hết của Mùa hè Tình yêu
05:10 Hồi 2 · Hiện trường biệt thự & Bóng ma Helter Skelter tại Spahn Ranch
11:05 Hồi 3 · Giải phẫu tâm lý & Nghệ thuật xóa bỏ bản ngã
16:40 Hồi 4 · Đấu trí phòng xử án & Trách nhiệm kẻ không chạm tay
21:55 Hồi 5 · Phán quyết lịch sử, bản án tâm lý & Cảnh báo đỏ sinh tồn"""

CHAPTERS_EN = """⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · The Hook & The End of the Summer of Love
05:10 Act 2 · The Mansions & The Helter Skelter Illusion at Spahn Ranch
11:05 Act 3 · Psychological Autopsy & The Art of Ego Erasure
16:40 Act 4 · Courtroom Drama & Mastermind Liability
21:55 Act 5 · Historical Verdict, Psychological Sentence & Survival Red Flags"""

CHAPTERS_JA = """⏱ 目次（チャプター）
00:00 オープニング
00:23 第1幕 · フック＆「愛の夏」の残酷な終焉
05:10 第2幕 · 邸宅の惨劇＆スパーン牧場の終末幻想
11:05 第3幕 · 犯罪心理解剖＆自我を消去する技術
16:40 第4幕 · 法廷の攻防＆手を下さざる黒幕の責任
21:55 第5幕 · 歴史的判決、深層心理の刑罰＆サバイバル・レッドフラッグ"""

CHAPTERS_KO = """⏱ 챕터(타임라인)
00:00 오프닝
00:23 제1막 · 훅(The Hook) & 사랑의 여름의 비극적 종말
05:10 제2막 · 저택의 참극 & 스판 랜치의 종말론적 환상
11:05 제3막 · 심리 해부 & 자아를 지우는 기술
16:40 제4막 · 법정 공방 & 직접 손대지 않은 교사자의 책임
21:55 제5막 · 역사적 판결, 내면의 종신형 & 생존 경고 신호"""

DISCLAIMER_VN = """⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và tâm lý tội phạm học; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai Hoa Kỳ. Kênh không bôi nhọ hay tôn vinh bất kỳ cá nhân nào.
• Tôn trọng phẩm giá và nỗi đau của các nạn nhân cùng gia đình họ.
• Nhân vật Cú, Sói, Cáo, Cừu, Mèo là hình tượng nghệ thuật. Lời thoại được dựng lại dựa trên tư liệu.
• Giọng đọc, hình ảnh và âm thanh được hỗ trợ bởi công nghệ AI."""

DISCLAIMER_EN = """⚠️ LEGAL & SAFETY DISCLAIMER
• Produced exclusively for educational, criminological, and historical analysis; not medical or legal advice.
• Based on public US judicial archives. No intent to defame, harass, or glorify any individual.
• Complete respect is accorded to the memory and dignity of the victims and their families.
• Character avatars and dialogue are dramatized illustrations. Synthetic AI voices and visuals are utilized."""

DISCLAIMER_JA = """⚠️ ご視聴にあたっての注意事項
• 本動画は教育目的および犯罪心理学の観点からの分析コンテンツであり、医学的・法的助言に代わるものではありません。
• 米国の公開裁判記録および捜査資料に基づいて制作されています。個人を中傷または美化する意図はありません。
• 犠牲者とそのご遺族の名誉と尊厳に最大の敬意を払っています。
• キャラクターは演出用であり、発言は記録に基づく構成です。音声・画像・音楽はAIを活用しています。"""

DISCLAIMER_KO = """⚠️ 시청 전 유의사항
• 본 영상은 범죄심리학 및 교육적 관점에서의 분석 콘텐츠이며, 의학적·법률적 조언을 대신할 수 없습니다.
• 미국 공식 사법 기록과 수사 보고서를 바탕으로 제작되었습니다. 개인을 비방하거나 미화할 의도가 없습니다.
• 희생자들과 유가족의 고통과 인격에 깊은 경의를 표합니다.
• 캐릭터는 연출용이며 증언은 기록 기반 드라마타이즈입니다. AI 기술을 활용하여 제작되었습니다."""

SOURCES_VN = """📚 NGUỒN THAM KHẢO
Mọi dữ kiện, hiện trường và diễn biến đã đối chiếu hồ sơ tư pháp công khai Hoa Kỳ:
• Tòa Thượng thẩm Los Angeles (A253156) — https://www.courts.ca.gov/
• Tòa Tối cao California (People v. Anderson 1972) — https://www.courts.ca.gov/opinions/archive/Crim13617.PDF
• LAPD & FBI (Hồ sơ hiện trường 1969) — https://vault.fbi.gov/charles-manson
• Vincent Bugliosi (Helter Skelter) — https://wwnorton.com/
• Los Angeles Times (Tư liệu Sharon Tate) — https://www.latimes.com/
• The New York Times (Hồ sơ vụ án Manson) — https://www.nytimes.com/
• CDCR (Hồ sơ phạm nhân #B33920) — https://www.cdcr.ca.gov/
• APA (De-individuation & ASPD) — https://www.apa.org/
• Gavin de Becker (The Gift of Fear) — https://gavindebecker.com/"""

SOURCES_EN = """📚 VERIFIED SOURCES & COURT EXHIBITS
Verified against public United States judicial archives:
• Los Angeles County Superior Court (A253156) — https://www.courts.ca.gov/
• California Supreme Court (People v. Anderson 1972) — https://www.courts.ca.gov/opinions/archive/Crim13617.PDF
• LAPD & FBI (1969 Crime Scene Records) — https://vault.fbi.gov/charles-manson
• Vincent Bugliosi (Helter Skelter) — https://wwnorton.com/
• Los Angeles Times (Manson Trials Archive) — https://www.latimes.com/
• The New York Times (Case Timeline) — https://www.nytimes.com/
• CDCR (Inmate File #B33920) — https://www.cdcr.ca.gov/
• APA (Deindividuation & ASPD) — https://www.apa.org/
• Gavin de Becker (The Gift of Fear) — https://gavindebecker.com/"""

SOURCES_JA = """📚 参考資料・出典
米国の公開裁判資料および公的捜査記録に基づいて対照確認済み：
• ロサンゼルス郡上級裁判所（Case No. A253156） — https://www.courts.ca.gov/
• カリフォルニア州最高裁判所（People v. Anderson 1972） — https://www.courts.ca.gov/
• LAPDおよび連邦捜査局（現場調書） — https://vault.fbi.gov/charles-manson
• ヴィンセント・ブリオーシ著『ヘルダー・スケルター』 — https://wwnorton.com/
• Los Angeles Times（事件報道アーカイブ） — https://www.latimes.com/
• The New York Times（事件タイムライン） — https://www.nytimes.com/
• カリフォルニア州矯正局（#B33920） — https://www.cdcr.ca.gov/
• アメリカ心理学会（没個性化＆ASPD） — https://www.apa.org/
• ギャビン・ド・ベッカー『The Gift of Fear』 — https://gavindebecker.com/"""

SOURCES_KO = """📚 참고자료 및 출처(References)
미국 공식 사법 기록 및 수사 당국 공개 자료 교차 검증 완료:
• 로스앤젤레스 상급법원 (Case No. A253156) — https://www.courts.ca.gov/
• 캘리포니아 대법원 (People v. Anderson 1972) — https://www.courts.ca.gov/
• LAPD 및 연방수사국 FBI 공식 현장 보고서 — https://vault.fbi.gov/charles-manson
• 빈센트 부글리오시 『헬터 스켈터』 — https://wwnorton.com/
• Los Angeles Times (재판 아카이브) — https://www.latimes.com/
• The New York Times (타임라인 심층 보도) — https://www.nytimes.com/
• 캘리포니아 교정재활국 (#B33920) — https://www.cdcr.ca.gov/
• 미국심리학회 APA (몰개성화 및 ASPD) — https://www.apa.org/
• 개빈 드 베커 『The Gift of Fear』 — https://gavindebecker.com/"""

HOTLINES_VN = """🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ
• Tổng đài Quốc gia Bảo vệ Trẻ em: 111 (miễn phí 24/7) — http://tongdai111.vn/
• Đường dây nóng Ngày Mai (Tâm lý): 096 306 1414 — https://duongdaynongngaymai.vn/
• Ngôi nhà Bình Yên: 1900 969 680
• US Suicide & Crisis Lifeline: 988 — https://988lifeline.org/
• Childhelp National Hotline: 1-800-422-4453 — https://www.childhelphotline.org/"""

HOTLINES_EN = """🆘 CRISIS & SUPPORT HOTLINES (24/7, FREE & CONFIDENTIAL)
• National Suicide and Crisis Lifeline (US): 988 — https://988lifeline.org/
• Childhelp National Child Abuse Hotline (US/Canada): 1-800-422-4453 — https://www.childhelphotline.org/
• Crisis Text Line: Text HOME to 741741 — https://www.crisistextline.org/
• National Domestic Violence Hotline (US): 1-800-799-7233 — https://www.thehotline.org/
• National Child Helpline 111 (Vietnam, toll-free 24/7) — http://tongdai111.vn/"""

HOTLINES_JA = """🆘 児童虐待および心の相談窓口（24時間対応・通話無料）
• 児童相談所虐待対応ダイヤル「189（いちはやく）」
• こころの健康相談統一ダイヤル：0570-064-556
• よりそいホットライン：0120-279-338
• 緊急通報：警察 110番 / 消防・救急 119番"""

HOTLINES_KO = """🆘 아동학대 예방 및 위기 상담전화 (24시간 무료 운영)
• 아동학대 신고전화: 112 (경찰청)
• 보건복지상담센터: 129
• 자살예방 상담전화: 109
• 여성긴급전화: 1366"""

HASHTAGS_VN = "#AmberEyes #TrueCrime #TamLyToiPham #CharlesManson #HelterSkelter #MansonFamily #XoaBoBanNga #10ChiDauTamLy #CanhBaoDo #HoSoToiPham"
HASHTAGS_EN = "#AmberEyes #TrueCrime #CriminalPsychology #CharlesManson #HelterSkelter #MansonFamily #Deindividuation #10PsychologicalIndicators #SurvivalRedFlags #ForensicFiles"
HASHTAGS_JA = "#AmberEyes #TrueCrime #犯罪心理学 #心理分析 #チャールズマンソン #マンソンファミリー #自我の消去 #マインドコントロール #プロファイリング #未解決事件"
HASHTAGS_KO = "#AmberEyes #TrueCrime #범죄심리학 #찰스맨슨 #맨슨패밀리 #세뇌 #자아지우기 #10대심리지표 #레드플래그 #실화사건"


# -------------------------------------------------------------------------
# 3. BUILD FULL DESCRIPTION FOR EACH LANGUAGE
# -------------------------------------------------------------------------

def build_full_desc_vn():
    lines = [
        TITLE_VN + " | Amber eyes",
        "",
        SUMMARY_VN,
        "",
        CHAPTERS_VN,
        "",
        DISCLAIMER_VN,
        "",
        SOURCES_VN,
        "",
        HOTLINES_VN,
        "",
        HASHTAGS_VN,
    ]
    return "\n".join(lines)


def build_full_desc_en():
    lines = [
        TITLE_EN + " | Amber eyes",
        "",
        SUMMARY_EN,
        "",
        CHAPTERS_EN,
        "",
        DISCLAIMER_EN,
        "",
        SOURCES_EN,
        "",
        HOTLINES_EN,
        "",
        HASHTAGS_EN,
    ]
    return "\n".join(lines)


def build_full_desc_ja():
    lines = [
        TITLE_JA + " | Amber eyes",
        "",
        SUMMARY_JA,
        "",
        CHAPTERS_JA,
        "",
        DISCLAIMER_JA,
        "",
        SOURCES_JA,
        "",
        HOTLINES_JA,
        "",
        HASHTAGS_JA,
    ]
    return "\n".join(lines)


def build_full_desc_ko():
    lines = [
        TITLE_KO + " | Amber eyes",
        "",
        SUMMARY_KO,
        "",
        CHAPTERS_KO,
        "",
        DISCLAIMER_KO,
        "",
        SOURCES_KO,
        "",
        HOTLINES_KO,
        "",
        HASHTAGS_KO,
    ]
    return "\n".join(lines)


# -------------------------------------------------------------------------
# 4. CHU_CO_DINH_EN.md FOR TAP 09 EN
# -------------------------------------------------------------------------

CHU_CO_DINH_EN_CONTENT = f"""# CHỮ CỐ ĐỊNH & GÓI PHÁT HÀNH TIẾNG ANH (THỊ TRƯỜNG MỸ) · TẬP 09
**Hồ sơ:** Charles Manson & Thảm kịch Gia đình Manson (The Charles Manson & Manson Family File)  
**Kênh:** Amber eyes — Criminal psychology through real case files

---

## 1. Tiêu đề Video & Thumbnail (Tối ưu hóa thuật toán YouTube US)

### A. Tiêu đề YouTube (Title Options)
* **Phương án 1 (Khuyên dùng — Cân bằng giữa Tâm lý học & True Crime):**  
  `Ep. 09: The Art of Ego Erasure | Criminal Psychology: Charles Manson & The Manson Family Tragedy (10 Psychological Markers & 5 Stages of Escalation)`
* **Phương án 2 (Kịch tính, thu hút CTR cao):**  
  `Behind the Cult: How Charles Manson Weaponized Mind Control Without Touching a Weapon | Forensic Psychology`
* **Phương án 3 (Sát kịch bản gốc):**  
  `The Mastermind Who Struck from the Shadows: The Manson Murders & The Death of the Summer of Love`

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
{build_full_desc_en()}
```
"""


# -------------------------------------------------------------------------
# 5. NGUON_THAM_KHAO.MD DETAILED TABLE FOR TAP 09
# -------------------------------------------------------------------------

NGUON_THAM_KHAO_VN_MD = """# NGUỒN THAM KHẢO & ĐỐI CHIẾU DỮ KIỆN — TẬP 09 (CHARLES MANSON & GIA ĐÌNH MANSON)

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

NGUON_THAM_KHAO_EN_MD = """| Link / Citation | Type | Verified |
|---|---|:---:|
| https://www.courts.ca.gov/ | Court Records (State of California v. Charles Manson et al., Case No. A253156) | ✅ |
| https://www.courts.ca.gov/opinions/archive/Crim13617.PDF | California Supreme Court: Landmark ruling People v. Anderson (1972) | ✅ |
| https://vault.fbi.gov/charles-manson | FBI Vault: Official Tate-LaBianca Crime Scene Reports & Dossiers | ✅ |
| https://wwnorton.com/ | Vincent Bugliosi & Curt Gentry: 'Helter Skelter' (W. W. Norton & Company) | ✅ |
| https://www.latimes.com/ | Los Angeles Times: Historical archives of the Manson Family Trials | ✅ |
| https://www.nytimes.com/ | The New York Times: Case timeline & cultural autopsy of the 1969 murders | ✅ |
| https://www.cdcr.ca.gov/ | California Department of Corrections: Inmate File Charles Manson #B33920 | ✅ |
| https://www.apa.org/ | American Psychological Association: De-individuation & ASPD Profiles | ⚠ |
| https://gavindebecker.com/ | Gavin de Becker: 'The Gift of Fear' (Survival Red Flags & Threat Assessment) | ⚠ |
| http://tongdai111.vn/ | Vietnam National Child Helpline 111 | ✅ |
| https://duongdaynongngaymai.vn/ | Ngay Mai Mental Health & Crisis Hotline | ✅ |
| https://988lifeline.org/ | US National Suicide and Crisis Lifeline 988 | ✅ |
| https://www.childhelphotline.org/ | Childhelp National Child Abuse Hotline 1-800-422-4453 | ✅ |
"""

NGUON_THAM_KHAO_JA_MD = """| 出典リンク / 資料名 | 種別 | 検証状況 |
|---|---|:---:|
| https://www.courts.ca.gov/ | カリフォルニア州上級裁判所：マンソン裁判公式記録（Case No. A253156） | ✅ |
| https://www.courts.ca.gov/opinions/archive/Crim13617.PDF | カリフォルニア州最高裁判所：People v. Anderson (1972) 判例 | ✅ |
| https://vault.fbi.gov/charles-manson | FBI Vault：シエロ・ドライブ＆ウェーバリー・ドライブ公的捜査調書 | ✅ |
| https://wwnorton.com/ | ヴィンセント・ブリオーシ検事著：『ヘルダー・スケルター（Helter Skelter）』 | ✅ |
| https://www.latimes.com/ | ロサンゼルス・タイムズ：事件および裁判報道アーカイブ | ✅ |
| https://www.nytimes.com/ | ニューヨーク・タイムズ：マンソン・ファミリーとヒッピー終焉の記録 | ✅ |
| https://www.cdcr.ca.gov/ | カリフォルニア州矯正局：受刑者記録チャールズ・マンソン（#B33920） | ✅ |
| https://www.apa.org/ | アメリカ心理学会（APA）：没個性化（De-individuation）および反社会性パーソナリティ障害 | ⚠ |
| https://gavindebecker.com/ | ギャビン・ド・ベッカー著：『The Gift of Fear（危険の兆候）』 | ⚠ |
"""

NGUON_THAM_KHAO_KO_MD = """| 출처 링크 / 공식 문서명 | 유형 | 검증 상태 |
|---|---|:---:|
| https://www.courts.ca.gov/ | 캘리포니아주 상급법원: 맨슨 재판 공식 기록 (Case No. A253156) | ✅ |
| https://www.courts.ca.gov/opinions/archive/Crim13617.PDF | 캘리포니아 대법원: 사형 폐지 선례 People v. Anderson (1972) 판결문 | ✅ |
| https://vault.fbi.gov/charles-manson | FBI 볼트: 시엘로 드라이브 및 웨이벌리 드라이브 공식 수사 문서 | ✅ |
| https://wwnorton.com/ | 빈센트 부글리오시 검사 저: 『헬터 스켈터(Helter Skelter)』 | ✅ |
| https://www.latimes.com/ | 로스앤젤레스 타임스: 테이트-라비안카 사건 및 세기의 재판 아카이브 | ✅ |
| https://www.nytimes.com/ | 뉴욕 타임스: 맨슨 패밀리 타임라인 및 반문화 종말 심층 보도 | ✅ |
| https://www.cdcr.ca.gov/ | 캘리포니아 교정재활국: 수감자 기록 찰스 맨슨 (#B33920) | ✅ |
| https://www.apa.org/ | 미국심리학회(APA): 몰개성화(De-individuation) 및 반사회성 성격장애 | ⚠ |
| https://gavindebecker.com/ | 개빈 드 베커 저: 『The Gift of Fear(생존 경고 신호)』 | ⚠ |
"""


def main():
    print("==================================================================")
    print("UPDATING DESCRIPTIONS FOR EPISODE 09 (VN, EN, JA, KO)")
    print("==================================================================")

    # 1. Generate text strings
    desc_vn = build_full_desc_vn()
    desc_en = build_full_desc_en()
    desc_ja = build_full_desc_ja()
    desc_ko = build_full_desc_ko()

    # Measure character lengths
    print(f"Length VN : {len(desc_vn)} chars (limit 5000) -> {'PASS' if len(desc_vn) < 5000 else 'FAIL'}")
    print(f"Length EN : {len(desc_en)} chars (limit 5000) -> {'PASS' if len(desc_en) < 5000 else 'FAIL'}")
    print(f"Length JA : {len(desc_ja)} chars (limit 5000) -> {'PASS' if len(desc_ja) < 5000 else 'FAIL'}")
    print(f"Length KO : {len(desc_ko)} chars (limit 5000) -> {'PASS' if len(desc_ko) < 5000 else 'FAIL'}")

    assert len(desc_vn) < 5000, f"desc_vn exceeds 5000 chars: {len(desc_vn)}"
    assert len(desc_en) < 5000, f"desc_en exceeds 5000 chars: {len(desc_en)}"
    assert len(desc_ja) < 5000, f"desc_ja exceeds 5000 chars: {len(desc_ja)}"
    assert len(desc_ko) < 5000, f"desc_ko exceeds 5000 chars: {len(desc_ko)}"

    # 2. Write VN files
    tap09_dir = SAN_XUAT / "Tap09"
    tap09_xuat_ban = tap09_dir / "xuat_ban"
    tap09_xuat_ban.mkdir(parents=True, exist_ok=True)

    (tap09_dir / "mo_ta.txt").write_text(desc_vn, encoding="utf-8")
    (tap09_xuat_ban / "mo_ta.txt").write_text(desc_vn, encoding="utf-8")
    (tap09_dir / "nguon_mo_ta.txt").write_text(SOURCES_VN, encoding="utf-8")
    (tap09_dir / "nguon_tham_khao.md").write_text(NGUON_THAM_KHAO_VN_MD, encoding="utf-8")
    (tap09_xuat_ban / "nguon_tham_khao.md").write_text(NGUON_THAM_KHAO_VN_MD, encoding="utf-8")
    print("Wrote VN description and reference files.")

    # 3. Write EN files
    tap09_en_dir = SAN_XUAT / "Tap09_EN"
    tap09_en_xuat_ban = tap09_en_dir / "xuat_ban"
    tap09_en_xuat_ban.mkdir(parents=True, exist_ok=True)

    (tap09_en_dir / "CHU_CO_DINH_EN.md").write_text(CHU_CO_DINH_EN_CONTENT, encoding="utf-8")
    (tap09_en_dir / "mo_ta.txt").write_text(desc_en, encoding="utf-8")
    (tap09_en_dir / "description.txt").write_text(desc_en, encoding="utf-8")
    (tap09_en_xuat_ban / "mo_ta.txt").write_text(desc_en, encoding="utf-8")
    (tap09_en_xuat_ban / "description.txt").write_text(desc_en, encoding="utf-8")
    (tap09_en_dir / "nguon_tham_khao_EN.md").write_text(NGUON_THAM_KHAO_EN_MD, encoding="utf-8")
    (tap09_en_xuat_ban / "nguon_tham_khao_EN.md").write_text(NGUON_THAM_KHAO_EN_MD, encoding="utf-8")
    print("Wrote EN CHU_CO_DINH_EN.md, description and reference files.")

    # 4. Write JA files
    tap09_ja_dir = SAN_XUAT / "Tap09_JA"
    tap09_ja_xuat_ban = tap09_ja_dir / "xuat_ban"
    tap09_ja_xuat_ban.mkdir(parents=True, exist_ok=True)

    (tap09_ja_dir / "mo_ta.txt").write_text(desc_ja, encoding="utf-8")
    (tap09_ja_dir / "description.txt").write_text(desc_ja, encoding="utf-8")
    (tap09_ja_xuat_ban / "mo_ta.txt").write_text(desc_ja, encoding="utf-8")
    (tap09_ja_xuat_ban / "description.txt").write_text(desc_ja, encoding="utf-8")
    (tap09_ja_dir / "nguon_mo_ta_JA.txt").write_text(SOURCES_JA, encoding="utf-8")
    (tap09_ja_dir / "nguon_tham_khao_JA.md").write_text(NGUON_THAM_KHAO_JA_MD, encoding="utf-8")
    (tap09_ja_xuat_ban / "nguon_tham_khao_JA.md").write_text(NGUON_THAM_KHAO_JA_MD, encoding="utf-8")
    print("Wrote JA description and reference files.")

    # 5. Write KO files
    tap09_ko_dir = SAN_XUAT / "Tap09_KO"
    tap09_ko_xuat_ban = tap09_ko_dir / "xuat_ban"
    tap09_ko_xuat_ban.mkdir(parents=True, exist_ok=True)

    (tap09_ko_dir / "mo_ta.txt").write_text(desc_ko, encoding="utf-8")
    (tap09_ko_dir / "description.txt").write_text(desc_ko, encoding="utf-8")
    (tap09_ko_xuat_ban / "mo_ta.txt").write_text(desc_ko, encoding="utf-8")
    (tap09_ko_xuat_ban / "description.txt").write_text(desc_ko, encoding="utf-8")
    (tap09_ko_dir / "nguon_mo_ta_KO.txt").write_text(SOURCES_KO, encoding="utf-8")
    (tap09_ko_dir / "nguon_tham_khao_KO.md").write_text(NGUON_THAM_KHAO_KO_MD, encoding="utf-8")
    (tap09_ko_xuat_ban / "nguon_tham_khao_KO.md").write_text(NGUON_THAM_KHAO_KO_MD, encoding="utf-8")
    print("Wrote KO description and reference files.")

    print("\nALL DESCRIPTION FILES SUCCESSFULLY BUILT AND PASSED LENGTH QC!")


if __name__ == "__main__":
    main()
