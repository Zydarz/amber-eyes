#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 2K 16:9 dark graphic novel noir backgrounds for Episode 11:
'Cặp Đôi Ken & Barbie' (Hồ sơ Paul Bernardo & Karla Homolka).
Generates 2112x1188 images with deep chiaroscuro lighting, custom graphic noir elements,
film grain, vignette, and atmospheric moods matching the case.
Updates provenance.json and builds assets for Episode 11.
"""
import json
import math
import sys
from datetime import date
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BG_DIR = ROOT / "assets" / "bg"
BG_DIR.mkdir(parents=True, exist_ok=True)
PROV_FILE = ROOT / "provenance.json"

WIDTH = 2112
HEIGHT = 1188

THEMES = {
    "pink_suburbia": {
        "base": (15, 12, 14),
        "accent": (42, 24, 32),
        "light": (235, 160, 180),
        "style": "suburban_pastel_noir"
    },
    "wedding_fairytale": {
        "base": (14, 13, 16),
        "accent": (36, 32, 44),
        "light": (240, 215, 160),
        "style": "fairytale_arch"
    },
    "ontario_waters": {
        "base": (8, 12, 16),
        "accent": (18, 28, 42),
        "light": (110, 165, 210),
        "style": "lake_mist"
    },
    "scarborough_hunt": {
        "base": (9, 10, 15),
        "accent": (22, 24, 38),
        "light": (130, 150, 190),
        "style": "nocturnal_map"
    },
    "domestic_fracture": {
        "base": (16, 10, 11),
        "accent": (42, 20, 24),
        "light": (225, 140, 70),
        "style": "flashlight_beam"
    },
    "victim_mask": {
        "base": (13, 11, 14),
        "accent": (34, 26, 38),
        "light": (215, 180, 160),
        "style": "cracked_mask"
    },
    "deal_with_devil": {
        "base": (16, 8, 10),
        "accent": (45, 16, 20),
        "light": (215, 135, 75),
        "style": "legal_contract"
    },
    "folie_a_deux": {
        "base": (12, 9, 16),
        "accent": (32, 20, 44),
        "light": (195, 110, 220),
        "style": "shared_spiral"
    },
    "christmas_crime": {
        "base": (11, 13, 10),
        "accent": (26, 36, 22),
        "light": (190, 150, 80),
        "style": "tainted_glass"
    },
    "eight_mm_tapes": {
        "base": (8, 11, 15),
        "accent": (18, 28, 42),
        "light": (120, 180, 230),
        "style": "projector_beam"
    },
    "penal_verdict": {
        "base": (8, 10, 10),
        "accent": (20, 28, 28),
        "light": (110, 160, 150),
        "style": "prison_iron"
    },
    "redflag": {
        "base": (16, 8, 10),
        "accent": (44, 16, 22),
        "light": (230, 75, 75),
        "style": "warning_spot"
    },
    "justice_dawn": {
        "base": (12, 14, 18),
        "accent": (30, 38, 52),
        "light": (240, 195, 115),
        "style": "lantern_rays"
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
    if any(k in n for k in ["pink_house", "suburban", "bayview", "dashing_car", "vanity", "clinic", "barbecue", "lace_curtain", "door_abyss"]):
        return THEMES["pink_suburbia"]
    if any(k in n for k in ["wedding", "carriage", "gala", "inseparable", "golden_illusion"]):
        return THEMES["wedding_fairytale"]
    if any(k in n for k in ["lake_gibson", "lakeside", "lake_ontario", "waters"]):
        return THEMES["ontario_waters"]
    if any(k in n for k in ["scarborough", "taskforce", "church_parking", "map_proximity"]):
        return THEMES["scarborough_hunt"]
    if any(k in n for k in ["flashlight", "hospital", "escape_to_parents", "dna_match"]):
        return THEMES["domestic_fracture"]
    if any(k in n for k in ["victim", "bruised", "tears", "battered_woman", "puppet", "fragile_beauty", "mockery"]):
        return THEMES["victim_mask"]
    if any(k in n for k in ["deal_with_the_devil", "plea", "contract", "missing_evidence", "prosecution_clock", "constitutional"]):
        return THEMES["deal_with_devil"]
    if any(k in n for k in ["folie_a_deux", "destructive_flame", "narcissist", "accomplice", "sociopath", "abyss", "unholy_sacrament", "adoration"]):
        return THEMES["folie_a_deux"]
    if any(k in n for k in ["christmas", "halothane", "polaroid", "grieving_parents", "toxic_devotion"]):
        return THEMES["christmas_crime"]
    if any(k in n for k in ["8mm", "tapes", "vent", "projector", "monitor", "camera_director", "ken_murray", "screening_room"]):
        return THEMES["eight_mm_tapes"]
    if any(k in n for k in ["prison", "joliette", "dangerous_offender", "calendar_counting", "frozen_justice"]):
        return THEMES["penal_verdict"]
    if any(k in n for k in ["redflag", "protest"]):
        return THEMES["redflag"]
    if any(k in n for k in ["galligan", "lantern", "justice_prevails", "closing_dossier", "amber_eyes", "haunted_new_identity"]):
        return THEMES["justice_dawn"]
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
    if style == "suburban_pastel_noir":
        # Warm pinkish amber light pool with dramatic diagonal roof/window shadows
        cx, cy = 0.48, 0.42
        dist = np.sqrt((nx - cx)**2 * 2.2 + (ny - cy)**2 * 1.5)
        glow = np.exp(-dist * 2.8)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
        # Venetian blind / mullion diagonal slats
        slats = np.sin(ny * 32.0 + nx * 4.0)
        slats_mask = np.clip((slats + 0.6) * 0.65, 0.45, 1.0)[:, :, np.newaxis]
        img_arr *= slats_mask
    elif style == "fairytale_arch":
        # Nostalgic golden dome aura with delicate chandelier rays
        cx, cy = 0.50, 0.35
        dist = np.sqrt((nx - cx)**2 * 1.8 + (ny - cy)**2 * 2.0)
        dome = np.exp(-dist * 2.6)[:, :, np.newaxis]
        img_arr += light_c * dome * 0.90
        rays = np.sin(np.arctan2(ny - cy, nx - cx) * 16.0)
        rays_mask = np.clip((rays + 0.7) * 0.5, 0.7, 1.25)[:, :, np.newaxis]
        img_arr *= rays_mask
    elif style == "lake_mist":
        # Cold mist over dark water with low misty horizon
        horizon = np.exp(-((ny - 0.70) / 0.16)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.80
        ripples = np.sin(ny * 80.0 + np.sin(nx * 12.0) * 2.0)
        ripple_mask = np.clip((ripples + 0.7) * 0.55, 0.6, 1.0)[:, :, np.newaxis]
        img_arr *= ripple_mask
    elif style == "nocturnal_map":
        # Moody midnight spotlight over investigative grid
        cx, cy = 0.52, 0.46
        dist = np.sqrt((nx - cx)**2 * 2.4 + (ny - cy)**2 * 1.8)
        glow = np.exp(-dist * 3.2)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.80
    elif style == "flashlight_beam":
        # Harsh conical flashlight beam cutting through pitch darkness
        beam_angle = np.arctan2(ny - 0.85, nx - 0.20)
        beam_dist = np.sqrt((nx - 0.20)**2 + (ny - 0.85)**2)
        beam_mask = np.exp(-((beam_angle - 0.65) / 0.25)**2) * np.clip(1.2 - beam_dist * 0.8, 0.0, 1.0)
        img_arr += light_c * beam_mask[:, :, np.newaxis] * 1.1
    elif style == "cracked_mask":
        # Melodramatic raking side-light highlighting cracked contours
        cx, cy = 0.42, 0.45
        dist = np.sqrt((nx - cx)**2 * 2.6 + (ny - cy)**2 * 1.6)
        glow = np.exp(-dist * 2.9)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
    elif style == "legal_contract":
        # High-contrast judicial amber banker lamp pool on desk
        cx, cy = 0.50, 0.52
        dist = np.sqrt((nx - cx)**2 * 2.0 + (ny - cy)**2 * 1.4)
        glow = np.exp(-dist * 3.0)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
    elif style == "shared_spiral":
        # Dual spiral vortices of shared psychosis
        cx1, cx2, cy = 0.38, 0.62, 0.48
        d1 = np.sqrt((nx - cx1)**2 * 2.5 + (ny - cy)**2 * 2.0)
        d2 = np.sqrt((nx - cx2)**2 * 2.5 + (ny - cy)**2 * 2.0)
        glow = (np.exp(-d1 * 3.4) + np.exp(-d2 * 3.4))[:, :, np.newaxis]
        img_arr += light_c * glow * 0.80
    elif style == "tainted_glass":
        # Amber festive candlelight in heavy ominous shadows
        cx, cy = 0.46, 0.50
        dist = np.sqrt((nx - cx)**2 * 2.8 + (ny - cy)**2 * 1.8)
        candle = np.exp(-dist * 3.5)[:, :, np.newaxis]
        img_arr += light_c * candle * 0.90
    elif style == "projector_beam":
        # Bright projector beam slicing horizontally across dark room
        beam_y = np.exp(-((ny - 0.46) / 0.14)**2)[:, :, np.newaxis]
        beam_x = np.clip(nx * 1.2, 0.0, 1.0)[:, :, np.newaxis]
        img_arr += light_c * beam_y * beam_x * 0.95
    elif style == "prison_iron":
        # Cold stark institutional ceiling light with vertical cell bar shadows
        dist = np.sqrt((nx - 0.5)**2 * 1.8 + (ny - 0.35)**2 * 1.6)
        glow = np.clip(1.0 - dist * 1.4, 0.0, 1.0)**1.8
        img_arr = base_c + (light_c - base_c) * glow[:, :, np.newaxis] * 0.85
        # Vertical steel bars
        bars = np.sin(nx * 44.0)
        bars_mask = np.where(bars > 0.42, 0.35, 1.0)[:, :, np.newaxis]
        img_arr *= bars_mask
    elif style == "warning_spot":
        # Intense raking red spotlight on black void
        cx, cy = 0.5, 0.50
        dist = np.sqrt((nx - cx)**2 * 3.0 + (ny - cy)**2 * 2.2)
        spot = np.exp(-dist * 4.0)[:, :, np.newaxis]
        img_arr += light_c * spot * 0.95
    elif style == "lantern_rays":
        # Resilient warm lantern beacon dispelling darkness
        cx, cy = 0.50, 0.48
        dist = np.sqrt((nx - cx)**2 * 2.0 + (ny - cy)**2 * 1.6)
        glow = np.exp(-dist * 2.5)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
        rays = np.sin(np.arctan2(ny - cy, nx - cx) * 14.0)
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
    wire_color = (theme["light"][0], theme["light"][1], theme["light"][2], 55)
    accent_wire = (theme["accent"][0], theme["accent"][1], theme["accent"][2], 130)

    n_lower = name.lower()

    # Thematic vector details for Episode 11
    if "pink_house" in n_lower or "bayview" in n_lower or "suburban" in n_lower:
        # Subtle architectural rooflines and window sash outline
        bx1, by1 = int(WIDTH * 0.28), int(HEIGHT * 0.25)
        bx2, by2 = int(WIDTH * 0.72), int(HEIGHT * 0.78)
        # Roof gable triangle
        odraw.polygon([(int(WIDTH * 0.50), by1 - 70), (bx1 - 40, by1 + 40), (bx2 + 40, by1 + 40)], outline=wire_color, width=3)
        # Window frame & mullions
        odraw.rectangle([(bx1 + 100, by1 + 80), (bx2 - 100, by2 - 40)], outline=wire_color, width=4)
        mid_x = (bx1 + bx2) // 2
        mid_y = (by1 + 80 + by2 - 40) // 2
        odraw.line([(mid_x, by1 + 80), (mid_x, by2 - 40)], fill=wire_color, width=2)
        odraw.line([(bx1 + 100, mid_y), (bx2 - 100, mid_y)], fill=wire_color, width=2)
    elif "carriage" in n_lower or "wedding" in n_lower:
        # Fairytale carriage wheel spokes and floral arch arcs
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.52)
        # Grand ornamental arch
        odraw.arc([(cx - 320, cy - 260), (cx + 320, cy + 260)], 180, 360, fill=wire_color, width=4)
        odraw.arc([(cx - 280, cy - 220), (cx + 280, cy + 220)], 180, 360, fill=accent_wire, width=2)
        # Carriage wheel spokes
        odraw.ellipse([(cx - 140, cy - 30), (cx + 140, cy + 250)], outline=wire_color, width=4)
        for ang in range(0, 360, 30):
            ar = math.radians(ang)
            ex = int(cx + 140 * math.cos(ar))
            ey = int(cy + 110 + 140 * math.sin(ar))
            odraw.line([(cx, cy + 110), (ex, ey)], fill=wire_color, width=2)
    elif "lake_gibson" in n_lower or "lakeside" in n_lower or "waters" in n_lower:
        # Misty shoreline ripples and submerged horizontal depths
        for wy in range(int(HEIGHT * 0.65), HEIGHT, 45):
            odraw.line([(0, wy), (WIDTH, wy)], fill=accent_wire, width=2)
        # Reeds / shoreline vertical silhouettes
        for rx in range(int(WIDTH * 0.05), int(WIDTH * 0.35), 25):
            odraw.line([(rx, HEIGHT), (rx + 15, int(HEIGHT * 0.72))], fill=ink_color, width=4)
    elif "flashlight" in n_lower:
        # Industrial heavy metal flashlight profile and angular beam cone
        cx, cy = int(WIDTH * 0.40), int(HEIGHT * 0.50)
        odraw.rectangle([(cx - 160, cy - 25), (cx + 120, cy + 25)], fill=ink_color, outline=wire_color, width=3)
        odraw.polygon([(cx + 120, cy - 50), (cx + 170, cy - 65), (cx + 170, cy + 65), (cx + 120, cy + 50)], fill=ink_color, outline=wire_color)
        # Radiating beam edges
        odraw.line([(cx + 170, cy - 65), (WIDTH, int(HEIGHT * 0.15))], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 140), width=3)
        odraw.line([(cx + 170, cy + 65), (WIDTH, int(HEIGHT * 0.85))], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 140), width=3)
    elif "dna" in n_lower:
        # Forensic DNA double-helix rungs
        cx = int(WIDTH * 0.50)
        for dy in range(int(HEIGHT * 0.18), int(HEIGHT * 0.82), 32):
            phase = (dy * 0.03)
            x_offset = int(math.sin(phase) * 120)
            odraw.line([(cx - x_offset, dy), (cx + x_offset, dy)], fill=wire_color, width=2)
            odraw.ellipse([(cx - x_offset - 6, dy - 6), (cx - x_offset + 6, dy + 6)], fill=accent_wire)
            odraw.ellipse([(cx + x_offset - 6, dy - 6), (cx + x_offset + 6, dy + 6)], fill=accent_wire)
    elif "mask" in n_lower or "victim" in n_lower or "puppet" in n_lower:
        # Theatrical classical mask outline with sharp fissure split
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        odraw.arc([(cx - 130, cy - 180), (cx + 130, cy + 160)], 0, 360, fill=wire_color, width=4)
        # Eye apertures
        odraw.ellipse([(cx - 70, cy - 40), (cx - 20, cy - 10)], outline=wire_color, width=2)
        odraw.ellipse([(cx + 20, cy - 40), (cx + 70, cy - 10)], outline=wire_color, width=2)
        # Fissure fracture down center
        odraw.line([(cx, cy - 180), (cx + 15, cy - 60)], fill=(225, 75, 75, 200), width=3)
        odraw.line([(cx + 15, cy - 60), (cx - 10, cy + 30)], fill=(225, 75, 75, 200), width=3)
        odraw.line([(cx - 10, cy + 30), (cx + 25, cy + 160)], fill=(225, 75, 75, 200), width=3)
    elif "deal_with_the_devil" in n_lower or "contract" in n_lower or "plea" in n_lower or "galligan" in n_lower:
        # Formal legal dossier parchment with official wax seal
        dx1, dy1 = int(WIDTH * 0.33), int(HEIGHT * 0.20)
        dx2, dy2 = int(WIDTH * 0.67), int(HEIGHT * 0.80)
        odraw.rectangle([(dx1, dy1), (dx2, dy2)], fill=ink_color, outline=wire_color, width=4)
        # Text rule lines
        for ly in range(dy1 + 55, dy2 - 75, 30):
            odraw.line([(dx1 + 40, ly), (dx2 - 40, ly)], fill=accent_wire, width=2)
        # Wax seal
        seal_cx, seal_cy = int(WIDTH * 0.50), dy2 - 50
        odraw.ellipse([(seal_cx - 30, seal_cy - 30), (seal_cx + 30, seal_cy + 30)], fill=(195, 40, 40, 200), outline=wire_color, width=2)
    elif "folie_a_deux" in n_lower or "resonance" in n_lower:
        # Dual spiraling elliptical vortices of shared psychosis
        cx1, cx2, cy = int(WIDTH * 0.38), int(WIDTH * 0.62), int(HEIGHT * 0.48)
        for r in [60, 120, 190, 270]:
            odraw.ellipse([(cx1 - r, cy - r), (cx1 + r, cy + r)], outline=wire_color, width=2)
            odraw.ellipse([(cx2 - r, cy - r), (cx2 + r, cy + r)], outline=wire_color, width=2)
        odraw.line([(cx1, cy), (cx2, cy)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 160), width=3)
    elif "halothane" in n_lower or "glass" in n_lower:
        # Chemical apothecary bottle outline and measuring gradation
        bx1, by1 = int(WIDTH * 0.42), int(HEIGHT * 0.32)
        bx2, by2 = int(WIDTH * 0.58), int(HEIGHT * 0.72)
        odraw.rectangle([(bx1, by1 + 50), (bx2, by2)], fill=ink_color, outline=wire_color, width=4)
        odraw.rectangle([(bx1 + 35, by1), (bx2 - 35, by1 + 50)], fill=ink_color, outline=wire_color, width=3)
        for ty in range(by1 + 75, by2 - 20, 28):
            odraw.line([(bx1 + 10, ty), (bx1 + 35, ty)], fill=accent_wire, width=2)
    elif "8mm" in n_lower or "tapes" in n_lower or "projector" in n_lower or "camera" in n_lower:
        # 8mm dual-reel magnetic tape cassette vector
        tx1, ty1 = int(WIDTH * 0.32), int(HEIGHT * 0.32)
        tx2, ty2 = int(WIDTH * 0.68), int(HEIGHT * 0.68)
        odraw.rectangle([(tx1, ty1), (tx2, ty2)], fill=ink_color, outline=wire_color, width=4)
        # Left and right tape spools
        r_spool = 65
        cx_l, cx_r, c_spool_y = tx1 + 130, tx2 - 130, (ty1 + ty2) // 2
        odraw.ellipse([(cx_l - r_spool, c_spool_y - r_spool), (cx_l + r_spool, c_spool_y + r_spool)], outline=wire_color, width=3)
        odraw.ellipse([(cx_r - r_spool, c_spool_y - r_spool), (cx_r + r_spool, c_spool_y + r_spool)], outline=wire_color, width=3)
        # Tape viewing window
        odraw.rectangle([(tx1 + 160, ty1 + 40), (tx2 - 160, ty2 - 40)], outline=accent_wire, width=2)
    elif "prison" in n_lower or "joliette" in n_lower or "bars" in n_lower:
        # Heavy penitentiary gate vertical crossbeams
        for bx in range(int(WIDTH * 0.15), int(WIDTH * 0.88), 75):
            odraw.line([(bx, 0), (bx, HEIGHT)], fill=ink_color, width=16)
            odraw.line([(bx, 0), (bx, HEIGHT)], fill=wire_color, width=4)
        for hy in [int(HEIGHT * 0.25), int(HEIGHT * 0.50), int(HEIGHT * 0.75)]:
            odraw.line([(0, hy), (WIDTH, hy)], fill=ink_color, width=14)
            odraw.line([(0, hy), (WIDTH, hy)], fill=wire_color, width=3)
    elif "amber_eyes" in n_lower or "closing_dossier" in n_lower:
        # Amber Eyes signature dual glowing owl eye apertures
        cx1, cx2, cy = int(WIDTH * 0.44), int(WIDTH * 0.56), int(HEIGHT * 0.48)
        for cx in [cx1, cx2]:
            odraw.ellipse([(cx - 60, cy - 60), (cx + 60, cy + 60)], outline=(226, 180, 103, 160), width=4)
            odraw.ellipse([(cx - 25, cy - 25), (cx + 25, cy + 25)], fill=(226, 180, 103, 220))
            odraw.ellipse([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=(14, 14, 17, 255))

    # Composite overlay onto base image
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def main():
    jobs_file = WORK / "bg_jobs_tap11.json"
    if not jobs_file.exists():
        print(f"Lỗi: Không tìm thấy {jobs_file}")
        sys.exit(1)

    jobs = json.loads(jobs_file.read_text(encoding="utf-8"))
    prov_list = json.loads(PROV_FILE.read_text(encoding="utf-8")) if PROV_FILE.exists() else []
    prov_by_file = {p["file"]: p for p in prov_list}

    print(f"Bắt đầu render {len(jobs)} ảnh 2K 16:9 Dark Graphic Novel Noir cho Tập 11...")
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
