#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh lai 66 anh nen Tap 11 bang Cloudflare FLUX.1 schnell.
Dung bg_jobs_tap11_v2.json (66 anh dang dung, bo 4 anh du).
Chi sinh anh nen (assets/bg/t11_*.png), KHONG render stills.
Chay: py -3 .work/gen_bg_tap11_v2.py
"""
import os, sys, json, time
from pathlib import Path
from datetime import date

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))

from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL, STYLE_PREFIX, STYLE_SUFFIX

OUT = ROOT / "assets" / "bg"
PROV_FILE = ROOT / "provenance.json"
JOBS_FILE = WORK / "bg_jobs_tap11_v2.json"

def update_provenance(records):
    prov = json.loads(PROV_FILE.read_text(encoding="utf-8"))
    by_file = {r["file"]: i for i, r in enumerate(prov)}
    added, updated = 0, 0
    today = str(date.today())
    for rec in records:
        fpath = rec["file"]
        entry = {
            "file": fpath,
            "loai": "nen 16:9 dung chung 3 ngon ngu",
            "cong_cu": f"Cloudflare Workers AI ({DEFAULT_MODEL})",
            "ngay": today,
            "prompt": rec["prompt"],
            "seed": None,
            "nguon_anh_tham_chieu": None,
            "kich_thuoc_goc": [2112, 1188],
            "dieu_khoan": "Cloudflare Workers AI Terms of Service",
            "kiem_tra_thuong_mai": "dat",
            "ghi_chu": "Sinh lai nen Tap11 v2 bang Cloudflare FLUX.1 schnell, 13/11/2026"
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

    print("=== SINH LAI 66 ANH NEN TAP 11 VOI CLOUDFLARE FLUX.1 (v2) ===")
    print(f"Account ID: {account_id[:6]}... | API Token: {api_token[:6]}...")
    print(f"Model: {DEFAULT_MODEL}")
    print(f"Output: {OUT}")
    print(f"Jobs file: {JOBS_FILE.name}\n")

    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    total = len(jobs)
    print(f"Tong so anh can sinh: {total} anh\n")

    OUT.mkdir(parents=True, exist_ok=True)
    prov_records = []
    errors = []

    for i, job in enumerate(jobs, 1):
        name = job["name"]
        target_path = OUT / f"{name}.png"
        prompt = job["prompt"]

        t0 = time.perf_counter()
        try:
            im = generate_16_9_background(prompt, steps=4, out_size=(2112, 1188))
            im.save(target_path, "PNG")
            dt_shot = time.perf_counter() - t0
            dt_total = time.perf_counter() - t_start
            rem = (total - i) * (dt_total / i)
            print(f"[{i:2d}/{total}] OK  {name} ({dt_shot:.1f}s) | Da qua: {dt_total/60:.1f}m | Con lai: ~{rem/60:.1f}m")
            prov_records.append({
                "file": f"assets/bg/{name}.png",
                "prompt": STYLE_PREFIX + prompt + STYLE_SUFFIX
            })
        except Exception as ex:
            dt_shot = time.perf_counter() - t0
            print(f"[{i:2d}/{total}] LOI {name}: {ex} ({dt_shot:.1f}s)")
            errors.append(name)

    if prov_records:
        update_provenance(prov_records)

    total_time = time.perf_counter() - t_start
    ok_count = total - len(errors)
    print(f"\n=== HOAN TAT SINH {total} ANH NEN TAP 11 ===")
    print(f"Thanh cong: {ok_count}/{total} | That bai: {len(errors)}")
    if errors:
        print(f"Danh sach loi: {errors}")
    print(f"Tong thoi gian: {total_time:.1f}s ({total_time/60:.2f}m) | TB: {total_time/ok_count:.2f}s/anh" if ok_count else "")

if __name__ == "__main__":
    main()
