#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh ảnh nền Tập 37, 38, 39 bằng Cloudflare Workers AI FLUX.1 (schnell).

Cùng chuẩn với gen_images_cloudflare_flux_tapXX.py:
  - 4 tầng prompt Deep Noir (H21): Style Prefix + Bối cảnh + Mood + Negative
  - 16:9 2K chuẩn 2112x1188, crop + Lanczos, dìm bão hoà -35%, tương phản +15%,
    vignette 4 góc, hạt phim 35mm (post_process_noir)
  - Auto-failover nhiều tài khoản Cloudflare khi hết quota (HTTP 429)
  - Lưu đúng tên job vào assets/bg/<name>.png => tự khớp shot (H25/H28)

Khác biệt so với script cũ (an toàn khi nhiều phiên chạy song song):
  - provenance.json ghi 1 lần / tập, dùng ghi file tạm + os.replace (atomic)
  - Không ghi provenance mỗi 10 ảnh (tránh đụng file 5 MB nhiều lần)

Usage:  py -3 .work/gen_images_cf_tap3739.py 37 38 39
"""
import os
import sys
import time
import json
import tempfile
from pathlib import Path
from datetime import date

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))

import flux_client
from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL

OUT = ROOT / "assets" / "bg"
PROV_FILE = ROOT / "provenance.json"


def pin_accounts(slot_spec):
    """Giới hạn pool Cloudflare theo slot để chạy nhiều tiến trình song song.

    AE_CF_SLOT="1,2" -> pool chỉ còn account ở vị trí 1 rồi 2 (theo thứ tự),
    và bắt đầu thử account đầu tiên. Nếu account đó hết quota (429) sẽ tự
    nhảy sang account kế tiếp trong danh sách rút gọn.
    """
    if not slot_spec:
        return
    import flux_client as fc
    full = fc.get_account_pool()
    idx = [int(x) for x in slot_spec.split(",") if x.strip().isdigit()]
    picked = [full[i] for i in idx if 0 <= i < len(full)]
    if not picked:
        print(f"CẢNH BÁO: AE_CF_SLOT={slot_spec} không hợp lệ, dùng toàn bộ pool.")
        return
    fc.get_account_pool = lambda: picked
    fc._ACTIVE_ACCOUNT_INDEX = 0
    print(f"Pool giới hạn: {len(picked)} account (slot {slot_spec}).")


def update_provenance(records, ep):
    """Ghi shard provenance theo tập (mỗi tiến trình 1 file) để không đụng nhau.

    Vì 3 tập chạy song song, mỗi tiến trình ghi .work/_prov_shard_tXX.json;
    sau đó gộp tất cả shard vào provenance.json bằng merge_prov_shards.py.
    """
    shard = WORK / f"_prov_shard_t{ep}.json"
    existing = []
    if shard.exists():
        existing = json.loads(shard.read_text(encoding="utf-8"))
    by_file = {r["file"]: i for i, r in enumerate(existing)}
    today = str(date.today())
    added, updated = 0, 0

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
            existing[by_file[fpath]] = entry
            updated += 1
        else:
            existing.append(entry)
            by_file[fpath] = len(existing) - 1
            added += 1

    fd, tmp = tempfile.mkstemp(dir=str(WORK), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)
        os.replace(tmp, shard)
    except Exception:
        if os.path.exists(tmp):
            os.remove(tmp)
        raise
    print(f"-> shard {shard.name}: +{added} mới, ~{updated} cập nhật.")


def image_ok(path):
    """Ảnh hợp lệ = có file, >100 KB và PIL mở được (bắt file PNG bị cắt cụt)."""
    try:
        if not path.exists() or path.stat().st_size <= 100_000:
            return False
        from PIL import Image
        with Image.open(path) as im:
            im.verify()
        return True
    except Exception:
        return False


def run_episode(ep):
    jobs_file = WORK / f"bg_jobs_tap{ep}.json"
    if not jobs_file.exists():
        print(f"BỎ QUA Tập {ep}: không tìm thấy {jobs_file}")
        return True

    jobs = json.loads(jobs_file.read_text(encoding="utf-8"))
    total = len(jobs)
    print("=" * 60)
    print(f"BẮT ĐẦU TẬP {ep}: {total} ảnh (2112x1188, Deep Noir H21)")
    print("=" * 60, flush=True)

    ok_count, fail_count = 0, 0
    records = []
    t_ep = time.perf_counter()

    for idx, item in enumerate(jobs, 1):
        name = item["name"]
        prompt_core = item["prompt"]
        target_path = OUT / f"{name}.png"
        rel_path = f"assets/bg/{name}.png"

        if image_ok(target_path):
            print(f"[{idx:03d}/{total}] ĐÃ CÓ: {name}.png, bỏ qua.")
            records.append({"file": rel_path, "prompt": prompt_core})
            ok_count += 1
            continue
        if target_path.exists():
            print(f"[{idx:03d}/{total}] {name} ... file hỏng, sinh lại.", end="", flush=True)

        print(f"[{idx:03d}/{total}] {name} ... ", end="", flush=True)
        t0 = time.perf_counter()
        try:
            img_out = generate_16_9_background(
                prompt=prompt_core,
                steps=4,
                out_size=(2112, 1188),
                with_noir_style=True,
            )
            if img_out:
                # compress_level=3 + optimize=False: PNG vẫn lossless, nhưng nén nhanh
                # ~8 lần (optimize=True tốn 15-20 s/ảnh, làm batch 445 ảnh chậm).
                img_out.save(target_path, "PNG", optimize=False, compress_level=3)
                print(f"XONG ({target_path.stat().st_size // 1024} KB, "
                      f"gen {time.perf_counter() - t0:.1f}s)")
                records.append({"file": rel_path, "prompt": prompt_core})
                ok_count += 1
            else:
                print("THẤT BẠI (không nhận được ảnh)")
                fail_count += 1
        except Exception as e:
            print(f"LỖI: {e}")
            fail_count += 1
            msg = str(e).lower()
            if "hết hạn mức" in msg or "429" in str(e) or "quota" in msg:
                print("DỪNG: pool Cloudflare đã hết hạn mức.")
                if records:
                    update_provenance(records, ep)
                return False

        time.sleep(0.5)

    if records:
        update_provenance(records, ep)

    print(f"XONG TẬP {ep}: {ok_count}/{total} thành công, {fail_count} lỗi "
          f"({(time.perf_counter() - t_ep) / 60:.1f} phút)")
    return True


def main():
    pin_accounts(os.environ.get("AE_CF_SLOT", "").strip())
    account_id, api_token = get_credentials()
    if not account_id or not api_token:
        print("LỖI: chưa có Cloudflare credentials!")
        sys.exit(1)

    OUT.mkdir(parents=True, exist_ok=True)
    eps = sys.argv[1:] or ["37", "38", "39"]
    t_start = time.perf_counter()

    for ep in eps:
        if not run_episode(ep):
            print(f"\nDừng tại Tập {ep} (hết quota pool hoặc lỗi).")
            break

    print("=" * 60)
    print(f"TỔNG THỜI GIAN: {(time.perf_counter() - t_start) / 60:.1f} phút")
    print("=" * 60)


if __name__ == "__main__":
    main()
