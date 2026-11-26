import re
import pathlib

src = pathlib.Path('01_KICH_BAN/TamLyHocToiPham/kichban_tap41_chien_loi_pham_va_cooling_off.md').read_text(encoding='utf-8')
lines = [l.strip() for l in src.splitlines() if l.strip()]

act = 0
speaker = 'H'
rows = []
for l in lines:
    if l.startswith('## HỒI '):
        act += 1
        continue
    if l.startswith('**HOST**'):
        speaker = 'H'
        continue
    if l.startswith('**N1**'):
        speaker = 'N1'
        continue
    if l.startswith('**N2**'):
        speaker = 'N2'
        continue
    if l.startswith('**N3**'):
        speaker = 'N3'
        continue
    if l.startswith('**CHUYÊN GIA'):
        speaker = 'C'
        continue
    if l.startswith('**ĐIỀU TRA VIÊN'):
        speaker = 'D'
        continue
    if l.startswith(('#', '|', '---', '**[', '**Chủ đề:', '**Hồ sơ', '**Phỏng vấn')):
        continue
    if act == 0:
        continue
    sents = [s.strip() for s in re.split(r'(?<=[.!?])\s+', l) if s.strip()]
    for s in sents:
        rows.append((act, speaker, s))

total_shots = len(rows)
target_bgs = 175
bg_list = []
for i in range(total_shots):
    bg_idx = min(target_bgs, int(i * target_bgs / total_shots) + 1)
    bg_list.append(f't41_bg_{bg_idx:03d}')

unique_bgs = len(set(bg_list))
print(f'Total parsed sentences: {total_shots}, Unique BGs: {unique_bgs}')

out = []
out.append('# BẢNG SHOT & PROMPT SINH ẢNH NỀN — TẬP 41 (CHIẾN LỢI PHẨM & COOLING-OFF PERIOD)\n\n')
out.append('- **Kịch bản nguồn:** `01_KICH_BAN/TamLyHocToiPham/kichban_tap41_chien_loi_pham_va_cooling_off.md`\n')
out.append(f'- **Tổng số câu thoại:** {total_shots} câu (5 hồi)\n')
out.append(f'- **Tổng số shot:** {total_shots} shot (mapping 1-1 với từng câu thoại)\n')
out.append(f'- **Tổng số ảnh nền duy nhất:** {unique_bgs} ảnh (`t41_bg_001` → `t41_bg_{unique_bgs:03d}`)\n')
out.append('- **Phong cách ảnh chuẩn (Graphic Novel Noir, 16:9, 2K):** *Graphic novel noir illustration, high contrast chiaroscuro lighting, deep shadows, muted slate blue and amber accents, atmospheric rain/fog, 16:9 widescreen, NO text, NO watermarks, real humans shown ONLY as dark silhouettes without facial features.*\n\n')

cur_act = 0
seen_roles = set()
prev_role = None
role_names = {'H': '✦ Cú', 'D': '✦ Sói', 'C': '✦ Cáo', 'N1': '✦ Cừu', 'N2': '✦ Mèo', 'N3': '✦ Khách'}

for idx, ((a, r, s), bg_id) in enumerate(zip(rows, bg_list), 1):
    if a != cur_act:
        cur_act = a
        out.append(f'\n## HỒI {a}\n\n')
        out.append('| Shot | Câu | Vai | Mẫu | Nền | Prompt sinh ảnh nền (Graphic Novel Noir) | Chữ trên hình | Nhân vật |\n')
        out.append('|---|---|---|---|---|---|---|---|\n')
    shot_id = f'{a}-{idx:03d}'
    cau_id = f'{a}.{idx:03d}'
    if r not in seen_roles:
        seen_roles.add(r)
        nv = role_names[r]
    elif r != prev_role:
        nv = f'→{r}'
    else:
        nv = '—'
    prev_role = r
    clean_s = s.replace('|', '/').replace('"', "'")
    prompt = f'Graphic novel noir 16:9 scene illustrating: {clean_s[:110]}... Dark moody chiaroscuro lighting, slate blue and amber tones, silhouette figures only, no faces, no text.'
    out.append(f'| {shot_id} | `{cau_id}` | {r} | T1 | `{bg_id}` | {prompt} | *{clean_s}* | {nv} |\n')

out_path = pathlib.Path('02_SAN_XUAT/Ho_So_Toi_Pham/Tap41/Bang_Shot_Anh_Tap41_ChienLoiPham.md')
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(''.join(out), encoding='utf-8')
print('Wrote:', out_path)
