#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So sánh kịch bản Tap05 MỚI (đã commit 5a3e2ba) với bản đã parse trước đó.

Câu hỏi: bảng shot / timeline cũ còn khớp với kịch bản mới không?
Đo: số element, số câu, các mã câu `X.YY#N` có còn tồn tại không.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

CASES = [
    ("VN", ROOT / "01_KICH_BAN/Tap05/kichban_tap05_23102026.md",
     WORK / "script_tap05.json", WORK / "shots_t05.json",
     ROOT / "02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md"),
    ("EN", ROOT / "01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md",
     WORK / "script_tap05_EN.json", WORK / "shots_EN_t05.json",
     ROOT / "02_SAN_XUAT/Tap05_EN/KeHoach_Video_Tap05_EN.md"),
    ("JA", ROOT / "01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md",
     WORK / "script_tap05_JA.json", WORK / "shots_JA_t05.json",
     ROOT / "02_SAN_XUAT/Tap05_JA/KeHoach_Video_Tap05_JA.md"),
]

sys.path.insert(0, str(WORK))
import parse_kichban as PK  # noqa: E402


def load(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def ids_of(els):
    out = set()
    for e in els:
        for s in e.get("sentences", []):
            out.add(s["id"])
    return out


for lang, src, old_json, shots_json, plan in CASES:
    print("=" * 78)
    print(f"### {lang}")
    if not src.exists():
        print("  !! không có kịch bản:", src)
        continue
    new = PK.parse_file(str(src))
    old = load(old_json) if old_json.exists() else []
    n_ids, o_ids = ids_of(new), ids_of(old)
    print(f"  kịch bản : {src.relative_to(ROOT)}")
    print(f"  element  : cũ {len(old):>4}  →  mới {len(new):>4}")
    print(f"  câu      : cũ {len(o_ids):>4}  →  mới {len(n_ids):>4}")
    lost = o_ids - n_ids
    add = n_ids - o_ids
    print(f"  mã câu mất  : {len(lost):>4}  {sorted(lost)[:8]}{'…' if len(lost) > 8 else ''}")
    print(f"  mã câu thêm : {len(add):>4}  {sorted(add)[:8]}{'…' if len(add) > 8 else ''}")
    # role counts
    def roles(els):
        d = {}
        for e in els:
            if e["kind"] == "LOI":
                d[e["role"]] = d.get(e["role"], 0) + len(e.get("sentences", []))
        return d
    print(f"  câu theo vai  cũ {roles(old)}")
    print(f"  câu theo vai  mới {roles(new)}")

    # bảng shot: mã câu có còn tồn tại trong kịch bản mới?
    if plan.exists():
        txt = plan.read_text(encoding="utf-8")
        m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", txt, re.M)
        sec = txt[m.end():] if m else ""
        mt = re.search(r"^\*\*Tổng:", sec, re.M)
        if mt:
            sec = sec[: mt.start()]
        rows = [l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]
        used = set()
        for l in rows:
            for mm, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", l):
                for k in range(int(a), int(b or a) + 1):
                    used.add(f"{mm}#{k}")
        bad = sorted(u for u in used if u not in n_ids)
        print(f"  bảng shot: {len(rows)} dòng · dùng {len(used)} mã câu · MẤT KHỎI KỊCH BẢN MỚI: {len(bad)}")
        if bad:
            print(f"      {bad[:14]}{'…' if len(bad) > 14 else ''}")
        sh = load(shots_json) if shots_json.exists() else None
        if sh:
            sids = [s["id"] for s in sh["shots"]]
            print(f"  shots.json: {len(sids)} shot · ID trùng: "
                  f"{len(sids) - len(set(sids))} · total={sh.get('total')}")
