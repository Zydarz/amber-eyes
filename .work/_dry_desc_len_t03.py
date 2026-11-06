#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap03 VN — kiểm mô tả YouTube KHÔNG ghi file (A12 + T15): mã câu hợp lệ, link giữ nguyên, <= 5000 ký tự."""
import json
import os
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
os.environ.setdefault("AE_EP", "03")
os.environ.setdefault("AE_LANG", "vi")
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402
import package as PK  # noqa: E402

TL = PK.TL
sents = {i["id"]: i["text"] for i in TL["items"]}

# ---- A12: mọi mã câu trong summary / need phải tồn tại
sum_vn = ED.EP.get("summary_vn", "")
ids_in_sum = re.findall(r"`(\d\.\d+#\d+)`", sum_vn)
missing_sum = [k for k in ids_in_sum if k not in sents]
need = ED.EP.get("need", [])
missing_need = [k for k in need if k not in sents]
print(f"[A12] summary_vn: {len(ids_in_sum)} mã câu · thiếu {len(missing_sum)} {missing_sum[:6]}")
print(f"[A12] need      : {len(need)} mã câu · thiếu {len(missing_need)} {missing_need[:6]}")

# ---- T15: độ dài mô tả + số link
blk, tbl = PK.sources_vn()
act_titles = ED.EP["act_titles"]
starts = PK.act_start_times(TL)
chap = ["00:00 Intro"] + [f"{PK.mmss(starts[a])} {act_titles[a]}" for a in sorted(starts)]
summary = ED.EP.get("summary_vn") or " ".join(sents.get(k, "") for k in ED.EP["summary"] if sents.get(k))
roles_line = ED.EP.get("roles_line", "")
credit = ED.EP.get("voice_credit", "")
credit_line = ("\n" + credit) if credit else ""
hashtags = ED.EP.get("hashtags", "")
tag_line = ("\n\n" + hashtags) if hashtags else ""
txt = f"""{PK.with_brand(ED.EP["title"])}

{summary}

⏱ MỐC CHƯƠNG
{chr(10).join(chap)}

⚠️ LƯU Ý
• Nội dung không phù hợp cho trẻ em.
• Nội dung mang tính giáo dục, phân tích dưới góc nhìn tâm lý học tội phạm;
  không thay thế tư vấn y tế, tâm lý hay pháp lý.
• Thông tin dựa trên tư liệu công khai (hồ sơ tòa án, báo chí) — xem nguồn bên dưới.
  Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là nhân vật minh hoạ, không phải người thật.
  {roles_line}
• Giọng đọc, hình ảnh và âm nhạch được tạo cho kênh bằng công cụ AI.{credit_line}

📚 NGUỒN THAM KHẢO
{blk}

🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia
bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).{tag_line}
"""
n = len(txt)
links = re.findall(r"https?://\S+", txt)
src_links = re.findall(r"https?://\S+", (ROOT / "02_SAN_XUAT/Tap03/nguon_tham_khao.md").read_text(encoding="utf-8"))
ok_links = len(re.findall(r"✅", (ROOT / "02_SAN_XUAT/Tap03/nguon_tham_khao.md").read_text(encoding="utf-8")))
print(f"[T15] độ dài mô tả = {n} ký tự (giới hạn YouTube 5000) -> "
      f"{'ĐẠT' if n <= 5000 else 'VƯỢT'}")
print(f"[T15] link trong mô tả = {len(links)} · link trong bảng nguồn = {len(src_links)} "
      f"· dòng ✅ = {ok_links}")
print(f"[T15] có '[PENDING]' / '[CHUA CO' không: "
      f"{('[PENDING' in txt) or ('[CHUA CO' in txt)}")
print(f"[T15] mốc chương: {chap}")
for a in sorted(starts):
    print(f"      Hồi {a}: timeline {starts[a]:.2f}s -> {PK.mmss(starts[a])}")
print(f"[T10] hashtags có trong mô tả: {bool(hashtags)}")
print(f"[H12] thumbnail bg = {ED.EP.get('thumb_bg')} | thumb lines = {ED.EP.get('thumb')}")
