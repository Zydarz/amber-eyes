# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 13 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap13/KE_HOACH_CLIP_TAP13.md
  02_SAN_XUAT/TIKTOK/Tap13/SPEC_AUDIO_CLIP_TAP13.json
  02_SAN_XUAT/TIKTOK/Tap13/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap13/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap13/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap13_EN/KE_HOACH_CLIP_TAP13_EN.md
  02_SAN_XUAT/TIKTOK/Tap13_EN/SPEC_AUDIO_CLIP_TAP13_EN.json (SPEC_AUDIO_CLIP_TAP13.json)
  02_SAN_XUAT/TIKTOK/Tap13_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap13_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap13_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap13_JA/KE_HOACH_CLIP_TAP13_JA.md
  02_SAN_XUAT/TIKTOK/Tap13_JA/SPEC_AUDIO_CLIP_TAP13_JA.json (SPEC_AUDIO_CLIP_TAP13.json)
  02_SAN_XUAT/TIKTOK/Tap13_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap13_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap13_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 13:
- timeline_s_t13.json (VI)
- timeline_s_EN_t13.json (EN)
- timeline_s_JA_t13.json (JA)
Luật: AGENTS.md K1–K10 / G1–G13 / A1–A13 / L1–L6.
"""

import json
import pathlib
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap13"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap13_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap13_JA"

OUT_VI.mkdir(parents=True, exist_ok=True)
OUT_EN.mkdir(parents=True, exist_ok=True)
OUT_JA.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WORK))
try:
    from vi_cer import vi_numbers
except ImportError:
    def vi_numbers(text):
        return text

# ----------------------------------------------------------------------------
# 0. TỶ LỆ ĐỌC THẬT (Đo từ master Tập 13)
# ----------------------------------------------------------------------------
def get_rates(timeline_file, is_ja=False):
    tl = json.loads((WORK / timeline_file).read_text(encoding="utf-8"))
    dur = defaultdict(float)
    units = defaultdict(int)
    for it in tl["items"]:
        n = len(it["text"].replace(" ", "")) if is_ja else len(it["text"].split())
        dur[it["role"]] += it["end"] - it["start"]
        units[it["role"]] += n
    return {r: dur[r] / units[r] for r in dur}

RATE_VI = get_rates("timeline_s_t13.json", is_ja=False)
RATE_EN = get_rates("timeline_s_EN_t13.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t13.json", is_ja=True)

# ----------------------------------------------------------------------------
# 1. LOAD SCRIPT GỐC 3 NGÔN NGỮ
# ----------------------------------------------------------------------------
def load_script_map(filename):
    data = json.loads((WORK / filename).read_text(encoding="utf-8"))
    res = {}
    for el in data:
        if "sentences" in el:
            role = el.get("role")
            if role == "N":
                role = "N1" if el["id"] == "1.07" else "N2"
            for s in el["sentences"]:
                txt = s["text"].strip()
                res[s["id"]] = (role, txt)
    return res

MAP_VI = load_script_map("script_tap13.json")
MAP_EN = load_script_map("script_tap13_EN.json")
MAP_JA = load_script_map("script_tap13_JA.json")

# ----------------------------------------------------------------------------
# 2. KHAI BÁO 5 CLIP TẬP 13 (BẢN VI, EN, JA)
# ----------------------------------------------------------------------------
CLIPS_CONFIG = [
    {
        "id": "TK1",
        "title_vn": "Vỏ bọc 'Con Nhà Người Ta' & Kỷ luật Cha Mẹ Hổ",
        "title_en": "The Golden Child Facade & Tiger Parenting Cage",
        "title_ja": "優等生の仮面とタイガーペアレンティングの檻",
        "signs": [1, 9],
        "theme_vn": "Hiệu ứng Hào quang (Halo Effect) & Điểm mù Áp lực Gia đình (Tiger Parenting Blind Spot)",
        "theme_en": "The Halo Effect & Familial Blind Spots",
        "theme_ja": "ハロー効果と教育熱心な家庭の盲点",
        "hook_vn": "Huy chương trượt băng, piano xuất sắc. Chiếc lồng giam vô hình đằng sau vỏ bọc 'con nhà người ta'.",
        "hook_en": "Figure skating medals, piano prodigy. The invisible prison behind the 'golden child' illusion.",
        "hook_ja": "フィギュアスケートの栄光、ピアノの天才。完璧な「優等生」の裏に隠された見えない檻。",
        "bgm": "bgm_cello_sad.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_cello_sad.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_cello_sad.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_cello_sad.mp3",
        "sfx_vn": ["amb_wind_cold.wav (nền)", "fx_piano_single_note.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_wind_cold.wav (bed)", "fx_piano_single_note.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_wind_cold.wav（環境音）", "fx_piano_single_note.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "HỒ SƠ JENNIFER PAN · MARKHAM, ONTARIO, CANADA", "dur_s": 3.0},
            {"sau_cau": "TK1.01#3", "text": "VỎ BỌC 'CON NHÀ NGƯỜI TA' HOÀN HẢO", "dur_s": 2.5},
            {"sau_cau": "TK1.01#5", "text": "KỶ LUẬT THÉP CỰC ĐOAN: CẤM BẠN BÈ, CẤM HẸN HÒ", "dur_s": 2.5},
            {"sau_cau": "TK1.01#7", "text": "NỖI SỢ HÃI TÊ LIỆT BÀO MÒN NHÂN CÁCH", "dur_s": 2.5},
            {"sau_cau": "TK1.01#8", "text": "MÔ HÌNH 'CHA MẸ HỔ' VÀ SỰ KỲ VỌNG ÁP ĐẶT", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "JENNIFER PAN DOSSIER · MARKHAM, ONTARIO, CANADA", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "THE FLAWLESS 'GOLDEN CHILD' FACADE", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "EXTREME DISCIPLINE: ZERO SOCIAL LIFE, FORBIDDEN DATING", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "PARALYZING FEAR ERODING TEENAGE PSYCHE", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "TIGER PARENTING & UNREALISTIC EXPECTATIONS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "ジェニファー・パン事件簿 · カナダ・オンタリオ州マーカム", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "地域社会が絶賛した「完璧な優等生」の虚像", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "交友・外出・恋愛の全面禁止：極端な鉄の規律", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "父親の怒りへの恐怖が心を徐々に蝕んでいく", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "タイガーペアレンティングと移民家庭の過剰な重圧", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("1.04#1", "neutral", -0.02, 0.6, "t13_perfect_daughter_facade", "push"),
            ("1.04#2", "neutral", -0.02, 0.6, "t13_perfect_daughter_facade", "pan"),
            ("1.04#3", "neutral", -0.02, 0.6, "t13_curtain_of_subservience_dropping", "pull"),
            ("1.04#4", "neutral", -0.02, 0.6, "t13_tiger_parent_looming_shadow", "still"),
            ("1.04#5", "neutral", -0.02, 0.6, "t13_tiger_parent_looming_shadow", "push"),
            ("1.04#6", "neutral", -0.02, 0.6, "t13_locked_bedroom_desk_clock", "pan"),
            ("1.04#7", "sad", -0.04, 0.6, "t13_locked_bedroom_desk_clock", "pull"),
            ("3.03#1", "neutral", -0.02, 0.0, "t13_tiger_parenting_immigrant_anxiety", "pan")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Tòa Tháp Dối Lừa 10 Năm & Lối Sống Hai Mặt",
        "title_en": "The 10-Year Web of Lies & Double Life",
        "title_ja": "10年間の嘘の楼閣と二重生活の崩壊",
        "signs": [6, 8],
        "theme_vn": "Quỹ đạo Leo thang Ảo tưởng (Fantasy Escalation) & Hội chứng Nói dối Bệnh lý (Mythomania)",
        "theme_en": "Escalation Trajectory & Pathological Lying",
        "theme_ja": "虚言の段階的エスカレーションと病的虚言症",
        "hook_vn": "Làm giả học bạ trung học, ngụy tạo bằng đại học Dược khoa. Một lời nói dối leo thang suốt 10 năm.",
        "hook_en": "Forging high school reports, faking pharmacy diplomas. A 10-year compounding web of deceit.",
        "hook_ja": "偽造された成績表、トロント大学の偽学位記。たった一つの嘘が10年間の楼閣となった。",
        "bgm": "bgm_ambient_deep.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_ambient_deep.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_ambient_deep.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_ambient_deep.mp3",
        "sfx_vn": ["amb_library_room.wav (nền)", "fx_paper_scissors.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_library_room.wav (bed)", "fx_paper_scissors.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_library_room.wav（環境音）", "fx_paper_scissors.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "PHÁT SÚNG ĐẦU TIÊN: LÀM GIẢ HỌC BẠ BẰNG DAO RỌC GIẤY", "dur_s": 2.5},
            {"sau_cau": "TK2.01#3", "text": "TÒA THÁP LỪA DỐI SUỐT GẦN MƯỜI NĂM TIẾP THEO", "dur_s": 2.5},
            {"sau_cau": "TK2.01#5", "text": "LỐI SỐNG HAI MẶT: NGỒI THƯ VIỆN ĐỌC TIỂU THUYẾT MỖI NGÀY", "dur_s": 3.0},
            {"sau_cau": "TK2.01#7", "text": "NGỤY TẠO BẰNG CỬ NHÂN DƯỢC & VIỆC LÀM TẠI BỆNH VIỆN", "dur_s": 2.5},
            {"sau_cau": "TK2.01#8", "text": "SỰ LEO THANG KHÔNG THỂ VÃN HỒI CỦA TỘI ÁC", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "FIRST STEP: FORGING REPORT CARDS WITH BLADES & GLUE", "dur_s": 2.5},
            {"after_id": "TK2.01#3", "text": "A HOUSE OF CARDS BUILT ACROSS A DECADE", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "DOUBLE LIFE: SPENDING FULL DAYS IN PUBLIC LIBRARIES", "dur_s": 3.0},
            {"after_id": "TK2.01#7", "text": "FAKING PHARMACY DEGREES & SICKKIDS HOSPITAL JOBS", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "IRREVERSIBLE ESCALATION OF PATHOLOGICAL FRAUD", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "始まりはカッターナイフと糊による成績表偽造", "dur_s": 2.5},
            {"after_id": "TK2.01#3", "text": "その後10年間崩れなかった巨大な嘘の楼閣", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "毎朝通学のふりをして図書館で過ごす二重生活", "dur_s": 3.0},
            {"after_id": "TK2.01#7", "text": "薬学部卒業証明書と小児病院の研究職まで偽装", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "名誉の幻影を守るための歯止めなきエスカレーション", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("1.06#5", "neutral", -0.02, 0.6, "t13_forgery_scissors_glue_photocopy", "still"),
            ("1.06#6", "neutral", -0.02, 0.6, "t13_house_of_cards_first_lie", "push"),
            ("1.06#7", "neutral", -0.02, 0.6, "t13_house_of_cards_first_lie", "pan"),
            ("1.09#1", "neutral", -0.02, 0.6, "t13_fake_university_acceptance_letter", "push"),
            ("1.09#2", "neutral", -0.02, 0.6, "t13_fake_university_acceptance_letter", "pan"),
            ("1.09#3", "neutral", -0.02, 0.6, "t13_morning_bus_stop_winter_mist", "pull"),
            ("1.09#4", "neutral", -0.02, 0.6, "t13_public_library_reading_hours", "still"),
            ("1.10#1", "neutral", -0.02, 0.0, "t13_father_growing_suspicion", "pull")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Cuộc Gọi 911 Kỳ Lạ & Hiện Trường Đầy Sơ Hở",
        "title_en": "The Bizarre 911 Call & Crime Scene Anomalies",
        "title_ja": "不可解な911通報と現場に残された矛盾",
        "signs": [7, 8],
        "theme_vn": "Thủ đoạn Gây án MO vs. Dấu ấn Signature & Lỗ hổng Ngụy tạo Hiện trường",
        "theme_en": "MO vs. Signature & Staged Crime Scene Flaws",
        "theme_ja": "手口MO対署名Signatureと偽装工作の致命的綻び",
        "hook_vn": "Bị trói hai tay sau lưng nhưng vẫn gọi được 911? Chi tiết lật tẩy màn kịch hoàn hảo.",
        "hook_en": "Hands tied tightly behind her back, yet dialing 911? The detail unraveling the staged home invasion.",
        "hook_ja": "両手を後ろ手に縛られながらどうやって911に通報したのか？ 完璧なシナリオを崩した決定的一撃。",
        "bgm": "bgm_piano_minimal.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_piano_minimal.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_piano_minimal.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_piano_minimal.mp3",
        "sfx_vn": ["amb_rain_night.wav (nền)", "fx_phone_dial_panic.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_rain_night.wav (bed)", "fx_phone_dial_panic.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_rain_night.wav（環境音）", "fx_phone_dial_panic.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "238 ĐẠI LỘ HELEN · MÀN KỊCH CƯỚP NHÀ ĐẪM MÁU", "dur_s": 2.5},
            {"sau_cau": "TK3.01#3", "text": "CỬA CHÍNH KHÔNG HỀ BỊ CẠY PHÁ", "dur_s": 2.5},
            {"sau_cau": "TK3.01#5", "text": "CUỘC GỌI 911 HOẢNG LOẠN: BỊ TRÓI NHƯNG BẤM MÁY HOÀN HẢO", "dur_s": 3.0},
            {"sau_cau": "TK3.01#7", "text": "TÀI SẢN QUÝ GIÁ CÒN NGUYÊN VẸN TRÊN BÀN", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "DẤU VẾT NGUY BỆNH CỦA KẺ CHỦ MƯU NỘI BỘ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "238 HELEN AVENUE · STAGED HOME INVASION", "dur_s": 2.5},
            {"after_id": "TK3.01#3", "text": "FRONT DOOR MYSTERIOUSLY UNLOCKED", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "911 CALL: DIALING WITH HANDS SUPPOSEDLY BOUND", "dur_s": 3.0},
            {"after_id": "TK3.01#7", "text": "VALUABLES LEFT UNTOUCHED IN PLAIN SIGHT", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "ANOMALIES POINTING TO AN INSIDE CONSPIRACY", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "ヘレン通り238番地 · 偽装された凶悪強盗事件", "dur_s": 2.5},
            {"after_id": "TK3.01#3", "text": "正面玄関に一切ないピッキングや破壊の痕跡", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "緊縛されながらスマートフォンを操作した不自然な通報", "dur_s": 3.0},
            {"after_id": "TK3.01#7", "text": "放置された現金や貴金属：強盗の動機不在", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "内部協力者の存在を示す現場鑑識の決定打", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("2.04#1", "neutral", -0.02, 0.6, "t13_simmering_resentment_dark_room", "pan"),
            ("2.04#2", "neutral", -0.02, 0.6, "t13_simmering_resentment_dark_room", "pull"),
            ("2.06#1", "neutral", -0.02, 0.6, "t13_unlocked_front_door_night", "pan"),
            ("2.10#1", "neutral", -0.02, 0.6, "t13_panicked_911_call_transcript", "pull"),
            ("2.10#2", "fearful", -0.03, 0.6, "t13_panicked_911_call_transcript", "still"),
            ("4.03#1", "neutral", -0.02, 0.6, "t13_unforced_entry_crime_scene_log", "pan"),
            ("4.03#2", "neutral", -0.02, 0.6, "t13_unforced_entry_crime_scene_log", "pull"),
            ("4.03#4", "neutral", -0.02, 0.0, "t13_unlocked_front_door_anomaly", "push")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Lời Khai Của Người Cha & Màn Đấu Trí Phòng Thẩm Vấn",
        "title_en": "The Father's Testimony & Interrogation Room Showdown",
        "title_ja": "父の証言と取調室の心理戦",
        "signs": [4, 5],
        "theme_vn": "Thái độ trước Bản án & Sự Thức tỉnh của Người cha (Survivor's Truth vs. Denial)",
        "theme_en": "Attitude to Reality & The Father's Shattering Truth",
        "theme_ja": "真実への直面と生き残った父親の告発",
        "hook_vn": "'Con gái tôi đi lại tự do và thì thầm với kẻ cướp.' Lời khai từ giường bệnh của người cha.",
        "hook_en": "'My daughter walked freely, whispering with the intruders.' A surviving father's testimony.",
        "hook_ja": "「娘は両手を縛られておらず、犯人と親しげに囁き合っていた」。昏睡から目覚めた父の証言。",
        "bgm": "bgm_violin_heart.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_violin_heart.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_violin_heart.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_violin_heart.mp3",
        "sfx_vn": ["amb_hospital_tone.wav (nền)", "fx_door_close_heavy.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_hospital_tone.wav (bed)", "fx_door_close_heavy.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_hospital_tone.wav（環境音）", "fx_door_close_heavy.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "NGƯỜI CHA HUEI HANN PAN TỈNH LẠI SAU CƠN HÔN MÊ", "dur_s": 2.5},
            {"sau_cau": "TK4.01#3", "text": "KÝ ỨC ĐẬP TAN MỌI LỜI NÓI DỐI CỦA CON GÁI", "dur_s": 2.5},
            {"sau_cau": "TK4.01#4", "text": "“TAY CON BÉ KHÔNG HỀ BỊ TRÓI, NÓ THÌ THẦM VỚI CHÚNG”", "dur_s": 3.0},
            {"sau_cau": "TK4.01#6", "text": "BUỔI THẨM VẤN LỊCH SỬ NGÀY 22/11/2010", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "HÀNG TRĂM TIN NHẮN TẬN DIỆT PHƠI BÀY", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "FATHER HUEI HANN PAN AWAKENS FROM COMA", "dur_s": 2.5},
            {"after_id": "TK4.01#3", "text": "SHATTERING MEMORY DESTROYING JENNIFER'S ALIBI", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "“HER HANDS WERE NOT TIED, SHE WHISPERED TO THEM”", "dur_s": 3.0},
            {"after_id": "TK4.01#6", "text": "HISTORIC INTERROGATION: NOVEMBER 22, 2010", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "INCRIMINATING FORENSIC TEXTS EXPOSED", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "奇跡的に昏睡から意識を取り戻した父ハン・パン", "dur_s": 2.5},
            {"after_id": "TK4.01#3", "text": "娘のアリバイを根底から覆した鮮明な記憶", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "「娘の手は縛られておらず、犯人と親しげに話していた」", "dur_s": 3.0},
            {"after_id": "TK4.01#6", "text": "2010年11月22日：歴史的取調室の対決", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "解析された携帯メッセージが暴いた完全犯罪の謀議", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("4.05#4", "neutral", -0.02, 0.6, "t13_father_broken_voice_testimony", "still"),
            ("4.06#1", "sad", -0.04, 0.6, "t13_father_memory_unmasked_daughter", "pan"),
            ("4.06#2", "sad", -0.04, 0.6, "t13_father_memory_unmasked_daughter", "pull"),
            ("4.06#4", "sad", -0.04, 0.6, "t13_unbound_hands_broken_heart", "push"),
            ("4.08#1", "neutral", -0.02, 0.6, "t13_third_interrogation_november_22", "still"),
            ("4.08#2", "neutral", -0.02, 0.6, "t13_third_interrogation_november_22", "push"),
            ("4.08#4", "neutral", -0.02, 0.6, "t13_forensic_cellphone_text_evidence", "pull"),
            ("4.09#1", "neutral", -0.02, 0.0, "t13_deception_body_language_analysis", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Nạn Nhân Học & 4 Tín Hiệu Cảnh Báo Đỏ Gia Đình",
        "title_en": "Victimology & 4 Familial Red Flags",
        "title_ja": "被害者学と家庭内危機の4つの警告サイン",
        "signs": [10],
        "theme_vn": "Nạn nhân học (Victimology) & 4 Tín hiệu Báo động Đỏ Sinh tồn trong Gia đình",
        "theme_en": "Victimology & 4 Familial Survival Red Flags",
        "theme_ja": "被害者学と家庭内トラウマを防ぐ4つの危険信号",
        "hook_vn": "Bốn tín hiệu cảnh báo đỏ nhận diện nguy cơ rạn nứt tâm lý và bạo lực ngầm trong gia đình.",
        "hook_en": "Four vital survival red flags to prevent hidden psychological trauma in families.",
        "hook_ja": "家庭内の心理的崩壊と悲劇を防ぐ「4つの危険信号」。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_room_tone.wav (nền)", "fx_page_turn.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_tone.wav (bed)", "fx_page_turn.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_tone.wav（環境音）", "fx_page_turn.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 CẢNH BÁO ĐỎ GIA ĐÌNH · AMBER EYES", "dur_s": 2.5},
            {"sau_cau": "TK5.01#2", "text": "CẢNH BÁO 1: TÌNH YÊU CÓ ĐIỀU KIỆN & TRỪNG PHẠT THẤT BẠI", "dur_s": 2.5},
            {"sau_cau": "TK5.01#4", "text": "CẢNH BÁO 2: LỜI NÓI DỐI LEO THANG & LỐI SỐNG HAI MẶT", "dur_s": 2.5},
            {"sau_cau": "TK5.01#6", "text": "CẢNH BÁO 3: KIỂM SOÁT CỰC ĐOAN TƯỚC ĐOẠT TỰ DO", "dur_s": 2.5},
            {"sau_cau": "TK5.01#8", "text": "CẢNH BÁO 4: ĐỨT GÃY GIAO TIẾP CẢM XÚC DƯỚI MỘT MÁI NHÀ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#10", "text": "LẮNG NGHE VÀ BAO DUNG LÀ CHIẾC KHIÊN BẢO VỆ GIA ĐÌNH", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "4 FAMILIAL RED FLAGS · AMBER EYES", "dur_s": 2.5},
            {"after_id": "TK5.01#2", "text": "FLAG 1: CONDITIONAL LOVE & SEVERE PUNISHMENT", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "FLAG 2: ESCALATING WEB OF DECEIT & DOUBLE LIFE", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "FLAG 3: TOTAL CONTROL CRUSHING AUTONOMY", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "FLAG 4: TOXIC SILENCE & EMOTIONAL DISCONNECT", "dur_s": 2.5},
            {"after_id": "TK5.01#10", "text": "EMPATHY & UNCONDITIONAL LOVE ARE TRUE SHIELDS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "家庭崩壊を防ぐ4つの危険信号 · 理性と共感", "dur_s": 2.5},
            {"after_id": "TK5.01#2", "text": "第1の警告：条件付きの愛と失敗に対する極端な処罰", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "第2の警告：エスカレートする嘘と長期化する二重生活", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "第3の警告：個人の尊厳と決定権を奪う過剰な管理", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "第4の警告：感情的対話の途絶と家庭内の冷たい沈黙", "dur_s": 2.5},
            {"after_id": "TK5.01#10", "text": "ありのままを受け入れる無条件の受容こそ最大の防壁", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("5.05#1", "neutral", -0.02, 0.5, "t13_four_redflags_overview_banner", "still"),
            ("5.05#2", "neutral", -0.02, 0.4, "t13_four_redflags_overview_banner", "push"),
            ("5.05#4", "neutral", -0.02, 0.5, "t13_prevention_compass_analytical_desk", "pull"),
            ("5.05#6", "neutral", -0.02, 0.4, "t13_redflag1_conditional_love_punishment", "push"),
            ("5.05#8", "neutral", -0.02, 0.5, "t13_fear_driven_compliance_prison", "pull"),
            ("5.05#10", "neutral", -0.02, 0.4, "t13_redflag2_escalating_web_of_lies", "push"),
            ("5.05#12", "neutral", -0.02, 0.5, "t13_compounding_lies_collapse", "pull"),
            ("5.05#14", "neutral", -0.02, 0.4, "t13_redflag3_total_control_autonomy_loss", "push"),
            ("5.05#17", "neutral", -0.02, 0.5, "t13_redflag4_emotional_disconnect_rupture", "still"),
            ("5.05#19", "neutral", -0.02, 0.0, "t13_authentic_soul_open_window_dawn", "pan")
        ]
    }
]

# ----------------------------------------------------------------------------
# 3. BUILD ALL FILES (VI, EN, JA)
# ----------------------------------------------------------------------------
def build_lang_artifacts(lang_code):
    if lang_code == "VI":
        out_dir = OUT_VI
        script_map = MAP_VI
        rates = RATE_VI
        is_ja = False
    elif lang_code == "EN":
        out_dir = OUT_EN
        script_map = MAP_EN
        rates = RATE_EN
        is_ja = False
    elif lang_code == "JA":
        out_dir = OUT_JA
        script_map = MAP_JA
        rates = RATE_JA
        is_ja = True

    spec_audio = {}
    plan_lines = []

    plan_header_title = {
        "VI": '# KẾ HOẠCH CLIP TIKTOK — TẬP 13 · "VỎ BỌC CON NHÀ NGƯỜI TA & LỜI NÓI DỐI 10 NĂM (JENNIFER PAN)"',
        "EN": '# TIKTOK CLIPS PLAN — EPISODE 13 · "THE GOLDEN CHILD ILLUSION & 10-YEAR WEB OF DECEIT (JENNIFER PAN)"',
        "JA": '# TIKTOKクリップ計画 — 第13話 ·「優等生の仮面と10年間の嘘の楼閣（ジェニファー・パン事件）」'
    }[lang_code]

    plan_lines.append(plan_header_title)
    plan_lines.append("")
    plan_lines.append(f"*Ngôn ngữ: **{lang_code}** · Nguồn dữ liệu: master Tập 13 · Tỷ lệ đọc ASR thật.*")
    plan_lines.append("*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md`.*")
    plan_lines.append("")
    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 0. Tóm tắt 5 clip và thời lượng đo lường")
    plan_lines.append("")
    plan_lines.append("| Clip | Chỉ dấu (K10) | Chủ đề | Hook mở đầu (0–3 s) | Ước lượng thời lượng |")
    plan_lines.append("|---|---|---|---|---|")

    def get_field(cfg, prefix):
        key = f"{prefix}_vn" if lang_code == "VI" else f"{prefix}_{lang_code.lower()}"
        return cfg[key]

    durations = {}
    clip_lines_data = {}

    for cfg in CLIPS_CONFIG:
        cid = cfg["id"]
        c_lines = []
        tot_dur = 0.0

        for idx, (sid, emot, spd, pause, bg, cam) in enumerate(cfg["lines_meta"], start=1):
            role, raw_txt = script_map[sid]
            spk = vi_numbers(raw_txt) if lang_code == "VI" else raw_txt
            spk = re.sub(r"<#[\d.]+#>", " ", spk)
            n_u = len(spk.replace(" ", "")) if is_ja else len(spk.split())
            dur_line = n_u * rates[role]
            line_id = f"{cid}.01#{idx}"
            c_lines.append({
                "id": line_id,
                "src_id": sid,
                "role": role,
                "emotion": emot,
                "speed": spd,
                "pause_after": pause,
                "bg": bg,
                "camera": cam,
                "text": raw_txt,
                "dur": round(dur_line, 2)
            })
            tot_dur += dur_line + pause

        durations[cid] = round(tot_dur, 1)
        clip_lines_data[cid] = c_lines

        title_col = get_field(cfg, "title")
        hook_col = get_field(cfg, "hook")
        theme_col = get_field(cfg, "theme")
        signs_str = " · ".join([f"#{s}" for s in cfg["signs"]])

        plan_lines.append(f'| **{cid}** | {signs_str} | {theme_col} | *"{hook_col}"* | **{durations[cid]} s** ({len(c_lines)} câu) |')

    plan_lines.append("")
    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 1. Chi tiết kịch bản và dàn dựng từng clip")
    plan_lines.append("")

    for cfg in CLIPS_CONFIG:
        cid = cfg["id"]
        title_c = get_field(cfg, "title")
        theme_c = get_field(cfg, "theme")
        hook_c = get_field(cfg, "hook")
        bgm_desc = get_field(cfg, "bgm_desc")
        sfx_list = ", ".join(get_field(cfg, "sfx"))
        overlay_list = cfg["overlay_vn"] if lang_code == "VI" else (cfg["overlay_en"] if lang_code == "EN" else cfg["overlay_ja"])

        plan_lines.append(f"### {cid} — {title_c}")
        plan_lines.append(f"- **Chủ đề**: {theme_c}")
        plan_lines.append(f"- **Thời lượng dự kiến**: {durations[cid]} giây ({len(clip_lines_data[cid])} câu)")
        plan_lines.append(f"- **BGM**: {bgm_desc}")
        plan_lines.append(f"- **SFX**: {sfx_list}")
        plan_lines.append("")
        plan_lines.append("| Mã câu | Vai | Cảm xúc | Tốc độ | Nghỉ | Hình nền & Camera | Lời thoại | Nguồn câu |")
        plan_lines.append("|---|---|---|---|---|---|---|---|")

        clip_spec_list = []
        for l in clip_lines_data[cid]:
            plan_lines.append(f"| `{l['id']}` | {l['role']} | {l['emotion']} | {l['speed']} | {l['pause_after']}s | `{l['bg']}` ({l['camera']}) | {l['text']} | `{l['src_id']}` |")
            clip_spec_list.append({
                "id": l["id"],
                "role": l["role"],
                "emotion": l["emotion"],
                "speed": l["speed"],
                "pause_after": l["pause_after"],
                "text": l["text"],
                "source": l["src_id"],
                "bg": l["bg"],
                "camera": l["camera"],
                "dur_est": l["dur"]
            })

        spec_audio[cid] = {
            "title": title_c,
            "theme": theme_c,
            "hook": hook_c,
            "total_dur_est": durations[cid],
            "bgm": cfg["bgm"],
            "sfx": get_field(cfg, "sfx"),
            "overlay": overlay_list,
            "lines": clip_spec_list
        }

        plan_lines.append("")
        plan_lines.append("**Thẻ chữ trên hình (Overlay Card):**")
        for ov in overlay_list:
            sau_k = "sau_cau" if "sau_cau" in ov else "after_id"
            plan_lines.append(f"- `{ov[sau_k]}` → *\"{ov['text']}\"* ({ov['dur_s']}s)")
        plan_lines.append("")

    # Ghi file KE_HOACH_CLIP_TAP13
    plan_filename = f"KE_HOACH_CLIP_TAP13{'' if lang_code == 'VI' else '_' + lang_code}.md"
    (out_dir / plan_filename).write_text("\n".join(plan_lines), encoding="utf-8")

    # Ghi file SPEC_AUDIO_CLIP_TAP13.json
    (out_dir / "SPEC_AUDIO_CLIP_TAP13.json").write_text(json.dumps(spec_audio, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[{lang_code}] Generated plan & spec successfully in {out_dir}")
    for cid, d in durations.items():
        print(f"  {cid}: {d}s")

if __name__ == "__main__":
    for code in ["VI", "EN", "JA"]:
        build_lang_artifacts(code)
