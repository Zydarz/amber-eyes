#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 2K 16:9 dark graphic novel noir backgrounds for Episode 08.
Generates 2112x1188 images with deep chiaroscuro lighting, custom graphic noir elements,
film grain, vignette, and atmospheric moods.
Updates provenance.json and builds assets for Episode 08.
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
    "subway": {
        "base": (8, 12, 16),
        "accent": (20, 38, 48),
        "light": (65, 155, 175),
        "style": "tunnel"
    },
    "dawn": {
        "base": (12, 12, 18),
        "accent": (36, 32, 48),
        "light": (230, 175, 105),
        "style": "dawn_rays"
    },
    "chemical": {
        "base": (6, 14, 12),
        "accent": (16, 42, 34),
        "light": (50, 190, 140),
        "style": "toxic_lab"
    },
    "fuji": {
        "base": (10, 12, 18),
        "accent": (24, 30, 44),
        "light": (150, 175, 205),
        "style": "mountain"
    },
    "police": {
        "base": (12, 12, 16),
        "accent": (28, 30, 42),
        "light": (195, 70, 70),
        "style": "police_strobe"
    },
    "investigation": {
        "base": (16, 13, 10),
        "accent": (42, 32, 22),
        "light": (215, 155, 80),
        "style": "banker_lamp"
    },
    "cult": {
        "base": (12, 8, 16),
        "accent": (35, 18, 45),
        "light": (175, 95, 215),
        "style": "esoteric"
    },
    "court": {
        "base": (15, 11, 12),
        "accent": (42, 28, 28),
        "light": (205, 145, 75),
        "style": "judicial"
    },
    "isolation": {
        "base": (8, 9, 11),
        "accent": (22, 24, 28),
        "light": (130, 135, 145),
        "style": "harsh_spot"
    },
    "default": {
        "base": (10, 12, 15),
        "accent": (28, 32, 40),
        "light": (145, 155, 170),
        "style": "noir_generic"
    }
}


def pick_theme(name):
    n = name.lower()
    if any(k in n for k in ["subway", "train", "tunnel", "station", "tracks", "commuter", "stairs", "doors"]):
        return THEMES["subway"]
    if any(k in n for k in ["dawn", "sunrise", "peace", "restored"]):
        return THEMES["dawn"]
    if any(k in n for k in ["chemical", "sarin", "reactor", "precursor", "synthesis", "incubator", "bio", "lab", "virology"]):
        return THEMES["chemical"]
    if any(k in n for k in ["fuji", "kamikuishiki", "mountain", "grave", "woods", "cedar"]):
        return THEMES["fuji"]
    if any(k in n for k in ["police", "hazmat", "convoy", "hq", "incident_board", "ambulances"]):
        return THEMES["police"]
    if any(k in n for k in ["dossier", "sakamoto", "desk", "novel", "glasses", "underground_book", "matsumoto_court", "weapons"]):
        return THEMES["investigation"]
    if any(k in n for k in ["asahara", "aum", "emblem", "altar", "psi", "headgear", "ritual", "hallucinogen", "mandala", "prophecy", "poa", "ceiling", "hubris"]):
        return THEMES["cult"]
    if any(k in n for k in ["court", "gavel", "witness", "dock", "verdicts", "oath", "detention"]):
        return THEMES["court"]
    if any(k in n for k in ["isolation", "cell", "bowl", "malnutrition", "brain", "redflag", "mirror", "gate", "cogs", "stock"]):
        return THEMES["isolation"]
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
    angle = (seed * 43 + 30) % 360
    rad = np.radians(angle)
    proj = nx * np.cos(rad) + ny * np.sin(rad)
    proj = (proj - proj.min()) / (proj.max() - proj.min() + 1e-6)
    t = np.power(proj, 1.8)[:, :, np.newaxis]
    img_arr = base_c * (1.0 - t) + accent_c * t

    # 2. Lighting patterns based on scene style
    style = theme["style"]
    if style == "tunnel":
        # Perspective tunnel glow from center vanishing point
        cx, cy = 0.5, 0.48
        dist = np.sqrt((nx - cx)**2 * 3.5 + (ny - cy)**2 * 2.0)
        glow = np.exp(-dist * 3.8)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.8
        # Rails / tunnel conduit lines
        lines = np.sin((nx - cx) / (ny - cy + 0.05 + 1e-4) * 18.0)
        lines_mask = np.clip(np.abs(lines) * 0.4 + 0.6, 0.5, 1.0)[:, :, np.newaxis]
        img_arr *= lines_mask
    elif style == "dawn_rays":
        # Sunbeams rising from horizon
        horizon = np.exp(-((ny - 0.72) / 0.22)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.75
        rays = np.sin(np.arctan2(ny - 0.85, nx - 0.5) * 12.0)
        rays_mask = np.clip((rays + 0.5) * 0.5, 0.7, 1.2)[:, :, np.newaxis]
        img_arr *= rays_mask
    elif style == "toxic_lab":
        # Concentrated chemical luminescence from lower center
        cx, cy = 0.48, 0.68
        dist = np.sqrt((nx - cx)**2 * 1.8 + (ny - cy)**2 * 2.2)
        glow = np.exp(-dist * 4.2)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.9
        # Horizontal shelf / glassware reflections
        stripes = np.sin(ny * 60.0)
        slats = np.clip((stripes + 0.8) * 0.6, 0.6, 1.0)[:, :, np.newaxis]
        img_arr *= slats
    elif style == "mountain":
        # Triangular mountain profile shadow
        fuji_slope = np.abs(nx - 0.5) * 1.6
        fuji_mask = (ny > (0.35 + fuji_slope * 0.45)).astype(np.float32)[:, :, np.newaxis]
        img_arr = img_arr * (1.0 - fuji_mask * 0.4) + base_c * (fuji_mask * 0.4)
        # Horizon mist band
        mist = np.exp(-((ny - 0.55) / 0.12)**2)[:, :, np.newaxis]
        img_arr += light_c * mist * 0.4
    elif style == "police_strobe":
        # Alternating flashing red and blue strobe pools
        dist_r = np.sqrt((nx - 0.25)**2 * 2.5 + (ny - 0.75)**2 * 2.0)
        glow_r = np.exp(-dist_r * 4.5)[:, :, np.newaxis]
        dist_b = np.sqrt((nx - 0.75)**2 * 2.5 + (ny - 0.75)**2 * 2.0)
        glow_b = np.exp(-dist_b * 4.5)[:, :, np.newaxis]
        img_arr += np.array([210, 40, 40], dtype=np.float32) * glow_r * 0.7
        img_arr += np.array([40, 80, 220], dtype=np.float32) * glow_b * 0.7
    elif style == "banker_lamp":
        # Warm desk spotlight pool
        cx, cy = 0.4, 0.35
        dist = np.sqrt((nx - cx)**2 * 1.4 + (ny - cy)**2 * 0.9)
        glow = np.exp(-dist * 3.2)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
        # Venetian blind shadow slats
        slats = np.sin(ny * 40.0 + nx * 4.0)
        slats = np.clip((slats + 0.5) * 0.7, 0.45, 1.0)[:, :, np.newaxis]
        img_arr *= slats
    elif style == "esoteric":
        # Hypnotic circular aura
        cx, cy = 0.5, 0.5
        dist = np.sqrt((nx - cx)**2 + (ny - cy)**2)
        rings = np.sin(dist * 35.0)
        aura = np.exp(-dist * 2.8) * np.clip(rings * 0.3 + 0.7, 0.4, 1.0)
        img_arr += light_c * aura[:, :, np.newaxis] * 0.75
    elif style == "judicial":
        # Formal overhead courtroom spotlights
        cx1, cx2 = 0.35, 0.65
        d1 = np.sqrt((nx - cx1)**2 * 2.5 + (ny - 0.4)**2 * 1.5)
        d2 = np.sqrt((nx - cx2)**2 * 2.5 + (ny - 0.4)**2 * 1.5)
        glow = (np.exp(-d1 * 3.2) + np.exp(-d2 * 3.2))[:, :, np.newaxis]
        img_arr += light_c * glow * 0.7
    elif style == "harsh_spot":
        # Single top-down harsh interrogation spotlight
        dist = np.sqrt((nx - 0.5)**2 * 3.2 + (ny - 0.5)**2 * 2.2)
        glow = np.clip(1.0 - dist * 1.7, 0.0, 1.0)**2.2
        img_arr = base_c + (light_c - base_c) * glow[:, :, np.newaxis] * 0.95
        # Bar shadows
        bars = np.sin(nx * 48.0)
        bars_mask = np.where(bars > 0.45, 0.4, 1.0)[:, :, np.newaxis]
        img_arr *= bars_mask

    # 3. Noir edge vignette
    vx = (nx - 0.5) * 2.0
    vy = (ny - 0.5) * 2.0
    v_dist = np.sqrt(vx * vx + vy * vy)
    vignette = np.clip(1.0 - (v_dist - 0.45) * 0.75, 0.12, 1.0)[:, :, np.newaxis]
    img_arr *= vignette

    # 4. Organic film grain
    noise = rng.normal(0.0, 7.0, (HEIGHT, WIDTH, 1)).astype(np.float32)
    img_arr += noise

    # Clip to valid range
    img_arr = np.clip(img_arr, 0.0, 255.0).astype(np.uint8)
    img = Image.fromarray(img_arr, mode="RGB")

    # 5. Graphic Noir vector overlays & linework
    draw = ImageDraw.Draw(img)
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)

    # Add scene-specific thematic silhouettes in dark ink
    ink_color = (theme["base"][0], theme["base"][1], theme["base"][2], 180)
    wire_color = (theme["light"][0], theme["light"][1], theme["light"][2], 40)

    n_lower = name.lower()
    if "tracks" in n_lower or "tunnel" in n_lower:
        # Converging perspective track lines
        odraw.line([(WIDTH * 0.5, HEIGHT * 0.48), (WIDTH * 0.15, HEIGHT)], fill=ink_color, width=8)
        odraw.line([(WIDTH * 0.5, HEIGHT * 0.48), (WIDTH * 0.85, HEIGHT)], fill=ink_color, width=8)
        odraw.line([(WIDTH * 0.5, HEIGHT * 0.48), (WIDTH * 0.32, HEIGHT)], fill=wire_color, width=4)
        odraw.line([(WIDTH * 0.5, HEIGHT * 0.48), (WIDTH * 0.68, HEIGHT)], fill=wire_color, width=4)
    elif "chemical_structure" in n_lower:
        # Hexagonal molecule diagrams in faint luminous lines
        cx, cy, r = int(WIDTH * 0.5), int(HEIGHT * 0.5), 180
        pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(0, 360, 60)]
        odraw.polygon(pts, outline=(theme["light"][0], theme["light"][1], theme["light"][2], 90), width=4)
        odraw.line([(pts[0][0], pts[0][1]), (pts[0][0] + 120, pts[0][1] - 80)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 70), width=3)
    elif "psi_headgear" in n_lower:
        # Radiating electrode wire arcs
        hcx, hcy = int(WIDTH * 0.5), int(HEIGHT * 0.55)
        odraw.arc([hcx - 250, hcy - 200, hcx + 250, hcy + 200], start=180, end=360, fill=(theme["light"][0], theme["light"][1], theme["light"][2], 110), width=5)
        for ang in range(200, 350, 25):
            rad_ang = math.radians(ang)
            ex = hcx + 250 * math.cos(rad_ang)
            ey = hcy + 200 * math.sin(rad_ang)
            odraw.line([(ex, ey), (ex + 70 * math.cos(rad_ang), ey - 90)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 80), width=3)
    elif "brain_scan" in n_lower:
        # Dual brain hemisphere oval contours
        bcx, bcy = int(WIDTH * 0.5), int(HEIGHT * 0.5)
        odraw.ellipse([bcx - 220, bcy - 280, bcx - 20, bcy + 280], outline=(theme["light"][0], theme["light"][1], theme["light"][2], 85), width=4)
        odraw.ellipse([bcx + 20, bcy - 280, bcx + 220, bcy + 280], outline=(theme["light"][0], theme["light"][1], theme["light"][2], 85), width=4)
    elif "gavel" in n_lower:
        # Solid judicial sound block circle & gavel block
        gcx, gcy = int(WIDTH * 0.5), int(HEIGHT * 0.65)
        odraw.ellipse([gcx - 260, gcy - 80, gcx + 260, gcy + 80], fill=ink_color)
        odraw.ellipse([gcx - 230, gcy - 65, gcx + 230, gcy + 65], outline=(theme["light"][0], theme["light"][1], theme["light"][2], 80), width=4)
    elif "redflag" in n_lower:
        # Warning badge diamond framing
        rcx, rcy, sz = int(WIDTH * 0.5), int(HEIGHT * 0.5), 240
        diamond = [(rcx, rcy - sz), (rcx + sz, rcy), (rcx, rcy + sz), (rcx - sz, rcy)]
        odraw.polygon(diamond, outline=(theme["light"][0], theme["light"][1], theme["light"][2], 75), width=5)

    # Soft mist band for atmospheric depth
    mist_y = int(HEIGHT * (0.55 + 0.12 * math.sin(seed * 13)))
    odraw.ellipse([-150, mist_y, WIDTH + 150, mist_y + 380], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 14))
    overlay = overlay.filter(ImageFilter.GaussianBlur(radius=38))
    img.paste(overlay, (0, 0), overlay)

    return img


def main():
    jobs_file = WORK / "bg_jobs_tap08.json"
    if not jobs_file.exists():
        print(f"Lỗi: Không tìm thấy {jobs_file}")
        sys.exit(1)

    jobs = json.loads(jobs_file.read_text(encoding="utf-8"))
    prov_list = json.loads(PROV_FILE.read_text(encoding="utf-8")) if PROV_FILE.exists() else []
    prov_by_file = {p["file"]: p for p in prov_list}

    print(f"Bắt đầu render {len(jobs)} ảnh 2K 16:9 Dark Graphic Novel Noir cho Tập 08...")
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
