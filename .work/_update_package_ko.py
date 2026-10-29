# -*- coding: utf-8 -*-
from pathlib import Path

p = Path(r"D:\TEST\Gax\Audi\.work\package.py")
content = p.read_text(encoding="utf-8")

# 1. Update font and geometry in thumbnail()
t_thumb = '''    font_name = "YuGothB.ttc" if ED.JA else "segoeuib.ttf"
    f = ImageFont.truetype(str(FONTS / font_name), 70 if (ED.EN or ED.JA) else 86)
    dy, y0 = (96, 260) if (ED.EN or ED.JA) else (108, 250)'''
r_thumb = '''    font_name = "malgunbd.ttf" if ED.KO else ("YuGothB.ttc" if ED.JA else "segoeuib.ttf")
    f = ImageFont.truetype(str(FONTS / font_name), 70 if (ED.EN or ED.JA or ED.KO) else 86)
    dy, y0 = (96, 260) if (ED.EN or ED.JA or ED.KO) else (108, 250)'''
if t_thumb in content:
    content = content.replace(t_thumb, r_thumb, 1)

# 2. Update description() dispatch
t_desc = '''def description():
    if ED.JA:
        return description_ja()
    if ED.EN:
        return description_en()'''
r_desc = '''def description():
    if ED.KO:
        return description_ko()
    if ED.JA:
        return description_ja()
    if ED.EN:
        return description_en()'''
if t_desc in content:
    content = content.replace(t_desc, r_desc, 1)

# 3. Add description_ko() before description_ja()
t_dja = 'def description_ja():'
r_dja = '''def description_ko():
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


def description_ja():'''
if t_dja in content:
    content = content.replace(t_dja, r_dja, 1)

# 4. Update verified_links()
t_vlink = 'src_p = ED.EP_DIR / ("nguon_tham_khao_JA.md" if ED.JA else "nguon_tham_khao_EN.md")'
r_vlink = 'src_p = ED.EP_DIR / ("nguon_tham_khao_KO.md" if ED.KO else ("nguon_tham_khao_JA.md" if ED.JA else "nguon_tham_khao_EN.md"))'
content = content.replace(t_vlink, r_vlink)

p.write_text(content, encoding="utf-8")
print("Updated package.py successfully")
