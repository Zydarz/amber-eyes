#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""ja_glossary — thuật ngữ cố định cho bản tiếng Nhật của AMBER EYES.

Dùng chung cho cả 29 tập => thuật ngữ nhất quán toàn series.
Mỗi mục: "cụm từ tiếng Việt" -> "bản dịch tiếng Nhật bắt buộc".
Không khớp chính xác thì không ép, nhưng các thuật ngữ chuyên ngành thì nên theo.
"""

# ---------------------------------------------------------------- vai trò (nhãn trong file JA)
ROLES_JA = {
    "HOST": "ホスト",
    "ĐIỀU TRA VIÊN": "捜査官",
    "CHUYÊN GIA TÂM LÝ": "心理学者",
    "NGƯỜI BÌNH THƯỜNG": "一般人",
    "ĐẶC VỤ FBI": "FBI特別捜査官",
    "CẢNH SÁT ĐỊA PHƯƠNG": "地方警察",
}

# ---------------------------------------------------------------- thuật ngữ chuyên ngành
TERMS = {
    # --- hội chứng / rối loạn ---
    "Hội chứng Münchausen qua trung gian": "代理型ミュンハウゼン症候群",
    "Rối loạn giả bệnh áp đặt lên người khác": "他者に虚偽の疾患を課す意図的偽装障害",
    "Rối loạn nhân cách ranh giới": "境界性人格障害",
    "Rối loạn nhân cách ranh giới (BPD)": "境界性人格障害（BPD）",
    "Rối loạn nhân cách chống đối xã hội": "反社会性人格障害",
    "Rối loạn nhân cách ám ảnh cưỡng chế": "強迫性人格障害",
    "Rối loạn nhân cách ái kỷ ẩn tàng": "自己愛性人格障害",
    "Rối loạn nhân cách ái kỷ": "自己愛性人格障害",
    "Rối loạn Nhân cách Chống đối Xã hội": "反社会性人格障害",
    "Rối loạn Nhân cách Bất cần Xã hội": "反社会性人格障害",
    "Rối loạn nhân cách kịch tính": "劇症人格障害",
    "Rối loạn hoang tưởng chia sẻ": "共有妄想",
    "Rối loạn tâm thần chia sẻ": "共有妄想",
    "Hội chứng Điên cuồng đôi": "共有妄想（フォリー・ドゥ）",
    "Hội chứng Folie à Deux": "共有妄想（フォリー・ドゥ）",
    "Hội chứng Stockholm": "ストックホルム症候群",
    "Hội chứng Nói dối bệnh lý": "病の嘘（架空病）症候群",
    "Hội chứng Giả bệnh tâm thần": "偽病（マリングリング）",
    "Hội chứng say mê tội phạm": "犯罪者愛好症（ヒブリストフィリア）",
    "Hội chứng Người phụ nữ bị Bạo hành": "虐待された女性の症候群",
    "Hội chứng người phụ nữ bị bạo hành": "虐待された女性の症候群",
    "Hội chứng Tước đoạt Cảm giác cực hạn": "極度の感覚剥奪症候群",
    "Hội chứng 'Vị cứu tinh' giả tạo": "偽の救済者症候群",
    "Hội chứng Münchausen kỹ thuật số": "デジタル型ミュンハウゼン症候群",
    "Hội chứng khao khát sự chú ý": "注目渇望症候群",
    "Loạn thần sau sinh": "産褥期精神病",
    "Loạn thần thực sự": "真性精神病",
    "Loạn thần tâm thần": "精神病",
    "Không chấp nhận bất kỳ ranh giới cá nhân nào": "いかなる境界も認めない姿勢",
    "Sự bất lực tập nhiễm": "学習性無力感",
    "Sự bất lực học tập": "学習性無力感",
    "Mạch ngầm tâm lý tội phạm": "犯罪心理の底流",
    "Cơ chế giải thể nhân cách": "解離（離人感）のメカニズム",
    "Ám tưởng điên cuồng": "狂気の妄想",
    "Hoang tưởng tôn giáo chia sẻ": "共有される宗教的妄想",
    "Ảo tưởng sở hữu": "所有の妄想",
    "Ảo tưởng kiểm soát": "支配の妄想",
    "Ảo tưởng kiểm soát tuyệt đối": "絶対的な支配の妄想",
    "Tâm lý học tội phạm": "犯罪心理学",
    "Tâm thần học pháp y": "司法精神医学",
    "Chuyên gia tâm lý học tội phạm": "犯罪心理学者",
    "Bác sĩ Tâm thần học Pháp y": "司法精神医学者",
    "Chuyên gia Tâm lý": "心理学者",
    "Điều tra viên": "捜査官",
    "Người trong cuộc": "当事者",
    "Nhân chứng": "証人",
    "Bị cáo": "被告",
    "Công lý": "検察",
    "Phiên tòa": "裁判",
    "Bản án": "判決",
    "Cuộc thẩm vấn": "取調",
    "Áp lực thời gian": "時間的圧力",
    "Áp lực kỳ vọng": "期待圧力",
    "Ảo tưởng kiểm soát con người thành vật thể": "人間を物のように支配しようとする妄想",
    # --- thuật ngữ tâm lý chung ---
    "Trầm cảm": "うつ",
    "Loạn thần": "精神病",
    "Ảo tưởng": "妄想",
    "Hoang tưởng": "妄想",
    "Ảo giác": "幻覚",
    "Ám ảnh": "強迫観念",
    "Giác ngủ mơ": "悪夢",
    "Tự sát": "自殺",
    "Hưng phấn": "躁病",
    "Nhân cách": "人格",
    "Tâm lý": "心理",
    "Tâm thần học": "精神医学",
    "Thói tắt mắt": "万引きの癖",
    "Môi trường gia đình": "家庭環境",
    "Chẩn đoán": "診断",
    "Kỹ thuật tâm lý": "心理テクニック",
    "Ám ảnh tâm lý": "心理的操作",
    "Thao túng tâm lý": "心理的操作",
    "Tâm lý bệnh học": "精神病理",
    "Nguyên tắc pháp quyền nhân đạo": "人権に内在する法の原則",
    # --- vai trò / nhãn ---
    "Người dẫn chuyện": "語り部",
    "Dẫn chuyện (Host)": "語り部（ホスト）",
    "Điều tra viên": "捜査官",
    "Chuyên gia Tâm lý": "心理学者",
    "Người trong cuộc 1": "当事者1",
    "Người trong cuộc 2": "当事者2",
    "Trầm ấm": "温かく力強い",
    "Trầm, kịch tính": "低く、緊迫感のある",
    "Điềm đạm, khách quan": "冷静で客観的",
    "Nam trung niên, điềm tĩnh": "中年の男声、冷静",
    "Bàng hoàng, dồn dập": "動揺し追い詰められた",
    "Nữ trung niên, đau đớn": "中年の女性声、苦しみの",
    # --- thể loại / cấu trúc ---
    "KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM": "犯罪心理学オーディオ／ポッドキャスト台本",
    "THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN": "制作仕様とナレーション構成",
    "BẢNG PHÂN VAI VÀ CẤU TRÚC GIỌNG ĐỌC": "配役表と音声構成",
    "Hồi": "第",
    "cảnh báo đỏ": "赤い警告",
    "4 cảnh báo đỏ": "4つの赤い警告",
    "bài học cảnh tỉnh": "覚醒の教訓",
    "Cảnh sát": "警察",
    "cảnh sát địa phương": "地方警察",
    "đặc vụ FBI": "FBI特別捜査官",
    "thám tử": "刑事",
    "cảnh sát tuần tra": "巡回警官",
    "tòa án": "裁判所",
    "viện tư pháp": "検察庁",
    "tài liệu lưu trữ tư pháp": "検察庁記録文書",
    "Nhân chứng trốn thoát": "脱出した証人",
    "Đại diện thân nhân nạn nhân": "被害者家族代理人",
    "người dân": "住民",
    "người đọc": "視聴者",
    "khán giả": "視聴者",
    "Bảo hiểm": "保険",
    "bảo hiểm": "保険",
    "tiền bạc": "金銭",
    "tiền từ thiện": "寄付金",
    "quỹ từ thiện": "寄付基金",
    "Quỹ Habitat for Humanity": "Habitat for Humanity基金",
}

# ---------------------------------------------------------------- quy tắc riêng cho từng tập (nếu cần)
EPISODE_EXTRA = {
    "01": {
        "Hội chứng Münchausen qua trung gian (FDIA)": "代理型ミュンハウゼン症候群（FDIA）",
    },
}

# ---------------------------------------------------------------- cấu trúc file JA
JA_PAUSE_PREFIX = "休止 "          # **[Nghỉ 2 giây]** -> **[休止 2秒]**
JA_ACT_PREFIX = "第"              # ## HỒI 1: -> ## 第1幕：
JA_ACT_SUFFIX = "幕"

BANNED_JA = [  # tương ứng danh sách từ cấm của bản VN (YouTube Safe)
    "血", "死体", "殺害", "殴", "縛", "打痕", "殴り", "頭部に毒", "大量死",
    "性関係", "強姦", "強制", "絞首", "斬首", "首切り",
]
