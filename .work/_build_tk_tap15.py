# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 15 (VI, EN, JA) — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap15/KE_HOACH_CLIP_TAP15.md
  02_SAN_XUAT/TIKTOK/Tap15/SPEC_AUDIO_CLIP_TAP15.json
  02_SAN_XUAT/TIKTOK/Tap15/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap15/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap15/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap15_EN/KE_HOACH_CLIP_TAP15_EN.md
  02_SAN_XUAT/TIKTOK/Tap15_EN/SPEC_AUDIO_CLIP_TAP15.json
  02_SAN_XUAT/TIKTOK/Tap15_EN/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap15_EN/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap15_EN/MoTa_Ngan_TK*.txt

  02_SAN_XUAT/TIKTOK/Tap15_JA/KE_HOACH_CLIP_TAP15_JA.md
  02_SAN_XUAT/TIKTOK/Tap15_JA/SPEC_AUDIO_CLIP_TAP15.json
  02_SAN_XUAT/TIKTOK/Tap15_JA/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap15_JA/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap15_JA/MoTa_Ngan_TK*.txt

Thời lượng clip đo bằng tỷ lệ đọc thực tế trên master Tập 15:
- timeline_s_t15.json (VI)
- timeline_s_EN_t15.json (EN)
- timeline_s_JA_t15.json (JA)
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
OUT_VI = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap15"
OUT_EN = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap15_EN"
OUT_JA = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap15_JA"

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
# 0. TỶ LỆ ĐỌC THẬT (Đo từ master Tập 15)
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

RATE_VI = get_rates("timeline_s_t15.json", is_ja=False)
RATE_EN = get_rates("timeline_s_EN_t15.json", is_ja=False)
RATE_JA = get_rates("timeline_s_JA_t15.json", is_ja=True)

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

MAP_VI = load_script_map("script_tap15.json")
MAP_EN = load_script_map("script_tap15_EN.json")
MAP_JA = load_script_map("script_tap15_JA.json")

# ----------------------------------------------------------------------------
# 2. KHAI BÁO 5 CLIP TẬP 15 (BẢN VI, EN, JA)
# ----------------------------------------------------------------------------
CLIPS_CONFIG = [
    {
        "id": "TK1",
        "title_vn": "Bí Ẩn Chiếc Máy Giặt & Dữ Liệu Kỹ Thuật Số",
        "title_en": "The Washing Machine Mystery & Digital Forensic Evidence",
        "title_ja": "洗濯機の謎と復元されたデジタル鑑識データ",
        "signs": [7, 8],
        "theme_vn": "Dấu ấn Signature vs. Thủ đoạn Gây án MO & Bằng chứng Giám định Kỹ thuật số",
        "theme_en": "MO vs. Signature & Digital Forensic Reconstruction",
        "theme_ja": "手口MO対署名Signatureとデジタルフォレンジックの決定打",
        "hook_vn": "Ném máy ảnh vào máy giặt đang chạy nước để phi tang. Nhưng dữ liệu số không bao giờ nói dối.",
        "hook_en": "Submerging the camera inside a running washing machine. But digital data never lies.",
        "hook_ja": "証拠隠滅のため洗濯機に沈められたカメラ。しかしデジタル鑑識は嘘をつかない。",
        "bgm": "bgm_cello_sad.mp3",
        "bgm_desc_vn": "Hồi 1 — bed tập: bgm_cello_sad.mp3",
        "bgm_desc_en": "Act 1 — episode bed: bgm_cello_sad.mp3",
        "bgm_desc_ja": "第1幕 — 本編BGM: bgm_cello_sad.mp3",
        "sfx_vn": ["amb_room_tone.wav (nền)", "fx_camera_shutter.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_tone.wav (bed)", "fx_camera_shutter.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_tone.wav（環境音）", "fx_camera_shutter.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK1.01#1", "text": "HIỆN TRƯỜNG MESA, ARIZONA · MÙA HÈ NĂM 2008", "dur_s": 2.5},
            {"sau_cau": "TK1.01#3", "text": "MÁY ẢNH SONY BỊ NGÂM DƯỚI ĐÁY LỒNG MÁY GIẶT NƯỚC", "dur_s": 3.0},
            {"sau_cau": "TK1.01#5", "text": "HÀNG LOẠT ẢNH BỊ XÓA ĐƯỢC PHỤC HỒI CHÍNH XÁC TỪNG GIÂY", "dur_s": 3.0},
            {"sau_cau": "TK1.01#7", "text": "17 GIỜ 29 PHÚT: BỨC ẢNH ĐỊNH MỆNH TRONG BUỒNG TẮM", "dur_s": 2.5},
            {"sau_cau": "TK1.01#9", "text": "DỮ LIỆU ĐIỆN TỬ LOẠI BỎ HOÀN TOÀN KẺ THỨ BA", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK1.01#1", "text": "CRIME SCENE MESA, ARIZONA · SUMMER 2008", "dur_s": 2.5},
            {"after_id": "TK1.01#3", "text": "SONY CAMERA SUBMERGED IN RUNNING WASHING MACHINE", "dur_s": 3.0},
            {"after_id": "TK1.01#5", "text": "DELETED PHOTOS RESTORED SECOND-BY-SECOND", "dur_s": 3.0},
            {"after_id": "TK1.01#7", "text": "5:29 PM: FATAL TIMESTAMP IN THE SHOWER", "dur_s": 2.5},
            {"after_id": "TK1.01#9", "text": "DIGITAL TIMESTAMPS EXCLUDING ANY THIRD PARTY", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK1.01#1", "text": "アリゾナ州メサの現場 · 2008年夏", "dur_s": 2.5},
            {"after_id": "TK1.01#3", "text": "水が回る洗濯機の底に沈められたソニー製カメラ", "dur_s": 3.0},
            {"after_id": "TK1.01#5", "text": "消去された写真群が秒単位で完全復元される", "dur_s": 3.0},
            {"after_id": "TK1.01#7", "text": "午後5時29分：浴室で撮影された最後の写真", "dur_s": 2.5},
            {"after_id": "TK1.01#9", "text": "第三者の関与を完全に否定したデジタル鑑識の証拠", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("1.14#3", "neutral", -0.02, 0.6, "t15_jodi_arias_a1_08_mesa", "still"),
            ("1.14#4", "neutral", -0.02, 0.6, "t15_b03_washing_machine_running_dark", "push"),
            ("1.14#5", "neutral", -0.02, 0.6, "t15_b03_washing_machine_running_dark", "pan"),
            ("1.14#6", "neutral", -0.02, 0.6, "t15_b03_washing_machine_running_dark", "pull"),
            ("2.04#1", "neutral", -0.02, 0.6, "t15_jodi_arias_a2_03_mirror", "still"),
            ("2.04#2", "neutral", -0.02, 0.6, "t15_jodi_arias_a2_04_interrogation", "push"),
            ("2.04#3", "neutral", -0.02, 0.6, "t15_jodi_arias_a2_05_mesa", "pan"),
            ("2.04#4", "fearful", -0.03, 0.6, "t15_jodi_arias_a2_06_arizona", "pull"),
            ("2.05#1", "neutral", -0.02, 0.0, "t15_jodi_arias_a2_07_desert", "still")
        ]
    },
    {
        "id": "TK2",
        "title_vn": "Hành Trình Xuyên Sa Mạc & Ba Can Xăng Bí Mật",
        "title_en": "Desert Crossing & The Three Secret Gas Cans",
        "title_ja": "砂漠越えのルートと3つの秘密のガソリン携行缶",
        "signs": [7, 8],
        "theme_vn": "Sự Chuẩn bị Toan tính (Premeditation) & Kỹ thuật Xóa dấu vết Ngoại phạm",
        "theme_en": "Chilling Premeditation & Alibi Fabrication Across State Lines",
        "theme_ja": "周到な事前計画と電子足跡の組織的隠蔽手口",
        "hook_vn": "Nhuộm tóc, tắt điện thoại, mang ba can xăng qua sa mạc. Sự toan tính lạnh lùng rùng mình.",
        "hook_en": "Dyed hair, powered-off phone, three gas cans across the desert. A chillingly premeditated journey.",
        "hook_ja": "黒染めした髪、切られた携帯電源、3つのガソリン缶。戦慄の完全犯罪計画。",
        "bgm": "bgm_ambient_deep.mp3",
        "bgm_desc_vn": "Hồi 2 — bed tập: bgm_ambient_deep.mp3",
        "bgm_desc_en": "Act 2 — episode bed: bgm_ambient_deep.mp3",
        "bgm_desc_ja": "第2幕 — 本編BGM: bgm_ambient_deep.mp3",
        "sfx_vn": ["amb_desert_wind.wav (nền)", "fx_car_driving_night.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_desert_wind.wav (bed)", "fx_car_driving_night.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_desert_wind.wav（環境音）", "fx_car_driving_night.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK2.01#1", "text": "2/6/2008: THUÊ XE TẠI REDDING, CALIFORNIA", "dur_s": 2.5},
            {"sau_cau": "TK2.01#3", "text": "MANG THEO 3 CAN XĂNG ĐỂ TRÁNH DÙNG THẺ TẠI ARIZONA", "dur_s": 3.0},
            {"sau_cau": "TK2.01#4", "text": "THỦ ĐOẠN TOAN TÍNH NGOẠI PHẠM BÀI BẢN VÀ LẠNH LÙNG", "dur_s": 2.5},
            {"sau_cau": "TK2.01#6", "text": "NHUỘM TÓC ĐỔI NHẬN DẠNG & TẮT NGUỒN ĐIỆN THOẠI", "dur_s": 2.5},
            {"sau_cau": "TK2.01#8", "text": "KỊCH BẢN NGỤY TẠO ĐÃ ĐƯỢC TÍNH TOÁN KỸ LƯỠNG", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK2.01#1", "text": "JUNE 2, 2008: RENTAL CAR ACQUIRED IN REDDING, CA", "dur_s": 2.5},
            {"after_id": "TK2.01#3", "text": "3 GAS CANS TO AVOID CREDIT CARD FOOTPRINTS IN ARIZONA", "dur_s": 3.0},
            {"after_id": "TK2.01#4", "text": "CHILLING PREMEDITATION DISPROVING SUDDEN PANIC", "dur_s": 2.5},
            {"after_id": "TK2.01#6", "text": "DARK HAIR DYE & PHONE DELIBERATELY POWERED OFF", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "METICULOUSLY CALCULATED FABRICATION SCENARIO", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK2.01#1", "text": "2008年6月2日：カリフォルニア州レディングでレンタカー確保", "dur_s": 2.5},
            {"after_id": "TK2.01#3", "text": "アリゾナでのカード履歴を避けるための3つのガソリン携行缶", "dur_s": 3.0},
            {"after_id": "TK2.01#4", "text": "突発的発作を完全に否定する周到な計画性", "dur_s": 2.5},
            {"after_id": "TK2.01#6", "text": "黒髪への偽装染色と携帯電話基地局追跡の遮断", "dur_s": 2.5},
            {"after_id": "TK2.01#8", "text": "綿密に組み立てられた戦慄のアリバイ工作", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("2.05#5", "neutral", -0.02, 0.6, "t15_darryl_brewer_garage_gas_cans", "still"),
            ("2.05#6", "neutral", -0.02, 0.6, "t15_jodi_arias_a2_10_bpd", "push"),
            ("2.05#7", "neutral", -0.02, 0.6, "t15_jodi_arias_a2_11_abandonment", "pan"),
            ("2.05#8", "neutral", -0.02, 0.6, "t15_b25_darryl_brewer_garage_gas_can", "pull"),
            ("2.05#9", "neutral", -0.02, 0.6, "t15_interstate_highway_gas_stop_midnight", "still"),
            ("2.05#10", "neutral", -0.02, 0.6, "t15_salt_lake_city_suburban_doorstep", "push"),
            ("2.05#13", "neutral", -0.02, 0.6, "t15_b62_jodi_arias_a2_02_photographs", "still"),
            ("2.05#16", "neutral", -0.02, 0.0, "t15_jodi_arias_a2_05_mesa", "pull")
        ]
    },
    {
        "id": "TK3",
        "title_vn": "Rối Loạn Ranh Giới (BPD) & Cơn Cuồng Nộ Bị Ruồng Bỏ",
        "title_en": "Borderline Personality Disorder & Abandonment Rage",
        "title_ja": "境界性パーソナリティ障害（BPD）と見捨てられ不安の暴走",
        "signs": [6, 8],
        "theme_vn": "Rối loạn Nhân cách Ranh giới (BPD), Tư duy Phân tách (Splitting) & Gắn kết Chấn thương (Trauma Bonding)",
        "theme_en": "BPD Splitting & Pathological Abandonment Panic",
        "theme_ja": "境界性パーソナリティ障害のスプリッティングと激しい怒り",
        "hook_vn": "Yêu say đắm buổi sáng, muốn hủy diệt buổi chiều. Giải mã tâm lý rối loạn nhân cách ranh giới.",
        "hook_en": "Idolized in the morning, dehumanized by evening. Unraveling Borderline Personality Disorder.",
        "hook_ja": "朝の崇拝から夕方の破壊願望へ。境界性パーソナリティ障害（BPD）が引き起こす激動の深層心理。",
        "bgm": "bgm_piano_minimal.mp3",
        "bgm_desc_vn": "Hồi 3 — bed tập: bgm_piano_minimal.mp3",
        "bgm_desc_en": "Act 3 — episode bed: bgm_piano_minimal.mp3",
        "bgm_desc_ja": "第3幕 — 本編BGM: bgm_piano_minimal.mp3",
        "sfx_vn": ["amb_room_tone.wav (nền)", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_tone.wav (bed)", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_tone.wav（環境音）", "fx_clock_ticking.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK3.01#1", "text": "GIÁM ĐỊNH TÂM THẦN HỌC LÂM SÀNG TẠI TÒA", "dur_s": 2.5},
            {"sau_cau": "TK3.01#2", "text": "RỐI LOẠN NHÂN CÁCH RANH GIỚI (BORDERLINE - BPD)", "dur_s": 3.0},
            {"sau_cau": "TK3.01#4", "text": "NỖI SỢ HÃI BỊ RUỒNG BỎ HOANG TƯỞNG CÙNG CỰC", "dur_s": 2.5},
            {"sau_cau": "TK3.01#6", "text": "TƯ DUY PHÂN TÁCH: LÝ TƯỞNG HÓA HOẶC PHI NHÂN HÓA", "dur_s": 3.0},
            {"sau_cau": "TK3.01#8", "text": "GẮN KẾT CHẤN THƯƠNG ĐẨY ĐẾN ĐIỂM GÃY HỦY DIỆT", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK3.01#1", "text": "FORENSIC CLINICAL PSYCHIATRIC EVALUATION", "dur_s": 2.5},
            {"after_id": "TK3.01#2", "text": "BORDERLINE PERSONALITY DISORDER (BPD)", "dur_s": 3.0},
            {"after_id": "TK3.01#4", "text": "TERROR OF ABANDONMENT TRIGGERING PRIMAL PANIC", "dur_s": 2.5},
            {"after_id": "TK3.01#6", "text": "SPLITTING MECHANISM: ALL-GOOD OR TOTAL ENEMY", "dur_s": 3.0},
            {"after_id": "TK3.01#8", "text": "TRAUMA BONDING ERUPTING INTO FATAL VIOLENCE", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK3.01#1", "text": "法廷で提出された臨床精神医学鑑定書", "dur_s": 2.5},
            {"after_id": "TK3.01#2", "text": "境界性パーソナリティ障害（BPD）の診断", "dur_s": 3.0},
            {"after_id": "TK3.01#4", "text": "狂気じみた「見捨てられ不安」がもたらす自己崩壊", "dur_s": 2.5},
            {"after_id": "TK3.01#6", "text": "スプリッティング：全か無か、理想化から悪魔化へ", "dur_s": 3.0},
            {"after_id": "TK3.01#8", "text": "トラウマ性愛着が引き起こした破滅的凶行", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("3.04#1", "neutral", -0.02, 0.6, "t15_jodi_arias_a3_03_arizona", "push"),
            ("3.04#2", "neutral", -0.02, 0.6, "t15_jodi_arias_a3_04_desert", "pan"),
            ("3.05#1", "neutral", -0.02, 0.6, "t15_jodi_arias_a3_06_gascan", "still"),
            ("3.05#2", "neutral", -0.02, 0.6, "t15_jodi_arias_a3_07_bpd", "push"),
            ("3.05#3", "neutral", -0.02, 0.6, "t15_jodi_arias_a3_08_abandonment", "pan"),
            ("3.05#5", "neutral", -0.02, 0.6, "t15_b67_borderline_splitting_black_w", "still"),
            ("3.05#10", "neutral", -0.02, 0.6, "t15_trauma_bonding_push_pull_tangle", "push"),
            ("3.11#1", "neutral", -0.02, 0.0, "t15_b63_cognitive_dissonance_scriptu", "push")
        ]
    },
    {
        "id": "TK4",
        "title_vn": "Trò Ảo Thuật Phòng Thẩm Vấn & Phiên Tòa Truyền Hình",
        "title_en": "Interrogation Room Acrobatics & The Media Trial",
        "title_ja": "取調室の三面記事的茶番と全米中継法廷",
        "signs": [4, 5],
        "theme_vn": "Hệ thống Tự bào chữa (Kỹ thuật Trung hòa Đạo đức) & Sự Tự thương hại Bệnh lý",
        "theme_en": "Neutralization Theory & Pathological Self-Pity Behind Camera Lights",
        "theme_ja": "中和の技術（自己正当化）と病的自己憐憫の仮面",
        "hook_vn": "Trồng cây chuối trong phòng hỏi cung, liên tục đổi kịch bản lời khai. Nước mắt của sự hối hận hay toan tính?",
        "hook_en": "Doing headstands inside police interrogation, constantly shifting stories. Genuine tears or cold manipulation?",
        "hook_ja": "取調室での逆立ち、二転三転する供述。法廷で見せた涙は真の悔悟か、それとも計算された演技か？",
        "bgm": "bgm_violin_heart.mp3",
        "bgm_desc_vn": "Hồi 4 — bed tập: bgm_violin_heart.mp3",
        "bgm_desc_en": "Act 4 — episode bed: bgm_violin_heart.mp3",
        "bgm_desc_ja": "第4幕 — 本編BGM: bgm_violin_heart.mp3",
        "sfx_vn": ["amb_wind_cold.wav (nền)", "fx_camera_flash_crowd.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_wind_cold.wav (bed)", "fx_camera_flash_crowd.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_wind_cold.wav（環境音）", "fx_camera_flash_crowd.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK4.01#1", "text": "PHỦ NHẬN BAN ĐẦU: 'TÔI KHÔNG HỀ ĐẾN ARIZONA'", "dur_s": 2.5},
            {"sau_cau": "TK4.01#3", "text": "KỊCH BẢN HAI KẺ ĐEO MẶT NẠ ĐỘT NHẬP HOANG TƯỞNG", "dur_s": 2.5},
            {"sau_cau": "TK4.01#5", "text": "HÀNH VI KỲ DỊ: HÁT MỘT MÌNH & TRỒNG CÂY CHUỐI KHI BỊ GIÁM SÁT", "dur_s": 3.0},
            {"sau_cau": "TK4.01#6", "text": "PHIÊN TÒA TRUYỀN HÌNH CHIA RẼ DƯ LUẬN NƯỚC MỸ NĂM 2013", "dur_s": 2.5},
            {"sau_cau": "TK4.01#8", "text": "TỰ THƯƠNG HẠI BỆNH LÝ KHI CHIẾC MẶT NẠ SỤP ĐỔ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK4.01#1", "text": "INITIAL DENIAL: 'I WAS NEVER IN ARIZONA'", "dur_s": 2.5},
            {"after_id": "TK4.01#3", "text": "FABRICATED MASKED INTRUDERS FICTION", "dur_s": 2.5},
            {"after_id": "TK4.01#5", "text": "BIZARRE BEHAVIOR: HEADSTANDS & SINGING ON CCTV", "dur_s": 3.0},
            {"after_id": "TK4.01#6", "text": "NATIONALLY TELEVISED TRIAL SENSATIONALIZING THE CRIME", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "PATHOLOGICAL SELF-PITY WHEN MANIPULATION FAILS", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK4.01#1", "text": "最初の嘘：「事件当時はアリゾナにいなかった」", "dur_s": 2.5},
            {"after_id": "TK4.01#3", "text": "覆面強盗2人組による襲撃という荒唐無稽な作り話", "dur_s": 2.5},
            {"after_id": "TK4.01#5", "text": "取調室の監視カメラの前で見せた逆立ちと独唱の奇行", "dur_s": 3.0},
            {"after_id": "TK4.01#6", "text": "2013年：全米が熱狂した生中継センセーション裁判", "dur_s": 2.5},
            {"after_id": "TK4.01#8", "text": "仮面が剥がれ落ちた後の病的自己憐憫の涙", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("2.08#1", "neutral", -0.02, 0.6, "t15_b41_jodi_arias_a2_11_abandonment", "pull"),
            ("2.08#2", "neutral", -0.02, 0.6, "t15_b26_darryl_brewer_garage_gas_can", "still"),
            ("2.08#3", "neutral", -0.02, 0.6, "t15_b17_interstate_highway_gas_stop_", "push"),
            ("4.07#1", "neutral", -0.02, 0.6, "t15_b18_jodi_arias_a4_09_interrogati", "pan"),
            ("4.07#2", "neutral", -0.02, 0.6, "t15_jodi_arias_a4_10_mesa", "pull"),
            ("4.08#1", "neutral", -0.02, 0.6, "t15_jodi_arias_a4_12_desert", "push"),
            ("4.11#1", "neutral", -0.02, 0.6, "t15_b30_jodi_arias_a4_09_interrogati", "pan"),
            ("4.11#8", "neutral", -0.02, 0.0, "t15_b10_two_guilt_polarities_scales", "push")
        ]
    },
    {
        "id": "TK5",
        "title_vn": "Nạn Nhân Học & 4 Cảnh Báo Đỏ Mối Quan Hệ Ám Ảnh",
        "title_en": "Victimology & 4 Red Flags of Obsessive Relationships",
        "title_ja": "被害者学と執着型関係の4つの危険信号",
        "signs": [10],
        "theme_vn": "Nạn nhân học (Victimology) & 4 Dấu hiệu Cảnh báo Đỏ Sinh tồn (The Gift of Fear - Gavin de Becker)",
        "theme_en": "Victimology & Survival Red Flags in Lethal Relationship Escalation",
        "theme_ja": "被害者学と破滅的な愛着関係から身を守る警告サイン",
        "hook_vn": "Bốn tín hiệu cảnh báo đỏ nhận diện kẻ săn mồi tâm lý ám ảnh để bảo vệ sinh mạng bản thân.",
        "hook_en": "Four vital survival red flags to detect obsessive psychological predators and save your life.",
        "hook_ja": "執着型パーソナリティの罠を見抜き、生命と尊厳を守る「4つの危険信号」。",
        "bgm": "bgm_piano_warm.mp3",
        "bgm_desc_vn": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
        "bgm_desc_en": "Act 5 — episode bed: bgm_piano_warm.mp3",
        "bgm_desc_ja": "第5幕 — 本編BGM: bgm_piano_warm.mp3",
        "sfx_vn": ["amb_room_tone.wav (nền)", "fx_page_turn.wav", "fx_stinger.wav"],
        "sfx_en": ["amb_room_tone.wav (bed)", "fx_page_turn.wav", "fx_stinger.wav"],
        "sfx_ja": ["amb_room_tone.wav（環境音）", "fx_page_turn.wav", "fx_stinger.wav"],
        "overlay_vn": [
            {"sau_cau": "TK5.01#1", "text": "4 CẢNH BÁO ĐỎ SINH TỒN · THE GIFT OF FEAR", "dur_s": 2.5},
            {"sau_cau": "TK5.01#3", "text": "CẢNH BÁO 1: LÝ TƯỞNG HÓA DỒN DẬP & HIỆU ỨNG TẮC KÈ HOA", "dur_s": 2.5},
            {"sau_cau": "TK5.01#5", "text": "CẢNH BÁO 2: XÂM PHẠM RANH GIỚI & THEO DÕI VI TẾ", "dur_s": 2.5},
            {"sau_cau": "TK5.01#7", "text": "CẢNH BÁO 3: TƯ DUY PHÂN TÁCH & CẢM XÚC BIẾN THIÊN CỰC ĐOAN", "dur_s": 2.5},
            {"sau_cau": "TK5.01#8", "text": "CẢNH BÁO 4: ĐE DỌA, PHÁ HOẠI TÀI SẢN KHI NÓI CHIA TAY", "dur_s": 2.5},
            {"sau_cau": "TK5.01#9", "text": "TRỰC GIÁC BẤT AN LÀ MÓN QUÀ SINH HỌC VÔ GIÁ", "dur_s": 3.0}
        ],
        "overlay_en": [
            {"after_id": "TK5.01#1", "text": "4 SURVIVAL RED FLAGS · THE GIFT OF FEAR", "dur_s": 2.5},
            {"after_id": "TK5.01#3", "text": "FLAG 1: RUSHED IDOLIZATION & CHAMELEON MIMICRY", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "FLAG 2: BOUNDARY VIOLATIONS & SUBTLE SURVEILLANCE", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "FLAG 3: SPLITTING COGNITION & VIOLENT MOOD SWINGS", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "FLAG 4: PROPERTY DAMAGE & ESCALATING SEPARATION THREATS", "dur_s": 2.5},
            {"after_id": "TK5.01#9", "text": "UNCOMFORTABLE INTUITION IS A LIFESAVING BIOLOGICAL GIFT", "dur_s": 3.0}
        ],
        "overlay_ja": [
            {"after_id": "TK5.01#1", "text": "生き残るための4つの危険信号 · 恐怖の知性", "dur_s": 2.5},
            {"after_id": "TK5.01#3", "text": "第1の警告：急激な理想化とカメレオン的同一化", "dur_s": 2.5},
            {"after_id": "TK5.01#5", "text": "第2の警告：境界線の侵害と日常的な監視行動", "dur_s": 2.5},
            {"after_id": "TK5.01#7", "text": "第3の警告：白黒思考と激しい感情のジェットコースター", "dur_s": 2.5},
            {"after_id": "TK5.01#8", "text": "第4の警告：別れを告げられた際の脅迫と器物破損", "dur_s": 2.5},
            {"after_id": "TK5.01#9", "text": "違和感を覚える直感こそ最大の自己防衛システムである", "dur_s": 3.0}
        ],
        "lines_meta": [
            ("5.06#1", "neutral", -0.02, 0.5, "t15_redflag2_frantic_efforts_avoid_abandonment", "pan"),
            ("5.06#2", "neutral", -0.02, 0.5, "t15_desert_monument_dawn_freedom", "pull"),
            ("5.06#4", "neutral", -0.02, 0.5, "t15_travis_foundation_scholarship_plaque", "push"),
            ("5.07#1", "neutral", -0.02, 0.5, "t15_redflag1_unstable_intense_relationships", "pan"),
            ("5.07#2", "neutral", -0.02, 0.5, "t15_personal_boundary_stone_wall_garden", "pull"),
            ("5.07#4", "neutral", -0.02, 0.5, "t15_truth_shines_desert_highway_horizon", "push"),
            ("5.08#1", "neutral", -0.02, 0.5, "t15_redflag3_identity_disturbance_mirror", "push"),
            ("5.08#3", "neutral", -0.02, 0.5, "t15_jodi_arias_a5_05_mirror", "pull"),
            ("5.10#3", "neutral", -0.02, 0.0, "t15_b54_jodi_arias_a5_08_arizona", "still")
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
        "VI": '# KẾ HOẠCH CLIP TIKTOK — TẬP 15 · "CƠN CUỒNG GHEN RỐI LOẠN NHÂN CÁCH RANH GIỚI (JODI ARIAS)"',
        "EN": '# TIKTOK CLIPS PLAN — EPISODE 15 · "BORDERLINE PERSONALITY DISORDER & FATAL OBSESSION (JODI ARIAS)"',
        "JA": '# TIKTOKクリップ計画 — 第15話 ·「境界性パーソナリティ障害と致命的執着（ジョディ・アリアス事件）」'
    }[lang_code]

    plan_lines.append(plan_header_title)
    plan_lines.append("")
    plan_lines.append(f"*Ngôn ngữ: **{lang_code}** · Nguồn dữ liệu: master Tập 15 · Tỷ lệ đọc ASR thật.*")
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

    # Ghi file KE_HOACH_CLIP_TAP15
    plan_filename = f"KE_HOACH_CLIP_TAP15{'' if lang_code == 'VI' else '_' + lang_code}.md"
    (out_dir / plan_filename).write_text("\n".join(plan_lines), encoding="utf-8")

    # Ghi file SPEC_AUDIO_CLIP_TAP15.json
    (out_dir / "SPEC_AUDIO_CLIP_TAP15.json").write_text(json.dumps(spec_audio, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[{lang_code}] Generated plan & spec successfully in {out_dir}")
    for cid, d in durations.items():
        print(f"  {cid}: {d}s")

if __name__ == "__main__":
    for code in ["VI", "EN", "JA"]:
        build_lang_artifacts(code)
