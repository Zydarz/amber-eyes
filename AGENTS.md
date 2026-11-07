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
| L10 | **CẤM commit media (video/audio) và artifact QC** (contact sheet PNG, khung hình QC, ảnh nền `assets/bg/`). Chỉ commit **tài liệu + code + config**; media/artifact đã bị `.gitignore` loại, file vẫn còn nguyên trên đĩa | Lịch sử repo phình ~680 MB vì ảnh nhị phân; người dùng chốt 01/11/2026 |

---

## 2. Quy trình — có cổng kiểm, KHÔNG được nhảy cổng

Mỗi bước chỉ làm khi bước trước **ĐẠT**. Lệnh cụ thể: tiêu chuẩn mục A3.

| Bước | Việc | ĐẠT khi |
|---|---|---|
| 1 | **Duyệt kịch bản** (mục 3) | Mọi dữ kiện về người thật đã đối chiếu nguồn công khai; 0 lỗi V9; đạt đủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (tiêu chuẩn A2c, K10); người dùng duyệt |
| 2 | Tách kịch bản `parse_kichban.py` | Số câu, N1/N2 đúng như bảng Phụ lục A của hồ sơ tập |
| 3 | Diễn xuất `make_acting_tapXX.py` | Lời đọc khớp từng chữ với câu gốc (mục 4, G6) |
| 4 | Đọc giọng `tts_sentences.py` | Đủ 100% câu |
| 5 | **Nghe theo vai** `voice_role_check.py` (G10) | Mỗi vai nghe liền ra **1 người**; 3 vai tách bạch. **Không đạt → DỪNG** |
| 6 | Âm thanh `build_audio3.py` (trước: `qc_pause_gate.py --pre`) | 0 khoảng câm > 0,3 s ở −60 dB · −16 ± 1 LUFS · đỉnh ≤ −1,5 dBFS · lời đầu 22,8–23,5 s · **nhịp nghỉ: trung vị ≥ 0,6 s, ≤ 25% < 0,4 s** (`qc_pause_gate.py`, A13) |
| 7 | Bảng shot `parse_shots.py` | Phủ 100% câu đúng thứ tự · mọi nền có file · số trên hình có trong câu |
| 8 | **Ảnh tĩnh MỌI shot** `build_video3.py --stills …` | Không lỗi, không đè chữ, không chữ lạ, không lộ mặt (mục 6) |
| 9 | Dựng hình `build_video3.py --workers 6` (~1 giờ / 27 phút video) | `picture.mp4` khớp `timeline.total` ± 0,05 s (đổi audio ⇒ phải chạy lại `parse_shots.py` + dựng lại hình, H14) |
| 10 | Phụ đề + đóng gói `subtitles.py`, `package.py --mux` | Hình = tiếng ± 0,05 s · giải mã 0 lỗi · thumbnail đúng tập · khung cuối có thẻ kết |
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
| K10 | **Hệ sinh thái 10 chỉ dấu tâm lý bắt buộc (tiêu chuẩn A2c):** Kịch bản PHẢI làm rõ: (1) Ảnh hưởng & sự quan tâm xã hội; (2) Cách hung thủ nhìn nạn nhân & vì sao; (3) Cách hung thủ nhìn người thân & chia ngăn; (4) Thái độ trước bản án; (5) Hệ thống tự bào chữa; (6) Ngòi nổ & điểm gãy tâm lý; (7) Dấu ấn Signature vs. Thủ đoạn MO; (8) Quỹ đạo leo thang ảo tưởng; (9) Hiệu ứng hào quang & điểm mù xã hội; (10) Nạn nhân học & cảnh báo đỏ sinh tồn. Tuyệt đối không biến kịch bản thành phóng sự phá án thuần túy |

---

## 4. Giọng đọc — phần dễ sai nhất

> **Higgs Audio v3 trên Kaggle GPU — đã dùng sản xuất Tập 02 (31/10/2026):** khi engine TTS là Higgs trên Cloud/Kaggle, đọc và tuân theo `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` (bản 4) — file đó thay mục này cùng T2, T8, T9. **Mọi quy tắc Higgs CHỈ áp dụng cho Higgs chạy trên Kaggle** (người dùng chốt 02/11/2026); chạy Higgs ở nơi khác = engine mới, phải đo lại và viết quy tắc riêng (Mac: `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`). Ba luật cốt lõi: đo cao độ **trên bản Higgs đọc**, không trên giọng mẫu · G9 xét **mọi cặp vai liền kề, kể cả khác giới** · **CẤM thẻ `<|emotion:…|>`**.
>
> **Higgs Audio v3 trên Mac Apple Silicon — đã dùng sản xuất Tập 04 & 05 EN (02/11/2026):** khi chạy Higgs Audio v3 cục bộ trên Mac (M1/M2/M3/M4), đọc và tuân theo `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md` — kỹ thuật pre-encoding giọng mẫu 1 lần (tiết kiệm 70% thời gian, giải quyết triệt để nghẽn RAM 16GB), tự động cắt tỉa đuôi câm $\ge 0.8\text{ s}$ @ $-45\text{ dBFS}$, kiểm định chất lượng song song bằng Whisper Base (CER) và UTMOSv2 (MOS) trên CPU.
>
> **Tạo giọng mẫu cho Higgs bằng VoxCPM2 (28/10/2026, đã chốt hướng, chưa chạy thử):** đọc `00_TIEU_CHUAN/TAO_GIONG_MAU_VOXCPM2.md` — chứa prompt Voice Design cho 7 vai, cách điền form web, và quy trình đóng gói thành file tham chiếu.
>
> **TÁCH RIÊNG giọng mẫu tiếng Việt và tiếng Anh (31/10/2026, người dùng chốt):** mỗi ngôn ngữ một bộ độc lập — thư mục, dataset Kaggle (`amber-eyes-voice-ref-voxcpm2` / `…-voxcpm2-en`), bảng gán vai (`g9_role_map.json` / `g9_role_map_EN.json`), clip EN mang đuôi `_EN`. **CẤM** chép, đổi tên hay ghi đè clip giữa hai bộ. Chi tiết: `QUY_TAC_AUDIO_HIGGS.md` §4.4.
>
> **Luật + ngưỡng đo cho giọng mẫu VoxCPM2 (29/10/2026):** `00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md` — cổng V1–V8 (CER < 2% **và 0 lỗi thanh điệu**, F0 theo vai, chuẩn WAV 24 kHz −18 LUFS), đo bằng `.work/voxcpm_do_mau.py`, báo cáo bắt buộc trước khi giao.

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
| A7 | Chuẩn hoá `loudnorm I=-16:TP=-1.5:LRA=11`, hai lượt, `linear=true`. **Đo lại trên mp4 cuối**: AAC đẩy true peak lên ~0,1–0,6 dB ⇒ `package.py` đã có `alimiter` giới hạn đỉnh trước khi mã hoá (A11 #38). **Bắt buộc `latency=1`** — thiếu nó thì limiter chèn trễ 5 ms (âm thanh lệch hình) và có thể tạo burst full-scale (A11 #64). **Trước khi ghép, ĐO đỉnh mẫu của master wav**: nếu đỉnh **thấp hơn** trần của limiter thì limiter **không kích hoạt** ⇒ không chắn chắn được true peak ⇒ phải hạ trần (A11 #114). **Chuỗi limiter khai theo tập × NGÔN NGỮ** — bản không phải EN rơi vào chuỗi mặc định thiếu `latency=1` nếu khai `if EN else …` (A11 #114) |
| A8 | **Nguồn SFX thứ 2: Freesound (CC0)** — dùng khi YouTube Audio Library không có track đúng nghĩa (19 mã đang dùng track thay thế, mục 4.2). Công cụ: `.work/freesound_client.py` + `.work/fs_fetch.py` + `.work/fs_provenance.py`. Token auth = cột "Client secret/Api key" của https://freesound.org/apiv2/apply. Chỉ tải được **preview 160 kbps mp3**, KHÔNG tải được file gốc (endpoint `download/` là OAuth2-required). Mọi file phải là **CC0** cho kênh kiếm tiền, và phải **nghe duyệt** trước khi nhập |
| A9 | **Tối ưu ducking và sàn môi trường tập dài (>30 phút):** dùng `np.cumsum` cho đường bao ducking (giảm từ 5 phút xuống 0,05 s); sàn môi trường đặt −31 dB, đuôi piano ấm 7,8 s fade out mượt để tránh lỗi V4 cuối video |
| A10 | **Bed nhạc nền phải khớp kịch bản, không copy pattern của tập khác.** Mỗi hồi lấy mood thẻ `[BGM]` ĐẦU TIÊN của hồi đó trong `01_KICH_BAN/TapXX/` (Hồi 1 lấy tại mốc `act1_cue`). Lỗi đã gặp 25/10/2026: 20/29 tập dùng chung 1 pattern; T09/T16 đòi guitar/organ nhưng bed trỏ piano/cello; 2 track dài nhất (220 s + 196 s) nằm không ai dùng. Kiểm: `py -3 .work/_qc_bgm_bed_start.py` trước khi dựng |
| A11 | **Sửa `edition.py` bằng script: giữ dấu nháy và `import` thật để kiểm.** Mất nháy làm `1: bgm_x.mp3` thành biểu thức thuộc tính — `py_compile` vẫn PASS nhưng lúc chạy sẽ NameError. Vá chỉ giá trị của đúng hồi, không dựng lại cả khối `bed`; luôn sao lưu `.work/_cu/` trước (L5) |
| A12 | **Mã câu trong `EPISODES[*]["summary"]` phải tồn tại trong script — nếu không `package.py --mux` crash `KeyError` (Tập 07, 08)**. Element `1.01` của T07/T08 là thẻ `[BGM]` không có câu thoại nên `1.01#1` không tồn tại (script đã sửa sau lúc dựng). Khi sửa kịch bản phải cập nhật lại `summary`. Kiểm: `.work/_patch_summary_t07.py` quét 29 tập |
| A13 | **Nhịp nghỉ giữa câu PHẢI đo trước khi trộn master — mỗi ngôn ngữ một file diễn xuất có `_pause_after` riêng.** Cổng `py -3 .work/qc_pause_gate.py` (`--pre` trước khi trộn; không cờ = đo `timeline_s_*.json` sau `build_audio3.py`, trong cùng hồi — tiêu chuẩn A4.3b): **trung vị khoảng nghỉ ≥ 0,6 s** và **số chỗ chỉ nghỉ tối thiểu (< 0,4 s) ≤ 25%**. `_pause_after` thường cần **≈ 50–65% số câu** (T04/T05: ~100; T06 viết lại: 135 VN/JA, 162 EN) — **cổng đo mới là chuẩn, số mục chỉ là hệ quả**; giá trị 0,3–0,9 s (TB ~0,45): 0,3 nối ý · 0,4–0,5 hết đoạn · 0,6–0,9 sau câu hé lộ/nặng nề · cuối lượt nói trước khi đổi vai ≥ 0,4. Thiếu file `acting_tapXX_<LANG>.json` ⇒ **DỪNG**, không trộn (máy trộn im lặng coi như 0 khoảng nghỉ). Mã câu sót từ kịch bản cũ cũng bị bỏ qua im lặng ⇒ phải 0 mã lạ. Sửa kịch bản/đổi mã câu ⇒ chuyển `_pause_after` THEO NỘI DUNG, so số mục trước–sau. Công cụ mẫu: `.work/_fix_pause_t06.py` (chuyển theo nội dung + bổ sung đến khi dự đoán đạt cổng) | Tập 06 (07/11/2026): đổi kịch bản 154→212 câu làm `acting_tap06.json` rơi từ 93 xuống **37** chỗ nghỉ; JA **không có file diễn xuất**. Trung vị nghỉ 0,35 s (Tập 05: 0,74 s), 138/207 (VN) và 171/207 (JA) câu dính liền ⇒ người dùng nghe "đọc nhanh, không chậm rãi" dù tốc độ đọc trong câu bằng Tập 05 (3,6 tiếng/s). Mọi cổng LUFS/câm/CER vẫn xanh |

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
| H7 | **Mẫu T5 (con số) chỉ hiện MỘT số / tiêu đề lớn.** Thông tin thêm viết nghiêng. Hai `**…**` sẽ đè lên nhau ("B8ẾN 01 · 2010"). **Mẫu T8 (cờ) chỉ hiện tiêu đề lớn khi caption BẮT ĐẦU bằng số: `*01* · **CẢNH BÁO ĐỎ 1 — …**`** (Tập 07: caption viết tay "Cảnh báo đỏ 1: …" ⇒ chỉ hiện cờ, **mất tiêu đề** — mọi cổng QC vẫn xanh, chỉ thấy khi soi bằng mắt) |
| H8 | **T3 "so sánh"** viết `trái → phải`; **T8 danh sách** đọc mọi đoạn; **T7 bản đồ** có nhãn ghim khai ở `route_pins` của tập (Tập 01 từng viết cứng "SPRINGFIELD/WISCONSIN") |
| H9 | **Ảnh tĩnh MỌI shot trước khi dựng cả tập** (151 ảnh ~2 phút). Một shot lỗi làm hỏng cả lượt dựng ~1 giờ — đã xảy ra |
| H10 | Mỗi shot 3–15 s; tắt bán thân linh thú `⊘` ở khoảnh khắc nặng nề; tránh một nền lặp quá 4 shot liền. **Cả hai vế phải ĐO bằng script, không ước lượng** (`.work/qc_final_t07/_qc_h10_t07.py`: thời lượng từng shot + chuỗi nền liên tiếp) |
| H12 | **Shot cuối (thẻ kết) PHẢI có chữ:** nhãn `HỒ SƠ TẬP XX · ĐÃ ĐÓNG` + tên kênh **AMBER EYES** + khẩu hiệu "Phân tích tâm lý tội phạm / qua những hồ sơ có thật". Cột Chữ của shot cuối không được để "—" (Tập 01 và Tập 02 từng kết thúc bằng tờ giấy trống). Renderer tự phóng to tên kênh ở shot cuối không lời |
| H13 | **Khớp 3 chiều (Ảnh — Chữ — Lời thoại):** Chữ trên hình lấy nguyên văn từ câu thoại đang đọc (H6/V3); ảnh nền phản ánh đúng ngữ cảnh câu đó (H3); vai nói và avatar bán thân khớp 100% kịch bản. Chạy script đối chiếu trước khi dựng |
| H11 | Thumbnail: nền và chữ **của đúng tập** (khoá `thumb`, `thumb_bg`). Tập 02 từng ra thumbnail mang nền nhà Tập 01 |
| H14 | **Đổi audio ⇒ phải dựng lại hình.** Mốc thời gian của bảng shot lấy **chỉ từ `timeline_s.json`**, nên đọc lại giọng / cắt lại nhạc ⇒ chạy lại `parse_shots.py` **rồi** `build_video3.py`. Tập 02 (31/10/2026): audio mới 1411,9 s nhưng `picture.mp4` cũ dài 1554,3 s → lệch tới 142 s và **mất thẻ kết** khi ghép. Cổng trước khi đóng gói: `picture.mp4` khớp `timeline.total` ± 0,05 s + trích khung `timeline.total − 2 s` thấy thẻ kết (tiêu chuẩn A11 #55) |
| H15 | **Renderer phải TẤT ĐỊNH**: cùng 1 shot, chạy 2 lần phải ra **cùng khung hình** (byte-for-byte). Seed của Python theo `hash()` bị ngẫu nhiên hoá theo `PYTHONHASHSEED` mỗi tiến trình ⇒ ảnh tĩnh QC **không** bảo đảm khớp video dựng thật | Dùng `zlib.crc32(shot["id"].encode("utf-8"))` làm seed. Sau khi sửa script dùng chung ⇒ A/B 2 lượt render trên ≥ 6 shot phải cho **6/6 giống byte** (`.work/_ab_pipe_test.py`) + kiểm hồi quy Tập 01 (L9) |
| H16 | **Video chia nhiều chunk ⇒ mỗi chunk BẮT ĐẦU Ở frame CỤC BỘ 0.** Mọi script đọc/so/seek khung hình trong file chunk phải **trừ offset** (`lfi = int(t*FPS) − int(round(--from * FPS))`), nếu không sẽ trích nhầm khung hình của shot khác — lỗi **chỉ lộ ở chunk B/C**, chunk A (offset 0) vẫn đúng nên dễ tưởng script ổn | Tự kiểm bằng shot đầu tiên của chunk: MAE đúng phải **2–6/255** (tổn thất nén H.264), lệch phải **> 15/255**. Sau khi sửa: chunk B **33/33 shot khớp · MAE TB 4,07** (tiêu chuẩn A11 #109) |

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
| T10 | **`mo_ta.txt` / `description.txt` là file SINH RA** bởi `.work/package.py` — sửa tay sẽ bị **ghi đè mất** khi chạy lại pipeline. Muốn đổi mô tả: sửa **generator + `edition.py`** (cấu hình tập), không sửa file thành phẩm | Sửa `.work/package.py` + `.work/edition.py`, chạy lại `AE_EP=XX python .work/package.py` (**KHÔNG** thêm `--mux` nếu không cần ghép lại video). Khoá cấu hình theo tập trong `edition.py`: `title` · `act_titles` · `roles_line` (câu disclaimer vai lời) · `hashtags` (dòng tag cuối). Sau đó **kiểm hồi quy Tập 01** (L9): sinh thử trong bộ nhớ (chặn `Path.write_text`) rồi diff với file trên đĩa |
| T12 | **Dòng hashtag cuối mô tả YouTube chỉ có ở bản EN** (`CHU_CO_DINH_EN.md`); template VN/JA/KO không có ⇒ video tiếng Việt đăng lên không có tag. Đã vá 02/11/2026 cho các tập VN 01–07 | Bộ tag = tag EN của tập + `#TamLyToiPham #PhamVan #HoiTo` (người dùng chốt) · khai ở `EPISODES["XX"]["hashtags"]` · `package.py` đọc khoá đó **chỉ ở nhánh VN**. Sinh lại bằng cách gọi `description()` **trực tiếp** — CLI còn gọi `thumbnail()` ⇒ ghi đè thumbnail đã xuất của tập cũ |
| T11 | **Mốc chương phải đo từ video, không đoán.** `package.py` hardcode `starts = {1: 20.5}` ⇒ mốc Hồi 1 lệch **2 s** so với thẻ "HỒI 01" thật trên màn hình (~22,0 s; intro 22,41 s). Mốc hồi 2–5 lấy từ ACT marker trong `timeline_s*.json` ⇒ đã đúng | Lấy mốc hồi 1 từ `timeline["intro"]` (22,41 s — mọi tập tiếng Việt đều bằng nhau) và **đối chiếu bằng frame trích từ mp4** trước khi đăng. Cổng: thẻ hồi phải hiện **trong ±1 s** của mốc ghi trong mô tả |
| T13 | **`package.py` (nhánh VN) ghi đè `mo_ta.txt` + `nguon_tham_khao.md` bằng khung RỖNG mỗi lần chạy ⇒ nguồn đã điền bị mất.** Đã vá 02/11/2026: `package.py` đọc nguồn thật từ `02_SAN_XUAT/<Tập>/nguon_mo_ta.txt` (khối chèn vào mục 📚 NGUỒN THAM KHẢO của mô tả) + `02_SAN_XUAT/<Tập>/nguon_tham_khao.md` (bảng đối chiếu từng câu). Không có file ⇒ giữ hành vi cũ (khung rỗng), **KHÔNG bịa nguồn** | Mỗi tập mới: tạo 2 file đó trong `EP_DIR` rồi chạy `AE_EP=XX python .work/package.py` (**không** `--mux` nếu không cần ghép lại video). Mô tả YouTube giới hạn **5000 ký tự** ⇒ `nguon_mo_ta.txt` phải rút gọn (1 dòng tên nguồn + URL), bảng đầy đủ để ở `nguon_tham_khao.md`. Kiểm link: `fbi.gov` / `leb.fbi.gov` / `britannica.com` chặn bot (403/WAF) nhưng **mở bình thường bằng trình duyệt** — đừng kết luận "link chết" |
| T14 | **PowerShell 5.1 `Tee-Object` ghi log UTF-16LE** ⇒ đọc log ra ký tự `\x00`; **đừng dùng kích thước file `part_*.mp4` để đo tiến độ** (ffmpeg ghi `mdat` theo lô ⇒ ước lượng sai gấp 2 lần) | Đọc log bằng `encoding="utf-16"` khi có BOM `fffe`; đo tiến độ bằng **bộ đếm khung trong log** (`[part_XX] fi/total`) |
| T15 | **`package.py` sinh lại `mo_ta.txt`/`description.txt` ⇒ có thể XOÁ link nguồn và vượt trần 5.000 ký tự, và không báo lỗi.** Đã dính 03/11/2026: `verified_links()` chỉ hiểu bảng 4 cột trong khi mọi tập EN dùng bảng 3 cột ⇒ mô tả Tập 03 EN mất 24/24 link, thành `[PENDING]` | Trước khi chạy `package.py`: **backup** `mo_ta.txt`/`description.txt` (L5). Sau khi sinh: kiểm khối `📚 SOURCES` **không chứa `[PENDING]`** và **số link == số dòng ✅ trong `nguon_tham_khao_EN.md`**; đo `len()` file ≤ **5.000** ký tự (giới hạn YouTube). Mẫu đo không ghi file: `.work/_dry_desc_len.py` · hồi quy link: `.work/_qc_regress_links.py` (tiêu chuẩn A11 #111, #112) |
| T16 | **ĐỪNG dừng tiến trình mình không spawn mà không xác định được owner.** `Get-Process` chỉ cho `StartTime`, **không** cho biết tiến trình đó thuộc session nào — đã dính 03/11/2026: dừng 6 `ffmpeg` tưởng là rác thừa, hoá ra là worker của lượt render Tập 04 EN chạy song song ⇒ lượt đó crash, mất 4200/7941 khung mỗi part | Trước khi `Stop-Process`: xem **CommandLine** (`Get-CimInstance Win32_Process`) + tệp log mà nó đang ghi. **Không xác định được owner ⇒ để nguyên** (thừa chỉ chậm; giết nhầm thì phá việc người khác). Dùng `task_stop` trên task cha đã biết. **2 session có thể chạy song song trong 1 workspace** (tiêu chuẩn A11 #113) |

| T17 | **File trong `.work/` có thể bị GHI ĐÈ bởi session khác giữa lúc đọc và lúc dùng — phải kiểm hash/mtime ngay TRƯỚC khi mux.** Đã dính 04/11/2026 (Tập 03 JA): đọc `timeline_s_JA_t03.json` lúc 22:24 cho `total` = 1936,71 s; lúc 22:40:06 file bị ghi đè hàng loạt (kèm `build_video3.py`, `edition.py`, `package.py`) ⇒ `total` = 1927,91 s. Lệch **8,80 s** toàn video | Trước khi mux: in **SHA-256 (12 ký tự) + mtime** của `timeline_s_*.json`, `shots_*.json`, `build_video3.py`, `edition.py`, `package.py` ⇒ ghi vào báo cáo. Nếu timeline có nhiều bản ⇒ chọn bản khớp audio master bằng **đo ASR nhiều mốc** (tiêu chuẩn A11 #117). Sau khi đọc lại file đã dùng ⇒ kiểm hash còn nguyên |
| T18 | **Cổng hồi quy so `EPISODES` phải dùng khoá `"%02d" % ep`** — dùng `str(ep)` ⇒ `"3"` ≠ `"03"` ⇒ mọi lần tra trượt ⇒ cổng báo "không khác biệt" **trong khi đã sửa** (tiêu chuẩn A11 #115) | Khoá `EPISODES` luôn là chuỗi 2 chữ số (`"01"`…`"29"`). Cổng hồi quy phải **in giá trị đọc được** và **fail** khi không có khác biệt dù đã kỳ vọng có |
| T19 | **File văn bản sửa bằng script mà không truyền `newline=''` ⇒ CR nhân đôi (`\r\r\n`) ⇒ diff toàn file, mà nội dung vẫn chạy được nên không cổng nào báo lỗi** (Tap04, 05/11/2026): đọc bằng `read_text()`/`open(newline='')` (giữ CRLF) rồi ghi bằng `write_text()`/`open('w')` (tự dịch `\n`→`\r\n` trên Windows) ⇒ mỗi dòng thành `\r\r\n`. Git lưu blob CRLF (không phải LF như repo) ⇒ `git diff` hiện 2684 dòng thay vì 84 dòng thật | Luôn `open(p, encoding='utf-8', newline='')` khi đọc-ghi file văn bản, hoặc chuẩn hoá về LF một lần. **Đo trước khi commit**: `b.count(b'\r\r\n')` phải = 0 và `git diff --stat` phải khớp quy mô thay đổi thật. Sửa: `b.replace(b'\r\r\n', b'\r\n')` + `py_compile` + so nội dung sau khi bỏ hết `\r` |
| T20 | **`timeline_s_*.json` có thể là bản ƯỚC LƯỢNG (theo thời lượng TTS dự kiến) chứ không phải bản ĐO — nên `timeline.total` LỆCH vài giây với master mp3 ⇒ toàn bộ hình trôi tiếng.** Đã dính 06/11/2026 (Tập 03 VN): timeline trong repo có `total` = 1683,72 s nhưng `Tap03_master.mp3` dài **1664,96 s** ⇒ lệch **18,76 s**; câu cuối của timeline kết thúc ở 1674,72 s ⇒ **vượt quá cuối file âm thanh** | **Cổng bắt buộc trước khi dựng**: `timeline.total` phải **bằng đúng** (≤ 0,05 s) thời lượng master mp3 (ffprobe `format=duration`) **VÀ** câu cuối phải kết thúc ≤ cuối audio. Lệch ⇒ **dựng lại timeline từ chính mp3** (đừng tin file cũ). `build_audio3.py` trộn âm thanh bằng đúng công thức ước lượng đó (`FIRST_VOICE 23,0` · `GAP_SENT 0,35` · `GAP_SPEAKER 0,70` · `GAP_ACT 2,0` · `MAX_PAUSE 2,5` · outro +9,0 s) ⇒ timeline mới phải khớp **tuyệt đối** master |
| T21 | **Cổng QC riêng phải DÙNG ĐÚNG QUY TẮC CỔNG DỰ ÁN — tự chế quy tắc thì "xanh" bằng cách ép người làm sửa sản phẩm.** Đã dính 06/11/2026 (Tập 03 VN): cổng tự viết kiểm số trên hình bằng bộ `\d+` ⇒ báo SAI cho `1.600` và `0,13`; cổng dự án `_qc_tap02_shots.py` kiểm `m in allowed or m in flat or tok in allowed` ⇒ **đúng, 0 lỗi**. Tương tự: cổng tự viết so "chữ trên hình phải là trích của câu đang đọc" ⇒ sai 74/110 vì thẻ tiêu đề là **tóm tắt diễn giải** của cả shot, không phải trích câu | **Ngữ cảnh để so là `ctx` = các câu CỦA SHOT** (dòng "giữ" mượn của shot cha; thẻ tiêu đề không có câu ⇒ lấy tên hồi), **không** phải câu đang đọc tại giữa shot. Nhãn cấu trúc (`HỒI/TẬP/NẤC/TẦNG` + số) được miễn kiểm số. Mốc đúng để kiểm "ảnh khớp lời" là: **câu đang đọc tại giữa shot phải thuộc chính shot đó** (Tập 03 VN: 110/110) |
| T22 | **Mốc chương trong `mo_ta.txt` là `mm:ss` — đừng parse nhầm thành `hh:mm`.** Đã dính 06/11/2026: cổng tự viết `ts = h*3600 + m*60` biến `00:23` thành 1380 s ⇒ báo sai lệch 1357 s với câu đầu hồi (thực tế mốc ĐÚNG) | Parse `mm:ss` ⇒ `ts = m*60 + s`. Cổng đúng phải so **dung sai ≤ 2 s** với `start` của câu đầu mỗi hồi trong timeline (Tập 03 VN: 5/5 mốc khớp, `00:23 / 06:02 / 11:32 / 16:44 / 22:07`) |

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

## 11. Dọn đĩa sau khi tập đã đăng

> Lần đầu áp dụng 02/11/2026 cho Tap01 + Tap02 (4 ngôn ngữ): giải phóng **20,1 GB** trên ổ D: (12,7 → 32,8 GB).

- **QUY TẮC**: tập đã upload YouTube xong → xoá media của tập đó khỏi đĩa. Dọn **theo tập × ngôn ngữ**, không dọn "mọi thứ cũ" — mỗi tập chạy song song, xoá nhầm là mất công dựng lại.
- **XOÁ**: `02_SAN_XUAT/TapXX*/xuat_ban/*_master.mp4|mp3` · `thumbnail.png` · `contact_sheet*` · `_qc_frames/` · `thu_giong*/` (mẫu giọng thử) · `.work/video3*` (picture.mp4, part_*.mp4) · `.work/audio_s*` (TTS theo câu) · `.work/stems*` (6 lớp âm thanh) · `.work/audio_master_*_t0X.wav` · `.work/kaggle_higgs/out_higgs_*t0X` (output Higgs TTS) · `.work/_cu/*` bản sao của tập đó · `assets/brand/intro_*_t0X.mov` + `intro_preview*`.
- **GIỮ**: file text của tập (`.md` `.txt` `.srt`) — xoá media **không** được xoá kịch bản/phụ đề · `assets/bg/` (dùng chung 29 tập) · `assets/voice_ref_voxcpm2*/` (thư viện giọng mẫu) · `assets/brand/intro_kenh.mov` + `intro_kenh_EN.mov` (intro gốc, mọi tập dùng lại) · output Higgs và `_cu` của **tập khác**.
- **Đường dẫn trong `.work` theo quy ước**: hậu tố `_EN` `_JA` `_KO` = ngôn ngữ, `_t02` = tập 2, **không hậu tố = tập 1**. Vậy `video3_EN_t02` = Tap02 EN, `video3_KO` = Tap01 KO.
- **Cơ chế xoá trên máy này**: `rm -- "<đường dẫn tuyệt đối>"` → runtime chuyển sang `mavis-trash` (**Recycle Bin**). KHÔNG dùng `Remove-Item`/`del`/script xoá — runtime chặn. KHÔNG gọi `mavis-trash` trực tiếp, và **không `cd` trước lệnh `rm`** (runtime chặn: "cannot be verified safely after a command working directory change").
- **Muốn thật sự giải phóng ổ D: phải dọn Recycle Bin sau đó**: `Clear-RecycleBin -DriveLetter D -Force`. Nó **báo lỗi `The system cannot find the path specified` nhưng vẫn dọn được** → kiểm bằng `Get-PSDrive D` (số GB trống), đừng tin exit code. Dọn Recycle Bin xoá **cả** rác cũ của người dùng trên ổ đó.
- **Sau khi xoá**: `git status` sẽ hiện `D` cho file media đang được track (vd `thumbnail.png`) → **PHẢI commit + push** để repo không bẩn. Thêm luật `.gitignore` `02_SAN_XUAT/Tap0[12]*/xuat_ban/thumbnail.png` để `package.py` chạy lại không track lại.
- **Đừng tin tên thư mục, hãy đọc log**: `.work/kaggle_higgs/out_higgs_prod` chứa file `amber-eyes-higgs-prod-t02-kaggle-gpu.log` → là **Tap02**, không phải Tap01. File `D_clone_d3sh_ko5_t01.wav` có `t01` là **số thứ tự clip**, không phải tập 1.

---

*Khi thêm bài học mới: thêm một dòng vào bảng phù hợp ở đây (ngắn, mệnh lệnh, kèm lỗi đã gặp) **và** vào tiêu chuẩn mục A11.*
