# ÂM THANH TẬP 02 — GIỌNG ĐỌC & HIỆU ỨNG (22–23/10/2026)

> **TRẠNG THÁI HIỆN TẠI (23/10/2026) — đọc mục này trước, phần dưới là nhật ký theo thời gian**
>
> | Hạng mục | Đang dùng trong `Tap02_master.mp4` |
> |---|---|
> | Giọng | **Bộ A**: Host `English_CaptivatingStoryteller` (trầm ấm) · Điều tra viên `Korean_ColdYoungMan` (lạnh lùng) · Chuyên gia `English_AssertiveQueen` (nhấn mạnh). Chọn qua 2 vòng thử, lý do và số liệu ở `BaoCao_GiongDoc_Tap02.md` §4–5. Mục 2.4 dưới đây ("đề xuất giữ giọng cũ") **đã bị thay** |
> | Diễn xuất | `acting_tap02.json`: cao độ luôn 0; chỉ neutral 160 · sad 28 · fearful 14 · surprised 13; 10 câu có một thẻ ngắt trước câu trích; 70 chỗ nghỉ thêm giữa câu (27 s) |
> | Số trong lời đọc | Tự đổi sang chữ tiếng Việt (G11): "1.400" → "một nghìn bốn trăm", "Elizabeth II" → "Elizabeth Đệ nhị". 23 câu đọc lại 23/10 |
> | Kiểm tra giọng | G10 đạt: mỗi vai nghe liền ra 1 người; 3 vai xen kẽ tách bạch 10/10 (`thu_giong_kiem_vai/`) |
> | Nền môi trường | 14 đoạn (`sfx_tap02.json`); **cả 8 nền đều là tiếng thật YouTube Audio Library** (căn cứ không quân · gió tuyết · đường xa · điều hoà văn phòng · máy ù tầng hầm · room tone phòng thẩm vấn · hội trường toà án · lửa). Thêm nền `amb_office_night` dưới lời kết (vá khoảng câm 0,6 s) |
> | Tiếng động | 37 lượt đặt, **24 mã tiếng — cả 24 đều là tiếng thật YouTube Audio Library** (mục 3.3.1). 21 mã được cắt đúng đoạn, toàn bộ 32 file đã mastering để không clip khi trộn (3.3.2) |
> | Quy tắc đã đưa vào tiêu chuẩn | A4.1 (bộ A), A4.2 G1–G11, A4.4 (nền, tắt nhạc, stereo), A11 bẫy #17–24 |

**Vì sao có file này:** người xem phản hồi Tập 01: (1) giọng mọi nhân vật đều đều, không lên xuống, không điểm nhấn, nghe buồn ngủ; (2) SFX nhàm chán, ít, không thấy chân thật. File này ghi chẩn đoán bằng số đo, cách sửa cho Tập 02, và việc còn chờ.

---

## 1. Chẩn đoán Tập 01 (đo trên file thật)

### Giọng (`.work/audio_s/`, 128 câu)

| Vai | Cảm xúc dùng | Cao độ giữa các câu lệch | Tốc độ | So với bản EN (đã diễn xuất từng câu) |
|---|---|---:|---:|---|
| Cú · Host | neutral 45 · sad 18 | 1,47 nửa cung | 3,28 âm tiết/s | — |
| Sói · Điều tra viên | **neutral 25/25** | **0,85** | **3,76** | EN: 4 loại cảm xúc, lệch 1,63 |
| Cáo · Chuyên gia | **neutral 34/34** | **0,87** | 3,48 | EN: 5 loại cảm xúc, lệch 2,28 |

**Nguyên nhân, theo thứ tự ảnh hưởng:**
1. **Bản tiếng Việt chưa từng có diễn xuất từng câu.** `tts_sentences.py` chỉ đổi cảm xúc theo *chỉ dẫn của cả lượt nói* (9 từ khoá); file diễn xuất và ngắt nghỉ `<#s#>` chỉ bật cho bản EN. Mọi câu trong một lượt đọc y hệt nhau.
2. **Đọc nhanh và đều:** Sói 3,76 âm tiết/giây, không có ngắt trong câu. Khoảng nghỉ giữa các câu cố định (0,35 / 0,60 / 0,70 s), nên câu hé lộ cũng chỉ được nghỉ đúng 0,35 s như mọi câu.
3. **Giọng được chọn theo độ đúng, không theo độ biểu cảm:** buổi thử giọng (`.work/voice_test5/`) chỉ đo tỉ lệ lỗi chữ (CER 0%). Ba giọng chính là giọng đa ngôn ngữ đọc tiếng Việt; kho giọng chỉ có **một** giọng tiếng Việt gốc (`Vietnamese_kindhearted_girl`).

*Lưu ý khi đọc số:* tiếng Việt có thanh điệu nên dải cao độ **trong** một câu luôn rộng (11–15 nửa cung). Thứ tạo cảm giác "đều đều" là cao độ và tốc độ **giữa** các câu không đổi — đó là chỉ số cần nâng.

### SFX (`build_audio3.py`)

- **14 tiếng trong 19 phút**, tức khoảng một tiếng mỗi 80 giây. Giữa các câu chỉ có nhạc.
- **Không có nền môi trường.** Người nghe không "ở trong" cảnh nào cả: phòng thẩm vấn, ngoài trời tuyết hay phòng xử đều cùng một không khí.
- **Toàn bộ mono, gần như khô:** độ vang chỉ là 5 tiếng dội cố định. Bản xuất là stereo nhưng hai kênh giống hệt nhau.
- Mức âm cố định, một lớp, không có nhấn kịch tính (hit, sub-drop, stinger) ở khoảnh khắc hé lộ.

---

## 2. Giọng — cách sửa cho Tập 02

### 2.1 Đã làm: diễn xuất từng câu cho cả 215 câu

- Bộ sinh: `.work/make_acting_tap02.py` → `.work/acting_tap02.json`. Cùng định dạng với `acting_EN.json`: `[cảm xúc, lệch tốc độ, cao độ, lời đọc riêng]`.
- **Không đổi chữ nào:** lời đọc riêng chỉ thêm `...` và thẻ ngắt `<#s#>`, phụ đề và chữ trên hình giữ nguyên. Đã kiểm bằng script: 214/215 câu khớp từng chữ. Câu `2.07#3` bỏ "(Signature)" để giọng Việt khỏi đọc tiếng Anh; phụ đề vẫn giữ.
- **Nguyên tắc diễn xuất:**

| Nguyên tắc | Cách làm | Ví dụ |
|---|---|---|
| Chậm hơn | Tốc độ gốc giảm 0,02–0,05 → mục tiêu ~3,0 âm tiết/s; câu chậm nhất giới hạn ở −0,14 | |
| Câu ngắn "đóng đinh" | ≤ 8 tiếng: chậm thêm 0,05, hạ 1 bậc cao độ | "Đó là sự sợ hãi." |
| Hé lộ = ngắt trước từ khoá | `... <#0.6#>` ngay trước thông tin mới | "…hạ cửa kính xuống… ‹0,6 s› chính là… ‹0,3 s› Chỉ huy trưởng căn cứ" |
| Đổi cảm xúc theo nhịp | Dẫn chuyện neutral → căng fearful → hé lộ surprised → lắng sad; lời kết happy, cao độ +1/+2 | Hồi 5 kết ấm lên |
| Liệt kê có nhịp | Mỗi mục cách 0,15–0,2 s | "chụp ảnh, ‹› lấy đồ, ‹› rồi ghi chép lại" |
| Câu hỏi | surprised, cao độ +1 | |
| Câu cuối lượt | hạ 1 bậc để khép ý | |
| Nghỉ thêm sau câu | 70 câu, tổng 27 s (`_pause_after`) — chừa chỗ cho khoảnh khắc và SFX | `4.10#9` "Có bản đồ không?" → nghỉ thêm 1,2 s |
| Cao độ an toàn | Giữ trong −4…+3 vì tiếng Việt có thanh điệu (đẩy xa dễ méo dấu) | |

Kết quả phân bố: neutral 145 · sad 28 · fearful 14 · surprised 13 · happy 12 · angry 2 · disgusted 1. Tập 01: Sói và Cáo 100% neutral.

### 2.2 Chưa làm được: thử giọng thật

Script thử đã sẵn: `.work/voice_act_test_tap02.py`. 7 câu then chốt, mỗi câu đọc 3 kiểu: **A** như Tập 01 · **B** có diễn xuất · **C** có diễn xuất + giọng thay thế (H `English_magnetic_voiced_man`, D `English_Deep-VoicedGentleman`, C `English_Wiselady`).

Kết quả đo gồm: tốc độ, tỉ lệ ngắt nghỉ, CER (có đọc đúng tiếng Việt không), thẻ ngắt có bị đọc ra không. Thêm file nghe so sánh `thu_giong/so_sanh_dien_xuat.mp3`.

**Trạng thái:** ngày 22/10, **dịch vụ đọc giọng lỗi phía máy chủ** ("audio post-processing failed… try again later"); thử 3 lần, kể cả một câu "Xin chào.", đều lỗi. Khi dịch vụ chạy lại:
```
py -3 .work/voice_act_test_tap02.py
```
**Tiêu chí chọn:**
- Đạt nếu B nghe khác A rõ rệt mà CER vẫn ≈ 0% và không đọc thẻ thành tiếng.
- Chỉ đổi giọng (C) khi C hay hơn B rõ và CER < 2%.
- Đổi giọng là đổi "diện mạo" kênh so với Tập 01, nên người dùng quyết.

### 2.3 Sửa code — ĐÃ LÀM 22/10 (người dùng cho phép)

| Script | Sửa |
|---|---|
| `tts_sentences.py` | Đọc file diễn xuất của tập cho **cả bản tiếng Việt** (hiện chỉ EN). Hàm `pause_tags`: dấu `:` trước chữ hoa tiếng Việt (Đ, Ư, Â…), hiện regex `[A-Z]` bỏ sót |
| `build_audio3.py` | Cộng `_pause_after` vào khoảng nghỉ sau câu |
| `qc_asr.py` | Chạy cho bản VN sau khi đọc, để bắt thẻ ngắt bị đọc ra hoặc lỗi chữ |

---

### 2.4 KẾT QUẢ THỬ GIỌNG 23/10/2026 (3 vòng, 74 bản đọc)

Chấm bằng mô hình nghe: mỗi câu ghép các bản đọc vào một file và hỏi bản nào biểu cảm, tự nhiên, đúng thanh điệu, hợp phim tài liệu hơn. Cộng thêm nhận dạng lại để bắt chữ đọc sai.

| Vòng | Cách diễn xuất | Khoảng lặng trong câu | Thắng / 7 câu | Nhận xét chính |
|---|---|---:|---:|---|
| 1 | Nhiều `...` + thẻ ngắt, chậm mạnh | 40–48% | 2 | "Vụn, như robot" — nhịp 3–4/10 |
| 2 | Giảm ngắt (≤ 2 thẻ, ≤ 0,35 s) | 34–47% | 3 | Vẫn vụn; cảm xúc sad/fearful tự làm máy đọc chậm |
| **3** | **Không ngắt giữa câu** (chỉ 1 thẻ trước câu trích), cảm xúc + cao độ, chậm ≤ 0,06 | **17–38%** | **7/7** (bản cũ A: 0/7) | Nhịp 5–6/10, biểu cảm 6/10 (A: 4–6) |

**Đã áp dụng:** `make_acting_tap02.py` hàm `soften()` → `acting_tap02.json`: lời đọc dựng lại từ câu gốc, giữ nguyên dấu câu; chỉ 10 câu có thẻ ngắt trước câu trích; lệch tốc độ trong −0,06…+0,02. Giữ nguyên cảm xúc, cao độ và 70 chỗ nghỉ thêm **giữa** các câu (27 s).

**Bài học cho các tập sau:** với giọng đọc tiếng Việt, kịch tính đặt ở **khoảng lặng giữa câu** + nhạc + tiếng động. **Không** đặt `...` hay thẻ ngắt giữa câu.

**Giọng — đề xuất lúc đó: GIỮ giọng hiện tại cho cả 5 vai** — ⚠ *đã bị thay ngày 23/10: người dùng phát hiện Host đổi danh tính và giọng nam giống nhau → bộ A, xem `BaoCao_GiongDoc_Tap02.md`.*

| Vai | Ứng viên tốt nhất | Lý do không đổi |
|---|---|---|
| Host | `English_Trustworth_Man` (thắng 1 câu) | Thua nặng câu còn lại (4/10, "nhanh và phẳng"); `audiobook_male_1` ổn định 6–7/10 |
| Điều tra viên | `Chinese (Mandarin)_Gentleman` (thắng 2/2 câu, chất giọng trầm hợp vai) | **Đọc sai "bản đồ" → "bạn nào" / "bận rộn" ở 2/3 vòng**, đúng câu đắt nhất tập |
| Chuyên gia | `English_CalmWoman` (thắng 1, thua 1) | Không hơn rõ; vòng thử 22/10 từng sai 9,3% chữ |
| N2 | — | `English_SereneWoman`, `Vietnamese_kindhearted_girl` không thắng câu nào |

Người dùng đã chấp nhận đổi giọng, nhưng số liệu chưa đủ để đổi. **Nghe để quyết:** `thu_giong_vong3/so_sanh_vong3.mp3`. Thứ tự mỗi câu: A → S → S2; riêng N2 không có S2.

Nếu vẫn muốn Sói giọng trầm hơn: thử `Chinese (Mandarin)_Gentleman` với **cao độ 0** (không hạ) để giữ thanh điệu, rồi kiểm lại câu `4.10#9`.


---

## 3. SFX — cách sửa cho Tập 02

### 3.1 Đã làm: bộ âm mới, ba lớp

Bộ sinh: `.work/make_sfx3.py` → `assets/sfx/t2/`, 32 file, **stereo**, có vang tích chập (phòng nhỏ / vừa / sảnh / ngoài trời). Tự tổng hợp, không dùng mẫu ngoài, có seed để tái lập.

> **Cập nhật 23/10/2026:** **32/32 file** trong bộ này đã bị **thay bằng tiếng tải từ YouTube Audio Library** (xem 3.3.1). Bản tự tổng hợp của cả 32 file được giữ lại ở `assets/sfx/t2/_code/` để quay về bất cứ lúc nào (chép đè lên `assets/sfx/t2/<mã>.wav`).

| Lớp | File | Vai trò |
|---|---|---|
| **1. Nền môi trường** (98–474 s, nối vòng) | `amb_airbase` · `amb_winter_wind` · `amb_road_night` · `amb_interrogation` (đèn huỳnh quang 120 Hz rè + máy lạnh) · `amb_basement` (ù + nước nhỏ giọt) · `amb_office_night` (đồng hồ + xe xa) · `amb_courtroom` · `amb_fire` | Chạy **liên tục** dưới lời, đổi theo cảnh, ở −27 … −38 dB so với lời. Đây là lớp thiếu nhất ở Tập 01 |
| **2. Tiếng động** | `fx_tire_snow` · `fx_footsteps_snow` · `fx_window_down` · `fx_flashlight` · `fx_police_radio` · `fx_door_metal_slam` · `fx_phone_ring` · `fx_camera_shutter` · `fx_drawer_open` · `fx_hdd_spin` · `fx_chair_scrape` · `fx_cup_down` · `fx_photo_slide` · `fx_paper_folder` · `fx_pen_scribble` · `fx_map_unfold` · `fx_metal_snip` · `fx_metal_crush` · `fx_fire_whoosh` · `fx_gavel_triple` | Gắn đúng hành động trong lời, có vị trí trái/phải |
| **3. Nhấn kịch tính** | `fx_sub_drop` · `fx_stinger` · `fx_heartbeat_slow` · `fx_tension_tick` | Ở 8 khoảnh khắc hé lộ, kèm **tắt nhạc** ở 5 đoạn (`music_drop`) |

**Bảng đặt âm:** `.work/sfx_tap02.json`:
- 13 đoạn nền theo câu.
- **37 tiếng động** gắn vào câu hoặc mốc SFX của kịch bản, gấp 2,6 lần Tập 01 trên mỗi phút.
- 5 đoạn tắt nhạc.

Đã kiểm: mọi mốc và file đều tồn tại.

**Nghe thử:** `02_SAN_XUAT/Tap02/thu_am/demo_sfx_tap02.mp3` (52 s, không lời) gồm ba cảnh: trạm kiểm soát đêm tuyết · phòng thẩm vấn · đốt quân phục, ép xe, búa tòa.

`demo_sfx_tap02_youtube.mp3` (133 s) — **reel đủ 32 mã**, mỗi mã một đoạn 3 s. `demo_amb_tap02.mp3` (75 s) — 8 file nền, mỗi file 8 s.

### 3.2 Kiểm tra "nghe mù" và giới hạn thật

Cho mô hình nhận dạng âm thanh nghe bản demo mà **không** cho biết nội dung, yêu cầu kể tên từng tiếng và chấm độ chân thật:

| Cảnh | Lần 1 | Lần 2 (sau khi chỉnh 6 tiếng bị nhầm) | Nhận ra đúng | Vẫn nhầm |
|---|---|---|---|---|
| Trạm kiểm soát | 6/10 | 6/10 | gió, không gian ngoài trời | lốp trên tuyết → "xúc sỏi", rồi "tên lửa"; mô-tơ kính xe → "còi hơi" |
| Phòng thẩm vấn | 7/10 | **8/10** | cửa sắt đóng sầm, phòng kín có vang | ghế cào nền → "tiếng rít" (lần 1), "dây xích" (lần 2) |
| Lửa · ép xe · búa tòa | 5/10 | 7/10 | lửa tí tách, kim loại nặng | búa tòa → "chuông" (lần 1); kéo cắt → "kính vỡ" |

**Kết luận thẳng:**
- Lớp nền và độ vang đã tạo được cảm giác "có không gian" — đó là điểm Tập 01 thiếu nhất.
- **Tiếng động tổng hợp bằng code chạm trần ở khoảng 6–8/10.** Các tiếng gắn với vật thật — lốp xe trên tuyết, kính xe, bộ đàm, bước chân, búa — vẫn dễ bị nghe thành thứ khác.
- Muốn "chân thật" như phim tài liệu, cần **tiếng thu thật** cho khoảng 8 tiếng chủ chốt.

### 3.3 Đề xuất nguồn tiếng thu thật (người dùng quyết)

| Nguồn | Chi phí | Dùng cho video kiếm tiền trên YouTube? | Ghi chú |
|---|---|---|---|
| **YouTube Audio Library** (Studio → Thư viện âm thanh → Hiệu ứng âm thanh) | Miễn phí | **Có** — giấy phép dành riêng cho video YouTube | Khuyến nghị: an toàn nhất cho kênh; tải tay, ghi vào `provenance.json` |
| Freesound.org — chỉ lọc giấy phép **CC0** | Miễn phí | Có (CC0 không ràng buộc) | Chất lượng không đều; cần kiểm từng file. Bỏ qua CC-BY-NC |
| BBC Sound Effects | Miễn phí | **Không** — giấy phép phi thương mại | Không dùng |

Nếu đồng ý dùng tiếng thu thật, 8 tiếng đáng thay nhất: lốp xe trên tuyết · kính xe hạ · bộ đàm cảnh sát · bước chân trên tuyết · ghế kim loại kéo · búa tòa · lửa cháy · máy ép kim loại. Phần nền và nhấn kịch tính giữ bản tự tổng hợp. Việc này **đổi quy tắc A4.4 / A6** ("không tải file ngoài") nên cần người dùng đồng ý.

### 3.3.1 ĐÃ LÀM 23/10/2026 — tải tiếng từ YouTube Audio Library (**32/32 mã**)

Quyết định ở §3.5 (22/10: không dùng tiếng thu thập tải ngoài) **đã bị đảo ngược** ngày 23/10/2026. Nguồn thực tế: **YouTube Audio Library** — Studio → Thư viện âm thanh → tab **Hiệu ứng âm thanh** (kênh *Amber Eyes*, `UCloOzyxGK3TGtp6ICJpGRBA`). Tải tay, nhập bằng `.work/import_sfx_video.py` → rãnh tiếng, stereo 44,1 kHz, ghi `provenance.json`.

**Kết quả: 32/32 mã của tập đều là tiếng thật** (8 nền + 24 tiếng động). Trong đó **15 mã khớp đúng vật thể**, **17 mã là bản thay thế gần nghĩa nhất** mà thư viện có.

| Mã | Track trên YouTube | Thể loại | Dài (s) | Mức khớp với cảnh |
|---|---|---|---|---|
| `amb_airbase` | Motor Running Aircraft | Phương tiện giao thông | 478.3 | Khớp — máy bay nổ tại căn cứ không quân |
| `amb_basement` | Metal Machine Hum | Công cụ | 119.8 | **Thay thế** — không có nền tầng hầm; tiếng máy ù |
| `amb_courtroom` | Convention Hall Ambience Noise | Không gian xung quanh | 98.3 | Khớp — tiếng hội trường |
| `amb_fire` | Fire | Không gian xung quanh | 190.4 | Khớp — tiếng lửa |
| `amb_interrogation` | Bowling Alley Room Tone | Thể thao | 127.7 | **Thay thế** — không có nền phòng thẩm vấn; room tone trong nhà (thay bản gió trước đó) |
| `amb_office_night` | Ambient Hum Air Conditioner | Không gian xung quanh | 117.9 | **Thay thế** — không có nền văn phòng ban đêm; tiếng điều hoà |
| `amb_road_night` | Distant Highway | Không gian xung quanh | 222.1 | Khớp — tiếng đường xa |
| `amb_winter_wind` | Wind In Pine Trees | Thời tiết | 214.3 | Khớp — gió qua cây thông |
| `fx_camera_shutter` | Play And Stop On A Camera | Công cụ | 26.9 | **Thay thế** — không có tiếng màn trập rời; tiếng bấm máy ảnh (play/stop) |
| `fx_chair_scrape` | Slide On Metal Grate Series | Tiếng động thực tế | 58.8 | **Thay thế** — không có tiếng kéo ghế; đây là kéo trên lưới kim loại |
| `fx_cup_down` | Cup on Saucer | Tiếng động trong nhà | 48.5 | Khớp — đặt tách lên đĩa |
| `fx_door_metal_slam` | Dumpster Door Slam | Phương tiện giao thông | 28.0 | **Thay thế** — không có tiếng cửa sắt; đóng cánh rác kim loại |
| `fx_drawer_open` | Drawer Open/Close | Tiếng động trong nhà | 26.5 | Khớp — mở/đóng ngăn kéo |
| `fx_fire_whoosh` | Wind Drawn Into Fire | Tiếng động trong nhà | 30.9 | **Thay thế** — không có tiếng quân phục cháy; gió hút vào lửa |
| `fx_flashlight` | Lamp Switch On/Off | Tiếng động trong nhà | 20.4 | **Thay thế** — không có tiếng đèn pin; tiếng công tắc đèn |
| `fx_footsteps_snow` | Walk on Snow Series | Tiếng động thực tế | 24.2 | Khớp — bước trên tuyết |
| `fx_gavel_triple` | Wooden Bead Hitting Series | Tiếng động thực tế | 14.0 | **Thay thế** — không có búa tòa; gõ hạt gỗ, cắt đúng 3 cú đầu |
| `fx_hdd_spin` | Disk Drive Insert and Spinning | Công cụ | 34.6 | Khớp — cắm ổ cứng + quay |
| `fx_heartbeat_slow` | Human Breathing Mouth | Giọng của con người | 12.2 | **Thay thế** — thư viện KHÔNG có tiếng tim; dùng tiếng thở |
| `fx_map_unfold` | Paper Folding | Tiếng động thực tế | 22.8 | **Thay thế** — không có tiếng mở bản đồ; tiếng gấp giấy |
| `fx_metal_crush` | Glass Crush | Va chạm | 3.5 | **Thay thế** — không có tiếng xe bị ép nát; vỡ kính |
| `fx_metal_snip` | Scissor Snips | Văn phòng | 7.2 | Khớp — cắt kéo |
| `fx_paper_folder` | Clipboard | Văn phòng | 25.7 | **Thay thế** — không có tiếng mở túi bìa; tiếng kẹp giấy |
| `fx_pen_scribble` | Pen Writing | Văn phòng | 29.1 | Khớp — viết tay |
| `fx_phone_ring` | Phone Alerts And Rings | Chuông báo | 19.8 | Khớp — chuông điện thoại |
| `fx_photo_slide` | Feeling Paper | Tiếng động thực tế | 19.7 | **Thay thế** — không có tiếng trượt ảnh; tiếng cầm giấy |
| `fx_police_radio` | Radio Static | Tiếng động thực tế | 29.1 | Khớp — nhiễu bộ đàm |
| `fx_stinger` | Sci Fi Vortex | Khoa học viễn tưởng | 37.7 | **Thay thế** — không có tiếng sting; tiếng xoáy sci-fi |
| `fx_sub_drop` | High To Low Sweep | Khoa học viễn tưởng | 36.0 | **Thay thế** — không có tiếng sub-drop; tiếng quét tần số giảm dần |
| `fx_tension_tick` | Setting Alarm Clock | Chuông báo | 19.6 | Khớp — tiếng đồng hồ báo thức (tick) |
| `fx_tire_snow` | Car Drive By | Phương tiện giao thông | 52.8 | Khớp — xe lăn qua; cắt 34–45 s (lần xe gần nhất) |
| `fx_window_down` | Trunk Window Open Hydraulic Hiss | Phương tiện giao thông | 2.4 | **Thay thế** — thư viện không có tiếng hạ kính xe; dùng tiếng hơi thủy lực khi mở cửa |

**Giới hạn thật — đọc trước khi dùng:**
- Thư viện chỉ có **~637 hiệu ứng**. Từ khóa `chair`, `gavel`, `court`, `office`, `basement`, `flashlight`, `heart`, `pulse`, `heartbeat` → **không có kết quả**. Với các mã đó phải dùng bản thay thế (xem cột cuối).
- Bản thay thế **không phải** ghi âm đúng vật thể trong phim — nghe sẽ ra "gần đúng" chứ không trúng. Ai cần đúng thì phải thu ngoài trời hoặc tạo bằng AI (Veo/MiniMax-H3 — xem `HuongDan_TaoSFX_Gemini.md`, hiện là phương án dự phòng chưa chạy).
- `fx_metal_crush` chỉ dài 3,4 s — đủ làm một nhịp rầm khi phát hiện chiếc xe, không có tiếng rẹo dài.
- File tải về là **cả bài 14–478 s**, không phải tiếng đơn. Bắt buộc cắt đúng đoạn, nếu không tiếng sẽ chạy dưới cả chục câu.
- Tiếng nền dài được `build_audio3.py` nối vòng có hoà chồng 1 s; dài hơn bản 40 s cũ nên lặp khó nhận hơn.

**Điều khoản YouTube Audio Library (bắt buộc):**
- Miễn phí dùng trong **video / nội dung do chính kênh sáng tạo** — đây là giấy phép cho video kiếm tiền trên YouTube.
- **KHÔNG** được cung cấp, phân phối hoặc phát hành riêng file âm thanh (không bán / nhận tải pack SFX, không đưa file gốc lên nơi khác ngoài dự án làm video).
- Không dùng cho mục đích phi thương mại hoặc nội dung bất hợp pháp.
- Đã ghi từng mục vào `provenance.json` (`cong_cu`, `dieu_khoan`, `track_youtube`, `the_loai_youtube`, `kiem_tra_thuong_mai`, `rms_dbfs`, `peak_dbfs`).

**Quy trình đã dùng (lặp lại được):**
1. `reload` trang Studio → click tab `tp-yt-paper-tab#sound-effects`.
2. **Tìm theo tên:** gõ từ khóa vào ô chip-bar → Enter → điền ô **Giá trị** → click **Áp dụng** (bộ lọc "Chứa cụm từ …").
   **Tìm theo thể loại:** gõ tên thể loại → chọn mục **Thể loại** trong menu gợi ý → tick ô tương ứng → **Áp dụng**. Danh sách thể loại (20 mục) rất hữu ích: *Văn phòng · Công cụ · Khoa học viễn tưởng · Chuông báo · Tiếng động trong nhà · Tiếng động thực tế · Phương tiện giao thông · Va chạm · Không gian xung quanh · Phim kinh dị…*
3. Click nút **Tải xuống** của dòng cần → `py -3 .work/yt_audio_library/collect.py <mã> --pick-title "<Tên Track>" --title "<Tên Track>" --genre "<Thể loại>" --expect <giây>`.
4. `py -3 .work/import_sfx_video.py --tool "YouTube Audio Library (YouTube Studio)"`.
5. `py -3 .work/yt_audio_library/normalize_crest.py` — bước mastering bắt buộc, xem 3.3.2.

Helper `collect.py` đọc thẻ ID3 để ghi đúng tên track vào `.work/yt_audio_library/manifest.json`. Lưu ý: Chrome **đổi tên file** khi tải — `/` thành `_`, bỏ dấu tiếng Việt (`Drawer Open/Close` → `Drawer Open_Close.mp3`) — nên dùng `--pick-title` (khớp tên) thay vì `--rank` (theo thứ tự thời gian).

#### 3.3.2 Cắt đoạn + mastering (bắt buộc, làm 23/10/2026)

**Cắt đoạn.** File YouTube là cả bài, nên phải cắt đúng đoạn chứa hành động. Cách làm: đo profile năng lượng theo khung 0,25 s (`.work/yt_audio_library/profile_sfx.py`), rồi chọn cửa sổ quanh điểm đỉnh — **21/32 mã được cắt**, kết quả nằm trong `CUTS` của `.work/import_sfx_video.py` (ví dụ `fx_door_metal_slam` lấy 8,6–11,0 s = đúng một cú đóng sầm, thay vì 6 cú lặp đều như máy).

**Mastering — vì sao cần.** `build_audio3.py` chuẩn hoá mọi file về RMS của lời rồi mới áp dB trong bảng (`x * (v_rms / rms(x)) * db(rel)`), nên **mức tuyệt đối của file không quan trọng** — nhưng **độ chênh peak/RMS (crest factor) thì có**. File tải về nhiều tiếng đơn lẻ (tiếng giấy, tiếng tick) có crest 30–43 dB; chuẩn hoá về RMS lời sẽ đẩy đỉnh vượt 0 dBFS và làm clip cả bản trộn.

`.work/yt_audio_library/normalize_crest.py` dùng limiter để ép crest xuống ≤ 20 dB rồi chuẩn hoá đỉnh về −1 dBFS. Sau khi chạy: **toàn bộ 32 file có crest ≤ 21,5 dB, đỉnh −1 dBFS** — trộn vào bất kỳ lớp nào cũng không clip.

### 3.4 Sửa code — ĐÃ LÀM 22/10

| Script | Sửa |
|---|---|
| `build_audio3.py` | (1) Trộn **stereo** (hiện trộn mono rồi nhân đôi kênh) · (2) đọc `sfx_tap02.json`: nền theo đoạn câu (mờ vào/ra 1,5 s, hạ thêm 4 dB dưới lời), tiếng động theo mốc, `music_drop` · (3) tiếng động rơi vào khoảng nghỉ: nếu đè lên lời quá 0,3 s thì dời vào khoảng nghỉ gần nhất |
| `TIEU_CHUAN_DUNG_VIDEO.md` A4 | Thêm lớp nền môi trường và lớp nhấn kịch tính vào tiêu chuẩn kênh, để Tập 03 trở đi dùng luôn |

---

## 3.5 Quyết định của người dùng (22/10/2026)

- **Không dùng tiếng thu thật tải ngoài** (quyết định 22/10 — đã đảo ngược 23/10, xem 3.5.1) → tạo bằng AI video. Người dùng chọn **tự tạo bằng Gemini (Veo)**: hướng dẫn và 12 prompt ở `HuongDan_TaoSFX_Gemini.md`; đặt video vào `sfx_gemini/` rồi chạy `.work/import_sfx_video.py` (lấy tiếng, thay vào `assets/sfx/t2/`, bản tự tổng hợp giữ ở `_code/`, ghi `provenance.json`). Phương án MiniMax-H3 (`.work/make_sfx_h3.py`) để dự phòng, **chưa chạy** vì có chi phí. Nền ngắn 8 s được `build_audio3.py` nối vòng có hoà chồng 1 s.
- **Chấp nhận giọng khác Tập 01** → buổi thử mở rộng: mỗi vai 2–3 giọng ứng viên (34 bản đọc), chọn theo độ biểu cảm + CER.
- **Cho phép sửa file .py** → đã sửa `edition.py` (bảng `EPISODES`, `AE_EP`), `tts_sentences.py` (diễn xuất cho bản VN), `build_audio3.py` (`_pause_after`, bảng âm thanh stereo, tắt nhạc), `parse_shots.py`, `build_video3.py`, `package.py`.

**Chạy thử khô Tập 02** (giọng giả cùng độ dài, đã xoá sau khi thử): bản trộn stereo · 0 khoảng câm > 0,3 s · −16,0 LUFS · 13 đoạn nền + 37 tiếng động đặt đúng · **83% thời lượng có lớp nền/tiếng động** (trung vị −34 dB so với lời; Tập 01 ≈ 0%). Thời lượng ước mới ≈ **29 phút** — đọc chậm hơn và nghỉ thêm làm tập dài ra ~3 phút so với ước tính cũ.

### 3.5.1 Đảo ngược quyết định 23/10/2026 — dùng tiếng tải từ YouTube Audio Library

Quyết định đầu mục 3.5 (22/10: không dùng tiếng thu thập tải ngoài) **đã bị đảo ngược** ngày 23/10/2026.

- Người dùng yêu cầu: đọc tài liệu sinh SFX rồi **lên YouTube Studio tải SFX về**.
- Đã tải **32/32 mã** của tập từ YouTube Audio Library (bảng track + giới hạn thật ở **3.3.1**), nhập vào `assets/sfx/t2/`; **bản tự tổng hợp cũ giữ ở `assets/sfx/t2/_code/`** (chép ngược lại để quay về).
- `provenance.json` của cả 32 file này đã sửa lại cho đúng thực tế: `cong_cu` ghi rõ tải tay từ YouTube Studio, `dieu_khoan` ghi điều khoản YouTube Audio Library, `kiem_tra_thuong_mai` ghi đạt có điều kiện, cộng thêm `track_youtube` + `the_loai_youtube` + `nguon_goc`.
- `HuongDan_TaoSFX_Gemini.md` (12 prompt Veo) **chỉ còn là phương án dự phòng, chưa chạy** — dùng lại được nếu sau này cần tiếng mà thư viện không có.
- ~~Chưa dựng lại audio Tập 02~~ → **đã dựng lại 23/10** với tiếng mới (32/32 mã — 3.3.1). Demo nghe thử đã dựng lại: `demo_sfx_tap02.mp3` (3 cảnh), `demo_sfx_tap02_youtube.mp3` (reel 32 mã), `demo_amb_tap02.mp3` (8 nền).

## 4. Việc tiếp theo (cập nhật 23/10/2026)

1. ~~Thử diễn xuất~~ ✅ 3 vòng (§2.4) · ~~chọn giọng~~ ✅ bộ A (`BaoCao_GiongDoc_Tap02.md`).
2. ~~Nhập tiếng thật, dựng lại âm thanh~~ ✅.
3. ~~Sửa code~~ ✅ · ~~đọc toàn tập~~ ✅ · ~~sửa đọc số~~ ✅ (G11).
4. **Còn lại:** (a) người dùng nghe 3 file demo ở `thu_am/`; (b) **17 mã đang là bản thay thế** (búa tòa · ghế · đèn pin · giấy · ảnh · bản đồ · tim · tầng hầm · văn phòng · kính xe) — nếu cần đúng vật thể thì phải thu ngoài trời hoặc tạo bằng AI, thư viện không có; (c) **dựng lại audio Tập 02**: thiếu `tts_manifest_t02.json` / `audio_s_t02/` (cần tạo giọng cho 216 câu — có chi phí) **và cần người dùng chốt giọng A/B/C** ở `BaoCao_GiongDoc_Tap02.md` §4–5 trước khi chạy `build_audio3.py`.
