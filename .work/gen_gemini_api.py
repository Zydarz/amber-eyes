#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Batch image generator for Episode 07 using Google AI Studio (Imagen 3 REST API).
Generates 16:9 backgrounds and saves them at 2112x1188 PNG into assets/bg/.
"""
import argparse
import base64
import json
import os
import sys
import time
import urllib.request
from datetime import date
from io import BytesIO
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
BG_DIR = ROOT / "assets" / "bg"
PROV_FILE = ROOT / "provenance.json"

STYLE_PREFIX = (
    "Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink linework, "
    "deep chiaroscuro lighting, subtle mist and film grain, desaturated muted palette, ominous quiet tension, highly detailed. "
)
STYLE_SUFFIX = (
    " Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
    "no watermark, no frame, no letterbox bars, full-bleed image."
)

MODEL = "imagen-3.0-generate-002"
ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:predict"


def get_api_key(cli_key=None):
    if cli_key:
        return cli_key.strip()
    if os.environ.get("GEMINI_API_KEY"):
        return os.environ["GEMINI_API_KEY"].strip()
    key_file = WORK / ".gemini_key"
    if key_file.exists():
        return key_file.read_text(encoding="utf-8").strip()
    root_key = ROOT / ".gemini_key"
    if root_key.exists():
        return root_key.read_text(encoding="utf-8").strip()
    return None


def call_imagen(prompt, api_key, tries=3):
    url = f"{ENDPOINT}?key={api_key}"
    payload = {
        "instances": [
            {"prompt": prompt}
        ],
        "parameters": {
            "sampleCount": 1,
            "aspectRatio": "16:9",
            "outputMimeType": "image/jpeg"
        }
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=data,
        headers={"Content-Type": "application/json"}
    )
    for attempt in range(tries):
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                res_body = resp.read().decode("utf-8")
                res_json = json.loads(res_body)
                preds = res_json.get("predictions", [])
                if not preds:
                    raise RuntimeError(f"No predictions returned: {res_body[:200]}")
                b64 = preds[0].get("bytesBase64Encoded")
                return base64.b64decode(b64)
        except Exception as e:
            if attempt == tries - 1:
                raise
            print(f"    [Retry {attempt+1}/{tries}] Error: {e}")
            time.sleep(3 * (attempt + 1))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help="Google AI Studio API Key")
    parser.add_argument("--all", action="store_true", help="Regenerate all images including existing ones")
    parser.add_argument("--only", help="Comma-separated list of image names to generate")
    args = parser.parse_args()

    api_key = get_api_key(args.key)
    if not api_key:
        print("LỖI: Chưa có API Key! Hãy truyền qua --key <API_KEY> hoặc gán biến môi trường GEMINI_API_KEY hoặc lưu vào file .work/.gemini_key")
        sys.exit(1)

    jobs = json.loads((WORK / "bg_jobs_tap07.json").read_text(encoding="utf-8"))
    prov_list = json.loads(PROV_FILE.read_text(encoding="utf-8")) if PROV_FILE.exists() else []
    prov_by_file = {p["file"]: p for p in prov_list}

    # Already high-quality images from earlier turn
    ALREADY_DONE = {
        "t7_digital_coercion_screen",
        "t7_highway_50km_isolation",
        "t7_kmart_parking_lot_morning"
    }

    if args.only:
        only_set = set(args.only.split(","))
        jobs = [j for j in jobs if j["name"] in only_set]
    elif not args.all:
        jobs = [j for j in jobs if j["name"] not in ALREADY_DONE]

    print(f"Bắt đầu tạo {len(jobs)} ảnh nền bằng Imagen 3 (Google AI Studio)...")
    today_str = str(date.today())

    success = 0
    for idx, job in enumerate(jobs):
        name = job["name"]
        prompt = f"{STYLE_PREFIX}{job['prompt']}{STYLE_SUFFIX}"
        out_png = BG_DIR / f"{name}.png"
        rel_path = f"assets/bg/{name}.png"

        print(f"[{idx+1:02d}/{len(jobs)}] Đang tạo: {name} ...", end=" ", flush=True)
        try:
            img_bytes = call_imagen(prompt, api_key)
            with Image.open(BytesIO(img_bytes)) as im:
                orig_w, orig_h = im.size
                im_resized = im.resize((2112, 1188), Image.LANCZOS)
                im_resized.save(out_png, format="PNG")

            prov_by_file[rel_path] = {
                "file": rel_path,
                "loai": "nền 16:9",
                "cong_cu": f"models/{MODEL} (Google AI Studio Imagen 3)",
                "ngay": today_str,
                "prompt": prompt,
                "seed": None,
                "nguon_anh_tham_chieu": None,
                "kich_thuoc_goc": [orig_w, orig_h],
                "dieu_khoan": "Google Generative AI Commercial Terms",
                "kiem_tra_thuong_mai": "đạt"
            }
            success += 1
            print(f"XONG ({orig_w}x{orig_h} -> 2112x1188)")
        except Exception as e:
            print(f"THẤT BẠI: {e}")

        # Sleep slightly to respect RPM
        time.sleep(1.2)

    new_prov = list(prov_by_file.values())
    PROV_FILE.write_text(json.dumps(new_prov, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nHoàn thành! Đã tạo thành công {success}/{len(jobs)} ảnh.")


if __name__ == "__main__":
    main()
