# -*- coding: utf-8 -*-
"""Sinh tài liệu bảng SFX Tap03..Tap29 -> 02_SAN_XUAT/Danh_Sach_SFX_Tap03-29.md"""
import os, sys, re, json
sys.path.insert(0, r'D:\TEST\Gax\Audi\.work')
from _sfx_analysis import DATA, TITLES, ROOT
try:
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
except Exception:
    pass

SFXDIR = os.path.join(ROOT, 'assets', 'sfx')
def exists(f):
    p = os.path.join(SFXDIR, f)
    return os.path.isfile(p)

# BGM gợi ý theo hồi (lấy từ spec table / cue BGM của kịch bản)
BGM_MAP = {
3:"H1 gió rít + tiếng dây điện thoại 1970 → `t2/amb_winter_wind` · H2 mưa + cần gạt → `t3/amb_rain_storm` · H3 nước nhỏ giọt hầm → `t3/amb_pipe_drain` · H4 máy ghi âm cassette → `t2/amb_interrogation` + `t3/fx_cassette_motor` · H5 tòa án → `t2/amb_courtroom` + `bgm_cello_sad_v2`",
4:"H1 máy thở cơ học + monitor → `amb_hospital_ventilator` (MỚI) · H2 piano tối giản + gõ bàn phím đêm → `bgm_piano_minimal_v2` + `keyboard_night` · H3 sub-bass + nhịp tim → `bgm_sub_drone` + `fx_heartbeat_slow` · H4 synth dồn dập → `bgm_ambient_deep` · H5 gavel + piano → `t2/fx_gavel_triple` + `bgm_piano_warm`",
5:"H1 máy đánh chữ cơ + gió đông → `typewriter` + `t2/amb_winter_wind` · H2 nhịp tim + cuộn băng từ → `fx_heartbeat_slow` + `t3/fx_cassette_motor` · H3 cello + sub-bass → `bgm_cello_sad` + `bgm_sub_drone` · H4 synth + quạt server → `bgm_ambient_deep` + `amb_server_fan` (MỚI) · H5 gavel → `bgm_piano_warm`",
6:"H1 dương cầm → `bgm_piano_minimal` · H2 dark ambient dồn dập → `bgm_ambient_deep` · H3 sub-drone → `bgm_sub_drone` · H4 vĩ cầm → `bgm_cello_sad` · H5 piano sâu lắng → `bgm_piano_warm`",
7:"H1 piano tối giản + synth → `bgm_piano_minimal_v2` · H2 pulse số → `bgm_ambient_deep` · H3 cello u uất → `bgm_cello_sad` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`",
8:"H1 dương cầm + heartbeat → `bgm_piano_minimal` + `fx_heartbeat_slow` · H2 dark ambient → `bgm_ambient_deep` · H3 piano u ám → `bgm_piano_minimal_v2` · H4 vĩ cầm → `bgm_cello_sad` · H5 piano ấm → `bgm_piano_warm`",
9:"H1 guitar acoustic 60s → *cần tải* (chưa có trong `assets/bgm/`) · H2 dark ambient + gió sa mạc → `bgm_ambient_deep` + `amb_wind_pines` (MỚI) · H3 piano tối giản → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`",
10:"H1 cello u buồn → `bgm_cello_sad` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`",
11:"H1 cello + gió → `bgm_cello_sad` + `t2/amb_winter_wind` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`",
12:"H1 cello + côn trùng nhiệt đới → `bgm_cello_sad` + `t3/amb_crickets_traffic` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`",
13:"H1 cello + đồng hồ treo tường → `bgm_cello_sad` + `clock_tick` · H2 dark ambient + đồng hồ → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`",
14:"H1 cello + sóng biển → `bgm_cello_sad` + `amb_ocean_waves_soft` (MỚI) · H2 dark ambient + búa tòa → `bgm_ambient_deep` + `gavel` · H3 dương cầm → `bgm_piano_minimal` · H4 vĩ cầm → `bgm_cello_sad_v2` · H5 piano ấm → `bgm_piano_warm`",
15:"H1 dark ambient + nước nhỏ giọt → `bgm_ambient_deep` + `t3/amb_pipe_drain` · H2 điện tử dồn dập → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin căng thẳng → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
16:"H1 organ nhà thờ → *cần tải* (chưa có organ trong `assets/bgm/`) + `t2/amb_winter_wind` · H2 điện tử + máy bay → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
17:"H1 dark ambient + gió → `bgm_ambient_deep` + `t2/amb_winter_wind` · H2 dark ambient + công viên giải trí → `bgm_ambient_deep` + `amb_carnival_ride_music_far` (MỚI) · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
18:"H1 dark ambient + gió biển + chuông gió → `bgm_ambient_deep` + `amb_ocean_waves_soft` (MỚI) · H2 điện tử dồn dập → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
19:"H1 drone + đồng hồ → `bgm_sub_drone` + `clock_tick` · H2 dark ambient → `bgm_ambient_deep` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
20:"H1 dark ambient + nhịp tim + đồng hồ → `bgm_ambient_deep` + `fx_heartbeat_slow` + `clock_tick` · H2 minimal ambient → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
21:"H1 cello + nhịp tim + mưa → `bgm_cello_sad` + `fx_heartbeat_slow` + `t3/amb_rain_storm` · H2 ambient trầm đục → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
22:"H1 dark ambient + còi xe → `bgm_ambient_deep` + `police_siren_distant` · H2 electronic pulse → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
23:"H1 dark ambient + đồng hồ → `bgm_ambient_deep` + `clock_tick` · H2 heavy bass → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
24:"H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 minimal ambient + bước chân hành lang → `bgm_sub_drone` + `footsteps` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
25:"H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass + hú báo động → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
26:"H1 cello + gió + tuyết → `bgm_cello_sad` + `t2/amb_winter_wind` · H2 deep ambient → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
27:"H1 cello + gió + mưa → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
28:"H1 cello + sấm + bão → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 heavy bass + động cơ xe → `bgm_sub_drone` · H3 dương cầm → `bgm_piano_minimal` · H4 violin → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
29:"H1 cello + bass + mưa + còi tuần tra → `bgm_cello_sad` + `t3/amb_rain_storm` · H2 cello + gõ nhịp kim loại + quạt → `bgm_cello_sad_v2` + `amb_ceiling_fan` (MỚI) · H3 piano tối giản → `bgm_piano_minimal` · H4 violin + búa tòa → `bgm_violin_heart` · H5 piano ấm → `bgm_piano_warm`",
}

# Bảng BGM chuẩn 5 hồi (tương đương T15–T29)
BGM_STD = ("Hồi 1 Dark Ambient/cello u buồn → Hồi 2 Dark Ambient điện tử dồn dập → "
           "Hồi 3 Minimalist Piano triết học → Hồi 4 Violin căng thẳng → Hồi 5 Warm Piano suy tư")

newfile_eps = {}
for ep, rows in DATA.items():
    for cid, desc, st, files, note in rows:
        if st == 'MOI':
            for f in files:
                if f == '—': continue
                newfile_eps.setdefault(f, set()).add(ep)

# Tong so cue doc tu file trich xuat (.work/sfx_cues_tap03_29.json)
_cues = json.load(open(os.path.join(ROOT, '.work', 'sfx_cues_tap03_29.json'), encoding='utf-8'))
TOT_SFX = sum(len(v['sfx']) for v in _cues.values())
TOT_BGM = sum(len(v['bgm']) for v in _cues.values())
TOT_NGHI = sum(len(v['nghi']) for v in _cues.values())
N_ROOT = len([f for f in os.listdir(SFXDIR) if f.endswith('.wav')])
N_NEN = sum(1 for e in DATA for r in DATA[e] if r[0].startswith(('BGM ', 'NGHI ')))

L = []
w = L.append
w("# DANH SÁCH SFX CẦN TẠO — TẬP 03 → TẬP 29")
w("")
w("**AMBER EYES** · rút từ toàn bộ cue `[SFX]:` / `[BGM]:` / `[Nghỉ …]` trong "
  "`01_KICH_BAN/Tap03/ … Tap29/` · ngày 23/10/2026")
w("")
w("---")
w("")
w("## 1. Tóm tắt")
w("")
w("| Hạng mục | Số lượng |")
w("|---|---:|")
w("| Tập khảo sát | 27 (Tập 03 – Tập 29) |")
w(f"| Tổng cue `[SFX]` đọc được | {TOT_SFX} |")
w(f"| Tổng cue `[BGM]` / nền | {TOT_BGM} |")
w(f"| Tổng cue `[Nghỉ …]` có mô tả âm thanh | {TOT_NGHI} |")
w(f"| Dòng dải nền đã tách từ cue `[BGM]` / `[Nghỉ]` | {N_NEN} dòng |")
w(f"| **File SFX mới phải tạo (unique)** | **{len(newfile_eps)}** |")
w(f"| Lượt file mới tính theo tập (tính cả file dùng chung) | {sum(len(set(f for r in DATA[e] if r[2]=='MOI' for f in r[3] if f != '—')) for e in DATA)} |")
w(f"| File đã có trong thư viện, tái dùng được | {len(set(f for e in DATA for r in DATA[e] if r[2]=='SAN' for f in r[3]))} |")
w(f"| Kịch bản tiếng Anh (`Tap03_EN` … `Tap29_EN`) | 27 bản — số cue khớp 100% ⇒ **dùng chung bảng SFX này** |")
w("| Nhạc nền (BGM) dùng lại từ `assets/bgm/` | 9 track |")
w("| Nhạc nền cần tải thêm (chưa có trong thư viện) | 2 (guitar acoustic 60s cho T09 · organ nhà thờ cho T16) |")
w("")
w("### Cách đọc ký hiệu")
w("")
w("| Ký hiệu | Ý nghĩa |")
w("|---|---|")
w("| 🔴 **TẠO MỚI** | Chưa có trong `assets/sfx/` — phải tải từ YouTube Audio Library, Freesound hoặc tổng hợp bằng `make_sfx3.py` |")
w("| 🟢 **TÁI DÙNG** | Đã có sẵn trong `assets/sfx/` (`/` = gốc, `t2/` = Tập 02, `t3/` = Tập 03) — chỉ cần trỏ file |")
w("| 🎵 **NHẠC NỀN** | Nhạc nền / dải nền, không phải tiếng động một lần |")
w("")
w("> **Cột “mã cue”** là mã element theo đúng logic `parse_kichban.py` (`1.02` = phần tử thứ 2 của Hồi 1) — dùng được ngay để ghi vào `.work/sfx_tapXX.json`.")
w("> Mỗi tập có **2 bảng**: tiếng động trong cue `[SFX]`, và **dải nền trong cue `[BGM]` / `[Nghỉ …]`** — bảng thứ 2 hay bị bỏ sót vì nằm lẫn trong mô tả nhạc.")
w("> Có một số cue trong kịch bản gộp 2–3 âm thanh vào một dòng (ví dụ `1.05` của Tập 12) — bảng này đã tách sẵn thành từng file.")
w("")
w("---")
w("")

# ---- Bảng tổng theo tập
w("## 2. Tổng nhanh theo tập")
w("")
w("| Tập | Hồ sơ | File mới | Tái dùng | Tổng cue SFX |")
w("|---|---|---:|---:|---:|")
for ep in sorted(DATA):
    rows = DATA[ep]
    nm = len(set(f for r in rows if r[2]=='MOI' for f in r[3]))
    rs = len(set(f for r in rows if r[2]=='SAN' for f in r[3]))
    ns = len([r for r in rows if r[2] != 'NHAC'])
    w(f"| {ep:02d} | {TITLES[ep][:58]} | {nm} | {rs} | {ns} |")
w("")
w("---")
w("")

# ---- Chi tiết từng tập
w("## 3. Chi tiết theo từng tập")
w("")
for ep in sorted(DATA):
    rows = DATA[ep]
    w(f"### Tập {ep:02d} — {TITLES[ep]}")
    w("")
    w(f"`01_KICH_BAN/Tap{ep:02d}/kichban_tap{ep:02d}_*.md`")
    w("")
    w("**Nhạc nền / dải nền theo hồi:**")
    w("")
    w(BGM_MAP.get(ep, '—'))
    w("")
    w("| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |")
    w("|---|---|---|---|---|")
    for cid, desc, st, files, note in DATA[ep]:
        if cid.startswith(('BGM ', 'NGHI ')):
            continue
        badge = {'MOI':'🔴 **TẠO MỚI**','SAN':'🟢 TÁI DÙNG','NHAC':'🎵 NHẠC NỀN'}[st]
        fl = '<br>'.join(f'`{f}`' for f in files)
        w(f"| `{cid}` | {desc} | {badge} | {fl} | {note} |")
    w("")
    nen_rows = [r for r in DATA[ep] if r[0].startswith(('BGM ', 'NGHI '))]
    if nen_rows:
        w("**Dải nền / âm thanh môi trường nằm trong cue `[BGM]` và `[Nghỉ …]`** — cũng cần file, không được bỏ sót:")
        w("")
        w("| Mã cue | Âm thanh trong kịch bản | Loại | File cần có | Ghi chú |")
        w("|---|---|---|---|---|")
        for cid, desc, st, files, note in nen_rows:
            badge = {'MOI':'🔴 **TẠO MỚI**','SAN':'🟢 TÁI DÙNG','NHAC':'🎵 NHẠC NỀN'}[st]
            fl = '<br>'.join(('⚠️ *không có track tương ứng*' if f == '—' else f'`{f}`') for f in files)
            w(f"| `{cid}` | {desc} | {badge} | {fl} | {note} |")
    w("")

w("---")
w("")

# ---- Danh mục file mới unique
w(f"## 4. Danh mục {len(newfile_eps)} file mới — đặt ở đâu, dùng cho tập nào")
w("")
w("**Quy tắc đặt file:** dùng ≥ 2 tập → `assets/sfx/<file>` (gốc, dùng chung toàn series) · chỉ 1 tập → `assets/sfx/tXX/<file>`.")
w("")
w("| # | File | Loại | Dùng cho tập | Đặt tại |")
w("|---:|---|---|---|---|")
ordered = sorted(newfile_eps.items(), key=lambda kv: (-len(kv[1]), kv[0]))
for i, (f, eps) in enumerate(ordered, 1):
    kind = 'nền môi trường' if f.startswith('amb_') else 'tiếng động'
    loc = f"`assets/sfx/{f}`" if len(eps) >= 2 else f"`assets/sfx/t{list(eps)[0]:02d}/{f}`"
    epstr = ', '.join(f'T{e:02d}' for e in sorted(eps))
    w(f"| {i} | `{f}` | {kind} | {epstr} | {loc} |")
w("")
n_shared = sum(1 for f, e in newfile_eps.items() if len(e) >= 2)
w(f"**Tóm tắt:** {len(newfile_eps)} file mới — {n_shared} file dùng chung (≥2 tập) đặt ở `assets/sfx/`, "
  f"{len(newfile_eps)-n_shared} file riêng một tập đặt trong `assets/sfx/tXX/`.")
w("")
w("### 4.1. 12 file dùng chung nhiều tập nhất — ưu tiên làm trước")
w("")
w("| File | Số tập dùng | Các tập |")
w("|---|---:|---|")
for f, eps in ordered[:12]:
    w(f"| `{f}` | {len(eps)} | {', '.join(f'T{e:02d}' for e in sorted(eps))} |")
w("")
w("---")
w("")

# ---- Nhạc nền
w("## 5. Nhạc nền (BGM)")
w("")
w("### 5.0. Bản tiếng Anh dùng CHUNG bảng SFX này")
w("")
w("Có **27 kịch bản tiếng Anh** (`01_KICH_BAN/Tap03_EN/ … Tap29_EN/`) và số cue SFX/BGM **khớp 100%** với bản tiếng Việt "
  "ở cả 27 tập (kiểm bằng script `.work/_audit_sfx.py`, mục A).")
w("")
w("⇒ **Một bảng SFX, dùng cho cả bản VN lẫn bản EN** — không phải làm hai lần. "
  "Các cue trong bản EN là bản dịch 1–1 của cue tiếng Việt, nên file âm thanh và mức dB giữ nguyên.")
w("")
w("### 5.1. Thư viện nhạc nền")
w("")
w("Thư viện hiện có (`assets/bgm/`, 9 track): `bgm_ambient_deep` · `bgm_cello_sad` · `bgm_cello_sad_v2` · "
  "`bgm_music_box` · `bgm_piano_minimal` · `bgm_piano_minimal_v2` · `bgm_piano_warm` · `bgm_sub_drone` · `bgm_violin_heart`")
w("")
w("### 5.2. Cấu trúc 5 hồi theo tập")
w("")
w("| Tập | Cấu trúc 5 hồi & file nhạc dùng | Dải nền mới phải tạo |")
w("|---|---|---|")
for ep in sorted(DATA):
    txt = BGM_MAP.get(ep, '')
    news = sorted(set(f for r in DATA[ep] if r[2]=='MOI' for f in r[3] if f.startswith('amb_')))
    w(f"| {ep:02d} | {txt} | {', '.join('`'+x+'`' for x in news) if news else '—'} |")
w("")
w("> **Chuẩn BGM 5 hồi** áp dụng cho Tập 15–29 (nhóm kịch bản viết cùng đợt): " + BGM_STD + ".")
w("> Tập 03–14 có nhịp riêng, xem cột “Nhạc nền / dải nền theo hồi” ở mục 3.")
w("")
w("**Cần tải thêm 2 track BGM (chưa có trong thư viện):**")
w("")
w("| Tập | Track cần | Ghi chú |")
w("|---|---|---|")
w("| 09 | Guitar acoustic mộc mạc thập niên 60, biến dạng dần sang u tối | Chưa có track guitar trong `assets/bgm/` |")
w("| 16 | Organ nhà thờ trầm buồn, u tối | Chưa có track organ trong `assets/bgm/` |")
w("")
w("---")
w("")

# ---- Quy trình
w("## 6. Quy trình tạo & đưa vào bảng âm thanh")
w("")
w("1. **Tải/tổng hợp file mới** theo bảng mục 4. Nguồn: YouTube Audio Library (ưu tiên — đã dùng cho Tập 03), "
  "Freesound (CC0), hoặc tổng hợp bằng `.work/make_sfx3.py` (bản `_code/` là bản dự phòng tự tổng hợp).")
w("2. **Đặt file** vào `assets/sfx/` (dùng chung) hoặc `assets/sfx/tXX/` (riêng tập) — đúng cột “Đặt tại” ở mục 4.")
w("3. **Ghi `.work/sfx_tapXX.json`** theo đúng format `sfx_tap03.json`:")
w("   - `ambience`: `[mã câu đầu, mã câu cuối, file, dB]` — **hai mốc đều là mã câu** (`2.06#1`), không phải mã element.")
w("   - `cues`: `[mốc, 'start'|'end', lệch (s), file, dB]` — mốc được **mã câu HOẶC mã element SFX/BGM/NGHI**.")
w("   - `music_drop.ranges`: `[mã câu, mã câu]` — tắt nhạc có giai điệu ở các câu hé lộ.")
w("   - ⚠️ `ambience` / `music_drop` phải dùng **mã câu**; nếu trỏ mã element thì cue bị **bỏ qua im lặng, không báo lỗi**.")
w("4. **Ghi `provenance.json`** cho từng file mới (nguồn tải, giấy phép, ngày tải) — file không có dòng sổ là mất lớp bảo vệ đầu tiên khi bị Content ID nhận nhầm.")
w("5. **Dựng thử** `AE_EP=XX py -3 .work/build_audio3.py` rồi nghe lại trên bản trộn để chỉnh dB (mức dB trong bảng chỉ là điểm khởi đầu, tính theo RMS lời).")
w("")
w("---")
w("")
w("## 7. Nhật ký review — những gì đã sửa sau lần soát đầu tiên")
w("")
w("Bản đầu tiên chỉ rút cue `[SFX]`. Khi soát lại toàn bộ kịch bản, đã phát hiện và sửa 5 lỗi sau:")
w("")
w("| # | Lỗi | Mức độ | Cách sửa |")
w("|---|---|---|---|")
w("| 1 | **Bỏ sót dải nền trong cue `[BGM]` và `[Nghỉ]`** — 82 cue có âm thanh môi trường cụ thể (gió, mưa, đồng hồ, tiếng tim, sóng biển…) "
  "nhưng bảng per-episode chỉ liệt kê cue `[SFX]` | Nghiêm trọng | Thêm bảng **“Dải nền / âm thanh môi trường”** riêng cho từng tập, "
  "gồm cả dải nền còn thiếu như `clock_tick`, `t2/amb_winter_wind`, `fx_heartbeat_slow`, `t3/amb_rain_storm` |")
w("| 2 | **Gán nhầm âm thanh: mỏ quay (rotary dial) cho cú bấm touch-tone** — Tập 13 (`2.09` “Bấm số 911”) và Tập 17 (`1.03` “Bấm phím khẩn cấp tút tút”) "
  "đều trỏ `t3/fx_twisting_dial.wav`. Kịch bản EN ghi rõ *“Frantic touch-tone dialing”* / *“distinct electronic tones of emergency dialing”* | Trung bình | "
  "Tạo mới `fx_dtmf_touch_tone_beep.wav` cho cả 2 tập, bỏ mỏ quay |")
w("| 3 | **Gió sa mạc bị gộp nhầm với gió rặng thông** — Tập 9 Hồi 2 là Mojave Desert (Spahn Ranch), khác Hồi 1 là gió rặng thông | Thấp | "
  "Tách thành 2 file: `amb_wind_pines.wav` (Hồi 1) + `amb_desert_wind_dry.wav` (Hồi 2) |")
w("| 4 | **Thiếu 2 âm thanh nền có trong cue BGM** — chuông gió lạnh lẽo (Tập 18) và sấm rền từ xa (Tập 28) | Thấp | "
  "Thêm `amb_wind_chime.wav` + `amb_thunder_distant.wav` |")
w("| 5 | **Cột “Nền dùng chung” của bảng BGM in sai** (luôn ra `assets/sfx/`) | Vặt | Sửa lại thành cột “Dải nền mới phải tạo” |")
w("")
w("Ngoài ra đã **thêm mục 5.0**: 27 kịch bản tiếng Anh có số cue khớp 100% ⇒ một bảng SFX dùng chung cho cả hai bản.")
w("")
w("---")
w("")
w("## 8. Bẫy đã gặp (rút từ Tập 02–03)")
w("")
w("| Bẫy | Hậu quả | Cách tránh |")
w("|---|---|---|")
w("| Trỏ `ambience` bằng mã element thay vì mã câu | Cue **bị bỏ qua im lặng**, không báo lỗi, tập thiếu nền mà QC vẫn xanh | Luôn kiểm tra mã đầu/cuối là mã câu dạng `X.YY#Z` |")
w("| Dùng `ambience`/`music_drop` trỏ element SFX/BGM cũ | Bỏ qua im lặng, không báo lỗi | Đối chiếu mã câu theo **nội dung câu**, không đánh số tay |")
w("| Xoá mp3 cũ rồi đọc lại khi hết số dư gói | API trả **402 “plan balance has run out”** → mất file, không retry được | Luôn lưu `node_id` của từng file TTS (`res_*.json`) để khôi phục |")
w("| Ghép mp4 cũ với audio mới | Lệch **1,77 s**, mọi cổng QC vẫn xanh vì mỗi file “hợp lệ” riêng lẻ | So `duration` mp4 với `.work/audio_master_tXX.wav` trước khi giao (lệch > 0,05 s = dựng lại) |")
w("| Tài sản tạo ngoài `gen_images.py` không có dòng sổ | Mất lớp bảo vệ bản quyền | Backfill bằng `.work/_prov_backfill.py` |")
w("")
w("---")
w("")
w("## 9. Phụ lục — câu lệnh kiểm tra nhanh")
w("")
w("```powershell")
w("# Trích xuất lại toàn bộ cue SFX từ kịch bản (đã chạy, cập nhật 23/10/2026)")
w("py -3 .work/_extract_sfx_cues.py")
w("")
w("# SOÁT LẠI: parity kịch bản VN vs EN + rà dải nền trong cue BGM/[Nghỉ]")
w("py -3 .work/_audit_sfx.py")
w("")
w("# In bảng cue của một tập bất kỳ (ví dụ Tập 17)")
w("py -3 .work/_dump_sfx_cues.py 17 17")
w("")
w("# Chạy lại phân tích + xuất bảng thống kê + sinh lại tài liệu")
w("py -3 .work/_sfx_analysis.py")
w("py -3 .work/_gen_sfx_doc.py")
w("```")
w("")
w(f"**Nguồn:** 27 file kịch bản trong `01_KICH_BAN/Tap03/ … Tap29/` · "
  f"thư viện hiện có: `assets/sfx/` ({N_ROOT} file gốc) + "
  f"`t2/` + `t3/` · `assets/bgm/` (9 track).")

out = os.path.join(ROOT, '02_SAN_XUAT', 'Danh_Sach_SFX_Tap03-29.md')
open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print('Ghi:', out)
print('Dong:', len(L))

# Kiem tra file tai dung co that tren dia
missing = set()
for ep, rows in DATA.items():
    for cid, desc, st, files, note in rows:
        if st == 'SAN':
            for f in files:
                if f != '—' and not exists(f): missing.add((ep, f))
print('\nFile TAI DUNG bi thieu tren dia:', len(missing))
for ep, f in sorted(missing): print(f'  T{ep:02d} -> {f}')
