#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 05 — kiểm tra lớp phủ chữ trên hình có truy được về câu MỚI không.

Quy tắc (H6/V3/A9.2):
  * trích dẫn ("…") phải NGUYÊN VĂN trong câu
  * chữ đậm/nghiêng phải bám câu (đo độ trùng token)
  * số trên hình phải có trong câu
Báo cáo từng dòng để biết dòng nào cần soạn lại chữ.
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

LANG = (sys.argv[1] if len(sys.argv) > 1 else "vi").lower()
CFG = {
    "vi": ("01_KICH_BAN/Tap05/kichban_tap05_23102026.md", "_t05_skeleton.json"),
    "en": ("01_KICH_BAN/Tap05_EN/kichban_tap05_EN.md", "_t05_skeleton.json"),
    "ja": ("01_KICH_BAN/Tap05_JA/kichban_tap05_JA.md", "_t05_skeleton.json"),
}[LANG]

els = parse_file(str(ROOT / CFG[0]))
idx = {e["id"]: [(s["id"], s["text"]) for s in e.get("sentences", [])]
       for e in els if e["kind"] == "LOI"}
sk = json.loads((W / CFG[1]).read_text(encoding="utf-8"))


def norm(s):
    s = s.lower()
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE)
    return " ".join(s.split())


def segs(chu):
    """Tách cột Chữ thành (kind, text) như parse_shots.parse_text."""
    out = []
    cell = re.sub(r"\*\*.+?\*\*|\*[^*]+?\*|“.+?”", lambda mm: mm.group(0).replace("→", "⟶"), chu)
    for raw in re.split(r"\s+→\s+", cell):
        raw = raw.replace("⟶", "→")
        for tok in re.finditer(r"\*\*(.+?)\*\*|\*(.+?)\*|“(.+?)”", raw):
            if tok.group(1):
                out.append(("bold", tok.group(1)))
            elif tok.group(2):
                out.append(("ital", tok.group(2)))
            else:
                out.append(("quote", tok.group(3)))
    return out


rows = []
bad_quote, weak, ok = [], [], 0
for r in sk["rows"]:
    if r["kind"] != "shot":
        continue
    ctx = " ".join(t for eid, a, b in r["spans"] for _, t in idx[eid][a - 1:b])
    nctx = norm(ctx)
    for kind, t in segs(r["cells"][5]):
        nt = norm(t)
        if kind == "quote":
            core = t.strip().strip("“”\"")
            for frag in [f.strip() for f in core.split("…") if f.strip()]:
                if norm(frag) not in nctx:
                    bad_quote.append(f"{r['sid']}: “{frag[:50]}”")
            continue
        if not nt:
            continue
        if nt in nctx:
            ok += 1
            continue
        # độ trùng token
        st = set(nt.split())
        ct = set(nctx.split())
        inter = len(st & ct)
        ratio = inter / len(st) if st else 0
        if ratio >= 0.6:
            weak.append(f"{r['sid']} [{kind}] trùng {ratio:.0%}: {t[:60]}")
        else:
            weak.append(f"{r['sid']} [{kind}] TRÙNG {ratio:.0%} — CẦN SOẠN LẠI: {t[:60]}")

print(f"[{LANG}] shot={sum(1 for r in sk['rows'] if r['kind']=='shot')} · "
      f"đoạn chữ khớp nguyên văn={ok} · cần xem lại={len(weak)} · trích dẫn sai={len(bad_quote)}")
if bad_quote:
    print("  TRÍCH DẪN KHÔNG NGUYÊN VĂN:")
    for b in bad_quote:
        print("    ", b)
need = [x for x in weak if "CẦN SOẠN LẠI" in x]
if need:
    print("  CẦN SOẠN LẠI:")
    for x in need:
        print("    ", x)
part = [x for x in weak if "CẦN SOẠN LẠI" not in x]
if part:
    print("  trùng một phần (chấp nhận được, nên soi lại):")
    for x in part:
        print("    ", x)
