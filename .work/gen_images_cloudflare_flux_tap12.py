#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 16:9 backgrounds for Episode 12 using Cloudflare Workers AI FLUX.1.
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

from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL, STYLE_PREFIX, STYLE_SUFFIX

OUT = ROOT / "assets" / "bg"
PROV_FILE = ROOT / "provenance.json"
JOBS_FILE = WORK / "bg_jobs_tap12.json"

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
            "ghi_chu": "Sinh nền bằng Cloudflare FLUX.1 schnell, crop 16:9 và resize 2112x1188"
        }
        if fpath in by_file:
            prov[by_file[fpath]] = entry
            updated += 1
        else:
            prov.append(entry)
            by_file[fpath] = len(prov) - 1
            added += 1
            
    PROV_FILE.write_text(json.dumps(prov, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Cap nhat provenance.json: {updated} ghi de, {added} them moi")

def main():
    t_start = time.perf_counter()
    account_id, api_token = get_credentials()
    if not account_id or not api_token:
        print("LOI: Chua co thong tin Cloudflare API trong .work/.flux_key hoac .work/.cloudflare_key!")
        sys.exit(1)
        
    print("=== SINH ANH NEN TAP 12 VOI CLOUDFLARE FLUX.1 ===")
    print(f"Account ID: {account_id[:6]}... | API Token: {api_token[:6]}...")
    print(f"Model: {DEFAULT_MODEL}")
    
    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    total = len(jobs)
    print(f"Tong so anh: {total} anh\n")
    
    OUT.mkdir(parents=True, exist_ok=True)
    prov_records = []
    
    for i, job in enumerate(jobs, 1):
        name = job["name"]
        target_path = OUT / f"{name}.png"
        prompt = job["prompt"]
        
        t0 = time.perf_counter()
        im = generate_16_9_background(prompt, steps=4, out_size=(2112, 1188))
        im.save(target_path, "PNG")
        
        dt_shot = time.perf_counter() - t0
        dt_total = time.perf_counter() - t_start
        rem = (total - i) * (dt_total / i)
        print(f"[{i:2d}/{total}] {name} ({dt_shot:.1f}s) | Da qua: {dt_total/60:.1f}m | Con lai: ~{rem/60:.1f}m")
        
        prov_records.append({
            "file": f"assets/bg/{name}.png",
            "prompt": STYLE_PREFIX + prompt + STYLE_SUFFIX
        })
        
    update_provenance(prov_records)
    total_time = time.perf_counter() - t_start
    print(f"\n=== HOAN TAT SINH 83 ANH NEN ===")
    print(f"Tong thoi gian: {total_time:.1f}s ({total_time/60:.2f}m) | TB: {total_time/total:.2f}s/anh")

if __name__ == "__main__":
    main()
