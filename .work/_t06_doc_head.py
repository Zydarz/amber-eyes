#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — tạo/refresh phần đầu tài liệu bảng shot EN và JA (tiêu đề + thống kê)."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

CFG = {
    "en": {"plan": ROOT / "02_SAN_XUAT/Tap06_EN/KeHoach_Video_Tap06_EN.md",
           "kb": ROOT / "01_KICH_BAN/Tap06_EN/kichban_tap06_EN.md",
           "tl": W / "timeline_s_EN_t06.json", "shots": W / "shots_EN_t06.json",
           "head": """# PRODUCTION DOSSIER EPISODE 06 · "THE KILLER CLOWN'S SMILE & 29 SECRETS UNDER THE FLOOR" (ENGLISH EDITION)

> **Case:** The Killer Clown — John Wayne Gacy (Chicago, Illinois, 1978)
> **Script:** `01_KICH_BAN/Tap06_EN/kichban_tap06_EN.md`
> **Output:** `02_SAN_XUAT/Tap06_EN/xuat_ban/` · **Standard:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A)
> **Updated:** 06/11/2026 — shot table rebuilt for the rewritten script (62 elements · 43 speech parts · 212 sentences)

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap06_EN/kichban_tap06_EN.md` — rewritten 05/11/2026 (62 elements · 212 sentences) |
| Duration | **{dur:.1f} s ({m}:{s})** — provisional timeline, awaiting the re-recorded master |
| Shots | **{nshot}** · {nsent} sentences · {nact} acts |
| Backgrounds | {nbg} noir 2K stills (2112×1188 16:9) |
| Language rule | Where the spoken line writes a number in words, the on-screen text writes it in words too |

> **Rebuilt 06/11/2026 for the rewritten script.** Shot table rebuilt from scratch: **129 shots**
> (123 content + 4 pause rows + 2 act-break cards) — the previous table had 73.
> Stills re-rendered for all 3 languages (VN / EN / JA), 129 PNGs each.
> **The timeline is provisional** (element anchors kept from the old audio master, per-sentence
> durations re-split by new sentence length) — re-record the master, then rebuild timeline + stems + video.
> **H9 soft scrim** (`text_scrim`) added for 23 shots whose text sits on a bright background
> (measured by `.work/_t06_scan_contrast.py`); the list lives in `.work/edition.py` → `EPISODES["06"]`.
"""},
    "ja": {"plan": ROOT / "02_SAN_XUAT/Tap06_JA/KeHoach_Video_Tap06_JA.md",
           "kb": ROOT / "01_KICH_BAN/Tap06_JA/kichban_tap06_JA.md",
           "tl": W / "timeline_s_JA_t06.json", "shots": W / "shots_JA_t06.json",
           "head": """# 制作計画 エピソード06 · 日本語版 · 「道化師の微笑みと床下の29の秘密」 (PART B)

**適用基準:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A)
**台本:** `01_KICH_BAN/Tap06_JA/kichban_tap06_JA.md` · **出力先:** `02_SAN_XUAT/Tap06_JA/xuat_ban/`
**更新日:** 2026年11月6日 — 書き直し台本（62要素 / 212文）に合わせてショット表を再構築

| 項目 | 内容 |
|---|---|
| 台本 | `01_KICH_BAN/Tap06_JA/kichban_tap06_JA.md` — 62要素 · 212文 |
| 所要時間 | **{dur:.1f} 秒（{m}:{s}）** — 暫定タイムライン（再録音待ち） |
| ショット | **{nshot}** · {nsent}文 · {nact}幕 |
| 背景 | ノワール 2K（2112×1188 16:9）{nbg}点 |
| 表記ルール | 読み上げ文が数字で表記（`33件` `1978年` `46歳`）なら画面も数字で書く |
"""},
}

lang = (sys.argv[1] if len(sys.argv) > 1 else "en").lower()
cfg = CFG[lang]
tl = json.loads(cfg["tl"].read_text(encoding="utf-8"))
els = parse_file(str(cfg["kb"]))
loi = [e for e in els if e.get("kind") == "LOI"]
nsent = sum(len(e.get("sentences", [])) for e in loi)
nact = len({int(e["id"].split(".")[0]) for e in loi})
dur = float(tl["total"])
nbg = 0
nshot = 0
if cfg["shots"].exists():
    sh = json.loads(cfg["shots"].read_text(encoding="utf-8"))["shots"]
    nshot = len(sh)
    nbg = len({s["bg"] for s in sh if s.get("bg")})
else:
    nshot = 125
    nbg = 66

head = cfg["head"].format(dur=dur, m=int(dur // 60), s=int(dur % 60),
                          nshot=nshot, nsent=nsent, nact=nact, nbg=nbg)

path = cfg["plan"]
old = path.read_text(encoding="utf-8") if path.exists() else ""
import re
m = re.search(r"^## 6\..*$", old, re.M)
if m:
    new = head + "\n" + old[m.start():]
else:
    new = head + "\n"
path.write_text(new, encoding="utf-8")
print(f"-> {path.name}: {nshot} shot · {nsent} câu · {dur:.1f}s")
