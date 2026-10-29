# QUY TẮC CHO AI — DỰNG VIDEO KÊNH AMBER EYES

> File này dành cho **mọi AI** (Claude, Gemini, GPT, Codex, Cursor…) làm việc trong thư mục này. Đọc hết trước khi làm bất cứ việc gì.
> Viết từ kinh nghiệm dựng Tập 01 và Tập 02 (21–24/10/2026). Mỗi quy tắc có lý do là **một lỗi đã thật sự xảy ra**.
> Chi tiết kỹ thuật (lệnh, thông số, mẫu khung) nằm ở `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` — gọi tắt **"tiêu chuẩn"**. File này là **luật**; tiêu chuẩn là **sổ tay**. Nếu hai file mâu thuẫn, hỏi người dùng.

Từ khoá: **PHẢI** = bắt buộc · **CẤM** = không bao giờ · **NÊN** = mặc định, chỉ bỏ khi có lý do ghi lại.

---

## 0. Kênh này là gì

- Kênh YouTube tiếng Việt **Amber eyes**: *phân tích tâm lý tội phạm qua những hồ sơ có thật*. Mỗi tập ~20–30 phút, 5 hồi.
- 3 vai chính, giọng AI:
  - **Host** (Cú): trầm ấm.
  - **Điều tra viên** (Sói): lạnh lùng.
  - **Chuyên gia tâm lý** (Cáo): nhấn mạnh, giọng nữ.
- 2 vai phụ: N1 (Cừu), N2 (Mèo).
- Hình: phong cách graphic novel noir. Nền vụ án luôn toàn khung; linh thú chỉ nhỏ ở góc. **Người thật chỉ hiện dạng bóng.**
- Mục tiêu: kiếm tiền được, ít bị khiếu nại, **0 đồng chi phí công cụ**. Ngôn ngữ làm việc với người dùng: **tiếng Việt**.

---

## 1. Luật làm việc chung

| # | Luật | Vì sao |
|---|---|---|
| L1 | **PHẢI đọc** `README.md` → file này → tiêu chuẩn → hồ sơ tập (`02_SAN_XUAT/TapXX/KeHoach_Video_TapXX.md`) trước khi chạy gì | Dự án có nhiều tập chạy song song, nhiều quyết định đã chốt |
| L2 | **CẤM bịa dữ kiện, con số, câu trích, link nguồn.** Không chắc → ghi "cần nguồn" và hỏi | Tập 01 từng tự thêm "19 tuổi"; Tập 02 có câu trích "OK" không hề tồn tại |
| L3 | **CẤM nói "xong" khi chưa đo.** Mỗi bước báo **số đo thật** (thời lượng, LUFS, số câu, số lỗi) | Nhiều lỗi chỉ lộ khi đo: khoảng câm 0,6 s, hình lệch tiếng |
| L4 | **PHẢI dừng hỏi người dùng** trước việc: tốn tiền (video AI, credit) · đổi giọng nhân vật · dùng tài sản tải ngoài · xoá / ghi đè thành phẩm · quyết định pháp lý | Người dùng từng đảo quyết định 2 lần; các việc này không hoàn tác được |
| L5 | **PHẢI sao lưu trước khi ghi đè** (đưa vào `.work/_cu/` hoặc scratchpad), ghi đường dẫn bản lưu vào báo cáo | Đổi giọng, đọc lại câu, dựng lại đều cần quay về được |
| L6 | **PHẢI ghi lại mọi quyết định và bài học** vào tài liệu (hồ sơ tập, tiêu chuẩn mục A11) ngay trong lượt làm | AI sau không đọc được cuộc trò chuyện, chỉ đọc được file |
| L7 | **Mọi tài sản PHẢI có dòng trong `provenance.json`** (công cụ, prompt, ngày, điều khoản, đã kiểm thương mại chưa) | Hồ sơ khi bị khiếu nại bản quyền |
| L8 | **Tách bạch tập:** mọi lệnh chạy với `AE_EP=XX` (Tập 01 không cần); bản ngôn ngữ khác thêm `AE_LANG=..`. **CẤM sửa script cho riêng một tập** — cấu hình tập nằm trong `EPISODES` của `.work/edition.py` | Tập 02 suýt ghi đè file Tập 01; nhiều chỗ "viết cứng cho Tập 01" gây lỗi ở Tập 02 |
| L9 | **Sửa script dùng chung → PHẢI kiểm hồi quy Tập 01** (danh sách câu, mốc thời gian, bảng shot giống hệt bản cũ) | Script dùng chung cho mọi tập |

---

## 2. Quy trình — có cổng kiểm, KHÔNG được nhảy cổng

Mỗi bước chỉ làm khi bước trước **ĐẠT**. Lệnh cụ thể: tiêu chuẩn mục A3.

| Bước | Việc | ĐẠT khi |
|---|---|---|
| 1 | **Duyệt kịch bản** (mục 3) | Mọi dữ kiện về người thật đã đối chiếu nguồn công khai; 0 lỗi V9; người dùng duyệt |
| 2 | Tách kịch bản `parse_kichban.py` | Số câu, N1/N2 đúng như bảng Phụ lục A của hồ sơ tập |
| 3 | Diễn xuất `make_acting_tapXX.py` | Lời đọc khớp từng chữ với câu gốc (mục 4, G6) |
| 4 | Đọc giọng `tts_sentences.py` | Đủ 100% câu |
| 5 | **Nghe theo vai** `voice_role_check.py` (G10) | Mỗi vai nghe liền ra **1 người**; 3 vai tách bạch. **Không đạt → DỪNG** |
| 6 | Âm thanh `build_audio3.py` | 0 khoảng câm > 0,3 s ở −60 dB · −16 ± 1 LUFS · đỉnh ≤ −1,5 dBFS · lời đầu 22,8–23,5 s |
| 7 | Bảng shot `parse_shots.py` | Phủ 100% câu đúng thứ tự · mọi nền có file · số trên hình có trong câu |
| 8 | **Ảnh tĩnh MỌI shot** `build_video3.py --stills …` | Không lỗi, không đè chữ, không chữ lạ, không lộ mặt (mục 6) |
| 9 | Dựng hình `build_video3.py --workers 6` (~1 giờ / 27 phút video) | `picture.mp4` đủ dài |
| 10 | Phụ đề + đóng gói `subtitles.py`, `package.py --mux` | Hình = tiếng ± 0,05 s · giải mã 0 lỗi · thumbnail đúng tập |
| 11 | Giao cho người dùng | Báo số đo + danh sách việc người dùng phải làm (nguồn, điều khoản, nghe duyệt) |

**Mốc dừng chờ người dùng:** sau bước 1 (kịch bản), sau bước 5 (nghe giọng), sau bước 8 (ảnh tĩnh), sau bước 11.

---

## 3. Kịch bản

| # | Luật |
|---|---|
| K1 | **PHẢI đối chiếu trên internet** mọi dữ kiện về người thật: ngày, tuổi, số liệu, chức danh, câu trích. Dùng nhiều nguồn (báo lớn, hồ sơ toà, Wikipedia làm điểm xuất phát). Ghi link vào bản review của kịch bản |
| K2 | **Câu trích PHẢI nguyên văn và có nguồn.** Không tìm được nguồn → bỏ câu trích hoặc chuyển thành lời kể. Câu trích tiếng Anh → dịch sang tiếng Việt cho giọng đọc, ghi rõ "theo bản ghi…" |
| K3 | **CẤM gán lời thoại bịa cho người thật hoặc "một người có thật".** Nhân vật minh hoạ nói thì lời dẫn phải là "hãy hình dung…", không phải "hãy lắng nghe một sĩ quan…" |
| K4 | **V9 — không mô tả bạo lực, thương tích, thi thể, cách gây hại.** Danh sách từ cấm: tiêu chuẩn A9.2. **CẤM mọi chi tiết tình dục liên quan trẻ vị thành niên** (vùng YouTube xử lý nặng nhất) |
| K5 | **Không khẳng định chẩn đoán tâm thần** cho người thật. Dùng "mang đặc điểm thường được mô tả trong…", "khung lý thuyết này giúp giải thích…" |
| K6 | **Đại từ phải rõ ai là ai** trong audio: hung thủ = "hắn"; thám tử, nhân chứng = tên hoặc "ông/bà". Tập 02 từng gọi cả thám tử lẫn hung thủ là "hắn" |
| K7 | **Số, ký hiệu viết bằng chữ khi có thể** (%, km, $, số La Mã). Script tự đổi số sang chữ khi đọc (G11), nhưng ký hiệu thì không |
| K8 | **Kiểm logic nội bộ:** cộng số (17 + 61 ≠ 82), đếm ngày (4/2 → 7/2 là 3 ngày), mâu thuẫn trước–sau, vai tự mời chính mình |
| K9 | Định dạng kịch bản theo tiêu chuẩn A2. Tên riêng có viết tắt có dấu chấm ("Robert F. Scott") sẽ bị tách câu sai → viết "Robert Scott" |

---

## 4. Giọng đọc — phần dễ sai nhất

> **Chuyển sang Higgs Audio v3 — chạy cục bộ Mac mini M2 16 GB qua MLX-Audio (27/10/2026, chưa dùng sản xuất):** khi engine TTS là Higgs, đọc và tuân theo `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` — file đó thay mục này cùng T2, T8, T9.
>
> **Tạo giọng mẫu cho Higgs bằng VoxCPM2 (28/10/2026, đã chốt hướng, chưa chạy thử):** đọc `00_TIEU_CHUAN/TAO_GIONG_MAU_VOXCPM2.md` — chứa prompt Voice Design cho 7 vai, cách điền form web, và quy trình đóng gói thành file tham chiếu.

**Ba bộ giọng của kênh.** Khai ở `.work/edition.py`: `CAST` (mặc định bản VN) · `EPISODES["01"]["cast"]` (ghim Tập 01).

| Vai | Bộ A (bản VN, từ Tập 02) | Tốc độ | Bộ EN | Tốc độ | CER đo (T2, 20 câu) |
|---|---|---:|---|---:|---|
| Host · trầm ấm | `English_CaptivatingStoryteller` | 0,90 | `English_magnetic_voiced_man` | 0,95 | **0,1%** · 0/20 vượt ngưỡng |
| Điều tra viên · lạnh lùng | `Korean_ColdYoungMan` | 0,95 | `English_Trustworth_Man` | 0,97 | **3,1%** · max 28,6% ⚠ |
| Chuyên gia · nhấn mạnh (nữ) | `English_AssertiveQueen` | 0,92 | `English_Wiselady` | 0,95 | 0,9% |
| N1 (nữ) | `Vietnamese_kindhearted_girl` | 0,95 | `English_SentimentalLady` | 0,95 | 0,0% |
| N2 (nữ) | `English_captivating_female1` | 0,95 | `English_captivating_female1` | 0,95 | 0,0% |

- **Tập 01 ghim bộ riêng** (để dựng lại ra đúng bản đã xuất): `audiobook_male_1` 0,90 · `male-qn-qingse` 0,95 · `audiobook_female_1` 0,92.
- **Kho chỉ có 1 giọng tiếng Việt gốc** (`Vietnamese_kindhearted_girl`, nữ) — chỉ đọc cho N1, chiếm 2% số câu. **3 vai chính đọc tiếng Việt bằng giọng `English_`/`Korean_`**: giọng hệ thống MiniMax **đa ngôn ngữ**, tiền tố là ngôn ngữ *gốc* của giọng, KHÔNG phải giới hạn ngôn ngữ đầu vào.
- ⚠ **Vai Điều tra viên là điểm yếu của bộ A** (CER 3,1%, max 28,6%) — đã đo 27/10/2026. Ứng viên thay thế đã sàng lọc xong: `90_LUU_TRU/BaoCao_SangLocGiongDieuTraVien_20261027.md`.
- **CẤM đổi giọng** khi chưa qua G8–G10 **+ G12** và chưa có người dùng đồng ý (L4).

| # | Luật | Lỗi đã gặp |
|---|---|---|
| G1 | **CẤM `...` và thẻ ngắt `<#s#>` giữa câu.** Chỉ được một thẻ `<#0.35#>` sau dấu `:` đứng trước câu trích | Ngắt giữa câu làm giọng Việt vụn "như robot" (nhịp 3–4/10) |
| G2 | **Kịch tính đặt GIỮA các câu** (`_pause_after` 0,2–1,2 s), cộng tắt nhạc và tiếng động | |
| G3 | Cảm xúc đổi theo nhịp truyện, **chỉ trong 4 cảm xúc an toàn**: `neutral · sad · fearful · surprised` | |
| G4 | Tốc độ lệch so với gốc chỉ trong **−0,06 … +0,02** | `sad`/`fearful` tự làm máy đọc chậm; cộng thêm −0,1 làm câu dài gấp đôi |
| G5 | **Cao độ (`pitch`) LUÔN = 0** | Giọng Host cũ: chỉnh cao độ ±1 thì **thành người khác**, nghe như "3 Host" |
| G6 | Lời đọc riêng **không được đổi chữ**; phụ đề và chữ trên hình luôn lấy câu gốc. Kiểm bằng script so từng chữ | |
| G7 | Không để giọng Việt đọc tiếng Anh dài; bỏ chú thích tiếng Anh trong ngoặc khỏi lời đọc | |
| G8 | **Mỗi giọng có bộ tham số an toàn:** cùng một câu × mọi thiết lập định dùng → nghe mù phải ra **1 người** | 7 thiết lập → 6 "người" với giọng cũ |
| G9 | **Các vai phải khác hẳn nhau:** hai giọng cùng giới cách nhau ≥ 4 nửa cung, khác rõ chất giọng; xen kẽ 3 vai → nghe mù gán đúng 100% | Hai giọng nam cũ chỉ cách 2 nửa cung, người nghe không phân biệt được |
| G10 | **Nghe liền theo vai trước khi dựng** (`voice_role_check.py`) | Lỗi "3 Host" lọt qua vì buổi thử chỉ so các bản của CÙNG một câu |
| G11 | **Số đọc bằng chữ tiếng Việt** (tự động trong `tts_sentences.vi_numbers`) | "1.400" bị đọc thành "một phẩy bốn trăm" |
| **G12** | **Giọng ngoại ngữ đọc tiếng Việt PHẢI đo CER bằng `listen_audio` (ngưỡng < 2%) cho từng vai dùng nó.** **CẤM suy độ đúng chữ hay giới tính từ tên giọng** — tiền tố `English_`/`Korean_` là ngôn ngữ *gốc*, không giới hạn ngôn ngữ đầu vào | `English_CalmWoman` đọc "chiếc" thành **"check"** → CER 13,2%. `Korean_ColdYoungMan` đọc "Thứ hắn lấy đi" thành **"Thương hiệu Han Lady"** → CER 28%. Cả hai đều nghe *đúng chữ* nhưng sai *thanh điệu* |
| **G13** | **Chọn giọng mới phải qua 4 lớp CÓ SỐ ĐO, theo thứ tự: (1) CER < 2% · (2) G8 ổn định danh tính · (3) G9 tách bạch ≥ 4 nửa cung với vai còn lại · (4) nghe thử bản dựng thật.** Điểm hợp vai (chấm 1–10) **không** thay được lớp đo CER và **không** thay được G8/G9 | `English_ReservedYoungMan` điểm hợp vai cao nhất (9/10) nhưng cách Host chỉ **3,8 nửa cung** → vi phạm G9 |

**Chọn giọng mới (nếu người dùng yêu cầu) — theo G13:**
- **Danh mục ứng viên**: `connector__matrix__get_voice_list` (332 giọng). **Code KHÔNG gọi API này** — `CAST` trong `edition.py` là **hardcode**; đổi danh mục không tự đổi giọng đang dùng.
- **Vắng mặt trong danh mục ≠ giọng chết.** `audiobook_male_1` / `male-qn-qingse` không có trong 332 giọng nhưng **vẫn gọi được** (đã kiểm 27/10/2026); `male-qn-qingse` còn là giọng mặc định của endpoint TTS. Muốn chắc chắn → **gọi TTS thật 1 câu**.
- **Mẫu đo**: 20 câu của đúng vai đó, dùng **đúng `emotion` + `speed` của production** (không dùng `neutral` chung cho mọi câu) → tự có baseline so sánh.
- **Đo trên file TTS đã xuất** thì **không cần tổng hợp lại** (tiết kiệm credit).
- **Giọng điểm hợp vai cao nhất thường trượt G8 hoặc G9.** Đừng chọn chỉ vì điểm hợp vai.

---

## 5. Âm thanh và tiếng động

| # | Luật |
|---|---|
| A1 | **V4: không im lặng tuyệt đối > 0,3 s.** Mọi chỗ tắt nhạc (`music_drop`, "nhạc dừng đột ngột") **PHẢI có nền môi trường** bên dưới — Tập 02 từng câm 0,6 s ở lời kết |
| A2 | Ba lớp, khai trong `.work/sfx_tapXX.json`: **nền môi trường liên tục theo cảnh** · **tiếng động gắn hành động trong câu** · **nhấn kịch tính** ở câu hé lộ. Trộn stereo |
| A3 | **Tiếng tải về (YouTube Audio Library) PHẢI được nghe kiểm trước khi nhập.** Kiểm 3 điều: đúng vật không (búa tòa từng hoá ra "lắc bình xịt"), có lẫn nhạc hay **giọng người** không, có lặp máy móc không |
| A4 | **PHẢI cắt đúng đoạn** tiếng động (thường 1–12 s). File tải về dài 14–59 s mà đặt nguyên thì sẽ kêu suốt chục câu. Khai `CUTS`; file sai khai `KEEP_CODE` trong `import_sfx_video.py` |
| A5 | Tiếng tự tổng hợp bằng code chỉ đạt ~6–8/10 độ thật: dùng tốt cho nền và nhấn kịch tính, **kém cho vật thật** (xe, bộ đàm, búa) |
| A6 | Nhạc chỉ lấy đoạn liên tục (`bgm_ambient_deep` có khoảng câm bên trong); nhạc hồi mới vào **tại ranh giới hồi** |
| A7 | Chuẩn hoá `loudnorm I=-16:TP=-1.5:LRA=11`, hai lượt, `linear=true` |
| A8 | **Nguồn SFX thứ 2: Freesound (CC0)** — dùng khi YouTube Audio Library không có track đúng nghĩa (19 mã đang dùng track thay thế, mục 4.2). Công cụ: `.work/freesound_client.py` + `.work/fs_fetch.py` + `.work/fs_provenance.py`. Token auth = cột "Client secret/Api key" của https://freesound.org/apiv2/apply. Chỉ tải được **preview 160 kbps mp3**, KHÔNG tải được file gốc (endpoint `download/` là OAuth2-required). Mọi file phải là **CC0** cho kênh kiếm tiền, và phải **nghe duyệt** trước khi nhập |
| A9 | **Tối ưu ducking và sàn môi trường tập dài (>30 phút):** dùng `np.cumsum` cho đường bao ducking (giảm từ 5 phút xuống 0,05 s); sàn môi trường đặt −31 dB, đuôi piano ấm 7,8 s fade out mượt để tránh lỗi V4 cuối video |
| A10 | **Bed nhạc nền phải khớp kịch bản, không copy pattern của tập khác.** Mỗi hồi lấy mood thẻ `[BGM]` ĐẦU TIÊN của hồi đó trong `01_KICH_BAN/TapXX/` (Hồi 1 lấy tại mốc `act1_cue`). Lỗi đã gặp 25/10/2026: 20/29 tập dùng chung 1 pattern; T09/T16 đòi guitar/organ nhưng bed trỏ piano/cello; 2 track dài nhất (220 s + 196 s) nằm không ai dùng. Kiểm: `py -3 .work/_qc_bgm_bed_start.py` trước khi dựng |
| A11 | **Sửa `edition.py` bằng script: giữ dấu nháy và `import` thật để kiểm.** Mất nháy làm `1: bgm_x.mp3` thành biểu thức thuộc tính — `py_compile` vẫn PASS nhưng lúc chạy sẽ NameError. Vá chỉ giá trị của đúng hồi, không dựng lại cả khối `bed`; luôn sao lưu `.work/_cu/` trước (L5) |
| A12 | **Mã câu trong `EPISODES[*]["summary"]` phải tồn tại trong script — nếu không `package.py --mux` crash `KeyError` (Tập 07, 08)**. Element `1.01` của T07/T08 là thẻ `[BGM]` không có câu thoại nên `1.01#1` không tồn tại (script đã sửa sau lúc dựng). Khi sửa kịch bản phải cập nhật lại `summary`. Kiểm: `.work/_patch_summary_t07.py` quét 29 tập |

---

## 6. Hình ảnh, bảng shot, renderer

| # | Luật |
|---|---|
| H1 | **V5: người thật chỉ hiện dạng bóng, mặt chìm hoàn toàn.** Quan chức, thẩm phán, bác sĩ: chỉ hiện tên. **Không vẽ nạn nhân**, kể cả dạng bóng, nếu vụ có xâm hại hay giết người |
| H2 | **Duyệt bằng mắt MỌI ảnh nền mới:** chữ lạ do AI vẽ (biển số, nhãn, đồng hồ), mặt lộ nét, viền đen/trắng, watermark. Phóng to vùng nghi ngờ |
| H3 | **Ảnh phải khớp lời, không chỉ khớp chủ đề.** Kịch bản nói "ngồi đối diện" mà ảnh hai người ngồi cạnh nhau → sai. Đang nói "mức lương 5$" mà ảnh chuyển sang tủ áo khoác → sai. Gom trọn các câu cùng chủ đề vào cùng một shot |
| H4 | **Không dùng hình minh hoạ đúng lúc lời nói về hành vi gây hại** (ví dụ bóng người leo cầu thang nhà dân đúng câu "tấn công tình dục") — dời sang ẩn dụ |
| H5 | **CẤM để AI vẽ chữ.** Mọi chữ trên hình do Pillow vẽ; font đã đo đủ dấu tiếng Việt (tiêu chuẩn A5.3). Georgia không có dấu; Bahnschrift thiếu "ỷ" |
| H6 | **V3: chữ trên hình lấy từ chính câu đang đọc.** Mọi chữ số trên hình phải có trong câu; câu trích phải nguyên văn |
| H7 | **Mẫu T5 (con số) chỉ hiện MỘT số / tiêu đề lớn.** Thông tin thêm viết nghiêng. Hai `**…**` sẽ đè lên nhau ("B8ẾN 01 · 2010") |
| H8 | **T3 "so sánh"** viết `trái → phải`; **T8 danh sách** đọc mọi đoạn; **T7 bản đồ** có nhãn ghim khai ở `route_pins` của tập (Tập 01 từng viết cứng "SPRINGFIELD/WISCONSIN") |
| H9 | **Ảnh tĩnh MỌI shot trước khi dựng cả tập** (151 ảnh ~2 phút). Một shot lỗi làm hỏng cả lượt dựng ~1 giờ — đã xảy ra |
| H10 | Mỗi shot 3–15 s; tắt bán thân linh thú `⊘` ở khoảnh khắc nặng nề; tránh một nền lặp quá 4 shot liền |
| H12 | **Shot cuối (thẻ kết) PHẢI có chữ:** nhãn `HỒ SƠ TẬP XX · ĐÃ ĐÓNG` + tên kênh **AMBER EYES** + khẩu hiệu "Phân tích tâm lý tội phạm / qua những hồ sơ có thật". Cột Chữ của shot cuối không được để "—" (Tập 01 và Tập 02 từng kết thúc bằng tờ giấy trống). Renderer tự phóng to tên kênh ở shot cuối không lời |
| H13 | **Khớp 3 chiều (Ảnh — Chữ — Lời thoại):** Chữ trên hình lấy nguyên văn từ câu thoại đang đọc (H6/V3); ảnh nền phản ánh đúng ngữ cảnh câu đó (H3); vai nói và avatar bán thân khớp 100% kịch bản. Chạy script đối chiếu trước khi dựng |
| H11 | Thumbnail: nền và chữ **của đúng tập** (khoá `thumb`, `thumb_bg`). Tập 02 từng ra thumbnail mang nền nhà Tập 01 |

---

## 7. Dùng AI để kiểm tra — và bẫy của nó

| # | Luật |
|---|---|
| Q1 | AI không tự nghe được. Dùng `connector__matrix__audios_understand` làm **người nghe mù**: hỏi "có mấy người nói?", "câu nào là ai?", "chấm 1–10 hợp vai". **Không nói trước đáp án** |
| Q2 | So sánh giọng: **ghép nhiều câu khác nhau của cùng một vai**, không chỉ nhiều bản của cùng một câu (G10) |
| Q3 | Đọc kỹ bản chép của `listen_audio` trước khi kết luận "đọc sai". **3 lỗi đo hay gặp:** (a) **SỐ** — chuẩn đã qua `vi_numbers()` nên là CHỮ (`"tám mươi tám"`) còn bản chép là SỐ (`"88"`) ⇒ **phải áp `vi_numbers()` cho CẢ HAI Vế**, nếu không CER phình to giả (một câu hoàn toàn đúng bị tính 21%, một câu 300%); (b) **BỘ LỌC GEMINI CHẶN CÂU** (nội dung nhạy cảm, vd *"Xâm nhập khi có người ở nhà"*) → `transcription` bị dính đuôi tiếng Anh *"This request was blocked…"* mà `code` vẫn là `0` ⇒ phải đọc nội dung, cắt đuôi, **loại câu khỏi mẫu**; (c) câu ngắn < 12 từ → 1 lỗi = 20%+ CER, tách riêng khi báo cáo |
| Q4 | Kết quả chấm của mô hình **có nhiễu** (mốc giây lệch, mô tả giới tính sai). Quyết định lớn dựa trên ≥ 2 phép thử khớp nhau + số đo F0 |
| Q5 | Đo bằng số khi được: F0 trung vị (cao độ), tỉ lệ khoảng lặng, LUFS, `silencedetect`, độ dài hình/tiếng |
| Q6 | **ASR không tất định:** 3/9 câu vượt ngưỡng **đổi kết quả** giữa 2 lượt (28%→18%, 3,9%→0,0%). **Không kết luận về 1 câu nào nếu chỉ 1 lượt** — chạy lượt 2 cho các câu vượt ngưỡng (rẻ, chỉ ~10 lượt). Mẫu nhỏ (≤ 20 câu) chỉ đủ phát hiện lỗi hệ thống, **không đủ** kết luận "giọng này hoàn hảo" |

---

## 8. Vận hành kỹ thuật

| # | Luật |
|---|---|
| T1 | Việc dài (đọc 200+ câu, dựng hình ~1 giờ) **chạy nền**, ghi log ra file, xâu chuỗi các bước với `set -e`. Chờ bằng điều kiện thật (tiến trình kết thúc / file xuất hiện), không đoán |
| T2 | Dịch vụ MiniMax có lúc lỗi hàng giờ ("audio/image post-processing failed"). Vòng chờ **chỉ coi là đã chạy lại khi phản hồi có `node_id`** — kiểm "không có chữ lỗi" từng báo nhầm |
| T3 | Phiên AI có thể đóng giữa chừng nhưng tiến trình nền **vẫn chạy**. Trước khi chạy lại, kiểm `tasklist` hoặc tiến trình đang ghi file, tránh chạy hai lượt dựng cùng lúc |
| T4 | **Khi chèn code bằng chuỗi Python:** dùng raw string hoặc ghi ra file. `\x00`, `\b` trong chuỗi thường đã từng biến thành byte null / backspace trong file `.py`. Sau khi sửa: `py -3 -m py_compile` |
| T5 | Tên file gửi lên connector **không có dấu chấm** (`s1_03_01`, không phải `1.03_01`); tham số dài truyền bằng `--args-file`, không qua dòng lệnh |
| T6 | Windows: đặt `PYTHONIOENCODING=utf-8`; đường dẫn có dấu cách phải đặt trong ngoặc kép |
| T7 | Sửa renderer cho tập mới → giữ đường cũ cho định dạng cũ (Tập 01) và chỉ **thêm** nhánh mới |
| T8 | **`batch_text_to_audio` chỉ nhận TỐI ĐA 10 request/lượt** (`requests.maxItems = 10`). Gửi 51 request → lỗi `connector_tool_error: Connector tool execution failed (latency_ms=0)` **không nói rõ là quá giới hạn** ⇒ 4 ứng viên TTS "hỏng" trong 1 lượt. Chia chunk 10; đọc `success_items[]` từng batch thay vì tin exit code |
| T9 | **`pitch` của connector = `voice_setting.pitch` của MiniMax = ĐỔI ÂM SẮC (timbre)**, mặc định `0` = giữ nguyên âm sắc gốc — **KHÔNG phải chỉnh F0 tự nhiên**. Đây là gốc rễ của G5: `pitch ≠ 0` là **đổi người**, không phải "cao độ cao hơn". Endpoint TTS **không có tham số `language`** ⇒ engine tự nhận diện ngôn ngữ từ văn bản (tiền tố `English_`/`Korean_` chỉ là ngôn ngữ *gốc* của giọng) |

---

## 9. Pháp lý và đăng

- Mô tả YouTube **không có email liên hệ**. Có lưu ý giáo dục, mục nguồn, đường dây hỗ trợ.
- `nguon_tham_khao.md`: **người dùng điền link**, AI chỉ gợi ý nguồn đã đối chiếu (L2).
- Trước khi bật kiếm tiền: kiểm điều khoản thương mại MiniMax (giọng, ảnh, nhạc), YouTube Audio Library (chỉ dùng trong video của kênh, không phát hành riêng file), Gemini/Veo nếu có dùng.
- Khi đăng: bật "Nội dung bị thay đổi hoặc tổng hợp" · "Không dành cho trẻ em" · danh mục Giáo dục · tự đánh giá quảng cáo trung thực.
- Hai thẻ miễn trừ trong intro đã được người dùng chốt: **CẤM sửa chữ**.

---

## 10. Báo cáo cho người dùng

- Viết tiếng Việt, ngắn, có **số đo**. Nói rõ cái gì đã kiểm, cái gì chưa kiểm được và vì sao.
- Khi phát hiện lỗi do chính AI gây ra (quy tắc sai, bỏ sót kiểm tra): **nói thẳng**, nêu nguyên nhân gốc, cách sửa, và ghi vào A11 của tiêu chuẩn.
- Kết thúc mỗi lượt bằng **danh sách việc người dùng phải làm** (nghe duyệt, điền nguồn, quyết định chờ).
- File cho người dùng nghe hoặc xem: đặt trong thư mục tập (`thu_giong*/`, `xuat_ban/`), ghi đường dẫn.

---

*Khi thêm bài học mới: thêm một dòng vào bảng phù hợp ở đây (ngắn, mệnh lệnh, kèm lỗi đã gặp) **và** vào tiêu chuẩn mục A11.*
