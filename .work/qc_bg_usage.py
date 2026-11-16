# -*- coding: utf-8 -*-
"""Cổng H22 — dùng HẾT ảnh đã sinh, mỗi shot đúng ảnh của nó, nền phân bổ đều.

    AE_EP=10 [AE_LANG=en] py -3 .work/qc_bg_usage.py [--jobs .work/bg_jobs_tap10.json]
                                                     [--max-shots 3] [--max-sec 30]

Chạy sau parse_shots.py, TRƯỚC ảnh tĩnh. Exit 1 = TRƯỢT. Đo:
  ① ảnh sinh (job trong bg_jobs_tapXX.json) mà không shot nào dùng = 0
  ② shot không phải dòng "giữ" mà mượn nền shot trước (bg_inherited) = 0
  ③ shot trỏ nền chưa có file = 0
  ④ nền dùng > max-shots shot hoặc > max-sec giây trong tập = 0
Nền đặc biệt (void) không tính.

    AE_EP=11 py -3 .work/qc_bg_usage.py --plan      # TRƯỚC KHI SINH ẢNH (H25)
Đọc mục 6 "DANH SÁCH SHOT" trong 02_SAN_XUAT/TapXX/KeHoach_Video_TapXX.md: mã nền
`tXX_*` đầu tiên ở cột "Nền + bóng", thời lượng = tổng "(x,y s)" ở cột "Câu"; dòng
không có mã nền (giữ / camera dời) tính cho nền của shot trước. Đo ④ trên kế hoạch,
số nền tối thiểu, và lệch giữa kế hoạch ↔ bg_jobs (mã thiếu job / job không có shot).
"""
import re
import argparse
import collections
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import edition as ED  # noqa: E402

SPECIAL = {"void"}


def plan_check(a, jobs):
    md = ED.ROOT / "02_SAN_XUAT" / f"Tap{ED.EPN}" / f"KeHoach_Video_Tap{ED.EPN}.md"
    text = md.read_text(encoding="utf-8")
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
    sec = text[m.end():] if m else text
    used = collections.Counter()
    sec_ = collections.defaultdict(float)
    cur, nrow = None, 0
    for line in sec.splitlines():
        if not re.match(r"\|\s*[1-5]-\d+", line):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) < 5:
            continue
        nrow += 1
        code = re.search(r"`(t\d+_[a-z0-9_]+)`", c[4])
        if code:
            cur = code.group(1)
        if not cur:
            continue
        dur = sum(float(x.replace(",", ".")) for x in re.findall(r"\((\d+(?:,\d+)?) ?s\)", c[1]))
        used[cur] += 1
        sec_[cur] += dur
    gen = set()
    if jobs.exists():
        j = json.loads(jobs.read_text(encoding="utf-8"))
        j = j.get("jobs", j) if isinstance(j, dict) else j
        gen = {x["name"] for x in j if isinstance(x, dict) and x.get("name")}
    over = sorted(((b, used[b], sec_[b]) for b in used if used[b] > a.max_shots or sec_[b] > a.max_sec),
                  key=lambda x: -x[2])
    need = sum(max(math.ceil(used[b] / a.max_shots), math.ceil(sec_[b] / a.max_sec)) for b in used)
    no_job = sorted(set(used) - gen) if gen else []
    no_shot = sorted(gen - set(used))
    tot = sum(used.values())
    print(f"KẾ HOẠCH Tập {ED.EPN} · {nrow} dòng shot · {len(used)} mã nền · {tot / max(len(used), 1):.1f} shot/nền"
          f" · {sum(sec_.values()):.0f} s")
    print(f"  nền tối thiểu theo H22: {need} (thiếu {max(need - len(used), 0)}) · mức H25 1,5–2 shot/nền:"
          f" {math.ceil(tot / 2)}–{math.ceil(tot / 1.5)}")
    if sum(sec_.values()) < 3 * nrow:
        print(f"  CẢNH BÁO: cột Câu thiếu \"(x,y s)\" ({sum(sec_.values()):.0f} s / {nrow} shot) ⇒ "
              "KHÔNG đo được giới hạn 30 s — bổ sung thời lượng vào bảng shot hoặc đo lại sau parse_shots.py")
    print(f"  ④ nền vượt {a.max_shots} shot/{a.max_sec:g} s : {len(over)}")
    for b, k, t in over[:15]:
        print(f"       {b}: {k} shot · {t:.0f} s")
    print(f"  mã nền chưa có job   : {len(no_job)}", no_job[:10])
    print(f"  job không shot nào dùng: {len(no_shot)}", no_shot[:10])
    fail = len(over) + len(no_job) + len(no_shot)
    print("KẾT QUẢ:", "ĐẠT" if not fail else "TRƯỢT")
    sys.exit(1 if fail else 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--jobs", default=None)
    ap.add_argument("--max-shots", type=int, default=3)
    ap.add_argument("--max-sec", type=float, default=30.0)
    ap.add_argument("--plan", action="store_true", help="đo trên bảng shot của KeHoach (trước khi sinh ảnh)")
    a = ap.parse_args()
    jobs = Path(a.jobs) if a.jobs else ED.WORK / f"bg_jobs_tap{ED.EPN}.json"
    if a.plan:
        plan_check(a, jobs)
    shots = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))["shots"]
    bg_dir = ED.ROOT / "assets" / "bg"

    gen = set()
    if jobs.exists():
        j = json.loads(jobs.read_text(encoding="utf-8"))
        j = j.get("jobs", j) if isinstance(j, dict) else j
        gen = {x["name"] for x in j if isinstance(x, dict) and x.get("name")}
    else:
        print(f"CẢNH BÁO: không thấy {jobs.name} — bỏ qua ① (không biết danh sách ảnh đã sinh)")

    used = collections.Counter()
    sec = collections.defaultdict(float)
    for s in shots:
        if s["bg"] in SPECIAL:
            continue
        used[s["bg"]] += 1
        sec[s["bg"]] += s["end"] - s["start"]

    unused = sorted(gen - set(used))
    borrowed = [s["id"] for s in shots if s.get("bg_inherited") and not s.get("hold")]
    missing = sorted(b for b in used if not (bg_dir / f"{b}.png").exists())
    over = sorted(((b, used[b], sec[b]) for b in used if used[b] > a.max_shots or sec[b] > a.max_sec),
                  key=lambda x: -x[2])

    n = len([s for s in shots if s["bg"] not in SPECIAL])
    print(f"Tập {ED.EPN} · {ED.LANG} · {len(shots)} shot · {len(used)} nền dùng · {len(gen)} ảnh sinh"
          f" · {n / max(len(used), 1):.1f} shot/nền")
    print(f"  ① ảnh sinh không dùng : {len(unused)}", unused[:10])
    print(f"  ② shot mượn nền       : {len(borrowed)}", borrowed[:10])
    print(f"  ③ nền chưa có file    : {len(missing)}", missing[:10])
    print(f"  ④ nền vượt {a.max_shots} shot/{a.max_sec:g} s : {len(over)}")
    for b, k, t in over[:15]:
        print(f"       {b}: {k} shot · {t:.0f} s")
    fail = len(unused) + len(borrowed) + len(missing) + len(over)
    print("KẾT QUẢ:", "ĐẠT" if not fail else "TRƯỢT")
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
