#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — QC tổng 3 ngôn ngữ (VN/EN/JA): bảng shot + ảnh tĩnh + đối chiếu chéo."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

LANG = {
    "vi": {"kb": ROOT / "01_KICH_BAN/Tap06/kichban_tap06_23102026.md",
           "tl": W / "timeline_s_t06.json", "sh": W / "shots_t06.json",
           "st": W / "video3_t06/stills", "plan": ROOT / "02_SAN_XUAT/Tap06/KeHoach_Video_Tap06.md"},
    "en": {"kb": ROOT / "01_KICH_BAN/Tap06_EN/kichban_tap06_EN.md",
           "tl": W / "timeline_s_EN_t06.json", "sh": W / "shots_EN_t06.json",
           "st": W / "video3_EN_t06/stills", "plan": ROOT / "02_SAN_XUAT/Tap06_EN/KeHoach_Video_Tap06_EN.md"},
    "ja": {"kb": ROOT / "01_KICH_BAN/Tap06_JA/kichban_tap06_JA.md",
           "tl": W / "timeline_s_JA_t06.json", "sh": W / "shots_JA_t06.json",
           "st": W / "video3_JA_t06/stills", "plan": ROOT / "02_SAN_XUAT/Tap06_JA/KeHoach_Video_Tap06_JA.md"},
}

FORBIDDEN = {
    "vi": ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập", "đầu độc",
           "diệt cỏ", "bỏ đói", "móc áo", "đồ lót", "quan hệ tình dục", "hiếp", "cưỡng ép"],
    "en": ["blood", "corpse", "strangle", "choke", "struggle", "raped", "rape",
           "underwear", "sexual intercourse", "orgasm", "penis", "vagina", "suffocat",
           "mutilat", "dismember", "torture"],
    "ja": ["血", "死体", "絞", "レイプ", "性交渉", "精通"],
}
SAFE = {
    "vi": ["ung thư máu", "đấu tập", "bàn tay", "cánh tay", "đầu tư", "đầu học",
           "đầu tiên", "đầu não", "trọng đầu", "bầu cửa", "bầu trời", "đập đầu", "trói buộc"],
    "en": ["blood type", "blood pressure", "blood vessel", "bloodstream", "blood cell",
           "struggle to survive", "struggled to"],
    "ja": [],
}
STRUCT_ANY = r"(HỒI|TẬP|NẤC|TẦNG|ACT|STAGE|LAYER|COMPARTMENT|EPISODE|CASE\s+FILE|第\s*\d+\s*幕)"

BG = {p.stem for p in (ROOT / "assets/bg").glob("*.png")}
ok = True
summary = {}

for lg, cfg in LANG.items():
    errs = []
    print(f"\n{'=' * 70}\n[{lg.upper()}]\n{'=' * 70}")
    if not cfg["sh"].exists() or not cfg["tl"].exists():
        print(f"  ✗ thiếu shots/timeline: {cfg['sh'].name}")
        ok = False
        continue
    sh = json.loads(cfg["sh"].read_text(encoding="utf-8"))["shots"]
    tl = json.loads(cfg["tl"].read_text(encoding="utf-8"))
    SENT = {it["id"]: it for it in tl["items"]}
    script = {}
    for e in parse_file(str(cfg["kb"])):
        if e.get("kind") == "LOI":
            for s in e.get("sentences", []):
                script[s["id"]] = s["text"]

    # 1. ID duy nhất
    ids = [s["id"] for s in sh]
    if len(set(ids)) != len(ids):
        errs.append(f"ID shot trùng: {[i for i in set(ids) if ids.count(i) > 1][:5]}")
    # 2. phủ câu + thứ tự
    order = [sid for s in sh for sid in s["sentences"]]
    expect = [sid for sid in script]
    if order != expect:
        errs.append(f"phủ/thứ tự lệch ({len(order)}/{len(expect)})")
    # 3. vai
    for s in sh:
        for sid in s["sentences"]:
            if s["role"] and SENT[sid]["role"] != s["role"]:
                errs.append(f"{s['id']}: vai {s['role']} ≠ {SENT[sid]['role']} ({sid})")
    # 4. nền
    miss_bg = sorted({s["bg"] for s in sh if s.get("bg")} - BG)
    if miss_bg:
        errs.append(f"nền thiếu file: {miss_bg}")
    # 5. chữ: trích dẫn / số / từ cấm
    q_bad = n_bad = f_bad = 0
    for s in sh:
        ctx = " ".join(SENT[x]["text"] for x in s["sentences"])
        if not ctx and (s["template"] == "T10" or not s.get("sentences")):
            ctx = " ".join(script.values())
        on = [(k, t) for seg in s["segments"] for k, t in seg["elems"]]
        for k, t in on:
            if k == "quote":
                core = t.strip().strip("“”\"")
                for frag in [f.strip() for f in core.split("…") if f.strip()]:
                    if frag not in ctx:
                        q_bad += 1
        flat = ctx.replace(" ", "")
        allowed = set(re.findall(r"\d+", flat))
        for a in list(allowed):
            allowed.add(a.zfill(2))
            allowed.add(str(int(a)))
        screen = " ".join(t for _k, t in on)
        for m in set(re.findall(r"\d[\d.,]*", screen)):
            if m in allowed or m in flat or m.replace(".", "") in allowed:
                continue
            if re.search(r"第\s*" + re.escape(m) + r"\s*[幕話]", screen):
                continue
            if re.search(STRUCT_ANY + r"\s*" + re.escape(m) + r"\b", screen):
                continue
            n_bad += 1
        low = screen.lower()
        for w in FORBIDDEN[lg]:
            if not re.search(r"(?<!\w)" + r"\s+".join(re.escape(x) for x in w.split()) + r"(?!\w)", low):
                continue
            if any(g in low for g in SAFE[lg] if g in w or w in g):
                continue
            f_bad += 1
    if q_bad:
        errs.append(f"trích dẫn không nguyên văn: {q_bad}")
    if n_bad:
        errs.append(f"số trên hình không có trong câu: {n_bad}")
    if f_bad:
        errs.append(f"từ cấm: {f_bad}")
    # 6. ảnh tĩnh
    pngs = {p.stem.replace("shot_", "") for p in cfg["st"].glob("*.png")} if cfg["st"].exists() else set()
    no_img = sorted(set(ids) - pngs)
    extra = sorted(pngs - set(ids))
    if no_img:
        errs.append(f"thiếu ảnh: {len(no_img)} ({no_img[:5]})")
    if extra:
        errs.append(f"ảnh thừa (stale): {len(extra)} ({extra[:5]})")
    # 7. bảng shot
    ptxt = cfg["plan"].read_text(encoding="utf-8") if cfg["plan"].exists() else ""
    rows = [l for l in ptxt.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]
    if len(rows) != len(ids):
        errs.append(f"bảng shot có {len(rows)} dòng, shots.json có {len(ids)}")

    print(f"  shot {len(ids)} · câu {len(order)}/{len(expect)} · ảnh {len(pngs)} · "
          f"timeline {tl['total']:.1f}s ({int(tl['total'] // 60)}:{int(tl['total'] % 60):02d})")
    print(f"  trích dẫn lỗi {q_bad} · số lỗi {n_bad} · từ cấm {f_bad} · "
          f"nền thiếu {len(miss_bg)} · ảnh thừa {len(extra)}")
    if errs:
        ok = False
        print("  ✗")
        for e in errs:
            print("   -", e)
    else:
        print("  ✓ tất cả cổng đạt")
    summary[lg] = {"ids": ids, "sent": order, "errs": errs}

# ---- đối chiếu chéo 3 ngôn ngữ ---------------------------------------------
if len(summary) == 3:
    print(f"\n{'=' * 70}\n[ĐỐI CHIẾU CHÉO 3 NGÔN NGỮ]\n{'=' * 70}")
    vi, en, ja = summary["vi"], summary["en"], summary["ja"]
    same_ids = vi["ids"] == en["ids"] == ja["ids"]
    print(f"  {'✓' if same_ids else '✗'} cùng bộ ID shot: {len(vi['ids'])} / {len(en['ids'])} / {len(ja['ids'])}")
    same_sent = vi["sent"] == en["sent"] == ja["sent"]
    print(f"  {'✓' if same_sent else '✗'} cùng thứ tự câu: {len(vi['sent'])} câu")
    if not same_ids:
        ok = False
    if not same_sent:
        ok = False

print("\n" + ("TẤT CẢ ĐẠT" if ok else "CÒN VIỆC CHƯA XONG"))
sys.exit(0 if ok else 1)
