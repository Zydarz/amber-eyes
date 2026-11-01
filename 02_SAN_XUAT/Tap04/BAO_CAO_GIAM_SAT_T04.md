# BÁO CÁO GIÁM SÁT — TẬP 04 (dựng lại 31/10/2026 19:29)
## 1. Số đo nền

| Hạng mục | Giá trị |
|---|---|
| Câu trong kịch bản / timeline | 154 |
| Timeline total | 1256.520 s |
| Shot | 83 (tb 14.9 s · dài nhất 34.8 s · ngắn nhất 1.3 s) |
| Shot dài > 16 s | 37/83 |
| Bản Higgs đã chọn | 154 câu · CER TB 0.66% · câu > 2%: 18 |
| Lệch shots ↔ timeline | 0.0000 s |

## 2. Cổng P10 — audio master

```
===== QC Tap04 — gate P10 =====
  master : Tap04_master.mp3
  thoi luong : 1256.5 s (20:56.5)
  LUFS        : -16.2
  dinh that   : -1.7 dBFS
  khoang lang >0,3s @-60dB : 0

  [OK]   P10 LUFS -16.2 trong -16 +/- 1
  [OK]   P10 dinh that -1.7 <= -1,5 dBFS
  [OK]   P10 0 khoang lang > 0,3 s @ -60 dB

  => 3 OK · 0 cảnh báo · 0 lỗi
```

## 3. Cổng bảng shot

```
===== QC bang shot Tap04 — 83 dong =====

  [OK]   1) Phu 100% 154 cau, dung thu tu, khong trung
  [OK]   2) 100% nen co file (76 lan dung)
  [OK]   3) H6: 33 chu so tren hinh deu co trong cau (+4 nhan thu tu 'DANH HIEU 0N' khop 'thu N')
  [OK]   4) H6: 11 trich danh deu nguyen van trong cau
  [OK]   5) H13: vai noi khop vai kich ban
  [OK]   6) H10: nen lap toi da 4 shot lien nhau
  [OK]   7) K3: nhan N2 khong gan cho nguoi that (n2 = ('Y TÁ CA ĐÊM', 'Nhân vật hình dung', 'Y TÁ CA ĐÊM'))
  [OK]   8) Tat ca dong du 9 cot, mau hop le, moc tam co that

  => 8 OK · 0 canh bao · 0 loi
```

## 4. Cổng giám sát cuối A–G

```
===== CỔNG GIÁM SÁT TAP04 =====
  master: 1256.519979 s | LUFS -16.2 | peak -1.7 | sil>0.3s 0 | lời đầu 23.07175
  final : 1256.5 s | LUFS -16.0 | peak -1.8
  video : h264,1920,1080,30/1
  audio : aac,48000,2
  (khung the ket: D:\TEST\Gax\amber-eyes\.work\_qc_endcard_04.png)

  [OK]   A) LUFS -16.2 trong -16 +/- 1
  [OK]   A) dinh that -1.7 <= -1,5 dBFS
  [OK]   A) 0 khoang lang > 0,3 s @ -60 dB
  [OK]   A) loi dau 23.07175 s trong 22,8-23,5 s
  [OK]   A) timeline.total 1256.52 khop master 1256.519979 (±0,05 s)
  [OK]   B) bang shot phu 100% 154 cau dung thu tu
  [OK]   B) moi 83 shot deu co nen
  [OK]   B) cac shot lien tuc, khong gap
  [OK]   C) picture.mp4 1256.5 s khop timeline.total 1256.52 (±0,05 s)
  [OK]   D) mp4 1256.5 s khop audio 1256.519979 (±0,05 s)
  [OK]   D) giai ma 0 loi
  [OK]   D) LUFS file cuoi -16.0 trong -16 +/- 1 (A7)
  [OK]   D) dinh that file cuoi -1.8 <= -1,5 dBFS (A7)
  [OK]   D) 1920x1080
  [OK]   D) video H.264
  [OK]   D) audio AAC
  [OK]   D) 0 khoang lang > 0,3 s trong file cuoi
  [OK]   E) phu de phu 100% loi thoai (324 cue / 154 cau)
  [OK]   E) cue cuoi 1246.52s nam trong file
  [OK]   F) thumbnail ton tai (1219977 bytes)
  [OK]   F) nen thumbnail theo ke hoach: t4_somerset_exterior
  [OK]   G) the ket co chu tai 1248.0s (18.45% pixel sang)
  [OK]   G) shot cuoi '5-18' la the ket (khong gan cau)
  [WARN] B) shot dai > 16 s: [('1-06', 21.1), ('1-10', 26.7), ('1-16', 22.8), ('1-17', 18.0), ('1-18', 34.8), ('2-01', 16.1)]
  [WARN] G) khung tai total-2 s den — outro cua renderer mo dan shot cuoi 3 s cuoi (dung chung T01-T03); the ket da kiem o giua shot cuoi

  => 23 OK · 2 canh bao · 0 loi
```

## 5. Kiểm kê thành phẩm

| File | Dung lượng | Thời lượng |
|---|---|---|
| `xuat_ban/CanNghe_Higgs_Tap04.txt` | 0.0 MB | — |
| `xuat_ban/mo_ta.txt` | 0.0 MB | — |
| `xuat_ban/nguon_tham_khao.md` | 0.0 MB | — |
| `xuat_ban/Tap04.srt` | 0.0 MB | — |
| `xuat_ban/Tap04_master.mp3` | 30.2 MB | 1256.52 s |
| `xuat_ban/Tap04_master.mp4` | 473.5 MB | 1256.50 s |
| `xuat_ban/thumbnail.png` | 1.2 MB | — |
