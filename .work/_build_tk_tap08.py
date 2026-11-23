# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 08 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap08/KE_HOACH_CLIP_TAP08.md
  02_SAN_XUAT/TIKTOK/Tap08/SPEC_AUDIO_CLIP_TAP08.json
  02_SAN_XUAT/TIKTOK/Tap08/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap08/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap08/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap08_EN/KE_HOACH_CLIP_TAP08_EN.md
  02_SAN_XUAT/TIKTOK/Tap08_EN/SPEC_AUDIO_CLIP_TAP08.json
  02_SAN_XUAT/TIKTOK/Tap08_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap08_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap08_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap08_JA/KE_HOACH_CLIP_TAP08_JA.md
  02_SAN_XUAT/TIKTOK/Tap08_JA/SPEC_AUDIO_CLIP_TAP08.json
  02_SAN_XUAT/TIKTOK/Tap08_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap08_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap08_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 08:
- timeline_s_t08.json (VI)
- timeline_s_EN_t08.json (EN)
- timeline_s_JA_t08.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap08"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap08_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap08_JA"

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
# 0. TỈ LỆ ĐỌC THẬT (Đo từ master Tập 08)
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

RATE_VI = get_rates("timeline_s_t08.json", is_ja=False)
RATE_EN = get_rates("timeline_s_EN_t08.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t08.json", is_ja=True)

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

MAP_VI = load_script_map("script_tap08.json")
MAP_EN = load_script_map("script_tap08_EN.json")
MAP_JA = load_script_map("script_tap08_JA.json")

# ----------------------------------------------------------------------------
# 2. KHAI BÁO 5 CLIP TẬP 08 (BẢN VI, EN, JA)
# ----------------------------------------------------------------------------
CLIPS_CONFIG = [
    {
        "id": "TK1",
        "title_vn": "Nghịch lý trí thức tinh hoa và sự trống rỗng hiện sinh",
        "title_en": "The Elite Intellectual Paradox & The Existential Vacuum",
        "title_ja": "エリート知識人の逆説と実存的真空の罠",
        "signs": [1, 9],
        "theme_vn": "Hiệu ứng hào quang trí tuệ & Điểm mù xã hội + Sự trống rỗng hiện sinh",
        "theme_en": "Intellectual Halo Effect & Existential Vacuum in Elite Youth",
        "theme_ja": "知性のハロー効果とエリート青年の実存的真空",
        "hook_vn": "Thủ khoa, bác sĩ trưởng khoa, nhà vật lý hàng đầu. Tại sao quỳ gối trước kẻ từng bán thuốc giả?",
        "hook_en": "Valedictorians, chief cardiologists, cosmic physicists. Why did they kneel before a half-blind charlatan?",
        "hook_ja": "名門大首席、循環器内科部長、宇宙物理学者。なぜ彼らはペテン師の足元に平伏したのか？",
        "bgm": "bgm_piano_minimal.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_piano_minimal.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_piano_minimal.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_piano_minimal.mp3",
        "sfx_vn": ["amb_lab_equipment.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_lab_equipment.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_lab_equipment.wav（環境音）", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "NGHỊCH LÝ CỦA CÁC THIÊN TÀI KHOA HỌC", "dur_s": 3.0},
            {"sau_cau": "TK1.01#3", "text": "ĐỘI NGŨ CHẤT XÁM CHƯA TỪNG CÓ TIỀN LỆ", "dur_s": 2.5},
            {"sau_cau": "TK1.01#4", "text": "BÁC SĨ TRƯỞNG KHOA TIM MẠCH ĐẠI HỌC KEIO", "dur_s": 2.5},
            {"sau_cau": "TK1.01#5", "text": "KHỦNG HOẢNG TÂM LÝ: SỰ TRỐNG RỖNG HIỆN SINH", "dur_s": 2.5},
            {"sau_cau": "TK1.01#8", "text": "ĐIỂM YẾU CHÍ MẠNG: CÁI TÔI TRÍ TUỆ QUÁ LỚN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "THE SCIENTIFIC GENIUS PARADOX", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "UNPRECEDENTED CONCENTRATION OF ACADEMIC ELITES", "dur_s": 2.5},
            {"after_id": "TK1.01#4", "text": "CHIEF CARDIOLOGIST FROM KEIO UNIVERSITY", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "THE PSYCHOLOGICAL CRISIS: EXISTENTIAL VACUUM", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "LETHAL VULNERABILITY: INTELLECTUAL HUBRIS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "科学の天才たちが陥った致命的逆説", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "前代未聞の超エリート頭脳集団の集結", "dur_s": 2.5},
            {"after_id": "TK1.01#4", "text": "慶應義塾大卒・元国立病院循環器内科部長", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "社会心理学的危機：実存的真空（生きる意味の喪失）", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "致命的な心理的盲点：過剰な知的プライド", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t8_todai_red_gate_shadow", "pull"),
            ("H", "3.02#8", "neutral", -0.02, 0.6, "t8_asahara_shadow_profile", "push"),
            ("H", "3.02#9", "neutral", -0.02, 0.6, "t8_todai_red_gate_shadow", "still"),
            ("D", "3.03#1", "neutral", -0.02, 0.6, "t8_dossier_elite_scientists", "pan"),
            ("D", "3.03#6", "neutral", -0.02, 0.6, "t8_cardiac_surgery_theatre", "still"),
            ("C", "3.05#1", "neutral", -0.02, 0.6, "t8_tokyo_stock_crash_1990", "pull"),
            ("C", "3.05#4", "neutral", -0.02, 0.6, "t8_moral_rationalization_books", "still"),
            ("C", "3.05#5", "neutral", -0.02, 0.6, "t8_fragile_boundary_mirror", "push"),
            ("H", "3.06#1", "neutral", -0.02, 0.6, "t8_intellectual_hubris_chess", "pan"),
            ("H", "cta", "neutral", -0.02, 0.0, "t8_tokyo_dawn_restored_peace", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Kỹ thuật làm suy kiệt thể xác và chiếc mũ điện cực PSI",
        "title_en": "Systematic Physical Deprivation & The PSI Electrode Headgear",
        "title_ja": "肉体の極限消耗と洗脳電極ヘッドギア「PSI」の戦慄",
        "signs": [6, 8],
        "theme_vn": "Kỹ thuật triệt tiêu tư duy phản biện & Quỹ đạo kiểm soát cưỡng bách",
        "theme_en": "Dismantling Critical Faculties & Escalation of Coercive Control",
        "theme_ja": "批判的思考の破壊技術と強迫的支配の暴走",
        "hook_vn": "Chỉ ngủ hai tiếng, thiền hai mươi tiếng trong bóng tối, và chiếc mũ điện cực hàng nghìn đô la.",
        "hook_en": "Two hours of sleep, twenty hours of dark meditation, and a multi-thousand-dollar electrode skullcap.",
        "hook_ja": "睡眠は2時間、暗闇で20時間の瞑想、そして数千ドルの電極ヘッドギア。",
        "bgm": "bgm_ambient_deep.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_ambient_deep.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_ambient_deep.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_ambient_deep.mp3",
        "sfx_vn": ["amb_dark_drone.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_dark_drone.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_dark_drone.wav（環境音）", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "CÔNG NGHỆ TẨY NÃO KHÉP KÍN TRONG BÓNG TỐI", "dur_s": 3.0},
            {"sau_cau": "TK2.01#3", "text": "SUY KIỆT THỂ XÁC TRIỆT TIÊU Ý CHÍ TỰ DO", "dur_s": 2.5},
            {"sau_cau": "TK2.01#4", "text": "VỎ NÃO TRƯỚC TRÁN TỰ ĐỘNG NGỪNG PHẢN BIỆN", "dur_s": 2.5},
            {"sau_cau": "TK2.01#6", "text": "THIẾT BỊ ĐIỆN CỰC PSI ĐỒNG BỘ SÓNG NÃO", "dur_s": 2.5},
            {"sau_cau": "TK2.01#8", "text": "THAO TÚNG HÓA CHẤT XÓA BỎ HOÀN TOÀN SỰ HOÀI NGHI", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "CLANDESTINE MIND CONTROL IN TOTAL ISOLATION", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "CHRONIC EXHAUSTION CRUSHING INDEPENDENT WILL", "dur_s": 2.5},
            {"after_id": "TK2.01#4", "text": "PREFRONTAL CORTEX FUNCTIONAL COLLAPSE", "dur_s": 2.5},
            {"after_id": "TK2.01#6", "text": "PSI BRAINWAVE SYNCHRONIZATION HEADGEAR", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "CHEMICAL MANIPULATION ERASING SKEPTICISM", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "完全隔離施設で行われた暗黒のマインドコントロール", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "自由意志を剥奪する計画的肉体酷使", "dur_s": 2.5},
            {"after_id": "TK2.01#4", "text": "極度の疲弊による前頭前野の機能麻痺", "dur_s": 2.5},
            {"after_id": "TK2.01#6", "text": "脳波同調ヘッドギア「PSI」の奇怪な実態", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "薬物投与と神経衰弱による批判力の完全消滅", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t8_concrete_cell_isolation", "pull"),
            ("H", "4.02#1", "neutral", -0.02, 0.6, "t8_concrete_cell_isolation", "still"),
            ("H", "4.02#3", "neutral", -0.02, 0.6, "t8_frontal_lobe_brain_scan", "push"),
            ("H", "4.02#4", "neutral", -0.02, 0.6, "t8_hidden_ceiling_hideout", "pan"),
            ("H", "4.02#6", "neutral", -0.02, 0.6, "t8_frontal_lobe_brain_scan", "still"),
            ("D", "4.03#1", "neutral", -0.02, 0.6, "t8_psi_headgear_electrodes", "pull"),
            ("D", "4.03#2", "neutral", -0.03, 0.6, "t8_psi_headgear_electrodes", "push"),
            ("D", "4.03#5", "neutral", -0.02, 0.6, "t8_hallucinogen_ritual_hall", "pan"),
            ("D", "4.03#7", "neutral", -0.02, 0.6, "t8_frontal_lobe_brain_scan", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t8_tokyo_dawn_restored_peace", "still")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Ma thuật tẩy não và bóp méo khái niệm Poa",
        "title_en": "Cult Brainwashing & The Perversion of Poa Doctrine",
        "title_ja": "洗脳の魔術と教義「ポア」の悪魔的すり替え",
        "signs": [5, 7],
        "theme_vn": "Hệ thống tự bào chữa & Cơ chế trung hòa đạo đức (Chữ ký Signature)",
        "theme_en": "Moral Disengagement & Cognitive Neutralization (Cult Signature)",
        "theme_ja": "自己正当化システムと道徳的離脱（カルトの署名）",
        "hook_vn": "Đoạt mạng người khác nhưng tin rằng mình đang làm việc thiện cứu rỗi linh hồn họ.",
        "hook_en": "Taking human lives while truly believing it was an act of holy mercy to save their souls.",
        "hook_ja": "命を奪いながら、自らを魂の救済者と信じ込む「大慈悲のポア」。",
        "bgm": "bgm_sub_drone.mp3",
        "bgm_desc_vn": "Hồi 3 — bed tập: bgm_sub_drone.mp3",
        "bgm_desc_en": "Act 3 — episode bed: bgm_sub_drone.mp3",
        "bgm_desc_ja": "第3幕 — 本編BGM: bgm_sub_drone.mp3",
        "sfx_vn": ["amb_dark_drone.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_dark_drone.wav (bed)", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_dark_drone.wav（環境音）", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "VŨ KHÍ HỦY DIỆT LƯƠNG TÂM: KHÁI NIỆM POA", "dur_s": 3.0},
            {"sau_cau": "TK3.01#3", "text": "ĐÁNH TRÁO GIẾT NGƯỜI THÀNH NGHĨA CỬ CAO CẢ", "dur_s": 2.5},
            {"sau_cau": "TK3.01#5", "text": "NGỤY BIỆN TẬN THẾ ĐỂ KÍCH ĐỘNG TỘI ÁC", "dur_s": 2.5},
            {"sau_cau": "TK3.01#6", "text": "ĐỈNH CAO CỦA KỸ THUẬT TRUNG HÒA ĐẠO ĐỨC", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "NGOẠI HÓA TRÁCH NHIỆM CHO ĐẤNG TỐI CAO", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "CONSCIENCE-CRUSHING WEAPON: PERVERTED POA", "dur_s": 3.0},
            {"after_id": "TK3.01#3", "text": "REPACKAGING HOMICIDE AS SUBLIME COMPASSION", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "APOCALYPTIC PROPHECIES FUELING EXTREMISM", "dur_s": 2.5},
            {"after_id": "TK3.01#6", "text": "THE ZENITH OF MORAL DISENGAGEMENT", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "EXTERNALIZING AGENCY TO THE SUPREME MASTER", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "良心を粉砕した悪魔の心理兵器「ポア」", "dur_s": 3.0},
            {"after_id": "TK3.01#3", "text": "冷酷な殺戮を崇高な救済へとすり替える詭弁", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "破滅的終末論を用いた悪業の正当化", "dur_s": 2.5},
            {"after_id": "TK3.01#6", "text": "道徳的離脱と認知的正当化の極致", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "責任の外部化：教祖の道具という名の自己免責", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t8_poa_twisted_doctrine", "pull"),
            ("H", "4.04#1", "neutral", -0.02, 0.6, "t8_poa_twisted_doctrine", "still"),
            ("H", "4.04#2", "neutral", -0.02, 0.6, "t8_buddhist_mandala_distortion", "pan"),
            ("H", "4.04#3", "neutral", -0.02, 0.6, "t8_broken_hippocratic_oath", "push"),
            ("C", "4.05#1", "neutral", -0.02, 0.6, "t8_apocalypse_prophecy_scroll", "pan"),
            ("C", "4.05#2", "neutral", -0.02, 0.6, "t8_devotion_altar_kneeling", "still"),
            ("C", "4.05#3", "neutral", -0.02, 0.6, "t8_weapons_of_mass_destruction", "pull"),
            ("C", "4.05#5", "neutral", -0.02, 0.6, "t8_moral_rationalization_books", "still"),
            ("C", "4.05#7", "neutral", -0.02, 0.6, "t8_devotion_altar_kneeling", "push"),
            ("C", "4.05#8", "neutral", -0.02, 0.6, "t8_moral_rationalization_books", "pan"),
            ("H", "cta", "neutral", -0.02, 0.0, "t8_tokyo_dawn_restored_peace", "still")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Nước mắt của bác sĩ tim mạch và sự sụp đổ của đấng cứu thế",
        "title_en": "Tears of the Keio Cardiologist & The Collapse of the Messiah",
        "title_ja": "名医の涙と偽りの救世主の無様な失墜",
        "signs": [3, 4],
        "theme_vn": "Cơ chế chia ngăn nhận thức + Sự sụp đổ của cái tôi ái kỷ bệnh lý",
        "theme_en": "Cognitive Compartmentalization & Collapse of Pathological Narcissism",
        "theme_ja": "認知的区分化（区画化）と自己愛性偶像の完全崩壊",
        "hook_vn": "Bàn tay từng phẫu thuật cứu người dùng ô chọc thủng túi độc. Và kẻ tự xưng thần thánh run rẩy trong hốc trần.",
        "hook_en": "Hands trained to save lives punctured sarin bags. And the self-proclaimed messiah trembled in a ceiling crawl space.",
        "hook_ja": "命を救うはずの手がサリンを突き刺した。そして自称救世主は天井裏で震えていた。",
        "bgm": "bgm_violin_heart.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_violin_heart.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_violin_heart.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_violin_heart.mp3",
        "sfx_vn": ["amb_courtroom.wav (nền)", "fx_gavel_triple.wav", "fx_door_metal_slam.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_courtroom.wav (bed)", "fx_gavel_triple.wav", "fx_door_metal_slam.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_courtroom.wav（環境音）", "fx_gavel_triple.wav", "fx_door_metal_slam.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "BI KỊCH TÊ LIỆT LƯƠNG TÂM CỦA MỘT DANH Y", "dur_s": 3.0},
            {"sau_cau": "TK4.01#3", "text": "BUỔI SÁNG ĐỊNH MỆNH TRÊN TUYẾN TÀU CHIYODA", "dur_s": 2.5},
            {"sau_cau": "TK4.01#4", "text": "LỜI KHAI TRƯỚC VÀNH MÓNG NGỰA: KHÔNG XIN THA THỨ", "dur_s": 2.5},
            {"sau_cau": "TK4.01#6", "text": "SỰ PHẢN BỘI LỜI THỀ HIPPOCRATES THIÊNG LIÊNG", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "16/5/1995: ĐẤNG CỨU THẾ CO RÔ TRONG HỐC TRẦN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "THE MORAL EXTINCTION OF AN ACCLAIMED SURGEON", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "TRAGIC MORNING ABOARD THE CHIYODA LINE", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "COURTROOM TESTIMONY: ASKING NO FORGIVENESS", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "BETRAYAL OF THE SACRED HIPPOCRATIC OATH", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "MAY 16, 1995: THE FALSE SAVIOR COWERING IN DARKNESS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "名門心臓外科医を襲った良心の麻痺", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "1995年3月20日 · 千代田線の惨劇", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "法廷での痛哭：いかなる減刑も寛恕も求めない", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "生涯をかけた神聖なヒポクラテスの誓いの裏切り", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "1995年5月16日：第6サティアン天井裏での無様な逮捕", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t8_dr_hayashi_umbrella_subway", "pull"),
            ("H", "4.06#1", "neutral", -0.02, 0.6, "t8_dr_hayashi_umbrella_subway", "still"),
            ("H", "4.06#2", "neutral", -0.02, 0.6, "t8_cardiac_surgery_theatre", "push"),
            ("H", "4.06#3", "neutral", -0.02, 0.6, "t8_dr_hayashi_umbrella_subway", "pan"),
            ("N2", "4.08#1", "sad", -0.02, 0.6, "t8_grand_courtroom_proceedings", "still"),
            ("N2", "4.08#2", "sad", -0.02, 0.6, "t8_tokyo_court_witness_stand", "pull"),
            ("N2", "4.08#3", "sad", -0.02, 0.6, "t8_broken_hippocratic_oath", "push"),
            ("N2", "4.08#4", "sad", -0.02, 0.6, "t8_tokyo_court_witness_stand", "still"),
            ("H", "4.09#6", "neutral", -0.02, 0.6, "t8_hidden_ceiling_hideout", "pan"),
            ("H", "4.09#7", "neutral", -0.02, 0.6, "t8_hidden_ceiling_hideout", "pull"),
            ("H", "cta", "neutral", -0.02, 0.0, "t8_tokyo_dawn_restored_peace", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Bốn tín hiệu cảnh báo đỏ trước cạm bẫy thao túng giáo phái",
        "title_en": "Four Survival Red Flags to Defeat Cult Mind Manipulation",
        "title_ja": "カルトのマインドコントロールを見破る4つの生存警告サイン",
        "signs": [10, 2],
        "theme_vn": "Nạn nhân học & 4 cảnh báo đỏ sinh tồn chống thao túng tâm lý",
        "theme_en": "Victimology & Four Vital Survival Red Flags Against Deceptive Coercion",
        "theme_ja": "被害者学と悪質なマインドコントロールから身を守る4つの警告",
        "hook_vn": "Bốn tín hiệu cảnh báo đỏ sinh tồn để không bao giờ trở thành nạn nhân của thao túng tâm lý độc hại.",
        "hook_en": "Four vital survival red flags to never fall victim to malicious psychological manipulation.",
        "hook_ja": "破滅的マインドコントロールの犠牲にならないための、4つの生存警告サイン。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_office_night.wav (nền)", "fx_paper_folder.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_office_night.wav (bed)", "fx_paper_folder.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_office_night.wav（環境音）", "fx_paper_folder.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 CẢNH BÁO ĐỎ SINH TỒN TRƯỚC BẪY THAO TÚNG", "dur_s": 3.0},
            {"sau_cau": "TK5.01#2", "text": "CẢNH BÁO 1: CHIẾN THUẬT CÔ LẬP XÃ HỘI", "dur_s": 2.5},
            {"sau_cau": "TK5.01#4", "text": "CẢNH BÁO 2: LÀM SUY KIỆT THỂ XÁC TRIỆT TIÊU LÝ TRÍ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#5", "text": "CẢNH BÁO 3: SÙNG BÁI CÁ NHÂN & CẤM HOÀI NGHI", "dur_s": 2.5},
            {"sau_cau": "TK5.01#7", "text": "CẢNH BÁO 4: ĐẢO NGƯỢC ĐẠO ĐỨC BIỆN MINH TỘI ÁC", "dur_s": 2.5},
            {"sau_cau": "TK5.01#9", "text": "KHÔNG CÓ MỤC ĐÍCH CAO CẢ CHO PHƯƠNG TIỆN TÀN BẠO", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "FOUR SURVIVAL RED FLAGS AGAINST CULT COERCION", "dur_s": 3.0},
            {"after_id": "TK5.01#2", "text": "RED FLAG 1: STRATEGIC SOCIAL ISOLATION", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "RED FLAG 2: SYSTEMATIC PHYSICAL EXHAUSTION", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "RED FLAG 3: ABSOLUTE CULT OF PERSONALITY", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "RED FLAG 4: MORAL INVERSION JUSTIFYING CRUELTY", "dur_s": 2.5},
            {"after_id": "TK5.01#9", "text": "NO NOBLE OBJECTIVE CAN JUSTIFY CRUEL METHODOLOGY", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "マインドコントロールを防ぐ4つの生存警告サイン", "dur_s": 3.0},
            {"after_id": "TK5.01#2", "text": "第1の警告：意図的な社会的分離と孤立化", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "第2の警告：批判力を麻痺させる計画的肉体酷使", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "第3の警告：絶対的個人崇拝と疑問の禁止", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "第4の警告：残虐行為を正当化する道徳規範の反転", "dur_s": 2.5},
            {"after_id": "TK5.01#9", "text": "いかなる崇高な目的も残虐な手段を正当化できない", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t8_redflag1_social_isolation", "pull"),
            ("H", "5.06#1", "neutral", -0.02, 0.6, "t8_redflag1_social_isolation", "still"),
            ("H", "5.06#2", "neutral", -0.02, 0.6, "t8_redflag1_social_isolation", "push"),
            ("H", "5.06#3", "neutral", -0.02, 0.6, "t8_redflag1_social_isolation", "pan"),
            ("H", "5.06#4", "neutral", -0.02, 0.6, "t8_redflag2_physical_exhaustion", "pull"),
            ("H", "5.06#7", "neutral", -0.02, 0.6, "t8_redflag3_cult_of_personality", "still"),
            ("H", "5.06#8", "neutral", -0.02, 0.6, "t8_redflag3_cult_of_personality", "push"),
            ("H", "5.06#9", "neutral", -0.02, 0.6, "t8_redflag4_moral_inversion", "pan"),
            ("H", "5.06#10", "neutral", -0.02, 0.6, "t8_redflag4_moral_inversion", "still"),
            ("H", "5.06#11", "neutral", -0.02, 0.6, "t8_tokyo_dawn_restored_peace", "pull"),
            ("H", "cta", "neutral", -0.02, 0.0, "t8_tokyo_dawn_restored_peace", "still")
        ]
    }
]

# ----------------------------------------------------------------------------
# 3. HÀM TÍNH THỜI LƯỢNG CHÍNH XÁC
# ----------------------------------------------------------------------------
CTA_VN = "Tập tám của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio."
CTA_EN = "Episode eight of Amber Eyes. Watch the full documentary at the link in bio."
CTA_JA = "Amber Eyes 第8話。事件の完全版はプロフィールのリンクからご覧いただけます。"

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
            line_dur = words * RATE_VI.get(role, 0.35)
        elif lang == "EN":
            words = len([w for w in re.sub(r"<#[\d.]+#>", " ", txt).split() if w.strip()])
            line_dur = words * RATE_EN.get(role, 0.35)
        else:
            chars = len(re.sub(r"<#[\d.]+#>", " ", txt).replace(" ", "").strip())
            line_dur = chars * RATE_JA.get(role, 0.18)
            
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
        "episode": "08",
        "lang": lang,
        "engine": "Higgs Audio v3 + VoxCPM2 reference voices",
        "clips": {}
    }
    
    if lang == "VI":
        plan_lines.append("# KẾ HOẠCH CLIP TIKTOK — TẬP 08 · \"KHI CÁC THIÊN TÀI BỊ TẨY NÃO\"\n")
        plan_lines.append("*Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*")
        plan_lines.append("*Nguồn duy nhất của mọi dữ kiện: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap08/KeHoach_Video_Tap08.md` · `.work/script_tap08.json` (218 câu)*")
        plan_lines.append("*Sinh tự động bởi `.work/_build_tk_tap08.py`*\n---\n")
        plan_lines.append("## 0. Tóm tắt chốt\n")
        plan_lines.append("| Hạng mục | Giá trị |")
        plan_lines.append("|---|---|")
        plan_lines.append("| Số clip | **5 clip** (TK1–TK4 phân tích chuyên sâu + TK5 cảnh báo đỏ sinh tồn) |")
        plan_lines.append("| Tổng câu thoại | **52 câu** đọc giọng (TK1: 10, TK2: 10, TK3: 11, TK4: 11, TK5: 11) |")
        plan_lines.append("| Chủ đề | Mỗi clip giải phẫu **1–2 chỉ dấu tâm lý cốt lõi** (Hệ sinh thái 10 chỉ dấu K10) |")
        plan_lines.append("| Ngôn ngữ | Tiếng Việt · vai Host (H), Điều tra viên (D), Chuyên gia (C), Lời khai Bác sĩ Hayashi (N2) |")
        plan_lines.append("| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** (đúng cast chuẩn Tập 08) |")
        plan_lines.append("| Hình ảnh | Nền dọc 9:16 crop/pad từ 74 nền 16:9 gốc của Tập 08 |")
        plan_lines.append("| Độ dài ước lượng | Đạt chuẩn 45–95 s (trung bình 67–83 s/clip) |\n---\n")
        plan_lines.append("## 1. Danh sách 5 clip và chỉ dấu tâm lý (K10)\n")
        plan_lines.append("| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng |")
        plan_lines.append("|---|---|---|---|---|")
    elif lang == "EN":
        plan_lines.append("# TIKTOK CLIP PRODUCTION PLAN — EPISODE 08 · \"WHEN GENIUSES ARE BRAINWASHED\"\n")
        plan_lines.append("*Status: **Script completed, ready for verification prior to TTS generation** (L4)*")
        plan_lines.append("*Single source of truth: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap08/KeHoach_Video_Tap08.md` · `.work/script_tap08_EN.json` (218 lines)*")
        plan_lines.append("*Auto-generated via `.work/_build_tk_tap08.py`*\n---\n")
        plan_lines.append("## 0. Executive Summary\n")
        plan_lines.append("| Item | Value |")
        plan_lines.append("|---|---|")
        plan_lines.append("| Total Clips | **5 clips** (TK1–TK4 narrative hooks + TK5 cult survival red flags) |")
        plan_lines.append("| Spoken Lines | **52 lines** (TK1: 10, TK2: 10, TK3: 11, TK4: 11, TK5: 11) |")
        plan_lines.append("| Framework | Psychological behavioral analysis based on 10 Core Markers (K10) |")
        plan_lines.append("| Cast | Host (H), Detective (D), Psychologist (C), Dr. Hayashi Testimony (N2) |")
        plan_lines.append("| Voice Engine | **Higgs Audio v3 + VoxCPM2 Reference Voices** |")
        plan_lines.append("| Visuals | 9:16 Vertical background art adapted from 74 original 16:9 backgrounds |")
        plan_lines.append("| Estimated Duration | Strictly within 45–95s TikTok gate (average 67–81s) |\n---\n")
        plan_lines.append("## 1. 5 Clips & Corresponding Psychological Markers (K10)\n")
        plan_lines.append("| Clip | Markers | Theme | Visual Hook Card (0–3 s) | Duration |")
        plan_lines.append("|---|---|---|---|---|")
    else:
        plan_lines.append("# TIKTOKクリップ制作計画 — 第08話 · 『天才たちが洗脳されたとき』\n")
        plan_lines.append("*ステータス: **台本策定完了 · 音声合成前の最終確認待ち** (L4)*")
        plan_lines.append("*情報源: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap08/KeHoach_Video_Tap08.md` · `.work/script_tap08_JA.json` (全218文)*")
        plan_lines.append("*`.work/_build_tk_tap08.py` により自動生成*\n---\n")
        plan_lines.append("## 0. 基本概要\n")
        plan_lines.append("| 項目 | 仕様 |")
        plan_lines.append("|---|---|")
        plan_lines.append("| クリップ数 | **全5本**（TK1–TK4 本編核心分析 + TK5 カルト生存警告サイン） |")
        plan_lines.append("| 総音声文数 | **52文**（TK1: 10文, TK2: 10文, TK3: 11文, TK4: 11文, TK5: 11文） |")
        plan_lines.append("| 分析枠組み | 犯罪心理学10大指標（K10）に準拠した深層行動プロファイリング |")
        plan_lines.append("| 配役 | ホスト (H), 捜査官 (D), 心理専門家 (C), 林郁夫医師の証言 (N2) |")
        plan_lines.append("| 音声エンジン | **Higgs Audio v3 + VoxCPM2 参照音声** |")
        plan_lines.append("| 映像素材 | 第08話公式背景（74枚）より適合させた 9:16 縦型美術背景 |")
        plan_lines.append("| 推定再生時間 | TikTok適正範囲（45–95秒）完全準拠（平均78–86秒） |\n---\n")
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

Tập 08 · Khi các thiên tài bị tẩy não — Chỉ dấu #{c['signs'][0]}: {c['theme_vn']}.
Hồ sơ vụ án có thật tại Tokyo, 100% dữ liệu đối chiếu hồ sơ điều tra và phán quyết tư pháp Nhật Bản.

📺 Xem trọn vẹn tập phân tích 32 phút ở link trong bio
🔎 Hồ sơ tâm lý học tội phạm · Vụ án Aum Shinrikyo & Khí độc Sarin 1995 · Thao túng tâm lý

Nội dung do AI hỗ trợ tạo hình và giọng phục vụ mục đích phân tích tâm lý giáo dục — không phải phóng sự giật gân.

#AmberEyes #TamLyToiPham #HosoCoThat #AumShinrikyo #ShokoAsahara #{c['id']} #TrueCrimeVN #PhanTichHanhVi #Tokyo1995

---
Ghi chú khi đăng (KHÔNG dán vào caption):
- BẬT toggle "Nội dung do AI tạo" (AI-generated content) trên TikTok.
- Dán link YouTube Tập 08 vào ô Website trong phần sửa hồ sơ cá nhân.
- Ước lượng thời lượng: {tot_dur} s ({num_l} câu).
- Tên file video thành phẩm: clip{c['id'][-1]}_{c['id']}.mp4 (1080x1920, 30fps).
"""
            mota_dai_text = f"""HỒ SƠ TẬP 08: KHI CÁC THIÊN TÀI BỊ TẨY NÃO — CLIP {c['id']}

CHỦ ĐỀ: {c['theme_vn']}
VỤ ÁN: Giáo phái Aum Shinrikyo & Thảm kịch khí độc Sarin tàu điện ngầm Tokyo (1995)

TÓM TẮT PHÂN TÍCH:
{c['hook_vn']}

Vụ tấn công khí độc tàu điện ngầm Tokyo năm 1995 là một trong những thảm kịch gây chấn động lịch sử nhân loại hiện đại. Điểm rùng mình và khó hiểu nhất của vụ án này không chỉ nằm ở độc chất sarin quân sự, mà nằm ở chính danh tính những kẻ chế tạo và thực thi: những nhà khoa học đỗ thủ khoa Đại học Tokyo, Đại học Kyoto, viện sĩ nghiên cứu virus và bác sĩ trưởng khoa tim mạch xuất chúng.

Dưới lăng kính của tâm lý học tội phạm và khoa học hành vi, clip này bóc tách bản chất của:
1. Cơ chế thao túng tâm lý và kiểm soát cưỡng bách đánh sập tư duy duy lý của giới tinh hoa.
2. Cách sự trống rỗng hiện sinh và cái tôi trí tuệ bị lợi dụng để biến tri thức thành công cụ hủy diệt.
3. Bài học thức tỉnh sâu sắc về ranh giới sinh tồn giữa trí tuệ lý trí và sự tỉnh táo của lương tri.

📺 XEM TRỌN VẸN HỒ SƠ 32 PHÚT TRÊN KÊNH YOUTUBE AMBER EYES (LINK TRONG BIO).
"""
            mota_ngan_text = f"""Tập 08 Amber Eyes — Clip {c['id']}: {c['title_vn']}.
{c['hook_vn']}
Xem hồ sơ giải phẫu tâm lý đầy đủ tại link bio. #AmberEyes #TamLyToiPham #{c['id']} #AumShinrikyo
"""
        elif lang == "EN":
            cap_text = f"""{c['hook_en']} 👁️

Ep. 08 · When Geniuses Are Brainwashed — Psychological Marker #{c['signs'][0]}: {c['theme_en']}.
Authentic criminal dossier from Tokyo, strictly source-verified against judicial records.

📺 Watch the full 32-minute documentary on YouTube — link in bio.
🔎 Criminal Psychology · Aum Shinrikyo & Tokyo Sarin Attack 1995 · Behavioral Profiling

Content created with AI assistance for behavioral and psychological educational purposes.

#AmberEyes #CriminalPsychology #TrueCrime #AumShinrikyo #ShokoAsahara #{c['id']} #CaseFile #Mindhunter #Tokyo1995

---
Publishing Notes (DO NOT paste into caption):
- TOGGLE ON 'AI-generated content' label in TikTok settings.
- Add YouTube Episode 08 URL to the Website field in your profile bio.
- Estimated duration: {tot_dur} s ({num_l} lines).
- Video output file: clip{c['id'][-1]}_{c['id']}_EN.mp4 (1080x1920, 30fps).
"""
            mota_dai_text = f"""DOSSIER EPISODE 08: WHEN GENIUSES ARE BRAINWASHED — CLIP {c['id']}

THEME: {c['theme_en']}
CASE FILE: Aum Shinrikyo & The 1995 Tokyo Subway Sarin Attack

ANALYSIS SUMMARY:
{c['hook_en']}

The 1995 Tokyo subway sarin attack remains one of the darkest milestones in modern criminal history. The most chilling enigma was not merely the weaponization of military neurotoxins, but the intellectual pedigree of the perpetrators: graduates of University of Tokyo, Kyoto University, virologists, and chief cardiologists.

Key Psychological Insights Explored:
1. Coercive control mechanisms that systematically dismantled elite rational defenses.
2. How existential vacuum and intellectual hubris turned brilliant minds into instruments of mass murder.
3. Vital behavioral insights safeguarding critical thinking and moral conscience.

📺 WATCH THE FULL 32-MINUTE DOCUMENTARY ON YOUTUBE (LINK IN BIO).
"""
            mota_ngan_text = f"""Amber Eyes Ep. 08 — Clip {c['id']}: {c['title_en']}.
{c['hook_en']}
Full behavioral case study available via link in bio. #AmberEyes #TrueCrime #{c['id']} #AumShinrikyo
"""
        else:
            cap_text = f"""{c['hook_ja']} 👁️

第08話 · 天才たちが洗脳されたとき — 心理指標 #{c['signs'][0]}: {c['theme_ja']}。
日本の司法記録および捜査公文書に基づく厳密な犯罪心理学プロファイリング。

📺 完全版ドキュメンタリー（32分）はYouTubeにて公開中 — プロフィールのリンクから
🔎 犯罪心理学 · オウム真理教事件 · 地下鉄サリン事件 · マインドコントロール分析

本コンテンツは心理分析および啓発を目的としてAI技術の支援を受けて制作されています。

#AmberEyes #犯罪心理学 #地下鉄サリン事件 #オウム真理教 #麻原彰晃 #{c['id']} #マインドハンター #実話事件簿

---
投稿時の注意事項（キャプション本文には貼り付けないでください）：
- TikTokアプリ内で「AI生成コンテンツ」のトグルを必ずONに設定してください。
- YouTube第08話へのリンクをプロフィール欄のウェブサイト項目に設定してください。
- 推定再生時間: {tot_dur} 秒 (全{num_l}文)。
- 出力動画ファイル名: clip{c['id'][-1]}_{c['id']}_JA.mp4 (1080x1920, 30fps)。
"""
            mota_dai_text = f"""事件簿 第08話：天才たちが洗脳されたとき — クリップ {c['id']}

テーマ：{c['theme_ja']}
事件名：オウム真理教と1995年地下鉄サリン事件（東京）

分析概要：
{c['hook_ja']}

1995年3月20日、東京の地下鉄を襲った化学兵器テロ。この未曾有の凶行において世界を最も震撼させたのは、実行犯たちが東大、京大、慶應大卒の超エリート科学者や高名な心臓病専門医であったという冷厳な事実でした。

心理学的分析の焦点：
1. 超エリートたちの理性的防壁を破綻させたマインドコントロール技術。
2. 現代社会における「実存的真空」と「過剰な知的プライド」の致命的結合。
3. 破滅的カルトや心理操作の罠から身を守るための重要な心理学的境界線。

📺 YouTube「Amber Eyes」にて32分の本編完全解説を公開中（プロフィールリンクより）。
"""
            mota_ngan_text = f"""Amber Eyes 第08話 — クリップ {c['id']}：『{c['title_ja']}』。
{c['hook_ja']}
事件の完全版解説はプロフィールのリンクから。 #AmberEyes #犯罪心理学 #{c['id']} #オウム真理教
"""

        cap_file.write_text(cap_text.strip() + "\n", encoding="utf-8")
        mota_dai_file.write_text(mota_dai_text.strip() + "\n", encoding="utf-8")
        mota_ngan_file.write_text(mota_ngan_text.strip() + "\n", encoding="utf-8")
        
    # Ghi file kế hoạch và spec json
    if lang == "VI":
        (out_dir / "KE_HOACH_CLIP_TAP08.md").write_text("\n".join(plan_lines), encoding="utf-8")
    elif lang == "EN":
        (out_dir / "KE_HOACH_CLIP_TAP08_EN.md").write_text("\n".join(plan_lines), encoding="utf-8")
    else:
        (out_dir / "KE_HOACH_CLIP_TAP08_JA.md").write_text("\n".join(plan_lines), encoding="utf-8")
        
    (out_dir / "SPEC_AUDIO_CLIP_TAP08.json").write_text(json.dumps(spec_json, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Hoàn thành xuất tài liệu TikTok Tập 08 cho ngôn ngữ: {lang} -> {out_dir}")

print("TẤT CẢ ĐÃ HOÀN TẤT THÀNH CÔNG 100%.")
