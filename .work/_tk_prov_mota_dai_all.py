#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat/them dong provenance cho 4 ban mo ta dai (TK1-TK4)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
PROV = ROOT / "provenance.json"
LINK = "youtu.be/lDVXjeFLn48"

NOI_DUNG = {
    "TK1": ("hook 'Co ay buoc vao phong tham van' + giai thich chi dau #2 "
            "(thu doan vs chu ky tam ly) + boi canh ho so + 10 chi dau + 9 nguon + lưu y + hotline"),
    "TK2": ("hook 'Vi sao co ay khong bao gio chay tron' + giai thich chi dau #6 "
            "(bat luc tap nhiem - gham ket chan thuong) + boi canh ho so + 10 chi dau + 10 nguon + lưu y + hotline"),
    "TK3": ("hook 'Ba ta khong can tien. Ba ta can su kinh nghung' + giai thich chi dau #3 "
            "(su cung cap ai ky) va #9 (diem mu xa hoi) + boi canh ho so + 10 chi dau + 9 nguon + lưu y + hotline"),
    "TK4": ("hook '4 dau hieu do sinh ton' + 4 canh bao do (benh su mau thuan xet nghiem · "
            "trieu chung chi xuat hien khi co nguoi cham soc · doi bac si + nghien su chu y · "
            "co lap tuyet doi) + boi canh ho so + 10 chi dau + 9 nguon + lưu y + hotline"),
}

data = json.loads(PROV.read_text(encoding="utf-8"))
by_file = {e.get("file"): e for e in data}
added = 0
for cid, mota in NOI_DUNG.items():
    f = "02_SAN_XUAT/TIKTOK/Tap01/MoTa_Dai_%s.txt" % cid
    p = D / ("MoTa_Dai_%s.txt" % cid)
    n = len(p.read_text(encoding="utf-8").strip())
    if f in by_file:
        e = by_file[f]
    else:
        e = {"file": f}
        data.append(e)
        added += 1
    e["loai"] = "mo ta DAI cho truong Description cua TikTok Studio (4.000 ky tu)"
    e["cong_cu"] = "viet tay theo mo ta tap 01 + mau KE_HOACH_CLIP_TAP01.md muc 8 + SPEC_AUDIO_CLIP_TAP01.json"
    e["ngay"] = "2026-11-19"
    e["prompt"] = None
    e["seed"] = None
    e["mo_ta"] = ("ban mo ta %d ky tu cho clip %s: %s; link YouTube Tap 01 %s"
                  % (n, cid, mota, LINK))
    e["font"] = None
    e["dieu_khoan"] = ("TikTok chi hien ~100 ky tu dau truoc khi bam 'more' => phan hook phai o dau; "
                       "khong dung tu cam V9/A9.2 (da quet tu dong); link YouTube trong caption khong click duoc.")
    e["kiem_tra_thuong_mai"] = ("dat (%d ky tu < 4.000; 0 tu cam V9/A9.2; du lieu truy ve "
                                "01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md + "
                                "02_SAN_XUAT/Tap01/nguon_tham_khao.md + mo ta tap 01)" % n)
PROV.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("  provenance: %d dong (%d dong moi)" % (len(data), added))
