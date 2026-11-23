# -*- coding: utf-8 -*-
"""Generate 02_SAN_XUAT/Ho_So_Toi_Pham/Tap13/KeHoach_Video_Tap13.md matching exact standards of Tap 10 & 11."""
import json, sys
from pathlib import Path

# Load shots and timeline
shots_data = json.load(open('.work/shots_t13.json', encoding='utf-8'))
shots = shots_data['shots']
tl = json.load(open('.work/timeline_s_t13.json', encoding='utf-8'))
sent_map = {it['id']: it for it in tl['items']}

ROLE_NAMES = {
    'H': 'Cú',
    'D': 'Sói',
    'C': 'Cáo',
    'N1': 'Cừu',
    'N2': 'Mèo'
}

ACT_HEADERS = {
    1: "### HỒI 1 — VỎ BỌC 'CON NHÀ NGƯỜI TA' VÀ TÒA THÁP DỐI LỪA MƯỜI NĂM",
    2: "### HỒI 2 — ĐÊM KINH HOÀNG TẠI ĐẠI LỘ HELEN VÀ CUỘC GỌI 911",
    3: "### HỒI 3 — GIẢI MÃ TÂM LÝ: TỪ 'CHA MẸ HỔ' ĐẾN HỘI CHỨNG NÓI DỐI BỆNH LÝ",
    4: "### HỒI 4 — ĐẤU TRÍ PHÒNG THẨM VẤN & SỰ THỨC TỈNH CỦA NGƯỜI CHA",
    5: "### HỒI 5 — BẢN ÁN LƯƠNG TÂM & LỜI CẢNH TỈNH"
}

# Determine role transitions and first appearances
seen_roles = set()
role_entries = {}
for i, s in enumerate(shots):
    r = s.get('role')
    if r and r not in seen_roles:
        seen_roles.add(r)
        role_entries[i] = r

# Build markdown
lines = []
lines.append('# HỒ SƠ SẢN XUẤT TẬP 13 · "VỎ BỌC \'CON NHÀ NGƯỜI TA\' & LỜI NÓI DỐI 10 NĂM" — VI EDITION\n')
lines.append('## B1. Thông tin tập\n')
lines.append('| Mục | Nội dung |')
lines.append('|---|---|')
lines.append('| Tên tập | **Tập 13: Vỏ Bọc \'Con Nhà Người Ta\' & Lời Nói Dối 10 Năm — Khi Kỳ Vọng Cực Đoan Tạo Ra Kẻ Chủ Mưu (Hồ Sơ Jennifer Pan)** |')
lines.append('| Vụ án | Hồ sơ Jennifer Pan & Bi kịch tại Markham (Markham, Ontario, Canada, 2010–2014) |')
lines.append('| Chủ đề | Hội chứng Nói dối bệnh lý (Mythomania) · Mô hình giáo dục Cha mẹ hổ (Tiger Parenting) · Sự phân rã nhân cách & Cơ chế hối hận thực dụng |')
lines.append('| Tổng thời lượng | **2030.48 s (~33 phút 50 giây)** · 5 hồi · **210 câu thoại** |')
lines.append('| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên) · Cáo (Chuyên gia tâm lý) · N1 (Bạn học phổ thông) · N2 (Ông Huei Hann Pan) |')
lines.append('| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) — **đã thu âm** |')
lines.append('| Timeline | [`.work/timeline_s_t13.json`] — **đo thật** từ master mp3 (T20) |')
lines.append(f'| Số shot | **{len(shots)}** dòng (210 shot nội dung + 4 thẻ chuyển hồi + 1 thẻ kết) |\n')
lines.append('---\n')
lines.append('## 6. DANH SÁCH SHOT — TẬP 13 (VI)\n')
lines.append('**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.')
lines.append('Cột *Nhân vật*: `✦` = lần đầu xuất hiện · `→X` = vai của shot kế tiếp · `⊘` = tắt bán thân.')
lines.append('Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.')
lines.append('Cột *Chữ* = **NGUYÊN VĂN** câu kịch bản của shot (A7/V3/H6): ≥ 40 ký tự ⇒ *nghiêng*, < 40 ký tự ⇒ **đậm**.')
lines.append('Nền `t13_*` là **tài sản dùng chung cho cả 3 ngôn ngữ** (H17/A8.1) — mã shot giống nhau luôn dùng cùng một nền.\n')
lines.append('### INTRO KÊNH · 0,00–22,41 s\n')
lines.append('Đặt `assets/brand/intro_kenh.mov` tại 0,00 s (A5.7). Không câu thoại nào thuộc intro.\n')

current_act = 0

for i, s in enumerate(shots):
    act = s['act']
    if act != current_act:
        current_act = act
        lines.append(ACT_HEADERS[act] + '\n')
        lines.append('| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |')
        lines.append('|---|---|---|---|---|---|---|---|---|')

    shot_id = s['id']
    role = s.get('role') or '—'
    template = s['template']
    if template == 'T4':
        template_str = 'T4 lời kể'
    else:
        template_str = template
    bg = s.get('bg') or 'void'
    cam = s.get('camera') or 'still'
    bg_str = f"`{bg}`, `{cam}`"

    # Chữ
    segs = s.get('segments', [])
    text_parts = []
    for seg in segs:
        for elem in seg.get('elems', []):
            kind, val = elem[0], elem[1]
            if kind == 'bold':
                text_parts.append(f"**{val}**")
            elif kind == 'ital':
                text_parts.append(f"*{val}*")
            else:
                text_parts.append(val)
    chu_str = " · ".join(text_parts) if template in ['T10', 'T2'] else "".join(text_parts)

    # Câu + thời lượng
    sents = s.get('sentences', [])
    if sents:
        sid = sents[0]
        it = sent_map.get(sid)
        if it:
            dur = it['end'] - it['start']
            dur_str = f"{dur:.1f}".replace('.', ',')
            cau_str = f"`{sid}` ({dur_str} s)"
        else:
            dur = s['end'] - s['start']
            dur_str = f"{dur:.1f}".replace('.', ',')
            cau_str = f"`{sid}` ({dur_str} s)"
    else:
        if template == 'T10':
            cau_str = "nghỉ chuyển hồi (2 s)"
        elif template == 'T2':
            cau_str = "hết tập (0,0 s)"
        else:
            cau_str = "—"

    # Beat
    beat_str = s.get('beat_text') or '—'

    # Nhân vật
    nv_str = '—'
    if i in role_entries:
        r_entry = role_entries[i]
        nv_str = f"✦ {ROLE_NAMES.get(r_entry, r_entry)}"
    elif template in ['T10', 'T2']:
        nv_str = '⊘'
    else:
        # Check if next shot changes role
        if i + 1 < len(shots):
            next_role = shots[i+1].get('role')
            if next_role and next_role != role and next_role != '—':
                nv_str = f"→{next_role}"

    # Cột cuối
    last_col = ''
    if template in ['T10', 'T2']:
        last_col = '◼'

    row = f"| {shot_id} | {cau_str} | {role} | {template_str} | {bg_str} | {chu_str} | {beat_str} | {nv_str} | {last_col} |"
    lines.append(row)

out_text = "\n".join(lines) + "\n"
out_path = Path('02_SAN_XUAT/Ho_So_Toi_Pham/Tap13/KeHoach_Video_Tap13.md')
out_path.write_text(out_text, encoding='utf-8')
print(f"Generated {out_path} ({len(shots)} shots).")
