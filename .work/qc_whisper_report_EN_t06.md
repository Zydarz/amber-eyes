# QC Whisper + UTMOS — EN_t06

ASR: `openai/whisper-large-v3` (greedy, Kaggle GPU) · CER = `vi_cer.cer_pair` (Q3a). MOS: `utmos22_strong` — mô hình tiếng Anh, **chỉ so tương đối** giữa các bản/vai.

| Vai | n | CER tb | CER max | file > 2% | UTMOS tb | UTMOS min |
|---|---:|---:|---:|---:|---:|---:|
| C | 94 | 0.48% | 5.0% | 9 | 4.40 | 4.28 |
| D | 113 | 0.29% | 4.2% | 4 | 3.88 | 3.47 |
| H | 219 | 0.38% | 11.6% | 9 | 4.36 | 3.74 |
| N1 | 10 | 1.87% | 8.6% | 2 | 4.26 | 4.13 |
| N2 | 10 | 1.19% | 3.5% | 3 | 3.37 | 3.11 |

## Câu mà MỌI bản đều > 2% (8/212 câu)

| Câu | Vai | CER tốt nhất | CER bỏ tên riêng | UTMOS | Bản chép (bản tốt nhất) |
|---|---|---:|---:|---:|---|
| 1.06#7 | H | 11.6% | 11.6% | 4.35 | The man promised to pay him a remarkable wage of $5 an hour. |
| 1.09#3 | N1 | 8.6% | 9.1% | 4.33 | Robert was so excited when Gacy mentioned a remodeling helper job paying $5 an hour. |
| 1.15#2 | C | 2.5% | 2.5% | 4.43 | Mask worn by predators of this typology is not forged from secretive isolation, but woven from the conspicuous glare of  |
| 2.04#4 | C | 2.3% | 2.3% | 4.40 | First stage, childhood trauma characterized by severe physical beatings and verbal humiliation by an alcoholic father, f |
| 2.04#5 | C | 5.0% | 5.3% | 4.42 | Second stage, initial sexual offenses in Iowa, where he began testing the use of social power to overpower vulnerable vi |
| 2.04#6 | C | 2.8% | 3.2% | 4.45 | Third stage, re-emerging post-prison with an upgraded facade of respectability, escalating to homicidal violence in Janu |
| 2.08#1 | H | 2.6% | 0.0% | 4.38 | An urgent identification search revealed that the JAS ring belonged to John Allen Sick, a 19-year-old young man who had  |
| 4.05#3 | N2 | 3.5% | 3.5% | 3.34 | Seconds later, when a crime scene detail was raised, his eyes would instantly snap cold, razor sharp, and calculating. |

## 10 file UTMOS thấp nhất (nghe kiểm tạp âm / méo)

| File | Vai | UTMOS | CER |
|---|---|---:|---:|
| 4_05_4_N2_N2_EN_t0.8_s1.wav | N2 | 3.11 | 0.9% |
| 4_05_5_N2_N2_EN_t0.8_s1.wav | N2 | 3.23 | 0.0% |
| 4_05_2_N2_N2_EN_t0.8_s1.wav | N2 | 3.29 | 0.0% |
| 4_05_1_N2_N2_EN_t0.8_s1.wav | N2 | 3.30 | 0.0% |
| 4_05_3_N2_N2_EN_t0.8_s0.wav | N2 | 3.34 | 3.5% |
| 4_05_1_N2_N2_EN_t0.8_s0.wav | N2 | 3.42 | 0.0% |
| 4_05_4_N2_N2_EN_t0.8_s0.wav | N2 | 3.45 | 0.9% |
| 4_05_2_N2_N2_EN_t0.8_s0.wav | N2 | 3.46 | 0.0% |
| 3_10_3_D_D_EN_t0.8_s1.wav | D | 3.47 | 0.0% |
| 4_05_5_N2_N2_EN_t0.8_s0.wav | N2 | 3.50 | 3.0% |
