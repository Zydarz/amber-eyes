#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 155 backgrounds for Episode 23 using Cloudflare Workers AI FLUX.1.
Model: @cf/black-forest-labs/flux-1-schnell
Adheres to:
  - 4-Tier Deep Noir Prompt Architecture
  - Lanczos 2K Resampling (2112x1188)
  - Color Grading: Mute Saturation (-35%) & Boost Contrast (+15%)
  - Post-processing: 4-Corner Vignette (-45%) + 35mm Film Grain
  - Multi-Account Auto-Failover
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
JOBS_FILE = WORK / "bg_jobs_tap24.json"

def update_provenance(records):
    prov = json.loads(PROV_FILE.read_text(encoding="utf-8"))
    by_file = {r["file"]: i for i, r in enumerate(prov)}
    
    added, updated = 0, 0
    today = str(date.today())
    
    for rec in records:
        fpath = rec["file"]
        entry = {
            "file": fpath,
            "loai": "nền 16:9 dùng chung 4 ngôn ngữ",
            "cong_cu": f"Cloudflare Workers AI ({DEFAULT_MODEL})",
            "ngay": today,
            "prompt": rec["prompt"],
            "seed": None,
            "nguon_anh_tham_chieu": None,
            "kich_thuoc_goc": [2112, 1188],
            "dieu_khoan": "Cloudflare Workers AI Terms of Service",
            "kiem_tra_thuong_mai": "đạt",
            "ghi_chu": "Sinh nền bằng Cloudflare FLUX.1 schnell, chuẩn Deep Noir H21/H25, crop 16:9 và resize 2112x1188"
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
        
    print("==================================================================")
    print("Bắt đầu pipeline sinh 155 ảnh Tập 23 qua Cloudflare Workers AI FLUX")
    print("==================================================================")
    
    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    total = len(jobs)
    print(f"Tổng số ảnh cần sinh: {total} ảnh mới (2112x1188 chuẩn 2K Deep Noir)")
    
    records = []
    success_cnt = 0
    skip_cnt = 0
    fail_cnt = 0
    
    for idx, item in enumerate(jobs, 1):
        name = item["name"]
        prompt_core = item["prompt"]
        target_path = OUT / f"{name}.png"
        rel_path = f"assets/bg/{name}.png"
        
        if target_path.exists() and target_path.stat().st_size > 100_000:
            print(f"[{idx:03d}/{total}] ĐÃ CÓ: {name}.png ({target_path.stat().st_size // 1024} KB), bỏ qua.")
            records.append({"file": rel_path, "prompt": prompt_core})
            skip_cnt += 1
            continue
            
        print(f"[{idx:03d}/{total}] Đang sinh {name}...", end=" ", flush=True)
        t0 = time.perf_counter()
        try:
            img_out = generate_16_9_background(
                prompt=prompt_core,
                steps=4,
                out_size=(2112, 1188),
                with_noir_style=True
            )
            if img_out:
                img_out.save(target_path, "PNG", optimize=True)
                elapsed = time.perf_counter() - t0
                print(f"XONG ({target_path.stat().st_size // 1024} KB, {elapsed:.1f}s)")
                records.append({"file": rel_path, "prompt": prompt_core})
                success_cnt += 1
                
                # Cập nhật provenance theo từng mẻ 10 ảnh
                if len(records) % 10 == 0:
                    update_provenance(records)
            else:
                print("LỖI: Không nhận được ảnh từ Cloudflare")
                fail_cnt += 1
        except Exception as e:
            print(f"THẤT BẠI: {e}")
            fail_cnt += 1
            if "hết hạn mức" in str(e).lower() or "429" in str(e):
                print("DỪNG PIPELINE: Tất cả tài khoản trong pool đã hết hạn mức!")
                break
        
        # Nghỉ nhẹ giữa các request để bảo vệ quota rate limit
        time.sleep(1.0)
        
    if records:
        update_provenance(records)
        
    t_total = time.perf_counter() - t_start
    print("==================================================================")
    print(f"HOÀN THÀNH PIPELINE TẬP 23: {success_cnt} ảnh mới, {skip_cnt} đã có, {fail_cnt} lỗi. Tổng thời gian: {t_total:.1f}s")
    print("==================================================================")

if __name__ == '__main__':
    main()
