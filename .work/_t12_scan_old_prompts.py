# -*- coding: utf-8 -*-
"""Tập 12 — quét prompt 83 nền CŨ (13/11) để tìm prompt YÊU CẦU CHỮ.

Nguyên nhân gốc (A11 #171): vật thể mang chữ trong prompt ⇒ AI vẽ chữ.
Danh sách này là "nghi" — kết luận phải soi ảnh.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
ALL = json.loads((ROOT / ".work/bg_jobs_tap12_v2.json").read_text(encoding="utf-8"))
NEW = {j["name"] for j in
       json.loads((ROOT / ".work/bg_jobs_tap12_new69.json").read_text(encoding="utf-8"))}

PAT = re.compile(
    r"\bprinted\b|\bflyers?\b|\bnewspaper|\bheadline|\bclipping|\bclippings|\bsigns?\b|"
    r"\bplaques?\b|\bbadges?\b|\bemblem|\binsignia|\blabels?\b|\blabelled\b|\blabeled\b|"
    r"\bmarked\b|\breports?\b|\bwriting\b|\bwritten\b|\binscribed\b|\bengraved\b|"
    r"\bposter|\bbulletin\b|\bcaption|\btyped\b|\btypewriter\b|\bgalleys\b|"
    r"\bnotes?\b|\bnotebooks?\b|\bpassbooks?\b|\bdeeds?\b|\benvelopes?\b|"
    r"\btelegrams?\b|\bappeals?\b|\bmonolith\b|\bnames\b|\bcards?\b|"
    r"\bvolts\b|\bdegrees\b|\baxis\b|\bgraph of\b|\bgraph showing\b|\bledger\b|"
    r"\bdossier\b|\bfile folder\b|\bseal\b|\bsignature\b|\bsigned\b|\bstamp\b|"
    r"\bmap of\b|\bnumber\b|\bnumbered\b",
    re.I)

old = [j for j in ALL if j["name"] not in NEW]
flag = [j for j in old if PAT.search(j["prompt"])]
print(f"nen cu: {len(old)} · prompt co dau yeu cau chu: {len(flag)} "
      f"({len(flag)/len(old)*100:.1f} %)")
out = ROOT / ".work/_t12/old83_textprompts.md"
lines = ["# Tập 12 — 83 nền cũ (13/11) có prompt YÊU CẦU CHỮ",
         "", f"Quét từ khoá: {len(flag)}/{len(old)} nền.", ""]
for j in sorted(flag, key=lambda x: x["name"]):
    hit = sorted(set(m.group(0).lower() for m in PAT.finditer(j["prompt"])))
    lines.append(f"- `{j['name']}` — {', '.join(hit)}")
out.write_text("\n".join(lines), encoding="utf-8")
print(f"-> {out}")
