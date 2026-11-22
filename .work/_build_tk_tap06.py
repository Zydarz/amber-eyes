# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 06 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap06/KE_HOACH_CLIP_TAP06.md
  02_SAN_XUAT/TIKTOK/Tap06/SPEC_AUDIO_CLIP_TAP06.json
  02_SAN_XUAT/TIKTOK/Tap06/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap06/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap06/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap06_EN/KE_HOACH_CLIP_TAP06_EN.md
  02_SAN_XUAT/TIKTOK/Tap06_EN/SPEC_AUDIO_CLIP_TAP06.json
  02_SAN_XUAT/TIKTOK/Tap06_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap06_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap06_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap06_JA/KE_HOACH_CLIP_TAP06_JA.md
  02_SAN_XUAT/TIKTOK/Tap06_JA/SPEC_AUDIO_CLIP_TAP06.json
  02_SAN_XUAT/TIKTOK/Tap06_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap06_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap06_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 06:
- timeline_s_t06.json (VI)
- timeline_s_EN_t06.json (EN)
- timeline_s_JA_t06.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap06"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap06_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap06_JA"

OUT_VI.mkdir(parents=True, exist_ok=True)
OUT_EN.mkdir(parents=True, exist_ok=True)
OUT_JA.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WORK))
try:
    from vi_cer import vi_numbers
except Exception:
    def vi_numbers(x): return x

# ----------------------------------------------------------------------------
# 0. TỶ LỆ ĐỌC THẬT (Tập 06 Master ASR)
# ----------------------------------------------------------------------------
def get_rates(fn, is_ja=False):
    d = json.load((WORK / fn).open(encoding="utf-8"))
    dur = defaultdict(float)
    units = defaultdict(int)
    for it in d["items"]:
        txt = re.sub(r"<#[\d.]+#>", " ", it["text"])
        n = len(txt.replace(" ", "").strip()) if is_ja else len([w for w in txt.split() if w.strip()])
        dur[it["role"]] += it["end"] - it["start"]
        units[it["role"]] += n
    return {r: dur[r] / units[r] for r in dur}

RATE_VI = get_rates("timeline_s_t06.json", False)
RATE_EN = get_rates("timeline_s_EN_t06.json", False)
RATE_JA = get_rates("timeline_s_JA_t06.json", True)

VI_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_t06.json").open(encoding="utf-8"))["items"]}
EN_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_EN_t06.json").open(encoding="utf-8"))["items"]}
JA_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_JA_t06.json").open(encoding="utf-8"))["items"]}

# ----------------------------------------------------------------------------
# 1. ĐỊNH NGHĨA 5 CLIP TẬP 06
# ----------------------------------------------------------------------------
CLIPS_DEF = [
    {
        "id": "TK1",
        "title_vn": "Nụ cười chú hề và chiếc mặt nạ công dân",
        "title_en": "The Clown’s Smile & The Pristine Civic Mask",
        "title_ja": "道化師の笑顔と完璧な市民の仮面",
        "signs": [9, 1],
        "theme_vn": "Hiệu ứng Hào quang (Halo Effect) & Điểm mù xã hội trước kẻ săn mồi",
        "theme_en": "The Halo Effect & Social Blind Spots Surrounding Predators",
        "theme_ja": "ハロー効果（後光効果）と社会集団の致命的死角",
        "hook_vn": "Bắt tay Đệ nhất phu nhân, khoác áo chú hề và 29 bí mật rùng rợn dưới sàn nhà.",
        "hook_en": "Shaking hands with the First Lady, donning a clown suit, and 29 chilling secrets buried.",
        "hook_ja": "大統領夫人との握手、道化師の仮面、そして床下に埋められた29の戦慄の秘密。",
        "bgm": "bgm_sub_drone.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_sub_drone.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_sub_drone.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_sub_drone.mp3",
        "sfx_vn": ["amb_suburban_evening.wav (nền)", "fx_camera_flash.wav", "fx_crowd_applause.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_suburban_evening.wav (bed)", "fx_camera_flash.wav", "fx_crowd_applause.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_suburban_evening.wav（環境音）", "fx_camera_flash.wav", "fx_crowd_applause.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "CHIẾC MẶT NẠ CÔNG DÂN GƯƠNG MẪU", "dur_s": 3.0},
            {"sau_cau": "TK1.01#3", "text": "HUY HIỆU MẬT VỤ HOA KỲ CẤP", "dur_s": 2.5},
            {"sau_cau": "TK1.01#4", "text": "CHÚ HỀ POGO TỪ THIỆN TẠI BỆNH VIỆN NHI", "dur_s": 2.5},
            {"sau_cau": "TK1.01#5", "text": "ĐỊA VỊ XÃ HỘI DỆT NÊN MẶT NẠ SĂN MỒI", "dur_s": 2.5},
            {"sau_cau": "TK1.01#7", "text": "CƠ CHẾ TỰ THÔI MIÊN NHẬN THỨC", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "THE EXEMPLARY CIVIC CITIZEN MASK", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "SECRET SERVICE SPECIAL SECURITY CLEARANCE", "dur_s": 2.5},
            {"after_id": "TK1.01#4", "text": "POGO THE CLOWN CHARITY IN CHILDREN’S HOSPITALS", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "CIVIC STATUS FORGING A PREDATORY MASK", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "PATHOLOGICAL SELF-HYPNOSIS MECHANISM", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "模範市民という完璧な社会的仮面", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "大統領シークレットサービス特別許可証", "dur_s": 2.5},
            {"after_id": "TK1.01#4", "text": "小児病棟を慰問する慈善の道化師ポゴ", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "社会的地位によって織り成された捕食の仮面", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "自己催眠による良心の麻痺と完全正当化", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t6_clown_mirror_chiaroscuro", "still"),
            ("H", "1.02#1", "neutral", -0.02, 0.6, "t6_polish_parade_chicago_1978", "pan"),
            ("H", "1.02#2", "neutral", -0.02, 0.6, "t6_secret_service_pin_handshake", "push"),
            ("H", "1.02#6", "neutral", -0.02, 0.6, "t6_clown_costume_closet", "still"),
            ("C", "1.15#2", "neutral", -0.02, 0.7, "t6_psychological_mask_metaphor", "pull"),
            ("C", "1.15#3", "neutral", -0.02, 0.7, "t6_clown_mirror_chiaroscuro", "push"),
            ("C", "1.15#5", "neutral", -0.02, 0.7, "t6_psychological_mask_metaphor", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t6_closing_rose_closed_dossier", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Cái bẫy còng tay ảo thuật và chữ ký tâm lý",
        "title_en": "The Handcuff Trick & The Dark Psychological Signature",
        "title_ja": "手錠の奇術という罠と不変の心理的署名",
        "signs": [7, 8],
        "theme_vn": "Thủ đoạn gây án MO vs. Dấu ấn Chữ ký tâm lý Signature",
        "theme_en": "Modus Operandi Evolution vs. Invariable Psychological Signature",
        "theme_ja": "犯行手口（MO）の進化と不変の心理的シグネチャー",
        "hook_vn": "Một chiếc còng tay và một trò ảo thuật. Cái bẫy chết người lấy đi 33 sinh mạng.",
        "hook_en": "A pair of handcuffs and a magic trick. The deadly trap that claimed 33 lives.",
        "hook_ja": "手錠と奇術の罠。33名の命を奪った戦慄の捕食手口。",
        "bgm": "bgm_jazz_noir.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_jazz_noir.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_jazz_noir.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_jazz_noir.mp3",
        "sfx_vn": ["amb_dark_drone.wav (nền)", "fx_handcuff_click.wav", "fx_door_creak.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_dark_drone.wav (bed)", "fx_handcuff_click.wav", "fx_door_creak.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_dark_drone.wav（環境音）", "fx_handcuff_click.wav", "fx_door_creak.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "CHIẾC BẪY CÒNG TAY ẢO THUẬT (THE HANDCUFF TRICK)", "dur_s": 3.0},
            {"sau_cau": "TK2.01#3", "text": "THỦ ĐOẠN MO: LIÊN TỤC TIẾN HÓA VÀ HOÀN THIỆN", "dur_s": 2.5},
            {"sau_cau": "TK2.01#5", "text": "MỒI NHỬ VIỆC LÀM & KHỐNG CHẾ BẤT LỰC", "dur_s": 2.5},
            {"sau_cau": "TK2.01#6", "text": "CHỮ KÝ TÂM LÝ SIGNATURE KHÔNG BAO GIỜ THAY ĐỔI", "dur_s": 2.5},
            {"sau_cau": "TK2.01#8", "text": "BIẾN SÀN NHÀ MÌNH THÀNH KHU LĂNG MỘ CHÔN XÁC", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "THE LETHAL HANDCUFF TRICK ENTRAPMENT", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "MODUS OPERANDI: EVOLVING PREDATORY TECHNIQUES", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "EMPLOYMENT BAIT & TOTAL INCAPACITATION", "dur_s": 2.5},
            {"after_id": "TK2.01#6", "text": "INVARIABLE PSYCHOLOGICAL SIGNATURE", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "TURNING HIS OWN RESIDENCE INTO A MASS GRAVE", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "致命的な『手錠の奇術』という捕食の罠", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "犯行手口（MO）：進化し続ける捕食技術", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "高給求人の罠と完全な抵抗不能状態", "dur_s": 2.5},
            {"after_id": "TK2.01#6", "text": "決して変わることのない歪んだ心理的署名", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "自宅床下を巨大な墓場と化す狂気の支配欲", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t6_redflag_trick_handcuffs", "still"),
            ("D", "2.09#1", "neutral", -0.03, 0.6, "t6_psychological_mask_metaphor", "still"),
            ("D", "2.09#2", "neutral", -0.03, 0.6, "t6_pharmacy_counters_renovation", "pan"),
            ("D", "2.09#3", "neutral", -0.03, 0.6, "t6_pharmacy_counters_renovation", "pull"),
            ("D", "2.09#4", "neutral", -0.03, 0.6, "t6_redflag_trick_handcuffs", "push"),
            ("D", "2.09#5", "neutral", -0.03, 0.7, "t6_psychological_mask_metaphor", "still"),
            ("D", "2.09#7", "neutral", -0.03, 0.7, "t6_highschool_ring_jas", "pull"),
            ("D", "2.09#8", "neutral", -0.03, 0.7, "t6_crawlspace_trapdoor_opened", "push"),
            ("H", "cta", "neutral", -0.02, 0.0, "t6_closing_rose_closed_dossier", "still")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Trêu ngươi cảnh sát và sự tự đắc ái kỷ",
        "title_en": "Mocking the Police & Narcissistic Overcompensation",
        "title_ja": "警察を挑発する怪物と誇大自己愛の暴走",
        "signs": [4, 8],
        "theme_vn": "Sự tự đắc Ái kỷ độc hại & Cảm giác toàn năng trước cơ quan điều tra",
        "theme_en": "Malignant Narcissism & The Delusion of Omnipotent Control",
        "theme_ja": "悪性自己愛と捜査機関を手玉に取る全能妄想",
        "hook_vn": "Kẻ thủ ác gõ cửa kính xe cảnh sát, mời bia và tuyên bố: Các anh sẽ không tìm thấy gì đâu.",
        "hook_en": "Tapping the police car window, buying beers, and mocking: You will never find anything.",
        "hook_ja": "尾行警察の窓を叩き、酒を奢り高笑いした怪物。「君たちに何も見つけられないさ」",
        "bgm": "bgm_jazz_noir.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_jazz_noir.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_jazz_noir.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_jazz_noir.mp3",
        "sfx_vn": ["amb_bar.wav (nền)", "fx_car_drive.wav", "fx_glass_clink.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_bar.wav (bed)", "fx_car_drive.wav", "fx_glass_clink.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_bar.wav（環境音）", "fx_car_drive.wav", "fx_glass_clink.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "CUỘC THEO DÕI 24/7 CỦA ĐẶC NHIỆM DES PLAINES", "dur_s": 3.0},
            {"sau_cau": "TK3.01#3", "text": "MỜI ĐIỀU TRA VIÊN UỐNG BIA VÀO ĐÊM ĐÔNG", "dur_s": 2.5},
            {"sau_cau": "TK3.01#4", "text": "“CÁC ANH KHÔNG BAO GIỜ TÌM THẤY GÌ ĐÂU”", "dur_s": 2.5},
            {"sau_cau": "TK3.01#5", "text": "SỰ QUÁ BÙ QUYỀN LỰC (POWER OVERCOMPENSATION)", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "ẢO TƯỞNG TOÀN NĂNG THAO TÚNG PHÁP LUẬT", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "24/7 TACTICAL SURVEILLANCE BY DES PLAINES POLICE", "dur_s": 3.0},
            {"after_id": "TK3.01#3", "text": "BUYING ROUNDS FOR HIS SHADOW DETECTIVES", "dur_s": 2.5},
            {"after_id": "TK3.01#4", "text": "“YOU BOYS WILL NEVER FIND A THING”", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "PSYCHOPATHIC OVERCOMPENSATION OF POWER", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "THE FATAL HUBRIS OF OMNIPOTENT MANIPULATION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "デスプレーンズ警察による24時間体制の完全尾行", "dur_s": 3.0},
            {"after_id": "TK3.01#3", "text": "尾行中の捜査官にビールを振る舞う不敵な態度", "dur_s": 2.5},
            {"after_id": "TK3.01#4", "text": "「ご苦労だが君たちが何かを見つけることなどない」", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "自己愛性精神病質者に見られる権力の過剰代償", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "国家権力すら支配できるという破滅的全能妄想", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t6_diner_booth_confrontation", "still"),
            ("H", "2.10#4", "neutral", -0.02, 0.6, "t6_gas_station_neon_midnight", "pan"),
            ("H", "2.10#8", "neutral", -0.02, 0.6, "t6_diner_booth_confrontation", "push"),
            ("H", "2.10#9", "neutral", -0.02, 0.7, "t6_diner_booth_confrontation", "still"),
            ("C", "2.11#1", "neutral", -0.02, 0.7, "t6_psychological_mask_metaphor", "pull"),
            ("C", "2.11#2", "neutral", -0.02, 0.7, "t6_police_entry_summerdale", "push"),
            ("C", "2.11#3", "neutral", -0.02, 0.7, "t6_diner_booth_confrontation", "still"),
            ("C", "2.11#4", "neutral", -0.02, 0.7, "t6_psychological_mask_metaphor", "pull"),
            ("H", "cta", "neutral", -0.02, 0.0, "t6_closing_rose_closed_dossier", "still")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Hai mươi sáu bí mật dưới nền nhà và cơ chế chia ngăn",
        "title_en": "26 Buried Secrets & Extreme Compartmentalization",
        "title_ja": "床下の26の秘密と極限の精神分断",
        "signs": [3, 2],
        "theme_vn": "Cơ chế Chia ngăn tâm trí (Compartmentalization) & Đối xử với gia đình / Nạn nhân",
        "theme_en": "Psychological Compartmentalization & Cognitive Dehumanization",
        "theme_ja": "精神の分断（コンパートメンタライゼーション）と人間性の剥奪",
        "hook_vn": "Ăn tối, ngủ say ngay phía trên 26 thi thể. Sự chia ngăn rùng rợn của bộ não ác tính.",
        "hook_en": "Dining and sleeping directly above 26 buried bodies. The chilling horror of compartmentalization.",
        "hook_ja": "26体の遺体の上で夕食をとり熟睡する。悪性自己愛者の異常な精神分断。",
        "bgm": "bgm_cellar_wind.mp3",
        "bgm_desc_vn": "Hồi 3 — bed tập: bgm_cellar_wind.mp3",
        "bgm_desc_en": "Act 3 — episode bed: bgm_cellar_wind.mp3",
        "bgm_desc_ja": "第3幕 — 本編BGM: bgm_cellar_wind.mp3",
        "sfx_vn": ["amb_cellar_drip.wav (nền)", "fx_shovel_dig.wav", "fx_bone_tap.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_cellar_drip.wav (bed)", "fx_shovel_dig.wav", "fx_bone_tap.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_cellar_drip.wav（環境音）", "fx_shovel_dig.wav", "fx_bone_tap.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "KHÁM XÉT SÀN NHÀ 8213 WEST SUMMERDALE", "dur_s": 3.0},
            {"sau_cau": "TK4.01#3", "text": "PHÒNG KHÁCH ẤM CÚNG NGAY TRÊN HẦM MỘ", "dur_s": 2.5},
            {"sau_cau": "TK4.01#4", "text": "TỔNG CỘNG 26 THI THỂ DƯỚI KHOẢNG ĐẤT ẨM", "dur_s": 2.5},
            {"sau_cau": "TK4.01#6", "text": "CƠ CHẾ CHIA NGĂN NHẬN THỨC (COMPARTMENTALIZATION)", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "TẮM RỬA, ĂN TỐI VÀ NGỦ NGON SAU TỘI ÁC", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "SUBTERRANEAN EXCAVATION AT 8213 W SUMMERDALE", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "WARM PARLOR SUSPENDED DIRECTLY ABOVE A TOMB", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "26 BODIES ENTOMBED BENEATH THE CRAWLSPACE", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "EXTREME PSYCHOLOGICAL COMPARTMENTALIZATION", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "SHOWERING, DINING, AND RESTING PEACEFULLY", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "サマーデール通り8213番地・床下這い込み空間の発掘", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "墓場の真上に位置する団欒のリビングルーム", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "床下の狭小な土中から発見された26体の遺体", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "精神の分断（コンパートメンタライゼーション）", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "殺戮直後にシャワーを浴び家族と団欒する病理", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t6_crawlspace_subterranean_tunnel", "still"),
            ("H", "3.08#1", "neutral", -0.02, 0.6, "t6_forensic_trowel_damp_soil", "pan"),
            ("H", "3.08#3", "neutral", -0.02, 0.6, "t6_crawlspace_trapdoor_opened", "push"),
            ("D", "3.10#4", "neutral", -0.03, 0.7, "t6_flashlight_beam_lime_dust", "still"),
            ("C", "3.11#1", "neutral", -0.02, 0.7, "t6_gacy_house_daylight_winter", "pull"),
            ("C", "3.11#2", "neutral", -0.02, 0.7, "t6_psychological_mask_metaphor", "push"),
            ("C", "3.11#3", "neutral", -0.02, 0.7, "t6_two_faces_silhouette", "still"),
            ("C", "3.11#8", "neutral", -0.02, 0.7, "t6_crawlspace_subterranean_tunnel", "pull"),
            ("H", "cta", "neutral", -0.02, 0.0, "t6_closing_rose_closed_dossier", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Bốn bài học cảnh báo đỏ sinh tồn",
        "title_en": "Four Vital Survival Red Flags",
        "title_ja": "日常に潜む4つの生存危険信号",
        "signs": [10],
        "theme_vn": "Nạn nhân học & 4 Dấu hiệu cảnh báo đỏ sinh tồn (Red Flags)",
        "theme_en": "Victimology & Four Critical Survival Red Flags",
        "theme_ja": "被害者学と日常に潜む4つの生存危険信号",
        "hook_vn": "Bốn dấu hiệu cảnh báo đỏ sinh tồn rút ra từ thảm kịch kinh hoàng mang tên John Wayne Gacy.",
        "hook_en": "Four vital survival red flags distilled from the harrowing John Wayne Gacy tragedy.",
        "hook_ja": "ジョン・ウェイン・ゲイシー事件の悲劇から導き出された、日常に潜む4つの生存危険信号。",
        "bgm": "bgm_cellar_wind.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_cellar_wind.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_cellar_wind.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_cellar_wind.mp3",
        "sfx_vn": ["amb_dark_drone.wav (nền)", "fx_clock_ticking.wav", "fx_warning_bell.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_dark_drone.wav (bed)", "fx_clock_ticking.wav", "fx_warning_bell.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_dark_drone.wav（環境音）", "fx_clock_ticking.wav", "fx_warning_bell.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN", "dur_s": 3.0},
            {"sau_cau": "TK5.01#3", "text": "ĐỎ 1: CẢNH GIÁC MẶT NẠ THIỆN NGUYỆN HÀO NHOÁNG", "dur_s": 2.5},
            {"sau_cau": "TK5.01#5", "text": "ĐỎ 2: BẪY CƠ HỘI VIỆC LÀM LƯƠNG CAO BẤT THƯỜNG", "dur_s": 2.5},
            {"sau_cau": "TK5.01#7", "text": "ĐỎ 3: TUYỆT ĐỐI KHÔNG ĐỂ NGƯỜI LẠ KHỐNG CHẾ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#9", "text": "ĐỎ 4: LUÔN LẮNG NGHE TRỰC GIÁC BẤT AN ĐẦU TIÊN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "FOUR VITAL SURVIVAL RED FLAGS", "dur_s": 3.0},
            {"after_id": "TK5.01#3", "text": "RED FLAG 1: CHARITY AND CIVIC PRESTIGE AS SHIELDS", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "RED FLAG 2: SUSPICIOUS HIGH-PAYING JOB OFFERS", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "RED FLAG 3: NEVER PERMIT RESTRAINT EVEN AS A TRICK", "dur_s": 2.5},
            {"after_id": "TK5.01#9", "text": "RED FLAG 4: TRUST YOUR INTUITIVE ALARM INSTANTLY", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "日常に潜む4つの生存のための危険信号", "dur_s": 3.0},
            {"after_id": "TK5.01#3", "text": "警告1：社会的地位や慈善の看板に惑わされない", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "警告2：若年層を狙った不自然な高額求人の罠", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "警告3：手品や冗談でも身体拘束を決して許さない", "dur_s": 2.5},
            {"after_id": "TK5.01#9", "text": "警告4：初期の違和感と直感の警報を信じて逃げる", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t6_closing_rose_closed_dossier", "still"),
            ("H", "5.06#9", "neutral", -0.02, 0.6, "t6_redflag_charity_facade", "still"),
            ("H", "5.06#11", "neutral", -0.02, 0.6, "t6_clown_mirror_chiaroscuro", "push"),
            ("H", "5.06#12", "neutral", -0.02, 0.6, "t6_pharmacy_counters_renovation", "pan"),
            ("H", "5.06#14", "neutral", -0.02, 0.6, "t6_deserted_parking_lot_snow", "pull"),
            ("H", "5.06#15", "neutral", -0.02, 0.6, "t6_redflag_trick_handcuffs", "still"),
            ("H", "5.06#17", "neutral", -0.02, 0.6, "t6_redflag_trick_handcuffs", "push"),
            ("H", "5.06#18", "neutral", -0.02, 0.6, "t6_redflag_externalized_blame", "still"),
            ("H", "5.06#20", "neutral", -0.02, 0.7, "t6_dossier_gacy_case_06", "pull"),
            ("H", "cta", "neutral", -0.02, 0.0, "t6_closing_rose_closed_dossier", "still")
        ]
    }
]

CTA_VI = "Tập sáu của Amber Eyes. Xem trọn vẹn tập phim tài liệu tại link trong bio."
CTA_EN = "Episode six of Amber Eyes. Watch the full documentary via the link in our bio."
CTA_JA = "アンバー・アイズ第6話。完全版ドキュメンタリーはプロフィールのリンクから。"

# ----------------------------------------------------------------------------
# 2. XUẤT CÁC FILE CHO TỪNG NGÔN NGỮ
# ----------------------------------------------------------------------------
def build_for_lang(lang):
    is_ja = (lang == "JA")
    is_en = (lang == "EN")
    is_vi = (lang == "VI")

    out_dir = OUT_VI if is_vi else (OUT_EN if is_en else OUT_JA)
    rates = RATE_VI if is_vi else (RATE_EN if is_en else RATE_JA)
    text_map = VI_MAP if is_vi else (EN_MAP if is_en else JA_MAP)

    spec_clips = {}
    summary_list = []

    for c in CLIPS_DEF:
        cid = c["id"]
        hook_txt = c["hook_vn"] if is_vi else (c["hook_en"] if is_en else c["hook_ja"])
        cta_txt = CTA_VI if is_vi else (CTA_EN if is_en else CTA_JA)
        title = c["title_vn"] if is_vi else (c["title_en"] if is_en else c["title_ja"])
        theme = c["theme_vn"] if is_vi else (c["theme_en"] if is_en else c["theme_ja"])
        bgm_desc = c["bgm_desc_vn"] if is_vi else (c["bgm_desc_en"] if is_en else c["bgm_desc_ja"])
        sfx_list = c["sfx_vn"] if is_vi else (c["sfx_en"] if is_en else c["sfx_ja"])
        overlays = c["overlay_vn"] if is_vi else (c["overlay_en"] if is_en else c["overlay_ja"])

        clip_lines = []
        tot_dur = 0.0

        for idx, (role, line_id, emo, spd, pause, bg, motion) in enumerate(c["items"], start=1):
            cl_id = f"{cid}.01#{idx}"
            if line_id == "hook":
                raw_text = hook_txt
                src_str = "hook — không phải dữ kiện kịch bản"
            elif line_id == "cta":
                raw_text = cta_txt
                src_str = "CTA — không phải dữ kiện kịch bản"
            else:
                raw_text = text_map[line_id]
                src_str = line_id

            if is_ja:
                units = len(re.sub(r"<#[\d.]+#>", " ", raw_text).replace(" ", "").strip())
                dur_line = units * rates[role]
            elif is_vi:
                spk = vi_numbers(re.sub(r"<#[\d.]+#>", " ", raw_text))
                units = len([w for w in spk.split() if w.strip()])
                dur_line = units * rates[role]
            else:
                spk = re.sub(r"<#[\d.]+#>", " ", raw_text)
                units = len([w for w in spk.split() if w.strip()])
                dur_line = units * rates[role]

            tot_dur += dur_line + pause

            clip_lines.append({
                "clip_line_id": cl_id,
                "role": role,
                "emotion": emo,
                "speed_offset": spd,
                "pause_after_s": pause,
                "bg": bg,
                "motion": motion,
                "text": raw_text,
                "src_script": src_str,
                "est_duration_s": round(dur_line + pause, 2)
            })

        tot_dur = round(tot_dur, 1)

        spec_clips[cid] = {
            "title": title,
            "theme": theme,
            "signs": c["signs"],
            "total_est_duration_s": tot_dur,
            "bgm": c["bgm"],
            "bgm_desc": bgm_desc,
            "sfx": sfx_list,
            "overlays": overlays,
            "lines": clip_lines
        }

        summary_list.append({
            "clip": cid,
            "title": title,
            "signs": c["signs"],
            "lines_count": len(clip_lines),
            "est_duration_s": tot_dur
        })

    # SPEC_AUDIO_CLIP_TAP06.json
    spec_full = {
        "_readme": f"Đặc tả audio và kịch bản dựng TikTok Tập 06 ({lang}) — sinh tự động bởi .work/_build_tk_tap06.py.",
        "_episode": "Tap06",
        "_language": lang,
        "_title": "NỤ CƯỜI CHÚ HỀ & 29 BÍ MẬT DƯỚI SÀN NHÀ" if is_vi else ("THE CLOWN'S SMILE & 29 BURIED SECRETS" if is_en else "道化師の笑顔と床下の29の秘密"),
        "_measured_rates": {r: round(rates[r], 4) for r in sorted(rates.keys())},
        "_clips_summary": summary_list,
        "clips": spec_clips
    }

    with (out_dir / f"SPEC_AUDIO_CLIP_TAP06.json").open("w", encoding="utf-8") as f:
        json.dump(spec_full, f, ensure_ascii=False, indent=2)

    # Viết Caption_TK*, MoTa_Ngan_TK*, MoTa_Dai_TK*
    for c in CLIPS_DEF:
        cid = c["id"]
        hook = c["hook_vn"] if is_vi else (c["hook_en"] if is_en else c["hook_ja"])
        title = c["title_vn"] if is_vi else (c["title_en"] if is_en else c["title_ja"])
        signs_str = " · ".join([f"#{s}" for s in c["signs"]])

        if is_vi:
            cap = f"""{hook} 👁️

Tập 06 · Nụ Cười Chú Hề — chỉ dấu tâm lý {signs_str}: {c['theme_vn']}.
Hồ sơ tâm lý tội phạm có thật về John Wayne Gacy dựa trên biên bản tòa án Cook County và hồ sơ điều tra của Sở Cảnh sát Des Plaines.

📺 Xem trọn vẹn tập phim tài liệu 32 phút tại link trong bio!
👉 Nhấn follow @ambereyes.vn để bước vào tâm trí kẻ thủ ác.

#tamlytoipham #ambereyes #johnwaynegacy #gacy #hosoanchuyen #khampha #kienthuc #toiphamcothat #podcastvietnam #truecrime"""

            mn = f"""{hook} 👁️
Tập 06 · Nụ Cười Chú Hề — Chỉ dấu {signs_str}: {c['theme_vn']}.

Hồ sơ tâm lý tội phạm có thật dựa trên biên bản tòa án Hạt Cook và tài liệu điều tra khai quật pháp y.
Khám phá chiếc bẫy còng tay ảo thuật chết người và cơ chế chia ngăn nhận thức rùng rợn của John Wayne Gacy.

📺 Xem đầy đủ tập phim tài liệu 32 phút tại link trên bio.
#tamlytoipham #ambereyes #johnwaynegacy #gacy #hosoanchuyen #truecrime"""

            md = f"""{hook} 👁️
TẬP 06 · NỤ CƯỜI CHÚ HỀ & 29 BÍ MẬT DƯỚI SÀN NHÀ
Chỉ dấu tâm lý chuyên sâu: {signs_str} — {c['theme_vn']}.

Suốt nhiều năm tại vùng ngoại ô Norwood Park, Chicago, John Wayne Gacy đã dệt nên một chiếc mặt nạ công dân hoàn hảo: Đội trưởng khu dân cư tận tụy, nhà thầu xây dựng PDM Contractors thành đạt, người từng bắt tay Đệ nhất phu nhân Rosalynn Carter và mang lại tiếng cười cho các bệnh nhi dưới lớp trang phục Chú hề Pogo. Chiếc mặt nạ hào nhoáng đó tạo nên Hiệu ứng Hào quang (Halo Effect) làm tê liệt hoàn toàn mọi nghi vấn của cộng đồng và chính quyền địa phương.

Thế nhưng, đằng sau cánh cửa số 8213 West Summerdale là chiếc bẫy săn mồi tinh vi. Lợi dụng lòng tin và lời hứa việc làm thêm mức lương hấp dẫn, Gacy dụ dỗ các thanh thiếu niên vào nhà, biểu diễn mánh khóe "còng tay ảo thuật" để khóa chặt khả năng tự vệ của nạn nhân. Dưới nền đất crawl space ẩm ướt, hắn đã biến chính mái ấm của mình thành một khu lăng mộ chôn cất 26 thi thể, trong khi vẫn thản nhiên tổ chức tiệc nướng, đón mẹ về sống cùng nhờ cơ chế Phân mảnh tâm trí (Compartmentalization) cực đoan.

Cuộc đối đầu kịch tính với Đội đặc nhiệm của Sở Cảnh sát Des Plaines do Trung úy Joseph Kozenczak dẫn đầu đã phơi bày toàn bộ sự ngạo mạn ái kỷ của hung thủ. Khi bị bắt, Gacy ngụy tạo nhân cách "Jack Hanley" nhằm chối bỏ trách nhiệm, nhưng bản án tử hình lịch sử tại Tòa án Cook County đã đặt dấu chấm hết cho con quỷ đội lốt người. Hồ sơ đúc kết 4 bài học cảnh báo đỏ sinh tồn vô giá cho thanh thiếu niên và các bậc phụ huynh.

📺 Xem trọn vẹn tập phim tài liệu 32 phút được phân tích chuyên sâu tại link bio kênh Amber Eyes.
👉 Follow kênh để đồng hành cùng những hồ sơ tâm lý tội phạm chấn động tiếp theo.

#tamlytoipham #ambereyes #johnwaynegacy #gacy #hosoanchuyen #khampha #kienthuc #toiphamcothat #podcastvietnam #truecrime #phapluat #tamlyhoc"""

        elif is_en:
            cap = f"""{hook} 👁️

Ep. 06 · The Clown's Smile — Psychological Markers {signs_str}: {c['theme_en']}.
Authentic true crime criminal profiling of John Wayne Gacy based on Cook County court transcripts and Des Plaines Police records.

📺 Watch the full 32-minute documentary via the link in our bio!
👉 Follow @ambereyes.official to venture into the psychology of extreme crime.

#truecrime #psychology #johnwaynegacy #gacy #criminalpsychology #forensics #fbi #crimedocumentary #podcast"""

            mn = f"""{hook} 👁️

Episode 06 · The Clown's Smile — Psychological Markers {signs_str}: {c['theme_en']}.
Authentic forensic breakdown based on official police records and subterranean excavation evidence.

Discover the fatal handcuff trick and John Wayne Gacy’s extreme psychological compartmentalization.

📺 Full 32-minute documentary streaming now via our bio link.
#truecrime #johnwaynegacy #gacy #forensics #criminalminds"""

            md = f"""{hook} 👁️
EPISODE 06 · THE CLOWN'S SMILE & 29 BURIED SECRETS
In-depth Psychological Analysis: Markers {signs_str} — {c['theme_en']}.

For years in suburban Norwood Park, Chicago, John Wayne Gacy cultivated a pristine civic mask: Democratic precinct captain, successful contractor of PDM Contractors, photographed shaking hands with First Lady Rosalynn Carter, and performing charity shows as Pogo the Clown for hospitalized children. This radiant civic facade created a potent Halo Effect that blinded his neighbors and law enforcement alike.

Behind the closed doors of 8213 West Summerdale, however, operated a lethal predatory trap. Exploiting young men’s desire for well-paying construction jobs, Gacy lured them into his home, demonstrating a deceptive "handcuff trick" under the guise of an escape challenge to incapacitate their resistance. Beneath the claustrophobic crawl space, he buried 26 young victims, continuing to host backyard barbeques and live placidly with his family through extreme psychological compartmentalization.

The high-stakes psychological war waged by Lieutenant Joseph Kozenczak and the Des Plaines Police Department ultimately broke the predator's defenses. Despite attempting to feign multiple personality disorder with the fabricated alter ego "Jack Hanley," Gacy was convicted of 33 counts of murder and sentenced to death. This landmark dossier provides four indispensable survival red flags against predatory manipulation.

📺 Watch the full 32-minute investigative documentary via the link in bio.
👉 Follow Amber Eyes for rigorous criminal psychological profiling.

#truecrime #johnwaynegacy #gacy #psychology #forensics #crimedocumentary #fbi #podcast"""

        else: # JA
            cap = f"""{hook} 👁️

第06話 · 道化師の笑顔 — 心理指標 {signs_str}: {c['theme_ja']}。
クック郡裁判記録およびデスプレーンズ警察調書に基づく本格犯罪心理学ドキュメンタリー。

📺 完全版ドキュメンタリー（32分）はYouTubeで公開中 — プロフィールのリンクから！
👉 フォローして次回の深層心理プロファイリングをお見逃しなく。

#犯罪心理学 #アンバーアイズ #実話 #未解決事件 #事件 #心理学 #ドキュメンタリー #ジョンウェインゲイシー #プロファイリング"""

            mn = f"""{hook} 👁️

第06話 · 道化師の笑顔 — 心理指標 {signs_str}: {c['theme_ja']}。
裁判記録・法医鑑定調書に基づく犯罪心理学ドキュメンタリー。

全米を震撼させた道化師の社会的仮面と、床下に封印された29の戦慄の真実。

📺 YouTubeで32分の完全版ドキュメンタリーを公開中 — プロフィールのリンクからご覧ください。
#犯罪心理学 #アンバーアイズ #実話 #事件 #ドキュメンタリー #ゲイシー"""

            md = f"""{hook} 👁️
第06話 · 道化師の笑顔と床下の29の秘密
深層心理学的プロファイリング：心理指標 {signs_str} — {c['theme_ja']}。

シカゴ郊外ノーウッド・パークで、ジョン・ウェイン・ゲイシーは完璧な「模範市民の仮面」を被り続けていました。有力建設業者PDMコントラクターズの社長、民主党の信望厚い地区幹部、ファーストレディであるロザリン・カーター夫人と握手を交わした名士、そして「道化師ポゴ」の衣装で小児病棟を慰問する心優しき篤志家。この眩い社会的立場が生み出した「ハロー効果」は、周囲の警戒心を完全に麻痺させていました。

しかし、サマーデール通り8213番地の自宅内部では、冷酷な捕食罠が張り巡らされていました。高額な求人や好条件の仕事を餌に少年たちを誘い込み、「手錠の奇術」と称する手品を見せると偽って獲物自身に手錠をかけさせ、無抵抗の極限状態に追い込む手口。自らが命を奪った犠牲者たちを自宅の床下這い込み空間に26体も埋めながら、その真上で家族と団欒し、平然とパーティーを開催する「極限の精神分断（コンパートメンタライゼーション）」の異常性。

デスプレーンズ警察のジョセフ・コゼンチャック警部補率いる特別捜査班による24時間の密着尾行と執念の家宅捜索により、悪夢の全貌が暴かれました。ゲイシーは「ジャック・ハンリー」という別人格を捏造して心神喪失を偽装しようと試みるも、緻密な計画性と証拠隠滅の意志が証明され、歴史的な有罪判決と死刑判決が下されました。本事件から導き出された4つの生存危険信号を詳細に解説します。

📺 YouTubeにて32分の完全版ドキュメンタリーを公開中 — プロフィールのリンクからご覧ください。
👉 アンバー・アイズをフォローして、深層心理の解明を共に見届けてください。

#犯罪心理学 #アンバーアイズ #実話 #事件 #ドキュメンタリー #ゲイシー #プロファイリング #海外事件 #歴史"""

        (out_dir / f"Caption_{cid}.txt").write_text(cap, encoding="utf-8")
        (out_dir / f"MoTa_Ngan_{cid}.txt").write_text(mn, encoding="utf-8")
        (out_dir / f"MoTa_Dai_{cid}.txt").write_text(md, encoding="utf-8")

    # KE_HOACH_CLIP_TAP06.md
    plan_fn = "KE_HOACH_CLIP_TAP06.md" if is_vi else (f"KE_HOACH_CLIP_TAP06_{lang}.md")
    
    doc_lines = []
    doc_lines.append(f"# KẾ HOẠCH CLIP TIKTOK — TẬP 06 ({lang}) · \"NỤ CƯỜI CHÚ HỀ & 29 BÍ MẬT DƯỚI SÀN NHÀ\"" if is_vi else (f"# TIKTOK CLIPS PLAN — EPISODE 06 ({lang}) · \"THE CLOWN'S SMILE & 29 BURIED SECRETS\"" if is_en else f"# TIKTOK企画書 — 第06話 ({lang}) · 『道化師の笑顔と床下の29の秘密』"))
    doc_lines.append("")
    doc_lines.append(f"*Ngày: 20/11/2026 · Ngôn ngữ: **{lang}** · Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*")
    doc_lines.append(f"*Đặc tả audio: `02_SAN_XUAT/TIKTOK/Tap06{'' if is_vi else '_' + lang}/SPEC_AUDIO_CLIP_TAP06.json`*")
    doc_lines.append("")
    doc_lines.append("---")
    doc_lines.append("")
    doc_lines.append("## 0. Tóm tắt chốt" if is_vi else ("## 0. Executive Summary" if is_en else "## 0. 概要サマリー"))
    doc_lines.append("")
    doc_lines.append("| Hạng mục | Giá trị |" if is_vi else ("| Item | Value |" if is_en else "| 項目 | 設定値 |"))
    doc_lines.append("|---|---|" if is_vi else ("|---|---|" if is_en else "|---|---|"))
    doc_lines.append(f"| Số clip | **5 clip** (TK1–TK4 phân tích + TK5 bài học sinh tồn) |" if is_vi else (f"| Clips Count | **5 clips** (TK1–TK4 Core Profiling + TK5 Survival Red Flags) |" if is_en else f"| クリップ数 | **全5本**（TK1〜TK4 心理分析 + TK5 生存警告） |"))
    total_lines_cnt = sum(len(c["items"]) for c in CLIPS_DEF)
    doc_lines.append(f"| Tổng câu | **{total_lines_cnt} câu** |" if is_vi else (f"| Total Lines | **{total_lines_cnt} lines** |" if is_en else f"| 総行数 | **{total_lines_cnt}行** |"))
    doc_lines.append(f"| Tỷ lệ đọc chuẩn đo từ Master | {rates} |" if is_vi else (f"| Measured Speech Rates from Master | {rates} |" if is_en else f"| マスター実測発話レート | {rates} |"))
    doc_lines.append("")
    doc_lines.append("---")
    doc_lines.append("")
    doc_lines.append("## 1. Danh sách 5 clip và chỉ dấu tâm lý (K10)" if is_vi else ("## 1. Five Clips and Psychological Indicators (K10)" if is_en else "## 1. 全5本クリップと心理指標（K10）"))
    doc_lines.append("")
    doc_lines.append("| Clip | Chỉ dấu | Chủ đề | Hook (0–3 s) | Thời lượng ước lượng |" if is_vi else ("| Clip | Indicators | Theme | Hook (0–3s) | Est. Duration |" if is_en else "| クリップ | 心理指標 | 主題テーマ | フック（0〜3秒） | 推定尺 |"))
    doc_lines.append("|---|---|---|---|---|" if is_vi else ("|---|---|---|---|---|" if is_en else "|---|---|---|---|---|"))

    for c in CLIPS_DEF:
        cid = c["id"]
        s_info = spec_clips[cid]
        s_signs = " · ".join([f"#{s}" for s in c["signs"]])
        h_txt = c["hook_vn"] if is_vi else (c["hook_en"] if is_en else c["hook_ja"])
        t_txt = c["theme_vn"] if is_vi else (c["theme_en"] if is_en else c["theme_ja"])
        doc_lines.append(f"| **{cid}** | {s_signs} | {t_txt} | *\"{h_txt}\"* | {s_info['total_est_duration_s']} s ({len(c['items'])} câu) |")

    doc_lines.append("")
    doc_lines.append("---")
    doc_lines.append("")
    doc_lines.append("## 2. Chi tiết từng clip (Kịch bản, Phân cảnh, Chữ trên hình & Âm thanh)" if is_vi else ("## 2. Detailed Clip Breakdown (Script, Visuals, Overlays & Audio)" if is_en else "## 2. 各クリップ詳細構成（台本・演出・画面テロップ・音響）"))
    doc_lines.append("")

    for c in CLIPS_DEF:
        cid = c["id"]
        s_info = spec_clips[cid]
        t_name = c["title_vn"] if is_vi else (c["title_en"] if is_en else c["title_ja"])
        doc_lines.append(f"### 2.{cid[-1]} CLIP {cid} — \"{t_name}\"")
        doc_lines.append("")
        doc_lines.append(f"*Thời lượng ước tính: {s_info['total_est_duration_s']} s · BGM: `{s_info['bgm']}` ({s_info['bgm_desc']})*")
        doc_lines.append(f"*SFX: {', '.join(s_info['sfx'])}*")
        doc_lines.append("")
        doc_lines.append("| Mã | Vai | Nghỉ (s) | Nền ảnh | Chuyển động | Lời đọc | Nguồn |" if is_vi else ("| Line ID | Role | Pause (s) | Background | Motion | Spoken Text | Source |" if is_en else "| 行ID | 役名 | 間（秒） | 背景画像 | カメラ動作 | 発話台本 | 原典 |"))
        doc_lines.append("|---|---|---:|---|---|---|---|" if is_vi else ("|---|---|---:|---|---|---|---|" if is_en else "|---|---|---:|---|---|---|---|"))

        for line in s_info["lines"]:
            doc_lines.append(f"| `{line['clip_line_id']}` | {line['role']} | {line['pause_after_s']} | `{line['bg']}` | {line['motion']} | {line['text']} | {line['src_script']} |")

        doc_lines.append("")
        doc_lines.append("**Thẻ chữ trên hình (Text Scrim / Overlay Card):**" if is_vi else ("**On-screen Overlay Cards:**" if is_en else "**画面表示テロップ（オーバーレイカード）：**"))
        for ov in s_info["overlays"]:
            key_id = ov.get("sau_cau") or ov.get("after_id")
            doc_lines.append(f"- `{key_id}` → *\"{ov['text']}\"* ({ov['dur_s']} s)")
        doc_lines.append("")

    (out_dir / plan_fn).write_text("\n".join(doc_lines), encoding="utf-8")
    print(f"Đã xuất thành công gói TikTok Tap06 [{lang}] vào {out_dir}")

# ----------------------------------------------------------------------------
# 3. CẬP NHẬT BẢNG THEO DÕI TIKTOK CSV
# ----------------------------------------------------------------------------
def update_tracking_table():
    csv_path = ROOT / "02_SAN_XUAT" / "TIKTOK" / "BangTheoDoi_TikTok.csv"
    if not csv_path.exists():
        return
    lines = csv_path.read_text(encoding="utf-8").splitlines()
    existing_keys = set()
    for l in lines:
        parts = l.split(",")
        if len(parts) >= 2:
            existing_keys.add(f"{parts[0]}_{parts[1]}")

    new_rows = []
    # Đoạn dữ liệu cần thêm
    for lang, prefix in [("VI", "Tap06"), ("EN", "Tap06_EN"), ("JA", "Tap06_JA")]:
        spec_fn = (ROOT / "02_SAN_XUAT" / "TIKTOK" / prefix / "SPEC_AUDIO_CLIP_TAP06.json")
        if not spec_fn.exists():
            continue
        data = json.load(spec_fn.open(encoding="utf-8"))
        for s in data["_clips_summary"]:
            cid = s["clip"]
            key = f"{prefix}_{cid}"
            if key in existing_keys:
                continue
            row = f"{prefix},{cid},{s['title']},{lang},{s['est_duration_s']},{s['lines_count']},Kịch bản hoàn thành,2026-11-20"
            new_rows.append(row)

    if new_rows:
        lines.extend(new_rows)
        csv_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print(f"Đã cập nhật thêm {len(new_rows)} dòng vào BangTheoDoi_TikTok.csv")

if __name__ == "__main__":
    for l in ["VI", "EN", "JA"]:
        build_for_lang(l)
    update_tracking_table()
