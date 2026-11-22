# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 14 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap14/KE_HOACH_CLIP_TAP14.md
  02_SAN_XUAT/TIKTOK/Tap14/SPEC_AUDIO_CLIP_TAP14.json
  02_SAN_XUAT/TIKTOK/Tap14/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap14/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap14/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap14_EN/KE_HOACH_CLIP_TAP14_EN.md
  02_SAN_XUAT/TIKTOK/Tap14_EN/SPEC_AUDIO_CLIP_TAP14.json
  02_SAN_XUAT/TIKTOK/Tap14_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap14_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap14_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap14_JA/KE_HOACH_CLIP_TAP14_JA.md
  02_SAN_XUAT/TIKTOK/Tap14_JA/SPEC_AUDIO_CLIP_TAP14.json
  02_SAN_XUAT/TIKTOK/Tap14_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap14_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap14_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 14:
- timeline_s_t14.json (VI)
- timeline_s_EN_t14.json (EN)
- timeline_s_JA_t14.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap14"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap14_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap14_JA"

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
# 0. TỶ LỆ ĐỌC THẬT (Đo từ master Tập 14)
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

RATE_VI = get_rates("timeline_s_t14.json", is_ja=False)
RATE_EN = get_rates("timeline_s_EN_t14.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t14.json", is_ja=True)

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

MAP_VI = load_script_map("script_tap14.json")
MAP_EN = load_script_map("script_tap14_EN.json")
MAP_JA = load_script_map("script_tap14_JA.json")

# ----------------------------------------------------------------------------
# 2. KHAI BÁO 5 CLIP TẬP 14 (BẢN VI, EN, JA)
# ----------------------------------------------------------------------------
CLIPS_CONFIG = [
    {
        "id": "TK1",
        "title_vn": "16 Năm Hy Sinh Nuôi Chồng & Lâu Đài Cát La Jolla",
        "title_en": "16 Years of Sacrifice & The La Jolla Sandcastle",
        "title_ja": "夫に捧げた16年の献身とラ・ホヤの砂の城",
        "signs": [1, 9],
        "theme_vn": "Bẫy Chi phí Chìm (Sunk Cost Fallacy) & Điểm mù Vị thế Hào nhoáng (Upper-Class Blind Spot)",
        "theme_en": "The Sunk Cost Fallacy & Prestige Blind Spots",
        "theme_ja": "サンクコスト効果と上流階級の威光の盲点",
        "hook_vn": "16 năm bươn chải nuôi chồng lấy bằng Cornell và Harvard. Để rồi bị thay thế khi bước lên đỉnh cao.",
        "hook_en": "16 years financing his Cornell and Harvard degrees. Only to be discarded at the pinnacle of prestige.",
        "hook_ja": "コーネル大とハーバード大の学費を16年稼ぎ続けた妻。夫が頂点に立った時、待っていた残酷な結末。",
        "bgm": "bgm_cello_sad.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_cello_sad.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_cello_sad.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_cello_sad.mp3",
        "sfx_vn": ["amb_wind_cold.wav (nền)", "fx_sewing_machine.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_wind_cold.wav (bed)", "fx_sewing_machine.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_wind_cold.wav（環境音）", "fx_sewing_machine.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "HỒ SƠ BETTY BRODERICK · LA JOLLA, SAN DIEGO", "dur_s": 3.0},
            {"sau_cau": "TK1.01#3", "text": "16 NĂM LÀM THÊM ĐỦ MỌI NGHỀ NUÔI CHỒNG HỌC", "dur_s": 2.5},
            {"sau_cau": "TK1.01#5", "text": "HAI TẤM BẰNG DANH GIÁ: Y KHOA CORNELL & LUẬT HARVARD", "dur_s": 2.5},
            {"sau_cau": "TK1.01#7", "text": "BIỆT THỰ LA JOLLA & CHỦ TỊCH ĐOÀN LUẬT SƯ", "dur_s": 2.5},
            {"sau_cau": "TK1.01#8", "text": "BẪY CHI PHÍ CHÌM VÀ SỰ RẠN NỨT TÂM LÝ ĐẦU TIÊN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "BETTY BRODERICK DOSSIER · LA JOLLA, SAN DIEGO", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "16 YEARS OF WORKING MULTIPLE JOBS TO SUPPORT HIM", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "DUAL DEGREES: CORNELL MEDICINE & HARVARD LAW", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "LA JOLLA MANSION & BAR ASSOCIATION PRESIDENT", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "SUNK COST TRAP & FIRST PSYCHOLOGICAL FRACTURES", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "ベティ・ブロデリック事件簿 · サンディエゴ・ラホヤ", "dur_s": 3.0},
            {"after_id": "TK1.01#3", "text": "16年間内職と育児で夫の勉学を支え続けた妻", "dur_s": 2.5},
            {"after_id": "TK1.01#5", "text": "コーネル大医学士＆ハーバード大法学博士の栄誉", "dur_s": 2.5},
            {"after_id": "TK1.01#7", "text": "豪邸ラホヤと弁護士会長の地位：年収数百億ドルの頂点", "dur_s": 2.5},
            {"after_id": "TK1.01#8", "text": "サンクコストの罠と豪華な邸宅に走った最初の亀裂", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("1.04#3", "neutral", -0.02, 0.6, "t14_c04_betty_teaching_kindergarten_classroom", "pull"),
            ("1.04#4", "neutral", -0.02, 0.6, "t14_tupperware_avon_sales_struggle", "still"),
            ("1.04#5", "neutral", -0.02, 0.6, "t14_early_struggles_sewing_machine", "push"),
            ("1.04#6", "neutral", -0.02, 0.6, "t14_c03_young_dan_med_books_studying", "pan"),
            ("1.04#7", "neutral", -0.02, 0.6, "t14_cornell_harvard_diplomas", "pull"),
            ("1.06#1", "neutral", -0.02, 0.6, "t14_luxury_sedans_driveway", "still"),
            ("1.06#2", "neutral", -0.02, 0.6, "t14_bar_association_president_office", "push"),
            ("1.06#3", "sad", -0.04, 0.0, "t14_san_diego_bar_association_gala", "pan")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Nghệ Thuật Gaslighting & Chiếc Mỏ Neo Nhận Thức Bị Bẻ Gãy",
        "title_en": "Gaslighting & The Shattering of Cognitive Anchors",
        "title_ja": "ガスライティングと認識の錨の破壊工作",
        "signs": [2, 3],
        "theme_vn": "Thao túng Thực tại (Gaslighting) & Kiểm soát Cưỡng bách Vô hình (Coercive Control)",
        "theme_en": "Reality Manipulation (Gaslighting) & Invisible Coercive Control",
        "theme_ja": "現実感覚の操作（ガスライティング）と不可視の強迫的統制",
        "hook_vn": "Ngoại tình công khai nhưng khẳng định vợ mắc bệnh tâm thần. Nghệ thuật Gaslighting tàn nhẫn.",
        "hook_en": "Denying obvious adultery while labeling his wife clinically insane. The cruel anatomy of Gaslighting.",
        "hook_ja": "明白な浮気を隠蔽し、疑惑を口にする妻を「精神病」と決めつける。ガスライティングの冷酷な罠。",
        "bgm": "bgm_ambient_deep.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_ambient_deep.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_ambient_deep.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_ambient_deep.mp3",
        "sfx_vn": ["amb_room_tone.wav (nền)", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_tone.wav (bed)", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_tone.wav（環境音）", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "MÙA THU 1983: NỮ TRỢ LÝ TRẺ 21 TUỔI XUẤT HIỆN", "dur_s": 2.5},
            {"sau_cau": "TK2.01#3", "text": "PHỦ NHẬN QUYẾT LIỆT & QUY KẾT VỢ BỊ HOANG TƯỞNG", "dur_s": 2.5},
            {"sau_cau": "TK2.01#5", "text": "CHIẾN DỊCH GASLIGHTING KÉO DÀI GẦN HAI NĂM RÒNG", "dur_s": 3.0},
            {"sau_cau": "TK2.01#7", "text": "KHI BẢN THÂN TIN ĐÔI MẮT MÌNH BỊ ĐIÊN LOẠN", "dur_s": 2.5},
            {"sau_cau": "TK2.01#8", "text": "KIỂM SOÁT CƯỠNG BÁCH: GIAM CẦM TRONG VÔ HÌNH", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "FALL 1983: 21-YEAR-OLD ASSISTANT HIRED", "dur_s": 2.5},
            {"after_id": "TK2.01#3", "text": "FORCEFUL DENIAL & ACCUSING WIFE OF PARANOIA", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "TWO YEARS OF RELENTLESS GASLIGHTING", "dur_s": 3.0},
            {"after_id": "TK2.01#7", "text": "CONVINCING A VICTIM HER OWN EYES ARE CRAZY", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "COERCIVE CONTROL: THE INVISIBLE PSYCHOLOGICAL CAGE", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "1983年秋：21歳の若い女性秘書の採用", "dur_s": 2.5},
            {"after_id": "TK2.01#3", "text": "断固とした否定と妻を「妄想狂」扱いする工作", "dur_s": 2.5},
            {"after_id": "TK2.01#5", "text": "2年間に及ぶ二重現実の否定と心理的孤立", "dur_s": 3.0},
            {"after_id": "TK2.01#7", "text": "自分の目と頭がおかしくなったと信じ込まされる恐怖", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "不可視の監獄：強迫的統制が奪った精神の自由", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("1.06#4", "neutral", -0.02, 0.6, "t14_young_secretary_reception_desk", "pull"),
            ("1.06#6", "neutral", -0.02, 0.6, "t14_gaslighting_accusations_living_room", "push"),
            ("1.06#7", "neutral", -0.02, 0.6, "t14_gaslighting_accusations_living_room", "pan"),
            ("1.09#1", "neutral", -0.02, 0.6, "t14_gaslighting_whispers_corridor", "push"),
            ("1.09#2", "neutral", -0.02, 0.6, "t14_silent_dinner_table_suspicion", "pan"),
            ("1.09#4", "neutral", -0.02, 0.6, "t14_gaslighting_whispers_corridor", "still"),
            ("1.09#5", "sad", -0.04, 0.6, "t14_unanswered_rotary_phone", "push"),
            ("3.03#1", "neutral", -0.02, 0.0, "t14_coercive_control_invisible_cage", "pull")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Cuộc Chiến Pháp Lý Không Cân Sức & Cơn Bão Thịnh Nộ Ái Kỷ",
        "title_en": "Asymmetric Legal Warfare & Narcissistic Rage",
        "title_ja": "非対称な法廷闘争と自己愛性憤怒のエスカレーション",
        "signs": [6, 8],
        "theme_vn": "Ngòi nổ Tâm lý (Precipitating Trigger) & Cơn Thịnh nộ Ái kỷ Tổn thương (Vulnerable Narcissistic Rage)",
        "theme_en": "Psychological Triggers & Narcissistic Injury/Rage",
        "theme_ja": "心理的引き金と自己愛性憤怒の暴走軌道",
        "hook_vn": "Dùng luật pháp thượng tầng bóp nghẹt tài chính vợ cũ. Giọt nước tràn ly kích hoạt án mạng.",
        "hook_en": "Weaponizing elite legal mastery to suffocate his ex-wife financially. The trigger of mutual destruction.",
        "hook_ja": "最高峰の法律知識を武器に元妻の生活を兵粮攻めにする。破滅を決定づけた最後の引き金。",
        "bgm": "bgm_piano_minimal.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_piano_minimal.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_piano_minimal.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_piano_minimal.mp3",
        "sfx_vn": ["amb_rain_night.wav (nền)", "fx_gavel_strike.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_rain_night.wav (bed)", "fx_gavel_strike.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_rain_night.wav（環境音）", "fx_gavel_strike.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "CUỘC CHIẾN LY HÔN TÀN KHỐC NHẤT LỊCH SỬ SAN DIEGO", "dur_s": 2.5},
            {"sau_cau": "TK3.01#3", "text": "DANIEL BRODERICK VẬN DỤNG TOÀN BỘ QUYỀN LỰC PHÁP LÝ", "dur_s": 2.5},
            {"sau_cau": "TK3.01#5", "text": "LỆNH CẤM TIẾP CẬN & PHẠT TIỀN TỪNG TỪ CHỬI BỚI", "dur_s": 3.0},
            {"sau_cau": "TK3.01#6", "text": "TƯỚC ĐOẠT QUYỀN NUÔI CẢ 4 NGƯỜI CON", "dur_s": 2.5},
            {"sau_cau": "TK3.01#8", "text": "CƠN THỊNH NỘ ÁI KỶ VÀ ĐIỂM GÃY TÂM LÝ BÙNG PHÁT", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "MOST BRUTAL DIVORCE BATTLE IN SAN DIEGO HISTORY", "dur_s": 2.5},
            {"after_id": "TK3.01#3", "text": "LEGAL POWER WEAPONIZED AGAINST A DESPERATE EX-WIFE", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "RESTRAINING ORDERS & FINES PER PROFANITY IN VOICEMAIL", "dur_s": 3.0},
            {"after_id": "TK3.01#6", "text": "FULL CUSTODY OF ALL FOUR CHILDREN STRIPPED", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "NARCISSISTIC INJURY IGNITING DESTRUCTIVE RAGE", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "サンディエゴ史上最も過酷と呼ばれた5年間の泥沼離婚劇", "dur_s": 2.5},
            {"after_id": "TK3.01#3", "text": "トップ弁護士の権力と法知識を総動員した徹底的包囲網", "dur_s": 2.5},
            {"after_id": "TK3.01#5", "text": "接近禁止命令と留守電の暴言1回ごとに課された罰金", "dur_s": 3.0},
            {"after_id": "TK3.01#6", "text": "4人の子どもの養育権を剥奪され完全孤立へ", "dur_s": 2.5},
            {"after_id": "TK3.01#8", "text": "自己愛性憤怒と復讐の妄想への歯止めなき暴走", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("2.04#1", "neutral", -0.02, 0.6, "t14_temporary_rental_isolation", "pull"),
            ("2.04#2", "neutral", -0.02, 0.6, "t14_boiling_rage_darkened_room", "still"),
            ("2.06#1", "neutral", -0.02, 0.6, "t14_crested_stationery_threatening_letters", "pan"),
            ("2.06#2", "neutral", -0.02, 0.6, "t14_legal_brief_restraining_orders", "pull"),
            ("2.06#4", "neutral", -0.02, 0.6, "t14_fine_deduction_ledger", "push"),
            ("2.06#7", "sad", -0.04, 0.6, "t14_b2_cardboard_moving_boxes_empty_room", "still"),
            ("3.05#1", "neutral", -0.02, 0.6, "t14_vulnerable_narcissist_mask", "still"),
            ("3.05#3", "neutral", -0.02, 0.0, "t14_b3_shattered_hourglass_flowing_sand", "pan")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Năm Phát Đạn Rạng Sáng & Phiên Tòa Chia Rẽ Nước Mỹ",
        "title_en": "Five Dawn Gunshots & The Trial That Divided America",
        "title_ja": "夜明けの5発の銃声と全米を二分した法廷",
        "signs": [4, 5],
        "theme_vn": "Hệ thống Tự bào chữa (Bẫy Đóng vai Nạn nhân) & Sự Thức tỉnh của Người thân",
        "theme_en": "Victimhood Entitlement & The Children's Heartbreaking Truth",
        "theme_ja": "被害者意識の固定化と法廷で証言した娘の真実",
        "hook_vn": "Rạng sáng Chủ nhật ngày 5/11/1989. Năm phát đạn và chiếc bẫy tâm lý 'nạn nhân hóa hoàn hảo'.",
        "hook_en": "Dawn of November 5, 1989. Five fatal gunshots and the psychological trap of total victimhood.",
        "hook_ja": "1989年11月5日の夜明け、放たれた5発の銃声。被害者意識が引き起こした悲劇の結末。",
        "bgm": "bgm_violin_heart.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_violin_heart.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_violin_heart.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_violin_heart.mp3",
        "sfx_vn": ["amb_wind_cold.wav (nền)", "fx_door_creak_night.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_wind_cold.wav (bed)", "fx_door_creak_night.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_wind_cold.wav（環境音）", "fx_door_creak_night.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "RẠNG SÁNG 5/11/1989 · ĐẠI LỘ MAR AVENUE, LA JOLLA", "dur_s": 2.5},
            {"sau_cau": "TK4.01#3", "text": "NĂM PHÁT ĐẠN RẠNG SÁNG KHÉP LẠI MỌI OÁN HẬN", "dur_s": 2.5},
            {"sau_cau": "TK4.01#4", "text": "CON GÁI LỚN KIM BRODERICK: NỖI ĐAU XÉ NÁT TÂM CAN", "dur_s": 3.0},
            {"sau_cau": "TK4.01#6", "text": "CHÌA KHÓA LẤY TRỘM BÓC TRẦN YẾU TỐ TOAN TÍNH", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "BẢN ÁN 32 NĂM TÙ: KHÔNG MỘT TIA ĂN NĂN HỐI HẬN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "DAWN OF NOVEMBER 5, 1989 · MAR AVENUE, LA JOLLA", "dur_s": 2.5},
            {"after_id": "TK4.01#3", "text": "FIVE GUNSHOTS COMMITTED IN COLD BLOOD", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "ELDEST DAUGHTER KIM BRODERICK: AGONY ON THE STAND", "dur_s": 3.0},
            {"after_id": "TK4.01#6", "text": "STOLEN KEY EXPOSING SYSTEMATIC PREMEDITATION", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "32-YEAR-TO-LIFE SENTENCE: ZERO REMORSE UNTIL TODAY", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "1989年11月5日早朝 · ラホヤの高級住宅街マー通り", "dur_s": 2.5},
            {"after_id": "TK4.01#3", "text": "元夫と再婚相手を奪った5発のリボルバーの銃声", "dur_s": 2.5},
            {"after_id": "TK4.01#4", "text": "長女キムの法廷証言：引き裂かれた子どもたちの心", "dur_s": 3.0},
            {"after_id": "TK4.01#6", "text": "盗み出された合鍵が暴いた完全な計画的犯行", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "禁錮32年の終身刑：最後まで消えなかった自己正当化", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("4.08#1", "neutral", -0.02, 0.6, "t14_b4_police_station_lobby_glass_counter", "push"),
            ("4.08#2", "neutral", -0.02, 0.6, "t14_surrender_police_headquarters", "pan"),
            ("4.08#3", "neutral", -0.02, 0.6, "t14_b4_bank_of_tv_news_cameras_tripods", "pull"),
            ("4.09#1", "sad", -0.04, 0.6, "t14_b4_oak_witness_box_empty_microphone", "pan"),
            ("4.09#2", "sad", -0.04, 0.6, "t14_daughter_kim_witness_stand", "pull"),
            ("4.09#4", "sad", -0.04, 0.6, "t14_stolen_key_unlocked_door", "push"),
            ("4.11#1", "neutral", -0.02, 0.6, "t14_b4_handprint_fogged_prison_glass", "push"),
            ("4.11#3", "neutral", -0.02, 0.0, "t14_b4_handprint_fogged_prison_glass", "pull")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Nạn Nhân Học & Bài Học Sinh Tồn Hôn Nhân",
        "title_en": "Victimology & Marital Survival Lessons",
        "title_ja": "被害者学と結婚破綻を生き抜く教訓",
        "signs": [10],
        "theme_vn": "Nạn nhân học (Victimology) & 4 Dấu hiệu Cảnh báo Đỏ trong Đổ vỡ Quan hệ",
        "theme_en": "Victimology & Survival Red Flags in Toxic Separation",
        "theme_ja": "被害者学と有毒な関係から命を守る危険信号",
        "hook_vn": "Bốn bài học sinh tồn nhận diện lạm dụng tâm lý và thoát khỏi cạm bẫy hận thù sau đổ vỡ.",
        "hook_en": "Four vital survival lessons to identify psychological abuse and walk away from toxic hatred.",
        "hook_ja": "心理的虐待を見抜き、泥沼の憎悪から命と尊厳を守る「4つの教訓」。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_room_tone.wav (nền)", "fx_page_turn.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_tone.wav (bed)", "fx_page_turn.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_tone.wav（環境音）", "fx_page_turn.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 BÀI HỌC SINH TỒN HÔN NHÂN · AMBER EYES", "dur_s": 2.5},
            {"sau_cau": "TK5.01#3", "text": "BÀI HỌC 1: NHẬN DIỆN CHIẾN DỊCH GASLIGHTING SỚM", "dur_s": 2.5},
            {"sau_cau": "TK5.01#4", "text": "BÀI HỌC 2: TỈNH TÁO TRƯỚC VỊ THẾ XÃ HỘI HÀO NHOÁNG", "dur_s": 2.5},
            {"sau_cau": "TK5.01#5", "text": "BÀI HỌC 3: GIỮ VỮNG ĐỘC LẬP TÀI CHÍNH & PHÁP LÝ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#6", "text": "BÀI HỌC 4: HỌC CÁCH BUÔNG BỎ ĐỂ TỰ GIẢI THOÁT", "dur_s": 2.5},
            {"sau_cau": "TK5.01#7", "text": "SỰ TRẢ THÙ ĐÍCH THỰC LÀ SỐNG MỘT ĐỜI BÌNH AN", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "4 MARITAL SURVIVAL LESSONS · AMBER EYES", "dur_s": 2.5},
            {"after_id": "TK5.01#3", "text": "LESSON 1: RECOGNIZE EARLY SIGNS OF GASLIGHTING", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "LESSON 2: NEVER CONFLATE PRESTIGE WITH INTEGRITY", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "LESSON 3: MAINTAIN ECONOMIC & LEGAL INDEPENDENCE", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "LESSON 4: THE ART OF LETTING GO OF HATRED", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "TRUE REVENGE IS HEALING AND LIVING PEACEFULLY", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "結婚の破綻から生き残るための4つの教訓", "dur_s": 2.5},
            {"after_id": "TK5.01#3", "text": "教訓1：初期段階のガスライティングを見抜く", "dur_s": 2.5},
            {"after_id": "TK5.01#4", "text": "教訓2：社会的肩書や富を人間性の保証と錯覚しない", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "教訓3：経済的・法的・精神的自立を決して手放さない", "dur_s": 2.5},
            {"after_id": "TK5.01#6", "text": "教訓4：憎悪を手放し自己を解放する勇気を持つ", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "最大の復讐とは、自らを癒やし平穏に生き抜くこと", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("5.05#1", "neutral", -0.02, 0.5, "t14_four_redflags_overview_banner_t14", "still"),
            ("5.05#3", "neutral", -0.02, 0.4, "t14_redflag2_systematic_reality_denial", "pan"),
            ("5.05#4", "neutral", -0.02, 0.5, "t14_b5_four_pinned_polaroid_dossier_board", "pull"),
            ("5.05#6", "neutral", -0.02, 0.4, "t14_california_no_fault_divorce_papers", "push"),
            ("5.05#8", "neutral", -0.02, 0.5, "t14_b5_leather_bound_journal_fountain_pen", "pull"),
            ("5.05#9", "neutral", -0.02, 0.4, "t14_toxic_ties_severed_chain", "still"),
            ("5.05#15", "neutral", -0.02, 0.0, "t14_b5_stone_bench_blooming_cliff_garden", "pan")
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
        "VI": '# KẾ HOẠCH CLIP TIKTOK — TẬP 14 · "KHI NẠN NHÂN GASLIGHTING BƯỚC QUA RANH GIỚI TỘI ÁC (BETTY BRODERICK)"',
        "EN": '# TIKTOK CLIPS PLAN — EPISODE 14 · "WHEN GASLIGHTING VICTIMS CROSS THE LINE (BETTY BRODERICK)"',
        "JA": '# TIKTOKクリップ計画 — 第14話 ·「ガスライティングの被害者が一線を越えた時（ベティ・ブロデリック事件）」'
    }[lang_code]

    plan_lines.append(plan_header_title)
    plan_lines.append("")
    plan_lines.append(f"*Ngôn ngữ: **{lang_code}** · Nguồn dữ liệu: master Tập 14 · Tỷ lệ đọc ASR thật.*")
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

    # Ghi file KE_HOACH_CLIP_TAP14
    plan_filename = f"KE_HOACH_CLIP_TAP14{'' if lang_code == 'VI' else '_' + lang_code}.md"
    (out_dir / plan_filename).write_text("\n".join(plan_lines), encoding="utf-8")

    # Ghi file SPEC_AUDIO_CLIP_TAP14.json
    (out_dir / "SPEC_AUDIO_CLIP_TAP14.json").write_text(json.dumps(spec_audio, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[{lang_code}] Generated plan & spec successfully in {out_dir}")
    for cid, d in durations.items():
        print(f"  {cid}: {d}s")

if __name__ == "__main__":
    for code in ["VI", "EN", "JA"]:
        build_lang_artifacts(code)
