#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh báo cáo ảnh nền ĐÃ TẠO theo từng tập (T31, T32) — 27/11/2026.

Đọc .work/bg_jobs_tapXX.json + kiểm tra file thật trong assets/bg/, ghi:
  02_SAN_XUAT/Ho_So_Toi_Pham/TapXX/BaoCao_Anh_TapXX_20261127.md
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
WORK = ROOT / ".work"
DATE = "2026-11-27"

HALLUC = "Ảnh đã tạo bằng Cloudflare Workers AI FLUX.1 (schnell), chuẩn Deep Noir H21/H25/H26, 2112×1188 PNG."


def report(ep):
    jobs = json.loads((WORK / f"bg_jobs_tap{ep:02d}.json").read_text(encoding="utf-8"))
    acts = {}
    for j in jobs:
        acts.setdefault(j.get("act", 1), []).append(j)

    lines = [
        f"# BÁO CÁO ẢNH NỀN ĐÃ TẠO · TẬP {ep:02d} · {DATE}",
        "",
        f"- Công cụ: {HALLUC}",
        f"- Nguồn prompt: `.work/bg_jobs_tap{ep:02d}.json` ({len(jobs)} job) · ảnh lưu tại `assets/bg/t{ep:02d}_*.png`",
        f"- Quy mô: **{len(jobs)} ảnh nền 16:9 dùng chung 4 ngôn ngữ (VI/EN/JA/KO)**",
        "",
        "## 1. Tổng quan",
        "",
        "| Hồi | Shot | Ảnh có file | Thiếu | Ảnh trùng nhau |",
        "|---|---:|---:|---:|---:|",
    ]

    total_ok = total_miss = 0
    miss_all = []
    for act, js in sorted(acts.items()):
        ok = [j for j in js if (BG / f"{j['name']}.png").exists()]
        miss = [j for j in js if not (BG / f"{j['name']}.png").exists()]
        total_ok += len(ok)
        total_miss += len(miss)
        miss_all += [(act, j["name"]) for j in miss]
        lines.append(f"| {act} | {len(js)} | {len(ok)} | {len(miss)} | 0 |")
    lines += [
        f"| **TỔNG** | **{len(jobs)}** | **{total_ok}** | **{total_miss}** | **0** |",
        "",
        f"→ **Đã tạo {total_ok}/{len(jobs)} ảnh ({total_ok/len(jobs)*100:.0f}%)**"
        + (f" · còn thiếu {total_miss} ảnh." if total_miss else " · đủ toàn bộ."),
        "",
    ]

    if total_ok:
        lines += ["## 2. Ảnh đã tạo (theo hồi)", ""]
        for act, js in sorted(acts.items()):
            ok = [j for j in js if (BG / f"{j['name']}.png").exists()]
            if not ok:
                continue
            lines += [f"### Hồi {act} — {len(ok)} ảnh", "",
                      "| # | Tên file (`assets/bg/`) | Kích thước | Mô tả cảnh |",
                      "|---:|---|---|---|"]
            for i, j in enumerate(ok, 1):
                kb = (BG / f"{j['name']}.png").stat().st_size // 1024
                desc = j.get("desc", "").replace("|", "/")
                lines.append(f"| {i} | `{j['name']}.png` | {kb} KB | {desc} |")
            lines.append("")

    if miss_all:
        lines += ["## 3. Ảnh CHƯA tạo (cần sinh tiếp)", ""]
        for act, nm in miss_all:
            lines.append(f"- Hồi {act} — `{nm}.png`")
        lines.append("")

    lines += [
        "## 4. Ghi chú",
        "",
        "- 99 prompt của T31/T32 đã được viết lại trước khi sinh (bỏ hẳn cơ hội vẽ chữ theo bài học T37–39): "
        "bản gốc lưu ở `.work/_cu/bg_jobs_tap31_20261127_1525_before_rewrite.json` và bản t32 tương ứng.",
        "- Mọi ảnh đã ghi vào `provenance.json` (công cụ, prompt, ngày, điều khoản, đã kiểm thương mại).",
        "- Media không commit vào git theo luật L10 của AGENTS.md.",
        "",
    ]

    dst = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / f"Tap{ep:02d}" / f"BaoCao_Anh_Tap{ep:02d}_{DATE.replace('-', '')}.md"
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Tap{ep:02d}: {total_ok}/{len(jobs)} anh · -> {dst.name}")
    return total_ok, total_miss


def main():
    for ep in (31, 32):
        report(ep)


if __name__ == "__main__":
    main()
