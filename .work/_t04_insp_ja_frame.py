#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — so lớp phủ JA với khung VN (rule 4) + kiểm trích dẫn nguyên văn (V3)."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from parse_kichban import parse_file  # noqa: E402

W = ROOT / ".work"
sk = json.loads((W / "_t04_skeleton.json").read_text(encoding="utf-8"))
vn = json.loads((W / "_t04_chu_vn.json").read_text(encoding="utf-8"))
ja = json.loads((W / "_t04_chu_ja.json").read_text(encoding="utf-8"))

idx = {}
for el in parse_file(str(ROOT / "01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md")):
    if el["kind"] == "LOI":
        idx[el["id"]] = [(s["id"], s["text"]) for s in el.get("sentences", [])]


def shape(text):
    """(marker, [danh sách vai trò theo thứ tự]) cho mỗi khối."""
    out = []
    for part in re.split(r"\s+→\s+", text):
        m = re.match(r"(?:ở\s+)?`#(\d+)`:?", part)
        out.append((m.group(1) if m else None,
                    [("B" if g[0] else "I" if g[1] else "Q")
                     for g in re.findall(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", part)]))
    return out


errs = []
shots = [r for r in sk["rows"] if r["kind"] == "shot"]
for r in shots:
    sid = r["sid"]
    sv, sj = shape(vn[sid]), shape(ja[sid])
    if [m for m, _ in sv] != [m for m, _ in sj]:
        errs.append(f"{sid}: vị trí mốc #N lệch · VN {[m for m, _ in sv]} vs JA {[m for m, _ in sj]}")
    if [e for _, e in sv] != [e for _, e in sj]:
        errs.append(f"{sid}: vai trò đậm/nghiêng lệch · VN {[e for _, e in sv]} vs JA {[e for _, e in sj]}")

print(f"[khung] so voi bang VN · lech: {len(errs)}")
for e in errs:
    print("  x", e)

# --- V3: trich dan "..." dung rieng phai NGUYEN VAN trong cau cua shot ---
qbad = []
for r in shots:
    sid = r["sid"]
    eid, a, b = r["spans"][0]
    ctx = " ".join(t for _, t in idx[eid][a - 1:b])
    for part in re.split(r"\s+→\s+", ja[sid]):
        part = re.sub(r"^\s*(?:ở\s+)?`#\d+`:?", "", part)
        for g in re.findall(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", part):
            t = g[0] or g[1] or g[2]
            if not g[0] and not g[1]:   # trich dan "..." (nhom 3)
                core = t.strip().strip("“”\"")
                for frag in [f.strip() for f in core.split("…") if f.strip()]:
                    if frag not in ctx:
                        qbad.append(f"{sid}: «{frag[:40]}» khong nguyen van")
print(f"[V3] trich dan \"...\" nguyen van trong cau: {len(qbad)} loi")
for e in qbad:
    print("  x", e)

# --- rau: khong co | , khong co nhay kep ASCII , moi shot co chu ---
pipe = [s for s, t in ja.items() if "|" in t]
ascii_q = [s for s, t in ja.items() if '"' in t]
missing = [r["sid"] for r in shots if r["sid"] not in ja]
print(f"[rau] shot thieu chu: {missing} · co '|': {pipe} · co nhay kep ASCII: {ascii_q}")
print(f"[rac] file chu co {len(ja)} khoa · beat co {len(json.loads((W / '_t04_beat_ja.json').read_text(encoding='utf-8')))} khoa")
