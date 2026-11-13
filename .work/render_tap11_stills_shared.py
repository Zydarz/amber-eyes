#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render toan bo anh tinh (stills) cho Tap 11 tren ca 3 ngon ngu (VI, EN, JA).
Tuan thu Rule H17, H5, T23, T24, L3, L5:
- 1 anh nen goc assets/bg/t11_*.png dung chung cho ca 3 ngon ngu.
- Chen lop chu, layout template (T1, T4, T8, T10, T2) va avatar linh thu theo tung ngon ngu.
- Luu vao:
    .work/video3_t11/stills/
    .work/video3_EN_t11/stills/
    .work/video3_JA_t11/stills/
"""
import os
import sys
import time
import importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))

def load_builder(lang):
    for m in list(sys.modules):
        if m in ("build_video3", "edition"):
            del sys.modules[m]
    os.environ["AE_EP"] = "11"
    if lang:
        os.environ["AE_LANG"] = lang
    else:
        os.environ.pop("AE_LANG", None)
    return importlib.import_module("build_video3")

def main():
    t_start = time.perf_counter()
    print("=== BAT DAU RENDER ANH TINH TAP 11 (3 NGON NGU) ===")
    
    # 1. Load builder cho 3 ngon ngu
    b_vi = load_builder(None)
    b_en = load_builder("en")
    b_ja = load_builder("ja")
    
    builders = {
        "vi": (b_vi, b_vi.ED.w("video3") / "stills"),
        "en": (b_en, b_en.ED.w("video3") / "stills"),
        "ja": (b_ja, b_ja.ED.w("video3") / "stills"),
    }
    
    for _, sd in builders.values():
        sd.mkdir(parents=True, exist_ok=True)
        
    by_id_vi = {s["id"]: s for s in b_vi.SH}
    by_id_en = {s["id"]: s for s in b_en.SH}
    by_id_ja = {s["id"]: s for s in b_ja.SH}
    
    all_tokens = [s["id"] for s in b_vi.SH]
    total_shots = len(all_tokens)
    print(f"Tong so shot can render: {total_shots} shot x 3 ngon ngu = {total_shots * 3} anh tinh")
    
    rendered_counts = {"vi": 0, "en": 0, "ja": 0}
    
    for idx, token in enumerate(all_tokens, 1):
        s_vi = by_id_vi[token]
        s_en = by_id_en[token]
        s_ja = by_id_ja[token]
        
        # Tinh thoi diem chup giua shot cho tung ngon ngu (co bu gio cho cac doan phu)
        def get_t_sec(b_mod, s):
            t_mid = (s["start"] + s["end"]) / 2
            _ts = b_mod.seg_times(s)
            if len(_ts) > 1:
                t_all = max(_ts) + 0.6
                t_mid = min(max(t_mid, t_all), s["end"] - 0.15)
            return t_mid
            
        t_vi = get_t_sec(b_vi, s_vi)
        t_en = get_t_sec(b_en, s_en)
        t_ja = get_t_sec(b_ja, s_ja)
        
        fi_vi = int(t_vi * b_vi.FPS)
        fi_en = int(t_en * b_en.FPS)
        fi_ja = int(t_ja * b_ja.FPS)
        
        out_name = f"shot_{token}.png"
        
        # Shot dac biet: intro (1-00) hoac shot cuoi co fade den (5-29) -> render qua render() rieng
        is_special = (token == "1-00" or token == all_tokens[-1] or s_vi.get("bg2"))
        
        if is_special:
            # Render rieng de dam bao dung hieu ung dac biet
            img_vi = b_vi.render(fi_vi).convert("RGB")
            img_en = b_en.render(fi_en).convert("RGB")
            img_ja = b_ja.render(fi_ja).convert("RGB")
        else:
            # Phuong phap tieu chuan T23, T24, H17:
            # Dung chung nen goc 1 lan -> Tiet kiem thoi gian, nhat quan thi giac
            base_frame = b_vi.bg_frame(s_vi, t_vi, fi_vi)
            
            # VI
            fr_vi = base_frame.copy()
            for e in b_vi.build_elements(s_vi):
                e.draw(fr_vi, t_vi)
            b_vi.draw_characters(fr_vi, t_vi, fi_vi, s_vi)
            img_vi = fr_vi.convert("RGB")
            
            # EN
            fr_en = base_frame.copy()
            for e in b_en.build_elements(s_en):
                e.draw(fr_en, t_en)
            b_en.draw_characters(fr_en, t_en, fi_en, s_en)
            img_en = fr_en.convert("RGB")
            
            # JA
            fr_ja = base_frame.copy()
            for e in b_ja.build_elements(s_ja):
                e.draw(fr_ja, t_ja)
            b_ja.draw_characters(fr_ja, t_ja, fi_ja, s_ja)
            img_ja = fr_ja.convert("RGB")
            
        # Luu file
        img_vi.save(builders["vi"][1] / out_name)
        img_en.save(builders["en"][1] / out_name)
        img_ja.save(builders["ja"][1] / out_name)
        
        rendered_counts["vi"] += 1
        rendered_counts["en"] += 1
        rendered_counts["ja"] += 1
        
        if idx % 25 == 0 or idx == total_shots:
            dt = time.perf_counter() - t_start
            speed = idx / dt
            rem = (total_shots - idx) / speed if speed > 0 else 0
            print(f"  [{idx:3d}/{total_shots}] Da render {idx*3} anh | {dt:.1f}s qua | Con lai ~{rem:.1f}s")
            
    dt_total = time.perf_counter() - t_start
    print(f"\n=== HOAN TAT RENDER ANH TINH TAP 11 ===")
    print(f"Tong thoi gian: {dt_total:.2f} giay ({dt_total/60:.2f} phut)")
    print(f"So anh da xuat: VI={rendered_counts['vi']}, EN={rendered_counts['en']}, JA={rendered_counts['ja']} (Tong: {sum(rendered_counts.values())})")

if __name__ == "__main__":
    main()
