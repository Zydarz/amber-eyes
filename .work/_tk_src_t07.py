# -*- coding: utf-8 -*-
"""Danh sach nen DOC 9:16 cho 5 clip TikTok Tap 07 + nguon 16:9 goc.

Nguon su that: quet tu 02_SAN_XUAT/TIKTOK/Tap07{,_EN,_JA}/SPEC_AUDIO_CLIP_TAP07.json
  50 shot · 28 nen duy nhat (ma t7_*) · dung chung cho ca 3 ngon ngu.
  -> TACH nen cho dat H22 (mot nen toi da 3 shot VA 30 s / tap):
     · t7_digital_lighthouse_beacon: 4 shot (TK1#2, TK5#1, TK5#2, TK5#8)
       => tach 2 + 2 bang 2 GOC QUAY khac nhau cua cung mot canh.
     · t7_closing_dossier_white_rose: 5 shot = the CTA (the chet) cua 5 clip
       => giu 1 nen (dung tien le Tập 06: tk06_closing_rose_closed_dossier 6 shot).

AI-that: dung anh nen 16:9 goc cua Tap 07 lam ANH THAM CHIEU cho MiniMax 9:16 (area 2K)
-> giu dung chu de + bang mau + net muc cua tap (dong phong cach game / graphic novel noir).

Xuat: .work/tk_img_raw_t07/tk07_<ten>.jpg -> assets/bg/tk07_<ten>.png (1080x1920)
"""
import os

ROOT = r"D:/TEST/Gax/amber-eyes"
RAW = os.path.join(ROOT, "assets/bg/_raw")

# (ten nen doc 9:16, ten file nguon 16:9 trong assets/bg/_raw)
PAIRS = [
    # --- TK1 : toi pham khong cham tay + phan quyet lich su ---
    ("tk07_digital_coercion_screen", "t7_digital_coercion_screen.png"),
    ("tk07_digital_lighthouse_beacon", "t7_digital_lighthouse_beacon.png"),
    ("tk07_social_media_notifications_flood", "t7_social_media_notifications_flood.png"),
    ("tk07_copied_script_lines_notebook", "t7_copied_script_lines_notebook.jpg"),
    ("tk07_courtroom_breathless_silence", "t7_courtroom_breathless_silence.jpg"),
    ("tk07_courtroom_projection_screen", "t7_courtroom_projection_screen.png"),
    ("tk07_court_verdict_document_guilty", "t7_court_verdict_document_guilty.jpg"),
    ("tk07_closing_dossier_white_rose", "t7_closing_dossier_white_rose.png"),
    # --- TK2 : kich ban bien kich viet san + ngoi no tam ly ---
    ("tk07_confession_message_turn", "t7_confession_message_turn.png"),
    ("tk07_ticking_clock_deadlines", "t7_ticking_clock_deadlines.png"),
    ("tk07_cracked_porcelain_mask", "t7_cracked_porcelain_mask.png"),
    ("tk07_staged_tragedy_mirror", "t7_staged_tragedy_mirror.png"),
    ("tk07_puppet_strings_metaphor", "t7_puppet_strings_metaphor.png"),
    ("tk07_night_sky_breath_of_life", "t7_night_sky_breath_of_life.png"),
    # --- TK3 : hoi chung Munchausen qua mang + chu ky tam ly ---
    ("tk07_drama_masks_digital_glitch", "t7_drama_masks_digital_glitch.jpg"),
    ("tk07_vintage_tv_glee_glow", "t7_vintage_tv_glee_glow.jpg"),
    ("tk07_clinical_depression_shadow", "t7_clinical_depression_shadow.png"),
    ("tk07_psychological_coercion_chess", "t7_psychological_coercion_chess.jpg"),
    ("tk07_baseball_field_charity_empty", "t7_baseball_field_charity_empty.png"),
    # --- TK4 : dong tin nhan tu thu + menh lenh trong bom toi ---
    ("tk07_confession_text_timestamp", "t7_confession_text_timestamp.png"),
    ("tk07_witness_trembling_phone", "t7_witness_trembling_phone.png"),
    ("tk07_incoming_call_timer_40min", "t7_incoming_call_timer_40min.jpg"),
    ("tk07_two_phone_screens_contrast", "t7_two_phone_screens_contrast.png"),
    ("tk07_bristol_county_indictment_stamp", "t7_bristol_county_indictment_stamp.jpg"),
    # --- TK5 : 4 dau hieu canh bao do sinh ton ---
    ("tk07_redflag1_isolated_virtual_bubble", "t7_redflag1_isolated_virtual_bubble.png"),
    ("tk07_redflag2_manipulative_text_provocation", "t7_redflag2_manipulative_text_provocation.png"),
    ("tk07_redflag3_performative_grief_stage", "t7_redflag3_performative_grief_stage.png"),
    ("tk07_redflag4_disconnect_phone_dawn", "t7_redflag4_disconnect_phone_dawn.png"),
    # --- TACH H22 : goc quay thu 2 cua phong hai (TK5#1, TK5#8) ---
    ("tk07_digital_lighthouse_beacon_wide", "t7_digital_lighthouse_beacon.png"),
]

MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}

# --------------------------------------------------------------------------
# PROMPT: giong bo tk01..tk06 da xuat ban (graphic novel noir = phong cach game).
# "Picture 1" = anh nen 16:9 goc cua Tap 07 (anh tham chieu).
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

# Mo ta trong tam canh (giup model giu dung chu de cua anh 16:9 goc)
SCENE = {
    "tk07_digital_coercion_screen": (
        "a dark room dominated by a cold glowing smartphone screen held close, a shadowy hand and a "
        "web of faint signal lines, the sense of someone being controlled at a distance"
    ),
    "tk07_digital_lighthouse_beacon": (
        "a lone lighthouse beam sweeping across a black night sea toward a fogbound distant shoreline, "
        "a tiny cold phone glow in the foreground darkness"
    ),
    "tk07_social_media_notifications_flood": (
        "a teenager's face lit from below by a smartphone overflowing with stacked glowing "
        "notification bubbles, the room around swallowed by darkness"
    ),
    "tk07_copied_script_lines_notebook": (
        "an open notebook filled with repeated handwritten lines beside a phone and a pen on a desk, "
        "cold desk lamp light, a rehearsed script for a tragedy"
    ),
    "tk07_courtroom_breathless_silence": (
        "a silent courtroom with an empty wooden witness bench and rows of vacant seats, cold air, "
        "shafted light falling from high windows"
    ),
    "tk07_courtroom_projection_screen": (
        "a courtroom dominated by a large glowing projection screen above the judge's bench, "
        "evidence thrown cold across the room"
    ),
    "tk07_court_verdict_document_guilty": (
        "a judge's hand resting beside a sealed verdict document bearing a dark official stamp, "
        "a wooden gavel at the edge of the frame, cold courtroom light"
    ),
    "tk07_closing_dossier_white_rose": (
        "a closed case dossier lying on a dark desk with a single white rose resting on it, "
        "a black ribbon, a shaft of cold light, the calm of a finished investigation"
    ),
    "tk07_confession_message_turn": (
        "a smartphone screen caught at the instant a message turns into a confession, the glow of the "
        "screen cutting across a dark bedroom, the hand holding it beginning to shake"
    ),
    "tk07_ticking_clock_deadlines": (
        "a wall clock ticking in a dim room above scattered papers and a phone, the sense of deadlines "
        "closing in, cold grey light"
    ),
    "tk07_cracked_porcelain_mask": (
        "a cracked porcelain theatre mask resting on a dark table, a fracture running across the cheek, "
        "a cold rim of light along the edge, the break point of a psyche"
    ),
    "tk07_staged_tragedy_mirror": (
        "a mirror reflecting a girl holding a perfectly staged pose of grief while her real silhouette "
        "stands in shadow behind, the double exposed"
    ),
    "tk07_puppet_strings_metaphor": (
        "thin marionette strings descending out of darkness toward a small human silhouette below, "
        "cold light catching the strings, a self that cannot let the play end"
    ),
    "tk07_night_sky_breath_of_life": (
        "a vast night sky above black water with a single pale luminous breath of light on the horizon, "
        "vast cold emptiness"
    ),
    "tk07_drama_masks_digital_glitch": (
        "a row of theatre drama masks breaking apart into scattered digital glitch fragments, "
        "a glowing screen behind them"
    ),
    "tk07_vintage_tv_glee_glow": (
        "an old cathode television glowing in a dark living room, a girl's silhouette sitting close to "
        "the screen, the warm halo of the tube against the cold room"
    ),
    "tk07_clinical_depression_shadow": (
        "a clinical office chair swallowed by a cold shadow, a girl sitting very still and perfectly "
    "composed, a plain desk, flat overcast light"
    ),
    "tk07_psychological_coercion_chess": (
        "a chessboard where the pieces are small human figures, a shadowed hand moving one of them, "
        "a person reduced to a pawn on someone's emotional board"
    ),
    "tk07_baseball_field_charity_empty": (
        "an empty baseball field at dusk with a charity banner on the fence and vacant bleachers, "
        "a single spotlight waiting on the stage"
    ),
    "tk07_confession_text_timestamp": (
        "a phone screen showing one long confession text with a small timestamp, held in two trembling "
        "hands in a dark room, the glow washing out the face above it"
    ),
    "tk07_witness_trembling_phone": (
        "hands trembling while holding a phone in a dark room, the screen light cutting up through the "
        "fingers, shock and horror"
    ),
    "tk07_incoming_call_timer_40min": (
        "a phone screen showing an incoming call with a long running timer, the dark interior of a "
    "parked vehicle, cold instrument glow"
    ),
    "tk07_two_phone_screens_contrast": (
        "two phone screens lying side by side in the dark, one glaringly bright and the other dimmer, "
        "two points of view on the same conversation"
    ),
    "tk07_bristol_county_indictment_stamp": (
        "a county prosecution indictment folder lying open on a desk with a heavy official stamp, "
        "cold fluorescent light, a thick case file"
    ),
    "tk07_redflag1_isolated_virtual_bubble": (
        "a small isolated figure alone inside a glowing translucent digital bubble floating in the dark, "
        "cut off from every other light"
    ),
    "tk07_redflag2_manipulative_text_provocation": (
        "a phone screen crowded with manipulative message threads, a shadowy hand typing, the glow "
        "throwing sharp light across an empty chair"
    ),
    "tk07_redflag3_performative_grief_stage": (
        "a staged public mourning on a spotlighted stage, a figure performing grief before a crowd, "
        "a theatrical curtain of darkness"
    ),
    "tk07_redflag4_disconnect_phone_dawn": (
        "a phone left switched off and disconnected on a windowsill at cold pale dawn, a dark bedroom "
        "behind it, the first light of a day without the manipulation"
    ),
}

# Scene rieng cho 1 nen MO (doi goc) — dung H22 cho t7_digital_lighthouse_beacon
SCENE_NEW = {
    # TK5.01#1 + TK5.01#8 — cung phong hai, nhung GOC QUAY XA HON
    "tk07_digital_lighthouse_beacon_wide": (
        "Transform Picture 1 into a new scene: the SAME lighthouse seen from a much wider and more "
        "distant camera angle, its rotating beam cutting across the night sky over a vast black ocean, "
        "a tiny cold phone glow barely visible far below in the foreground darkness, most of the frame "
        "given over to empty dark sky and sea. "
        "Keep the exact ink linework, palette, chiaroscuro lighting and level of detail of Picture 1. "
        "Build a full-bleed vertical 9:16 composition, continue the sky, the horizon and the sea "
        "upward and downward, no letterboxing, no black bars, no borders, no frame. "
        "Place the lighthouse in the middle band of the frame and keep the upper third and the lower "
        "third as quiet, dark, low-contrast shadow areas where captions can be overlaid. "
        "No people in this image. " + NEG
    ),
}

PROMPT_KEEP = STYLE + FRAME + NEG


def prompt_for(name):
    if name in SCENE_NEW:
        return SCENE_NEW[name]
    scene = SCENE.get(name, "")
    if not scene:
        return PROMPT_KEEP
    return (STYLE + "Scene content: " + scene + ". " + FRAME + NEG)


def src_path(ref):
    return os.path.join(RAW, ref)


def missing_sources():
    return [(n, r) for n, r in PAIRS if not os.path.exists(src_path(r))]


if __name__ == "__main__":
    print("so nen can sinh:", len(PAIRS))
    miss = missing_sources()
    print("thieu nguon 16:9:", miss if miss else "khong co")
    for n, r in PAIRS:
        print("  %-44s <- %-42s %s" % (n, r, "MO" if n in SCENE_NEW else ""))
