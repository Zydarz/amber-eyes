# CER lượt sản xuất Tập 02 (EN) — Higgs Audio v3

ASR `listen_audio` **2 lượt/câu**, lấy lượt xấu hơn. CER chính thức = `vi_cer.cer_pair` (chuẩn hoá **cả hai vế**, Q3a). `cer_pair_nonum` bỏ số · `cer_pair_prop` bỏ danh từ riêng (tách nhiễu ASR khỏi lỗi TTS). Ngưỡng: **CER < 2% mỗi vai**.

| Vai | Clip | Temp | n | CER tb | CER max | >2% | CER⊘Số tb | CER⊘DanhTự tb | F0 tb (AC thô) | Âm tiết/s |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| C | C_EN.wav | 0.8 | 19 | 0.45% | 2.8% | 1/19 | 0.32% | 0.29% | 188 Hz | 2.81 |
| D | D_EN.wav | 0.8 | 43 | 0.37% | 2.2% | 2/43 | 0.39% | 1.28% | 94 Hz | 2.45 |
| H | H_EN.wav | 0.8 | 32 | 1.52% | 43.1% | 3/32 | 1.78% | 3.54% | 112 Hz | 2.87 |
| N2 | N2_EN.wav | 0.8 | 8 | 1.16% | 5.3% | 2/8 | 1.16% | 1.16% | 231 Hz | 2.91 |

## Câu có ít nhất 1 bản CER > 2% (cần vòng 2 theo §7)

| Câu | CER max | số bản |
|---|---:|---:|
| 4.12#5 | 43.1% | 2 |
| 4.06#3 | 5.3% | 2 |
| 4.11#6 | 2.8% | 2 |
| 4.06#4 | 2.6% | 2 |
| 4.03#2 | 2.3% | 2 |
| 4.10#7 | 2.2% | 3 |

**Tổng: 6/47 câu có ít nhất 1 bản vượt 2%.**
