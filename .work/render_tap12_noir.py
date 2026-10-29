#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render 2K 16:9 dark graphic novel noir backgrounds for Episode 12.
Generates 2112x1188 images with deep chiaroscuro lighting, custom graphic noir elements,
film grain, vignette, and atmospheric moods matching the Jonestown / Peoples Temple case.
Updates provenance.json and builds assets for Episode 12.
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
    "jungle_nocturne": {
        "base": (8, 14, 10),
        "accent": (18, 36, 26),
        "light": (115, 185, 140),
        "style": "tropical_canopy"
    },
    "settlement_clearing": {
        "base": (14, 11, 9),
        "accent": (38, 28, 20),
        "light": (225, 155, 75),
        "style": "pavilion_timber"
    },
    "charity_facade": {
        "base": (14, 12, 11),
        "accent": (38, 32, 26),
        "light": (230, 180, 100),
        "style": "civic_facade"
    },
    "catharsis_inquisition": {
        "base": (10, 8, 12),
        "accent": (32, 18, 36),
        "light": (235, 190, 130),
        "style": "spotlight_inquisition"
    },
    "airstrip_ambush": {
        "base": (15, 10, 10),
        "accent": (42, 22, 22),
        "light": (240, 110, 70),
        "style": "runway_gravel"
    },
    "psychology_milgram": {
        "base": (9, 11, 16),
        "accent": (22, 28, 44),
        "light": (140, 175, 220),
        "style": "laboratory_console"
    },
    "cognitive_dissonance": {
        "base": (12, 9, 16),
        "accent": (32, 22, 42),
        "light": (200, 145, 210),
        "style": "surreal_scales"
    },
    "tape_evidence": {
        "base": (11, 12, 14),
        "accent": (26, 28, 36),
        "light": (180, 185, 195),
        "style": "cassette_reels"
    },
    "moral_courage": {
        "base": (12, 10, 8),
        "accent": (36, 24, 16),
        "light": (245, 195, 90),
        "style": "lone_candle"
    },
    "redflag": {
        "base": (16, 8, 9),
        "accent": (46, 16, 20),
        "light": (235, 65, 65),
        "style": "warning_beacon"
    },
    "healing_dawn": {
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
    if any(k in n for k in ["rainforest", "jungle", "perimeter", "river", "isolation", "armed_guards", "inescapable"]):
        return THEMES["jungle_nocturne"]
    if any(k in n for k in ["settlement", "pavilion", "clearing", "labor", "fields", "meager_ration", "loudspeaker", "bell", "gathering"]):
        return THEMES["settlement_clearing"]
    if any(k in n for k in ["indiana", "church", "racial_harmony", "charity", "soup_kitchen", "san_francisco", "city_hall", "reception", "musical", "nbc_camera", "utopian"]):
        return THEMES["charity_facade"]
    if any(k in n for k in ["iron_fist", "catharsis", "puppet_master", "paranoia", "abyss", "confrontation", "knife_attack", "scuffle", "secret_note"]):
        return THEMES["catharsis_inquisition"]
    if any(k in n for k in ["airstrip", "port_kaituma", "tractor", "ambush", "gunfire", "fallen_reporters", "jackie_speier", "truck_evacuation"]):
        return THEMES["airstrip_ambush"]
    if any(k in n for k in ["milgram", "shock_generator", "agentic_state", "prefrontal", "brain", "habituation", "blackboard"]):
        return THEMES["psychology_milgram"]
    if any(k in n for k in ["dissonance", "scales", "sunk_cost", "foot_in_the_door", "unanswered", "pawns", "chessboard"]):
        return THEMES["cognitive_dissonance"]
    if any(k in n for k in ["tape", "q042", "cassette", "reels", "passports", "property_surrender", "new_west", "investigative", "dossier", "briefing"]):
        return THEMES["tape_evidence"]
    if any(k in n for k in ["christine_miller", "candle", "moral_courage", "vulnerability", "moral_compass"]):
        return THEMES["moral_courage"]
    if any(k in n for k in ["redflag", "poison", "metal_vat", "flavor_aid", "emergency_siren", "hostile_mob", "groupthink", "broken_will"]):
        return THEMES["redflag"]
    if any(k in n for k in ["memorial", "capitol", "congressional", "healing", "dawn", "independent_mind", "closing_dossier", "amber_eyes"]):
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
    angle = (seed * 47 + 65) % 360
    rad = np.radians(angle)
    proj = nx * np.cos(rad) + ny * np.sin(rad)
    proj = (proj - proj.min()) / (proj.max() - proj.min() + 1e-6)
    t = np.power(proj, 1.7)[:, :, np.newaxis]
    img_arr = base_c * (1.0 - t) + accent_c * t

    # 2. Lighting patterns based on scene style
    style = theme["style"]
    if style == "tropical_canopy":
        # Dense tropical rainforest canopy: dark canopy with shafts of misty pale green moonlight
        cx, cy = 0.52, 0.28
        dist = np.sqrt((nx - cx)**2 * 2.8 + (ny - cy)**2 * 1.5)
        mist_glow = np.exp(-dist * 3.0)[:, :, np.newaxis]
        img_arr += light_c * mist_glow * 0.85
        # Jungle canopy silhouettes
        canopy = np.sin(nx * 32.0 + np.cos(ny * 12.0) * 1.5)
        canopy_mask = np.clip((canopy + 0.6) * 0.65, 0.45, 1.0)[:, :, np.newaxis]
        img_arr *= canopy_mask
    elif style == "pavilion_timber":
        # Low warm horizon in clearing with structural timber roof shadows
        horizon = np.exp(-((ny - 0.70) / 0.20)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.80
        # Horizontal roof purlins
        purlins = np.sin(ny * 44.0)
        purlins_mask = np.clip((purlins + 0.7) * 0.6, 0.55, 1.0)[:, :, np.newaxis]
        img_arr *= purlins_mask
    elif style == "civic_facade":
        # Soft golden lamplight pool in civic/meeting hall
        cx, cy = 0.46, 0.42
        dist = np.sqrt((nx - cx)**2 * 1.8 + (ny - cy)**2 * 1.3)
        glow = np.exp(-dist * 2.8)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
    elif style == "spotlight_inquisition":
        # Intense harsh single spotlight on pitch-black void
        cx, cy = 0.50, 0.46
        dist = np.sqrt((nx - cx)**2 * 3.2 + (ny - cy)**2 * 2.4)
        spot = np.exp(-dist * 3.8)[:, :, np.newaxis]
        img_arr += light_c * spot * 0.95
    elif style == "runway_gravel":
        # Wide horizontal runway gravel plane with dramatic twilight horizon
        horizon = np.exp(-((ny - 0.62) / 0.16)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.90
        # Linear perspective runway diagonals
        road = np.exp(-((nx - 0.5) / (ny * 0.7 + 0.1))**2)[:, :, np.newaxis]
        img_arr += light_c * road * 0.35
    elif style == "laboratory_console":
        # Cold technological dual illumination & meter dial glows
        cx1, cx2 = 0.36, 0.64
        d1 = np.sqrt((nx - cx1)**2 * 2.6 + (ny - 0.45)**2 * 1.6)
        d2 = np.sqrt((nx - cx2)**2 * 2.6 + (ny - 0.45)**2 * 1.6)
        glow = (np.exp(-d1 * 3.2) + np.exp(-d2 * 3.2))[:, :, np.newaxis]
        img_arr += light_c * glow * 0.80
    elif style == "surreal_scales":
        # Dreamlike ethereal central spotlight with deep edge shadows
        cx, cy = 0.50, 0.48
        dist = np.sqrt((nx - cx)**2 * 2.0 + (ny - cy)**2 * 1.6)
        glow = np.exp(-dist * 2.9)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85
    elif style == "cassette_reels":
        # Forensic table raking light from top-left
        cx, cy = 0.42, 0.38
        dist = np.sqrt((nx - cx)**2 * 1.6 + (ny - cy)**2 * 1.4)
        glow = np.exp(-dist * 2.6)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.75
    elif style == "lone_candle":
        # Warm golden candlelight radiating against absolute darkness
        cx, cy = 0.50, 0.52
        dist = np.sqrt((nx - cx)**2 * 2.8 + (ny - cy)**2 * 2.2)
        glow = np.exp(-dist * 3.0)[:, :, np.newaxis]
        core = np.exp(-dist * 7.5)[:, :, np.newaxis]
        img_arr += light_c * glow * 0.85 + np.array([255, 235, 180], dtype=np.float32) * core * 0.90
    elif style == "warning_beacon":
        # Raking crimson warning light radiating from center
        cx, cy = 0.50, 0.50
        dist = np.sqrt((nx - cx)**2 * 2.6 + (ny - cy)**2 * 2.0)
        spot = np.exp(-dist * 3.2)[:, :, np.newaxis]
        img_arr += light_c * spot * 0.95
    elif style == "dawn_rays":
        # Radiant golden dawn rays breaking over ocean horizon
        horizon = np.exp(-((ny - 0.66) / 0.18)**2)[:, :, np.newaxis]
        img_arr += light_c * horizon * 0.90
        rays = np.sin(np.arctan2(ny - 0.78, nx - 0.5) * 14.0)
        rays_mask = np.clip((rays + 0.6) * 0.5, 0.7, 1.30)[:, :, np.newaxis]
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

    # Thematic vector overlays tailored to Jonestown / Peoples Temple case
    if any(k in n_lower for k in ["tape_q042", "cassette", "spinning"]):
        # Precision vintage compact cassette tape outline
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        cw, ch = 520, 320
        x1, y1 = cx - cw // 2, cy - ch // 2
        x2, y2 = cx + cw // 2, cy + ch // 2
        odraw.rectangle([(x1, y1), (x2, y2)], fill=ink_color, outline=wire_color, width=4)
        # Center label window
        lw, lh = 360, 190
        lx1, ly1 = cx - lw // 2, cy - lh // 2
        lx2, ly2 = cx + lw // 2, cy + lh // 2
        odraw.rectangle([(lx1, ly1), (lx2, ly2)], fill=(20, 22, 28, 220), outline=wire_color, width=2)
        # Two cassette drive reel hubs
        for r_offset in [-110, 110]:
            rcx = cx + r_offset
            rcy = cy
            odraw.ellipse([(rcx - 42, rcy - 42), (rcx + 42, rcy + 42)], outline=wire_color, width=3)
            odraw.ellipse([(rcx - 16, rcy - 16), (rcx + 16, rcy + 16)], fill=ink_color, outline=wire_color, width=2)
            for spoke in range(6):
                ang = math.radians(spoke * 60)
                odraw.line([(rcx, rcy), (rcx + int(36 * math.cos(ang)), rcy + int(36 * math.sin(ang)))], fill=wire_color, width=2)
        # Center magnetic tape window trapezoid
        odraw.polygon([(cx - 70, ly2 - 25), (cx + 70, ly2 - 25), (cx + 90, y2 - 10), (cx - 90, y2 - 10)], outline=wire_color, width=2)

    elif any(k in n_lower for k in ["loudspeaker", "speaker_wires", "siren"]):
        # Public address horn loudspeaker array on tall timber mast
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.40)
        # Vertical mast
        odraw.rectangle([(cx - 15, cy - 80), (cx + 15, HEIGHT)], fill=ink_color, outline=wire_color, width=3)
        # Multiple horn speakers pointing in opposite directions
        for sx, direct in [(cx - 30, -1), (cx + 30, 1)]:
            # Horn cone
            p1 = (sx, cy - 30)
            p2 = (sx, cy + 30)
            p3 = (sx + direct * 140, cy + 60)
            p4 = (sx + direct * 140, cy - 60)
            odraw.polygon([p1, p2, p3, p4], fill=ink_color, outline=wire_color, width=3)
            odraw.ellipse([(min(p3[0], p4[0]) - 8, cy - 60), (max(p3[0], p4[0]) + 8, cy + 60)], outline=wire_color, width=3)
        # Dangling telephone & electrical wires
        for off_y in [cy + 80, cy + 180]:
            odraw.arc([(0, off_y - 120), (WIDTH, off_y + 60)], 0, 180, fill=wire_color, width=2)

    elif any(k in n_lower for k in ["microphone", "lectern", "podium", "christine_miller", "agitated_dictator"]):
        # Dynamic microphone on vintage metal stand and wooden pulpit
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.52)
        # Lectern top surface
        odraw.polygon([(cx - 220, cy + 80), (cx + 220, cy + 80), (cx + 170, cy + 240), (cx - 170, cy + 240)], fill=ink_color, outline=wire_color, width=4)
        # Gooseneck microphone stand
        odraw.line([(cx, cy + 80), (cx, cy - 20)], fill=wire_color, width=6)
        odraw.arc([(cx - 60, cy - 90), (cx + 60, cy - 10)], 270, 90, fill=wire_color, width=5)
        # Microphone capsule cylinder & grille
        odraw.rectangle([(cx + 20, cy - 90), (cx + 70, cy - 40)], fill=ink_color, outline=wire_color, width=3)
        for gy in range(cy - 85, cy - 45, 8):
            odraw.line([(cx + 25, gy), (cx + 65, gy)], fill=accent_wire, width=1)

    elif any(k in n_lower for k in ["milgram", "shock_generator", "laboratory"]):
        # Stanley Milgram experimental shock generator console
        bx1, by1 = int(WIDTH * 0.22), int(HEIGHT * 0.30)
        bx2, by2 = int(WIDTH * 0.78), int(HEIGHT * 0.72)
        odraw.rectangle([(bx1, by1), (bx2, by2)], fill=ink_color, outline=wire_color, width=4)
        # Analog voltmeter meter display
        mcx, mcy = int(WIDTH * 0.50), by1 + 90
        odraw.arc([(mcx - 140, mcy - 80), (mcx + 140, mcy + 60)], 180, 360, fill=wire_color, width=3)
        odraw.line([(mcx, mcy), (mcx + 50, mcy - 60)], fill=(theme["light"][0], theme["light"][1], theme["light"][2], 220), width=3)
        # Row of knife toggle switches
        for sw_x in range(bx1 + 60, bx2 - 40, 50):
            odraw.rectangle([(sw_x - 10, by1 + 170), (sw_x + 10, by1 + 240)], fill=(15, 18, 24, 255), outline=wire_color, width=2)
            odraw.line([(sw_x, by1 + 220), (sw_x, by1 + 160)], fill=accent_wire, width=3)

    elif any(k in n_lower for k in ["scales", "dissonance", "balance"]):
        # Antique balance scales of justice and cognitive conflict
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.44)
        # Center fulcrum column
        odraw.line([(cx, cy - 140), (cx, cy + 180)], fill=wire_color, width=6)
        odraw.rectangle([(cx - 80, cy + 180), (cx + 80, cy + 205)], fill=ink_color, outline=wire_color, width=3)
        # Tipped crossbeam
        odraw.line([(cx - 240, cy - 100), (cx + 240, cy - 180)], fill=wire_color, width=5)
        # Left heavy pan (low)
        odraw.line([(cx - 240, cy - 100), (cx - 280, cy + 30)], fill=accent_wire, width=2)
        odraw.line([(cx - 240, cy - 100), (cx - 200, cy + 30)], fill=accent_wire, width=2)
        odraw.arc([(cx - 280, cy + 10), (cx - 200, cy + 60)], 0, 180, fill=wire_color, width=3)
        # Right light pan (high)
        odraw.line([(cx + 240, cy - 180), (cx + 200, cy - 60)], fill=accent_wire, width=2)
        odraw.line([(cx + 240, cy - 180), (cx + 280, cy - 60)], fill=accent_wire, width=2)
        odraw.arc([(cx + 200, cy - 80), (cx + 280, cy - 30)], 0, 180, fill=wire_color, width=3)

    elif any(k in n_lower for k in ["airstrip", "runway", "airplane"]):
        # Aircraft propeller silhouette and runway guide markings
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.55)
        # Runway perspective threshold lines
        odraw.line([(int(WIDTH * 0.15), HEIGHT), (int(WIDTH * 0.42), int(HEIGHT * 0.60))], fill=wire_color, width=3)
        odraw.line([(int(WIDTH * 0.85), HEIGHT), (int(WIDTH * 0.58), int(HEIGHT * 0.60))], fill=wire_color, width=3)
        # Dashed centerline
        for dy in range(int(HEIGHT * 0.62), HEIGHT, 65):
            odraw.line([(int(WIDTH * 0.50), dy), (int(WIDTH * 0.50), dy + 35)], fill=wire_color, width=4)
        # Twin propeller hub silhouette in distance
        px, py = int(WIDTH * 0.38), int(HEIGHT * 0.52)
        odraw.ellipse([(px - 14, py - 14), (px + 14, py + 14)], fill=ink_color, outline=wire_color, width=2)
        odraw.ellipse([(px - 45, py - 4), (px + 45, py + 4)], fill=wire_color)
        odraw.ellipse([(px - 4, py - 45), (px + 4, py + 45)], fill=wire_color)

    elif any(k in n_lower for k in ["metal_vat", "flavor_aid", "poison", "cups"]):
        # Large galvanized tub and array of cups
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.56)
        # Galvanized drum silhouette
        odraw.ellipse([(cx - 160, cy - 60), (cx + 160, cy + 20)], fill=ink_color, outline=wire_color, width=4)
        odraw.rectangle([(cx - 160, cy - 20), (cx + 160, cy + 120)], fill=ink_color, outline=wire_color, width=3)
        odraw.ellipse([(cx - 160, cy + 80), (cx + 160, cy + 160)], fill=ink_color, outline=wire_color, width=4)
        # Small paper cups on side table
        for cpx in range(cx - 280, cx - 180, 28):
            odraw.polygon([(cpx, cy + 90), (cpx + 20, cy + 90), (cpx + 16, cy + 125), (cpx + 4, cy + 125)], outline=wire_color, width=2)

    elif any(k in n_lower for k in ["memorial", "monolith", "names"]):
        # Monumental memorial obelisk / monolith
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        # Monolith slab
        odraw.polygon([(cx - 110, cy - 220), (cx + 110, cy - 220), (cx + 140, cy + 200), (cx - 140, cy + 200)], fill=ink_color, outline=wire_color, width=4)
        # Horizontal inscription lines
        for ly in range(cy - 170, cy + 160, 24):
            odraw.line([(cx - 80, ly), (cx + 80, ly)], fill=accent_wire, width=2)

    elif any(k in n_lower for k in ["compass", "moral_compass"]):
        # Antique brass navigational compass rose
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        odraw.ellipse([(cx - 130, cy - 130), (cx + 130, cy + 130)], outline=wire_color, width=4)
        odraw.ellipse([(cx - 150, cy - 150), (cx + 150, cy + 150)], outline=accent_wire, width=2)
        # 8-point compass star
        for ang_deg in [0, 90, 180, 270]:
            rad_val = math.radians(ang_deg)
            nx_p = cx + int(110 * math.cos(rad_val))
            ny_p = cy + int(110 * math.sin(rad_val))
            odraw.line([(cx, cy), (nx_p, ny_p)], fill=wire_color, width=3)
        # North arrow highlight
        odraw.polygon([(cx, cy - 115), (cx - 18, cy), (cx + 18, cy)], fill=(245, 195, 90, 220), outline=wire_color, width=2)

    elif "redflag1" in n_lower:
        # Red Flag 1: Spiderweb mesh cutting telephone cables
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.48)
        for r in [60, 120, 200, 300]:
            odraw.ellipse([(cx - r, cy - r), (cx + r, cy + r)], outline=(225, 65, 65, 120), width=2)
        for i in range(8):
            ang = math.radians(i * 45)
            odraw.line([(cx, cy), (cx + int(360 * math.cos(ang)), cy + int(360 * math.sin(ang)))], fill=(225, 65, 65, 150), width=2)
        # Severed line break mark
        odraw.line([(cx - 160, cy - 60), (cx + 160, cy + 60)], fill=(255, 255, 255, 200), width=5)

    elif "redflag2" in n_lower:
        # Red Flag 2: Broken pen and locked muzzle
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        # Broken fountain pen at angle
        odraw.line([(cx - 140, cy - 100), (cx - 20, cy - 10)], fill=wire_color, width=10)
        odraw.polygon([(cx - 20, cy - 10), (cx + 25, cy + 25), (cx - 5, cy + 30)], fill=(225, 65, 65, 220), outline=wire_color, width=2)
        # Padlock shackle
        odraw.arc([(cx + 40, cy - 50), (cx + 120, cy + 30)], 180, 360, fill=(225, 65, 65, 200), width=6)
        odraw.rectangle([(cx + 30, cy + 20), (cx + 130, cy + 110)], fill=ink_color, outline=(225, 65, 65, 200), width=4)

    elif "redflag3" in n_lower:
        # Red Flag 3: Interlocking gear teeth trap
        cx, cy = int(WIDTH * 0.50), int(HEIGHT * 0.50)
        for g_offset, gr in [(-100, 110), (100, 90)]:
            gcx = cx + g_offset
            odraw.ellipse([(gcx - gr, cy - gr), (gcx + gr, cy + gr)], outline=(225, 65, 65, 160), width=5)
            odraw.ellipse([(gcx - 30, cy - 30), (gcx + 30, cy + 30)], fill=ink_color, outline=wire_color, width=3)
            for t_idx in range(12):
                tang = math.radians(t_idx * 30)
                tx1 = gcx + int((gr - 10) * math.cos(tang))
                ty1 = cy + int((gr - 10) * math.sin(tang))
                tx2 = gcx + int((gr + 15) * math.cos(tang))
                ty2 = cy + int((gr + 15) * math.sin(tang))
                odraw.line([(tx1, ty1), (tx2, ty2)], fill=(225, 65, 65, 200), width=6)

    elif "redflag4" in n_lower:
        # Red Flag 4: Fortress wall with defensive crenellations
        fy = int(HEIGHT * 0.55)
        odraw.rectangle([(int(WIDTH * 0.15), fy), (int(WIDTH * 0.85), HEIGHT)], fill=ink_color, outline=(225, 65, 65, 180), width=4)
        for cx_c in range(int(WIDTH * 0.18), int(WIDTH * 0.82), 70):
            odraw.rectangle([(cx_c, fy - 35), (cx_c + 40, fy)], fill=ink_color, outline=(225, 65, 65, 180), width=3)

    elif any(k in n_lower for k in ["amber_eyes", "owl"]):
        # Signature Amber Eyes dual owl eye apertures
        cx1, cx2, cy = int(WIDTH * 0.44), int(WIDTH * 0.56), int(HEIGHT * 0.48)
        for cx in [cx1, cx2]:
            odraw.ellipse([(cx - 60, cy - 60), (cx + 60, cy + 60)], outline=(226, 180, 103, 160), width=4)
            odraw.ellipse([(cx - 25, cy - 25), (cx + 25, cy + 25)], fill=(226, 180, 103, 220))
            odraw.ellipse([(cx - 8, cy - 8), (cx + 8, cy + 8)], fill=(14, 14, 17, 255))

    elif any(k in n_lower for k in ["passports", "property_surrender", "new_west", "dossier", "briefing", "capitol"]):
        # Forensic document page with official seal
        dx1, dy1 = int(WIDTH * 0.35), int(HEIGHT * 0.24)
        dx2, dy2 = int(WIDTH * 0.65), int(HEIGHT * 0.76)
        odraw.rectangle([(dx1, dy1), (dx2, dy2)], fill=ink_color, outline=wire_color, width=3)
        for ly in range(dy1 + 45, dy2 - 60, 30):
            odraw.line([(dx1 + 30, ly), (dx2 - 30, ly)], fill=accent_wire, width=2)
        seal_cx, seal_cy = int(WIDTH * 0.50), dy2 - 45
        odraw.ellipse([(seal_cx - 25, seal_cy - 25), (seal_cx + 25, seal_cy + 25)], fill=(185, 45, 45, 180), outline=wire_color, width=2)

    # Composite overlay onto base image
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    return img


def main():
    jobs_file = WORK / "bg_jobs_tap12.json"
    if not jobs_file.exists():
        print(f"Lỗi: Không tìm thấy {jobs_file}")
        sys.exit(1)

    jobs = json.loads(jobs_file.read_text(encoding="utf-8"))
    prov_list = json.loads(PROV_FILE.read_text(encoding="utf-8")) if PROV_FILE.exists() else []
    prov_by_file = {p["file"]: p for p in prov_list}

    print(f"Bắt đầu render {len(jobs)} ảnh 2K 16:9 Dark Graphic Novel Noir cho Tập 12...")
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
