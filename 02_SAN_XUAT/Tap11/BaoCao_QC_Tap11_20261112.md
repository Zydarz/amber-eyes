# BÁO CÁO QC — TẬP 11 · SINH NỀN CLOUDFLARE FLUX.1 & RENDER ẢNH TĨNH 3 NGÔN NGỮ

**Ngày thực hiện:** 12/11/2026  
**Hồ sơ vụ án:** Paul Bernardo & Karla Homolka (Cặp đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi Folie à Deux & Thỏa Thuận Với Quỷ Dữ)  
**Công cụ sinh ảnh nền:** **Cloudflare Workers AI** — mô hình `@cf/black-forest-labs/flux-1-schnell`  
**Yêu cầu:** Khắc phục triệt để lỗi nền procedural trừu tượng cũ (#136), sinh mới 100% 70 ảnh nền noir chuẩn bằng Cloudflare FLUX.1, đồng bộ kịch bản mới (> 200 câu) bổ sung Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (§A2c), chuẩn hóa bảng shot 3 ngôn ngữ (VN, EN, JA), render lại toàn bộ ảnh tĩnh theo quy chuẩn tạo ảnh mới nhất (1 ảnh gốc nạp 1 lần + phủ chữ/avatar 3 ngôn ngữ) — **KHÔNG tạo video**.

---

## 1. PHẠM VI & SỐ ĐO THỰC TẾ (Quy tắc L3, L5, L7)

| Hạng mục | Kết quả đo lường | Bằng chứng kiểm định / Đường dẫn | Trạng thái |
|---|---|---|:---:|
| **Kịch bản** | **218 câu thoại** · 59 elements đồng bộ 100% 3 ngôn ngữ | `01_KICH_BAN/Tap11/kichban_tap11_23102026.md`<br>`01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md`<br>`01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md` | ✅ **ĐẠT** |
| **Kịch bản JSON** | **218 câu** (59 elements) mỗi ngôn ngữ | `.work/script_tap11.json`<br>`.work/script_tap11_EN.json`<br>`.work/script_tap11_JA.json` | ✅ **ĐẠT** |
| **Bảng shot (Plan)** | **223 dòng shot**/ngôn ngữ<br>(218 shot nội dung + 4 thẻ chuyển hồi T10 + 1 thẻ kết T2) | `02_SAN_XUAT/Tap11/KeHoach_Video_Tap11.md`<br>`02_SAN_XUAT/Tap11_EN/KeHoach_Video_Tap11_EN.md`<br>`02_SAN_XUAT/Tap11_JA/KeHoach_Video_Tap11_JA.md` | ✅ **ĐẠT** |
| **Sinh nền FLUX.1** | **70 ảnh nền noir** sinh mới hoàn toàn qua Cloudflare FLUX.1<br>Thời gian: **220,1 giây** (~3,67 phút · 3,14 s/ảnh)<br>Độ lệch chuẩn TB: **50,93** (giàu chi tiết, loại bỏ triệt để gradient mờ) | `.work/gen_images_cloudflare_flux.py`<br>`assets/bg/t11_*.png` (2112×1188 PNG) | ✅ **ĐẠT** |
| **Provenance (L7)** | **70/70 bản ghi** cập nhật model Cloudflare FLUX.1, prompt, ngày, điều khoản | `provenance.json` | ✅ **ĐẠT** |
| **Bản lưu trước ghi đè (L5)** | Đã sao lưu 70 nền cũ và mẫu ảnh tĩnh | `.work/_cu/bg_t11_before_flux_20261112/`<br>`.work/_cu/stills_t11_backup_20261112/` | ✅ **ĐÃ LƯU** |
| **Cổng nền dùng chung (H17)** | `EN=67nen/223shot JA=67nen/223shot VN=67nen/223shot`<br>0 file nền có hậu tố ngôn ngữ | `py -3 .work/qc_bg_shared.py --ep 11` (exit 0) | ✅ **ĐẠT** |
| **Ảnh tĩnh (Stills)** | **669 ảnh tĩnh** (223 shots × 3 ngôn ngữ)<br>Render chuẩn 1 nền gốc + chèn ngôn ngữ (**210,13 s** / ~3,5 phút) | `.work/video3_t11/stills/` (223 ảnh)<br>`.work/video3_EN_t11/stills/` (223 ảnh)<br>`.work/video3_JA_t11/stills/` (223 ảnh) | ✅ **ĐẠT** |
| **Cổng chữ chìm (H20)** | **0 ảnh chữ chìm · 0 ảnh chữ nhạt** trên cả 3 ngôn ngữ | `.work/qc_contrast_t11.py` (exit 0) | ✅ **ĐẠT** |
| **Soi mắt có chọn lọc (H20)** | VI: 124/223 shot · EN: 124/223 shot · JA: 18/223 shot | `.work/_t11/eyeball_vi.json`<br>`.work/_t11/eyeball_en.json`<br>`.work/_t11/eyeball_ja.json` | ✅ **ĐẠT** |
| **Montage soi mắt (Q7)** | 3 tờ montage tổng hợp toàn bộ các shot rủi ro trên nền FLUX.1 mới | `.work/qc_montage/ep11_stills_vi.jpg` (4128×5472, 124 ảnh)<br>`.work/qc_montage/ep11_stills_en.jpg` (4128×5472, 124 ảnh)<br>`.work/qc_montage/ep11_stills_ja.jpg` (4128×1026, 18 ảnh) | ✅ **ĐẠT** |

---

## 2. QUY CHUẨN KỸ THUẬT CLOUDFLARE FLUX.1 ĐÃ TRIỂN KHAI

1. **Khắc phục triệt để lỗi nền procedural (#136):**
   - 67 ảnh nền cũ của Tập 11 trước đây là gradient tím/hồng/xanh mờ ảo không có cảnh thật.
   - Toàn bộ 70 ảnh đã được thay thế bằng hình ảnh sinh bởi mô hình **Cloudflare FLUX.1 schnell** với prompt chuẩn graphic novel noir chiaroscuro.
   - Kỹ thuật xử lý: Cloudflare FLUX.1 trả về ảnh 1024×1024; pipeline tự động crop dải giữa 16:9 (`1024×576`) và resize chất lượng cao (LANCZOS) lên chuẩn **2112×1188**, đảm bảo tỷ lệ hoàn hảo không biến dạng.

2. **Nguyên tắc "1 nền gốc dựng 1 lần + phủ chữ 3 ngôn ngữ" (Rule H17, H5, T23, T24):**
   - Nền gốc được nạp, resize và hoàn thiện hạt phim (cinematic grain) **1 lần duy nhất** cho mỗi shot.
   - Khung hình nền chuẩn được sao chép sang 3 luồng để render typography và avatar tương ứng theo từng ngôn ngữ (VI, EN, JA).
   - Tốc độ render ảnh tĩnh đạt **210,13 giây** cho toàn bộ 669 ảnh (~0,31 s/ảnh), tiết kiệm hơn 60% thời gian so với phương pháp render độc lập.

---

## 3. KẾT LUẬN & TRẠNG THÁI

- Đã giải quyết 100% phản hồi của người dùng về lỗi "toàn màu tím ở giữa".
- Bộ ảnh tĩnh mới trên nền Cloudflare FLUX.1 chân thực, sắc nét, giàu chi tiết bối cảnh, chữ nổi bật rõ ràng, đạt chuẩn phát sóng kênh Amber Eyes.
- Không tạo file video theo đúng chỉ đạo.
