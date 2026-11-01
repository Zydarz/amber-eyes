# Chạy thử Higgs bản TIẾNG ANH — Tập 02 hồi 4 (31/10/2026)

Kernel `chiduong2026/amber-eyes-higgs-prod-en-t02-a4-kaggle-gpu` · dataset `chiduong2026/amber-eyes-voice-ref-voxcpm2-en` (riêng, §4.4) · bộ giọng TẠM `.work/g9_role_map_EN.json`.
47 câu (H 16, D 18, C 9, N2 4) · **102/102 file OK, 0 FAIL** (2 worker × 51, ~9,5 phút). Lượt tải đầu chỉ được 100 file (CLI tải 1 trang 100 file + phiên CLI gián đoạn) — đã tải bổ sung `4.12#6` + manifest/log. `measure_cer_prod.py` (AE_LANG=en) chạy trọn: 102/102 có ASR; `4.12#6` CER 0%. **46/47 câu có bản ≤ 2%**.

## Giọng mẫu (trước khi chạy)
ASR 2 lượt trên 5 clip `_EN`: **CER 0%** cả 5 (§4.2 đạt).

## Cao độ trên bản Higgs đọc (câu neutral, AC / YIN)
| Vai | AC | YIN |
|---|---:|---:|
| H | 113,7 | 115,9 |
| D | 93,8 | **73,8** |
| C | 185,4 | 190,3 |
| N2 | 231,4 | 233,4 |

G9 (min AC/YIN): **D–H 3,35 nc TRƯỢT** (AC; YIN cho 7,8 nc — giọng D rất khàn, 2 thuật toán lệch 4 nc) · C–H 8,45 · H–N2 12,11 · C–D 11,80 ✅. G8: 0 bản lệch ≥ 4 nc.
Khác bản Việt: Higgs đọc tiếng Anh **không** kéo Host lên ~125 Hz (114–116 Hz).

## CER (en_cer, 2 lượt, lấy lượt xấu hơn)
| Vai | file | CER tb | max | >2% |
|---|---:|---:|---:|---:|
| H | 30 | 1,62% | 43,1% | 3 |
| D | 43 | 0,37% | 2,2% | 2 |
| C | 19 | 0,45% | 2,8% | 1 |
| N2 | 8 | 1,16% | 5,3% | 2 |

Theo câu (bản tốt nhất): **45/46 câu ≤ 2%**. Câu còn lại `4.03#2` 2,3% là lỗi chuẩn hoá ("3:00 PM" ↔ "3:00 p.m."), không phải lỗi đọc.

## Kết luận
- Đọc đúng chữ rất tốt (tốt hơn bản Việt: T02 VN lượt 1 có 29/203 câu > 2%).
- **Chặn duy nhất: D–H theo cổng G9** — cần tai người dùng phân xử (file `02_SAN_XUAT/Tap02_EN/thu_giong_higgs_a4/2_xen_ke_H_D_C.wav`).
- File nghe: `02_SAN_XUAT/Tap02_EN/thu_giong_higgs_a4/1_hoi4_lien_mach.wav` (46 câu, 282,6 s).
