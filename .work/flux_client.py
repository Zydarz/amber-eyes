#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Client module for Cloudflare Workers AI FLUX.1.
Reusable for all episodes in Amber Eyes pipeline.
Upgraded to match Kaggle Deep Noir standard:
  - 4-Tier Deep Noir Prompt Architecture
  - Lanczos 2K Resampling (2112x1188)
  - Color Grading: Mute Saturation (-35%) & Boost Contrast (+15%)
  - Post-processing: 4-Corner Vignette (-45%) + 35mm Film Grain
"""
import os
import sys
import json
import time
import base64
import urllib.request
import urllib.error
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageEnhance
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

DEFAULT_MODEL = "@cf/black-forest-labs/flux-1-schnell"

# Deep Noir Prompts matching QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §2
STYLE_PREFIX = (
    "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, "
    "bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
)
ATMOSPHERE_CORE = (
    "gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, "
    "creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, "
    "decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
)
STYLE_SUFFIX = (
    "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, "
    "no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, "
    "no signs, no labels, no logos, no watermark, full-bleed 16:9."
)

def get_credentials():
    """Retrieve Account ID and API Token from env or key files."""
    account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip()
    api_token = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
    
    for key_file in [WORK / ".flux_key", WORK / ".cloudflare_key"]:
        if key_file.exists():
            for line in key_file.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                if line.startswith("CLOUDFLARE_ACCOUNT_ID="):
                    if not account_id:
                        account_id = line.split("=", 1)[1].strip().strip('"').strip("'")
                elif line.startswith("CLOUDFLARE_API_TOKEN="):
                    if not api_token:
                        api_token = line.split("=", 1)[1].strip().strip('"').strip("'")
                        
    return account_id, api_token

def generate_image(prompt, steps=4, timeout=60, max_retries=3, model=DEFAULT_MODEL):
    """Call Cloudflare Workers AI FLUX.1-schnell and return PIL Image (1024x1024)."""
    account_id, api_token = get_credentials()
    if not account_id or not api_token:
        raise RuntimeError("Missing Cloudflare FLUX credentials in .work/.flux_key or environment variables.")
        
    url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}"
    payload = json.dumps({"prompt": prompt, "steps": steps}).encode("utf-8")
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    
    for attempt in range(1, max_retries + 1):
        try:
            req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                if data.get("success") and "result" in data and "image" in data["result"]:
                    img_bytes = base64.b64decode(data["result"]["image"])
                    return Image.open(BytesIO(img_bytes)).convert("RGB")
                raise RuntimeError(f"Cloudflare FLUX error: {data}")
        except urllib.error.HTTPError as e:
            err = e.read().decode("utf-8", errors="replace")
            if attempt == max_retries:
                raise RuntimeError(f"HTTP {e.code} from Cloudflare: {err}")
            time.sleep(2 * attempt)
        except Exception as ex:
            if attempt == max_retries:
                raise
            time.sleep(2 * attempt)

def post_process_noir(base_img, out_size=(2112, 1188)):
    """Apply Kaggle Deep Noir post-processing standard (QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §4)."""
    # 1. 16:9 center crop & Lanczos upscale
    w, h = base_img.size
    target_h = int(w * 9 / 16)
    top = (h - target_h) // 2
    im_16_9 = base_img.crop((0, top, w, top + target_h))
    img_2k = im_16_9.resize(out_size, Image.Resampling.LANCZOS)
    
    # 2. Color Grading: Mute Saturation 35% & Boost Contrast 15%
    color_enhancer = ImageEnhance.Color(img_2k)
    img_muted = color_enhancer.enhance(0.65)
    
    contrast_enhancer = ImageEnhance.Contrast(img_muted)
    img_contrast = contrast_enhancer.enhance(1.15)
    
    # 3. Noir Vignette & 35mm Film Grain
    arr = np.array(img_contrast, dtype=np.float32)
    h_arr, w_arr, c = arr.shape
    y, x = np.ogrid[:h_arr, :w_arr]
    cx, cy = w_arr / 2, h_arr / 2
    dist = np.sqrt((x - cx)**2 + (y - cy)**2)
    max_dist = np.sqrt(cx**2 + cy**2)
    
    # 4-corner vignette
    vignette = 1.0 - 0.45 * (dist / max_dist)**1.8
    vignette = np.clip(vignette, 0.4, 1.0)[:, :, np.newaxis]
    arr = arr * vignette
    
    # Film grain
    np.random.seed(42)
    grain = np.random.normal(0, 7.5, arr.shape)
    arr = np.clip(arr + grain, 0, 255).astype(np.uint8)
    
    return Image.fromarray(arr)

def generate_16_9_background(prompt, steps=4, out_size=(2112, 1188), with_noir_style=True):
    """Generate 16:9 background cropped, graded and styled to Amber Eyes standard."""
    if with_noir_style:
        full_prompt = f"{STYLE_PREFIX}{prompt}, {ATMOSPHERE_CORE} {STYLE_SUFFIX}"
    else:
        full_prompt = prompt
        
    raw_img = generate_image(full_prompt, steps=steps)
    return post_process_noir(raw_img, out_size=out_size)

if __name__ == "__main__":
    acc, tok = get_credentials()
    print("Cloudflare FLUX Client Upgraded.")
