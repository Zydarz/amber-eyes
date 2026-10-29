# CER tiếng Việt — Tập 02 (đã sửa chuẩn hóa số + loại lỗi ASR bị chặn)

Đo trên chính file TTS đã xuất của Tập 02. ASR = `listen_audio`, CER = `cer()` của dự án.
Cả hai vế (chuẩn và giọng đọc) đều đưa về dạng chữ bằng `vi_numbers()` trước khi so.
Ngưỡng dự án: **< 2%**.

## Host — `English_CaptivatingStoryteller`
- Số câu: **15** · CER trung vị **0.0%** · trung bình **0.5%** · thấp nhất 0.0% · cao nhất 3.9%
- Vượt ngưỡng 2%: **2/15** câu

| id | CER | AI nghe sai chỗ nào |
|---|---:|---|
| `1.14#2` | 3.9% | [replace] "ấy chủ" -> "nay chú" |
| `2.04#2` | 2.2% | [replace] "hắn" -> "hẳn"; [replace] "ròng" -> "rong" |
| `5.04#6` | 1.0% | [replace] "genest" -> "jenest" |
| `4.03#4` | 1.0% | [replace] "smyth" -> "smith" |
| _(11 câu CER = 0,0%)_ | 0,0% | |

## Dieu tra vien — `Korean_ColdYoungMan`
- Số câu: **15** · CER trung vị **0.0%** · trung bình **3.0%** · thấp nhất 0.0% · cao nhất 28.0%
- Vượt ngưỡng 2%: **6/15** câu

| id | CER | AI nghe sai chỗ nào |
|---|---:|---|
| `2.05#9` | 28.0% | [replace] "thứ hắn lấy đi" -> "thương hiệu han lady" |
| `2.05#3` | 5.2% | [replace] "ban đầu williams" -> "mando william" |
| `4.08#1` | 4.3% | [replace] "jim smyth" -> "james smith" |
| `2.05#12` | 3.9% | [replace] "lờn" -> "nâng" |
| `4.08#5` | 2.2% | [replace] "tweed" -> "twit" |
| `4.08#3` | 2.1% | [replace] "smyth" -> "smith"; [replace] "williams" -> "william" |
| _(9 câu CER = 0,0%)_ | 0,0% | |

## Chuyen gia — `English_AssertiveQueen`
- Số câu: **15** · CER trung vị **0.0%** · trung bình **0.4%** · thấp nhất 0.0% · cao nhất 3.4%
- Vượt ngưỡng 2%: **1/15** câu

| id | CER | AI nghe sai chỗ nào |
|---|---:|---|
| `3.08#6` | 3.4% | [delete] "ở" -> "" |
| `4.11#5` | 1.5% | [replace] "smyth" -> "smith" |
| `4.11#3` | 1.4% | [replace] "smyth" -> "smith" |
| _(12 câu CER = 0,0%)_ | 0,0% | |

## Doi chung — `English_CalmWoman`, `Vietnamese_kindhearted_girl`
- Số câu: **10** · CER trung vị **0.0%** · trung bình **1.4%** · thấp nhất 0.0% · cao nhất 13.2%
- Vượt ngưỡng 2%: **1/10** câu

| id | CER | AI nghe sai chỗ nào |
|---|---:|---|
| `1.14#2` | 13.2% | [replace] "ấy chủ" -> "nay chú"; [replace] "lái chiếc" -> "lại check"; [replace] "chiếc" -> "check" |
| `1.14#2` | 1.3% | [replace] "chủ" -> "chú" |
| _(8 câu CER = 0,0%)_ | 0,0% | |
