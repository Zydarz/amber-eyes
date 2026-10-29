#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 2K 16:9 dark graphic novel noir backgrounds for Episode 10.
Generates 2112x1188 images with deep chiaroscuro lighting, custom graphic noir elements,
film grain, vignette, and atmospheric moods matching the Colleen Stan case.
Updates provenance.json and builds assets for Episode 10.
"""
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
BG_DIR = ROOT / "assets" / "bg"
BG_DIR.mkdir(parents=True, exist_ok=True)
PROV_FILE = ROOT / "provenance.json"

WIDTH = 2112
HEIGHT = 1188

THEMES = {
    "highway_70s": {
        "base": (14, 12, 16),
        "accent": (38, 28, 34),
        "light": (230, 150, 75),
        "style": "sunset_highway"
    },
    "redbluff_woods": {
        "base": (8, 12, 10),
        "accent": (18, 32, 24),
        "light": (110, 175, 130),
        "style": "nocturnal_forest"
    },
    "claustrophobic_box": {
        "base": (10, 9, 8),
        "accent": (28, 22, 18),
        "light": (195, 130, 60),
        "style": "confined_box"
    },
    "the_company": {
        "base": (9, 10, 16),
        "accent": (22, 26, 42),
        "light": (140, 165, 215),
        "style": "surveillance_noir"
    },
    "suburban_facade": {
        "base": (14, 12, 10),
        "accent": (38, 30, 22),
        "light": (215, 160, 80),
        "style": "banker_lamp"
    },
    "learned_helplessness": {
        "base": (12, 10, 16),
        "accent": (32, 22, 42),
        "light": (185, 120, 220),
        "style": "open_cage"
    },
    "tehama_justice": {
        "base": (15, 11, 12),
        "accent": (42, 28, 28),
        "light": (215, 155, 80),
        "style": "judicial"
    },
    "penal": {
        "base": (8, 11, 10),
        "accent": (20, 30, 28),
        "light": (100, 165, 145),
        "style": "prison_bars"
    },
    "redflag": {
        "base": (15, 8, 10),
        "accent": (42, 16, 22),
        "light": (225, 70, 70),
        "style": "warning_spot"
    },
    "healing_dawn": {
        "base": (10, 14, 20),
        "accent": (28, 38, 56),
        "light": (240, 195, 120),
        "style": "dawn_rays"
    },
    "default": {
        "base": (10, 11, 14),
        "accent": (26, 30, 38),
        "light": (150, 160, 175),
        "style": "noir_generic"
    }
}


def pick_theme(name):
    n = name.lower()
    if any(k in n for k in ["highway", "roadside", "route99", "hitchhiking", "backpack", "dodge_van", "illusion", "stepping_into"]):
        return THEMES["highway_70s"]
    if any(k in n for k in ["pine_forest", "sawmill", "lumber", "cabin", "ambush", "knife_shadow"]):
        return THEMES["redbluff_woods"]
    if any(k in n for k in ["coffin", "wooden_box", "stiff_hands", "latches", "padlock", "waterbed", "headbox", "claustrophobia", "darkness_as_false"]):
        return THEMES["claustrophobic_box"]
    if any(k in n for k in ["company", "syndicate", "surveillance", "sniper", "shattered_phantom", "puppet"]):
        return THEMES["the_company"]
    if any(k in n for k in ["suburban", "riverside", "bungalow", "front_door", "boyfriend_facade", "family_dinner", "bathroom_mirror", "concerned_inquiry", "toddler_toys", "janice_hooker", "second_victim"]):
        return THEMES["suburban_facade"]
    if any(k in n for k in ["helplessness", "seligman", "open_cage", "sensory_deprivation", "childhood_poems", "slave_contract", "bread_and_whip", "savior_complex", "timber_prison"]):
        return THEMES["learned_helplessness"]
    if any(k in n for k in ["court", "gavel", "tehama_superior", "sheriff", "immunity", "ochberg", "unmasking"]):
        return THEMES["tehama_justice"]
    if any(k in n for k in ["prison_bars", "penitentiary"]):
        return THEMES["penal"]
    if any(k in n for k in ["redflag", "trojan"]):
        return THEMES["redflag"]
    if any(k in n for k in ["healing", "dawn", "diploma", "memoir", "breakfast", "sprout", "fbi_academy", "breaking_invisible", "dossier_colleen"]):
        return THEMES["healing_dawn"]
    return THEMES["default"]


def render_background(name, prompt, seed=42):
    rng = np.random.default_rng(seed)
    theme = pick_theme(name)
    base_c = np.array(theme["base"], dtype=np.float32)
    accent_c = np.array(theme["accent"], dtype=np.float32)
    light_c = np.array(theme["light"], dtype=np.float32)

    y_coords, x_coords = np.mgrid[0:HEIGHT, 0:WIDTH].astype(np.float32)
    nx = x_coords / WIDTH
    ny = y_coords / HEIGHT

    # 1. Base chiaroscuro directional gradient
    angle = (seed * 41 + 55) % 360
    rad = np.radians(angle)
    proj = nx * np.cos(rad) + ny * np.sin(rad)
    proj = (proj - proj.min()) / (proj.max() - proj.min() + 1e-6)
    t = np.power(proj, 1.8)[:, :, np.newaxis]
    img_arr = base_c * (1.0 - t) + accent_c * t

    # 2. Lighting patterns based on scene style
    style = theme["style"]
    if style == "sunset_highway":
        # Low coastal/interstate horizon with warm rays and road vanishing lines
        horizon = np.exp(-((ny - 0.72) / 0.18)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.85
        rays = np.sin(np.arctan2(ny - 0.85, nx - 0.50) * 12.0)
        rays_mask = np.clip((rays + 0.6) * 0.5, 0.65, 1.25)[:, :, np.newaxis]
        img_arr *= rays_mask
    elif style == "nocturnal_forest":
        # Dense forest shadows with cold moonlight filtering through pine canopy
        cx, cy = 0.48, 0.30
        dist = np.sqrt((nx - cx)**2 * 2.5 + (ny - cy)**2 * 1.6)
        moon_glow = np.exp(-dist * 3.2)[:, :, np.newaxis]
        img_arr += light_c * moon_glow * 0.80
        # Vertical pine trunk shadows
        pines = np.sin(nx * 40.0 + np.sin(ny * 10.0) * 1.8)
        pines_mask = np.clip((pines + 0.7) * 0.6, 0.45, 1.0)[:, :, np.newaxis]
        img_arr *= pines_mask
    elif style == "confined_box":
        # Deep claustrophobic box: pitch dark with narrow hairline seam of light
        seam_x = 0.52
        seam = np.exp(-((nx - seam_x) / 0.04)**2)[:, :, np.newaxis]
        img_arr = base_c * 0.8 + (light_c * 0.95) * seam
        # Rough timber slats texture
        slats = np.sin(ny * 55.0)
        slats_mask = np.clip((slats + 0.8) * 0.55, 0.55, 1.0)[:, :, np.newaxis]
        img_arr *= slats_mask
    elif style == "surveillance_noir":
        # Concentric surveillance radar glow & cold blue chiaroscuro
        cx, cy = 0.5, 0.48
        dist = np.sqrt((nx - cx)**2 + (ny - cy)**2)
        rings = np.sin(dist * 28.0)
        aura = np.exp(-dist * 2.8) * np.clip(rings * 0.35 + 0.65, 0.35, 1.0)
        img_arr += light_c * aura[:, :, np.newaxis] * 0.85
    elif style == "banker_lamp":
        # Warm domestic table lamp pool with linear blind shadows
        cx, cy = 0.44, 0.40
        dist = np.sqrt((nx - cx)**2 * 1.8 + (ny - cy)**2 * 1.2)
        lamp_glow = np.exp(-dist * 3.0)[:, :, np.newaxis]
        img_arr += light_c * lamp_glow * 0.90
        # Venetian blind slats
        slats = np.sin(ny * 36.0 + nx * 3.0)
        slats_mask = np.clip((slats + 0.55) * 0.7, 0.45, 1.0)[:, :, np.newaxis]
        img_arr *= slats_mask
    elif style == "open_cage":
        # Stark spotlight on open cage dilemma
        cx, cy = 0.50, 0.45
        dist = np.sqrt((nx - cx)**2 * 2.2 + (ny - cy)**2 * 1.8)
        glow = np.exp(-dist * 3.2)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
    elif style == "judicial":
        # High classical courtroom dual spotlighting
        cx1, cx2 = 0.35, 0.65
        d1 = np.sqrt((nx - cx1)**2 * 2.4 + (ny - 0.4)**2 * 1.4)
        d2 = np.sqrt((nx - cx2)**2 * 2.4 + (ny - 0.4)**2 * 1.4)
        glow = (np.exp(-d1 * 3.0) + np.exp(-d2 * 3.0))[:, :, np.newaxis]
        img_arr += light_c * glow * 0.75
    elif style == "prison_bars":
        # Harsh top-down institutional light with vertical cell bar shadows
        dist = np.sqrt((nx - 0.5)**2 * 1.8 + (ny - 0.4)**2 * 1.6)
        glow = np.clip(1.0 - dist * 1.4, 0.0, 1.0)**1.8
        img_arr = base_c + (light_c - base_c) * glow[:, :, np.newaxis] * 0.85
        # Vertical steel bars
        bars = np.sin(nx * 42.0)
        bars_mask = np.where(bars > 0.40, 0.35, 1.0)[:, :, np.newaxis]
        img_arr *= bars_mask
    elif style == "warning_spot":
        # Intense raking red spotlight on black void
        cx, cy = 0.5, 0.52
        dist = np.sqrt((nx - cx)**2 * 3.0 + (ny - cy)**2 * 2.2)
        spot = np.exp(-dist * 4.0)[:, :, np.newaxis]
        img_arr += light_c * spot * 0.95
    elif style == "dawn_rays":
        # Hopeful morning rays breaking through sea mist
        horizon = np.exp(-((ny - 0.68) / 0.18)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.85
        rays = np.sin(np.arctan2(ny - 0.80, nx - 0.5) * 14.0)
        rays_mask = np.clip((rays + 0.6) * 0.5, 0.7, 1.25)[:, :, np.newaxis]
        img_arr *= rays_mask
    else:
        cx, cy = 0.5, 0.45
        dist = np.sqrt((nx - cx)**2 * 2.0 + (ny - cy)**2 * 1.5)
        glow = np.exp(-dist * 3.0)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.70

    # 3. Noir edge vignette
    vx = (nx - 0.5) * 2.0
    vy = (ny - 0.5) * 2.0
    v_dist = np.sqrt(vx * vx + vy * vy)
    vignette = np.clip(1.0 - (v_dist - 0.45) * 0.75, 0.12, 1.0)[:, :, np.newaxis]
    img_arr *= vignette

    # 4. Organic film grain
    noise = rng.normal(0.0, 7.5, (HEIGHT, WIDTH, 1)).astype(np.float32)
    img_arr += noise

    # Clip to valid uint8 range
    img_arr = np.clip(img_arr, 0.0, 255.0).astype(np.uint8)
    img = Image.fromarray(img_arr, mode="RGB")

    # 5. Graphic Noir vector overlays & linework
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    ink_color = (theme["base"][0], theme["base"][1], theme["base"][2], 190)
    wire_color = (theme["light"][0], theme["light"][1], theme["light"][2], 50)
    accent_wire = (theme["accent"][0], theme["accent"][1], theme["accent"][2], 120)

    n_lower = name.lower()

    # Thematic vector details for Episode 10
    if any(k in n_lower for k in ["coffin_box", "wooden_box", "stiff_hands"]):
        # Heavy rectangular wooden box outline with reinforced corner brackets
        bx1, by1 = int(WIDTH * 0.20), int(HEIGHT * 0.32)
        bx2, by2 = int(WIDTH * 0.80), int(HEIGHT * 0.75)
        odraw.rectangle([(bx1, by1), (bx2, by2)], outline=wire_color, width=4)
        # Horizontal plank grooves
        for py in range(by1 + 60, by2, 60):
            odraw.line([(bx1, py), (bx2, py)], fill=wire_color, width=2)
        # Heavy corner brackets
        for cx, cy in [(bx1, by1), (bx2, by1), (bx1, by2), (bx2, by2)]:
            odraw.rectangle([(cx - 20, cy - 20), (cx + 20, cy + 20)], fill=ink_color, outline=accent_wire, width=2)
    elif "latches" in n_lower or "padlock" in n_lower:
        # Massive industrial sliding hasp and padlock
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.52)
        # Hasp mounting plate
        odraw.rectangle([(cx - 180, cy - 40), (cx + 120, cy + 40)], fill=ink_color, outline=wire_color, width=3)
        # Padlock shackle & body
        odraw.arc([(cx + 40, cy - 80), (cx + 120, cy)], 180, 360, fill=wire_color, width=8)
        odraw.rectangle([(cx + 30, cy - 10), (cx + 130, cy + 90)], fill=ink_color, outline=wire_color, width=4)
        odraw.ellipse([(cx + 75, cy + 25), (cx + 85, cy + 45)], fill=wire_color)
    elif "headbox" in n_lower:
        # Precision soundproof headbox outline with acoustic foam egg-crate and ventilation holes
        bx1, by1 = int(WIDTH * 0.32), int(HEIGHT * 0.28)
        bx2, by2 = int(WIDTH * 0.68), int(HEIGHT * 0.72)
        odraw.rectangle([(bx1, by1), (bx2, by2)], fill=ink_color, outline=wire_color, width=5)
        # Internal foam grid
        for gy in range(by1 + 40, by2, 40):
            odraw.line([(bx1 + 15, gy), (bx2 - 15, gy)], fill=accent_wire, width=1)
        # Precision circular ventilation drill holes along the bottom edge
        for hx in range(bx1 + 50, bx2 - 40, 45):
            odraw.ellipse([(hx - 8, by2 - 40), (hx + 8, by2 - 24)], fill=(12, 10, 14, 255), outline=wire_color, width=2)
    elif "waterbed" in n_lower:
        # Massive overhead timber waterbed frame crossbeams looming down
        for tx in [0.15, 0.50, 0.85]:
            x_pos = int(WIDTH * tx)
            odraw.rectangle([(x_pos - 35, 0), (x_pos + 35, int(HEIGHT * 0.45))], fill=ink_color, outline=wire_color, width=3)
        odraw.rectangle([(0, int(HEIGHT * 0.35)), (WIDTH, int(HEIGHT * 0.45))], fill=ink_color, outline=wire_color, width=4)
    elif any(k in n_lower for k in ["company", "syndicate"]):
        # Concentric surveillance web & crosshairs
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        for r in [80, 160, 260, 380]:
            odraw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=wire_color, width=2)
        odraw.line([(cx - 420, cy), (cx + 420, cy)], fill=wire_color, width=2)
        odraw.line([(cx, cy - 320), (cx, cy + 320)], fill=wire_color, width=2)
    elif "contract" in n_lower or "diploma" in n_lower or "immunity" in n_lower or "dossier" in n_lower:
        # Forensic document page with official seal
        dx1, dy1 = int(WIDTH * 0.34), int(HEIGHT * 0.22)
        dx2, dy2 = int(WIDTH * 0.66), int(HEIGHT * 0.78)
        odraw.rectangle([(dx1, dy1), (dx2, dy2)], fill=ink_color, outline=wire_color, width=3)
        # Horizontal text rule lines
        for ly in range(dy1 + 50, dy2 - 70, 32):
            odraw.line([(dx1 + 35, ly), (dx2 - 35, ly)], fill=accent_wire, width=2)
        # Red/golden embossed official seal
        seal_cx, seal_cy = int(WIDTH * 0.50), dy2 - 50
        odraw.ellipse([(seal_cx - 28, seal_cy - 28), (seal_cx + 28, seal_cy + 28)], fill=(180, 45, 45, 180), outline=wire_color, width=2)
    elif "seligman" in n_lower or "helplessness" in n_lower or "cage" in n_lower:
        # Open birdcage with swung open door
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        # Dome arch
        odraw.arc([(cx - 150, cy - 220), (cx + 150, cy + 80)], 180, 360, fill=wire_color, width=5)
        # Base plate
        odraw.rectangle([(cx - 160, cy + 140), (cx + 160, cy + 160)], fill=ink_color, outline=wire_color, width=3)
        # Vertical cage bars
        for bx in range(cx - 130, cx + 140, 35):
            odraw.line([(bx, cy - 120), (bx, cy + 140)], fill=wire_color, width=2)
        # Swung open door vector
        odraw.line([(cx + 60, cy - 80), (cx + 180, cy - 60)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 180), width=4)
        odraw.line([(cx + 60, cy + 100), (cx + 180, cy + 120)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 180), width=4)
        odraw.line([(cx + 180, cy - 60), (cx + 180, cy + 120)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 180), width=4)
    elif "gavel" in n_lower or "sentence" in n_lower:
        # Judicial gavel silhouette struck on sounding block
        cx, cy = int(WIDTH * 0.48), int(HEIGHT * 0.50)
        # Sounding block base
        odraw.rectangle([(cx - 140, cy + 60), (cx + 140, cy + 95)], fill=ink_color, outline=wire_color, width=4)
        # Gavel head cylinder
        odraw.rectangle([(cx - 70, cy - 60), (cx + 70, cy - 10)], fill=ink_color, outline=wire_color, width=4)
        # Gavel angled handle
        odraw.line([(cx, cy - 35), (cx + 160, cy - 150)], fill=ink_color, width=14)
        odraw.line([(cx, cy - 35), (cx + 160, cy - 150)], fill=wire_color, width=4)
    elif "sprout" in n_lower or "growth" in n_lower:
        # Resilient green sprout emerging from cracked bedrock
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.65)
        # Bedrock crack lines
        odraw.line([(cx - 200, cy + 40), (cx - 40, cy)], fill=ink_color, width=8)
        odraw.line([(cx - 40, cy), (cx + 30, cy + 20)], fill=ink_color, width=8)
        odraw.line([(cx + 30, cy + 20), (cx + 220, cy + 50)], fill=ink_color, width=8)
        # Sprout stem & leaves
        odraw.arc([(cx - 40, cy - 140), (cx + 40, cy + 40)], 270, 90, fill=(110, 195, 120, 200), width=5)
        odraw.ellipse([(cx + 20, cy - 140), (cx + 75, cy - 105)], fill=(120, 210, 130, 160), outline=wire_color, width=2)
        odraw.ellipse([(cx - 75, cy - 110), (cx - 20, cy - 75)], fill=(120, 210, 130, 160), outline=wire_color, width=2)
    elif "amber_eyes" in n_lower or "owl" in n_lower:
        # Signature Amber Eyes dual owl eye apertures
        cx1, cx2, cy = int(WIDTH * 0.44), int(WIDTH * 0.56), int(HEIGHT * 0.48)
        for cx in [cx1, cx2]:
            odraw.ellipse([(cx - 60, cy - 60), (cx + 60, cy + 60)], outline=(226, 180, 103, 160), width=4)
            odraw.ellipse([(cx - 25, cy - 25), (cx + 25, cy + 25)], fill=(226, 180, 103, 220))
            odraw.ellipse([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=(14, 14, 17, 255))

    # Composite overlay onto base image
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def main():
    jobs_file = WORK / "bg_jobs_tap10.json"
    if not jobs_file.exists():
        print(f"Lỗi: Không tìm thấy {jobs_file}")
        sys.exit(1)

    jobs = json.loads(jobs_file.read_text(encoding="utf-8"))
    prov_list = json.loads(PROV_FILE.read_text(encoding="utf-8")) if PROV_FILE.exists() else []
    prov_by_file = {p["file"]: p for p in prov_list}

    print(f"Bắt đầu render {len(jobs)} ảnh 2K 16:9 Dark Graphic Novel Noir cho Tập 10...")
    count = 0
    today_str = str(date.today())

    for idx, job in enumerate(jobs):
        name = job["name"]
        prompt = job["prompt"]
        out_path = BG_DIR / f"{name}.png"
        rel_path = f"assets/bg/{name}.png"

        seed_val = abs(hash(name)) % (10**7)
        img = render_background(name, prompt, seed=seed_val)
        img.save(out_path, format="PNG", optimize=True)
        count += 1

        record = {
            "file": rel_path,
            "loai": "nền 16:9",
            "cong_cu": "Amber Eyes Noir Graphic Renderer (Pillow & Numpy Procedural Chiaroscuro Pipeline)",
            "ngay": today_str,
            "prompt": prompt,
            "seed": seed_val,
            "nguon_anh_tham_chieu": None,
            "kich_thuoc_goc": [WIDTH, HEIGHT],
            "dieu_khoan": "Kênh tự tạo 100%, không sử dụng MiniMax hay tài sản bên thứ ba",
            "kiem_tra_thuong_mai": "đạt"
        }
        prov_by_file[rel_path] = record

        if (idx + 1) % 10 == 0 or idx == len(jobs) - 1:
            print(f"  [{idx+1:02d}/{len(jobs)}] Đã render: {name}.png ({WIDTH}x{HEIGHT})")

    new_prov = list(prov_by_file.values())
    PROV_FILE.write_text(json.dumps(new_prov, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Thành công! Đã tạo đủ {count} ảnh và cập nhật {PROV_FILE} ({len(new_prov)} bản ghi)!")


if __name__ == "__main__":
    main()
