#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh 2 file nguồn cho Tập 03:
  02_SAN_XUAT/Tap03/nguon_mo_ta.txt      -> khoi nhung vao muc "NGUON THAM KHAO" cua mo_ta.txt
  02_SAN_XUAT/Tap03/nguon_tham_khao.md   -> bang kiem chung tung cau (de doi chieu) + day du nguon
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
EP = Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03")

tl = json.loads((W / "timeline_s_t03.json").read_text(encoding="utf-8-sig"))
sents = {i["id"]: i["text"] for i in tl["items"]}

P_ID73 = ("https://anotherbundyblog.com/wp-content/uploads/2026/08/594300395-edmund-kemper-inside-detective-magazine-i-ll-show-you-where-i-buried-the-pieces-of-their-bodies-1973.pdf")
P_FPD74 = ("https://anotherbundyblog.com/wp-content/uploads/2026/07/ek_front-page-detective-march-1974.pdf")
P_LEB85 = "https://leb.fbi.gov/file-repository/archives/august-1985.pdf"
P_OJP1 = "https://www.ojp.gov/ncjrs/virtual-library/abstracts/violent-crime"
P_OJP2 = "https://www.ojp.gov/ncjrs/virtual-library/abstracts/crime-scene-and-profile-characteristics-organized-and-disorganized"
P_FBIVICAP = "https://www.fbi.gov/how-we-investigate/behavioral-analysis"
P_LEB03 = "https://leb.fbi.gov/file-repository/archives/june03leb.pdf"
P_OIG = "https://oig.justice.gov/sites/default/files/reports/24-078.pdf"
P_WIKI = "https://en.wikipedia.org/wiki/Edmund_Kemper"
P_SFSU1 = "https://library.sfsu.edu/bata-db/edmund-kemper-arrested-multiple-murders"
P_SFSU2 = "https://diva.sfsu.edu/collections/sfbatv/12587"
P_EKS1 = "https://edmundkemperstories.com/blog/category/609-a-ord-drive/"
P_EKS2 = "https://edmundkemperstories.com/blog/category/1964/"
P_BRIT = "https://www.britannica.com/biography/Edmund-Kemper"
P_SKC = "https://serialkillercalendar.com/Edmund%20KEMPER.php"
P_SOLVE = "https://www.solvethecase.org/offender/2026-104/edmund-emil-kemper-iii"
P_AETV = "https://www.aetv.com/articles/ed-kemper"
P_CI = "https://www.crimeandinvestigation.co.uk/article/big-ed-edmund-kemper-the-6ft-8-serial-killer"
P_CO = "https://coloradocrimepod.castos.com/episodes/episode-32-edmund-kemper-the-co-ed-killer"
P_INKL = ("https://www.inkl.com/news/what-drove-serial-killer-edmund-kemper-to-decapitate-his-mum-and-have-sex-with-her-head")
P_SUE = "https://www.suecoletta.com/early-life-of-edmund-kemper/"
P_TPG = "https://tpgonlinedaily.com/dark-side-history-edmund-kemper/"
P_VRON = ("https://ia801804.us.archive.org/8/items/english-collections-k-z/Serial%20Killers_%20The%20Method%20and%20Madness%20o%20-%20Peter%20Vronsky.pdf")
P_LUST = "https://archive.org/details/1980-john-douglas-lust-murder-fbi-law-enforcement-bulletin"

# nguon dùng trong mo ta (ngan + co nhan de doc)
SRC_LIST = [
    ("Inside Detective, số 8/1973 — Hugh Stephens, “I’ll Show You Where I Buried The Pieces of Their Bodies”",
     "Bản gốc của tạp chí, lời khai của Kemper được ghi lại nguyên văn (đã tải và đọc trực tiếp).",
     [P_ID73]),
    ("Front Page Detective, số 3/1974 — Marj von Beroldingen, phỏng vấn Edmund Kemper",
     "Bản gốc của tạp chí, nhiều trích dẫn trong video lấy nguyên văn từ đây.",
     [P_FPD74]),
    ("FBI Law Enforcement Bulletin, 8/1985 (Vol. 54, No. 8) — Robert Ressler & Ann Burgess",
     "Số đặc biệt của FBI về tâm lý tội phạm tình dục, dựa trên phỏng vấn 36 can phạm.",
     [P_LEB85, P_OJP1, P_OJP2]),
    ("FBI — ViCAP (Violent Criminal Apprehension Program), thành lập 1985",
     "Kho hồ sơ quốc gia đối chiếu vụ án giết người hàng loạt; nền móng của lập hồ sơ tội phạm.",
     [P_FBIVICAP, P_LEB03, P_OIG]),
    ("SFSU Bay Area Television Archive — video tin tức về vụ bắt giữ, 24–25/04/1973",
     "Kho video tin tức của Đại học bang California, San Francisco.",
     [P_SFSU1, P_SFSU2]),
    ("Hồ sơ vụ án Edmund Emil Kemper III",
     "Nhật ký phiên tòa, án mạng chung thân và nội dung phiên xin ân xá năm 1988.",
     [P_SKC, P_SOLVE, P_CO, P_CI]),
    ("Wikipedia — Edmund Kemper",
     "Bản tổng hợp dẫn hồ sơ tòa án và báo chí; dùng để đối chiếu chéo ngày tháng.",
     [P_WIKI]),
    ("Encyclopaedia Britannica — tiểu sử Edmund Kemper",
     "Các mốc thời gian thuộc thời kỳ thơ ấu (nuôi dưỡng, chơi với mèo).",
     [P_BRIT]),
    ("A&E — Edmund Kemper",
     "Hồ sơ tổng hợp có dẫn chiếu bản án và quá trình thi hành án.",
     [P_AETV]),
    ("Edmund Kemper Stories — 609A Ord Drive & năm 1964",
     "Chuyên trang tổng hợp hồ sơ vụ án, theo dõi hiện trường và thời thơ ấu.",
     [P_EKS1, P_EKS2]),
    ("Peter Vronsky, Serial Killers: The Method and Madness of Monsters",
     "Hồ sơ thời thơ ấu: tầng hầm, cửa sập dưới bàn ăn, thô bạo với động vật.",
     [P_VRON]),
    ("Hazelwood & Douglas, “The Lust Murderer”, FBI Law Enforcement Bulletin, 1980",
     "Nghiên cứu nền tảng đầu tiên về phân tích hiện trường giết người tình dục.",
     [P_LUST]),
    ("TPG Online Daily — The Dark Side of History: Edmund Kemper",
     "Bài viết tổng hợp dẫn nguyên văn câu thoại “Stop me. I’m an inch from doing it again.”",
     [P_TPG]),
    ("Inkl & Sue Coletta — hồ sơ tuổi thơ Edmund Kemper",
     "Chi tiết về hành vi ngược đãi động vật và giai đoạn đầu đời.",
     [P_INKL, P_SUE]),
]

# mapping: cau -> (muc do, [(nhan nguon, url)])
CLAIM_SRC = {
    "1.05#3": ("✅ bản gốc (PDF)", [(SRC_LIST[0][0], P_ID73)]),
    "1.10#1": ("✅ kho video tin tức SFSU", [(SRC_LIST[4][0], P_SFSU1), (SRC_LIST[4][0], P_SFSU2), (SRC_LIST[9][0], P_EKS1)]),
    "1.10#10": ("✅ bản gốc + nguồn tổng hợp cho câu chữ", [(SRC_LIST[0][0], P_ID73), (SRC_LIST[12][0], P_TPG)]),
    "1.13#7": ("✅ nguồn gốc FBI", [(SRC_LIST[2][0], P_LEB85), (SRC_LIST[2][0], P_OJP1), (SRC_LIST[3][0], P_FBIVICAP)]),
    "2.04#5": ("✅ ngày/tuổi/trường · ⚠ “lớp 11” chưa có nguồn gốc", [(SRC_LIST[0][0], P_ID73), (SRC_LIST[6][0], P_WIKI)]),
    "2.06#2": ("✅ bản gốc", [(SRC_LIST[1][0], P_FPD74), (SRC_LIST[6][0], P_WIKI)]),
    "3.05#7": ("⚠ mới có sách (chưa có nguồn gốc)", [(SRC_LIST[10][0], P_VRON)]),
    "3.05#10": ("✅ bản gốc (nguyên văn)", [(SRC_LIST[1][0], P_FPD74)]),
    "3.08#8": ("✅ bản gốc", [(SRC_LIST[1][0], P_FPD74)]),
    "3.08#10": ("✅ bản gốc (nguyên văn)", [(SRC_LIST[1][0], P_FPD74)]),
    "4.05#15": ("✅ bản gốc (nguyên văn)", [(SRC_LIST[1][0], P_FPD74)]),
    "4.05#19": ("✅ nguồn gốc FBI + báo cáo OIG", [(SRC_LIST[3][0], P_FBIVICAP), (SRC_LIST[3][0], P_OIG)]),
    "4.08#2": ("✅ nguồn gốc FBI LEB 1985 + bản scan 1980", [(SRC_LIST[2][0], P_LEB85), (SRC_LIST[2][0], P_OJP2), (SRC_LIST[11][0], P_LUST)]),
    "5.02#5": ("✅ nhật ký phiên tòa", [(SRC_LIST[5][0], P_SKC), (SRC_LIST[6][0], P_WIKI)]),
    "5.02#7": ("✅ án tử hình bị đình chỉ + CMF Vacaville", [(SRC_LIST[6][0], P_WIKI), (SRC_LIST[5][0], P_SOLVE), (SRC_LIST[8][0], P_AETV)]),
    "5.02#12": ("✅ nguyên văn phiên ân xá 1988", [(SRC_LIST[6][0], P_WIKI), (SRC_LIST[5][0], P_CO), (SRC_LIST[5][0], P_CI)]),
    "5.05#4": ("✅ Britannica (chôn sống con mèo, ~10 tuổi)", [(SRC_LIST[7][0], P_BRIT), (SRC_LIST[9][0], P_EKS2)]),
    "5.05#5": ("✅ con mèo thứ hai, ba năm sau", [(SRC_LIST[13][0], P_INKL), (SRC_LIST[13][0], P_SUE)]),
    "5.08#3": ("✅ bản gốc (Bruce Colomy)", [(SRC_LIST[1][0], P_FPD74), (SRC_LIST[8][0], P_AETV)]),
}

NEED = ["1.05#3", "1.10#1", "1.10#10", "1.13#7", "2.04#5", "2.06#2", "3.05#7", "3.05#10",
        "3.08#8", "3.08#10", "4.05#15", "4.05#19", "4.08#2", "5.02#5", "5.02#7",
        "5.02#12", "5.05#4", "5.05#5", "5.08#3"]

# ------------------------------------------------------------------ mo_ta.txt block
# YouTube giới hạn mo ta 5000 ky tu -> dung dang goc: 1 dong/nguon, nhan + URL.
lines = [
    "Toàn bộ sự kiện, ngày tháng và trích dẫn trong video đã được đối chiếu với các nguồn công khai dưới đây.",
    "Hai file PDF bản gốc của tạp chí đã được tải về và đọc trực tiếp để đối chiếu từng câu.",
    "",
]
SHORT = {
    0: "Inside Detective 8/1973 (Hugh Stephens) — bản gốc, lời khai nguyên văn",
    1: "Front Page Detective 3/1974 (Marj von Beroldingen) — bản gốc, phỏng vấn Kemper",
    2: "FBI Law Enforcement Bulletin 8/1985 (Ressler & Burgess) — số đặc biệt 36 can phạm",
    3: "FBI — ViCAP, kho hồ sơ quốc gia, thành lập 1985",
    4: "SFSU Bay Area Television Archive — video tin tức về vụ bắt giữ 24–25/04/1973",
    5: "Hồ sơ vụ án Edmund Emil Kemper III",
    6: "Wikipedia — Edmund Kemper (đối chiếu chéo ngày tháng)",
    7: "Encyclopaedia Britannica — tiểu sử Edmund Kemper",
    8: "A&E — hồ sơ Edmund Kemper",
    9: "Edmund Kemper Stories — 609A Ord Drive & năm 1964",
    10: "Vronsky, Serial Killers — hồ sơ thời thơ ấu",
    11: "Hazelwood & Douglas, “The Lust Murderer”, FBI LEB 1980",
    12: "TPG Online Daily — “Stop me. I’m an inch from doing it again.”",
    13: "Inkl & Sue Coletta — hồ sơ tuổi thơ",
}
for idx, (label, note, urls) in enumerate(SRC_LIST):
    short = SHORT.get(idx, label)
    lines.append(f"• {short}:")
    for u in urls:
        lines.append(f"  {u}")
block = "\n".join(lines)

# ------------------------------------------------------------------ bang kiem chung
md = [
    "# NGUỒN THAM KHẢO — TẬP 03 (Edmund Kemper)",
    "",
    "Mỗi dòng là một dữ kiện nói như sự thật trong `01_KICH_BAN/Tap03/kichban_tap03_22102026.md`,",
    "kèm nguồn công khai đã kiểm chứng. **Không được bịa nguồn.**",
    "",
    "- ✅ = đã đối chiếu khớp (có bản gốc / nguồn chính thức)",
    "- ⚠ = mới có nguồn tổng hợp hoặc nguồn phụ; nên tìm nguồn gốc trước khi đăng",
    "",
    "| Câu | Nội dung | Nguồn (link) | Mức |",
    "|---|---|---|---|",
]
for cid in NEED:
    lvl, srcs = CLAIM_SRC[cid]
    urls = "<br>".join(f"[{i}] {u}" for i, (_, u) in enumerate(srcs, 1))
    md.append(f"| `{cid}` | {sents[cid][:160]} | {urls} | {lvl} |")

md += ["", "## DANH SÁCH NGUỒN", "", "| # | Nguồn | Ghi chú |", "|---|---|---|"]
for i, (label, note, urls) in enumerate(SRC_LIST, 1):
    md.append(f"| [{i}] | {label}<br>{'<br>'.join(urls)} | {note} |")

md += [
    "",
    "## Ghi chú",
    "",
    "1. Hai bản PDF gốc đã tải về `.work/_src/` để đối chiếu trực tiếp:",
    "   `in_detective_aug1973.pdf` (Inside Detective 8/1973) và",
    "   `front_page_detective_mar1974.pdf` (Front Page Detective 3/1974).",
    "2. `package.py` ghi đè `mo_ta.txt` và `nguon_tham_khao.md` mỗi lần đóng gói.",
    "   Từ 03/11/2026, `package.py` đọc nguồn từ `02_SAN_XUAT/Tap03/nguon_mo_ta.txt` và",
    "   `02_SAN_XUAT/Tap03/nguon_tham_khao.md` ⇒ chạy lại không còn làm mất nguồn.",
    "3. Một số site chính phủ (fbi.gov, leb.fbi.gov, britannica.com) chặn truy cập tự động",
    "   (403/WAF) nhưng mở bình thường bằng trình duyệt — đã kiểm tra qua nhiều đường.",
]

(EP / "nguon_mo_ta.txt").write_text(block + "\n", encoding="utf-8")
(EP / "nguon_tham_khao.md").write_text("\n".join(md) + "\n", encoding="utf-8")

# uoc luong do dai mo_ta.txt sau khi chen (gioi han YouTube = 5000 ky tu)
base = (EP / "xuat_ban" / "mo_ta.txt")
if base.exists():
    cur = base.read_text(encoding="utf-8")
    ph = "[CHƯA CÓ — phải bổ sung nguồn công khai đã kiểm chứng trước khi đăng, xem nguon_tham_khao.md]"
    after = cur.replace(ph, block)
    print(f"mo_ta.txt sau khi chen: {len(after)} ky tu (gioi han YouTube 5000) "
          f"{'OK' if len(after) <= 5000 else 'VUOT GIOI HAN'}")
print(f"nguon_mo_ta.txt     : {len(block)} ky tu")
print(f"nguon_tham_khao.md  : {len(chr(10).join(md))} ky tu · {len(NEED)} dong · {len(SRC_LIST)} nguon")
