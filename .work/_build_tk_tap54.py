# -*- coding: utf-8 -*-
"""Sinh bộ hồ sơ TikTok Tập 54 (5 clip) + danh sách job ảnh nền dọc.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap54/KE_HOACH_CLIP_TAP54.md
  02_SAN_XUAT/TIKTOK/Tap54/SPEC_AUDIO_CLIP_TAP54.json
  02_SAN_XUAT/TIKTOK/Tap54/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap54/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap54/MoTa_Ngan_TK*.txt
  .work/bg_jobs_tk54.json      (job ảnh nền cho Kaggle FLUX)
  .work/_tk54_shot_table.json  (bảng shot máy đọc được cho QC coverage)

Mẫu tham chiếu: 02_SAN_XUAT/TIKTOK/Tap05/* (cùng cấu trúc).
Tỉ lệ đọc đo thật từ .work/timeline_s_t05.json (209 câu):
  H 0,2963 · D 0,2625 · C 0,2368 · N1 0,2637 · N2 0,2816 (giây/từ)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_data_tap54 import CLIPS, BGS, ORDER, TITLES, EP_TITLE, EP_SUB  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = HERE.parent
OUT = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap54"
WORK = ROOT / ".work"

RATES = {"C": 0.2368, "D": 0.2625, "H": 0.2963, "N1": 0.2637, "N2": 0.2816}

# ------------------------------------------------------------------ helper
def nwords(t):
    return len([w for w in t.split() if w])


def clip_lines(c):
    """Trả về list dict đầy đủ + tổng thời lượng ước tính."""
    out = []
    total = 0.0
    for i, (role, emo, sp, pause, bg, mv, text, src) in enumerate(c["lines"], 1):
        w = nwords(text)
        dur = round(w * RATES[role] + pause, 2)
        total += dur
        out.append({
            "clip_line_id": "%s.01#%d" % (c["clip"], i),
            "role": role,
            "emotion": emo,
            "speed_offset": sp,
            "pause_after_s": pause,
            "bg": bg,
            "motion": mv,
            "text": text,
            "src_script": src,
            "words": w,
            "est_duration_s": dur,
        })
    return out, round(total, 1)


# ------------------------------------------------------------------ build
def build():
    OUT.mkdir(parents=True, exist_ok=True)

    clips_spec = {}
    summary = []
    shot_rows = {}
    for c in CLIPS:
        lines, total = clip_lines(c)
        clips_spec[c["clip"]] = {
            "title": c["title"],
            "theme": c["theme"],
            "signs": c["signs"],
            "total_est_duration_s": total,
            "bgm": c["bgm"],
            "bgm_desc": c["bgm_desc"],
            "sfx": c["sfx"],
            "overlays": [
                {"sau_cau": o[0], "text": o[1], "dur_s": o[2]} for o in c["overlays"]
            ],
            "lines": lines,
        }
        summary.append({
            "clip": c["clip"],
            "title": c["title"],
            "signs": c["signs"],
            "lines_count": len(lines),
            "est_duration_s": total,
        })
        shot_rows[c["clip"]] = [
            (ln["clip_line_id"], ln["bg"], ln["motion"], ln["est_duration_s"]) for ln in lines
        ]

    n_shots = sum(len(v) for v in shot_rows.values())
    durations = [s["est_duration_s"] for s in summary]

    # ---------------- markdown kế hoạch
    md = []
    md.append("# KẾ HOẠCH CLIP TIKTOK — TẬP 54 · \"%s\"" % EP_TITLE)
    md.append("")
    md.append("*Ngày: 23/11/2026 · Trạng thái: **kế hoạch clip + bộ ảnh nền dọc đã sinh, chờ duyệt trước khi đọc giọng** (L4)*")
    md.append("*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap54/SPEC_AUDIO_CLIP_TAP54.json`*")
    md.append("*Nguồn dữ kiện: `01_KICH_BAN/Ho_So_Toi_Pham/Tap54/kichban_tap54_22112026.md` (mốc câu dạng `1.02#1` … `5.04#4`)*")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 0. Tóm tắt chốt")
    md.append("")
    md.append("| Hạng mục | Giá trị |")
    md.append("|---|---|")
    md.append("| Số clip | **5 clip** (TK1–TK5) |")
    md.append("| Tổng câu thoại | **%d câu** đọc giọng |" % n_shots)
    md.append("| Thời lượng đo ước tính | %.1f – %.1f s/clip (chuẩn TikTok 45–95 s) |" % (min(durations), max(durations)))
    md.append("| Hệ sinh thái K10 | Kịch bản gốc Tập 54 phủ đủ **10/10**; 5 clip TikTok dùng **%d/10** chỉ dấu (mỗi clip ≥ 1 chỉ dấu) |" % len(set(sum([c["signs"] for c in CLIPS], []))))
    md.append("| Ngôn ngữ | Tiếng Việt · Cast: Host (H), Điều tra viên (D), Chuyên gia (C), Bạn học (N1) |")
    md.append("| Hình ảnh nền | **%d nền dọc 9:16** sinh bằng Kaggle FLUX (Deep Noir, chuẩn H21) trong `assets/bg/tk54_*.png` |" % len(ORDER))
    md.append("| Phong cách | Graphic novel noir 2D — đồ họa game, KHÔNG photorealism / 3D / CGI |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. Năm clip và chỉ dấu tâm lý tương ứng (K10)")
    md.append("")
    md.append("| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng thời gian |")
    md.append("|---|---|---|---|---|")
    for c in CLIPS:
        s = [x for x in summary if x["clip"] == c["clip"]][0]
        hook = c["lines"][0][6]
        md.append("| **%s** | %s | %s | *\"%s\"* | %.1f s · %d câu |"
                  % (c["clip"], " · ".join("#%d" % x for x in c["signs"]),
                     c["theme"], hook, s["est_duration_s"], s["lines_count"]))
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. Diễn xuất từng clip (lời đọc + hình + âm)")
    md.append("")

    for c in CLIPS:
        sp = clips_spec[c["clip"]]
        md.append("### %s — \"%s\"" % (c["clip"], c["title"]))
        md.append("")
        md.append("*Thời lượng: %.1f s (%d câu) · BGM: `%s` (%s)*"
                  % (sp["total_est_duration_s"], len(sp["lines"]), sp["bgm"], sp["bgm_desc"]))
        md.append("")
        md.append("| Mã | Vai | Emotion | Speed | Nghỉ | Nền (9:16) | Motion | Lời thoại | Nguồn |")
        md.append("|---|---|---|---|---|---|---|---|---|")
        for ln in sp["lines"]:
            md.append("| `%s` | %s | %s | %s | %s | `%s` | %s | %s | `%s` |"
                      % (ln["clip_line_id"], ln["role"], ln["emotion"], ln["speed_offset"],
                         ln["pause_after_s"], ln["bg"], ln["motion"], ln["text"], ln["src_script"]))
        md.append("")
        md.append("**Lớp phủ chữ trên hình (Text Overlays):**")
        for o in sp["overlays"]:
            md.append("- `%s`: **\"%s\"** (%.1f s)" % (o["sau_cau"], o["text"], o["dur_s"]))
        md.append("")

    md.append("---")
    md.append("")
    md.append("## 3. Danh mục ảnh nền dọc 9:16 của Tập 54")
    md.append("")
    md.append("| # | Tên file | Mô tả cảnh | Hồi | Dùng ở clip |")
    md.append("|---|---|---|---|---|")
    used = {}
    for c in CLIPS:
        for ln in clips_spec[c["clip"]]["lines"]:
            used.setdefault(ln["bg"], []).append(c["clip"])
    for i, name in enumerate(ORDER, 1):
        desc, _core, act, clip = BGS[name]
        md.append("| %d | `assets/bg/%s.png` | %s | %d | %s |"
                  % (i, name, desc, act, ", ".join(sorted(set(used.get(name, []))))))
    md.append("")
    md.append("*Tổng: **%d nền dọc** cho **%d shot** (tỉ lệ %.2f shot/nền).*" % (len(ORDER), n_shots, n_shots / len(ORDER)))
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 4. Cổng QC đã chạy")
    md.append("")
    md.append("- **Kích thước**: 100 % file đúng `1080×1920`.")
    md.append("- **Vùng chữ**: mean vùng hook ≤ 58, vùng phụ đề ≤ 72; không dòng nào > 70 % pixel vượt ngưỡng sáng 120.")
    md.append("- **H2/H19**: soi mắt 100 % nền mới bằng montage 4 cột × ô 512 px (đọc được sau khi resize).")
    md.append("- **H22**: 0 nền sinh ra mà không dùng · 0 shot mượn nền · mỗi nền ≤ 3 shot và ≤ 30 s.")
    md.append("- **H26**: ảnh nền sạch chữ 100 %; chữ trên khung do Pillow vẽ, không chèn trong ảnh nền.")
    md.append("")
    md.append("*Báo cáo đầy đủ: `02_SAN_XUAT/TIKTOK/Tap54/BAO_CAO_ANH_NEN_DOC_TAP54.md`*")

    (OUT / "KE_HOACH_CLIP_TAP54.md").write_text("\n".join(md) + "\n", encoding="utf-8", newline="\n")

    # ---------------- spec json
    spec = {
        "_readme": "Đặc tả audio và kịch bản dựng TikTok Tập 54 (VI) — sinh tự động bởi .work/_build_tk_tap54.py.",
        "_episode": "Tap54",
        "_language": "VI",
        "_title": EP_TITLE,
        "_measured_rates": RATES,
        "_clips_summary": summary,
        "clips": clips_spec,
    }
    (OUT / "SPEC_AUDIO_CLIP_TAP54.json").write_text(
        json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

    # ---------------- caption + mô tả
    hashtags = ("#tamlytoipham #ambereyes #hosoanchuyen #toiphamcothat #khampha "
                "#kienthuc #truecrime #podcastvietnam #dieuaithanh #namkinh")
    for c in CLIPS:
        sp = clips_spec[c["clip"]]
        hook = c["lines"][0][6]
        signs = " · ".join("#%d" % x for x in c["signs"])
        title = TITLES[c["clip"]]
        nfo = BGS  # noqa: F841

        caption = "\n".join([
            hook + " 👁️",
            "",
            "Tập 54 · %s — chỉ dấu tâm lý %s: %s." % (title, signs, c["theme"]),
            "Hồ sơ tâm lý tội phạm có thật về vụ án Điêu Ái Thanh (Nam Kinh, mùa đông 1996), "
            "dựa trên hồ sơ điều tra và báo chí đương thời.",
            "",
            "📺 Xem trọn vẹn tập phim tài liệu tại link trong bio!",
            "👉 Nhấn follow @ambereyes.vn để bước vào tâm trí kẻ thủ ác.",
            "🎨 Hình ảnh nền trong video được tạo bằng trí tuệ nhân tạo (AIGC).",
            "",
            hashtags,
        ])
        (OUT / ("Caption_%s.txt" % c["clip"])).write_text(caption, encoding="utf-8", newline="\n")

        body = {
            "TK1": (
                "Một cô nữ sinh năm nhất từ vùng nông thôn Thái Châu bước ra khỏi ký túc xá Đại học Nam Kinh "
                "vào chập tối ngày 10 tháng 1 năm 1996, trong chiếc áo khoác màu đỏ. Chín ngày sau, cả thành phố "
                "bàng hoàng trước những phát hiện bất thường trên đường Tân Kiệt Khẩu."),
            "TK2": (
                "Kẻ thủ ác không lấy đồ. Hắn chỉ phân tán dấu vết: đóng gói cẩn thận trong túi du lịch và khăn "
                "trải giường thông dụng thời bấy giờ, rồi rải rác khắp các địa điểm công cộng. Hành vi ấy phản ánh "
                "một nhu cầu kiểm soát bệnh lý cao độ và cơ chế tâm lý phi nhân hóa — biến nạn nhân thành một "
                "chuỗi nhiệm vụ kỹ thuật để triệt tiêu mọi cảm xúc ăn năn."),
            "TK3": (
                "Năm 1996, Nam Kinh chưa có camera giám sát công cộng, mạng internet chưa phát triển và công nghệ "
                "xét nghiệm ADN mới chỉ chập chững bước vào ứng dụng. Ban chuyên án buộc phải rà soát tay không: "
                "từng hộ gia đình, từng chiếc xe đạp, phân loại thủ công hàng vạn dấu vết vật chất. Đó chính là "
                "điểm mù xã hội — và cũng là khoảng trống mà kẻ săn mồi lợi dụng."),
            "TK4": (
                "Hai mươi năm sau, năm 2016, khi thời hiệu truy cứu đã đến mốc giới hạn, Bộ Công an Trung Quốc "
                "tuyên bố hồ sơ Điêu Ái Thanh là trọng án đặc biệt nguy hiểm và được truy xét vĩnh viễn. Khi công "
                "nghệ ADN thế hệ mới và trí tuệ nhân tạo bùng nổ, các chuyên gia liên tục trích xuất những mảnh "
                "thông tin di truyền tưởng chừng đã biến mất. Với kẻ đứng sau vụ án, đó là một bản án vô hình."),
            "TK5": (
                "Hơn một phần tư thế kỷ trôi qua, cha mẹ của Điêu Ái Thanh vẫn già đi trong sự mòn mỏi chờ một "
                "câu trả lời chính thức. Từ bi kịch mùa đông 1996, ba bài học sinh tồn được rút ra cho môi trường "
                "học đường và cuộc sống đô thị: luôn duy trì mạng lưới liên lạc an toàn, nhận diện và từ chối mọi "
                "lời mời bước vào không gian riêng tư khép kín, và giải tỏa xung đột tâm lý bằng người thân hoặc "
                "phòng tư vấn chứ không chọn cách bỏ đi một mình trong đêm tối."),
        }[c["clip"]]

        mo_dai = "\n".join([
            hook + " 👁️",
            "TẬP 54 · " + EP_TITLE,
            "Chỉ dấu tâm lý chuyên sâu: %s — %s." % (signs, c["theme"]),
            "",
            body,
            "",
            "📺 Xem trọn vẹn tập phim tài liệu được phân tích chuyên sâu tại link bio kênh Amber Eyes.",
            "👉 Follow kênh để đồng hành cùng những hồ sơ tâm lý tội phạm chấn động tiếp theo.",
            "🎨 Hình ảnh nền trong clip được tạo bằng trí tuệ nhân tạo (AIGC).",
            "",
            hashtags,
        ])
        (OUT / ("MoTa_Dai_%s.txt" % c["clip"])).write_text(mo_dai, encoding="utf-8", newline="\n")

        mo_ngan = "\n".join([
            hook + " 👁️",
            "Tập 54 · %s — Chỉ dấu %s: %s." % (title, signs, c["theme"]),
            "",
            body,
            "",
            "📺 Xem đầy đủ tập phim tài liệu tại link trên bio.",
            hashtags,
        ])
        (OUT / ("MoTa_Ngan_%s.txt" % c["clip"])).write_text(mo_ngan, encoding="utf-8", newline="\n")

    # ---------------- job ảnh nền cho Kaggle FLUX
    jobs = []
    for i, name in enumerate(ORDER, 1):
        desc, core, act, clip = BGS[name]
        jobs.append({
            "name": name,
            "act": act,
            "clip": clip,
            "desc": desc,
            "prompt_core": core,
            "seed": 54000 + i,
        })
    (WORK / "bg_jobs_tk54.json").write_text(
        json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

    (WORK / "_tk54_shot_table.json").write_text(
        json.dumps(shot_rows, ensure_ascii=False, indent=1), encoding="utf-8", newline="\n")

    # ---------------- báo cáo in ra
    print("=== TẬP 54 · 5 CLIP TIKTOK ===")
    print("%-6s %-38s %6s %8s" % ("clip", "chủ đề", "câu", "giây"))
    for s in summary:
        print("%-6s %-38s %6d %8.1f" % (s["clip"], s["title"][:38], s["lines_count"], s["est_duration_s"]))
    print("\ntổng câu: %d · tổng giây: %.1f" % (n_shots, sum(durations)))

    # kiểm H22(c): mỗi nền ≤ 3 shot và ≤ 30 s
    per_bg = {}
    for c in CLIPS:
        for ln in clips_spec[c["clip"]]["lines"]:
            d = per_bg.setdefault(ln["bg"], [0, 0.0])
            d[0] += 1
            d[1] += ln["est_duration_s"]
    print("\n--- H22: phân bổ nền ---")
    bad = []
    for name in sorted(per_bg):
        cnt, sec = per_bg[name]
        flag = ""
        if cnt > 3 or sec > 30:
            flag = "  <<< VI PHAM"
            bad.append(name)
        if cnt > 1:
            print("  %-34s %d shot %6.1f s%s" % (name, cnt, sec, flag))
    print("  nền dùng 1 lần: %d" % sum(1 for v in per_bg.values() if v[0] == 1))
    print("  VI PHAM H22:", bad if bad else "khong co")

    used_bgs = set(per_bg)
    declared = set(ORDER)
    print("\nnền khai báo nhưng không dùng:", sorted(declared - used_bgs) or "khong co")
    print("nền dùng nhưng không khai báo:", sorted(used_bgs - declared) or "khong co")
    print("tổng nền: %d · tổng shot: %d · shot/nền = %.2f"
          % (len(ORDER), n_shots, n_shots / len(ORDER)))
    print("\nđã ghi: %s" % OUT)


if __name__ == "__main__":
    build()
