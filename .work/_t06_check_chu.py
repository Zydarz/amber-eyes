#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 — kiểm lớp phủ chữ trên hình cho EN / JA (trích dẫn nguyên văn, số trên hình, từ cấm).

Dùng:  py -3 .work/_t06_check_chu.py en|ja
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.path.insert(0, str(W))
from parse_kichban import parse_file  # noqa: E402

KB = {"en": ROOT / "01_KICH_BAN/Tap06_EN/kichban_tap06_EN.md",
      "ja": ROOT / "01_KICH_BAN/Tap06_JA/kichban_tap06_JA.md"}
CHU = {"en": W / "_t06_chu_en.json", "ja": W / "_t06_chu_ja.json"}

FORBIDDEN = {
    "en": ["blood", "corpse", "strangle", "choke", "struggle", "raped", "rape",
           "underwear", "sexual intercourse", "orgasm", "penis", "vagina", "suffocat",
           "mutilat", "dismember", "torture"],
    "ja": ["血", "死体", "絞", "レイプ", "性交渉", "精通"],
}
SAFE = {"en": ["blood type", "blood pressure", "blood vessel", "bloodstream",
               "blood cell", "struggle to survive", "struggled to"],
        "ja": []}
STRUCT_EN = r"(ACT|STAGE|LAYER|COMPARTMENT|EPISODE|CASE\s+FILE)"
STRUCT_JA = r"(第\s*\d+\s*[幕話])"

lang = (sys.argv[1] if len(sys.argv) > 1 else "en").lower()
plan = json.loads((W / "_t06_plan_vi.json").read_text(encoding="utf-8"))
chu = json.loads(CHU[lang].read_text(encoding="utf-8"))

els = parse_file(str(KB[lang]))
script = {}
for e in els:
    if e.get("kind") == "LOI":
        script[e["id"]] = {s["id"]: s["text"] for s in e.get("sentences", [])}


def sent_list(cell):
    out = []
    for part in str(cell).split(","):
        m = re.match(r"^#(\d+)(?:-#(\d+))?$", part.strip())
        if m:
            a = int(m.group(1))
            out += list(range(a, int(m.group(2) or a) + 1))
    return out


def parse_chu(cell):
    cell = re.sub(r"\*\*.+?\*\*|\*[^*]+?\*|“.+?”",
                  lambda m: m.group(0).replace("→", "⟶"), cell)
    segs = []
    for raw in re.split(r"\s+→\s+", cell):
        raw = raw.replace("⟶", "→")
        at = None
        m = re.match(r"(?:ở\s+)?`#(\d+)`:?\s*(.*)", raw)
        if m:
            at, raw = int(m.group(1)), m.group(2)
        elems = []
        for tok in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", raw):
            if tok.group(1):
                elems.append(("bold", tok.group(1)))
            elif tok.group(2):
                elems.append(("ital", tok.group(2)))
            else:
                elems.append(("quote", tok.group(3)))
        if elems:
            segs.append((at, elems))
    return segs


errs = []
if len(chu) != len(plan["shots"]):
    errs.append(f"số mục {len(chu)} ≠ số shot {len(plan['shots'])}")

for i, sh in enumerate(plan["shots"]):
    key = str(i)
    if key not in chu:
        errs.append(f"[{i}] thiếu mục")
        continue
    text = chu[key]
    if not text.strip():
        errs.append(f"[{i}] chuỗi rỗng")
        continue
    el = sh["el"]
    ctx = ""
    if sh.get("kind") in (None, "shot"):
        ctx = " ".join(script.get(el, {}).get(f"{el}#{k}", "") for k in sent_list(sh["sent"]))
    on_screen = [(k, t) for _at, elems in parse_chu(text) for k, t in elems]
    if not on_screen:
        errs.append(f"[{i}] không có phần chữ nào đọc được (thiếu ** / * / “”)")
    # trích dẫn nguyên văn
    for kind, t in on_screen:
        if kind != "quote":
            continue
        core = t.strip().strip("“”\"")
        for frag in [f.strip() for f in core.split("…") if f.strip()]:
            if frag not in ctx:
                errs.append(f"[{i}] trích dẫn “{frag[:50]}…” không nguyên văn trong câu")
    # số trên hình
    flat = ctx.replace(" ", "")
    allowed = set(re.findall(r"\d+", flat))
    for a in list(allowed):
        allowed.add(a.zfill(2))
        allowed.add(str(int(a)))
    screen = " ".join(t for _k, t in on_screen)
    for m in set(re.findall(r"\d[\d.,]*", screen)):
        tok = m.replace(".", "")
        if m in allowed or m in flat or tok in allowed:
            continue
        if lang == "ja" and re.search(r"第\s*" + re.escape(m) + r"\s*[幕話]", screen):
            continue
        if lang == "en" and re.search(STRUCT_EN + r"\s*" + re.escape(m) + r"\b", screen):
            continue
        errs.append(f"[{i}] số “{m}” không có trong câu của shot")
    # từ cấm
    low = screen.lower()
    for w in FORBIDDEN[lang]:
        if not re.search(r"(?<!\w)" + r"\s+".join(re.escape(x) for x in w.split()) + r"(?!\w)", low):
            continue
        if any(g in low for g in SAFE[lang] if g in w or w in g):
            continue
        errs.append(f"[{i}] từ cấm “{w}” trên hình")
    # số phần
    n_parts = len([1 for _at, elems in parse_chu(text) for _k, _t in elems])
    if sh.get("kind") not in ("open", "end") and n_parts != 2:
        errs.append(f"[{i}] có {n_parts} phần chữ (kỳ vọng 2)")

print(f"[{lang}] {len(chu)}/{len(plan['shots'])} shot")
if errs:
    print(f"✗ {len(errs)} lỗi:")
    for e in errs[:50]:
        print("  -", e)
    sys.exit(1)
print("✓ toàn bộ lớp phủ đạt")
