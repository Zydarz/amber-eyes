# TẬP 01 · BẢN TIẾNG ANH · HỒ SƠ CHỜ DUYỆT

**Phương án:** cách 2, dựng lại toàn bộ bằng tiếng Anh (giọng đọc, chữ trên màn hình, intro, phụ đề, gói đăng). Hình nền, linh thú, nhạc, nhịp shot dùng lại của bản VN.
**Trạng thái (22/10/2026): ĐÃ DỰNG XONG.**
- Video: **`xuat_ban/Tap01_EN_master.mp4`** (19:21, lần 2).
- Lần 2 có giọng Host mới, diễn xuất từng câu và thêm SFX. Bản lần 1 lưu ở `xuat_ban/_lan1/`.
- Đi kèm: `Tap01_EN_master.mp3`, `Tap01_EN.srt`, `thumbnail.png`, `description.txt`.
- Số đo và QC: `KeHoach_Video_Tap01_EN.md` mục B2.

**Đã duyệt:** khẩu hiệu EN; tên kênh “Amber eyes” giống bản VN; giọng Host `English_magnetic_voiced_man` (chọn sau khi nghe demo `thu_giong/host_moi/`); 4 giọng còn lại là ứng viên 1 ở §3.

---

## 1. Các file cần đọc

| # | File | Nội dung | Việc của bạn |
|---|---|---|---|
| 1 | `01_KICH_BAN/Tap01_EN/kichban_tap01_EN.md` | Kịch bản tiếng Anh, cùng cấu trúc bản VN v2 (33 lượt · 128 câu · 2.639 từ), đã review | Đọc duyệt lời |
| 1b | `02_SAN_XUAT/Tap01_EN/REVIEW_EN.md` | Báo cáo review chính tả, dữ kiện, pháp lý Mỹ và 63 câu đã đổi | Đọc trước |
| 2 | `02_SAN_XUAT/Tap01_EN/CHU_CO_DINH_EN.md` | Khẩu hiệu, 2 thẻ intro, nhãn nhân vật, chữ giao diện, tiêu đề hồi, thumbnail, mô tả YouTube | Duyệt từng chữ các mục ⚠ |
| 3 | `02_SAN_XUAT/Tap01_EN/KeHoach_Video_Tap01_EN.md` | Bảng 122 shot, chữ màn hình tiếng Anh | Đọc lướt cột Chữ |
| 4 | `02_SAN_XUAT/Tap01_EN/thu_giong/` | `so_sanh_giong_EN.mp3` (10 đoạn, mỗi vai 2 giọng) + `report.md` (CER, tốc độ, cao độ) | Nghe và chọn 1 giọng mỗi vai (§3) |

File phụ trợ (không cần đọc): `.work/script_EN.json` (kịch bản đã tách câu), `.work/shots_text_EN.json` (nguồn chữ của bảng shot), `.work/_build_plan_en.py` (dựng và kiểm bảng shot EN), `.work/voice_audition_EN.py` (thử giọng).

Đã kiểm bằng script:
- `parse_kichban.py` đọc bản EN ra 61 phần tử, 128 câu, **mã câu trùng 100%** bản VN; đầu ra bản VN không đổi.
- `parse_shots.py` đọc bảng shot EN ra 122 shot, không thiếu nền.
- 21 cụm beat tiếng Anh đều có trong câu tương ứng.
- Số và trích dẫn trên màn hình khớp lời (V3).

## 2. Review chính tả, dữ kiện và luật pháp Mỹ: ĐÃ XONG (22/10/2026)

Chi tiết ở **`REVIEW_EN.md`**. Tóm tắt:
- **Chính tả:** kiểm tự động 1.704 từ, 0 lỗi. Đã chuẩn hoá theo kiểu Mỹ: *Munchausen* không dấu, dấu câu trong ngoặc kép, gạch dài.
- **Ngôn ngữ:** bỏ “groomed” vì ở Mỹ dễ hiểu là dụ dỗ xâm hại trẻ em; sửa câu lủng và từ lặp.
- **Dữ kiện:** sửa 16 điểm sai hoặc không có nguồn. Quan trọng nhất:
  - câu trích của Gypsy không có thật → thay bằng câu thật trên GMA (01/2024);
  - lời Patterson → thuật lại đúng ý ông;
  - “48 hours” → “one day later”;
  - chi tiết vụ 2011;
  - Disneyland → Disney World;
  - bỏ địa chỉ nhà riêng.
- **Pháp lý:**
  - sửa đúng mọi lời trích hoặc thuật của người còn sống;
  - phân tích tâm lý viết thành ý kiến, không khẳng định như sự thật;
  - bỏ nhận xét “unstable personality” về Godejohn;
  - nhân vật ghi “Fictional character · AI voice · Dramatized”;
  - mô tả có thêm các câu miễn trừ;
  - khi đăng chọn *Not made for kids* và bật *Altered or synthetic content*.
- **Chỉ sửa bản tiếng Anh** (quyết định ngày 22/10/2026); bản VN giữ nguyên.
- Nguồn cho từng dữ kiện: **`nguon_tham_khao_EN.md`** (✅ đã khớp, ⚠ cần nguồn gốc tốt hơn).

## 3. Chọn giọng

Mỗi vai thử 2 giọng tiếng Anh, đọc cùng một câu. Bảng đo ở `thu_giong/report.md`.

| Vai | Ứng viên 1 | Ứng viên 2 | Câu thử |
|---|---|---|---|
| H · Cú | `English_CaptivatingStoryteller` | `English_expressive_narrator` | `2.04#2` |
| D · Sói | `English_Deep-VoicedGentleman` | `English_Trustworth_Man` | `1.11#3` |
| C · Cáo | `English_Wiselady` | `English_CalmWoman` | `3.08#2` |
| N1 · Cừu | `English_SentimentalLady` | `English_Kind-heartedGirl` | `1.07#1` |
| N2 · Mèo | `English_captivating_female1` (đang dùng cho Mèo ở bản VN) | `English_radiant_girl` | `4.03#1` |

Thứ tự trong file mp3 giống bảng trên (H1, H2, D1, D2…). Lần thử đầu cho Host dùng câu `1.03#1` (“June 14th, 2015.”, chỉ 2 giây). Câu quá ngắn để đánh giá, và ASR ghi ngày theo cách khác nên CER báo sai 78,6% dù hai giọng đọc đúng. Vì vậy đã thử lại bằng câu dài hơn; bản đầu lưu ở `thu_giong/_lan1/`. Giọng nào cũng phải đạt CER 0–2%; nếu bạn không ưng cặp nào, tôi thử thêm ứng viên.

## 4. Quyết định của bạn

1. **Đăng ở đâu?**
   - **(a) Kênh tiếng Anh riêng** (ví dụ “Amber eyes” bản EN). Đề xuất: YouTube gợi ý video theo ngôn ngữ của kênh, trộn hai ngôn ngữ dễ làm cả hai bản kém đề xuất.
   - **(b) Cùng kênh, danh sách phát riêng.**
   - (YouTube có tính năng thêm *audio track* nhiều ngôn ngữ cho cùng một video, nhưng chữ trên màn hình vẫn là tiếng Việt, nên không hợp với cách 2.)
2. **Duyệt chữ ⚠** trong `CHU_CO_DINH_EN.md`: khẩu hiệu EN và 2 thẻ intro EN.
3. **Chọn 5 giọng** (§3).
4. **Đọc `REVIEW_EN.md`**, nhất là phụ lục 63 câu đã đổi.

## 5. Cách chạy lại (đã triển khai)

Mọi script đọc công tắc `AE_LANG` trong `.work/edition.py`. Không đặt thì chạy bản VN với đường dẫn cũ (đã kiểm: `shots.json` và `tts_manifest.json` bản VN giống hệt từng byte).

```
set AE_LANG=en            (Git Bash: AE_LANG=en py -3 …)
py -3 .work/tts_sentences.py      → .work/audio_s_EN/
py -3 .work/qc_asr.py             → .work/qc_asr_EN/report.md
py -3 .work/build_audio3.py       → timeline_s_EN.json, stems_EN/, Tap01_EN_master.mp3
py -3 .work/parse_shots.py        → shots_EN.json
py -3 .work/build_audio3.py       → lượt 2: đặt SFX theo shot (sfx_shots_EN.json)
py -3 .work/build_video3.py       → video3_EN/picture.mp4   (~25 phút)
py -3 .work/subtitles.py          → Tap01_EN.srt
py -3 .work/package.py --mux      → Tap01_EN_master.mp4, thumbnail.png, description.txt
py -3 .work/make_intro.py         → assets/brand/intro_kenh_EN.mov (chỉ khi đổi thẻ intro)
```
Sửa chữ màn hình: sửa `.work/shots_text_EN.json` → `py -3 .work/_build_plan_en.py` → dựng lại bảng shot.

## 5b. Kế hoạch ban đầu (đã làm hết)

Nguyên tắc: **không ghi đè bất kỳ file nào của bản VN.** Mọi đầu ra EN có hậu tố `_EN` hoặc nằm trong `02_SAN_XUAT/Tap01_EN/`.

| Bước | Script | Thay đổi | Đầu ra |
|---|---|---|---|
| 1 | Tất cả script `.work/` | Thêm tham số ngôn ngữ `--lang en`, chọn bộ đường dẫn: `script_EN.json`, `tts_manifest_EN.json`, `timeline_s_EN.json`, `shots_EN.json`, `audio_s_EN/`, `stems_EN/`, `video3_EN/`, `OUT_DIR = 02_SAN_XUAT/Tap01_EN/xuat_ban`. Mặc định vẫn là `vi` nên lệnh cũ chạy y như trước | — |
| 2 | `make_logo.py`, `make_intro.py` | Khẩu hiệu và 2 thẻ EN (sau khi duyệt) | `assets/brand/logo_lockup_EN.png`, `intro_kenh_EN.mov` |
| 3 | `tts_sentences.py` | `CAST_EN` theo giọng đã chọn. Cảm xúc và tốc độ **lấy theo mã câu từ `tts_manifest.json` bản VN**, vì ghi chú diễn xuất bản EN là tiếng Anh, không khớp từ khoá VN. Vẫn giữ quy tắc `N_ELEMENT` (1.07 → N1, 4.03 → N2) | 128 file `audio_s_EN/s*_*.mp3` |
| 4 | QC giọng | Nhận dạng lại 128 câu (prompt tiếng Anh), CER phải bằng 0; câu lỗi thì thu lại | báo cáo CER |
| 5 | `build_audio3.py` | Giữ nguyên logic: intro 22,41 s, lời đầu 23,0 s, các mốc `1.06`/`1.09`/`1.12` cùng mã. Đo lại toàn bộ thời gian | `timeline_s_EN.json`, `Tap01_EN_master.mp3`, −16 LUFS |
| 6 | `parse_shots.py` | `PLAN` → `KeHoach_Video_Tap01_EN.md` | `shots_EN.json` |
| 7 | `build_video3.py` | Bảng chữ theo ngôn ngữ (`ROLE_NAME`, NEXT, ILLUSTRATION, dấu CONFIDENTIAL/FORGED, dòng “Fictional character · AI voice · Dramatized”); dấu mộc tự co chữ theo bề ngang; intro EN | `video3_EN/part*.mp4` → `Tap01_EN_master.mp4` |
| 8 | `subtitles.py` | Phụ đề tiếng Anh từ `script_EN.json`, nhãn vai EN | `Tap01_EN.srt` |
| 9 | `package.py` | Thumbnail, mô tả, mốc chương EN (tự điền mốc từ timeline EN) | `thumbnail.png`, `description.txt`, `nguon_tham_khao_EN.md` |
| 10 | QC toàn tập | Như bản VN: không có đoạn câm tuyệt đối, phủ 128/128 câu, V3, 0 từ bạo lực (thêm danh sách từ tiếng Anh), giải mã 0 lỗi | báo cáo QC |

Thời gian máy chạy ước tính tương đương bản VN. Bản EN ngắn hơn khoảng 1 phút (≈ 18 phút so với 18:53).
