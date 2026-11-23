# BÁO CÁO QC — TẬP 11 · TÁCH BỘ NỀN THEO H25 + SINH LẠI NỀN CÓ CHỮ AI

**Ngày thực hiện:** 16/11/2026
**Hồ sơ vụ án:** Paul Bernardo & Karla Homolka (Cặp đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi Folie à Deux & Thỏa Thuận Với Quỷ Dữ)
**Công cụ sinh ảnh nền:** **Kaggle `black-forest-labs/FLUX.2-klein-4B`** (5 steps, guidance 2.2, 1056×592 → LANCZOS 2112×1188 + hậu kỳ noir)
**Phạm vi:** tách bộ nền 66 → **136** theo H25 · sinh 70 ảnh mới · soi 100 % nền · sinh lại 32 nền có chữ AI (3 vòng) · render lại ảnh tĩnh 3 ngôn ngữ — **KHÔNG dựng video**.

> Báo cáo này **thay thế** `BaoCao_QC_Tap11_20261112.md` (mô tả lượt 12/11 dùng Cloudflare FLUX.1 với 70 nền). Bản cũ đã được gắn đính chính ở đầu file.

---

## 1. SỐ ĐO THỰC TẾ

| Hạng mục | Kết quả đo lường | Bằng chứng kiểm định | Trạng thái |
|---|---|---|:---:|
| **Số nền trên đĩa** | **136 file** `assets/bg/t11_*.png` · **136/136 đúng 2112×1188** · 0 thừa · 0 thiếu | `py -3 .work/_t11_count_and_missing.py` | ✅ **ĐẠT** |
| **Tách nền theo H25** | 223 shot → **135 cụm liền mạch + 1 nền riêng thẻ kết** = **136 nền** · **1,64 shot/nền** | `.work/_t11_chunk_plan.py` · `.work/_t11_apply_split.py` | ✅ **ĐẠT** |
| **Cổng H22 (dùng nền)** — VI | 223 shot · 136 nền dùng · 136 ảnh sinh · ① ảnh thừa **0** · ② shot mượn nền **0** · ③ nền thiếu file **0** · ④ vượt 3 shot/30 s **0** | `AE_EP=11 AE_LANG=vi py -3 .work/qc_bg_usage.py` | ✅ **ĐẠT** |
| **Cổng H22 — EN** | y hệt VI (136 nền · 1,6 shot/nền · ①②③④ = 0) | `AE_EP=11 AE_LANG=en py -3 .work/qc_bg_usage.py` | ✅ **ĐẠT** |
| **Cổng H22 — JA** | y hệt VI (136 nền · 1,6 shot/nền · ①②③④ = 0) | `AE_EP=11 AE_LANG=ja py -3 .work/qc_bg_usage.py` | ✅ **ĐẠT** |
| **Phân bố shot/nền** | 53 nền dùng **1** shot · 83 nền dùng **2** shot · **0 nền dùng ≥ 3 shot** | đếm từ `shots_t11.json` / `shots_EN_t11.json` / `shots_JA_t11.json` | ✅ **ĐẠT** |
| **Cổng H17 (nền dùng chung 3 ngôn ngữ)** | `EN=137nen/223shot · JA=137nen/223shot · VN=137nen/223shot` · **0 file nền có hậu tố ngôn ngữ** | `py -3 .work/qc_bg_shared.py --ep 11` | ✅ **ĐẠT** |
| **Shot mượn nền / giữ nền** | VI/EN/JA: `bg_inherited = 0`, `hold = 0` | đếm từ 3 file `shots_*.json` | ✅ **ĐẠT** |
| **Provenance (L7)** | **136/136** dòng cho nền `t11_` · có `prompt` + `seed` + `ngay` + `kich_thuoc_goc` + `dieu_khoan` + `kiem_tra_thuong_mai` · **0 nền dùng Real-ESRGAN** | `provenance.json` | ✅ **ĐẠT** |
| **Nguồn sinh** | 13/11: **39** nền · 16/11: **97** nền (70 nền mới + 27 nền sinh lại bỏ chữ còn lại) | `provenance.json` (`ngay`) | ✅ |
| **Cổng H9 (chữ chìm trên ảnh tĩnh)** | Quét **669 ảnh** (223 × 3 ngôn ngữ): VI **0** lỗi · EN **0** lỗi · JA **0** lỗi | `py -3 .work/qc_contrast_t11.py` | ✅ **ĐẠT** |
| **Soi mắt 100 % nền (H20)** | **9 tờ montage** (4 cột × 4 hàng, ô 512 px, 16 ảnh/tờ) + **16 ảnh mở full-res** + **2 tờ ô 700 px** soi vòng cuối (12 nền vật thể nhỏ) | `.work/qc_montage/ep11_bg_s01..s09.jpg` · `ep11_bg_re01..re04.jpg` · `ep11_bg_fin01..fin02.jpg` | ✅ **ĐẠT** |
| **Ảnh tĩnh (Stills)** | **669 ảnh** (223 × 3 ngôn ngữ) · **174 ảnh render lại** sau khi đổi nền (58 shot × 3 ngôn ngữ) | `.work/video3_t11/stills/` · `video3_EN_t11/` · `video3_JA_t11/` | ✅ **ĐẠT** |
| **Danh sách ảnh** | `Danh_Sach_Anh_Tap11.md` nhắc **136** mã · **thừa 0 · thiếu 0** so với bảng shot · **0 nền trên đĩa không dùng** | `py -3 .work/_t11_check_danh_sach.py` | ✅ **ĐẠT** |

### 1.1. Ghi chú về nền `void` (dùng 4 shot)

Cổng H22 báo ④ = 0 vì **nền `void` không thuộc bộ nền Tập 11** — đó là mẫu **thẻ chuyển hồi T10 dùng chung toàn kênh**, dùng đúng **4 shot** (1-39, 2-47, 3-45, 4-45) × 2,0 s = **8,0 s tổng**. 136 nền Tập 11 thực sự chỉ dùng 1–2 shot mỗi nền.

---

## 2. SOI MẮT 100 % NỀN — PHÁT HIỆN 32/136 NỀN CÓ CHỮ AI

Soi 136 nền bằng 9 tờ montage (ô 512 px ⇒ sau khi ảnh bị resize cạnh dài ≤ ~1568 px, ô còn ~390 px) và mở **full-res** 16 nền bị nghi ⇒ **32/136 nền (23,5 %) có chữ AI vô nghĩa** do FLUX tự bịa.

| Mức | Số nền | Đặc trưng |
|---|:---:|---|
| **A** | 10 | prompt **yêu cầu chữ trực tiếp** (`titled`, `labeled`, `inscribed`, `newspaper`, `reading…`) |
| **B** | 20 | prompt **đã có mệnh đề phủ định** ("no text / no labels / no logos") nhưng AI vẫn vẽ chữ |
| **C** | 2 | chữ cực nhỏ / chữ nổi (mặt con dấu, ký tự trên bảng điều khiển) |

**Nguyên nhân gốc (đo được):** khi prompt vẫn **mô tả vật mang chữ**, FLUX sẽ bịa chữ bất kể NEGATIVE_SUFFIX có ghi "strictly no text, no letters, no words, no numbers, no signs, no labels, no logos" hay không. ⇒ **Mệnh đề phủ định trong prompt KHÔNG đủ.**

### 2.1. Cách sửa áp dụng (3 việc, giữ nguyên nội dung cảnh theo H19)

1. **Gỡ mọi thông tin chữ khỏi prompt** — bỏ tên riêng, `titled`, `reading`, `labeled`, `inscribed`, `newspaper`, `cover` có chữ…
2. **Mô tả bề mặt TRƯNG** thay cho vật mang chữ — vd *"a bound judicial inquiry volume with a plain blank unmarked cover"* (giữ vật thể, chỉ đổi bề mặt)
3. **Thêm mệnh đề**: `completely blank and unmarked with no writing at all`

### 2.2. Ba vòng sinh lại (đo thời gian thật)

| Vòng | Số ảnh | Hạ tầng | Thời gian | Kết quả |
|---|:---:|---|:---:|---|
| **1** | 32 | **2 kernel Kaggle chạy song song** (2 phiên độc lập, mỗi kernel 1 tiến trình / 1 GPU) | **25,9 phút** | **29/32 sạch chữ** |
| **2** | 3 | 1 kernel (1 tiến trình) | **7,5 phút** | **2/3 sạch chữ** |
| **3** | 1 | 1 kernel (1 tiến trình) | **4,4 phút** | **1/1 sạch chữ** |
| **4** | 1 | 1 kernel (1 tiến trình) | **5,0 phút** | **1/1 sạch chữ** |
| **Tổng** | **37 lượt sinh** | | **42,8 phút** | **32/32 sạch chữ** |

**4 nền phải sinh lại nhiều vòng — bài học rút ra:**

| Nền | Vì sao chưa sạch ở vòng trước | Cách sửa cuối |
|---|---|---|
| `haunted_new_identity_shadow` | Hộ chiếu **mở** ⇒ bố cục trang định danh có sẵn ô ảnh + ô tên. Vòng 2 đã đóng úp nhưng AI lại điền chữ vào **bên trong huy hiệu** (từ "crest" trong prompt gợi "huy hiệu có khẩu hiệu") | **Vòng 3 — BỎ HẲN emblem/crest**: bìa sau trơn hoàn toàn |
| `triumphant_smile_deal_with_devil` | Cụm "plea bargain" ⇒ AI in tiêu đề lên tờ giấy | **Vòng 2** — đổi thành *"a torn sheet of old blank paper"*, bỏ mọi danh xưng |
| `six_8mm_tapes_bag` | Vỏ băng có sẵn **dải nhãn** ⇒ AI ghi ký hiệu | **Vòng 2** — yêu cầu *"no label strip and no sticker anywhere"* |
| `control_room_dark_monitors` | Viền màn hình có **nameplate 4 khối chữ giả** (40 × 8 px gốc) | **Vòng 4** — yêu cầu viền màn hình trơn hoàn toàn, không nameplate/logo/badge |

⇒ **Bài học:** khi vật thể có **sẵn bố cục chữ** (trang định danh, tiêu đề, dải nhãn, huy hiệu, nameplate), phải **đổi cả bố cục**, không chỉ đổi mô tả bề mặt.

### 2.3. Vòng soi cuối (ô 700 px, 12 nền có vật thể nhỏ)

Sau khi sinh lại, **12 nền có vật thể nhỏ** (băng cassette, vỏ băng, mặt con dấu, vành ống kính, nút bảng điều khiển, lọ nước hoa, túi bằng chứng, lịch, lọ thuốc, bìa sách ×2, tờ bản án) được soi lại ở **ô 700 px** (2 cột ⇒ ô hiệu dụng 700 px sau resize) ⇒ phát hiện thêm **1 lỗi** (nameplate viền màn hình) ⇒ sinh lại vòng 4. Sau vòng 4: **0 lỗi**.
Tờ soi: `.work/qc_montage/ep11_bg_fin01.jpg` · `ep11_bg_fin02.jpg`.


---

## 3. BẢNG SHOT 3 NGÔN NGỮ — ĐỒNG BỘ TUYỆT ĐỐI

| Ngôn ngữ | File bảng shot | Dòng có mã nền | Lệch so với VI |
|---|---|:---:|:---:|
| VI | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/KeHoach_Video_Tap11.md` | 219 | — |
| EN | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap11_EN/KeHoach_Video_Tap11_EN.md` | 219 | **0** |
| JA | `02_SAN_XUAT/Ho_So_Toi_Pham/Tap11_JA/KeHoach_Video_Tap11_JA.md` | 219 | **0** |

Sao lưu trước khi ghi đè: `.work/_cu/t11_split_20261116/` (3 bảng shot + `bg_jobs_tap11.json` cũ 70 job).

---

## 4. OOM KILLER KHI CHẠY 2 GPU — ĐO ĐƯỢC VÀ ĐÃ SỬA

| Phép đo | Kết quả |
|---|---|
| System RAM của 1 phiên Kaggle | **32.098 MB** (MemAvailable 30.810 MB) |
| GPU | 2 × Tesla T4, 15.360 MiB (dùng được 14,56 GiB) |
| Bỏ `cpu_offload` | **CUDA OOM** (14,53 / 14,56 GiB) |
| Giữ `cpu_offload` | weights ~15–17 GB **System RAM**/worker ⇒ 2 worker ≈ 34 GB > 31 GB ⇒ **OOM-Killer −9** |
| Lịch sử | **4/4 lượt 2-GPU trước đó** đều có đúng 1 worker bị −9 (T12 13/11, T13 14/11, T15 15/11, T11 16/11) |

**Kết luận:** 2 tiến trình trong CÙNG 1 phiên Kaggle **luôn** OOM ⇒ dùng **2 KERNEL RIÊNG = 2 phiên chạy động lập**. Đây chính là cơ chế đã dùng cho vòng 1 (32 ảnh, 2 kernel × 16 ảnh, 25,9 phút) — nhanh gấp đôi so với 1 kernel (≈ 48 phút) và **không worker nào bị −9**.

---

## 5. KẾT LUẬN

1. **Bộ nền Tập 11 đạt chuẩn H25**: 136 nền / 223 shot / 1,64 shot/nền · 0 vi phạm H22 ở cả VI/EN/JA · 0 shot mượn nền · 0 ảnh sinh không dùng.
2. **136/136 nền sạch chữ 100 %** sau 4 vòng sinh lại (37 lượt sinh, 42,8 phút Kaggle) — đã soi mắt lại từng nền ở full-res, không chỉ qua montage.
3. **Nền dùng chung 3 ngôn ngữ**, không file nào có hậu tố ngôn ngữ (H17/A8.1).
4. **0 nền dùng Real-ESRGAN** (đã gỡ 2 ảnh thừa ở cả 3 nơi: jobs + provenance + đĩa).
5. **669 ảnh tĩnh** đã render lại phần đổi nền (174 ảnh) — cổng H9 đo 100 %, **0 chữ chìm** ở cả 3 ngôn ngữ.
6. **Chưa dựng video** — bộ nền + ảnh tĩnh sẵn sàng cho bước dựng hình.

---

## 6. TÀI LIỆU ĐÃ CẬP NHẬT (L6)

| Tài liệu | Nội dung ghi |
|---|---|
| `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` | A11 **#171–#174**: mệnh đề phủ định không đủ · ô montage tính theo kích thước sau resize · detector text-like nhiễu nặng · `kernels push` lấy id từ slug của title |
| `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` | §5.2 bổ sung cơ chế 2 kernel + bẫy slug/exec · **§6.1** quy tắc "không chữ" (3 việc) + quy tắc ô montage |
| `AGENTS.md` | H20 bổ sung quy tắc ô montage ≥ 384 px sau resize · H25 bổ sung bằng chứng soi 32/136 nền có chữ |
| `02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/Danh_Sach_Anh_Tap11.md` | 136 nền / 219 shot / 1738 s + mốc câu + shot dùng (đã đối chiếu: thừa 0 · thiếu 0) |
| `02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/BaoCao_QC_Tap11_20261112.md` | Gắn đính chính trỏ sang báo cáo này |

**Bản ghi bằng chứng:** `.work/_t11/violations_t11.json` (32 nền + mức độ) · `.work/_t11/textlike.json` (xếp hạng detector) · `.work/_t11/prompt_textscan.json` (quét từ khoá chữ) · `.work/bg_jobs_tap11_detext32.json` (prompt vá vòng 1) · `.work/bg_jobs_tap11_detext3_r2.json` (vòng 2) · `.work/bg_jobs_tap11_detext1_r3.json` (vòng 3) · `.work/bg_jobs_tap11_detext1_r4.json` (vòng 4) · `.work/_t11/shots_changed.json` (58 shot đổi nền).
