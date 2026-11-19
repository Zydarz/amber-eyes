#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them dong provenance cho clip TikTok TK1 (mp4) + BGM + SFX + caption,
doc ket qua QC that (khong ghi 'dat' chung chung)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
PROV = ROOT / "provenance.json"
HERE = ROOT / ".work"
CLIP = "02_SAN_XUAT/TIKTOK/Tap01/clip01_TK1.mp4"
CAPTION = "02_SAN_XUAT/TIKTOK/Tap01/Caption_TK1.txt"

qc = json.loads((HERE / "_qc_tk01_clip.json").read_text(encoding="utf-8"))
ln = json.loads((HERE / "_tk1_loudnorm.json").read_text(encoding="utf-8"))

loi = qc.get("loi", [])
n_dat = 14 - len(loi)
trang_thai = ("DAT 14/14 cong" if not loi
              else "TRUOT %d/14: %s" % (len(loi), "; ".join(loi)[:300]))
khoi_kt = qc.get("khoang_cam", {}).get("so", 0)
lo = qc.get("loudness", {}).get("I_lufs")
tp = qc.get("loudness", {}).get("true_peak_dbfs")
mb = qc.get("dung_luong_mb", 0)

res = []
res.append({
    "file": CLIP,
    "loai": "clip TikTok 9:16 (1080x1920, 30 fps, H.264 + AAC) - clip 1/4 Tap 01",
    "cong_cu": ("Pillow 12.2 (nen + chu, H6/H9) + FFmpeg 9.0 libopenh264; "
                "ngoai chuyen dong pull/push/pan/still theo SPEC_AUDIO_CLIP_TAP01.json; "
                "am thanh: master giong + BGM MiniMax co ducking + SFX tu tong hop"),
    "ngay": "2026-11-18",
    "prompt": ("nen doc 9:16 tai san xuat tai 02_SAN_XUAT/TIKTOK/Tap01/ "
               "assets/bg/tk01_<nen>.png; chu ve bang Pillow (khong de AI ve chu)"),
    "seed": None,
    "mo_ta": ("TK1 'Co ay buoc vao phong tham van bang doi chan cua chinh minh' - "
              "12 cau, %0.2f s, chu hook 0-3 s, the overlay tai TK1.01#6, "
              "phu de burn-in 52 px (chunk theo cau, nguyen van loi doc)"
              % qc.get("do_dai_s", 0)),
    "font": "Segoe UI Semibold (phu de 52 px) · Segoe UI Bold (hook 76 px, the 44 px)",
    "dieu_khoan": ("BGM chi dung 'assets/bgm/bgm_sub_drone.mp3' (MiniMax Music - duoc phep TikTok); "
                   "SFX tu tong hop; KHONG dung 2 BGM + 211 SFX cua YouTube Audio Library "
                   "(khong co license TikTok). Caption kem dong AIGC bat buoc. "
                   "L10: file media - KHONG commit."),
    "kiem_tra_thuong_mai": ("%s; I=%s LUFS, TP=%s dBFS, %s MB, khoang cam %d. Chi tiet: "
                            "02_SAN_XUAT/TIKTOK/Tap01/BaoCao_QC_TikTok_TK1_20261118.md"
                            % (trang_thai, lo, tp, mb, khoi_kt)),
})
res.append({
    "file": CAPTION,
    "loai": "caption + hashtag + ghi chu danh TikTok cho clip TK1",
    "cong_cu": "viet tay theo KE_HOACH_CLIP_TAP01.md muc 8",
    "ngay": "2026-11-18",
    "prompt": None,
    "seed": None,
    "mo_ta": ("caption 364 ky tu; bat buoc kem toggle 'AI-generated content' + "
              "dong 'Noi dung do AI tao hinh va giong, dung de phan tich tam ly - "
              "khong phai phong su.'"),
    "font": None,
    "dieu_khoan": "TikTok bat buoc nhan AIGC; gioi han 2.200 ky tu - caption hien 364 ky tu.",
    "kiem_tra_thuong_mai": "dat (khop mau trong KE_HOACH_CLIP_TAP01.md §8 TK1)",
})


def main():
    data = json.loads(PROV.read_text(encoding="utf-8"))
    existing = {e.get("file") for e in data}
    n0 = len(data)
    for e in res:
        if e["file"] in existing:
            print("  da co -> bo qua: %s" % e["file"])
            continue
        data.append(e)
    PROV.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("  provenance: %d -> %d dong" % (n0, len(data)))


if __name__ == "__main__":
    main()
