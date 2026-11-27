# BÁO CÁO CẬP NHẬT PHẦN MÔ TẢ TẬP 25 — 4 NGÔN NGỮ (VN / EN / JA / KO)

**Ngày:** 26/11/2026 · **Tập:** 25 — Yoo Young-chul (Sát nhân áo mưa) · **Công cụ:** `.work/make_descriptions_t25.py`
**Mẫu chuẩn tham khảo:** `.work/make_descriptions_t24.py` (Tập 24 — bản mô tả đầy đủ nhất trong kho)

---

## 1. Vì sao phải sửa (bằng chứng)

| Vấn đề | Bằng chứng đo được |
|---|---|
| Bản EN/JA/KO **quá mỏng** — không có đoạn dẫn, không có 10 chỉ dấu, không có tên nguồn | `Tap25_EN/mo_ta.txt` cũ = **1.921 ký tự**, dòng mở đầu là câu chung *"Criminal psychology documentary analysis through real forensic case files."* — không nói gì về vụ án. `Tap24_EN/mo_ta.txt` = 4.867 ký tự, có đủ 10 chỉ dấu + nguồn. |
| **Tiêu đề JA/KO bị sai** — lấy nhầm tiêu đề *kịch bản* thay vì tiêu đề *video* | JA cũ: `第25話 · 詳細台本：…` ("chi tiết kịch bản"), KO cũ: `26화 · 범죄심리 오디오 / 팟캐스트 스크립트 상세` — người xem thấy "kịch bản" thay vì tên tập. |
| **Mốc chương là bộ ước lượng tròn** ⇒ lệch hồi trong video thật 34,1 phút | Cũ (cả 4 ngôn ngữ): `00:23 / 05:00 / 10:00 / 15:00 / 20:00`. Video thật: `Tap25_master.mp3` **2048,6 s (34,1 phút)**, 230 câu Higgs. ⇒ "15:00" rơi vào **Hồi 3** (thực tế 13:22), "20:00" rơi vào **Hồi 4** (thực tế 21:09). |
| Bản VN thiếu khối **10 chỉ dấu tâm lý** (K10/§A2c) mà tập trước đều có | `Tap25/mo_ta.txt` cũ = 4.519 ký tự, không có mục nào dạng "1. … 10. …"; `Tap24/mo_ta.txt` có đủ. |
| Thiếu khối nguồn riêng cho JA/KO | `Tap25_JA/nguon_mo_ta_JA.txt`, `Tap25_KO/nguon_mo_ta_KO.txt` **không tồn tại** (Tập 24 có) ⇒ `package.py` không lấy được nguồn khi sinh lại mô tả. |

---

## 2. Mốc chương ĐO THẬT (đo từ file thành phẩm)

| Hồi | VN (CanNghe) | EN (SRT) | JA (SRT) | KO |
|---|---|---|---|---|
| Intro | 00:00 | 00:00 | 00:00 | 00:00 |
| Hồi 1 | 00:23 | 00:25 | 00:23 | 00:23 *(tạm)* |
| Hồi 2 | 07:40 | 07:25 | 08:30 | 07:40 *(tạm)* |
| Hồi 3 | 13:22 | 13:07 | 15:10 | 13:22 *(tạm)* |
| Hồi 4 | 21:09 | 21:40 | 24:02 | 21:09 *(tạm)* |
| Hồi 5 | 28:09 | 28:49 | 32:13 | 28:09 *(tạm)* |

- **VN**: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap25/xuat_ban/CanNghe_Tap25_higgs.md` — 230 dòng, mốc từng câu (`0:23.00 | 1.02#1 | H`) ⇒ lấy câu đầu mỗi hồi.
- **EN / JA**: khớp câu mở đầu hồi trong kịch bản với cue đầu tiên trong `xuat_ban/Tap25_EN.srt` / `Tap25_JA.srt`.
- **KO**: **chưa có master** ⇒ mọc tạm theo VN. **PHẢI đo lại** khi dựng xong audio KO.
- Công cụ: `.work/_act_times_t25.py` → `.work/_act_times_t25.json`.

---

## 3. Chuẩn áp dụng (theo Tập 24)

Mỗi bản mô tả gồm 8 khối: **tiêu đề bản địa hoá + thương hiệu** → **đoạn dẫn lấy nguyên văn từ kịch bản** (1.02#1 + 3.02#1) → **Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (§A2c)** → **mốc chương** → **khối miễn trừ trách nhiệm** → **khối nguồn có tên + link** → **đường dây nóng hỗ trợ bản địa hoá** → **hashtag riêng theo tập**.

Nội dung 10 chỉ dấu rút từ chính kịch bản Tập 25 (Hồi 3 + Hồi 5):
1. Ảnh hưởng xã hội · 2. Vật hóa nạn nhân · 3. Người thân & chia ngăn · 4. Thái độ trước bản án · 5. Hệ thống tự bào chữa · 6. Ngòi nổ & điểm gãy tâm lý · 7. Signature vs. MO · 8. Leo thang ảo tưởng · 9. Hào quang & điểm mù xã hội · 10. Nạn nhân học & 4 cảnh báo đỏ sinh tồn.

4 cảnh báo đỏ (Hồi 5): đổ lỗi & ganh ghét thành công người khác · phân biệt đối xử với phụ nữ và người yếu thế · nhận dịch vụ ở nơi kín đáo không có người thứ ba giám sát · lời đe dọa mang tính phán xét đạo đức.

---

## 4. File đã ghi (19 file)

| Thư mục | File | Ký tự |
|---|---|---|
| `Tap25/` | `mo_ta.txt`, `xuat_ban/mo_ta.txt` | 4.959 |
| `Tap25/` | `nguon_mo_ta.txt` (khối nguồn đầy đủ) | 1.445 |
| `Tap25_EN/` | `description.txt`, `mo_ta.txt`, `xuat_ban/description.txt`, `xuat_ban/mo_ta.txt` | 4.960 |
| `Tap25_EN/` | `nguon_mo_ta_EN.txt` (mới) | 1.473 |
| `Tap25_JA/` | `description.txt`, `mo_ta.txt`, `xuat_ban/description.txt`, `xuat_ban/mo_ta.txt` | 3.064 |
| `Tap25_JA/` | `nguon_mo_ta_JA.txt` (mới) | 702 |
| `Tap25_KO/` | `description.txt`, `mo_ta.txt`, `xuat_ban/description.txt`, `xuat_ban/mo_ta.txt` | 3.435 |
| `Tap25_KO/` | `nguon_mo_ta_KO.txt` (mới) | 732 |

**Không ghi đè** `nguon_tham_khao*.md` của cả 4 ngôn ngữ (bảng đối chiếu dữ kiện đã kiểm chứng) — đã kiểm lại sau khi sinh: vẫn nguyên 40 dòng bảng (VN/EN/JA) và 32 (KO).

**Sao lưu bản cũ:** `.work/_cu/mo_ta_t25_20261126/` (15 file) — `.work/_backup_mota_t25.py`.

---

## 5. Kiểm tra đã chạy

| Cổng | Kết quả |
|---|---|
| Độ dài ≤ 5.000 ký tự (giới hạn YouTube) | VN 4.959 · EN 4.960 · JA 3.064 · KO 3.435 — **4/4 PASS** |
| Mốc chương trong file = mốc đo được | 4/4 khớp |
| Quét ký tự rác trong JA/KO (Latin lạn, Hán tự Trung lạn) | JA: chỉ còn thuật ngữ hợp lệ (Narcissistic Injury, Moral Vigilante Delusion, God Complex, Signature…) · KO: **0 Hán tự** (đã bỏ "서울地方警察청" → "서울 경찰청") |
| Số mục 10 chỉ dấu trong 4 bản | 4/4 đủ 10 |
| Link trong khối nguồn | VN 6 · EN 6 · JA 5 · KO 5 — **không bịa nguồn mới** (L2) |

---

## 6. Thứ tự vận hành (A11 #70, #195)

`mo_ta.txt` / `description.txt` là **file SINH RA**. `package.py` và `generate_all_descriptions.py` sẽ ghi đè bằng mẫu cũ (mẫu tròn 5 phút + không có 10 chỉ dấu). Vì vậy:

```
py -3 .work/make_descriptions_t25.py      ← chạy SAU CÙNG, sau mọi bước package/generate
```

Nếu phải chạy lại pipeline → chạy lại lệnh trên để khôi phục mô tả đầy đủ.

## 7. Việc còn lại (chưa làm)

1. **KO chưa có master** ⇒ mốc chương KO đang mượn của VN ⇒ **đo lại** khi dựng audio KO, rồi chạy lại `make_descriptions_t25.py`.
2. `generate_all_descriptions.py` (mục "25") vẫn chứa bộ nguồn cũ có câu mô tả phương thức gây án; nếu chạy lại script này sẽ ghi đè `nguon_mo_ta.txt` — cân nhắc đồng bộ khối nguồn trong script cho khớp.
3. `KeHoach_Video_Tap25.md` trong thư mục sản xuất **đang sai (còn nội dung Richard Ramirez + số đo `****` trống)** — không thuộc phạm vi lượt này nhưng cần sửa riêng.

## 8. Bài học đã ghi

`00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` — **A11 #195**: mốc chương trong mô tả YouTube phải đo từ file thành phẩm, không dùng bộ ước lượng tròn.
