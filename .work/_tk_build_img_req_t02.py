# -*- coding: utf-8 -*-
"""Build request cho 26 anh nen DOC 9:16 cho clip TikTok Tap 02.

Dung anh nen 16:9 GOC cua Tap 02 (assets/bg/_raw/t2_*) lam ANH THAM CHIEU
(reference_images) de giu dung chu de + bang mau + net muc cua tap, khong ve lai
tu dau — giong het cach Tap 01 lam (.work/_tk_build_img_req.py).

Output: .work/_tk_img_req_t02_b{1,2,3}.json
        (mcp goi connector__matrix__generate_image, toi da 10 request/lot)
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
REFS = HERE / "_tk_refs_t02.json"

# Thu tu uoc tien: theo thu tu xuat hien trong SPEC_AUDIO_CLIP_TAP02.json.
# LAY TRUC TIEP tu generator kich ban (import) de .md / .json / anh nen khong bao
# gio chung — khong hardcode lai danh sach.
def used_names():
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "_build_tk_tap02", str(HERE / "_build_tk_tap02.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    seen, out = set(), []
    for c in m.CLIPS:
        for ln in c["lines"]:
            n = ln[4]
            if n not in seen:
                seen.add(n)
                out.append(n)
    return out


NAMES = used_names()

# Giu NGUYEN wording cua Tap 01 de 5 clip TikTok + 16 nen tk01_* dong bo phong cach
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

RAW = HERE.parent / "assets" / "bg" / "_raw"


def mime_of(name):
    """mime_type thuc te cua file goc 16:9 (uu tien .png roi .jpg)."""
    base = name.replace("tk02_", "t2_")
    for ext, mime in ((".png", "image/png"), (".jpg", "image/jpeg")):
        if (RAW / (base + ext)).exists():
            return mime
    return "image/jpeg"


MIME = {}  # tk02_* -> mime_type cua file goc


def main():
    batch = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    refs = json.loads(REFS.read_text(encoding="utf-8-sig"))
    names = NAMES[(batch - 1) * 10: batch * 10]
    if not names:
        raise SystemExit("batch %d rong" % batch)
    missing = [n for n in names if n not in refs]
    if missing:
        raise SystemExit("thieu anh tham chieu: %s" % missing)

    requests = []
    for n in names:
        requests.append({
            "prompt": f"{STYLE}, {TASK} {NEG}",
            "reference_images": [{"url": refs[n], "mime_type": mime_of(n)}],
            "aspect_ratio": "9:16",
            "area": "2K",
            "n": 1,
            "output_format": "jpeg",
            "output_file": n,
        })

    out_path = HERE / ("_tk_img_req_t02_b%d.json" % batch)
    out_path.write_text(json.dumps({"requests": requests}, ensure_ascii=False, indent=1),
                        encoding="utf-8")
    print("lot %d: %d requests -> %s" % (batch, len(requests), out_path))


if __name__ == "__main__":
    main()
