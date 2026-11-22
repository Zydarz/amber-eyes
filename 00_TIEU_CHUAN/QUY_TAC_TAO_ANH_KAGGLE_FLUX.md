# TIÊU CHUẨN TẠO ẢNH NỀN BẰNG KAGGLE FLUX CHO KÊNH AMBER EYES

> **Phiên bản:** 1.0 — Ban hành ngày 13/11/2026.  
> **Áp dụng cho:** Toàn bộ quá trình tạo ảnh nền noir 16:9 (2112×1188) trên môi trường **Kaggle GPU** (mô hình `FLUX.2-klein-4B`).  
> **Mục tiêu:** Đồng nhất 100% phong cách thị giác Graphic Novel Noir — Chiaroscuro tâm lý học, giữ nguyên độ lạnh lùng, ghê rợn và ngột ngạt đặc trưng của hồ sơ vụ án Amber Eyes; 0 đồng chi phí công cụ, tối ưu hoá thời gian chạy và an toàn bản quyền thương mại.

---

## 1. NGUYÊN TẮC CỐT LÕI (BẮT BUỘC TUÂN THỦ)

1. **Khắc phục xu hướng tự nhiên của FLUX (Training Bias):**
   - FLUX vốn được huấn luyện nhiều trên ảnh thương mại hiện đại, có xu hướng tự động vẽ cảnh vật "trong trẻo, tươi sáng, bầu trời xanh, ánh sáng ấm áp".
   - **Bắt buộc:** Phải can thiệp từ khóa dìm ánh sáng và dìm màu (Muted/Desaturated) ngay trong prompt, kết hợp pipeline hậu kỳ (Post-processing) để ép về chuẩn màu noir điều tra.
2. **CẤM dùng mô hình upscaler phục hồi ảnh thực (Real-ESRGAN/Photo-restoration):**
   - Các mô hình upscaler thực tế sẽ làm bóng bẩy và quang hóa nét vẽ, biến tranh graphic novel thành ảnh chụp 3D.
   - **Quy chuẩn:** Phóng to ảnh cơ sở lên **2112×1188 (16:9 2K)** bằng thuật toán nội suy đồ họa **LANCZOS**, sau đó áp dụng xử lý hạt phim và vignette.
3. **Tuân thủ tuyệt đối quy định V5 & V9 (AGENTS.md):**
   - **V5:** Người thật trong vụ án chỉ hiện dạng bóng lưng / khuất mặt hoàn toàn trong bóng tối. Tuyệt đối không vẽ nạn nhân nếu vụ án có xâm hại hay sát hại.
   - **V9:** Không miêu tả bạo lực đẫm máu, thương tích, thi thể trực diện. Thể hiện hiện trường và vật chứng dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.
   - **Không chữ (Text-free):** Cấm mọi chữ viết, biển hiệu, con số do AI tự vẽ trong nền.

---

## 2. BỘ CẤU TRÚC PROMPT CHUẨN (DEEP NOIR PROMPT ARCHITECTURE)

Mọi prompt sinh ảnh nền cho Amber Eyes khi đưa vào FLUX phải được ghép theo công thức 4 tầng:

```text
[STYLE_PREFIX] + [BỐI CẢNH CỤ THỂ CỦA CÂU/CẢNH] + [MOOD & ÁNH SÁNG TÂM LÝ] + [NEGATIVE_SUFFIX]
```

### 2.1. Tiền tố phong cách bắt buộc (STYLE_PREFIX)
```text
A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, 
bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, 
```

### 2.2. Hạt nhân ánh sáng & Bầu không khí ngột ngạt (MOOD & ATMOSPHERE)
Để tạo ra nét lạnh lùng, ghê rợn đặc trưng của kênh, luôn bổ sung các thành phần:
```text
gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, 
creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, 
decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, 
```

### 2.3. Hậu tố phủ định tuyệt đối (NEGATIVE_SUFFIX)
```text
Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, 
no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, 
no signs, no labels, no logos, no watermark, full-bleed 16:9.
```

---

## 3. THIẾT LẬP THÔNG SỐ PIPELINE INFERENCE (FLUX.2-klein-4B)

Khi chạy trên GPU Kaggle (Tesla T4), sử dụng cấu hình inference sau:

| Tham số | Giá trị chuẩn | Ý nghĩa kỹ thuật |
|---|---|---|
| **Model** | `black-forest-labs/FLUX.2-klein-4B` | Mô hình 4-step rectified flow, tốc độ cực nhanh trên T4 |
| **Dtype** | `torch.bfloat16` | Tiết kiệm VRAM, giữ nguyên dải động học màu sắc |
| **Offload** | `pipe.enable_model_cpu_offload()` | Chống tràn bộ nhớ VRAM (OOM) tuyệt đối |
| **VAE Tiling** | `pipe.vae.enable_tiling()` | Giúp giải mã ảnh kích thước lớn an toàn |
| **Base Resolution** | `width=1056, height=592` | Tỷ lệ 16:9 cơ sở tối ưu của FLUX.2 |
| **Inference Steps** | **4 đến 5 steps** | Đủ độ hội tụ cho rectified flow, không làm cháy nét |
| **Guidance Scale** | **2.0 đến 2.2** | Ép mô hình bám sát từ khóa noir/rùng rợn, triệt tiêu xu hướng tự do vẽ cảnh đẹp |

---

## 4. QUY TRÌNH HẬU KỲ ĐỒ HỌA NOIR TỰ ĐỘNG (POST-PROCESSING)

Ảnh cơ sở sau khi sinh ra **bắt buộc** phải đi qua 3 bước xử lý kỹ thuật số bằng Python (Pillow + Numpy) trước khi lưu:

### Bước 1: Phóng to chuẩn 2K kênh Amber Eyes
```python
img_2k = base_img.resize((2112, 1188), Image.Resampling.LANCZOS)
```

### Bước 2: Dìm màu & Tăng tương phản bóng tối (Color Grading)
Khử tính hoạt hình/thương mại của FLUX:
```python
# Giảm saturation 35% để đưa về bảng màu xám tro / ố vàng tư liệu cũ
color_enhancer = ImageEnhance.Color(img_2k)
img_muted = color_enhancer.enhance(0.65)

# Tăng tương phản 15% để khối đen đặc chiaroscuro sâu thẳm
contrast_enhancer = ImageEnhance.Contrast(img_muted)
img_contrast = contrast_enhancer.enhance(1.15)
```

### Bước 3: Áp hiệu ứng Noir Vignette & Hạt phim 35mm (Film Grain)
Tạo cảm giác rình rập, cô lập như trích xuất từ hồ sơ lưu trữ:
```python
arr = np.array(img_contrast, dtype=np.float32)
h, w, c = arr.shape
y, x = np.ogrid[:h, :w]
cx, cy = w / 2, h / 2
dist = np.sqrt((x - cx)**2 + (y - cy)**2)
max_dist = np.sqrt(cx**2 + cy**2)

# Vignette: dìm tối 45% ở các góc ngoài
vignette = 1.0 - 0.45 * (dist / max_dist)**1.8
vignette = np.clip(vignette, 0.4, 1.0)[:, :, np.newaxis]
arr = arr * vignette

# Film Grain: nhiễu Gaussian nhẹ tạo độ gai góc của giấy truyện tranh
np.random.seed(42)
grain = np.random.normal(0, 7.5, arr.shape)
arr = np.clip(arr + grain, 0, 255).astype(np.uint8)

final_img = Image.fromarray(arr)
```

---

## 5. TỐI ƯU HÓA TÀI NGUYÊN KAGGLE (MULTI-GPU 2x T4 SONG SONG)

Kaggle cấp môi trường **2 GPU Tesla T4 (mỗi GPU 16GB VRAM)** nhưng **System Host RAM giới hạn ~30GB**.

### 5.1. Bài học xương máu: Tránh lỗi Linux OOM-Killer (Mã lỗi -9)

**ĐO ĐƯỢC (probe 16/11/2026, kernel `chiduong2026/amber-eyes-flux2-probe-vram-ram`):**

| Số đo | Giá trị thật |
|---|---|
| System RAM của **1 phiên** Kaggle | **32.098 MB** (MemAvailable 30.810 MB) |
| GPU | 2 × Tesla T4, 15.360 MiB (dùng được **14,56 GiB**) |
| **KHÔNG** `cpu_offload` → model nằm thẳng trong VRAM | **CUDA OOM** — process chiếm **14,53 / 14,56 GiB** ⇒ **KHÔNG khả thi** trên T4 15 GB |
| **CÓ** `cpu_offload` → weights nằm trong **System RAM** | ~15–17 GB / worker ⇒ 2 worker ≈ 34 GB > 31 GB ⇒ **OOM-Killer -9** |

- **Lỗi đã gặp (13/11/2026 - Tập 12):** Khởi chạy 2 tiến trình Python độc lập (`subprocess.Popen`) cùng một lúc khiến cả 2 tiến trình đồng thời nạp weights 4B vào System RAM. Tổng lượng RAM tiêu thụ vượt quá 30GB, dẫn đến việc kernel Linux gửi tín hiệu `SIGKILL (-9)` tiêu diệt GPU 0.
- **Lỗi tái diễn (16/11/2026 - Tập 11):** 4/4 lượt chạy 2 GPU đều có **đúng 1 worker bị -9** (T12: GPU_0 chết; T13/T15/T11: GPU_1 chết, chết ngay trong `from_pretrained()` nên không in được dòng nào).
- **QUY TẮC BẤT DI BẤT DỊCH:** **CẤM** khởi động đồng thời 2 tiến trình Python độc lập cùng nạp model **trong cùng 1 phiên Kaggle** — đây không phải lỗi ngẫu nhiên mà là **tràn System RAM có hệ thống** (2 bản sao weights × ~15-17 GB > 31 GB).
- **LỖI CỦA GIẢI PHÁP A (đã sửa 16/11/2026):** mô tả cũ ghi worker 0 *"nạp xong pipeline **vào VRAM** và gọi `gc.collect()` giải phóng System RAM"* — nhưng code thật dùng `pipe.enable_model_cpu_offload()`, tức weights **nằm lại trong System RAM** suốt lượt chạy ⇒ worker 0 **không bao giờ giải phóng RAM** ⇒ giấc 120 s **không cứu được** 2 worker. Giải pháp A chỉ đúng khi worker không giữ weights trong RAM.

### 5.2. Cách chạy song song 2 GPU ĐÃ ĐƯỢC CHỨNG MINH (đo 16/11/2026)

> **Kết luận từ số đo:** trong **cùng 1 phiên** Kaggle thì **KHÔNG CÓ** cách nào chạy 2 worker an toàn với `FLUX.2-klein-4B`:
> bỏ `cpu_offload` ⇒ nổi VRAM T4 (14,53/14,56 GiB); giữ `cpu_offload` ⇒ nổi System RAM khi chạy 2 worker.
> `enable_sequential_cpu_offload()` sẽ giảm RAM/worker nhưng chậm gấp đôi ⇒ hiệu quả ròng ≈ 0.

#### ✅ GIẢI PHÁP DUY NHẤT CÒN LẠI: 2 KERNEL RIÊNG = 2 PHIÊN CHẠY ĐỘNG LẬP
- Mỗi kernel là **1 phiên VM riêng**, có **System RAM riêng ~32 GB** ⇒ 2 worker không tranh RAM nhau.
- Mỗi kernel chạy **1 tiến trình / 1 GPU** (`CUDA_VISIBLE_DEVICES=0`), giữ nguyên `enable_model_cpu_offload()` ⇒ **không đổi pipeline, không đổi tốc độ (75,5 s/ảnh)**.
- **Đã kiểm chứng 16/11/2026 10:38:** kernel `…-flux2-generator` (v31) và kernel `…-flux2-probe-vram-ram` (v1) chạy **đồng thời**, cùng trạng thái RUNNING ⇒ tài khoản cho phép 2 phiên GPU song song.
- Cách làm: tách jobs làm đôi → `.work/kaggle_flux/make_2kernel_batches.py` dựng 2 notebook + 2 `kernel-metadata.json` → push cả 2 kernel → chạy 2 watcher.
- **Đã dùng thật 16/11/2026 cho đợt sinh lại 32 nền bỏ chữ**: `.work/kaggle_flux/make_2kernel_detext.py` (tách đôi 32 job → 16 + 16, **seed RIÊNG theo job** để 2 kernel không trùng seed) → push 2 kernel `chiduong2026/amber-eyes-flux2-detext-k1` / `-k2` → watcher `.work/kaggle_flux/watch_detext32.py` tải 2 zip, giải nén, ghi đè `assets/bg/`, cập nhật `provenance.json`.
- **Đã dùng thật 16/11/2026 cho Tập 12 (69 nền mới theo H25)**: `.work/kaggle_flux/make_2kernel_t12_new69.py` → 2 kernel `chiduong2026/amber-eyes-flux2-t12-k1` (34 ảnh) / `-k2` (35 ảnh) → watcher `.work/kaggle_flux/watch_t12_new69.py`.
  - **Mỗi lần sinh phải dùng khoảng seed RIÊNG** (Tập 12 cũ 12000+idx → lô mới **22000+idx**) để không trùng seed với ảnh đã có; seed phải **không trùng giữa 2 kernel** (kiểm bằng script trước khi push).
  - **`title` = slug của `id`** ⇒ kernel tạo ra đúng id mong muốn, không cần đoán lại (A11 #174).
- ⚠️ **`kaggle kernels push` lấy `id` từ SLUG CỦA `title`, không phải `id` trong `kernel-metadata.json`.** Đặt metadata `id: …/amber-eyes-flux2-generator2` + `title: "Amber Eyes Flux2 Detext k2"` ⇒ Kaggle tạo kernel thật là **`chiduong2026/amber-eyes-flux2-detext-k2`** và in cảnh báo *"Your kernel title does not resolve to the specified id"*. ⇒ **Đặt `title` = slug của `id`**, hoặc đọc `kaggle kernels list --mine` sau khi push để lấy id thật rồi dùng id đó cho `kernels status/output`.
- ⚠️ Khi `exec` khuôn `make_nb_tapXX_parallel.py` để dựng notebook, `__file__` **phải trỏ về chính file khuôn** — nếu trỏ sang thư mục khác thì `ROOT` tính lệch và lệnh ghi notebook ném `FileNotFoundError`.

#### ❌ Giải pháp A (KHÔNG còn hiệu quả — đo 16/11/2026): Staggered Subprocess Startup (Khởi động so-le thời gian)
Nếu chạy 2 worker qua `subprocess` (mỗi worker một biến môi trường `CUDA_VISIBLE_DEVICES` độc lập):
1. Worker 0 (`CUDA_VISIBLE_DEVICES=0`) khởi động trước.
2. Worker 0 nạp xong pipeline vào VRAM và gọi `gc.collect()` giải phóng System RAM (~90 giây).
3. Đặt lệnh `time.sleep(120)` chờ Worker 0 ổn định hoàn toàn rồi mới khởi chạy Worker 1 (`CUDA_VISIBLE_DEVICES=1`).
4. Lúc này đỉnh tiêu thụ System RAM không bao giờ vượt quá 16GB $\rightarrow$ Cả 2 GPU chạy song song 100% công suất an toàn tuyệt đối.

#### ❌ Giải pháp B (KHÔNG còn hiệu quả — 2 pipeline = 2 bản sao weights trong RAM): Single-Process Multi-Threading
Sử dụng `concurrent.futures.ThreadPoolExecutor(max_workers=2)` trong cùng một tiến trình Python:
- Pipeline 0 nạp trực tiếp vào `cuda:0`.
- Pipeline 1 nạp trực tiếp vào `cuda:1`.
- Chia sẻ chung bộ nhớ Python runtime, không bị nhân đôi overhead của OS.

### 5.3. Hiệu năng thực tế
- Chạy 1 GPU: ~55–60 phút / batch 80 ảnh (~75s / ảnh).
- Chạy song song 2 GPU: **~25–28 phút / batch 80 ảnh** (giảm 50% thời gian chờ đợi).

---

## 6. QUY TRÌNH KIỂM SOÁT CHẤT LƯỢNG (QC GATE)

Mỗi bộ ảnh nền mới sinh từ Kaggle FLUX phải vượt qua các cổng kiểm định:

| Cổng QC | Tiêu chuẩn ĐẠT | Cách kiểm |
|---|---|---|
| **Kích thước** | Đúng `2112×1188` (100% số file) | Script đo kích thước tự động |
| **Không chữ (H2/H26)** | 0 chữ, 0 số, 0 logo, 0 nhãn giả do AI vẽ | Soi mắt qua Montage `.work/qc_montage.py` |
| **Độ tương phản** | Đạt chuẩn chiaroscuro, không bị mờ đục xám xịt | Soi góc tối đạt độ đen sâu |
| **Bản quyền (L7)** | Đầy đủ bản ghi trong `provenance.json` | Cập nhật tự động: công cụ, prompt, seed, điều khoản thương mại |

### 6.1. Quy tắc "không chữ" — ĐO ĐƯỢC 16/11/2026 (Tập 11)

**Mệnh đề phủ định trong prompt KHÔNG đủ.** Tập 11: soi 100 % 136 nền ⇒ **32/136 nền (23,5 %) có chữ AI**; trong đó **22 nền có prompt đã ghi "no text / no labels / no logos"** mà AI vẫn vẽ chữ (nhãn băng cassette, dòng chữ trên túi bằng chứng, chữ khắc trên vòng ống kính…). Nguyên nhân: **prompt vẫn mô tả vật mang chữ**.

Khi sinh lại ảnh có chữ, làm **ĐÚNG 3 việc** (giữ nguyên nội dung cảnh cụ thể theo H19):
1. **Gỡ mọi thông tin chữ khỏi prompt** — bỏ tên riêng, `titled`, `reading`, `labeled`, `inscribed`, `newspaper`, `cover` có chữ…
2. **Mô tả bề mặt TRƯNG** thay cho vật mang chữ — ví dụ *"a bound judicial inquiry volume with a plain blank unmarked cover"* (vẫn giữ vật thể, chỉ đổi bề mặt).
3. **Thêm mệnh đề**: `completely blank and unmarked with no writing at all`.

Cách kiểm hiệu quả nhất: **quét từ khoá trong prompt** (`titled/labeled/inscribed/newspaper/writing/labels/headline/placard/caption/…`) để lập danh sách nghi, rồi **soi mắt 100 %**; nền bị nghi ⇒ mở **full-res** (`assets/bg/tXX_*.png`), montage **thay tờ nhiều, không thay zoom 100 %**. Ô montage phải ≥ 384 px **sau khi ảnh bị resize** (cạnh dài ≤ ~1568 px) ⇒ **4 cột × 4 hàng, ô 512 px** (A11 #172). Sửa lại **đúng tên** ảnh đó (không sinh lại cả lô), seed riêng.

---
*Tài liệu này là quy chuẩn kỹ thuật bắt buộc cho toàn bộ các tập tiếp theo sử dụng engine Kaggle FLUX.*
