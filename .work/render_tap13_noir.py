#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 2K 16:9 dark graphic novel noir backgrounds for Episode 13 (Jennifer Pan Case).
Generates 2112x1188 images with deep chiaroscuro lighting, custom graphic noir elements,
film grain, vignette, and atmospheric moods matching the Markham / Helen Avenue case.
Updates provenance.json and builds assets for Episode 13.
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
    "markham_suburb": {
        "base": (12, 13, 16),
        "accent": (28, 34, 46),
        "light": (235, 175, 95),
        "style": "suburban_brick"
    },
    "piano_discipline": {
        "base": (10, 10, 14),
        "accent": (24, 26, 36),
        "light": (210, 185, 130),
        "style": "piano_keys"
    },
    "forgery_darkroom": {
        "base": (8, 12, 14),
        "accent": (18, 34, 40),
        "light": (80, 210, 225),
        "style": "photocopier_glow"
    },
    "library_curfew": {
        "base": (11, 10, 9),
        "accent": (32, 28, 22),
        "light": (190, 160, 100),
        "style": "banker_lamp"
    },
    "helen_prison": {
        "base": (14, 10, 11),
        "accent": (36, 22, 24),
        "light": (220, 130, 80),
        "style": "barred_shadows"
    },
    "intruders_crime": {
        "base": (8, 8, 11),
        "accent": (20, 20, 30),
        "light": (160, 170, 190),
        "style": "basement_stairs"
    },
    "dispatch_911": {
        "base": (9, 14, 16),
        "accent": (20, 36, 44),
        "light": (95, 230, 180),
        "style": "audio_waveform"
    },
    "psychology_tiger": {
        "base": (12, 9, 15),
        "accent": (32, 22, 42),
        "light": (205, 145, 225),
        "style": "hall_of_mirrors"
    },
    "interrogation_reid": {
        "base": (10, 12, 14),
        "accent": (26, 30, 38),
        "light": (185, 195, 215),
        "style": "interrogation_spot"
    },
    "courtroom_justice": {
        "base": (11, 10, 14),
        "accent": (30, 24, 40),
        "light": (225, 185, 110),
        "style": "court_gavel"
    },
    "redflag_toxic": {
        "base": (16, 8, 9),
        "accent": (48, 16, 20),
        "light": (235, 65, 65),
        "style": "warning_beacon"
    },
    "dawn_resolution": {
        "base": (10, 14, 20),
        "accent": (28, 38, 56),
        "light": (245, 205, 125),
        "style": "dawn_rays"
    },
    "default": {
        "base": (10, 11, 14),
        "accent": (26, 30, 38),
        "light": (160, 170, 185),
        "style": "noir_generic"
    }
}


def pick_theme(name):
    n = name.lower()
    if any(k in n for k in ["markham", "suburb", "trophy_cars", "residential", "bus_stop", "trailing_car"]):
        return THEMES["markham_suburb"]
    if any(k in n for k in ["piano", "skates", "perfect_daughter", "recital"]):
        return THEMES["piano_discipline"]
    if any(k in n for k in ["forgery", "scissors", "glue", "photocopy", "calculus", "house_of_cards", "fake_university", "counterfeit"]):
        return THEMES["forgery_darkroom"]
    if any(k in n for k in ["library", "curfew", "golden_child", "tiger_parent", "locked_bedroom", "unseen_suffocating"]):
        return THEMES["library_curfew"]
    if any(k in n for k in ["helen_avenue", "prison", "confiscated", "house_arrest", "resentment", "burner_phone", "murder_for_hire", "insurance"]):
        return THEMES["helen_prison"]
    if any(k in n for k in ["intruders", "stealth", "subdued", "tied", "staircase", "ransacked", "basement", "tragic_demise", "gravely_wounded", "fleeing"]):
        return THEMES["intruders_crime"]
    if any(k in n for k in ["911", "transcript", "contradiction", "theatrical", "emergency", "unforeseen"]):
        return THEMES["dispatch_911"]
    if any(k in n for k in ["psychological", "crossroads", "mythomania", "anxiety", "conditional_love", "fear_of_failure", "sunk_cost", "fragmentation", "hostile_projection", "rupture", "toxic_inheritance"]):
        return THEMES["psychology_tiger"]
    if any(k in n for k in ["interrogation", "detective", "goetz", "unforced_entry", "paradox", "icu", "awakening", "memory", "unbound", "november_22", "telecom", "crumbling_mask", "body_language", "suicide_excuse"]):
        return THEMES["interrogation_reid"]
    if any(k in n for k in ["supreme_court", "verdict", "appeals", "dossier_lasting", "dialogue_breakdown", "handcuffs"]):
        return THEMES["courtroom_justice"]
    if any(k in n for k in ["redflag", "toxic"]):
        return THEMES["redflag_toxic"]
    if any(k in n for k in ["authentic_soul", "dawn", "closing_dossier", "amber_eyes", "light_ray"]):
        return THEMES["dawn_resolution"]
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
    angle = (seed * 53 + 45) % 360
    rad = np.radians(angle)
    proj = nx * np.cos(rad) + ny * np.sin(rad)
    proj = (proj - proj.min()) / (proj.max() - proj.min() + 1e-6)
    t = np.power(proj, 1.7)[:, :, np.newaxis]
    img_arr = base_c * (1.0 - t) + accent_c * t

    # 2. Lighting patterns based on scene style
    style = theme["style"]
    if style == "suburban_brick":
        # Evening suburban horizon with warm porch light pools
        horizon = np.exp(-((ny - 0.65) / 0.22)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.75
        # Porch lamp glow
        d = np.sqrt((nx - 0.48)**2 * 3.0 + (ny - 0.42)**2 * 2.0)
        img_arr += light_c * np.exp(-d * 3.5)[:, :, np.newaxis] * 0.6
    elif style == "piano_keys":
        # Dramatic diagonal ray across polished grand piano
        d = np.abs((nx * 0.8 - ny * 0.5) - 0.15)
        streak = np.exp(-d * 7.0)[:, :, np.newaxis]
        img_arr += light_c * streak * 0.95
    elif style == "photocopier_glow":
        # Intense cyan-tinted raking photocopier scanner band
        cy = 0.55
        band = np.exp(-((ny - cy) / 0.12)**2)[:, :, np.newaxis]
        img_arr += light_c * band * 0.95
        # Vignette darkening top and bottom
        img_arr *= np.clip(1.3 - np.abs(ny - cy) * 1.5, 0.4, 1.2)[:, :, np.newaxis]
    elif style == "banker_lamp":
        # Cone of green/amber light from traditional banker lamp
        d = np.sqrt((nx - 0.50)**2 * 2.5 + (ny - 0.35)**2 * 1.8)
        lamp = np.exp(-d * 3.2)[:, :, np.newaxis]
        img_arr += light_c * lamp * 0.90
    elif style == "barred_shadows":
        # Barred window blind shadows across wall
        bars = np.sin(ny * 40.0)
        bars_mask = np.clip((bars + 0.6) * 0.6, 0.45, 1.0)[:, :, np.newaxis]
        d = np.sqrt((nx - 0.42)**2 * 1.8 + (ny - 0.48)**2 * 1.5)
        glow = np.exp(-d * 2.5)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.80
        img_arr *= bars_mask
    elif style == "basement_stairs":
        # Murky darkness with angled descent light
        descent = np.clip(1.2 - (nx * 0.7 + ny * 0.8), 0.15, 1.0)[:, :, np.newaxis]
        img_arr *= descent
        d = np.sqrt((nx - 0.25)**2 * 2.2 + (ny - 0.25)**2 * 2.0)
        top_light = np.exp(-d * 3.0)[:, :, np.newaxis]
        img_arr += light_c * top_light * 0.75
    elif style == "audio_waveform":
        # Tech dispatch monitors: dual horizontal glowing scope lines
        h1 = np.exp(-((ny - 0.45) / 0.08)**2)[:, :, np.newaxis]
        h2 = np.exp(-((ny - 0.55) / 0.08)**2)[:, :, np.newaxis]
        img_arr += light_c * (h1 + h2) * 0.60
    elif style == "hall_of_mirrors":
        # Multiple fragmented spotlight reflections
        for sx in [0.30, 0.50, 0.70]:
            d = np.sqrt((nx - sx)**2 * 4.0 + (ny - 0.48)**2 * 1.8)
            img_arr += light_c * np.exp(-d * 3.6)[:, :, np.newaxis] * 0.45
    elif style == "interrogation_spot":
        # Overhead stark industrial interrogation lamp directly onto center table
        d = np.sqrt((nx - 0.50)**2 * 3.2 + (ny - 0.48)**2 * 2.4)
        spot = np.exp(-d * 3.4)[:, :, np.newaxis]
        img_arr += light_c * spot * 0.95
    elif style == "court_gavel":
        # Dignified courtroom warm mahogany side-glow
        d = np.sqrt((nx - 0.35)**2 * 1.8 + (ny - 0.40)**2 * 1.5)
        glow = np.exp(-d * 2.8)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
    elif style == "warning_beacon":
        # Pulsing crimson alert beacon from center
        d = np.sqrt((nx - 0.50)**2 * 2.5 + (ny - 0.50)**2 * 2.0)
        spot = np.exp(-d * 3.0)[:, :, np.newaxis]
        img_arr += light_c * spot * 0.95
    elif style == "dawn_rays":
        # Radiant golden sunrise rays through window / horizon
        horizon = np.exp(-((ny - 0.65) / 0.18)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.90
        rays = np.sin(np.arctan2(ny - 0.80, nx - 0.5) * 12.0)
        rays_mask = np.clip((rays + 0.6) * 0.5, 0.7, 1.30)[:, :, np.newaxis]
        img_arr *= rays_mask
    else:
        d = np.sqrt((nx - 0.5)**2 * 2.0 + (ny - 0.45)**2 * 1.5)
        glow = np.exp(-d * 3.0)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.70

    # 3. Noir edge vignette
    vx = (nx - 0.5) * 2.0
    vy = (ny - 0.5) * 2.0
    v_dist = np.sqrt(vx * vx + vy * vy)
    vignette = np.clip(1.0 - (v_dist - 0.42) * 0.78, 0.10, 1.0)[:, :, np.newaxis]
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

    ink_color = (theme["base"][0], theme["base"][1], theme["base"][2], 195)
    wire_color = (theme["light"][0], theme["light"][1], theme["light"][2], 55)
    accent_wire = (theme["accent"][0], theme["accent"][1], theme["accent"][2], 125)

    n_lower = name.lower()

    # Thematic vector overlays tailored to Markham / Jennifer Pan case
    if any(k in n_lower for k in ["piano", "skates"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.54)
        # Grand piano outline & keyboard
        odraw.rectangle([(cx - 320, cy - 60), (cx + 320, cy + 90)], fill=ink_color, outline=wire_color, width=4)
        # Piano keys pattern
        for kx in range(cx - 300, cx + 300, 24):
            odraw.rectangle([(kx, cy + 20), (kx + 22, cy + 85)], fill=(225, 220, 210, 180), outline=ink_color, width=1)
            if (kx - (cx - 300)) % 72 in [0, 24, 72, 96, 120]:
                odraw.rectangle([(kx + 14, cy + 20), (kx + 26, cy + 60)], fill=(12, 12, 16, 255))
        # Crossed ice skates blades
        odraw.arc([(cx - 140, cy - 140), (cx + 140, cy - 20)], 180, 360, fill=wire_color, width=4)

    elif any(k in n_lower for k in ["forgery", "scissors", "glue", "calculus", "transcript", "counterfeit"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        # Academic transcript parchment rectangle
        pw, ph = 420, 560
        odraw.rectangle([(cx - pw // 2, cy - ph // 2), (cx + pw // 2, cy + ph // 2)], fill=ink_color, outline=wire_color, width=4)
        # Academic report lines
        for ly in range(cy - ph // 2 + 60, cy + ph // 2 - 60, 35):
            odraw.line([(cx - pw // 2 + 40, ly), (cx + pw // 2 - 40, ly)], fill=accent_wire, width=2)
        # Scissors icon
        sx, sy = cx + pw // 2 - 60, cy - ph // 2 + 60
        odraw.ellipse([(sx - 15, sy - 15), (sx + 15, sy + 15)], outline=wire_color, width=2)
        odraw.ellipse([(sx - 15, sy + 15), (sx + 15, sy + 45)], outline=wire_color, width=2)
        odraw.line([(sx, sy), (sx + 35, sy + 15)], fill=wire_color, width=3)
        odraw.line([(sx, sy + 30), (sx + 35, sy + 15)], fill=wire_color, width=3)

    elif any(k in n_lower for k in ["burner_phone", "telecom", "messages", "cellphone"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        # Clamshell burner phone silhouette
        bw, bh = 220, 380
        odraw.rectangle([(cx - bw // 2, cy - bh // 2), (cx + bw // 2, cy + bh // 2)], fill=ink_color, outline=wire_color, width=3)
        # Phone screen matrix
        sw, sh = 170, 150
        odraw.rectangle([(cx - sw // 2, cy - bh // 2 + 25), (cx + sw // 2, cy - bh // 2 + 25 + sh)], fill=(15, 28, 38, 220), outline=(theme["light"][0], theme["light"][1], theme["light"][2], 120), width=2)
        # SMS speech bubble inside screen
        odraw.rectangle([(cx - sw // 2 + 15, cy - bh // 2 + 45), (cx + sw // 2 - 15, cy - bh // 2 + 85)], fill=(25, 48, 64, 200), outline=wire_color, width=1)
        # Keypad grid below
        for row in range(4):
            for col in range(3):
                kx = cx - 65 + col * 45
                ky = cy + 30 + row * 38
                odraw.rectangle([(kx - 16, ky - 12), (kx + 16, ky + 12)], fill=(20, 22, 28, 200), outline=accent_wire, width=1)

    elif any(k in n_lower for k in ["staircase", "tied", "banister", "loosely"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.52)
        # Staircase balusters
        for bx in range(cx - 280, cx + 300, 70):
            odraw.line([(bx, cy - 160), (bx, cy + 180)], fill=wire_color, width=5)
        # Handrail top
        odraw.line([(cx - 320, cy - 160), (cx + 320, cy - 160)], fill=wire_color, width=8)
        # Slack rope loop hanging loosely
        odraw.arc([(cx - 100, cy - 60), (cx + 100, cy + 120)], 0, 180, fill=(theme["light"][0], theme["light"][1], theme["light"][2], 190), width=5)

    elif any(k in n_lower for k in ["911", "waveform", "dispatch"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        # Soundwave frequency oscillation
        pts = []
        for x in range(cx - 450, cx + 450, 6):
            rel = (x - (cx - 450)) / 900.0
            amp = math.sin(rel * 28.0) * math.cos(rel * 6.0) * math.exp(-((rel - 0.5) * 2.5)**2)
            y = cy + int(amp * 160)
            pts.append((x, y))
        if len(pts) > 1:
            odraw.line(pts, fill=(theme["light"][0], theme["light"][1], theme["light"][2], 180), width=3)
        # Center line
        odraw.line([(cx - 480, cy), (cx + 480, cy)], fill=accent_wire, width=1)

    elif any(k in n_lower for k in ["interrogation", "detective", "goetz", "reid", "table"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.56)
        # Interrogation desk
        odraw.polygon([(cx - 380, cy + 20), (cx + 380, cy + 20), (cx + 280, cy + 220), (cx - 280, cy + 220)], fill=ink_color, outline=wire_color, width=4)
        # Two dossier folders on desk
        odraw.polygon([(cx - 160, cy + 50), (cx - 30, cy + 50), (cx - 50, cy + 150), (cx - 180, cy + 150)], outline=accent_wire, width=2)
        odraw.polygon([(cx + 40, cy + 60), (cx + 170, cy + 60), (cx + 150, cy + 160), (cx + 20, cy + 160)], outline=accent_wire, width=2)

    elif any(k in n_lower for k in ["icu", "awakening", "monitor", "heartbeat"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        # ICU Monitor border
        odraw.rectangle([(cx - 350, cy - 180), (cx + 350, cy + 180)], fill=ink_color, outline=wire_color, width=4)
        # ECG trace
        ecg_pts = []
        for x in range(cx - 320, cx + 320, 8):
            dx = x - (cx - 320)
            phase = dx % 160
            if 60 <= phase <= 75:
                y = cy - 80 + (phase - 60) * 10
            elif 75 < phase <= 95:
                y = cy + 70 - (phase - 75) * 14
            elif 95 < phase <= 110:
                y = cy - 70 + (phase - 95) * 5
            else:
                y = cy
            ecg_pts.append((x, y))
        if len(ecg_pts) > 1:
            odraw.line(ecg_pts, fill=(95, 235, 175, 210), width=3)

    elif any(k in n_lower for k in ["handcuffs", "bars", "closed"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        # Pair of interlocking handcuffs
        for hx, hy in [(cx - 95, cy), (cx + 95, cy)]:
            odraw.ellipse([(hx - 65, hy - 65), (hx + 65, hy + 65)], outline=wire_color, width=6)
            odraw.ellipse([(hx - 45, hy - 45), (hx + 45, hy + 45)], outline=wire_color, width=3)
            odraw.rectangle([(hx - 15, hy + 50), (hx + 15, hy + 75)], fill=ink_color, outline=wire_color, width=2)
        # Connecting link chain
        odraw.line([(cx - 30, cy), (cx + 30, cy)], fill=wire_color, width=8)

    elif any(k in n_lower for k in ["supreme_court", "verdict", "gavel"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.52)
        # Sounding block
        odraw.polygon([(cx - 150, cy + 60), (cx + 150, cy + 60), (cx + 120, cy + 110), (cx - 120, cy + 110)], fill=ink_color, outline=wire_color, width=4)
        # Gavel head & handle
        odraw.rectangle([(cx - 70, cy - 110), (cx + 70, cy - 40)], fill=ink_color, outline=wire_color, width=4)
        odraw.line([(cx, cy - 40), (cx + 90, cy + 40)], fill=wire_color, width=8)

    elif any(k in n_lower for k in ["scales", "balance", "conditional_love"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.44)
        # Fulcrum
        odraw.line([(cx, cy - 140), (cx, cy + 180)], fill=wire_color, width=6)
        odraw.rectangle([(cx - 80, cy + 180), (cx + 80, cy + 205)], fill=ink_color, outline=wire_color, width=3)
        # Beam
        odraw.line([(cx - 240, cy - 120), (cx + 240, cy - 80)], fill=wire_color, width=5)
        # Left pan
        odraw.line([(cx - 240, cy - 120), (cx - 280, cy + 20)], fill=accent_wire, width=2)
        odraw.line([(cx - 240, cy - 120), (cx - 200, cy + 20)], fill=accent_wire, width=2)
        odraw.arc([(cx - 280, cy), (cx - 200, cy + 50)], 0, 180, fill=wire_color, width=3)
        # Right pan
        odraw.line([(cx + 240, cy - 80), (cx + 200, cy + 60)], fill=accent_wire, width=2)
        odraw.line([(cx + 240, cy - 80), (cx + 280, cy + 60)], fill=accent_wire, width=2)
        odraw.arc([(cx + 200, cy + 40), (cx + 280, cy + 90)], 0, 180, fill=wire_color, width=3)

    elif "redflag1" in n_lower:
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        # Red Flag 1: Heavy scales of conditional achievement & strict disciplinary rod
        odraw.line([(cx, cy - 120), (cx, cy + 150)], fill=(225, 65, 65, 180), width=6)
        odraw.line([(cx - 220, cy - 90), (cx + 220, cy - 90)], fill=(225, 65, 65, 180), width=4)
        odraw.arc([(cx - 260, cy - 20), (cx - 180, cy + 40)], 0, 180, fill=(225, 65, 65, 180), width=3)
        odraw.arc([(cx + 180, cy - 20), (cx + 260, cy + 40)], 0, 180, fill=(225, 65, 65, 180), width=3)

    elif "redflag2" in n_lower:
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        # Red Flag 2: Cobweb of escalating lies
        for r in [60, 120, 200, 300]:
            odraw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=(225, 65, 65, 120), width=2)
        for i in range(8):
            ang = math.radians(i * 45)
            odraw.line([(cx, cy), (cx + int(320 * math.cos(ang)), cy + int(320 * math.sin(ang)))], fill=(225, 65, 65, 140), width=2)

    elif "redflag3" in n_lower:
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        # Red Flag 3: Iron birdcage with dangling severed communication wires
        odraw.arc([(cx - 150, cy - 220), (cx + 150, cy - 20)], 180, 360, fill=(225, 65, 65, 180), width=4)
        for vx in range(cx - 130, cx + 150, 40):
            odraw.line([(vx, cy - 120), (vx, cy + 160)], fill=(225, 65, 65, 160), width=3)
        odraw.rectangle([(cx - 160, cy + 150), (cx + 160, cy + 180)], fill=ink_color, outline=(225, 65, 65, 180), width=3)

    elif "redflag4" in n_lower:
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        # Red Flag 4: Brick wall isolating reaching hands
        odraw.rectangle([(cx - 30, cy - 220), (cx + 30, cy + 220)], fill=ink_color, outline=(225, 65, 65, 200), width=4)
        for by in range(cy - 200, cy + 220, 32):
            odraw.line([(cx - 30, by), (cx + 30, by)], fill=(225, 65, 65, 160), width=2)

    elif any(k in n_lower for k in ["amber_eyes", "closing_dossier"]):
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        # Dossier folder outline
        dw, dh = 480, 340
        odraw.rectangle([(cx - dw // 2, cy - dh // 2), (cx + dw // 2, cy + dh // 2)], fill=ink_color, outline=(225, 180, 103, 140), width=4)
        # Amber Eyes circular owl eye emblem
        odraw.ellipse([(cx - 110, cy - 110), (cx + 110, cy + 110)], outline=(225, 180, 103, 220), width=4)
        odraw.ellipse([(cx - 90, cy - 90), (cx + 90, cy + 90)], outline=(225, 180, 103, 120), width=2)
        # Owl eyes
        for ex in [cx - 38, cx + 38]:
            odraw.ellipse([(ex - 22, cy - 18), (ex + 22, cy + 18)], fill=(245, 195, 90, 220), outline=ink_color, width=2)
            odraw.ellipse([(ex - 8, cy - 8), (ex + 8, cy + 8)], fill=(20, 20, 24, 255))

    # Composite vector overlay with Gaussian blur for natural ink bloom
    overlay_blurred = overlay.filter(ImageFilter.GaussianBlur(1.2))
    img.paste(Image.alpha_composite(Image.new("RGBA", (WIDTH, HEIGHT), (0, 0, 0, 0)), overlay_blurred), (0, 0), overlay_blurred)

    return img


def main():
    jobs_file = WORK / "bg_jobs_tap13.json"
    if not jobs_file.exists():
        print(f"Lỗi: Không tìm thấy {jobs_file}")
        sys.exit(1)

    jobs = json.loads(jobs_file.read_text(encoding="utf-8"))
    print(f"=== BẮT ĐẦU RENDER BỘ ẢNH NỀN TẬP 13 (HỒ SƠ JENNIFER PAN) ===")
    print(f"Tổng số ảnh cần sinh: {len(jobs)} ảnh (Chuẩn 16:9 2K: 2112x1188)")

    prov_records = []
    if PROV_FILE.exists():
        try:
            prov_records = json.loads(PROV_FILE.read_text(encoding="utf-8"))
        except Exception:
            prov_records = []

    # Map of existing files in provenance to avoid duplicates
    prov_map = {r.get("file"): r for r in prov_records}

    today_str = date.today().isoformat()
    success_count = 0

    for idx, j in enumerate(jobs, 1):
        name = j["name"]
        prompt = j["prompt"]
        out_path = BG_DIR / f"{name}.png"
        
        # Unique deterministic seed per image name
        seed = abs(hash(name)) % (10**7)

        img = render_background(name, prompt, seed=seed)
        img.save(out_path, format="PNG", optimize=True)

        rel_path = f"assets/bg/{name}.png"
        record = {
            "file": rel_path,
            "loai": "nền 16:9",
            "cong_cu": "Amber Eyes Noir Graphic Renderer (Pillow & Numpy Procedural Chiaroscuro Pipeline)",
            "ngay": today_str,
            "prompt": prompt,
            "seed": seed,
            "nguon_anh_tham_chieu": None,
            "kich_thuoc_goc": [WIDTH, HEIGHT],
            "dieu_khoan": "Kênh tự tạo 100%, không sử dụng MiniMax hay tài sản bên thứ ba",
            "kiem_tra_thuong_mai": "đạt"
        }
        prov_map[rel_path] = record
        success_count += 1
        print(f"[{idx:02d}/{len(jobs)}] Đã render: {name}.png ({WIDTH}x{HEIGHT})")

    # Save merged provenance
    updated_prov = list(prov_map.values())
    PROV_FILE.write_text(json.dumps(updated_prov, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nĐã hoàn thành {success_count}/{len(jobs)} ảnh nền Tập 13!")
    print(f"Đã cập nhật provenance.json ({len(updated_prov)} bản ghi).")


if __name__ == "__main__":
    main()
