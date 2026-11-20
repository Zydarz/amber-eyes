# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 04 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap04/KE_HOACH_CLIP_TAP04.md
  02_SAN_XUAT/TIKTOK/Tap04/SPEC_AUDIO_CLIP_TAP04.json
  02_SAN_XUAT/TIKTOK/Tap04/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap04/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap04/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap04_EN/KE_HOACH_CLIP_TAP04_EN.md
  02_SAN_XUAT/TIKTOK/Tap04_EN/SPEC_AUDIO_CLIP_TAP04.json
  02_SAN_XUAT/TIKTOK/Tap04_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap04_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap04_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap04_JA/KE_HOACH_CLIP_TAP04_JA.md
  02_SAN_XUAT/TIKTOK/Tap04_JA/SPEC_AUDIO_CLIP_TAP04.json
  02_SAN_XUAT/TIKTOK/Tap04_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap04_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap04_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỉ lệ đọc thực tế trên master Tập 04:
- timeline_s_t04.json (VI)
- timeline_s_EN_t04.json (EN)
- timeline_s_JA_t04.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_JA"

OUT_VI.mkdir(parents=True, exist_ok=True)
OUT_EN.mkdir(parents=True, exist_ok=True)
OUT_JA.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WORK))
try:
    from vi_cer import vi_numbers
except Exception:
    def vi_numbers(x): return x

# ----------------------------------------------------------------------------
# 0. TỈ LỆ ĐỌC THẬT (Tập 04 Master ASR)
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

RATE_VI = get_rates("timeline_s_t04.json", False)
RATE_EN = get_rates("timeline_s_EN_t04.json", False)
RATE_JA = get_rates("timeline_s_JA_t04.json", True)

VI_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_t04.json").open(encoding="utf-8"))["items"]}
EN_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_EN_t04.json").open(encoding="utf-8"))["items"]}
JA_MAP = {it["id"]: it["text"] for it in json.load((WORK / "timeline_s_JA_t04.json").open(encoding="utf-8"))["items"]}

# ----------------------------------------------------------------------------
# 1. ĐỊNH NGHĨA 5 CLIP TẬP 04
# ----------------------------------------------------------------------------
CLIPS_DEF = [
    {
        "id": "TK1",
        "title_vn": "Nấc thang hủy lệnh Pyxis và lỗ hổng chết người",
        "title_en": "The Pyxis Cancel Loophole & The Lethal Escalation",
        "title_ja": "薬剤分配機Pyxisのキャンセル抜け穴と致死のエスカレーション",
        "signs": [6, 7],
        "theme_vn": "Kẽ hở công nghệ máy phát thuốc Pyxis & Quỹ đạo leo thang của Thiên thần Tử thần",
        "theme_en": "Technological Vulnerability in Automated Dispensing & The Angel of Death Escalation",
        "theme_ja": "自動薬剤分配機の技術的脆弱性と「死の天使」のエスカレーション軌道",
        "hook_vn": "Nhập lệnh lấy thuốc độc. Rồi nhấn hủy chỉ sau một giây.",
        "hook_en": "Ordered lethal drugs. Then hit cancel one second later.",
        "hook_ja": "劇薬を出庫し、わずか1秒後に取り消しボタンを押す。",
        "bgm": "bgm_ambient_tension.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_ambient_tension.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_ambient_tension.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_ambient_tension.mp3",
        "sfx_vn": ["amb_sterile_night.wav (nền)", "fx_pyxis_keypad.wav", "fx_drawer_open.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_sterile_night.wav (bed)", "fx_pyxis_keypad.wav", "fx_drawer_open.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_sterile_night.wav（環境音）", "fx_pyxis_keypad.wav", "fx_drawer_open.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "MÁY PHÁT THUỐC TỰ ĐỘNG PYXIS MEDSTATION", "dur_s": 3.0},
            {"sau_cau": "TK1.01#4", "text": "LỖ HỔNG HỦY LỆNH: DIGOXIN & INSULIN BIẾN MẤT", "dur_s": 2.5},
            {"sau_cau": "TK1.01#6", "text": "GIAI ĐOẠN 4: MẤT KIỂM SOÁT HOÀN TOÀN", "dur_s": 2.5},
            {"sau_cau": "TK1.01#7", "text": "CHỮ KÝ TÂM LÝ: “PHỨC CẢM CHÚA TRỜI”", "dur_s": 2.5},
            {"sau_cau": "TK1.01#8", "text": "ẢO TƯỞNG TOÀN NĂNG ĐỨNG TRÊN SỐ PHẬN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "PYXIS MEDSTATION AUTOMATED CABINETS", "dur_s": 3.0},
            {"after_id": "TK1.01#4", "text": "CANCEL LOOPHOLE: DIGOXIN & INSULIN VANISH", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "STAGE 4: COMPLETE COLLAPSE OF INHIBITION", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "PSYCHOLOGICAL SIGNATURE: “GOD COMPLEX”", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "OMNIPOTENCE ILLUSION: ARBITER OF LIFE & DEATH", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "自動薬剤分配機「PYXIS MEDSTATION」", "dur_s": 3.0},
            {"after_id": "TK1.01#4", "text": "取り消し抜け穴：劇薬のアンプルが消える", "dur_s": 2.5},
            {"after_id": "TK1.01#6", "text": "第4段階：抑制の完全な崩壊と無差別標的", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "心理的シグネチャー：「神コンプレックス」", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "全能感の錯覚：生死を掌る支配者", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t4_pyxis_station", "still"),
            ("D", "2.06#1", "neutral", -0.03, 0.6, "t4_pyxis_station", "pull"),
            ("D", "2.06#3", "neutral", -0.03, 0.6, "t4_pyxis_station", "pan"),
            ("D", "2.06#4", "neutral", -0.03, 0.6, "t4_pyxis_drawer_ajar", "push"),
            ("D", "2.06#5", "neutral", -0.03, 0.7, "t4_pyxis_drawer_ajar", "still"),
            ("D", "2.06#14", "neutral", -0.03, 0.7, "t4_pyxis_printout", "push"),
            ("C", "2.08#5", "neutral", -0.02, 0.7, "t4_neutral_letter", "pull"),
            ("C", "2.11#7", "neutral", -0.02, 0.7, "t4_institutional_bystander", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t4_closing_desk", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Người đồng nghiệp mẫu mực và hiệu ứng hào quang chiếc áo blouse",
        "title_en": "The Model Colleague & The Halo Effect of the White Coat",
        "title_ja": "模範的同僚と白衣の「ハロー効果」",
        "signs": [9, 1],
        "theme_vn": "Hiệu ứng hào quang (Halo Effect) & Điểm mù xã hội trước kẻ săn mồi hiền lành",
        "theme_en": "Halo Effect & Collective Blind Spot Obscuring a Gentle Predator",
        "theme_ja": "ハロー効果（後光効果）と温厚な捕食者に対する集団的死角",
        "hook_vn": "Người y tá hiền lành nhất bệnh viện. Lại là kẻ sát nhân tàn khốc nhất.",
        "hook_en": "The gentlest nurse on the ward. And America’s most prolific killer.",
        "hook_ja": "病院で最も温厚だった看護師。その正体は、史上最悪の殺人鬼だった。",
        "bgm": "bgm_jazz_noir.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_jazz_noir.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_jazz_noir.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_jazz_noir.mp3",
        "sfx_vn": ["amb_hospital_night.wav (nền)", "fx_heart_monitor.wav", "fx_footsteps_hallway.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_hospital_night.wav (bed)", "fx_heart_monitor.wav", "fx_footsteps_hallway.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_hospital_night.wav（環境音）", "fx_heart_monitor.wav", "fx_footsteps_hallway.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "TRUNG TÂM Y TẾ SOMERSET · MÙA THU 2003", "dur_s": 3.0},
            {"sau_cau": "TK2.01#5", "text": "CHIẾC ÁO BLOUSE TRẮNG: HIỆU ỨNG HÀO QUANG", "dur_s": 2.5},
            {"sau_cau": "TK2.01#7", "text": "“CHARLIE LÀ NGƯỜI BẠN TUYỆT VỜI NHẤT”", "dur_s": 2.5},
            {"sau_cau": "TK2.01#9", "text": "LẠNH SỐNG LƯNG: LÀM VIỆC CẠNH ÁC QUỶ", "dur_s": 2.5},
            {"sau_cau": "TK2.01#10", "text": "CƠ CHẾ PHI NHÂN HÓA VÀ VẬT HÓA NẠN NHÂN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "SOMERSET MEDICAL CENTER · AUTUMN 2003", "dur_s": 3.0},
            {"after_id": "TK2.01#5", "text": "WHITE SCRUBS: THE LETHAL HALO EFFECT", "dur_s": 2.5},
            {"after_id": "TK2.01#7", "text": "“CHARLIE WAS AN INCREDIBLE FRIEND”", "dur_s": 2.5},
            {"after_id": "TK2.01#9", "text": "CHILL DOWN THE SPINE: WORKING BESIDE A MONSTER", "dur_s": 2.5},
            {"after_id": "TK2.01#10", "text": "OBJECTIFICATION & DEHUMANIZATION OF VICTIMS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "サマセット医療センター · 2003年秋", "dur_s": 3.0},
            {"after_id": "TK2.01#5", "text": "白衣の裏側：完全な「ハロー効果」", "dur_s": 2.5},
            {"after_id": "TK2.01#7", "text": "「CHARLIEは本当に素晴らしい友人でした」", "dur_s": 2.5},
            {"after_id": "TK2.01#9", "text": "背筋の凍る真実：殺人鬼のすぐ隣で勤務", "dur_s": 2.5},
            {"after_id": "TK2.01#10", "text": "被害者の「客体化」と非人間化の深淵", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t4_nurse_station", "still"),
            ("H", "1.03#1", "neutral", -0.02, 0.5, "t4_somerset_exterior", "pan"),
            ("H", "1.03#2", "neutral", -0.02, 0.6, "t4_somerset_exterior", "pull"),
            ("H", "1.03#4", "neutral", -0.02, 0.6, "t4_icu_night", "still"),
            ("H", "1.03#6", "neutral", -0.02, 0.6, "t4_cullen_silhouette", "push"),
            ("H", "1.05#2", "neutral", -0.02, 0.6, "t4_code_blue_aftermath", "pan"),
            ("N1", "1.07#1", "neutral", -0.02, 0.6, "t4_breakroom_night", "still"),
            ("N1", "1.07#2", "neutral", -0.02, 0.6, "t4_breakroom_night", "push"),
            ("N1", "1.07#5", "sad", -0.04, 0.7, "t4_corridor_shadow", "pull"),
            ("C", "2.11#1", "neutral", -0.02, 0.7, "t4_institutional_bystander", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t4_closing_desk", "still")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Nữ y tá mang máy nghe lén đối đầu bạn thân",
        "title_en": "The Wiretap Nurse & The Tense Diner Confrontation",
        "title_ja": "盗聴器を纏う看護師と緊迫のダイナー対峙",
        "signs": [6, 4],
        "theme_vn": "Điểm gãy tâm lý & Cuộc đối đầu sinh tử của Amy Loughren tại quán ăn",
        "theme_en": "Psychological Breaking Point & Amy Loughren’s Perilous Diner Operation",
        "theme_ja": "心理的限界点とエイミー・ローレンの命懸けのダイナー潜入作戦",
        "hook_vn": "Chiếc micro dưới áo khoác mùa đông. Và cuộc hẹn sinh tử tại quán ăn.",
        "hook_en": "A hidden wire beneath her winter coat. A deadly dinner with her best friend.",
        "hook_ja": "セーターの下の盗聴マイク。親友との命懸けのダイナー密会。",
        "bgm": "bgm_sub_drone.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_sub_drone.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_sub_drone.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_sub_drone.mp3",
        "sfx_vn": ["amb_diner_murmur.wav (nền)", "fx_wire_static.wav", "fx_coffee_cup.wav", "fx_heartbeat_tense.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_diner_murmur.wav (bed)", "fx_wire_static.wav", "fx_coffee_cup.wav", "fx_heartbeat_tense.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_diner_murmur.wav（環境音）", "fx_wire_static.wav", "fx_coffee_cup.wav", "fx_heartbeat_tense.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "CHIẾC MICRO DƯỚI ÁO KHOÁC MÙA ĐÔNG", "dur_s": 3.0},
            {"sau_cau": "TK3.01#4", "text": "MẸ ĐƠN THÂN VÀ CĂN BỆNH CƠ TIM NGUY HIỂM", "dur_s": 2.5},
            {"sau_cau": "TK3.01#5", "text": "“TÔI KHÔNG CÓ QUYỀN IM LẶNG TRƯỚC TỘI ÁC”", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "“TÔI MUỐN DỪNG LẠI, MUỐN MỌI CHUYỆN KẾT THÚC”", "dur_s": 2.5},
            {"sau_cau": "TK3.01#9", "text": "LỜI THỪA NHẬN SÁT HẠI HÀNG CHỤC NẠN NHÂN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "COVERT TRANSMITTER BENEATH WINTER SWEATER", "dur_s": 3.0},
            {"after_id": "TK3.01#4", "text": "SINGLE MOTHER BATTLING SEVERE CARDIOMYOPATHY", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "“STAYING SILENT WOULD MAKE ME COMPLICIT”", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "“I WANT TO STOP, I WANT IT ALL TO BE OVER”", "dur_s": 2.5},
            {"after_id": "TK3.01#9", "text": "FULL CONFESSION: DIGOXIN & INSULIN MURDERS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "セーターの内側に仕掛けられた盗聴マイク", "dur_s": 3.0},
            {"after_id": "TK3.01#4", "text": "重度の心筋症と幼い娘二人を抱える母の決断", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "「沈黙を守り凶行を見過ごすことなどできない」", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "「やめたい、すべてを終わりにしたい」", "dur_s": 2.5},
            {"after_id": "TK3.01#9", "text": "自白：DIGOXINとINSULINによる連続殺害", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t4_diner_exterior", "still"),
            ("H", "4.02#7", "neutral", -0.02, 0.6, "t4_diner_exterior", "pull"),
            ("D", "4.04#1", "neutral", -0.03, 0.6, "t4_diner_booth", "pan"),
            ("D", "4.04#6", "neutral", -0.03, 0.6, "t4_amy_scrubs", "still"),
            ("N2", "4.06#6", "fearful", -0.04, 0.7, "t4_amy_scrubs", "push"),
            ("H", "4.08#3", "neutral", -0.02, 0.6, "t4_wire_closeup", "push"),
            ("H", "4.08#6", "neutral", -0.02, 0.7, "t4_diner_booth", "still"),
            ("H", "4.08#8", "sad", -0.03, 0.7, "t4_diner_booth", "pull"),
            ("D", "4.12#5", "neutral", -0.03, 0.7, "t4_interrogation_room", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t4_closing_desk", "still")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Mười sáu năm im lặng của chín bệnh viện",
        "title_en": "Sixteen Years of Silence Across Nine Hospitals",
        "title_ja": "9つの病院が続けた16年間の沈黙",
        "signs": [9, 3],
        "theme_vn": "Sự thờ ơ thể chế (Institutional Bystander Effect) & 400 nạn nhân trong bóng tối",
        "theme_en": "Institutional Bystander Effect & 400 Victims in the Shadows",
        "theme_ja": "組織的傍観者効果と闇に葬られた400名の犠牲者",
        "hook_vn": "Chín bệnh viện biết hắn có vấn đề. Nhưng tất cả đều chọn im lặng.",
        "hook_en": "Nine hospitals suspected him. Every single one chose silence.",
        "hook_ja": "9つの病院が彼を疑っていた。しかし全員が沈黙を選んだ。",
        "bgm": "bgm_ambient_deep.mp3",
        "bgm_desc_vn": "Hồi 1/5 — bed tập: bgm_ambient_deep.mp3",
        "bgm_desc_en": "Act 1/5 — episode bed: bgm_ambient_deep.mp3",
        "bgm_desc_ja": "第1/5幕 — 本編BGM: bgm_ambient_deep.mp3",
        "sfx_vn": ["amb_hospital_corridor.wav (nền)", "fx_paper_shuffle.wav", "fx_stamp_confidential.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_hospital_corridor.wav (bed)", "fx_paper_shuffle.wav", "fx_stamp_confidential.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_hospital_corridor.wav（環境音）", "fx_paper_shuffle.wav", "fx_stamp_confidential.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "16 NĂM · 9 BỆNH VIỆN VÀ 1 VIỆN DƯỠNG LÃO", "dur_s": 3.0},
            {"sau_cau": "TK4.01#5", "text": "BUỘC THÔI VIỆC TRONG IM LẶNG: BẢO VỆ DANH TIẾNG", "dur_s": 2.5},
            {"sau_cau": "TK4.01#6", "text": "ƯỚC TÍNH THỰC TẾ CÓ THỂ LÊN TỚI 400 NẠN NHÂN", "dur_s": 2.5},
            {"sau_cau": "TK4.01#7", "text": "SỰ IM LẶNG ĐỒNG LÕA CỦA CÁC NHÀ QUẢN LÝ", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "ĐẠO LUẬT CULLEN 2004: CHẤM DỨT SỰ IM LẶNG", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "16 YEARS · 9 HOSPITALS & 1 NURSING HOME", "dur_s": 3.0},
            {"after_id": "TK4.01#5", "text": "QUIET DISMISSALS: PROTECTING INSTITUTIONAL REPUTATION", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "ESTIMATED ACTUAL DEATH TOLL: UP TO 400 VICTIMS", "dur_s": 2.5},
            {"after_id": "TK4.01#7", "text": "SYSTEMIC SILENCE TRANSFORMED HEALING INTO CARNAGE", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "THE CULLEN ACT 2004: MANDATORY REPORTING ENACTED", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "16年間 · 9つの病院と1つの介護施設", "dur_s": 3.0},
            {"after_id": "TK4.01#5", "text": "保身のための秘密裏の解雇と白紙の推薦状", "dur_s": 2.5},
            {"after_id": "TK4.01#6", "text": "推計犠牲者数：最大400名に達する可能性", "dur_s": 2.5},
            {"after_id": "TK4.01#7", "text": "管理者たちの組織的沈黙が生んだ悲劇", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "2004年「カレン法」：沈黙の連鎖を永久に遮断", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t4_ten_hospitals_map", "still"),
            ("D", "1.14#2", "neutral", -0.03, 0.6, "t4_somerset_exterior", "pan"),
            ("D", "1.14#3", "neutral", -0.03, 0.6, "t4_ten_hospitals_map", "pull"),
            ("D", "1.14#4", "neutral", -0.03, 0.6, "t4_ten_hospitals_map", "push"),
            ("D", "1.14#5", "neutral", -0.03, 0.7, "t4_neutral_letter", "still"),
            ("D", "1.14#7", "neutral", -0.03, 0.7, "t4_case_file_open", "push"),
            ("C", "5.05#6", "neutral", -0.02, 0.7, "t4_institutional_bystander", "still"),
            ("D", "5.06#2", "neutral", -0.03, 0.7, "t4_courtroom_bench", "still"),
            ("H", "cta", "neutral", -0.02, 0.0, "t4_closing_desk", "still")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Bài học sinh tồn từ lòng dũng cảm của Amy Loughren",
        "title_en": "Survival Lessons & The Courage of Amy Loughren",
        "title_ja": "生存の教訓とエイミー・ローレンの勇気",
        "signs": [10],
        "theme_vn": "Nạn nhân học & Bài học sinh tồn: Dũng cảm phá vỡ sự im lặng",
        "theme_en": "Victimology & Survival Red Flags: Courage to Break the Silence",
        "theme_ja": "被害者学と生存の危険信号：沈黙を破る勇気",
        "hook_vn": "Bài học sinh tồn lớn nhất: Đừng bao giờ im lặng trước cái ác.",
        "hook_en": "The greatest survival lesson: Never stay silent in the face of wrong.",
        "hook_ja": "最大の生存の教訓：決して不正の前に沈黙してはならない。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_gentle_night.wav (nền)", "fx_clock_chime.wav", "fx_sub_drop.wav", "fx_warm_resolve.wav"],
        "sfx_en": ["amb_gentle_night.wav (bed)", "fx_clock_chime.wav", "fx_sub_drop.wav", "fx_warm_resolve.wav"],
        "sfx_ja": ["amb_gentle_night.wav（環境音）", "fx_clock_chime.wav", "fx_sub_drop.wav", "fx_warm_resolve.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "BÀI HỌC SINH TỒN VÀ TRÁCH NHIỆM XÃ HỘI", "dur_s": 3.0},
            {"sau_cau": "TK5.01#3", "text": "CẢNH BÁO ĐỎ SINH TỒN: SỰ BẤT AN TẬP THỂ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#5", "text": "TÁI THIẾT KẾ QUY TRÌNH QUẢN LÝ DƯỢC TOÀN QUỐC", "dur_s": 2.5},
            {"sau_cau": "TK5.01#7", "text": "LÒNG DŨNG CẢM CỦA NỮ Y TÁ AMY LOUGHREN", "dur_s": 2.5},
            {"sau_cau": "TK5.01#8", "text": "LẮNG NGHE VÀ TIN TƯỞNG VÀO TRỰC GIÁC", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "SURVIVAL LESSONS & SOCIAL RESPONSIBILITY", "dur_s": 3.0},
            {"after_id": "TK5.01#3", "text": "SURVIVAL RED FLAGS: THE COST OF COLLECTIVE SILENCE", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "NATIONWIDE RE-ENGINEERING OF PHARMACEUTICAL PROTOCOLS", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "THE REMARKABLE COURAGE OF NURSE AMY LOUGHREN", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "ALWAYS LISTEN TO AND HONOR YOUR INTUITION", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "生存の教訓と社会的責任", "dur_s": 3.0},
            {"after_id": "TK5.01#3", "text": "生存の危険信号：集団的沈黙が招いた代償", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "全米における自動薬剤管理プロセスの抜本的再設計", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "看護師エイミー・ローレンが示した不屈の勇気", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "自分自身の直感を信じ、決して沈黙しないこと", "dur_s": 3.0}
        ],
        "items": [
            ("H", "hook", "neutral", -0.02, 0.5, "t4_somerset_courtroom", "still"),
            ("H", "1.16#4", "neutral", -0.02, 0.6, "t4_boardroom_empty", "pan"),
            ("H", "1.16#5", "neutral", -0.02, 0.7, "t4_somerset_exterior", "pull"),
            ("D", "5.06#2", "neutral", -0.03, 0.6, "t4_courtroom_bench", "still"),
            ("D", "5.06#5", "neutral", -0.03, 0.6, "t4_pyxis_station", "pan"),
            ("H", "5.08#4", "neutral", -0.02, 0.7, "t4_nurse_station", "still"),
            ("H", "5.08#6", "neutral", -0.02, 0.7, "t4_amy_scrubs", "push"),
            ("H", "5.08#7", "neutral", -0.02, 0.8, "t4_closing_desk", "pull"),
            ("H", "cta", "neutral", -0.02, 0.0, "t4_closing_desk", "still")
        ]
    }
]

CTA_VI = "Tập bốn của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio."
CTA_EN = "Episode four of Amber Eyes. Watch the full documentary via the bio link."
CTA_JA = "Amber Eyes第4話。プロフィールリンクから完全版ドキュメンタリーをご覧ください。"

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

            item_dict = {
                "clip_line_id": cl_id,
                "role": role,
                "emotion": emo,
                "speed_offset": spd,
                "pause_after_s": pause,
                "bg": bg,
                "motion": motion,
                "text": raw_text,
                ("characters_spoken" if is_ja else "words_spoken"): units,
                "est_dur_s": round(dur_line, 2),
                "src_script": src_str
            }
            clip_lines.append(item_dict)

        tot_dur = round(tot_dur, 1)

        spec_clips[cid] = {
            "id": cid,
            "title": title,
            "theme": theme,
            "psychological_signs": c["signs"],
            "bgm": c["bgm"],
            "bgm_desc": bgm_desc,
            "sfx": sfx_list,
            "overlays": overlays,
            "lines": clip_lines,
            "total_est_duration_s": tot_dur
        }

        summary_list.append({
            "clip": cid,
            "title": title,
            "signs": c["signs"],
            "lines_count": len(clip_lines),
            "est_duration_s": tot_dur
        })

    # SPEC_AUDIO_CLIP_TAP04.json
    spec_full = {
        "_readme": f"Đặc tả audio và kịch bản dựng TikTok Tập 04 ({lang}) — sinh tự động bởi .work/_build_tk_tap04.py.",
        "_episode": "Tap04",
        "_language": lang,
        "_title": "THIÊN THẦN TỬ THẦN & PHỨC CẢM CHÚA TRỜI" if is_vi else ("ANGEL OF DEATH & THE GOD COMPLEX" if is_en else "死の天使と神コンプレックス"),
        "_measured_rates": {r: round(rates[r], 4) for r in sorted(rates.keys())},
        "_clips_summary": summary_list,
        "clips": spec_clips
    }

    with (out_dir / "SPEC_AUDIO_CLIP_TAP04.json").open("w", encoding="utf-8") as f:
        json.dump(spec_full, f, ensure_ascii=False, indent=2)

    # Viết Caption_TK*, MoTa_Ngan_TK*, MoTa_Dai_TK*
    for c in CLIPS_DEF:
        cid = c["id"]
        hook = c["hook_vn"] if is_vi else (c["hook_en"] if is_en else c["hook_ja"])
        title = c["title_vn"] if is_vi else (c["title_en"] if is_en else c["title_ja"])
        signs_str = " · ".join([f"#{s}" for s in c["signs"]])

        if is_vi:
            cap = f"""{hook} 👁️

Tập 04 · Thiên Thần Tử Thần — chỉ dấu tâm lý {signs_str}: {c['theme_vn']}.
Hồ sơ tâm lý tội phạm có thật dựa trên biên bản toà án New Jersey và tài liệu điều tra độc quyền.

📺 Xem trọn vẹn tập phim tài liệu 21 phút tại link trong bio!
👉 Nhấn follow @ambereyes.vn để bước vào tâm trí kẻ thủ ác.

#tamlytoipham #ambereyes #charlescullen #hosoanchuyen #khampha #kienthuc #toiphamcothat #podcastvietnam #truecrime"""

            mn = f"""{hook} 👁️
Tập 04 · Thiên Thần Tử Thần — Chỉ dấu {signs_str}: {c['theme_vn']}.

Hồ sơ tâm lý tội phạm có thật dựa trên biên bản toà án New Jersey và tài liệu điều tra pháp y độc quyền.
Khám phá góc khuất tàn khốc về sự im lặng thể chế và hành trình phá án nghẹt thở của nữ y tá Amy Loughren.

📺 Xem đầy đủ tập phim tài liệu 21 phút tại link trên bio.
#tamlytoipham #ambereyes #charlescullen #hosoanchuyen #truecrime"""

            md = f"""{hook} 👁️
TẬP 04 · THIÊN THẦN TỬ THẦN & PHỨC CẢM CHÚA TRỜI
Chỉ dấu tâm lý chuyên sâu: {signs_str} — {c['theme_vn']}.

Trong suốt 16 năm công tác tại 9 bệnh viện và 1 viện dưỡng lão trên khắp New Jersey và Pennsylvania, Charles Cullen đã lợi dụng chiếc áo blouse trắng và hiệu ứng hào quang của một người chăm sóc mẫu mực để âm thầm gieo rắc cái chết cho hàng trăm bệnh nhân vô tội. Bằng thủ đoạn hủy lệnh trên máy cấp phát thuốc Pyxis và tiêm lén các liều độc dược Digoxin hay Insulin, hắn thỏa mãn "Phức cảm Chúa trời" bệnh hoạn khi tự cho mình quyền quyết định sinh tử.

Sự im lặng có hệ thống của các nhà quản lý vì nỗi sợ kiện tụng đã tiếp tay cho bi kịch kéo dài suốt 16 năm, cướp đi sinh mạng của ước tính lên tới 400 nạn nhân. Chỉ đến khi nữ y tá quả cảm Amy Loughren dũng cảm chấp nhận hiểm nguy, mang máy nghe lén bí mật đối đầu với người bạn thân tại một quán ăn địa phương, sự thật kinh hoàng mới được bóc trần trước ánh sáng công lý.

Đạo luật Cullen năm 2004 đã được ban hành để bẻ gãy vĩnh viễn sự im lặng thể chế nguy hiểm này. Bài học sinh tồn lớn nhất: Hãy luôn lắng nghe trực giác và đừng bao giờ im lặng trước cái ác!

📺 Xem trọn vẹn tập phim tài liệu 21 phút được phân tích đa chiều tại link bio kênh Amber Eyes.
👉 Follow kênh để đón xem những hồ sơ tâm lý tội phạm chấn động tiếp theo.

#tamlytoipham #ambereyes #charlescullen #hosoanchuyen #khampha #kienthuc #toiphamcothat #podcastvietnam #truecrime #kyluc #phapluat"""

        elif is_en:
            cap = f"""{hook} 👁️

Ep. 04 · The Angel of Death — Psychological Markers {signs_str}: {c['theme_en']}.
True crime psychological profiling based on New Jersey court records and exclusive investigative files.

📺 Watch the full 21-minute documentary via the link in our bio!
👉 Follow @ambereyes.official to venture into the psychology of extreme crime.

#truecrime #psychology #charlescullen #criminalpsychology #angelofdeath #crimedocumentary #fbi #forensics #podcast"""

            mn = f"""{hook} 👁️

Episode 04 · The Angel of Death — Psychological Markers {signs_str}: {c['theme_en']}.
Authentic psychological forensic breakdown based on official Superior Court records.

Uncover the chilling reality of systemic hospital silence and nurse Amy Loughren's harrowing undercover operation.

📺 Full 21-minute documentary streaming now via our bio link.
#truecrime #charlescullen #angelofdeath #criminalminds #forensics"""

            md = f"""{hook} 👁️
EPISODE 04 · THE ANGEL OF DEATH & THE GOD COMPLEX
In-depth Psychological Analysis: Markers {signs_str} — {c['theme_en']}.

Across 16 years and ten medical facilities in New Jersey and Pennsylvania, Charles Cullen exploited the pristine halo of the nursing uniform to systematically murder dozens, potentially hundreds, of vulnerable patients. Utilizing software flaws in automated Pyxis dispensing cabinets and administering lethal overdoses of Digoxin and Insulin, Cullen fulfilled a distorted “God Complex” by arbitrating life and death.

Systemic institutional bystander silence—fueled by hospital liability fears—shielded his predatory trajectory for nearly two decades, leaving an estimated death toll reaching 400 innocent victims. Only when nurse Amy Loughren bravely agreed to wear a hidden wiretap and confront her best friend inside a local diner was Cullen’s wall of deception finally dismantled.

Enacted in 2004, the landmark Cullen Act permanently mandated institutional reporting to safeguard future patients. The paramount survival lesson remains clear: Always trust your instincts, and never remain silent in the face of evil.

📺 Watch the full 21-minute investigative documentary via the link in bio.
👉 Follow Amber Eyes for rigorous true crime profiling.

#truecrime #charlescullen #angelofdeath #psychology #forensics #crimedocumentary #justice #fbi #podcast"""

        else: # JA
            cap = f"""{hook} 👁️

第04話 · 死の天使 — 心理指標 {signs_str}: {c['theme_ja']}。
裁判記録および公的捜査資料に基づく本格犯罪心理学ドキュメンタリー。

📺 完全版ドキュメンタリー（21分）はYouTubeで公開中 — プロフィールのリンクから！
👉 フォローして次回の深層心理プロファイリングをお見逃しなく。

#犯罪心理学 #アンバーアイズ #実話 #未解決事件 #事件 #心理学 #ドキュメンタリー #チャールズカレン #プロファイリング"""

            mn = f"""{hook} 👁️

第04話 · 死の天使 — 心理指標 {signs_str}: {c['theme_ja']}。
裁判記録・公的調書に基づく犯罪心理学ドキュメンタリー。

全米を震撼させた組織的沈黙の闇と、親友に盗聴器をつけて対峙した看護師エイミー・ローレンの真実。

📺 YouTubeで21分の完全版ドキュメンタリーを公開中 — プロフィールのリンクからご覧ください。
#犯罪心理学 #アンバーアイズ #実話 #事件 #ドキュメンタリー"""

            md = f"""{hook} 👁️
第04話 · 死の天使と神コンプレックス
専門心理指標解析：{signs_str} — {c['theme_ja']}。

ニュージャージー州とペンシルベニア州の9つの病院および1つの介護施設において、16年間にわたり白衣の「ハロー効果（後光効果）」を悪用し続けたCharles Cullen。彼は自動薬剤分配機Pyxisのキャンセル機能を悪用し、DigoxinやInsulinといった劇薬を密かに混入させて「神コンプレックス」を満たしていました。

訴訟と責任追及を恐れた病院管理者たちの組織的な沈黙により、推計400名もの罪なき患者が犠牲となりました。この絶望的な闇を切り裂いたのは、重い心臓病を抱えながらも自らの身に盗聴マイクを装着し、ダイナーで親友と対峙した看護師エイミー・ローレンの並外れた勇気でした。

この悲劇を契機に2004年「カレン法」が制定され、医療機関における危険行為の通報が義務化されました。最大の生存の教訓は、「常に自らの直感を信じ、不正の前に決して沈黙しないこと」です。

📺 21分におよぶ完全版ドキュメンタリーは、YouTube公式チャンネル（プロフィールのリンク）にて公開中。
👉 フォローして次なるプロファイリングをお楽しみください。

#犯罪心理学 #アンバーアイズ #実話 #事件 #心理学 #ドキュメンタリー #チャールズカレン #プロファイリング #教養"""

        (out_dir / f"Caption_{cid}.txt").write_text(cap, encoding="utf-8")
        (out_dir / f"MoTa_Ngan_{cid}.txt").write_text(mn, encoding="utf-8")
        (out_dir / f"MoTa_Dai_{cid}.txt").write_text(md, encoding="utf-8")

    # Kế hoạch Markdown tổng thể cho từng ngôn ngữ
    md_plan_name = "KE_HOACH_CLIP_TAP04.md" if is_vi else (f"KE_HOACH_CLIP_TAP04_{lang}.md")
    
    plan_lines = []
    if is_vi:
        plan_lines.append("# KẾ HOẠCH CLIP TIKTOK — TẬP 04 · \"THIÊN THẦN TỬ THẦN & PHỨC CẢM CHÚA TRỜI\"\n")
        plan_lines.append("*Ngày: 20/11/2026 · Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*\n")
        plan_lines.append("*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap04/SPEC_AUDIO_CLIP_TAP04.json`*\n")
        plan_lines.append("*Nguồn duy nhất của mọi dữ kiện: `02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md` · `.work/timeline_s_t04.json` (212 câu) · `02_SAN_XUAT/Tap04/nguon_tham_khao.md`*\n\n---\n\n## 0. Tóm tắt chốt\n\n")
        plan_lines.append("| Hạng mục | Giá trị |\n|---|---|\n")
        plan_lines.append("| Số clip | **5 clip** (TK1–TK4 chính + TK5 bài học sinh tồn) |\n")
        plan_lines.append("| Tổng câu đọc | **48 câu** đọc giọng (chuẩn hóa đo lường ASR) |\n")
        plan_lines.append("| Độ dài đo thực tế | Ước lượng 63.2 – 82.3 s/clip (mục tiêu 60–90 s · cổng QC 45–95 s) |\n")
        plan_lines.append("| Chủ đề | Mỗi clip = **1–2 chỉ dấu tâm lý cốt lõi** của Tập 04 (K10) |\n")
        plan_lines.append("| Ngôn ngữ | Tiếng Việt · vai Host (H), Điều tra viên (D), Chuyên gia (C), Y tá Somerset (N1), Y tá Amy (N2) |\n")
        plan_lines.append("| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** (bộ giọng chuẩn Tập 04) |\n")
        plan_lines.append("| Hình ảnh | Nền dọc 9:16 crop/pad từ 51 nền noir 2K gốc của Tập 04 |\n")
        plan_lines.append("| Chi phí | **0 đồng** (Kaggle GPU có sẵn) |\n\n---\n\n## 1. Năm clip và chỉ dấu tâm lý tương ứng (K10)\n\n")
        plan_lines.append("| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng thời lượng |\n|---|---|---|---|---|\n")
        for s in summary_list:
            c_info = next(x for x in CLIPS_DEF if x["id"] == s["clip"])
            plan_lines.append(f"| **{s['clip']}** | {' · '.join(['#' + str(x) for x in s['signs']])} | {c_info['theme_vn']} | *\"{c_info['hook_vn']}\"* | {s['est_duration_s']} s · {s['lines_count']} câu |\n")
        plan_lines.append("\n**Thứ tự đăng đề xuất:** TK2 → TK1 → TK3 → TK4 → TK5\n\n---\n\n## 2. Diễn xuất và đặc tả chi tiết từng clip\n\n")
    elif is_en:
        plan_lines.append("# TIKTOK PRODUCTION PLAN — EPISODE 04 · \"ANGEL OF DEATH & THE GOD COMPLEX\"\n\n")
        plan_lines.append("*Date: 2026-11-20 · Status: **Script completed, ready for approval prior to TTS generation** (L4)*\n")
        plan_lines.append("*Master plan: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Machine-readable audio spec: `02_SAN_XUAT/TIKTOK/Tap04_EN/SPEC_AUDIO_CLIP_TAP04.json`*\n")
        plan_lines.append("*Single source of truth: `02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md` · `.work/timeline_s_EN_t04.json` (212 items) · `02_SAN_XUAT/Tap04/nguon_tham_khao.md`*\n\n---\n\n## 0. Executive Summary\n\n")
        plan_lines.append("| Item | Specification |\n|---|---|\n")
        plan_lines.append("| Clip Count | **5 clips** (TK1–TK4 core psychological hooks + TK5 survival takeaways) |\n")
        plan_lines.append("| Spoken Lines | **48 lines** total |\n")
        plan_lines.append("| Measured Duration | 66.3 – 78.8 s/clip (target 60–90 s · QC gate 45–95 s) |\n")
        plan_lines.append("| Core Themes | 1–2 mandatory psychological markers per clip (K10) |\n")
        plan_lines.append("| Language | English (Host H, Detective D, Psychologist C, Nurse N1, Nurse Amy N2) |\n")
        plan_lines.append("| TTS Engine | **Higgs Audio v3 + VoxCPM2 reference voices (EN cast)** |\n\n---\n\n## 1. Five Clips and Psychological Markers\n\n")
        plan_lines.append("| Clip | Markers | Theme | Hook (0–3 s) | Duration |\n|---|---|---|---|---|\n")
        for s in summary_list:
            c_info = next(x for x in CLIPS_DEF if x["id"] == s["clip"])
            plan_lines.append(f"| **{s['clip']}** | {' · '.join(['#' + str(x) for x in s['signs']])} | {c_info['theme_en']} | *\"{c_info['hook_en']}\"* | {s['est_duration_s']} s · {s['lines_count']} lines |\n")
        plan_lines.append("\n---\n\n## 2. Granular Acting & Visual Specifications\n\n")
    else: # JA
        plan_lines.append("# TIKTOK制作計画書 — 第04話 · 「死の天使と神コンプレックス」\n\n")
        plan_lines.append("*日付: 2026-11-20 · ステータス: **脚本完成・音声合成前承認待ち** (L4)*\n")
        plan_lines.append("*親計画書: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · 音声仕様書: `02_SAN_XUAT/TIKTOK/Tap04_JA/SPEC_AUDIO_CLIP_TAP04.json`*\n")
        plan_lines.append("*事実情報源: `02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md` · `.work/timeline_s_JA_t04.json` (212行) · `02_SAN_XUAT/Tap04/nguon_tham_khao.md`*\n\n---\n\n## 0. 概要サマリー\n\n")
        plan_lines.append("| 項目 | 仕様・計測値 |\n|---|---|\n")
        plan_lines.append("| クリップ数 | **5クリップ** (TK1–TK4 心理指標フック + TK5 生存の教訓) |\n")
        plan_lines.append("| 総音声行数 | **48行** |\n")
        plan_lines.append("| 計測推定尺 | 74.8 – 92.1秒/クリップ (目標60–90秒 · QCゲート45–95秒内) |\n")
        plan_lines.append("| テーマ | 必須心理指標1〜2項目を厳格網羅 (K10) |\n")
        plan_lines.append("| 言語 | 日本語（Host H, 捜査官 D, 心理専門家 C, 看護師 N1, Amy N2） |\n")
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
    
    # Check if Tap04 already in csv
    has_t04 = any("Tap04" in l for l in lines)
    if not has_t04:
        new_rows = [
            "Tap04,TK1,Nấc thang hủy lệnh Pyxis,VI,63.2,9,Kịch bản hoàn thành,2026-11-20",
            "Tap04,TK2,Hiệu ứng hào quang chiếc áo blouse,VI,77.9,11,Kịch bản hoàn thành,2026-11-20",
            "Tap04,TK3,Nữ y tá mang máy nghe lén,VI,82.3,10,Kịch bản hoàn thành,2026-11-20",
            "Tap04,TK4,Mười sáu năm im lặng thể chế,VI,71.7,9,Kịch bản hoàn thành,2026-11-20",
            "Tap04,TK5,Bài học sinh tồn từ lòng dũng cảm,VI,75.7,9,Kịch bản hoàn thành,2026-11-20",
            "Tap04_EN,TK1,The Pyxis Cancel Loophole,EN,69.9,9,Kịch bản hoàn thành,2026-11-20",
            "Tap04_EN,TK2,The Halo Effect of the White Coat,EN,69.5,11,Kịch bản hoàn thành,2026-11-20",
            "Tap04_EN,TK3,The Wiretap Nurse,EN,78.8,10,Kịch bản hoàn thành,2026-11-20",
            "Tap04_EN,TK4,Sixteen Years of Silence,EN,69.4,9,Kịch bản hoàn thành,2026-11-20",
            "Tap04_EN,TK5,Survival Lessons & Courage,EN,66.3,9,Kịch bản hoàn thành,2026-11-20",
            "Tap04_JA,TK1,Pyxisのキャンセル抜け穴,JA,86.8,9,Kịch bản hoàn thành,2026-11-20",
            "Tap04_JA,TK2,模範的同僚と白衣のハロー効果,JA,86.1,11,Kịch bản hoàn thành,2026-11-20",
            "Tap04_JA,TK3,盗聴器を纏う看護師,JA,92.1,10,Kịch bản hoàn thành,2026-11-20",
            "Tap04_JA,TK4,9つの病院が続けた16年間の沈黙,JA,81.6,9,Kịch bản hoàn thành,2026-11-20",
            "Tap04_JA,TK5,生存の教訓とエイミーの勇気,JA,74.8,9,Kịch bản hoàn thành,2026-11-20"
        ]
        if lines:
            lines.extend(new_rows)
        else:
            lines = ["Episode,ClipID,Title,Language,EstDuration_s,Lines,Status,Date"] + new_rows
        csv_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
        print("Updated BangTheoDoi_TikTok.csv")

if __name__ == "__main__":
    for l in ["VI", "EN", "JA"]:
        build_for_lang(l)
    update_tracking_table()
    print("All Tap04 TikTok multi-language packages successfully created!")
