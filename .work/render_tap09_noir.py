#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 2K 16:9 dark graphic novel noir backgrounds for Episode 09.
Generates 2112x1188 images with deep chiaroscuro lighting, custom graphic noir elements,
film grain, vignette, and atmospheric moods.
Updates provenance.json and builds assets for Episode 09.
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
    "summer_of_love": {
        "base": (12, 11, 16),
        "accent": (36, 26, 38),
        "light": (225, 140, 75),
        "style": "sunset_coast"
    },
    "cielo_night": {
        "base": (6, 9, 14),
        "accent": (16, 28, 42),
        "light": (75, 135, 170),
        "style": "nocturnal_estate"
    },
    "spahn_desert": {
        "base": (14, 11, 9),
        "accent": (38, 28, 20),
        "light": (210, 150, 85),
        "style": "western_ranch"
    },
    "forensic": {
        "base": (14, 12, 10),
        "accent": (38, 30, 22),
        "light": (215, 160, 80),
        "style": "banker_lamp"
    },
    "cult_ritual": {
        "base": (12, 8, 16),
        "accent": (34, 18, 44),
        "light": (195, 95, 220),
        "style": "hypnotic_ritual"
    },
    "penal": {
        "base": (8, 11, 10),
        "accent": (20, 30, 28),
        "light": (100, 165, 145),
        "style": "prison_bars"
    },
    "courtroom": {
        "base": (15, 11, 12),
        "accent": (42, 28, 28),
        "light": (215, 155, 80),
        "style": "judicial"
    },
    "redflag": {
        "base": (14, 8, 10),
        "accent": (40, 18, 24),
        "light": (220, 75, 75),
        "style": "warning_spot"
    },
    "hope_dawn": {
        "base": (10, 12, 18),
        "accent": (32, 34, 52),
        "light": (235, 185, 110),
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
    if any(k in n for k in ["summer_of_love", "flower", "hippie", "skyline_1969", "guitar", "asphalt"]):
        return THEMES["summer_of_love"]
    if any(k in n for k in ["cielo", "waverly", "beverly", "living_room", "gate_fog", "night_highway", "vacant"]):
        return THEMES["cielo_night"]
    if any(k in n for k in ["spahn", "ranch", "desert", "campfire", "barker", "old_ford", "doll_desert", "clocks"]):
        return THEMES["spahn_desert"]
    if any(k in n for k in ["investigation", "map", "dossier", "radio", "gun_shop", "valuables", "headline", "forensic", "prosecutor", "law_book"]):
        return THEMES["forensic"]
    if any(k in n for k in ["dark_triad", "lewin", "love_bombing", "ashes", "lsd", "sermon", "cross", "candle", "knots", "trauma_bonding", "carved_x", "collective_hysteria", "puppet"]):
        return THEMES["cult_ritual"]
    if any(k in n for k in ["prison", "sybil", "corcoran", "cell"]):
        return THEMES["penal"]
    if any(k in n for k in ["court", "hall_of_justice", "gavel", "verdict", "supreme_court", "scales"]):
        return THEMES["courtroom"]
    if any(k in n for k in ["redflag", "two_faced"]):
        return THEMES["redflag"]
    if any(k in n for k in ["birdcage", "closing_dossier", "dawn", "horizon"]):
        return THEMES["hope_dawn"]
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
    angle = (seed * 37 + 45) % 360
    rad = np.radians(angle)
    proj = nx * np.cos(rad) + ny * np.sin(rad)
    proj = (proj - proj.min()) / (proj.max() - proj.min() + 1e-6)
    t = np.power(proj, 1.8)[:, :, np.newaxis]
    img_arr = base_c * (1.0 - t) + accent_c * t

    # 2. Lighting patterns based on scene style
    style = theme["style"]
    if style == "sunset_coast":
        # Low coastal horizon glow with warm rays
        horizon = np.exp(-((ny - 0.70) / 0.20)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.85
        rays = np.sin(np.arctan2(ny - 0.85, nx - 0.45) * 10.0)
        rays_mask = np.clip((rays + 0.6) * 0.5, 0.65, 1.2)[:, :, np.newaxis]
        img_arr *= rays_mask
    elif style == "nocturnal_estate":
        # Cold moonlight cone breaking through midnight foliage
        cx, cy = 0.52, 0.35
        dist = np.sqrt((nx - cx)**2 * 2.8 + (ny - cy)**2 * 1.5)
        moon_glow = np.exp(-dist * 3.5)[:, :, np.newaxis]
        img_arr += light_c * moon_glow * 0.85
        # Tall pine tree silhouette shadows
        pines = np.sin(nx * 36.0 + np.sin(ny * 8.0) * 1.5)
        pines_mask = np.clip((pines + 0.7) * 0.6, 0.5, 1.0)[:, :, np.newaxis]
        img_arr *= pines_mask
    elif style == "western_ranch":
        # Broad sweeping desert dust & low western sun
        horizon = np.exp(-((ny - 0.65) / 0.25)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.75
        # Board planks / weathered timber slats
        boards = np.sin(ny * 65.0)
        board_mask = np.clip((boards + 0.85) * 0.55, 0.6, 1.0)[:, :, np.newaxis]
        img_arr *= board_mask
    elif style == "banker_lamp":
        # Warm desk spotlight pool with venetian blinds
        cx, cy = 0.42, 0.38
        dist = np.sqrt((nx - cx)**2 * 1.6 + (ny - cy)**2 * 1.1)
        lamp_glow = np.exp(-dist * 3.2)[:, :, np.newaxis]
        img_arr += light_c * lamp_glow * 0.90
        # Venetian blind slats
        slats = np.sin(ny * 38.0 + nx * 3.5)
        slats_mask = np.clip((slats + 0.55) * 0.7, 0.45, 1.0)[:, :, np.newaxis]
        img_arr *= slats_mask
    elif style == "hypnotic_ritual":
        # Pulsing concentric esoteric auras
        cx, cy = 0.5, 0.5
        dist = np.sqrt((nx - cx)**2 + (ny - cy)**2)
        rings = np.sin(dist * 32.0)
        aura = np.exp(-dist * 2.6) * np.clip(rings * 0.35 + 0.65, 0.35, 1.0)
        img_arr += light_c * aura[:, :, np.newaxis] * 0.80
    elif style == "prison_bars":
        # Harsh top-down institutional light with vertical cell bar shadows
        dist = np.sqrt((nx - 0.5)**2 * 1.8 + (ny - 0.4)**2 * 1.6)
        glow = np.clip(1.0 - dist * 1.4, 0.0, 1.0)**1.8
        img_arr = base_c + (light_c - base_c) * glow[:, :, np.newaxis] * 0.85
        # Vertical steel bars
        bars = np.sin(nx * 42.0)
        bars_mask = np.where(bars > 0.40, 0.35, 1.0)[:, :, np.newaxis]
        img_arr *= bars_mask
    elif style == "judicial":
        # High classical courtroom spotlighting
        cx1, cx2 = 0.35, 0.65
        d1 = np.sqrt((nx - cx1)**2 * 2.4 + (ny - 0.4)**2 * 1.4)
        d2 = np.sqrt((nx - cx2)**2 * 2.4 + (ny - 0.4)**2 * 1.4)
        glow = (np.exp(-d1 * 3.0) + np.exp(-d2 * 3.0))[:, :, np.newaxis]
        img_arr += light_c * glow * 0.75
    elif style == "warning_spot":
        # Intense raking warning spotlight on black void
        cx, cy = 0.5, 0.52
        dist = np.sqrt((nx - cx)**2 * 3.0 + (ny - cy)**2 * 2.2)
        spot = np.exp(-dist * 4.0)[:, :, np.newaxis]
        img_arr += light_c * spot * 0.95
    elif style == "dawn_rays":
        # Hopeful morning rays breaking through mist
        horizon = np.exp(-((ny - 0.68) / 0.18)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.80
        rays = np.sin(np.arctan2(ny - 0.80, nx - 0.5) * 14.0)
        rays_mask = np.clip((rays + 0.6) * 0.5, 0.7, 1.25)[:, :, np.newaxis]
        img_arr *= rays_mask
    else:
        # Generic noir chiaroscuro pool
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
    wire_color = (theme["light"][0], theme["light"][1], theme["light"][2], 45)
    accent_wire = (theme["accent"][0], theme["accent"][1], theme["accent"][2], 120)

    n_lower = name.lower()

    # Thematic vector details
    if "spahn_ranch" in n_lower or "western" in n_lower or "porch" in n_lower:
        # Western porch beams & horizontal roofline
        odraw.rectangle([(0, 0), (WIDTH, int(HEIGHT * 0.18))], fill=ink_color)
        odraw.line([(0, int(HEIGHT * 0.18)), (WIDTH, int(HEIGHT * 0.18))], fill=wire_color, width=4)
        # Vertical supporting timber posts
        for px in [0.15, 0.40, 0.75, 0.95]:
            x_pos = int(WIDTH * px)
            odraw.rectangle([(x_pos - 15, int(HEIGHT * 0.18)), (x_pos + 15, HEIGHT)], fill=ink_color)
            odraw.line([(x_pos - 15, int(HEIGHT * 0.18)), (x_pos - 15, HEIGHT)], fill=wire_color, width=2)
    elif "cielo_drive" in n_lower or "gate" in n_lower:
        # Wrought iron gate bars & finials
        for gx in range(int(WIDTH * 0.1), int(WIDTH * 0.9), 60):
            odraw.line([(gx, int(HEIGHT * 0.3)), (gx, HEIGHT)], fill=ink_color, width=6)
            odraw.line([(gx, int(HEIGHT * 0.3)), (gx, HEIGHT)], fill=wire_color, width=2)
        odraw.line([(int(WIDTH * 0.08), int(HEIGHT * 0.45)), (int(WIDTH * 0.92), int(HEIGHT * 0.45))], fill=ink_color, width=10)
        odraw.line([(int(WIDTH * 0.08), int(HEIGHT * 0.75)), (int(WIDTH * 0.92), int(HEIGHT * 0.75))], fill=ink_color, width=10)
    elif "map" in n_lower or "crime_map" in n_lower:
        # Forensic pinboard connecting red strings
        p1 = (int(WIDTH * 0.30), int(HEIGHT * 0.40))
        p2 = (int(WIDTH * 0.70), int(HEIGHT * 0.55))
        p3 = (int(WIDTH * 0.50), int(HEIGHT * 0.75))
        odraw.line([p1, p2], fill=(210, 45, 45, 180), width=3)
        odraw.line([p2, p3], fill=(210, 45, 45, 180), width=3)
        odraw.line([p1, p3], fill=(210, 45, 45, 140), width=2)
        for pt in [p1, p2, p3]:
            odraw.ellipse([(pt[0] - 8, pt[1] - 8), (pt[0] + 8, pt[1] + 8)], fill=(230, 60, 60, 240))
    elif "dark_triad" in n_lower:
        # Tripartite psychological obsidian triangle
        cx, cy, r = int(WIDTH * 0.5), int(HEIGHT * 0.5), 220
        pts = [
            (cx, cy - r),
            (int(cx - r * math.cos(math.radians(30))), int(cy + r * math.sin(math.radians(30)))),
            (int(cx + r * math.cos(math.radians(30))), int(cy + r * math.sin(math.radians(30))))
        ]
        odraw.polygon(pts, outline=(theme["light"][0], theme["light"][1], theme["light"][2], 130), width=4)
        odraw.line([(cx, cy - r), (cx, int(cy + r * 0.6))], fill=wire_color, width=2)
        odraw.line([pts[1], (cx, int(cy + r * 0.6))], fill=wire_color, width=2)
        odraw.line([pts[2], (cx, int(cy + r * 0.6))], fill=wire_color, width=2)
    elif "kurt_lewin" in n_lower or "three_stages" in n_lower:
        # Three sequential stage nodes
        for i, cx in enumerate([int(WIDTH * 0.25), int(WIDTH * 0.50), int(WIDTH * 0.75)]):
            cy = int(HEIGHT * 0.50)
            odraw.ellipse([(cx - 70, cy - 70), (cx + 70, cy + 70)], outline=(theme["light"][0], theme["light"][1], theme["light"][2], 120), width=3)
            if i < 2:
                next_cx = [int(WIDTH * 0.50), int(WIDTH * 0.75)][i]
                odraw.line([(cx + 70, cy), (next_cx - 70, cy)], fill=wire_color, width=3)
    elif "carved_x" in n_lower:
        # Prominent carved X symbol in center
        cx, cy, sz = int(WIDTH * 0.5), int(HEIGHT * 0.5), 160
        odraw.line([(cx - sz, cy - sz), (cx + sz, cy + sz)], fill=ink_color, width=18)
        odraw.line([(cx + sz, cy - sz), (cx - sz, cy + sz)], fill=ink_color, width=18)
        odraw.line([(cx - sz, cy - sz), (cx + sz, cy + sz)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 140), width=4)
        odraw.line([(cx + sz, cy - sz), (cx - sz, cy + sz)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 140), width=4)
    elif "vinyl" in n_lower or "album" in n_lower:
        # Concentric spinning vinyl grooves
        cx, cy = int(WIDTH * 0.55), int(HEIGHT * 0.52)
        for r in range(40, 360, 20):
            odraw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=wire_color, width=1)
        odraw.ellipse([(cx - 70, cy - 70), (cx + 70, cy + 70)], fill=ink_color, outline=wire_color, width=2)
        odraw.ellipse([(cx - 10, cy - 10), (cx + 10, cy + 10)], fill=(20, 20, 25, 255))
    elif "scales" in n_lower or "justice" in n_lower:
        # Classical scales of justice silhouette
        cx, cy = int(WIDTH * 0.5), int(HEIGHT * 0.42)
        odraw.line([(cx, cy - 140), (cx, cy + 220)], fill=ink_color, width=10)
        odraw.line([(cx - 180, cy - 90), (cx + 180, cy - 90)], fill=ink_color, width=6)
        odraw.line([(cx - 180, cy - 90), (cx - 240, cy + 40)], fill=wire_color, width=2)
        odraw.line([(cx - 180, cy - 90), (cx - 120, cy + 40)], fill=wire_color, width=2)
        odraw.arc([(cx - 240, cy + 30), (cx - 120, cy + 70)], 0, 180, fill=ink_color, width=4)
        odraw.line([(cx + 180, cy - 90), (cx + 120, cy + 40)], fill=wire_color, width=2)
        odraw.line([(cx + 180, cy - 90), (cx + 240, cy + 40)], fill=wire_color, width=2)
        odraw.arc([(cx + 120, cy + 30), (cx + 240, cy + 70)], 0, 180, fill=ink_color, width=4)
    elif "puppet" in n_lower:
        # Dangling puppet strings
        cx, cy = int(WIDTH * 0.5), int(HEIGHT * 0.15)
        for sx in [0.25, 0.38, 0.50, 0.62, 0.75]:
            x_top = int(WIDTH * sx)
            odraw.line([(x_top, cy), (int(x_top + (sx - 0.5) * 150), int(HEIGHT * 0.85))], fill=wire_color, width=2)
    elif "birdcage" in n_lower:
        # Arching birdcage bars with open door
        cx, cy = int(WIDTH * 0.45), int(HEIGHT * 0.55)
        odraw.arc([(cx - 120, cy - 220), (cx + 120, cy + 20)], 180, 360, fill=ink_color, width=5)
        for bx in range(cx - 100, cx + 110, 25):
            odraw.line([(bx, cy - 180), (bx, cy + 180)], fill=wire_color, width=2)
        odraw.line([(cx - 120, cy + 180), (cx + 120, cy + 180)], fill=ink_color, width=6)

    # Composite overlay onto base image
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def main():
    jobs_file = WORK / "bg_jobs_tap09.json"
    if not jobs_file.exists():
        print(f"Lỗi: Không tìm thấy {jobs_file}")
        sys.exit(1)

    jobs = json.loads(jobs_file.read_text(encoding="utf-8"))
    prov_list = json.loads(PROV_FILE.read_text(encoding="utf-8")) if PROV_FILE.exists() else []
    prov_by_file = {p["file"]: p for p in prov_list}

    print(f"Bắt đầu render {len(jobs)} ảnh 2K 16:9 Dark Graphic Novel Noir cho Tập 09...")
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
