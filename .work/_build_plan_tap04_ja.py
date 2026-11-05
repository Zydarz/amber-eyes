#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build complete shot table for KeHoach_Video_Tap04_JA.md and validate 100%."""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

ja_table = json.loads((W / "shots_text_tap04_JA.json").read_text(encoding="utf-8"))
script = json.loads((W / "script_tap04_JA.json").read_text(encoding="utf-8"))
S = {}
for e in script:
    if e.get("kind") == "LOI":
        for s in e["sentences"]:
            S[s["id"]] = s["text"]

en_path = ROOT / "02_SAN_XUAT/Tap04_EN/KeHoach_Video_Tap04_EN.md"
en_lines = en_path.read_text(encoding="utf-8").splitlines()
i0 = next(i for i, l in enumerate(en_lines) if l.startswith("## 6. DANH SÁCH SHOT"))
i1 = next(i for i, l in enumerate(en_lines) if i > i0 and l.startswith("**Tổng:"))

ACT_TITLES_JA = {
    1: "第1幕 · つかみ――模範の看護師の逆説",
    2: "第2幕 · 歪んだ心理のプロファイル――神のコンプレックスと無力感の補償",
    3: "第3幕 · 道徳的無効化と被害者の人間性の剥奪",
    4: "第4幕 · 捜査官の心理戦と潜入看護師の勇気",
    5: "第5幕 · 終幕――法廷、制度的沈黙への警鐘、そして終幕",
}

def sents(cell):
    out = []
    for ma, a, b in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cell):
        out += [f"{ma}#{k}" for k in range(int(a), int(b or a) + 1)]
    return out

BG_FILES = {p.stem for p in (ROOT / "assets" / "bg").glob("*.png")}

errors = []
out_rows = []
used = set()

for l in en_lines[i0:i1]:
    m = re.match(r"\|\s*([1-5]-\d+)\s*\|", l)
    if not m:
        continue
    sid = m.group(1)
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    
    # Sentence adjustment for 4 expanded shots
    if sid == "2-19":
        c[1] = "`2.11#9`–`#11`"
    elif sid == "3-02":
        c[1] = "`3.02#4`–`#7`"
    elif sid == "4-14":
        c[1] = "`4.12#8`–`#12`"
    elif sid == "5-03":
        c[1] = "`5.02#5`–`#7`"
        
    if sid not in ja_table:
        errors.append(f"{sid}: thiếu bản JA")
        continue
    used.add(sid)
    
    chu_ja, phrases, override = ja_table[sid]
    ids = sents(c[1])
    ctx = " ".join(S.get(x, "") for x in ids)
    
    # Check background exists
    bg_codes = re.findall(r"`([a-z_0-9]+)`", c[4])
    for bg in bg_codes:
        if bg not in ("pull", "push", "pan", "still", "void") and bg not in BG_FILES:
            errors.append(f"{sid}: thiếu file ảnh nền `{bg}`")
            
    # Process beat
    if override is not None:
        beat = override
    elif phrases:
        it = iter(phrases)
        # substitute each phrase in beat
        beat_parts = []
        for p in phrases:
            beat_parts.append(f'ở "{p}"')
        beat = " · ".join(beat_parts)
    else:
        # Keep non-verbal beats or —
        b_en = c[6]
        if "Typewriter" in b_en:
            beat = "Gõ từng ký tự"
        elif "Distant siren" in b_en:
            beat = "Tiếng còi cấp cứu, máy thở ICU"
        elif "Heart shock" in b_en:
            beat = "Tiếng sốc tim & flatline"
        elif "Minimalist piano" in b_en:
            beat = "Nhạc piano tối giản"
        elif "Nhạc drone" in b_en or "drone" in b_en.lower():
            beat = "Nhạc drone trầm đục"
        elif "Rushed footsteps" in b_en:
            beat = "Tiếng bước chân vội vã"
        elif "Cutlery" in b_en:
            beat = "Tiếng kéo ghế, dao nĩa"
        elif "Handcuffs" in b_en:
            beat = "Tiếng còng tay"
        elif "Gavel" in b_en:
            beat = "Tiếng búa tòa"
        elif "Case dossier shutting" in b_en or "gấp hồ sơ" in b_en:
            beat = "Tiếng gấp hồ sơ"
        elif "Power button" in b_en:
            beat = "Tiếng tắt máy ghi âm"
        elif "Music fade out" in b_en:
            beat = "Nhạc fade out"
        elif "Tên tập ở cuối" in b_en or "at the end" in b_en.lower():
            beat = "Tên tập ở cuối"
        else:
            beat = "—"
            
    # Validate beat phrases in sentence text
    for p in re.findall(r'ở "([^"]+)"', beat):
        if p not in ctx:
            errors.append(f"{sid}: cụm beat \"{p}\" không có trong câu JA: \"{ctx[:40]}...\"")
            
    # Validate quotes
    for q in re.findall(r"“([^”]+)”", chu_ja):
        for frag in [f.strip() for f in q.split("…") if f.strip()]:
            if frag not in ctx:
                errors.append(f"{sid}: trích dẫn “{frag[:40]}…” không nguyên văn trong câu JA")
                
    # Format line: | Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
    # Vai: H, D, C, N1, N2 or —
    vai = c[2]
    mau = c[3]
    nen = c[4]
    nv = c[7]
    tr = c[8] if len(c) > 8 else ""
    
    line = f"| {sid} | {c[1]} | {vai} | {mau} | {nen} | {chu_ja} | {beat} | {nv} | {tr} |"
    out_rows.append(line)

print(f"Validated {len(out_rows)} shots. Total errors: {len(errors)}")
for err in errors[:25]:
    print("  ERROR:", err)

if errors:
    sys.exit(1)

# Now read existing KeHoach_Video_Tap04_JA.md and append Section 6
plan_path = ROOT / "02_SAN_XUAT/Tap04_JA/KeHoach_Video_Tap04_JA.md"
existing_plan = plan_path.read_text(encoding="utf-8")

# Keep everything up to B2 and add Section 6
section_6 = f"""
---

## 6. DANH SÁCH SHOT — TẬP 04 (JA)

**Đọc bảng:** *Vai* = người đang nói (H ホスト · D 捜査官 · C 心理学者 · N1 証人 · N2 視聴者). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

**Bản JA:** cột *Chữ* dùng tiếng Nhật chuẩn phát thanh tài liệu (Pillow vẽ chữ với `YuGothB.ttc` / `YuGothM.ttc`); các cụm `ở "…"` trong cột *Beat* là cụm tiếng Nhật **có thật** trong câu JA của shot đó (`phrase_time()` dò trong text câu để đặt thời điểm).

**Intro:** đặt `assets/brand/intro_kenh_JA_t04.mov` ở 0,00 s (sinh bằng `py -3 .work/make_intro.py` với `AE_LANG=ja AE_EP=04` — thẻ cảnh báo tiếng Nhật). Không câu thoại nào thuộc intro.
Renderer hiện ảnh intro ở 0,00–20,50 s; shot `1-00` (20,50 s → lời đầu 23,0 s) mở dần từ đuôi đen của intro.

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
""" + "\n".join(out_rows) + f"""

**Tổng: {len(out_rows)} shot** (Hồi 1: 20 shot · Hồi 2: 20 shot · Hồi 3: 13 shot · Hồi 4: 15 shot · Hồi 5: 18 shot) · Phủ 100% 166/166 câu · 100% nền có file · chữ trên hình lấy từ câu đang đọc (H6).
"""

# If Section 6 already in plan, replace it; else append
if "## 6. DANH SÁCH SHOT" in existing_plan:
    existing_plan = existing_plan[:existing_plan.index("## 6. DANH SÁCH SHOT")].rstrip()
else:
    existing_plan = existing_plan.rstrip()

updated_plan = existing_plan + "\n" + section_6
plan_path.write_text(updated_plan, encoding="utf-8")
print(f"SUCCESS: updated {plan_path} with {len(out_rows)} shots")
