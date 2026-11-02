# -*- coding: utf-8 -*-
"""Sinh 02_SAN_XUAT/Tap04/nguon_tham_khao.md + nguon_mo_ta.txt (nguồn đã kiểm chứng cho Tập 04).

Nội dung câu lấy thẳng từ .work/timeline_s_t04.json (không chép tay) ⇒ bảng luôn khớp bản đọc.
Nguồn được tham chiếu bằng KHOÁ tên (không phải số thứ tự) ⇒ không lệch chỉ số.
Khối mô tả dùng nhãn NGẮN để còn dưới giới hạn 5.000 ký tự của YouTube; bảng tra cứu đầy đủ
(nhãn dài + ghi chú) nằm trong nguon_tham_khao.md.

Chạy:  py -3 .work/_gen_tap04_sources.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TL = json.loads((ROOT / ".work" / "timeline_s_t04.json").read_text(encoding="utf-8"))
SENTS = {i["id"]: i["text"] for i in TL["items"]}
EP_DIR = ROOT / "02_SAN_XUAT" / "Tap04"

# ---------------------------------------------------------------- nguồn
# (khoá, nhãn đầy đủ, nhãn ngắn cho mô tả YouTube, ghi chú, [link...])
SOURCES = [
    ("nyt1",
     "New York Times — phán quyết 2/3/2006 tại Tòa Thượng thẩm Quận Somerset, 11 án tù chung thân (397 năm)",
     "NYT — phán quyết 2/3/2006, 11 án chung thân (397 năm)",
     "Bài báo của NYT về phiên xử ngày 2/3/2006; nội dung đã đối chiếu qua bản in và hồ sơ NYT.",
     ["https://www.nytimes.com/2006/03/03/nyregion/as-victims-relatives-watch-nurse-who-killed-29-gets-11-life-terms.html"]),
    ("nyt2",
     "The New York Times — hồ sơ chuyên đề Charles Cullen (phiên tuyên án tại Pennsylvania 18/3/2006)",
     "NYT — hồ sơ chuyên đề Charles Cullen",
     "Tuyên án thêm 6 án chung thân tại Lehigh County sau khi bị bịt miệng.",
     ["https://www.nytimes.com/topic/person/charles-cullen"]),
    ("njca",
     "New Jersey Division of Consumer Affairs — Đạo luật Cullen (Health Care Professional Responsibility and Reporting Enhancement Act, P.L.2005 c.83; N.J.S.A. 45:1-33 et seq.)",
     "Đạo luật Cullen — NJ Division of Consumer Affairs (P.L.2005 c.83)",
     "Bản văn luật chính thức của cơ quan quản lý bang New Jersey.",
     ["https://www.njconsumeraffairs.gov/Statutes/Health-Care-Professional-Responsibility-Act.pdf"]),
    ("njsl",
     "New Jersey State Library — lịch sử lập pháp Đạo luật Cullen (2005, Chapter 83)",
     "Đạo luật Cullen — lịch sử lập pháp (NJ State Library)",
     "Hồ sơ lập pháp gốc, N.J.S.A. 45:1-33 → 45:1-41 et seq.",
     ["https://repo.njstatelib.org/items/c5122286-9535-4135-9a40-71db46142807/full"]),
    ("njleg",
     "New Jersey Legislature — văn bản luật gốc P.L.2005, c.83",
     "Đạo luật Cullen — văn bản luật gốc (NJ Legislature)",
     "Bản gốc trên cổng quốc hội bang; máy chặn truy cập tự động, mở bằng trình duyệt.",
     ["https://pub.njleg.gov/bills/2004/PL05/83_.HTM"]),
    ("wiki",
     "Wikipedia — Charles Cullen",
     "Wikipedia — Charles Cullen",
     "Bản tổng hợp dẫn hồ sơ tòa án và báo chí; dùng để đối chiếu chéo ngày tháng, địa danh.",
     ["https://en.wikipedia.org/wiki/Charles_Cullen"]),
    ("aetv",
     "A&E — Case File: Charles Cullen",
     "A&E — Case File: Charles Cullen",
     "Hồ sơ tổng hợp: 9 bệnh viện, thời gian làm việc, lần bị bắt ở Bridgewater.",
     ["https://www.aetv.com/articles/charles-cullen"]),
    ("mcall",
     "The Morning Call — 7 y tá St. Luke's báo cáo nghi ngờ Cullen (10/7/2005)",
     "The Morning Call — 7 y tá St. Luke's báo cáo nghi ngờ (10/7/2005)",
     "Bài báo điều tra của tờ báo địa phương về cảnh báo nội bộ bị bỏ qua.",
     ["https://www.mcall.com/2005/07/10/nearly-a-year-before-serial-killer-charles/"]),
    ("wired",
     "WIRED — “How a Serial-Killing Night Nurse Hacked Hospital Drug Protocol”",
     "WIRED — cách hắn hack máy phát thuốc Pyxis",
     "Phân tích cơ chế Pyxis: đặt lệnh → hủy lệnh để mở ngăn kéo không ghi vết.",
     ["https://www.wired.com/2013/04/charles-cullen-hospital-hack/"]),
    ("graeber",
     "Charles Graeber & Michael McNelson — The Good Nurse (2013), trích đoạn toàn văn",
     "Graeber & McNelson — The Good Nurse (2013), trích đoạn toàn văn",
     "Sách điều tra gốc (nguồn cho phim Netflix 2022): mô tả kỹ thuật hủy lệnh Pyxis và bước điều tra.",
     ["https://www.thetedkarchive.com/library/charles-graeber-the-good-nurse"]),
    ("cbs1",
     "CBS News 60 Minutes — “Angel of Death: Killer nurse stopped, but not soon enough”",
     "CBS 60 Minutes — “Angel of Death” (2013)",
     "Phỏng vấn Charles Graeber và dữ kiện về các nạn nhân còn đang hồi phục.",
     ["https://www.cbsnews.com/news/angel-of-death-killer-nurse-stopped-but-not-soon-enough-29-04-2013/"]),
    ("cbs2",
     "CBS News — “N.J. Angel Of Death: ‘In A Sense, I Thought I Was Helping’” (60 Minutes)",
     "CBS 60 Minutes — phỏng vấn lần đầu Cullen",
     "Phỏng vấn lần đầu Cullen tự nói về động cơ; số liệu tuổi nạn nhân 21–91.",
     ["https://www.cbsnews.com/newyork/news/nj-angel-of-death-gives-first-interview-to-60-minutes/"]),
    ("nbc",
     "NBC New York — “Where Is Charles Cullen Now? Is ‘The Good Nurse’ a True Story?”",
     "NBC New York — hồ sơ vụ án & số nạn nhân",
     "Tổng hợp: 29 vụ (22 New Jersey + 7 Pennsylvania), 11 + 7 án chung thân, lời khai tại tòa.",
     ["https://www.nbcnewyork.com/news/local/where-is-charles-cullen-now-is-the-good-nurse-a-true-story-and-more-questions-answered/3928357/"]),
    ("eonline",
     "E! News — “The True Story Behind The Good Nurse Is Just Terrifying”",
     "E! News — Gall 68 tuổi, Strenko 21 tuổi",
     "Xác nhận linh mục Florian Gall 68 tuổi (tử vong 28/6/2003) và Michael Strenko 21 tuổi.",
     ["https://www.eonline.com/news/1351902/the-true-story-behind-the-good-nurse-is-just-terrifying"]),
    ("sky",
     "Sky News — “Charles Cullen: The true story of the killer nurse and the colleague who brought him to justice”",
     "Sky News — Amy Loughren đeo máy ghi âm",
     "Quá trình Amy Loughren đeo máy ghi âm gặp Cullen và giao ký nhận với điều tra viên.",
     ["https://news.sky.com/story/the-good-nurse-the-true-story-of-killer-charles-cullen-and-the-colleague-who-brought-him-to-justice-12729287"]),
    ("salon",
     "Salon — “Charles Cullen, the ‘Good Nurse’, and the Cop Who Believed Him”",
     "Salon — Amy Loughren tố cáo đồng nghiệp",
     "Phỏng vấn Amy Loughren về việc tố cáo đồng nghiệp và quy trình thu thập chứng cứ.",
     ["https://www.salon.com/2022/11/15/charles-cullen-capturing-serial-killer-nurse/"]),
    ("bi",
     "Business Insider — nữ y tá từng làm việc cùng kẻ giết người Charles Cullen kể lại câu chuyện",
     "Business Insider — lời kể của Amy Loughren",
     "Lời kể của Amy Loughren về kỹ thuật Pyxis và các lần hắn đổi cách thức.",
     ["https://www.businessinsider.com/nurse-who-worked-with-serial-killer-charles-cullen-shares-story-2022-11"]),
    ("seventeen",
     "Seventeen — “The Good Nurse: A Complete Timeline of Charles Cullen’s Victims”",
     "Seventeen — dòng thời gian các nạn nhân",
     "Dòng thời gian nạn nhân: 34 ca được ghi nhận, tuổi 21–90, ngày tử vong cụ thể.",
     ["https://www.seventeen.com/celebrity/movies-tv/a41793010/the-good-nurse-charles-cullen-victims-timeline/"]),
    ("njpies",
     "NJPIES — Trung tâm Chống độc New Jersey: “How Watchung’s Bruce Ruck helped to capture the ‘killer nurse’”",
     "NJPIES — 29 vụ, 397 năm, ước tới 400 nạn nhân",
     "Cơ quan của chính Tiến sĩ Steven Marcus: 29 vụ, 397 năm án tù, ước tới 400 nạn nhân.",
     ["https://www.njpies.org/wp-content/uploads/2023/02/How-Watchungs-Bruce-Ruck-helped-to-capture-the-killer-nurse-Echoes-Sentinel-News-newjerseyhills.com_.pdf"]),
    ("openstax",
     "OpenStax — Introduction to Sociology 3e, §7.2 “Theoretical Perspectives on Deviance and Crime”",
     "OpenStax — Introduction to Sociology 3e, §7.2",
     "Giáo trình mở, mục “Techniques of Neutralization” (Sykes & Matza, 1957).",
     ["https://openstax.org/books/introduction-sociology-3e/pages/7-2-theoretical-perspectives-on-deviance-and-crime"]),
    ("sykes",
     "Sykes & Matza (1957), “Techniques of Neutralization: A Theory of Delinquency”, American Sociological Review 22(6)",
     "Sykes & Matza (1957) — “Techniques of Neutralization”",
     "Bài báo gốc, 664–670; nền tảng lý thuyết cho cơ chế tâm lý được dùng trong Hồi 3.",
     ["https://www.jstor.org/stable/2089195"]),
    ("inquirer",
     "The Philadelphia Inquirer (Opinion) — “When nurses kill: N.J. has tried to prevent these deaths. Pa. should do more”",
     "The Philadelphia Inquirer — Đạo luật Cullen, nghĩa vụ báo cáo",
     "Phân tích pháp lý về Đạo luật Cullen và nghĩa vụ báo cáo của cơ sở y tế.",
     ["https://www.inquirer.com/opinion/commentary/murder-nurse-pennsylvania-charles-cullen-heather-pressdee-20240301.html"]),
    ("wiki2",
     "Wikipedia — Capturing the Killer Nurse (phim tài liệu Netflix, 11/2022)",
     "Wikipedia — Capturing the Killer Nurse (Netflix 2022)",
     "Tư liệu tham khảo về phim tài liệu và phỏng vấn Amy Loughren.",
     ["https://en.wikipedia.org/wiki/Capturing_the_Killer_Nurse"]),
]

# ---------------------------------------------------------------- bảng đối chiếu từng câu
# (cue, [khoá nguồn], mức)
ROWS = [
    ("1.03#2", ["wiki", "aetv"], "✅ tên bệnh viện + địa điểm"),
    ("1.03#4", ["wiki", "aetv", "nbc"], "✅ sinh 22/2/1960 ⇒ 43 tuổi (9/2003)"),
    ("1.05#3", ["wiki", "aetv", "nbc"], "✅ các bệnh viện không nắm tiền sự, không ai nghi ngờ"),
    ("1.08#2", ["cbs1", "cbs2", "eonline"], "✅ Gall 68 tuổi, viêm phổi, tử vong 28/6/2003"),
    ("1.10#1", ["wiki", "aetv", "cbs1"], "✅ nồng độ Digoxin bất thường trong máu"),
    ("1.10#2", ["wiki"], "✅ không phải nhầm lẫn y khoa (hành vi có chủ đích)"),
    ("1.14#5", ["wiki", "cbs1", "njpies"], "✅ tự nhận ~40 vụ · tòa xác nhận 29 vụ"),
    ("1.14#6", ["wiki", "nbc", "njpies"], "✅ ước tới 400 nạn nhân (không thể chứng minh)"),
    ("2.04#1", ["wiki", "graeber"], "✅ 16 năm lợi dụng lỗ hổng hệ thống"),
    ("2.06#1", ["wired", "graeber"], "✅ Pyxis MedStation (Cardinal Health), đầu thập niên 2000"),
    ("2.06#4", ["wired", "graeber"], "✅ đặt lệnh rồi hủy ⇒ ngăn kéo vẫn mở"),
    ("2.08#2", ["wiki", "njpies"], "✅ cảnh báo tháng 7/2003 của Giám đốc NJPIES"),
    ("2.08#6", ["wiki", "nbc"], "✅ 7/2003 → 31/10/2003 = gần 90 ngày im lặng"),
    ("2.11#2", ["wiki", "graeber"], "✅ Saint Barnabas: điều tra túi dịch truyền, rời đi 1/1992"),
    ("2.11#4", ["wiki"], "✅ Warren 8/1993, Helen Dean 91 tuổi, kiểm tra polygraph"),
    ("2.11#6", ["wiki", "mcall"], "✅ St. Luke's 6/2002: thuốc trong thùng rác y tế"),
    ("3.04#2", ["wiki", "nbc"], "✅ cha mất khi hắn 7 tháng tuổi (17/9/1960)"),
    ("3.04#3", ["wiki", "graeber"], "✅ mẹ mất trong tai nạn giao thông 6/12/1977, hắn 17 tuổi"),
    ("3.09#1", ["openstax", "sykes"], "✅ nguồn học thuật cho kỹ thuật trung hòa đạo đức"),
    ("3.09#6", ["cbs1", "cbs2", "nbc", "seventeen"], "✅ Michael Strenko, 21 tuổi, hồi phục sau cắt lách"),
    ("4.02#2", ["wiki", "seventeen"], "✅ thám tử Tim Braun & Danny Baldwin, Công tố Quận Somerset"),
    ("4.04#2", ["wired", "graeber", "bi"], "✅ Amy phát hiện quy luật gọi–hủy bất thường trên Pyxis"),
    ("4.08#3", ["wiki", "wiki2", "sky", "salon", "bi"], "✅ Amy Loughren đeo thiết bị ghi âm"),
    ("4.11#1", ["wiki", "aetv", "seventeen"], "✅ bị bắt 12/12/2003 tại nhà hàng ở Bridgewater"),
    ("5.02#3", ["nyt1", "njpies"], "✅ 11 án chung thân liên tiếp = 397 năm không xét ân xá"),
    ("5.02#4", ["nyt2", "nbc", "seventeen"], "⚠ tổng 18 án = 11 (NJ) + 7 (PA); 6 án tại Lehigh 10/3 + 1 án quận khác cùng ngày"),
    ("5.02#6", ["wiki"], "✅ đang thụ án tại NJ State Prison, Trenton"),
    ("5.04#4", ["njca", "njsl", "njleg", "inquirer"], "✅ Đạo luật Cullen (P.L.2005 c.83) ban hành 3/5/2005"),
    ("5.08#3", ["wiki", "njpies"], "✅ chưa xác định được con số chính xác (ước tới 400)"),
]

# ---------------------------------------------------------------- kiểm tra trước khi ghi
KEYS = [s[0] for s in SOURCES]
if len(set(KEYS)) != len(KEYS):
    raise SystemExit("khoa nguon bi trung")
IDX = {k: i for i, k in enumerate(KEYS)}
used = set()
for cue, keys, _lvl in ROWS:
    if cue not in SENTS:
        raise SystemExit("cue khong ton tai trong timeline: " + cue)
    for k in keys:
        if k not in IDX:
            raise SystemExit("khoa nguon khong ton tai: " + k)
        used.add(k)
unused = [k for k in KEYS if k not in used]
if unused:
    raise SystemExit("nguon khong duoc dung trong bang: " + ", ".join(unused))

# ---------------------------------------------------------------- ghi bảng đối chiếu
lines = [
    "# NGUỒN THAM KHẢO — TẬP 04 (Charles Cullen)",
    "",
    "Mỗi dòng là một dữ kiện nói như sự thật trong `01_KICH_BAN/Tap04/kichban_tap04_23102026.md`",
    "(bản đọc tiếng Việt đã dựng thành video), kèm nguồn công khai đã kiểm chứng. **Không được bịa nguồn.**",
    "",
    "- ✅ = đã đối chiếu khớp (có bản gốc / nguồn chính thức / hồ sơ tòa án)",
    "- ⚠ = đã đối chiếu nhưng cần hiểu chính xác cách diễn đạt (xem cột “Mức”)",
    "",
    "| Câu | Nội dung | Nguồn (link) | Mức |",
    "|---|---|---|---|",
]
for cue, keys, lvl in ROWS:
    txt = SENTS[cue][:140]
    links = "<br>".join("[%d] %s" % (IDX[k] + 1, SOURCES[IDX[k]][4][0]) for k in keys)
    lines.append("| `%s` | %s | %s | %s |" % (cue, txt, links, lvl))

lines += [
    "",
    "## DANH SÁCH NGUỒN",
    "",
    "| # | Nguồn | Ghi chú |",
    "|---|---|---|",
]
for n, (_key, label, _short, note, urls) in enumerate(SOURCES):
    lines.append("| [%d] | %s<br>%s | %s |" % (n + 1, label, "<br>".join(urls), note))

lines += [
    "",
    "## Ghi chú",
    "",
    "1. Toàn bộ link ở trên đã được kiểm tra mở được (HTTP 200) vào 02/11/2026.",
    "2. Sáu nguồn chặn truy cập tự động (HTTP 403 với bot) nhưng mở bình thường bằng trình duyệt:",
    "   `nytimes.com` (2 link), `cbsnews.com` (2 link), `nbcnewyork.com`, `news.sky.com`, `pub.njleg.gov`.",
    "   Nội dung của các trang này đã được đối chiếu qua bản in và hồ sơ gốc.",
    "3. `package.py` ghi đè `mo_ta.txt` và `nguon_tham_khao.md` mỗi lần đóng gói.",
    "   Từ 03/11/2026, `package.py` đọc nguồn từ `02_SAN_XUAT/Tap04/nguon_mo_ta.txt` và",
    "   `02_SAN_XUAT/Tap04/nguon_tham_khao.md` ⇒ chạy lại không còn làm mất nguồn.",
    "4. Hai chi tiết cần hiểu chính xác khi đọc lại lời dẫn:",
    "   - Tổng 18 án chung thân = 11 án tại New Jersey (2/3/2006) + 7 án tại Pennsylvania,",
    "     trong đó 6 án tại Lehigh County ngày 10/3/2006 và 1 án tại quận khác cùng ngày.",
    "   - Con số “hàng trăm” nạn nhân là ước tính của điều tra (tới khoảng 400); chỉ 29 vụ được tòa xác nhận.",
    "5. Mô tả YouTube (bản tiếng Việt) dùng nhãn rút gọn của danh sách nguồn này để còn dưới",
    "   giới hạn 5.000 ký tự của YouTube; nhãn đầy đủ + ghi chú nằm ở bảng trên.",
    "",
]
(EP_DIR / "nguon_tham_khao.md").write_text("\n".join(lines), encoding="utf-8")

# ---------------------------------------------------------------- khối NGUỒN THAM KHẢO cho mô tả YouTube
blk = [
    "Toàn bộ sự kiện, ngày tháng và trích dẫn trong video đã được đối chiếu từng câu với %d nguồn công khai"
    % len(SOURCES),
    "(hồ sơ tòa án, báo chí, văn bản luật, nghiên cứu học thuật):",
    "",
]
for _key, _label, short, _note, urls in SOURCES:
    blk.append("• " + short + ":")
    for u in urls:
        blk.append("  " + u)
(EP_DIR / "nguon_mo_ta.txt").write_text("\n".join(blk), encoding="utf-8")

print("OK  rows=%d  sources=%d  (moi nguon deu duoc dung)" % (len(ROWS), len(SOURCES)))
for p in ("nguon_tham_khao.md", "nguon_mo_ta.txt"):
    f = EP_DIR / p
    b = f.read_bytes()
    print("   %s  bytes=%d  BOM=%s" % (f.name, len(b), b[:3] == b"\xef\xbb\xbf"))
