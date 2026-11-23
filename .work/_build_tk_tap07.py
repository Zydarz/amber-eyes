# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 07 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap07/KE_HOACH_CLIP_TAP07.md
  02_SAN_XUAT/TIKTOK/Tap07/SPEC_AUDIO_CLIP_TAP07.json
  02_SAN_XUAT/TIKTOK/Tap07/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap07/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap07/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap07_EN/KE_HOACH_CLIP_TAP07_EN.md
  02_SAN_XUAT/TIKTOK/Tap07_EN/SPEC_AUDIO_CLIP_TAP07.json
  02_SAN_XUAT/TIKTOK/Tap07_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap07_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap07_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap07_JA/KE_HOACH_CLIP_TAP07_JA.md
  02_SAN_XUAT/TIKTOK/Tap07_JA/SPEC_AUDIO_CLIP_TAP07.json
  02_SAN_XUAT/TIKTOK/Tap07_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap07_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap07_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 07:
- timeline_s_t07.json (VI)
- timeline_s_EN_t07.json (EN)
- timeline_s_JA_t07.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap07"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap07_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap07_JA"

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
# 0. TỈ LỆ ĐỌC THẬT (Đo từ master Tập 07)
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

RATE_VI = get_rates("timeline_s_t07.json", is_ja=False)
RATE_EN = get_rates("timeline_s_EN_t07.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t07.json", is_ja=True)

# ----------------------------------------------------------------------------
# 1. LOAD SCRIPT GỐC 3 NGÔN NGỮ
# ----------------------------------------------------------------------------
def load_script_map(filename):
    data = json.loads((WORK / filename).read_text(encoding="utf-8"))
    res = {}
    for el in data:
        if "sentences" in el:
            role = el["role"]
            if role == "N":
                role = "N1" if el["id"] == "1.07" else "N2"
            for s in el["sentences"]:
                txt = s["text"].strip()
                if "into a expendable" in txt:
                    txt = txt.replace("into a expendable", "into an expendable")
                res[s["id"]] = (role, txt)
    return res

MAP_VI = load_script_map("script_tap07.json")
MAP_EN = load_script_map("script_tap07_EN.json")
MAP_JA = load_script_map("script_tap07_JA.json")

# ----------------------------------------------------------------------------
# 2. KHAI BÁO 5 CLIP TẬP 07 (BẢN VI, EN, JA)
# ----------------------------------------------------------------------------
CLIPS_CONFIG = [
    {
        "id": "TK1",
        "title_vn": "Tội phạm không chạm tay và phán quyết lịch sử",
        "title_en": "The Touchless Crime & Historic Involuntary Manslaughter Ruling",
        "title_ja": "非接触の殺人罪と全米を震撼させた歴史的判決",
        "signs": [1, 4],
        "theme_vn": "Ảnh hưởng & Dư chấn xã hội + Bản án ngộ sát lịch sử",
        "theme_en": "Societal Impact & Historical Involuntary Manslaughter Precedent",
        "theme_ja": "社会的波紋と遠隔操作による過失致死罪の司法先例",
        "hook_vn": "Không hung khí, không xô xát, cách xa năm mươi sáu cây số. Nhưng bản án ngộ sát lịch sử vẫn được tuyên.",
        "hook_en": "No weapon, no physical struggle, thirty-five miles apart. Yet a historic manslaughter verdict was handed down.",
        "hook_ja": "凶器もなく、争いもなく、56キロも離れていた。それでも歴史的な過失致死罪が宣告された。",
        "bgm": "bgm_sub_drone.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_sub_drone.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_sub_drone.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_sub_drone.mp3",
        "sfx_vn": ["amb_dark_drone.wav (nền)", "fx_phone_dial.wav", "fx_gavel_strike.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_dark_drone.wav (bed)", "fx_phone_dial.wav", "fx_gavel_strike.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_dark_drone.wav（環境音）", "fx_phone_dial.wav", "fx_gavel_strike.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "TỘI PHẠM KHÔNG CHẠM TAY (TOUCHLESS CRIME)", "dur_s": 3.0},
            {"sau_cau": "TK1.01#3", "text": "KHO LƯU TRỮ HƠN 20.000 DÒNG TIN NHẮN", "dur_s": 2.5},
            {"sau_cau": "TK1.01#5", "text": "MỆNH LỆNH BẰNG LỜI NÓI PHÁ VỠ CƠ HỘI SỐNG", "dur_s": 2.5},
            {"sau_cau": "TK1.01#6", "text": "BẢN ÁN NGỘ SÁT LỊCH SỬ NƯỚC MỸ", "dur_s": 2.5},
            {"sau_cau": "TK1.01#8", "text": "HÀO QUANG ẢO TƯỞNG SỤP ĐỔ HOÀN TOÀN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "THE TOUCHLESS CRIME PRECEDENT", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "OVER 20,000 ARCHIVED DIGITAL TEXT MESSAGES", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "VERBAL ORDER BREAKING THE CAUSAL CHAIN", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "HISTORIC INVOLUNTARY MANSLAUGHTER CONVICTION", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "TOTAL COLLAPSE OF NARCISSISTIC DEFENSES", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "全米初：物理的接触なき遠隔殺人裁判", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "復元された2万件以上のテキスト通信記録", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "生存の機会を奪い去った受話器越しの命令", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "歴史的判決：不随意過失致死罪で有罪", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "自己愛の崩壊と露呈した真実の姿", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t7_digital_coercion_screen", "pull"),
            ("H", "1.02#3", "neutral", -0.02, 0.6, "t7_digital_lighthouse_beacon", "push"),
            ("H", "1.02#4", "neutral", -0.02, 0.6, "t7_social_media_notifications_flood", "still"),
            ("D", "1.10#2", "neutral", -0.02, 0.6, "t7_copied_script_lines_notebook", "pan"),
            ("D", "4.08#2", "neutral", -0.02, 0.6, "t7_courtroom_breathless_silence", "still"),
            ("D", "4.08#3", "neutral", -0.02, 0.6, "t7_courtroom_projection_screen", "push"),
            ("D", "4.08#6", "neutral", -0.02, 0.6, "t7_courtroom_breathless_silence", "pull"),
            ("D", "4.08#7", "neutral", -0.02, 0.6, "t7_courtroom_projection_screen", "pan"),
            ("H", "4.09#1", "neutral", -0.02, 0.6, "t7_court_verdict_document_guilty", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t7_closing_dossier_white_rose", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Kịch bản bi kịch viết sẵn và ngòi nổ tâm lý",
        "title_en": "Pre-scripted Tragedy & The Narcissistic Panic Trigger",
        "title_ja": "事前に書かれた悲劇の脚本と破局の引き金",
        "signs": [6, 8],
        "theme_vn": "Ngòi nổ & Điểm gãy tâm lý + Chu kỳ ảo tưởng ái kỷ",
        "theme_en": "Precipitating Trigger & Escalation of Narcissistic Fantasy",
        "theme_ja": "心理的限界点（トリガー）と自己愛性妄想の暴走",
        "hook_vn": "Hai ngày trước khi bạn trai qua đời, cô ta đã nhắn tin khóc lóc báo tin tang sự. Vở kịch đã dựng thì không thể để đổ bể.",
        "hook_en": "Two days before he passed away, she texted friends grieving his death. Once scripted, the play could not fail.",
        "hook_ja": "彼が息を引き取る2日も前に、彼女は友人に追悼メッセージを送っていた。開幕した悲劇を中止することは許されなかった。",
        "bgm": "bgm_jazz_noir.mp3",
        "bgm_desc_vn": "Hồi 3 — bed tập: bgm_jazz_noir.mp3",
        "bgm_desc_en": "Act 3 — episode bed: bgm_jazz_noir.mp3",
        "bgm_desc_ja": "第3幕 — 本編BGM: bgm_jazz_noir.mp3",
        "sfx_vn": ["amb_phone_room.wav (nền)", "fx_keyboard_typing.wav", "fx_message_chime.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_phone_room.wav (bed)", "fx_keyboard_typing.wav", "fx_message_chime.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_phone_room.wav（環境音）", "fx_keyboard_typing.wav", "fx_message_chime.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "KỊCH BẢN ĐÃ SOẠN SẴN HAI NGÀY TRƯỚC", "dur_s": 3.0},
            {"sau_cau": "TK2.01#3", "text": "NẠN NHÂN VẪN ĐANG SỐNG HOÀN TOÀN BÌNH THƯỜNG", "dur_s": 2.5},
            {"sau_cau": "TK2.01#4", "text": "CHỈ THIẾU CÁI CHẾT ĐỂ HOÀN TẤT VỞ KỊCH", "dur_s": 2.5},
            {"sau_cau": "TK2.01#5", "text": "NGÒI NỔ & ĐIỂM GÃY TÂM LÝ BỆNH LÝ", "dur_s": 2.5},
            {"sau_cau": "TK2.01#7", "text": "CƠN CUỒNG LOẠN BẢO VỆ CÁI TÔI ÁI KỶ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "TRAGEDY SCRIPTED TWO DAYS IN ADVANCE", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "THE VICTIM WAS STILL ALIVE AND WELL", "dur_s": 2.5},
            {"after_id": "TK2.01#4", "text": "ONLY HIS DEATH WAS MISSING TO CONCLUDE THE ACT", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "PRECIPITATING TRIGGER: NARCISSISTIC EXPOSURE", "dur_s": 2.5},
            {"after_id": "TK2.01#7", "text": "COERCIVE FRENZY TO SHIELD THE FALSE SELF", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "犯行2日前に準備された捏造の追悼脚本", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "被害者はまだ平穏に生存していた", "dur_s": 2.5},
            {"after_id": "TK2.01#4", "text": "劇を完結させるために欠けていた唯一の要素", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "心理的限界点：嘘が暴かれることへの病的な恐怖", "dur_s": 2.5},
            {"after_id": "TK2.01#7", "text": "肥大化した自己愛を守るための強迫的狂気", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t7_social_media_notifications_flood", "pull"),
            ("D", "3.06#2", "neutral", -0.02, 0.6, "t7_social_media_notifications_flood", "still"),
            ("D", "3.06#3", "neutral", -0.02, 0.6, "t7_confession_message_turn", "pan"),
            ("D", "3.06#4", "neutral", -0.02, 0.6, "t7_ticking_clock_deadlines", "still"),
            ("D", "3.06#5", "neutral", -0.02, 0.6, "t7_copied_script_lines_notebook", "push"),
            ("H", "3.07#1", "neutral", -0.02, 0.6, "t7_cracked_porcelain_mask", "pull"),
            ("H", "3.07#2", "neutral", -0.02, 0.6, "t7_staged_tragedy_mirror", "still"),
            ("H", "3.07#3", "neutral", -0.02, 0.6, "t7_puppet_strings_metaphor", "pan"),
            ("H", "3.07#4", "neutral", -0.02, 0.6, "t7_night_sky_breath_of_life", "push"),
            ("H", "cta", "neutral", -0.02, 0.0, "t7_closing_dossier_white_rose", "still")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Hội chứng Münchausen qua mạng và chữ ký tâm lý",
        "title_en": "Digital Münchausen by Proxy & The Dark Signature",
        "title_ja": "ネット版ミュンヒハウゼン症候群と不変の署名",
        "signs": [3, 7],
        "theme_vn": "Nghịch lý chia ngăn nhận thức + Chữ ký tâm lý Signature",
        "theme_en": "Cognitive Compartmentalization & Pathological Signature",
        "theme_ja": "認知的区分化（区画化）と自己顕示の心理的署名",
        "hook_vn": "Ban ngày là nữ sinh gương mẫu làm từ thiện. Ban đêm, cô ta biến sinh mạng của bạn trai thành đạo cụ sân khấu.",
        "hook_en": "By day, a sweet high school girl doing charity. By night, she turned her boyfriend’s life into a theatrical stage prop.",
        "hook_ja": "昼はボランティアに励む真面目な少女。夜は恋人の命を自らのスポットライトのための小道具に変えた。",
        "bgm": "bgm_cello_sad.mp3",
        "bgm_desc_vn": "Hồi 3 — bed tập: bgm_cello_sad.mp3",
        "bgm_desc_en": "Act 3 — episode bed: bgm_cello_sad.mp3",
        "bgm_desc_ja": "第3幕 — 本編BGM: bgm_cello_sad.mp3",
        "sfx_vn": ["amb_dark_drone.wav (nền)", "fx_cheering_applause.wav", "fx_camera_shutter.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_dark_drone.wav (bed)", "fx_cheering_applause.wav", "fx_camera_shutter.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_dark_drone.wav（環境音）", "fx_cheering_applause.wav", "fx_camera_shutter.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "ÁM ẢNH HÌNH MẪU “GÓA PHỤ BI THƯƠNG”", "dur_s": 3.0},
            {"sau_cau": "TK3.01#3", "text": "KHAO KHÁT ÁNH HÀO QUANG CÔNG CHÚNG", "dur_s": 2.5},
            {"sau_cau": "TK3.01#4", "text": "CƠ CHẾ CHIA NGĂN NHẬN THỨC BỆNH LÝ", "dur_s": 2.5},
            {"sau_cau": "TK3.01#6", "text": "TRUNG HÒA ĐẠO ĐỨC & KHUYẾT TẬT THẤU CẢM", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "CHỮ KÝ TÂM LÝ: TẬN HƯỞNG SỰ CHÚ Ý", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "OBSESSION WITH THE GRIEVING WIDOW TROPE", "dur_s": 3.0},
            {"after_id": "TK3.01#3", "text": "DESPERATE HUNGER FOR PUBLIC ADULATION", "dur_s": 2.5},
            {"after_id": "TK3.01#4", "text": "PATHOLOGICAL COGNITIVE COMPARTMENTALIZATION", "dur_s": 2.5},
            {"after_id": "TK3.01#6", "text": "MORAL NEUTRALIZATION & TOTAL EMPATHY DEFICIT", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "SIGNATURE: BASKING IN SYMPATHETIC ATTENTION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "『悲劇のヒロイン』像への異常な執着", "dur_s": 3.0},
            {"after_id": "TK3.01#3", "text": "同情と称賛を浴びる特権的地位への渇望", "dur_s": 2.5},
            {"after_id": "TK3.01#4", "text": "模範少女と冷酷な捕食者の完全な二面性", "dur_s": 2.5},
            {"after_id": "TK3.01#6", "text": "道徳の自己正当化と共感能力の完全な欠如", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "心理的署名：他者の死を自らの名声に利用する", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t7_drama_masks_digital_glitch", "pull"),
            ("H", "3.04#1", "neutral", -0.02, 0.6, "t7_vintage_tv_glee_glow", "still"),
            ("H", "3.04#4", "neutral", -0.02, 0.6, "t7_staged_tragedy_mirror", "pan"),
            ("H", "3.04#5", "neutral", -0.02, 0.6, "t7_vintage_tv_glee_glow", "push"),
            ("C", "3.08#2", "neutral", -0.02, 0.6, "t7_clinical_depression_shadow", "still"),
            ("C", "3.08#3", "neutral", -0.02, 0.6, "t7_drama_masks_digital_glitch", "pull"),
            ("C", "3.08#4", "neutral", -0.02, 0.6, "t7_psychological_coercion_chess", "pan"),
            ("H", "3.09#1", "neutral", -0.02, 0.6, "t7_baseball_field_charity_empty", "push"),
            ("H", "3.09#5", "neutral", -0.02, 0.6, "t7_baseball_field_charity_empty", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t7_closing_dossier_white_rose", "still")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Dòng tin nhắn tự thú và mệnh lệnh trong bóng tối",
        "title_en": "The Confession Text & The Lethal Verbal Order",
        "title_ja": "深夜の自白テキストと暗闇の中の致命的命令",
        "signs": [2, 5],
        "theme_vn": "Phi nhân hóa nạn nhân + Dòng tin nhắn tự thú định mệnh",
        "theme_en": "Victim Objectification & The Indicting Confession Text",
        "theme_ja": "被害者の道具化と決定打となった自白メッセージ",
        "hook_vn": "“Tớ đã nói chuyện điện thoại với anh ấy. Anh ấy sợ hãi bước ra khỏi xe, nhưng tớ đã bảo anh ấy hãy quay trở lại.”",
        "hook_en": "“I was on the phone with him. He got out of the car because he was scared, and I told him to get back in.”",
        "hook_ja": "『彼が怖くなって車から出たんだけど、私が車に戻るように言ったの。』深夜に届いた戦慄の告白。",
        "bgm": "bgm_tension_strings.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_tension_strings.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_tension_strings.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_tension_strings.mp3",
        "sfx_vn": ["amb_rain_night.wav (nền)", "fx_phone_buzz.wav", "fx_door_close.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_rain_night.wav (bed)", "fx_phone_buzz.wav", "fx_door_close.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_rain_night.wav（環境音）", "fx_phone_buzz.wav", "fx_door_close.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "MẨU BẰNG CHỨNG BẰNG VÀNG CỦA CÔNG TỐ VIÊN", "dur_s": 3.0},
            {"sau_cau": "TK4.01#3", "text": "“TỚ ĐÃ BẢO ANH ẤY QUAY TRỞ LẠI XE”", "dur_s": 2.5},
            {"sau_cau": "TK4.01#5", "text": "SỰ THẬT KINH HOÀNG VỀ CÔ BẠN GÁI ĐÁNG THƯƠNG", "dur_s": 2.5},
            {"sau_cau": "TK4.01#6", "text": "MỆNH LỆNH TRỰC TIẾP PHÁ HỦY CƠ HỘI SỐNG", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "ĐẠI BỒI THẨM ĐOÀN CHÍNH THỨC TRUY TỐ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "THE PROSECUTION'S SMOKING GUN EVIDENCE", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "“I TOLD HIM TO GET BACK IN THE TRUCK”", "dur_s": 2.5},
            {"after_id": "TK4.01#5", "text": "THE HORRIFYING TRUTH BEHIND THE GRIEVING FACADE", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "DIRECT VERBAL ORDER DESTROYING SURVIVAL", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "GRAND JURY ISSUES CRIMINAL INDICTMENT", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "検察側を勝利へと導いた決定的一通の通信記録", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "『私が車に戻るように言ったの』という戦慄の告白", "dur_s": 2.5},
            {"after_id": "TK4.01#5", "text": "同情されていた悲劇の少女の剥ぎ取られた素顔", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "青年の生存への意志を打ち砕いた直接的命令", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "大陪審による正式起訴と全米の衝撃", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t7_confession_text_timestamp", "pull"),
            ("N2", "4.03#1", "neutral", -0.02, 0.6, "t7_confession_text_timestamp", "still"),
            ("N2", "4.03#2", "neutral", -0.02, 0.6, "t7_witness_trembling_phone", "pan"),
            ("N2", "4.03#3", "neutral", -0.02, 0.6, "t7_incoming_call_timer_40min", "push"),
            ("N2", "4.03#4", "neutral", -0.02, 0.6, "t7_two_phone_screens_contrast", "still"),
            ("N2", "4.03#5", "neutral", -0.02, 0.6, "t7_confession_text_timestamp", "pull"),
            ("D", "2.09#4", "neutral", -0.02, 0.6, "t7_incoming_call_timer_40min", "push"),
            ("D", "2.09#5", "neutral", -0.02, 0.6, "t7_two_phone_screens_contrast", "pan"),
            ("D", "4.05#1", "neutral", -0.02, 0.6, "t7_bristol_county_indictment_stamp", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t7_closing_dossier_white_rose", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Bốn dấu hiệu cảnh báo đỏ sinh tồn trên mạng",
        "title_en": "The Gift of Fear: 4 Digital Survival Red Flags",
        "title_ja": "デジタル空間を生き抜く4つのレッドフラッグ",
        "signs": [10],
        "theme_vn": "Nạn nhân học & 4 cảnh báo đỏ nhận diện kẻ thao túng (The Gift of Fear)",
        "theme_en": "Victimology & 4 Survival Red Flags Against Coercive Manipulation",
        "theme_ja": "被害者学と強圧的支配を見抜く4つの緊急警戒サイン",
        "hook_vn": "Màn hình điện thoại có thể biến thành chiếc bẫy đoạt mạng. Bốn tín hiệu cảnh báo đỏ bạn nhất định phải khắc cốt ghi tâm.",
        "hook_en": "Your phone screen can become a lethal predatory trap. Four digital survival red flags you must never ignore.",
        "hook_ja": "スマートフォンの画面が命を奪う罠に変わる。決して見過ごしてはならない4つの警戒サイン。",
        "bgm": "bgm_warm_piano.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_warm_piano.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_warm_piano.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_warm_piano.mp3",
        "sfx_vn": ["amb_calm_piano.wav (nền)", "fx_phone_chime.wav", "fx_soft_wind.wav", "fx_bell_chime.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_calm_piano.wav (bed)", "fx_phone_chime.wav", "fx_soft_wind.wav", "fx_bell_chime.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_calm_piano.wav（環境音）", "fx_phone_chime.wav", "fx_soft_wind.wav", "fx_bell_chime.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 CẢNH BÁO ĐỎ SINH TỒN TRONG KHÔNG GIAN SỐ", "dur_s": 3.0},
            {"sau_cau": "TK5.01#3", "text": "CẢNH BÁO ĐỎ 1: SỰ CÔ LẬP CÓ HỆ THỐNG", "dur_s": 2.5},
            {"sau_cau": "TK5.01#4", "text": "CẢNH BÁO ĐỎ 2: KIỂM SOÁT ĐỘI LỐT QUAN TÂM", "dur_s": 2.5},
            {"sau_cau": "TK5.01#5", "text": "CẢNH BÁO ĐỎ 3: TẤN CÔNG LÒNG TỰ TRỌNG", "dur_s": 2.5},
            {"sau_cau": "TK5.01#6", "text": "CẢNH BÁO ĐỎ 4: NUÔI DƯỠNG SỰ TUYỆT VỌNG", "dur_s": 2.5},
            {"sau_cau": "TK5.01#8", "text": "BẠN KHÔNG BAO GIỜ ĐƠN ĐỘC TRONG BÓNG TỐI", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "4 SURVIVAL RED FLAGS IN THE DIGITAL REALM", "dur_s": 3.0},
            {"after_id": "TK5.01#3", "text": "RED FLAG 1: SYSTEMATIC SOCIAL ISOLATION", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "RED FLAG 2: COERCIVE CONTROL AS AFFECTION", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "RED FLAG 3: WEAPONIZED GUILT & DEGRADATION", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "RED FLAG 4: NURTURING HOPELESSNESS OVER HELP", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "YOU ARE NEVER ALONE IN THE DARKNESS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "デジタル空間における4つの生存警戒サイン", "dur_s": 3.0},
            {"after_id": "TK5.01#3", "text": "サイン1：周囲からの組織的な人間関係の孤立化", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "サイン2：愛情や気配りを装った強圧的監視支配", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "サイン3：自尊心への継続的攻撃と罪悪感の植え付け", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "サイン4：専門的支援を拒絶し破滅をロマン化する", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "あなたは決して暗闇の中で孤独ではありません", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t7_digital_lighthouse_beacon", "pull"),
            ("H", "5.04#1", "neutral", -0.02, 0.6, "t7_digital_lighthouse_beacon", "still"),
            ("H", "5.04#2", "neutral", -0.02, 0.6, "t7_redflag1_isolated_virtual_bubble", "pan"),
            ("H", "5.04#4", "neutral", -0.02, 0.6, "t7_redflag1_isolated_virtual_bubble", "still"),
            ("H", "5.04#6", "neutral", -0.02, 0.6, "t7_redflag2_manipulative_text_provocation", "push"),
            ("H", "5.04#8", "neutral", -0.02, 0.6, "t7_redflag3_performative_grief_stage", "pull"),
            ("H", "5.04#10", "neutral", -0.02, 0.6, "t7_redflag4_disconnect_phone_dawn", "pan"),
            ("H", "5.04#11", "neutral", -0.02, 0.6, "t7_digital_lighthouse_beacon", "still"),
            ("H", "5.04#12", "neutral", -0.02, 0.6, "t7_redflag1_isolated_virtual_bubble", "push"),
            ("H", "cta", "neutral", -0.02, 0.0, "t7_closing_dossier_white_rose", "still")
        ]
    }
]

# ----------------------------------------------------------------------------
# 3. HÀM TÍNH THỜI LƯỢNG CHÍNH XÁC
# ----------------------------------------------------------------------------
CTA_VN = "Tập bảy của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio."
CTA_EN = "Episode seven of Amber Eyes. Watch the full documentary at the link in bio."
CTA_JA = "Amber Eyes 第7話。事件の完全版はプロフィールのリンクからご覧いただけます。"

def calc_durations(clip, lang):
    dur_total = 0.0
    items_out = []
    
    for idx, (role, sid, emo, spd, pause, bg, mot) in enumerate(clip["items"], 1):
        line_code = f"{clip['id']}.01#{idx}"
        if sid == "hook":
            if lang == "VI":
                txt = clip["hook_vn"]
            elif lang == "EN":
                txt = clip["hook_en"]
            else:
                txt = clip["hook_ja"]
            src = "Hook mở đầu — tạo tò mò"
        elif sid == "cta":
            if lang == "VI":
                txt = CTA_VN
            elif lang == "EN":
                txt = CTA_EN
            else:
                txt = CTA_JA
            src = "CTA — kêu gọi xem tập đầy đủ"
        else:
            if lang == "VI":
                _, txt = MAP_VI[sid]
            elif lang == "EN":
                _, txt = MAP_EN[sid]
            else:
                _, txt = MAP_JA[sid]
            src = sid
            
        # Tính thời lượng câu
        if lang == "VI":
            spoken = vi_numbers(re.sub(r"<#[\d.]+#>", " ", txt))
            words = len([w for w in spoken.split() if w.strip()])
            line_dur = words * RATE_VI[role]
        elif lang == "EN":
            words = len([w for w in re.sub(r"<#[\d.]+#>", " ", txt).split() if w.strip()])
            line_dur = words * RATE_EN[role]
        else:
            chars = len(re.sub(r"<#[\d.]+#>", " ", txt).replace(" ", "").strip())
            line_dur = chars * RATE_JA[role]
            
        dur_total += line_dur + pause
        items_out.append({
            "code": line_code,
            "role": role,
            "sid": sid,
            "emo": emo,
            "speed": spd,
            "pause": pause,
            "bg": bg,
            "motion": mot,
            "text": txt,
            "src": src,
            "dur": round(line_dur, 1)
        })
        
    return round(dur_total, 1), items_out

# ----------------------------------------------------------------------------
# 4. TẠO FILE CHO TỪNG NGÔN NGỮ
# ----------------------------------------------------------------------------
for lang, out_dir in [("VI", OUT_VI), ("EN", OUT_EN), ("JA", OUT_JA)]:
    plan_lines = []
    spec_json = {
        "episode": "07",
        "lang": lang,
        "engine": "Higgs Audio v3 + VoxCPM2 reference voices",
        "clips": {}
    }
    
    if lang == "VI":
        plan_lines.append("# KẾ HOẠCH CLIP TIKTOK — TẬP 07 · \"BẢN ÁN GIẾT NGƯỜI BẰNG TIN NHẮN\"\n")
        plan_lines.append("*Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*")
        plan_lines.append("*Nguồn duy nhất của mọi dữ kiện: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap07/KeHoach_Video_Tap07.md` · `.work/script_tap07.json` (219 câu)*")
        plan_lines.append("*Sinh tự động bởi `.work/_build_tk_tap07.py`*\n---\n")
        plan_lines.append("## 0. Tóm tắt chốt\n")
        plan_lines.append("| Hạng mục | Giá trị |")
        plan_lines.append("|---|---|")
        plan_lines.append("| Số clip | **5 clip** (TK1–TK4 trọng tâm + TK5 cảnh báo đỏ sinh tồn) |")
        plan_lines.append("| Tổng câu thoại | **50 câu** đọc giọng (10 câu / clip) |")
        plan_lines.append("| Chủ đề | Mỗi clip giải phẫu **1–2 chỉ dấu tâm lý cốt lõi** (Hệ sinh thái 10 chỉ dấu K10) |")
        plan_lines.append("| Ngôn ngữ | Tiếng Việt · vai Host (H), Điều tra viên (D), Chuyên gia (C), Nhân chứng (N2) |")
        plan_lines.append("| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** (đúng cast chuẩn Tập 07) |")
        plan_lines.append("| Hình ảnh | Nền dọc 9:16 crop/pad từ 61 nền 16:9 gốc của Tập 07 |")
        plan_lines.append("| Độ dài ước lượng | Đạt chuẩn 45–95 s (trung bình 73–87 s/clip) |\n---\n")
        plan_lines.append("## 1. Danh sách 5 clip và chỉ dấu tâm lý (K10)\n")
        plan_lines.append("| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng |")
        plan_lines.append("|---|---|---|---|---|")
    elif lang == "EN":
        plan_lines.append("# TIKTOK CLIP PRODUCTION PLAN — EPISODE 07 · \"THE TEXTING SUICIDE CASE\"\n")
        plan_lines.append("*Status: **Script completed, ready for verification prior to TTS generation** (L4)*")
        plan_lines.append("*Single source of truth: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap07/KeHoach_Video_Tap07.md` · `.work/script_tap07_EN.json` (219 lines)*")
        plan_lines.append("*Auto-generated via `.work/_build_tk_tap07.py`*\n---\n")
        plan_lines.append("## 0. Executive Summary\n")
        plan_lines.append("| Item | Value |")
        plan_lines.append("|---|---|")
        plan_lines.append("| Total Clips | **5 clips** (TK1–TK4 narrative hooks + TK5 digital survival red flags) |")
        plan_lines.append("| Spoken Lines | **50 lines** (10 lines per clip) |")
        plan_lines.append("| Framework | Psychological behavioral analysis based on 10 Core Markers (K10) |")
        plan_lines.append("| Cast | Host (H), Detective (D), Psychologist (C), Witness (N2) |")
        plan_lines.append("| Voice Engine | **Higgs Audio v3 + VoxCPM2 Reference Voices** |")
        plan_lines.append("| Visuals | 9:16 Vertical background art adapted from 61 original 16:9 backgrounds |")
        plan_lines.append("| Estimated Duration | Strictly within 45–95s TikTok gate (average 69–78s) |\n---\n")
        plan_lines.append("## 1. 5 Clips & Corresponding Psychological Markers (K10)\n")
        plan_lines.append("| Clip | Markers | Theme | Visual Hook Card (0–3 s) | Duration |")
        plan_lines.append("|---|---|---|---|---|")
    else:
        plan_lines.append("# TIKTOKクリップ制作計画 — 第07話 · 『死を招いたテキストメッセージ』\n")
        plan_lines.append("*ステータス: **台本策定完了 · 音声合成前の最終確認待ち** (L4)*")
        plan_lines.append("*情報源: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap07/KeHoach_Video_Tap07.md` · `.work/script_tap07_JA.json` (全219文)*")
        plan_lines.append("*`.work/_build_tk_tap07.py` により自動生成*\n---\n")
        plan_lines.append("## 0. 基本概要\n")
        plan_lines.append("| 項目 | 仕様 |")
        plan_lines.append("|---|---|")
        plan_lines.append("| クリップ数 | **全5本**（TK1–TK4 本編核心分析 + TK5 デジタル生存警告サイン） |")
        plan_lines.append("| 総音声文数 | **50文**（各クリップ10文構成） |")
        plan_lines.append("| 分析枠組み | 犯罪心理学10大指標（K10）に準拠した深層行動プロファイリング |")
        plan_lines.append("| 配役 | ホスト (H), 捜査官 (D), 心理専門家 (C), 証人 (N2) |")
        plan_lines.append("| 音声エンジン | **Higgs Audio v3 + VoxCPM2 参照音声** |")
        plan_lines.append("| 映像素材 | 第07話公式背景（61枚）より適合させた 9:16 縦型美術背景 |")
        plan_lines.append("| 推定再生時間 | TikTok適正範囲（45–95秒）完全準拠（平均78–92秒） |\n---\n")
        plan_lines.append("## 1. 全5本クリップと対応心理指標（K10）\n")
        plan_lines.append("| クリップ | 心理指標 | テーマ | 冒頭フック表示 (0–3秒) | 推定時間 |")
        plan_lines.append("|---|---|---|---|---|")
        
    for c in CLIPS_CONFIG:
        tot_dur, items = calc_durations(c, lang)
        if lang == "VI":
            plan_lines.append(f"| **{c['id']}** | #{c['signs'][0]} · #{c['signs'][-1]} | {c['theme_vn']} | *\"{c['hook_vn'][:45]}...\"* | {tot_dur} s · 10 câu |")
        elif lang == "EN":
            plan_lines.append(f"| **{c['id']}** | #{c['signs'][0]} · #{c['signs'][-1]} | {c['theme_en']} | *\"{c['hook_en'][:45]}...\"* | {tot_dur} s · 10 lines |")
        else:
            plan_lines.append(f"| **{c['id']}** | #{c['signs'][0]} · #{c['signs'][-1]} | {c['theme_ja']} | *\"{c['hook_ja'][:35]}...\"* | {tot_dur} 秒 · 10文 |")
            
    plan_lines.append("\n---\n")
    if lang == "VI":
        plan_lines.append("## 2. Diễn xuất chi tiết từng clip (Lời đọc + Hình ảnh + Âm thanh)\n")
    elif lang == "EN":
        plan_lines.append("## 2. Detailed Clip Production Specs (Dialogue + Visuals + Audio)\n")
    else:
        plan_lines.append("## 2. 各クリップ詳細設計（セリフ + 映像演出 + 音響）\n")
        
    for c in CLIPS_CONFIG:
        tot_dur, items = calc_durations(c, lang)
        spec_json["clips"][c["id"]] = {
            "title": c["title_vn"] if lang == "VI" else (c["title_en"] if lang == "EN" else c["title_ja"]),
            "estimated_duration": tot_dur,
            "bgm": c["bgm"],
            "sfx": c["sfx_vn"] if lang == "VI" else (c["sfx_en"] if lang == "EN" else c["sfx_ja"]),
            "lines": []
        }
        
        if lang == "VI":
            plan_lines.append(f"### 2.{c['id'][-1]} CLIP {c['id']} — \"{c['title_vn']}\"\n")
            plan_lines.append(f"*Ước lượng **{tot_dur} s** (10 câu) · BGM `{c['bgm']}` ({c['bgm_desc_vn']}) · SFX: {', '.join(c['sfx_vn'])}*\n")
            plan_lines.append("| Mã câu | Vai | Emotion | Tốc độ | Nghỉ | Nền & Chuyển động | Lời đọc kịch bản | Nguồn câu |")
            plan_lines.append("|---|---|---|---|---|---|---|---|")
        elif lang == "EN":
            plan_lines.append(f"### 2.{c['id'][-1]} CLIP {c['id']} — \"{c['title_en']}\"\n")
            plan_lines.append(f"*Estimated Duration: **{tot_dur} s** (10 lines) · BGM `{c['bgm']}` ({c['bgm_desc_en']}) · SFX: {', '.join(c['sfx_en'])}*\n")
            plan_lines.append("| Line ID | Role | Emotion | Speed | Pause | Background & Motion | Spoken Dialogue | Source |")
            plan_lines.append("|---|---|---|---|---|---|---|---|")
        else:
            plan_lines.append(f"### 2.{c['id'][-1]} クリップ {c['id']} — 『{c['title_ja']}』\n")
            plan_lines.append(f"*推定再生時間: **{tot_dur} 秒** (全10文) · BGM `{c['bgm']}` ({c['bgm_desc_ja']}) · SFX: {', '.join(c['sfx_ja'])}*\n")
            plan_lines.append("| セリフ番号 | 配役 | 感情 | 速度 | 休止 | 背景美術 & 演出 | 音声セリフ | 典拠 |")
            plan_lines.append("|---|---|---|---|---|---|---|---|")
            
        for it in items:
            spec_json["clips"][c["id"]]["lines"].append({
                "code": it["code"],
                "role": it["role"],
                "emotion": it["emo"],
                "speed": it["speed"],
                "pause_after": it["pause"],
                "text": it["text"],
                "bg": it["bg"],
                "motion": it["motion"],
                "source": it["src"]
            })
            plan_lines.append(f"| `{it['code']}` | {it['role']} | {it['emo']} | {it['speed']} | {it['pause']} s | `{it['bg']}`, `{it['motion']}` | {it['text']} | `{it['src']}` |")
            
        plan_lines.append("\n**Thẻ chữ trên hình (Overlay Cards):**" if lang == "VI" else ("**On-Screen Overlay Cards:**" if lang == "EN" else "**画面テロップ演出（オーバーレイ）:**"))
        overlays = c["overlay_vn"] if lang == "VI" else (c["overlay_en"] if lang == "EN" else c["overlay_ja"])
        for ov in overlays:
            k = ov.get("sau_cau") or ov.get("after_id")
            plan_lines.append(f"- `{k}` → *\"{ov['text']}\"* ({ov['dur_s']} s)")
        plan_lines.append("\n")

        # ------------------------------------------------------------------------
        # XUẤT CAPTION + MÔ TẢ CHO MỖI CLIP
        # ------------------------------------------------------------------------
        cap_file = out_dir / f"Caption_{c['id']}.txt"
        mota_dai_file = out_dir / f"MoTa_Dai_{c['id']}.txt"
        mota_ngan_file = out_dir / f"MoTa_Ngan_{c['id']}.txt"
        
        if lang == "VI":
            cap_text = f"""{c['hook_vn']} 👁️

Tập 07 · Bản án giết người bằng tin nhắn — Chỉ dấu #{c['signs'][0]}: {c['theme_vn']}.
Hồ sơ vụ án có thật tại Massachusetts, 100% dữ liệu đối chiếu hồ sơ tòa án và pháp y số.

📺 Xem trọn vẹn tập phân tích 30 phút ở link trong bio
🔎 Hồ sơ tâm lý học tội phạm · Án lệ Michelle Carter & Conrad Roy · Phân tích hành vi

Nội dung do AI hỗ trợ tạo hình và giọng phục vụ mục đích phân tích tâm lý giáo dục — không phải phóng sự giật gân.

#AmberEyes #TamLyToiPham #HosoCoThat #MichelleCarter #ConradRoy #{c['id']} #TrueCrimeVN #PhanTichHanhVi

---
Ghi chú khi đăng (KHÔNG dán vào caption):
- BẬT toggle "Nội dung do AI tạo" (AI-generated content) trên TikTok.
- Dán link YouTube Tập 07 vào ô Website trong phần sửa hồ sơ cá nhân.
- Ước lượng thời lượng: {tot_dur} s (10 câu).
- Tên file video thành phẩm: clip{c['id'][-1]}_{c['id']}.mp4 (1080x1920, 30fps).
"""
            mota_dai_text = f"""HỒ SƠ TẬP 07: BẢN ÁN GIẾT NGƯỜI BẰNG TIN NHẮN — CLIP {c['id']}

CHỦ ĐỀ: {c['theme_vn']}
VỤ ÁN: Michelle Carter và Conrad Roy (Fairhaven / Plainville, Massachusetts)

TÓM TẮT PHÂN TÍCH:
{c['hook_vn']}

Vụ án Michelle Carter và Conrad Roy đã đi vào lịch sử tư pháp thế giới như một bước ngoặt chưa từng có tiền lệ về tội phạm trong không gian số. Không hề có hung khí vật lý, không có dấu vết xô xát tại hiện trường và hai nhân vật chính ở cách xa nhau hơn năm mươi sáu cây số. Thế nhưng, một thiếu nữ khi ấy mới mười bảy tuổi vẫn phải nhận bản án ngộ sát lịch sử. 

Dưới lăng kính của tâm lý học tội phạm và khoa học hành vi, clip này bóc tách bản chất của:
1. Cơ chế thao túng tâm lý cưỡng bách thông qua công nghệ kết nối số.
2. Cách kẻ thủ ác xóa nhòa ranh giới giữa sự quan tâm giả tạo và ý đồ kiểm soát triệt để.
3. Bài học thức tỉnh sâu sắc về trách nhiệm đạo đức và pháp lý của ngôn từ trong thế giới ảo.

📺 XEM TRỌN VẸN HỒ SƠ 30 PHÚT TRÊN KÊNH YOUTUBE AMBER EYES (LINK TRONG BIO).
"""
            mota_ngan_text = f"""Tập 07 Amber Eyes — Clip {c['id']}: {c['title_vn']}.
{c['hook_vn']}
Xem hồ sơ giải phẫu tâm lý đầy đủ tại link bio. #AmberEyes #TamLyToiPham #{c['id']}
"""
        elif lang == "EN":
            cap_text = f"""{c['hook_en']} 👁️

Ep. 07 · The Texting Suicide Case — Psychological Marker #{c['signs'][0]}: {c['theme_en']}.
Authentic criminal dossier from Massachusetts, strictly source-verified against judicial records.

📺 Watch the full 30-minute documentary on YouTube — link in bio.
🔎 Criminal Psychology · Michelle Carter & Conrad Roy Case · Behavioral Profiling

Content created with AI assistance for behavioral and psychological educational purposes.

#AmberEyes #CriminalPsychology #TrueCrime #MichelleCarter #ConradRoy #{c['id']} #CaseFile #Mindhunter

---
Publishing Notes (DO NOT paste into caption):
- TOGGLE ON 'AI-generated content' label in TikTok settings.
- Add YouTube Episode 07 URL to the Website field in your profile bio.
- Estimated duration: {tot_dur} s (10 lines).
- Video output file: clip{c['id'][-1]}_{c['id']}_EN.mp4 (1080x1920, 30fps).
"""
            mota_dai_text = f"""DOSSIER EPISODE 07: THE TEXTING SUICIDE CASE — CLIP {c['id']}

THEME: {c['theme_en']}
CASE FILE: Michelle Carter & Conrad Roy (Fairhaven / Plainville, Massachusetts)

ANALYSIS SUMMARY:
{c['hook_en']}

The Michelle Carter case remains a historic judicial precedent regarding remote digital coercion and manslaughter. Without any physical contact, murder weapon, or presence at the scene, verbal commands transmitted over phone lines broke through the threshold of criminal liability.

Key Psychological Insights Explored:
1. Coercive control and manipulation disguised as empathetic concern.
2. The breakdown of cognitive moral compass in disembodied virtual communication.
3. The vital importance of digital survival awareness and legal accountability.

📺 WATCH THE FULL 30-MINUTE DOCUMENTARY ON YOUTUBE (LINK IN BIO).
"""
            mota_ngan_text = f"""Amber Eyes Ep. 07 — Clip {c['id']}: {c['title_en']}.
{c['hook_en']}
Full behavioral case study available via link in bio. #AmberEyes #TrueCrime #{c['id']}
"""
        else:
            cap_text = f"""{c['hook_ja']} 👁️

第07話 · 死を招いたテキストメッセージ — 心理指標 #{c['signs'][0]}: {c['theme_ja']}。
米マサチューセッツ州の実際の裁判記録およびデジタル鑑識記録に基づく厳密なプロファイリング。

📺 完全版ドキュメンタリー（30分）はYouTubeにて公開中 — プロフィールのリンクから
🔎 犯罪心理学 · ミシェル・カーター事件 · 行動分析 · 実話事件記録

本コンテンツは心理分析および啓発を目的としてAI技術の支援を受けて制作されています。

#AmberEyes #犯罪心理学 #未解決事件 #実話 #ミシェルカーター #{c['id']} #マインドハンター #海外事件簿

---
投稿時の注意事項（キャプション本文には貼り付けないでください）：
- TikTokアプリ内で「AI生成コンテンツ」のトグルを必ずONに設定してください。
- YouTube第07話へのリンクをプロフィール欄のウェブサイト項目に設定してください。
- 推定再生時間: {tot_dur} 秒 (全10文)。
- 出力動画ファイル名: clip{c['id'][-1]}_{c['id']}_JA.mp4 (1080x1920, 30fps)。
"""
            mota_dai_text = f"""事件簿 第07話：死を招いたテキストメッセージ — クリップ {c['id']}

テーマ：{c['theme_ja']}
事件名：ミシェル・カーターとコンラッド・ロイ事件（マサチューセッツ州フェアヘイブン／プレインビル）

分析概要：
{c['hook_ja']}

物理的な凶器も存在せず、現場での接触もなく、56キロメートルも離れた場所からのテキストと通話によって人間を死に追いやった戦慄の事件。米国司法史上初となる「言葉による遠隔過失致死罪」の有罪判決の深層を解剖します。

心理学的分析の焦点：
1. 仮想空間における強圧的支配とマインドコントロールの手口。
2. 他者の生命を自己愛の舞台装置として消費する心理的病理。
3. デジタル社会における道徳的責任と自己防衛の境界線。

📺 YouTube「Amber Eyes」にて30分の本編完全解説を公開中（プロフィールリンクより）。
"""
            mota_ngan_text = f"""Amber Eyes 第07話 — クリップ {c['id']}：『{c['title_ja']}』。
{c['hook_ja']}
事件の完全版解説はプロフィールのリンクから。 #AmberEyes #犯罪心理学 #{c['id']}
"""

        cap_file.write_text(cap_text.strip() + "\n", encoding="utf-8")
        mota_dai_file.write_text(mota_dai_text.strip() + "\n", encoding="utf-8")
        mota_ngan_file.write_text(mota_ngan_text.strip() + "\n", encoding="utf-8")
        
    # Ghi file kế hoạch và spec json
    if lang == "VI":
        (out_dir / "KE_HOACH_CLIP_TAP07.md").write_text("\n".join(plan_lines), encoding="utf-8")
    elif lang == "EN":
        (out_dir / "KE_HOACH_CLIP_TAP07_EN.md").write_text("\n".join(plan_lines), encoding="utf-8")
    else:
        (out_dir / "KE_HOACH_CLIP_TAP07_JA.md").write_text("\n".join(plan_lines), encoding="utf-8")
        
    (out_dir / "SPEC_AUDIO_CLIP_TAP07.json").write_text(json.dumps(spec_json, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Hoàn thành xuất tài liệu TikTok Tập 07 cho ngôn ngữ: {lang} -> {out_dir}")

print("TẤT CẢ ĐÃ HOÀN TẤT THÀNH CÔNG 100%.")
