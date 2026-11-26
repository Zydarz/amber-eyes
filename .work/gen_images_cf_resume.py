#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resume sinh ảnh nền Tập 37/38/39 bằng Cloudflare FLUX (chỉ Cloudflare, không Kaggle).

Làm 2 việc:
  (1) ẢNH THIẾU  — job chưa có file hợp lệ trong assets/bg  -> sinh mới.
  (2) ẢNH LỖI   — danh sách trong .work/_qc_flags_t37_39.json (AI vẽ chữ / lệch nghĩa)
                  -> XOÁ file cũ rồi sinh lại CÙNG TÊN, với negative siết thêm.

Dùng: py -3 .work/gen_images_cf_resume.py 37 38 39
Biến môi trường: AE_CF_SLOT="1,2" (giới hạn account), AE_CF_ROUNDS=2 (số lần thử lại)
"""
import os
import sys
import json
import time
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))

import flux_client
from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL

OUT = ROOT / "assets" / "bg"
FLAGS_FILE = WORK / "_qc_flags_t37_39.json"


def pin_accounts(slot_spec):
    if not slot_spec:
        return
    full = flux_client.get_account_pool()
    idx = [int(x) for x in slot_spec.split(",") if x.strip().isdigit()]
    picked = [full[i] for i in idx if 0 <= i < len(full)]
    if not picked:
        print(f"CẢNH BÁO: AE_CF_SLOT={slot_spec} không hợp lệ.")
        return
    flux_client.get_account_pool = lambda: picked
    flux_client._ACTIVE_ACCOUNT_INDEX = 0
    print(f"Pool giới hạn: {len(picked)} account (slot {slot_spec}).")


def image_ok(path):
    try:
        if not path.exists() or path.stat().st_size <= 100_000:
            return False
        from PIL import Image
        with Image.open(path) as im:
            im.verify()
        return True
    except Exception:
        return False


def load_flags():
    if not FLAGS_FILE.exists():
        return {}, ""
    data = json.loads(FLAGS_FILE.read_text(encoding="utf-8"))
    extra = data.get("extra_negative", "")
    by_ep = {}
    for f in data.get("flags", []):
        by_ep.setdefault(int(f["ep"]), {})[f["name"]] = f.get("reason", "")
    return by_ep, extra


def update_shard(ep, records):
    shard = WORK / f"_prov_shard_t{ep}.json"
    entries = json.loads(shard.read_text(encoding="utf-8")) if shard.exists() else []
    by_file = {r["file"]: i for i, r in enumerate(entries)}
    today = str(date.today())
    added = updated = 0
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
            "ghi_chu": "Sinh nền bằng Cloudflare FLUX.1 schnell, chuẩn Deep Noir H21/H25/H26, crop 16:9 và resize 2112x1188",
        }
        if fpath in by_file:
            entries[by_file[fpath]] = entry
            updated += 1
        else:
            entries.append(entry)
            by_file[fpath] = len(entries) - 1
            added += 1
    shard.write_text(json.dumps(entries, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  shard t{ep}: +{added} mới, ~{updated} cập nhật")


def run_episode(ep, flags_by_ep, extra_negative):
    jobs_file = WORK / f"bg_jobs_tap{ep}.json"
    if not jobs_file.exists():
        print(f"BỎ QUA tập {ep}: không có {jobs_file}")
        return True
    jobs = json.loads(jobs_file.read_text(encoding="utf-8"))
    bad = flags_by_ep.get(ep, {})

    todo = []
    for j in jobs:
        p = OUT / f"{j['name']}.png"
        if j["name"] in bad:
            todo.append((j, True))
        elif not image_ok(p):
            todo.append((j, False))

    n_bad = sum(1 for _, b in todo if b)
    n_miss = len(todo) - n_bad
    print("=" * 60)
    print(f"TẬP {ep}: cần sinh {len(todo)} ảnh ({n_miss} thiếu + {n_bad} lỗi QC)")
    print("=" * 60, flush=True)

    if not todo:
        return True

    ok = fail = 0
    records = []
    for idx, (j, is_bad) in enumerate(todo, 1):
        name = j["name"]
        prompt = j["prompt"].strip()
        if is_bad:
            prompt = f"{prompt}, {extra_negative}"
        target = OUT / f"{name}.png"
        rel = f"assets/bg/{name}.png"

        print(f"[{idx:03d}/{len(todo)}] {'SINH LAI' if is_bad else 'THIEU   '} {name} ... ", end="", flush=True)
        t0 = time.perf_counter()
        try:
            img = generate_16_9_background(prompt=prompt, steps=4, out_size=(2112, 1188), with_noir_style=True)
            if img:
                img.save(target, "PNG", optimize=False, compress_level=3)
                print(f"XONG ({target.stat().st_size // 1024} KB, gen {time.perf_counter() - t0:.1f}s)")
                records.append({"file": rel, "prompt": prompt})
                ok += 1
            else:
                print("THAT BAI")
                fail += 1
        except Exception as e:
            print(f"LOI: {e}")
            fail += 1
            if "hết hạn mức" in str(e).lower() or "429" in str(e) or "quota" in str(e).lower():
                print("DUNG: het quota pool Cloudflare.")
                if records:
                    update_shard(ep, records)
                return False
        time.sleep(0.4)

    if records:
        update_shard(ep, records)
    print(f"TẬP {ep}: {ok}/{len(todo)} thành công, {fail} lỗi")
    return True


def main():
    pin_accounts(os.environ.get("AE_CF_SLOT", "").strip())
    account_id, api_token = get_credentials()
    if not account_id or not api_token:
        print("LOI: chua co Cloudflare credentials!")
        sys.exit(1)
    OUT.mkdir(parents=True, exist_ok=True)

    flags_by_ep, extra_negative = load_flags()
    eps = [int(x) for x in sys.argv[1:]] or [37, 38, 39]
    t0 = time.perf_counter()
    for ep in eps:
        if not run_episode(ep, flags_by_ep, extra_negative):
            print(f"\nDung tai tap {ep} (het quota).")
            break
    print(f"\nTONG THOI GIAN: {(time.perf_counter() - t0) / 60:.1f} phut")


if __name__ == "__main__":
    main()
