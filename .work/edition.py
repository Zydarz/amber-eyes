# -*- coding: utf-8 -*-
"""Language edition + episode switch shared by the pipeline scripts.

    AE_LANG=en py -3 .work/<script>.py     -> English edition (Tap01_EN)
    AE_LANG=ko py -3 .work/<script>.py     -> Korean edition  (Tap01_KO)
    AE_EP=02 py -3 .work/<script>.py       -> Tập 02 (bản tiếng Việt)
    py -3 .work/<script>.py                -> Tập 01 tiếng Việt, đường dẫn như cũ

Every English output carries an _EN suffix or lives under 02_SAN_XUAT/Tap01_EN, every Korean
output carries a _KO suffix or lives under 02_SAN_XUAT/Tap01_KO, and every Tập 02 intermediate
file carries a _t02 suffix, so no edition or episode overwrites another.
"""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent   # gốc dự án = thư mục cha của .work (tự dòng, không cứng đường dẫn)
WORK = ROOT / ".work"
LANG = os.environ.get("AE_LANG", "vi").strip().lower()
EN = LANG == "en"
KO = LANG == "ko"
JA = LANG == "ja"
EPN = os.environ.get("AE_EP", "01").strip().zfill(2)
if (EN or KO or JA) and not (EPN.isdigit() and 1 <= int(EPN) <= 29):
    raise SystemExit("Bản tiếng Anh/Hàn/Nhật hỗ trợ từ Tập 01 đến Tập 29 (AE_EP=01..29).")
SUF = ("_EN" if EN else ("_KO" if KO else ("_JA" if JA else ""))) + ("" if EPN == "01" else f"_t{EPN}")


def w(name):
    """.work data file or folder for this edition/episode: 'timeline_s.json' -> 'timeline_s_t02.json'."""
    p = Path(name)
    return WORK / (p.stem + SUF + p.suffix)


# ---------------------------------------------------------------- per-episode settings
# Mọi chỗ trước đây viết cứng cho Tập 01 trong các script (A12) nằm ở đây.
EPISODES = {
    "01": {
        "script": WORK / ("script_tap01_new_en.json" if EN else "script_tap01_new_vn.json"),
        "script_ja": WORK / "script_tap01_new_ja.json",
        "script_ko": WORK / "script_tap01_new_ko.json",
        "dir": "Tap01_EN" if EN else "Tap01",
        "plan": "KeHoach_Video_Tap01_EN.md" if EN else "KeHoach_Video_Tap01.md",
        "master": "Tap01_EN_master" if EN else "Tap01_master",
        "srt": "Tap01_EN.srt" if EN else "Tap01.srt",
        "intro": "intro_kenh_EN.mov" if EN else "intro_kenh.mov",
        "tts_fix": {"1.03#1": "June fourteenth, twenty fifteen."},
        "n_element": {"1.07": "N1", "4.03": "N2"},
        "acting": w("acting.json") if EN else None,        # acting_EN.json
        "sfx_sheet": None,
        # build_audio3: nhạc Hồi 1 vào ở mốc · "im lặng tuyệt đối" · tiếng "Tách"
        "act1_cue": "1.12", "silence_cue": "1.09", "click_cues": ("1.06", "1.12"),
        "bed": {1: "bgm_cello_sad.mp3", 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: "bgm_ambient_deep.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [
            ("police_siren_distant.wav", "1.02", -2.80, -3), ("door_knock.wav", "1.02", -0.90, -2),
            ("radio_chatter.wav", "1.10", -3.00, -6), ("heart_beep.wav", "2.01", -5.03, -18),
            ("paper_rustle.wav", "2.03", -1.00, -8), ("lock_door.wav", "2.08", -1.10, -2),
            ("heartbeat_slow.wav", "4.01", -4.97, -18), ("chains.wav", "4.06", -2.50, -5),
            ("keyboard_night.wav", "4.14", -2.20, -12), ("gavel.wav", "5.01", -1.10, 1),
            ("folder_close.wav", "5.13", -0.47, -8)],
        "mux_af": "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1",
        # parse_shots: cảnh ghép sẵn, đổi nền trong shot, ảnh ghim
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "text_scrim": [
      "1-02",
      "1-18",
      "1-19",
      "1-25",
      "1-27",
      "1-36",
      "1-40",
      "2-01",
      "2-02",
      "2-06",
      "2-07",
      "2-12",
      "2-18",
      "2-24",
      "2-25",
      "2-27",
      "2-28",
      "2-29",
      "2-30",
      "2-32",
      "2-36",
      "2-38",
      "3-04",
      "3-05",
      "3-06",
      "3-07",
      "3-09",
      "3-11",
      "3-20",
      "3-21",
      "3-26",
      "3-33",
      "3-35",
      "4-08",
      "4-10",
      "4-11",
      "4-13",
      "4-14",
      "4-15",
      "4-19",
      "4-22",
      "4-23",
      "4-25",
      "4-29",
      "4-34",
      "4-37",
      "5-01",
      "5-03",
      "5-04",
      "5-08",
      "5-18",
      "5-19",
      "5-20",
      "5-23",
      "5-25",
      "5-29",
      "5-31",
        ],
        "route_pins": {"1-29": ("SPRINGFIELD, MISSOURI", "WISCONSIN")},   # T7: nhãn 2 ghim
        # package
        "thumb": ("POISON IN THE NAME", "OF A MOTHER’S LOVE") if EN else ("母の愛という名の", "毒薬") if JA else ("엄마의 사랑이라는", "이름의 독약") if KO else ("ĐỘC DƯỢC", "NHÂN DANH TÌNH MẸ"),
        "title": ("Ep. 01: Poison in the Name of Mother’s Love | Criminal Psychology: Gypsy Rose & Dee Dee Blanchard (FDIA & 10 Behavioral Markers)" if EN else
                  "第01話 · 母の愛という名の毒薬 | 犯罪心理学：ジプシー・ローズ＆ディー・ディー・ブランチャード（代理型ミュンハウゼン症候群＆10の心理指標）" if JA else
                  "01화 · 모성이라는 이름의 독약 | 범죄심리학: 집시 로즈 & 디디 블랜차드 (대리인에 의한 뮌하우젠 증후군 & 10가지 심리 지표)" if KO else
                  "Tập 01: Độc Dược Nhân Danh Tình Mẹ | Tâm lý học tội phạm: Gypsy Rose Blanchard (FDIA & 10 Chỉ Dấu Tâm Lý)"),
        "act_titles": ({1: "Act 1 · The Moment Trust Broke & Social Blind Spots", 2: "Act 2 · Crime Scene & The Escalating Medical Abyss",
                        3: "Act 3 · Psychological Autopsy — Inside the Mind of FDIA", 4: "Act 4 · The Victim's Perspective — Why Couldn't Gypsy Just Stand Up?",
                        5: "Act 5 · Forensic Verdict, Psychological Judgment & Survival Red Flags"} if EN else
                       {1: "第1幕 · 信頼が崩れる瞬間＆社会の盲点", 2: "第2幕 · 犯罪現場＆医療の深淵へのエスカレーション",
                        3: "第3幕 · 心理剖検――FDIA犯罪者の脳の内部", 4: "第4幕 · 被害者の視点――ジプシーはなぜ立ち上がれなかったのか？",
                        5: "第5幕 · 法医学的判定、心理の審判＆生存のための赤い警告"} if JA else
                       {1: "제1막 · 무너진 신뢰의 순간 & 사회적 맹점", 2: "제2막 · 범죄 현장 & 의료 심연으로의 에스컬레이션",
                        3: "제3막 · 심리 부검――FDIA 범죄자의 뇌 속으로", 4: "제4막 · 피해자의 시선――집시는 왜 일어서지 못했는가?",
                        5: "제5막 · 법의학적 판결, 심리적 심판 & 생존을 위한 위험 신호"} if KO else
                       {1: "Hồi 1 · Khoảnh khắc đứt gãy niềm tin & Điểm mù xã hội", 2: "Hồi 2 · Hiện trường & Quỹ đạo leo thang của vực thẳm y tế",
                        3: "Hồi 3 · Giải phẫu tâm lý — Bên trong bộ não kẻ mắc FDIA", 4: "Hồi 4 · Góc nhìn nạn nhân — Tại sao Gypsy không đứng dậy?",
                        5: "Hồi 5 · Phán quyết pháp y, bản án tâm lý & Cảnh báo đỏ sinh tồn"}),
        # Hashtag dòng cuối mô tả YouTube (bản tiếng Việt). Bản EN có sẵn trong
        # CHU_CO_DINH_EN.md; bản JA/KO chưa có dòng hashtag.
        "hashtags": "#TrueCrime #CriminalPsychology #MunchausenSyndrome #GypsyRoseBlanchard #FDIA #ForensicPsychology #Documentary #AmberEyes #TamLyToiPham #PhamVan #HoiTo",
        "summary": ("1.13#3", "3.02#6"),
        "need": ["1.03#1", "2.04#3", "2.04#15", "2.07#4", "3.04#11", "4.07#1",
                 "4.10#1", "5.04#1", "5.05#7"],
        "case": "Blanchard", "n1": (("SPRINGFIELD RESIDENT", "Longtime neighbor", "SPRINGFIELD RESIDENT") if EN else
                                    ("スプリングフィールド住民", "長年の隣人", "証人") if JA else
                                    ("스프링필드 주민", "오랜 이웃", "증인") if KO else
                                    ("NGƯỜI DÂN SPRINGFIELD", "Hàng xóm nhiều năm", "NGƯỜI DÂN")),
        "n2": (("VIEWER", "Following the case", "VIEWER") if EN else
               ("視聴者", "事件を見守る人", "視聴者") if JA else
               ("시청자", "사건을 지켜본 사람", "시청자") if KO else
               ("KHÁN GIẢ", "Theo dõi vụ án", "KHÁN GIẢ")),
        "cast": None if (EN or JA or KO) else {"H": ("audiobook_male_1", 0.90), "D": ("male-qn-qingse", 0.95), "C": ("audiobook_female_1", 0.92)},   # giữ giọng Tập 01 đã xuất
        "cast_ko": True,
    },
    "02": {
        "script": WORK / ("script_tap02_EN.json" if EN else "script_tap02.json"),
        "dir": "Tap02_EN" if EN else "Tap02",
        "plan": "KeHoach_Video_Tap02_EN.md" if EN else "KeHoach_Video_Tap02.md",
        "master": "Tap02_EN_master" if EN else "Tap02_master",
        "srt": "Tap02_EN.srt" if EN else "Tap02.srt",
        "intro": "intro_kenh_EN_t02.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.07": "N1", "4.06": "N2"},
        "acting": WORK / ("acting_tap02_EN.json" if EN else "acting_tap02.json"),
        "sfx_sheet": WORK / "sfx_tap02.json",
        "act1_cue": "1.16", "silence_cue": "1.09", "click_cues": ("1.06",),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: ("bgm_cello_sad_v2.mp3", "bgm_sub_drone.mp3"), 4: "bgm_sub_drone.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],                                        # Tập 02 dùng sfx_sheet
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},                                      # T7 Tập 02: ghim không nhãn (không nêu địa điểm nhà nạn nhân)
        "thumb": ("THE TWO-FACED", "COLONEL") if EN else ("二重生活の", "大佐") if JA else ("ĐẠI TÁ", "HAI MẶT"),
        "thumb_bg": "t2_two_chairs",                           # nền thumbnail (Tập 01 mặc định house_police)
        "title": ("Ep. 02: A Predator Disguised as Honor | Criminal Psychology: Colonel Russell Williams (10 Psychological Markers & 4 Stages of Escalation)" if EN else
                  "第02話 · 二重生活の大佐とエスカレーションの深淵 | ラッセル・ウィリアムズ大佐の犯罪心理学 (10の心理指標と4段階の暴走)" if JA else
                  ("02화 · 두 얼굴의 대령과 심연의 에스컬레이션 | 러셀 윌리엄스 대령의 범죄심리학 (10가지 심리 지표와 4단계의 파멸)" if KO else
                   "Tập 02: Kẻ Săn Mồi Ẩn Sau Quân Hàm Đại Tá | Tâm lý học tội phạm: Russell Williams (10 Chỉ Dấu Tâm Lý & 4 Bậc Thang Vực Thẳm)")),
        "act_titles": ({1: "Act 1 · The Extreme Contrast Behind a Colonel’s Rank",
                        2: "Act 2 · The Scene & Dossier — The 4 Stages of the Abyss",
                        3: "Act 3 · Psychological Autopsy — Compartmentalization & Self-Justification",
                        4: "Act 4 · The Interrogation Room & Ten-Hour Duel — Unmasking the Predator",
                        5: "Act 5 · The Verdict, Psychological Sentence & Red Flag Lessons"} if EN else
                       {1: "第1幕 · 大佐の階級章の裏にある極端な対比",
                        2: "第2幕 · 現場と犯行記録――エスカレーションの深淵",
                        3: "第3幕 · 心理の深層解剖――精神の分断と自己正当化",
                        4: "第4幕 · 尋問室での心理戦――10時間の仮面の崩壊",
                        5: "第5幕 · 判決、心理的結末と生存の警告"} if JA else
                       {1: "제1막 · 대령의 계급장 뒤에 숨겨진 극단적 대비",
                        2: "제2막 · 현장 & 범죄 프로파일 – 심연의 에스컬레이션 궤적",
                        3: "제3막 · 심층 심리 해부 – 심리적 구획화와 자기 합리화",
                        4: "제4막 · 취조실 안의 심리전 – 10시간의 가면의 붕괴",
                        5: "제5막 · 판결, 심리적 종말 & 생존의 경고"} if KO else
                       {1: "Hồi 1 · Sự tương phản cực đại phía sau quân hàm đại tá",
                        2: "Hồi 2 · Hiện trường & Quỹ đạo leo thang của vực thẳm",
                        3: "Hồi 3 · Giải phẫu tâm lý chuyên sâu — Sự chia ngăn & Tự bào chữa",
                        4: "Hồi 4 · Phòng thẩm vấn & Cuộc đấu trí mười tiếng — Sụp đổ mặt nạ",
                        5: "Hồi 5 · Phán quyết, bản án tâm lý & Bài học cảnh báo đỏ sinh tồn"}),
        # 02/11/2026: tên hồi 1 phải có "cực đại" — thẻ trên màn hình ghi
        # "HỒI 01 · SỰ TƯƠNG PHẢN CỰC ĐẠI PHÍA SAU QUÂN HÀM ĐẠI TÁ" (đo trên mp4).
        # Dòng disclaimer vai lời: nhãn phụ đề thực tế của tập 02 là
        # [ĐIỀU TRA VIÊN] · [CHUYÊN GIA TÂM LÝ] · [BINH SĨ] · [KHÁN GIẢ] (không có "Người dân").
        "roles_line": "Lời của Điều tra viên, Chuyên gia tâm lý, Binh sĩ căn cứ Trenton và Khán giả theo dõi vụ án là lời dựng lại dựa trên tư liệu.",
        # Hashtag dòng cuối mô tả YouTube (bản tiếng Việt). Bản EN có sẵn trong
        # CHU_CO_DINH_EN.md; bản JA/KO chưa có dòng hashtag.
        "hashtags": "#AmberEyes #TrueCrime #TamLyToiPham #RussellWilliams #QuyLuatLeoThang #ChiaNganTamTri #ThamVanDinhCao #10ChiDauTamLy #CanhBaoDo #HoSoToiPham",
        "hashtags_en": "#AmberEyes #TrueCrime #CriminalPsychology #RussellWilliams #BehavioralEscalation #Compartmentalization #InterrogationTechniques #ForensicPsychology #RedFlags #Documentary",
        "hashtags_ja": "#AmberEyes #TrueCrime #犯罪心理学 #心理分析 #ラッセルウィリアムズ #エスカレーションの法則 #精神の分断 #取調室の心理戦 #プロファイリング #未解決事件",
        "hashtags_ko": "#AmberEyes #TrueCrime #범죄심리학 #러셀윌리엄스 #프로파일링 #에스컬레이션 #심리적구획화 #10시간의취조 #레드플래그 #실화사건",
        "summary": ("1.18#3", "3.04#1"),
        "summary_vn": 'Tháng 7/2009, Đại tá David Russell Williams nhậm chức chỉ huy trưởng Căn cứ Không quân Trenton – căn cứ chiến lược lớn nhất Canada. Từng lái chuyên cơ cho Nữ hoàng Elizabeth II và Thủ tướng Canada, Williams là biểu tượng mẫu mực của kỷ luật thép và học thức. Nhưng sau quân phục danh dự là một kẻ săn mồi nguy hiểm với đời sống hai mặt bệnh hoạn. Vụ án chỉ khép lại sau cuộc đấu trí 10 tiếng trong phòng thẩm vấn của Trung sĩ OPP Jim Smyth ngày 07/02/2010.\n\nHồ sơ Russell Williams được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:\n1. DƯ CHẤN XÃ HỘI & NỖI HOANG TƯỞNG TẬP THỂ: Sự biến mất của Jessica Lloyd gieo rắc kinh hoàng; phụ nữ chèn ghế sau then cửa, niềm tin vào quân đội sụp đổ.\n2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Coi nạn nhân là "vật phẩm" trong bộ sưu tập; lưu hàng nghìn bức ảnh chiến tích để kích hoạt lại cảm giác quyền lực.\n3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Biến vợ và mái ấm thành "tấm khiên bình thường hóa", cô lập 2 thế giới để sống song song mà không xung đột nội tâm.\n4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Nhận án chung thân 25 năm, hắn chỉ tự thương hại bản thân vì mất danh dự, quân hàm, không hề có sự ăn năn chân thành.\n5. HỆ THỐNG TỰ BÀO CHỮA (NEUTRALIZATION): Ngụy biện mình là sĩ quan tốt bị "xung lực nhất thời cuốn đi", đổ lỗi cho ham muốn để bảo vệ bản ngã.\n6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Thăng chức chỉ huy căn cứ Trenton (7/2009) đẩy áp lực trách nhiệm lên tột độ, kích hoạt xung lực giải tỏa bệnh hoạn.\n7. SIGNATURE VS. THỦ ĐOẠN MO: MO (cắt dây điện thoại, che dấu vết) liên tục đổi để trốn tránh; Signature (chụp ảnh chiến tích, mặc đồ nạn nhân) bất biến vì là nguồn thỏa mãn tâm lý duy nhất.\n8. QUỸ ĐẠO LEO THANG 4 GIAI ĐOẠN: Sự trơ lỳ thụ thể Dopamine khiến ngưỡng thỏa mãn sụp đổ: nhìn trộm (1) → trộm đồ lưu niệm (2) → đột nhập khống chế (3) → sát hại (4).\n9. HIỆU ỨNG HÀO QUANG: Quân hàm đại tá và các huân chương tạo nên điểm mù xã hội che mắt toàn bộ cộng đồng lẫn cơ quan điều tra suốt nhiều năm.\n10. CẢNH BÁO ĐỎ SINH TỒN: 4 tín hiệu nhận diện kẻ săn mồi ẩn mình phía sau những lớp vỏ bọc đạo mạo, hoàn hảo.',
        "summary_ja": '2009年7月、デイヴィッド・ラッセル・ウィリアムズ大佐は、カナダ軍最大の戦略空軍基地であるトレントン基地の最高司令官に着任しました。エリザベス女王やカナダ首相の専用機操縦士を務め、完璧な軍規と高い知性、そして理想的な夫としての顔を持つ「非の打ち所がないエリート軍人」――それが表の顔でした。\n\nしかし、勲章に飾られた軍服の裏で、彼は二重生活を送る冷酷な捕食者でした。夜間の盗撮・下着窃盗から始まり、住居侵入、そして2名の女性（マリー＝フランス・コモー伍長、ジェシカ・ロイドさん）の命を奪うに至るまで、4段階のエスカレーションを駆け上がったのです。その仮面は2010年2月7日、オンタリオ州警察（OPP）のジム・スミス捜査官による10時間の伝説的な尋問によって完全に剥ぎ取られました。\n\n犯罪心理学ドキュメンタリー『Amber eyes』第02話では、ラッセル・ウィリアムズ事件を「10の心理・行動指標エコシステム」を通じて深層解剖します：\n1. 社会的衝撃と集団的偏執病（Collective Paranoia）：平和な町を突如襲った失踪事件は住民を疑心暗鬼に陥れ、ドアの後ろに椅子を挟んで夜を明かす恐怖と、軍への全幅の信頼が崩壊した社会的トラウマを検証。\n2. 被害者の「モノ化（Objectification）」と記念品収集：被害者を血の通った人間としてではなく、自らの支配欲を満たす「コレクション」として扱い、膨大な写真を撮影して優越感を再体験する心理構造。\n3. 身内への認識と「精神の区画化（Compartmentalization）」：献身的な妻と家庭を自らの怪異を隠す「正常性の盾」として利用し、良心の呵責を感じることなく二重生活を可能にした防音壁のメカニズム。\n4. 判決への態度と自己愛性崩壊（Narcissistic Collapse）：仮釈放なしの終身刑を宣告された際に見せたのは、被害者への真の悔悟ではなく、地位・名誉・年金を失ったことに対する病的自己憐憫（エゴの崩壊）。\n5. 自己正当化の防衛機制（Techniques of Neutralization）：「自分は本来規律正しい人間であり、抑えきれない衝動に流されただけだ」と責任を外的衝動に転嫁する認知的正当化。\n6. 心理的トリガーと限界点：2009年7月の基地司令官昇進に伴う極度の重圧が、歪んだコントロール欲求を爆発させた引き金。\n7. シグネチャー（Signature）vs 手口（MO）：発覚を防ぐために進化し続けた手口（MO）と、心理的快感を得るために一切妥協しなかった執着（シグネチャー）の決定的な違い。\n8. 4段階のエスカレーションとドーパミン耐性：神経伝達物質の耐性化により満足の閾値が崩壊し、覗き・下着窃盗から住居侵入、そして最悪の結末へと暴走した軌跡。\n9. ハロー効果（Halo Effect）と組織の盲点：輝かしい肩書と社会的威光が周囲の警戒心を麻痺させ、長年にわたり捜査網から逃れ続けた心理的要因。\n10. 生存のためのレッドフラッグ：完璧な仮面を被った捕食者を見破り、身を守るための4つの危機兆候。',
        "summary_ko": '2009년 7월, 데이비드 러셀 윌리엄스 대령은 캐나다군 최대 전략 기지인 트렌턴 공군기지의 최고사령관으로 취임했습니다. 영국 엘리자베스 2세 여왕과 캐나다 총리의 전용기를 직접 조종했던 베테랑 파일럿이자, 흠잡을 데 없는 군인 정신과 완벽한 지성을 겸비한 모범적인 남편――그것이 그가 세상에 보여준 모습이었습니다.\n\n하지만 훈장으로 가득 찬 제복 뒤편에는, 밤마다 이웃집을 배회하며 4단계의 치명적인 에스컬레이션을 거듭하던 위험한 포식자가 숨어 있었습니다. 단순 관음과 연쇄 주거침입에서 시작된 그의 범행은 결국 두 여성(마리 프랑스 코모 하사와 제시카 로이드)의 생명을 앗아가는 비극으로 치달았습니다. 그의 이중생활은 2010년 2월 7일, 온타리오 주경찰(OPP) 짐 스미스 형사가 이끈 10시간의 전설적인 심리전 끝에 종지부를 찍게 됩니다.\n\n범죄심리학 다큐멘터리 \'Amber eyes\' 02화에서는, 러셀 윌리엄스 사건을 \'10가지 핵심 심리 및 행동 지표\'를 통해 심층 해부합니다:\n1. 사회적 파장 및 집단적 공포(Collective Paranoia): 제시카 로이드의 실종 이후 마을 전체를 집어삼킨 공포, 문 뒤에 의자를 괴어놓고 밤을 지새우던 여성들, 그리고 군 최고 엘리트의 몰락이 가져온 제도적 신뢰의 붕괴.\n2. 피해자의 \'사물화(Objectification)\'와 전리품 수집: 피해자를 인격체가 아닌 지배 욕망을 채우기 위한 \'도구\'이자 \'수집품\'으로 취급하고, 수천 장의 사진을 촬영해 지배감을 지속적으로 재체험한 왜곡된 심리.\n3. 가족을 향한 태도와 \'심리적 구획화(Compartmentalization)\': 가정과 아내를 자신의 일탈을 숨기기 위한 \'정상성의 방패\'로 삼고, 두 개의 상반된 인격을 철저히 분리해 내적 갈등 없이 이중생활을 유지한 인지적 방음벽.\n4. 판결 앞에서의 나르시시즘적 붕괴(Narcissistic Collapse): 25년간 가석방 없는 무기징역 선고 앞에서도 피해자에 대한 진정한 참회가 아닌, 자신의 계급·연금·명예를 잃은 것에 대한 병적인 자기연민.\n5. 자기 정당화 및 중화 기술(Techniques of Neutralization): "나는 본래 훌륭한 군인이었으나 통제할 수 없는 충동에 휩쓸렸을 뿐"이라며 책임을 회피하고 자아를 보존하려 한 인지적 왜곡.\n6. 방아쇠가 된 심리적 트리거: 2009년 7월 기지사령관 승진에 따른 극도의 책임감과 중압감이 통제 욕구를 분출시킨 결정적 계기.\n7. 시그니처(Signature) vs 범행 수법(MO): 수사망을 피하기 위해 끊임없이 진화한 수법(MO)과, 왜곡된 쾌락을 위해 결코 포기하지 않았던 심리적 각인(시그니처)의 본질.\n8. 4단계 에스컬레이션과 도파민 내성: 신경생물학적 자극 역치가 무너지며 관음증(1단계) → 절도(2단계) → 주거침입 결박(3단계) → 살인(4단계)으로 질주한 궤적.\n9. 후광 효과(Halo Effect)와 제도의 맹점: 높은 사회적 신분과 완벽한 외적 평판이 만들어낸 보이지 않는 방패가 경찰과 사회의 감시망을 무력화한 과정.\n10. 생존을 위한 레드플래그: 도덕적 완벽주의의 가면 뒤에 숨은 포식자를 감지하고 스스로를 보호하기 위한 4대 생존 경고 신호.',
        "mux_af": ("alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1" if (EN or JA) else
                   "alimiter=limit=0.7943:attack=5:release=50:level=disabled"),
        "need": ["1.03#4", "1.05#1", "1.05#2", "1.10#2", "1.12#2", "1.14#2", "1.17#3", "2.04#1", "2.04#2",
                 "2.05#6", "2.05#7", "2.05#13", "2.05#15", "2.08#7", "3.08#10", "4.03#6", "4.08#3",
                 "4.08#7", "4.10#1", "4.10#3", "4.10#7", "4.10#8", "4.10#9", "4.11#5", "4.11#8", "4.12#2",
                 "5.02#4", "5.04#2", "5.04#3", "5.04#5", "5.04#6", "5.04#7", "5.04#8", "5.04#9"],
        "case": "Williams",
        "n1": (("BASE PERSONNEL", "Military Community Perspective", "BASE PERSONNEL") if EN else
               ("トレントン基地関係者", "軍関係者の証言", "関係者") if JA else
               ("트렌턴 기지 관계자", "군 관련자 증언", "관계자") if KO else
               ("BINH SĨ CĂN CỨ TRENTON", "Nhân vật hình dung", "BINH SĨ")),
        "n2": (("CASE OBSERVER", "Public Reaction", "CASE OBSERVER") if EN else
               ("ツイード住民", "市民の反応", "住民") if JA else
               ("트위드 주민", "시민의 반응", "주민") if KO else
               ("KHÁN GIẢ", "Theo dõi vụ án", "KHÁN GIẢ")),
        # ---- bản tiếng Anh: nhãn vai (CHU_CO_DINH_EN.md §3)
        "roles_en": {"H": ("HOST", "Your Narrator"), "D": ("INVESTIGATOR", "Forensic Case Analysis"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("BASE PERSONNEL", "Military Community Perspective"),
                     "N2": ("CASE OBSERVER", "Public Reaction")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "BASE PERSONNEL", "N2": "CASE OBSERVER"},
        # ---- bản tiếng Nhật / Hàn: nhãn vai riêng cho Tập 02.
        # Vai N1 = quan binh căn cứ Trenton · N2 = dân Tweed (Mèo). Nhãn chung
        # ("証人"/"증인") của Tập 01 sai với vụ án này -> phải khai riêng.
        "roles_ja": {"H": ("ホスト", "ナレーター"), "D": ("捜査官", "事件記録 Williams"),
                     "C": ("心理学者", "犯罪心理学"),
                     "N1": ("トレントン基地関係者", "軍関係者の証言"),
                     "N2": ("ツイード住民", "市民の反応")},
        "sub_tags_ja": {"H": "ホスト", "D": "捜査官", "C": "心理学者",
                        "N1": "関係者", "N2": "住民"},
        "roles_ko": {"H": ("호스트", "내레이터"), "D": ("수사관", "사건 기록 Williams"),
                     "C": ("심리학자", "범죄심리학"),
                     "N1": ("트렌턴 기지 관계자", "군 관련자 증언"),
                     "N2": ("트위드 주민", "시민의 반응")},
        "sub_tags_ko": {"H": "호스트", "D": "수사관", "C": "심리학자",
                        "N1": "관계자", "N2": "주민"},
        # ---- bản tiếng Anh: thẻ cảnh báo intro (CHU_CO_DINH_EN.md §2) — chữ dài hơn bản Tập 01
        # nên thẻ rộng hơn, chữ nhỏ hơn, mỗi gạch đầu dòng tự xuống dòng.
        "cards_en": (
            ("ABOUT THIS DOCUMENTARY", [
                [("Educational content:", 1),
                 (" A forensic & criminal psychology analysis based strictly on public records, "
                  "trial exhibits, and official police interrogation transcripts.", 0)],
                [("Investigative purpose:", 1),
                 (" Produced solely for educational, criminological, and public safety awareness.", 0)],
                [("No defamation:", 1),
                 (" Not intended to defame, harass, or inflict distress upon any innocent individuals "
                  "or victims’ families.", 0)]]),
            ("VIEWER DISCRETION & ADVISORY", [
                [("Mature audience only:", 1),
                 (" Contains mature themes, discussions of burglary, stalking, and non-graphic "
                  "accounts of violent crime. Viewer discretion is advised.", 0)],
                [("AI & Dramatization:", 1),
                 (" Narrated with synthetic AI voices. Visuals and character avatars are "
                  "dramatized illustrations and do not depict real persons.", 0)],
                [("Professional boundaries:", 1),
                 (" Not a substitute for professional legal, medical, or psychiatric advice.", 0)]])),
        "card_geom": {"cw": 1660, "ch": 780, "size": 40, "line_h": 54, "gap": 22, "y0": 178},
        "cast": None,                  # dùng giọng mặc định của kênh (bộ A)
        "cast_ko": True,
    },
    "03": {
        "script": WORK / ("script_tap03_EN.json" if EN else "script_tap03.json"),
        "dir": "Tap03_EN" if EN else "Tap03",
        "plan": "KeHoach_Video_Tap03_EN.md" if EN else "KeHoach_Video_Tap03.md",
        "master": "Tap03_EN_master" if EN else "Tap03_master",
        "srt": "Tap03_EN.srt" if EN else "Tap03.srt",
        "intro": "intro_kenh_EN_t03.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.09": "N1", "2.09": "N2"},
        "acting": WORK / ("acting_tap03_EN.json" if EN else "acting_tap03.json"),
        "sfx_sheet": WORK / "sfx_tap03.json",
        "act1_cue": "1.14", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_piano_minimal.mp3"),
                2: ("bgm_ambient_deep.mp3",),
                3: "bgm_cello_sad_v2.mp3",
                4: "bgm_sub_drone.mp3",
                5: ("bgm_violin_heart.mp3", "bgm_piano_minimal.mp3")},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("IQ 145", "GIANT") if EN else ("IQ 145の", "怪物") if JA else ("IQ 145", "GƯƠNG"),
        "thumb_bg": "t3_brain_mirror",
        "title": ("Ep. 03: The IQ 145 Giant & The Mirror of Psychological Autopsy | Criminal Psychology: Edmund Kemper (10 Psychological Markers & The Birth of FBI Mindhunter)" if EN else
                  "第03話 · IQ 145の巨人と精神解剖の鏡 | エドマンド・ケンパーの犯罪心理学 (10の心理指標とFBIマインドハンターの起源)" if JA else
                  ("03화 · IQ 145의 거인과 정신 해부의 거울 | 에드먼드 켐퍼의 범죄심리학 (10가지 심리 지표와 FBI 마인드헌터의 기원)" if KO else
                   "Tập 03: Gã Khổng Lồ IQ 145 & Chiếc Gương Giải Phẫu Tâm Trí | Tâm lý học tội phạm: Edmund Kemper (10 Chỉ Dấu Tâm Lý & Nguồn Gốc FBI Mindhunter)")),
        "summary_vn": ("Rạng sáng ngày 24/4/1973, từ một bốt điện thoại ven đường tại thị trấn Pueblo, bang Colorado, "
                        "một gã thanh niên khổng lồ cao 2m06, nặng 127kg đã gọi điện đến đồn cảnh sát Santa Cruz, California "
                        "để đầu thú về chuỗi tội ác kinh hoàng: sát hại mẹ ruột, bạn thân của mẹ và 6 nữ sinh trẻ tuổi. "
                        "Đó là Edmund Kemper – một trường hợp dị biệt sở hữu chỉ số IQ 145 thuộc top 0,13% trí tuệ nhân loại. "
                        "Thay vì chối tội, Kemper đã mở toang tâm trí trong buồng giam tại Cơ sở Y tế Vacaville, đối thoại hàng chục "
                        "giờ đồng hồ cùng các đặc vụ tiên phong Robert Ressler và John Douglas, đặt nền móng khai sinh ra "
                        "Đơn vị Khoa học Hành vi (BSU) và mạng lưới hồ sơ tội phạm quốc gia VICAP của FBI."),
        "summary_en": ("In the early morning of April 24, 1973, from a roadside payphone in Pueblo, Colorado, a 6'9\", 280-pound giant "
                        "called Santa Cruz police to confess to a string of horrifying murders: his mother, her friend, and six young college students. "
                        "That man was Edmund Kemper — an extraordinary anomaly in criminal history possessing an IQ of 145. Rather than denying guilt, "
                        "Kemper opened his mind at the Vacaville Medical Facility, engaging in deep dialogues with FBI pioneering agents "
                        "Robert Ressler and John Douglas that laid the cornerstone for the Behavioral Science Unit (BSU) and VICAP."),
        "summary_ja": ("1973年4月24日未明、コロラド州プエブロの公衆電話から、身長2メートル06、体重127キロの巨漢が警察に電話をかけ、"
                        "実母と親友、そして6人の女子大生たちの連続殺害を自首しました。その男の名はエドマンド・ケンパー――IQ 145の天才的頭脳を持つ"
                        "異例の連続殺人鬼でした。彼は独房でFBI特別捜査官ロバート・レスラーやジョン・ダグラスと対話を重ね、"
                        "自身の精神を冷徹に解剖してみせ、FBI行動科学部門（BSU）と凶悪犯罪追跡網（ViCAP）の礎となりました。"),
        "summary_ko": ("1973년 4월 24일 새벽, 콜로라도주 푸에블로의 공중전화에서 키 2m 06cm, 몸무게 127kg의 거구가 경찰에 전화를 걸어 "
                        "친어머니와 어머니의 친구, 그리고 6명의 여대생 연쇄 살인을 자수했습니다. IQ 145의 천재적 지능을 지닌 에드먼드 켐퍼였습니다. "
                        "그는 독방에서 FBI 프로파일러 로버트 레슬러, 존 더글러스와 마주 앉아 자신의 내면을 냉철하게 해부하며 "
                        "FBI 행동과학국(BSU)과 연쇄범죄 추적망(ViCAP)의 초석을 놓았습니다."),
        "voice_credit": "This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio",
        "act_titles": ({1: "Act 1 · Midnight Call from a Colorado Phone Booth",
                        2: "Act 2 · The Scene & The Hunting Chain — Ladder of Substitution",
                        3: "Act 3 · Psychological Autopsy — Inside the Mind of an Introspective Psychopath",
                        4: "Act 4 · Dialogues with the FBI — Foundation of Criminal Profiling",
                        5: "Act 5 · Verdict, Red Flag Lessons & Epilogue"} if EN else
                       {1: "第1幕 · コロラドの電話ボックスから届く深夜の通話",
                        2: "第2幕 · 現場と狩りの連鎖――代替の階段",
                        3: "第3幕 · 心理剖検――内省型サイコパスの脳の内側",
                        4: "第4幕 · FBIとの対話――犯罪プロファイリング技術の基礎",
                        5: "第5幕 · 判決、赤い警鐘の教訓＆終幕"} if JA else
                       {1: "Hồi 1 · Cuộc gọi nửa đêm từ bốt điện thoại Colorado",
                        2: "Hồi 2 · Hiện trường & chuỗi săn mồi — Nấc thang của sự thay thế",
                        3: "Hồi 3 · Giải phẫu tâm lý — Bên trong bộ não kẻ thái nhân cách tự phản tỉnh",
                        4: "Hồi 4 · Đối thoại với FBI — Nền tảng của nghệ thuật lập hồ sơ tội phạm",
                        5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ & lời kết"}),
        # Hashtag dòng cuối mô tả YouTube (bản tiếng Việt). Bản EN có sẵn trong
        # CHU_CO_DINH_EN.md; bản JA/KO chưa có dòng hashtag.
        "hashtags": "#TrueCrime #CriminalPsychology #EdmundKemper #Mindhunter #FBIProfiling #ForensicPsychology #Documentary #AmberEyes #TamLyToiPham #PhamVan #HoiTo",
        "summary": ("1.03#1", "5.08#1"),
        # A7 + A11 #64 (bản EN, 03/11/2026): audio master EN có đỉnh mẫu −2,5 dBFS ⇒
        # AAC dựng lại vọn true peak lên −0,7 dBFS (vượt trần A7 −1,5 dBFS).
        # Hạ trần alimiter xuống −4 dBFS (0.63) + latency=1 để bù trễ 4,98 ms của
        # limiter ⇒ true peak ≈ −2,2 dBFS và lệch A/V ≈ 0 ms.
        # Bản VN giữ nguyên chuỗi cũ (đang đạt −1,7 dBFS) ⇒ không đổi thành phẩm đã xuất.
        # Bản JA (03/11/2026): đo master wav JA = true peak −1,6 dBFS / sample peak −1,90 dBFS
        # ⇒ chỉ 0,1 dB dưới trần A7 −1,5 dBFS; AAC dựng lại vọn true peak lên ~+1,8 dB
        # (đúng như bản EN) ⇒ dùng CÙNG chuỗi đã chứng minh cho EN: limit=0.63 (−4 dBFS)
        # + latency=1 (bù trễ 4,98 ms của limiter ⇒ lệch A/V ≈ 0 ms).
        # KHÔNG đụng chuỗi của VN/KO (đã xuất, đang đạt chuẩn).
        "mux_af": ("alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1" if (EN or JA) else
                   "alimiter=limit=0.7943:attack=5:release=50:level=disabled"),
        "need": ["1.05#3", "1.10#1", "1.10#10", "1.13#7", "2.04#5", "2.06#2", "3.05#7", "3.05#10", "3.08#8", "3.08#10", "4.05#15", "4.05#19", "4.08#2", "5.02#5", "5.02#7", "5.02#12", "5.05#4", "5.05#5", "5.08#3"],
        "case": "Kemper",
        "n1": (("SANTA CRUZ DESK OFFICER", "Night Desk Officer", "SANTA CRUZ DESK") if EN else
               ("サンタクルーズ警察当直", "当直警官の証言", "警察官") if JA else
               ("TRỰC BAN CẢNH SÁT SANTA CRUZ", "Người trực đêm", "TRỰC BAN")),
        "n2": (("BAR COLLEAGUE OFFICER", "The Jury Room Regular", "BAR POLICE") if EN else
               ("酒場の同僚警察官", "市民と警察の視点", "警察官") if JA else
               ("CẢNH SÁT QUÁN RƯỢU", "Đồng nghiệp tại The Jury Room", "CẢNH SÁT")),
        # ---- bản tiếng Anh: nhãn vai (CHU_CO_DINH_EN.md §3)
        # THIẾU khối này thì ROLE_NAME/SUB_TAG rơi về nhãn cứng của Tập 01 EN
        # ("Blanchard case file", "SPRINGFIELD RESIDENT") -> sai vụ án hiện trên màn hình.
        "roles_en": {"H": ("HOST", "Your Narrator"), "D": ("INVESTIGATOR", "Forensic Case Analysis"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("SANTA CRUZ DESK OFFICER", "Night Desk Officer"),
                     "N2": ("BAR COLLEAGUE OFFICER", "The Jury Room Regular")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "SANTA CRUZ DESK", "N2": "BAR POLICE"},
        "cast": None,                  # dùng giọng mặc định của kênh (bộ A)
        "cast_ko": True,
    },
    "04": {
        "script": WORK / ("script_tap04_EN.json" if EN else "script_tap04.json"),
        "dir": "Tap04_EN" if EN else "Tap04",
        "plan": "KeHoach_Video_Tap04_EN.md" if EN else "KeHoach_Video_Tap04.md",
        "master": "Tap04_EN_master" if EN else "Tap04_master",
        "srt": "Tap04_EN.srt" if EN else "Tap04.srt",
        "intro": "intro_kenh_EN_t04.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.07": "N1", "4.06": "N2"},
        "acting": WORK / ("acting_tap04_EN.json" if EN else "acting_tap04.json"),
        "sfx_sheet": WORK / "sfx_tap04.json",
        "act1_cue": "1.15", "silence_cue": "1.11", "click_cues": ("1.06", "4.05"),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_piano_minimal.mp3", "bgm_sub_drone.mp3"), 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: "bgm_sub_drone.mp3", 4: "bgm_ambient_deep.mp3", 5: ("bgm_violin_heart.mp3", "bgm_piano_minimal.mp3")},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},                                      # T7 Tập 02: ghim không nhãn (không nêu địa điểm nhà nạn nhân)
        "thumb": ("ANGEL OF", "DEATH") if EN else ("死の天使", "16年の沈黙") if JA else ("THIÊN THẦN", "TỬ THẦN"),
        "thumb_bg": "t4_somerset_exterior",
        # H9: nen sang o dai chu -> them lop toi mem (chi T04; T01/T02 giu nguyen duong cu)
        "text_scrim": ["1-06", "1-09", "1-10", "1-11", "1-15", "1-16", "1-18", "2-01", "2-04", "2-05", "2-10", "2-11", "2-12", "2-13",
                    "3-02", "3-11", "3-14", "3-15", "4-04", "4-05", "4-10", "4-11", "4-20", "5-02", "5-05", "5-18", "5-19"] + (["1-13", "1-14", "1-17", "2-06", "2-08", "2-09", "2-15", "2-17", "3-01", "3-04", "3-16", "4-02", "4-06", "4-15",
                       "4-17", "4-19", "4-21", "5-01", "5-03", "5-04", "5-07", "5-14"] if (EN or JA) else [])
                    + (["2-12", "2-13", "2-21", "3-07", "3-10", "4-03", "4-10", "5-09"] if JA else []),   # EN: chữ dài hơn bản VN (06/11/2026)
        "voice_credit": "This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio",
        "mux_af": ("alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1" if (EN or JA) else
                   "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1"),
        "title": ("Ep. 04: The Angel of Death & The God Complex | Criminal Psychology: Charles Cullen" if EN else
                  "第04話 · 死の天使と神コンプレックス | 犯罪心理学：チャールズ・カレン事件" if JA else
                  "04화 · 죽음의 천사와 신 콤플렉스 | 범죄심리학: 찰스 컬런 사건" if KO else
                  "Tập 04: Thiên Thần Tử Thần & Phức Cảm Chúa Trời | Tâm lý học tội phạm: Charles Cullen (Phức cảm Chúa trời)"),
        "act_titles": ({1: "Act 1 · The Paradox of the Model Nurse",
                        2: "Act 2 · The Crime Scene – The Escalation Trajectory of the Abyss",
                        3: "Act 3 · Psychological Autopsy – Inside the Brain of the God Complex",
                        4: "Act 4 · The Interrogation & The Breakthrough",
                        5: "Act 5 · The Verdict, Survival Red Flags & Epilogue"} if EN else
                       {1: "第1幕 · 模範的看護師のパラドックス",
                        2: "第2幕 · 犯行現場――深淵のエスカレーション軌道",
                        3: "第3幕 · 心理解剖――神コンプレックスの脳内",
                        4: "第4幕 · 取調の攻防――捜査の重大な転換点",
                        5: "第5幕 · 判決、生存への警告と結び"} if JA else
                       {1: "제1막 · 모범 간호사의 역설",
                        2: "제2막 · 범죄 현장 – 심연의 에스컬레이션 궤적",
                        3: "제3막 · 심리 부검 – 신 콤플렉스의 뇌 속으로",
                        4: "제4막 · 심문실의 공방 – 수사의 결정적 돌파구",
                        5: "제5막 · 판결, 생존을 위한 경고와 맺음말"} if KO else
                       {1: "Hồi 1 · Nghịch lý của người y tá mẫu mực",
                        2: "Hồi 2 · Hiện trường & Hồ sơ tội ác – Quỹ đạo leo thang của vực thẳm",
                        3: "Hồi 3 · Giải phẫu tâm lý – Bên trong bộ não của kẻ mang Phức cảm Chúa trời",
                        4: "Hồi 4 · Đấu trí thẩm vấn & Bước ngoặt điều tra",
                        5: "Hồi 5 · Phán quyết, Bài học cảnh báo đỏ & Lời kết"}),
        # Hashtag dòng cuối mô tả YouTube (bản tiếng Việt). Bản EN có sẵn trong
        # CHU_CO_DINH_EN.md; bản JA/KO chưa có dòng hashtag.
        "hashtags": "#TrueCrime #CriminalPsychology #CharlesCullen #TheGoodNurse #ForensicPsychology #AngelOfDeath #Documentary #AmberEyes #TamLyToiPham #PhamVan #HoiTo",
        "summary": ("1.03#1", "5.08#2"),
        # 02/11/2026: 29 mốc dữ kiện đã đối chiếu nguồn công khai (bảng nguồn:
        # 02_SAN_XUAT/Tap04/nguon_tham_khao.md). Trước đó rỗng ⇒ package.py ghi
        # bảng "cần bổ sung" rỗng và mô tả thiếu mục NGUỒN THAM KHẢO.
        "need": ["1.03#2", "1.03#4", "1.05#3", "1.08#2", "1.10#1", "1.10#2", "1.14#5", "1.14#6",
                 "2.04#1", "2.06#1", "2.06#4", "2.08#2", "2.08#6", "2.11#2", "2.11#4", "2.11#6",
                 "3.04#2", "3.04#3", "3.09#1", "3.09#6", "4.02#2", "4.04#2", "4.08#3", "4.11#1",
                 "5.02#3", "5.02#4", "5.02#6", "5.04#4", "5.08#3"],
        "case": "Cullen",
        "n1": (("SOMERSET NURSE", "Night Shift Perspective", "NURSE") if EN else
               ("ソマーセットの看護師", "夜勤の同僚", "看護師") if JA else
               ("NỮ Y TÁ SOMERSET", "Đồng nghiệp ca đêm", "Y TÁ")),
        "n2": (("NIGHT-SHIFT NURSE", "Imagined Perspective", "NURSE") if EN else
               ("夜勤の看護師", "想像上の視点", "看護師") if JA else
               ("Y TÁ CA ĐÊM", "Nhân vật hình dung", "Y TÁ CA ĐÊM")),
        # ---- bản tiếng Anh: nhãn vai (CHU_CO_DINH_EN.md §3)
        "roles_en": {"H": ("HOST", "Your Narrator"), "D": ("INVESTIGATOR", "Forensic Case Analysis"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("SOMERSET NURSE", "Night Shift Perspective"),
                     "N2": ("NIGHT-SHIFT NURSE", "Imagined Perspective")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "SOMERSET NURSE", "N2": "NIGHT-SHIFT NURSE"},
        # ---- bản tiếng Nhật: nhãn vai riêng cho Tập 04.
        # Thiếu khoá này thì ROLE_NAME rơi về nhãn chung của Tập 01
        # ("証人"/"視聴者") -> sai với vụ án Cullen (N1 = y tá ca đêm ở Somerset,
        # N2 = Amy Laughren, đồng nghiệp ICU & người tố giác).
        "roles_ja": {"H": ("ホスト", "ナレーター"), "D": ("捜査官", "事件記録 Cullen"),
                     "C": ("心理学者", "犯罪心理学"),
                     "N1": ("ソマーセットの看護師", "夜勤の同僚"),
                     "N2": ("夜勤の看護師", "想像上の視点")},
        "sub_tags_ja": {"H": "ホスト", "D": "捜査官", "C": "心理学者",
                        "N1": "看護師", "N2": "看護師"},
        "cast": None,
        "cast_ko": True,
    },
    "05": {
        "script": WORK / ("script_tap05_EN.json" if EN else "script_tap05.json"),
        "dir": "Tap05_EN" if EN else "Tap05",
        "plan": "KeHoach_Video_Tap05_EN.md" if EN else "KeHoach_Video_Tap05.md",
        "master": "Tap05_EN_master" if EN else "Tap05_master",
        "srt": "Tap05_EN.srt" if EN else "Tap05.srt",
        "intro": "intro_kenh_EN_t05.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.09": "N1", "4.15": "N2"},
        "acting": WORK / ("acting_tap05_EN.json" if EN else "acting_tap05.json"),
        "sfx_sheet": WORK / "sfx_tap05.json",
        "act1_cue": "1.15", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_piano_minimal.mp3"), 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 4: "bgm_ambient_deep.mp3",
                5: ("bgm_violin_heart.mp3", "bgm_piano_minimal.mp3")},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {"2-06": "t5_park_trashcan_drop", "2-10": "t5_church_council_altar"},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("THE PURPLE", "FLOPPY DISK") if EN else ("紫色の", "フロッピーディスク") if JA else ("CHIẾC ĐĨA MỀM", "MÀU TÍM"),
        "thumb_bg": "t5_purple_floppy_disk",
        "title": ("Ep. 05: The Purple Floppy Disk | The Psychology of BTK Dennis Rader (10 Psychological Markers & Compartmentalization)"
                  if EN else "第05話：紫色のフロッピーディスク | BTK デニス・レイダーの犯罪心理学（10の心理指標と精神の分断）" if JA else
                  "05화 · 보라색 플로피 디스크 | BTK 데니스 레이더의 범죄심리학 (10가지 심리 지표와 내면의 구획화)" if KO else
                  "Tập 05: Chiếc Đĩa Mềm Màu Tím & Cơn Nghiện Ái Kỷ | Tâm lý học tội phạm: BTK Dennis Rader (10 Chỉ Dấu Tâm Lý & Sự Phân Mảnh Tâm Trí)"),
        "act_titles": ({1: "Act 1 · The Letter Resurfaces After 13 Years of Silence",
                        2: "Act 2 · The Crime Scene & Psychological Signature of a Two-Faced Predator",
                        3: "Act 3 · Inside the Mind of Malignant Narcissism — Compartmentalization & Factor X",
                        4: "Act 4 · The Interrogation & The Digital Forensic Trap",
                        5: "Act 5 · The Verdict, Survival Red Flags & Epilogue"} if EN else
                       {1: "第1幕 · 13年の沈黙を破る手紙",
                        2: "第2幕 · 犯罪現場と二面獣の心理的署名",
                        3: "第3幕 · 歪んだ自己愛の内面――精神の分断とファクターX",
                        4: "第4幕 · 尋問の心理戦とフロッピーディスクの罠",
                        5: "第5幕 · 判決、赤い警報と終幕"} if JA else
                       {1: "제1막 · 13년의 침묵을 깨고 나타난 편지",
                        2: "제2막 · 범죄 현장과 두 얼굴을 가진 포식자의 시그너처",
                        3: "제3막 · 악성 나르시시즘의 내면 — 구획화와 요인 X",
                        4: "제4막 · 심문실의 심리전과 플로피 디스크의 함정",
                        5: "제5막 · 판결, 생존을 위한 붉은 경보와 맺음말"} if KO else
                       {1: "Hồi 1 · Bức thư tái xuất sau 13 năm lặng căm", 2: "Hồi 2 · Hiện trường & Chữ ký tâm lý của con thú hai mặt",
                        3: "Hồi 3 · Bên trong bộ não ái kỷ ác tính — Sự chia ngăn & Tự bào chữa", 4: "Hồi 4 · Đấu trí thẩm vấn & Bẫy công nghệ đĩa mềm",
                        5: "Hồi 5 · Phán quyết, bài học cảnh báo đỏ và lời kết"}),
        "roles_line": "Lời của Điều tra viên, Chuyên gia tâm lý, Người dân Park City và Kerri Rawson là lời dựng lại dựa trên tư liệu.",
        "hashtags": "#AmberEyes #TrueCrime #TamLyToiPham #BTK #DennisRader #ChiecDiaMemMauTim #ChiaNganTamTri #AiKyAcTinh #10ChiDauTamLy #CanhBaoDo #HoSoToiPham",
        "summary": ("1.10#5", "3.02#1"),
        "summary_vn": (
            "Suốt hơn 30 năm (1974–2005), Dennis Lynn Rader đã dựng nên một chiếc mặt nạ công dân mẫu mực đến kinh ngạc tại Park City, Kansas: "
            "chủ tịch hội đồng nhà thờ Lutheran, huynh trưởng Hướng đạo sinh, cựu quân nhân Không quân và kiểm soát viên trật tự đô thị nghiêm khắc. "
            "Nhưng ẩn sâu dưới vỏ bọc đạo mạo đó là kẻ săn mồi hai mặt gieo rắc kinh hoàng cho cả vùng Wichita. "
            "Cuộc đấu trí lịch sử chỉ ngã ngũ vào ngày 25/02/2005 khi trung úy Ken Landwehr giăng chiếc bẫy công nghệ qua một chiếc đĩa mềm màu tím, "
            "bóc trần toàn bộ cơ chế phân mảnh tâm trí và cơn nghiện ái kỷ ác tính kéo dài ba thập kỷ.\n\n"
            "Hồ sơ Dennis Rader (\"BTK\") được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:\n"
            "1. DƯ CHẤN XÃ HỘI & NỖI HOANG TƯỞNG TẬP THỂ: Cuộc săn lùng kéo dài 3 thập kỷ gieo rắc kinh hoàng tại Wichita; người dân chốt cửa, mua vũ khí, nghịch lý khi chính Rader lắp đặt còi báo động cho hàng trăm gia đình.\n"
            "2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem nạn nhân là \"dự án\", \"con mồi\" vô danh; cướp đồ lưu niệm và phác thảo sơ đồ để kích hoạt lại cảm giác toàn năng trong tưởng tượng.\n"
            "3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Xây dựng \"bức tường bê tông\" tâm lý tách biệt hoàn hảo người chồng mẫu mực, chủ tịch hội đồng nhà thờ với kẻ săn mồi máu lạnh.\n"
            "4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Khi nhận án 175 năm tù, Rader chỉ than vãn về việc bị cảnh sát lừa dối qua đĩa mềm và danh dự cá nhân tan biến, không hề có sự ăn năn thực thụ.\n"
            "5. HỆ THỐNG TỰ BÀO CHỮA (NEUTRALIZATION / FACTOR X): Ngụy tạo khái niệm \"Nhân tố X\" ma quái như một thực thể ngoại lai chiếm đoạt tâm trí để phủi sạch trách nhiệm đạo đức.\n"
            "6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Năm 2004, kỷ niệm 30 năm vụ án Otero và cuốn sách sắp xuất bản của tờ Wichita Eagle đe dọa biến hắn thành kẻ vô danh, kích hoạt cơn khát danh vọng trở lại.\n"
            "7. SIGNATURE VS. THỦ ĐOẠN MO: MO (cắt dây điện thoại, dùng đĩa mềm, ký hiệu chữ) biến đổi theo công nghệ; Signature (thư khiêu khích, trói buộc biểu tượng, nhu cầu được công chúng sùng bái) bất biến.\n"
            "8. QUỸ ĐẠO LEO THANG 4 GIAI ĐOẠN: Sự trơ lỳ thụ thể Dopamine đẩy hành vi qua 4 nấc: ảo tưởng xâm nhập (1) → bám đuôi rình rập (2) → đột nhập khống chế (3) → xâm hại và tước đoạt sinh mạng (4).\n"
            "9. HIỆU ỨNG HÀO QUANG: Chiếc áo phản quang kiểm soát viên trật tự đô thị và chức chủ tịch hội đồng nhà thờ tạo điểm mù tuyệt đối che mắt láng giềng suốt 3 thập kỷ.\n"
            "10. CẢNH BÁO ĐỎ SINH TỒN: 4 tín hiệu nhận diện kẻ săn mồi ẩn danh: lạm quyền vi mô, thói quen thu thập đồ đạc bí mật, sự thấu cảm có điều kiện và phản ứng giận dữ tột cùng khi bị phớt lờ."
        ),
        "summary_ja": (
            "30年以上にわたり（1974–2005）、デニス・リン・レイダーは米カンザス州パークシティで完璧な善良市民の仮面を維持し続けました。"
            "ルーテル教会の役員会長、ボーイスカウトの指導員、空軍退役軍人、そして厳格な市規律取締官――しかしその裏で、彼はウィチタ一帯を恐怖に陥れた連続捕食者「BTK」でした。"
            "2004年に13年の沈黙を破った彼は、2005年2月25日、ケン・ランドウェアー警部補が仕掛けた「紫色のフロッピーディスク」のデジタルフォレンジックの罠に落ち、30年におよぶ二重生活は自滅へと向かいます。\n\n"
            "本動画では、デニス・レイダー（BTK）の精神構造を「10の核心的心理・行動指標」から徹底解剖します：\n"
            "1. 社会的余震と集団的妄想：30年にわたる恐怖がウィチタを覆い、市民が防犯に走る中、皮肉にもレイダー自身が警報装置の設置技術者として家庭に入り込んでいた逆説。\n"
            "2. 被害者の客体化（モノ化）：被害者を人格なき「標的」「獲物」と見なし、記念品を奪いスケッチを描くことで全能感を反芻する心理。\n"
            "3. 精神の分断（コンパートメンタライゼーション）：模範的な家長・教団幹部と冷酷な捕食者を強固な心理的分離壁で隔て、良心の呵責なく共存させた異常機制。\n"
            "4. 自己愛の崩壊（ナルシシスティック・コラプス）：懲役175年の判決に直面しても、警察に騙されたことと社会的地位の喪失を嘆くだけで、真の悔悟は見られない自己憐憫。\n"
            "5. 自己正当化システム（中和技術・ファクターX）：「ファクターX」という外的な悪霊の仕業だと主張し、道徳的責任を外部化して自尊心を守る防衛機制。\n"
            "6. 心理的トリガーと破綻点：2004年、オテロ事件30周年と地元紙記者による書籍化計画に危機感を覚え、自らの名声が忘れ去られる恐怖から再始動した衝動。\n"
            "7. シグネチャー対犯行手口（MO）：手口（電話線切断、フロッピー活用）は進化する一方、シグネチャー（挑発文、象徴的拘束、世間の称賛欲求）は一生不変の核心動機。\n"
            "8. 4段階のエスカレーション軌道：ドーパミン受容体の鈍麻による閾値低下：侵入的妄想（1）→ 執拗な尾行・ストーキング（2）→ 住居侵入拘束（3）→ 致命的危害（4）。\n"
            "9. ハロー効果と社会的盲点：行政制服、記章、教団役員の肩書が最強の社会的防壁となり、近隣住民や捜査機関の目を30年間完全に遮断した盲点。\n"
            "10. 生存のための赤い警報（レッドフラグ）：微細な権力乱用、収集癖と隠し場所、条件付きの共感性、無視された際の激しい自己愛憤怒の4つの危険シグナル。"
        ),
        "summary_ko": (
            "30년이 넘는 세월(1974~2005) 동안 데니스 린 레이더는 미국 캔자스주 파크시티에서 완벽한 모범 시민의 가면을 유지했습니다. "
            "루터교회 평의회 의장, 보이스카우트 지도자, 공군 전역자, 그리고 엄격한 시 조례 단속관—하지만 그 점잖은 외피 아래에는 위치타 일대를 공포에 떨게 한 연쇄 포식자 'BTK'가 숨어 있었습니다. "
            "2004년 13년의 침묵을 깨고 나타난 그는 2005년 2월 25일, 켄 랜드웨어 경위가 파놓은 '보라색 플로피 디스크' 디지털 포렌식 함정에 걸려들며 30년간의 이중생활에 종지부를 찍게 됩니다.\n\n"
            "본 영상에서는 데니스 레이더의 내면을 '10가지 핵심 심리 및 행동 지표'를 통해 정밀 해부합니다:\n"
            "1. 사회적 여진과 집단적 공포증: 30년간 위치타를 짓누른 공포 속에서 시민들이 문을 걸어 잠글 때, 정작 레이더 자신이 방범 경보기를 설치하며 집집마다 드나든 잔혹한 역설.\n"
            "2. 피해자의 객체화(사물화): 피해자를 인격체가 아닌 '프로젝트'이자 소유물로 취급하며, 전리품과 스케치를 통해 전능감을 환상 속에서 지속적으로 재활성화.\n"
            "3. 내면의 구획화(심리적 콘크리트벽): 헌신적인 가장·교회 지도자의 영역과 냉혹한 가해자의 영역 사이에 절대적 분리벽을 세워 죄책감 없이 병행한 이상 방어기제.\n"
            "4. 악성 나르시시즘의 붕괴: 175년형 선고 앞에서도 피해자에 대한 진정한 참회 없이, 경찰의 속임수에 넘어간 수치심과 자신의 명예 실추만을 한탄하는 자기연민.\n"
            "5. 자기정당화 기제(요인 X의 왜곡): 내면의 범죄 충동을 '요인 X'라는 외부 초자연적 존재 탓으로 돌려 도덕적 죄책감을 회피하고 자아를 방어한 기술.\n"
            "6. 심리적 방아쇠와 임계점: 2004년 오테로 사건 30주년과 지역 기자의 책 출간 소식이 자신의 악명을 잊히게 만들 것이라는 공포를 자극해 재출현을 촉발.\n"
            "7. 시그너처 대 범행 수법(MO): 수법(전화선 절단, 디스크 전달)은 상황에 따라 변했으나, 시그너처(도발 편지, 상징적 결박, 사회적 관심 갈망)는 불변의 핵심 욕망으로 지속.\n"
            "8. 4단계 에스컬레이션 궤적: 도파민 수용체 둔감화로 인한 자극 역치 붕괴: 침습적 망상(1) → 스토킹 및 미행(2) → 가택 침입(3) → 치명적 가해(4).\n"
            "9. 후광 효과와 사회적 맹점: 단속관 완장, 군 경력, 교회 회장이라는 반듯한 사회적 지위가 이웃과 수사망을 30년간 완벽히 가린 맹점 형성.\n"
            "10. 생존을 위한 붉은 경보: 일상적 소권력 남용, 비밀 수집벽, 조건부 공감 능력, 무시당했을 때 폭발하는 나르시시즘적 분노 등 4가지 위험 신호."
        ),
        "sos_ja": """🆘 相談窓口・緊急連絡先（日本国内）
• 警察相談専用電話：#9110（事件事故に至る前のストーカー・嫌がらせ・犯罪被害等の相談窓口）
• よりそいホットライン：0120-279-338（通話料無料・24時間対応）
• こころの健康相談統一ダイヤル：0570-064-556
• 緊急通報：110（警察）、119（消防・救急）""",
        "sos_ko": """🆘 범죄 피해 및 위기 상담 전화 (대한민국)
• 경찰청 범죄 신고: 112
• 여성긴급전화: 1366 (24시간 가정폭력·성폭력 상담)
• 정신건강위기상담전화: 1577-0199
• 자살예방상담전화: 109""",
        "hashtags_ja": "#AmberEyes #犯罪心理学 #BTK #デニスレイダー #実録犯罪 #心理分析 #デジタルフォレンジック #フロッピーディスク #事件記録 #プロファイリング",
        "hashtags_ko": "#AmberEyes #범죄심리학 #BTK #데니스レイ더 #연쇄살인 #프로파일링 #디지털포렌식 #플로피디스크 #실제사건 #사건기록",
        "need": [],
        "case": "Rader",
        "n1": (("PARK CITY RESIDENT", "Suburban Neighbor", "RESIDENT") if EN else
               ("パークシティ住民", "郊外の隣人", "住民") if JA else
               ("NGƯỜI DÂN PARK CITY", "Hàng xóm ngoại ô", "NGƯỜI DÂN")),
        "n2": (("KERRI RAWSON", "Daughter of Dennis Rader", "KERRI") if EN else
               ("ケリー・ローソン", "デニス・レイダーの実娘", "娘") if JA else
               ("KERRI RAWSON", "Con gái ruột", "KERRI")),
        "roles_en": {"H": ("HOST", "Your Narrator"), "D": ("INVESTIGATOR", "Forensic Case Analysis"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("PARK CITY RESIDENT", "Suburban Neighbor"),
                     "N2": ("KERRI RAWSON", "Daughter of Dennis Rader")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "PARK CITY RESIDENT", "N2": "KERRI RAWSON"},
        # JA: phải có roles_ja/sub_tags_ja — nếu thiếu thì badge vai rơi về nhãn
        # chung ("証人"/"視聴者") chứ không phải tên vai của tập này.
        "roles_ja": {"H": ("ホスト", "ナレーター"), "D": ("捜査官", "事件記録 Rader"),
                     "C": ("心理学者", "犯罪心理学"),
                     "N1": ("パークシティ住民", "郊外の隣人"),
                     "N2": ("ケリー・ローソン", "デニス・レイダーの実娘")},
        "sub_tags_ja": {"H": "ホスト", "D": "捜査官", "C": "心理学者",
                        "N1": "住民", "N2": "娘"},
        # KO: tên vai lấy theo chính kịch bản KO (Park City 주민 / Kerri Rawson)
        "roles_ko": {"H": ("호스트", "내레이터"), "D": ("수사관", "사건 기록 Rader"),
                     "C": ("심리학자", "범죄심리학"),
                     "N1": ("Park City 주민", "교외 이웃"),
                     "N2": ("Kerri Rawson", "Dennis Rader의 친딸")},
        "sub_tags_ko": {"H": "호스트", "D": "수사관", "C": "심리학자",
                        "N1": "주민", "N2": "Rawson"},
        "cards_en": (
            ("ABOUT THIS DOCUMENTARY", [
                [("Educational content:", 1),
                 (" A forensic & criminal psychology analysis based strictly on public records, "
                  "trial exhibits, and official police interrogation transcripts.", 0)],
                [("Investigative purpose:", 1),
                 (" Produced solely for educational, criminological, and public safety awareness.", 0)],
                [("No defamation:", 1),
                 (" Not intended to defame, harass, or inflict distress upon any innocent individuals "
                  "or victims’ families.", 0)]]),
            ("VIEWER DISCRETION & ADVISORY", [
                [("Mature audience only:", 1),
                 (" Contains mature themes, discussions of serial homicide, and non-graphic "
                  "accounts of violent crime. Viewer discretion is advised.", 0)],
                [("AI & Dramatization:", 1),
                 (" Narrated with synthetic AI voices. Visuals and character avatars are dramatized "
                  "illustrations and do not depict real persons.", 0)],
                [("Professional boundaries:", 1),
                 (" Not a substitute for professional legal, medical, or psychiatric advice.", 0)]])),
        "cast": None,
        # A7 + A11 #64 (bản EN, 04/11/2026): đo master mp3 EN Tap05 = true peak −1,9 dBFS
        # / I −16,3 LUFS. Trần mặc định 0,7943 (−2,00 dBFS) cao hơn đỉnh master chỉ 0,1 dB
        # ⇒ limiter gần như không kích hoạt, còn AAC dựng lại vọn true peak lên ~0,1–0,6 dB
        # ⇒ có thể vượt trần A7 −1,5 dBFS. Dùng CÙNG chuỗi đã chứng minh cho EN/JA
        # (Tap03): limit=0,63 (−4 dBFS) + latency=1 (bù trễ 4,98 ms của limiter ⇒ lệch A/V ≈ 0 ms).
        # KHÔNG đụng chuỗi VN (đã xuất).
        "mux_af": ("alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1" if (EN or JA) else
                   "alimiter=limit=0.7943:attack=5:release=50:level=disabled"),
    },
    "06": {
        "script": WORK / ("script_tap06_EN.json" if EN else
                          "script_tap06_JA.json" if JA else
                          "script_tap06_KO.json" if KO else "script_tap06.json"),
        "dir": "Tap06_EN" if EN else "Tap06_JA" if JA else "Tap06_KO" if KO else "Tap06",
        "plan": "KeHoach_Video_Tap06_EN.md" if EN else
                "KeHoach_Video_Tap06_JA.md" if JA else
                "KeHoach_Video_Tap06_KO.md" if KO else "KeHoach_Video_Tap06.md",
        "master": "Tap06_EN_master" if EN else "Tap06_JA_master" if JA else
                  "Tap06_KO_master" if KO else "Tap06_master",
        "srt": "Tap06_EN.srt" if EN else "Tap06_JA.srt" if JA else
               "Tap06_KO.srt" if KO else "Tap06.srt",
        "intro": "intro_kenh_EN_t06.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.09": "N1", "4.05": "N2"},
        "acting": WORK / ("acting_tap06_EN.json" if EN else
                          "acting_tap06_JA.json" if JA else "acting_tap06.json"),
        "sfx_sheet": WORK / "sfx_tap06.json",
        "act1_cue": "1.06", "silence_cue": "1.05", "click_cues": ("1.08", "4.03"),
        "bed": {1: "bgm_piano_minimal.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_sub_drone.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        # H9: nen sang o dai chu -> them lop toi mem (do bang _t06_scan_contrast.py)
        "text_scrim": ["1-01", "1-09", "1-19", "1-20", "1-28", "1-31", "1-33", "2-01",
                       "2-02", "2-06", "2-07", "2-12", "2-17", "2-26", "3-01", "3-20",
                       "4-02", "4-07", "4-16", "5-05", "5-13", "5-15", "5-17"],
        "thumb": (("THE CLOWN'S SMILE", "& 29 SECRETS") if EN else
                  ("道化師の微笑みと", "床下の29の秘密") if JA else
                  ("광대의 미소와", "29개의 비밀") if KO else
                  ("NỤ CƯỜI CHÚ HỀ", "29 BÍ MẬT DƯỚI SÀN")),
        "thumb_bg": "t6_clown_mirror_chiaroscuro",
        "title": ("Ep. 06: The Killer Clown’s Smile & 29 Secrets Under the Floor | Criminal Psychology: John Wayne Gacy (ASPD & Malignant Narcissism)"
                  if EN else
                  "第06話 · 道化師の微笑みと床下の29の秘密 | 犯罪心理学：ジョン・ウェイン・ゲイシー事件 (反社会性人格障害と悪性自己愛)"
                  if JA else
                  "06화 · 광대의 미소와 바닥 아래 29개의 비밀 | 범죄심리학: 존 웨인 게이시 사건 (반사회적 성격장애와 악성 자기애)"
                  if KO else
                  "Tập 06: Nụ Cười Chú Hề & 29 Bí Mật Dưới Sàn Nhà | Tâm lý học tội phạm: John Wayne Gacy (ASPD & Ái Kỷ Ác Tính)"),
        "act_titles": ({1: "Act 1 · The Photograph with the First Lady and the Pharmacy Boy",
                        2: "Act 2 · The Crime Scene & The Escalation Trajectory of the Abyss",
                        3: "Act 3 · Psychological Autopsy — Compartmentalization & The Summerdale Void",
                        4: "Act 4 · The Interrogation Duel & The Collapse of the Multiple Personality Defense",
                        5: "Act 5 · The Verdict, Psychological Sentence & Survival Red Flags"}
                       if EN else
                       {1: "第1幕 · 大統領夫人との写真と薬局の少年",
                        2: "第2幕 · 現場と犯行記録――深淵のエスカレーション軌道",
                        3: "第3幕 · 心理の深層解剖――精神の分断とサマーデールの空隙",
                        4: "第4幕 · 取調の攻防――多重人格劇の崩壊と法の審判",
                        5: "第5幕 · 判決、心理的結末と生存の警告"}
                       if JA else
                       {1: "제1막 · 영부인과의 사진과 약국의 소년",
                        2: "제2막 · 현장과 범죄 기록 – 심연의 에스컬레이션 궤적",
                        3: "제3막 · 심리 부검 – 인지적 구획화와 서머데일의 심연",
                        4: "제4막 · 심문실 안의 심리전 – 다중인격 연극의 붕괴와 법의 심판",
                        5: "제5막 · 판결, 심리적 종말과 생존을 위한 경고"}
                       if KO else
                       {1: "Hồi 1 · Bức ảnh với Đệ nhất phu nhân và cậu bé hiệu thuốc",
                        2: "Hồi 2 · Hiện trường & Quỹ đạo leo thang của vực thẳm",
                        3: "Hồi 3 · Giải phẫu tâm lý — Sự chia ngăn nhận thức & Khoảng tối Summerdale",
                        4: "Hồi 4 · Đấu trí thẩm vấn & Sụp đổ vở kịch đa nhân cách",
                        5: "Hồi 5 · Phán quyết, bản án tâm lý & bài học cảnh báo đỏ sinh tồn"}),
        "hashtags": "#TrueCrime #CriminalPsychology #JohnWayneGacy #TheKillerClown #ForensicPsychology #Documentary #AmberEyes #TamLyToiPham #PhamVan #HoiTo",
        "summary": ("1.02#1", "3.10#4"),
        "need": ["1.02#1", "1.02#2", "1.02#4", "1.02#5", "1.02#6", "1.02#7", "1.02#8",
                 "1.06#1", "1.06#2", "1.06#3", "1.06#4", "1.06#6", "1.06#7",
                 "1.08#1", "1.08#3", "1.08#6", "1.09#1",
                 "1.09#2", "1.11#2", "1.13#1", "1.14#2", "1.16#1", "2.03#1", "2.03#2",
                 "2.03#3", "2.03#4", "2.04#1", "2.04#2", "2.04#3", "2.04#4", "2.04#5",
                 "2.04#6", "2.04#7", "2.05#2", "2.07#3",
                 "2.07#4", "2.07#5", "2.07#6", "2.08#1", "2.08#2", "2.08#3", "2.09#3",
                 "2.09#4", "2.09#7", "2.10#3", "2.10#4", "2.10#7", "2.10#8", "2.11#1",
                 "2.11#2", "2.12#1", "2.12#2", "3.02#1",
                 "3.02#2", "3.03#1", "3.03#2", "3.03#3", "3.06#1", "3.06#2", "3.08#1",
                 "3.08#2", "3.08#3", "3.10#1", "3.10#2", "3.10#4", "3.10#6", "3.10#7",
                 "3.11#3", "3.11#4", "3.11#9", "3.11#12", "3.11#13",
                 "3.12#1", "4.03#2", "4.03#3", "4.05#1",
                 "4.05#2", "4.05#3", "4.05#4", "4.06#1", "4.07#1", "4.07#2", "4.07#3",
                 "4.07#4", "4.08#1", "4.09#2", "4.09#4", "4.10#1", "4.10#2", "4.11#1",
                 "4.11#3", "4.11#4", "5.02#1", "5.02#3", "5.02#4",
                 "5.04#1", "5.04#2", "5.06#4", "5.06#5", "5.06#6", "5.06#8"],
        "case": "Gacy",
        "n1": (("KIM BYERS", "Pharmacy coworker", "KIM") if EN else
               ("KIM BYERS", "Nhân viên hiệu thuốc", "KIM")),
        "n2": (("MIKE ALBRECHT", "Des Plaines surveillance officer", "ALBRECHT") if EN else
               ("MIKE ALBRECHT", "Sĩ quan theo dõi Des Plaines", "ALBRECHT")),
        "cast": None,
        "cast_ko": True,
        "mux_af": ("alimiter=limit=0.63:attack=5:release=50:level=disabled:latency=1" if EN else
                   "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1"),
        "voice_credit": "This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio",
    },
    "07": {
        "script": WORK / ("script_tap07_EN.json" if EN else "script_tap07.json"),
        "dir": "Tap07_EN" if EN else "Tap07",
        "plan": "KeHoach_Video_Tap07_EN.md" if EN else "KeHoach_Video_Tap07.md",
        "master": "Tap07_EN_master" if EN else "Tap07_master",
        "srt": "Tap07_EN.srt" if EN else "Tap07.srt",
        "intro": "intro_kenh_EN_t07.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.07": "N1", "4.03": "N2"},
        # 06/11/2026: badge vai cho bản EN/JA. Mặc định của edition.py là của
        # Tập 01 ("Blanchard case file" / "SPRINGFIELD RESIDENT") — sai với vụ
        # án Carter, nên phải khai riêng (giống Tập 02 / 04 / 05 / 06).
        "roles_en": {"H": ("HOST", "Your Narrator"),
                     "D": ("INVESTIGATOR", "Carter Case File"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("LYNN ROY", "Victim's Mother"),
                     "N2": ("SAMANTHA BOARDMAN", "Witness Testimony")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "LYNN ROY", "N2": "BOARDMAN"},
        "roles_ja": {"H": ("ホスト", "ナレーター"),
                     "D": ("捜査官", "事件記録 Carter"),
                     "C": ("心理学者", "犯罪心理学"),
                     "N1": ("リン・ロイ", "被害者の母"),
                     "N2": ("サマンサ・ボードマン", "証言")},
        "sub_tags_ja": {"H": "ホスト", "D": "捜査官", "C": "心理学者",
                        "N1": "ロイ", "N2": "ボードマン"},
        "acting": WORK / ("acting_tap07_EN.json" if EN else "acting_tap07.json"),
        "sfx_sheet": WORK / ("sfx_tap07_EN.json" if (EN and (WORK / "sfx_tap07_EN.json").exists()) else "sfx_tap07.json"),
        "act1_cue": "1.12", "silence_cue": "1.04", "click_cues": ("1.02", "4.08"),
        "bed": {1: "bgm_piano_minimal.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_cello_sad.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        # H9: lớp tối mềm sau chữ — các shot có nền sáng làm chữ "chìm".
        # Đo bằng `_t07/_t07_scan_contrast.py` (ngưỡng >8% nét chữ bị chìm),
        # gộp cả 3 ngôn ngữ (HỢP: shot chìm ở bất kỳ ngôn ngữ nào).
        # 09/11/2026: đo lại sau khi bảng shot dựng mới (203 dòng / 198 shot nội dung)
        # ⇒ HỢP 3 ngôn ngữ = 57 shot cần lớp tối mềm; đo lại sau khi bật ⇒ 0 shot chữ chìm.
        "text_scrim": [
      "1-01",
      "1-06",
      "1-29",
      "1-33",
      "1-34",
      "1-35",
      "1-37",
      "1-38",
      "1-40",
      "1-43",
      "1-44",
      "1-45",
      "1-47",
      "2-12",
      "2-13",
      "2-16",
      "2-17",
      "2-18",
      "2-20",
      "2-22",
      "2-24",
      "2-25",
      "2-26",
      "2-30",
      "2-39",
      "2-40",
      "2-41",
      "2-43",
      "2-44",
      "3-01",
      "3-02",
      "3-05",
      "3-06",
      "3-09",
      "3-10",
      "3-13",
      "3-14",
      "3-22",
      "3-24",
      "3-25",
      "3-26",
      "3-28",
      "3-29",
      "3-33",
      "3-37",
      "3-38",
      "3-39",
      "3-41",
      "3-42",
      "4-04",
      "4-07",
      "4-08",
      "4-11",
      "4-13",
      "4-16",
      "4-17",
      "4-20",
      "4-28",
      "4-30",
      "4-32",
      "4-35",
      "4-36",
      "4-40",
      "5-22",
      "5-36",
        ],
        # 09/11/2026: thẻ giới thiệu nhân vật (first-appearance card) mặc định nằm
        # ở (490, H-250) ⇒ TRÙNG khối chữ T1 ở đáy khung (chữ "HOST" đè câu đầu).
        # Tập 07 đặt thẻ lên cao (trên vai bán thân) ⇒ không còn chữ đè chữ.
        # Tập khác không khai ⇒ giữ nguyên vị trí cũ (hồi quy Tập 01: hash không đổi).
        "intro_card_pos": (490, 250),
        # thẻ giới thiệu có nền tối (đọc được trên nền sáng)
        "intro_card_panel": True,
        # giữ thẻ giới thiệu đặc (mờ) tới hết 4,2 s rồi mới mờ trong 0,4 s
        "intro_card_hold": 5.8,
        # T7 tuyến đường (shot 2-06 = câu 2.02#6): ghim tên 2 địa điểm trên
        # cung đường Plainville <-> Mattapoisett (35 dặm, chưa đầy 1 giờ lái xe).
        # 09/11/2026: id đổi theo bảng shot mới (2-02 -> 2-06).
        "route_pins": {"2-06": ("Plainville", "Mattapoisett")},
        "thumb": ("BẢN ÁN GIẾT NGƯỜI", "BẰNG TIN NHẮN"),
        # H11: thumbnail phải mang nền CỦA TẬP NÀY (Tập 02 từng dùng nhà của Tập 01)
        "thumb_bg": "t7_confession_text_timestamp",
        # A11 #64: latency=1 bù trễ của alimiter khi ghép (không có = lệch 4,98 ms)
        "mux_af": "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1",
        # QUY_TAC_AUDIO_HIGGS §2: bắt buộc ghi công Higgs trong mô tả YouTube
        "voice_credit": "This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio",
        "title": "Tập 07: Bản Án Giết Người Bằng Tin Nhắn | Tâm lý học tội phạm: Michelle Carter (Nhân cách kịch tính)",
        "act_titles": {1: "Hồi 1 · Buổi sáng định mệnh tại bãi đỗ xe Kmart", 2: "Hồi 2 · Mê cung hai mươi nghìn dòng tin nhắn",
                       3: "Hồi 3 · Vở kịch cô bạn gái đau khổ & bộ não ái kỷ kịch tính", 4: "Hồi 4 · Dòng tin nhắn đầy tội lỗi và bản án lịch sử",
                       5: "Hồi 5 · Đạo đức không gian số & Đạo luật Conrad"},
        # Hashtag dòng cuối mô tả YouTube (bản tiếng Việt). Bản EN có sẵn trong
        # CHU_CO_DINH_EN.md; bản JA/KO chưa có dòng hashtag.
        "hashtags": "#TrueCrime #CriminalPsychology #MichelleCarter #ConradRoy #DigitalForensics #Documentary #AmberEyes #TamLyToiPham #PhamVan #HoiTo",
        "summary": ("1.02#1", "3.04#1"),
        "need": [
      "1.04#1",
      "1.06#1",
      "1.10#1",
      "1.11#1",
      "1.04#2",
      "1.07#2",
      "1.06#3",
      "1.09#3",
      "1.10#3",
      "1.06#5",
      "1.06#8",
      "2.02#1",
      "2.03#1",
      "2.05#1",
      "2.08#1",
      "2.02#2",
      "2.03#2",
      "2.05#2",
      "2.08#2",
      "2.09#2",
      "2.03#3",
      "2.06#3",
      "2.09#3",
      "2.02#4",
      "2.03#4",
      "2.05#4",
      "2.09#4",
      "2.02#6",
      "2.05#6",
      "2.08#6",
      "3.03#1",
      "3.04#1",
      "3.06#1",
      "3.09#1",
      "3.03#2",
      "3.04#2",
      "3.06#2",
      "3.07#2",
      "3.08#2",
      "3.02#3",
      "3.04#3",
      "3.06#3",
      "3.07#3",
      "3.09#3",
      "3.02#4",
      "3.04#4",
      "3.06#4",
      "3.08#4",
      "3.03#5",
      "3.06#5",
      "3.07#5",
      "3.07#6",
      "4.03#1",
      "4.05#1",
      "4.07#1",
      "4.08#1",
      "4.09#1",
      "4.05#2",
      "4.06#2",
      "4.07#2",
      "4.08#2",
      "4.02#3",
      "4.03#3",
      "4.05#3",
      "4.08#3",
      "4.09#3",
      "4.06#4",
      "4.07#4",
      "4.02#5",
      "4.05#5",
      "4.06#5",
      "4.08#5",
      "4.08#6",
      "5.02#1",
      "5.03#4",
      "5.04#4",
      "5.03#6",
      "5.04#6",
      "5.02#8",
      "5.04#8",
      "5.02#9",
      "5.04#10",
      "5.02#12",
      "5.04#14",
      "5.04#15",
      "5.04#17",
        ],
        # 03/11/2026: 56 moc du lieu da doi chieu nguon cong khai (bang nguon:
        # 02_SAN_XUAT/Tap07/nguon_tham_khao.md — 54 nguon). Truoc do rong => package.py ghi
        # bang "can bo sung" rong va mo ta thieu muc NGUON THAM KHAO.
        "case": "Carter", "n1": ("BÀ LYNN ROY", "Mẹ của nạn nhân", "BÀ ROY"),
        "n2": ("SAMANTHA BOARDMAN", "Bạn thân của Michelle", "SAMANTHA"),
        "cast": None,
    },
    "08": {
        "script": WORK / ("script_tap08_EN.json" if EN else "script_tap08.json"),
        "dir": "Tap08_EN" if EN else "Tap08",
        "plan": "KeHoach_Video_Tap08_EN.md" if EN else "KeHoach_Video_Tap08.md",
        "master": "Tap08_EN_master" if EN else "Tap08_master",
        "srt": "Tap08_EN.srt" if EN else "Tap08.srt",
        "intro": "intro_kenh_EN_t08.mov" if EN else "intro_kenh.mov",
        "n_element": {"1.07": "N1", "4.08": "N2"},
        "acting": WORK / ("acting_tap08_EN.json" if EN else "acting_tap08.json"),
        "sfx_sheet": WORK / ("sfx_tap08_EN.json" if (EN and (WORK / "sfx_tap08_EN.json").exists()) else "sfx_tap08.json"),
        "act1_cue": "1.01", "silence_cue": "1.05", "click_cues": ("1.02", "4.09"),
        "bed": {1: "bgm_piano_minimal.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_sub_drone.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        # H9: lớp tối mềm sau chữ — các shot có nền sáng làm chữ "chìm".
        # Đo bằng `_t08/_t08_scan_contrast.py` (ngưỡng >8% nét chữ bị chìm),
        # gộp cả 3 ngôn ngữ (HỢP: shot chìm ở bất kỳ ngôn ngữ nào).
        # 09/11/2026: đo sau khi bảng shot dựng lại (223 dòng / 218 shot nội dung)
        # ⇒ 43 shot cần lớp tối mềm (VI 0 · EN 0 · JA 1).
        "text_scrim": [
      "1-02",
      "1-09",
      "1-31",
      "1-33",
      "1-36",
      "1-39",
      "1-41",
      "2-17",
      "2-23",
      "2-36",
      "3-07",
      "3-10",
      "3-17",
      "3-19",
      "3-25",
      "3-27",
      "3-31",
      "3-35",
      "3-36",
      "3-38",
      "3-40",
      "3-42",
      "3-44",
      "4-04",
      "4-07",
      "4-08",
      "4-18",
      "4-19",
      "4-20",
      "4-21",
      "4-22",
      "4-24",
      "4-25",
      "4-26",
      "4-37",
      "4-39",
      "4-42",
      "4-43",
      "5-09",
      "5-20",
      "5-22",
      "5-37",
      "5-41",
        ],
        "intro_card_pos": [490, 250],
        "intro_card_panel": True,
        "intro_card_hold": 5.8,
        "route_pins": {},
        "thumb": ("WHEN GENIUSES", "ARE BRAINWASHED") if EN else ("洗脳された", "天才たち") if JA else ("KHI THIÊN TÀI", "BỊ TẨY NÃO"),
        "thumb_bg": "t8_frontal_lobe_brain_scan",              # H11: nền CỦA TẬP 08
        "title": "Khi Các Thiên Tài Bị Tẩy Não — Thao túng tâm lý tinh hoa và thảm họa Sarin (vụ Aum Shinrikyo & Shoko Asahara)",
        "act_titles": ({1: "Act 1 · A Fateful Morning Beneath the Streets of Tokyo", 2: "Act 2 · The Base at the Foot of Mount Fuji and the Death Laboratory",
                       3: "Act 3 · The Paradox of Scientific Genius", 4: "Act 4 · Brainwashing and the Poa Doctrine",
                       5: "Act 5 · The Historic Verdict & the Lesson on Free Thought"} if EN else
                       {1: "第1幕 · 東京の地下に訪れた運命の朝", 2: "第2幕 · 富士山の麓の巨大拠点と「死の実験室」",
                       3: "第3幕 · エリートの科学者たちの矛盾", 4: "第4幕 · 洗脳の技術と「ポア」",
                       5: "第5幕 · 歴史的判決と自由思想の教訓"} if JA else
                       {1: "Hồi 1 · Buổi sáng định mệnh dưới lòng đất Tokyo", 2: "Hồi 2 · Khu căn cứ dưới chân núi Phú Sĩ và phòng thí nghiệm tử thần",
                       3: "Hồi 3 · Nghịch lý của các thiên tài khoa học", 4: "Hồi 4 · Ma thuật tẩy não & khái niệm Poa",
                       5: "Hồi 5 · Phán quyết lịch sử & bài học về sự tự do tư tưởng"}),
        "summary": ("1.02#1", "3.04#1"),
        "need": [],
        "case": "Aum", "n1": ("HÀNH KHÁCH TOKYO", "Nhân chứng sống sót", "HÀNH KHÁCH"),
        "n2": ("BÁC SĨ IKUO HAYASHI", "Cựu bác sĩ Aum", "HAYASHI"),
        "roles_en": {'H': ('HOST', 'Your Narrator'), 'D': ('INVESTIGATOR', 'Forensic Case Analysis'), 'C': ('PSYCHOLOGIST', 'Behavioral Dynamics'), 'N1': ('TOKYO COMMUTER', 'Surviving Witness'), 'N2': ('DR. IKUO HAYASHI', 'Former Aum Doctor')},
        "sub_tags_en": {'H': 'HOST', 'D': 'INVESTIGATOR', 'C': 'PSYCHOLOGIST', 'N1': 'COMMUTER', 'N2': 'HAYASHI'},
        "roles_ja": {'H': ('ホスト', 'ナレーター'), 'D': ('捜査官', '事件記録 Aum'), 'C': ('心理学者', '犯罪心理学'), 'N1': ('東京の通勤客', '生存者の証言'), 'N2': ('林郁夫医師', '元オウム医師')},
        "sub_tags_ja": {'H': 'ホスト', 'D': '捜査官', 'C': '心理学者', 'N1': '通勤客', 'N2': '林郁夫'},
        "roles_ko": {'H': ('호스트', '내레이터'), 'D': ('수사관', '사건 기록 Aum'), 'C': ('심리학자', '범죄심리학'), 'N1': ('도쿄 승객', '생존자 증언'), 'N2': ('하야시 이쿠오 의사', '전직 옴진리교 의사')},
        "sub_tags_ko": {'H': '호스트', 'D': '수사관', 'C': '심리학자', 'N1': '승객', 'N2': '하야시'},
        "hashtags": "#AmberEyes #TrueCrime #TamLyToiPham #AumShinrikyo #ShokoAsahara #SarinTokyo #ThaoTungTamLy #10ChiDauTamLy #CanhBaoDo #HoSoToiPham",
        "hashtags_en": "#AmberEyes #TrueCrime #CriminalPsychology #AumShinrikyo #ShokoAsahara #TokyoSarinAttack #CultMindControl #ExistentialVacuum #RedFlags #Documentary",
        "hashtags_ja": "#AmberEyes #TrueCrime #犯罪心理学 #心理分析 #オウム真理教 #麻原彰晃 #地下鉄サリン事件 #マインドコントロール #実存的真空 #プロファイリング",
        "hashtags_ko": "#AmberEyes #TrueCrime #범죄심리학 #옴진리교 #아사하라쇼코 #도쿄지하철사린 #세뇌 #실존적진공 #마인드컨트롤 #레드플래그",
        "cast": None,
    },
    "09": {
        "script": WORK / ("script_tap09_EN.json" if EN else "script_tap09_JA.json" if JA else "script_tap09_KO.json" if KO else "script_tap09.json"),
        "dir": "Tap09_EN" if EN else "Tap09_JA" if JA else "Tap09_KO" if KO else "Tap09",
        "plan": "KeHoach_Video_Tap09_EN.md" if EN else "KeHoach_Video_Tap09_JA.md" if JA else "KeHoach_Video_Tap09_KO.md" if KO else "KeHoach_Video_Tap09.md",
        "master": "Tap09_EN_master" if EN else "Tap09_JA_master" if JA else "Tap09_KO_master" if KO else "Tap09_master",
        "srt": "Tap09_EN.srt" if EN else "Tap09_JA.srt" if JA else "Tap09_KO.srt" if KO else "Tap09.srt",
        "n_element": {"1.07": "N1", "4.05": "N2"},
        "acting": WORK / ("acting_tap09_EN.json" if EN else "acting_tap09_JA.json" if JA else "acting_tap09_KO.json" if KO else "acting_tap09.json"),
        "sfx_sheet": WORK / ("sfx_tap09_EN.json" if (EN and (WORK / "sfx_tap09_EN.json").exists()) else "sfx_tap09_JA.json" if (JA and (WORK / "sfx_tap09_JA.json").exists()) else "sfx_tap09.json"),
        "act1_cue": "1.12", "silence_cue": "1.05", "click_cues": ("1.02", "4.06"),
        "bed": {1: "bgm_guitar_acoustic_60s.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        # H9: lớp tối mềm sau chữ — các shot có nền sáng làm chữ "chìm".
        # Đo bằng `_t09/_t09_scan_contrast.py` (ngưỡng >8% nét chữ bị chìm),
        # gộp cả 3 ngôn ngữ (HỢP: shot chìm ở bất kỳ ngôn ngữ nào).
        # 09/11/2026: nền MiniMax sáng hơn nền procedural ⇒ nhiều shot cần lớp tối mềm.
        # ⇒ 52 shot cần lớp tối mềm (VI 41 · EN 41 · JA 42).
        "text_scrim": [
      "1-06",
      "1-12",
      "1-13",
      "1-14",
      "1-16",
      "1-24",
      "1-27",
      "1-29",
      "1-33",
      "1-35",
      "1-36",
      "2-04",
      "2-10",
      "2-20",
      "2-24",
      "2-27",
      "2-28",
      "2-29",
      "2-33",
      "2-36",
      "2-38",
      "3-03",
      "3-05",
      "3-13",
      "3-17",
      "3-18",
      "3-23",
      "3-24",
      "3-26",
      "3-28",
      "3-32",
      "4-04",
      "4-07",
      "4-08",
      "4-09",
      "4-25",
      "4-26",
      "4-29",
      "4-30",
      "4-32",
      "4-36",
      "4-38",
      "4-39",
      "4-40",
      "4-41",
      "5-01",
      "5-05",
      "5-06",
      "5-09",
      "5-11",
      "5-12",
      "5-14",
        ],
        # 09/11/2026 (Tập 09): thẻ giới thiệu vai đặt ở GÓC TRÊN PHẢI (960,90) +
        # nền tối ⇒ không đè lên khối chữ T1 ở đáy khung (bài học Tập 07) và không
        # đè lên khối lời kể T4 (vốn nằm ở x=470, y≥330 — vị trí cũ của Tập 08
        # làm chữ bị che, xem ảnh tĩnh Tập 08 shot_1-17).
        "intro_card_pos": [960, 90],
        "intro_card_panel": True,
        "intro_card_hold": 5.8,
        "route_pins": {},
        "intro": "intro_kenh_EN.mov" if EN else "intro_kenh.mov",
        "thumb_bg": "t9_cielo_drive_estate_night",
        "thumb": ("THE ART OF", "DEINDIVIDUATION") if EN else ("自我の消去", "マンソン・ファミリー") if JA else ("NGHỆ THUẬT", "XÓA BỎ BẢN NGÃ"),
        "mux_af": "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1",
        "title": 'Tập 09: Nghệ Thuật Xóa Bỏ Bản Ngã | Tâm lý học tội phạm: Charles Manson & Thảm kịch Gia đình Manson (10 Chỉ Dấu Tâm Lý & 5 Nấc Thang Vực Thẳm)',
        "act_titles": {
            1: "Hồi 1 · The Hook & Dấu chấm hết của Mùa hè Tình yêu",
            2: "Hồi 2 · Hiện trường biệt thự & Bóng ma Helter Skelter tại Spahn Ranch",
            3: "Hồi 3 · Giải phẫu tâm lý & Nghệ thuật xóa bỏ bản ngã",
            4: "Hồi 4 · Đấu trí phòng xử án & Trách nhiệm kẻ không chạm tay",
            5: "Hồi 5 · Phán quyết lịch sử, bản án tâm lý & Cảnh báo đỏ sinh tồn",
        },
        "roles_line": "Lời của Điều tra viên, Chuyên gia tâm lý, Cư dân Los Angeles và Linda Kasabian là lời dựng lại dựa trên tư liệu.",
        "hashtags": '#AmberEyes #TrueCrime #TamLyToiPham #CharlesManson #HelterSkelter #MansonFamily #XoaBoBanNga #10ChiDauTamLy #CanhBaoDo #HoSoToiPham',
        "hashtags_en": '#AmberEyes #TrueCrime #CriminalPsychology #CharlesManson #HelterSkelter #MansonFamily #Deindividuation #10PsychologicalIndicators #SurvivalRedFlags #ForensicFiles',
        "hashtags_ja": '#AmberEyes #TrueCrime #犯罪心理学 #心理分析 #チャールズマンソン #マンソンファミリー #自我の消去 #マインドコントロール #プロファイリング #未解決事件',
        "hashtags_ko": '#AmberEyes #TrueCrime #범죄심리학 #찰스맨슨 #맨슨패밀리 #세뇌 #자아지우기 #10대심리지표 #레드플래그 #실화사건',
        "summary": ("1.02#1", "3.02#1"),
        "summary_vn": 'Nước Mỹ cuối thập niên 1960 đang chìm đắm trong cao trào của phong trào Hippie và thông điệp hòa bình của "Mùa hè Tình yêu". Nhưng vào hai đêm đẫm máu tháng 8/1969 tại đồi Beverly và Los Angeles, ảo tưởng ngây thơ ấy sụp đổ hoàn toàn. Năm nạn nhân tại biệt thự 10050 Cielo Drive – trong đó có nữ diễn viên Sharon Tate đang mang thai 8 tháng rưỡi – cùng vợ chồng doanh nhân Leno và Rosemary LaBianca bị tàn sát man rợ. Điều gây rúng động nhất: kẻ chủ mưu không hề chạm tay vào hung khí tại hiện trường. Hắn là Charles Manson, kẻ đã dùng ma túy, âm nhạc và nghệ thuật thao túng tâm lý để biến những thanh niên ưu tú thành công cụ giết người mù quáng.\n\nHồ sơ Charles Manson & Gia đình Manson được giải phẫu qua Hệ sinh thái 10 chỉ dấu tâm lý & hành vi cốt lõi:\n1. DƯ CHẤN XÃ HỘI & NỖI HOANG TƯỞNG TẬP THỂ: Vụ án Sharon Tate chôn vùi kỷ nguyên Hippie; cư dân LA mua súng, thuê chó bảo vệ; phán quyết People v. Anderson (1972) bãi bỏ án tử hình.\n2. VẬT HÓA NẠN NHÂN (OBJECTIFICATION): Xem nạn nhân là "Pigs" và đạo cụ trong ảo tưởng Helter Skelter; khuyết tật Thuyết tâm trí biến tiếng van xin thành chất kích hoạt hưng phấn quyền lực.\n3. CƠ CHẾ CHIA NGĂN (COMPARTMENTALIZATION): Coi môn đồ là "công cụ kéo dài của bản ngã"; ban ngày du ca tại Spahn Ranch, ban đêm thành cỗ máy tàn sát; bi kịch phụ huynh.\n4. BẢN NGÃ ÁI KỶ SỤP ĐỔ (NARCISSISTIC COLLAPSE): Diễn trò ái kỷ tại tòa (khắc chữ X, tấn công thẩm phán); sụp đổ cái tôi và tự thương hại trong tù Corcoran đến khi qua đời 2017.\n5. HỆ THỐNG TỰ BÀO CHỮA (NEUTRALIZATION): Kỹ thuật trung hòa đạo đức (Sykes & Matza): kháng cáo lý tưởng tâm linh, đổ lỗi nhà tù, ngoại hóa trách nhiệm vì không chạm hung khí.\n6. NGÒI NỔ TÂM LÝ & ĐIỂM GÃY: Bị Terry Melcher từ chối hợp đồng âm nhạc sỉ nhục cái tôi; ảo tưởng chiến tranh sắc tộc bế tắc dẫn đến thảm sát tại 10050 Cielo Drive.\n7. SIGNATURE VS. THỦ ĐOẠN MO: MO (cắt dây điện, đồ đen, vũ khí lạnh) biến đổi để che giấu; Signature (chữ máu PIG, RISE, HEALTER SKELTER, dây thừng nối nạn nhân) bất biến.\n8. QUỸ ĐẠO LEO THANG 5 NẤC THANG: 5 nấc leo thang: trộm cắp (1) → giáo phái LSD (2) → Creepy Crawling (3) → sát hại Gary Hinman (4) → thảm sát Cielo Drive & Waverly Drive (5).\n9. HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI: Chiếc áo ngụy trang Hippie giúp kẻ săn mồi đội lốt đạo sư du mục; xã hội chủ quan coi hội nhóm thanh niên chỉ là sự nổi loạn vô hại.\n10. CẢNH BÁO ĐỎ SINH TỒN (GAVIN DE BECKER): 4 tín hiệu nhận diện tà giáo: cảnh giác Love Bombing dồn dập, nhận diện cô lập, chống tư duy nhị nguyên, và giữ vững quyền lương tri.',
        "summary_en": 'In the late 1960s, America was captivated by the counterculture wave and the peaceful idealism of the "Summer of Love." But over two bloodstained nights in August 1969 in the hills of Los Angeles, that innocent delusion was shattered forever. Five victims at 10050 Cielo Drive – including eight-and-a-half-month pregnant actress Sharon Tate – along with Leno and Rosemary LaBianca on Waverly Drive, were brutally slain. The most chilling reality: the mastermind never personally touched a weapon at the scene. He was Charles Manson, a sociopathic narcissist who weaponized LSD, psychological manipulation, and communal isolation to transform ordinary youth into compliant executioners.\n\nAmber eyes dissects the case through our 10-Indicator Behavioral & Psychological Ecosystem:\n1. SOCIAL IMPACT & COLLECTIVE PARANOIA: The Tate-LaBianca murders ended the counterculture era; LA residents bought firearms; set historic legal precedent for mastermind liability & People v. Anderson (1972).\n2. OBJECTIFICATION & DEHUMANIZATION: Victims were treated as "Pigs" and stage props in Helter Skelter; Theory of Mind deficits turned pleas into power arousal.\n3. COMPARTMENTALIZATION & "THE FAMILY": Followers served as extensions of Manson\'s self; daytime communes at Spahn Ranch separated from nighttime slaughter; family heartbreak.\n4. NARCISSISTIC COLLAPSE & SENTENCE: Theatrical narcissism on trial (carving Xs, attacking judge); decades of collapse & pathological self-pity in prison until death in 2017.\n5. TECHNIQUES OF NEUTRALIZATION (SYKES & MATZA): Spiritual loyalties, blaming society and penal system, externalizing guilt ("hands touched no weapon").\n6. PRECIPITATING TRIGGER: Record producer Terry Melcher rejected Manson\'s music, crushing his ego; race war deadlock triggered the slaughter at 10050 Cielo Drive.\n7. SIGNATURE VS. MO: MO (cut phone wires, black clothes, knives, desert flight) adapted; Signature (blood slogans PIG, RISE, HEALTER SKELTER, rope) immutable.\n8. 5-STAGE ESCALATION TRAJECTORY: 5 steps: petty crimes (1) → LSD cult (2) → Creepy Crawling (3) → murdering Gary Hinman (4) → Tate & LaBianca massacres (5).\n9. HALO EFFECT & SOCIETAL BLIND SPOTS: Hippie flower-power counterculture camouflaged a predator; society dismissed communes as harmless youth rebellion.\n10. SURVIVAL RED FLAGS (GAVIN DE BECKER): 4 life-saving signals: beware Love Bombing, recognize isolation, reject us-versus-them dualism, and protect moral autonomy.',
        "summary_ja": '1960年代後半のアメリカは、ヒッピー文化と「愛の夏（Summer of Love）」の平和的理想に酔いしれていました。しかし1969年8月、ビバリーヒルズとロサンゼルスの丘で起きた血塗られた2夜によって、その無邪気な幻想は残酷に打ち砕かれました。妊娠8か月半の女優シャロン・テートを含む10050シエロ・ドライブの5名の犠牲者、そしてレノ＆ローズマリー・ラビアンカ夫妻が命を奪われました。最も戦慄すべき真実は、黒幕自身が現場で凶器に一度も触れていなかったことです。男の名はチャールズ・マンソン。LSDと心理的操作、共同体の孤立化を武器に、普通のエリート青年たちを盲目的な実行犯へと改造したのです。\n\n犯罪心理学ドキュメンタリー『Amber eyes』第09話では、本事件を「10の心理・行動指標」に基づいて解剖します：\n1. 社会的衝撃と集団的偏執病（Collective Paranoia）：ヒッピー時代の終焉と市民の銃器買い占めパニック。首謀者責任の確立と1972年「ピープル対アンダーソン」判例。\n2. 被害者の客体化と非人間化（Objectification）：被害者を「Pigs」や終末戦争の舞台小道具とみなす認知。心の理論の欠陥により命乞いが権力の性的興奮を誘発。\n3. 精神の分断（Compartmentalization）と「ファミリー」：信徒を「肥大化した自己の延長物」とみなす支配構造。牧歌的な昼と夜の冷酷な暗殺者という完全な分断。\n4. 自己愛の完全崩壊（Narcissistic Collapse）と判決：法廷での劇的な自己愛（額のX傷、裁判官襲撃）。刑務所で忘れ去られる中で見せた病的な自己憐憫と2017年の孤独死。\n5. 中和の技術（Techniques of Neutralization）：サイクス＆マッツァの理論に基づく自己正当化（高次の精神的理想への訴求、社会や刑務所への責任転嫁、外在化）。\n6. 心理的トリガーと限界点：音楽プロデューサーのテリー・メルチャーによるレコード契約拒絶が自己愛を粉砕。人種戦争が起きない焦りからシエロ・ドライブを標的に設定。\n7. 署名（Signature）vs 手口（MO）：MO（電話線切断、黒服、刃物、砂漠逃亡）は隠蔽のため変遷したが、署名（壁の「PIG」「RISE」「HEALTER SKELTER」血文字）は不変。\n8. 5段階のエスカレーション軌道：刺激耐性の形成過程：小犯罪（1）→ LSDカルト（2）→ 夜間侵入「クリーピー・クローリング」（3）→ ヒンマン殺害（4）→ テート事件（5）。\n9. 後光効果（Halo Effect）と社会の死角：平和と愛を掲げるヒッピーの隠れ蓑。若者の共同体を無害な反抗と侮った社会の盲点。\n10. サバイバル・レッドフラッグ（ギャビン・ド・ベッカー）：『The Gift of Fear』に基づく4大警告（ラブ・ボンビング警戒、社会的孤立察知、二元論拒絶、良心の自己決定権保持）。',
        "summary_ko": '1960년대 후반의 미국은 히피 반문화와 ‘사랑의 여름(Summer of Love)’이 약속한 평화의 이상에 깊이 빠져 있었습니다. 그러나 1969년 8월, 로스앤젤레스 베벌리 힐스 언덕에서 벌어진 이틀간의 유혈 참극은 그 순진한 환상을 단숨에 산산조각 냈습니다. 임신 8개월 반이었던 여배우 샤론 테이트를 비롯한 10050 시엘로 드라이브의 희생자 5명과 레노·로즈마리 라비안카 부부가 참혹하게 희생되었습니다. 가장 충격적인 사실은 주범이 현장에서 흉기에 손끝 하나 대지 않았다는 점이었습니다. 그의 이름은 찰스 맨슨. LSD와 음악, 정교한 심리적 가스라이팅으로 평범한 청년들을 맹목적인 살인 기계로 개조한 사이코패스적 교주였습니다.\n\n범죄심리학 채널 ‘Amber eyes’ 09화에서는 맨슨 패밀리 사건을 ‘10대 핵심 심리 및 행동 지표’를 통해 입체적으로 해부합니다:\n1. 사회적 충격과 집단적 편집증(Collective Paranoia): 히피 시대의 비극적 종말과 LA 시민들의 총기·경비견 사재기 공포. 빈센트 부글리오시 검사의 교사자 책임 법리 및 1972년 사형 폐지(People v. Anderson) 선례.\n2. 피해자의 객체화와 비인간化(Objectification): 피해자들을 ‘Pigs’이자 헬터 스켈터 종말 환상의 무대 소품으로 전락시킴. 마음 이론의 결함으로 인해 애원의 목소리가 권력적 흥분을 촉발.\n3. 심리적 구획화(Compartmentalization)와 ‘가족’: 신도들을 ‘과대 자아의 연장선’으로 취급. 스판 랜치에서의 목가적인 낮과 밤의 냉혈한 살인자라는 이중생활의 구획화, 부모들의 정체성 붕괴.\n4. 자기애의 완전한 붕괴(Narcissistic Collapse)와 판결: 법정에서의 연극적 자기애(이마의 X자 흉터, 판사 공격 시도). 코코런 교도소에서 잊혀지며 드러난 병적인 자기연민과 2017년 고독사.\n5. 도덕적 중화 기술(Techniques of Neutralization): 사이크스와 마자의 중화 이론(인류 구원이라는 상위 충성심 호소, 사회와 교도소에 대한 책임 전가, ‘직접 죽이지 않았다’는 외재화).\n6. 심리적 방아쇠와 촉발점: 음반 프로듀서 테리 멜처의 계약 거절로 인한 자아의 치명적 상처. 종족 전쟁이 일어나지 않자 멜처가 살던 시엘로 드라이브를 표적으로 선택.\n7. 시그니처(Signature) vs 범행수법(MO): 수법(전화선 절단, 검은 옷, 흉기 은닉, 사막 도주)은 진화했으나, 시그니처(벽에 남긴 PIG, RISE, HEALTER SKELTER 혈서, 밧줄 결박)는 불변.\n8. 5단계 에스컬레이션 궤적: 도파민 불감증에 따른 5단계 파멸: 잡범 및 사기(1) → LSD 히피 공동체(2) → 야간 주거침입 ‘크리피 크롤링’(3) → 게리 힌먼 살해(4) → 시엘로·웨이벌리 드라이브 참극(5).\n9. 후광 효과(Halo Effect)와 사회적 맹점: 자유와 평화를 표방한 히피 문화가 포식자에게 완벽한 위장막을 제공; 청년 공동체를 단순한 방황으로 치부한 기성세대의 안일함.\n10. 서바이벌 레드플래그(개빈 드 베커): 『The Gift of Fear』 원리에 기반한 4대 생존 경고 신호(애정 폭격 경계, 사회적 고립 수법 감지, 흑백논리 거부, 양심의 판단권을 타인에게 넘기지 말 것).',
        "need": [],
        "case": "Manson",
        "n1": ("CƯ DÂN LOS ANGELES", "Nhân chứng thời đại", "CƯ DÂN"),
        "n2": ("LINDA KASABIAN", "Cựu thành viên Gia đình Manson", "KASABIAN"),
        "roles_en": {'H': ('HOST', 'Your Narrator'), 'D': ('INVESTIGATOR', 'Forensic Case Analysis'), 'C': ('PSYCHOLOGIST', 'Behavioral Dynamics'), 'N1': ('LOS ANGELES RESIDENT', 'Witness to History'), 'N2': ('LINDA KASABIAN', 'Former Manson Family Member')},
        "sub_tags_en": {'H': 'HOST', 'D': 'INVESTIGATOR', 'C': 'PSYCHOLOGIST', 'N1': 'RESIDENT', 'N2': 'KASABIAN'},
        "roles_ja": {'H': ('ホスト', 'ナレーター'), 'D': ('捜査官', '事件記録 Manson'), 'C': ('心理学者', '犯罪心理学'), 'N1': ('ロサンゼルス住民', '時代の目撃者'), 'N2': ('リンダ・カサビアン', '元マンソン・ファミリー')},
        "sub_tags_ja": {'H': 'ホスト', 'D': '捜査官', 'C': '心理学者', 'N1': '住民', 'N2': 'カサビアン'},
        "roles_ko": {'H': ('호스트', '내레이터'), 'D': ('수사관', '사건 기록 Manson'), 'C': ('심리학자', '범죄심리학'), 'N1': ('로스앤젤레스 주민', '시대의 목격자'), 'N2': ('린다 카사비안', '전 맨슨 패밀리 일원')},
        "sub_tags_ko": {'H': '호스트', 'D': '수사관', 'C': '심리학자', 'N1': '주민', 'N2': '카사비안'},
        "cast": None,
    },
    "10": {
        # ---- bản tiếng Anh: 11/11/2026 thêm nhánh EN (Tập 10 có đủ 3 ngôn ngữ).
        # Nền `t10_*` là tài sản DÙNG CHUNG mọi ngôn ngữ (H17/A8.1) ⇒ không nhân bản
        # nền theo hậu tố ngôn ngữ, chỉ đổi tên thư mục sản xuất + file kế hoạch.
        "script": WORK / ("script_tap10_EN.json" if EN else "script_tap10.json"),
        "dir": "Tap10_EN" if EN else "Tap10",
        "plan": "KeHoach_Video_Tap10_EN.md" if EN else "KeHoach_Video_Tap10.md",
        "master": "Tap10_EN_master" if EN else "Tap10_master",
        "srt": "Tap10_EN.srt" if EN else "Tap10.srt",
        "n_element": {"1.07": "N1", "4.05": "N2"},
        "acting": WORK / ("acting_tap10_EN.json" if EN else "acting_tap10.json"),
        "sfx_sheet": WORK / "sfx_tap10.json",
        "act1_cue": "1.12", "silence_cue": "1.05", "click_cues": ("1.03", "4.06"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        # H9: lớp tối mềm sau chữ — các shot có nền sáng làm chữ "chìm".
        # Đo bằng `_t10/_t10_scan_contrast.py` (ngưỡng >8% nét chữ bị chìm),
        # gộp cả 3 ngôn ngữ (HỢP: shot chìm ở bất kỳ ngôn ngữ nào).
        # 11/11/2026: nền MiniMax sáng hơn nền procedural ⇒ phải đo lại toàn bộ.
        # ⇒ 9 shot cần lớp tối mềm (VI 8 · EN 8 · JA 8).
                # H9: lớp tối mềm sau chữ — các shot có nền sáng làm chữ "chìm".
        # Đo bằng `_t10/_t10_scan_contrast.py` (ngưỡng >8% nét chữ bị chìm),
        # gộp cả 3 ngôn ngữ (HỢP: shot chìm ở bất kỳ ngôn ngữ nào).
        # 11/11/2026: nền MiniMax sáng hơn nền procedural ⇒ phải đo lại toàn bộ.
        # ⇒ 33 shot cần lớp tối mềm (VI 18 · EN 19 · JA 20).
                # H9: lớp tối mềm sau chữ — các shot có nền sáng làm chữ "chìm".
        # Đo bằng `_t10/_t10_scan_contrast.py` (ngưỡng >8% nét chữ bị chìm),
        # gộp cả 3 ngôn ngữ (HỢP: shot chìm ở bất kỳ ngôn ngữ nào).
        # 11/11/2026: nền MiniMax sáng hơn nền procedural ⇒ phải đo lại toàn bộ.
        # ⇒ 41 shot cần lớp tối mềm (VI 7 · EN 8 · JA 7).
        "text_scrim": [
      "1-04",
      "1-05",
      "1-16",
      "1-17",
      "1-32",
      "1-33",
      "1-34",
      "1-35",
      "1-41",
      "2-08",
      "2-22",
      "2-23",
      "2-25",
      "2-34",
      "2-35",
      "2-36",
      "2-37",
      "2-43",
      "3-05",
      "3-06",
      "3-08",
      "3-14",
      "3-40",
      "4-11",
      "4-27",
      "4-28",
      "4-31",
      "4-32",
      "4-33",
      "4-34",
      "4-35",
      "4-36",
      "5-02",
      "5-03",
      "5-05",
      "5-08",
      "5-12",
      "5-18",
      "5-27",
      "5-28",
      "5-29",
        ]
,
        "route_pins": {},
        "thumb": ("CHIẾC HỘP GỖ", "7 NĂM VÔ HÌNH"),
        "thumb_bg": "t10_wooden_box_under_bed_shadow",
        "title": "Chiếc Hộp Gỗ Dưới Gầm Giường — Sự Bất Lực Tập Nhiễm & Bóng Ma 'The Company' (Hồ Sơ Colleen Stan)",
        "act_titles": {1: "Hồi 1 · Chuyến xe định mệnh và chiếc hộp đen dưới gầm giường", 2: "Hồi 2 · Bảy năm trong bóng tối và sự biến mất của thời gian",
                       3: "Hồi 3 · Nghịch lý ngày về và sự bất lực tập nhiễm", 4: "Hồi 4 · Sự rạn nứt của lồng giam và cuộc giải cứu ngầm",
                       5: "Hồi 5 · Ánh sáng sau bảy năm địa ngục & Sự hồi sinh kỳ diệu"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Colleen", "n1": ("BẠN CỦA COLLEEN", "Nhân chứng thời đại", "BẠN BÈ"),
        "n2": ("JANICE HOOKER", "Đồng phạm kiêm người giải cứu", "JANICE"),
        # ---- bản tiếng Anh: nhãn vai (mặc định của edition.py là của Tập 01
        # "Blanchard case file" / "SPRINGFIELD RESIDENT" -> sai vụ án Stan).
        "roles_en": {"H": ("HOST", "Your Narrator"),
                     "D": ("INVESTIGATOR", "Colleen Stan Case File"),
                     "C": ("PSYCHOLOGIST", "Behavioral Dynamics"),
                     "N1": ("COLLEEN'S FRIEND", "Contemporary Witness"),
                     "N2": ("JANICE HOOKER", "Accomplice and Rescuer")},
        "sub_tags_en": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST",
                        "N1": "FRIEND", "N2": "JANICE"},
        # ---- bản tiếng Nhật: nhãn vai riêng cho Tập 10.
        "roles_ja": {"H": ("ホスト", "ナレーター"),
                     "D": ("捜査官", "事件記録 Colleen"),
                     "C": ("心理学者", "犯罪心理学"),
                     "N1": ("コロleenの友人", "同時代の目撃者"),
                     "N2": ("ジャニス・フッカー", "共犯であり救出者")},
        "sub_tags_ja": {"H": "ホスト", "D": "捜査官", "C": "心理学者",
                        "N1": "友人", "N2": "ジャニス"},
        "cast": None,
    },
    "11": {
        "script": WORK / "script_tap11.json",
        "dir": "Tap11",
        "plan": "KeHoach_Video_Tap11.md",
        "master": "Tap11_master",
        "srt": "Tap11.srt",
        "n_element": {"1.06": "N1", "4.08": "N2"},
        "acting": WORK / "acting_tap11.json",
        "sfx_sheet": WORK / "sfx_tap11.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.06"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("KEN & BARBIE", "THỎA THUẬN VỚI QUỶ DỮ"),
        "title": "Cặp Đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi & Thỏa Thuận Với Quỷ Dữ (Hồ Sơ Paul Bernardo & Karla Homolka)",
        "act_titles": {1: "Hồi 1 · Vỏ bọc hoàn hảo của Cặp đôi Ken & Barbie",
                       2: "Hồi 2 · Hiện trường & Vực thẳm leo thang — 4 nấc thang tội ác",
                       3: "Hồi 3 · Giải mã liên minh bệnh hoạn — Điên cuồng đôi & Trung hòa đạo đức",
                       4: "Hồi 4 · Thỏa thuận với Quỷ dữ & Sự sụp đổ của mặt nạ nạn nhân",
                       5: "Hồi 5 · Phán quyết, di chứng tư pháp & Bài học cảnh báo đỏ"},
        "summary": ("1.03#1", "3.02#1"),
        "need": [],
        "case": "Bernardo", "n1": ("NGƯỜI HÀNG XÓM", "Cư dân Port Dalhousie", "HÀNG XÓM"),
        "n2": ("CÔNG TỐ VIÊN", "Điều tra viên vụ án", "CÔNG TỐ VIÊN"),
        "cast": None,
    },
    "12": {
        "script": WORK / "script_tap12.json",
        "dir": "Tap12",
        "plan": "KeHoach_Video_Tap12.md",
        "master": "Tap12_master",
        "srt": "Tap12.srt",
        "n_element": {"1.07": "N1", "4.10": "N2"},
        "acting": WORK / "acting_tap12.json",
        "sfx_sheet": WORK / "sfx_tap12.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("THẢM KỊCH", "JONESTOWN"),
        "title": "Thảm Kịch Jonestown — Khi 918 Con Người Cùng Bước Vào Chỗ Chết (Hồ Sơ Jim Jones & Peoples Temple)",
        "act_titles": {1: "Hồi 1 · Lời hứa thiên đường và bóng ma nơi rừng sâu", 2: "Hồi 2 · Cuộc phục kích đường băng và tiếng còi báo động định mệnh",
                       3: "Hồi 3 · Giải mã cơ chế tâm lý: Từ phục tùng đến tư duy tập thể", 4: "Hồi 4 · Cuộn băng tử thần Q 042 và tiếng nói phản kháng cô đơn",
                       5: "Hồi 5 · Bài học đắt giá về tâm lý bầy đàn & Lời cảnh tỉnh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Jonestown", "n1": ("LESLIE WAGNER-WILSON", "Cựu thành viên Peoples Temple", "CỰU TÍN ĐỒ"),
        "n2": ("ĐIỀU TRA VIÊN FBI", "Tiếp cận hiện trường Jonestown", "ĐIỀU TRA VIÊN"),
        "cast": None,
    },
    "13": {
        "script": WORK / "script_tap13.json",
        "dir": "Tap13",
        "plan": "KeHoach_Video_Tap13.md",
        "master": "Tap13_master",
        "srt": "Tap13.srt",
        "n_element": {"1.07": "N1", "4.06": "N2"},
        "acting": WORK / "acting_tap13.json",
        "sfx_sheet": WORK / "sfx_tap13.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("CON NHÀ", "NGƯỜI TA"),
        "title": "Vỏ Bọc 'Con Nhà Người Ta' & Lời Nói Dối 10 Năm (Hồ Sơ Jennifer Pan)",
        "act_titles": {1: "Hồi 1 · Vỏ bọc 'Con nhà người ta' và tòa tháp dối lừa mười năm", 2: "Hồi 2 · Đêm kinh hoàng tại đại lộ Helen và cuộc gọi 911",
                       3: "Hồi 3 · Giải mã tâm lý: Từ 'Cha mẹ hổ' đến hội chứng nói dối bệnh lý", 4: "Hồi 4 · Đấu trí phòng thẩm vấn & Sự thức tỉnh của người cha",
                       5: "Hồi 5 · Bản án lương tâm & Lời cảnh tỉnh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Pan", "n1": ("BẠN HỌC", "Bạn thời phổ thông", "BẠN HỌC"),
        "n2": ("HUEI HANN PAN", "Người cha sống sót", "NGƯỜI CHA"),
        "cast": None,
    },
    "14": {
        "script": WORK / "script_tap14.json",
        "dir": "Tap14",
        "plan": "KeHoach_Video_Tap14.md",
        "master": "Tap14_master",
        "srt": "Tap14.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap14.json",
        "sfx_sheet": WORK / "sfx_tap14.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NẠN NHÂN", "GASLIGHTING"),
        "title": "Khi Nạn Nhân Gaslighting Bước Qua Ranh Giới Tội Ác (Hồ Sơ Betty Broderick)",
        "act_titles": {1: "Hồi 1 · Người vợ hy sinh và chiếc bẫy thao túng thực tại", 2: "Hồi 2 · Cuộc chiến pháp lý tàn khốc và sự đứt gãy tâm lý",
                       3: "Hồi 3 · Giải mã tâm lý: Gaslighting, tổn thương ái kỷ & bẫy nạn nhân", 4: "Hồi 4 · Năm phát đạn rạng sáng và phiên tòa chia rẽ nước Mỹ",
                       5: "Hồi 5 · Bài học đắt giá về rủi ro hôn nhân & Lời cảnh tỉnh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Broderick", "n1": ("BẠN THÂN LA JOLLA", "Bạn thân của Betty", "BẠN THÂN"),
        "n2": ("KIM BRODERICK", "Con gái lớn", "CON GÁI"),
        "cast": None,
    },
    "15": {
        "script": WORK / "script_tap15.json",
        "dir": "Tap15",
        "plan": "KeHoach_Video_Tap15.md",
        "master": "Tap15_master",
        "srt": "Tap15.srt",
        "n_element": {"1.07": "N1", "4.06": "N2"},
        "acting": WORK / "acting_tap15.json",
        "sfx_sheet": WORK / "sfx_tap15.json",
        "act1_cue": "1.16", "silence_cue": "1.09", "click_cues": ("1.06",),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("CƠN CUỒNG GHEN", "RANH GIỚI"),
        "title": "Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới — Nỗi Sợ Bị Ruồng Bỏ & Thảm Kịch Phòng Tắm (Hồ Sơ Jodi Arias)",
        "act_titles": {1: "Hồi 1 · Ám ảnh độc hại và thảm kịch trong buồng tắm", 2: "Hồi 2 · Dấu vết kỹ thuật số và chiếc bình xăng bí mật",
                       3: "Hồi 3 · Giải mã tâm lý: Rối loạn nhân cách ranh giới (BPD) & Cơn cuồng nộ ruồng bỏ", 4: "Hồi 4 · Trò ảo thuật phòng thẩm vấn và phiên tòa truyền hình",
                       5: "Hồi 5 · Phán quyết chung thân & 4 cảnh báo đỏ của mối quan hệ ám ảnh"},
        "summary": ("1.03#1", "3.02#1"),
        "need": [],
        "case": "Arias", "n1": ("BẠN THÂN MESA", "Đồng nghiệp của Travis", "BẠN THÂN"),
        "n2": ("BỒI THẨM ĐOÀN", "Hạt Maricopa", "BỒI THẨM"),
        "cast": None,
    },
    "16": {
        "script": WORK / "script_tap16.json",
        "dir": "Tap16",
        "plan": "KeHoach_Video_Tap16.md",
        "master": "Tap16_master",
        "srt": "Tap16.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap16.json",
        "sfx_sheet": WORK / "sfx_tap16.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_church_organ.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("ĐƯA LÊN", "THIÊN ĐÀNG"),
        "title": "Kẻ Tước Đoạt Mạng Sống Cả Gia Đình Để 'Đưa Họ Lên Thiên Đàng' (Hồ Sơ John List)",
        "act_titles": {1: "Hồi 1 · Biệt thự u ám Breeze Knoll và khám phá kinh hoàng sau một tháng", 2: "Hồi 2 · Vụ mất tích thế kỷ và chiếc kéo cắt mặt trong album ảnh",
                       3: "Hồi 3 · Giải mã tâm lý: Rối loạn nhân cách ám ảnh cưỡng chế (OCPD) & Bẫy ngụy biện đạo đức", 4: "Hồi 4 · Bức tượng sáp của Frank Bender và cú điện thoại từ America's Most Wanted",
                       5: "Hồi 5 · Bài học đắt giá về sự cuồng kiểm soát & 4 cảnh báo đỏ"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "List", "n1": ("JEAN PHILLIPS", "Giáo viên dạy kịch", "GIÁO VIÊN"),
        "n2": ("WANDA FLANERY", "Hàng xóm tại Colorado", "HÀNG XÓM"),
        "cast": None,
    },
    "17": {
        "script": WORK / "script_tap17.json",
        "dir": "Tap17",
        "plan": "KeHoach_Video_Tap17.md",
        "master": "Tap17_master",
        "srt": "Tap17.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap17.json",
        "sfx_sheet": WORK / "sfx_tap17.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NGỤC TÙ", "NGOẠI Ô"),
        "title": "13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Kiểm Soát Cưỡng Chế & Cú Nhảy Sinh Tồn (Hồ Sơ Gia Đình Turpin)",
        "act_titles": {1: "Hồi 1 · Cú nhảy qua cửa sổ rạng sáng và cuộc gọi 911 từ chiếc điện thoại hỏng", 2: "Hồi 2 · Ngục tù ngoại ô và vỏ bọc hoàn hảo của gia đình kiểu mẫu",
                       3: "Hồi 3 · Giải mã tâm lý: Kiểm soát cưỡng chế, ảo tưởng điên cuồng đôi & sự ấu trĩ hóa nạn nhân", 4: "Hồi 4 · Bản cáo trạng rúng động và phiên tòa đối diện công lý",
                       5: "Hồi 5 · Hành trình tái sinh từ tro tàn & 4 cảnh báo đỏ về bạo hành gia đình kín"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Turpin", "n1": ("TRỰC TỔNG ĐÀI 911", "Tổng đài viên Hạt Riverside", "TỔNG ĐÀI"),
        "n2": ("ĐẠI DIỆN Y TẾ", "Bác sĩ Bệnh viện Riverside", "BÁC SĨ"),
        "cast": None,
    },
    "18": {
        "script": WORK / "script_tap18.json",
        "dir": "Tap18",
        "plan": "KeHoach_Video_Tap18.md",
        "master": "Tap18_master",
        "srt": "Tap18.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap18.json",
        "sfx_sheet": WORK / "sfx_tap18.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NGÀY TẬN THẾ", "DOOMSDAY MOM"),
        "title": "Lời Tiên Tri Ngày Tận Thế & Ảo Tưởng Ma Quỷ (Hồ Sơ Lori Vallow & Chad Daybell)",
        "act_titles": {1: "Hồi 1 · Bãi biển Hawaii và bí ẩn hai đứa trẻ biến mất", 2: "Hồi 2 · Mảnh đất nông trại và bí mật dưới lòng đất",
                       3: "Hồi 3 · Giải mã tâm lý: Hoang tưởng tôn giáo chia sẻ & cơ chế phi nhân tính hóa", 4: "Hồi 4 · Bản án trần thế và phán quyết tử hình",
                       5: "Hồi 5 · Nỗi đau đọng lại & 4 cảnh báo đỏ về các hội nhóm cuồng tín"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Vallow", "n1": ("KAY WOODCOCK", "Bà nội của bé JJ", "BÀ NỘI"),
        "n2": ("BỒI THẨM ĐOÀN", "Hạt Ada, Idaho", "BỒI THẨM"),
        "cast": None,
    },
    "19": {
        "script": WORK / "script_tap19.json",
        "dir": "Tap19",
        "plan": "KeHoach_Video_Tap19.md",
        "master": "Tap19_master",
        "srt": "Tap19.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap19.json",
        "sfx_sheet": WORK / "sfx_tap19.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_sub_drone.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("MÀN KỊCH", "CON QUỶ"),
        "title": "Màn Kịch 'Con Quỷ Trong Đầu' — Giả Bệnh Tâm Thần & Sự Thật Trước Máy Quay (Hồ Sơ Nikolas Cruz)",
        "act_titles": {1: "Hồi 1 · Căn phòng hỏi cung và lời nói dối về 'con quỷ'", 2: "Hồi 2 · Chiếc máy quay không chớp mắt và khoảnh khắc chiếc mặt nạ rơi xuống",
                       3: "Hồi 3 · Giải mã tâm lý: Giả bệnh tâm thần (Malingering) vs. Loạn thần thực sự", 4: "Hồi 4 · Bản án 34 án chung thân và sự phán xét của công lý",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa bạo lực học đường"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Cruz", "n1": ("HỌC SINH PARKLAND", "Sống sót thảm kịch", "HỌC SINH"),
        "n2": ("BỒI THẨM ĐOÀN", "Hạt Broward, Florida", "BỒI THẨM"),
        "cast": None,
    },
    "20": {
        "script": WORK / "script_tap20.json",
        "dir": "Tap20",
        "plan": "KeHoach_Video_Tap20.md",
        "master": "Tap20_master",
        "srt": "Tap20.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap20.json",
        "sfx_sheet": WORK / "sfx_tap20.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("KHOẢNH KHẮC", "SỤP ĐỔ"),
        "title": "Khoảnh Khắc Sụp Đổ Trước Ống Kính — Ám Ảnh Rình Rập & Phản Ứng Đóng Băng Kỳ Dị (Hồ Sơ Stephen McDaniel)",
        "act_titles": {1: "Hồi 1 · Cuộc phỏng vấn định mệnh & tin báo bất ngờ từ thùng rác", 2: "Hồi 2 · Bức tượng đá trong phòng hỏi cung & cú sốc nhận thức",
                       3: "Hồi 3 · Giải mã tâm lý: Kẻ rình rập ngầm & phản ứng đóng băng kỳ dị", 4: "Hồi 4 · Phán quyết chung thân & sự trừng phạt của công lý",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa kẻ rình rập ngầm"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "McDaniel", "n1": ("BẠN HỌC TRƯỜNG LUẬT", "Hàng xóm Barristers Hall", "BẠN HỌC"),
        "n2": ("ĐẠI DIỆN GIA ĐÌNH", "Chị gái của Lauren Giddings", "GIA ĐÌNH"),
        "cast": None,
    },
    "21": {
        "script": WORK / "script_tap21.json",
        "dir": "Tap21",
        "plan": "KeHoach_Video_Tap21.md",
        "master": "Tap21_master",
        "srt": "Tap21.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap21.json",
        "sfx_sheet": WORK / "sfx_tap21.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("LOẠN THẦN", "SAU SINH"),
        "title": "Bi Kịch Của Cơn Loạn Thần Sau Sinh — Khi Ảo Giác Đánh Cắp Thiên Chức Làm Mẹ (Hồ Sơ Andrea Yates)",
        "act_titles": {1: "Hồi 1 · Cuộc gọi 911 rạng sáng & ngôi nhà im lìm tại Houston", 2: "Hồi 2 · Vực thẳm của sự cô độc & tiếng chuông cảnh báo bị phớt lờ",
                       3: "Hồi 3 · Giải mã tâm lý: Loạn thần sau sinh (Psychosis) & hoang tưởng cứu chuộc", 4: "Hồi 4 · Phiên tòa lịch sử & phán quyết Không có tội vì lý do tâm thần",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện Loạn thần sau sinh"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Yates", "n1": ("HÀNG XÓM CLEAR LAKE", "Cư dân Houston, Texas", "HÀNG XÓM"),
        "n2": ("BỒI THẨM ĐOÀN", "Tòa án Hạt Harris, Texas", "BỒI THẨM"),
        "cast": None,
    },
    "22": {
        "script": WORK / "script_tap22.json",
        "dir": "Tap22",
        "plan": "KeHoach_Video_Tap22.md",
        "master": "Tap22_master",
        "srt": "Tap22.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap22.json",
        "sfx_sheet": WORK / "sfx_tap22.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NƯỚC MẮT", "CÁ SẤU"),
        "title": "Nước Mắt Cá Sấu Của Kẻ Thuê Sát Thủ Giết Chồng — Thao Túng Trơ Trẽn & Màn Kịch Trước Máy Quay (Hồ Sơ Dalia Dippolito)",
        "act_titles": {1: "Hồi 1 · Màn kịch hiện trường giả & nước mắt người vợ mới cưới", 2: "Hồi 2 · Ván bài lật ngửa & nghệ thuật thao túng trơ trẽn (Gaslighting)",
                       3: "Hồi 3 · Giải mã tâm lý: Sự thao túng trơ trẽn & nhân cách ái kỷ ác tính", 4: "Hồi 4 · Cuộc chiến pháp lý 8 năm & bản án 16 năm tù giam",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện kẻ thao túng trục lợi"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Dippolito", "n1": ("HÀNG XÓM BOYNTON BEACH", "Nhân chứng tại hiện trường", "HÀNG XÓM"),
        "n2": ("BỒI THẨM ĐOÀN", "Tòa án Hạt Palm Beach, Florida", "BỒI THẨM"),
        "cast": None,
    },
    "23": {
        "script": WORK / "script_tap23.json",
        "dir": "Tap23",
        "plan": "KeHoach_Video_Tap23.md",
        "master": "Tap23_master",
        "srt": "Tap23.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap23.json",
        "sfx_sheet": WORK / "sfx_tap23.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NIGHT STALKER", "SAY MÊ KẺ ÁC"),
        "title": "Ám Ảnh 'Night Stalker' & Bí Ẩn Hội Chứng Say Mê Tội Phạm (Hồ Sơ Richard Ramirez)",
        "act_titles": {1: "Hồi 1 · Mùa hè rực lửa 1985 & cơn ác mộng rình rập ban đêm", 2: "Hồi 2 · Phiên tòa cuồng loạn & những người hâm mộ kẻ sát nhân",
                       3: "Hồi 3 · Giải mã tâm lý: Chấn thương não bộ & hội chứng say mê tội phạm (Hybristophilia)", 4: "Hồi 4 · Di sản tư pháp & sự sụp đổ của một ảo tượng",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện hội chứng say mê độc hại"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Ramirez", "n1": ("CƯ DÂN ĐÔNG LOS ANGELES", "Nhân chứng vây bắt năm 1985", "CƯ DÂN"),
        "n2": ("NHÀ BÁO THEO DÕI PHIÊN TÒA", "Tòa Thượng thẩm Los Angeles", "NHÀ BÁO"),
        "cast": None,
    },
    "24": {
        "script": WORK / "script_tap24.json",
        "dir": "Tap24",
        "plan": "KeHoach_Video_Tap24.md",
        "master": "Tap24_master",
        "srt": "Tap24.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap24.json",
        "sfx_sheet": WORK / "sfx_tap24.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("KÝ ỨC", "HWASEONG"),
        "title": "Ký Ức Kẻ Sát Nhân Hwaseong — Sự Thật 33 Năm Dưới Lớp Sương Mù & Lời Thú Tội Muộn Màng (Hồ Sơ Lee Choon-jae)",
        "act_titles": {1: "Hồi 1 · Những cánh đồng đêm Hwaseong & 33 năm trong sương mù", 2: "Hồi 2 · Cuộc đấu trí tại Trại giam Busan & lời tự bạch lạnh gáy",
                       3: "Hồi 3 · Giải mã tâm lý: Kẻ sát nhân kiểm soát quyền lực (Power-Control) & nghịch lý thú tội", 4: "Hồi 4 · Phiên tòa giải oan thế kỷ & lời xin lỗi của công lý",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa tội phạm săn mồi ban đêm"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Lee", "n1": ("CƯ DÂN HWASEONG", "Sống trong nỗi sợ hãi thập niên 1980", "CƯ DÂN"),
        "n2": ("NGƯỜI ĐƯỢC MINH OAN", "Nạn nhân án oan 20 năm", "MINH OAN"),
        "cast": None,
    },
    "25": {
        "script": WORK / "script_tap25.json",
        "dir": "Tap25",
        "plan": "KeHoach_Video_Tap25.md",
        "master": "Tap25_master",
        "srt": "Tap25.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap25.json",
        "sfx_sheet": WORK / "sfx_tap25.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("SÁT NHÂN", "ÁO MƯA"),
        "title": "Sát Nhân Áo Mưa & Cơn Cuồng Nộ Thù Hận Xã Hội — Vỏ Bọc Tự Ti & Tội Ác Đội Lốt Phán Xét (Hồ Sơ Yoo Young-chul)",
        "act_titles": {1: "Hồi 1 · Cơn ác mộng áo mưa vàng & Những bóng ma sau cánh cửa biệt thự Seoul", 2: "Hồi 2 · Cuộc đào tẩu chớp nhoáng & Sự trơ tráo sau chiếc mặt nạ phán xét",
                       3: "Hồi 3 · Giải mã tâm lý: Thù hận xã hội (Sociopathic Resentment) & Cơ chế đổ lỗi ngoại hóa", 4: "Hồi 4 · Bản án tử hình & Phán quyết nghiêm minh của công lý",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện nhân cách thù hận xã hội"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Yoo", "n1": ("CHỦ CƠ SỞ MASSAGE", "Nhân chứng Mapo năm 2004", "MASSAGE"),
        "n2": ("GIA ĐÌNH NẠN NHÂN", "Con trai nạn nhân Sinsa-dong", "GIA ĐÌNH"),
        "cast": None,
    },
    "26": {
        "script": WORK / "script_tap26.json",
        "dir": "Tap26",
        "plan": "KeHoach_Video_Tap26.md",
        "master": "Tap26_master",
        "srt": "Tap26.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap26.json",
        "sfx_sheet": WORK / "sfx_tap26.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NỮ HỘ SINH", "KOTOBUKI"),
        "title": "Nữ Hộ Sinh Kotobuki & Tội Ác Dưới Lớp Vỏ Bọc Từ Thiện — Sự Suy Đồi Đạo Đức & Bi Kịch Hậu Chiến (Hồ Sơ Miyuki Ishikawa)",
        "act_titles": {1: "Hồi 1 · Đêm đông Tokyo 1948 & Chiếc xe kéo bí ẩn trên phố vắng", 2: "Hồi 2 · Đế chế Kotobuki & Đường dây trục lợi từ nỗi tuyệt vọng",
                       3: "Hồi 3 · Giải mã tâm lý: Sự suy đồi đạo đức & Cơ chế tự biện minh hậu chiến", 4: "Hồi 4 · Bản án trước vành móng ngựa & Bước ngoặt thể chế hậu chiến",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ bảo vệ trẻ em trước các cơ sở trục lợi"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Ishikawa", "n1": ("CẢNH SÁT TUẦN TRA", "Đồn Cảnh sát Waseda năm 1948", "TUẦN TRA"),
        "n2": ("NGƯỜI MẸ NẠN NHÂN", "Nạn nhân Nhà hộ sinh Kotobuki", "NGƯỜI MẸ"),
        "cast": None,
    },
    "27": {
        "script": WORK / "script_tap27.json",
        "dir": "Tap27",
        "plan": "KeHoach_Video_Tap27.md",
        "master": "Tap27_master",
        "srt": "Tap27.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap27.json",
        "sfx_sheet": WORK / "sfx_tap27.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("ÁI KỶ TRẢ THÙ", "BÌNH PHƯỚC"),
        "title": "Tổn Thương Ái Kỷ & Thao Túng Đồng Phạm — Cơn Cuồng Nộ Trả Thù Sau Đổ Vỡ Tình Cảm (Hồ Sơ Nguyễn Hải Dương)",
        "act_titles": {1: "Hồi 1 · Buổi sáng định mệnh tại Minh Hưng & Hiện trường biệt thự đẫm máu", 2: "Hồi 2 · Màn kịch tại đám tang & Cuộc đại phá án thần tốc trong 60 giờ",
                       3: "Hồi 3 · Giải mã tâm lý: Tổn thương ái kỷ (Narcissistic Injury) & Nghệ thuật thao túng đồng phạm", 4: "Hồi 4 · Phiên tòa lưu động tại Bình Phước & Bản án nghiêm khắc của pháp luật",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ nhận diện kẻ thao túng, thù hận độc hại"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Duong", "n1": ("NGƯỜI LÀM CÔNG XƯỞNG GỖ", "Nhân chứng phát hiện vụ án", "XƯỞNG GỖ"),
        "n2": ("NHÂN CHỨNG PHIÊN TÒA", "Người theo dõi phiên tòa Bình Phước", "NHÂN CHỨNG"),
        "cast": None,
    },
    "28": {
        "script": WORK / "script_tap28.json",
        "dir": "Tap28",
        "plan": "KeHoach_Video_Tap28.md",
        "master": "Tap28_master",
        "srt": "Tap28.srt",
        "n_element": {"1.07": "N1", "4.09": "N2"},
        "acting": WORK / "acting_tap28.json",
        "sfx_sheet": WORK / "sfx_tap28.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: "bgm_cello_sad.mp3", 2: "bgm_ambient_deep.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("BI KỊCH", "LÊ VĂN LUYỆN"),
        "title": "Cơn Cuồng Loạn Trong Đêm Mưa Bão & Bi Kịch Vị Thành Niên — Sự Trượt Dài Từ Thế Giới Ảo (Hồ Sơ Lê Văn Luyện)",
        "act_titles": {1: "Hồi 1 · Đêm mưa bão tại Phố Sàn & Tiệm vàng im lìm trong buổi sáng định mệnh", 2: "Hồi 2 · Cuộc đại truy lùng xuyên biên giới & Khoảnh khắc bắt giữ tại Na Hình",
                       3: "Hồi 3 · Giải mã tâm lý: Tội phạm vị thành niên & Hội chứng chuột cùng đường", 4: "Hồi 4 · Phiên tòa lịch sử tại Bắc Giang & Nguyên tắc pháp quyền nhân đạo",
                       5: "Hồi 5 · Bài học cảnh tỉnh & 4 cảnh báo đỏ phòng ngừa tội phạm đột nhập ban đêm"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Luyen", "n1": ("NGƯỜI DÂN PHỐ SÀN", "Hàng xóm tiệm vàng Ngọc Bích", "HÀNG XÓM"),
        "n2": ("NHÂN CHỨNG PHIÊN TÒA", "Người theo dõi phiên tòa Bắc Giang", "NHÂN CHỨNG"),
        "cast": None,
    },
    "29": {
        "script": WORK / "script_tap29.json",
        "dir": "Tap29",
        "plan": "KeHoach_Video_Tap29.md",
        "master": "Tap29_master",
        "srt": "Tap29.srt",
        "n_element": {"1.07": "N1", "4.07": "N2"},
        "acting": WORK / "acting_tap29.json",
        "sfx_sheet": WORK / "sfx_tap29.json",
        "act1_cue": "1.10", "silence_cue": "1.06", "click_cues": ("1.03", "4.05"),
        "bed": {1: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 2: "bgm_cello_sad.mp3",
                3: "bgm_piano_minimal.mp3", 4: "bgm_violin_heart.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),
        "route_pins": {},
        "thumb": ("NỖI SỢ", "BỊ BỎ RƠI"),
        "title": "Sát Nhân Từ Nỗi Sợ Bị Bỏ Rơi Bệnh Lý & Ảo Tưởng Kiểm Soát Tuyệt Đối (Hồ Sơ Jeffrey Dahmer)",
        "act_titles": {1: "Hồi 1 · Căn hộ 213 & Khoảnh khắc người sống sót trốn thoát lúc nửa đêm", 2: "Hồi 2 · Cuộc thẩm vấn 60 giờ & Lời thú tội của kẻ cô đơn cùng cực",
                       3: "Hồi 3 · Giải mã tâm lý: Rối loạn nhân cách ranh giới & Ảo tưởng sở hữu", 4: "Hồi 4 · Phiên tòa Milwaukee & Tranh biện: Điên loạn hay Tỉnh táo tàn nhẫn?",
                       5: "Hồi 5 · Bài học cảnh tỉnh xã hội & 4 cảnh báo đỏ nhận diện kẻ săn mồi"},
        "summary": ("1.02#1", "3.02#1"),
        "need": [],
        "case": "Dahmer", "n1": ("TRACY EDWARDS", "Người trốn thoát khỏi căn hộ 213", "EDWARDS"),
        "n2": ("THÂN NHÂN NẠN NHÂN", "Đại diện thân nhân tại tòa Milwaukee", "THÂN NHÂN"),
        "cast": None,
    },
}
if EPN not in EPISODES:
    raise SystemExit(f"Chưa khai báo tập {EPN} trong edition.EPISODES")
EP = EPISODES[EPN]

# ---------------------------------------------------------------- bản tiếng Hàn (KO) & Nhật (JA)
# Kịch bản KO: 01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md  (chuẩn: 00_TIEU_CHUAN/CHU_CO_DINH_KO.md)
# Kịch bản JA: 01_KICH_BAN/TapXX_JA/kichban_tapXX_JA.md  (chuẩn: 00_TIEU_CHUAN/CHU_CO_DINH_JA.md)
# Cùng mã câu với bản VN nên dùng chung được acting_tapXX.json / shots.json / sfx_tapXX.json.
KO_SRC = ROOT / "01_KICH_BAN" / f"Tap{EPN}_KO" / f"kichban_tap{EPN}_KO.md"
JA_SRC = ROOT / "01_KICH_BAN" / f"Tap{EPN}_JA" / f"kichban_tap{EPN}_JA.md"
if KO:
    EP = dict(EP)
    EP["script"] = WORK / EP.get("script_ko", WORK / f"script_tap{EPN}_KO.json")
    EP["dir"] = f"Tap{EPN}_KO"
    EP["plan"] = f"KeHoach_Video_Tap{EPN}_KO.md"
    EP["master"] = f"Tap{EPN}_KO_master"
    EP["srt"] = f"Tap{EPN}_KO.srt"
    EP["acting"] = WORK / f"acting_tap{EPN}_KO.json"
    EP["intro"] = f"intro_kenh_KO_t{EPN}.mov"
    if not KO_SRC.exists():
        raise SystemExit(f"Chưa có kịch bản tiếng Hàn: {KO_SRC}")
if JA:
    EP = dict(EP)
    EP["script"] = WORK / EP.get("script_ja", WORK / f"script_tap{EPN}_JA.json")
    EP["dir"] = f"Tap{EPN}_JA"
    EP["plan"] = f"KeHoach_Video_Tap{EPN}_JA.md"
    EP["master"] = f"Tap{EPN}_JA_master"
    EP["srt"] = f"Tap{EPN}_JA.srt"
    EP["acting"] = WORK / f"acting_tap{EPN}_JA.json"
    EP["intro"] = f"intro_kenh_JA_t{EPN}.mov"
    if not JA_SRC.exists():
        raise SystemExit(f"Chưa có kịch bản tiếng Nhật: {JA_SRC}")

SCRIPT_JSON = EP["script"]
EP_DIR = ROOT / "02_SAN_XUAT" / EP["dir"]
OUT_DIR = EP_DIR / "xuat_ban"
PLAN = EP_DIR / EP["plan"]
MASTER = EP["master"]
SRT = EP["srt"]
N_ELEMENT = EP["n_element"]
ACTING = EP["acting"]
INTRO_MOV = ROOT / "assets" / "brand" / EP.get("intro", "intro_kenh.mov")

# ---------------------------------------------------------------- on-screen strings
TAGLINE = ("Criminal psychology through real case files" if EN else
           "実際の事件記録から読み解く犯罪心理学" if JA else
           " 범죄심리학 — 실사 사건 기록으로 읽는 인간 심리" if KO else
           "Phân tích tâm lý tội phạm qua những hồ sơ có thật")
ROLE_NAME = ((EP.get("roles_en") or
              {"H": ("HOST", "Your narrator"), "D": ("INVESTIGATOR", "Blanchard case file"),
               "C": ("PSYCHOLOGIST", "Criminal psychology"),
               "N1": ("SPRINGFIELD RESIDENT", "Longtime neighbor"), "N2": ("VIEWER", "Following the case")})
             if EN else
             (EP.get("roles_ja") or
              {"H": ("ホスト", "ストーリーテラー"), "D": ("捜査官", f"事件記録 {EP['case']}"),
               "C": ("心理学者", "犯罪心理学"),
               "N1": ("証人", "当事者"), "N2": ("視聴者", "事件を見守る人")}) if JA else
             (EP.get("roles_ko") or
              {"H": ("호스트", "내레이터"), "D": ("수사관", f"사건 기록 {EP['case']}"),
               "C": ("심리학자", "범죄심리학"),
               "N1": ("증인", "당사자"), "N2": ("시청자", "사건을 지켜본 사람")}) if KO else
             {"H": ("HOST", "Người dẫn chuyện"), "D": ("ĐIỀU TRA VIÊN", f"Hồ sơ vụ án {EP['case']}"),
              "C": ("CHUYÊN GIA TÂM LÝ", "Tâm lý học tội phạm"),
              "N1": EP["n1"][:2], "N2": EP["n2"][:2]})
SUB_TAG = ((EP.get("sub_tags_en") or
            {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST", "N1": "RESIDENT", "N2": "VIEWER"}) if EN else
           (EP.get("sub_tags_ja") or
            {"H": "ホスト", "D": "捜査官", "C": "心理学者", "N1": "証人", "N2": "視聴者"}) if JA else
           (EP.get("sub_tags_ko") or
            {"H": "호스트", "D": "수사관", "C": "심리학자", "N1": "증인", "N2": "시청자"}) if KO else
           {"H": "HOST", "D": "ĐIỀU TRA VIÊN", "C": "CHUYÊN GIA TÂM LÝ", "N1": EP["n1"][2], "N2": EP["n2"][2]})
UI = ({"next": "NEXT", "illus": "ILLUSTRATION", "intro_line": "Fictional character · AI voice · Dramatized",
       "stamp_forged": "FORGED", "stamp_secret": "CONFIDENTIAL"} if EN else
      {"next": "次へ", "illus": "イメージ", "intro_line": "架空のキャラクター · AI音声 · 演出",
       "stamp_forged": "偽造", "stamp_secret": "機密"} if JA else
      {"next": "다음", "illus": "모식화", "intro_line": "가상 인물 · AI 음성 · 각색",
       "stamp_forged": "위조", "stamp_secret": "기밀"} if KO else
      {"next": "TIẾP THEO", "illus": "MINH HOẠ", "intro_line": "Nhân vật minh hoạ · giọng đọc AI",
       "stamp_forged": "GIẢ MẠO", "stamp_secret": "MẬT"})

# intro disclaimer cards: (title, [[(text, highlighted)]])
if EN and EP.get("cards_en"):
    CARD_A, CARD_B = EP["cards_en"]
else:
    CARD_A = (("ABOUT THIS VIDEO", [
        [("Educational", 1), (" content: an analysis of criminal psychology.", 0)],
        [("Based on ", 0), ("public records", 1), ("; sources are in the description.", 0)],
        [("Not intended to accuse or defame anyone.", 0)]]) if EN else
        ("본 콘텐츠에 대하여", [
        [("본 영상은 ", 0), ("교육 목적", 1), ("의 범죄심리학 분석 콘텐츠입니다.", 0)],
        [("공개된 공식 기록", 1), ("을 기반으로 제작되었으며, 출처는 설명란에 기재되어 있습니다.", 0)],
        [("특정인을 비방하거나 단죄하려는 의도가 없습니다.", 0)]]) if KO else
        ("この動画について", [
        [("本動画は", 0), ("教育目的", 1), ("の犯罪心理学分析コンテンツです。", 0)],
        [("公開記録", 1), ("に基づいており、出典は概要欄に記載されています。", 0)],
        [("特定の個人を非難または中傷する意図はありません。", 0)]]) if JA else
        ("VỀ NỘI DUNG NÀY", [
        [("Nội dung ", 0), ("giáo dục", 1), (", phân tích tâm lý học tội phạm.", 0)],
        [("Dựa trên ", 0), ("tư liệu công khai", 1), (", nguồn ở phần mô tả.", 0)],
        [("Không nhằm kết tội hay bôi nhọ bất kỳ ai.", 0)]]))
    CARD_B = (("BEFORE YOU WATCH", [
        [("Not suitable for children", 1), (".", 0)],
        [("Sounds and images are ", 0), ("for illustration only", 1), (".", 0)],
        [("Not a substitute for medical, psychological or legal advice.", 0)]]) if EN else
        ("시청 전 유의사항", [
        [("청소년에게 적합하지 않을 수 있습니다", 1), (".", 0)],
        [("음향 및 시각 자료는 ", 0), ("이해를 돕기 위한 연출", 1), ("입니다.", 0)],
        [("본 내용은 의학적, 심리학적 또는 법률적 조언을 대신할 수 없습니다.", 0)]]) if KO else
        ("ご視聴前の注意", [
        [("お子様向けではありません", 1), ("。", 0)],
        [("音声および画像は", 0), ("イメージ", 1), ("です。", 0)],
        [("医学的、心理学的、または法的なアドバイスに代わるものではありません。", 0)]]) if JA else
        ("LƯU Ý TRƯỚC KHI XEM", [
        [("Nội dung ", 0), ("không phù hợp cho trẻ em", 1), (".", 0)],
        [("Âm thanh và hình ảnh ", 0), ("chỉ mang tính minh hoạ", 1), (".", 0)],
        [("Không thay thế tư vấn y khoa, tâm lý hay pháp lý.", 0)]]))

# ---------------------------------------------------------------- TTS cast (voice_id, base speed)
# Bản EN: `English_Deep-VoicedGentleman` (vai D của Tập 01 EN) bị đổi màu khi đổi cảm xúc
# (G10 23/10: "Investigator -> 3 người"; thí nghiệm .work/_voice_band_test.py cho thấy
# tốc độ đọc KHÔNG làm đổi người, chỉ CẢM XÚC mới đổi — với vai D của Tập 02 có cảm xúc
# sad/fearful ở các câu then chốt). `English_Trustworth_Man` giữ nguyên 1 người ở cả 4
# cảm xúc (SPEAKERS: 1) và vẫn tách bạch với Host · Chuyên gia.
CAST = ({"H": ("English_magnetic_voiced_man", 0.95), "D": ("English_Trustworth_Man", 0.97),
         "C": ("English_Wiselady", 0.95), "N1": ("English_SentimentalLady", 0.95),
         "N2": ("English_captivating_female1", 0.95)} if EN else
        # BẢN TIẾNG NHẬT (JA): 5 giọng chuẩn qua thử nghiệm ASR CER 0% & F0 phân tách rõ
        {"H": ("Japanese_GentleButler", 0.95), "D": ("Japanese_SeriousCommander", 0.97),
         "C": ("Japanese_DependableWoman", 0.95), "N1": ("Japanese_KindLady", 0.95),
         "N2": ("Japanese_DecisivePrincess", 0.95)} if JA else
        # BẢN TIẾNG HÀN: chưa có bộ giọng đã qua G8–G10 (cần thử giọng tiếng Hàn thật).
        # Không dùng nhầm bộ giọng VN/EN — sẽ ra giọng đọc sai ngôn ngữ.
        {"H": ("Korean_CalmGentleman", 0.95), "D": ("Korean_ColdYoungMan", 0.95),
         "C": ("Korean_DecisiveQueen", 0.92), "N1": ("Korean_GentleWoman", 0.95),
         "N2": ("Korean_SweetGirl", 0.95)} if KO else
        # BỘ A (chốt 23/10/2026, BaoCao_GiongDoc_Tap02.md §4): ổn định danh tính khi đổi cảm xúc, 3 vai tách bạch
        {"H": ("English_CaptivatingStoryteller", 0.90), "D": ("Korean_ColdYoungMan", 0.95),
         "C": ("English_AssertiveQueen", 0.92), "N1": ("Vietnamese_kindhearted_girl", 0.95),
         "N2": ("English_captivating_female1", 0.95)})
if EP["cast"]:
    CAST = {**CAST, **EP["cast"]}
if KO and not EP.get("cast_ko"):
    raise SystemExit(
        "Bản tiếng Hàn chưa có bộ giọng đã qua G8–G10.\n"
        "  1) thử giọng: py -3 .work/voice_audition.py (chọn giọng tiếng Hàn)\n"
        "  2) khai 'cast_ko' trong EPISODES của edition.py cho tập này\n"
        "  3) chạy G10: py -3 .work/voice_role_check.py\n"
        "Kịch bản tiếng Hàn đã sẵn sàng ở 01_KICH_BAN/Tap%s_KO/ — chỉ thiếu bước chọn giọng." % EPN)

# TTS-only spelling for sentences the voice would read the wrong way (screen text unchanged)
TTS_FIX = (EP.get("tts_fix", {}) if EN else {})

# Bản EN dùng lại diễn xuất của bản VN (cùng mã câu): manifest VN của chính tập đó
# + tốc độ gốc của bộ giọng VN để tự tính lệch tốc độ. Bản KO dùng chung mã câu với VN.
VN_MANIFEST = (WORK / (f"tts_manifest_t{EPN}.json" if EPN != "01" else "tts_manifest.json")) if (EN or KO or JA) else None
VN_CAST_BASE = {"H": 0.90, "D": 0.95, "C": 0.92, "N1": 0.95, "N2": 0.95}
