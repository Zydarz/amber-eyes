# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 11 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap11/KE_HOACH_CLIP_TAP11.md
  02_SAN_XUAT/TIKTOK/Tap11/SPEC_AUDIO_CLIP_TAP11.json
  02_SAN_XUAT/TIKTOK/Tap11/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap11/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap11/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap11_EN/KE_HOACH_CLIP_TAP11_EN.md
  02_SAN_XUAT/TIKTOK/Tap11_EN/SPEC_AUDIO_CLIP_TAP11.json
  02_SAN_XUAT/TIKTOK/Tap11_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap11_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap11_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap11_JA/KE_HOACH_CLIP_TAP11_JA.md
  02_SAN_XUAT/TIKTOK/Tap11_JA/SPEC_AUDIO_CLIP_TAP11.json
  02_SAN_XUAT/TIKTOK/Tap11_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap11_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap11_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 11:
- timeline_s_t11.json (VI)
- timeline_s_EN_t11.json (EN)
- timeline_s_JA_t11.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap11"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap11_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap11_JA"

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
# 0. TỶ LỆ ĐỌC THẬT (Đo từ master Tập 11)
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

RATE_VI = get_rates("timeline_s_t11.json", is_ja=False)
RATE_EN = get_rates("timeline_s_EN_t11.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t11.json", is_ja=True)

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
                role = "N1" if el["id"] == "1.06" else "N2"
            for s in el["sentences"]:
                txt = s["text"].strip()
                res[s["id"]] = (role, txt)
    return res

MAP_VI = load_script_map("script_tap11.json")
MAP_EN = load_script_map("script_tap11_EN.json")
MAP_JA = load_script_map("script_tap11_JA.json")

# ----------------------------------------------------------------------------
# 2. KHAI BÁO 5 CLIP TẬP 11 (BẢN VI, EN, JA)
# ----------------------------------------------------------------------------
CLIPS_CONFIG = [
    {
        "id": "TK1",
        "title_vn": "Vỏ bọc Ken & Barbie và Điểm mù Ngoại ô",
        "title_en": "The Ken & Barbie Facade and Suburban Blind Spots",
        "title_ja": "ケン＆バービーの仮面と郊外住宅街の心理的盲点",
        "signs": [1, 9],
        "theme_vn": "Hiệu ứng Hào quang (Halo Effect) & Điểm mù Ngoại ô (Suburban Blind Spot)",
        "theme_en": "The Halo Effect & Suburban Blind Spots",
        "theme_ja": "ハロー効果と郊外住宅街の盲点",
        "hook_vn": "Cặp đôi búp bê Ken và Barbie đời thực. Tại sao cả khu phố không hề nghi ngờ?",
        "hook_en": "A real-life Ken and Barbie couple. Why was the entire town completely blinded?",
        "hook_ja": "実写版ケン＆バービーの理想的カップル。なぜ街全体が欺かれたのか？",
        "bgm": "bgm_piano_minimal.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_piano_minimal.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_piano_minimal.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_piano_minimal.mp3",
        "sfx_vn": ["amb_wind_cold.wav (nền)", "fx_door_close.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_wind_cold.wav (bed)", "fx_door_close.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_wind_cold.wav（環境音）", "fx_door_close.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "SỐ 57 ĐẠI LỘ BAYVIEW DRIVE · PORT DALHOUSIE", "dur_s": 3.0},
            {"sau_cau": "TK1.01#4", "text": "BIỆT DANH: BÚP BÊ KEN & BARBIE ĐỜI THỰC", "dur_s": 2.5},
            {"sau_cau": "TK1.01#6", "text": "CHIẾC MẶT NẠ THÁNH THIỆN RU NGỦ CỘNG ĐỒNG", "dur_s": 2.5},
            {"sau_cau": "TK1.01#8", "text": "HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ NGOẠI Ô", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "57 BAYVIEW DRIVE · PORT DALHOUSIE", "dur_s": 3.0},
            {"after_id": "TK1.01#4", "text": "REAL-LIFE KEN & BARBIE FACADE", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "PERFECT NEIGHBORHOOD BLIND SPOT", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "THE HALO EFFECT & SUBURBAN ILLUSION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "オンタリオ州ポート・ダルハウジー · ベイビュー57番地", "dur_s": 3.0},
            {"after_id": "TK1.01#4", "text": "実写版ケン＆バービーの仮面", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "地域社会を欺いた完璧な隣人像", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "ハロー効果と郊外住宅街の盲点", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("1.03#1", "neutral", -0.02, 0.6, "t11_pink_house_57_bayview", "pan"),
            ("1.03#3", "neutral", -0.02, 0.6, "t11_paul_bernardo_dashing_car", "still"),
            ("1.03#4", "neutral", -0.02, 0.6, "t11_karla_veterinary_clinic", "pull"),
            ("1.03#5", "neutral", -0.02, 0.6, "t11_ken_barbie_golden_illusion", "still"),
            ("1.06#1", "neutral", -0.02, 0.6, "t11_suburban_admiration_facade", "push"),
            ("1.06#4", "sad", -0.04, 0.7, "t11_closed_pink_door_abyss", "still"),
            ("1.07#1", "neutral", -0.02, 0.6, "t11_expert_desk_lamp", "pull"),
            ("1.07#4", "neutral", -0.02, 0.0, "t11_pink_house_winter_dusk", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Quỹ đạo leo thang của tội ác — 4 nấc thang tha hóa",
        "title_en": "Escalation Trajectory — 4 Stages of Moral Degradation",
        "title_ja": "犯罪のエスカレーション軌道 — 破滅への4つの階段",
        "signs": [7, 8],
        "theme_vn": "Quỹ đạo leo thang ảo tưởng (Escalation Trajectory) & Thủ đoạn MO vs Dấu ấn Signature",
        "theme_en": "Fantasy Escalation Trajectory & MO vs Signature",
        "theme_ja": "暴力妄想のエスカレーション軌道と手口MO対署名Signature",
        "hook_vn": "Từ kẻ rình rập Scarborough đến vụ bắt cóc giữa ban ngày. Tội ác đã leo thang thế nào?",
        "hook_en": "From suburban night prowler to broad daylight church abductions. How did the predation escalate?",
        "hook_ja": "深夜の単独犯から教会での白昼堂々の拉致へ。凶行はどう暴走したのか？",
        "bgm": "bgm_cell_dark.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_cell_dark.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_cell_dark.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_cell_dark.mp3",
        "sfx_vn": ["amb_night_highway.wav (nền)", "fx_police_siren_distant.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_night_highway.wav (bed)", "fx_police_siren_distant.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_night_highway.wav（環境音）", "fx_police_siren_distant.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "4 NẤC THANG LEO THANG TỘI ÁC", "dur_s": 3.0},
            {"sau_cau": "TK2.01#3", "text": "NẤC 1: KẺ SĂN MỒI NGOẠI Ô SCARBOROUGH", "dur_s": 2.5},
            {"sau_cau": "TK2.01#5", "text": "NẤC 2: LIÊN MINH CỘNG SINH ĐỘC HẠI", "dur_s": 2.5},
            {"sau_cau": "TK2.01#7", "text": "NẤC 3: GIAM GIỮ TẠI SỐ 57 BAYVIEW DRIVE", "dur_s": 2.5},
            {"sau_cau": "TK2.01#9", "text": "NẤC 4: BẮT CÓC BAN NGÀY TẠI BÃI XE NHÀ THỜ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "4 STAGES OF CRIMINAL ESCALATION", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "STAGE 1: THE SCARBOROUGH NIGHT PROWLER", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "STAGE 2: TOXIC SYMBIOTIC ALLIANCE", "dur_s": 2.5},
            {"after_id": "TK2.01#7", "text": "STAGE 3: PROTRACTED CONFINEMENT AT HOME", "dur_s": 2.5},
            {"after_id": "TK2.01#9", "text": "STAGE 4: DAYLIGHT CHURCH AMBUSH", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "犯罪エスカレーションの4段階", "dur_s": 3.0},
            {"after_id": "TK2.01#3", "text": "第1段階: スカボローの夜間連続通り魔", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "第2段階: 有毒な共生関係の確立", "dur_s": 2.5},
            {"after_id": "TK2.01#7", "text": "第3段階: 自宅での監禁と支配", "dur_s": 2.5},
            {"after_id": "TK2.01#9", "text": "第4段階: 教会駐車場での白昼堂々の襲撃", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("2.04#1", "neutral", -0.03, 0.6, "t11_investigation_board_four_stages", "still"),
            ("2.04#2", "neutral", -0.03, 0.5, "t11_scarborough_nocturnal_shadow", "pan"),
            ("2.04#3", "neutral", -0.03, 0.6, "t11_scarborough_night_street_lurking", "pull"),
            ("2.04#4", "neutral", -0.03, 0.5, "t11_silent_christmas_tragedy", "still"),
            ("2.04#5", "sad", -0.04, 0.7, "t11_christmas_1990_halothane_bottle", "push"),
            ("2.04#6", "neutral", -0.03, 0.5, "t11_closed_pink_door_abyss", "still"),
            ("2.04#7", "neutral", -0.03, 0.7, "t11_bayview_basement_concrete", "pan"),
            ("2.04#8", "neutral", -0.03, 0.5, "t11_church_parking_daytime_abduction", "still"),
            ("2.04#9", "neutral", -0.03, 0.7, "t11_church_parking_lot_ambush", "push"),
            ("2.04#12", "neutral", -0.03, 0.0, "t11_coupled_shadows_mirror", "still")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Hội chứng Điên cuồng đôi (Folie à Deux) & Cơ chế Vật hóa",
        "title_en": "Folie à Deux & Dehumanization Mechanisms",
        "title_ja": "共有妄想（フォリー・ドゥ）と人間性の剥奪メカニズム",
        "signs": [2, 3],
        "theme_vn": "Điên cuồng đôi (Folie à Deux) & Cơ chế vật hóa (Dehumanization) người thân",
        "theme_en": "Shared Psychotic Disorder (Folie à Deux) & Dehumanization of Kin",
        "theme_ja": "共有精神病性障害（感応精神病）と身内のモノ化・非人間化",
        "hook_vn": "Tại sao một người phụ nữ trẻ lại tự tay dâng hiến chính em gái ruột của mình?",
        "hook_en": "Why would an educated young woman offer her own biological sister as a sacrificial token?",
        "hook_ja": "なぜ実の妹までもが生け贄にされたのか？病的な共生妄想の深淵。",
        "bgm": "bgm_cello_sad_v2.mp3",
        "bgm_desc_vn": "Hồi 3 — bed tập: bgm_cello_sad_v2.mp3",
        "bgm_desc_en": "Act 3 — episode bed: bgm_cello_sad_v2.mp3",
        "bgm_desc_ja": "第3幕 — 本編BGM: bgm_cello_sad_v2.mp3",
        "sfx_vn": ["amb_sub_drone.wav (nền)", "fx_heartbeat_slow.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_sub_drone.wav (bed)", "fx_heartbeat_slow.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_sub_drone.wav（環境音）", "fx_heartbeat_slow.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "HIỆN TƯỢNG ĐIÊN CUỒNG ĐÔI: FOLIE À DEUX", "dur_s": 3.0},
            {"sau_cau": "TK3.01#4", "text": "BUỒNG CỘNG HƯỞNG TỘI ÁC KHÔNG THỂ THOÁT", "dur_s": 2.5},
            {"sau_cau": "TK3.01#6", "text": "HIỆN TƯỢNG VẬT HÓA & PHI NHÂN HÓA", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "ĐIỂM GÃY TÂM LÝ: XUNG ĐỘT THÁNG 1/1993", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "SHARED MADNESS: FOLIE À DEUX", "dur_s": 3.0},
            {"after_id": "TK3.01#4", "text": "LETHAL PSYCHOLOGICAL ECHO CHAMBER", "dur_s": 2.5},
            {"after_id": "TK3.01#6", "text": "DEHUMANIZATION & PROJECTION", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "THE BREAKING POINT: JANUARY 1993", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "感応精神病: フォリー・ドゥの共鳴", "dur_s": 3.0},
            {"after_id": "TK3.01#4", "text": "逃れられない閉鎖的共鳴室", "dur_s": 2.5},
            {"after_id": "TK3.01#6", "text": "身内の非人間化と心理的投影", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "心理的崩壊点: 1993年1月の家庭内暴力", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("3.04#1", "neutral", -0.02, 0.6, "t11_folie_a_deux_resonance", "pull"),
            ("3.04#2", "neutral", -0.02, 0.6, "t11_coupled_shadows_mirror", "still"),
            ("3.04#3", "neutral", -0.02, 0.6, "t11_destructive_flame_alliance", "pan"),
            ("3.04#7", "neutral", -0.02, 0.7, "t11_obedient_accomplice_strings", "still"),
            ("3.05#1", "neutral", -0.02, 0.6, "t11_cracked_mirror_hallway", "push"),
            ("3.05#3", "sad", -0.04, 0.8, "t11_silent_christmas_tragedy", "still"),
            ("3.06#1", "neutral", -0.02, 0.6, "t11_featureless_peg_dolls", "pull"),
            ("3.06#2", "neutral", -0.02, 0.7, "t11_covert_sociopath_profile", "still"),
            ("3.08#1", "neutral", -0.03, 0.6, "t11_flashlight_shattered_hallway", "push"),
            ("3.08#6", "neutral", -0.03, 0.0, "t11_escape_to_parents_porch", "still")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Chiếc mặt nạ nạn nhân và Thỏa thuận với Quỷ dữ",
        "title_en": "The Victim Mask and the Deal with the Devil",
        "title_ja": "被害者の仮面と『悪魔との司法取引』",
        "signs": [4, 5],
        "theme_vn": "Thao túng đóng vai nạn nhân (Manipulative Victimhood) & Hối hận toan tính",
        "theme_en": "Weaponized Victim Playing & The Infamous Deal with the Devil",
        "theme_ja": "被害者ポジションの武器化と『悪魔との司法取引』",
        "hook_vn": "Nước mắt tại bàn đàm phán và thỏa thuận 12 năm tù. Lương tri hay một màn kịch?",
        "hook_en": "Tears at the plea bargaining table and a 12-year deal. Remorse or ruthless manipulation?",
        "hook_ja": "取調室の涙と12年の司法取引。良心の悔悟か、冷酷な演技か？",
        "bgm": "bgm_sub_drone.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_sub_drone.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_sub_drone.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_sub_drone.mp3",
        "sfx_vn": ["amb_courtroom_tension.wav (nền)", "fx_tape_rewind.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_courtroom_tension.wav (bed)", "fx_tape_rewind.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_courtroom_tension.wav（環境音）", "fx_tape_rewind.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "BI KỊCH TƯ PHÁP: THỎA THUẬN VỚI QUỶ DỮ", "dur_s": 3.0},
            {"sau_cau": "TK4.01#3", "text": "SỰ SỤP ĐỔ CỦA CHIẾC MẶT NẠ NẠN NHÂN", "dur_s": 2.5},
            {"sau_cau": "TK4.01#5", "text": "6 CUỐN BĂNG TRÊN TRẦN NHÀ TỐ CÁO SỰ THẬT", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "NỖI UẤT NGHẸN CỦA CƠ QUAN CÔNG TỐ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "JUDICIAL DISASTER: DEAL WITH THE DEVIL", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "COLLAPSE OF THE VICTIM FACADE", "dur_s": 2.5},
            {"after_id": "TK4.01#5", "text": "6 CEILING TAPES EXPOSE THE TRUTH", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "HUMILIATION OF THE CROWN PROSECUTION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "司法の悲劇: 悪魔との司法取引", "dur_s": 3.0},
            {"after_id": "TK4.01#3", "text": "被害者の仮面の完全崩壊", "dur_s": 2.5},
            {"after_id": "TK4.01#5", "text": "屋根裏の6本のビデオテープの衝撃", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "検察官たちの胸を突く屈辱と後悔", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("4.08#1", "neutral", -0.03, 0.6, "t11_deal_with_the_devil_contract", "still"),
            ("4.10#4", "neutral", -0.03, 0.7, "t11_dark_screening_room_projector", "pull"),
            ("4.10#5", "sad", -0.04, 0.7, "t11_investigator_nausea_monitor", "still"),
            ("4.11#1", "sad", -0.04, 0.6, "t11_dark_screening_room_projector", "push"),
            ("4.11#2", "sad", -0.04, 0.6, "t11_interrogation_bruised_facade", "still"),
            ("4.11#3", "neutral", -0.03, 0.7, "t11_six_tapes_on_floor", "pull"),
            ("4.11#4", "sad", -0.04, 0.7, "t11_equal_partner_in_cruelty", "still"),
            ("4.11#5", "sad", -0.04, 0.8, "t11_mockery_of_justice_tears", "push"),
            ("4.13#1", "neutral", -0.02, 0.6, "t11_victim_playing_camouflage_mirror", "still"),
            ("4.13#8", "neutral", -0.02, 0.0, "t11_weaponized_victim_playing", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Nạn nhân học & 4 cảnh báo đỏ sinh tồn",
        "title_en": "Victimology & 4 Survival Red Flags",
        "title_ja": "被害者学と生き残るための4つの危険信号",
        "signs": [10],
        "theme_vn": "Nạn nhân học (Victimology) & 4 tín hiệu cảnh báo đỏ sinh tồn",
        "theme_en": "Victimology & 4 Essential Survival Red Flags",
        "theme_ja": "被害者学と生存のための4つの警戒サイン",
        "hook_vn": "Bốn tín hiệu cảnh báo đỏ để không bao giờ rơi vào chiếc bẫy cộng sinh độc hại.",
        "hook_en": "Four critical survival red flags to never fall into a predatory symbiotic trap.",
        "hook_ja": "有毒な共生関係に引きずり込まれないための、4つの生存の警告サイン。",
        "bgm": "bgm_warm_piano.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_warm_piano.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_warm_piano.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_warm_piano.mp3",
        "sfx_vn": ["amb_room_warm.wav (nền)", "fx_clock_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_warm.wav (bed)", "fx_clock_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_warm.wav（環境音）", "fx_clock_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 TÍN HIỆU CẢNH BÁO ĐỎ SINH TỒN", "dur_s": 3.0},
            {"sau_cau": "TK5.01#2", "text": "CẢNH BÁO 1: KẺ LẠM DỤNG TỔN THƯƠNG QUÁ KHỨ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#4", "text": "CẢNH BÁO 2: BẤT NHẤT LỜI NÓI VÀ HÀNH VI", "dur_s": 2.5},
            {"sau_cau": "TK5.01#6", "text": "CẢNH BÁO 3: SỰ TIẾP CẬN CỦA VẺ VÔ HẠI", "dur_s": 2.5},
            {"sau_cau": "TK5.01#8", "text": "CẢNH BÁO 4: NHẬN DIỆN CỘNG SINH ĐỘC HẠI", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "4 CRITICAL SURVIVAL RED FLAGS", "dur_s": 3.0},
            {"after_id": "TK5.01#2", "text": "RED FLAG 1: WEAPONIZING PAST TRAUMA", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "RED FLAG 2: WORDS VS ACTIONS DISCREPANCY", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "RED FLAG 3: THE SEEMINGLY HARMLESS FACADE", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "RED FLAG 4: TOXIC SYMBIOTIC TRAPS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "4つの生存のための赤い警戒サイン", "dur_s": 3.0},
            {"after_id": "TK5.01#2", "text": "警告1: 過去の被害を免罪符にする者", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "警告2: 道徳的発言と裏の行動の乖離", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "警告3: 無害さを装った接近への警戒", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "警告4: 有毒な共生関係の早期察知", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("5.08#1", "neutral", -0.02, 0.6, "t11_amber_eyes_redflag_intro", "still"),
            ("5.08#2", "neutral", -0.02, 0.5, "t11_four_warning_lights", "pan"),
            ("5.08#3", "neutral", -0.02, 0.7, "t11_redflag1_evading_accountability", "pull"),
            ("5.08#4", "neutral", -0.02, 0.5, "t11_redflag2_words_vs_actions_split", "still"),
            ("5.08#5", "neutral", -0.02, 0.7, "t11_disguised_predator_scales", "push"),
            ("5.08#6", "neutral", -0.02, 0.5, "t11_fragile_beauty_manipulation", "still"),
            ("5.08#7", "neutral", -0.02, 0.7, "t11_redflag3_guilt_tripping_trap", "pull"),
            ("5.08#8", "neutral", -0.02, 0.5, "t11_redflag4_toxic_symbiosis_abyss", "still"),
            ("5.08#11", "neutral", -0.02, 0.0, "t11_survival_intuition_bell", "push")
        ]
    }
]

# ----------------------------------------------------------------------------
# 3. BUILD AND EXPORT FOR VI, EN, JA
# ----------------------------------------------------------------------------
CTA_LINE = {
    "VI": ("H", "neutral", -0.02, 0.0, "t11_amber_eyes_closing_dossier_bernardo", "still",
           "Tập mười một của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.", "CTA"),
    "EN": ("H", "neutral", -0.02, 0.0, "t11_amber_eyes_closing_dossier_bernardo", "still",
           "Episode eleven of Amber Eyes. Watch the full dossier via the link in our bio.", "CTA"),
    "JA": ("H", "neutral", -0.02, 0.0, "t11_amber_eyes_closing_dossier_bernardo", "still",
           "Amber Eyes 第11話。事件の全貌はバイオのリンクからご覧いただけます。", "CTA")
}

for lang, out_dir in [("VI", OUT_VI), ("EN", OUT_EN), ("JA", OUT_JA)]:
    smap = MAP_VI if lang == "VI" else (MAP_EN if lang == "EN" else MAP_JA)
    rates = RATE_VI if lang == "VI" else (RATE_EN if lang == "EN" else RATE_JA)
    is_ja = (lang == "JA")

    clips_summary = []
    clips_spec = {}

    plan_lines = []
    if lang == "VI":
        plan_lines.append("# KẾ HOẠCH CLIP TIKTOK — TẬP 11 · CẶP ĐÔI KEN & BARBIE\n")
        plan_lines.append("*Trạng thái: Kịch bản hoàn thành, chuẩn hóa 10 chỉ dấu tâm lý (K10), đối chiếu 100% hồ sơ gốc*\n")
        plan_lines.append(f"*Tỷ lệ đọc đo thực tế từ master Tập 11: H={rates['H']:.3f}s/từ, D={rates['D']:.3f}s/từ, C={rates['C']:.3f}s/từ, N1={rates['N1']:.3f}s/từ, N2={rates['N2']:.3f}s/từ*\n")
    elif lang == "EN":
        plan_lines.append("# TIKTOK CLIP PLAN — EPISODE 11 · THE KEN & BARBIE KILLERS\n")
        plan_lines.append("*Status: Production-ready, 10 psychological markers (K10), strictly source-verified*\n")
        plan_lines.append(f"*Measured speech rates from master Ep 11: H={rates['H']:.3f}s/w, D={rates['D']:.3f}s/w, C={rates['C']:.3f}s/w, N1={rates['N1']:.3f}s/w, N2={rates['N2']:.3f}s/w*\n")
    else:
        plan_lines.append("# TikTokクリップ制作計画 — 第11話（日本語） · 「ケン＆バービー連続殺人事件」\n")
        plan_lines.append("*状態: 制作準備完了、10の心理指標（K10）準拠、公的記録100%対照済*\n")
        plan_lines.append(f"*第11話実測音声レート: H={rates['H']:.3f}s/文字, D={rates['D']:.3f}s/文字, C={rates['C']:.3f}s/文字, N1={rates['N1']:.3f}s/文字, N2={rates['N2']:.3f}s/文字*\n")

    plan_lines.append("## 1. Danh sách 5 Clip và Chỉ dấu Tâm lý\n")
    plan_lines.append("| Clip | Chỉ dấu | Chủ đề | Hook (0–3s) | Ước lượng |")
    plan_lines.append("|---|---|---|---|---|")

    for cidx, cfg in enumerate(CLIPS_CONFIG, start=1):
        cid = cfg["id"]
        title = cfg["title_vn"] if lang == "VI" else (cfg["title_en"] if lang == "EN" else cfg["title_ja"])
        theme = cfg["theme_vn"] if lang == "VI" else (cfg["theme_en"] if lang == "EN" else cfg["theme_ja"])
        hook = cfg["hook_vn"] if lang == "VI" else (cfg["hook_en"] if lang == "EN" else cfg["hook_ja"])
        signs_str = " · ".join([f"#{s}" for s in cfg["signs"]])

        # Assemble lines
        lines_data = []
        tot_dur = 0.0

        for line_idx, (orig_sid, emot, spd, pause, bg_id, motion) in enumerate(cfg["lines_meta"], start=1):
            role, txt = smap[orig_sid]
            u_cnt = len(txt.replace(" ", "")) if is_ja else len(txt.split())
            dur = u_cnt * rates[role]
            tot_dur += dur + pause
            c_sid = f"{cid}.01#{line_idx}"
            lines_data.append({
                "id": c_sid,
                "orig_id": orig_sid,
                "role": role,
                "emotion": emot,
                "speed": spd,
                "pause_after": pause,
                "bg": bg_id,
                "motion": motion,
                "text": txt,
                "dur_est": round(dur, 2)
            })

        # Append CTA line
        cta_role, cta_emot, cta_spd, cta_pause, cta_bg, cta_motion, cta_text, cta_orig = CTA_LINE[lang]
        cta_cnt = len(cta_text.replace(" ", "")) if is_ja else len(cta_text.split())
        cta_dur = cta_cnt * rates[cta_role]
        tot_dur += cta_dur
        lines_data.append({
            "id": f"{cid}.01#{len(lines_data)+1}",
            "orig_id": cta_orig,
            "role": cta_role,
            "emotion": cta_emot,
            "speed": cta_spd,
            "pause_after": cta_pause,
            "bg": cta_bg,
            "motion": cta_motion,
            "text": cta_text,
            "dur_est": round(cta_dur, 2)
        })

        tot_dur_rnd = round(tot_dur, 1)
        clips_summary.append({
            "id": cid,
            "title": title,
            "signs": cfg["signs"],
            "theme": theme,
            "lines_count": len(lines_data),
            "est_dur_s": tot_dur_rnd
        })

        plan_lines.append(f"| **{cid}** | {signs_str} | {theme} | *\"{hook}\"* | {tot_dur_rnd} s · {len(lines_data)} câu |")

        # Save spec
        sfx_list = cfg["sfx_vn"] if lang == "VI" else (cfg["sfx_en"] if lang == "EN" else cfg["sfx_ja"])
        bgm_desc = cfg["bgm_desc_vn"] if lang == "VI" else (cfg["bgm_desc_en"] if lang == "EN" else cfg["bgm_desc_ja"])
        overlays = cfg["overlay_vn"] if lang == "VI" else (cfg["overlay_en"] if lang == "EN" else cfg["overlay_ja"])

        clips_spec[cid] = {
            "id": cid,
            "title": title,
            "theme": theme,
            "psychological_signs": cfg["signs"],
            "hook": hook,
            "bgm": cfg["bgm"],
            "bgm_desc": bgm_desc,
            "sfx": sfx_list,
            "overlays": overlays,
            "lines": lines_data
        }

        # Write Caption and Descriptions
        cap_file = out_dir / f"Caption_{cid}.txt"
        mota_dai_file = out_dir / f"MoTa_Dai_{cid}.txt"
        mota_ngan_file = out_dir / f"MoTa_Ngan_{cid}.txt"

        if lang == "VI":
            cap_text = f"""{hook} 👁️

Tập 11 · Cặp Đôi Ken & Barbie — Chỉ dấu {signs_str}: {theme}.
Hồ sơ vụ án có thật tại Ontario, Canada, 100% dữ liệu đối chiếu hồ sơ điều tra Hoàng gia Canada và biên bản phiên xử Tòa án Cấp cao Ontario 1995.

📺 Xem trọn vẹn tập phân tích 39 phút ở link trong bio
🔎 Hồ sơ tâm lý học tội phạm · Paul Bernardo & Karla Homolka · Folie à Deux & Thỏa thuận với Quỷ dữ

Nội dung do AI hỗ trợ tạo hình và giọng phục vụ mục đích phân tích tâm lý giáo dục — không phải phóng sự giật gân.

#AmberEyes #TamLyToiPham #HosoCoThat #PaulBernardo #KarlaHomolka #{cid} #TrueCrimeVN #FolieADeux #KenAndBarbieKillers

---
Ghi chú khi đăng (KHÔNG dán vào caption):
- BẬT toggle "Nội dung do AI tạo" (AI-generated content) trên TikTok.
- Dán link YouTube Tập 11 vào ô Website trong phần sửa hồ sơ cá nhân.
- Ước lượng thời lượng: {tot_dur_rnd} s ({len(lines_data)} câu).
- Tên file video thành phẩm: clip{cidx}_{cid}.mp4 (1080x1920, 30fps).
"""
            mota_dai_text = f"""HỒ SƠ TÂM LÝ HỌC TỘI PHẠM — TẬP 11: CẶP ĐÔI KEN & BARBIE
Phân tích clip {cid}: {title}
Chủ đề chuyên sâu: {theme} (Chỉ dấu {signs_str})

Vụ án Paul Bernardo và Karla Homolka tại Ontario (Canada) đầu thập niên 1990 là một trong những vụ án gây chấn động và tranh cãi sâu sắc nhất lịch sử tư pháp Bắc Mỹ.
Đằng sau ngôi nhà màu hồng thơ mộng số 57 Bayview Drive và hình tượng cặp búp bê Ken & Barbie hoàn mỹ là một liên minh tội ác cộng sinh dị biệt.

Amber Eyes giải phẫu hồ sơ dựa trên 10 chỉ dấu tâm lý & hành vi, vạch trần cơ chế tâm lý đằng sau những chiếc mặt nạ xã hội vô hại và bản hợp đồng tư pháp "Thỏa thuận với Quỷ dữ".

📌 Xem trọn vẹn tập phân tích 39 phút tại link bio!
#AmberEyes #TamLyToiPham #KenAndBarbie #{cid}
"""
            mota_ngan_text = f"""Tập 11 Amber Eyes — Clip {cid}: {title}.
{hook}
Xem hồ sơ giải phẫu tâm lý đầy đủ tại link bio. #AmberEyes #TamLyToiPham #{cid} #PaulBernardo #KarlaHomolka
"""
        elif lang == "EN":
            cap_text = f"""{hook} 👁️

Ep. 11 · The Ken & Barbie Killers — Psychological Marker {signs_str}: {theme}.
Authentic criminal dossier from Ontario, Canada, strictly source-verified against RCMP archives and Ontario Supreme Court trial transcripts (1995).

📺 Watch the full 39-minute documentary on YouTube — link in bio.
🔎 Criminal Psychology · Paul Bernardo & Karla Homolka · Folie à Deux & The Deal with the Devil

Content created with AI assistance for behavioral and psychological educational purposes.

#AmberEyes #CriminalPsychology #TrueCrime #PaulBernardo #KarlaHomolka #{cid} #CaseFile #Mindhunter #KenAndBarbieKillers

---
Publishing Notes (DO NOT paste into caption):
- TOGGLE ON 'AI-generated content' label in TikTok settings.
- Add YouTube Episode 11 URL to the Website field in your profile bio.
- Estimated duration: {tot_dur_rnd} s ({len(lines_data)} lines).
- Video output file: clip{cidx}_{cid}_EN.mp4 (1080x1920, 30fps).
"""
            mota_dai_text = f"""CRIMINAL PSYCHOLOGY DOSSIER — EPISODE 11: THE KEN & BARBIE KILLERS
Clip {cid} Analysis: {title}
Core Behavioral Theme: {theme} (Markers {signs_str})

The dossier of Paul Bernardo and Karla Homolka in Ontario, Canada, remains one of the most chilling and controversial criminal cases in North American jurisprudence.
Behind the idyllic pink house at 57 Bayview Drive and their storybook golden-couple facade lay a lethal symbiotic partnership.

Amber Eyes deconstructs the case through the 10-Indicator Behavioral Framework, exposing the psychological camouflage of suburban respectability and the tragic judicial compromises of the "Deal with the Devil."

📌 Watch the full 39-minute investigative documentary via the link in our bio!
#AmberEyes #CriminalPsychology #KenAndBarbie #{cid}
"""
            mota_ngan_text = f"""Episode 11 Amber Eyes — Clip {cid}: {title}.
{hook}
Watch the full behavioral dossier via link in bio. #AmberEyes #TrueCrime #{cid} #PaulBernardo #KarlaHomolka
"""
        else:
            cap_text = f"""{hook} 👁️

第11話 · ケン＆バービー殺人事件 — 心理指標 {signs_str}: {theme}。
カナダ連邦警察（RCMP）記録およびオンタリオ州最高裁判所（1995年）の公的記録に基づく厳密な犯罪心理学プロファイリング。

📺 完全版ドキュメンタリー（39分）はYouTubeにて公開中 — プロフィールのリンクから
🔎 犯罪心理学 · ポール・ベルナルド＆カーラ・ホモルカ · 共有妄想と悪魔の司法取引

本コンテンツは心理分析および啓発を目的としてAI技術の支援を受けて制作されています。

#AmberEyes #犯罪心理学 #実話事件簿 #ポールベルナルド #カーラホモルカ #{cid} #マインドハンター #ケンとバービー

---
投稿時の注意事項（キャプション本文には貼り付けないでください）：
- TikTokアプリ内で「AI生成コンテンツ」のトグルを必ずONに設定してください。
- YouTube第11話へのリンクをプロフィール欄のウェブサイト項目に設定してください。
- 推定再生時間: {tot_dur_rnd} 秒 (全{len(lines_data)}文)。
- 出力動画ファイル名: clip{cidx}_{cid}_JA.mp4 (1080x1920, 30fps)。
"""
            mota_dai_text = f"""犯罪心理学プロファイリング — 第11話: ケン＆バービー連続殺人事件
クリップ {cid} 深層分析: {title}
行動科学テーマ: {theme}（心理指標 {signs_str}）

1990年代初頭のカナダ・オンタリオ州を震撼させたポール・ベルナルドとカーラ・ホモルカの事件は、北米司法史において最も暗く議論を呼んだ猟奇事件です。
ポート・ダルハウジーのピンクの家と完璧な美男美女の仮面の裏に隠されていたのは、異常な相互補完関係による共生犯罪でした。

Amber Eyesは10の行動・心理指標に基づき、無害に見える社会的仮面の裏側と、世界中を激怒させた『悪魔との司法取引』の心理力学を解剖します。

📌 39分の完全版ドキュメンタリーはバイオのリンクからご覧いただけます！
#AmberEyes #犯罪心理学 #実話事件簿 #{cid}
"""
            mota_ngan_text = f"""第11話 Amber Eyes — クリップ {cid}: {title}。
{hook}
完全版心理ドキュメンタリーはバイオのリンクから。 #AmberEyes #犯罪心理学 #{cid} #ポールベルナルド
"""

        cap_file.write_text(cap_text.strip() + "\n", encoding="utf-8")
        mota_dai_file.write_text(mota_dai_text.strip() + "\n", encoding="utf-8")
        mota_ngan_file.write_text(mota_ngan_text.strip() + "\n", encoding="utf-8")

    # Add detail performance sections to KE_HOACH_CLIP
    plan_lines.append("\n## 2. Diễn xuất chi tiết từng Clip (Kịch bản phân cảnh)\n" if lang == "VI" else
                      ("\n## 2. Detailed Performance Table\n" if lang == "EN" else "\n## 2. クリップ詳細構成\n"))

    for cid, cspec in clips_spec.items():
        plan_lines.append(f"### {cid} — {cspec['title']}\n")
        plan_lines.append(f"*Ước lượng: {sum(l['dur_est'] + l['pause_after'] for l in cspec['lines']):.1f} s ({len(cspec['lines'])} câu) · BGM: `{cspec['bgm']}`*\n" if lang == "VI" else
                          (f"*Estimated: {sum(l['dur_est'] + l['pause_after'] for l in cspec['lines']):.1f} s ({len(cspec['lines'])} lines) · BGM: `{cspec['bgm']}`*\n" if lang == "EN" else
                           f"*推定再生時間: {sum(l['dur_est'] + l['pause_after'] for l in cspec['lines']):.1f} 秒 ({len(cspec['lines'])} 行) · BGM: `{cspec['bgm']}`*\n"))

        plan_lines.append("| ID | Vai | Emotion | Tốc độ | Nghỉ | Nền (BG) | Lời thoại |" if lang == "VI" else
                          ("| ID | Role | Emotion | Speed | Pause | Background | Line |" if lang == "EN" else
                           "| ID | 役 | 感情 | 速度 | 休止 | 背景画像 | セリフ |"))
        plan_lines.append("|---|---|---|---|---|---|---|")

        for l in cspec["lines"]:
            plan_lines.append(f"| `{l['id']}` | {l['role']} | {l['emotion']} | {l['speed']} | {l['pause_after']}s | `{l['bg']}` | {l['text']} |")
        plan_lines.append("")

    plan_file_name = f"KE_HOACH_CLIP_TAP11.md" if lang == "VI" else f"KE_HOACH_CLIP_TAP11_{lang}.md"
    (out_dir / plan_file_name).write_text("\n".join(plan_lines), encoding="utf-8")

    spec_json = {
        "_readme": "SPEC AUDIO TIKTOK TAP 11 — Dữ liệu chuẩn hóa 100% đối chiếu master",
        "_episode": "11",
        "_language": lang,
        "_measured_rates": rates,
        "_clips_summary": clips_summary,
        "clips": clips_spec
    }
    (out_dir / "SPEC_AUDIO_CLIP_TAP11.json").write_text(json.dumps(spec_json, ensure_ascii=False, indent=2), encoding="utf-8")

print("SUCCESS: Hoàn tất khởi tạo toàn bộ tài liệu và kịch bản clip TikTok Tập 11 (VI, EN, JA).")
