#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 135 backgrounds for Episode 26 (Miyuki Ishikawa) using Cloudflare Workers AI FLUX.1.
Model: @cf/black-forest-labs/flux-1-schnell
Adheres to:
  - 4-Tier Deep Noir Prompt Architecture
  - Auto-Failover Multi-Account Pool (.work/.cloudflare_accounts)
  - 16:9 2K Standard (2112x1188)
  - Dark Graphic Novel Noir Aesthetic (H21/H25/H26, no text, no gore, silhouettes)
"""
import sys
import time
import json
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))

from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL

OUT = ROOT / "assets" / "bg"
PROV_FILE = ROOT / "provenance.json"
JOBS_FILE = WORK / "bg_jobs_tap26.json"

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
            "ghi_chu": "Sinh nền bằng Cloudflare FLUX.1 schnell, chuẩn Deep Noir H21/H25/H26, crop 16:9 và resize 2112x1188"
        }
        if fpath in by_file:
            prov[by_file[fpath]] = entry
            updated += 1
        else:
            prov.append(entry)
            by_file[fpath] = len(prov) - 1
            added += 1
            
    PROV_FILE.write_text(json.dumps(prov, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"-> Đã đồng bộ provenance.json: +{added} mới, ~{updated} cập nhật.")

def main():
    t_start = time.perf_counter()
    account_id, api_token = get_credentials()
    if not account_id or not api_token:
        print("LỖI: Chưa có Cloudflare credentials!")
        sys.exit(1)
        
    OUT.mkdir(parents=True, exist_ok=True)
    
    if not JOBS_FILE.exists():
        print(f"LỖI: Không tìm thấy {JOBS_FILE}")
        sys.exit(1)
        
    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    total = len(jobs)
    print(f"Tổng số ảnh cần sinh: {total} ảnh (2112x1188 chuẩn 2K Deep Noir)")
    
    success_count = 0
    records = []
    
    for idx, item in enumerate(jobs, 1):
        name = item["name"]
        prompt_core = item["prompt"]
        target_path = OUT / f"{name}.png"
        rel_path = f"assets/bg/{name}.png"
        
        if target_path.exists() and target_path.stat().st_size > 100_000:
            print(f"[{idx:03d}/{total}] ĐÃ CÓ: {name}.png ({target_path.stat().st_size // 1024} KB), bỏ qua.")
            records.append({"file": rel_path, "prompt": prompt_core})
            success_count += 1
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
                success_count += 1
                
                # Cập nhật provenance mỗi 10 ảnh
                if len(records) % 10 == 0:
                    update_provenance(records)
            else:
                print("THẤT BẠI (Không nhận được ảnh)")
        except Exception as e:
            print(f"LỖI: {e}")
            # Nếu tất cả tài khoản trong pool đều cạn kiệt thì dừng
            if "hết hạn mức" in str(e).lower() or "429" in str(e):
                print("DỪNG PIPELINE: Tất cả tài khoản trong pool đã hết hạn mức!")
                break
                
        # Giữ nhịp nhẹ 1s để ổn định kết nối
        time.sleep(1.0)
        
    if records:
        update_provenance(records)
        
    total_time = time.perf_counter() - t_start
    print(f"\n==========================================")
    print(f"HOÀN TẤT BATCH: {success_count}/{total} ảnh thành công trong {total_time/60:.1f} phút.")
    print(f"==========================================")

if __name__ == '__main__':
    main()
