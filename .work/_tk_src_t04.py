# -*- coding: utf-8 -*-
"""Danh sach 23 nen DOC 9:16 can cho 5 clip TikTok Tap 04 + nguon 16:9 goc.

Nguon su that: .work/_tk04_bg_needed.json (quet tu KE_HOACH_CLIP_TAP04.md).
Thu tu theo clip TK1 -> TK5 de QC de doi ten (shot nao dung nen nao).

LUU Y: 5 nen trong KE_HOACH_CLIP_TAP04.md vi ten KHONG ton tai o assets/bg/_raw/
(t4_closing_desk, t4_diner_exterior, t4_diner_booth, t4_wire_closeup,
t4_courtroom_bench). Da khop sang anh goc THAT cua Tap 04 theo
02_SAN_XUAT/Tap04/Danh_Sach_Anh_Tap04.md (bang mo ta noi dung tung anh).
"""
import os

ROOT = r"D:/TEST/Gax/amber-eyes"
RAW = os.path.join(ROOT, "assets/bg/_raw")

# (ten nen doc 9:16, ten file nguon 16:9 trong assets/bg/_raw)
PAIRS = [
    # --- TK1 : may cap phat thuoc Pyxis ---
    ("tk04_pyxis_station", "t4_pyxis_station.png"),
    ("tk04_pyxis_drawer_ajar", "t4_pyxis_drawer_ajar.jpg"),
    ("tk04_pyxis_printout", "t4_pyxis_printout.jpg"),
    ("tk04_neutral_letter", "t4_neutral_letter.png"),
    ("tk04_institutional_bystander", "t4_institutional_bystander.png"),
    # t4_closing_desk -> hồ sơ/bìa dây trên bàn làm việc (CTA "xem hồ sơ đầy đủ");
    # tach rieng tk04_case_file_open (t4_case_file_open.png) de khong trung anh
    ("tk04_closing_desk", "t4_cullen_law_doc.png"),
    # --- TK2 : hieu ung hao quang ---
    ("tk04_nurse_station", "t4_nurse_station.png"),
    ("tk04_somerset_exterior", "t4_somerset_exterior.png"),
    ("tk04_icu_night", "t4_icu_night.png"),
    ("tk04_cullen_silhouette", "t4_cullen_silhouette.png"),
    ("tk04_code_blue_aftermath", "t4_code_blue_aftermath.png"),
    ("tk04_breakroom_night", "t4_breakroom_night.jpg"),
    ("tk04_corridor_shadow", "t4_corridor_shadow.jpg"),
    # --- TK3 : cuoc doi dau tai quan an ---
    # t4_diner_exterior -> The Office Beer Bar (quán ăn ngoài trời)
    ("tk04_diner_exterior", "t4_somerville_diner.jpg"),
    # t4_diner_booth -> cuộc đối thoại qua bàn ăn
    ("tk04_diner_booth", "t4_diner_table.png"),
    ("tk04_amy_scrubs", "t4_amy_scrubs.jpg"),
    # t4_wire_closeup -> thiết bị ghi âm bí mật dưới áo len
    ("tk04_wire_closeup", "t4_wire_recorder.png"),
    ("tk04_interrogation_room", "t4_interrogation_room.png"),
    # --- TK4 : 16 nam im lang cua 9 benh vien ---
    ("tk04_ten_hospitals_map", "t4_ten_hospitals_map.jpg"),
    ("tk04_case_file_open", "t4_case_file_open.png"),
    # t4_courtroom_bench -> búa công lý trên bàn xử án
    ("tk04_courtroom_bench", "t4_judge_gavel.png"),
    # --- TK5 : bai hoc sinh ton ---
    ("tk04_somerset_courtroom", "t4_somerset_courtroom.jpg"),
    ("tk04_boardroom_empty", "t4_boardroom_empty.png"),
]

MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}

# Prompt phong cach: giong bo tk01/tk02/tk03 da xuat ban (graphic novel noir).
# "Picture 1" = anh nen 16:9 goc cua Tap 04 (anh tham chieu).
PROMPT = (
    "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, "
    "bold black ink linework, high contrast psychological chiaroscuro lighting, "
    "deep pitch-black shadows, cold desaturated grey-blue palette, faded eerie retro colors, "
    "decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
    "gloomy overcast suffocating atmosphere, cold mist, unsettling silence, creeping psychological dread, "
    "hidden crime scene atmosphere, "
    "Recompose the scene of Picture 1 as a full-bleed vertical 9:16 illustration for a mobile phone video. "
    "Keep exactly the same subject, mood, ink linework, palette, lighting direction and level of detail "
    "as Picture 1. Extend the scene upward and downward so it fills the vertical frame naturally: "
    "continue the wall, the floor, the ceiling and the background, no letterboxing, no black bars, "
    "no borders, no frame. Place the main subject in the middle band of the frame and keep the upper "
    "third and the lower third as quiet, dark, low-contrast shadow areas where captions can be overlaid. "
    "If a person is present, keep them a fully dark silhouette seen from behind or in profile, with no "
    "facial features visible, no visible eyes and no expression. "
    "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, "
    "no 3D render, no CGI, no photorealism, no photographic look, "
    "strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, "
    "no captions, no subtitles, no title, no border, no letterbox bars, no collage, no split screen"
)


def src_path(ref):
    return os.path.join(RAW, ref)


def missing_sources():
    out = []
    for name, ref in PAIRS:
        if not os.path.exists(src_path(ref)):
            out.append((name, ref))
    return out


if __name__ == "__main__":
    print("so nen can sinh:", len(PAIRS))
    miss = missing_sources()
    print("thieu nguon 16:9:", miss if miss else "khong co")
    for n, r in PAIRS:
        print("  %-28s <- %s" % (n, r))
