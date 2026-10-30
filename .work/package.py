#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B10 — mux picture + audio, thumbnail, YouTube description (plan v9 section 9)."""
import json
import re
import subprocess
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, str(Path(__file__).parent))
import edition as ED  # noqa: E402  (AE_LANG=en -> English edition)

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8"))["shots"]
FONTS = Path(r"C:\Windows\Fonts")
OUT_DIR = ED.OUT_DIR                                       # thành phẩm của tập


def mux():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / (ED.MASTER + ".mp4")
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(ED.w("video3") / "picture.mp4"),
                    "-i", str(ED.w("audio_master.wav")), "-map", "0:v", "-map", "1:a",
                    "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest",
                    "-movflags", "+faststart", str(out)], check=True)
    return out


def thumbnail():
    bg = Image.open(ROOT / "assets" / "bg" / (ED.EP.get("thumb_bg", "house_police") + ".png")).convert("RGB").resize((1280, 720), Image.LANCZOS)
    bg = Image.blend(bg, Image.new("RGB", bg.size, (10, 10, 14)), 0.35).convert("RGBA")
    g = Image.new("L", (1280, 720), 0)
    ImageDraw.Draw(g).rectangle([0, 360, 1280, 720], fill=200)
    g = g.filter(ImageFilter.GaussianBlur(120))
    bg.paste(Image.new("RGBA", bg.size, (0, 0, 0, 255)), (0, 0), g)
    for role, x, flip in (("D", -90, False), ("C", 990, True)):
        p = Image.open(ROOT / "assets" / "cast" / role / "P1.png").convert("RGBA").resize((380, 452), Image.LANCZOS)
        if flip:
            p = p.transpose(Image.FLIP_LEFT_RIGHT)
        bg.alpha_composite(p, (x, 720 - 452))
    d = ImageDraw.Draw(bg)
    font_name = "malgunbd.ttf" if ED.KO else ("YuGothB.ttc" if ED.JA else "segoeuib.ttf")
    f = ImageFont.truetype(str(FONTS / font_name), 70 if (ED.EN or ED.JA or ED.KO) else 86)
    dy, y0 = (96, 260) if (ED.EN or ED.JA or ED.KO) else (108, 250)
    lines = ED.EP["thumb"]
    for i, line in enumerate(lines):
        w = d.textlength(line, font=f)
        d.text(((1280 - w) / 2 + 4, y0 + i * dy + 4), line, font=f, fill=(0, 0, 0, 200))
        d.text(((1280 - w) / 2, y0 + i * dy), line, font=f, fill=(242, 239, 233, 255))
    logo = Image.open(ROOT / "assets" / "brand" / "logo_mark.png").convert("RGBA").resize((150, 150), Image.LANCZOS)
    bg.alpha_composite(logo, (565, 60))
    bg.convert("RGB").save(OUT_DIR / "thumbnail.png")


def mmss(t):
    return f"{int(t // 60):02d}:{int(t % 60):02d}"


def description():
    if ED.KO:
        return description_ko()
    if ED.JA:
        return description_ja()
    if ED.EN:
        return description_en()
    act_titles = ED.EP["act_titles"]
    starts = {1: 20.5}
    for m in TL["markers"]:
        if m["type"] == "ACT":
            starts[m["act"]] = m["start"]
    chap = ["00:00 Intro"] + [f"{mmss(starts[a])} {act_titles[a]}" for a in sorted(starts)]
    sents = {i["id"]: i["text"] for i in TL["items"]}
    summary = " ".join(sents[k] for k in ED.EP["summary"])
    txt = f"""{ED.EP["title"]} | Amber eyes

{summary}

⏱ MỐC CHƯƠNG
{chr(10).join(chap)}

⚠️ LƯU Ý
• Nội dung không phù hợp cho trẻ em.
• Nội dung mang tính giáo dục, phân tích dưới góc nhìn tâm lý học tội phạm;
  không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Thông tin dựa trên tư liệu công khai (hồ sơ tòa án, báo chí) — xem nguồn bên dưới.
  Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là nhân vật minh hoạ, không phải người thật.
  Lời của Điều tra viên, Chuyên gia và Người dân là lời dựng lại dựa trên tư liệu.
• Giọng đọc, hình ảnh và âm nhạc được tạo cho kênh bằng công cụ AI.

📚 NGUỒN THAM KHẢO
[CHƯA CÓ — phải bổ sung nguồn công khai đã kiểm chứng trước khi đăng, xem nguon_tham_khao.md]

🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia
bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).
"""
    (OUT_DIR / "mo_ta.txt").write_text(txt, encoding="utf-8")
    need = ED.EP["need"]
    md = ["# NGUỒN THAM KHẢO — CẦN BỔ SUNG TRƯỚC KHI ĐĂNG", "",
          "Mỗi dòng cần một nguồn công khai có link mở được (hồ sơ tòa án, bài báo). **Không được bịa nguồn.**", "",
          "| Câu | Nội dung | Nguồn (link) |", "|---|---|---|"]
    md += [f"| `{k}` | {sents[k][:140]} | |" for k in need]
    (OUT_DIR / "nguon_tham_khao.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    return chap


def description_en():
    """English edition: description.txt from CHU_CO_DINH_EN.md (the fenced block that holds
    the ⏱ CHAPTERS list), chapter times measured from the EN timeline, SOURCES = the verified
    (✅) links of nguon_tham_khao_EN.md. The sources file itself is never rewritten."""
    act_titles = ED.EP["act_titles"]
    starts = {1: 20.5}
    for m in TL["markers"]:
        if m["type"] == "ACT":
            starts[m["act"]] = m["start"]
    chap = ["00:00 Intro"] + [f"{mmss(starts[a])} {act_titles[a]}" for a in sorted(starts)]
    tpl = (ED.EP_DIR / "CHU_CO_DINH_EN.md").read_text(encoding="utf-8")
    body = pick_block(tpl)
    body = repl_chapters(body, ["00:00"] + [mmss(starts[a]) for a in sorted(starts)])
    links = verified_links()
    src = ("📚 SOURCES\n" + (links if links else
            "[PENDING — add the verified public links from nguon_tham_khao_EN.md before publishing]")
            + "\n\n")
    if "📚 SOURCES" in body:
        body = re.sub(r"📚 SOURCES\n(?:.*\n)*?(?=\n)", src, body, count=1)
    else:
        m = re.search(r"^#\S", body, re.M)
        body = body[:m.start()] + src + body[m.start():] if m else body.rstrip() + "\n\n" + src
    (OUT_DIR / "description.txt").write_text(body, encoding="utf-8")
    (OUT_DIR / "mo_ta.txt").write_text(body, encoding="utf-8")
    return chap


def pick_block(tpl):
    """Khối ``` ... ``` trong CHU_CO_DINH_EN.md có chứa mốc CHAPTERS (bản Tập 01 ở §7, Tập 02 ở §4)."""
    best = None
    for m in re.finditer(r"```(?:text)?\n(.*?)```", tpl, re.S):
        if "CHAPTERS" in m.group(1):
            best = m.group(1)
    if best is None:
        raise SystemExit("không tìm thấy khối mô tả có mốc CHAPTERS trong CHU_CO_DINH_EN.md")
    return best


def repl_chapters(body, times):
    """Giữ nguyên nhãn chương trong tài liệu, thay bằng mốc thời gian đo thực tế."""
    def f(m):
        out, k = [], 0
        for l in m.group(1).split("\n"):
            if re.match(r"^\d\d:\d\d\s", l) and k < len(times):
                l = times[k] + l[5:]
                k += 1
            out.append(l)
        return "⏱ CHAPTERS\n" + "\n".join(out)
    return re.sub(r"⏱ CHAPTERS\n((?:\d\d:\d\d .*\n)+)", f, body)


def description_ko():
    """Korean edition: description.txt and mo_ta.txt with measured chapter times,
    proper Korean disclaimers, and verified source links."""
    act_titles = ED.EP["act_titles"]
    starts = {1: 20.5}
    for m in TL["markers"]:
        if m["type"] == "ACT":
            starts[m["act"]] = m["start"]
    chap = ["00:00 오프닝"] + [f"{mmss(starts[a])} {act_titles[a]}" for a in sorted(starts)]
    sents = {i["id"]: i["text"] for i in TL["items"]}
    summary = " ".join(sents[k] for k in ED.EP["summary"])
    raw_title = ED.EP["title"]
    title = raw_title if "Amber eyes" in raw_title else f"{raw_title} | Amber eyes"
    links = verified_links()
    src_text = links if links else "[출처 미확인 — 공개 기록의 출처 링크를 추가해주세요]"
    body = f"""{title}

{summary}

⏱ 챕터(타임라인)
{chr(10).join(chap)}

⚠️ 시청 전 유의사항
• 본 콘텐츠는 청소년에게 적합하지 않을 수 있습니다.
• 본 영상은 범죄심리학 및 교육적 관점에서의 분석 콘텐츠이며, 의학적, 심리학적 또는 법률적 조언을 대신할 수 없습니다.
• 공식 공개 기록(법원 판결문, 수사 기록, 언론 보도)을 바탕으로 제작되었습니다.
  특정인을 비방하거나 단죄하려는 의도가 없습니다.
• 등장하는 올빼미(호스트), 늑대(수사관), 여우(심리학자), 양(증인), 고양이(시청자)는 연출을 위한 가상 캐릭터입니다.
• 본 영상의 음성, 시각 자료 및 음악은 AI 기술을 활용하여 제작되었습니다.

📚 참고자료 및 출처(References)
{src_text}

🆘 아동학대 예방 및 신고 상담전화
주변에 학대받거나 방치된 아동을 발견하시면 국번없이 112(경찰청) 또는 129(보건복지상담센터)로 신고해 주시기 바랍니다.
"""
    (OUT_DIR / "description.txt").write_text(body, encoding="utf-8")
    (OUT_DIR / "mo_ta.txt").write_text(body, encoding="utf-8")
    return chap


def description_ja():
    """Japanese edition: description.txt and mo_ta.txt with measured chapter times,
    proper Japanese disclaimers, and verified source links."""
    act_titles = ED.EP["act_titles"]
    starts = {1: 20.5}
    for m in TL["markers"]:
        if m["type"] == "ACT":
            starts[m["act"]] = m["start"]
    chap = ["00:00 オープニング"] + [f"{mmss(starts[a])} {act_titles[a]}" for a in sorted(starts)]
    sents = {i["id"]: i["text"] for i in TL["items"]}
    summary = " ".join(sents[k] for k in ED.EP["summary"])
    raw_title = ED.EP["title"]
    title = raw_title if "Amber eyes" in raw_title else f"{raw_title} | Amber eyes"
    links = verified_links()
    src_text = links if links else "[未確認 — 公開記録の出典リンクを追加してください]"
    body = f"""{title}

{summary}

⏱ 目次（チャプター）
{chr(10).join(chap)}

⚠️ ご視聴にあたっての注意事項
• 本動画はお子様向けではありません。
• 本動画は教育目的および犯罪心理学の観点からの分析・解説コンテンツであり、
  医学的、心理学的、または法的なアドバイスに代わるものではありません。
• 公開記録（裁判資料、報道記録、公式インタビュー等）に基づいて制作されています。
  動画内の心理分析はチャンネル独自の見解・考察であり、特定の個人に対する臨床的診断ではありません。
  特定の個人を告発、中傷、または美化する意図は一切ありません。
• 登場するキャラクター（フクロウ、オオカミ、キツネ、羊、猫）は演出用の架空のキャラクターです。
  捜査官、心理学者、住民、視聴者の発言は公開記録に基づいて構成されたドラマタイズであり、
  実在の特定の人物や団体を代表するものではありません。
• 音声、画像、音楽はAIツールを活用して制作されています。

📚 参考資料・出典
{src_text}

🆘 児童虐待に関する相談窓口
もし虐待を受けている子ども、または虐待の疑いがある子どもに気づいた場合は、
児童相談所虐待対応ダイヤル「189（いちはやく）」（通話料無料・24時間対応）へご連絡ください。
緊急の場合は110番または119番通報を行ってください。
"""
    (OUT_DIR / "description.txt").write_text(body, encoding="utf-8")
    (OUT_DIR / "mo_ta.txt").write_text(body, encoding="utf-8")
    return chap


def verified_links():
    """Các link đã đánh dấu ✅ trong nguon_tham_khao_JA.md / nguon_tham_khao_EN.md."""
    src_p = ED.EP_DIR / ("nguon_tham_khao_KO.md" if ED.KO else ("nguon_tham_khao_JA.md" if ED.JA else "nguon_tham_khao_EN.md"))
    if not src_p.exists():
        if ED.EN:
            write_sources_en()
        src_p = ED.EP_DIR / ("nguon_tham_khao_KO.md" if ED.KO else ("nguon_tham_khao_JA.md" if ED.JA else "nguon_tham_khao_EN.md"))
    if not src_p.exists():
        return ""
    links = []
    for row in src_p.read_text(encoding="utf-8").splitlines():
        if row.startswith("| `") or row.startswith("| Mô tả") or row.startswith("| `1.") or row.startswith("| `2.") or row.startswith("| `3.") or row.startswith("| `4.") or row.startswith("| `5."):
            cells = [c.strip() for c in row.strip("|").split("|")]
            if len(cells) >= 4 and cells[3].startswith("✅"):
                for u in re.findall(r"https?://\S+", cells[2]):
                    if u not in links:
                        links.append(u)
    return "\n".join(links)


def write_sources_en():
    """Tạo bảng nguồn (khung rỗng) cho bản EN — KHÔNG bịa nguồn, người dùng điền link đã kiểm chứng."""
    sents = {i["id"]: i["text"] for i in TL["items"]}
    md = ["# SOURCES · EPISODE 02 (ENGLISH EDITION) — TO BE FILLED BEFORE PUBLISHING", "",
          "Every factual claim in `kichban_tap02_EN.md` needs at least one **openable public source**",
          "(court records, police releases, reputable news archives). **Do not fabricate sources.**", "",
          "- ✅ = source verified against the line.",
          "- ⚠ = only a secondary/aggregator source; find the original before publishing.", "",
          "Copy the ✅ links into the **📚 SOURCES** section of the YouTube description before upload.", "",
          "| Câu | Dữ kiện | Nguồn | |", "|---|---|---|---|"]
    for k in ED.EP["need"]:
        md.append(f"| `{k}` | {sents.get(k, '')} | — | ⚠ chưa có nguồn |")
    (ED.EP_DIR / "nguon_tham_khao_EN.md").write_text("\n".join(md) + "\n", encoding="utf-8")


if __name__ == "__main__":
    import sys
    if "--mux" in sys.argv:
        print("mux ->", mux())
    thumbnail()
    print("\n".join(description()))
