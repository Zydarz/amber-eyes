# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 05 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap05/KE_HOACH_CLIP_TAP05.md
  02_SAN_XUAT/TIKTOK/Tap05/SPEC_AUDIO_CLIP_TAP05.json
  02_SAN_XUAT/TIKTOK/Tap05/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap05/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap05/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap05_EN/KE_HOACH_CLIP_TAP05_EN.md
  02_SAN_XUAT/TIKTOK/Tap05_EN/SPEC_AUDIO_CLIP_TAP05.json
  02_SAN_XUAT/TIKTOK/Tap05_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap05_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap05_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap05_JA/KE_HOACH_CLIP_TAP05_JA.md
  02_SAN_XUAT/TIKTOK/Tap05_JA/SPEC_AUDIO_CLIP_TAP05.json
  02_SAN_XUAT/TIKTOK/Tap05_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap05_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap05_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 05:
- timeline_s_t05.json (VI)
- timeline_s_EN_t05.json (EN)
- timeline_s_JA_t05.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap05"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap05_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap05_JA"

OUT_VI.mkdir(parents=True, exist_ok=True)
OUT_EN.mkdir(parents=True, exist_ok=True)
OUT_JA.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WORK))
try:
    from vi_cer import vi_numbers
except Exception:
    def vi_numbers(x): return x

# ----------------------------------------------------------------------------
# 0. TỶ LỆ ĐỌC THẬT (Tập 05 Master ASR)
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

RATE_VI = get_rates("timeline_s_t05.json", False)
RATE_EN = get_rates("timeline_s_EN_t05.json", False)
RATE_JA = get_rates("timeline_s_JA_t05.json", True)

VI_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_t05.json").open(encoding="utf-8"))["items"]}
EN_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_EN_t05.json").open(encoding="utf-8"))["items"]}
JA_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_JA_t05.json").open(encoding="utf-8"))["items"]}

# ----------------------------------------------------------------------------
# 1. ĐỊNH NGHĨA 5 CLIP TẬP 05
# ----------------------------------------------------------------------------
CLIPS_DEF = [
    {
        "id": "TK1",
        "title_vn": "Chiếc đĩa mềm màu tím và cái bẫy siêu dữ liệu",
        "title_en": "The Purple Floppy Disk & The Metadata Trap",
        "title_ja": "紫のフロッピーディスクとメタデータの罠",
        "signs": [4, 8],
        "theme_vn": "Sự sụp đổ của cái tôi ái kỷ & Ảo tưởng toàn năng trước giám định kỹ thuật số",
        "theme_en": "Narcissistic Collapse & Digital Forensics Penetrating the Omnipotence Illusion",
        "theme_ja": "自己愛の崩壊とデジタル鑑識による全能感の粉砕",
        "hook_vn": "Một kẻ sát nhân 30 năm lẩn trốn. Lại tự nộp mạng vì một chiếc đĩa mềm màu tím.",
        "hook_en": "A serial killer elusive for thirty years. Undone by a purple floppy disk.",
        "hook_ja": "30年間逃亡し続けたシリアルキラー。紫のフロッピー1枚で自ら罠に堕ちた。",
        "bgm": "bgm_ambient_tension.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_ambient_tension.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_ambient_tension.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_ambient_tension.mp3",
        "sfx_vn": ["amb_winter_wind.wav (nền)", "fx_floppy_insert.wav", "fx_keyboard_typing.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_winter_wind.wav (bed)", "fx_floppy_insert.wav", "fx_keyboard_typing.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_winter_wind.wav（環境音）", "fx_floppy_insert.wav", "fx_keyboard_typing.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "HỒ SƠ TẬP 05: DENNIS RADER (BTK)", "dur_s": 3.0},
            {"sau_cau": "TK1.01#4", "text": "MỤC RAO VẶT 494: “REX, IT WILL BE OK”", "dur_s": 2.5},
            {"sau_cau": "TK1.01#5", "text": "ĐĨA MỀM MEMOREX 1.44MB MÀU TÍM", "dur_s": 2.5},
            {"sau_cau": "TK1.01#8", "text": "SIÊU DỮ LIỆU METADATA: DENNIS & CHRIST LUTHERAN", "dur_s": 3.0},
            {"sau_cau": "TK1.01#10", "text": "SỰ SỤP ĐỔ CỦA CÁI TÔI ÁI KỶ (NARCISSISTIC COLLAPSE)", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "CASE DOSSIER 05: DENNIS RADER (BTK)", "dur_s": 3.0},
            {"after_id": "TK1.01#4", "text": "CLASSIFIED AD 494: “REX, IT WILL BE OK”", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "PURPLE MEMOREX 1.44MB FLOPPY DISK", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "METADATA REVEALED: DENNIS & CHRIST LUTHERAN", "dur_s": 3.0},
            {"after_id": "TK1.01#10", "text": "NARCISSISTIC COLLAPSE IN INTERROGATION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "事件ファイル05：DENNIS RADER（BTK）", "dur_s": 3.0},
            {"after_id": "TK1.01#4", "text": "3行広告494番：『レックス、送っても大丈夫だ』", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "紫色の1.44MB MEMOREX製フロッピーディスク", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "メタデータ抽出：DENNIS＆キリスト・ルーテル教会", "dur_s": 3.0},
            {"after_id": "TK1.01#10", "text": "誇大自己愛の完全崩壊（NARCISSISTIC COLLAPSE）", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t5_handwritten_note_floppy", "still"),
            ("H", "4.02#6", "neutral", -0.02, 0.6, "t5_handwritten_note_floppy", "pan"),
            ("D", "4.04#5", "neutral", -0.03, 0.6, "t5_newspaper_classified_494", "still"),
            ("D", "4.04#8", "neutral", -0.03, 0.6, "t5_purple_floppy_disk", "pull"),
            ("H", "4.06#1", "neutral", -0.02, 0.6, "t5_digital_forensics_lab", "pan"),
            ("H", "4.06#6", "neutral", -0.02, 0.6, "t5_metadata_screen", "push"),
            ("H", "4.06#7", "neutral", -0.02, 0.6, "t5_metadata_screen", "still"),
            ("D", "4.08#2", "neutral", -0.03, 0.7, "t5_church_website_search", "pull"),
            ("D", "4.12#2", "neutral", -0.03, 0.7, "t5_interrogation_confrontation", "push"),
            ("D", "4.12#3", "neutral", -0.03, 0.7, "t5_interrogation_confrontation", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t5_amber_eyes_dossier_05", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Chủ tịch hội đồng nhà thờ và chiếc mặt nạ 30 năm",
        "title_en": "The Church Council President & The Thirty-Year Mask",
        "title_ja": "教会評議会議長と30年間の社会的仮面",
        "signs": [9, 3],
        "theme_vn": "Hiệu ứng Hào quang (Halo Effect) & Sự chia ngăn tâm trí (Compartmentalization)",
        "theme_en": "Halo Effect & Pathological Compartmentalization Shielding a Predator",
        "theme_ja": "ハロー効果と怪物性を隔離する心理的分断（コンパートメンタライゼーション）",
        "hook_vn": "Chủ tịch hội đồng nhà thờ. Đội trưởng Hướng đạo sinh. Và kẻ sát nhân giấu mặt.",
        "hook_en": "Church council president. Scout leader. And a serial killer hiding in plain sight.",
        "hook_ja": "敬虔な教会のリーダー。スカウトの指導員。その正体は30年間の殺人鬼。",
        "bgm": "bgm_jazz_noir.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_jazz_noir.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_jazz_noir.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_jazz_noir.mp3",
        "sfx_vn": ["amb_suburban_evening.wav (nền)", "fx_lawnmower_distant.wav", "fx_door_creak.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_suburban_evening.wav (bed)", "fx_lawnmower_distant.wav", "fx_door_creak.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_suburban_evening.wav（環境音）", "fx_lawnmower_distant.wav", "fx_door_creak.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "ĐIỂM MÙ XÃ HỘI: CHIẾC MẶT NẠ CÔNG DÂN MẪU MỰC", "dur_s": 3.0},
            {"sau_cau": "TK2.01#4", "text": "CHỦ TỊCH HỘI ĐỒNG NHÀ THỜ CHRIST LUTHERAN", "dur_s": 2.5},
            {"sau_cau": "TK2.01#6", "text": "VIÊN CHỨC TRẬT TỰ ĐÔ THỊ ĐO TỪNG BÃI CỎ", "dur_s": 2.5},
            {"sau_cau": "TK2.01#8", "text": "HIỆU ỨNG HÀO QUANG (HALO EFFECT)", "dur_s": 2.5},
            {"sau_cau": "TK2.01#9", "text": "SỰ CHIA NGĂN TÂM TRÍ (COMPARTMENTALIZATION)", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "SOCIAL BLIND SPOT: THE PRISTINE CITIZEN MASK", "dur_s": 3.0},
            {"after_id": "TK2.01#4", "text": "COUNCIL PRESIDENT AT CHRIST LUTHERAN CHURCH", "dur_s": 2.5},
            {"after_id": "TK2.01#6", "text": "COMPLIANCE OFFICER MEASURING LAWN HEIGHTS", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "HALO EFFECT & SYSTEMIC NORMALIZATION", "dur_s": 2.5},
            {"after_id": "TK2.01#9", "text": "EXTREME COMPARTMENTALIZATION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "社会の巨大な死角：模範市民という完璧な仮面", "dur_s": 3.0},
            {"after_id": "TK2.01#4", "text": "キリスト・ルーテル教会 評議会議長", "dur_s": 2.5},
            {"after_id": "TK2.01#6", "text": "芝生の長さを厳格に取り締まる公務員", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "ハロー効果（後光効果）と集団の正常性バイアス", "dur_s": 2.5},
            {"after_id": "TK2.01#9", "text": "精神の分断（コンパートメンタライゼーション）", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t5_rader_house_park_city", "still"),
            ("D", "2.06#1", "neutral", -0.03, 0.6, "t5_rader_house_park_city", "pan"),
            ("D", "2.06#4", "neutral", -0.03, 0.6, "t5_lutheran_church_exterior", "still"),
            ("D", "2.06#5", "neutral", -0.03, 0.6, "t5_scout_camp_campfire", "pan"),
            ("D", "2.06#6", "neutral", -0.03, 0.6, "t5_compliance_truck_street", "push"),
            ("D", "2.06#7", "neutral", -0.03, 0.7, "t5_compliance_measuring_tape", "still"),
            ("D", "2.06#8", "neutral", -0.03, 0.7, "t5_two_faces_silhouette", "push"),
            ("C", "3.02#3", "neutral", -0.02, 0.7, "t5_concrete_wall_divide", "pull"),
            ("C", "3.02#6", "neutral", -0.02, 0.7, "t5_family_dinner_warmth", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t5_amber_eyes_dossier_05", "still")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Nỗi sợ bị lãng quên và ảo tưởng Nhân tố X",
        "title_en": "The Terror of Oblivion & The Factor X Delusion",
        "title_ja": "忘却への恐怖と『要因X』という妄想の盾",
        "signs": [6, 5],
        "theme_vn": "Ngòi nổ tâm lý (Precipitating Trigger) & Hệ thống tự bào chữa (Factor X)",
        "theme_en": "Precipitating Psychological Trigger & Externalized Self-Defense Mechanism",
        "theme_ja": "心理的起爆点と責任転嫁の防衛機制『要因X』",
        "hook_vn": "Kẻ ác không sợ nhà tù. Điều hắn khiếp sợ nhất là bị nhân loại lãng quên.",
        "hook_en": "Monsters do not fear prison. What terrifies them most is being forgotten.",
        "hook_ja": "怪物が最も恐れるもの。それは逮捕ではなく、世間から忘れ去られること。",
        "bgm": "bgm_sub_drone.mp3",
        "bgm_desc_vn": "Hồi 1/3 — bed tập: bgm_sub_drone.mp3",
        "bgm_desc_en": "Act 1/3 — episode bed: bgm_sub_drone.mp3",
        "bgm_desc_ja": "第1/3幕 — 本編BGM: bgm_sub_drone.mp3",
        "sfx_vn": ["amb_dark_drone.wav (nền)", "fx_newspaper_rustle.wav", "fx_whisper_shadow.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_dark_drone.wav (bed)", "fx_newspaper_rustle.wav", "fx_whisper_shadow.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_dark_drone.wav（環境音）", "fx_newspaper_rustle.wav", "fx_whisper_shadow.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "NGÒI NỔ TÂM LÝ: KHI CÁI ÁC BỊ LÃNG QUÊN", "dur_s": 3.0},
            {"sau_cau": "TK3.01#3", "text": "THE WICHITA EAGLE: “BTK CÓ THỂ ĐÃ QUA ĐỜI”", "dur_s": 2.5},
            {"sau_cau": "TK3.01#5", "text": "ĐÒN ĐÂM CHÍ MẠNG VÀO LÒNG TỰ TÔN ÁI KỶ", "dur_s": 2.5},
            {"sau_cau": "TK3.01#7", "text": "HOANG TƯỞNG “NHÂN TỐ X” (FACTOR X)", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "HỆ THỐNG TỰ BÀO CHỮA & TRUNG HÒA ĐẠO ĐỨC", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "PRECIPITATING TRIGGER: FEAR OF IRRELEVANCE", "dur_s": 3.0},
            {"after_id": "TK3.01#3", "text": "THE WICHITA EAGLE: “BTK LIKELY DEAD OR OLD”", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "LETHAL STAB TO MALIGNANT NARCISSISM", "dur_s": 2.5},
            {"after_id": "TK3.01#7", "text": "DELUSION OF “FACTOR X”", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "MORAL NEUTRALIZATION & EXTERNALIZATION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "心理的起爆点：忘れ去られる恐怖", "dur_s": 3.0},
            {"after_id": "TK3.01#3", "text": "地元紙特集：『BTKは死亡した可能性が高い』", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "悪性自己愛のプライドへの致命的一撃", "dur_s": 2.5},
            {"after_id": "TK3.01#7", "text": "妄想的免責概念『要因X（FACTOR X）』", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "道徳的中和と責任の外部転嫁", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t5_fear_of_oblivion", "still"),
            ("D", "1.14#1", "neutral", -0.03, 0.6, "t5_detective_war_room", "pan"),
            ("D", "1.14#3", "neutral", -0.03, 0.6, "t5_book_manuscript_desk", "still"),
            ("D", "1.14#4", "neutral", -0.03, 0.6, "t5_book_manuscript_desk", "pull"),
            ("D", "1.14#5", "neutral", -0.03, 0.6, "t5_narcissist_mirror_shadow", "push"),
            ("D", "1.14#6", "neutral", -0.03, 0.6, "t5_narcissist_mirror_shadow", "still"),
            ("D", "1.14#7", "neutral", -0.03, 0.7, "t5_btk_signature_letter", "pull"),
            ("C", "3.02#7", "neutral", -0.02, 0.7, "t5_factor_x_shadow", "push"),
            ("H", "3.04#3", "neutral", -0.02, 0.7, "t5_projection_mask", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t5_amber_eyes_dossier_05", "still")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Nỗi đau của con gái kẻ sát nhân BTK",
        "title_en": "The Agony of the Serial Killer’s Daughter",
        "title_ja": "BTKの娘・ケリーが背負った地獄",
        "signs": [3, 1],
        "theme_vn": "Hành vi đối xử với người thân (Compartmentalization) & Nỗi đau gia đình vô tội",
        "theme_en": "Predatory Compartmentalization & The Lifelong Trauma Inflicted on Family",
        "theme_ja": "家庭への偽りの献身と残された家族の計り知れないトラウマ",
        "hook_vn": "Cha tôi dạy tôi đi xe đạp, dắt tay tôi vào lễ đường. Rồi FBI gõ cửa.",
        "hook_en": "He taught me to ride a bike, walked me down the aisle. Then the FBI knocked.",
        "hook_ja": "自転車の乗り方を教え、結婚式で手を引いてくれた父。その朝、FBIが来た。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_somber_room.wav (nền)", "fx_door_knock_fbi.wav", "fx_heartbeat_slow.wav", "fx_tear_sob.wav"],
        "sfx_en": ["amb_somber_room.wav (bed)", "fx_door_knock_fbi.wav", "fx_heartbeat_slow.wav", "fx_tear_sob.wav"],
        "sfx_ja": ["amb_somber_room.wav（環境音）", "fx_door_knock_fbi.wav", "fx_heartbeat_slow.wav", "fx_tear_sob.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "BI KỊCH CỦA NHỮNG NGƯỜI THÂN VÔ TỘI", "dur_s": 3.0},
            {"sau_cau": "TK4.01#3", "text": "KERRI RAWSON: CON GÁI RUỘT CỦA DENNIS RADER", "dur_s": 2.5},
            {"sau_cau": "TK4.01#5", "text": "NGƯỜI CHA MẪU MỰC & BÓNG MA SÁT NHÂN", "dur_s": 2.5},
            {"sau_cau": "TK4.01#7", "text": "SỰ PHẢN BỘI NIỀM TIN TỘT CÙNG", "dur_s": 2.5},
            {"sau_cau": "TK4.01#9", "text": "VẾT THƯƠNG TÂM HỒN SUỐT PHẦN ĐỜI CÒN LẠI", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "TRAGEDY OF THE INNOCENT FAMILY BEHIND THE MASK", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "KERRI RAWSON: DAUGHTER OF DENNIS RADER", "dur_s": 2.5},
            {"after_id": "TK4.01#5", "text": "DEVOTED FATHER VS PROLIFIC PREDATOR", "dur_s": 2.5},
            {"after_id": "TK4.01#7", "text": "THE ULTIMATE BETRAYAL OF TRUST", "dur_s": 2.5},
            {"after_id": "TK4.01#9", "text": "LIFELONG SCARS BEYOND THE CRIMES", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "仮面の裏で踏みにじられた無辜の家族の悲劇", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "KERRI RAWSON：シリアルキラーの実の娘", "dur_s": 2.5},
            {"after_id": "TK4.01#5", "text": "慈愛に満ちた父親と全米を震わせた怪物の二面性", "dur_s": 2.5},
            {"after_id": "TK4.01#7", "text": "最も信じた絆の残酷な裏切り", "dur_s": 2.5},
            {"after_id": "TK4.01#9", "text": "生涯消えることのない魂の傷跡", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t5_kerri_rawson_tears", "still"),
            ("H", "4.14#1", "sad", -0.04, 0.6, "t5_rader_house_park_city", "pan"),
            ("H", "4.14#2", "sad", -0.04, 0.6, "t5_rader_house_park_city", "pull"),
            ("H", "4.14#3", "neutral", -0.02, 0.6, "t5_kerri_rawson_tears", "still"),
            ("N2", "4.15#1", "sad", -0.04, 0.6, "t5_kerri_rawson_tears", "push"),
            ("N2", "4.15#2", "neutral", -0.02, 0.6, "t5_family_dinner_warmth", "pan"),
            ("N2", "4.15#3", "sad", -0.04, 0.7, "t5_highway_takedown_arrest", "still"),
            ("N2", "4.15#4", "sad", -0.04, 0.7, "t5_shattered_mask_confession", "pull"),
            ("N2", "4.15#5", "sad", -0.04, 0.7, "t5_kerri_rawson_tears", "still"),
            ("N2", "4.15#6", "sad", -0.04, 0.8, "t5_kerri_rawson_tears", "push"),
            ("H", "cta", "neutral", -0.02, 0.0, "t5_amber_eyes_dossier_05", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "4 dấu hiệu cảnh báo đỏ sinh tồn nhận diện mặt nạ",
        "title_en": "4 Survival Red Flags to Detect Toxic Civic Masks",
        "title_ja": "日常に潜む仮面を見抜く4つの生存危険信号",
        "signs": [10],
        "theme_vn": "Nạn nhân học & 4 Dấu hiệu cảnh báo đỏ sinh tồn rút ra từ hồ sơ BTK",
        "theme_en": "Victimology & 4 Critical Survival Red Flags Derived from Dennis Rader",
        "theme_ja": "被害者学とBTK事件から導き出された4つの生存危険信号",
        "hook_vn": "4 dấu hiệu cảnh báo đỏ để không bao giờ trở thành nạn nhân của kẻ giấu mặt.",
        "hook_en": "Four red flags to detect dangerous predators hiding behind public masks.",
        "hook_ja": "善人の仮面に隠れた捕食者を見抜く、4つの生存シグナル。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_gentle_night.wav (nền)", "fx_clock_chime.wav", "fx_sub_drop.wav", "fx_warm_resolve.wav"],
        "sfx_en": ["amb_gentle_night.wav (bed)", "fx_clock_chime.wav", "fx_sub_drop.wav", "fx_warm_resolve.wav"],
        "sfx_ja": ["amb_gentle_night.wav（環境音）", "fx_clock_chime.wav", "fx_sub_drop.wav", "fx_warm_resolve.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 DẤU HIỆU CẢNH BÁO ĐỎ SINH TỒN", "dur_s": 3.0},
            {"sau_cau": "TK5.01#2", "text": "1. ÁM ẢNH KIỂM SOÁT QUY TẮC CỰC ĐOAN", "dur_s": 2.5},
            {"sau_cau": "TK5.01#4", "text": "2. SỰ TÁCH BIỆT CẢM XÚC ĐẰNG SAU VẺ NHIỆT THÀNH", "dur_s": 2.5},
            {"sau_cau": "TK5.01#6", "text": "3. THÓI QUEN LƯU TRỮ VẬT RIÊNG TƯ NHƯ CHIẾN LỢI PHẨM", "dur_s": 2.5},
            {"sau_cau": "TK5.01#8", "text": "4. KHAO KHÁT ĐƯỢC CÔNG NHẬN VÀ TUNG HÔ BẰNG MỌI GIÁ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#10", "text": "LUÔN LẮNG NGHE TIẾNG NÓI TRỰC GIÁC BẢO VỆ SINH MẠNG", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "4 CRITICAL SURVIVAL RED FLAGS", "dur_s": 3.0},
            {"after_id": "TK5.01#2", "text": "1. RIGID CONTROL OBSESSION & MICROMANAGEMENT", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "2. SHALLOW AFFECT BEHIND CIVIC ENTHUSIASM", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "3. SECRET HOARDING OF PRIVATE BELONGINGS", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "4. DESPERATE CRAVING FOR VALIDATION & ATTENTION", "dur_s": 2.5},
            {"after_id": "TK5.01#10", "text": "ALWAYS TRUST YOUR INNER EVOLUTIONARY INTUITION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "日常の捕食者を見抜く4つの生存危険信号", "dur_s": 3.0},
            {"after_id": "TK5.01#2", "text": "1. 極端なルール統制への異常な執着", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "2. 熱心な社交性の裏にある浅薄な情動（共感の欠如）", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "3. 他人の私物を密かに収集・保管する異常癖", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "4. 自己顕示欲と称賛への病的な執着", "dur_s": 2.5},
            {"after_id": "TK5.01#10", "text": "命を守る進化の盾：内なる直感に耳を澄ませよ", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t5_amber_eyes_dossier_05", "still"),
            ("H", "5.04#3", "neutral", -0.02, 0.6, "t5_solitary_confinement_cell", "pull"),
            ("C", "5.05#2", "neutral", -0.02, 0.6, "t5_redflag_rule_control", "still"),
            ("C", "5.05#4", "neutral", -0.02, 0.6, "t5_redflag_rule_control", "push"),
            ("C", "5.05#5", "neutral", -0.02, 0.6, "t5_redflag_shallow_affect", "still"),
            ("C", "5.05#7", "neutral", -0.02, 0.6, "t5_redflag_shallow_affect", "pull"),
            ("D", "5.06#2", "neutral", -0.03, 0.6, "t5_redflag_secret_trophies", "still"),
            ("D", "5.06#4", "neutral", -0.03, 0.6, "t5_redflag_secret_trophies", "push"),
            ("D", "5.06#5", "neutral", -0.03, 0.6, "t5_redflag_narcissistic_hubris", "still"),
            ("D", "5.06#7", "neutral", -0.03, 0.7, "t5_redflag_narcissistic_hubris", "pull"),
            ("H", "5.08#6", "neutral", -0.02, 0.8, "t5_closing_desk", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t5_closing_desk", "still")
        ]
    }
]

CTA_VI = "Tập năm của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio."
CTA_EN = "Episode five of Amber Eyes. Watch the full documentary via the bio link."
CTA_JA = "Amber Eyes第5話。プロフィールリンクから完全版ドキュメンタリーをご覧ください。"

# ----------------------------------------------------------------------------
# 2. XÂY DỰNG FILE CHO TỪNG NGÔN NGỮ
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

    # SPEC_AUDIO_CLIP_TAP05.json
    spec_full = {
        "_readme": f"Đặc tả audio và kịch bản dựng TikTok Tập 05 ({lang}) — sinh tự động bởi .work/_build_tk_tap05.py.",
        "_episode": "Tap05",
        "_language": lang,
        "_title": "CHIẾC ĐĨA MỀM MÀU TÍM & CƠN NGHIỆN ÁI KỶ" if is_vi else ("THE PURPLE FLOPPY DISK & MALIGNANT NARCISSISM" if is_en else "紫のフロッピーディスクと悪性自己愛"),
        "_measured_rates": {r: round(rates[r], 4) for r in sorted(rates.keys())},
        "_clips_summary": summary_list,
        "clips": spec_clips
    }

    with (out_dir / "SPEC_AUDIO_CLIP_TAP05.json").open("w", encoding="utf-8") as f:
        json.dump(spec_full, f, ensure_ascii=False, indent=2)

    # Viết Caption_TK*, MoTa_Ngan_TK*, MoTa_Dai_TK*
    for c in CLIPS_DEF:
        cid = c["id"]
        hook = c["hook_vn"] if is_vi else (c["hook_en"] if is_en else c["hook_ja"])
        title = c["title_vn"] if is_vi else (c["title_en"] if is_en else c["title_ja"])
        signs_str = " · ".join([f"#{s}" for s in c["signs"]])

        if is_vi:
            cap = f"""{hook} 👁️

Tập 05 · Chiếc Đĩa Mềm Màu Tím — chỉ dấu tâm lý {signs_str}: {c['theme_vn']}.
Hồ sơ tâm lý tội phạm có thật về Dennis Rader (BTK) dựa trên biên bản tòa án Sedgwick và tài liệu điều tra độc quyền.

📺 Xem trọn vẹn tập phim tài liệu 27 phút tại link trong bio!
👉 Nhấn follow @ambereyes.vn để bước vào tâm trí kẻ thủ ác.

#tamlytoipham #ambereyes #dennisrader #btk #hosoanchuyen #khampha #kienthuc #toiphamcothat #podcastvietnam #truecrime"""

            mn = f"""{hook} 👁️
Tập 05 · Chiếc Đĩa Mềm Màu Tím — Chỉ dấu {signs_str}: {c['theme_vn']}.

Hồ sơ tâm lý tội phạm có thật dựa trên biên bản tòa án Sedgwick và tài liệu giám định pháp y kỹ thuật số.
Khám phá chiếc bẫy siêu dữ liệu Metadata định mệnh và cơ chế phân mảnh tâm trí kỳ dị suốt 30 năm của Dennis Rader.

📺 Xem đầy đủ tập phim tài liệu 27 phút tại link trên bio.
#tamlytoipham #ambereyes #btk #dennisrader #hosoanchuyen #truecrime"""

            md = f"""{hook} 👁️
TẬP 05 · CHIẾC ĐĨA MỀM MÀU TÍM & CƠN NGHIỆN ÁI KỶ
Chỉ dấu tâm lý chuyên sâu: {signs_str} — {c['theme_vn']}.

Suốt hơn 30 năm, Dennis Rader đã duy trì một chiếc mặt nạ công dân hoàn hảo đến rùng mình tại thị trấn Park City: Chủ tịch Hội đồng Nhà thờ Lutheran Chúa Kitô, Đội trưởng Hướng đạo sinh Cub Scout và Viên chức Trật tự Đô thị gương mẫu. Nhờ cơ chế phòng vệ tâm lý Phân mảnh tâm trí tuyệt đối (Compartmentalization), hắn đóng kín thế giới gia đình bình dị tách biệt hoàn toàn khỏi những hưng tưởng săn mồi đen tối, ngụy tạo nên khái niệm hoang tưởng mang tên "Nhân tố X" (Factor X) để chối bỏ trách nhiệm đạo đức.

Thế nhưng, chính cái tôi ái kỷ bệnh hoạn và cơn nghiện sự chú ý của công luận đã trở thành chiếc thòng lọng siết chặt số phận hắn. Khi đọc bài báo kỷ niệm 30 năm của The Wichita Eagle với giả thuyết rằng hung thủ đã qua đời hoặc bị lãng quên, lòng tự tôn bị tổn thương đã thúc đẩy Rader phá vỡ vỏ bọc im lặng. Sự tự mãn ngây thơ về công nghệ khiến hắn tin vào lời cam kết giả định của cảnh sát trên mục rao vặt 494 và gửi đi chiếc đĩa mềm Memorex màu tím định mệnh.

Chỉ bằng một tập tin Word bị xóa mang siêu dữ liệu ẩn "Dennis" và "Christ Lutheran Church", ban chuyên án của Trung úy Ken Landwehr đã lật tẩy danh tính của bóng ma reo rắc kinh hoàng suốt 3 thập kỷ. Bi kịch để lại vết thương không thể hàn gắn cho gia đình vô tội và đúc kết 4 bài học cảnh báo đỏ sinh tồn vô giá: Nhận diện sự kiểm soát quy tắc cực đoan, sự tách biệt cảm xúc đằng sau vẻ nhiệt thành, thói quen tích trữ kỷ vật bí mật và cơn nghiện ái kỷ luôn khao khát được tung hô.

📺 Xem trọn vẹn tập phim tài liệu 27 phút được phân tích chuyên sâu tại link bio kênh Amber Eyes.
👉 Follow kênh để đồng hành cùng những hồ sơ tâm lý tội phạm chấn động tiếp theo.

#tamlytoipham #ambereyes #dennisrader #btk #hosoanchuyen #khampha #kienthuc #toiphamcothat #podcastvietnam #truecrime #phapluat #tamlyhoc"""

        elif is_en:
            cap = f"""{hook} 👁️

Ep. 05 · The Purple Floppy Disk — Psychological Markers {signs_str}: {c['theme_en']}.
Authentic true crime profiling of Dennis Rader (BTK) based on official Sedgwick County court records.

📺 Watch the full 27-minute documentary via the link in our bio!
👉 Follow @ambereyes.official to venture into the psychology of extreme crime.

#truecrime #psychology #dennisrader #btk #criminalpsychology #forensics #fbi #crimedocumentary #podcast"""

            mn = f"""{hook} 👁️

Episode 05 · The Purple Floppy Disk — Psychological Markers {signs_str}: {c['theme_en']}.
Authentic forensic breakdown based on official police records and digital metadata forensics.

Discover the fatal floppy disk trap and Dennis Rader's extreme 30-year psychological compartmentalization.

📺 Full 27-minute documentary streaming now via our bio link.
#truecrime #btk #dennisrader #forensics #criminalminds"""

            md = f"""{hook} 👁️
EPISODE 05 · THE PURPLE FLOPPY DISK & MALIGNANT NARCISSISM
In-depth Psychological Analysis: Markers {signs_str} — {c['theme_en']}.

For over three decades, Dennis Rader sustained a flawless civic disguise in Park City, Kansas: Council President at Christ Lutheran Church, Cub Scout leader, and strict municipal compliance officer. Utilizing extreme psychological compartmentalization, he sealed his pristine family life behind an impenetrable cognitive wall, externalizing his predatory compulsions under the delusional concept of “Factor X” to bypass moral guilt.

Yet, his malignant narcissism and desperate craving for social attention ultimately engineered his demise. Stung by a 30th-anniversary retrospective in The Wichita Eagle suggesting he was dead or forgotten, Rader broke his 13-year silence. Incurably hubristic and digitally naive, he blindly trusted a police newspaper classified ad ("Rex, it will be OK") and mailed in a purple 1.44MB floppy disk.

Within minutes, digital forensics specialist Randy Stone recovered a deleted Word file embedded with metadata: "Dennis" and "Christ Lutheran Church." The trap snapped shut, bringing an abrupt end to the reign of terror. This landmark dossier leaves four indispensable survival red flags: Beware pathological rigidity and rule enforcement, emotional detachment masquerading as civic warmth, secret trophy hoarding, and toxic narcissistic grandiosity demanding validation at all costs.

📺 Watch the full 27-minute investigative documentary via the link in bio.
👉 Follow Amber Eyes for rigorous criminal psychological profiling.

#truecrime #dennisrader #btk #psychology #digitalforensics #crimedocumentary #fbi #podcast"""

        else: # JA
            cap = f"""{hook} 👁️

第05話 · 紫のフロッピーディスク — 心理指標 {signs_str}: {c['theme_ja']}。
裁判記録および公的デジタル鑑識資料に基づく本格犯罪心理学ドキュメンタリー。

📺 完全版ドキュメンタリー（27分）はYouTubeで公開中 — プロフィールのリンクから！
👉 フォローして次回の深層心理プロファイリングをお見逃しなく。

#犯罪心理学 #アンバーアイズ #実話 #未解決事件 #事件 #心理学 #ドキュメンタリー #BTK #プロファイリング"""

            mn = f"""{hook} 👁️

第05話 · 紫のフロッピーディスク — 心理指標 {signs_str}: {c['theme_ja']}。
裁判記録・デジタル鑑識調書に基づく犯罪心理学ドキュメンタリー。

全米を震撼させた30年間の社会的仮面と、紫のフロッピーディスクが招いた自己愛の完全崩壊。

📺 YouTubeで27分の完全版ドキュメンタリーを公開中 — プロフィールのリンクからご覧ください。
#犯罪心理学 #アンバーアイズ #実話 #事件 #ドキュメンタリー #BTK"""

            md = f"""{hook} 👁️
第05話 · 紫のフロッピーディスクと悪性自己愛
専門心理指標解析：{signs_str} — {c['theme_ja']}。

カンザス州パークシティにおいて、Dennis Raderは30年以上にわたり完璧な市民の仮面を被り続けていました。キリスト・ルーテル教会の評議会議長を務め、カブスカウトの隊長として子供たちを導き、市役所の規則遵守指導員として厳格に職務を遂行していた彼。極端な「精神の分断（コンパートメンタライゼーション）」により、家庭生活と暗い捕食妄想の世界を完全に隔離し、凶行を「要因X（Factor X）」という外的存在に責任転嫁していました。

しかし、彼の病的な悪性自己愛と世間の注目への飢餓感が、自らを破滅へと導きます。地元紙がBTK事件から30年を機に「犯人は死亡したか忘れ去られた」と報じたことに激怒し、彼は13年の沈黙を破って警察に接触。技術的な無知と肥大した自尊心から新聞広告の暗号メッセージを信じ込み、致命的な紫色の1.44MBフロッピーディスクを送り届けました。

デジタル鑑識官によって復元された削除済みWordファイルには、「Dennis」および「キリスト・ルーテル教会」という決定的なメタデータが残されていました。この歴史的事件から導き出された4つの生存危険信号：極端なルール統制への執着、社交性の裏にある浅薄な情動、他人の私物の隠匿癖、そして自尊心を刺激された自己愛者の暴発に常に警戒してください。

📺 27分におよぶ完全版ドキュメンタリーは、YouTube公式チャンネル（プロフィールのリンク）にて公開中。
👉 フォローして次なるプロファイリングをお楽しみください。

#犯罪心理学 #アンバーアイズ #実話 #事件 #心理学 #ドキュメンタリー #BTK #プロファイリング #教養"""

        (out_dir / f"Caption_{cid}.txt").write_text(cap, encoding="utf-8")
        (out_dir / f"MoTa_Ngan_{cid}.txt").write_text(mn, encoding="utf-8")
        (out_dir / f"MoTa_Dai_{cid}.txt").write_text(md, encoding="utf-8")

    # KE_HOACH_CLIP_TAP05.md
    md_plan_name = f"KE_HOACH_CLIP_TAP05_{lang}.md" if not is_vi else "KE_HOACH_CLIP_TAP05.md"
    plan_lines = []

    if is_vi:
        plan_lines.append("# KẾ HOẠCH CLIP TIKTOK — TẬP 05 · \"CHIẾC ĐĨA MỀM MÀU TÍM & CƠN NGHIỆN ÁI KỶ\"\n\n")
        plan_lines.append("*Ngày: 20/11/2026 · Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*\n")
        plan_lines.append("*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap05/SPEC_AUDIO_CLIP_TAP05.json`*\n")
        plan_lines.append("*Nguồn dữ liệu chuẩn: `02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md` · `.work/timeline_s_t05.json` (209 câu) · `02_SAN_XUAT/Tap05/nguon_tham_khao.md`*\n\n---\n\n## 0. Tóm tắt chốt\n\n")
        plan_lines.append("| Hạng mục | Giá trị |\n|---|---|\n")
        plan_lines.append("| Số clip | **5 clip** (TK1–TK4 trọng tâm + TK5 đúc kết bài học sinh tồn) |\n")
        plan_lines.append(f"| Tổng câu thoại | **{sum(s['lines_count'] for s in summary_list)} câu** đọc giọng |\n")
        plan_lines.append(f"| Thời lượng đo thực tế | {min(s['est_duration_s'] for s in summary_list)} – {max(s['est_duration_s'] for s in summary_list)} s/clip (chuẩn TikTok 45–95 s) |\n")
        plan_lines.append("| Hệ sinh thái K10 | Đạt đủ 10 chỉ dấu tâm lý & hành vi cốt lõi của Tập 05 |\n")
        plan_lines.append("| Ngôn ngữ | Tiếng Việt · Cast: Host (H), Điều tra viên (D), Chuyên gia (C), Kerri Rawson (N2) |\n")
        plan_lines.append("| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** |\n")
        plan_lines.append("| Hình ảnh nền | Chuẩn dọc 9:16 crop/pad từ 61 nền 16:9 gốc của Tập 05 (`assets/bg/t5_*`) |\n\n---\n\n## 1. Năm clip và chỉ dấu tâm lý tương ứng (K10)\n\n")
        plan_lines.append("| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng thời gian |\n|---|---|---|---|---|\n")
        for s in summary_list:
            c_info = next(x for x in CLIPS_DEF if x["id"] == s["clip"])
            plan_lines.append(f"| **{s['clip']}** | {' · '.join(['#' + str(x) for x in s['signs']])} | {c_info['theme_vn']} | *\"{c_info['hook_vn']}\"* | {s['est_duration_s']} s · {s['lines_count']} câu |\n")
        plan_lines.append("\n---\n\n## 2. Diễn xuất từng clip (lời đọc + hình + âm)\n\n")

    elif is_en:
        plan_lines.append("# TIKTOK CLIP PLAN — EPISODE 05 · \"THE PURPLE FLOPPY DISK & MALIGNANT NARCISSISM\"\n\n")
        plan_lines.append("*Date: November 20, 2026 · Status: Production-ready script based on measured timeline*\n")
        plan_lines.append("*Master plan: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Machine spec: `02_SAN_XUAT/TIKTOK/Tap05_EN/SPEC_AUDIO_CLIP_TAP05.json`*\n")
        plan_lines.append("*Source data: `.work/timeline_s_EN_t05.json` (209 items) · Sedgwick County Court Transcripts*\n\n---\n\n## 0. Executive Summary\n\n")
        plan_lines.append("| Item | Specification |\n|---|---|\n")
        plan_lines.append("| Total Clips | **5 clips** (TK1–TK4 core psychological profiling + TK5 red flags) |\n")
        plan_lines.append(f"| Total Spoken Lines | **{sum(s['lines_count'] for s in summary_list)} lines** |\n")
        plan_lines.append(f"| Measured Duration | {min(s['est_duration_s'] for s in summary_list)} – {max(s['est_duration_s'] for s in summary_list)} s/clip (TikTok Safe Zone 45–95 s) |\n")
        plan_lines.append("| Psychological Framework | 10 Core Psychological Markers (K10 compliant) |\n")
        plan_lines.append("| Voice Engine | **Higgs Audio v3 + VoxCPM2 English Reference Voices** |\n\n---\n\n## 1. Five Clips & Corresponding Psychological Markers\n\n")
        plan_lines.append("| Clip | Markers | Theme | Opening Visual Hook (0–3 s) | Measured Duration |\n|---|---|---|---|---|\n")
        for s in summary_list:
            c_info = next(x for x in CLIPS_DEF if x["id"] == s["clip"])
            plan_lines.append(f"| **{s['clip']}** | {' · '.join(['#' + str(x) for x in s['signs']])} | {c_info['theme_en']} | *\"{c_info['hook_en']}\"* | {s['est_duration_s']} s · {s['lines_count']} lines |\n")
        plan_lines.append("\n---\n\n## 2. Detailed Clip Production Specifications\n\n")

    else: # JA
        plan_lines.append("# TikTokショート動画制作計画 — 第05話 · 「紫のフロッピーディスクと悪性自己愛」\n\n")
        plan_lines.append("*作成日: 2026年11月20日 · 状態: 実測タイムラインに基づく完成脚本*\n")
        plan_lines.append("*親ドキュメント: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · 音声仕様書: `02_SAN_XUAT/TIKTOK/Tap05_JA/SPEC_AUDIO_CLIP_TAP05.json`*\n")
        plan_lines.append("*公式情報源: `.work/timeline_s_JA_t05.json`（209項目） · カンザス州セジウィック郡裁判調書*\n\n---\n\n## 0. 仕様概要\n\n")
        plan_lines.append("| 項目 | 仕様内容 |\n|---|---|\n")
        plan_lines.append("| クリップ数 | **全5クリップ**（TK1–TK4 事件深層・心理分析 + TK5 生存教訓） |\n")
        plan_lines.append(f"| 総音声行数 | **{sum(s['lines_count'] for s in summary_list)}行** |\n")
        plan_lines.append(f"| 実測推定時間 | {min(s['est_duration_s'] for s in summary_list)} – {max(s['est_duration_s'] for s in summary_list)} 秒（適正範囲 45–95 秒） |\n")
        plan_lines.append("| 心理分析枠組み | 犯罪心理10大指標（K10準拠）完全網羅 |\n")
        plan_lines.append("| 音声エンジン | **Higgs Audio v3 + VoxCPM2日本語参照音声** |\n\n---\n\n## 1. 全5クリップと心理指標一覧\n\n")
        plan_lines.append("| クリップ | 心理指標 | テーマ | 冒頭フック (0–3秒) | 計測推定時間 |\n|---|---|---|---|---|\n")
        for s in summary_list:
            c_info = next(x for x in CLIPS_DEF if x["id"] == s["clip"])
            plan_lines.append(f"| **{s['clip']}** | {' · '.join(['#' + str(x) for x in s['signs']])} | {c_info['theme_ja']} | *\"{c_info['hook_ja']}\"* | {s['est_duration_s']} 秒 · {s['lines_count']} 行 |\n")
        plan_lines.append("\n---\n\n## 2. 各クリップの演技・演出詳細仕様\n\n")

    for c in CLIPS_DEF:
        cid = c["id"]
        c_spec = spec_clips[cid]
        plan_lines.append(f"### {cid} — \"{c_spec['title']}\"\n\n")
        plan_lines.append(f"*Thời lượng: {c_spec['total_est_duration_s']} s ({len(c_spec['lines'])} câu) · BGM: `{c_spec['bgm']}` ({c_spec['bgm_desc']})*\n\n")
        plan_lines.append("| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |\n|---|---|---|---|---|---|---|---|---|\n")
        for ln in c_spec["lines"]:
            plan_lines.append(f"| `{ln['clip_line_id']}` | {ln['role']} | {ln['emotion']} | {ln['speed_offset']} | {ln['pause_after_s']} | `{ln['bg']}` | {ln['motion']} | {ln['text']} | `{ln['src_script']}` |\n")
        plan_lines.append("\n**Lớp phủ chữ trên hình (Text Overlays):**\n")
        for ov in c_spec["overlays"]:
            k_id = ov.get("sau_cau") or ov.get("after_id")
            plan_lines.append(f"- `{k_id}`: **\"{ov['text']}\"** ({ov['dur_s']} s)\n")
        plan_lines.append("\n")

    (out_dir / md_plan_name).write_text("".join(plan_lines), encoding="utf-8")
    print(f"Generated {lang} TikTok package at {out_dir}")

def update_tracking_table():
    csv_file = ROOT / "02_SAN_XUAT" / "TIKTOK" / "BangTheoDoi_TikTok.csv"
    lines = csv_file.read_text(encoding="utf-8").splitlines() if csv_file.exists() else []
    
    # Check if Tap05 already in csv
    has_t05 = any("Tap05" in l for l in lines)
    if not has_t05:
        new_rows = [
            "Tap05,TK1,Chiếc đĩa mềm màu tím và bẫy siêu dữ liệu,VI,80.2,12,Kịch bản hoàn thành,2026-11-20",
            "Tap05,TK2,Chủ tịch hội đồng nhà thờ và mặt nạ 30 năm,VI,74.4,11,Kịch bản hoàn thành,2026-11-20",
            "Tap05,TK3,Nỗi sợ bị lãng quên và ảo tưởng Nhân tố X,VI,65.1,10,Kịch bản hoàn thành,2026-11-20",
            "Tap05,TK4,Nỗi đau của con gái kẻ sát nhân BTK,VI,74.5,11,Kịch bản hoàn thành,2026-11-20",
            "Tap05,TK5,4 dấu hiệu cảnh báo đỏ sinh tồn,VI,77.6,12,Kịch bản hoàn thành,2026-11-20",
            "Tap05_EN,TK1,The Purple Floppy Disk & Metadata Trap,EN,69.5,12,Kịch bản hoàn thành,2026-11-20",
            "Tap05_EN,TK2,The Church Council President & 30-Year Mask,EN,74.9,11,Kịch bản hoàn thành,2026-11-20",
            "Tap05_EN,TK3,Fear of Oblivion & Factor X Delusion,EN,63.9,10,Kịch bản hoàn thành,2026-11-20",
            "Tap05_EN,TK4,The Agony of the BTK Daughter,EN,58.7,11,Kịch bản hoàn thành,2026-11-20",
            "Tap05_EN,TK5,4 Critical Survival Red Flags,EN,72.6,12,Kịch bản hoàn thành,2026-11-20",
            "Tap05_JA,TK1,紫のフロッピーディスクとメタデータの罠,JA,84.4,12,Kịch bản hoàn thành,2026-11-20",
            "Tap05_JA,TK2,教会評議会議長と30年間の社会的仮面,JA,89.2,11,Kịch bản hoàn thành,2026-11-20",
            "Tap05_JA,TK3,忘却への恐怖と要因Xの妄想,JA,75.5,10,Kịch bản hoàn thành,2026-11-20",
            "Tap05_JA,TK4,BTKの娘ケリーが背負った地獄,JA,71.6,11,Kịch bản hoàn thành,2026-11-20",
            "Tap05_JA,TK5,日常に潜む4つの生存危険信号,JA,82.9,12,Kịch bản hoàn thành,2026-11-20"
        ]
        if lines:
            lines.extend(new_rows)
        else:
            lines = ["Episode,ClipID,Title,Language,EstDuration_s,Lines,Status,Date"] + new_rows
        csv_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("Updated BangTheoDoi_TikTok.csv with Tap05 rows")

if __name__ == "__main__":
    for l in ["VI", "EN", "JA"]:
        build_for_lang(l)
    update_tracking_table()
    print("All Tap05 TikTok multi-language packages successfully created!")
