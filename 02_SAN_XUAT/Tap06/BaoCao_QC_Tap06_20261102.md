# BÁO CÁO GIÁM SÁT CHẤT LƯỢNG — TẬP 06 · 02/11/2026

**Thẩm phẩm:** `02_SAN_XUAT/Tap06/xuat_ban/Tap06_master.mp4`
**Nguyên nhân dựng lại:** đổi giọng từ **bộ A** (giọng `English_*`/`Korean_*` đọc tiếng Việt) sang **giọng tiếng Việt Higgs Audio v3** ⇒ âm thanh đổi hoàn toàn ⇒ phải dựng lại hình (A11 #55, H14).

---

## 1. Số đo thật (không ước lượng)

| Mục | Giá trị | Chuẩn | Kết quả |
|---|---|---|---|
| Thời lượng mp4 cuối | **1265,400 s** (21:05) | — | — |
| Thời lượng audio master | 1265,409979 s | khớp ±0,05 s | ✅ lệch 0,010 s |
| `timeline.total` | 1265,41 s | khớp ±0,05 s | ✅ lệch 0,010 s |
| `picture.mp4` (trước khi ghép) | 1265,400 s | khớp `timeline.total` ±0,05 s | ✅ **H14 đạt** |
| LUFS — master mp3 | **−16,2 LUFS** | −16 ± 1 | ✅ |
| LUFS — mp4 cuối | **−16,0 LUFS** | −16 ± 1 | ✅ |
| True peak — master mp3 | −1,6 dBFS | ≤ −1,5 | ✅ |
| True peak — mp4 cuối | **−1,8 dBTP** | ≤ −1,5 | ✅ |
| Khoảng lặng > 0,3 s @ −60 dB | **0** (master và mp4 cuối) | 0 | ✅ |
| Lời đầu tiên | **23,011 s** | 22,8 – 23,5 s | ✅ |
| **Lệch âm thanh – hình** | **0,0 ms** (tương quan 1,0000) | 0 | ✅ (A11 #64) |
| Giải mã toàn file | **0 lỗi** | 0 | ✅ |
| Video | h264 · 1920×1080 · 30/1 · 3,04 Mbps | H.264 1080p30 | ✅ |
| Audio | AAC · 48 000 Hz · 2 kênh | AAC | ✅ |
| Dung lượng | 458,2 MB | — | — |
| Phụ đề | 324 cue · UTF-8 không BOM | phủ 100% lời thoại | ✅ |
| Thẻ kết (giữa shot cuối, 1257,3 s) | 10,62 % pixel sáng | có chữ | ✅ |
| Shot cuối | `5-14` — thẻ kết, không gắn câu | H12 | ✅ |

**Kết luận cổng QC A–G: 23 OK · 2 cảnh báo · 0 lỗi.**

---

## 2. Bảng shot — viết lại từ đầu theo nội dung câu

Bảng shot mục 6 vẫn trỏ mã câu của bản **165 câu** cũ trong khi kịch bản đã tách còn **154 câu**. `parse_shots.py` **không báo lỗi** vì mã cũ vẫn là chuỗi hợp lệ — nhưng nội dung hình đã sai. Đã map **cũ → mới theo diff nội dung câu** (đọc bản gốc ở commit `f3b5db9`), không đoán số thứ tự.

**11 element đổi số câu:** `1.06` 8→7 · `1.08` 5→6 · `1.09` 6→5 · `1.14` 3→2 · `3.05` 3→1 · `3.07` 3→2 · `3.09` 2→1 · `3.10` 5→4 · `4.08` 4→3 · `5.02` 6→4 · `5.04` 4→3.

### 2.1. Lỗi đã sửa

| Nhóm | Chi tiết |
|---|---|
| **Phủ câu** | Thêm shot `1-15` cho câu mới `1.08#6` (lời dẫn dắt về Kim Byers); xoá shot `3-04` (nội dung "hộp sáp thơm khử mùi" đã bị gỡ khỏi kịch bản); đánh lại id Hồi 1 (`1-15`→`1-23`) và Hồi 3 (`3-04`→`3-10`). Kết quả: **154/154 câu, 0 trùng** |
| **Cột Vai** | **10 dòng sai** → badge và bán thân hiện **sai người nói**: `2-02` `2-03` `2-10` (ghi H, thực là D) · `3-03` `3-06` `3-07` (ghi D, thực là H) · `3-10` (ghi H, thực là D) · `4-02` (ghi H, thực là D) · `4-03` (ghi D, thực là **N2** — Mike Albrecht) |
| **Số trên hình** | `13 · 03 · 1980` → kịch bản ghi **12**/3/1980 · bỏ `12/12/1978` (không có trong câu) · bỏ `Trại cải tạo Anamosa` (kịch bản ghi **Waterloo**) · `cao gấp hơn hai lần` → `cao gần gấp đôi` · `Cảnh báo đỏ 4/3/2/1` → `thứ tư/ba/hai/nhất` · `18 tháng` → `mười tám tháng` · `3 ngoài sân` → `3 trong khuôn viên` |
| **Câu trích** | `"MẸ ƠI, MẸ ĐỢI CON VÀI PHÚT NHÉ"` (đã gỡ khỏi kịch bản) · `"Kiss my ass"` (đã gỡ) · `"Họ bảo tôi là quái vật"` (nay là "tự truyện và các đoạn ghi âm") · 2 trích của N1/N2 viết lại theo nguyên văn câu mới |
| **Nền** | `3-04` sáp thơm khử mùi (xoá) · `4-08` "ảo thuật còng tay" (chi tiết đã bị gỡ khỏi `4.08`) → đổi nền `t6_lawyer_office_night` + tiêu đề "MÁNH KHÓE LỪA GẠT" |
| **Từ cấm A9.2** | `đòn roi` (4-05) → `bị bạo hành` |

### 2.2. Lỗi chưa từng ai phát hiện: cột handoff

Tap06 đặt mã handoff `→X` ở **cột chuyển cảnh (cột 9)** trong khi `parse_shots.py` đọc handoff từ **cột Nhân vật (cột 8)** ⇒ `flags["handoff"]` rỗng ở **0/73 shot** ⇒ badge "TIẾP THEO" (Host mời ai) **chưa bao giờ hiện** trong Tập 06 — trong khi Tap04 có 7 shot và Tap05 có 2 shot có handoff.

Đã chuyển handoff về đúng cột và **tính lại theo quy tắc** `handoff(dòng i) = vai của dòng i+1` (quy tắc này tái tạo đúng bảng gốc Tap04/Tap05). Kết quả: **18/73 shot có handoff**, đã kiểm bằng mắt trên ảnh tĩnh và trên khung trích từ chính mp4 cuối.

### 2.3. Bản chẩn

Áp `⊘` (tắt bán thân) theo đúng quy tắc B2 của hồ sơ: nắp hầm crawl space · khai quật · sông Des Plaines · buồng tử tù Menard · phòng thi hành án Stateville (`3-03`, `3-04`, `3-05`, `3-06`, `3-08`, `3-09`, `5-01`, `5-05`, `5-06`). Bảng cũ **không dòng nào** có `⊘` ở Hồi 3/5.

---

## 3. QC ảnh tĩnh (A9.3)

- Render **73/73 shot** (`.work/video3_t06/stills/`) + 5 contact sheet (16 ảnh/tờ) → soi bằng mắt toàn bộ.
- Không lỗi chữ đè nhau, không mặt người lộ, không chữ lạ do AI, mọi nền có file trong `assets/bg/`.
- Shot mới `1-15` (Tâm trạng Kim Byers) dùng nền `t6_pharmacy_counters_renovation` — đúng bối cảnh hiệu thuốc tối hôm ấy.

---

## 4. Cảnh báo (không phải lỗi)

| Cảnh báo | Giải thích |
|---|---|
| 42 shot dài > 15 s (TB 17,1 s; dài nhất 30,4 s) | Bản cũ còn tệ hơn (**54** shot > 15 s, TB 20,7 s, dài nhất 39,9 s) — giọng Higgs đọc nhanh hơn nên shot ngắn lại. Đây là quy ước của dự án (Tập 05 có 77/83 shot một tiêu đề). A7 ghi "3–15 s" nhưng không có cổng QC nào đo; đã ghi nhận để cân nhắc tách đoạn chữ ở lần sau |
| Khung tại `total − 2 s` bị đen | Renderer mờ dần 3 s cuối (dùng chung T01–T03). Thẻ kết đã kiểm ở **giữa shot cuối** (1257,3 s) → 10,62 % pixel sáng ✅ |

---

## 5. Nguồn tham khảo — đã kiểm chứng từng link (L2)

Bảng nguồn đã **điền xong**: **58 mốc dữ kiện × 20 nguồn công khai**. Không bịa link — mỗi URL đã tải thật và đo HTTP status.

| Mục | Số đo thật |
|---|---|
| Số URL ứng viên đã thử | **50** |
| HTTP 200 (dùng được) | **20** → 20 nguồn cuối cùng |
| HTTP 403 (Cloudflare/bot-block: Britannica, People, CBS, FBI.gov, NBC Chicago, eagle1023fm) | 6 → **loại**, vì không đọc được nội dung để đối chiếu |
| HTTP 404 (URL sai slug) | 7 → **loại** |
| HTTP 409 / 429 / ERR / timeout | 5 → **loại** |
| Mốc dữ kiện đối chiếu | **58** (51 `✅` · 7 `⚠`) |
| Link trong `mo_ta.txt` | 20/20 — kiểm chứng lại lúc sinh file |

**4 cổng validator chạy trước khi ghi file** (`.work/_gen_t06_sources.py` — chặn ghi nếu trượt):

1. Mọi URL phải có meta HTTP **200** trong cache `.work/_src_cache/` **và** nội dung tải về ≥ 500 byte.
2. Mọi mã câu phải tồn tại thật trong `.work/script_tap06.json` (43 element `LOI`, 154 câu).
3. Khoá nguồn phải hợp lệ **và mọi nguồn đều phải được dùng** — nguồn thừa cũng bị chặn.
4. Không trùng mã câu trong bảng.

**Mâu thuẫn đã xác minh là KHÔNG có** (nghi vấn ban đầu): nhiều nguồn ghi "13/3/1980". Hồ sơ viện chưởng viện làm rõ **ngày 12/3/1980 là phán quyết có tội**, **ngày 13/3/1980 là ngày tuyên án** ⇒ kịch bản `4.10#1` + `4.10#2` **đã đúng**, không cần sửa.

### 5.1. 7 mốc `⚠` — cần người dùng duyệt lại câu chữ

| Mã câu | Vấn đề | Nguồn nói gì |
|---|---|---|
| `1.08#1` | "cao gần gấp đôi **mức lương tối thiểu liên bang**" | Wikipedia: "almost double **the pay Piest earned at the pharmacy**" (so với lương ở hiệu thuốc, **không** phải lương tối thiểu). Báo chí: "gấp đôi mức lương tối thiểu **2,50 USD**" — đó là mức của **bang Illinois**; liên bang năm 1978 là **2,35 USD**. Câu hiện tại gộp cả hai ⇒ sai |
| `2.06#3` | "một chiếc **phù hiệu cảnh sát giả**" | Wikipedia/hồ sơ điều tra: "**several** police badges, a starting pistol, a syringe… handcuffs" — **không** nói phù hiệu là giả, và là **nhiều** chiếc |
| `2.11#2` | "**nhà hàng ăn nhanh**… **gõ cửa kính xe**… uống cà phê cùng ăn tối" | Nguồn chỉ xác nhận: mời ăn tối ở nhà hàng, mời vào nhà ấm, mua bia cho họ. **Không** có "fast food", **không** có "gõ cửa kính xe" |
| `2.11#3` | "**trả tiền bữa ăn** cho họ" | Nguồn chỉ ghi Gacy **mua bia** cho họ; không có nguồn nói Gacy trả tiền bữa ăn |
| `3.06#1` | "cao **chưa đầy một mét**" | Sách *Witnesses from the Grave* (theo hồ sơ cảnh sát): "a muddy **eighteen-inch-high** crawl space" (≈46 cm) ⇒ câu đúng nhưng thô, nên dùng "chưa đầy nửa mét" |
| `3.11#1` | "quy mô **lớn chưa từng thấy** trong lịch sử bang Illinois" | **Chưa có nguồn** xác nhận khẳng định siêu nhân này (chỉ xác nhận quy mô khai quật + việc phải tháo sàn nhà) |
| `5.02#3` | "**hàng trăm** bức tranh sơn dầu" | Hồ sơ viện chưởng viện: "more than **2,000** oil paintings"; Wikipedia: "approximately **2,500** paintings" ⇒ "hàng trăm" thấp hơn thực tế |

### 5.2. Ba điểm "đúng" nhưng nên ghi chú

| Mã câu | Nội dung | Ghi chú |
|---|---|---|
| `4.03#2` | 4 nhân cách | Nguồn: "John the contractor, John the **clown**, John the politician" + Jack Hanley. Kịch bản tách **Pogo** thành nhân cách riêng (thay cho "John the clown") — cùng số nhân cách nhưng cách gán khác |
| `5.02#1` | "nằm trong **khu biệt giam** tử tù tại Menard" | Mọi nguồn viết "**on death row**" (hàng chờ tử hình), không khẳng định "biệt giam" |
| `5.02#4` | "trong **cuốn tự truyện** và các **đoạn ghi âm**" | Khớp: bản thảo tự truyện Gacy viết trong thời gian ở hàng chờ tử hình được dự định đặt tên "**The 34th Victim**"; hồ sơ còn có "audio interviews recorded just after his arrest" |

> ⚠ **Sửa 7 câu `⚠` = đổi kịch bản = dựng lại toàn bộ** (TTS → ảnh tĩnh → video 28 phút → phụ đề → đóng gói). Cần người dùng quyết trước (L4).

---

## 6. VẤN ĐỀ CHẶN — tái tạo TTS không chạy được trên máy này (03/11/2026)

> **ĐÃ GỠ 03/11/2026 — kết luận ở §6.1 SAI.** `kaggle` CLI có trên máy này ở `%LOCALAPPDATA%\kaggle-venv\Scripts\kaggle.exe` (ngoài PATH) và xác thực được — 4 kernel Tập 06 ngày 02/11 đều đẩy từ máy này. Thiếu GPU/torch ở máy không liên quan (Higgs chạy trên Kaggle). Kết quả sửa: xem **§9**.

Người dùng đã chốt: **sửa cả 7 câu `⚠` rồi dựng lại toàn bộ Tập 06**. Việc sửa câu **đã dừng lại** vì gặp blocker kỹ thuật thật.

### 6.1. Vì sao chặn

Sửa một câu trong kịch bản ⇒ phải tạo lại file TTS của câu đó. **Engine Higgs Audio v3 của dự án chỉ chạy được trên Kaggle GPU** (`00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` §"PHẠM VI": *"MỌI QUY TẮC TRONG FILE NÀY CHỈ ÁP DỤNG KHI HIGGS CHẠY TRÊN KAGGLE GPU"*; chạy ở nơi khác = **engine mới**, phải đo lại CER/G8/G9 từ đầu).

**Đo trên máy này (03/11/2026):**

| Hạng mục | Kết quả |
|---|---|
| GPU (`nvidia-smi`) | ❌ **không có** |
| `kaggle` CLI trong PATH | ❌ **không có** |
| `~/.kaggle/kaggle.json` | ❌ **không có** (Test-Path = False) |
| Python module `kaggle` / `torch` / `mlx_audio` | ❌ **không có** cả ba |
| Kernel sản xuất đã dùng | `.work/higgs_prod_t06_kaggle.ipynb` (kernel `amber-eyes-higgs-prod-t06-kaggle-gpu`) — **chạy ở máy khác** |

⇒ **Không tạo lại được 7 file WAV** sau khi sửa câu: `s1_08_01.wav`, `s2_06_03.wav`, `s2_11_02.wav`, `s2_11_03.wav`, `s3_06_01.wav`, `s3_11_01.wav`, `s5_02_03.wav` (tồn tại trong `.work/audio_s_higgs_t06/`, 154 file/đợt).

### 6.2. Đã audit thêm: 11 chữ trên hình cũng cần sửa

QC cổng "số trên hình có trong câu" **không bắt được** loại lỗi này (đây là *hành vi* khẳng định, không phải *số*). Audit 73/73 caption một lượt cho ra thêm 4 lỗi mới:

| Shot | Chữ hiện tại | Vấn đề |
|---|---|---|
| `2-15` | **RÚT TIỀN MẶT CHUẨN BỊ BỎ TRỐN** | ❌ **không nguồn nào** xác nhận. Câu `2.11#5`–`#6` chỉ nói "các thám tử nhận thấy Gacy ngày càng mất bình tĩnh" / "cơ hội hành động duy nhất đã điểm". Đã grep toàn bộ 20 nguồn: không có "withdraw"/"bank"/"cash" nào liên quan Gacy |
| `3-03` | **NẮP HẦM KỸ THUẬT PHÒNG NGỦ** | ❌ **SAI**: sách *Witnesses from the Grave* ghi "a trap door in a **closet** inside Gacy's house" ⇒ nắp hầm ở **tủ quần áo**, không phải phòng ngủ |
| `5-07` | **BÀI HỌC KINH ĐIỂN TẠI HỌC VIỆN FBI** | ❌ **không nguồn nào** nhắc "FBI Academy"/Quantico. Câu `5.06#2` chỉ nói "nhiều trung tâm nghiên cứu tội phạm" |
| `1-05` | *Vận hành suốt gần một thập kỷ giữa khu dân cư* | ⚠ nguồn: "murdering 33 young men and boys between **1972 and 1978**" (Oxygen), "first murder in **1972**" (Biography.com) ⇒ **6 năm**, không phải "gần một thập kỷ" |
| `2-08` | *Lời ngụy biện mua từ tiệm cầm đồ* | ⚠ câu `2.07#4` chỉ nói "một lời giải thích qua loa"; chưa tìm được "tiệm cầm đồ" trong 20 nguồn đã kiểm chứng |
| `5-01` | **14 NĂM TẠI KHU BIỆT GIAM TỬ TÙ** | ⚠ nguồn viết "**on death row**" (hàng chờ tử hình), không khẳng định "khu biệt giam" |

Các caption `1-12`, `2-06`, `2-14`, `3-04`, `3-08` chỉ lặp lại nội dung sai của 7 câu ở §5.1.

### 6.3. Gói sửa đã chuẩn bị sẵn (chưa áp dụng)

**`02_SAN_XUAT/Tap06/DeXuat_Sua_Tap06.md`** — 7 câu (nhóm A) + 11 chữ trên hình (nhóm B), mỗi mục có **câu hiện tại được trích tự động từ `script_tap06.json`** ⇒ không thể lệch với kịch bản thật, kèm câu đề xuất + nguồn + file TTS phải tạo lại + quy trình 6 bước.

### 6.4. Việc có thể làm **không cần** Kaggle

Nhóm B (11 chữ trên hình) **không đổi câu** ⇒ không cần TTS ⇒ chỉ cần render lại ảnh tĩnh của 11 shot đó rồi dựng lại hình. Việc này vẫn bị chặn bởi việc **file âm thanh master phải khớp timeline** ⇒ nên làm cùng đợt với nhóm A.

### 6.5. Khuyến nghị

Chạy **1 lượt Kaggle** cho đúng 7 câu (kernel `amber-eyes-higgs-prod-t06-kaggle-gpu`, payload `.work/kaggle_higgs/higgs_payload_t06.json` cập nhật 7 câu) → rồi áp toàn bộ gói sửa theo `DeXuat_Sua_Tap06.md` §C. Trong lúc chờ, **bảng nguồn đã đủ minh bạch**: 51 mốc `✅` + 7 mốc `⚠` kèm giải thích chi tiết từng câu.

---

## 7. Việc còn lại của người dùng

1. **Nghe duyệt** — danh sách 12 câu cần nghe: `02_SAN_XUAT/Tap06/CanNghe_Tap06_higgs.md`.
2. **Duyệt 7 câu `⚠` + 11 chữ trên hình** — gói sửa: `02_SAN_XUAT/Tap06/DeXuat_Sua_Tap06.md` (đã chuẩn bị, **chưa áp dụng**).
3. **Cấp quyền chạy Kaggle** (hoặc tự chạy 1 lượt kernel) để mở khóa bước dựng lại — xem §6.

---

## 8. Sao lưu (L5)

| Bản cũ | Đường dẫn |
|---|---|
| Master mp4/mp3 + srt + shots + timeline (bộ giọng A, 24/10) | `.work/_cu/t06_truoc_dung_lai_Higgs/` |
| Master mp4/mp3/srt (bộ MiniMax) | `.work/_cu/t06_minimax_20261102/` |
| Bảng shot 165 câu (trước khi viết lại) | commit `f3b5db9` + `.work/_cu/t06_shottable_165cu` |
| Hồ sơ tập trước khi sửa Phụ lục A | `.work/_cu/t06_plan_truoc_appendixA.md` |
| `provenance.json` trước khi thêm dòng Tập 06 | `.work/_cu/provenance_truoc_tap06.json` |
| `mo_ta.txt` + `nguon_tham_khao.md` trước khi điền nguồn | `.work/_cu/t06_mo_ta_truoc_nguon/` |
| `provenance.json` trước khi thêm dòng nguồn | `.work/_cu/provenance_truoc_nguon_t06.json` |
| `edition.py` + tiêu chuẩn + AGENTS.md | git (chưa commit) |

---

## 9. CẬP NHẬT 03/11/2026 — đã sửa kịch bản + audio + mọi thứ trừ video

**Phạm vi người dùng chốt:** chạy Kaggle, sửa, điều chỉnh tất cả nhưng **không tạo video**.

### 9.1. Kịch bản — 6 câu sửa theo nguồn, 1 câu giữ nguyên
| Câu | Sửa thành |
|---|---|
| `2.06#3` (D) | …còng tay kim loại và **nhiều chiếc phù hiệu cảnh sát**. |
| `2.11#2` (H) | …hắn thản nhiên dừng xe lại và **mời các sĩ quan đang bám theo mình vào nhà hàng ăn tối cùng hắn**. |
| `2.11#3` (H) | Hắn hào phóng **mua bia** cho họ… |
| `3.06#1` (D) | …cao chưa đầy **nửa mét**… |
| `3.11#1` (H) | Một chiến dịch khai quật **với quy mô khổng lồ** lập tức được triển khai khẩn cấp **ngay trong những ngày cuối năm ấy**. (giữ câu dài — câu Host ngắn dễ bị đọc trầm, §12.8) |
| `5.02#3` (H) | Hắn vẽ **hơn hai nghìn** bức tranh sơn dầu… |
| `1.08#1` | **GIỮ NGUYÊN.** Bộ Lao động Mỹ: lương tối thiểu liên bang từ 01/01/1978 = **2,65 USD** ⇒ 5 USD ≈ 1,9 lần = "gần gấp đôi" ⇒ câu đúng. Con số "2,35 USD" trong §5.1 là **sai**; đề xuất đổi sang "bang Illinois" cũng sai (Illinois 2,10 năm 1976, 2,30 năm 1979) |

### 9.2. Audio Higgs (Kaggle)
- Vòng 4 (P8b): 6 câu × 4 bản = 24 file. ⚠ Lượt đẩy đầu tiên **chạy nhầm spec vòng 3** (Kaggle gắn bản dataset cũ dù `status: ready`) ⇒ ra 12 file cũ, đã cất ở `.work/kaggle_higgs/_sai_r4_spec_cu_out_higgs_r2_t06/`, đẩy lại sau khi tải `prod_spec_r2_t06.json` từ Kaggle về kiểm nội dung.
- Mọi câu sửa có bản **CER 0%**; F0 bản đọc lệch ≤ 2 nc (H 114–137 Hz, D 77–85 Hz); G8 0 file lệch mới; G9 D–H 5,43 · C–H 8,95 · C–D 15,09 nc ✅.
- 154/154 câu cài, 0 bản chọn trong danh sách loại; 14/154 câu còn > 2% (không đổi so với 02/11).

### 9.3. Master `xuat_ban/Tap06_master.mp3`
**1260,9 s · −16,3 LUFS · true peak −2,3 dBFS · 0 khoảng câm > 0,3 s ở −60 dB · lời đầu 23,0 s** ✅. `timeline.total` = 1260,93 s.
Lần ghép đầu ra đỉnh **−1,3 dBFS (trượt)** — `build_audio3.py` chỉ giới hạn một lần ở 0,75. Đã sửa thành vòng siết dần 0,75 → 0,70 → 0,65 → 0,60; hồi quy Tập 05 ra master giống từng byte.
Bản master Higgs 02/11 (1265,4 s): `.work/_cu/t06_higgs_v1_20261103/`.

### 9.4. Bảng shot + phụ đề + ảnh tĩnh (không dựng video)
- Chữ trên hình: 10 mục nhóm B (bỏ `1-12` vì `1.08#1` giữ nguyên) — giữ đúng H6 (chữ lấy từ câu đang đọc): `1-05` *Âm thầm vận hành ngay giữa khu dân cư yên bình* · `2-06` **CÒNG TAY KIM LOẠI & NHIỀU PHÙ HIỆU CẢNH SÁT** · `2-08` *…Một lời giải thích qua loa* · `2-14` **HÀO PHÓNG MUA BIA CHO CẢNH SÁT** · `2-15` **NGÀY CÀNG MẤT BÌNH TĨNH** + nền đổi `t6_bank_cash_withdrawal` → `t6_des_plaines_police_station` · `3-03` **NẮP SÀN DẪN XUỐNG GẦM NHÀ** · `3-04` *Cao chưa đầy nửa mét…* · `3-08` **CHIẾN DỊCH KHAI QUẬT QUY MÔ KHỔNG LỒ** · `5-01` **MƯỜI BỐN NĂM TẠI MENARD** · `5-07` **MỘT BÀI HỌC ĐẮT GIÁ**.
- Thêm lỗi H6 do `qc_shots_t04.py --ep 06` bắt: `1-06` (số nhà 8213 không có trong câu) · `1-17`, `4-03` (trích dẫn cắt ghép không nguyên văn; `4-03` còn đặt lời dẫn "Hãy hình dung…" vào ngoặc kép như lời sĩ quan — K3) · `5-08`→`5-11` "CẢNH BÁO ĐỎ 1/2/3/4" → "THỨ NHẤT/HAI/BA/TƯ" khớp lời đọc.
- QC bảng shot: 6 OK · 6 "lỗi" còn lại đều **báo nhầm** (5 ngày `06 · 05` ↔ "6 tháng 5" do số 0 đứng đầu, `5-03` chữ hoa).
- `parse_shots.py` 73 shot, 0 nền thiếu · `subtitles.py` 322 cue, có chữ mới, 0 chữ cũ.
- Ảnh tĩnh 17 shot đã sửa: soi mắt — đủ dấu, không đè chữ, không chữ lạ; nền `5-07` không có chữ FBI.

### 9.5. Nguồn + mô tả
- `_gen_t06_sources.py`: 7 dòng ⚠ → ✅ (6 câu đã sửa + `1.08#1` đối chiếu DOL). Trang DOL chặn curl (403) ⇒ **không** đưa vào bảng nguồn tự động (validator đòi cache 200), chỉ ghi URL trong ghi chú. Bảng: 58 mốc · 20 nguồn · **0 ⚠**.
- `mo_ta.txt` sinh lại bằng `description()` (không chạy CLI): 4673/5000 ký tự, có ghi công Higgs, mốc chương theo timeline mới (Hồi 2 05:41 · Hồi 3 10:12 · Hồi 4 13:14 · Hồi 5 16:47).

### 9.6. CHƯA LÀM (theo yêu cầu)
- **Video:** `Tap06_master.mp4` hiện tại là bản 02/11 (1265,4 s) — **không khớp** audio mới 1260,9 s. Phải chạy `build_video3.py --workers 6` → `package.py --mux` → QC A/V khi được duyệt (H14).
- 2 câu lời vẫn còn khẳng định yếu nguồn (chỉ sửa chữ trên hình, chưa sửa lời): `1.04#1` "gần một thập kỷ" (nguồn: 1972–1978) · `5.02#1` "khu biệt giam tử tù" (nguồn: "death row").
- Nền `2-14` vẽ cà phê + burger trong khi lời là "mua bia" (H3 lệch nhẹ).

### 9.7. CẬP NHẬT lần 2 (03/11/2026) — sửa 2 câu lời yếu nguồn (người dùng đồng ý)
- `1.04#1`: "…vận hành suốt **gần một thập kỷ**…" → "…vận hành suốt **nhiều năm**…" (nguồn: các vụ án 1972–1978).
- `5.02#1`: "Suốt mười bốn năm **nằm trong khu biệt giam tử tù** tại…" → "Suốt mười bốn năm **chờ thi hành án** tại…" (nguồn: "on death row").
- Higgs vòng 5: 2 câu × 4 bản = 8 file (đã kiểm spec trên Kaggle trước khi đẩy — A11 #96). Mọi bản đọc đúng ≥ 3/4 bản CER 0%; F0 113–124 Hz (lệch ≤ 1,3 nc). G8 0 · G9 D–H 5,43 · C–H 8,95 · C–D 15,09 nc ✅.
- **Master mới `Tap06_master.mp3`: 1258,4 s · −16,2 LUFS · true peak −1,8 dBFS · 0 khoảng câm > 0,3 s · lời đầu 23,0 s** ✅ · 154/154 câu, 0 bản chọn trong danh sách loại, 14/154 câu > 2% (không đổi). Bản trước (1260,9 s): `.work/_cu/t06_higgs_v2_20261103/`.
- Sinh lại: `parse_shots` (73 shot, QC 6 OK + 6 báo nhầm như §9.4) · phụ đề 321 cue · nguồn (`5.02#1` ghi chú → đã sửa; 0 ⚠) · mô tả 4673 ký tự (mốc chương không đổi ở mức phút:giây). Chữ trên hình `1-05`, `5-01` đã trung tính từ trước nên vẫn khớp câu mới.
- §9.6 mục 2 câu yếu nguồn: **ĐÃ XỬ LÝ**. **Video vẫn chưa dựng lại** — mp4 cũ 1265,4 s lệch audio mới 1258,4 s.

---

## 10. CẬP NHẬT 03/11/2026 (lần 3) — **ĐÃ DỰNG LẠI VIDEO** + đo lại toàn bộ

### 10.1. Vì sao phải chia build

Một lần build **37.751 frame** (1.258,37 s × 30 fps) mất **~73 phút** > trần **60 phút** của một lệnh bash ⇒ lần dựng trước (bắt đầu 11:41, hủy 12:37) để lại 6 part **cắt cụt**: mỗi part ~45 MB / ~3.000 frame, `ffprobe` báo **`moov atom not found`** ⇒ **không dùng được, không ghép được**. Phải dựng lại từ đầu.

`render(fi)` trong `build_video3.py` **chỉ phụ thuộc `fi`** ⇒ chia theo khoảng frame cho kết quả **y hệt** một lần build liên tục:

| Nửa | Frame | `--from` → `--to` | Thư mục part |
|---|---|---|---|
| A | 0 – 18.874 | `0` → `629.167` | `.work/video3_t06_A/` |
| B | 18.875 – 37.750 | `629.167` → `1258.37` | `.work/video3_t06_B/` |

Tổng **37.751 frame** = `int(timeline.total × 30)` = `int(1258,37 × 30)`.

### 10.2. Hai tối ưu — số đo, không suy đoán

| Cấu hình | Aggregate | Ghi chú |
|---|---|---|
| 6 tiến trình, **chỉ render** (không encode) | **12,60 fps** | trần cứng của máy |
| 6 tiến trình, pipe mặc định Windows (**4 KB**) | **8,32 fps** | mất **34 %** chỉ vì đường ống |
| 6 tiến trình, **pipe buffer 4 MB** | **11,58 fps** | đạt **92 %** trần |
| 10 tiến trình, chỉ render | 13,27 fps | **máy bão hoà ~13 fps** |

CPU lúc build chỉ **~42 %** (6 tiến trình × ~55 %) ⇒ nút thắt là **băng thông bộ nhớ**, **không phải CPU** ⇒ **thêm worker không giúp** (đo ở 2 mức 6 vs 10 mới kết luận được).

Tối ưu `finishing()` (cast `float32` rõ ràng + vignette pre-expand `(H,W,3)`): **127,8 → 94,0 ms/frame (−26 %)**, kết quả **BIT-IDENTICAL** — kiểm **240/240** mẫu (120 frame × 2 nguồn: mảng ngẫu nhiên + frame thật) ⇒ **73 ảnh tĩnh đã QC vẫn hợp lệ**, không phải render lại.

### 10.3. Không sửa script dùng chung (L9)

Dùng **bản sao** `.work/_build_video3_split.py` (đọc `AE_VID` từ env; ba patch đều **tắt mặc định**) ⇒ **`build_video3.py` không đổi một byte** ⇒ không phát sinh nghĩa vụ hồi quy Tập 01 cho file đó.
Hồi quy vẫn chạy: `AE_EP=01 py -3 .work/parse_shots.py` ⇒ `shots.json` giữ nguyên hash `37C9B0247AA628F8…` ✅

### 10.4. Quy trình đã chạy

1. **Sao lưu (L5)** — `.work/_cu/t06_truoc_dung_lai_20261103/` (master mp4/mp3/srt/thumbnail + shots/timeline/script/higgs_selection/tts_manifest/acting) và `.work/_cu/t06_part_huy_20261103/` (6 part cắt cụt của lần build bị hủy) và `.work/_cu/t06_smoke_20261103/`.
2. **Dựng nửa A** — `--from 0 --to 629.167 --workers 6` → `.work/video3_t06_A/` (6 part × 3.146 frame).
3. **Dựng nửa B** — `--from 629.167 --to 1258.37 --workers 6` → `.work/video3_t06_B/` (6 part × 3.146 frame).
4. **Ghép 12 part** → `.work/video3_t06/picture.mp4` bằng **một** lần `ffmpeg -f concat -safe 0 -c copy`.
5. **Đóng gói** — `package.mux()` + `package.description()` **trực tiếp**, **không** gọi `thumbnail()` (A11 #72).
6. **QC** — 5 lớp: số đo thành phẩm · lag A/V · đối chiếu khung hình với ảnh tĩnh · cổng giám sát `qc_video_t04.py` · hồi quy Tập 01.

### 10.5. Số đo thành phẩm (đo trên chính file, không ước lượng)

| Hạng mục | Giá trị | Ngưỡng | Kết quả |
|---|---|---|---|
| `picture.mp4` | 37.751 frame · 1920×1080@30 · h264 · **1.258,366667 s** · 446.191.166 B | = `int(1258,37 × 30)` | ✅ |
| `Tap06_master.mp4` | **477.815.032 B** (455,7 MB) · **1.258,366667 s** · h264 + AAC 48 kHz stereo 192k | — | ✅ |
| Lệch thời lượng video ↔ audio | **0,02 s** | ≤ 0,05 s | ✅ |
| **Lag âm thanh–hình** (tương quan FFT, đoạn 30 s tại t=120 s) | **+0,0 ms** · r = 0,9998 | \|lag\| ≤ 40 ms | ✅ |
| Loudness **file cuối** | **−16,0 LUFS** | −16 ± 1 | ✅ |
| Loudness master mp3 | −16,2 LUFS | −16 ± 1 | ✅ |
| True peak **file cuối** | **−2,0 dBFS** | ≤ −1,5 dBFS | ✅ |
| True peak master mp3 | −1,8 dBFS | ≤ −1,5 dBFS | ✅ |
| Lỗi giải mã toàn file | **0** | 0 | ✅ |
| Khoảng lặng > 0,3 s @ −60 dB | **0** | 0 | ✅ |
| Lời đầu | 23,011375 s | 22,8 – 23,5 s | ✅ |
| Phụ đề `Tap06.srt` | **321 cue / 154 câu** · 36.255 B · CRLF · không BOM · 0 byte NUL | phủ 100 % lời thoại | ✅ |
| 6 câu đã sửa có mặt trong phụ đề | **6/6** | 6/6 | ✅ |
| Mô tả `mo_ta.txt` | 4.138 ký tự (4.067 sau quy đổi newline) · không BOM/NUL | < 5.000 | ✅ |
| `nguon_tham_khao.md` | 58 dòng dữ liệu | — | ✅ |
| `thumbnail.png` | hash **không đổi** (`d55e50665fe1…`) | không ghi đè | ✅ |
| Khung hình video vs ảnh tĩnh đã QC | **12/12 khớp** (MAE 3,87–5,50 · p99 15–23) | MAE < 8 · p99 < 30 | ✅ |
| SHA-256 master | `951bb0ba44f2bdbc551ded3f2f7a1181447b12d3e454105867550f2669af8ce0` | — | — |

### 10.6. Cổng giám sát `qc_video_t04.py --ep 06` ⇒ **23 OK · 2 cảnh báo · 0 lỗi**

Đạt: A) loudness · đỉnh · khoảng lặng · lời đầu · khớp `timeline.total` · B) bảng shot phủ 100 % 154 câu · 73/73 shot có nền · không gap · C) `picture.mp4` khớp timeline · D) mp4 khớp audio · giải mã 0 lỗi · LUFS/đỉnh file cuối · 1920×1080 · H.264 + AAC · 0 khoảng lặng · E) phụ đề phủ 100 % lời thoại · cue cuối 1248,77 s · F) thumbnail đúng nền theo kế hoạch · G) thẻ kết có chữ tại 1250,3 s (10,64 % pixel sáng), shot cuối `5-14` là thẻ kết.

Cảnh báo (không phải lỗi, **có sẵn từ trước lần dựng lại**):
- **B) 6 shot dài > 16 s** — `1-01` 16,9 · `1-04` 17,2 · `1-08` 18,6 · `1-12` 17,8 · `1-19` 21,2 · `1-20` 22,9 s.
- **G) khung tại `total − 2 s` bị đen** — outro của renderer mờ dần 3 s cuối (dùng chung T01–T03) ⇒ thẻ kết đã được kiểm ở **giữa shot cuối** (A11 #65).

### 10.7. Còn lại

| Việc | Người làm | Ghi chú |
|---|---|---|
| Nghe duyệt 12 câu giọng | **người dùng** | `CanNghe_Tap06_higgs.md` — chưa có phản hồi |
| Duyệt 20 nguồn / 58 mốc trước khi đăng | **người dùng** | bảng đã kiểm chứng HTTP 200 từng link; **0 ⚠** |
| **14/154 câu còn CER > 2 %** | cảnh báo, **không chặn** | cao nhất `1.09#2` N1 = 5,6 %; C 4 câu · D 4 câu · H 4 câu; **không câu nào trong 6 câu đã sửa nằm trong nhóm này** |
| Nền `2-14` vẽ cà phê + burger trong khi lời là "mua bia" | H3 lệch nhẹ | đã ghi nhận, chưa sửa |


