# SO SÁNH 10 GIỌNG NỮ — câu mở đầu tập 01

**Câu thử:** *"Ngày 14 tháng 6 năm 2015. Tại thị trấn yên bình Springfield, bang Missouri, nước Mỹ."*
(block `O.4` của `KeHoach_ThuAm_Tap01.md` — dòng lời đầu tiên của tập, nằm ở **00:32 → 00:40,87**)

**Tham số giữ nguyên cho mọi bản** (chỉ đổi `voice_id`):
`emotion: sad` · `speed: 0.88` · `pitch: 0` · `volume: 1.0`

## File

| File | Nội dung |
|---|---|
| `so_sanh_giong_nu.mp3` | **Nghe tổng hợp** — 10 bản nối tiếp, mỗi bản cách nhau 1 s, đúng thứ tự A → J |
| `A_…` → `J_….mp3` | Từng bản riêng |
| `args.json` | Payload TTS gửi thật cho cả 10 bản |

## Bảng đo

| # | File | `voice_id` | Thời lượng | RMS | F0 | Âm tiết/s |
|---|---|---|---:|---:|---:|---:|
| A | `A_book_female.mp3` | `audiobook_female_1` **← đang dùng** | 7,94 s | −20,5 dB | 214,8 Hz | 1,39 |
| B | `B_whispering_girl.mp3` | `English_Whispering_girl` | 9,50 s | **−41,1 dB** | 216,2 Hz | 1,16 |
| C | `C_soft_spoken_girl.mp3` | `English_Soft-spokenGirl` | 11,15 s | −21,8 dB | **278,3 Hz** | 0,99 |
| D | `D_graceful_lady.mp3` | `English_Graceful_Lady` | 10,90 s | −15,1 dB | **185,0 Hz** | 1,01 |
| E | `E_lovely_girl.mp3` | `English_LovelyGirl` | 11,77 s | −18,8 dB | 250,0 Hz | 0,93 |
| F | `F_radiant_girl.mp3` | `English_radiant_girl` | 8,53 s | −21,8 dB | 210,5 Hz | 1,29 |
| G | `G_captivating_female.mp3` | `English_captivating_female1` | 7,60 s | −17,8 dB | 223,8 Hz | **1,45** |
| H | `H_sentimental_lady.mp3` | `English_SentimentalLady` | 10,66 s | −25,3 dB | 211,2 Hz | 1,03 |
| I | `I_vietnamese_kindhearted.mp3` | `Vietnamese_kindhearted_girl` | 8,72 s | −22,4 dB | 266,7 Hz | 1,26 |
| J | `J_compelling_lady.mp3` | `English_compelling_lady1` | 10,30 s | −16,9 dB | 214,0 Hz | 1,07 |

**Đường chuẩn để so sánh:** giọng nam `audiobook_male_1` đo được F0 **104–114 Hz**; giọng nữ
`audiobook_female_1` đo được **214,8 Hz** — cao gấp ~2×, đó là lý do bạn nghe "hơ hơ".

**Âm tiết/s** = tốc độ đọc cùng một câu. Nhóm voice English kéo dài 10–11,8 s
(0,93–1,16 âm tiết/s) → dấu hiệu đọc theo chính tả từng chữ. `audiobook_female_1` (1,39)
và `captivating_female1` (1,45) đọc trôi chảy nhất.

**Lưu ý:** mọi số đo trên bằng máy (autocorrelation + RMS). Chất tiếng Việt, ngữ điệu và
cảm giác "thì thầm" chỉ người nghe mới kết luận được.

## Vì sao có bản này

Bản gốc (`A`) dùng `emotion: sad`. Enum `emotion` của connector
`connector__matrix__batch_text_to_audio` **chỉ có**:
`happy · sad · angry · fearful · disgusted · surprised · neutral`
— không có `serious`, không có `whisper`.

Plan ghi chỉ dẫn *"DẪN: rất nhẹ, gần như thì thầm"* cho block `O.4`, nhưng theo ràng buộc
R1 mọi `*DẪN: …*` đều bị xoá trước khi gửi TTS ⇒ engine **không hề biết** chỉ dẫn đó.
Thứ nghe được là mặc định của voice + `sad` + `speed 0.88`.

Bản `B` (`English_Whispering_girl`, RMS −41,1 dB) là ứng viên khớp nhất với ý "gần như
thì thầm", nhưng phải bù gain khi mix.
