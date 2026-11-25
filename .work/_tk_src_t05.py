# -*- coding: utf-8 -*-
"""Danh sach 32 nen DOC 9:16 can cho 5 clip TikTok Tap 05 + nguon 16:9 goc.

Nguon su that: .work/_tk05_bg_needed.json (quet tu KE_HOACH_CLIP_TAP05.md):
  54 shot · 32 nen duy nhat · chi 1 nen khong co nguon 16:9 (t5_closing_desk)
  -> khop sang anh goc THAT cua Tap 05: t5_closing_typewriter_rose.png
     (dung o shot 5.10#1-#3 "ket tap" cua ban YouTube Tap 05).

AI-that: dung 32 anh 16:9 goc lam ANH THAM CHIEU cho MiniMax 9:16 (area 2K)
-> giu dung chu de + bang mau + net muc cua tap.
"""
import os

ROOT = r"D:/TEST/Gax/amber-eyes"
RAW = os.path.join(ROOT, "assets/bg/_raw")

# (ten nen doc 9:16, ten file nguon 16:9 trong assets/bg/_raw)
PAIRS = [
    # --- TK1 : chiec dia mem mau tim ---
    ("tk05_handwritten_note_floppy", "t5_handwritten_note_floppy.jpg"),
    ("tk05_newspaper_classified_494", "t5_newspaper_classified_494.jpg"),
    ("tk05_purple_floppy_disk", "t5_purple_floppy_disk.png"),
    ("tk05_digital_forensics_lab", "t5_digital_forensics_lab.png"),
    ("tk05_metadata_screen", "t5_metadata_screen.png"),
    ("tk05_church_website_search", "t5_church_website_search.png"),
    ("tk05_interrogation_confrontation", "t5_interrogation_confrontation.png"),
    ("tk05_amber_eyes_dossier_05", "t5_amber_eyes_dossier_05.png"),
    # --- TK2 : hieu ung hao quang ---
    ("tk05_rader_house_park_city", "t5_rader_house_park_city.png"),
    ("tk05_lutheran_church_exterior", "t5_lutheran_church_exterior.png"),
    ("tk05_scout_camp_campfire", "t5_scout_camp_campfire.png"),
    ("tk05_compliance_truck_street", "t5_compliance_truck_street.png"),
    ("tk05_compliance_measuring_tape", "t5_compliance_measuring_tape.png"),
    ("tk05_two_faces_silhouette", "t5_two_faces_silhouette.jpg"),
    ("tk05_concrete_wall_divide", "t5_concrete_wall_divide.framefix.png"),
    ("tk05_family_dinner_warmth", "t5_family_dinner_warmth.png"),
    # --- TK3 : nhoi no tam ly ---
    ("tk05_fear_of_oblivion", "t5_fear_of_oblivion.png"),
    ("tk05_detective_war_room", "t5_detective_war_room.png"),
    ("tk05_book_manuscript_desk", "t5_book_manuscript_desk.png"),
    ("tk05_narcissist_mirror_shadow", "t5_narcissist_mirror_shadow.png"),
    ("tk05_btk_signature_letter", "t5_btk_signature_letter.png"),
    ("tk05_factor_x_shadow", "t5_factor_x_shadow.png"),
    ("tk05_projection_mask", "t5_projection_mask.png"),
    # --- TK4 : bien kich nguoi than ---
    ("tk05_kerri_rawson_tears", "t5_kerri_rawson_tears.png"),
    ("tk05_highway_takedown_arrest", "t5_highway_takedown_arrest.png"),
    ("tk05_shattered_mask_confession", "t5_shattered_mask_confession.jpg"),
    # 2 nen tach them de dat H22 (nen cu toi da 5 shot / 37 s trong TK4)
    ("tk05_narcissistic_throne", "t5_narcissistic_throne.png"),
    ("tk05_darkened_house_exterior", "t5_darkened_house_exterior.jpg"),
    # --- TK5 : 4 dau hieu canh bao do ---
    ("tk05_solitary_confinement_cell", "t5_solitary_confinement_cell.png"),
    ("tk05_redflag_rule_control", "t5_redflag_rule_control.png"),
    ("tk05_redflag_shallow_affect", "t5_redflag_shallow_affect.png"),
    ("tk05_redflag_secret_trophies", "t5_redflag_secret_trophies.jpg"),
    ("tk05_redflag_narcissistic_hubris", "t5_redflag_narcissistic_hubris.jpg"),
    ("tk05_closing_desk", "t5_closing_typewriter_rose.png"),
]

MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}

# Prompt phong cach: giong bo tk01/tk02/tk03/tk04 da xuat ban (graphic novel noir).
# "Picture 1" = anh nen 16:9 goc cua Tap 05 (anh tham chieu).
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
    return [(n, r) for n, r in PAIRS if not os.path.exists(src_path(r))]


if __name__ == "__main__":
    print("so nen can sinh:", len(PAIRS))
    miss = missing_sources()
    print("thieu nguon 16:9:", miss if miss else "khong co")
    for n, r in PAIRS:
        print("  %-34s <- %s" % (n, r))
