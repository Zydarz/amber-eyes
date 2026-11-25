# -*- coding: utf-8 -*-
"""Danh sach nen DOC 9:16 cho 5 clip TikTok Tap 06 + nguon 16:9 goc.

Nguon su that: quet tu 02_SAN_XUAT/TIKTOK/Tap06{,_EN,_JA}/SPEC_AUDIO_CLIP_TAP06.json
  54 shot · 22 nen duy nhat (ma t6_*) · bang ke hoach TikTok Tap 06.
  -> TACH nen cho dat H22 (mot nen toi da 3 shot VA 30 s / clip):
     · TK3 t6_diner_booth_confrontation: 4 shot / 33,7-36,4 s  => tach #7
     · TK5 t6_redflag_trick_handcuffs   : 4 shot / 30,9-35,9 s  => tach #6+#7
     · t6_psychological_mask_metaphor  : 7 shot / 55-77 s ca tap => tach 4 shot
     · t6_two_faces_silhouette: KHONG co anh 16:9 goc trong assets/bg/_raw
       => dung t6_four_masks_psychiatric.jpg lam anh tham chieu.

AI-that: dung anh nen 16:9 goc cua Tap 06 lam ANH THAM CHIEU cho MiniMax 9:16 (area 2K)
-> giu dung chu de + bang mau + net muc cua tap (dong phong cach game / graphic novel noir).

Xuat: .work/tk_img_raw_t06/tk06_<ten>.jpg -> assets/bg/tk06_<ten>.png (1080x1920)
"""
import os

ROOT = r"D:/TEST/Gax/amber-eyes"
RAW = os.path.join(ROOT, "assets/bg/_raw")

# (ten nen doc 9:16, ten file nguon 16:9 trong assets/bg/_raw)
PAIRS = [
    # --- TK1 : hieu ung hao quang + mat na cong dan ---
    ("tk06_clown_mirror_chiaroscuro", "t6_clown_mirror_chiaroscuro.png"),
    ("tk06_polish_parade_chicago_1978", "t6_polish_parade_chicago_1978.png"),
    ("tk06_secret_service_pin_handshake", "t6_secret_service_pin_handshake.png"),
    ("tk06_clown_costume_closet", "t6_clown_costume_closet.jpg"),
    ("tk06_psychological_mask_metaphor", "t6_psychological_mask_metaphor.png"),
    ("tk06_psychological_mask_twin_silhouette", "t6_broken_mirror_narcissism.png"),
    ("tk06_closing_rose_closed_dossier", "t6_closing_rose_closed_dossier.png"),
    # --- TK2 : thu doan gay an + chu ky tam ly ---
    ("tk06_redflag_trick_handcuffs", "t6_redflag_trick_handcuffs.png"),
    ("tk06_pharmacy_counters_renovation", "t6_pharmacy_counters_renovation.png"),
    ("tk06_highschool_ring_jas", "t6_highschool_ring_jas.png"),
    ("tk06_crawlspace_trapdoor_opened", "t6_crawlspace_trapdoor_opened.jpg"),
    # --- TK3 : tu dac ai ky + quyen luc ---
    ("tk06_diner_booth_confrontation", "t6_diner_booth_confrontation.jpg"),
    ("tk06_gas_station_neon_midnight", "t6_gas_station_neon_midnight.png"),
    ("tk06_police_entry_summerdale", "t6_police_entry_summerdale.jpg"),
    ("tk06_diner_counter_officers", "t6_diner_booth_confrontation.jpg"),
    # --- TK4 : chia nghan tam tri + 26 bi mat duoi san nha ---
    ("tk06_crawlspace_subterranean_tunnel", "t6_crawlspace_subterranean_tunnel.png"),
    ("tk06_forensic_trowel_damp_soil", "t6_forensic_trowel_damp_soil.jpg"),
    ("tk06_flashlight_beam_lime_dust", "t6_flashlight_beam_lime_dust.png"),
    ("tk06_gacy_house_daylight_winter", "t6_gacy_house_daylight_winter.jpg"),
    ("tk06_compartmentalization_floor_section", "t6_psychological_floor_cross_section.jpg"),
    # KHONG co t6_two_faces_silhouette trong _raw => dung anh 16:9 "hai khuon mat"
    # t5_two_faces_silhouette.jpg (cung kien thuc: mat chia doi, hai ngan keo biet lap)
    ("tk06_two_faces_silhouette", "t5_two_faces_silhouette.jpg"),
    # --- TK5 : 4 dau hieu canh bao do ---
    ("tk06_redflag_charity_facade", "t6_redflag_charity_facade.png"),
    ("tk06_deserted_parking_lot_snow", "t6_deserted_parking_lot_snow.png"),
    ("tk06_handcuff_trick_demonstration", "t6_handcuff_trick_demonstration.jpg"),
    ("tk06_redflag_externalized_blame", "t6_redflag_externalized_blame.png"),
    ("tk06_dossier_gacy_case_06", "t6_dossier_gacy_case_06.png"),
]

MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}

# --------------------------------------------------------------------------
# PROMPT: giong bo tk01..tk05 da xuat ban (graphic novel noir = phong cach game).
# "Picture 1" = anh nen 16:9 goc cua Tap 06 (anh tham chieu).
# --------------------------------------------------------------------------
STYLE = (
    "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, "
    "bold black ink linework, high contrast psychological chiaroscuro lighting, "
    "deep pitch-black shadows, cold desaturated grey-blue palette, faded eerie retro colors, "
    "decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
    "gloomy overcast suffocating atmosphere, cold mist, unsettling silence, creeping psychological dread, "
    "hidden crime scene atmosphere, "
)

FRAME = (
    "Recompose the scene of Picture 1 as a full-bleed vertical 9:16 illustration for a mobile phone video. "
    "Keep exactly the same subject, mood, ink linework, palette, lighting direction and level of detail "
    "as Picture 1. Extend the scene upward and downward so it fills the vertical frame naturally: "
    "continue the wall, the floor, the ceiling and the background, no letterboxing, no black bars, "
    "no borders, no frame. Place the main subject in the middle band of the frame and keep the upper "
    "third and the lower third as quiet, dark, low-contrast shadow areas where captions can be overlaid. "
    "If a person is present, keep them a fully dark silhouette seen from behind or in profile, with no "
    "facial features visible, no visible eyes and no expression. "
)

NEG = (
    "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, "
    "no 3D render, no CGI, no photorealism, no photographic look, "
    "strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, "
    "no captions, no subtitles, no title, no border, no letterbox bars, no collage, no split screen"
)

PROMPT_KEEP = STYLE + FRAME + NEG

# Scene rieng cho 5 nen MO (doi goc / doi chu de) — giu dung bo net muc cua tap.
SCENE_NEW = {
    # TK1.01#7 · TK2.01#6 · TK3.01#8 — "mat na" / "tu thoi mien" / "ao tuong toan nang"
    "tk06_psychological_mask_twin_silhouette": (
        "Transform Picture 1 into a new scene: a lone man's dark silhouette standing in front of a "
        "shattered mirror, the reflection split into two separate halves staring in opposite directions, "
        "symbolizing two totally isolated mental compartments. "
        "Keep the exact ink linework, palette, chiaroscuro lighting and level of detail of Picture 1. "
        "Build a full-bleed vertical 9:16 composition, continue the wall, the floor and the background "
        "upward and downward, no letterboxing, no black bars, no borders, no frame. "
        "Place the silhouette in the middle band of the frame and keep the upper third and the lower third "
        "as quiet, dark, low-contrast shadow areas where captions can be overlaid. "
        "The figure must be a fully dark silhouette seen from behind or in profile, with no facial features, "
        "no visible eyes and no expression. " + NEG
    ),
    # TK4.01#6 — "chia nghan nhan thuc": mat cat ngang nha, khoang am bi che giu
    "tk06_compartmentalization_floor_section": (
        "Transform Picture 1 into a new scene: a dark architectural cross-section cutaway of a modest "
        "suburban house, revealing a hidden crawlspace beneath the living room floor and a narrow secret "
        "tunnel running under the bedroom, a dim trapdoor opening in the wooden floorboards above. "
        "Keep the exact ink linework, palette, chiaroscuro lighting and level of detail of Picture 1. "
        "Build a full-bleed vertical 9:16 composition, no letterboxing, no black bars, no borders, no frame. "
        "Keep the upper third and the lower third as quiet, dark, low-contrast shadow areas where captions "
        "can be overlaid. No people in this image. " + NEG
    ),
    # TK4.01#7 — "hai ngan keo biet lap": mat bo chia doi
    "tk06_two_faces_silhouette": (
        "Transform Picture 1 into a new scene: a single man's dark silhouette whose face is split down "
        "the middle into two completely separate halves, one mask-like half hanging loose and detached, "
        "cold empty clinical room shadow behind him. "
        "Keep the exact ink linework, palette, chiaroscuro lighting and level of detail of Picture 1. "
        "Build a full-bleed vertical 9:16 composition, continue the wall and the floor upward and downward, "
        "no letterboxing, no black bars, no borders, no frame. "
        "Place the silhouette in the middle band of the frame and keep the upper third and the lower third "
        "as quiet, dark, low-contrast shadow areas where captions can be overlaid. "
        "No facial features, no visible eyes, no expression. " + NEG
    ),
    # TK3.01#7 — goc nhin moi cung booc: vien canh sat nhu khán giả
    "tk06_diner_counter_officers": (
        "Recompose the SAME scene of Picture 1 from a DIFFERENT camera angle: a wide view from behind two "
        "uniformed police officers seated at the diner counter as an audience, the man in the booth seen "
        "beyond them as a dark silhouette, empty glasses and a beer mug on the counter. "
        "Keep the same booth, the same ink linework, palette, lighting direction and level of detail as "
        "Picture 1. Build a full-bleed vertical 9:16 composition, continue the wall, the floor, the ceiling "
        "and the background upward and downward, no letterboxing, no black bars, no borders, no frame. "
        "Keep the upper third and the lower third as quiet, dark, low-contrast shadow areas where captions "
        "can be overlaid. "
        "All people are fully dark silhouettes seen from behind, no facial features, no visible eyes, "
        "no expression. " + NEG
    ),
    # TK5.01#6 + #7 — "coi tro do dua" that bai
    "tk06_handcuff_trick_demonstration": (
        "Recompose the SAME scene of Picture 1 from a DIFFERENT camera angle: a tight close-up of an adult "
        "hand holding out an open handcuff towards a hesitant teenager's outstretched wrist, cold metal "
        "catching a thin rim of light. "
        "Keep the same ink linework, palette, lighting direction and level of detail as Picture 1. "
        "Build a full-bleed vertical 9:16 composition, continue the wall and the floor upward and downward, "
        "no letterboxing, no black bars, no borders, no frame. "
        "Keep the upper third and the lower third as quiet, dark, low-contrast shadow areas where captions "
        "can be overlaid. "
        "Both hands are dark silhouettes, no facial features, no visible eyes, no expression. " + NEG
    ),
}


def prompt_for(name):
    return SCENE_NEW.get(name, PROMPT_KEEP)


def src_path(ref):
    return os.path.join(RAW, ref)


def missing_sources():
    return [(n, r) for n, r in PAIRS if not os.path.exists(src_path(r))]


if __name__ == "__main__":
    print("so nen can sinh:", len(PAIRS))
    miss = missing_sources()
    print("thieu nguon 16:9:", miss if miss else "khong co")
    for n, r in PAIRS:
        print("  %-38s <- %-42s %s" % (n, r, "MO" if n in SCENE_NEW else ""))
