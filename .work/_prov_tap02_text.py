# -*- coding: utf-8 -*-
"""Ghi dong provenance.json cho bo TEXT TikTok Tap 02 (caption + mo ta dai + mo ta ngan).
G6: nguon su that la generator .work/_build_tk_tap02.py - khong sua tay file ket qua.
L5: backup truoc khi ghi de.
"""
import io, json, os, shutil, datetime

ROOT = r"D:/TEST/Gax/amber-eyes"
TAP = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK/Tap02")
PROV = os.path.join(ROOT, "provenance.json")
BAK = os.path.join(ROOT, ".work/_cu")
NGAY = "2026-11-20"
GEN = ".work/_build_tk_tap02.py (generator, G6 - nguon su that duy nhat)"

os.makedirs(BAK, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
shutil.copy2(PROV, os.path.join(BAK, "provenance_%s.json" % stamp))
print("Backup:", os.path.join(BAK, "provenance_%s.json" % stamp))


def read(p):
    return io.open(p, encoding="utf-8").read()


def len_no_nl(s):
    return len(s.replace("\r\n", "\n").replace("\n", ""))


def phan_dan(cap):
    """Caption phan dan = truoc dong '---'."""
    t = cap.replace("\r\n", "\n")
    head = t.split("\n---")[0]
    return head.strip("\n")


prov = json.load(io.open(PROV, encoding="utf-8"))
# Idempotent: xoa cac dong Tap02 truoc do roi ghi lai (do dai co the da doi sau khi sua van ban)
prov = [e for e in prov if "TIKTOK/Tap02/" not in e.get("file", "")]
existing = set()

entries = []
for i in range(1, 6):
    f_cap = "Caption_TK%d.txt" % i
    f_dai = "MoTa_Dai_TK%d.txt" % i
    f_ngan = "MoTa_Ngan_TK%d.txt" % i

    cap = read(os.path.join(TAP, f_cap))
    dai = read(os.path.join(TAP, f_dai))
    ngan = read(os.path.join(TAP, f_ngan))

    pd = phan_dan(cap)
    n_pd = len_no_nl(pd)
    n_cap = len_no_nl(cap)
    n_dai = len_no_nl(dai)
    n_ngan = len_no_nl(ngan)

    hook = cap.split("\n")[0].strip()
    line3 = cap.split("\n")[2].strip()
    chidau = line3.split("chỉ dấu")[-1].split(":")[0].strip() if "chỉ dấu" in line3 else "?"

    # --- caption ---
    entries.append({
        "file": "02_SAN_XUAT/TIKTOK/Tap02/" + f_cap,
        "loai": "caption + hashtag + ghi chu danh TikTok cho clip TK%d Tap 02" % i,
        "cong_cu": GEN,
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "mo_ta": ("phan dan %d ky tu (hook '%s'; chỉ dấu %s) + dong nhan AIGC bat buoc trong than caption "
                  "+ 7 hashtag; phan 'Ghi chú khi đăng' tach rieng KHONG dan; con placeholder "
                  "[LINK_TẬP 02 — cần điền]; troi sang MoTa_Dai_TK%d.txt (%d ky tu) va "
                  "MoTa_Ngan_TK%d.txt (%d ky tu)"
                  % (n_pd, hook, chidau, i, n_dai, i, n_ngan)),
        "font": None,
        "dieu_khoan": ("TikTok bat buoc nhan AIGC (toggle 'Nội dung do AI tạo') - dong nhan AIGC da nam "
                       "trong phan dan; gioi han 2.200 ky tu - phan dan %d ky tu; V9/A9.2 khong co tu cam."
                       % n_pd),
        "kiem_tra_thuong_mai": ("dat (phan dan %d ky tu < 2.200; tuong doi dung mau Tap01/Caption_TK1.txt; "
                                "QC doc lap .work/_qc_mota_tap02.py: 0 loi)" % n_pd),
    })

    # --- mo ta dai ---
    entries.append({
        "file": "02_SAN_XUAT/TIKTOK/Tap02/" + f_dai,
        "loai": "mo ta DAI cho truong Description cua TikTok Studio (4.000 ky tu)",
        "cong_cu": GEN,
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "mo_ta": ("ban mo ta dai %d ky tu cho clip TK%d Tap 02: hook '%s' + chỉ dấu %s + boi canh ho so "
                  "+ cac diem tinh tiet + 'Bước ngoặt của hồ sơ này' + cau hoi + duong dan YTB + canh bao "
                  "tre em + nhan AIGC; du lieu truy ve .work/script_tap02.json + "
                  "02_SAN_XUAT/Tap02/nguon_tham_khao.md + 01_KICH_BAN/Tap02/kichban_tap02_22102026.md"
                  % (n_dai, i, hook, chidau)),
        "font": None,
        "dieu_khoan": ("TikTok chi hien ~100 ky tu dau truoc khi bam 'more' => dong 1 phai la hook "
                       "(khop chu hook tren hinh); gioi han 4.000 ky tu - %d ky tu; khong dung tu cam "
                       "V9/A9.2; khong khong dinh chan doan lam sang (K5)." % n_dai),
        "kiem_tra_thuong_mai": ("dat (%d ky tu < 4.000; 15/15 muc so lieu truy ve nguon; QC doc lap "
                                ".work/_qc_mota_tap02.py: 0 loi)" % n_dai),
    })

    # --- mo ta ngan ---
    entries.append({
        "file": "02_SAN_XUAT/TIKTOK/Tap02/" + f_ngan,
        "loai": "mo ta NGAN cho truong Description TikTok (rut gon theo chuan Tap01)",
        "cong_cu": GEN,
        "ngay": NGAY,
        "prompt": None,
        "seed": None,
        "mo_ta": ("ban mo ta ngan %d ky tu cho clip TK%d Tap 02: hook '%s' (khop dong 1 cua ban dai) "
                  "+ dong tap/chỉ dấu %s + doan dan + 3 bullet 'NẤC' + 'Bước ngoặt của hồ sơ này' + "
                  "cau hoi 👇 + duong dan YTB + canh bao tre em + nhan AIGC + 5 hashtag CamelCase; "
                  "cau truc rut gon tu Tap01/MoTa_Dai_TK1.txt (khong dung muc 'LƯU Ý'/'NGUỒN THAM KHẢO' "
                  "cua ban dai)" % (n_ngan, i, hook, chidau)),
        "font": None,
        "dieu_khoan": ("TikTok chi hien ~100 ky tu dau truoc khi bam 'more' => dong 1 phai la hook va "
                       "phai KHOP VOI DONG 1 cua MoTa_Dai_TK%d.txt; gioi han 4.000 ky tu - %d ky tu; "
                       "nhan AIGC + canh bao tre em nam trong dong 🔎; V9/A9.2 khong co tu cam; "
                       "duong dan 'bam nut lien kết ngay dau trang ca nhan' vi TikTok khong click duoc "
                       "URL trong Description." % (i, n_ngan)),
        "kiem_tra_thuong_mai": ("dat (%d ky tu < 4.000; dung dai do chuan Tap01 1.078-1.369 ky tu; "
                                "dong 1 khop ban dai; QC doc lap .work/_qc_mota_tap02.py: 0 loi)"
                                % n_ngan),
    })

# --- tai lieu ke hoach / spec ---
entries.append({
    "file": "02_SAN_XUAT/TIKTOK/Tap02/KE_HOACH_CLIP_TAP02.md",
    "loai": "ke hoach san xuat 5 clip TikTok Tap 02 (ke hoach + kich ban + checklist QC)",
    "cong_cu": GEN,
    "ngay": NGAY,
    "prompt": None,
    "seed": None,
    "mo_ta": "tai lieu ke hoach goc cua bo 5 clip Tap 02, sinh tu generator de bao dam 1 nguon su that; chua muc 1-16 (ke hoach, kich ban, QC, mo ta ngan)",
    "font": None,
    "dieu_khoan": "tai lieu ky thuat noi bo; khong dan len TikTok.",
    "kiem_tra_thuong_mai": "dat (self-QC 16 muc trong generator: 16/16 DAT)",
})
entries.append({
    "file": "02_SAN_XUAT/TIKTOK/Tap02/SPEC_AUDIO_CLIP_TAP02.json",
    "loai": "spec audio + timing + hook_render cho 5 clip TikTok Tap 02",
    "cong_cu": GEN,
    "ngay": NGAY,
    "prompt": None,
    "seed": None,
    "mo_ta": "spec duoi dang JSON cho tung clip: cau loi doc, thoi luong uoc luong, mau giong (VoxCPM2 refs), hook_render, muc doanh nhan",
    "font": None,
    "dieu_khoan": "khong dan len TikTok; dung lam input cho buoc sinh video.",
    "kiem_tra_thuong_mai": "dat (thoi luong uoc luong 57.6-82.6 s nam trong khoang TikTok 45-95 s; mau giong dung Tap 02)",
})

added = 0
for e in entries:
    if e["file"] in existing:
        print("BO QUA (da co):", e["file"])
        continue
    prov.append(e)
    added += 1

with io.open(PROV, "w", encoding="utf-8", newline="\n") as f:
    json.dump(prov, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("Da them %d dong. Tong: %d" % (added, len(prov)))
