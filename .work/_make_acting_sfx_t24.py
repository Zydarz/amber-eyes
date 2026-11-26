#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh bảng diễn xuất (acting) + bảng âm thanh (sfx) cho Tập 24 — 3 ngôn ngữ.

acting_tap24[_EN|_JA].json : { "1.02#1": [cảm xúc, lệch tốc độ, cao độ=0, null], ...,
                               "_pause_after": { "1.02#1": 0.5, ... } }
  - Cảm xúc lấy từ CHÚ DẪN DIỄN XUẤT của từng element trong kịch bản (G3: chỉ 4 cảm xúc
    an toàn neutral · sad · fearful · surprised).
  - Lệch tốc độ trong khoảng −0,06 … +0,02 (G4); cao độ LUÔN = 0 (G5).
  - `_pause_after` ĐO TỪ TIMELINE THẬT của từng ngôn ngữ (A13: mỗi ngôn ngữ một file,
    khoảng nghỉ 0,2–1,2 s).

sfx_tap24[_EN|_JA].json : { "ambience": [[câu_đầu, câu_cuối, file, dB]],
                             "cues": [[mốc, 'start'|'end', lệch_s, file, dB]] }
  - Đọc bởi build_audio3.py::place_sheet(); file thiếu -> bỏ qua, không làm hỏng tập.

Dùng:  py -3 .work/_make_acting_sfx_t24.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
SFX = ROOT / "assets" / "sfx"

# ------------------------------------------------------------------ diễn xuất
# element -> (cảm xúc, lệch tốc độ) — bám đúng chú dẫn diễn xuất trong kịch bản
DIRECTION = {
    "1.02": ("sad", -0.02),        # giọng trầm, nỗi xót xa lịch sử
    "1.04": ("neutral", 0.00),     # tái hiện chiến dịch điều tra
    "1.05": ("neutral", -0.01),    # điềm đạm, phân tích điểm mù nhận thức
    "1.06": ("sad", -0.03),        # giọng trầm lắng, huyền thoại xã hội
    "1.08": ("sad", -0.03),        # nỗi đau kéo dài ba thập kỷ
    "1.09": ("fearful", -0.02),    # N1 bàng hoàng, xót xa
    "1.11": ("neutral", 0.00),     # bước đột phá ADN 2019
    "1.12": ("neutral", 0.02),     # D điềm tĩnh, đanh thép
    "1.13": ("neutral", 0.00),     # khép lại Hồi 1
    "2.02": ("neutral", -0.04),    # tiết tấu chậm rãi
    "2.04": ("neutral", -0.01),    # xây dựng lòng tin
    "2.05": ("neutral", -0.01),    # cơ chế thú tội không sợ hãi
    "2.07": ("fearful", -0.02),    # lời thú tội kinh hoàng
    "2.09": ("sad", -0.02),        # nhìn lại sai lầm đau xót
    "2.10": ("neutral", 0.00),     # động cơ thú tội khi hết thời hiệu
    "2.11": ("neutral", 0.00),     # khép lại Hồi 2
    "3.02": ("neutral", -0.04),    # chậm rãi, dẫn nhập chuyên môn
    "3.03": ("neutral", -0.01),    # C điềm đạm, học thuật
    "3.04": ("neutral", -0.01),    # tiếp nối nghịch lý thú tội
    "3.05": ("neutral", -0.01),    # tâm lý tự mãn
    "3.06": ("neutral", -0.01),    # hiện tượng Coerced Confession
    "3.07": ("neutral", -0.01),    # lời thú tội cưỡng bức
    "3.08": ("neutral", 0.02),     # D đanh thép, chiêm nghiệm
    "3.09": ("neutral", 0.00),     # chốt lại Hồi 3
    "4.02": ("neutral", 0.00),     # tái hiện phiên toà tái thẩm 2020
    "4.04": ("neutral", 0.00),     # tuyên án trắng án
    "4.06": ("sad", -0.03),        # D cúi đầu tạ tội
    "4.07": ("neutral", -0.02),    # trang nghiêm
    "4.08": ("sad", -0.01),        # chấn thương đạo đức
    "4.10": ("neutral", 0.00),     # bản án chung thân
    "4.11": ("sad", -0.03),        # N2 nghẹn ngào, kiên cường
    "4.12": ("neutral", 0.00),     # Đạo luật Taewan
    "4.13": ("neutral", -0.01),    # đúc kết khoa học hình sự
    "4.14": ("neutral", 0.00),     # khép lại Hồi 4
    "5.02": ("sad", -0.04),        # suy ngẫm, triết lý
    "5.03": ("neutral", 0.02),     # D trách nhiệm không bỏ cuộc
    "5.04": ("neutral", -0.01),    # tội phạm săn mồi ban đêm
    "5.05": ("neutral", 0.00),     # dấu hiệu cảnh báo + lời kết
}

# ------------------------------------------------------------------ âm thanh
# (mốc trong kịch bản, file, lệch s, dB) — file phải tồn tại trong assets/sfx/
SFX_CUES = [
    ("1.03", "police_siren_distant.wav", 0.0, -22),    # còi xe cảnh sát trong đêm
    ("1.03", "fx_footsteps_run_gravel.wav", 0.6, -24),  # bước chân chạy trên nền đất bùn
    ("1.07", "paper_rustle.wav", 0.0, -24),             # lật hồ sơ lưu trữ cũ
    ("1.07", "fx_sigh_emotional.wav", 1.1, -22),       # thở dài nặng nhọc
    ("1.10", "keyboard_night.wav", 0.0, -26),          # gõ phím trong phòng thí nghiệm
    ("1.10", "fx_dtmf_touch_tone_beep.wav", 1.4, -28), # bíp máy quét quang học
    ("2.03", "fx_glasses_clink.wav", 0.0, -30),        # kim loại rít (THAY THẾ: không có tiếng ghế)
    ("2.06", "fx_breathing_tense_close.wav", 0.0, -24),  # hít một hơi thật sâu
    ("2.06", "fx_glasses_clink.wav", 1.2, -30),        # đặt cốc giấy xuống bàn (THAY THẾ)
    ("2.08", "card_flip.wav", 0.0, -26),               # lật trang tài liệu điều tra
    ("2.08", "fx_sigh_emotional.wav", 1.3, -24),       # thở dài phẫn uất của sĩ quan
    ("4.03", "gavel.wav", 0.0, -14),                   # búa toà
    ("4.03", "fx_crowd_relief_sigh.wav", 0.9, -20),    # vỗ tay nghẹn ngào
    ("4.05", "fx_mouse_click_rapid.wav", 0.0, -24),    # máy ảnh bấm tanh tách
    ("4.05", "amb_tv_camera_operator.wav", 0.2, -26),  # xôn xao phóng viên
    ("4.09", "fx_door_kick_boot.wav", 0.0, -16),       # cánh cửa sắt nặng nề
    ("4.09", "chains.wav", 0.8, -22),                  # xiềng xích
    ("5.05", "stamp_thud.wav", 0.0, -18),              # thẻ kết hồ sơ
]

# nền môi trường theo hồi: (mốc đầu, mốc cuối, file, dB)
AMBIENCE_BY_ACT = {
    1: ("rain_loop.wav", -33),          # mưa đêm đồng ruộng, sương mù 1986–1991
    2: ("amb_ceiling_fan.wav", -34),    # tiếng quạt trần phòng thẩm vấn Busan
    3: ("amb_hospital_monitor_heartbeat.wav", -33),  # phòng thí nghiệm ADN
    4: ("amb_crowd_murmur_courtroom.wav", -33),      # toà án Suwon
    5: ("amb_tv_camera_operator.wav", -35),          # Hwaseong hiện đại, bình minh
}


def pause_value(gap, cross):
    """Khoảng nghỉ sau câu (A13): 0,2–1,2 s. Chỉ ghi khi đáng kể."""
    if cross:
        if gap >= 1.45:
            return 0.8
        if gap >= 1.20:
            return 0.7
        if gap >= 1.05:
            return 0.6
        return 0.5
    if gap >= 0.90:
        if gap >= 1.20:
            return 0.6
        if gap >= 1.05:
            return 0.5
        return 0.4
    return None


def make_acting(script_path, tl_path, out_path, lang):
    script = json.loads(script_path.read_text(encoding="utf-8"))
    tl = json.loads(tl_path.read_text(encoding="utf-8"))
    items = tl["items"]

    # cảm xúc / tốc độ theo element
    emo, spd = {}, {}
    for e in script:
        if e.get("kind") != "LOI":
            continue
        d = DIRECTION.get(e["id"], ("neutral", -0.01))
        for s in e.get("sentences", []):
            emo[s["id"]] = d[0]
            spd[s["id"]] = d[1]

    # khoảng nghỉ đo từ timeline thật
    pause = {}
    for a, b in zip(items, items[1:]):
        gap = b["start"] - a["end"]
        cross = a["element"] != b["element"]
        v = pause_value(gap, cross)
        if v is not None:
            pause[a["id"]] = v

    out = {}
    for it in items:
        sid = it["id"]
        out[sid] = [emo.get(sid, "neutral"), spd.get(sid, -0.01), 0, None]
    out["_doc"] = (f"Diễn xuất từng câu cho TTS bản {lang.upper()} Tập 24 — Hồ sơ Lee Choon-jae "
                   f"(Hwaseong). id: [cảm xúc, lệch tốc độ, cao độ=0, lời đọc riêng hoặc null]. "
                   "Cảm xúc lấy từ chú dẫn diễn xuất của element trong kịch bản; "
                   "_pause_after đo từ timeline_s_*.json của chính ngôn ngữ này (A13). "
                   "G3/G4/G5 — sinh bởi .work/_make_acting_sfx_t24.py")
    out["_pause_after"] = dict(sorted(pause.items()))
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    n = sum(1 for k in out if not k.startswith("_"))
    return n, len(pause)


def make_sfx(script_path, out_path):
    script = json.loads(script_path.read_text(encoding="utf-8"))
    ids = {e["id"] for e in script}
    # mốc đầu/cuối mỗi hồi (theo câu thoại đầu/cuối)
    act_first, act_last = {}, {}
    for e in script:
        if e.get("kind") != "LOI":
            continue
        ss = e.get("sentences", [])
        if not ss:
            continue
        a = e.get("act")
        act_first.setdefault(a, ss[0]["id"])
        act_last[a] = ss[-1]["id"]

    amb = []
    for a in sorted(act_first):
        if a not in AMBIENCE_BY_ACT:
            continue
        name, db = AMBIENCE_BY_ACT[a]
        amb.append([act_first[a], act_last[a], name, db])

    cues = []
    missing = []
    for ref, name, off, db in SFX_CUES:
        if ref not in ids:
            missing.append(ref)
            continue
        if not (SFX / name).exists():
            missing.append(name)
            continue
        cues.append([ref, "start", off, name, db])

    out = {
        "_doc": ("Bảng âm thanh stereo Tập 24 — Hồ sơ Lee Choon-jae (Hwaseong). "
                 "Đọc bởi build_audio3.py::place_sheet(). "
                 " ambience: [câu đầu, câu cuối, file, dB] · cues: [mốc, 'start'|'end', lệch s, file, dB]. "
                 "Ghi chú: 2.03 (tiếng ghế kim loại) và 2.06 (tiếng đặt cốc) dùng file kim loại "
                 "thay thế vì thư viện SFX chưa có tiếng ghế/cốc."),
        "ambience": amb,
        "cues": cues,
    }
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return len(amb), len(cues), missing


def main():
    for lang, suffix in (("vi", ""), ("en", "_EN"), ("ja", "_JA")):
        script = WORK / f"script_tap24{suffix}.json"
        tl = WORK / f"timeline_s{suffix}_t24.json"
        n, p = make_acting(script, tl, WORK / f"acting_tap24{suffix}.json", lang)
        a, c, miss = make_sfx(script, WORK / f"sfx_tap24{suffix}.json")
        print(f"{lang}: acting {n} câu · _pause_after {p} mục ({p/n:.0%}) | "
              f"sfx ambience {a} · cues {c}" + (f" · THIẾU {miss}" if miss else ""))


if __name__ == "__main__":
    main()
