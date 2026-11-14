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
- **Lỗi đã gặp (13/11/2026 - Tập 12):** Khởi chạy 2 tiến trình Python độc lập (`subprocess.Popen`) cùng một lúc khiến cả 2 tiến trình đồng thời nạp weights 4B vào System RAM. Tổng lượng RAM tiêu thụ vượt quá 30GB, dẫn đến việc kernel Linux gửi tín hiệu `SIGKILL (-9)` tiêu diệt GPU 0.
- **Quy tắc bất di bất dịch:** **CẤM** khởi động đồng thời 2 tiến trình Python độc lập cùng nạp model.

### 5.2. Hai giải pháp chạy song song 2 GPU chuẩn xác

#### Giải pháp A (Khuyến nghị): Staggered Subprocess Startup (Khởi động so-le thời gian)
Nếu chạy 2 worker qua `subprocess` (mỗi worker một biến môi trường `CUDA_VISIBLE_DEVICES` độc lập):
1. Worker 0 (`CUDA_VISIBLE_DEVICES=0`) khởi động trước.
2. Worker 0 nạp xong pipeline vào VRAM và gọi `gc.collect()` giải phóng System RAM (~90 giây).
3. Đặt lệnh `time.sleep(120)` chờ Worker 0 ổn định hoàn toàn rồi mới khởi chạy Worker 1 (`CUDA_VISIBLE_DEVICES=1`).
4. Lúc này đỉnh tiêu thụ System RAM không bao giờ vượt quá 16GB $\rightarrow$ Cả 2 GPU chạy song song 100% công suất an toàn tuyệt đối.

#### Giải pháp B: Single-Process Multi-Threading (1 Tiến trình - 2 Luồng)
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
| **Không chữ (H2/H5)** | 0 chữ, 0 số, 0 logo, 0 nhãn giả do AI vẽ | Soi mắt qua Montage `.work/qc_montage.py` |
| **Độ tương phản** | Đạt chuẩn chiaroscuro, không bị mờ đục xám xịt | Soi góc tối đạt độ đen sâu |
| **Bản quyền (L7)** | Đầy đủ bản ghi trong `provenance.json` | Cập nhật tự động: công cụ, prompt, seed, điều khoản thương mại |

---
*Tài liệu này là quy chuẩn kỹ thuật bắt buộc cho toàn bộ các tập tiếp theo sử dụng engine Kaggle FLUX.*
