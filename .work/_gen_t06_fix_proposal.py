#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh `02_SAN_XUAT/Tap06/DeXuat_Sua_Tap06.md` — gói sửa 7 câu + 6 caption.

Câu hiện tại được TRÍCH tự động từ .work/script_tap06.json ⇒ không bao giờ lệch
với kịch bản thật. Chỉ ghi file, KHÔNG sửa kịch bản (L4: cần người dùng duyệt).
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
EP = ROOT / "02_SAN_XUAT" / "Tap06"

data = json.loads((ROOT / ".work/script_tap06.json").read_text(encoding="utf-8-sig"))
S = {s["id"]: s["text"] for el in data if el.get("kind") == "LOI"
     for s in el.get("sentences", [])}

# (mã câu, câu đề xuất, nguồn, ghi chú)
CAU = [
    ("1.08#1",
     "Mức lương năm đô la một giờ vào năm 1978 cao gần gấp đôi mức lương tối thiểu ở bang Illinois lúc bấy giờ.",
     "[1] Wikipedia · [15] Oxygen",
     "Wikipedia: 'almost double the pay Piest earned at the pharmacy'. Báo chí: 'gấp đôi mức lương tối thiểu 2,50 USD' — "
     "đó là mức tối thiểu của **bang Illinois**; mức **liên bang** năm 1978 là 2,35 USD. Câu hiện tại gộp cả hai."),
    ("2.06#3",
     "Đó là một chiếc còng tay kim loại và nhiều chiếc phù hiệu cảnh sát.",
     "[1] Wikipedia",
     "Wikipedia: 'several police badges, a starting pistol, a syringe and hypodermic needle, handcuffs'. "
     "Không có nguồn nào nói phù hiệu là **giả**, và là **nhiều** chiếc chứ không phải một."),
    ("2.11#2",
     "Thậm chí vào những đêm đông lạnh giá, hắn thản nhiên dừng xe lại và mời các sĩ quan ăn tối cùng hắn.",
     "[1] Wikipedia · [14] Esquire · [15] Oxygen · [16] TheWrap",
     "Nguồn xác nhận: mời Albrecht và Hachmeister đến nhà hàng ăn tối ('invited them to a restaurant for a meal'), "
     "mời vào nhà ấm, mua bia cho họ. **Không** có nguồn nào nói 'nhà hàng ăn nhanh' hay 'gõ cửa kính xe'."),
    ("2.11#3",
     "Hắn hào phóng mua bia cho họ và nở nụ cười rạng rỡ như thể đang tiếp đãi bạn bè.",
     "[14] Esquire · [15] Oxygen · [16] TheWrap",
     "Oxygen: 'Gacy bought them beers'. **Không** có nguồn nói Gacy trả tiền bữa ăn cho họ."),
    ("3.06#1",
     "Bên dưới ngôi nhà không có tầng hầm bê tông, mà chỉ là một khoảng không gian bò chật hẹp cao chưa đầy nửa mét, "
     "chạy dọc theo toàn bộ diện tích sàn nhà.",
     "[1] Wikipedia · [13] Witnesses from the Grave",
     "Sách (theo hồ sơ cảnh sát): 'a muddy **eighteen-inch-high** crawl space' ≈ 46 cm. Câu 'cao chưa đầy một mét' "
     "không sai nhưng thô; 'chưa đầy nửa mét' khớp nguồn."),
    ("3.11#1",
     "Một chiến dịch khai quật khổng lồ lập tức được triển khai khẩn cấp.",
     "[3] Chicago Tribune · [13] Witnesses from the Grave",
     "Không nguồn nào xác nhận khẳng định siêu nhân 'lớn chưa từng thấy trong lịch sử bang Illinois'. "
     "Nguồn chỉ xác nhận quy mô khai quật và việc phải tháo sàn nhà để đào."),
    ("5.02#3",
     "Hắn vẽ hơn hai nghìn bức tranh sơn dầu mô tả hình ảnh Chú hề Pogo với khóe miệng nhọn hoắt đầy ma quái "
     "rồi tìm cách bán chúng ra bên ngoài.",
     "[1] Wikipedia · [2] Clark County SA · [9] Biography.com · [11] Slate",
     "Clark County SA: 'more than **2,000** oil paintings'. Wikipedia: 'approximately **2,500** paintings'. "
     "Câu 'hàng trăm bức' thấp hơn thực tế."),
]

# (shot, chữ trên hình hiện tại, chữ đề xuất, lý do)
CAPTION = [
    ("1-12", "Cao gần gấp đôi mức lương tối thiểu **liên bang** năm 1978",
     "Cao gần gấp đôi mức lương tối thiểu **ở bang Illinois** năm 1978",
     "Đồng bộ với câu 1.08#1."),
    ("2-06", "**CÒNG TAY KIM LOẠI & PHÙ HIỆU GIẢ**",
     "**CÒNG TAY KIM LOẠI & NHIỀU PHÙ HIỆU**",
     "Đồng bộ với câu 2.06#3. Nền `t6_handcuffs_fake_badge` giữ nguyên (hình vẽ, không phải dữ kiện)."),
    ("2-14", "**MỜI CÀ PHÊ VÀ TRẢ TIỀN BỮA ĂN**",
     "**MỜI CẢNH SÁT ĂN TỐI CÙNG**",
     "Bỏ 'cà phê' và 'trả tiền' — không có nguồn."),
    ("3-04", "Cao chưa đầy **một mét**",
     "Cao chưa đầy **nửa mét**",
     "Đồng bộ với câu 3.06#1 (18 inch ≈ 46 cm)."),
    ("3-08", "Quy mô lớn **chưa từng thấy** trong lịch sử Illinois",
     "Quy mô **khổng lồ** với ngôi nhà bị xé từng lớp",
     "Bỏ khẳng định siêu nhân không có nguồn."),
    ("2-15", "**RÚT TIỀN MẶT CHUẨN BỊ BỎ TRỐN**",
     "**NGÀY CÀNG MẤT BÌNH TĨNH**",
     "LỖI MỚI: không nguồn nào xác nhận Gacy rút tiền mặt chuẩn bị bỏ trốn; câu 2.11#5–#6 chỉ nói "
     "'các thám tử nhận thấy Gacy ngày càng mất bình tĩnh'."),
    ("3-03", "**NẮP HẦM KỸ THUẬT PHÒNG NGỦ**",
     "**NẮP HẦM KỸ THUẬT TRONG TỦ**",
     "LỖI MỚI: Witnesses from the Grave — 'lowered himself through a trap door in a **closet** inside Gacy's house'. "
     "Nắp hầm ở tủ quần áo, không phải phòng ngủ."),
    ("5-01", "**14 NĂM TẠI KHU BIỆT GIAM TỬ TÙ**",
     "**14 NĂM TRÊN HÀNG CHỜ TỬ HÌNH**",
     "Nguồn viết 'on death row' (hàng chờ tử hình), không khẳng định 'khu biệt giam'."),
    ("5-07", "**BÀI HỌC KINH ĐIỂN TẠI HỌC VIỆN FBI**",
     "**BÀI HỌC KINH ĐIỂN TRONG NGHIÊN CỨU TỘI PHẠM**",
     "LỖI MỚI: không nguồn nào trong 20 nguồn đã kiểm chứng nhắc 'FBI Academy'; câu 5.06#2 chỉ nói "
     "'nhiều trung tâm nghiên cứu tội phạm'."),
    ("2-08", "*Lời ngụy biện mua từ tiệm cầm đồ*",
     "*Lời giải thích qua loa không đáng tin*",
     "Cần kiểm: câu 2.07#4 chỉ nói 'một lời giải thích qua loa', không nói 'tiệm cầm đồ'; "
     "chưa tìm được câu này trong 20 nguồn đã kiểm chứng."),
    ("1-05", "*Vận hành suốt gần một thập kỷ giữa khu dân cư*",
     "*Các vụ giết kéo dài từ năm 1972 đến 1978*",
     "Nguồn: 'convicted of murdering 33 young men and boys between **1972 and 1978**' (Oxygen), "
     "'committed his first murder in **1972**' (Biography.com) ⇒ 6 năm, không phải 'gần một thập kỷ'."),
]

TTS = {"1.08#1": "s1_08_01", "2.06#3": "s2_06_03", "2.11#2": "s2_11_02",
       "2.11#3": "s2_11_03", "3.06#1": "s3_06_01", "3.11#1": "s3_11_01",
       "5.02#3": "s5_02_03"}

L = ["# ĐỀ XUẤT SỬA — TẬP 06 (7 câu + 11 chữ trên hình) · 03/11/2026",
     "",
     "> **Trạng thái: CHỜ DUYỆT — CHƯA ÁP DỤNG.** Kịch bản và video hiện tại **giữ nguyên**.",
     "> Lý do chưa áp dụng: sửa câu = phải tạo lại file TTS, mà **engine Higgs Audio v3 chỉ chạy được trên Kaggle GPU** — ",
     "> máy này không có GPU / kaggle CLI / kaggle.json / torch / mlx_audio. Chi tiết ở `BaoCao_QC_Tap06_20261102.md` §6.",
     "",
     "Mỗi mục ghi: **câu hiện tại** (trích tự động từ `.work/script_tap06.json`) → **đề xuất** → **nguồn**. ",
     "Câu trích tự động ⇒ không thể lệch với kịch bản thật.",
     "",
     "---",
     "",
     "## A. Sửa câu trong kịch bản (7 câu)",
     ""]
for sid, new, src, note in CAU:
    cur = S.get(sid, "!! KHÔNG TỒN TẠI !!")
    L += [f"### `{sid}`",
          "",
          f"**Hiện tại:** {cur}",
          "",
          f"**Đề xuất:** {new}",
          "",
          f"**Nguồn:** {src}",
          "",
          f"**Vì sao:** {note}",
          "",
          f"**File TTS phải tạo lại:** `.work/audio_s_higgs_t06/{TTS[sid]}.wav`",
          ""]
L += ["---", "",
      "## B. Sửa chữ trên hình (bảng shot mục 6 của hồ sơ tập)",
      "",
      "Các chữ này **lặp lại** nội dung sai đã nêu ở nhóm A, hoặc khẳng định điều không có nguồn. ",
      "Sửa chữ trên hình **không đổi câu** ⇒ không cần TTS, chỉ cần render lại ảnh tĩnh của shot đó.",
      "",
      "| Shot | Chữ hiện tại | Chữ đề xuất | Vì sao |",
      "|---|---|---|---|"]
for sid, cur, new, why in CAPTION:
    L.append(f"| `{sid}` | {cur} | {new} | {why} |")
L += ["", "---", "",
      "## C. Nếu được duyệt — quy trình thực thi",
      "",
      "**Bước 1 — Tạo lại TTS (BẮT BUỘC, cần Kaggle GPU).** "
      "7 file trong `.work/audio_s_higgs_t06/`: " + ", ".join(f"`{v}.wav`" for v in TTS.values()) + ".",
      "",
      "- Kernel: `.work/higgs_prod_t06_kaggle.ipynb` (kernel `amber-eyes-higgs-prod-t06-kaggle-gpu`).",
      "- Cần: `kaggle` CLI + `~/.kaggle/kaggle.json` + dataset `amber-eyes-voice-ref-voxcpm2`.",
      "- Payload: `.work/kaggle_higgs/higgs_payload_t06.json` — phải cập nhật 7 câu trước khi push.",
      "- Quy tắc: `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` §7 (seed tất định, `max_new_tokens`, đo lại F0/G9, "
      "kiểm tra đuôi đuôi đọc bằng đôi mắt + ASR trước khi ghép master).",
      "",
      "**Bước 2 — Sửa kịch bản** `01_KICH_BAN/Tap06/kichban_tap06_23102026.md` (7 câu ở nhóm A) "
      "rồi sinh lại `.work/script_tap06.json`.",
      "",
      "**Bước 3 — Sửa bảng shot** (nhóm B) trong `02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md` mục 6.",
      "",
      "**Bước 4 — Dựng lại:** `parse_shots.py` → `build_audio3.py` → `subtitles.py` → "
      "`build_video3.py --stills all` (soi mắt) → `build_video3.py --workers 6` (~28 phút) → "
      "`package.py --mux` → QC `qc_video_t04.py --ep 06` + đo lag A/V.",
      "",
      "**Bước 5 — Hồ sơ:** cập nhật `BaoCao_QC_Tap06_20261102.md`, `KeHoach_Video_Tap06.md`, "
      "`00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (A11), `provenance.json`, `README.md`.",
      "",
      "**Bước 6 — Hồi quy Tập 01 (L9):** `AE_EP=01 parse_shots.py` ⇒ `.work/shots.json` không đổi một byte.",
      "",
      "---", "",
      "## D. Nguồn (20 nguồn, mọi URL đã kiểm chứng HTTP 200 ngày 02/11/2026)",
      "",
      "| # | Nguồn |",
      "|---|---|"]
srcs = [
    ("1", "Wikipedia — John Wayne Gacy"), ("2", "Clark County State's Attorney (IL) — hồ sơ Gacy #237"),
    ("3", "Chicago Tribune — dòng thời gian vụ án"),
    ("4", "Chicago Tribune — 40 năm sau, danh sách nạn nhân"),
    ("5", "A&E — xét xử vụ Gacy"), ("6", "A&E — vụ bắt giữ và khám xét nhà"),
    ("7", "A&E — Case File: John Wayne Gacy"), ("8", "Encyclopedia.com — hồ sơ xét xử 1980"),
    ("9", "Biography.com — John Wayne Gacy"), ("10", "Netflix Tudum — hồ sơ loạt phim tài liệu"),
    ("11", "Slate — đánh giá 'Devil in Disguise'"), ("12", "Solve The Case — hồ sơ nghi phạm"),
    ("13", "Joyce & Stover — 'Witnesses from the Grave' (sách)"),
    ("14", "Esquire — phỏng vấn cựu thám tử Albrecht"),
    ("15", "Oxygen — cách Gacy bị phát hiện"), ("16", "TheWrap — lời khai thám tử Des Plaines"),
    ("17", "NBC News — docuseries và các nạn nhân"), ("18", "LegalNews (AP) — 'Defending a Monster'"),
    ("19", "Chicago Bar Association — bản vụ của William Kunkle"),
    ("20", "Den of Geek — đánh giá 'Devil in Disguise'"),
]
for k, n in srcs:
    L.append(f"| {k} | {n} |")
L.append("")
L.append("Bảng đối chiếu đầy đủ 58 mốc: `02_SAN_XUAT/Tap06/nguon_tham_khao.md`.")

out = "\n".join(L) + "\n"
if "\x00" in out:
    raise SystemExit("CHẶN — byte NUL")
(EP / "DeXuat_Sua_Tap06.md").write_text(out, encoding="utf-8")
print(f"OK  DeXuat_Sua_Tap06.md: {len(out)} ký tự · {len(CAU)} câu · {len(CAPTION)} caption")
miss = [c[0] for c in CAU if c[0] not in S]
if miss:
    raise SystemExit("CHẶN — mã câu không tồn tại: " + ", ".join(miss))
print("OK  cả 7 mã câu tồn tại trong script_tap06.json")
