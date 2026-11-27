#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Client module for Cloudflare Workers AI FLUX.1.
Reusable for all episodes in Amber Eyes pipeline.
Upgraded to match Kaggle Deep Noir standard:
  - 4-Tier Deep Noir Prompt Architecture
  - Lanczos 2K Resampling (2112x1188)
  - Color Grading: Mute Saturation (-35%) & Boost Contrast (+15%)
  - Post-processing: 4-Corner Vignette (-45%) + 35mm Film Grain
  - Multi-Account Auto-Failover (HTTP 429 quota rotation)
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

def get_account_pool():
    """Retrieve all configured Cloudflare accounts for automatic rotation and failover."""
    accounts = []
    
    # 1. Check .cloudflare_accounts (pool file)
    pool_file = WORK / ".cloudflare_accounts"
    if pool_file.exists():
        cur_acc = {}
        for line in pool_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.startswith("[") and line.endswith("]"):
                if cur_acc.get("id") and cur_acc.get("token"):
                    accounts.append(cur_acc)
                cur_acc = {}
            elif line.startswith("CLOUDFLARE_ACCOUNT_ID="):
                cur_acc["id"] = line.split("=", 1)[1].strip().strip('"').strip("'")
            elif line.startswith("CLOUDFLARE_API_TOKEN="):
                cur_acc["token"] = line.split("=", 1)[1].strip().strip('"').strip("'")
        if cur_acc.get("id") and cur_acc.get("token"):
            accounts.append(cur_acc)
            
    # 2. Check legacy single-key files if pool is empty
    if not accounts:
        for key_file in [WORK / ".flux_key", WORK / ".cloudflare_key"]:
            if key_file.exists():
                acc_id, tok = "", ""
                for line in key_file.read_text(encoding="utf-8").splitlines():
                    line = line.strip()
                    if line.startswith("CLOUDFLARE_ACCOUNT_ID="):
                        acc_id = line.split("=", 1)[1].strip().strip('"').strip("'")
                    elif line.startswith("CLOUDFLARE_API_TOKEN="):
                        tok = line.split("=", 1)[1].strip().strip('"').strip("'")
                if acc_id and tok:
                    accounts.append({"id": acc_id, "token": tok})
                    break

    # 3. Environment variables fallback
    env_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip()
    env_tok = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
    if env_id and env_tok and not any(a["id"] == env_id for a in accounts):
        accounts.insert(0, {"id": env_id, "token": env_tok})
        
    return accounts

def get_credentials():
    """Get the primary active account credentials."""
    pool = get_account_pool()
    if pool:
        return pool[0]["id"], pool[0]["token"]
    return "", ""

# Track the index of the currently active working account
# 2026-11-27: ACCOUNT_7 (index 6) added — fresh quota, tried first; failover walks back to 5,4,...0
_ACTIVE_ACCOUNT_INDEX = 6

def generate_image(prompt, steps=4, timeout=60, max_retries=3, model=DEFAULT_MODEL):
    """Call Cloudflare Workers AI FLUX.1 with automatic multi-account failover on 429 quota exhaustion."""
    global _ACTIVE_ACCOUNT_INDEX
    pool = get_account_pool()
    if not pool:
        raise RuntimeError("Không tìm thấy Cloudflare credentials trong .work/.cloudflare_accounts!")
        
    payload = json.dumps({"prompt": prompt, "steps": steps}).encode("utf-8")
    
    # Try through available accounts starting from active index
    attempts_total = len(pool)
    for pool_attempt in range(attempts_total):
        acc_idx = (_ACTIVE_ACCOUNT_INDEX + pool_attempt) % len(pool)
        acc = pool[acc_idx]
        account_id = acc["id"]
        api_token = acc["token"]
        
        url = f"https://api.cloudflare.com/client/v4/accounts/{account_id}/ai/run/{model}"
        headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
        
        success = False
        quota_exhausted = False
        
        for attempt in range(1, max_retries + 1):
            try:
                req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
                with urllib.request.urlopen(req, timeout=timeout) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                    if data.get("success") and "result" in data and "image" in data["result"]:
                        img_bytes = base64.b64decode(data["result"]["image"])
                        _ACTIVE_ACCOUNT_INDEX = acc_idx # remember this working account
                        return Image.open(BytesIO(img_bytes)).convert("RGB")
                    raise RuntimeError(f"Cloudflare FLUX error: {data}")
            except urllib.error.HTTPError as e:
                err = e.read().decode("utf-8", errors="replace")
                if e.code == 429 or "used up your daily free allocation" in err or "10,000 neurons" in err:
                    print(f"\n[QUOTA CẢNH BÁO] Account {acc_idx+1} ({account_id[:6]}...{account_id[-4:]}) đã hết quota neurons (HTTP 429).")
                    quota_exhausted = True
                    break # immediately switch to next account
                if attempt == max_retries:
                    raise RuntimeError(f"HTTP {e.code} from Cloudflare (Account {account_id[:6]}): {err}")
                time.sleep(2 * attempt)
            except Exception as ex:
                if attempt == max_retries:
                    raise
                time.sleep(2 * attempt)
                
        if quota_exhausted:
            next_idx = (acc_idx + 1) % len(pool)
            print(f"-> TỰ ĐỘNG CHUYỂN SANG ACCOUNT {next_idx+1} ({pool[next_idx]['id'][:6]}...{pool[next_idx]['id'][-4:]})")
            continue
            
    raise RuntimeError("Tất cả các tài khoản Cloudflare trong pool đều đã hết hạn mức (Quota Exhausted)!")

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
    h_arr, w_arr, _ = arr.shape
    y, x = np.ogrid[:h_arr, :w_arr]
    cx, cy = w_arr / 2, h_arr / 2
    dist = np.sqrt((x - cx)**2 + (y - cy)**2)
    max_dist = np.sqrt(cx**2 + cy**2)
    
    # Smooth cosine vignette (45% edge darkening)
    vignette = 1.0 - 0.45 * (dist / max_dist)**2.2
    vignette = np.clip(vignette, 0.40, 1.0)
    arr = arr * vignette[..., np.newaxis]
    
    # Fine 35mm film grain
    grain = np.random.normal(0, 5.0, arr.shape)
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
    print("Cloudflare FLUX Multi-Account Client Ready.")
    pool = get_account_pool()
    print(f"Loaded {len(pool)} account(s) in pool:")
    for i, a in enumerate(pool, 1):
        print(f"  [{i}] ID: {a['id'][:6]}...{a['id'][-4:]} | Token: {a['token'][:8]}...{a['token'][-4:]}")
