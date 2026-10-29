import json
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(r"D:\TEST\Gax\Audi")
shots = json.loads((ROOT / ".work" / "shots_t04.json").read_text(encoding="utf-8"))["shots"]
script = json.loads((ROOT / ".work" / "script_tap04.json").read_text(encoding="utf-8"))
tl = json.loads((ROOT / ".work" / "timeline_s_t04.json").read_text(encoding="utf-8"))

items = {it["id"]: it for it in tl["items"]}
sents = {}
for e in script:
    if e["kind"] == "LOI":
        r = e["role"]
        if e["id"] == "1.07": r = "N1"
        elif e["id"] == "4.06": r = "N2"
        for s in e["sentences"]:
            sents[s["id"]] = {"role": r, "text": s["text"], "elem": e["id"]}

# Kiểm tra danh sách 51 ảnh nền trong assets/bg
bg_files = {p.stem for p in (ROOT / "assets" / "bg").glob("t4_*.png")}
print(f"Tổng số ảnh nền t4: {len(bg_files)}")

# Bảng phân tích chi tiết từng shot
print(f"\n{'SHOT':<5} | {'VAI':<3} | {'THỜI GIAN (s)':<16} | {'DUR':<5} | {'NỀN (BG)':<25} | {'MẪU':<4} | {'CÂU':<15}")
print("-" * 85)
for s in shots:
    sid = s["id"]
    st = s["start"]
    et = s["end"]
    dur = et - st
    bg = s.get("bg", "")
    tmpl = s.get("template") or ""
    role = s.get("role") or ""
    c_list = s.get("sentences", [])
    c_str = f"{c_list[0]}..{c_list[-1]}" if len(c_list) > 1 else (c_list[0] if c_list else "—")
    print(f"{sid:<5} | {role:<3} | {st:6.1f} -> {et:6.1f} | {dur:4.1f}s | {bg:<25} | {tmpl:<4} | {c_str:<15}")
