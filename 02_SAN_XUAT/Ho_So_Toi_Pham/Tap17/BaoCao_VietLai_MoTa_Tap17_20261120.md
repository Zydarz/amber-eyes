# BÁO CÁO VIẾT LẠI MÔ TẢ TẬP 17 — 4 NGÔN NGỮ (VI / EN / JA / KO)

**Ngày thực hiện:** 20/11/2026
**Hồ sơ vụ án:** 13 Đứa Trẻ Trong Ngục Tù Ngoại Ô — Kiểm Soát Cưỡng Chế, Ảo Tưởng Điên Cuồng Đôi & Cú Nhảy Sinh Tồn (Hồ Sơ Gia Đình Turpin)
**Mẫu format tham chiếu:** Tập 16 (mẫu mới nhất, dựng 19/11/2026) — cùng cấu trúc với Tập 13–16
**Căn cứ nội dung:** `01_KICH_BAN/Ho_So_Toi_Pham/Tap17/kichban_tap17_23102026.md` (bản 226 câu, 14/11/2026) + `01_KICH_BAN/Ho_So_Toi_Pham/Tap17/REVIEW_kichban_tap17_10chiau.md`
**Quy chuẩn:** `AGENTS.md` (L2/L5/L6/L7, K1–K10) · `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2c, A10 — trần mô tả YouTube ≤ 5.000 ký tự)

> ⚠️ Báo cáo cũ `BaoCao_BoSung_MoTa_Tap17_20261107.md` mô tả bộ mô tả ĐÃ BỊ THAY THẾ bởi lần viết lại này.

---

## 1. VÌ SAO VIẾT LẠI

Bộ mô tả cũ (07/11/2026) lệch với kịch bản hiện hành và lệch format:

| Vấn đề | Bằng chứng |
|---|---|
| **Thân bài bị rút gọn còn 1 đoạn** | Bản VI trong `xuat_ban/` ngày 19/11 chỉ còn 4.175 ký tự — mất hẳn Hệ sinh thái 10 chỉ dấu (K10, tiêu chuẩn A2c) |
| **Mốc chương EN/KO cũ** | Bản EN/KO dùng mốc `05:30 / 11:15 / 17:00 / 22:45` (bản kịch bản cũ) trong khi video đã dựng lại 19/11 ⇒ bấm chương lệch |
| **Header nguồn bị lặp** | `📚 NGUỒN THAM KHẢO` + `📚 TỔNG HỢP NGUỒN THAM KHẢO…` dính liền nhau trong file VI |
| **Thiếu tiêu đề tập** | Bản VI thiếu tiều tố `Tập 17:` (Tập 16 có `Tập 16:`) |
| **Thiếu hashtag ở bản VI/JA/KO** | Chỉ bản EN có dòng tag — video tiếng Việt đăng lên YouTube không có tag nào |
| **`package.py` crash khi đóng gói bản EN** | Thiếu `02_SAN_XUAT/Ho_So_Toi_Pham/Tap17_EN/CHU_CO_DINH_EN.md` ⇒ `description_en()` ném `FileNotFoundError` (video EN 19/11 vẫn ra vì `mux()`/`thumbnail()` chạy trước) |

## 2. CẤU TRÚC MÔ TẢ MỚI (giống hệt Tập 16)

```
{tiêu đề} | Amber eyes
→ đoạn dẫn (bối cảnh + dữ kiện nhân vật)
→ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (10 mục đánh số, nhãn IN HOA)
→ ⏱ MỐC CHƯƠNG (00:00 + 5 hồi, mốc đo thật)
→ ⚠️ LƯU Ý PHÁP LÝ & AN TOÀN (3 gạch đầu dòng)
→ 📚 NGUỒN THAM KHẢO CHÍNH THỨC (5 mục: nhãn ngắn + URL)
→ 🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ (3–4 số)
→ dòng hashtag
```

Tên khối theo ngôn ngữ: VI `⏱ MỐC CHƯƠNG / ⚠️ LƯU Ý PHÁP LÝ & AN TOÀN / 📚 NGUỒN THAM KHẢO CHÍNH THỨC / 🆘 ĐƯỜNG DÂY NÓNG HỖ TRỢ` · EN `⏱ CHAPTER TIMESTAMPS / ⚠️ LEGAL & SAFETY ADVISORY / 📚 OFFICIAL SOURCES / 🆘 CRISIS & PROTECTION HOTLINES` · JA `⏱ タイムスタンプ / ⚠️ 免責事項・安全基準 / 📚 公式参考文献 / 🆘 緊急相談窓口` · KO `⏱ 챕터 타임스탬프 / ⚠️ 법적 고지 및 콘텐츠 안내 / 📚 공식 참고 문헌 / 🆘 아동 보호 및 가정폭력 긴급 지원 핫라인`.

## 3. ĐO LƯỜNG THẬT (không ước lượng)

Đo bằng `py -3 .work/_qc_desc_t17.py` trên file đã ghi trên đĩa:

| Ngôn ngữ | File kiểm tra | Số ký tự | Trần | Trạng thái |
|---|---|---:|:---:|:---:|
| **VI** | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap17/mo_ta.txt` + `xuat_ban/mo_ta.txt` | **4.985** | ≤ 5.000 | **PASS** |
| **EN** | `Tap17_EN/description.txt`, `mo_ta.txt`, `xuat_ban/*` | **4.968** | ≤ 5.000 | **PASS** |
| **JA** | `Tap17_JA/description.txt`, `mo_ta.txt`, `xuat_ban/*` | **2.559** | ≤ 5.000 | **PASS** |
| **KO** | `Tap17_KO/description.txt`, `mo_ta.txt`, `xuat_ban/*` | **2.937** | ≤ 5.000 | **PASS** |

14/18 file mô tả + 4 file khối nguồn — **tất cả PASS**, không file nào vượt trần.

### 3.1. Nguồn số liệu mốc chương

| Ngôn ngữ | Nguồn | Hồi 1–5 |
|---|---|---|
| VI | `.work/timeline_s_t17.json` (đo thật) | 00:23 / 06:22 / 12:52 / 19:16 / 26:37 (tổng 33:47) |
| EN | `.work/timeline_s_EN_t17.json` (đo thật) | 00:23 / 05:22 / 11:06 / 16:51 / 23:07 (tổng 28:59) |
| JA | `.work/timeline_s_JA_t17.json` (đo thật) | 00:23 / 06:22 / 12:58 / 20:03 / 27:46 (tổng 35:00) |
| **KO** | **ƯỚC LƯỢNG** — audio KO chưa dựng | 00:23 / 08:09 / 16:51 / 25:31 / 35:11 (tổng ≈ 44:00) |

Cách hiệu chuẩn mốc KO: tỉ trọng ký tự lời thoại theo từng hồi (đo trên `kichban_tap17_KO.md`) × tốc độ đọc hiệu chuẩn từ timeline JA đã đo thật. Kiểm chéo bằng tỉ lệ KO/VI đo được ở Tập 02 (1,2863) ⇒ 43:27, khớp với ước lượng 44:00 (sai số ≈ 1,3 %).
**⇒ Khi dựng xong audio KO phải chạy lại `.work/make_descriptions_t17.py` để mốc chương KO thành số đo thật.**

### 3.2. QC sạch ngôn ngữ

`py -3 .work/_qc_lang_purity_t17.py` — chặn ký tự lạn quốc / ngôn ngữ trộn trong 4 thân bài:

| Bản | Ký tự | Mục chỉ dấu | Kết quả |
|---|---:|:---:|:---:|
| VI | 2.815 | 10/10 | SẠCH |
| EN | 2.974 | 10/10 | SẠCH |
| JA | 1.336 | 10/10 | SẠCH |
| KO | 1.606 | 10/10 | SẠCH |

(Bản dự thảo đầu có lẫn Cyrillic/Hán tự trong thân bài JA và KO ⇒ đã viết lại, QC bắt được trước khi xuất bản.)

## 4. NỘI DUNG 10 CHỈ DẤU — CĂN CỨ KỊCH BẢN HIỆN HÀNH

Đối chiếu `REVIEW_kichban_tap17_10chiau.md` (14/11/2026) — bản mô tả cũ dùng bảng 10 chỉ dấu của kịch bản **cũ (210 câu, 07/11)**:

| # | Chỉ dấu | Điểm mới so với bản cũ |
|---|---|---|
| 1 | Dư chấn xã hội & cải cách thể chế | Gắn vụ án với phiên điều trần lập pháp siết giám sát trường tư thục tại gia |
| 2 | Vật hóa & phi nhân hóa nạn nhân | "Đạo cụ sống" + nghi thức tra tấn tâm lý bằng thức ăn/đồ chơi |
| 3 | Nghịch lý chia ngăn | Kỹ sư quốc phòng ban ngày ↔ kẻ giam cầm ban đêm (chia ngăn **cực đoan**) |
| 4 | Thái độ trước bản án | Tự thương hại bệnh lý + **ngụy biện tâm linh** ("Chúa có kế hoạch đặc biệt cho các con") |
| 5 | Hệ thống tự bào chữa & trung hòa đạo đức | Ngắt kết nối đạo đức thay vì chỉ "tự khoác áo thiên thần" |
| 6 | Ngòi nổ & điểm gãy | Gồm cả phía nạn nhân: nguy cơ em nhỏ tử vong kích hoạt bản năng sinh tồn |
| 7 | Dấu ấn Signature vs. thủ đoạn MO | MO = trường tư thục tại gia / rèm tối / đảo ngày đêm; Signature = đồ đồng phục, dàn ảnh Las Vegas |
| 8 | Quỹ đạo leo thang | Chu kỳ mắng mỏ → úp mặt tường → nhốt phòng → dây thừng → xích + ổ khóa |
| 9 | Hiệu ứng hào quang & điểm mù xã hội | Đóng kín cửa + tôn trọng quyền riêng tư thái quá ⇒ bức tường vô hình |
| 10 | Nạn nhân học & cảnh báo đỏ sinh tồn | Thêm cơ chế tha thứ như **giải phóng cảm xúc** + **Tăng trưởng sau sang chấn (PTG)**; nêu tường minh 4 cảnh báo đỏ |

Dữ kiện nhân vật dùng trong mô tả đều có trong kịch bản: Jordan Turpin 17 tuổi · cuộc gọi 911 dài 20 phút bằng điện thoại đã ngắt dịch vụ · David Turpin 56 tuổi (kỹ sư máy tính, từng làm cho tập đoàn quốc phòng) · Louise Turpin 49 tuổi · 7 người con là người trưởng thành 18–29 tuổi · chị cả 29 tuổi nặng ~37 kg · Sandcastle Day School · ảnh Disneyland / lễ thề hôn nhân Las Vegas · cáo trạng 18/01/2018 · thỏa thuận nhận tội 22/02/2019 · tuyên án 19/04/2019 (25 năm đến chung thân, Thẩm phán Bernard Schwartz) · phỏng vấn ABC News 20/20 (11/2021).

## 5. FILES ĐÃ THAY ĐỔI

**Sinh lại (nguồn duy nhất: `.work/make_descriptions_t17.py`)**
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap17/mo_ta.txt`, `xuat_ban/mo_ta.txt`, `nguon_mo_ta.txt`
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap17_EN/{description.txt, mo_ta.txt, xuat_ban/description.txt, xuat_ban/mo_ta.txt, nguon_mo_ta_EN.txt}`
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap17_JA/{description.txt, mo_ta.txt, xuat_ban/*, nguon_mo_ta_JA.txt}`
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap17_KO/{description.txt, mo_ta.txt, xuat_ban/*, nguon_mo_ta_KO.txt}`

**Tạo mới**
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap17_EN/CHU_CO_DINH_EN.md` — mẫu mô tả EN (thiếu file này ⇒ `package.py` crash; header `📚 SOURCES` để `package.py` thay khối nguồn tại chỗ, không chèn thêm ⇒ vẫn ≤ 5.000).
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap17_EN/nguon_tham_khao_EN.md` — chuyển sang bảng ✅ (định dạng Tập 16) để `verified_links()` lấy được link thật.

**Cấu hình**
- `.work/edition.py` → `EPISODES["17"]`: thêm `title` có tiều tố `Tập 17:` (VI) / `제17화:` (KO), `act_titles` khớp mô tả, `hashtags` + `hashtags_en/ja/ko`, `summary_vn/summary_ja/summary_ko` = thân bài 10 chỉ dấu ⇒ lần chạy `package.py` sau **không xoá mất** nội dung (A11 #70).
- `provenance.json` — thêm 19 dòng cho các tài sản mô tả (L7).
- Sao lưu bản cũ: `.work/_cu/desc_t17_rewrite/`, `.work/_cu/edition_t17_desc_sync.py`.

## 6. KIỂM CHỨNG LẠI LẦN CHẠY PIPELINE SAU

`py -3 .work/_qc_pkg_desc_t17.py` — gọi thẳng `package.description()` cho Tập 17 (không gọi CLI để khỏi ghi đè `thumbnail.png`, A11 #72):

| Ngôn ngữ | Kết quả `package.description()` | Giữ được mục 10 | ≤ 5.000 |
|---|---|:---:|:---:|
| VI | 4.791 ký tự | ✅ | ✅ |
| EN | 4.617 ký tự | ✅ | ✅ |
| JA | 2.680 ký tự | ✅ | ✅ |
| KO | `edition.py` dừng sớm — chưa có bộ giọng Hàn qua G8–G10 (tập KO chưa dựng) | — | — |

## 7. VIỆC CÒN LẠI (KHÔNG LÀM TRONG LƯỢT NÀY)

1. **Audio KO chưa dựng** ⇒ mốc chương KO là ước lượng; chạy lại `.work/make_descriptions_t17.py` sau khi có timeline KO để thay bằng số đo thật.
2. **Chưa đăng video** — mô tả đã sẵn sàng để dán vào YouTube Studio cho 4 kênh ngôn ngữ.
3. Khi đăng: bật "Nội dung bị thay đổi hoặc tổng hợp" · "Không dành cho trẻ em" · danh mục Giáo dục (A10).
