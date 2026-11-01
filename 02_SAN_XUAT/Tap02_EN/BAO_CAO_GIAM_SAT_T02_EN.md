# BÁO CÁO GIÁM SÁT — TẬP 02 BẢN TIẾNG ANH (dựng lại 01/11/2026)

## 1. Số đo nền

| Hạng mục | Giá trị |
|---|---|
| Câu trong kịch bản / timeline | 203 |
| Timeline total | 1392.790 s (23:12.79) |
| Hồi | hồi 1: 23.0–280.4 · hồi 2: 282.4–493.63 · hồi 3: 495.63–810.89 · hồi 4: 812.89–1112.76 · hồi 5: 1114.76–1383.79 |
| Độ dài câu | min 1.28 · median 5.64 · max 15.96 · TB 6.04 s |
| Câu > 20 s (dư im lặng) | 0 |
| Shot | 151 (tb 9.1 s · dài nhất 26.7 s · ngắn nhất 1.3 s) |
| Shot > 15 s | 23 / 151 |
| Master mp3 | 1392.79 s · -16.2 LUFS · peak -1.7 dBFS · 0 đoạn câm > 0,3 s |
| Video cuối | 1392.77 s · 1920x1080 @ 30/1 · 41783 khung |
| Codec cuối | h264 + aac (48000 Hz, 2 kênh) |
| Lệch hình ↔ tiếng (file cuối) | 0.023 s |
| Loudness file cuối | -16.0 LUFS · peak -1.7 dBFS |
| Giải mã toàn bộ mp4 | 0 lỗi |
| Phụ đề | 402 cue · cue cuối kết thúc 00:22:59,835 (video 00:23:12,767) |
| G10 — đồng nhất giọng theo vai | ĐẠT |

## 2. Các lỗi đã phát hiện và xử lý trong lượt dựng này

| # | Vấn đề | Mức độ | Xử lý |
|---|---|---|---|
| 1 | Câu `3.02#1` (mở đầu hồi 3) có **41,57 s im lặng kỹ thuật** kéo theo (tổng file 47,56 s, lời đọc chỉ 5,99 s). Bản dựng 25/10 dùng bản này ⇒ shot 3-01 dài 48,1 s, vỡ nhịp hồi 3 | Nghiêm trọng | Thay bằng **seed s1** đã sinh sẵn (6,60 s, ASR 2 vòng khớp 100%, đuôi im lặng 0,36 s). File cũ giữ ở `.work/_cu/audio_s_higgs_EN_t02_seed_fix/` |
| 2 | Câu `4.08#6` đọc **“the snowshoe footprint”** còn kịch bản duyệt + hồi 1 (`1.17#1`) ghi **“snow boot mark / snow boot impression”** ⇒ lệch nội dung với chính tập này; nguyên nhân: `acting_tap02_EN.json` còn 1 dòng `alt` cũ ghi đè chữ | Nghiêm trọng | Sửa `alt` + **sinh lại riêng câu này trên Kaggle GPU** (kernel `…-higgs-fix-4-08-6-en-t02-kaggle-gpu`), 3 bản, chọn bản s1: **CER 0,00%**, peak −1,50 dBFS, đuôi 0,34 s |
| 3 | `tts_manifest_EN_t02.json` còn `display` cũ cho 4 câu ⇒ **phụ đề lệch với tiếng đọc** (3.11#2 “hundreds”/“thousands”, 4.06#4, 4.08#6, 4.10#1 “classified”) | Trung bình | Đồng bộ `display` ← kịch bản (4 câu) |
| 4 | 3 dòng bảng shot trong kế hoạch không khớp câu đang đọc: 4-08 (mô tả người), 4-13 (loại dấu vết), 4-16 (từ “classified” không có trong câu) | Trung bình | Sửa kế hoạch + render lại still, QC A9.2 kiểm tra lại đạt |
| 5 | Bản dựng 25/10 dài 1674,6 s còn bản hình cũ; audio Higgs mới chỉ 1392,8 s ⇒ lệch 281,8 s, không thể ghép | Hệ thống | Dựng lại toàn bộ hình theo H14 |

## 3. Cổng QC A9.1 / A9.3 / A9.4 (file chuẩn của dự án)

```
=== A9.4 file cuoi ===
   mp4  = 1392.767 s (23:12.77)
   wav  = 1392.790 s
[OK  ] Hinh va tieng cung thoi luong (±0,05 s) — lech 0.023 s
   codec_name=h264 width=1920 height=1080 r_frame_rate=30/1 nb_frames=41783 
[OK  ] Video 1920x1080 @ 30 fps
[OK  ] So khung = so giay x 30 — 41783 khung
   giai ma toan bo mp4 ...
[OK  ] Giai ma khong loi
=== A9.1 am thanh ===
[OK  ] Khong co khoang cam tuyet doi > 0,3 s (V4) — 0 doan: []
   doan im lap >= 2,5 s (chi duoc phep neu co chu dich): 0 []
   loudness: I:         -16.0 LUFS
[OK  ] Do lon trong khoang -16 ± 1 LUFS — -16.0 LUFS
[OK  ] Loi dau tien 22,8 – 23,5 s — 23.0 s
=== A9.3 hinh: 1 khung giua moi shot lay tu chinh mp4 thanh pham ===
[OK  ] Lay du 151 khung giua shot tu mp4
   10 contact sheet -> D:\TEST\Gax\amber-eyes\.work\qc_final_EN_t02
=== phu de: 402 cue ===
[OK  ] Phu de khong co cue chong lap / vo trong
   cue cuoi ket thuc luc 1383.8 s · video 1392.8 s

TAT CA DA DAT
```

## 4. Cổng giám sát bổ sung P1–P6 (nhip · sync · dead air · frame · phụ đề · đối chiếu chữ)

```
==============================================================================
P1 — NHIP (pacing) cua bang shot moi
==============================================================================
   151 shot · min 1.30 · p25 5.59 · median 8.31 · p75 12.46 · max 26.72 · TB 9.09
   shot > 15 s: 23  [('1-25', 19.8), ('1-31', 16.2), ('2-09', 16.2), ('2-13', 17.8), ('2-14', 20.0), ('2-16', 15.0), ('2-19', 15.7), ('3-07', 16.9)]
   shot < 3 s : 20 (cac hang nghỉ/nghỉ chuyen hoi — thiet ke)
[OK  ] Khong shot co loi nao < 1,5 s
   [GHI] 23 shot > 15 s co loi — QC A9.2 đã xác nhận có nhịp/bám V2: 1-25=19.8s, 1-31=16.2s, 2-09=16.2s, 2-13=17.8s, 2-14=20.0s, 2-16=15.0s, 2-19=15.7s, 3-07=16.9s, 3-10=16.8s, 3-18=16.5s
   so sanh ban du 25/10: 151 shot · TB 11.0 s · max 33.9 s · > 15 s: 37
                ban moi : 151 shot · TB 9.1 s · max 26.7 s · > 15 s: 23

==============================================================================
P2 — SYNC: moi shot co loi phai co tieng trong khoang
==============================================================================
   master: 1392.79 s @ 48000 Hz, 2 kenh
[OK  ] Moi shot co loi deu co tieng trong khoang
[OK  ] Moi 1 trong 203 cau deu co tieng

==============================================================================
P3 — DEAD AIR trong master (nguong -45 dB, >= 1,0 s)
==============================================================================
   doan im >= 1,0 s: 0
[OK  ] Khong co dead air > 1,0 s ngoai khoang nghi da thiet ke

==============================================================================
P4 — FRAME: khong khung den toan bo / khong freeze
==============================================================================
   doan den toan bo >= 0,5 s: 6 [('0', '0.766667'), ('280.4', '280.933333'), ('493.5', '494.133333'), ('810.4', '811.433333'), ('1112.633333', '1113.266667'), ('1390.166667', '1392.733333')]
[OK  ] Khong co khung den toan bo ngoai dip chuyen hoi / intro / outro — []
   den o cuoi (nen thiet ke): [(1390.166667, 1392.733333)]
   ranh hoi (dip thiet ke): [280.4, 493.6, 810.9, 1112.8, 1383.8]
   doan freeze >= 3 s: 0 []
[OK  ] Khong co freeze >= 6 s (tru doan cuoi chuyen den) — []

==============================================================================
P5 — PHU DE
==============================================================================
   402 cue
[OK  ] Cue phu de khong chong lap
[OK  ] Cue cuoi phai nam trong video — 1383.8 vs 1392.8
[OK  ] Moi cau trong timeline deu co trong phu de
   cau khong doi chung: 0

==============================================================================
P6 — DOI CHIEU text: timeline / phu de / ke hoach
==============================================================================
[OK  ] Text timeline == text phu de (tuoc 1:1)
[OK  ] Bang shot khong con cum cu 'snowshoe' — []
[OK  ] Bang shot khong con cum cu 'man disguised' — []
[OK  ] Bang shot khong con cum cu 'classified' — []

==============================================================================
P7 — DRIFT: audio trong mp4 co khop voi master mp3 (tuong quan cheo)
==============================================================================
   tai    20 s -> lech -0.0050 s | tuong quan 0.9945
   tai   300 s -> lech -0.0050 s | tuong quan 0.9946
   tai   700 s -> lech -0.0050 s | tuong quan 0.9886
   tai  1000 s -> lech -0.0050 s | tuong quan 0.9899
   tai  1300 s -> lech -0.0050 s | tuong quan 0.9947
[OK  ] Lech audio mp4 <-> master mp3 < 50 ms o moi moc — 20s:-0.005s, 300s:-0.005s, 700s:-0.005s, 1000s:-0.005s, 1300s:-0.005s
[OK  ] Khong co drift tich luy (do lech giua cac moc < 20 ms) — spread 0.0000 s
[OK  ] Tuong quan audio mp4 <-> master mp3 >= 0,95 o moi moc — 20s:0.994, 300s:0.995, 700s:0.989, 1000s:0.990, 1300s:0.995

==============================================================================
TONG KET: 0 phep that bai
==============================================================================
```

## 5. Kiểm kê thành phẩm

| File | Dung lượng | Thời lượng |
|---|---|---|
| `xuat_ban/description.txt` | 3.7 KB | — |
| `xuat_ban/mo_ta.txt` | 3.7 KB | — |
| `xuat_ban/Tap02_EN.srt` | 38.2 KB | — |
| `xuat_ban/Tap02_EN_master.mp3` | 33.4 MB | 1392.79 s |
| `xuat_ban/Tap02_EN_master.mp4` | 503.9 MB | 1392.77 s |
| `xuat_ban/thumbnail.png` | 1.1 MB | — |

## 6. Việc còn lại trước khi đăng

1. Người dùng xem toàn tập (nhất là hồi 3 — vị trí vừa sửa nhịp).
2. Bổ sung link nguồn gốc cho các dòng ⚠ trong `nguon_tham_khao_EN.md`.
3. Rà lại điều khoản thương mại của Higgs Audio v3 (đã ghi công trong mô tả §2).
4. Đánh dấu “Altered or synthetic content” khi đăng YouTube.

