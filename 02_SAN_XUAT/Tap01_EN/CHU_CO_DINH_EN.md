# CHỮ CỐ ĐỊNH · BẢN TIẾNG ANH (Tập 01 + kênh)

> **BẢN NHÁP CHỜ DUYỆT (22/10/2026).** Đây là toàn bộ chữ tiếng Anh **không nằm trong kịch bản hay bảng shot**: khẩu hiệu, thẻ intro, nhãn nhân vật, chữ giao diện, thumbnail, mô tả YouTube.
> Mỗi mục ghi **chỗ đang viết cứng trong code** để khi triển khai chỉ cần thay đúng chỗ đó. Mục đánh dấu **⚠ DUYỆT** là chữ pháp lý hoặc thương hiệu, cần người dùng duyệt từng chữ giống bản VN.

---

## 1. Thương hiệu

| Mục | Tiếng Việt (đã duyệt) | Tiếng Anh (đề xuất) | Chỗ trong code |
|---|---|---|---|
| Tên kênh | Amber eyes | **Amber eyes** (giữ nguyên) | — |
| Khẩu hiệu ⚠ DUYỆT | Phân tích tâm lý tội phạm qua những hồ sơ có thật | **Criminal psychology through real case files** | `make_logo.py:158`, `assets/brand/channel.json` → `tagline` |

Phương án khác cho khẩu hiệu: *“Inside the criminal mind, one real case at a time”* hoặc *“Real cases. Real psychology.”* Đề xuất câu đầu vì sát nghĩa bản VN nhất.

## 2. Intro kênh (`make_intro.py:41-49` → xuất `assets/brand/intro_kenh_EN.mov`) ⚠ DUYỆT

Giữ nguyên nhạc `bgm_music_box` (22,41 s), thời điểm, bố cục. Chữ **đậm** = phần tô màu hổ phách, giống bản VN.

**Thẻ A — tiêu đề: `ABOUT THIS VIDEO`** (VN: VỀ NỘI DUNG NÀY)

| # | Tiếng Việt (đã duyệt) | Tiếng Anh (đề xuất) |
|---|---|---|
| 1 | Nội dung **giáo dục**, phân tích tâm lý học tội phạm. | **Educational** content: an analysis of criminal psychology. |
| 2 | Dựa trên **tư liệu công khai**, nguồn ở phần mô tả. | Based on **public records**; sources are in the description. |
| 3 | Không nhằm kết tội hay bôi nhọ bất kỳ ai. | Not intended to accuse or defame anyone. |

**Thẻ B — tiêu đề: `BEFORE YOU WATCH`** (VN: LƯU Ý TRƯỚC KHI XEM)

| # | Tiếng Việt (đã duyệt) | Tiếng Anh (đề xuất) |
|---|---|---|
| 1 | Nội dung **không phù hợp cho trẻ em**. | **Not suitable for children**. |
| 2 | Âm thanh và hình ảnh **chỉ mang tính minh hoạ**. | Sounds and images are **for illustration only**. |
| 3 | Không thay thế tư vấn y khoa, tâm lý hay pháp lý. | Not a substitute for medical, psychological or legal advice. |

Ghi chú: chữ tiếng Anh ngắn hơn bản VN nên vừa khung, không phải đổi cỡ chữ.

## 3. Nhãn nhân vật

**Badge góc trên trái** (`build_video3.py:37-39`, `ROLE_NAME`; khung 470 px):

| Vai | Tiếng Việt | Tiếng Anh — dòng 1 | Tiếng Anh — dòng 2 |
|---|---|---|---|
| H · Cú | HOST · Người dẫn chuyện | **HOST** | Your narrator |
| D · Sói | ĐIỀU TRA VIÊN · Hồ sơ vụ án Blanchard | **INVESTIGATOR** | Blanchard case file |
| C · Cáo | CHUYÊN GIA TÂM LÝ · Tâm lý học tội phạm | **PSYCHOLOGIST** | Criminal psychology |
| N1 · Cừu | NGƯỜI DÂN SPRINGFIELD · Hàng xóm nhiều năm | **SPRINGFIELD RESIDENT** | Longtime neighbor |
| N2 · Mèo | KHÁN GIẢ · Theo dõi vụ án | **VIEWER** | Following the case |

**Nhãn vai trong phụ đề** (`subtitles.py:16`): `INVESTIGATOR` · `PSYCHOLOGIST` · `RESIDENT` · `VIEWER` (Host không gắn nhãn, giống bản VN).

## 4. Chữ giao diện trong renderer (`build_video3.py`)

| Dòng | Tiếng Việt | Tiếng Anh | Ghi chú |
|---|---|---|---|
| 851 | TIẾP THEO | **NEXT** | Thẻ “Host mời” (`→X`) |
| 894 | Nhân vật minh hoạ · giọng đọc AI | **Fictional character · AI voice · Dramatized** | Dòng nhỏ dưới thẻ giới thiệu `✦`. Thêm “Dramatized” để người xem Mỹ không nhầm Sói/Cáo là điều tra viên hay chuyên gia có thật (xem `REVIEW_EN.md` §3) |
| 696 | MINH HOẠ | **ILLUSTRATION** | Nhãn góc trên ảnh minh hoạ |
| 375 | MẬT | **CONFIDENTIAL** | Dấu mộc. Chữ dài hơn → cỡ chữ dấu tự co theo bề ngang (cần thêm khi triển khai) |
| 375 | GIẢ MẠO | **FORGED** | Dấu mộc ở shot 4-20 |

Không đổi: từ khoá tiếng Việt mà renderer dò trong cột Beat (“Dấu mộc”, “giả mạo”, “Thanh tiến trình”). Cột Beat của bảng shot EN vẫn để tiếng Việt nên vẫn khớp.

**Font:** giữ Cambria (chữ có chân) và Bahnschrift (chữ số) như bản VN để hai bản cùng một giao diện. Cambria có đủ dấu của Folie à deux, DSM-5-TR. Bản EN viết **Munchausen** không có dấu hai chấm trên chữ u, theo cách viết thông dụng ở Mỹ (DSM, báo chí, từ khoá tìm kiếm).

## 5. Tiêu đề hồi

Dùng ở thẻ chuyển hồi (bảng shot, đã điền), mốc chương trong mô tả và tên chương (`package.py:57-59`).

| Hồi | Tiếng Việt | Tiếng Anh |
|---|---|---|
| 1 | Khoảnh khắc đứt gãy niềm tin | The Moment Trust Broke |
| 2 | 23 năm trong nhà tù y khoa | 23 Years in a Medical Prison |
| 3 | Bên trong bộ não của kẻ mắc FDIA | Inside the Mind Behind FDIA |
| 4 | Tại sao Gypsy không đứng dậy? | Why Didn’t Gypsy Stand Up? |
| 5 | Phán quyết pháp y & lời kết | The Verdict & Closing |

## 6. Thumbnail (`package.py:43`)

Hai dòng, giữ bố cục và font như bản VN:

```
POISON IN THE NAME
OF A MOTHER’S LOVE
```

Phương án ngắn hơn, đọc được trên điện thoại: `POISONED` / `BY HER MOTHER’S LOVE`. Đề xuất bản đầu vì trùng tên tập.

## 7. Mô tả YouTube (xuất ra `xuat_ban/description.txt`)

Mốc chương để `[mm:ss]`. Script tự điền sau khi đo thời lượng bản EN (bản EN ngắn hơn bản VN nên mốc sẽ khác).

```
Poison in the Name of a Mother’s Love — Inside Munchausen Syndrome by Proxy | Amber eyes

Today we step inside a small pink house in Missouri to unpack one of the strangest and cruelest psychological disorders ever hidden behind a mask of love: Munchausen syndrome by proxy. Dee Dee Blanchard was never formally diagnosed, but her behavior is widely believed to reflect this condition, which the modern diagnostic manual DSM-5-TR calls factitious disorder imposed on another (FDIA).

⏱ CHAPTERS
00:00 Intro
[mm:ss] Act 1 · The Moment Trust Broke
[mm:ss] Act 2 · 23 Years in a Medical Prison
[mm:ss] Act 3 · Inside the Mind Behind FDIA
[mm:ss] Act 4 · Why Didn’t Gypsy Stand Up?
[mm:ss] Act 5 · The Verdict & Closing

⚠️ PLEASE NOTE
• This video is not suitable for children.
• It is educational content, analyzed from the perspective of criminal psychology,
  and it is not a substitute for medical, psychological or legal advice.
• Information is based on public records (court documents, news reports, published interviews); see the sources below.
  Psychological analysis in this video is the channel’s opinion and commentary, not a clinical diagnosis of any person.
  The channel does not intend to accuse, defame or glorify any individual.
• The Owl, Wolf, Fox, Sheep and Cat are fictional, illustrated characters, not real people.
  The Investigator, the Psychologist, the neighbor and the viewer are dramatized composites; their lines are written
  from public records and do not represent any real investigator, psychologist, agency or resident.
• This video is not affiliated with or endorsed by any person, agency or organization mentioned.
• Voices, images and music were created for this channel with AI tools.

📚 SOURCES
[Paste the ✅ links from 02_SAN_XUAT/Tap01_EN/nguon_tham_khao_EN.md, one per line, before publishing]

🆘 If you know a child who is being abused, call or text the Childhelp National Child Abuse Hotline
at 1-800-422-4453 (USA, free, confidential, 24/7). In an emergency, call 911.
Outside the US, contact your local child protection hotline.
```

Số Childhelp 1-800-422-4453 (gọi hoặc nhắn tin, 24/7) đã kiểm trên trang chính thức childhelphotline.org ngày 22/10/2026. Nên kiểm lại lần nữa ngay trước khi đăng. Nếu kênh nhắm khán giả nhiều nước, giữ câu “Outside the US…”.

## 8. Tên tập và thẻ YouTube

- **Tiêu đề video:** `Poison in the Name of a Mother’s Love — Inside Munchausen Syndrome by Proxy | Amber eyes`. Dài 88 ký tự, dưới giới hạn 100.
- **Tên tập trên màn hình** (shot 1-21): `EPISODE 01 · POISON IN THE NAME OF A MOTHER’S LOVE`
- **Thẻ đề xuất:** Gypsy Rose Blanchard, Dee Dee Blanchard, Munchausen syndrome by proxy, FDIA, factitious disorder, criminal psychology, true crime, psychology explained, learned helplessness, trauma bonding
