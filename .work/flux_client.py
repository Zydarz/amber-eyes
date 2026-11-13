#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Client module for Cloudflare Workers AI FLUX.1.
Reusable for all episodes in Amber Eyes pipeline.

Usage:
    from flux_client import generate_16_9_background
    img = generate_16_9_background("A noir detective in rain...")
    img.save("assets/bg/my_scene.png")
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
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

DEFAULT_MODEL = "@cf/black-forest-labs/flux-1-schnell"

STYLE_PREFIX = (
    "Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink linework, "
    "deep chiaroscuro lighting, subtle mist and film grain, desaturated muted palette, ominous quiet tension, highly detailed. "
)
STYLE_SUFFIX = (
    " Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
    "no watermark, no frame, no letterbox bars, full-bleed image."
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

def generate_16_9_background(prompt, steps=4, out_size=(2112, 1188), with_noir_style=True):
    """Generate 16:9 background cropped and resized to Amber Eyes standard."""
    full_prompt = (STYLE_PREFIX + prompt + STYLE_SUFFIX) if with_noir_style else prompt
    im = generate_image(full_prompt, steps=steps)
    w, h = im.size
    # Center crop 16:9
    target_h = int(w * 9 / 16)
    top = (h - target_h) // 2
    im_16_9 = im.crop((0, top, w, top + target_h))
    return im_16_9.resize(out_size, Image.Resampling.LANCZOS)

if __name__ == "__main__":
    acc, tok = get_credentials()
    print("Cloudflare FLUX Client Test:")
    print(f"  Account ID: {acc[:6]}..." if acc else "  Account ID: NOT FOUND")
    print(f"  API Token:  {tok[:6]}..." if tok else "  API Token:  NOT FOUND")
    if acc and tok:
        print("Credentials loaded successfully!")
