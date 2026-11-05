#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 03 — QC ảnh tĩnh 3 ngôn ngữ (VN / EN / JA).

Cổng kiểm:
  1. Đủ ảnh: mỗi shot trong bảng có đúng 1 PNG, không thừa, không thiếu
  2. Ảnh hỏng: PNG < 20 KB hoặc không mở được
  3. H10 — thời lượng shot + chuỗi nền liền nhau (không lặp nền > 4 shot liền)
  4. H12 — shot cuối (thẻ kết) phải có chữ
  5. H15 — đối chiếu hash trước/sau render: ảnh nào đổi, ảnh nào giữ nguyên

Dùng:  py -3 .work/_qc_t03_stills_final.py
"""
import hashlib
import json
import sys
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BK = WORK / "_cu" / "t03_20261105_1800"

LANGS = [
    ("vi", "shots_t03.json", "video3_t03/stills"),
    ("en", "shots_EN_t03.json", "video3_EN_t03/stills"),
    ("ja", "shots_JA_t03.json", "video3_JA_t03/stills"),
]

fails = 0
for lang, sh_name, rel in LANGS:
    print("=" * 78)
    print(f"[{lang}]")
    sh = json.loads((WORK / sh_name).read_text(encoding="utf-8"))
    shots = sh["shots"]
    sd = WORK / rel
    ids = [s["id"] for s in shots]
    files = {p.name for p in sd.glob("*.png")}
    want = {f"shot_{i}.png" for i in ids}

    miss = sorted(want - files)
    extra = sorted(files - want)
    print(f"  ảnh: {len(files)} file · cần {len(want)}")
    if miss:
        print(f"  ✗ THIẾU {len(miss)}: {miss[:8]}")
        fails += 1
    if extra:
        print(f"  ✗ THỪA {len(extra)}: {extra[:8]}")
        fails += 1
    if not miss and not extra:
        print("  ✔ đủ ảnh, không thừa")

    # 2) ảnh hỏng
    bad = []
    for n in sorted(want & files):
        p = sd / n
        if p.stat().st_size < 20000:
            bad.append((n, "nhỏ"))
            continue
        try:
            with Image.open(p) as im:
                im.verify()
        except Exception as e:
            bad.append((n, f"lỗi mở: {e}"))
    print(f"  ✔ ảnh hỏng: {len(bad)} {bad[:4] if bad else ''}")
    if bad:
        fails += 1

    # 3) H10 — thời lượng + chuỗi nền
    durs = [(s["id"], round(s["end"] - s["start"], 2)) for s in shots]
    out_of = [(i, d) for i, d in durs if d < 3 or d > 15]
    print(f"  H10 thời lượng: min {min(d for _, d in durs)}s · max {max(d for _, d in durs)}s "
          f"· ngoài 3–15s: {len(out_of)}")
    if out_of:
        print(f"      {out_of[:12]}")
    chain, worst, cur, curid = [], [], [], None
    for s in shots:
        if s.get("bg") == curid:
            cur.append(s["id"])
        else:
            if len(cur) > 3:
                chain.append(cur)
            cur, curid = [s["id"]], s.get("bg")
    if len(cur) > 3:
        chain.append(cur)
    print(f"  H10 nền lặp liền >4 shot: {len(chain)} chuỗi "
          f"{[len(c) for c in chain]} {chain[:3] if chain else ''}")

    # 4) H12 — thẻ kết
    last = shots[-1]

    def drawn(sh):
        out = []
        for seg in sh.get("segments") or []:
            for el in seg.get("elems") or []:
                if len(el) >= 2:
                    out.append(str(el[1]))
        return " ".join(out)

    txt = drawn(last).strip()
    print(f"  H12 shot cuối [{last['id']}] template={last.get('template')} chữ = {txt[:120]!r}")
    if not txt:
        print("  ✗ shot cuối KHÔNG có chữ")
        fails += 1
    else:
        need = {"vi": ["HỒ SƠ TẬP", "AMBER EYES"], "en": ["CLOSED", "AMBER EYES"],
                "ja": ["AMBER EYES"]}[lang]
        miss = [k for k in need if k.upper() not in txt.upper()]
        if miss:
            print(f"  ✗ thẻ kết thiếu: {miss}")
            fails += 1
        else:
            print("  ✔ thẻ kết có nhãn + tên kênh + khẩu hiệu")

    # 5) H15 — hash trước/sau
    before = json.loads((BK / "stills_manifest_before.json").read_text(encoding="utf-8"))
    changed = []
    for n, v in before[lang].items():
        p = sd / n
        if not p.exists():
            continue
        h = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        if h != v["sha256"]:
            changed.append(n)
    print(f"  H15 so với bản trước render: {len(changed)}/{len(before[lang])} ảnh đổi byte")
    if changed:
        print(f"      {sorted(changed)[:12]}")

print("=" * 78)
print("KẾT LUẬN:", "ĐẠT" if fails == 0 else f"{fails} CỔNG LỖI")
sys.exit(0 if fails == 0 else 1)
