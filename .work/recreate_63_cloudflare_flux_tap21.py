#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate all 63 original backgrounds of Episode 21 using Cloudflare Workers AI FLUX.1.
Model: @cf/black-forest-labs/flux-1-schnell
"""
import os
import sys
import json
import time
from pathlib import Path
from datetime import date

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))

from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL

OUT = ROOT / "assets" / "bg"
PROV_FILE = ROOT / "provenance.json"
JOBS_FILE = WORK / "bg_jobs_tap21.json"
NEW_PROMPTS_FILE = WORK / "scratch_recreate_63_prompts.json"

def update_provenance(records):
    prov = json.loads(PROV_FILE.read_text(encoding="utf-8"))
    by_file = {r["file"]: i for i, r in enumerate(prov)}
    
    added, updated = 0, 0
    today = str(date.today())
    
    for rec in records:
        fpath = rec["file"]
        entry = {
            "file": fpath,
            "loai": "nền 16:9 dùng chung 3 ngôn ngữ",
            "cong_cu": f"Cloudflare Workers AI ({DEFAULT_MODEL})",
            "ngay": today,
            "prompt": rec["prompt"],
            "seed": None,
            "nguon_anh_tham_chieu": None,
            "kich_thuoc_goc": [2112, 1188],
            "dieu_khoan": "Cloudflare Workers AI Terms of Service",
            "kiem_tra_thuong_mai": "đạt",
            "ghi_chu": "Tạo lại nền bằng Cloudflare FLUX.1 schnell, chuẩn Deep Noir H21/H25, crop 16:9 và resize 2112x1188"
        }
        if fpath in by_file:
            prov[by_file[fpath]] = entry
            updated += 1
        else:
            prov.append(entry)
            by_file[fpath] = len(prov) - 1
            added += 1
            
    PROV_FILE.write_text(json.dumps(prov, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Cập nhật provenance.json: {updated} ghi đè, {added} thêm mới")

def main():
    t_start = time.perf_counter()
    account_id, api_token = get_credentials()
    if not account_id or not api_token:
        print("LỖI: Chưa có Cloudflare credentials!")
        sys.exit(1)
        
    print(f"Cloudflare Account ID: {account_id[:6]}...{account_id[-4:]}")
    
    with open(NEW_PROMPTS_FILE, "r", encoding="utf-8") as f:
        prompts_63 = json.load(f)
        
    total = len(prompts_63)
    print(f"Tái tạo và ghi đè toàn bộ: {total} ảnh nền cũ của Tập 21 bằng Cloudflare FLUX.1")
    
    records = []
    success_cnt = 0
    fail_cnt = 0
    
    for idx, (name, prompt_core) in enumerate(prompts_63.items(), 1):
        target_path = OUT / f"{name}.png"
        rel_path = f"assets/bg/{name}.png"
        
        print(f"[{idx}/{total}] Đang tạo lại {name}...", end=" ", flush=True)
        try:
            img_out = generate_16_9_background(
                prompt=prompt_core,
                steps=4,
                out_size=(2112, 1188),
                with_noir_style=True
            )
            if img_out:
                img_out.save(target_path, "PNG", optimize=True)
                print(f"XONG ({target_path.stat().st_size // 1024} KB)")
                records.append({"file": rel_path, "prompt": prompt_core})
                success_cnt += 1
            else:
                print("THẤT BẠI (img_out is None)!")
                fail_cnt += 1
        except Exception as e:
            print(f"LỖI: {e}")
            fail_cnt += 1
            
        time.sleep(0.5)
        
    if records:
        update_provenance(records)
        
    # Also update bg_jobs_tap21.json with the upgraded prompts
    with open(JOBS_FILE, "r", encoding="utf-8") as f:
        all_jobs = json.load(f)
        
    for j in all_jobs:
        if j["name"] in prompts_63:
            j["prompt"] = prompts_63[j["name"]]
            
    with open(JOBS_FILE, "w", encoding="utf-8") as f:
        json.dump(all_jobs, f, ensure_ascii=False, indent=2)
    print("Đã cập nhật bg_jobs_tap21.json với các prompt mới nâng cấp.")
        
    elapsed = time.perf_counter() - t_start
    print(f"\n=== HOÀN TẤT TÁI TẠO 63 ẢNH CŨ TẬP 21 ===")
    print(f"Thành công: {success_cnt} | Thất bại: {fail_cnt} | Tổng: {total}")
    print(f"Thời gian thực hiện: {elapsed:.1f} s")

if __name__ == "__main__":
    main()
