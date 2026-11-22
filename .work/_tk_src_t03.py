# -*- coding: utf-8 -*-
"""Danh sach 28 nen DOC 9:16 can cho 5 clip TikTok Tap 03 + nguon 16:9 goc.

Nguon su that: .work/_tk03_bg_needed.json (quet tu KE_HOACH_CLIP_TAP03.md).
Thu tu theo clip TK1 -> TK5 de QC de doi ten (shot nao dung nen nao).
"""
import json
import os

ROOT = r"D:/TEST/Gax/amber-eyes"
RAW = os.path.join(ROOT, "assets/bg/_raw")

# (ten nen doc 9:16, ten file nguon 16:9 trong assets/bg/_raw)
PAIRS = [
    # --- TK1 : phone booth Santa Cruz ---
    ("tk03_phone_booth", "t3_phone_booth.jpg"),
    ("tk03_dispatch_desk", "t3_dispatch_desk.jpg"),
    ("tk03_apartos_house", "t3_apartos_house.framefix.png"),
    ("tk03_brain_mirror", "t3_brain_mirror.png"),
    ("tk03_closing_desk", "t3_closing_desk.png"),
    # --- TK2 : quan rua The Jury Room ---
    ("tk03_bar_stool_shadow", "t3_bar_stool_shadow.png"),
    ("tk03_bar_jury_room", "t3_bar_jury_room.png"),
    ("tk03_galaxie", "t3_galaxie.framefix.png"),
    ("tk03_hitchhiker", "t3_hitchhiker.png"),
    # --- TK3 : tang ham Montana ---
    ("tk03_basement_stairs", "t3_basement_stairs.png"),
    ("tk03_coal_furnace", "t3_coal_furnace.png"),
    ("tk03_small_bed", "t3_small_bed.png"),
    ("tk03_trapdoor", "t3_trapdoor.png"),
    ("tk03_mother_shadow", "t3_mother_shadow.jpg"),
    ("tk03_ucsc_campus", "t3_ucsc_campus.jpg"),
    # --- TK4 : nha tu Vacaville 1978 ---
    ("tk03_vacaville_1978", "t3_vacaville_1978.png"),
    ("tk03_two_agents", "t3_two_agents.png"),
    ("tk03_giant_doorway", "t3_giant_doorway.png"),
    ("tk03_interview_room", "t3_interview_room.jpg"),
    ("tk03_cassette", "t3_cassette.png"),
    ("tk03_fantasy_spiral", "t3_fantasy_spiral.png"),
    ("tk03_trophy_box", "t3_trophy_box.png"),
    ("tk03_organized_split", "t3_organized_split.png"),
    ("tk03_self_observation", "t3_self_observation.jpg"),
    ("tk03_case_photos", "t3_case_photos.png"),
    # --- TK5 : 4 ho chuong canh bao ---
    ("tk03_red_flags", "t3_red_flags.png"),
    ("tk03_gift_drowned", "t3_gift_drowned.png"),
    ("tk03_life_sentence", "t3_life_sentence.png"),
]

MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}

# Prompt phong cach: giong bo tk01/tk02 da xuat ban (graphic novel noir).
# "Picture 1" = anh nen 16:9 goc cua Tap 03 (anh tham chieu).
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
        print("  %-24s <- %s" % (n, r))
