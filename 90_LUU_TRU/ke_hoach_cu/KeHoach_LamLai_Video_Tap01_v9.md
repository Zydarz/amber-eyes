# KẾ HOẠCH LÀM LẠI VIDEO TẬP 01 — "ĐỘC DƯỢC NHÂN DANH TÌNH MẸ"

**Phiên bản 9** · Cập nhật 22/10/2026 · *v8: intro kênh, lời miễn trừ, nhận diện kênh, hồ sơ pháp lý · v9: kịch bản giảm bạo lực (V9, Phụ lục B) + sửa 12 lỗi sau lần rà soát ngày 22/10*
**Kịch bản nguồn:** `kichban_tap01_22102026_v2.md` — bản **giảm bạo lực** (23 chỗ sửa, giữ nguyên 128 câu), lập từ `kichban_tap01_22102026.md` (4 vai: Host · Điều tra viên · Chuyên gia tâm lý · Người bình thường). Danh sách sửa ở Phụ lục B.
**Tạo hình & bố cục:** `PhuongAn_TaoHinh_5NhanVat.md` — đã chốt **Graphic Novel Noir + 5 linh thú dẫn chuyện + nền vụ án toàn màn hình, nhân vật dạng nhỏ ở góc**
**Thay cho:** mọi bản trước (v5–v8) — chỉ dùng bản này
**Đầu vào duy nhất từ người dùng:** file kịch bản. Mọi bước còn lại do AI thực hiện và tự kiểm tra.

---

## MỐC 0 — ĐỌC TRƯỚC TIÊN

### Chín quy tắc vàng

| # | Quy tắc | Vì sao |
|---|---|---|
| **V1** | **Đơn vị đồng bộ là CÂU.** TTS đọc từng câu thành một file riêng. | Bản cũ chia block theo tỉ lệ → hình lệch lời tới 16 giây |
| **V2** | **Hình chỉ đổi ở đầu câu.** Cấm chia shot theo tỉ lệ thời gian. | Lỗi "vào nội dung rồi hình mới xuất hiện" |
| **V3** | **Chữ trên hình lấy từ chính câu đang đọc.** Không thêm dữ kiện, con số, câu trích. | Bản cũ tự bịa "19 tuổi", tự đặt câu trích |
| **V4** | **Không có im lặng tuyệt đối quá 0,3 giây.** Chỗ "im lặng" giữ nền trầm −40 dB. | Bản cũ câm 6 giây ở 0:26 |
| **V5** | **Người thật trong vụ án** (Dee Dee, Gypsy, Godejohn) **chỉ hiện dưới dạng bóng**, không nét mặt. **Tiến sĩ Flasterstein và ông Dan Patterson không được vẽ** — chỉ hiện tên trên giấy tờ, bảng tên. | Vụ án có thật; nạn nhân từng bị khai là trẻ vị thành niên; hai người kia là người thật còn sống |
| **V6** | **Năm linh thú là nhân vật minh hoạ**, có nhãn *"Nhân vật minh hoạ · giọng đọc AI"* ở lần xuất hiện đầu. | Kịch bản giới thiệu "Điều tra viên trực tiếp thụ lý" — không để người xem hiểu là phỏng vấn thật |
| **V7** | **Nền vụ án luôn chiếm toàn màn hình. Linh thú không bao giờ chiếm quá 20% khung.** | Bố cục đã chốt ở `PhuongAn_TaoHinh_5NhanVat.md` mục 5.2 |
| **V8** | **Mọi tập mở đầu bằng intro kênh 22,4 s** (nhạc `bgm_music_box`, nhận diện kênh, 2 thẻ miễn trừ). **Mọi tài sản trong video phải có nguồn gốc ghi trong `provenance.json`.** | Yêu cầu người dùng 22/10; giảm rủi ro khiếu nại bản quyền và nội dung |
| **V9** | **Trọng tâm là phân tích tâm lý.** Lời và hình **không mô tả chi tiết** bạo lực, thương tích, thi thể hay cách gây hại. Hành vi gây hại chỉ nêu ở mức khái quát ("hình phạt nghiêm khắc", "can thiệp y khoa không cần thiết"); không có màu đỏ máu, vết thương, vũ khí trên hình | Mục tiêu nội dung của kênh; giảm rủi ro quảng cáo hạn chế |

### Hai tầng nhân vật — tách bạch tuyệt đối

| | **Tầng dẫn chuyện** | **Tầng vụ án** |
|---|---|---|
| Ai | 5 linh thú: Cú (Host) · Sói (Điều tra viên) · Cáo (Chuyên gia) · Cừu (N1 Hàng xóm) · Mèo (N2 Khán giả) | Dee Dee · Gypsy Rose · Godejohn · đám đông |
| Hình dạng | **Linh thú** mặc trang phục noir, có mắt, kính, biểu cảm | **Người**, dạng **bóng** một màu, không nét mặt |
| Vị trí | Chỉ ở **góc màn hình** (bán thân nhỏ, thẻ badge) | Nằm **trong** khung cảnh vụ án |
| Màu | Mỗi vai một màu viền sáng riêng (mục 5.2) | Chỉ màu vụ án: `pink`, `pink_deep`, đen |

Hai tầng khác nhau cả về **loài** (thú / người), **vị trí** (góc / trong cảnh) và **màu** → người xem không bao giờ nhầm người kể với người trong vụ án.

### Trạng thái file

| File | Dùng lại? |
|---|---|
| `assets/bgm/*.mp3` (9 file nhạc) | **Có** |
| `.work/parse_kichban.py` | **Có** — đã chạy thử, ra 33 lượt / 128 câu (Phụ lục A) |
| `kichban_tap01_22102026_v2.md` + `.work/script_v2.json` | **Nguồn chính** của bản dựng này |
| `kichban_tap01_22102026.md` (bản gốc) | Giữ nguyên, chỉ để đối chiếu |
| `.work/scenes.py`, `shotlib.py`, `layouts.py` | **Có một phần** — chỉ giữ phần vẽ sơ đồ, chữ, thẻ; cảnh nền chuyển sang ảnh AI (mục 5.6) |
| `.work/build_audio.py`, `build_video2.py` | **Có**, sửa theo mục 3 và mục 7 |
| `assets/cast/host_owl_mascot.jpg` | **Tham khảo** — đúng hướng Cú nhưng có watermark `pollinations.ai`, nét 3D chưa ra chất mực truyện tranh → **tạo lại** |
| `assets/cast/host_concept.jpg`, `detective_concept.jpg`, `psychologist_concept.jpg` | **Không dùng** — nhân vật người (hướng đã bỏ). Giữ làm tham chiếu **ánh sáng, bối cảnh, độ chi tiết nét mực** |
| `assets/cast/neighbor_concept.jpg`, `host_mysterious_cartoon.jpg`, `host_stylized_dark_cartoon.jpg` | **Không dùng** — người, lệch phong cách, có watermark |
| `.work/audio/*.mp3` (kịch bản cũ), `.work/build_shots.py`, `KeHoach_ThuAm_Tap01.md` | **Không** |

---

## 1. TỔNG QUAN KỊCH BẢN (đo ngày 22/10/2026)

| Chỉ số | Giá trị |
|---|---|
| Lượt nói | 33 (Host 21 · Chuyên gia 6 · Điều tra viên 4 · Người dân 2) |
| Câu | **128** |
| Số từ | 3.545 (bản v2; bản gốc 3.565) — Host 50% · Chuyên gia 24% · Điều tra viên 20% · Người dân 5% |
| Khoảng nghỉ trong kịch bản | 13 chỗ, tổng 24,5 s |
| **Thời lượng dự kiến** | **≈ 20,5 phút** = intro 22,4 s + ≈ 20 phút nội dung (ước lượng theo 3,17 từ/s đo ở bản cũ). Kịch bản ghi 25–27 phút là cao hơn thực tế; muốn đủ 25 phút cần thêm ~1.000 từ |

**Hai "Người bình thường" là hai nhân vật khác nhau:** `1.07` là **N1 · Hàng xóm (Cừu)**, `4.03` là **N2 · Khán giả (Mèo)**. Khác hình, khác giọng.

---

## 2. QUY TRÌNH TỔNG THỂ

```
NGƯỜI DÙNG: kichban_tapXX.md
   │
B0 CHUẨN BỊ (một lần cho cả series)
   ├─ B0a thử giọng 5 nhân vật → cast.json (mục 3.2)
   ├─ B0b tạo 5 linh thú × 3 ảnh → tách nền → assets/cast/<vai>/ (mục 5.4)
   ├─ B0c tạo 6 bóng người vụ án → tách nền → assets/sil/ (mục 5.5)
   └─ B0d bộ nhận diện kênh + intro_kenh.mov 22,41 s, chỉ hình (mục 5.11) — render 1 lần, dùng mọi tập
   │
B1 parse_kichban.py     kịch bản → script.json                          ĐÃ CÓ
B2 make_tts_args.py     → 13 batch ≤ 10 câu → .work/audio_s/<id>.mp3     SỬA
B3 build_audio.py       → Tap01_master.mp3 · timeline_s.json · stems/   SỬA
B4 make_backgrounds.py  tạo các nền 16:9 còn thiếu cho tập (mục 5.6)    MỚI
B5 shots.json           AI chuyển bảng mục 6 thành JSON                 MỚI
   └─ validate_shots.py kiểm tra phủ câu, vai, nội dung chữ
B6 render_layers.py     Pillow vẽ chữ, sơ đồ, thẻ, badge                MỚI
B7 build_video3.py      ghép nền + bóng + đồ hoạ + lớp nhân vật         SỬA
B8 subtitles.py         → Tap01.srt (có tên vai)                        MỚI
B9 qc.py                tự kiểm tra, sai là dừng                        MỚI
B10 package.py          thumbnail + mô tả YouTube                       MỚI
```

| Mốc | Phạm vi | Qua mốc khi |
|---|---|---|
| **M0** | B0: giọng + 5 linh thú + bóng người + **logo kênh** | Ảnh đạt checklist 5.4 / 5.5 / 5.11; 5 giọng phân biệt rõ |
| **M0.5** | **Prototype 40 s** = intro kênh 22,4 s + 15 s đầu Hồi 1 (nền nhà hồng + Cú góc trái + sóng âm amber + giọng thật) | Người dùng duyệt thẩm mỹ **và nội dung 2 thẻ miễn trừ** |
| **M1** | B1–B3: audio | `qc.py --audio` đạt |
| **M2** | B4–B9 cho **Hồi 1** (~4 phút, có đủ 4 vai) | `qc.py` đạt; người dùng xem thử (tuỳ chọn) |
| **M3** | Toàn tập + B10 | `qc.py` đạt toàn bộ |

---

## 3. ÂM THANH

### 3.1 Tách kịch bản (B1 — đã chạy thử)

| Dòng trong kịch bản | Xử lý |
|---|---|
| `## HỒI N` | Bắt đầu hồi N, đếm mã từ `N.01` |
| `**HOST** *(chỉ dẫn)*:` và 3 vai còn lại | Bắt đầu lượt nói; chỉ dẫn **không đọc** |
| `**[SFX]:**` · `**[BGM]:**` | Phần tử cue |
| `**[Nghỉ X giây – …]**` | Phần tử `NGHI` X giây |
| `*   ` · `1.  ` | Bỏ ký hiệu, **mỗi dòng là một câu mới** |
| `**…**` · `*…*` | Bỏ ký hiệu, giữ chữ |
| `'…'` | Hiển thị `“…”`; **bỏ dấu khi gửi TTS** |

Cue nằm giữa lượt nói cắt lượt thành 2 phần tử cùng vai (ví dụ `1.03` và `1.05`). Câu cắt tại `. ? ! …` (kể cả khi sau đó là `”`) nếu theo sau là chữ hoa.

### 3.2 Năm giọng

| Nhân vật | `voice_id` (ứng viên) | Trạng thái | `speed` |
|---|---|---|---:|
| **Cú · Host** | `audiobook_male_1` | ✅ đã dùng | 0,90 |
| **Sói · Điều tra viên** | `male-qn-qingse` | ✅ đã từng chạy | 0,95 |
| **Cáo · Chuyên gia** (nữ) | `audiobook_female_1` | ✅ đã dùng, đọc trôi | 0,92 |
| **Cừu · N1 Hàng xóm** | `Vietnamese_kindhearted_girl` | ✅ đã thử | 0,95 |
| **Mèo · N2 Khán giả** | `English_captivating_female1` | ✅ đã thử, đọc trôi nhất | 0,95 |

**B0a:** đọc thử một câu của mỗi nhân vật → `so_sanh_5_giong.mp3` + bảng F0, tốc độ âm tiết. Loại giọng < 1,1 âm tiết/s. Hai giọng cùng giới tính phải chênh F0 ≥ 15 Hz hoặc khác nhóm voice. Kết quả ghi `cast.json`.

### 3.3 Chỉ dẫn diễn xuất → tham số TTS

`emotion` chỉ nhận: `happy · sad · angry · fearful · disgusted · surprised · neutral`.

| Chỉ dẫn | `emotion` | `speed` |
|---|---|---:|
| "chậm, trầm, giữ khoảng cách khách quan" | `neutral` | −0,02 |
| "xúc động, chân thật như đang trả lời phỏng vấn" | `sad` | 0 |
| "Đẩy nhanh nhịp độ hơn một chút" | `neutral` | +0,04 |
| "hạ trầm, sắc lạnh và dứt khoát" · "đanh thép" | `neutral` | +0,02 |
| "trầm lắng" · "trăn trở" | `sad` | −0,02 |
| "phân tích chuyên môn" · "nhấn mạnh từng ý" · "tiếp lời" · "thuật lại hồ sơ" · "điềm đạm" · "băn khoăn" | `neutral` | 0 |
| "Hạ giọng trầm, chậm rãi hơn" | `neutral` | −0,04 |
| "trầm ấm, truyền cảm" | `neutral` | −0,02 |

Lượt không có chỉ dẫn kế thừa chỉ dẫn của lượt trước cùng vai trong cùng hồi.

### 3.4 Khoảng ngắt

| Vị trí | Độ dài |
|---|---:|
| Giữa 2 câu cùng lượt | 0,35 s |
| Sau câu kết thúc bằng `?` | 0,60 s |
| Đổi người nói (kịch bản không có nghỉ) | 0,70 s |
| `[Nghỉ X giây]` | X giây, tối đa 2,5 s |
| Ranh giới hồi (thêm mới) | 2,0 s |

### 3.5 Nhạc, SFX, nền trầm

- **Intro kênh (0,00–22,41 s):** `bgm_music_box.mp3` phát **trọn bài, không cắt, không lặp**. Không lời đọc trong intro.
  - Music box được **đặt thẳng vào audio master ở t = 0** trong `build_audio.py` (không ghép file intro có sẵn tiếng), để đoạn đuôi intro trộn được với âm thanh riêng của từng tập (drone, còi).
  - Mức: nhạc intro thấp hơn lời 4 dB (trong master, trước `loudnorm`). Dùng `loudnorm` **2 lượt, chế độ tuyến tính** (`linear=true`) để tỉ lệ intro / lời không bị nén lại.
- **Nối sang Hồi 1** — intro và `1.01` dùng chung music box nên **không phát lại** music box ở `1.01`:
  - 19,5 s: drone `bgm_sub_drone` vào từ −40 dB, dâng dần ("bóp nghẹt" music box đúng như kịch bản `1.01`);
  - 20,5 s: còi cảnh sát xa + gõ cửa (`1.02`, bỏ qua nếu chưa có file);
  - 22,4 s: music box tắt hẳn, drone còn ở −26 dB;
  - **Lời đầu tiên của Host ≈ 23,0 s.**
- `1.09` "im lặng tuyệt đối": tắt nhạc có giai điệu, **giữ drone −40 dB**.
- `1.12`: "Tách" + cello vào **dưới** lời chào Host.
- `bgm_ambient_deep.mp3` lặp suốt tập ở −40 dB.
- Tiếng "Tách" máy ghi âm (`1.06`, `1.12`, `5.13`) tạo bằng ffmpeg — ký hiệu âm thanh của Host. SFX khác chưa có file: bỏ qua im lặng.
- Mix: lời 0 dB · nhạc −26 / −14 dB · SFX −22 dB · loudnorm `I=-16:TP=-1.5:LRA=11`.

### 3.6 Đầu ra B3

- `timeline_s.json`: mỗi câu có `id`, `role`, `turn`, `start`, `end`, `text` (đo bằng ffprobe từng file câu).
- `stems/{H,D,C,N1,N2}.wav`: mỗi nhân vật một file cùng độ dài master, chỗ người khác nói là im lặng → vẽ sóng âm.

---

## 4. HỢP ĐỒNG DỮ LIỆU

### 4.1 `cast.json`

```json
{
 "H":  {"animal":"Cú mèo",  "name":"HOST", "title":"Người dẫn chuyện",
        "voice":"audiobook_male_1", "color":"amber", "art":"assets/cast/H/"},
 "D":  {"animal":"Sói xám", "name":"ĐIỀU TRA VIÊN", "title":"Hồ sơ vụ án Blanchard",
        "voice":"male-qn-qingse", "color":"cold", "art":"assets/cast/D/"},
 "C":  {"animal":"Cáo",     "name":"CHUYÊN GIA TÂM LÝ", "title":"Tâm lý học tội phạm",
        "voice":"audiobook_female_1", "color":"violet", "art":"assets/cast/C/"},
 "N1": {"animal":"Cừu non", "name":"NGƯỜI DÂN SPRINGFIELD", "title":"Hàng xóm nhiều năm",
        "voice":"Vietnamese_kindhearted_girl", "color":"sand", "art":"assets/cast/N1/"},
 "N2": {"animal":"Mèo con", "name":"KHÁN GIẢ", "title":"Theo dõi vụ án",
        "voice":"English_captivating_female1", "color":"cyan", "art":"assets/cast/N2/"}
}
```

### 4.2 `shots.json` — **chỉ mô tả tầng câu chuyện**

```json
{
 "id": "1-17",
 "from": "1.11#3", "to": "1.11#4",
 "bg": "interrogation",
 "sil": [{"id": "gypsy_stand", "x": 1180, "y": 260, "h": 640}],
 "template": "T1",
 "text": {"label": "", "headline": "CÔ TA TỰ BƯỚC ĐI"},
 "beats": [{"layer": "lamp_on", "at": "1.11#4"}],
 "camera": {"type": "push", "z0": 1.00, "z1": 1.05},
 "in": "dissolve",
 "cast": {"handoff": null, "bust": "auto"}
}
```

**Lớp nhân vật (badge, bán thân, sóng âm) không ghi tay** — `build_video3.py` tự đặt theo `role` trong `timeline_s.json` (mục 5.7). Shot chỉ ghi ngoại lệ: `handoff` (Host mời ai) và `bust: "off"` (tắt bán thân khi cần trống góc).

### 4.3 Quy tắc thời gian

| Thứ | Thời điểm |
|---|---|
| Shot mới | `start` câu `from` − 0,20 s |
| Beat có `phrase` | vị trí ký tự trong câu × thời lượng câu − 0,15 s (chỉ trong một câu) |
| Badge vào / ra | `start` câu đầu lượt − 0,30 s / `end` câu cuối lượt + 0,20 s |
| Bán thân vào / ra | như mục 5.7 |

---

## 5. HỆ THỐNG ĐỒ HOẠ

### 5.1 Định hướng — Graphic Novel Noir

Truyện tranh điện ảnh tối: nét mực đậm ở viền ngoài, mảnh bên trong; đổ bóng tương phản cao (chiaroscuro); **viền sáng (rim light) mang màu vai**; hạt phim, sương mờ. Tham chiếu: *Blacksad*, *The Wolf Among Us*, *Batman: The Animated Series*, *Disco Elysium*.

**Bố cục chốt:**
```
┌──────────────────────────────── 1920 × 1080 ────────────────────────────────┐
│ ┌─────────────────┐                                                        │
│ │ ◉ SÓI · ĐIỀU TRA │  ← Badge hồ sơ (luôn có khi nhân vật đó nói)          │
│ │   VIÊN  ∿∿∿∿∿∿   │                                                        │
│ └─────────────────┘                                                        │
│                                                                             │
│        NỀN VỤ ÁN TOÀN MÀN HÌNH (ảnh AI 16:9 + bóng người + đồ hoạ)          │
│        camera đẩy / trượt chậm · sương · hạt phim                           │
│                                                                             │
│ ┌──────────┐                                                                │
│ │  BÁN     │        TIÊU ĐỀ / LUẬN ĐIỂM CHÍNH                               │
│ │  THÂN    │        dòng phụ                                                │
│ │  LINH THÚ│                                                                │
└─┴──────────┴────────────────────────────────────────────────────────────────┘
   ↑ chỉ hiện ở câu đầu mỗi lượt và câu chốt, chìm dần vào bóng ở đáy
```

### 5.2 Bảng màu

| Token | Hex | Dùng cho |
|---|---|---|
| `ink` | `#0E0E11` | Nền chính |
| `night` | `#151A2A` | Trời đêm |
| `slate` | `#1C1F2B` | Nền badge (85%) |
| `paper` / `paper_ink` | `#E6DED0` / `#1C1B1F` | Giấy hồ sơ / chữ trên giấy |
| `text` / `muted` | `#F2EFE9` / `#9C988F` | Chữ chính / phụ |
| `pink` / `pink_deep` | `#E8A0BF` / `#A85273` | **Độc quyền vụ án**: nhà 2103, xe lăn, bóng Dee Dee |
| `red` | `#C8423A` | Gạch bỏ, cờ đỏ, nguy hiểm |
| **`amber`** | `#E2B467` | **Cú · Host** |
| **`cold`** | `#86A9CC` | **Sói · Điều tra viên** |
| **`violet`** | `#A99BD6` | **Cáo · Chuyên gia** |
| **`sand`** | `#D9B99B` | **Cừu · N1 Hàng xóm** |
| **`cyan`** | `#6E8CA0` | **Mèo · N2 Khán giả** |

**Luật màu vai:** đường gạch chân, viền khung thẻ, vạch nhấn và sóng âm đổi sang màu của **người đang nói**. `pink` không bao giờ dùng cho nhân vật dẫn chuyện.

**Tông theo hồi** (nền vụ án): Hồi 1 đêm xanh + hồng + chớp đèn cảnh sát · Hồi 2 xám lạnh bệnh viện · Hồi 3 tím đen · Hồi 4 tối nhất, xanh lạnh · Hồi 5 hổ phách tòa án → bình minh.

### 5.3 Chữ

Font có sẵn trên máy, đã kiểm chứng tiếng Việt.

| Vai trò | Font | Cỡ |
|---|---|---:|
| Tiêu đề | Segoe UI Bold `segoeuib.ttf` | 60–72 px |
| Nhãn, tên vai | Segoe UI Semibold `seguisb.ttf` | 24–28 px, hoa, giãn +8% |
| Dòng phụ | Segoe UI `segoeui.ttf` | 30–34 px |
| Trích dẫn, lời kể | Georgia Italic `georgiai.ttf` | 52–64 px |
| Tiêu đề chương | Georgia `georgia.ttf` | 72 px |
| Hồ sơ, dữ liệu (Sói) | Consolas `consola.ttf` | 24–30 px |
| Con số lớn | Bahnschrift `bahnschrift.ttf` | 220–300 px |

> **Sửa khi dựng (22/10):** đo bằng script, **Georgia thiếu 92 ký tự tiếng Việt** (ơ, ư, ả, ạ, ề, ể, ố…) → mọi chữ tiếng Việt dùng **Cambria** (`cambria.ttc`, `cambriai.ttf`, `cambriab.ttf`) thay Georgia. Georgia chỉ còn dùng cho chữ "AMBER EYES" của logo. Bahnschrift thiếu "ỷ" và dấu trừ "−" → chỉ dùng cho chữ số, dấu trừ viết bằng "-".

**Mọi chữ trên hình do Pillow vẽ, không để AI vẽ chữ** (ảnh AI hay ra chữ sai, ví dụ các concept cũ có chữ "THE CONSPIRACY", "DR. ELEANOR VANCE").

Luật chung: chữ ≥ 24 px; ≤ 3 khối chữ / khung; ≤ 25 từ; không đè chủ thể; không đè vùng bán thân (mục 5.7).

### 5.4 Năm linh thú dẫn chuyện

#### Bộ mã nhận diện

| | **CÚ MÈO · HOST** | **SÓI XÁM · ĐIỀU TRA VIÊN** | **CÁO · CHUYÊN GIA** | **CỪU NON · N1 HÀNG XÓM** | **MÈO CON · N2 KHÁN GIẢ** |
|---|---|---|---|---|---|
| Hình khối nhận ra ở 64 px | Đầu tròn, 2 túm lông tai, **kính tròn phát sáng** | Vai rộng, **mũ fedora nghiêng**, mõm dài | Tai nhọn cao, **kính mắt mèo phát sáng** | Đầu tròn bông xù, **tai rủ** | **Mũ hoodie trùm** có 2 tai nhọn nhô lên |
| Trang phục | Áo len cổ lọ than chì | Măng-tô navy cổ dựng | Blazer kem | Khăn len dày quấn cổ | Hoodie xám sẫm |
| Đạo cụ | Micro tay đòn | Bìa hồ sơ, huy hiệu bạc **không chữ** | Bút máy, sổ tay da | Hai tay ôm khăn | Cằm tì lên tay, ánh màn hình |
| Viền sáng | `amber` | `cold` | `violet` | `sand` | `cyan` từ dưới lên |
| Biểu cảm | Điềm tĩnh, trung lập | Lạnh, kiên định | Điềm đạm, sắc sảo | Xúc động, xót xa | Băn khoăn, mắt mở to |
| Giới tính giọng | Nam | Nam | Nữ | Nữ | Nữ |

#### Bộ ảnh mỗi linh thú (15 ảnh cho cả series)

| Mã | Khung | Dùng ở |
|---|---|---|
| `P1` | Bán thân 1:1, nghiêng ¾, tư thế trung tính | Bán thân góc màn hình (mặc định) |
| `P2` | Bán thân 1:1, tư thế nhấn mạnh (nghiêng đầu / giơ đạo cụ) | Câu chốt; xen kẽ với P1 ở đầu câu |
| `P0` | Cận đầu, cắt tròn 256 px | Badge, thẻ khách mời, thumbnail |

#### Cách tạo

| Tầng | Công cụ | Ghi chú |
|---|---|---|
| 1 | Connector tạo ảnh của phiên (nếu có `text_to_image`) | Kiểm tra ở B0 |
| 2 | Pollinations API (concept cũ đã dùng) hoặc FastSD CPU (chạy trên máy) | **Ảnh không được có watermark.** Tạo lại bằng tuỳ chọn không watermark nếu dịch vụ cho phép; **không tự xoá watermark**. Kiểm tra điều khoản dùng thương mại trước khi đăng |
| 3 | Pillow — vẽ khối vector theo bảng trên | Luôn chạy được, thô hơn |

**Prompt master** (từ `PhuongAn_TaoHinh_5NhanVat.md` mục 6.1, giữ nguyên):
```
Iconic cartoon mascot bust portrait, anthropomorphic animal in vintage noir detective attire,
chest-up view, dark graphic novel noir animation aesthetic, bold black ink linework,
high contrast chiaroscuro, sharp colored glowing accents, isolated on pure solid black void
background, clean silhouette edges for video overlay compositing, masterwork channel mascot
```
Thêm cho mọi nhân vật: `no text, no letters, no logo, no watermark`.
Phần riêng của từng linh thú: dùng nguyên mục 6.1 của tài liệu tạo hình, **bỏ chữ `EVIDENCE` và `police shield`** khỏi prompt Sói (thay bằng `plain unmarked folder`, `plain silver badge without insignia`).

**Giữ đồng nhất cả bộ:** cùng prompt master, cùng seed gốc cho 5 nhân vật; P2 dùng seed P1 + cụm `head tilted, gesturing with [đạo cụ]`.

**Tách nền:** ảnh trên nền đen tuyệt đối →
1. `rembg` (miễn phí, chạy trên máy) → PNG trong suốt;
2. nếu viền lỗi: khoá độ sáng (pixel < 6% → trong suốt, mép làm mềm 3 px);
3. đáy ảnh mờ dần 25% dưới cùng để "chìm vào bóng tối" khi đặt ở góc.

**`P0` không tạo riêng** — cắt từ `P1` (vùng đầu, tròn 256 px) để biểu tượng chắc chắn giống bán thân. Chỉ cần tạo P1 và P2 → **10 ảnh AI** cho cả series.

**Hậu kỳ (Pillow):** kéo về bảng màu 5.2 · tăng viền sáng màu vai · hạt phim nhẹ.

**Checklist chấp nhận (AI tự xem từng ảnh):**
- [ ] Nhận ra loài và vai **chỉ bằng bóng dáng** khi thu về 64 px
- [ ] Đúng màu viền sáng của vai; không có màu `pink`
- [ ] Không chữ, không logo, không watermark, không phù hiệu thật
- [ ] P1, P2, P0 trông là cùng một nhân vật
- [ ] Năm linh thú cùng một phong cách nét mực (đặt cạnh nhau không lạc tông)
- [ ] Biểu cảm nghiêm túc — **không dễ thương kiểu hoạt hình thiếu nhi** (bài toán số 1 của tài liệu tạo hình)

Không đạt → tạo lại với seed khác, tối đa 6 lần; vẫn không đạt → xuống tầng tiếp theo.

### 5.5 Bóng người trong vụ án

Tạo theo `PhuongAn_TaoHinh_5NhanVat.md` mục 6.3, trên nền đen, rồi tách nền giống mục 5.4. Dùng lại cho nhiều cảnh.

| Mã | Ai | Prompt nguồn | Ghi chú |
|---|---|---|---|
| `deedee_wheelchair` | Dee Dee đứng nắm tay xe lăn | 6.3 #1 | |
| `gypsy_wheelchair` | Gypsy trên xe lăn, mũ len | 6.3 #2 | Bỏ cụm `child's princess dress` → `oversized dress` (không gợi thương hiệu) |
| `gypsy_stand` | Gypsy đứng, nhìn từ sau lưng | biến thể 6.3 #2 | Phòng thẩm vấn, cửa |
| `gypsy_walk` | Gypsy bước đi tự do | biến thể 6.3 #2 | Lời kết |
| `godejohn_screen` | Godejohn trong ánh điện thoại | 6.3 #3 | |
| `crowd` | 5–8 bóng hàng xóm đứng xa | mới | |

**Luật V5 khi duyệt ảnh:** mặt hoàn toàn trong bóng; không thấy răng, mắt, nét mặt. Mục 4 của tài liệu tạo hình (mô tả nụ cười, ánh mắt, hàm răng của Dee Dee và Gypsy; khuôn mặt Flasterstein, Patterson) **chỉ dùng làm định hướng tâm lý, không vẽ ra**.

### 5.6 Thư viện nền 16:9 (tạo bằng AI)

Tài liệu tạo hình đề xuất 5 nền (một nền mỗi hồi). **Một nền cho 4–6 phút sẽ lặp lại đúng lỗi "đơn điệu" của bản cũ**, nên bản này dùng 5 nền đó làm **nền chủ đạo của từng hồi**, cộng thêm các nền phụ theo bảng shot.

Prompt master (mục 6.2 tài liệu tạo hình) + `no people, no text, no letters, no watermark`. **Bỏ địa chỉ "2103 North Volunteer Blvd" khỏi prompt** (AI sẽ cố vẽ chữ); số nhà do Pillow thêm nếu cần.

| Mã nền | Mô tả (phần riêng của prompt) | Hồi |
|---|---|---|
| **`house_night`** ★ | Nhà nhỏ một tầng sơn hồng nhạt, đêm sương mưa, băng niêm phong vàng | 1 (chủ đạo) |
| `house_police` | `house_night` + vệt đèn đỏ/xanh phản chiếu mặt đường ướt | 1 |
| `phone_dark` | Mặt bàn tối, một chiếc điện thoại úp sáng mờ | 1 |
| `bedroom_door` | Hành lang tối, cửa phòng ngủ hé, vệt đèn pin lạnh | 1, 2 |
| `empty_room` | Phòng ngủ trống, giường gọn, rèm kéo | 1 |
| **`wheelchair_room`** ★ | Xe lăn bỏ không giữa phòng, bình oxy, kệ lọ thuốc, ánh trăng qua rèm | 2 (chủ đạo), 1 |
| `interrogation` | Phòng thẩm vấn: bàn, 2 ghế, đèn treo hình nón | 1 |
| `route_night` | Đường cao tốc đêm nhìn từ trên cao, đèn xe kéo vệt | 1 |
| `records` | Chồng hồ sơ bệnh án cao, ánh đèn bàn lạnh | 2 |
| `clinical` | Phòng khám trống, giường khám, ánh huỳnh quang | 2 |
| `pinboard` | Bảng ghim bần, dây đỏ, **thẻ trống không chữ**, đèn trần lạnh | 2, 4 |
| `storm` | Mưa bão đêm, nước dâng, mái nhà | 2 |
| `house_closed` | Cận cửa sổ nhà hồng, rèm kéo kín, khoá cửa | 2 |
| **`brain_desk`** ★ | Bàn làm việc: sách DSM mở (chữ mờ), mô hình não thuỷ tinh phát sáng, dây đỏ | 3 (chủ đạo) |
| `void` | Nền đen có sương và bụi | mọi hồi |
| `charity` | Bàn với phong bì từ thiện, đồng xu, hộp quà | 3 |
| `fog` | Sương dày, một khoảng sáng mờ | 3 |
| `spotlight` | Sân khấu tối, một luồng đèn rọi | 3 |
| `dress_hanger` | Váy xoè trẻ em treo móc trong tủ tối | 3 |
| `doll` | Búp bê sứ nằm trong lòng bàn tay lớn | 3 |
| **`locked_door`** ★ | Hành lang tối nhìn về cửa phòng khoá chốt ngoài, ánh xanh lọt dưới khe | 4 (chủ đạo) |
| `glass_box` | Hộp kính trống giữa phòng tối | 4 |
| `cage` | Lồng chim cổ, cửa đóng (+ bản cửa mở, cùng seed) | 4, 5 |
| `hands` | Bàn tay lớn nắm bàn tay nhỏ, ánh nghiêng | 4 |
| `night_street` | Phố vắng đêm, đèn đường | 4 |
| `screen_off` | Màn hình máy tính trong phòng tối (bản sáng + bản tắt, cùng seed) | 4 |
| `corridor` | Hành lang dài nhiều cửa đóng | 4 |
| `night_screen` | Góc phòng tối, ánh màn hình xanh | 4 |
| **`court_dawn`** ★ | Phòng xử trống lúc bình minh, búa gỗ trên hồ sơ, nắng hổ phách | 5 (chủ đạo) |
| `prison_window` | Ô cửa sổ song sắt, nắng chiếu vào | 5 |
| `house_dawn` | Nhà hồng lúc bình minh, tông ấm | 5 |
| `podcast_desk` | Bàn podcast trống: micro, máy cassette, đèn bàn (không có nhân vật) | 1, 5 |

★ = 5 nền chủ đạo theo tài liệu tạo hình. Tổng **32 nền**, tạo một lần; tập sau dùng lại phần lớn.

**Kích thước:** tạo 16:9 ở độ phân giải cao nhất công cụ cho phép (≥ 1344×768), phóng lên 2112×1188 (Lanczos + làm nét nhẹ); hạt phim che phần mềm.
**Đồ hoạ không dùng AI:** dòng thời gian, thẻ thuật ngữ, cờ đỏ, sơ đồ não 3 tầng, thẻ trên bảng ghim, con số — Pillow vẽ đè lên nền (chữ luôn đúng).

### 5.7 Lớp nhân vật — 3 dạng hiển thị (tự động theo `timeline_s.json`)

| Dạng | Hình | Vị trí / cỡ | Khi nào |
|---|---|---|---|
| **Dạng 2 · Badge hồ sơ** | Thẻ bo góc `slate` 85% · ảnh P0 tròn 80 px · tên vai 26 px màu vai · **sóng âm thật** từ `stems/` (`showwaves`, màu vai, 160×40) | Góc trên-trái `x=72 y=60`, **380×120** | **Suốt mọi lượt của cả 5 nhân vật** |
| **Dạng 1 · Bán thân nổi** | Ảnh P1/P2 tách nền, đáy chìm vào bóng · **thở** 1,000↔1,006 (4 s) · **viền sáng bừng +15%** 0,3 s ở đầu câu | Góc dưới-trái `x=48`, **420×500**, đáy chạm mép khung | **Câu đầu mỗi lượt** (3–6 s) · câu ghi `🅑` trong bảng mục 6 · lần đầu xuất hiện kèm thẻ giới thiệu |
| **Dạng 3 · Đổi người nói** | Badge cũ trượt ra trái 0,3 s → badge mới trượt vào 0,3 s | — | Mỗi lần đổi `role`. **Nền vụ án phía sau không cắt** |

**Lớp phụ:**

| Lớp | Nội dung | Khi nào |
|---|---|---|
| **Thẻ giới thiệu** | Cạnh phải bán thân: tên vai 34 px · chức danh 26 px · *"Nhân vật minh hoạ · giọng đọc AI"* 22 px | Lần đầu mỗi nhân vật nói, 4 s |
| **Lời mời** | Badge của nhân vật **sắp nói** hiện mờ 50% ở góc trên-phải + chữ *TIẾP THEO* | Khi Host nói câu mời (cột `handoff` trong bảng) |
| **Hai badge** | Badge Cáo trái + Sói phải; người đang nói sáng 100% + sóng âm, người kia 50% | `5.07`–`5.08` (4 cờ đỏ) |
| **Dàn khách mời** | 5 ảnh P0 xếp hàng ở 1/3 dưới, nền vụ án vẫn chạy | `5.12#1` |

**Vùng cấm chữ khi bán thân đang hiện:** `x 0–520, y 560–1080`. Mọi mẫu khung đặt chữ ở bên trái phải dời khối chữ sang `x ≥ 560` trong lúc đó (`render_layers.py` tự dời; `qc.py` kiểm tra giao nhau).

**Mỗi vai vẫn "sở hữu" kiểu đồ hoạ tầng câu chuyện** để hình kể đúng giọng người nói:

| Vai | Đồ hoạ minh hoạ khi vai này nói | Mẫu khung chính |
|---|---|---|
| Cú · Host | Cảnh điện ảnh toàn khung, câu chốt lớn | T1, T4, T10 |
| Sói · Điều tra viên | Bảng ghim, giấy hồ sơ, dấu mộc, dòng thời gian, tuyến đường | T2, T6, T7, T8 gạch bỏ |
| Cáo · Chuyên gia | Sơ đồ đường mảnh, thẻ thuật ngữ, so sánh hai cột, não 3 tầng | T9, T3, `brain3` |
| Cừu / Mèo · Người dân | Lời kể Georgia Italic trong ngoặc kép trên nền mờ ấm | T4 "lời kể" |

### 5.8 Mẫu khung (tầng câu chuyện)

Toạ độ trên 1920×1080. Vùng an toàn: lề 96 px trái/phải, 72 px trên/dưới; tránh chữ quan trọng ở 140 px đáy; **tránh vùng badge** `x 72–452, y 60–180`.

| Mẫu | Tên | Bố cục |
|---|---|---|
| **T1** | Toàn cảnh | Nền full khung · lớp tối 45% đáy · khối chữ `x=96` (hoặc `x=560` khi có bán thân), đáy `y=900` |
| **T2** | Thẻ hồ sơ | Giấy 900×620 tại (**960**, 220), xoay −1,5° · kẹp giấy · dấu mộc `red` · Consolas/Georgia · nửa trái nền mờ 50% |
| **T3** | Chia đôi / so sánh | Trái: đối tượng trên nền · vạch màu vai `x=920` · phải `x 960–1824`: chữ |
| **T4** | Trích dẫn / lời kể | Nền tối 70% + mờ · `“` 220 px · Georgia Italic 52–64 px, khối 1200 px **lệch phải** (`x=600`) · gạch chân màu vai · hiện từng dòng |
| **T5** | Con số | Bahnschrift 280 px **ở 2/3 phải** · đếm lên 1,2 s · nhãn trên, phụ dưới |
| **T6** | Dòng thời gian | Trục `y=520`, `x 160–1760` (**`x 600–1760` khi bán thân đang hiện**) · mốc chấm + năm + chú thích · tự vẽ 0,8 s · camera trượt theo mốc |
| **T7** | Tuyến đường | 2 ghim + đường đứt nét tự vẽ trên `route_night` |
| **T8** | Danh sách | ≤ 5 mục ở `x ≥ 960` · mục mới hiện, cũ mờ 60% · **gạch bỏ** · **cờ đỏ** 4 ô |
| **T9** | Thuật ngữ | Tên Việt 76 px · tên Anh Consolas 32 px · vạch màu vai · định nghĩa ≤ 2 dòng · **lệch phải** `x=760` |
| **T10** | Thẻ chương / tiêu đề | Nền `void` · `HỒI 0X` Consolas 28 · tên hồi Georgia 72. **Trong khoảng nghỉ: ẩn badge và bán thân. Khi đang có lời** (`1-21`, `5-20`): **giữ badge và bán thân** của người đang nói |
| **T11** | Bài đăng | Thẻ 760×420 giữa khung, giao diện trung tính, không logo, nhãn `MINH HOẠ` |

Đã bỏ T12–T16 của v6 (chân dung toàn khung, chuyển lời toàn khung…) — thay bằng lớp nhân vật tự động ở mục 5.7.

### 5.9 Chuyển động

- **Camera nền:** mỗi shot một chuyển động — `push` 1,00→1,05 (mặc định) · `pull` · `pan` 40–80 px · `hero` 1,00→1,10 · `still`.
- **Phần tử:** mờ dần + nhích 24 px, 0,35 s.
- **Linh thú:** thở · viền sáng bừng ở đầu câu · đổi P1↔P2 ở đầu câu chốt (hoà tan 0,25 s). **Không cử động miệng/mỏ.**
- **Chuyển cảnh nền:** hoà tan 0,35 s (mặc định) · ✂ cắt thẳng · ◼ tối đen 0,6 + 0,6 s ở ranh giới hồi. **Đổi người nói không phải lý do để cắt nền** — chỉ badge trượt.
- **Nhịp:** shot 3–15 s; câu > 15 s cần beat mỗi ≤ 7 s.

### 5.10 Thứ tự lớp

```
1. Nền AI 2112×1188 → camera
2. Hạt phim noise=alls=2 · rgbashift ±1                 ← chỉ lớp nền
3. Bóng người vụ án, motif, ánh sáng
4. Chữ, sơ đồ (1920×1080, không zoom)
5. Lớp nhân vật: bán thân · badge · sóng âm             ← trên cùng, không hạt
6. Vignette PI/5 rất nhẹ
```

### 5.11 Intro kênh và bộ nhận diện kênh

#### Bộ nhận diện (`channel.json` — làm một lần)

| Thành phần | Thiết kế | Cách tạo |
|---|---|---|
| **Tên kênh** | **Amber eyes** (người dùng chốt 22/10). Trên hình viết hoa **AMBER EYES**; trong mô tả, tiêu đề giữ đúng "Amber eyes". Tên khớp trực tiếp với logo đôi kính hổ phách của Cú | — |
| **Khẩu hiệu** | *"Phân tích tâm lý tội phạm qua những hồ sơ có thật"* | — |
| **Logo** | **Đôi kính tròn hổ phách phát sáng** (lấy từ Cú · Host) nối với nhau bằng **một sợi chỉ đỏ** (bảng ghim của Sói), đặt trên bìa hồ sơ tối. Thu nhỏ 64 px vẫn nhận ra 2 vòng sáng + 1 vạch đỏ | **Pillow vẽ vector** — không dùng AI để logo thuộc quyền của kênh trọn vẹn, không vướng điều khoản công cụ tạo ảnh |
| **Chữ tên kênh** | Georgia, viết hoa, giãn chữ +20%, màu `text`; vạch `amber` 2 px bên dưới | Pillow |
| **Âm hiệu** | Tiếng "Tách" máy ghi âm (đã có ở mục 3.5) | ffmpeg |
| **Bộ màu kênh** | `ink` nền · `amber` chủ đạo · `red` sợi chỉ · 4 màu vai còn lại chỉ xuất hiện ở cảnh dàn nhân vật | — |

Xuất: `assets/brand/logo.png` (2048 px, nền trong suốt) · `logo_64.png` · `watermark.png` (logo 96 px, 35% độ mờ, đặt góc dưới-phải suốt video, **ẩn trong intro và thẻ chương**).

#### Kịch bản hình intro — khớp với nhịp `bgm_music_box.mp3` (đo ngày 22/10)

Đường âm lượng của bài nhạc: nốt mạnh đầu tiên ở **1,5 s**; chỗ lặng ở **1,0 s · 3,0 s · 8,5–9,0 s**; nốt nhấn ở **18,0 s**; tự nhỏ dần từ **20,5 s** tới hết ở **22,4 s**.

Mỗi thẻ miễn trừ cần **≥ 8 s** để đọc kịp (đo ngày 22/10: thẻ B 30 từ / 129 ký tự). Vì vậy phần logo rút còn 4 s; mỗi thẻ được 8,25 s. Chỗ lặng 8,5–9,0 s rơi vào giữa thẻ A — không cắt cảnh ở đó, chỉ để dòng thứ hai của thẻ hiện ra đúng lúc nhạc vào lại.

| Shot | Thời gian | Nhịp nhạc | Hình | Chữ trên hình | Chuyển động |
|---|---|---|---|---|---|
| **I-01** | 0,0 – 4,0 s | Mở đầu, nốt mạnh 1,5 s, lặng 3,0 s | Nền `ink` + hạt phim; sợi chỉ đỏ tự vẽ (0,0–1,4 s); mắt hiện mờ từ 0,5 s, **bừng sáng đúng 1,5 s**; tên kênh gõ từng chữ (Georgia) 2,2–3,4 s; khẩu hiệu 3,4 s | **AMBER EYES** · *Phân tích tâm lý tội phạm qua những hồ sơ có thật* | Đẩy chậm 1,00→1,04 |
| **I-02** | 4,0 – 12,25 s | Câu nhạc 2, lặng 8,5–9,0 s | **Thẻ miễn trừ A** trên giấy hồ sơ `paper` 1400×640 · logo nhỏ góc thẻ | Xem nội dung bên dưới | Dòng 1 ở 4,30 s · dòng 2 ở 5,70 s · dòng 3 ở 7,10 s (đủ cả thẻ trước 7,5 s → còn ≥ 5 s đọc lại) |
| **I-03** | 12,25 – 20,5 s | Nốt nhấn 12,5 s và 18,0 s | **Thẻ miễn trừ B**; từ 18,0 s **5 vòng tròn màu vai** sáng lần lượt dọc đáy thẻ (**tạm thời** — thay bằng biểu tượng P0 của 5 linh thú sau M0, chạy lại `make_intro.py` ~1 phút) | Xem nội dung bên dưới | Dòng 1 ở 12,55 s · dòng 2 ở 13,95 s · dòng 3 ở 15,35 s |
| **I-04** | 20,5 – 22,41 s | Nhạc nhỏ dần | Thẻ mờ dần **về nền đen** | — | Mờ 1,9 s |

#### Nội dung hai thẻ miễn trừ

**Thẻ A — VỀ NỘI DUNG NÀY** *(32 từ · nội dung người dùng chốt ngày 22/10)*
> Nội dung **giáo dục**, phân tích tâm lý học tội phạm.
> Dựa trên **tư liệu công khai**, nguồn ở phần mô tả.
> Không nhằm kết tội hay bôi nhọ bất kỳ ai.

**Thẻ B — LƯU Ý TRƯỚC KHI XEM** *(nội dung người dùng chốt ngày 22/10)*
> Nội dung **không phù hợp cho trẻ em**.
> Âm thanh và hình ảnh **chỉ mang tính minh hoạ**.
> Không thay thế tư vấn y khoa, tâm lý hay pháp lý.

> Việc công khai nội dung tạo bằng AI vẫn được giữ ở **mô tả YouTube** (mục 9.1), ở **thẻ giới thiệu nhân vật** (V6) và ở tuỳ chọn **"Nội dung bị thay đổi hoặc nội dung tổng hợp"** khi tải lên.

Định dạng: nhãn Consolas 26 px `red` (*VỀ NỘI DUNG NÀY*) · thân Segoe UI 38 px `paper_ink`, từ in đậm bằng Segoe Bold · khối rộng 1200 px · logo 64 px góc trên-phải thẻ.

> **Giới hạn cần biết:** lời miễn trừ **không ngăn được** khiếu nại bản quyền hay đơn kiện. Nó giúp người xem hiểu đúng và thể hiện thiện chí. Lớp bảo vệ thật nằm ở mục 9.2: chỉ dùng tài sản tự tạo hoặc có giấy phép, ghi nguồn gốc từng tài sản, và trích nguồn công khai cho từng dữ kiện.

#### Luật cho intro

- **Phần dùng chung mọi tập:** `assets/brand/intro_kenh.mov` — **chỉ hình, không tiếng**, 22,41 s, kết thúc bằng nền đen. Render một lần.
- **Phần riêng của từng tập** nằm ngoài file intro: âm thanh (music box đặt vào master ở t = 0, drone + còi của Tập 1 vào từ 19,5 s) và hình nền đầu hồi 1 (`house_police` hiện dần **chồng lên** 1,9 s cuối màu đen của intro — shot `1-00`).
  → Tập sau chỉ đổi phần riêng, không đụng vào intro.
- Không đưa số tập hay tên tập vào intro — tên tập đã có ở shot `1-21`.
- Trong intro: **ẩn badge, bán thân, watermark**; không lời đọc.
- Thời lượng intro cố định **22,41 s** = đúng độ dài file nhạc.

---

## 6. DANH SÁCH SHOT — TOÀN TẬP

**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng chỉ mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo mục 5.7.
Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X (hiện badge chờ) · `✦` = lần đầu xuất hiện (thẻ giới thiệu) · `⊘` = tắt bán thân.
Cột cuối: trống = hoà tan · ✂ cắt · ◼ tối đen.

### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`

Đặt `assets/brand/intro_kenh.mov` (chỉ hình, shot I-01 → I-04, chi tiết ở mục 5.11) ở 0,00 s. Không câu thoại nào thuộc intro.

### HỒI 1 — KHOẢNH KHẮC ĐỨT GÃY NIỀM TIN · nền chủ đạo `house_night`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s, chồng lên phần đen cuối intro) | — | T1 | `house_police` hiện dần từ đen, `push` | *HỒI 01 · KHOẢNH KHẮC ĐỨT GÃY NIỀM TIN* | Đèn cảnh sát quét; drone dâng | ⊘ | |
| 1-01 | `1.03#1`–`#2` | H | T5 ngày | `house_night` mờ | **14 · 06 · 2015** · *Springfield, Missouri* | Gõ từng ký tự | ✦ Cú | |
| 1-02 | `1.03#3` | H | T11 | `phone_dark` | *TRANG MẠNG XÃ HỘI CHUNG CỦA HAI MẸ CON* → **MỘT DÒNG TRẠNG THÁI KHIẾN CẢ KHU PHỐ CHẾT LẶNG** | Bài đăng hiện dạng các dòng mờ, không đọc được chữ, ở "đầy hằn học" | | |
| 1-03 | `1.04` (nghỉ 2 s) | — | — | giữ 1-02, ánh đỏ nhấp nháy | — | — | | |
| 1-04 | `1.05#1` | H | T1 | `house_police` + `crowd` | **NGÔI NHÀ NHỎ SƠN MÀU HỒNG PHẤN** · *Springfield, Missouri* (không hiện số nhà — nhà riêng, có thể đang có người ở) | — | | |
| 1-05 | `1.05#2` | H | T1 | `house_night`, `pull` | *LẮNG NGHE:* **MỘT NGƯỜI DÂN CÙNG KHU PHỐ** | — | →N1 | |
| 1-06 | `1.07#1` | N1 | T4 lời kể | `house_night` ấm, mờ | “Biểu tượng của tình mẫu tử thiêng liêng” | — | ✦ Cừu | |
| 1-07 | `1.07#2` | N1 | T8 | `wheelchair_room` + `deedee_wheelchair` | *NHỮNG GÌ CẢ KHU PHỐ TIN* · *Bại liệt từ thắt lưng trở xuống · Ung thư máu · Loạn dưỡng cơ · Động kinh nặng · Trí tuệ ngang trẻ lên bảy* | Mỗi mục tại cụm từ | | |
| 1-08 | `1.07#3` | N1 | T4 lời kể | `house_night` ấm | “Ai trong thị trấn này cũng rơi nước mắt cảm phục” | — | 🅑 | |
| 1-09 | `1.08#1` | H | T1 | `bedroom_door` | **NGƯỜI MẸ ĐÃ QUA ĐỜI** | — | | |
| 1-10 | `1.08#2` | H | T1 | `empty_room`, `still` | **GYPSY ROSE ĐÃ BIẾN MẤT** | — | ⊘ | ✂ |
| 1-11 | `1.08#3`–`#4` | H | T1 | `wheelchair_room` | **XE LĂN · BÌNH OXY · HÀNG CHỤC LỌ THUỐC** | `#3` sáng xe lăn, `#4` sáng kệ | | |
| 1-12 | `1.08#5` | H | T3 | `wheelchair_room` tối + dấu `?` lớn | *CẢ NƯỚC MỸ HỎI* · **AI ĐÃ GÂY RA CÁI CHẾT CỦA NGƯỜI MẸ?** | — | | |
| 1-13 | `1.08#6` | H | T1 | `interrogation`, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN THỤ LÝ HỒ SƠ** | — | →D | |
| 1-14 | `1.09`–`1.10` (nghỉ 2 s) | — | — | giữ 1-13, nhiễu bộ đàm `cold` | — | — | ⊘ | |
| 1-15 | `1.11#1` | D | T2 | `pinboard` | **LỆNH TRUY TÌM TOÀN QUỐC** | Dấu mộc ở "phát lệnh truy tìm" | ✦ Sói | |
| 1-16 | `1.11#2` | D | T7 | `route_night` | **48 GIỜ SAU** · *Bang Wisconsin — cách hàng trăm dặm* | Đường tự vẽ, số đếm | | |
| 1-17 | `1.11#3`–`#4` | D | T1 | `interrogation` + `gypsy_stand` | **CÔ TA TỰ BƯỚC ĐI** | Đèn treo sáng ở `#4` | | |
| 1-18 | `1.11#5`–`#7` | D | T8 gạch bỏ | giấy hồ sơ trên `records` | *Ung thư máu · Loạn dưỡng cơ · Tổn thương não* | Mỗi câu gạch một mục | | ✂ |
| 1-19 | `1.11#8` | D | T1 `hero` | `bedroom_door` + `gypsy_stand`, tối dần | **CÔ CON GÁI BÉ BỎNG CỦA BÀ** | Tiêu đề ở "không ai khác" | 🅑 P2 | |
| 1-20 | `1.13#1` | H | T1 | `podcast_desk`, cassette quay | **HỒ SƠ PHÂN TÍCH TÂM LÝ HỌC TỘI PHẠM** | "Tách" ở đầu | 🅑 | |
| 1-21 | `1.13#2` | H | T9 → T10 | `house_night` | **HỘI CHỨNG MÜNCHAUSEN QUA TRUNG GIAN** → *TẬP 01 · ĐỘC DƯỢC NHÂN DANH TÌNH MẸ* | Thuật ngữ ở "Hội chứng"; tên tập cuối câu | | |
| 1-22 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 02* · **23 NĂM TRONG NHÀ TÙ Y KHOA** | — | ⊘ | ◼ |

### HỒI 2 — HIỆN TRƯỜNG & HỒ SƠ BỆNH ÁN · nền chủ đạo `wheelchair_room`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 2-01 | `2.02#1`–`#2` | H | T1 | `bedroom_door` | **KHÔNG PHẢI CĂN PHÒNG NGỦ** · *Tháng 6 năm 2015* | Tiêu đề ở `#2` | | |
| 2-02 | `2.02#3` | H | T5 | `wheelchair_room` + `gypsy_wheelchair` | *HIỆN TRƯỜNG THỰC SỰ* · **23 NĂM** | Số đếm | | |
| 2-03 | `2.04#1`–`#5` | H | T6 | `records`, `pan` | *1991 · Sinh ra khỏe mạnh* → *3 tháng tuổi · Ngưng thở khi ngủ* → *Danh sách bệnh án bắt đầu* → *7 tuổi · Tổn thương tủy sống · Xe lăn* → *Cạo trọc đầu · Hoá trị ung thư máu* | Mỗi câu một mốc | ⊘ | |
| 2-04 | `2.06#1` | H | T1 | `clinical` | **KHÔNG CHỈ LÀ LỜI NÓI DỐI** | — | 🅑 | |
| 2-05 | `2.06#2` | H | T2 | `records` | **HÀNG NGÀN TRANG BỆNH ÁN** · *Can thiệp y khoa trực tiếp lên cơ thể Gypsy* | — | | |
| 2-06 | `2.06#3` | H | T1 | `pinboard` mờ, `push` | *LẮNG NGHE:* **ĐIỀU TRA VIÊN CÔNG BỐ HỒ SƠ** | — | →D | |
| 2-07 | `2.07#1` | D | T2 | `pinboard` | **BA DẤU VẾT TRONG HỒ SƠ Y TẾ** | Bộ đếm `0/3` | | |
| 2-08 | `2.07#2` | D | T3 `1/3` | `wheelchair_room` cận kệ thuốc | **THUỐC CHỐNG ĐỘNG KINH LIỀU CAO** · *Dù cô không hề bị động kinh* | Phụ ở "dù cô không hề" | | |
| 2-09 | `2.07#3` | D | T3 `2/3` | `clinical` | **ỐNG NUÔI ĂN QUA DẠ DÀY** | — | | |
| 2-10 | `2.07#4` | D | T3 `3/3` | `clinical` tối | **PHẪU THUẬT KHÔNG CẦN THIẾT** · *Từ những triệu chứng giả trước mắt bác sĩ* | — | | |
| 2-11 | `2.07#5` | D | T5 | `clinical` + lưới ~100 biểu tượng bác sĩ (Pillow) | **HÀNG TRĂM BÁC SĨ** · *Không ai phát hiện ra?* | Biểu tượng hiện dần | | |
| 2-12 | `2.07#6` | D | T9 | `pinboard`, `pull` | **PHƯƠNG THỨC HÀNH ĐỘNG** *(Modus Operandi)* | 3 thẻ trống ghim lên | 🅑 | |
| 2-13 | `2.07#7` | D | T2 trên bảng ghim | camera dời tới thẻ 1 | *01* · **TỪNG LÀM HỘ LÝ** · *Nắm rõ thuật ngữ y khoa* | — | | |
| 2-14 | `2.07#8`–`#9` | D | T2 trên bảng ghim | thẻ 2 có ảnh `storm` thu nhỏ | *02 · 2005* · **BÃO KATRINA** → `#9`: *Mọi lịch sử y tế chỉ qua lời bà Dee Dee* | Dây đỏ nối ở `#9` | | |
| 2-15 | `2.07#10` | D | T2 trên bảng ghim | thẻ 3 + ghi chú Consolas | *03* · **AI NGHI NGỜ → ĐỔI BỆNH VIỆN, CHUYỂN NHÀ** · *BS. Bernardo Flasterstein · 2007* (chỉ chữ, V5) | Kéo ra thấy cả bảng | | |
| 2-16 | `2.09#1`–`#2` | H | T1 | `house_closed` | **CỬA SỔ LUÔN ĐÓNG KÍN** · *Không được đi học* | Tiếng khoá cửa ở đầu | | |
| 2-17 | `2.09#3` | H | T5 | `house_closed` mờ | **−4 TUỔI** · *Khai gian để mãi là trẻ vị thành niên* | — | | |
| 2-18 | `2.09#4` | H | T1 | `house_night` + bóng song sắt ghép từ lọ thuốc, ống truyền (Pillow) | **MỘT NHÀ TÙ KHÔNG CHẤN SONG** | Song sắt ở "được xây bằng" | | |
| 2-19 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 03* · **BÊN TRONG BỘ NÃO CỦA KẺ MẮC FDIA** | — | ⊘ | ◼ |

### HỒI 3 — GIẢI PHẪU TÂM LÝ · nền chủ đạo `brain_desk`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 3-01 | `3.02#1` | H | T5 | `void`, `still` | *CÂU HỎI LỚN NHẤT* · **TẠI SAO?** | Đúng ở "Tại sao" | ⊘ | ✂ |
| 3-02 | `3.02#2` | H | T1 | `fog` + `deedee_wheelchair` | **HƠN HAI THẬP KỶ** | — | | |
| 3-03 | `3.02#3`–`#4` | H | T3 | `charity` | **TRỤC LỢI TỪ THIỆN?** → `#4`: **TIỀN CHỈ LÀ PHẦN THƯỞNG PHỤ** | Đồng xu mờ ở `#4` | | |
| 3-04 | `3.02#5` | H | T9 | `brain_desk` | **HỘI CHỨNG MÜNCHAUSEN QUA TRUNG GIAN** *(Münchausen Syndrome by Proxy)* · *DSM-5-TR: Rối loạn giả bệnh áp đặt lên người khác — FDIA* | Dòng DSM ở "DSM-5-TR" | | |
| 3-05 | `3.03` (nghỉ) | — | — | giữ 3-04 | — | — | | |
| 3-06 | `3.04#1`–`#2` | H | T1 | `brain_desk`, `push` | *LẮNG NGHE:* **CHUYÊN GIA TÂM LÝ HỌC TỘI PHẠM** → *3 tầng tâm lý* | — | →C | |
| 3-07 | `3.05#1` | C | T9 | `brain_desk` + sơ đồ `brain3` | **3 TẦNG ĐỘNG CƠ** · *Vô thức và ý thức* | 3 vòng sáng lần lượt | ✦ Cáo | |
| 3-08 | `3.05#2` | C | T4 | `brain_desk` tối, tầng 1 sáng + `halo` | *TẦNG 01 · CƠN NGHIỆN HÀO QUANG* · “Vị thánh tử đạo” | — | | |
| 3-09 | `3.05#3`–`#4` | C | T3 so sánh | `brain_desk` mờ | **MALINGERING** *(Giả bệnh trục lợi) → tiền* · `#4`: **MÜNCHAUSEN** *→ sự chú ý, thương cảm, tôn sùng* | Cột phải ở `#4` | | |
| 3-10 | `3.05#5`–`#6` | C | T1 | `fog` + `deedee_wheelchair` mờ | *Gia đình xa lánh · Hôn nhân tan vỡ ở tuổi 24* → **MỘT CÁI BÓNG MỜ NHẠT** | Tiêu đề ở `#6` | | |
| 3-11 | `3.05#7` | C | T1 | `spotlight` + `deedee_wheelchair` | **TRUNG TÂM CỦA VŨ TRỤ** | Đèn bật ở "bỗng nhiên" | | ✂ |
| 3-12 | `3.05#8` | C | T1 | `spotlight` + biểu tượng bác sĩ, hàng xóm, tờ báo | **VỊ THÁNH SỐNG** | Mỗi biểu tượng ở cụm từ | | |
| 3-13 | `3.05#9` | C | T5 | `void` + đường nhịp tăng vọt | **DOPAMINE** · *Mỗi lần Gypsy nhập viện cấp cứu* | Nhịp nhấp nháy | 🅑 P2 | |
| 3-14 | `3.06` (nghỉ) | — | — | tối dần | — | — | | |
| 3-15 | `3.07#1` | H | T1 | `brain_desk` | **MỚI CHỈ LÀ BỀ NỔI** | — | | |
| 3-16 | `3.07#2` | H | T2 | `records` | *LỜI KHAI GIA ĐÌNH BÊN NGOẠI* · **BỊ NGHI GÂY HẠI CHO NGƯỜI THÂN** | — | →C | |
| 3-17 | `3.08#1` | C | T9 | `brain_desk`, tầng 2 sáng | *TẦNG 02* · **NỖI SỢ BỊ BỎ RƠI · NHU CẦU KIỂM SOÁT** | — | | |
| 3-18 | `3.08#2`–`#4` | C | T3 | `hands` | **MỘT VẬT SỞ HỮU DUY NHẤT** → `#3`: *Đi học → bạn bè → yêu đương → rời xa mẹ* → `#4`: **GIỮ MỘT CON NGƯỜI MÃI MÃI?** | 3 beat | | |
| 3-19 | `3.08#5` | C | T1 `hero` | `void`, tối dần | **HÃY KHIẾN CON BÉ TIN RẰNG MÌNH BỆNH TẬT** | Tiêu đề ở "Hãy khiến" | ⊘ | |
| 3-20 | `3.08#6` | C | T3 | `wheelchair_room` + `gypsy_wheelchair` | **NGƯỜI DUY NHẤT NẮM GIỮ CUỘC SỐNG CỦA CON GÁI** | — | | |
| 3-21 | `3.09` (nghỉ) | — | — | giữ 3-20 | — | — | | |
| 3-22 | `3.10#1` | C | T9 | `brain_desk`, tầng 3 sáng | *TẦNG 03* · **DẤU ẤN XOÁ BỎ NHÂN DẠNG** *(Signature)* | — | | |
| 3-23 | `3.10#2` | C | T3 | `dress_hanger` | **CẠO TRỌC ĐẦU · VÁY CÔNG CHÚA** · *Ngay cả khi cô đã hơn 20 tuổi* | — | | |
| 3-24 | `3.10#3`–`#4` | C | T9 | `dress_hanger` mờ | *Không chỉ là giả bệnh ung thư* → **TƯỚC ĐOẠT SỰ TRƯỞNG THÀNH** *(Infantilization)* | Thuật ngữ ở `#4` | 🅑 | |
| 3-25 | `3.10#5`–`#6` | C | T1 | `doll` | **CON BÚP BÊ SỨ 7 TUỔI** | Tiêu đề ở "búp bê sứ" | | |
| 3-26 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 04* · **TẠI SAO GYPSY KHÔNG ĐỨNG DẬY?** | — | ⊘ | ◼ |

### HỒI 4 — GÓC NHÌN NẠN NHÂN · nền chủ đạo `locked_door`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 4-01 | `4.02#1` | H | T1 | `night_screen` + bong bóng bình luận mờ (Pillow, không tên) | **CÂU HỎI ĐẦY HOÀI NGHI** · *Dành cho chính Gypsy Rose* | — | | |
| 4-02 | `4.02#2` | H | T1 | `night_screen`, `push` | *LẮNG NGHE:* **MỘT KHÁN GIẢ THEO DÕI VỤ ÁN** | — | →N2 | |
| 4-03 | `4.03#1` | N2 | T4 lời kể | `night_screen` | “Cô ấy biết rõ đôi chân mình không hề bị liệt.” | — | ✦ Mèo | |
| 4-04 | `4.03#2`–`#3` | N2 | T4 lời kể | `wheelchair_room` tối, xe lăn trống dưới đèn rọi | “Mỗi tối… cô ấy vẫn tự đứng dậy đi lại bình thường.” → “Vậy tại sao… Gypsy không một lần đứng phắt dậy khỏi chiếc xe lăn để tố cáo mẹ mình?” | Mỗi câu một dòng | 🅑 ở `#3` | |
| 4-05 | `4.04` (nghỉ) | — | — | tối dần | — | — | | |
| 4-06 | `4.05#1` | H | T1 | `glass_box` + `gypsy_wheelchair` nhỏ | **LỚN LÊN TRONG LỒNG KÍNH** | — | | |
| 4-07 | `4.05#2` | H | T3 | `locked_door` · 2 thẻ thuật ngữ | **BẤT LỰC TẬP NHIỄM** *(Learned Helplessness)* · **GẮN KẾT CHẤN THƯƠNG** *(Trauma Bonding)* | Mỗi thẻ ở cụm từ | →C | |
| 4-08 | `4.07#1` | C | T9 | `cage` đóng | **SỰ BẤT LỰC TẬP NHIỄM** · *Martin Seligman · 1967* | Tiếng xích ở đầu | | |
| 4-09 | `4.07#2` | C | T4 `hero` | `cage` đóng, tối dần | “Mọi sự vùng vẫy đều vô nghĩa” | Câu trích ở cụm từ | | |
| 4-10 | `4.07#3` | C | T1 | `cage` đóng → mở (hoà tan 2 nền cùng seed) | **CỬA LỒNG ĐÃ MỞ TOANG** · *…nhưng không bao giờ bước ra nữa* | Cửa mở ở "cánh cửa lồng" | | |
| 4-11 | `4.07#4` | C | T1 | `locked_door` | **THẾ GIỚI QUAN CỦA GYPSY** | — | 🅑 P2 | |
| 4-12 | `4.07#5`–`#6` | C | T3 | `hands` | **BÀ LUÔN NẮM CHẶT TAY GYPSY** · `#6`: *Với người ngoài: cử chỉ âu yếm* | — | | |
| 4-13 | `4.07#7` | C | T3 | `hands`, ánh `cold` | *Với Gypsy: một mật lệnh đe dọa* · **MỘT LỜI CẢNH CÁO KHÔNG THÀNH TIẾNG** | Hai bàn tay khép chặt hơn ở "siết chặt" | | |
| 4-14 | `4.07#8` | C | T2 | `locked_door` | *SAU BUỔI KHÁM BỆNH* · **HÌNH PHẠT NGHIÊM KHẮC · KIỂM SOÁT NGỘT NGẠT** | Khe sáng tắt ở "khép lại" | | |
| 4-15 | `4.08` (nghỉ) | — | — | tối dần | — | — | | |
| 4-16 | `4.09#1` | H | T1 | `locked_door`, khe sáng dưới cửa | **GYPSY TỪNG CỐ GẮNG TỰ CỨU MÌNH** | — | | ✂ |
| 4-17 | `4.09#2` | H | T2 | `records` | *BIÊN BẢN THẨM VẤN* · **BIẾN CỐ NĂM 2011** | — | | |
| 4-18 | `4.09#3` | H | T1 | `pinboard` mờ | *LẮNG NGHE:* **HỒ SƠ SỰ VIỆC TỪ ĐIỀU TRA VIÊN** | — | →D | |
| 4-19 | `4.10#1` | D | T6 | `night_street` + `gypsy_stand` | *2011 · 19 tuổi* · **TRỐN KHỎI NHÀ ĐỂ CẦU CỨU** | — | | |
| 4-20 | `4.10#2`–`#3` | D | T2 | `pinboard`, tập giấy tờ, dấu `GIẢ MẠO` | **VÀI GIỜ SAU, BÀ LẦN RA DẤU VẾT** → `#3`: *Giấy tờ giả mạo: vị thành niên · thiểu năng trí tuệ · mất năng lực hành vi dân sự* | Dấu mộc ở "giả mạo" | | |
| 4-21 | `4.10#4` | D | T1 | `house_night` + `gypsy_walk` đi về nhà | **TRAO TRẢ VỀ NGÔI NHÀ MÀU HỒNG** | — | | |
| 4-22 | `4.10#5` | D | T1 | `screen_off` | **ĐÊM HÔM ĐÓ** · *Không bao giờ được bước ra khỏi cửa* | Màn hình tắt dần ở "phá hỏng" | 🅑 P2 | |
| 4-23 | `4.11` (nghỉ) | — | — | tối dần | — | — | | |
| 4-24 | `4.12#1` | H | T1 | `night_street` + `crowd` quay lưng | **XÃ HỘI CHỈ TIN NGƯỜI MẸ** · *Cú sốc năm 2011* | — | | |
| 4-25 | `4.12#2` | H | T1 | `locked_door` + một sợi chỉ mảnh (Pillow) | *LẮNG NGHE:* **SỢI DÂY VÔ HÌNH** | — | →C | |
| 4-26 | `4.13#1` | C | T9 | `hands` mờ | **GẮN KẾT CHẤN THƯƠNG** *(Trauma Bonding)* | — | | |
| 4-27 | `4.13#2` | C | T4 | `dress_hanger` tối | *Người gây ra bệnh tật — cũng là người duy nhất ôm ấp cô* → “thiên thần nhỏ của mẹ” | Câu trích ở cụm từ | | |
| 4-28 | `4.13#3` | C | T3 | `void` + đường ranh giới tan dần (Pillow) | **TÊ LIỆT KHẢ NĂNG PHÂN ĐỊNH RANH GIỚI** | Đường tan trong câu | | |
| 4-29 | `4.15#1` | H | T1 | `corridor` | **MỌI LỐI THOÁT HỢP PHÁP BỊ BỊT KÍN** | Tiếng bàn phím ở đầu | | |
| 4-30 | `4.15#2` | H | T1 | `night_screen` + `godejohn_screen` | **NICHOLAS GODEJOHN** · *Quen qua mạng Internet* | — | | |
| 4-31 | `4.15#3` | H | T9 | `void` + 2 bóng người, bóng đổ hoà làm một | **FOLIE À DEUX** *(Điên cuồng đôi)* | Bóng nhập ở "trượt vào" | | |
| 4-32 | `4.15#4`–`#5` | H | T1 `hero` | `house_night`, cửa mở, ánh sáng tràn | *Chỉ khi mẹ cô biến mất…* → **THÁNG 6 · 2015** | Cửa sáng ở "mở cửa" | ⊘ | |
| 4-33 | nghỉ chuyển hồi (2 s) | — | T10 | `void` | *HỒI 05* · **PHÁN QUYẾT PHÁP Y & LỜI KẾT** | — | ⊘ | ◼ |

### HỒI 5 — PHÁN QUYẾT, DẤU HIỆU NHẬN DIỆN & LỜI KẾT · nền chủ đạo `court_dawn`

| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |
|---|---|---|---|---|---|---|---|---|
| 5-01 | `5.02#1` | H | T1 | `court_dawn` | **TÒA ÁN BANG MISSOURI** | Búa gõ ở đầu câu | | |
| 5-02 | `5.02#2` | H | T2 | `court_dawn` mờ | *VỀ MẶT LUẬT PHÁP* · **MỘT TRỌNG TỘI KHÔNG THỂ CHỐI CÃI** | — | | |
| 5-03 | `5.02#3` | H | T2 | `court_dawn` mờ + bảng tên trên bàn (Pillow) | *Dan Patterson · Chánh biện lý hạt Greene* (chỉ chữ, V5) · **KẺ CHỦ MƯU — ĐỒNG THỜI LÀ NẠN NHÂN** | Tiêu đề ở "kẻ chủ mưu" | | |
| 5-04 | `5.03` (nghỉ) | — | — | giữ 5-03 | — | — | | |
| 5-05 | `5.04#1` | H | T5 | `court_dawn` | *2016 · Giết người cấp độ hai* · **10 NĂM** · *Mức án thấp nhất có thể* | Số đếm 0 → 10 | | |
| 5-06 | `5.04#2` | H | T4 `hero` | `prison_window` | *LỜI GYPSY TRONG TRẠI GIAM* → “Ở trong nhà tù của pháp luật, lần đầu tiên trong đời tôi cảm thấy mình được tự do hơn cả khi sống trong ngôi nhà của mẹ.” | Câu trích từng dòng từ dấu `:` | ⊘ | |
| 5-07 | `5.04#3` | H | T5 | `prison_window`, nắng sáng dần | *12 · 2023* · **85%** · *Chính thức được trả tự do* | Thanh tiến trình | | |
| 5-08 | `5.05` (nghỉ) | — | — | sáng dần | — | — | | |
| 5-09 | `5.06#1` | H | T1 | `court_dawn`, `pull` | **4 DẤU HIỆU CẢNH BÁO ĐỎ** *(Red Flags)* · *Chuyên gia tâm lý & Điều tra viên* | — | →C+D | |
| 5-10 | `5.07#1` | C | T8 cờ | `void` đỏ sẫm, 4 ô cờ | *01* · **BỆNH SỬ DÀY ĐẶC — XÉT NGHIỆM LUÔN MÂU THUẪN** | Cờ 1 tô đầy | hai badge | |
| 5-11 | `5.07#2` | C | T8 cờ | cờ 2 | *02* · **TRIỆU CHỨNG CHỈ CÓ KHI NGƯỜI CHĂM SÓC CÓ MẶT** | — | hai badge | |
| 5-12 | `5.08#1` | D | T8 cờ | cờ 3 | *03* · **HÀO HỨNG VỚI THỦ THUẬT · PHÔ TRƯƠNG BỆNH · ĐỔI BÁC SĨ** | 3 cụm theo cụm từ | hai badge · Sói sáng | |
| 5-13 | `5.08#2` | D | T8 cờ | cờ 4 | *04* · **CÔ LẬP KHỎI TRƯỜNG HỌC, BẠN BÈ, NGƯỜI THÂN** + dấu mộc “bảo vệ sức khỏe” | Dấu mộc ở cụm từ | hai badge | |
| 5-14 | `5.09` (nghỉ 2,5 s) | — | T8 | đủ 4 cờ, `still` | 4 dòng tóm tắt | — | ⊘ | |
| 5-15 | `5.10#1` | H | T1 | `podcast_desk`, đèn ấm dần | **HỒ SƠ KHÉP LẠI** | — | | |
| 5-16 | `5.10#2` | H | T1 `hero` | `house_dawn` + `gypsy_walk`, xe lăn bỏ lại | **TỰ BƯỚC ĐI TRÊN ĐÔI CHÂN CỦA MÌNH** | Trời sáng dần | ⊘ | |
| 5-17 | `5.10#3` | H | T1 | `cage` mở, nắng | **THỨ KHOÁC ÁO THIÊN THẦN** | Tiêu đề ở "khoác áo thiên thần" | | |
| 5-18 | `5.11` (nghỉ) | — | — | giữ 5-17 | — | — | | |
| 5-19 | `5.12#1` | H | T1 | `podcast_desk` | **CẢM ƠN CÁC KHÁCH MỜI** · *Nhân vật minh hoạ · giọng đọc AI* | Dàn khách mời: 5 ảnh P0 sáng lần lượt | dàn khách mời | |
| 5-20 | `5.12#2` | H | T10 | `podcast_desk` mờ | **HẸN GẶP LẠI Ở TẬP TIẾP THEO** · *Để lại góc nhìn của bạn ở phần bình luận* | — | 🅑 | |
| 5-21 | `5.13`–`5.14` | — | T2 | `podcast_desk`, bìa hồ sơ gập (Pillow), cassette dừng | — | Bìa gập ở "Bụp"; mờ ra đen | ⊘ | ◼ |

**Tổng: 122 dòng = 104 shot có lời + 18 dòng không lời.** Phủ 128/128 câu, đúng thứ tự, cột Vai khớp người nói (kiểm tra bằng script ngày 22/10; `validate_shots.py` phải lặp lại).

**Xuất hiện của linh thú (ước tính):**

| Nhân vật | Lượt nói | Bán thân (câu đầu lượt + `🅑`) | Lần được mời (`→`) |
|---|---:|---:|---:|
| Cú · Host | 21 | ~22 (21 đầu lượt + 3 `🅑` − 2 đầu lượt bị `⊘`) | — |
| Sói · Điều tra viên | 4 | 7 | 4 |
| Cáo · Chuyên gia | 6 | 9 | 5 |
| Cừu · N1 | 1 | 2 | 1 |
| Mèo · N2 | 1 | 2 | 1 |

Badge hiện **suốt** mọi lượt của cả 5 nhân vật.

---

## 7. DỰNG VIDEO (B6–B7)

### 7.1 B6 · `render_layers.py`

Mỗi shot → `assets/gfx3/<shot>/`: `bg.png` (nền AI + bóng, 2112×1188) · `L01.png`… (chữ, sơ đồ, 1920×1080 trong suốt) · `meta.json`.
Lớp nhân vật (badge, bán thân, thẻ giới thiệu, dàn khách mời) vẽ **một lần cho mỗi nhân vật** trong `assets/cast/<vai>/ui/`.

### 7.2 B7 · `build_video3.py`

1. Chunk cắt ở ranh giới shot; mốc từ `timeline_s.json`.
2. Nền: `zoompan` + `noise` + `rgbashift`. Chữ overlay sau, không zoom.
3. Beat: `overlay=enable='gte(t,T)'` + `fade=t=in:st=T:d=0.35:alpha=1`.
4. **Lớp nhân vật — sinh tự động từ `timeline_s.json`:**
   - Badge: `[stem_X]showwaves=s=160x40:mode=cline:colors=<màu vai>:rate=30,format=rgba` → overlay vào ô sóng âm (đã chạy thử: nền trong suốt).
   - Trượt badge: `overlay=x='if(lt(t,T+0.3),72-452*(1-(t-T)/0.3),72)'`.
   - Bán thân thở: `zoompan z='1.003+0.003*sin(2*PI*on/120)'` trên ảnh P1 420×500.
   - Viền sáng bừng: lớp viền riêng của ảnh (tách bằng lọc cạnh sáng) với `fade` in/out 0,15 s ở đầu câu.
5. Chuyển cảnh nền theo cột cuối bảng mục 6. **Badge và bán thân không bị hoà tan theo nền** — chúng nằm ở lớp trên cùng.

Encoder: `libopenh264 -b:v 1500k -maxrate 2400k -bufsize 3000k` · AAC 160k · `-movflags +faststart`.

### 7.3 B8 · Phụ đề

Mỗi cue ≤ 2 dòng × 42 ký tự, ≤ 6 s. Cue đầu mỗi lượt ghi tên vai: `[ĐIỀU TRA VIÊN] Ban đầu, chúng tôi…`. Tải lên YouTube dạng file riêng.

---

## 8. TỰ KIỂM TRA (B9 · `qc.py`)

Sai bất kỳ mục nào → dừng, ghi `qc_report.md`.

### 8.1 Âm thanh

| Kiểm tra | Ngưỡng |
|---|---|
| Im lặng tuyệt đối (`silencedetect=n=-60dB:d=0.3`) | 0 đoạn |
| Không lời > 2,5 s (`n=-35dB`) | 0 đoạn, trừ 3 s cuối |
| Intro: music box phát trọn 22,41 s, không lời, thấp hơn mức lời 4 ± 1 LU | Có |
| Lời đầu tiên | 22,8 – 23,5 s (≤ 1,1 s sau khi intro hết) |
| Mỗi câu đúng giọng của vai | 128/128 |
| N1 ≠ N2 về `voice_id` | Có |
| Loudness | −16 ± 1 LUFS, TP ≤ −1,0 |

### 8.2 Khớp hình — lời

| Kiểm tra | Ngưỡng |
|---|---|
| Mỗi câu thuộc đúng 1 shot, shot nối liền | 128/128 |
| `shot.start` so với đầu câu | −0,30 … 0 s |
| Shot 3–15 s; > 15 s có beat mỗi ≤ 7 s | 100% |
| Khung đen ngoài điểm ◼ | 0 |

### 8.3 Nhân vật và bố cục

| Kiểm tra | Ngưỡng |
|---|---|
| Badge của vai X hiện **đúng và chỉ** trong lượt của X (ngoại lệ duy nhất: intro) | 100% thời lượng, 0 khung sai |
| Sóng âm badge lấy đúng `stems/X` | 100% |
| Bán thân hiện ở câu đầu mọi lượt (trừ câu có `⊘`) | 100% |
| Lần đầu mỗi nhân vật có thẻ giới thiệu + *"Nhân vật minh hoạ · giọng đọc AI"* | 5/5 |
| **Linh thú chiếm ≤ 20% diện tích khung** (V7) | 100% khung |
| Chữ shot **không giao** vùng bán thân / badge | 0 khung |
| Đường nhấn, viền thẻ đúng màu vai đang nói | 100% |
| Không dùng `pink` trong lớp nhân vật | 0 pixel `pink` ±8 trong ảnh cast |

### 8.4 Nội dung chữ

| Kiểm tra | Ngưỡng |
|---|---|
| Mọi con số, tên riêng trên hình có trong câu của shot | 100% |
| Chữ trong ngoặc kép xuất hiện nguyên văn trong kịch bản | 100% |
| Không "Facebook", "Disney", logo, phù hiệu, watermark | 0 |
| Ảnh AI không chứa chữ (AI tự xem từng nền) | 0 ảnh có chữ |
| Font đủ dấu tiếng Việt | 0 lỗi glyph |

### 8.4b Intro và pháp lý

| Kiểm tra | Ngưỡng |
|---|---|
| Intro dài 22,41 ± 0,05 s, đứng đầu video | Có |
| Mỗi thẻ miễn trừ hiện ≥ (số từ ÷ 4) giây — thẻ A 32 từ cần 8,0 s, thẻ B 30 từ cần 7,5 s; mỗi thẻ có 8,25 s | Thẻ A, B đều đạt |
| `intro_kenh.mov` không có luồng âm thanh và giống hệt nhau giữa các tập (so mã băm) | Có |
| Chữ hai thẻ khớp nguyên văn mục 5.11 (hoặc bản người dùng đã duyệt ở M0.5) | 100% |
| Không badge / bán thân / watermark trong intro | 0 khung |
| Watermark logo có mặt ngoài intro và thẻ chương | 100% |
| **Mọi file trong `assets/` dùng ở video có dòng trong `provenance.json`** | 100% |
| Danh sách nguồn trong mô tả: mỗi link mở được (HTTP 200) | 100% |

### 8.5 Duyệt bằng mắt (AI tự xem)

`qc_sheet_<hồi>.png`: mỗi shot một khung kèm câu và vai đang nói. Trả lời cho từng ô:
1. Hình có minh hoạ đúng câu không?
2. **Nhìn góc màn hình có biết ai đang nói không?**
3. Có chỗ nào linh thú, chữ, nền chồng lên nhau khó đọc không?
4. Có khuôn mặt người thật nào lộ nét không? Có chữ lạ do AI vẽ không?

Một câu không đạt → sửa shot, render lại chunk (`AUDI_ONLY`).

---

## 9. ĐÓNG GÓI (B10)

| File | Nội dung |
|---|---|
| `Tap01_master.mp4` | Video chính |
| `Tap01.srt` | Phụ đề có tên vai |
| `thumbnail.png` | 1280×720: nền `house_police` · **Sói** bán thân trái, **Cáo** bán thân phải (P2) · chữ **ĐỘC DƯỢC NHÂN DANH TÌNH MẸ** (Segoe Bold 110 px) |
| `mo_ta.txt` | Theo mẫu mục 9.1 |
| `provenance.json` | Hồ sơ nguồn gốc mọi tài sản (mục 9.2) — **lưu trữ, không đăng** |
| `nguon_tham_khao.md` | Danh sách nguồn công khai cho từng dữ kiện (mục 9.3) |

Khi tải lên YouTube: bật **"Nội dung bị thay đổi hoặc nội dung tổng hợp"** · chọn **"Không, nội dung này không dành cho trẻ em"** (không ảnh hưởng kiếm tiền) · **không** tự bật giới hạn 18+ · đặt danh mục *Giáo dục* · ở bước tự đánh giá quảng cáo, khai trung thực mục *chủ đề gây tranh cãi* ở mức "thảo luận, không mô tả chi tiết" (đúng với bản v2). Nếu bị biểu tượng vàng → gửi yêu cầu xem xét thủ công.

### 9.1 Mẫu mô tả YouTube

```
{Tên tập} | Amber eyes

{2–3 câu tóm tắt, lấy từ câu 1.13#2 và 3.02#5 của kịch bản}

⏱ MỐC CHƯƠNG
00:00 Intro
{mm:ss} Hồi 1 · Khoảnh khắc đứt gãy niềm tin
{mm:ss} Hồi 2 · 23 năm trong nhà tù y khoa
{mm:ss} Hồi 3 · Bên trong bộ não của kẻ mắc FDIA
{mm:ss} Hồi 4 · Tại sao Gypsy không đứng dậy?
{mm:ss} Hồi 5 · Phán quyết pháp y & lời kết
   (mốc lấy tự động từ start của các thẻ T10 trong timeline_s.json)

⚠️ LƯU Ý
• Nội dung không phù hợp cho trẻ em.
• Nội dung mang tính giáo dục, phân tích dưới góc nhìn tâm lý học tội phạm;
  không thay thế tư vấn y khoa, tâm lý hay pháp lý.
• Thông tin dựa trên tư liệu công khai (hồ sơ tòa án, báo chí) — xem nguồn bên dưới.
  Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Các nhân vật Cú, Sói, Cáo, Cừu, Mèo là nhân vật minh hoạ, không phải người thật.
  Lời của Điều tra viên, Chuyên gia và Người dân là lời dựng lại dựa trên tư liệu.
• Giọng đọc, hình ảnh và âm nhạc được tạo cho kênh bằng công cụ AI.

📚 NGUỒN THAM KHẢO
{danh sách từ nguon_tham_khao.md}

🆘 Nếu bạn biết một trẻ em đang bị bạo hành, hãy gọi Tổng đài quốc gia
bảo vệ trẻ em 111 (Việt Nam, miễn phí, 24/7).
```

### 9.2 Pháp lý và bản quyền — hồ sơ nguồn gốc

**Nguyên tắc:** video chỉ chứa thứ **kênh tự tạo** hoặc **có giấy phép rõ ràng**. Mỗi tài sản ghi một dòng vào `provenance.json` ngay lúc tạo:

```json
{"file":"assets/bgm/bgm_music_box.mp3", "loai":"nhạc",
 "cong_cu":"connector batch_text_to_music (MiniMax)", "ngay":"2026-10-21",
 "prompt":"<prompt đã dùng>", "seed":null,
 "dieu_khoan":"<link điều khoản dùng thương mại của nhà cung cấp>",
 "kiem_tra_thuong_mai":"chưa"}
```

| Nhóm tài sản | Nguồn | Việc cần làm trước khi đăng |
|---|---|---|
| Nhạc nền (9 file `assets/bgm/`) | AI (MiniMax) | Ghi lại prompt; kiểm tra điều khoản thương mại. Nếu YouTube báo trùng Content ID với bản nhạc khác → dùng hồ sơ này để **kháng nghị** |
| Giọng đọc | AI (MiniMax) | Kiểm tra điều khoản dùng giọng hệ thống cho nội dung kiếm tiền |
| 5 linh thú, bóng người, nền 16:9 | AI (connector / Pollinations / FastSD) | **Không watermark**; ghi prompt + seed; kiểm tra điều khoản từng dịch vụ |
| Logo, chữ, sơ đồ, thẻ, cờ, dòng thời gian | Pillow (kênh tự vẽ) | Không cần thêm |
| Font Segoe UI, Georgia, Consolas, Bahnschrift | Đi kèm Windows | Dùng để tạo hình trong video thường được chấp nhận, nhưng **phương án sạch nhất** là đổi sang font giấy phép mở SIL OFL có đủ dấu tiếng Việt: *Be Vietnam Pro* (thay Segoe), *Noto Serif* (thay Georgia), *JetBrains Mono* (thay Consolas) — tải miễn phí, ghi vào `provenance.json` |
| SFX "Tách" | ffmpeg (kênh tự tạo) | Không cần thêm |
| **Cấm dùng** | Ảnh báo chí, ảnh gia đình, cảnh phim tài liệu khác, nhạc có bản quyền, logo thương hiệu | `qc.py` từ chối file nào không có dòng `provenance` |

### 9.3 Nguồn cho dữ kiện và các câu nên rà lại

AI lập `nguon_tham_khao.md`: mỗi dữ kiện quan trọng (ngày tháng, con số, câu trích, chẩn đoán) gắn **một nguồn công khai có link**. Link phải mở được (`qc.py` kiểm tra). **Không bịa nguồn**; dữ kiện không tìm được nguồn thì **báo người dùng**, không tự sửa kịch bản (V3).

Các câu dưới đây nói về **người thật** và mang tính cáo buộc hoặc trích lời. Kịch bản giữ nguyên, nhưng **bắt buộc có nguồn** trước khi đăng; người dùng cân nhắc thêm cụm ghi nguồn như *"theo hồ sơ phiên tòa"*, *"theo lời kể của Gypsy"*:

| Câu | Nội dung | Vì sao cần rà |
|---|---|---|
| `4.15#2` | Godejohn "có tiền sử rối loạn phổ tự kỷ và nhân cách bất ổn" | Thông tin sức khoẻ của **người còn sống** |
| `5.02#3` | Ông Dan Patterson "đã thừa nhận rằng…" | Thuật lại lời của **một người thật, có tên** — phải khớp nguồn |
| `5.04#2` | Câu nói của Gypsy trong trại giam | Trích dẫn trực tiếp (bản dịch) lời **người còn sống** — ghi rõ "lời dịch" trong nguồn |
| `2.07#10` | Ghi chú năm 2007 của Tiến sĩ Flasterstein | Trích hồ sơ y tế của **người thật** |
| `3.05#5`, `3.07#2` | "Thói tắt mắt", "bị nghi có những hành vi gây hại cho người thân" | Cáo buộc từ phía gia đình — bản v2 đã bỏ chi tiết cụ thể, vẫn cần nguồn |
| `4.07#8`, `4.10#5` | "Hình phạt nghiêm khắc", "phá hỏng chiếc máy tính" | Bản v2 đã khái quát hoá; chủ yếu từ lời kể của Gypsy — nên ghi nguồn lời kể |
| `1.11`, `2.07`, `4.10` (toàn lượt Điều tra viên) | "Chúng tôi phát lệnh truy tìm…" | Lời dựng lại — đã có nhãn V6; nội dung vẫn phải khớp tư liệu |

---

## 10. RỦI RO

| # | Rủi ro | Xử lý |
|---|---|---|
| 1 | **Linh thú làm nhẹ tính nghiêm trọng** của vụ bạo hành trẻ em có thật | Biểu cảm nghiêm (checklist 5.4) · linh thú chỉ ở góc ≤ 20% khung (V7) · tắt bán thân `⊘` ở mọi khoảnh khắc nặng nề nhất (`1-10`, `3-19`, `4-32`, `5-06`, `5-16`) |
| 2 | Ảnh AI có watermark / điều khoản thương mại không rõ | Tạo lại không watermark; kiểm tra điều khoản trước M3; không tự xoá watermark |
| 3 | Năm linh thú lệch phong cách nhau | Cùng prompt master + seed; checklist "đặt cạnh nhau" |
| 4 | AI vẽ chữ lạ vào nền | Prompt `no text`; AI tự soát (8.4); chữ chỉ do Pillow vẽ |
| 5 | Nền AI độ phân giải thấp, mờ khi zoom | Phóng Lanczos + làm nét; zoom tối đa 1,10 |
| 6 | Người xem tưởng Điều tra viên / Chuyên gia là người thật | V6 + dàn khách mời cuối tập + mô tả |
| 7 | Năm giọng nghe giống nhau | B0a đo F0, tốc độ; nghe thử ở M0 |
| 8 | Thời lượng ~20 phút, ngắn hơn dự kiến 25–27 | Báo người dùng; muốn dài phải thêm lời |
| 9 | **Intro 22,4 s đặt trước phần mồi** → người xem có thể thoát trước khi nghe lời đầu tiên | Giữ theo yêu cầu. Theo dõi tỉ lệ giữ chân ở giây 30 sau khi đăng; nếu thấp, phương án B là đưa intro ra **sau** shot `1-02` (dòng trạng thái trên mạng xã hội) — chỉ cần đổi thứ tự ghép, không render lại |
| 10 | Nhạc AI bị YouTube nhận nhầm là trùng bản nhạc khác (Content ID) | Hồ sơ `provenance.json` để kháng nghị; nếu cần, tạo lại music box với prompt khác |
| 11 | Lời miễn trừ bị hiểu là "lá chắn pháp lý" | Đã ghi rõ giới hạn ở mục 5.11; bảo vệ thật là mục 9.2 + 9.3 |

---

## PHỤ LỤC A — CẤU TRÚC KỊCH BẢN (`parse_kichban.py` trên `kichban_tap01_22102026_v2.md`, 22/10/2026)

B1 phải sinh ra **đúng bảng này**; khác là dừng và báo.

| Mã | Vai / loại | Câu | Từ | Chỉ dẫn / mô tả |
|---|---|---:|---:|---|
| `1.01` | *BGM* | — | — | Hộp nhạc lên dây cót, bị drone bóp nghẹt |
| `1.02` | *SFX* | — | — | Còi cảnh sát xa, gõ cửa dồn dập |
| `1.03` | Cú · Host | 3 | 70 | Chậm, trầm, giữ khoảng cách khách quan |
| `1.04` | *Nghỉ 2,0 s* | — | — | |
| `1.05` | Cú · Host | 2 | 66 | (kế thừa) |
| `1.06` | *SFX* | — | — | Băng ghi âm "Tách" |
| `1.07` | **Cừu · N1** | 3 | 105 | Xúc động, chân thật như trả lời phỏng vấn |
| `1.08` | Cú · Host | 6 | 151 | Đẩy nhanh nhịp độ |
| `1.09` | *Nghỉ 2,0 s* | — | — | Nhạc dừng đột ngột (giữ drone −40 dB) |
| `1.10` | *SFX* | — | — | Bộ đàm rè, mở cửa phòng thẩm vấn |
| `1.11` | **Sói · Điều tra viên** | 8 | 143 | Hạ trầm, sắc lạnh, dứt khoát |
| `1.12` | *SFX* | — | — | "Tách", cello vào |
| `1.13` | Cú · Host | 2 | 60 | — |
| `2.01` | *BGM* | — | — | Máy đo nhịp tim + piano |
| `2.02` | Cú · Host | 3 | 68 | Đều đặn, dẫn dắt |
| `2.03` | *SFX* | — | — | Lật giấy hồ sơ |
| `2.04` | Cú · Host | 5 | 131 | (kế thừa) |
| `2.05` | *Nghỉ 1,5 s* | — | — | |
| `2.06` | Cú · Host | 3 | 57 | (kế thừa) |
| `2.07` | **Sói · Điều tra viên** | 10 | 348 | Đanh thép, nhấn từng chứng cứ |
| `2.08` | *SFX* | — | — | Khoá cửa sắt "Cạch" |
| `2.09` | Cú · Host | 4 | 91 | Trầm lắng |
| `3.01` | *BGM* | — | — | Ambient sâu, học thuật |
| `3.02` | Cú · Host | 5 | 159 | — |
| `3.03` | *Nghỉ 2,0 s* | — | — | |
| `3.04` | Cú · Host | 2 | 43 | — |
| `3.05` | **Cáo · Chuyên gia** | 9 | 239 | Phân tích chuyên môn, rõ ràng |
| `3.06` | *Nghỉ 1,5 s* | — | — | |
| `3.07` | Cú · Host | 2 | 69 | — |
| `3.08` | **Cáo · Chuyên gia** | 6 | 147 | Hạ giọng trầm, chậm rãi hơn |
| `3.09` | *Nghỉ 2,0 s* | — | — | |
| `3.10` | **Cáo · Chuyên gia** | 6 | 122 | (kế thừa) |
| `4.01` | *BGM* | — | — | Nhịp tim chậm + violin |
| `4.02` | Cú · Host | 2 | 55 | Trăn trở |
| `4.03` | **Mèo · N2** | 3 | 74 | Băn khoăn, hoài nghi |
| `4.04` | *Nghỉ 2,0 s* | — | — | |
| `4.05` | Cú · Host | 2 | 72 | — |
| `4.06` | *SFX* | — | — | Xiềng xích, kim loại |
| `4.07` | **Cáo · Chuyên gia** | 8 | 207 | — |
| `4.08` | *Nghỉ 1,5 s* | — | — | |
| `4.09` | Cú · Host | 3 | 61 | — |
| `4.10` | **Sói · Điều tra viên** | 5 | 135 | Trầm, thuật lại hồ sơ |
| `4.11` | *Nghỉ 2,0 s* | — | — | Host lắng xuống |
| `4.12` | Cú · Host | 2 | 66 | — |
| `4.13` | **Cáo · Chuyên gia** | 3 | 70 | — |
| `4.14` | *SFX* | — | — | Bàn phím gõ trong đêm |
| `4.15` | Cú · Host | 5 | 116 | — |
| `5.01` | *BGM* | — | — | Búa tòa án → piano ấm |
| `5.02` | Cú · Host | 3 | 116 | Điềm đạm, tổng kết |
| `5.03` | *Nghỉ 1,5 s* | — | — | |
| `5.04` | Cú · Host | 3 | 107 | (kế thừa) |
| `5.05` | *Nghỉ 2,0 s* | — | — | |
| `5.06` | Cú · Host | 1 | 60 | (kế thừa) |
| `5.07` | **Cáo · Chuyên gia** | 2 | 77 | Nhấn mạnh từng ý, góc lâm sàng |
| `5.08` | **Sói · Điều tra viên** | 2 | 82 | Tiếp lời, góc hành vi xã hội |
| `5.09` | *Nghỉ 2,5 s* | — | — | Piano dâng nhẹ |
| `5.10` | Cú · Host | 3 | 114 | Trầm ấm, truyền cảm |
| `5.11` | *Nghỉ 1,5 s* | — | — | |
| `5.12` | Cú · Host | 2 | 64 | (kế thừa) |
| `5.13` | *SFX* | — | — | Gấp hồ sơ "Bụp", tắt máy ghi âm "Tách" |
| `5.14` | *BGM* | — | — | Piano ngân 5 s rồi tắt |
| | **Tổng** | **128** | **3.545** | |

---

## PHỤ LỤC B — 23 CHỖ GIẢM BẠO LỰC (`kichban_tap01_22102026.md` → `_v2.md`)

Nguyên tắc: **giữ dữ kiện và luận điểm tâm lý, bỏ chi tiết thể xác**. Không thêm dữ kiện mới. Số câu và mã câu không đổi.

| Câu | Bản gốc | Bản v2 |
|---|---|---|
| `1.03#3` | …khiến cả khu phố chết lặng: *"Con khốn đó chết rồi."* | …một dòng trạng thái ngắn ngủi, đầy hằn học, thông báo rằng bà Dee Dee đã qua đời – khiến cả khu phố chết lặng |
| `1.08#1` | họ tìm thấy thi thể của người mẹ… | họ phát hiện người mẹ… đã qua đời trong phòng ngủ |
| `1.08#5` | Kẻ máu lạnh nào đã sát hại người mẹ tận tụy ấy, rồi bắt cóc… | Ai đã gây ra cái chết của người mẹ tận tụy ấy, rồi đưa đi… |
| `1.11#8` | kế hoạch đoạt mạng bà mẹ "thánh thiện" | kế hoạch dẫn đến cái chết của bà mẹ "thánh thiện" |
| `2.02#1` | chọn cách kết liễu mẹ ruột | đi đến một lựa chọn cực đoan với chính mẹ ruột |
| `2.02#2` | căn phòng ngủ đẫm máu | căn phòng ngủ |
| `2.07#1` | trực tiếp hủy hoại cơ thể con gái | trực tiếp tác động lên sức khỏe con gái |
| `2.07#2` | hàm răng bị mục ruỗng và phải nhổ bỏ toàn bộ răng cửa | sức khỏe răng miệng của cô bé bị tổn hại nghiêm trọng |
| `2.07#3` | phẫu thuật đặt ống truyền thức ăn trực tiếp qua thành bụng vào dạ dày | đặt ống nuôi ăn qua dạ dày |
| `2.07#4` | bôi thuốc gây tê vào nướu để nước bọt chảy ròng ròng… cắt bỏ tuyến nước bọt | tạo ra những triệu chứng giả trước mắt bác sĩ… một ca phẫu thuật tuyến nước bọt không cần thiết |
| `3.02#2` | biến đứa con… thành một phế nhân đau đớn | khiến đứa con… phải sống như một người bệnh |
| `3.07#2` | bị nghi bỏ thuốc diệt cỏ vào thức ăn của mẹ kế và bỏ đói mẹ ruột… | bị nghi có những hành vi gây hại cho chính người thân trong gia đình |
| `3.08#5` | Hãy làm cho con bé tàn tật và phụ thuộc hoàn toàn vào mình | Hãy khiến con bé tin rằng mình bệnh tật và phụ thuộc hoàn toàn vào mẹ |
| `3.08#6` | không thể tự ăn uống mà phải truyền qua ống thông dạ dày… vị Chúa tể duy nhất nắm giữ sự sống | tin rằng mình… không thể tự chăm sóc bản thân… người duy nhất nắm giữ cuộc sống |
| `3.10#6` | yếu ớt, vô tính và… | yếu ớt và… |
| `4.07#2` | chịu đựng sự đau đớn lặp đi lặp lại | chịu đựng những áp lực tiêu cực lặp đi lặp lại |
| `4.07#7` | siết chặt lại đến mức bầm tím | siết chặt lại như một lời cảnh cáo không thành tiếng |
| `4.07#8` | những trận đòn bằng móc áo, bị bỏ đói và bị trói vào thành giường suốt hai tuần | những hình phạt nghiêm khắc và sự kiểm soát ngột ngạt |
| `4.10#5` | dùng búa đập nát chiếc máy tính… đe doạ đập nát các ngón tay | phá hỏng chiếc máy tính… cảnh cáo cô không bao giờ được bước ra khỏi cửa |
| `4.13#2` | người đầu độc Gypsy | người gây ra bệnh tật cho Gypsy |
| `4.13#3` | bạo hành thể xác | kiểm soát hà khắc |
| `5.02#2` | lên kế hoạch sát hại mẹ ruột | lên kế hoạch dẫn đến cái chết của mẹ ruột |
| `5.02#3` | bạo hành y khoa | lạm dụng y khoa |
| `5.08#1` | thủ thuật y khoa đau đớn | thủ thuật y khoa xâm lấn |

**Giữ nguyên có chủ đích:** "ung thư máu" (tên bệnh) · "giết người cấp độ hai" ở `5.04#1` (tên tội danh trong bản án — đổi sẽ sai sự thật) · "cạo trọc đầu", "váy công chúa" ở `2.04#5`, `3.10#2` (cốt lõi của luận điểm *tước đoạt sự trưởng thành*, không mang tính bạo lực).

---

*Không file nguồn nào bị sửa: `kichban_tap01_22102026.md`, `PhuongAn_TaoHinh_5NhanVat.md`, `Kc_1.txt`, `Kich_ban.txt`, `KeHoach_ThuAm_Tap01.md`, `KeHoach_ThuAm_Tap01_VIDEO.md` giữ nguyên.*
