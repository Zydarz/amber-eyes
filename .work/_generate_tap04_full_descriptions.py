#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh toàn bộ phần mô tả chi tiết đạt chuẩn 10 chỉ dấu cho Tập 04 trên 4 ngôn ngữ (VI, EN, JA, KO).
Đảm bảo 100% dung lượng dưới trần 5.000 ký tự của YouTube cho tất cả các bản.
Tuân thủ Luật L2, L3, L5, K1-K10 của Amber Eyes.
"""
from pathlib import Path
import re
import sys

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG ANH (EN) — < 5,000 KÝ TỰ
# ==============================================================================
MO_TA_EN = """Ep. 04: The Angel of Death & The God Complex | Criminal Psychology: Charles Cullen (10 Markers & Institutional Silence) | Amber eyes

In October 2003, ICU nurse Charles Edmund Cullen seemed like a model employee—quiet, dedicated, and always rushing to cardiac crises. Behind his scrubs lurked the deadliest serial killer in US healthcare history. Over 16 years across nine hospitals in NJ and PA, Cullen weaponized lethal doses of Digoxin, Insulin, and Vecuronium, ending up to 400 lives. His double life collapsed when ICU colleague Amy Loughren bravely wore a hidden wire for Somerset detectives to break his wall of silence.

Amber eyes dissects the case through our 10-Indicator Behavioral & Psychological Ecosystem:
1. SOCIAL IMPACT & INSTITUTIONAL BETRAYAL: Public trust shattered as 16 years of hospital silence turned ICUs into covert death traps.
2. OBJECTIFICATION: Reducing vulnerable patients to biological props to satisfy an omnipotent delusion over life and death.
3. COMPARTMENTALIZATION: Insulating his daytime role as a gentle father from his nocturnal reality as an ICU serial poisoner.
4. NARCISSISTIC COLLAPSE: Confronted by digital logs and his closest friend, his savior facade dissolved into self-pity, accepting 397 years without parole.
5. TECHNIQUES OF NEUTRALIZATION: Rationalizing murder as mercy ('I wanted to end their suffering') to mask covert sadistic omnipotence.
6. PSYCHOLOGICAL TRIGGER: Childhood isolation and hospital mishandling of his mother's death bred unconscious hostility and a craving for absolute control.
7. SIGNATURE VS. MO: MO adapted via Pyxis dispensing loopholes; Signature remained covertly poisoning IV bags to savor Code Blue chaos from afar.
8. ESCALATION TRAJECTORY: Dopamine desensitization escalated minor thefts into serial lethal overdoses spanning 9 hospitals over 16 years.
9. HALO EFFECT: A quiet work ethic masked danger, while corporate liability fears prompted silent dismissals rather than police alerts.
10. SURVIVAL RED FLAGS: 4 key warnings: shift-specific cardiac spikes, unexplained high-risk drug overrides, code fascination, and institutional cover-ups.

⏱ CHAPTERS
00:00 Intro & Advisory
00:23 Act 1 · The Paradox of the Model Nurse
05:15 Act 2 · The Crime Scene – Escalation Trajectory of the Abyss
10:45 Act 3 · Psychological Autopsy – Inside the God Complex
16:15 Act 4 · Interrogation & The Breakthrough
21:30 Act 5 · The Verdict, Survival Red Flags & Epilogue

⚠️ LEGAL & SAFETY DISCLAIMER
• Produced strictly for educational and criminological analysis; not medical or legal advice.
• Based on public US judicial records (NJ Superior Court, Somerset Police, state health archives). No intent to defame or glorify any individual.
• Avatars and dialogue are dramatized illustrations. Synthetic AI voices and visuals utilized.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 SOURCES
Verified against public US judicial archives & investigative records:
• State v. Cullen Sentencing (397 Years) — https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html
• The Cullen Act (NJ P.L.2005 c.83) — https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf
• Somerset Prosecutor Interrogation & Wire — https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287
• CBS 60 Minutes: 'Angel of Death' Interview — https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/
• Charles Graeber: The Good Nurse (Dossier) — https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse
• WIRED: Inside the Hospital Pyxis Hack — https://www.wired.com/2013/04/charles-cullen-hospital-hack/
• Sykes & Matza: Techniques of Neutralization — https://www.jstor.org/stable/2089195
• Complete 23-source fact-checking archive: See nguon_tham_khao_EN.md

🆘 CRISIS & SUPPORT HOTLINES (24/7, FREE & CONFIDENTIAL)
• Patient Safety Action Network (PSAN): https://patientsafetyaction.org
• National Whistleblower Center: https://www.whistleblowers.org
• Suicide & Crisis Lifeline: 988 — https://988lifeline.org
• National Domestic Violence Hotline: 1-800-799-SAFE — https://www.thehotline.org
• Childhelp National Child Abuse Hotline: 1-800-422-4453 — https://www.childhelp.org

#TrueCrime #CriminalPsychology #CharlesCullen #TheGoodNurse #ForensicPsychology #AngelOfDeath #GodComplex #InstitutionalSilence #AmberEyes #Documentary"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG VIỆT (VI) — < 5,000 KÝ TỰ
# ==============================================================================
MO_TA_VI = """Tập 04: Thiên Thần Tử Thần & Phức Cảm Chúa Trời | Tâm lý học tội phạm: Charles Cullen (10 Chỉ Dấu Tâm Lý & Sự Im Lặng Thể Chế) | Amber eyes

Mùa thu năm 2003, tại ICU Bệnh viện Somerset (New Jersey), y tá Charles Edmund Cullen (43 tuổi) luôn được xem là nhân viên mẫu mực: trầm tính, tận tụy, luôn nhận ca trực đêm và sốt sắng hỗ trợ cấp cứu ngưng tim. Nhưng sau áo blouse trắng là kẻ giết người nguy hiểm nhất lịch sử y tế Mỹ. Suốt 16 năm qua 9 bệnh viện, Cullen đã dùng Digoxin, Insulin, Vecuronium tước đoạt sinh mạng của 29 nạn nhân đã xác nhận và ước tính tới 400 bệnh nhân. Vụ án chỉ khép lại nhờ nữ đồng nghiệp Amy Loughren dũng cảm đeo máy ghi âm phối hợp cùng cảnh sát phá vỡ bức tường im lặng.

Hồ sơ Charles Cullen được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi:
1. DƯ CHẤN XÃ HỘI & NỖI HOANG MANG TẬP THỂ: Bệnh viện biến thành bẫy chết người; niềm tin ngành y sụp đổ trước 16 năm im lặng của 9 cơ sở y tế.
2. VẬT HÓA NẠN NHÂN: Tước đoạt nhân tính bệnh nhân, biến họ thành công cụ sinh học để thỏa mãn ảo tưởng quyền lực tối thượng.
3. CƠ CHẾ CHIA NGĂN: Cô lập nhân cách người cha hiền lành và đồng nghiệp mến khách khỏi bản năng tra độc vào túi dịch truyền ca đêm.
4. BẢN NGÃ ÁI KỶ SỤP ĐỔ: Đối diện dữ liệu Pyxis và người bạn thân, chiếc mặt nạ cứu rỗi rơi xuống; hắn tự thương hại, lãnh 397 năm tù không ân xá.
5. HỆ THỐNG TỰ BÀO CHỮA: Ngụy biện 'chấm dứt nỗi đau' để chối bỏ sự tổn hại, biến hành vi sát hại thành sứ mệnh giải thoát cao quý.
6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Tuổi thơ cô lập, mẹ mất mà viện hỏa táng không báo kịp gieo mầm hận thù y tế; sự bất lực đời tư kích hoạt xung lực nắm giữ sinh tử.
7. SIGNATURE VS. THỦ ĐOẠN MO: MO thích ứng qua kẽ hở lệnh Cancel máy Pyxis; Signature bất biến: tra độc vào túi dịch truyền để quan sát hỗn loạn Code Blue từ xa.
8. QUỸ ĐẠO LEO THANG: Sự trơ lỳ cảm xúc đẩy ngưỡng kích thích từ trộm thuốc nhỏ đến sát hại hàng loạt, từ bệnh nhân nặng đến người sắp hồi phục.
9. HIỆU ỨNG HÀO QUANG: Vỏ bọc cần mẫn ca đêm kết hợp nỗi sợ kiện tụng khiến các bệnh viện chọn sa thải êm thấm thay vì báo cảnh sát.
10. CẢNH BÁO ĐỎ SINH TỒN: 4 tín hiệu: số ca tử vong tăng theo ca trực, hủy lệnh thuốc liều cao bất thường, thái độ sốt sắng quanh ca cấp cứu, và văn hóa bưng bít.

⏱ MỐC CHƯƠNG
00:00 Intro & Khuyến cáo
00:23 Hồi 1 · Nghịch lý của người y tá mẫu mực
05:15 Hồi 2 · Hiện trường & Hồ sơ tội ác – Quỹ đạo leo thang của vực thẳm
10:45 Hồi 3 · Giải phẫu tâm lý – Bên trong bộ não của kẻ mang Phức cảm Chúa trời
16:15 Hồi 4 · Đấu trí thẩm vấn & Bước ngoặt điều tra
21:30 Hồi 5 · Phán quyết, Bài học cảnh báo đỏ & Lời kết

⚠️ LƯU Ý PHÁP LÝ & AN TOÀN
• Video mang tính giáo dục, tư liệu lịch sử và phân tích tâm lý tội phạm học; không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Dựa trên hồ sơ tư pháp công khai tại Hoa Kỳ (Tòa Thượng thẩm NJ, Cảnh sát Somerset, báo cáo y tế). Kênh không bôi nhọ hay tôn vinh cá nhân nào.
• Nhân vật Cú, Sói, Cáo, Cừu, Mèo là hình tượng minh họa. Giọng đọc, hình ảnh và âm thanh hỗ trợ bởi công nghệ AI.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 NGUỒN THAM KHẢO
Đối chiếu hồ sơ công khai và tư liệu tư pháp Hoa Kỳ:
• Tòa Thượng thẩm New Jersey: Bản án State v. Cullen (397 năm tù) — https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html
• Cục Quản lý Người tiêu dùng NJ: Đạo luật Cullen (P.L.2005 c.83) — https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf
• Sở Cảnh sát Somerset: Hồ sơ thẩm vấn & Gài máy ghi âm — https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287
• CBS News 60 Minutes: Phỏng vấn Charles Cullen — https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/
• Charles Graeber: The Good Nurse (Tư liệu điều tra) — https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse
• WIRED: Kẽ hở bảo mật máy phát thuốc tự động Pyxis — https://www.wired.com/2013/04/charles-cullen-hospital-hack/
• Sykes & Matza (1957): Kỹ thuật trung hòa đạo đức — https://www.jstor.org/stable/2089195
• Toàn bộ 23 nguồn công khai đối chiếu từng câu: Xem hồ sơ nguon_tham_khao.md

🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia
bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).
• Đường dây nóng hỗ trợ bệnh nhân & phản ánh sai phạm y tế (Bộ Y tế): 1900 9095
• Patient Safety Action Network: https://patientsafetyaction.org
• National Whistleblower Center: https://www.whistleblowers.org

#AmberEyes #TrueCrime #CharlesCullen #TheGoodNurse #TamLyToiPham #PhucCamChuaTroi #10ChiDauTamLy #CanhBaoDo #YTeHoaKy #GiaiPhauTamLy"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG NHẬT (JA) — < 5,000 KÝ TỰ
# ==============================================================================
MO_TA_JA = """第04話 · 死の天使と神コンプレックス | 犯罪心理学：チャールズ・カレン事件 (10の心理指標と制度的沈黙) | Amber eyes

2003年秋、米ニュージャージー州サマセット医療センターのICU。43歳の看護師チャールズ・エドマンド・カレンは、過酷な夜勤を率先して引き受け、急変時に駆けつける模範的職員と見なされていました。しかしその白衣の裏に隠されていたのは、米国医療史上最悪の連続殺人犯でした。16年間で9つの病院を渡り歩き、ジゴキシンやインスリン等の薬剤を悪用して推定最大400名もの患者の命を奪いました。同僚看護師エイミー・ローレンが盗聴器を身につけて警察に協力し、カレンの心理的防壁を突き崩したことで事件は終結しました。

アンバーアイズは本事件を「10の核心的心理・行動指標エコシステム」を通じて解剖します：
1. 社会的余波と集団的不安: 命を預けるべき病院が見えない死の罠と化し、9つの病院の16年におよぶ沈黙が医療への信頼を根底から覆しました。
2. 被害者の客体化: 生死を司る全能感を満たすため、生身の患者を自らの歪んだ欲求を満たす「生体ツール」へと還元しました。
3. 心理的区画化: 穏やかな父親・献身的な同僚という昼の顔と、夜のICUで毒物を混入させる捕食者という二重生活を矛盾なく維持しました。
4. 自己愛の崩壊: 動かぬ電算記録と親友を前に救済者の仮面は崩壊し、自己憐憫へ逃避。真の悔悟なきまま397年の終身刑を受け入れました。
5. 自己正当化と中和の技術: 「苦痛を終わらせてあげたかった」という偽りの慈悲を掲げ、冷酷な毒殺を高潔な救済任務へとすり替えました。
6. 心理的引き金: 孤独な幼少期、病院側の不手際で母の死と火葬を事後報告されたトラウマが医療機関への無意識の怨恨と支配欲の引き金となりました。
7. 署名対手口: ピクシス投薬機のキャンセル機能を悪用した手口に対し、不変の署名は輸液バッグへの毒物混入と急変パニックの遠隔支配でした。
8. 4段階のエスカレーション: 刺激に対する耐性形成により、薬品の不正持ち出しから重篤患者、さらに回復期患者へと標的を無差別に拡大しました。
9. 後光効果と制度的盲点: 模範的看護師という後光と訴訟を恐れる病院経営陣の隠蔽体質が結託し、警察通報ではなく推薦状付き解雇を繰り返しました。
10. 生存のレッドフラッグ: 4つの警報：特定職員シフト時の心停止急増、投薬機の不自然な取消履歴、コード・ブルーへの執着、組織的隠蔽文化。

⏱ 目次（チャプター）
00:00 オープニング＆視聴にあたって
00:23 第1幕 · 模範的看護師のパラドックス
05:15 第2幕 · 犯行現場――深淵のエスカレーション軌道
10:45 第3幕 · 心理解剖――神コンプレックスの脳内
16:15 第4幕 · 取調の攻防――捜査の重大な転換点
21:30 第5幕 · 判決、生存への警告と結び

⚠️ ご視聴にあたっての注意事項
• 本動画は教育および犯罪心理学の観点からの分析コンテンツであり、医学的・法的なアドバイスではありません。
• 米国の公開司法記録（ニュージャージー州高裁、サマセット警察捜査資料等）に基づきます。特定個人の誹謗中傷や美化の意図はありません。
• 登場するキャラクターは演出用の架空キャラクターです。音声・画像はAIツールを活用しています。
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 参考資料・出典
米国司法・公的記録との照合済み：
• ニュージャージー州高等裁判所：判決記録（終身刑397年） — https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html
• NJ消費者局：カレン法（P.L.2005 c.83） — https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf
• サマセット警察：捜査記録・潜入録音 — https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287
• CBS 60 Minutes：チャールズ・カレン単独インタビュー — https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/
• Charles Graeber：『The Good Nurse』調査記録 — https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse
• WIRED：ピクシス投薬システムの脆弱性 — https://www.wired.com/2013/04/charles-cullen-hospital-hack/
• Sykes & Matza (1957)：犯罪社会学における中和の技術 — https://www.jstor.org/stable/2089195
• 23件の全出典リスト：制作アーカイブ nguon_tham_khao_JA.md 参照

🆘 相談窓口・支援ホットライン
• 日本医療安全調査機構（医療事故相談）：https://www.medsafe.or.jp/
• 警察相談専用電話：#9110（全国共通）
• よりそいホットライン：0120-279-338
• こころの健康相談統一ダイヤル：0570-064-556
• 児童相談所虐待対応ダイヤル：189

#犯罪心理学 #TrueCrime #チャールズカレン #グッドナース #死の天使 #神コンプレックス #医療サスペンス #10の心理指標 #レッドフラッグ #AmberEyes"""

# ==============================================================================
# NỘI DUNG MÔ TẢ TIẾNG HÀN (KO) — < 5,000 KÝ TỰ
# ==============================================================================
MO_TA_KO = """04화 · 죽음의 천사와 신 콤플렉스 | 범죄심리학: 찰스 컬런 사건 (10대 심리 지표와 제도의 침묵) | Amber eyes

2003년 가을, 미국 뉴저지주 서머싯 메디컬 센터의 중환자실(ICU). 43세의 간호사 찰스 에드먼드 컬런은 야간 근무를 자원하고 응급 상황마다 솔선수범하는 모범 직원으로 통했습니다. 그러나 그 백의 이면에는 미국 의료 역사상 가장 많은 인명을 앗아간 연쇄 살인마가 숨어 있었습니다. 16년 동안 9개 병원을 거치며 디곡신, 인슐린, 베쿠로늄 등을 악용해 최대 400명의 무고한 환자를 살해했습니다. 동료 간호사 에이미 로렌이 신변 위협을 무릅쓰고 도청 장치를 착용해 수사관들과 공조함으로써 16년간의 침묵이 깨졌습니다.

Amber eyes는 본 사건을 '10대 핵심 심리·행동 지표 생태계'를 통해 심층 해부합니다:
1. 사회적 파장과 집단적 공포: 가장 안전해야 할 병원이 죽음의 덫으로 전락하며 9개 병원이 16년간 지켜온 침묵의 카르텔이 신뢰를 무너뜨렸습니다.
2. 피해자의 사물화: 환자의 존엄성을 박탈하고 생사를 가르는 전능감을 시험·충족하기 위한 '생체 도구'로 축소했습니다.
3. 심리적 구획화: 온화한 아버지이자 따뜻한 동료라는 낮의 모습과, 수액 백에 독물을 주입하는 포식자라는 밤의 모습을 철저히 분리했습니다.
4. 나르시시즘적 붕괴: 전산 기록과 동료의 설득 앞에 구원자 가면이 벗겨지자 자기연민으로 도피, 참회 없이 397년 징역을 받아들였습니다.
5. 자기 정당화 및 중화 기술: '고통을 끝내주고 싶었다'는 위선적 자비심으로 가해 행위를 부정하고 숭고한 안식 제공으로 포장했습니다.
6. 심리적 트리거: 불우한 유년기, 모친 시신 화장의 일방적 통보로 인한 트라우마가 의료 기관을 향한 무의식적 원한과 통제욕의 뇌관이 되었습니다.
7. 시그니처 vs 범행 수법: 자동 투약기 취소 기능을 악용한 수법(MO)과 달리, 불변의 시그니처는 수액 백 독물 주입 후 응급 코드 패닉을 원거리 관망하는 것이었습니다.
8. 4단계 에스컬레이션: 자극 역치 붕괴로 단순 절도에서 중환자, 나아가 회복기 환자까지 무차별 표적으로 삼으며 9개 병원을 질주했습니다.
9. 후광 효과와 제도의 맹점: 성실한 야간 간호사라는 후광과 소송을 두려워한 병원들의 소극적 은폐가 결합해 권고사직과 추천서를 남발했습니다.
10. 생존을 위한 레드플래그: 4대 경고 신호: 특정 근무조의 비정상적 심정지 급증, 불필요한 약물 검색·취소, 응급 현장에 대한 집착, 조직적 침묵 문화.

⏱ 챕터(타임라인)
00:00 오프닝 & 시청 안내
00:23 제1막 · 모범 간호사의 역설
05:15 제2막 · 범죄 현장 – 심연의 에스컬레이션 궤적
10:45 제3막 · 심리 부검 – 신 콤플렉스의 뇌 속으로
16:15 제4막 · 심문실의 공방 – 수사의 결정적 돌파구
21:30 제5막 · 판결, 생존을 위한 경고와 맺음말

⚠️ 시청 전 법적 유의사항
• 본 콘텐츠는 교육 및 범죄심리학적 분석 다큐멘터리이며 전문적 의학·법률 조언을 대신하지 않습니다.
• 미국 공식 사법 기록(뉴저지주 고등법원 판결문, 서머싯 경찰서 수사 기록 등)을 바탕으로 제작되었습니다.
• 등장 캐릭터는 시각적 연출을 위한 가상 캐릭터이며, 음성과 이미지는 AI 기술을 활용하였습니다.
This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

📚 공식 참고자료 및 공판 기록
미국 공식 사법 기록 및 탐사 보도와의 교차 검증:
• 뉴저지주 고등법원: State v. Cullen 판결문 (397년 징역) — https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html
• NJ 소비자보호국: 컬런 법 (P.L.2005 c.83) — https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf
• 서머싯 경찰서: 수사 기록 및 도청 작전 — https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287
• CBS 60 Minutes: 찰스 컬런 첫 단독 인터뷰 — https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/
• Charles Graeber: 《그 남자, 좋은 간호사》 심층 탐사 — https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse
• WIRED: 픽시스(Pyxis) 약물 자동발급기 취약점 수법 — https://www.wired.com/2013/04/charles-cullen-hospital-hack/
• Sykes & Matza (1957): 범죄사회학 중화 기술 논문 — https://www.jstor.org/stable/2089195
• 23개 전 출처 교차 검증 목록: 제작 아카이브 nguon_tham_khao_KO.md 참조

🆘 위기 상담 및 피해자 지원 핫라인 (무료 & 비밀보장)
• 환자안전보고학습시스템 (KOPS): https://www.kops.or.kr
• 국민권익위원회 공익신고: 국번없이 1398
• 보건복지상담센터: 국번없이 129
• 경찰청 범죄신고: 국번없이 112
• 아동학대 예방 및 신고 상담전화: 국번없이 112 또는 129

#AmberEyes #범죄심리학 #TrueCrime #찰스컬런 #그남자좋은간호사 #죽음의천사 #신콤플렉스 #10대심리지표 #레드플래그 #사건기록 #다큐멘터리"""

def write_files():
    # 1. TIẾNG VIỆT
    vi_dir = ROOT / "02_SAN_XUAT" / "Tap04"
    vi_xb = vi_dir / "xuat_ban"
    vi_xb.mkdir(parents=True, exist_ok=True)
    
    (vi_dir / "mo_ta.txt").write_text(MO_TA_VI, encoding="utf-8")
    (vi_xb / "mo_ta.txt").write_text(MO_TA_VI, encoding="utf-8")
    print(f"VI mo_ta.txt written, len: {len(MO_TA_VI)} chars")

    # 2. TIẾNG ANH
    en_dir = ROOT / "02_SAN_XUAT" / "Tap04_EN"
    en_xb = en_dir / "xuat_ban"
    en_xb.mkdir(parents=True, exist_ok=True)
    
    (en_dir / "description.txt").write_text(MO_TA_EN, encoding="utf-8")
    (en_dir / "mo_ta.txt").write_text(MO_TA_EN, encoding="utf-8")
    (en_xb / "description.txt").write_text(MO_TA_EN, encoding="utf-8")
    (en_xb / "mo_ta.txt").write_text(MO_TA_EN, encoding="utf-8")
    print(f"EN description.txt written, len: {len(MO_TA_EN)} chars")

    # Cập nhật khối description trong CHU_CO_DINH_EN.md
    chu_co_dinh = en_dir / "CHU_CO_DINH_EN.md"
    if chu_co_dinh.exists():
        c_text = chu_co_dinh.read_text(encoding="utf-8")
        new_block = "```text\n" + MO_TA_EN.strip() + "\n```"
        c_text_new = re.sub(r'```text\nEp\. 04:.*?\n```', new_block, c_text, flags=re.S)
        if c_text_new != c_text:
            chu_co_dinh.write_text(c_text_new, encoding="utf-8")
            print("Updated CHU_CO_DINH_EN.md Section 4 description block")
        else:
            print("Note: Could not regex match Section 4 in CHU_CO_DINH_EN.md, inspecting manually.")

    # 3. TIẾNG NHẬT
    ja_dir = ROOT / "02_SAN_XUAT" / "Tap04_JA"
    ja_xb = ja_dir / "xuat_ban"
    ja_xb.mkdir(parents=True, exist_ok=True)
    
    (ja_dir / "description.txt").write_text(MO_TA_JA, encoding="utf-8")
    (ja_dir / "mo_ta.txt").write_text(MO_TA_JA, encoding="utf-8")
    (ja_xb / "description.txt").write_text(MO_TA_JA, encoding="utf-8")
    (ja_xb / "mo_ta.txt").write_text(MO_TA_JA, encoding="utf-8")
    print(f"JA description.txt written, len: {len(MO_TA_JA)} chars")

    # 4. TIẾNG HÀN
    ko_dir = ROOT / "02_SAN_XUAT" / "Tap04_KO"
    ko_xb = ko_dir / "xuat_ban"
    ko_xb.mkdir(parents=True, exist_ok=True)
    
    (ko_dir / "description.txt").write_text(MO_TA_KO, encoding="utf-8")
    (ko_dir / "mo_ta.txt").write_text(MO_TA_KO, encoding="utf-8")
    (ko_xb / "description.txt").write_text(MO_TA_KO, encoding="utf-8")
    (ko_xb / "mo_ta.txt").write_text(MO_TA_KO, encoding="utf-8")
    print(f"KO description.txt written, len: {len(MO_TA_KO)} chars")

    # 5. CẬP NHẬT CÁC TỆP NGUON_MO_TA
    def extract_sources(desc_text, start_marker, end_marker):
        parts = desc_text.split(start_marker)
        if len(parts) > 1:
            return parts[1].split(end_marker)[0].strip()
        return ""

    src_en = extract_sources(MO_TA_EN, "📚 SOURCES", "🆘 CRISIS & SUPPORT HOTLINES")
    if src_en:
        (en_dir / "nguon_mo_ta_EN.txt").write_text(src_en, encoding="utf-8")
        print(f"Updated nguon_mo_ta_EN.txt, len: {len(src_en)} chars")

    src_ja = extract_sources(MO_TA_JA, "📚 参考資料・出典", "🆘 相談窓口・支援ホットライン")
    if src_ja:
        (ja_dir / "nguon_mo_ta_JA.txt").write_text(src_ja, encoding="utf-8")
        print(f"Updated nguon_mo_ta_JA.txt, len: {len(src_ja)} chars")

    src_ko = extract_sources(MO_TA_KO, "📚 공식 참고자료 및 공판 기록", "🆘 위기 상담 및 피해자 지원 핫라인")
    if src_ko:
        (ko_dir / "nguon_mo_ta_KO.txt").write_text(src_ko, encoding="utf-8")
        print(f"Updated nguon_mo_ta_KO.txt, len: {len(src_ko)} chars")

if __name__ == "__main__":
    write_files()
