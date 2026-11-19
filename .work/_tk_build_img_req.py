"""Build request cho 16 anh nen DOC 9:16 cho clip TikTok Tap 01.

Dung anh nen 16:9 cua Tap 01 lam ANH THAM CHIEU (reference_images) de giu dung
chu de + bang mau + net muc cua tap, khong ve lai tu dau.

Output: .work/_tk_img_req_t01.json  (mcp goi connector__matrix__generate_image)
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE / "_tk_refs_t01.json"
OUT = HERE / "_tk_img_req_t01.json"

# Thu tu uu tien: theo thu tu xuat hien trong SPEC_AUDIO_CLIP_TAP01.json
NAMES = [
    "interrogation_gypsy", "crowd_house", "brain_desk", "records",
    "pinboard", "doll", "spotlight_deedee", "podcast_desk",
    "wheelchair_room", "cage", "cage_open", "hands",
    "house_night", "clinical", "crowd_away", "two_shadows",
]

STYLE = (
    "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, "
    "bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
    "cold desaturated grey-blue palette, faded eerie retro colors, decayed autumn tones, "
    "fine 35mm film grain, David Fincher meets vintage crime comic style, "
    "gloomy overcast suffocating atmosphere, cold mist, unsettling silence, creeping psychological dread, "
    "hidden crime scene atmosphere"
)

TASK = (
    "Recompose the scene of Picture 1 as a full-bleed vertical 9:16 illustration for a mobile phone video. "
    "Keep exactly the same subject, mood, ink linework, palette, lighting direction and level of detail as Picture 1. "
    "Extend the scene upward and downward so it fills the vertical frame naturally: continue the wall, the floor, "
    "the ceiling and the background, no letterboxing, no black bars, no borders, no frame. "
    "Place the main subject in the middle band of the frame and keep the upper third and the lower third as quiet, "
    "dark, low-contrast shadow areas where captions can be overlaid. "
    "If a person is present, keep them a fully dark silhouette seen from behind or in profile, with no facial features visible, "
    "no visible eyes and no expression."
)

NEG = (
    "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, "
    "no 3D render, no CGI, no photorealism, no photographic look, "
    "strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, "
    "no captions, no subtitles, no title, no border, no letterbox bars, no collage, no split screen"
)


def main():
    import sys
    # Tool gioi han 10 request/lot -> chia 2 lo 8 + 1 lo 3 cho 3 nen con lai
    batch = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    if batch == 3:
        names = ["clinical", "crowd_away", "two_shadows"]
        refs_path = HERE / "_tk_refs_t01_b3.json"
        out_path = HERE / "_tk_img_req_t01_b3.json"
    else:
        names = NAMES[(batch - 1) * 8: batch * 8]
        refs_path = REFS
        out_path = HERE / ("_tk_img_req_t01_b%d.json" % batch)

    refs = json.loads(refs_path.read_text(encoding="utf-8-sig"))
    missing = [n for n in names if n not in refs]
    if missing:
        raise SystemExit("thieu anh tham chieu: %s" % missing)

    requests = []
    for n in names:
        requests.append({
            "prompt": f"{STYLE}, {TASK} {NEG}",
            "reference_images": [{"url": refs[n], "mime_type": "image/png"}],
            "aspect_ratio": "9:16",
            "area": "2K",
            "n": 1,
            "output_format": "jpeg",
            "output_file": f"tk01_{n}",
        })

    out_path.write_text(json.dumps({"requests": requests}, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    print("lot %d: %d requests -> %s" % (batch, len(requests), out_path))


if __name__ == "__main__":
    main()
