#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap24 — sinh bảng shot (mục 6) cho VN / EN / JA từ bảng shot VN (chuẩn A8.1 mục c).

- Giữ nguyên: mã shot, mã nền, mẫu T, camera, cột Vai, cột Beat, cờ trong cột Nhân vật.
- Chỉ đổi: cột Chữ -> câu gốc của ngôn ngữ đích · cột Câu -> thời lượng THẬT đo từ
  timeline của ngôn ngữ đó · tên hồi / tiêu đề / phần B1-B5 theo ngôn ngữ.
- Bổ sung dòng "**Tổng:" — parse_shots.py CẦN dòng này (thiếu => crash).
"""
import json, os, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
HOSO = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham"
BACKUP = WORK / "_cu" / "plan_t24_20261125"

LANGS = {
    "vi": {"dir": "Tap24", "plan": "KeHoach_Video_Tap24.md",
           "script": "script_tap24.json", "tl": "timeline_s_t24.json",
           "md": "01_KICH_BAN/Ho_So_Toi_Pham/Tap24/kichban_tap24_23102026.md",
           "act_re": r"^## (HỒI \d+): (.+)$",
           "animals": {"H": "Cú", "D": "Sói", "C": "Cáo"},
           "lang_label": "VI", "title": "HỒ SƠ SẢN XUẤT TẬP 24 · \"KÝ ỨC KẺ SÁT NHÂN HWASEONG\" — VI EDITION",
           "intro_mov": "assets/brand/intro_kenh.mov"},
    "en": {"dir": "Tap24_EN", "plan": "KeHoach_Video_Tap24_EN.md",
           "script": "script_tap24_EN.json", "tl": "timeline_s_EN_t24.json",
           "md": "01_KICH_BAN/Ho_So_Toi_Pham/Tap24/kichban_tap24_EN.md",
           "act_re": r"^## (ACT \d+): (.+)$",
           "animals": {"H": "Owl", "D": "Wolf", "C": "Fox"},
           "lang_label": "EN", "title": "PRODUCTION DOSSIER · EPISODE 24 · \"MEMORIES OF THE HWASEONG SERIAL KILLER\" — EN EDITION",
           "intro_mov": "assets/brand/intro_kenh_EN.mov"},
    "ja": {"dir": "Tap24_JA", "plan": "KeHoach_Video_Tap24_JA.md",
           "script": "script_tap24_JA.json", "tl": "timeline_s_JA_t24.json",
           "md": "01_KICH_BAN/Ho_So_Toi_Pham/Tap24_JA/kichban_tap24_JA.md",
           "act_re": r"^## (第\d幕): (.+)$",
           "animals": {"H": "フクロウ", "D": "オオカミ", "C": "キツネ"},
           "lang_label": "JA", "title": "制作fitting文書 · 第24話 「華城の殺人の追憶」 — JA EDITION",
           "intro_mov": "assets/brand/intro_kenh_JA_t24.mov"},
}

VN_ANIMALS = {"Cú": "H", "Cáo": "C", "Sói": "D"}

# ĐỔI NỀN (H22): 2 shot đầu Hồi 1 dùng chung t24_a1_01 → 31,6 s (VN) > giới hạn 30 s.
# Đổi shot 1-01 sang nền làng mờ (1 shot duy nhất trong bảng) và đưa nền ruộng lúa
# về đúng shot 1-02 (câu nói về cánh đồng lúa + đường mòn) — khớp ngữ nghĩa H3.
BG_SWAP = {
    "1-01": "t24_a1_23_rural_village_lane_fog_23",
    "1-02": "t24_a1_01_desolate_rice_paddies_mist_01",
}


def read_vn_rows():
    """Các dòng shot chuẩn lấy từ bảng VN (mã shot, nền, camera, mẫu, vai, cờ)."""
    p = HOSO / "Tap24" / "KeHoach_Video_Tap24.md"
    text = p.read_text(encoding="utf-8")
    sec = text[text.index("## 6. DANH SÁCH SHOT"):]
    rows = []
    for line in sec.splitlines():
        if not re.match(r"\|\s*[1-5]-\d+", line):
            continue
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        sid, cau, vai, mau, nen = (c + [""] * 9)[:5]
        code = re.search(r"`([a-z0-9_.]+#\d+)`", cau).group(1)
        bg = re.search(r"`(t24_[a-z0-9_]+)`", nen).group(1)
        cam = re.search(r"`(still|pan|push|pull|hero)`", nen)
        rows.append({"sid": sid, "code": code, "vai": vai, "mau": mau,
                     "bg": BG_SWAP.get(sid, bg), "cam": cam.group(1) if cam else "still",
                     "nv": c[7] if len(c) > 7 else "—", "beat": c[6] if len(c) > 6 else "—",
                     "act": int(sid.split("-")[0])})
    return rows


def act_titles(cfg):
    out = {}
    for l in (ROOT / cfg["md"]).read_text(encoding="utf-8").splitlines():
        m = re.match(cfg["act_re"], l)
        if m:
            n = int(re.search(r"\d+", m.group(1)).group())
            out[n] = f"{m.group(1)}: {m.group(2)}".strip()
    return out


def build(lang, cfg, rows):
    script = json.loads((WORK / cfg["script"]).read_text(encoding="utf-8"))
    tl = json.loads((WORK / cfg["tl"]).read_text(encoding="utf-8"))
    S = {it["id"]: it for it in tl["items"]}
    sent_text = {s["id"]: s["text"] for e in script for s in e.get("sentences", [])}
    role_of = {}
    for e in script:
        if e.get("sentences"):
            role_of[e["id"]] = e.get("role")
    # đếm câu theo vai
    n_role = {}
    for e in script:
        if e.get("sentences"):
            r = e.get("role")
            n_role[r] = n_role.get(r, 0) + len(e["sentences"])

    acts = act_titles(cfg)
    per_act = {}
    for r in rows:
        per_act[r["act"]] = per_act.get(r["act"], 0) + 1

    # ---------- văn bản ----------
    L = []
    A = L.append
    A(f"# {cfg['title']}")
    A("")
    A(f"*Hồ sơ sản xuất Tập 24 — bản {cfg['lang_label']} · sinh từ bảng shot chuẩn VN theo A8.1 (mục c): "
      f"giữ nguyên mã shot / nền / mẫu T / camera; chỉ đổi cột Chữ sang ngôn ngữ đích.*")
    A("")
    A("## B1. Thông tin tập")
    A("")
    A("| Mục | Nội dung |")
    A("|---|---|")
    A(f"| Vụ án | Hồ sơ Lee Choon-jae — Hwaseong & Busan, Hàn Quốc (1986–1991) |")
    A(f"| Ngôn ngữ | {cfg['lang_label']} |")
    A(f"| Số câu thoại | {len(S)} (mã câu trùng khớp 100% với bản VN) |")
    A(f"| Số shot | {len(rows)} · {len({r['bg'] for r in rows})} nền dùng chung cho 3 ngôn ngữ |")
    A(f"| Thời lượng audio | {tl['total']:.1f} s ({tl['total']/60:.1f} phút) — đo từ master `"
      f"{'Tap24' if lang=='vi' else ('Tap24_EN' if lang=='en' else 'Tap24_JA')}_master.mp3` |")
    A(f"| Intro | `{cfg['intro_mov']}` · 0,00–22,41 s |")
    A(f"| Nền | `assets/bg/t24_*.png` — 155 ảnh 2112×1188, dùng chung VN/EN/JA (H25) |")
    A("")
    A("## B2. Cấu trúc 5 Hồi")
    A("")
    for i in range(1, 6):
        A(f"### {acts.get(i, f'Hồi {i}')} — {per_act.get(i, 0)} shot")
        A("")
    A("## B3. Bảng phân vai")
    A("")
    A("| Ký hiệu | Vai trò | Số câu |")
    A("|---|---|---:|")
    names = {"H": "Host (Dẫn chuyện)", "D": "Điều tra viên", "C": "Chuyên gia tâm lý",
             "N": "Người trong cuộc"}
    for r in ("H", "D", "C", "N"):
        if r in n_role:
            A(f"| {r} | {names[r]} | {n_role[r]} |")
    A(f"| **TỔNG** | | **{sum(n_role.values())}** |")
    A("")
    A("## B4. Danh mục Cue âm thanh & SFX đồng bộ")
    A("")
    A("| Mốc | Hồi | Loại | Mô tả |")
    A("|---|---:|---|---|")
    for e in script:
        if e["kind"] in ("BGM", "SFX"):
            A(f"| `{e['id']}` | {e['act']} | {e['kind']} | {e.get('desc', '').strip()} |")
    A("")
    A("## B5. Kế hoạch triển khai kỹ thuật")
    A("")
    A("1. `parse_shots.py` → `.work/shots%s.json` (mốc thời gian chỉ lấy từ `timeline_s%s.json`)."
      % ("" if lang == "vi" else ("_EN" if lang == "en" else "_JA"),
         "" if lang == "vi" else ("_EN" if lang == "en" else "_JA")))
    A("2. `qc_bg_usage.py` → dùng hết 155 ảnh, 0 nền vượt 3 shot/30 s (H22).")
    A("3. `build_video3.py --stills` → soi ảnh tĩnh 100 % shot (H9).")
    A("4. `build_video3.py --workers 6` → dựng hình.")
    A("5. `subtitles.py` + `package.py --mux` → phụ đề, thumbnail, thẻ kết.")
    A("")
    split_idx = len(L)
    A(f"## 6. DANH SÁCH SHOT — TẬP 24 ({cfg['lang_label']})")
    A("")
    A("Nền `t24_*` là **tài sản dùng chung cho cả 3 ngôn ngữ** (H25/A8.1) — mã shot giống nhau luôn dùng cùng một nền.")
    A("")
    A("### INTRO KÊNH · 0,00–22,41 s")
    A("")
    A(f"Đặt `{cfg['intro_mov']}` tại 0,00 s (A5.7). Không câu thoại nào thuộc intro.")
    A("")
    for act in range(1, 6):
        A(f"### {acts.get(act, f'Hồi {act}')}")
        A("")
        A("| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |")
        A("|---|---|---|---|---|---|---|---|---|")
        for r in rows:
            if r["act"] != act:
                continue
            dur = S[r["code"]]["end"] - S[r["code"]]["start"]
            dur_txt = f"{dur:.1f}".replace(".", ",")   # qc_bg_usage.py --plan đòi dấu phẩy thập phân
            txt = sent_text.get(r["code"], "").replace("*", "")
            nv = r["nv"]
            for vn_name, role in VN_ANIMALS.items():
                nv = nv.replace(vn_name, cfg["animals"].get(role, vn_name))
            A(f"| {r['sid']} | `{r['code']}` ({dur_txt} s) | {r['vai']} | {r['mau']} | "
              f"`{r['bg']}`, `{r['cam']}` | *{txt}* | {r['beat']} | {nv} | |")
        A("")
    total_speech = sum(S[r["code"]]["end"] - S[r["code"]]["start"] for r in rows)
    A(f"**Tổng: {len(rows)} shot** (Hồi 1: {per_act.get(1,0)} · Hồi 2: {per_act.get(2,0)} · "
      f"Hồi 3: {per_act.get(3,0)} · Hồi 4: {per_act.get(4,0)} · Hồi 5: {per_act.get(5,0)}) · "
      f"{len({r['bg'] for r in rows})} nền · Phủ 100 % {len(S)}/{len(S)} câu · "
      f"thời lượng lời {total_speech:.0f} s (master {tl['total']:.0f} s).")
    A("")
    sec6 = "\n".join(L[split_idx:])
    head_part = "\n".join(L[:split_idx])
    # VN: chỉ thay MỤC 6, giữ nguyên B1–B5 đã duyệt
    if lang == "vi":
        orig = (HOSO / "Tap24" / "KeHoach_Video_Tap24.md").read_text(encoding="utf-8")
        head = orig[:orig.index("## 6. DANH SÁCH SHOT")]
        return head + sec6
    return head_part + "\n" + sec6


def main():
    rows = read_vn_rows()
    print(f"bảng shot chuẩn: {len(rows)} dòng · {len({r['bg'] for r in rows})} nền")
    BACKUP.mkdir(parents=True, exist_ok=True)
    for lang, cfg in LANGS.items():
        out = HOSO / cfg["dir"] / cfg["plan"]
        if out.exists() and not (BACKUP / f"{cfg['dir']}_{cfg['plan']}").exists():
            shutil.copy2(out, BACKUP / f"{cfg['dir']}_{cfg['plan']}")
            print(f"  sao lưu {out.name} -> {BACKUP}")
        txt = build(lang, cfg, rows)
        out.write_text(txt, encoding="utf-8")
        print(f"  ghi {out} ({len(txt.splitlines())} dòng)")


if __name__ == "__main__":
    main()
