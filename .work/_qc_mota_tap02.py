# -*- coding: utf-8 -*-
"""QC mo ta + caption TikTok Tap 02 — do that, khong cam tinh."""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DIR = pathlib.Path("02_SAN_XUAT/TIKTOK/Tap02")
KB = pathlib.Path("01_KICH_BAN/Ho_So_Toi_Pham/Tap02/kichban_tap02_22102026.md").read_text(encoding="utf-8-sig")
NGUON = pathlib.Path("02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md").read_text(encoding="utf-8-sig")
TL = json.loads(pathlib.Path(".work/timeline_s_t02.json").read_text(encoding="utf-8-sig"))

# A9.2 — danh sach tu cam (ke ca "ung thu mau")
CAM = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập", "đầu độc",
       "diệt cỏ", "bỏ đói", "móc áo"]
CAM_RE = re.compile(
    r"(?<![\wàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])"
    + "|".join(re.escape(w) for w in CAM) +
    r"(?![\wàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđ])",
    re.IGNORECASE)

# So lieu phai truy duoc ve kich ban tap
NG = KB + "\n" + NGUON
FACTS = {
    "82": KB, "88": KB, "Marie-France Comeau": KB, "37 tuổi": KB,
    "Jessica Lloyd": KB, "25 năm": KB, "46 tuổi": KB, "Nissan Pathfinder": KB,
    "Hubert Genest": KB, "Robert Scott": KB, "Jim Smyth": KB,
    "Trenton": KB, "Tweed": KB, "Belleville": KB, "2010 ONSC 5946": NG,
}

# Kiem tra an toan TikTok
AIGC_LINE = "Nội dung do AI tạo hình và giọng"
MAX_CAPTION = 2200
MAX_DESC = 4000


def check(name, text, is_caption, mode="dai"):
    """mode: 'dai' (mô tả dài) | 'ngan' (mô tả ngắn) | 'caption' (phần dán).

    is_caption=True: kiem tra phan DAN (truoc '---').
    """
    r = {"ten": name, "ky_tu": len(text), "loi": []}
    body = text.split("\n---")[0] if mode == "caption" else text
    hits = [m.group(0) for m in CAM_RE.finditer(body)]
    if hits:
        r["loi"].append("TU CAM V9: %s" % sorted(set(hits)))
    limit = MAX_CAPTION if mode == "caption" else MAX_DESC
    if len(body) > limit:
        r["loi"].append("VUOT gioi han %d ky tu" % limit)
    tags = re.findall(r"#\w+", body)
    # Bo ma chi dau (#8, #9, #10...) — chu co chu so, khong phai hashtag TikTok
    tags = [t for t in tags if not re.fullmatch(r"#\d+", t)]
    if not (5 <= len(tags) <= 8):
        r["loi"].append("hashtag %d (can 5-8)" % len(tags))
    if "#AmberEyes" not in tags:
        r["loi"].append("thieu #AmberEyes")
    if "#HosoCoThat" not in tags:
        r["loi"].append("thieu #HosoCoThat")
    if AIGC_LINE not in body:
        r["loi"].append("thieu dong nhan AIGC")
    if "không phải phóng sự" not in body:
        r["loi"].append("thieu 'khong phong su'")
    if mode in ("dai", "ngan"):
        # canh bao tre em: bat buoc o MO TA (Description), KHONG bat buoc o caption
        # (chu Tap01: caption chi can dong AIGC; canh bao tre em nam o mo ta)
        if "Nội dung không phù hợp cho trẻ em" not in body and \
                "Không phù hợp cho trẻ em" not in body:
            r["loi"].append("thieu canh bao tre em")
    if mode == "caption":
        # Caption: bat buoc co nhan AIGC + hook + "Tập N" + "Hồ sơ có thật"
        if "Hồ sơ có thật" not in body:
            r["loi"].append("thieu 'Ho so co that'")
        if "Tập 02" not in body:
            r["loi"].append("thieu 'Tập 02'")
        if "👁️" not in body:
            r["loi"].append("thieu hook")
    elif mode == "dai":
        # Mo ta dai: canh bao tre em + ghi nhan AIGC + phan luu y + nguon
        if "LƯU Ý" not in body:
            r["loi"].append("thieu phan LUU Y")
        if "NGUỒN THAM KHẢO" not in body:
            r["loi"].append("thieu phan NGUON THAM KHAO")
    else:
        # Mo ta ngan: cau truc chuan Tap 01 — KHONG co dau ke, KHONG co phan muc
        if "——————" in body:
            r["loi"].append("con dau ke (ban ngan khong dung dau muc)")
        if "Bước ngoặt của hồ sơ này:" not in body:
            r["loi"].append("thieu dong 'Buoc ngoat'")
        if "Theo bạn," not in body or "👇" not in body:
            r["loi"].append("thieu cau hoi + dau mui")
        if "Tập 02 · Đại tá hai mặt — Chỉ dấu #" not in body:
            r["loi"].append("thieu dong tap/chi dau")
        # T34: so SO MUC liet ke voi so tu dinh luong trong cau dan
        # ("bon nac thang" nhung chi liet ke 3 bullet => thieu 1 muc).
        n_bullet = body.count("\n• ")
        for tu, so in (("bốn nấc", 4), ("ba nấc", 3), ("năm nấc", 5)):
            if tu in body.lower() and n_bullet < so:
                r["loi"].append("noi '%s' nhung chi liet ke %d bullet" % (tu, n_bullet))
    return r, tags


def main():
    print("=" * 78)
    print("QC MO TA + CAPTION TIKTOK TAP 02")
    print("=" * 78)
    print("Do dai tap YouTube (timeline_s_t02.json): %.2f s = %.1f phut"
          % (TL["total"], TL["total"] / 60))
    print("Gioi han: caption TikTok <= %d · Description TikTok Studio <= %d"
          % (MAX_CAPTION, MAX_DESC))
    print()

    total_loi = 0
    for i in range(1, 6):
        dp = DIR / ("MoTa_Dai_TK%d.txt" % i)
        cp = DIR / ("Caption_TK%d.txt" % i)
        ng = DIR / ("MoTa_Ngan_TK%d.txt" % i)
        dt = dp.read_text(encoding="utf-8-sig")
        ct = cp.read_text(encoding="utf-8-sig")
        nt = ng.read_text(encoding="utf-8-sig")

        rd, tags = check("MoTa_Dai_TK%d" % i, dt, False, "dai")
        rn, _ = check("MoTa_Ngan_TK%d" % i, nt, False, "ngan")
        rc, _ = check("Caption_TK%d" % i, ct, True, "caption")

        # caption phai co phan "Ghi chu khi dang" va con tro placeholder
        if "Ghi chú khi đăng" not in ct:
            rc["loi"].append("thieu phan 'Ghi chu khi dang'")
        if "KHÔNG dán vào caption" not in ct:
            rc["loi"].append("phan ghi chu khong co canh bao khong dan")
        if "LINK_TẬP 02" not in ct:
            rc["loi"].append("thieu cho dieu link YouTube")

        # mo ta ngan: cau truc chuan Tap 01 + dong 1 khop ban dai
        if not (900 <= len(nt) <= 1600):
            rn["loi"].append("do dai %d ngoai 900-1600" % len(nt))
        if "Bước ngoặt của hồ sơ này:" not in nt:
            rn["loi"].append("thieu dong 'Buoc ngoat'")
        if "Theo bạn," not in nt or "👇" not in nt:
            rn["loi"].append("thieu cau hoi + dau mui")
        if "📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút" not in nt:
            rn["loi"].append("thieu dong Xem tron bo (25 phut)")
        if nt.splitlines()[0].strip() != dt.splitlines()[0].strip():
            rn["loi"].append("dong 1 lech ban dai")
        if nt.count("——————"):
            rn["loi"].append("con duong ke (nen bo, dung dang dau muc)")

        print("TK%d" % i)
        for r in (rd, rn, rc):
            st = "DAT" if not r["loi"] else "LOI %d" % len(r["loi"])
            print("  %-16s %5d ky tu  %-6s  %s"
                  % (r["ten"], r["ky_tu"], st, "; ".join(r["loi"]) if r["loi"] else ""))
            total_loi += len(r["loi"])
        print("  hashtag mo ta: %d -> %s" % (len(tags), " ".join(tags)))
        print()

    print("-" * 78)
    print("Tong loi: %d" % total_loi)

    print()
    print("SO LIEU TRONG MO TA — TRUY VE KICH BAN TAP")
    for k, _ in FACTS.items():
        in_mota = sum(1 for i in range(1, 6)
                      if k in (DIR / ("MoTa_Dai_TK%d.txt" % i)).read_text(encoding="utf-8-sig"))
        in_kb = NG.count(k)
        print("  %-20s xuat hien trong %d/5 mo ta · %d lan trong kich ban/nguon -> %s"
              % (k, in_mota, in_kb, "OK" if (in_mota == 0 or in_kb > 0) else "KHONG CO NGUON"))

    print()
    print("SO SANH THOI LUONG")
    spec = json.loads((DIR / "SPEC_AUDIO_CLIP_TAP02.json").read_text(encoding="utf-8-sig"))
    for c in spec["clips"]:
        u = sum(l["uoc_luong_s"] for l in c["lines"])
        n = len(c["lines"])
        print("  %-4s %2d cau · uoc luong %5.1f s (%d cau) · uoc luong co pause: %5.1f s"
              % (c["id"], n, u, n, sum(l["uoc_luong_s"] + l["pause_after"] for l in c["lines"])))


if __name__ == "__main__":
    main()
