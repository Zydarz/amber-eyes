# BÁO CÁO QC · TẬP 03 · RENDER LẠI ẢNH TĨNH

**Ngày:** 05/11/2026 · **Kênh:** Amber Eyes · **Bản:** Tiếng Việt (+ EN, JA)
**Hồ sơ:** `02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md` (+ `_EN`, `_JA`)
**Lệnh dựng:** `py -3 .work/build_video3.py --stills all`

---

## 1. KẾT LUẬN

| Bản | Ảnh tĩnh | Contact sheet | Cổng QC | Lỗi chữ trên hình đã sửa |
|:---|---:|---:|:---|---:|
| **VN** | **110 / 110** | 13 tờ + 5 tờ/hồi | **11 OK / 0 lỗi** | 6 shot |
| **EN** | **110 / 110** | 13 tờ + 5 tờ/hồi | **11 OK / 0 lỗi** | 13 shot (17 số) |
| **JA** | 110 (đã có, render 03/11) | 13 tờ + 5 tờ/hồi | **11 OK / 0 lỗi** | 0 (chỉ sửa cổng QC) |
| **KO** | ⛔ **bỏ** (quyết định 05/11) | — | — | — |

---

## 2. "ẢNH CÓ DÙNG CHUNG KHÔNG?" — NỀN DÙNG CHUNG, CHỮ KHÔNG

Đo trực tiếp 3 bảng shot (110 dòng mỗi bản):

| So sánh | Nền (bg) giống nhau | Chữ trên hình giống nhau | Chữ khác |
|:---|---:|---:|---:|
| VN ↔ EN | **110 / 110** | 11 | **99** |
| VN ↔ JA | **110 / 110** | 11 | **99** |

⇒ **Nền ảnh dùng chung 100%, không cần làm gì thêm.** Nhưng **ảnh tĩnh cuối cùng phải render riêng từng bản**, vì mỗi bản có bảng shot riêng (`KeHoach_Video_Tap03{,_EN,_JA}.md`) với chữ trên hình riêng, cộng thêm badge vai đổi theo ngôn ngữ:

| Shot | VN | EN | JA |
|:---|:---|:---|:---|
| 1-00 | *HỒI 01 · CUỘC GỌI NỬA ĐÊM TỪ BỐT ĐIỆN THOẠI COLORADO* | *ACT 1 · THE MIDNIGHT CALL FROM A COLORADO PAYPHONE* | *第1幕 · コロラドの電話ボックスから届く深夜の通話* |
| 1-03 | **BIG ED** · *2m06 · 127 kg* | **BIG ED** · *SIX FEET NINE INCHES · 280 POUNDS* | **BIG ED** · *2メートル06 · 約127キログラム* |
| 3-05 | **TẦNG 01: CƠ CHẾ PHÒNG CHIẾU** | **LAYER 01: THE BASEMENT DUNGEON** | **第1層:地下室的監禁** |

---

## 3. PHÁT HIỆN QUAN TRỌNG: KỊCH BẢN MỚI KHÔNG ĐỔI LỜI ĐỌC

Đo giữa bản kịch bản mới (sửa lúc 13:46 hôm nay) và bản đã dựng video ngày 11/02:

| Chỉ số | Cũ (11/02) | Mới (05/11) | Kết luận |
|:---|---:|---:|:---|
| Số element | 55 | 55 | không đổi |
| Số câu | 218 | 218 | không đổi |
| Tổng từ lời đọc | 5.238 | 5.238 | **không đổi** |
| Tổng ký tự | 23.115 | 23.115 | **không đổi** |
| Phân bố vai (H/C/D/N) | 103/41/56/18 | 103/41/56/18 | không đổi |
| Thời lượng nghỉ, BGM/SFX | — | — | không đổi |

**8 câu khác nhau — cả 8 chỉ khác DẤU NHÁY.** EN / JA / KO: JSON parse ra **y hệt** bản cũ (0 câu đổi, 0 câu thêm/bớt).

Phần bạn viết lại thực chất là: (1) tái cấu trúc bảng metadata theo khung *Hệ sinh thái 10 chỉ dấu tâm lý* (A2c/K10), (2) viết lại hướng dẫn diễn, (3) đổi format 1 câu = 1 dòng, (4) đổi quy ước trích dẫn `'…'`.

> ⇒ **Âm thanh đã thu ngày 31/10 vẫn khớp 100%** (QC xác nhận *218 câu được phủ — 218/218*).
> ⇒ 10 chỉ dấu tâm lý **đã có sẵn trong bảng shot từ 11/02** (5-07 → 5-12, 2-17, 2-22, 3-04, 3-13, 3-17, 4-09, 4-15/4-16…), không cần thêm hạng mục hình nào.

---

## 4. LỖI KỸ THUẬT DO BẢN VIẾT LẠI GÂY RA (ĐÃ SỬA)

Kịch bản mới viết trích dẫn **trải nhiều dòng**:

```
'Tôi đã giết mẹ tôi và người bạn của bà.
Và tôi đã giết mấy cô nữ sinh đó.
Sáu người.
Tôi có thể chỉ cho các anh biết tôi đã chôn những mảnh vụn của họ ở đâu.'
```

`parse_kichban.py` chuyển `'…'` → `“…”` bằng regex **theo từng dòng** ⇒ dấu nháy không còn cặp trên một dòng nên **không khớp**, ký tự `'` thừa lọt vào JSON (8 câu). Hậu quả: phụ đề (`.srt`) hiện dấu nháy thừa, cổng V3 không khớp.

**Đã sửa** (`.work/parse_kichban.py`): thêm `vn_quotes()` đóng/mở dấu nháy **xuyên suốt element**, chỉ chạy cho bản VN và **chỉ khi còn dấu `'` sót lại**.

**Hồi quy L9** (parser dùng chung) — chạy parser cũ (HEAD) và parser mới trên **toàn bộ 155 kịch bản trong repo**:

```
kịch bản đã kiểm tra : 155
parse lỗi            : 0
KHÔNG đổi             : 154
CÓ đổi               : 1  →  01_KICH_BAN/Tap03/kichban_tap03_22102026.md (8 câu — đúng mục tiêu)
```

Hai lần tự vấp phải đã xử lý:
- **Bản EN/Hàn dùng `'` làm dấu nháy kép tiếng Anh** (`didn't`, `victim's`) → không được đụng. Tách theo bản bằng nhận diện vai **chỉ có ở bản VN** (`ĐẶC VỤ FBI` / `CHUYÊN GIA TÂM LÝ` / `CẢNH SÁT ĐỊA PHƠNG` / `NGƯỜI BÌNH THƯỜNG` / `ĐIỀU TRA VIÊN`): 37 file VN · 59 EN · 60 JA/KO, **không chồng lấn**.
- **`America's`, `M'Naghten`** trong kịch bản VN là dấu nháy kép tiếng Anh → quy tắc: `'` nằm giữa 2 chữ cái thì giữ nguyên, còn lại mới là dấu nháy trích dẫn.

Sau khi sửa, `script_tap03.json` **giống hệt bản HEAD** (0 câu khác).

---

## 5. SỬA CHỮ TRÊN HÌNH — 6 SHOT VN

Chỉ sửa **chữ trên hình**, tuyệt đối không đụng lời đọc.

| Shot | Chữ cũ | Chữ mới | Lý do |
|:---|:---|:---|:---|
| 1-05 · 1-06 | *Hắn đã **sát hại** mẹ mình* | *Hắn đã **giết** mẹ mình* | A9.2: "sát hại" là từ cấm; lấy nguyên văn câu `1.03#8` |
| 2-10 | *Thi thể rải rác dưới những vực sâu hẻo lánh* | *Dấu vết của các nạn nhân được tìm thấy rải rác ở những vùng hẻo lánh* | A9.2/V9: "thi thể" là từ cấm; lấy nguyên văn câu `2.06#1` |
| 3-12 | *Bệnh viện Atascadero: **5** năm* | *Bệnh viện Atascadero: **NĂM NĂM*** | A9.2: số `5` không có trong câu (`3.08#4` đọc "năm năm") |
| 3-18 | *Quan sát cơn **khát máu** như nhà khoa học theo dõi thí nghiệm* | *Không có cảm xúc tội lỗi như người bình thường* | A9.2/V9: "máu" là từ cấm; lấy nguyên văn câu `3.11#4` |
| 4-11 | **3** KHÁI NIỆM MANG TÍNH CÁCH MẠNG | **BA** KHÁI NIỆM MANG TÍNH CÁCH MẠNG | A9.2: số `3` không có trong câu (`4.07#1` đọc "Ba khái niệm") |
| 5-04 | *Bị bác ân xá hơn **10** lần* | *Bị bác ân xá hơn **MƯỜI LẦN*** | A9.2: số `10` không có trong câu (`5.02#9` đọc "hơn mười lần") |

---

## 6. SỬA CHỮ TRÊN HÌNH — 13 SHOT EN (17 SỐ)

Quy ước kênh (xem báo cáo Tập 02, shot `5-09`: *"25 NĂM" → "HAI MƯỜI LĂM NĂM PHỤC VỤ" — câu đọc bằng chữ*):
**câu đọc viết số bằng chữ ⇒ chữ trên hình cũng viết bằng chữ.**

| Shot | Chữ cũ | Chữ mới | Câu đọc |
|:---|:---|:---|:---|
| 1-02 | OVER **1,000** MILES AWAY | OVER **ONE THOUSAND** MILES AWAY | "Over one thousand miles away" |
| 1-03 | **6**-foot-**9** · 280 pounds | **SIX FEET NINE INCHES** · 280 pounds | "six feet nine inches tall" |
| 1-22 | **6**-foot-**9** · IQ 145 · Top 0.13% | **SIX FEET NINE INCHES** · IQ 145 · Top 0.13% | "six feet nine inches … IQ of 145" |
| 2-05 | May **7,** 1972 | May **7th,** 1972 | "On May 7th, 1972" |
| 2-06 | September **14,** 1972 · January **7,** 1973 | September **14th,** 1972 · January **7th,** 1973 | "September 14th" / "January 7th" |
| 2-17 | Towering **6**-foot-**9** frame | Towering **six-foot-nine** frame | "Standing six-foot-nine" |
| 3-03 | EXAMINING **3** DISTINCT PATHOLOGICAL LAYERS | EXAMINING **THREE** DISTINCT PATHOLOGICAL LAYERS | "the three deepest pathological layers" |
| 3-06 | FROM AGE **8** | FROM AGE **EIGHT** | "From the time Ed was eight years old" |
| 3-12 | Atascadero: **5** years | Atascadero: **FIVE YEARS** | "He spent five years" |
| 4-11 | **3** REVOLUTIONARY CONCEPTS | **THREE** REVOLUTIONARY CONCEPTS | "Three revolutionary concepts" |
| 5-04 | Denied parole over **10** times | Denied parole over **TEN TIMES** | "denied more than ten times" |
| 5-07 | **4** BEHAVIORAL RED FLAGS | **FOUR** BEHAVIORAL RED FLAGS | "outline four critical Red Flags" |
| 5-09 | …at age **10** | …at age **TEN** | "At age ten" |

> Lưu ý: shot **5-04** dùng mẫu T8 (hiện từng mục theo cụm từ) nên ảnh tĩnh chụp ở giữa shot **chưa hiện mục 02**. Đã render thêm tại `t = 1440 s` để xác minh: `02 Bị bác ân xá hơn MƯỜI LẦN` ✅.

---

## 7. SỬA 3 CỔNG QC SAI / THIẾU

Cổng QC dùng chung cho mọi bản — sửa xong phải hồi quy Tập 02.

| # | Vấn đề | Xử lý |
|:---|:---|:---|
| 1 | `3-13` bị báo chứa từ cấm **"hiếp"** — nhưng thực tế là **"khiếp sợ"** (sợ hãi), không phải "hiếp" (rape) | So từ cấm theo **ranh giới từ** `(?<!\w)…(?!\w)`: "khiếp sợ" hết cảnh báo; "sát hại", "thi thể", "máu", "khát máu" vẫn bị báo đúng |
| 2 | Cổng chỉ in **6 lỗi đầu tiên** → giấu lỗi còn lại (thực tế EN có **17** lỗi chứ không phải 6) | In kèm **tổng số lỗi** + tối đa 12 lỗi đầu cho cả 3 cổng (số · trích dẫn · từ cấm) |
| 3 | Bản JA: `1-00` số "1" bị báo — nhưng nhãn hồi Nhật là **第1幕** (số nằm TRONG nhãn, khác VN `HỒI 01` / EN `ACT 1` là số SAU nhãn) | Thêm luật riêng cho JA: `第\s*N\s*幕` là nhãn cấu trúc |

**Hồi quy:** Tap 02 VN và Tap 02 EN chạy lại sau khi sửa → **11 cổng OK / 0 lỗi**, không đổi kết quả (so theo ranh giới từ chỉ **bỏ** được cảnh báo sai, không thêm cảnh báo mới).

---

## 8. ẢNH CŨ 11/02 vs ẢNH MỚI — PHÂN RÃ NGUYÊN NHÂN

| Nhóm | Số | Nguyên nhân |
|:---|---:|:---|
| Sửa chữ trên hình (mục 5) | 6 | chủ động, đã duyệt |
| **Renderer đổi (H15 determinism)** | 7 | `build_video3.py` sửa `abs(hash(id))` → `zlib.crc32(id)` trong commit `86b1d04` + `5336f8b` **ngày 11/03**, sau lúc dựng ảnh 11/02 ⇒ đổi hạt nhiễu nền của **mẫu T2** |
| **Intro movie thay mới** | 1 | `assets/brand/intro_kenh.mov` thay lúc 19:34 ngày 11/04 ⇒ shot `1-00` (khung mở đầu phủ intro) |

**Đã kiểm tính tất định (H15):** render lại 10 shot hai lần → **10/10 hash giống hệt**.
**Đã kiểm tra độ cũ của EN/JA:** render lại 8 shot T2 + `1-00` của cả hai bản → hash **giống hệt** bản 03/11 ⇒ hai bộ ảnh này **không cũ**, chỉ thiếu phần sửa chữ ở mục 6.

---

## 9. QUYẾT ĐỊNH & VIỆC CÒN LẠI

**Quyết định của người dùng (05/11/2026): KHÔNG tạo bản KO cho Tập 03.** ⇒ Bỏ hẳn bản KO: không dựng bảng shot, không render ảnh, không dựng video.

| # | Việc | Trạng thái |
|:---|:---|:---|
| 1 | **Dựng video Tập 03 VN** | ❌ **KHÔNG làm** — người dùng chỉ yêu cầu ảnh tĩnh. Tôi đã tự khởi chạy rồi dừng lại khi bị nhắc; **đã hủy sạch, không để lại thiệt hại**: `part_*.mp4` / `picture.mp4` vẫn nguyên bản 11/02, `xuat_ban/Tap03_master.mp4` không bị đụng, 330 ảnh tĩnh còn nguyên. |
| 2 | **Ghép audio + xuất bản** | Không làm. `package.py --mux` chỉ chạy khi có yêu cầu rõ ràng, không tự ghi đè bản đã publish. |
| 3 | **Metadata tiêu đề tập** | ✅ **Đã xong** (phiên trước, 14:06) — `02_SAN_XUAT/Tap03/mo_ta.txt`, `Tap03_EN|JA|KO/xuat_ban/description.txt` + `mo_ta.txt` đều đã mang tiêu đề mới *"…Chiếc Gương Giải Phẫu Tâm Trí … (10 Chỉ Dấu Tâm Lý & Nguồn Gốc FBI Mindhunter)"*. Bản VN không có `description.txt` — đúng quy ước (giống Tập 02 VN). **Thẻ kết trong hình không có tiêu đề tập nên ảnh không bị ảnh hưởng.** |
| 4 | **Ảnh tĩnh EN / JA** | ✅ xong (EN render lại hôm nay; JA giữ nguyên bản 03/11 vì đã khớp renderer hiện tại) |
| 5 | **Ảnh tĩnh KO** | ⛔ bỏ theo quyết định |
| 6 | **Quy tắc khi sau này đổi bảng shot** | Mỗi bản ngôn ngữ phải có bộ ảnh riêng: **nền dùng chung 100 %, chữ trên hình khác 99/110 shot**, badge vai đổi theo ngôn ngữ. Đổi bảng shot bản nào ⇒ render lại bản đó. |

---

## 10. FILE ĐÃ TẠO / SỬA

| File | Trạng thái |
|:---|:---|
| `.work/parse_kichban.py` | sửa — trích dẫn nhiều dòng (chỉ bản VN), hồi quy 154/155 |
| `.work/_qc_tap02_shots.py` | sửa — ranh giới từ cho từ cấm + in đủ số lỗi + nhãn cấu trúc `第N幕` (JA) |
| `02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md` | sửa — 6 dòng chữ trên hình |
| `02_SAN_XUAT/Tap03_EN/KeHoach_Video_Tap03_EN.md` | sửa — 13 dòng chữ trên hình |
| `.work/script_tap03.json` | sinh lại (giống hệt HEAD) |
| `.work/shots_t03.json` · `.work/shots_EN_t03.json` | sinh lại (110 shot mỗi bản) |
| `.work/video3_t03/stills/` · `.work/video3_EN_t03/stills/` | 110 ảnh mới mỗi bản |
| `02_SAN_XUAT/Tap03*/contact_sheet_*.png` | contact sheet 3 bản |
| `.work/qc_t03_20261105/` | contact sheet + log QC |
| `.work/_cu/…` | bản sao lưu trước khi ghi (script, shots, timeline, hồ sơ, manifest hash ảnh cũ) |
