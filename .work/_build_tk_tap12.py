# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 12 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap12/KE_HOACH_CLIP_TAP12.md
  02_SAN_XUAT/TIKTOK/Tap12/SPEC_AUDIO_CLIP_TAP12.json
  02_SAN_XUAT/TIKTOK/Tap12/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap12/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap12/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap12_EN/KE_HOACH_CLIP_TAP12_EN.md
  02_SAN_XUAT/TIKTOK/Tap12_EN/SPEC_AUDIO_CLIP_TAP12.json
  02_SAN_XUAT/TIKTOK/Tap12_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap12_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap12_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap12_JA/KE_HOACH_CLIP_TAP12_JA.md
  02_SAN_XUAT/TIKTOK/Tap12_JA/SPEC_AUDIO_CLIP_TAP12.json
  02_SAN_XUAT/TIKTOK/Tap12_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap12_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap12_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 12:
- timeline_s_t12.json (VI)
- timeline_s_EN_t12.json (EN)
- timeline_s_JA_t12.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap12"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap12_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap12_JA"

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
# 0. TỶ LỆ ĐỌC THẬT (Đo từ master Tập 12)
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

RATE_VI = get_rates("timeline_s_t12.json", is_ja=False)
RATE_EN = get_rates("timeline_s_EN_t12.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t12.json", is_ja=True)

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

MAP_VI = load_script_map("script_tap12.json")
MAP_EN = load_script_map("script_tap12_EN.json")
MAP_JA = load_script_map("script_tap12_JA.json")

# ----------------------------------------------------------------------------
# 2. KHAI BÁO 5 CLIP TẬP 12 (BẢN VI, EN, JA)
# ----------------------------------------------------------------------------
CLIPS_CONFIG = [
    {
        "id": "TK1",
        "title_vn": "Vỏ bọc Bác ái và Điểm mù Chính trị của Peoples Temple",
        "title_en": "Charitable Illusion & Political Blind Spots of Peoples Temple",
        "title_ja": "慈善の仮面と人民寺院の政治的盲点",
        "signs": [1, 9],
        "theme_vn": "Hiệu ứng Hào quang (Halo Effect) & Điểm mù Chính trị (Political Blind Spot)",
        "theme_en": "The Halo Effect & Political Blind Spots",
        "theme_ja": "ハロー効果と政治的盲点",
        "hook_vn": "Nhận nuôi trẻ em đa chủng tộc, mở bếp ăn từ thiện. Tại sao cả xã hội bị ru ngủ?",
        "hook_en": "Rainbow family, soup kitchens, political alliances. Why was an entire city completely blinded?",
        "hook_ja": "人種融和の理想郷、慈善活動の英雄。なぜ社会全体が完璧に欺かれたのか？",
        "bgm": "bgm_cello_sad.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_cello_sad.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_cello_sad.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_cello_sad.mp3",
        "sfx_vn": ["amb_wind_cold.wav (nền)", "fx_crowd_applause.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_wind_cold.wav (bed)", "fx_crowd_applause.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_wind_cold.wav（環境音）", "fx_crowd_applause.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "HỒ SƠ PEOPLES TEMPLE · SAN FRANCISCO THẬP NIÊN 1970", "dur_s": 3.0},
            {"sau_cau": "TK1.01#3", "text": "CHỦ TỊCH ỦY BAN NHÀ Ở SAN FRANCISCO", "dur_s": 2.5},
            {"sau_cau": "TK1.01#4", "text": "HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ CHÍNH TRỊ", "dur_s": 2.5},
            {"sau_cau": "TK1.01#6", "text": "TÊ LIỆT GIÁM SÁT TRƯỚC SỨC ÉP DƯ LUẬN", "dur_s": 2.5},
            {"sau_cau": "TK1.01#7", "text": "BỨC RÈM TỪ THIỆN CHE GIẤU ĐẾ CHẾ ĐỘC TÀI", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "PEOPLES TEMPLE · SAN FRANCISCO 1970S", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "CHAIRMAN OF SF HOUSING AUTHORITY", "dur_s": 2.5},
            {"after_id": "TK1.01#4", "text": "HALO EFFECT & POLITICAL BLIND SPOTS", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "OVERSIGHT PARALYZED BY FEAR OF BACKLASH", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "CHARITABLE MASK HIDING TOTALITARIAN EMPIRE", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "人民寺院ファイル · 1970年代サンフランシスコ", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "サンフランシスコ住宅局長の公職", "dur_s": 2.5},
            {"after_id": "TK1.01#4", "text": "ハロー効果と政治的盲点の形成", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "社会的反発を恐れて麻痺した法執行機関", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "慈善のヴェールの裏の全体主義的支配", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("1.04#3", "neutral", -0.02, 0.6, "t12_racial_harmony_facade", "still"),
            ("1.04#4", "neutral", -0.02, 0.6, "t12_racial_harmony_facade", "pan"),
            ("1.04#6", "neutral", -0.02, 0.6, "t12_charity_soup_kitchen_bread", "push"),
            ("1.04#7", "neutral", -0.02, 0.6, "t12_san_francisco_temple_expansion", "still"),
            ("1.04#8", "neutral", -0.02, 0.6, "t12_san_francisco_temple_expansion", "pan"),
            ("1.04#10", "neutral", -0.02, 0.6, "t12_city_hall_political_alliances", "push"),
            ("1.06#1", "neutral", -0.02, 0.0, "t12_iron_fist_behind_velvet_curtain", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Thiên đường Rừng sâu hay Trại giam Tâm lý Khép kín?",
        "title_en": "Jungle Paradise or Closed Psychological Prison?",
        "title_ja": "密林の楽園か、それとも閉鎖された心理的監獄か？",
        "signs": [2, 3],
        "theme_vn": "Cơ chế Tách rời Thực tại & Phá hủy Liên kết Thân tộc (Social Isolation & Family Severing)",
        "theme_en": "Social Isolation & Familial Severing",
        "theme_ja": "現実からの隔離と家族解体による絶対支配",
        "hook_vn": "Bán hết nhà cửa, giao nộp hộ chiếu. Khi thiên đường hóa thành chiếc lồng giam không lối thoát.",
        "hook_en": "Homes sold, passports confiscated. When paradise turned into an inescapable jungle cage.",
        "hook_ja": "財産を売り払い、旅券を没収される。約束の地が逃げ場なき牢獄と化した瞬間。",
        "bgm": "bgm_ambient_deep.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_ambient_deep.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_ambient_deep.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_ambient_deep.mp3",
        "sfx_vn": ["amb_jungle_insects.wav (nền)", "fx_trunk_lock.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_jungle_insects.wav (bed)", "fx_trunk_lock.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_jungle_insects.wav（環境音）", "fx_trunk_lock.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "THANH LỌC TÂM TRÍ: CƯỠNG BỨC SỈ NHỤC CÔNG KHAI", "dur_s": 2.5},
            {"sau_cau": "TK2.01#3", "text": "TƯỚC ĐOẠT TÀI SẢN · CẮT ĐỨT HỖ TRỢ THÂN TỘC", "dur_s": 2.5},
            {"sau_cau": "TK2.01#5", "text": "THU GIỮ TOÀN BỘ HỘ CHIẾU VÀ TIỀN BẠC TẠI CỔNG VÀO", "dur_s": 3.0},
            {"sau_cau": "TK2.01#7", "text": "HỌNG SÚNG AN NINH BAO VÂY 24/7", "dur_s": 2.5},
            {"sau_cau": "TK2.01#8", "text": "TRỰC GIÁC BÁO ĐỘNG CỦA NGƯỜI MẸ TRẺ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "CATHARSIS SESSIONS: FORCED PUBLIC HUMILIATION", "dur_s": 2.5},
            {"after_id": "TK2.01#3", "text": "ASSETS CONFISCATED · FAMILIES TORN APART", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "PASSPORTS & MONEY SEIZED AT GATES", "dur_s": 3.0},
            {"after_id": "TK2.01#7", "text": "ARMED PATROLS ENFORCING TOTAL ISOLATION", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "A MOTHER'S DESPERATE INTUITION TO ESCAPE", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "精神浄化：公衆の面前での強制侮辱", "dur_s": 2.5},
            {"after_id": "TK2.01#3", "text": "全財産の没収と血縁ネットワークの解体", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "到着と同時に没収されたパスポートと所持金", "dur_s": 3.0},
            {"after_id": "TK2.01#7", "text": "脱走を阻む武装警備隊の24時間警戒", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "母親としての直感と脱出への決意", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("1.06#2", "neutral", -0.02, 0.6, "t12_iron_fist_behind_velvet_curtain", "pan"),
            ("1.06#4", "neutral", -0.02, 0.6, "t12_catharsis_session_interrogation", "push"),
            ("1.06#5", "neutral", -0.02, 0.6, "t12_property_surrender_passbooks", "still"),
            ("1.07#1", "neutral", -0.02, 0.6, "t12_utopian_promise_mirage", "still"),
            ("1.07#3", "neutral", -0.02, 0.6, "t12_confiscated_passports_trunk", "pull"),
            ("1.07#4", "neutral", -0.02, 0.6, "t12_confiscated_passports_trunk", "push"),
            ("1.07#5", "neutral", -0.02, 0.6, "t12_equatorial_forced_labor_fields", "still"),
            ("1.07#8", "sad", -0.04, 0.0, "t12_inescapable_labor_camp_cage", "push")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Tư duy Tập thể (Groupthink) & Bẫy Tâm lý Milgram",
        "title_en": "Groupthink & The Milgram Obedience Trap",
        "title_ja": "集団浅慮（グループシンク）とミルグラム服従の罠",
        "signs": [6, 8],
        "theme_vn": "Sự Phục tùng Quyền lực (Milgram Paradigm) & Tư duy Tập thể (Groupthink - Irving Janis)",
        "theme_en": "Obedience to Authority & Groupthink",
        "theme_ja": "権威への服従実験と集団浅慮の認知トラップ",
        "hook_vn": "Tại sao 918 con người cùng bước vào chỗ chết mà không phản kháng? Bí ẩn tâm lý học bầy đàn.",
        "hook_en": "Why did 918 people walk into destruction without mass revolt? The anatomy of group obedience.",
        "hook_ja": "なぜ918人もの人間が抵抗せず破滅へ向かったのか？ 群集心理の暗黒メカニズム。",
        "bgm": "bgm_piano_minimal.mp3",
        "bgm_desc_vn": "Hồi 3 — bed tập: bgm_piano_minimal.mp3",
        "bgm_desc_en": "Act 3 — episode bed: bgm_piano_minimal.mp3",
        "bgm_desc_ja": "第3幕 — 本編BGM: bgm_piano_minimal.mp3",
        "sfx_vn": ["amb_room_tone.wav (nền)", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_tone.wav (bed)", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_tone.wav（環境音）", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "CÂU HỎI LỚN NHẤT CỦA THẢM KỊCH: TẠI SAO?", "dur_s": 2.5},
            {"sau_cau": "TK3.01#3", "text": "THÍ NGHIỆM MILGRAM: CHUYỂN GIAO TRÁCH NHIỆM ĐẠO ĐỨC", "dur_s": 3.0},
            {"sau_cau": "TK3.01#5", "text": "IRVING JANIS: HIỆN TƯỢNG TƯ DUY TẬP THỂ (GROUPTHINK)", "dur_s": 3.0},
            {"sau_cau": "TK3.01#7", "text": "KỸ THUẬT LEO THANG CAM KẾT (FOOT-IN-THE-DOOR)", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "CHIẾC BẪY TỰ NGUYỆN MÙ QUÁNG HOÀN HẢO", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "THE ULTIMATE QUESTION: WHY DID IT HAPPEN?", "dur_s": 2.5},
            {"after_id": "TK3.01#3", "text": "MILGRAM EXPERIMENT: SURRENDERING MORAL AGENCY", "dur_s": 3.0},
            {"after_id": "TK3.01#5", "text": "IRVING JANIS: GROUPTHINK DYSFUNCTION", "dur_s": 3.0},
            {"after_id": "TK3.01#7", "text": "FOOT-IN-THE-DOOR: ESCALATING COMMITMENT", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "THE PERFECT TRAP OF VOLUNTARY BLINDNESS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "最大の疑問：なぜ抵抗なく従ったのか？", "dur_s": 2.5},
            {"after_id": "TK3.01#3", "text": "ミルグラム実験：道徳的責任の権威への委譲", "dur_s": 3.0},
            {"after_id": "TK3.01#5", "text": "アーヴィング・ジャニス：集団浅慮（グループシンク）", "dur_s": 3.0},
            {"after_id": "TK3.01#7", "text": "フット・イン・ザ・ドア：コミットメントのエスカレーション", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "自発的盲従を生み出す完全な心理的罠", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("3.02#1", "neutral", -0.02, 0.5, "t12_unanswered_question_diorama", "pan"),
            ("3.03#1", "neutral", -0.02, 0.5, "t12_milgram_experiment_shock_generator", "push"),
            ("3.03#2", "neutral", -0.02, 0.5, "t12_milgram_experiment_shock_generator", "still"),
            ("3.04#1", "neutral", -0.02, 0.5, "t12_groupthink_hostile_mob_shadows", "still"),
            ("3.05#1", "neutral", -0.02, 0.5, "t12_cognitive_dissonance_scales", "pull"),
            ("3.05#2", "neutral", -0.02, 0.5, "t12_cognitive_dissonance_scales", "push"),
            ("3.05#4", "neutral", -0.02, 0.5, "t12_closed_circle_of_stools", "pan"),
            ("3.05#13", "neutral", -0.02, 0.0, "t12_staircase_into_blackness", "pull")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Cuộn băng Tử thần Q 042 & Tiếng nói Phản kháng Đơn độc",
        "title_en": "Death Tape Q 042 & The Solitary Voice of Defiance",
        "title_ja": "死のテープQ042と孤立した抵抗の声",
        "signs": [4, 5],
        "theme_vn": "Hệ thống Tự bào chữa (Sykes & Matza) & Lương tri Độc lập (Independent Conscience)",
        "theme_en": "Neutralization Theory & Independent Conscience",
        "theme_ja": "中和の技術（自己正当化）と孤立した独立良心の勇気",
        "hook_vn": "Băng cassette giải mật 44 phút của FBI. Người phụ nữ duy nhất dám đứng lên chất vấn giáo chủ.",
        "hook_en": "The FBI's 44-minute declassified death tape. The lone woman who stood up to question the leader.",
        "hook_ja": "FBI機密解除テープQ042・44分間の肉声。教祖に立ち向かった唯一の女性。",
        "bgm": "bgm_violin_heart.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_violin_heart.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_violin_heart.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_violin_heart.mp3",
        "sfx_vn": ["amb_tape_hiss.wav (nền)", "fx_cassette_play.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_tape_hiss.wav (bed)", "fx_cassette_play.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_tape_hiss.wav（環境音）", "fx_cassette_play.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "CUỘN BĂNG TỬ THẦN Q 042 · TƯ LIỆU GIẢI MẬT FBI", "dur_s": 3.0},
            {"sau_cau": "TK4.01#2", "text": "44 PHÚT GHI ÂM BUỔI CHIỀU ĐỊNH MỆNH 18/11/1978", "dur_s": 2.5},
            {"sau_cau": "TK4.01#4", "text": "BÀ CHRISTINE MILLER (60 TUỔI): ĐỨNG LÊN CHẤT VẤN", "dur_s": 3.0},
            {"sau_cau": "TK4.01#6", "text": "“CHỪNG NÀO CÒN CÓ SỰ SỐNG, CHÚNG TA VẪN CÒN HY VỌNG”", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "LƯƠNG TRI ĐỘC LẬP BẢO VỆ MẦM SỐNG", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "FBI DECLASSIFIED EVIDENCE: DEATH TAPE Q 042", "dur_s": 3.0},
            {"after_id": "TK4.01#2", "text": "44 MINUTES OF CHILLING HISTORICAL RECORDING", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "CHRISTINE MILLER (AGE 60): THE LONE DEFENDER", "dur_s": 3.0},
            {"after_id": "TK4.01#6", "text": "“AS LONG AS THERE’S LIFE, THERE’S HOPE”", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "INDEPENDENT CONSCIENCE DEFENDING INNOCENCE", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "FBI機密解除証拠：死のテープQ042", "dur_s": 3.0},
            {"after_id": "TK4.01#2", "text": "1978年11月18日の真実を刻む44分間の生録音", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "クリスティーン・ミラー（60歳）：たった一人の抵抗", "dur_s": 3.0},
            {"after_id": "TK4.01#6", "text": "「命がある限り、人間にはまだ希望があるはず」", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "子どもたちの命を守ろうとした独立した良心", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("2.11#1", "neutral", -0.02, 0.6, "t12_knife_attack_scuffle_pavilion", "pull"),
            ("2.11#2", "neutral", -0.02, 0.6, "t12_knife_attack_scuffle_pavilion", "push"),
            ("2.11#3", "neutral", -0.02, 0.6, "t12_old_radio_receiver_dark", "still"),
            ("4.04#1", "neutral", -0.02, 0.6, "t12_miller_silhouette_at_microphone", "pull"),
            ("4.04#2", "neutral", -0.02, 0.6, "t12_miller_silhouette_at_microphone", "push"),
            ("4.04#3", "fearful", -0.03, 0.6, "t12_empty_microphone_after_crowd", "still"),
            ("4.06#1", "neutral", -0.02, 0.6, "t12_raised_fist_behind_microphone", "still"),
            ("4.07#5", "neutral", -0.02, 0.0, "t12_brass_compass_on_bare_table", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Nạn nhân học & 4 Cảnh báo Đỏ Sinh tồn",
        "title_en": "Victimology & 4 Survival Red Flags",
        "title_ja": "被害者学と生き残るための4つの危険信号",
        "signs": [10],
        "theme_vn": "Nạn nhân học (Victimology) & 4 Dấu hiệu Cảnh báo Đỏ Sinh tồn (The Gift of Fear)",
        "theme_en": "Victimology & 4 Survival Red Flags",
        "theme_ja": "被害者学と生存のための4つの警告サイン",
        "hook_vn": "Bốn tín hiệu cảnh báo đỏ để không bao giờ rơi vào chiếc bẫy thao túng tâm lý cực đoan.",
        "hook_en": "Four psychological red flags to never fall prey to coercive mind control.",
        "hook_ja": "破壊的カルトや心理操作の罠から命を守る「4つの危険信号」。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_room_tone.wav (nền)", "fx_page_turn.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_tone.wav (bed)", "fx_page_turn.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_tone.wav（環境音）", "fx_page_turn.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 CẢNH BÁO ĐỎ SINH TỒN · THE GIFT OF FEAR", "dur_s": 2.5},
            {"sau_cau": "TK5.01#2", "text": "CẢNH BÁO 1: CÔ LẬP KHỎI MẠNG LƯỚI XÃ HỘI", "dur_s": 2.5},
            {"sau_cau": "TK5.01#4", "text": "CẢNH BÁO 2: TƯỚC ĐOẠT TÀI CHÍNH & TỰ CHỦ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#6", "text": "CẢNH BÁO 3: LÀM SUY KIỆT THỂ CHẤT ĐỂ TRIỆT TIÊU PHẢN BIỆN", "dur_s": 2.5},
            {"sau_cau": "TK5.01#8", "text": "CẢNH BÁO 4: THẦN THÁNH HÓA THỦ LĨNH & CẤM HOÀI NGHI", "dur_s": 2.5},
            {"sau_cau": "TK5.01#10", "text": "TRỰC GIÁC BẤT AN LÀ MÓN QUÀ SINH TỒN QUÝ GIÁ NHẤT", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "4 SURVIVAL RED FLAGS · THE GIFT OF FEAR", "dur_s": 2.5},
            {"after_id": "TK5.01#2", "text": "FLAG 1: TOTAL SOCIAL ISOLATION", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "FLAG 2: FINANCIAL CONTROL & ASSET SEIZURE", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "FLAG 3: PHYSICAL EXHAUSTION CRUSHING REASON", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "FLAG 4: DEIFICATION OF LEADER & DISSENT FORBIDDEN", "dur_s": 2.5},
            {"after_id": "TK5.01#10", "text": "INTUITION IS HUMANITY'S GREATEST SURVIVAL GIFT", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "生き残るための4つの危険信号 · 理性と直感", "dur_s": 2.5},
            {"after_id": "TK5.01#2", "text": "第1の警告：外部社会・親族からの完全な孤立化", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "第2の警告：経済的支配と身分証明書類の没収", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "第3の警告：過労と睡眠遮断による批判的思考の破壊", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "第4の警告：指導者の絶対神格化と疑問の断罪", "dur_s": 2.5},
            {"after_id": "TK5.01#10", "text": "違和感を覚える直感こそ最大の生存能力である", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("5.05#1", "neutral", -0.02, 0.5, "t12_amber_eyes_closing_dossier_jonestown", "pan"),
            ("5.05#2", "neutral", -0.02, 0.4, "t12_redflag1_total_social_isolation", "pull"),
            ("5.05#4", "neutral", -0.02, 0.5, "t12_redflag2_silenced_critical_thinking", "still"),
            ("5.05#5", "neutral", -0.02, 0.4, "t12_redflag3_escalating_commitment_trap", "pan"),
            ("5.05#7", "neutral", -0.02, 0.5, "t12_empty_trunk_open_padlock", "push"),
            ("5.05#8", "neutral", -0.02, 0.4, "t12_exhausted_worker_hut_wall", "still"),
            ("5.05#10", "neutral", -0.02, 0.5, "t12_sleep_deprived_bare_bunk", "pull"),
            ("5.05#11", "neutral", -0.02, 0.4, "t12_redflag4_fortress_paranoia_wall", "push"),
            ("5.05#13", "neutral", -0.02, 0.5, "t12_paranoia_wall_coiled_wire", "pan"),
            ("5.05#15", "neutral", -0.02, 0.0, "t12_instinct_bent_branch_path", "push")
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
        "VI": '# KẾ HOẠCH CLIP TIKTOK — TẬP 12 · "THẢM KỊCH JONESTOWN (JIM JONES & PEOPLES TEMPLE)"',
        "EN": '# TIKTOK CLIPS PLAN — EPISODE 12 · "JONESTOWN TRAGEDY (JIM JONES & PEOPLES TEMPLE)"',
        "JA": '# TIKTOKクリップ計画 — 第12話 ·「ジョーンズタウンの悲劇（ジム・ジョーンズと人民寺院）」'
    }[lang_code]

    plan_lines.append(plan_header_title)
    plan_lines.append("")
    plan_lines.append(f"*Ngôn ngữ: **{lang_code}** · Nguồn dữ liệu: master Tập 12 · Tỷ lệ đọc ASR thật.*")
    plan_lines.append("*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md`.*")
    plan_lines.append("")
    plan_lines.append("---")
    plan_lines.append("")
    plan_lines.append("## 0. Tóm tắt 5 clip và thời lượng đo lường")
    plan_lines.append("")
    plan_lines.append("| Clip | Chỉ dấu (K10) | Chủ đề | Hook mở đầu (0–3 s) | Ước lượng thời lượng |")
    plan_lines.append("|---|---|---|---|---|")

    # Pass 1: tính thời lượng và tóm tắt
    durations = {}
    clip_lines_data = {}

    # Helper field access
    def get_field(cfg, prefix):
        key = f"{prefix}_vn" if lang_code == "VI" else f"{prefix}_{lang_code.lower()}"
        return cfg[key]

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

    # Ghi file KE_HOACH_CLIP_TAP12
    plan_filename = f"KE_HOACH_CLIP_TAP12{'' if lang_code == 'VI' else '_' + lang_code}.md"
    (out_dir / plan_filename).write_text("\n".join(plan_lines), encoding="utf-8")

    # Ghi file SPEC_AUDIO_CLIP_TAP12.json
    (out_dir / "SPEC_AUDIO_CLIP_TAP12.json").write_text(json.dumps(spec_audio, ensure_ascii=False, indent=2), encoding="utf-8")

    # Sinh Caption, MoTa_Dai, MoTa_Ngan
    for cfg in CLIPS_CONFIG:
        cid = cfg["id"]
        title_c = get_field(cfg, "title")
        hook_c = get_field(cfg, "hook")
        theme_c = get_field(cfg, "theme")

        if lang_code == "VI":
            caption = f"{hook_c}\n\nGiải mã tâm lý học tội phạm Tập 12: Thảm kịch Jonestown và Cuộn băng tử thần Q 042.\nXem hồ sơ đầy đủ 34 phút trên kênh YouTube Amber Eyes (link ở bio)!\n\n#ambereyes #tamlyhoctoipham #jonestown #jimjones #groupthink #thegiftoffear #vuanhothat #kienthuc"
            mota_ngan = f"{title_c} — Hồ sơ Jonestown (Tập 12 Amber Eyes). Xem trọn bộ tại link bio!"
            mota_dai = f"HỒ SƠ TẬP 12: THẢM KỊCH JONESTOWN — JIM JONES & PEOPLES TEMPLE\n\nPhần trích đoạn: {title_c}\nChủ đề: {theme_c}\n\nVào ngày 18/11/1978, thảm kịch Jonestown đã cướp đi 918 sinh mạng vô tội sâu trong rừng nhiệt đới Guyana. Kênh Amber Eyes giải mã toàn diện các cơ chế thao túng tâm lý bầy đàn, sự phục tùng quyền lực mù quáng và 4 tín hiệu cảnh báo đỏ sinh tồn giúp bạn bảo vệ bản thân trong cuộc sống hiện đại.\n\nXem bản phân tích podcast tài liệu hoàn chỉnh (34 phút) trên YouTube Amber Eyes.\nLink xem video đầy đủ tại phần tiểu sử (bio) của kênh!"
        elif lang_code == "EN":
            caption = f"{hook_c}\n\nCriminal Psychology Dossier Ep 12: The Jonestown Tragedy & Declassified Death Tape Q 042.\nWatch the full 34-min documentary on Amber Eyes YouTube channel (link in bio)!\n\n#ambereyes #criminalpsychology #jonestown #jimjones #groupthink #thegiftoffear #truecrime #mindcontrol"
            mota_ngan = f"{title_c} — Jonestown Dossier (Ep 12 Amber Eyes). Watch full episode in bio link!"
            mota_dai = f"DOSSIER EPISODE 12: THE JONESTOWN TRAGEDY — JIM JONES & PEOPLES TEMPLE\n\nClip Segment: {title_c}\nTheme: {theme_c}\n\nOn November 18, 1978, 918 lives were lost in the remote jungle of Guyana. Amber Eyes dissects the chilling mechanics of cult mind control, destructive groupthink, and 4 vital survival red flags to protect yourself and your loved ones.\n\nWatch the full 34-minute documentary podcast on Amber Eyes YouTube.\nFull video link available in channel bio!"
        elif lang_code == "JA":
            caption = f"{hook_c}\n\n犯罪心理学ファイル第12話：ジョーンズタウンの悲劇とFBI機密解除死のテープQ042。\n34分間の完全版ドキュメンタリーはYouTube公式チャンネル「Amber Eyes」で公開中（プロフ欄リンクへ）！\n\n#ambereyes #犯罪心理学 #ジョーンズタウン #洗脳 #マインドコントロール #集団浅慮 #未解決事件 #実話"
            mota_ngan = f"{title_c} — ジョーンズタウン事件（第12話 Amber Eyes）。完全版はプロフ欄リンクから！"
            mota_dai = f"事件ファイル第12話：ジョーンズタウンの悲劇 — ジム・ジョーンズと人民寺院\n\nクリップ抜粋：{title_c}\nテーマ：{theme_c}\n\n1978年11月18日、ガイアナの密林で918人の命が失われた未曾有の悲劇。Amber Eyesは、権威への盲従、集団浅慮、そして現代社会を生き抜くための「4つの危険信号」を心理学的に徹底解剖します。\n\n本編34分間の完全版ドキュメンタリーはYouTube「Amber Eyes」にて公開中。\nプロフィール欄のリンクからぜひご視聴ください！"

        (out_dir / f"Caption_{cid}.txt").write_text(caption, encoding="utf-8")
        (out_dir / f"MoTa_Ngan_{cid}.txt").write_text(mota_ngan, encoding="utf-8")
        (out_dir / f"MoTa_Dai_{cid}.txt").write_text(mota_dai, encoding="utf-8")

    print(f"[{lang_code}] Successfully generated all files in {out_dir}")
    for cid, d in durations.items():
        print(f"  {cid}: {d}s")

if __name__ == "__main__":
    for code in ["VI", "EN", "JA"]:
        build_lang_artifacts(code)
