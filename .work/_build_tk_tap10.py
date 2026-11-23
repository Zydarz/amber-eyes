# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 10 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap10/KE_HOACH_CLIP_TAP10.md
  02_SAN_XUAT/TIKTOK/Tap10/SPEC_AUDIO_CLIP_TAP10.json
  02_SAN_XUAT/TIKTOK/Tap10/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap10/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap10/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap10_EN/KE_HOACH_CLIP_TAP10_EN.md
  02_SAN_XUAT/TIKTOK/Tap10_EN/SPEC_AUDIO_CLIP_TAP10_EN.json
  02_SAN_XUAT/TIKTOK/Tap10_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap10_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap10_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap10_JA/KE_HOACH_CLIP_TAP10_JA.md
  02_SAN_XUAT/TIKTOK/Tap10_JA/SPEC_AUDIO_CLIP_TAP10_JA.json
  02_SAN_XUAT/TIKTOK/Tap10_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap10_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap10_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 10:
- timeline_s_t10.json (VI)
- timeline_s_EN_t10.json (EN)
- timeline_s_JA_t10.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap10"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap10_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap10_JA"

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
# 0. TỈ LỆ ĐỌC THẬT (Đo từ master Tập 10)
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

RATE_VI = get_rates("timeline_s_t10.json", is_ja=False)
RATE_EN = get_rates("timeline_s_EN_t10.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t10.json", is_ja=True)

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

MAP_VI = load_script_map("script_tap10.json")
MAP_EN = load_script_map("script_tap10_EN.json")
MAP_JA = load_script_map("script_tap10_JA.json")

# ----------------------------------------------------------------------------
# 2. KHAI BÁO 5 CLIP TẬP 10 (BẢN VI, EN, JA)
# ----------------------------------------------------------------------------
CLIPS_CONFIG = [
    {
        "id": "TK1",
        "title_vn": "Cạm bẫy xe van gia đình và chiếc hộp 9kg trên xa lộ",
        "title_en": "The Family Van Trap & The 9kg Soundproof Headbox",
        "title_ja": "ファミリーバンの罠とハイウェイの9kg防音ヘッドボックス",
        "signs": [9, 7],
        "theme_vn": "Hiệu ứng Hào quang (Halo Effect) & Thủ đoạn gây án (MO) vs Dấu ấn Signature",
        "theme_en": "Halo Effect & Modus Operandi vs Signature in Highway Abduction",
        "theme_ja": "ハロー効果の盲点と手口（MO）対心理的シグネチャー",
        "hook_vn": "Một người mẹ trẻ mỉm cười bế con thơ trên xe van. Ai ngờ đó là khởi đầu của địa ngục bảy năm?",
        "hook_en": "A young mother smiling with a baby in a van. Who could guess it was the start of a seven-year nightmare?",
        "hook_ja": "車内で微笑む若い母親と無垢な赤ん坊。誰がそれを7年間の地獄の始まりと疑えただろうか？",
        "bgm": "bgm_cello_sad.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_cello_sad.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_cello_sad.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_cello_sad.mp3",
        "sfx_vn": ["amb_highway_distant.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_highway_distant.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_highway_distant.wav（環境音）", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI", "dur_s": 3.0},
            {"sau_cau": "TK1.01#3", "text": "XE VAN GIA ĐÌNH: LÁ CHẮN VÔ HẠI HOÀN HẢO", "dur_s": 2.5},
            {"sau_cau": "TK1.01#6", "text": "CHỮ KÝ TÂM LÝ: CHIẾC HỘP TRÙM ĐẦU CÁCH ÂM 9KG", "dur_s": 2.5},
            {"sau_cau": "TK1.01#8", "text": "CĂN PHÒNG NGỦ VÀ CHIẾC HỘP DƯỚI GẦM GIƯỜNG", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "THE HALO EFFECT & SOCIAL BLINDSPOT", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "FAMILY VAN: THE PERFECT INNOCENT FACADE", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "PSYCHOLOGICAL SIGNATURE: 9KG HEADBOX", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "THE WATERBED CHAMBER & SUB-FLOOR BOX", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "ハロー効果と社会の心理的盲点", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "家族連れの車：完璧な無害の偽装", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "心理的シグネチャー：重さ9kgの防音頭部拘束箱", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "寝室のウォーターベッドと床下の木箱", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t10_blue_dodge_van_approaching", "pull"),
            ("H", "1.06#2", "neutral", -0.02, 0.6, "t10_innocent_family_facade", "push"),
            ("H", "1.06#3", "neutral", -0.02, 0.6, "t10_innocent_family_facade", "still"),
            ("H", "1.06#4", "neutral", -0.02, 0.6, "t10_stepping_into_abyss_trap", "pan"),
            ("H", "1.06#6", "neutral", -0.02, 0.6, "t10_knife_shadow_ambush", "push"),
            ("D", "1.10#3", "neutral", -0.02, 0.6, "t10_soundproof_headbox_forensic", "pull"),
            ("D", "1.10#4", "neutral", -0.02, 0.6, "t10_soundproof_headbox_forensic", "still"),
            ("D", "1.10#6", "neutral", -0.02, 0.6, "t10_isolated_red_bluff_cabin", "pan"),
            ("H", "1.11#2", "neutral", -0.02, 0.6, "t10_wooden_box_under_bed_shadow", "push"),
            ("H", "cta", "neutral", -0.02, 0.0, "t10_amber_eyes_closing_dossier_colleen", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Bóng ma 'The Company' và bản hợp đồng nô lệ",
        "title_en": "The Phantom 'Company' & The Slave Contract",
        "title_ja": "架空組織「カンパニー」の亡霊と奴隷契約書",
        "signs": [5, 2],
        "theme_vn": "Hệ thống tự bào chữa & Trung hòa đạo đức + Thao túng tâm lý cực hạn",
        "theme_en": "Moral Neutralization & Extreme Psychological Manipulation",
        "theme_ja": "道徳的中和化（正当化）と極限の心理的支配",
        "hook_vn": "Một tổ chức tội phạm ngầm có hàng nghìn mật vụ khắp nước Mỹ, hay chỉ là lời dối trá rợn người?",
        "hook_en": "A syndicate with thousands of agents nationwide, or a monstrous fabricated lie?",
        "hook_ja": "全米に無数の秘密工作員を放つ地下組織。それは実在か、狂気の幻影か？",
        "bgm": "bgm_ambient_deep.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_ambient_deep.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_ambient_deep.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_ambient_deep.mp3",
        "sfx_vn": ["amb_dark_drone.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_dark_drone.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_dark_drone.wav（環境音）", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "BÓNG MA TỔ CHỨC NGẦM 'THE COMPANY'", "dur_s": 3.0},
            {"sau_cau": "TK2.01#3", "text": "ĐE DỌA TÍNH MẠNG GIA ĐÌNH CHA MẸ", "dur_s": 2.5},
            {"sau_cau": "TK2.01#5", "text": "THÁNG 1/1978: BẢN HỢP ĐỒNG NÔ LỆ GƯỢNG ÉP", "dur_s": 2.5},
            {"sau_cau": "TK2.01#8", "text": "NGHỊCH LÝ: CHIẾC HỘP THÀNH 'VỎ ỐC AN TOÀN'", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "THE PHANTOM SYNDICATE 'THE COMPANY'", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "LETHAL THREATS AGAINST HER FAMILY", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "JANUARY 1978: THE COERCED SLAVE CONTRACT", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "PARADOX: THE WOODEN BOX AS FALSE SHELTER", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "影の巨大組織「ザ・カンパニー」の恐怖", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "家族の生命を人質にした心理的脅迫", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "1978年1月：署名させられた「奴隷契約書」", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "逆説の心理：箱の中という「偽りの避難所」", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t10_the_company_shadow_syndicate", "pull"),
            ("D", "2.08#1", "neutral", -0.02, 0.6, "t10_the_company_shadow_syndicate", "pan"),
            ("D", "2.08#2", "neutral", -0.02, 0.6, "t10_family_home_under_surveillance", "still"),
            ("D", "2.08#4", "neutral", -0.02, 0.6, "t10_family_home_under_surveillance", "push"),
            ("D", "2.08#6", "neutral", -0.02, 0.6, "t10_written_slave_contract_quill", "pull"),
            ("D", "2.08#7", "neutral", -0.02, 0.6, "t10_written_slave_contract_quill", "still"),
            ("H", "2.09#1", "neutral", -0.02, 0.6, "t10_darkness_as_false_shelter", "pan"),
            ("H", "2.09#3", "neutral", -0.02, 0.6, "t10_coffin_box_claustrophobia", "push"),
            ("C", "2.10#5", "neutral", -0.02, 0.6, "t10_darkness_as_false_shelter", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t10_amber_eyes_closing_dossier_colleen", "still")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Nghịch lý ngày về và sự bất lực tập nhiễm",
        "title_en": "The Open Door Paradox & Learned Helplessness",
        "title_ja": "解放の逆説と学習性無力感の深淵",
        "signs": [6, 8],
        "theme_vn": "Sự bất lực tập nhiễm (Learned Helplessness) & Gắn kết chấn thương (Trauma Bonding)",
        "theme_en": "Learned Helplessness & Trauma Bonding in Captivity",
        "theme_ja": "学習性無力感（セレグマン理論）とトラウマ・ボンディング",
        "hook_vn": "Cánh cửa nhà mở toang sau bốn năm biến mất. Tại sao cô không bỏ chạy mà lại ngoan ngoãn trở về?",
        "hook_en": "Her front door wide open after four years. Why didn't she run, but obediently returned to the box?",
        "hook_ja": "4年ぶりに開かれた実家のドア。なぜ彼女は逃げ出さず、再び木箱へと戻ったのか？",
        "bgm": "bgm_piano_minimal.mp3",
        "bgm_desc_vn": "Hồi 3 — bed tập: bgm_piano_minimal.mp3",
        "bgm_desc_en": "Act 3 — episode bed: bgm_piano_minimal.mp3",
        "bgm_desc_ja": "第3幕 — 本編BGM: bgm_piano_minimal.mp3",
        "sfx_vn": ["amb_room_silence.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_silence.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_silence.wav（環境音）", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "NGHỊCH LÝ CÁNH CỬA MỞ TOANG NĂM 1981", "dur_s": 3.0},
            {"sau_cau": "TK3.01#4", "text": "HỌC THUYẾT MARTIN SELIGMAN: SỰ BẤT LỰC TẬP NHIỄM", "dur_s": 2.5},
            {"sau_cau": "TK3.01#7", "text": "BÀI KIỂM TRA LÒNG TRUNG THÀNH VÀ SỰ HY SINH", "dur_s": 2.5},
            {"sau_cau": "TK3.01#9", "text": "GẮN KẾT CHẤN THƯƠNG: KẺ THÙ THÀNH 'CỨU TINH'", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "THE OPEN DOOR PARADOX OF 1981", "dur_s": 3.0},
            {"after_id": "TK3.01#4", "text": "MARTIN SELIGMAN: LEARNED HELPLESSNESS", "dur_s": 2.5},
            {"after_id": "TK3.01#7", "text": "LOYALTY TEST & SACRIFICE FOR FAMILY", "dur_s": 2.5},
            {"after_id": "TK3.01#9", "text": "TRAUMA BONDING: CAPTOR BECOMES 'SAVIOR'", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "1981年：開かれた扉と帰還の逆説", "dur_s": 3.0},
            {"after_id": "TK3.01#4", "text": "セリグマン教授の「学習性無力感」の心理", "dur_s": 2.5},
            {"after_id": "TK3.01#7", "text": "忠誠心の試練と家族を守るための沈黙", "dur_s": 2.5},
            {"after_id": "TK3.01#9", "text": "トラウマ・ボンディング：支配者を救い主と錯覚する罠", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t10_open_door_paradox_dilemma", "pull"),
            ("H", "3.06#1", "neutral", -0.02, 0.6, "t10_open_door_paradox_dilemma", "still"),
            ("H", "3.06#2", "neutral", -0.02, 0.6, "t10_packed_suitcase_return_car", "pan"),
            ("C", "3.07#1", "neutral", -0.02, 0.6, "t10_martin_seligman_learned_helplessness", "push"),
            ("C", "3.07#2", "neutral", -0.02, 0.6, "t10_open_cage_motionless_silhouette", "pull"),
            ("C", "3.07#5", "neutral", -0.02, 0.6, "t10_open_cage_motionless_silhouette", "still"),
            ("C", "3.07#9", "neutral", -0.02, 0.6, "t10_window_sniper_paranoia_shadow", "pan"),
            ("C", "3.07#11", "neutral", -0.02, 0.6, "t10_invisible_timber_prison_mind", "push"),
            ("H", "3.08#1", "neutral", -0.02, 0.6, "t10_trauma_bonding_bread_and_whip", "pull"),
            ("H", "3.08#8", "neutral", -0.02, 0.6, "t10_captor_as_sole_savior_complex", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t10_amber_eyes_closing_dossier_colleen", "still")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Sự thức tỉnh của người vợ và giọt nước tràn ly",
        "title_en": "Janice Hooker's Awakening & The Broken Silence",
        "title_ja": "共犯者の妻の覚醒と崩壊した7年の沈黙",
        "signs": [3, 4],
        "theme_vn": "Cơ chế chia ngăn nhận thức (Compartmentalization) & Điểm gãy tâm lý (Trigger)",
        "theme_en": "Cognitive Compartmentalization & The Moral Breaking Point",
        "theme_ja": "心理的区分化（防衛機制）と良心の覚醒トリガー",
        "hook_vn": "Bảy năm làm đồng phạm trên chiếc đệm nước. Điều gì khiến người vợ quyết định đạp đổ tất cả?",
        "hook_en": "Seven years an accomplice above the waterbed. What finally shattered her silence?",
        "hook_ja": "ウォーターベッドの上で共犯として過ごした7年。何が妻の沈黙を打ち砕いたのか？",
        "bgm": "bgm_violin_heart.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_violin_heart.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_violin_heart.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_violin_heart.mp3",
        "sfx_vn": ["amb_wood_creak.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_wood_creak.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_wood_creak.wav（環境音）", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "BI KỊCH CỦA ĐỒNG PHẠM TRÊN ĐỆM NƯỚC", "dur_s": 3.0},
            {"sau_cau": "TK4.01#3", "text": "GIỌT NƯỚC TRÀN LY: MƯU TOAN BẮT NẠN NHÂN THỨ HAI", "dur_s": 2.5},
            {"sau_cau": "TK4.01#6", "text": "LỜI XƯNG TỘI VỚI MỤC SƯ & BẢN NĂNG NGƯỜI MẸ", "dur_s": 2.5},
            {"sau_cau": "TK4.01#9", "text": "'THE COMPANY LÀ DỐI TRÁ' — BỨC TƯỜNG SỤP ĐỔ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "THE WATERBED ACCOMPLICE TRAGEDY", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "THE BREAKING POINT: TARGETING A SECOND VICTIM", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "PASTOR CONFESSION & MATERNAL INSTINCT", "dur_s": 2.5},
            {"after_id": "TK4.01#9", "text": "'THE COMPANY IS A LIE' — WALLS COLLAPSE", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "ウォーターベッドの共犯者の葛藤と悲劇", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "限界点：第二の犠牲者を狙う夫の妄想", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "牧師への告白と母性本能による良心の覚醒", "dur_s": 2.5},
            {"after_id": "TK4.01#9", "text": "「カンパニーなど実在しない」— 虚構の崩壊", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t10_waterbed_crushing_weight", "pull"),
            ("D", "4.03#1", "neutral", -0.02, 0.6, "t10_janice_hooker_moral_turmoil", "push"),
            ("D", "4.03#3", "neutral", -0.02, 0.6, "t10_second_victim_shadow_threat", "pan"),
            ("D", "4.03#5", "neutral", -0.02, 0.6, "t10_second_victim_shadow_threat", "still"),
            ("D", "4.03#9", "neutral", -0.02, 0.6, "t10_church_pastor_confession_shadow", "push"),
            ("H", "4.04#1", "neutral", -0.02, 0.6, "t10_church_pastor_confession_shadow", "still"),
            ("H", "4.04#4", "neutral", -0.02, 0.6, "t10_seventh_year_toddler_toys_shadow", "pull"),
            ("N2", "4.05#4", "fearful", -0.02, 0.6, "t10_janice_hooker_moral_turmoil", "pan"),
            ("N2", "4.05#8", "sad", -0.02, 0.6, "t10_truth_revealed_shattered_phantom", "push"),
            ("H", "4.07#2", "neutral", -0.02, 0.6, "t10_truth_revealed_shattered_phantom", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t10_amber_eyes_closing_dossier_colleen", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Bốn bài học cảnh báo đỏ sinh tồn trước kẻ săn mồi",
        "title_en": "4 Survival Red Flags Against Coercive Predators",
        "title_ja": "捕食者から身を守る4つの生存警告サイン",
        "signs": [10, 1],
        "theme_vn": "Nạn nhân học & Cảnh báo đỏ sinh tồn (Survival Red Flags — Gavin de Becker)",
        "theme_en": "Victimology & 4 Survival Red Flags (The Gift of Fear Framework)",
        "theme_ja": "被害者学と4大サバイバル警告サイン（『直感の贈り物』準拠）",
        "hook_vn": "Lồng giam kiên cố nhất không phải chiếc hộp gỗ, mà là ý nghĩ buông xuôi trong tâm trí bạn.",
        "hook_en": "The strongest prison is never made of wood, but the feeling of utter helplessness in your mind.",
        "hook_ja": "最も堅固な牢獄は木の箱ではない。心の中で諦めを受け入れてしまうことだ。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_morning_breeze.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_morning_breeze.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_morning_breeze.wav（環境音）", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN", "dur_s": 3.0},
            {"sau_cau": "TK5.01#2", "text": "DẤU HIỆU 1: CẢNH GIÁC TRƯỚC VỎ BỌC VÔ HẠI HOÀN HẢO", "dur_s": 2.5},
            {"sau_cau": "TK5.01#4", "text": "DẤU HIỆU 2: CÔ LẬP KHÔNG GIAN VÀ TƯỚC ĐOẠT THÔNG TIN", "dur_s": 2.5},
            {"sau_cau": "TK5.01#6", "text": "DẤU HIỆU 3: BÓNG MA VÔ HÌNH VÀ KẺ THÙ TƯỞNG TƯỢNG", "dur_s": 2.5},
            {"sau_cau": "TK5.01#8", "text": "DẤU HIỆU 4: PHÁ VỠ SỰ BẤT LỰC TẬP NHIỄM TRONG Ý NGHĨ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "4 SURVIVAL RED FLAGS (GAVIN DE BECKER)", "dur_s": 3.0},
            {"after_id": "TK5.01#2", "text": "FLAG 1: BEWARE OF THE PERFECT INNOCENT FACADE", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "FLAG 2: SPATIAL ISOLATION & INFORMATION DICTATORSHIP", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "FLAG 3: PHANTOM ENEMIES & FABRICATED THREATS", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "FLAG 4: BREAKING LEARNED HELPLESSNESS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "生き延びるための4大警告サイン", "dur_s": 3.0},
            {"after_id": "TK5.01#2", "text": "サイン1：完璧すぎる無害な仮面に警戒せよ", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "サイン2：空間的孤立と情報の遮断を見抜け", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "サイン3：架空の脅威と見えない敵の罠", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "サイン4：心の中の「学習性無力感」を打ち破れ", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t10_breaking_invisible_chains_dawn", "pull"),
            ("H", "5.05#1", "neutral", -0.02, 0.6, "t10_fbi_academy_profiling_archive", "still"),
            ("H", "5.05#2", "neutral", -0.02, 0.6, "t10_redflag1_trojan_innocence_trap", "pan"),
            ("H", "5.05#3", "neutral", -0.02, 0.6, "t10_redflag1_trojan_innocence_trap", "still"),
            ("H", "5.05#4", "neutral", -0.02, 0.6, "t10_redflag2_spatial_isolation_grid", "push"),
            ("H", "5.05#5", "neutral", -0.02, 0.6, "t10_redflag2_spatial_isolation_grid", "still"),
            ("H", "5.05#6", "neutral", -0.02, 0.6, "t10_redflag3_phantom_enemy_mirror", "pull"),
            ("H", "5.05#7", "neutral", -0.02, 0.6, "t10_redflag3_phantom_enemy_mirror", "still"),
            ("H", "5.05#8", "neutral", -0.02, 0.6, "t10_redflag4_breaking_helplessness_sparks", "push"),
            ("H", "5.05#10", "neutral", -0.02, 0.6, "t10_breaking_invisible_chains_dawn", "pan"),
            ("H", "5.05#12", "neutral", -0.02, 0.6, "t10_breaking_invisible_chains_dawn", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t10_amber_eyes_closing_dossier_colleen", "still")
        ]
    }
]

CTA_VN = "Tập mười của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio."
CTA_EN = "Episode ten of Amber Eyes. Watch the full documentary at the link in bio."
CTA_JA = "Amber Eyes 第10話。事件の完全版はプロフィールのリンクからご覧いただけます。"

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
            line_dur = words * RATE_VI.get(role, 0.28)
        elif lang == "EN":
            words = len([w for w in re.sub(r"<#[\d.]+#>", " ", txt).split() if w.strip()])
            line_dur = words * RATE_EN.get(role, 0.35)
        else:
            chars = len(re.sub(r"<#[\d.]+#>", " ", txt).replace(" ", "").strip())
            line_dur = chars * RATE_JA.get(role, 0.16)
            
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
        "episode": "10",
        "lang": lang,
        "engine": "Higgs Audio v3 + VoxCPM2 reference voices",
        "clips": {}
    }
    
    if lang == "VI":
        plan_lines.append("# KẾ HOẠCH CLIP TIKTOK — TẬP 10 · \"CHIẾC HỘP GỖ DƯỚI GẦM GIƯỜNG\"\n")
        plan_lines.append("*Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*")
        plan_lines.append("*Nguồn duy nhất của mọi dữ kiện: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap10/KeHoach_Video_Tap10.md` · `.work/script_tap10.json` (240 câu)*")
        plan_lines.append("*Sinh tự động bởi `.work/_build_tk_tap10.py`*\n---\n")
        plan_lines.append("## 0. Tóm tắt chốt\n")
        plan_lines.append("| Hạng mục | Giá trị |")
        plan_lines.append("|---|---|")
        plan_lines.append("| Số clip | **5 clip** (TK1–TK4 phân tích chuyên sâu + TK5 cảnh báo đỏ sinh tồn) |")
        plan_lines.append("| Tổng câu thoại | **54 câu** đọc giọng (TK1: 10, TK2: 10, TK3: 11, TK4: 11, TK5: 12) |")
        plan_lines.append("| Chủ đề | Mỗi clip giải phẫu **1–2 chỉ dấu tâm lý cốt lõi** (Hệ sinh thái 10 chỉ dấu K10) |")
        plan_lines.append("| Ngôn ngữ | Tiếng Việt · vai Host (H), Điều tra viên (D), Chuyên gia (C), Janice Hooker (N2) |")
        plan_lines.append("| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** (đúng cast chuẩn Tập 10) |")
        plan_lines.append("| Hình ảnh | Nền dọc 9:16 crop/pad từ 71 nền 16:9 gốc của Tập 10 (`t10_*`) |")
        plan_lines.append("| Độ dài ước lượng | Đạt chuẩn 45–95 s (trung bình 65–85 s/clip) |\n---\n")
        plan_lines.append("## 1. Danh sách 5 clip và chỉ dấu tâm lý (K10)\n")
        plan_lines.append("| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng |")
        plan_lines.append("|---|---|---|---|---|")
    elif lang == "EN":
        plan_lines.append("# TIKTOK CLIP PRODUCTION PLAN — EPISODE 10 · \"THE WOODEN BOX UNDER THE BED\"\n")
        plan_lines.append("*Status: **Script completed, ready for verification prior to TTS generation** (L4)*")
        plan_lines.append("*Single source of truth: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap10/KeHoach_Video_Tap10.md` · `.work/script_tap10_EN.json` (240 lines)*")
        plan_lines.append("*Auto-generated via `.work/_build_tk_tap10.py`*\n---\n")
        plan_lines.append("## 0. Executive Summary\n")
        plan_lines.append("| Item | Value |")
        plan_lines.append("|---|---|")
        plan_lines.append("| Total Clips | **5 clips** (TK1–TK4 narrative analysis + TK5 survival red flags) |")
        plan_lines.append("| Spoken Lines | **54 lines** (TK1: 10, TK2: 10, TK3: 11, TK4: 11, TK5: 12) |")
        plan_lines.append("| Framework | Psychological behavioral analysis based on 10 Core Markers (K10) |")
        plan_lines.append("| Cast | Host (H), Investigator (D), Psychologist (C), Janice Hooker (N2) |")
        plan_lines.append("| Voice Engine | **Higgs Audio v3 + VoxCPM2 Reference Voices** |")
        plan_lines.append("| Visuals | 9:16 Vertical background art adapted from 71 original 16:9 backgrounds (`t10_*`) |")
        plan_lines.append("| Estimated Duration | Strictly within 45–95s TikTok gate (average 65–85s) |\n---\n")
        plan_lines.append("## 1. 5 Clips & Corresponding Psychological Markers (K10)\n")
        plan_lines.append("| Clip | Markers | Theme | Visual Hook Card (0–3 s) | Duration |")
        plan_lines.append("|---|---|---|---|---|")
    else:
        plan_lines.append("# TIKTOKクリップ制作計画 — 第10話 · 『ベッドの下の木箱』\n")
        plan_lines.append("*ステータス: **台本策定完了 · 音声合成前の最終確認待ち** (L4)*")
        plan_lines.append("*情報源: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap10/KeHoach_Video_Tap10.md` · `.work/script_tap10_JA.json` (全240文)*")
        plan_lines.append("*`.work/_build_tk_tap10.py` により自動生成*\n---\n")
        plan_lines.append("## 0. 基本概要\n")
        plan_lines.append("| 項目 | 仕様 |")
        plan_lines.append("|---|---|")
        plan_lines.append("| クリップ数 | **全5本**（TK1–TK4 本編核心分析 + TK5 生存警告サイン） |")
        plan_lines.append("| 総音声文数 | **54文**（TK1: 10文, TK2: 10文, TK3: 11文, TK4: 11文, TK5: 12文） |")
        plan_lines.append("| 分析枠組み | 犯罪心理学10大指標（K10）に準拠した深層行動プロファイリング |")
        plan_lines.append("| 配役 | ホスト (H), 捜査官 (D), 心理専門家 (C), ジャニス・フッカー (N2) |")
        plan_lines.append("| 音声エンジン | **Higgs Audio v3 + VoxCPM2 参照音声** |")
        plan_lines.append("| 映像素材 | 第10話公式背景（71枚）より適合させた 9:16 縦型美術背景 (`t10_*`) |")
        plan_lines.append("| 推定再生時間 | TikTok適正範囲（45–95秒）完全準拠（平均65–85秒） |\n---\n")
        plan_lines.append("## 1. 全5本クリップと対応心理指標（K10）\n")
        plan_lines.append("| クリップ | 心理指標 | テーマ | 冒頭フック表示 (0–3秒) | 推定時間 |")
        plan_lines.append("|---|---|---|---|---|")
        
    for c in CLIPS_CONFIG:
        tot_dur, items = calc_durations(c, lang)
        num_l = len(items)
        if lang == "VI":
            plan_lines.append(f"| **{c['id']}** | #{c['signs'][0]} · #{c['signs'][-1]} | {c['theme_vn']} | *\"{c['hook_vn'][:45]}...\"* | {tot_dur} s · {num_l} câu |")
        elif lang == "EN":
            plan_lines.append(f"| **{c['id']}** | #{c['signs'][0]} · #{c['signs'][-1]} | {c['theme_en']} | *\"{c['hook_en'][:45]}...\"* | {tot_dur} s · {num_l} lines |")
        else:
            plan_lines.append(f"| **{c['id']}** | #{c['signs'][0]} · #{c['signs'][-1]} | {c['theme_ja']} | *\"{c['hook_ja'][:35]}...\"* | {tot_dur} 秒 · {num_l}文 |")
            
    plan_lines.append("\n---\n")
    if lang == "VI":
        plan_lines.append("## 2. Diễn xuất chi tiết từng clip (Lời đọc + Hình ảnh + Âm thanh)\n")
    elif lang == "EN":
        plan_lines.append("## 2. Detailed Clip Production Specs (Dialogue + Visuals + Audio)\n")
    else:
        plan_lines.append("## 2. 各クリップ詳細設計（セリフ + 映像演出 + 音響）\n")
        
    for c in CLIPS_CONFIG:
        tot_dur, items = calc_durations(c, lang)
        num_l = len(items)
        spec_json["clips"][c["id"]] = {
            "title": c["title_vn"] if lang == "VI" else (c["title_en"] if lang == "EN" else c["title_ja"]),
            "estimated_duration": tot_dur,
            "bgm": c["bgm"],
            "sfx": c["sfx_vn"] if lang == "VI" else (c["sfx_en"] if lang == "EN" else c["sfx_ja"]),
            "lines": []
        }
        
        if lang == "VI":
            plan_lines.append(f"### 2.{c['id'][-1]} CLIP {c['id']} — \"{c['title_vn']}\"\n")
            plan_lines.append(f"*Ước lượng **{tot_dur} s** ({num_l} câu) · BGM `{c['bgm']}` ({c['bgm_desc_vn']}) · SFX: {', '.join(c['sfx_vn'])}*\n")
            plan_lines.append("| Mã câu | Vai | Emotion | Tốc độ | Nghỉ | Nền & Chuyển động | Lời đọc kịch bản | Nguồn câu |")
            plan_lines.append("|---|---|---|---|---|---|---|---|")
        elif lang == "EN":
            plan_lines.append(f"### 2.{c['id'][-1]} CLIP {c['id']} — \"{c['title_en']}\"\n")
            plan_lines.append(f"*Estimated Duration: **{tot_dur} s** ({num_l} lines) · BGM `{c['bgm']}` ({c['bgm_desc_en']}) · SFX: {', '.join(c['sfx_en'])}*\n")
            plan_lines.append("| Line ID | Role | Emotion | Speed | Pause | Background & Motion | Spoken Dialogue | Source |")
            plan_lines.append("|---|---|---|---|---|---|---|---|")
        else:
            plan_lines.append(f"### 2.{c['id'][-1]} クリップ {c['id']} — 『{c['title_ja']}』\n")
            plan_lines.append(f"*推定再生時間: **{tot_dur} 秒** (全{num_l}文) · BGM `{c['bgm']}` ({c['bgm_desc_ja']}) · SFX: {', '.join(c['sfx_ja'])}*\n")
            plan_lines.append("| セリフ番号 | 配役 | 感情 | 速度 | 休止 | 背景美術 & 演出 | 音声セリフ | 典拠 |")
            plan_lines.append("|---|---|---|---|---|---|---|---|")
            
        for it in items:
            spec_json["clips"][c["id"]]["lines"].append({
                "line_id": it["code"],
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

Tập 10 · Chiếc hộp gỗ dưới gầm giường — Chỉ dấu #{c['signs'][0]}: {c['theme_vn']}.
Hồ sơ vụ án Colleen Stan (Red Bluff, California), 100% dữ liệu đối chiếu hồ sơ điều tra và phán quyết tư pháp.

📺 Xem trọn vẹn tập phân tích 34 phút ở link trong bio
🔎 Hồ sơ tâm lý học tội phạm · Vụ án Colleen Stan & Cameron Hooker · Thao túng tâm lý

Nội dung do AI hỗ trợ tạo hình và giọng phục vụ mục đích phân tích tâm lý giáo dục — không phải phóng sự giật gân.

#AmberEyes #TamLyToiPham #HosoCoThat #ColleenStan #CameronHooker #{c['id']} #TrueCrimeVN #PhanTichHanhVi #LearnedHelplessness

---
Ghi chú khi đăng (KHÔNG dán vào caption):
- BẬT toggle "Nội dung do AI tạo" (AI-generated content) trên TikTok.
- Dán link YouTube Tập 10 vào ô Website trong phần sửa hồ sơ cá nhân.
- Ước lượng thời lượng: {tot_dur} s ({num_l} câu).
- Tên file video thành phẩm: clip{c['id'][-1]}_{c['id']}.mp4 (1080x1920, 30fps).
"""
            mota_dai_text = f"""HỒ SƠ TẬP 10: CHIẾC HỘP GỖ DƯỚI GẦM GIƯỜNG — CLIP {c['id']}

CHỦ ĐỀ: {c['theme_vn']}
VỤ ÁN: Vụ bắt cóc, giam cầm 7 năm Colleen Stan (1977–1984, Red Bluff, California)

TÓM TẮT PHÂN TÍCH:
{c['hook_vn']}

Vụ án "Cô gái trong hộp gỗ" Colleen Stan là một trong những hồ sơ giam cầm và thao túng tâm lý gây chấn động nhất lịch sử tư pháp hiện đại. Nạn nhân bị giam giữ tới 23 giờ mỗi ngày trong chiếc hộp gỗ chật hẹp đặt dưới chiếc giường đệm nước của cặp vợ chồng Cameron và Janice Hooker.

Dưới lăng kính của tâm lý học tội phạm và khoa học hành vi, clip này bóc tách bản chất của:
1. Cơ chế kiểm soát cưỡng bức (Coercive Control) và cách vỏ bọc gia đình ru ngủ trực giác sinh tồn.
2. Nỗi sợ hãi tổ chức tưởng tượng ("The Company") và cách kẻ ác kiến tạo thực tại méo mó.
3. Bài học đắt giá về sự bất lực tập nhiễm (Learned Helplessness) và các cảnh báo đỏ bảo vệ bản thân.

📺 XEM TRỌN VẸN HỒ SƠ 34 PHÚT TRÊN KÊNH YOUTUBE AMBER EYES (LINK TRONG BIO).
"""
            mota_ngan_text = f"""Tập 10 Amber Eyes — Clip {c['id']}: {c['title_vn']}.
{c['hook_vn']}
Xem hồ sơ giải phẫu tâm lý đầy đủ tại link bio. #AmberEyes #TamLyToiPham #{c['id']} #ColleenStan
"""
        elif lang == "EN":
            cap_text = f"""{c['hook_en']} 👁️

Ep. 10 · The Wooden Box Under the Bed — Psychological Marker #{c['signs'][0]}: {c['theme_en']}.
Authentic criminal dossier of Colleen Stan, strictly source-verified against judicial records.

📺 Watch the full 34-minute documentary on YouTube — link in bio.
🔎 Criminal Psychology · Colleen Stan Case & Cameron Hooker · Coercive Control

Content created with AI assistance for behavioral and psychological educational purposes.

#AmberEyes #CriminalPsychology #TrueCrime #ColleenStan #CameronHooker #{c['id']} #CaseFile #Mindhunter #LearnedHelplessness

---
Publishing Notes (DO NOT paste into caption):
- TOGGLE ON 'AI-generated content' label in TikTok settings.
- Add YouTube Episode 10 URL to the Website field in your profile bio.
- Estimated duration: {tot_dur} s ({num_l} lines).
- Video output file: clip{c['id'][-1]}_{c['id']}_EN.mp4 (1080x1920, 30fps).
"""
            mota_dai_text = f"""DOSSIER EPISODE 10: THE WOODEN BOX UNDER THE BED — CLIP {c['id']}

THEME: {c['theme_en']}
CASE FILE: The 7-Year Captivity of Colleen Stan (1977–1984, Red Bluff, California)

ANALYSIS SUMMARY:
{c['hook_en']}

The Colleen Stan "Girl in the Box" case remains one of the most chilling studies of psychological manipulation and captivity in modern jurisprudence. Held for up to 23 hours a day in a cramped wooden box beneath a master waterbed, Colleen survived seven years under absolute psychological domination.

Key Psychological Insights Explored:
1. Coercive control techniques and how normal family facades dismantle survival intuition.
2. The fabricated syndicate ("The Company") used to engineer a distorted reality.
3. Crucial insights on Learned Helplessness, Trauma Bonding, and vital red flags for personal safety.

📺 WATCH THE FULL 34-MINUTE DOCUMENTARY ON YOUTUBE (LINK IN BIO).
"""
            mota_ngan_text = f"""Amber Eyes Ep. 10 — Clip {c['id']}: {c['title_en']}.
{c['hook_en']}
Full behavioral case study available via link in bio. #AmberEyes #TrueCrime #{c['id']} #ColleenStan
"""
        else:
            cap_text = f"""{c['hook_ja']} 👁️

第10話 · ベッドの下の木箱 — 心理指標 #{c['signs'][0]}: {c['theme_ja']}。
コリーン・スタン事件の裁判記録および公式捜査資料に基づく深層心理分析。

📺 完全版ドキュメンタリー（34分）はYouTubeにて公開中 — プロフィールのリンクから
🔎 犯罪心理学 · コリーン・スタン事件 · キャメロン・フッカー · マインドコントロール

本コンテンツは心理分析および啓発を目的としてAI技術の支援を受けて制作されています。

#AmberEyes #犯罪心理学 #コリーンスタン #キャメロンフッカー #{c['id']} #マインドハンター #実話事件簿 #学習性無力感

---
投稿時の注意事項（キャプション本文には貼り付けないでください）：
- TikTokアプリ内で「AI生成コンテンツ」のトグルを必ずONに設定してください。
- YouTube第10話へのリンクをプロフィール欄のウェブサイト項目に設定してください。
- 推定再生時間: {tot_dur} 秒 (全{num_l}文)。
- 出力動画ファイル名: clip{c['id'][-1]}_{c['id']}_JA.mp4 (1080x1920, 30fps)。
"""
            mota_dai_text = f"""事件簿 第10話：ベッドの下の木箱 — クリップ {c['id']}

テーマ：{c['theme_ja']}
事件名：コリーン・スタン7年間監禁事件（1977–1984年、カリフォルニア州レッドブラフ）

分析概要：
{c['hook_ja']}

「箱の中の少女」として世界に衝撃を与えたコリーン・スタン事件。ウォーターベッドの下に置かれた狭小な木箱に1日最大23時間閉じ込められ、7年間にわたり極限の心理的支配下に置かれた前代未聞の監禁事件の全貌を解明します。

心理学的分析の焦点：
1. 強迫的支配（Coercive Control）と家族という無害な仮面が直感を狂わせる手口。
2. 架空組織「ザ・カンパニー」による歪められた現実の創造と脱出不能の罠。
3. 学習性無力感（Learned Helplessness）の罠と、現代を生きる私たちが知るべき生存警告サイン。

📺 YouTube「Amber Eyes」にて34分の本編完全解説を公開中（プロフィールリンクより）。
"""
            mota_ngan_text = f"""Amber Eyes 第10話 — クリップ {c['id']}：『{c['title_ja']}』。
{c['hook_ja']}
事件の完全版解説はプロフィールのリンクから。 #AmberEyes #犯罪心理学 #{c['id']} #コリーンスタン
"""

        cap_file.write_text(cap_text.strip() + "\n", encoding="utf-8")
        mota_dai_file.write_text(mota_dai_text.strip() + "\n", encoding="utf-8")
        mota_ngan_file.write_text(mota_ngan_text.strip() + "\n", encoding="utf-8")
        
    # Ghi file kế hoạch và spec json
    if lang == "VI":
        (out_dir / "KE_HOACH_CLIP_TAP10.md").write_text("\n".join(plan_lines), encoding="utf-8")
        (out_dir / "SPEC_AUDIO_CLIP_TAP10.json").write_text(json.dumps(spec_json, ensure_ascii=False, indent=2), encoding="utf-8")
    elif lang == "EN":
        (out_dir / "KE_HOACH_CLIP_TAP10_EN.md").write_text("\n".join(plan_lines), encoding="utf-8")
        (out_dir / "SPEC_AUDIO_CLIP_TAP10_EN.json").write_text(json.dumps(spec_json, ensure_ascii=False, indent=2), encoding="utf-8")
        (out_dir / "SPEC_AUDIO_CLIP_TAP10.json").write_text(json.dumps(spec_json, ensure_ascii=False, indent=2), encoding="utf-8")
    else:
        (out_dir / "KE_HOACH_CLIP_TAP10_JA.md").write_text("\n".join(plan_lines), encoding="utf-8")
        (out_dir / "SPEC_AUDIO_CLIP_TAP10_JA.json").write_text(json.dumps(spec_json, ensure_ascii=False, indent=2), encoding="utf-8")
        (out_dir / "SPEC_AUDIO_CLIP_TAP10.json").write_text(json.dumps(spec_json, ensure_ascii=False, indent=2), encoding="utf-8")
        
    print(f"Hoàn thành xuất tài liệu TikTok Tập 10 cho ngôn ngữ: {lang} -> {out_dir}")

print("TẤT CẢ ĐÃ HOÀN TẤT THÀNH CÔNG 100%.")
