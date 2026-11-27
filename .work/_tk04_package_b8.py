# -*- coding: utf-8 -*-
"""Buoc 8 - Dong goi Tap 04 (VN/EN/JA).

- them dong nhan AIGC + khoi 'Ghi chu khi dang' vao 15 Caption_TK*.txt (giu nguyen phan caption)
- tao mo_ta.txt (dong goi) cho Tap04 / Tap04_EN / Tap04_JA
- tao checklist_dang.md cho Tap04 / Tap04_EN / Tap04_JA

Chay lai duoc: py -3 .work/_tk04_package_b8.py [--write]
Mac dinh: chi tinh toan + in preview, khong ghi file.
"""
import argparse, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
TK = ROOT / "02_SAN_XUAT" / "TIKTOK"
LANGS = [("VN", "Tap04"), ("EN", "Tap04_EN"), ("JA", "Tap04_JA")]
CLIPS = ["TK1", "TK2", "TK3", "TK4", "TK5"]
DATE = "2026-11-27"

AIGC = {
    "VN": "Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.",
    "EN": "Content created with AI assistance for behavioral analysis. Viewer discretion advised.",
    "JA": "AI技術を活用して心理分析目的で制作されたコンテンツです。閲覧にはご注意ください。",
}

# trang thai QC tung clip (tu BAO_CAO_QC_TIKTOK_TAP04.md + do lai 27/11)
QC_BLOCK = {
    ("VN", "TK1"): ("TRƯỢT T13 — từ cấm “sát hại” trong kịch bản (TK1.01#6) — CHỜ người dùng duyệt câu thay thế, chưa đăng được.", "TK1.01#6"),
    ("VN", "TK3"): ("TRƯỢT T13 — từ cấm “sát hại” trong kịch bản (TK3.01#9) — CHỜ người dùng duyệt câu thay thế, chưa đăng được.", "TK3.01#9"),
    ("EN", "TK2"): ("ĐẠT trọn 14 cổng (T1–T14 + H26 + H29) — đã trộn lại master 27/11.", ""),
}
BG_BLOCK = {
    "EN_TK2": "Nguồn nhạc nền: `bgm_ambient_deep.mp3` (MiniMax, có dòng provenance) — chờ người dùng xác nhận quyền dùng thương mại.",
}


def fmt_num(x, nd=1):
    return f"{x:.{nd}f}".replace(".", ",")


def qc_status(lang, clip):
    if (lang, clip) in QC_BLOCK:
        s, cid = QC_BLOCK[(lang, clip)]
        if s.startswith("TRƯỢT"):
            if lang == "VN":
                return s
            if lang == "EN":
                return ("FAILS T13 — banned word “sát hại” in the script (%s) — WAITING for the user to approve a "
                        "replacement line; do not post yet." % cid)
            return ("T13不合格 — 台詞に禁止語「sát hại」（%s）— 代替文のユーザー承認待ち。投稿不可。" % cid)
    if lang == "VN":
        return "ĐẠT trọn 14 cổng (T1–T14 + H26 + H29)."
    if lang == "EN":
        return "PASSES all 14 gates (T1–T14 + H26 + H29)."
    return "14ゲートすべて合格（T1–T14 + H26 + H29）。"


def bg_line(lang, clip):
    key = f"{lang}_{clip}"
    if key in BG_BLOCK:
        return BG_BLOCK[key]
    if lang == "VN":
        return "Nguồn nhạc nền: bed đã mất file nguồn (T9/L7) — chờ người dùng xác nhận nguồn trước khi đăng."
    if lang == "EN":
        return "Music bed: the source file can no longer be traced (T9/L7) — the user must confirm the source before posting."
    return "BGM：原本ファイルを特定できません（T9/L7）— 投稿前にユーザーが出典を確認してください。"


def measure():
    m = json.loads((ROOT / ".work" / "_tk04_pkg_measure.json").read_text(encoding="utf-8"))
    # them so do QC (LUFS/TP) tu bao cao QC
    qc = {
        "VN_TK1": (-16.1, -4.2), "VN_TK2": (-16.0, -4.4), "VN_TK3": (-16.0, -4.4), "VN_TK4": (-16.1, -4.2), "VN_TK5": (-16.0, -4.3),
        "EN_TK1": (-16.3, -4.0), "EN_TK2": (-16.3, -4.5), "EN_TK3": (-16.1, -4.3), "EN_TK4": (-16.2, -4.2), "EN_TK5": (-16.1, -4.1),
        "JA_TK1": (-16.3, -4.2), "JA_TK2": (-16.0, -4.4), "JA_TK3": (-16.0, -4.3), "JA_TK4": (-16.4, -4.2), "JA_TK5": (-16.0, -4.4),
    }
    for k, v in m.items():
        lufs, tp = qc[k]
        v["lufs"], v["tp"] = lufs, tp
    return m


def build_caption(lang, clip, meas, folder):
    """Tra ve (caption_body, notes_block)."""
    cap_path = folder / f"Caption_{clip}.txt"
    raw = cap_path.read_bytes().decode("utf-8")
    body = raw.replace("\r\n", "\n")
    if "\n\n---\n" in body:          # cat khoi ghi chu da ghi (chay lai duoc)
        body = body.split("\n\n---\n")[0]
    body = body.rstrip("\n")

    lines = body.split("\n")
    # tim dong hashtag (dong bat dau bang '#')
    tag_idx = max(i for i, l in enumerate(lines) if l.lstrip().startswith("#"))
    if tag_idx == 0:
        raise SystemExit(f"{cap_path}: khong tim thay dong hashtag")
    # chen dong AIGC + dong trong truoc hashtag (trong hashtag da co 1 dong trong san)
    if AIGC[lang] not in lines:
        lines[tag_idx:tag_idx] = [AIGC[lang], ""]
    body_new = "\n".join(lines)
    aigc_line_no = lines.index(AIGC[lang]) + 1

    n_chars = len(body_new)
    dur = meas[f"{lang}_{clip}"]["dur_s"]
    mb = meas[f"{lang}_{clip}"]["size_mb"]
    nlines = meas[f"{lang}_{clip}"]["n_lines"]
    dai = len((folder / f"MoTa_Dai_{clip}.txt").read_text(encoding="utf-8").replace("\r\n", "\n").strip())
    ngan = len((folder / f"MoTa_Ngan_{clip}.txt").read_text(encoding="utf-8").replace("\r\n", "\n").strip())

    if lang == "VN":
        notes = [
            "---",
            "Ghi chú khi đăng (KHÔNG dán vào caption):",
            "- BẬT toggle “Nội dung do AI tạo” (AI-generated content) — TikTok bắt buộc nhãn AIGC.",
            f"- Dòng nhãn AIGC ĐÃ nằm sẵn trong caption (dòng thứ {aigc_line_no}): không cần thêm khi dán.",
            "- Link YouTube Tập 04: [LINK_TẬP 04 — cần điền]  ← CHƯA CÓ, phải điền trước khi đăng.",
            "  · Dán vào ô “Links / Website” trong Edit profile (chỉ ô này click được).",
            "  · URL gõ tay trong caption/bio KHÔNG click được — chỉ để người xem tự chép.",
            f"- Độ dài caption: {n_chars} ký tự (giới hạn TikTok 2.200 ký tự).",
            f"- File: {clip}_video.mp4 (1080×1920, 30 fps, H.264+AAC, {fmt_num(dur,2)} s, {fmt_num(mb,1)} MB).",
            f"- Số câu thoại: {nlines} câu.",
            f"- QC: {qc_status(lang, clip)}",
            f"- {bg_line(lang, clip)}",
            f"- BẢN MÔ TẢ DÀI ({dai} ký tự) dán vào ô Description của TikTok Studio: MoTa_Dai_{clip}.txt",
            f"- BẢN MÔ TẢ NGẮN ({ngan} ký tự) — bản rút gọn, dùng thay hoặc kèm bản dài: MoTa_Ngan_{clip}.txt",
        ]
    elif lang == "EN":
        notes = [
            "---",
            "Publishing Notes (DO NOT paste into caption):",
            "- TOGGLE ON ‘AI-generated content’ label on TikTok.",
            f"- The AIGC disclosure line is ALREADY in the caption (line {aigc_line_no}) — do not add it again when pasting.",
            "- Link to YouTube Episode 04: [LINK_EPISODE_04 — TO BE FILLED IN]  ← NOT AVAILABLE YET; fill in before posting.",
            "  · Paste it into the “Links / Website” field in Edit profile (only that field is clickable).",
            "  · A typed URL in the caption/bio is NOT clickable — viewers have to copy it.",
            f"- Caption length: {n_chars} characters (TikTok limit 2,200).",
            f"- File: {clip}_video.mp4 (1080x1920, 30 fps, H.264+AAC, {fmt_num(dur,2)} s, {fmt_num(mb,1)} MB).",
            f"- Spoken lines: {nlines}.",
            f"- QC: {qc_status(lang, clip)}",
            f"- {bg_line(lang, clip)}",
            f"- LONG description ({dai} chars) for the TikTok Studio Description field: MoTa_Dai_{clip}.txt",
            f"- SHORT description ({ngan} chars): MoTa_Ngan_{clip}.txt",
        ]
    else:
        notes = [
            "---",
            "投稿時の注意事項（キャプション本文には貼り付けないでください）：",
            "- TikTokアプリで「AI生成コンテンツ」のトグルを必ずONにしてください。",
            f"- AIGC開示文はキャプション本文の第{aigc_line_no}行目にすでに入っています（貼り付け時に重複追加しない）。",
            "- YouTube第04話へのリンク: [LINK_EPISODE_04 — 要入力]  ← 未取得、投稿前に記入してください。",
            "  · 「プロフィール編集」の「リンク」欄のみクリック可能です。",
            "  · 本文に打ったURLはクリックできません（視聴者が手動でコピー）。",
            f"- キャプション長: {n_chars}文字（TikTok上限 2,200文字）。",
            f"- 出力動画ファイル名: {clip}_video.mp4 (1080x1920, 30fps, H.264+AAC, {fmt_num(dur,2)}秒, {fmt_num(mb,1)}MB)。",
            f"- 読み上げ文: {nlines}文。",
            f"- QC: {qc_status(lang, clip)}",
            f"- {bg_line(lang, clip)}",
            f"- 詳細説明（{dai}文字）: MoTa_Dai_{clip}.txt",
            f"- 短い説明（{ngan}文字）: MoTa_Ngan_{clip}.txt",
        ]
    return body_new, "\n".join(notes)


SAFETY = {
    "VN": [
        "• Nội dung không phù hợp cho trẻ em.",
        "• Mang tính giáo dục, phân tích tâm lý tội phạm; không thay thế tư vấn y khoa hay pháp lý.",
        "• Dựa trên tư liệu công khai (hồ sơ toà án, báo chí điều tra). Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.",
        "• Nhân vật Cú, Sói, Cáo là linh thú minh họa; lời thoại phục dựng dựa trên tư liệu điều tra.",
        "• Giọng đọc, hình ảnh và âm nhạc được tạo bằng công cụ AI.",
        "",
        "🆘 Nếu bạn biết một trẻ em đang bị bạo hành hoặc lạm dụng y tế, hãy gọi Tổng đài quốc gia bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).",
    ],
    "EN": [
        "• Not suitable for children.",
        "• Educational criminal-psychology analysis only — not a substitute for medical or legal advice.",
        "• Based on public records (court transcripts, investigative journalism). This channel does not accuse, defame or disparage any individual.",
        "• The characters Cú, Sói, Cáo are illustrative animal personas; the dialogue is dramatised from investigative material.",
        "• Voice, visuals and music are AI-generated.",
        "",
        "🆘 If you know a child is being abused or medically neglected, call the national child-protection hotline 111 (Vietnam, free, 24/7).",
    ],
    "JA": [
        "• 子ども向けコンテンツではありません。",
        "• 教育目的の犯罪心理分析であり、医療・法律上の助言の代わりにはなりません。",
        "• 公開資料（裁判記録・捜査報道）に基づきます。本チャンネルは个人を告発・名誉毀損・中傷するものではありません。",
        "• キャラクター（Cú・Sói・Cáo）は寓情的動物 персонаであり、台詞は捜査資料に基づく脚色です。",
        "• 音声・映像・音楽はすべてAIで生成しています。",
        "",
        "🆘 子どもの虐待や医療的ネグレクトを知っている場合は、児童虐待相談専用ダイヤル（189・24時間）へご連絡ください。",
    ],
}

TITLE = {
    "VN": "MÔ TẢ ĐỂ ĐĂNG — CLIP TIKTOK TẬP 04 (tiếng Việt)",
    "EN": "POSTING PACKAGE — TIKTOK CLIPS EPISODE 04 (English)",
    "JA": "投稿パッケージ — TikTokクリップ 第04話（日本語）",
}

SEC_A = {
    "VN": "CAPTION DÁN VÀO TIKTOK",
    "EN": "CAPTION TO PASTE INTO TIKTOK",
    "JA": "TikTok に貼り付けるキャプション",
}
SEC_A2 = {
    "VN": "LINK YOUTUBE — ĐẶT VÀO BIO (chỉ ô này click được)",
    "EN": "YOUTUBE LINK — GOES IN BIO (only that field is clickable)",
    "JA": "YouTubeリンク — プロフィールの「リンク」欄へ（ここだけクリック可）",
}
SEC_B = {
    "VN": "DÒNG BẮT BUỘC KÈM THEO (TikTok bắt buộc nhãn AIGC)",
    "EN": "REQUIRED DISCLOSURE LINE (TikTok mandates the AIGC label)",
    "JA": "必須の開示文（TikTokのAI生成コンテンツ表示義務）",
}
SEC_C = {
    "VN": "LƯU Ý AN TOÀN + HOTLINE (dán thêm nếu muốn đồng nhất với mô tả tập YouTube)",
    "EN": "SAFETY NOTES + HOTLINE (optional extra block)",
    "JA": "安全上の注意 + ホットライン（任意で追加）",
}
SEC_D = {
    "VN": "GHI CHÚ KỸ THUẬT",
    "EN": "TECHNICAL NOTES",
    "JA": "技術メモ",
}

A2_BLOCK = {
    "VN": [
        "[LINK_TẬP 04 — CHƯA CÓ, phải điền trước khi đăng]",
        "",
        "• Path: Profile → Edit profile → Links (hoặc Website) → Add → dán URL → Save.",
        "• Điều kiện: ≥ 1.000 follower (tài khoản cá nhân) HOẶC Verified Business Account; chỉ làm được trên app.",
        "• URL gõ tay trong caption / bio / bình luận KHÔNG click được — chỉ để người xem tự chép.",
        "• Nếu TikTok gỡ link YouTube khỏi ô Links: dùng 1 trang link-in-bio trên domain riêng rồi trỏ ô Links về trang đó.",
        "• Tập 01 (đã có): https://youtu.be/lDVXjeFLn48",
    ],
    "EN": [
        "[LINK_EPISODE_04 — NOT AVAILABLE YET, must be filled in before posting]",
        "",
        "• Path: Profile → Edit profile → Links (or Website) → Add → paste URL → Save.",
        "• Requirement: ≥ 1,000 followers (personal account) OR Verified Business Account; app only.",
        "• A typed URL in caption / bio / comments is NOT clickable — viewers must copy it manually.",
        "• If TikTok strips the YouTube link from the Links field: use a link-in-bio page on your own domain.",
        "• Episode 01 (available): https://youtu.be/lDVXjeFLn48",
    ],
    "JA": [
        "[LINK_EPISODE_04 — 未取得。投稿前に記入してください]",
        "",
        "• 手順: プロフィール → プロフィール編集 → リンク（またはウェブサイト）→ Add → URL を貼り付け → Save。",
        "• 条件: フォロワー1,000人以上（個人アカウント）または認証済みビジネスアカウント。アプリからのみ実行可能。",
        "• 本文・プロフィール・コメントに打ったURLはクリックできません（視聴者が手動コピー）。",
        "• YouTubeリンクがTikTokに削除される場合の代替: 自ドメインのlink-in-bioページを用意し「リンク」欄をそこに向ける。",
        "• 第01話（公開済み）: https://youtu.be/lDVXjeFLn48",
    ],
}

B_BLOCK = {
    "VN": [
        "Dòng nhãn AIGC đã nằm SẴN trong phần [A] của cả 5 caption (dòng thứ 9) — không cần thêm khi dán.",
        "",
        "→ BẬT toggle “Nội dung do AI tạo” (AI-generated content) trong bước đăng.",
        "",
        "Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.",
    ],
    "EN": [
        "The AIGC line is ALREADY inside every caption in [A] (line 9) — do not add it again when pasting.",
        "",
        "→ TOGGLE ON ‘AI-generated content’ in the posting step.",
        "",
        "Content created with AI assistance for behavioral analysis. Viewer discretion advised.",
    ],
    "JA": [
        "AIGC開示文は[ A ]の5本すべてのキャプション本文にすでに入っています（9行目）— 貼り付け時に追加不要。",
        "",
        "→ 投稿時に「AI生成コンテンツ」のトグルをONにしてください。",
        "",
        "AI技術を活用して心理分析目的で制作されたコンテンツです。閲覧にはご注意ください。",
    ],
}


def build_mota(lang, folder, meas, bodies):
    L = []
    A = L.append
    durs = [meas[f"{lang}_{c}"]["dur_s"] for c in CLIPS]
    mbs = [meas[f"{lang}_{c}"]["size_mb"] for c in CLIPS]
    A(TITLE[lang])
    A("=" * len(TITLE[lang]))
    A(f"Files: {', '.join(f'{c}_video.mp4' for c in CLIPS)}")
    A(f"1080×1920 · 30 fps · H.264 + AAC · {fmt_num(min(durs),2)}–{fmt_num(max(durs),2)} s · {fmt_num(min(mbs),1)}–{fmt_num(max(mbs),1)} MB/clip")
    A("Chỉ dẫn gốc: 02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md mục 4 — Bước 8 (đóng gói)")
    A("Báo cáo QC: 02_SAN_XUAT/TIKTOK/Tap04/BAO_CAO_QC_TIKTOK_TAP04.md")
    A("")
    for c in CLIPS:
        n = len(bodies[c][0])
        A(f"[{SEC_A[lang]} — {c} ({n} ký tự — giới hạn 2.200)" if lang == "VN" else
          f"[{SEC_A[lang]} — {c} ({n} characters — limit 2,200)" if lang == "EN" else
          f"[{SEC_A[lang]} — {c}（{n}文字・上限2,200）")
        A("-" * 60)
        A(bodies[c][0])
        A("")
    A(f"[{SEC_A2[lang]}]")
    A("-" * 60)
    for l in A2_BLOCK[lang]:
        A(l)
    A("")
    A(f"[{SEC_B[lang]}]")
    A("-" * 60)
    for l in B_BLOCK[lang]:
        A(l)
    A("")
    A(f"[{SEC_C[lang]}]")
    A("-" * 60)
    for l in SAFETY[lang]:
        A(l)
    A("")
    A(f"[{SEC_D[lang]}]")
    A("-" * 60)
    hdr = ("| Clip | Thời lượng | MB | LUFS | TP dBFS | Câu | QC |" if lang == "VN" else
           "| Clip | Duration | MB | LUFS | TP dBFS | Lines | QC |" if lang == "EN" else
           "| クリップ | 再生時間 | MB | LUFS | TP dBFS | 文数 | QC |")
    A(hdr)
    A("|---|---:|---:|---:|---:|---:|---|")
    for c in CLIPS:
        m = meas[f"{lang}_{c}"]
        st = qc_status(lang, c)
        st = ("TRƯỢT T13 (từ cấm)" if st.startswith("TRƯỢT") else
              "ĐẠT 14 cổng" if lang == "VN" else
              "PASS 14 gates" if lang == "EN" else "14ゲート合格")
        A(f"| {c} | {fmt_num(m['dur_s'],2)} s | {fmt_num(m['size_mb'],1)} | {fmt_num(m['lufs'],1)} | {fmt_num(m['tp'],1)} | {m['n_lines']} | {st} |")
    A("")
    if lang == "VN":
        A("- Cổng QC: T1–T14 + H26 (không chữ trên khung) + H29 (logo góc trên-phải x 684–780, y 60–156).")
        A("- Không dán phần “Ghi chú khi đăng” của file Caption_TK*.txt vào caption.")
        A("- 2 clip VN TK1/TK3 TRƯỢT T13 (từ cấm “sát hại” trong kịch bản) — CHỜ người dùng duyệt câu thay thế.")
        A("- 14 clip có nhạc nền chưa truy vết được file nguồn (T9/L7) — chờ người dùng xác nhận.")
    elif lang == "EN":
        A("- QC gates: T1–T14 + H26 (no text overlay) + H29 (logo top-right x 684–780, y 60–156).")
        A("- Do NOT paste the “Publishing Notes” block of Caption_TK*.txt into the caption.")
        A("- The music bed of 14 clips can no longer be traced to a source file (T9/L7) — the user must confirm the source before posting.")
    else:
        A("- QCゲート: T1–T14 + H26（画面文字なし）+ H29（右上ロゴ x 684–780, y 60–156）。")
        A("- Caption_TK*.txt の「投稿時の注意事項」は本文に貼り付けないでください。")
        A("- 14クリップのBGMは原本ファイルを特定できていません（T9/L7）— 用户的確認待ち。")
    return "\n".join(L)


def build_checklist(lang, folder, meas, cap_range):
    L = []
    A = L.append
    if lang == "VN":
        A("# CHECKLIST ĐĂNG — CLIP TIKTOK TẬP 04 (tiếng Việt)")
        A("")
        A("*Ngày lập: 27/11/2026 · 5 clip · báo cáo QC: `BAO_CAO_QC_TIKTOK_TAP04.md` · đóng gói: `mo_ta.txt` (file này) · caption: `Caption_TK*.txt`*")
        A("")
        A("## 1. Từng clip")
        A("")
        A("| # | Clip | File video | QC 14 cổng | Caption + nhãn AIGC | Toggle AIGC khi đăng | Link Tập 04 trong bio | Lưu ý an toàn | Trạng thái | Ngày đăng |")
        A("|---|---|---|---|---|---|---|---|---|---|")
    elif lang == "EN":
        A("# POSTING CHECKLIST — TIKTOK CLIPS EPISODE 04 (English)")
        A("")
        A("*Created: 27/11/2026 · 5 clips · QC report: `BAO_CAO_QC_TIKTOK_TAP04.md` · package: `mo_ta.txt` · captions: `Caption_TK*.txt`*")
        A("")
        A("## 1. Per clip")
        A("")
        A("| # | Clip | Video file | QC 14 gates | Caption + AIGC line | AIGC toggle at posting | Ep.04 link in bio | Safety notes | Status | Date posted |")
        A("|---|---|---|---|---|---|---|---|---|---|")
    else:
        A("# 投稿チェックリスト — TikTokクリップ 第04話（日本語）")
        A("")
        A("*作成日: 27/11/2026 · 5クリップ · QC報告: `BAO_CAO_QC_TIKTOK_TAP04.md` · パッケージ: `mo_ta.txt` · キャプション: `Caption_TK*.txt`*")
        A("")
        A("## 1. クリップ別")
        A("")
        A("| # | クリップ | 動画ファイル | QC 14ゲート | キャプション+AIGC文 | 投稿時AIGCトグル | 第04話リンク | 安全上の注意 | 状態 | 投稿日 |")
        A("|---|---|---|---|---|---|---|---|---|---|")

    for i, c in enumerate(CLIPS, 1):
        st = qc_status(lang, c)
        blocked = st.startswith("TRƯỢT")
        if blocked:
            status = ("CHẶN — chờ duyệt kịch bản (từ cấm “sát hại”)" if lang == "VN" else
                      "BLOCKED — awaiting script approval (banned word)" if lang == "EN" else
                      "ブロック — 台詞承認待ち（禁止語）")
        else:
            status = ("CHỜ — link YouTube Tập 04 + xác nhận nguồn nhạc nền" if lang == "VN" else
                      "PENDING — Ep.04 YouTube link + BGM source confirmation" if lang == "EN" else
                      "保留 — 第04話のYouTubeリンク+BGM出典の確認待ち")
        qcell = ("TRƯỢT T13" if lang == "VN" else "FAIL T13" if lang == "EN" else "T13不合格") if blocked else \
                ("ĐẠT 14 cổng" if lang == "VN" else "PASS 14" if lang == "EN" else "14合格")
        A(f"| {i} | {c} | {c}_video.mp4 | {qcell} | ☑ | ☐ | ☐ | ☐ | {status} | |")

    A("")
    if lang == "VN":
        A("## 2. Việc chung của tập (làm 1 lần, trước clip đầu tiên)")
        A("")
        A("| # | Việc | Trạng thái |")
        A("|---|---|---|")
        A("| 1 | Điền link YouTube Tập 04 vào ô Links/Website của bio | ☐ CHƯA CÓ link (Tập 01: `https://youtu.be/lDVXjeFLn48`) |")
        A("| 2 | BẬT toggle “Nội dung do AI tạo” (AIGC) mặc định khi đăng | ☐ |")
        A("| 3 | Xác nhận nguồn nhạc nền 14 clip (T9/L7 — bed đã mất file nguồn) | ☐ CHỜ người dùng |")
        A("| 4 | Duyệt câu thay thế cho 2 từ cấm `sát hại` (VN TK1/TK3) + chạy lại TTS → ASR → render → QC | ☐ CHỜ người dùng |")
        A("| 5 | Đặt tài khoản 18+ (nội dung hồ sơ tội phạm) | ☐ |")
        A("| 6 | Chọn thẻ bìa (cover) 9:16 | ☐ |")
        A("| 7 | Đăng **bản master sạch** (`TKn_video.mp4`), không tải lại từ YouTube | ☐ |")
        A("")
        A("## 3. Cảnh báo trước khi đăng")
        A("")
        A("- **VN TK1 và VN TK3 TRƯỢT cổng T13** (từ cấm `sát hại` trong kịch bản gốc) — **chưa được đăng** cho tới khi có câu thay thế được duyệt và dựng lại clip.")
        A("- **14 clip có nhạc nền chưa truy vết được file nguồn** (T9/L7) — cần người dùng xác nhận nguồn trước khi đăng. Riêng **EN TK2** dùng `bgm_ambient_deep.mp3` (có provenance đầy đủ).")
        A("- Link YouTube Tập 04 **chưa có** — caption dùng placeholder `[LINK_TẬP 04 — cần điền]`.")
        A("- **Không dán** khối “Ghi chú khi đăng” (sau dấu `---`) vào caption.")
        A(f"- Caption + nhãn AIGC: độ dài mỗi caption {fmt_num(cap_range[0],0)}–{fmt_num(cap_range[1],0)} ký tự (VN), "
          f"{fmt_num(cap_range[2],0)}–{fmt_num(cap_range[3],0)} (EN), {fmt_num(cap_range[4],0)}–{fmt_num(cap_range[5],0)} (JA) — dưới trần 2.200.")
    elif lang == "EN":
        A("## 2. Episode-wide tasks (do once, before the first clip)")
        A("")
        A("| # | Task | Status |")
        A("|---|---|---|")
        A("| 1 | Put the Episode 04 YouTube link into the bio Links/Website field | ☐ NO LINK YET (Ep. 01: `https://youtu.be/lDVXjeFLn48`) |")
        A("| 2 | Turn the ‘AI-generated content’ toggle ON by default when posting | ☐ |")
        A("| 3 | Confirm the BGM source for the 14 clips (T9/L7 — source file lost) | ☐ AWAITING USER |")
        A("| 4 | Approve replacement wording for the banned word in VN TK1/TK3, then re-run TTS → ASR → render → QC | ☐ AWAITING USER |")
        A("| 5 | Set the account to 18+ (true-crime case material) | ☐ |")
        A("| 6 | Pick a 9:16 cover | ☐ |")
        A("| 7 | Post the **clean master** (`TKn_video.mp4`), never a re-download from YouTube | ☐ |")
        A("")
        A("## 3. Warnings before posting")
        A("")
        A("- **VN TK1 and VN TK3 FAIL gate T13** (banned word `sát hại` in the original script) — **do not post** until the replacement line is approved and the clips are re-rendered.")
        A("- **14 clips have a music bed whose source file can no longer be traced** (T9/L7) — the user must confirm the source before posting. **EN TK2** uses `bgm_ambient_deep.mp3` (full provenance).")
        A("- The Episode 04 YouTube link **does not exist yet** — captions carry the placeholder `[LINK_EPISODE_04 — TO BE FILLED IN]`.")
        A("- **Do NOT paste** the “Publishing Notes” block (after the `---` line) into the caption.")
        A(f"- Caption + AIGC line length: {fmt_num(cap_range[2],0)}–{fmt_num(cap_range[3],0)} characters (EN) — well under the 2,200 limit.")
    else:
        A("## 2. 第04話共通作業（最初の1本目の前に1回だけ）")
        A("")
        A("| # | 作業 | 状態 |")
        A("|---|---|---|")
        A("| 1 | 第04話のYouTubeリンクをプロフィールの「リンク」欄へ | ☐ リンク未取得（第01話: `https://youtu.be/lDVXjeFLn48`） |")
        A("| 2 | 投稿時に「AI生成コンテンツ」トグルを既定でON | ☐ |")
        A("| 3 | 14クリップのBGM出典を確認（T9/L7 — 原本ファイル消失） | ☐ ユーザーの確認待ち |")
        A("| 4 | VN TK1/TK3の禁止語の代替台詞を承認し、TTS→ASR→再レンダリング→QCを再実行 | ☐ ユーザーの承認待ち |")
        A("| 5 | アカウントを18+に設定（実録・犯罪心理系） | ☐ |")
        A("| 6 | 9:16の表紙を選択 | ☐ |")
        A("| 7 | **クリーンマスター**（`TKn_video.mp4`）を投稿（YouTubeからの再ダウンロードは不可） | ☐ |")
        A("")
        A("## 3. 投稿前の注意")
        A("")
        A("- **VN TK1とVN TK3はT13ゲート不合格**（原台詞に禁止語 `sát hại`）— 代替文の承認と再レンダリングが完了するまで**投稿不可**。")
        A("- **14クリップのBGMは原本ファイルを特定できません**（T9/L7）— 投稿前にユーザーが出典を確認する必要があります。**EN TK2**のみ `bgm_ambient_deep.mp3`（provenance完備）。")
        A("- 第04話のYouTubeリンクは**未取得** — キャプションは `[LINK_EPISODE_04 — 要入力]` のプレースホルダー。")
        A("- 「投稿時の注意事項」（`---` の後）は本文に貼り付けないでください。")
        A(f"- キャプション+AIGC文の長さ: {fmt_num(cap_range[4],0)}–{fmt_num(cap_range[5],0)}文字（JA）— 上限2,200文字を大きく下回ります。")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    args = ap.parse_args()
    meas = measure()

    # vong 1: dung caption moi cho 3 ngon ngu
    all_bodies = {}
    for lang, d in LANGS:
        folder = TK / d
        bodies = {}
        for c in CLIPS:
            body, notes = build_caption(lang, c, meas, folder)
            bodies[c] = (body, notes)
        all_bodies[lang] = (folder, bodies)

    # dai caption (phan dan, chua kem khoi ghi chu) theo ngon ngu
    cap_range = []
    for lang, _ in LANGS:
        ns = [len(all_bodies[lang][1][c][0]) for c in CLIPS]
        cap_range += [min(ns), max(ns)]

    written = []
    for lang, d in LANGS:
        folder, bodies = all_bodies[lang]
        for c in CLIPS:
            body, notes = bodies[c]
            new = body + "\n\n" + notes
            if args.write:
                (folder / f"Caption_{c}.txt").write_bytes(new.replace("\n", "\r\n").encode("utf-8"))
            written.append(f"{d}/Caption_{c}.txt")
        mota = build_mota(lang, folder, meas, bodies)
        chk = build_checklist(lang, folder, meas, cap_range)
        if args.write:
            (folder / "mo_ta.txt").write_bytes((mota + "\r\n").replace("\n", "\r\n").encode("utf-8"))
            (folder / "checklist_dang.md").write_bytes((chk + "\r\n").replace("\n", "\r\n").encode("utf-8"))
        written += [f"{d}/mo_ta.txt", f"{d}/checklist_dang.md"]
    print(("DA GHI " if args.write else "SE GHI ") + str(len(written)) + " file:")
    for w in written:
        print("  ", w)
    print("DAI CAPTION (ky tu):", cap_range)


if __name__ == "__main__":
    main()
