# -*- coding: utf-8 -*-
"""Ghi số đo probe 16/11/2026 vào QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §5 + TIEU_CHUAN A11 #170."""
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
QC = ROOT / "00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md"
STD = ROOT / "00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md"

NEW_51 = """### 5.1. Bài học xương máu: Tránh lỗi Linux OOM-Killer (Mã lỗi -9)

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

"""

NEW_52_HEAD = """### 5.2. Cách chạy song song 2 GPU ĐÃ ĐƯỢC CHỨNG MINH (đo 16/11/2026)

> **Kết luận từ số đo:** trong **cùng 1 phiên** Kaggle thì **KHÔNG CÓ** cách nào chạy 2 worker an toàn với `FLUX.2-klein-4B`:
> bỏ `cpu_offload` ⇒ nổi VRAM T4 (14,53/14,56 GiB); giữ `cpu_offload` ⇒ nổi System RAM khi chạy 2 worker.
> `enable_sequential_cpu_offload()` sẽ giảm RAM/worker nhưng chậm gấp đôi ⇒ hiệu quả ròng ≈ 0.

#### ✅ GIẢI PHÁP DUY NHẤT CÒN LẠI: 2 KERNEL RIÊNG = 2 PHIÊN CHẠY ĐỘNG LẬP
- Mỗi kernel là **1 phiên VM riêng**, có **System RAM riêng ~32 GB** ⇒ 2 worker không tranh RAM nhau.
- Mỗi kernel chạy **1 tiến trình / 1 GPU** (`CUDA_VISIBLE_DEVICES=0`), giữ nguyên `enable_model_cpu_offload()` ⇒ **không đổi pipeline, không đổi tốc độ (75,5 s/ảnh)**.
- **Đã kiểm chứng 16/11/2026 10:38:** kernel `…-flux2-generator` (v31) và kernel `…-flux2-probe-vram-ram` (v1) chạy **đồng thời**, cùng trạng thái RUNNING ⇒ tài khoản cho phép 2 phiên GPU song song.
- Cách làm: tách jobs làm đôi → `.work/kaggle_flux/make_2kernel_batches.py` dựng 2 notebook + 2 `kernel-metadata.json` → push cả 2 kernel → chạy 2 watcher.

#### ❌ Giải pháp A (KHÔNG còn hiệu quả — đo 16/11/2026): Staggered Subprocess Startup (Khởi động so-le thời gian)"""

t = QC.read_text(encoding="utf-8")
h1 = t.find("### 5.1.")
h2 = t.find("### 5.2.")
assert 0 < h1 < h2, "khong tim thay 5.1/5.2"
tail_marker = "#### Giải pháp A (Khuyến nghị): Staggered Subprocess Startup (Khởi động so-le thời gian)"
k = t.find(tail_marker, h2)
assert k > h2, "khong tim thay dong Giải pháp A"
t = t[:h1] + NEW_51 + NEW_52_HEAD + t[k + len(tail_marker):]
t = t.replace("#### Giải pháp B: Single-Process Multi-Threading (1 Tiến trình - 2 Luồng)",
              "#### ❌ Giải pháp B (KHÔNG còn hiệu quả — 2 pipeline = 2 bản sao weights trong RAM): Single-Process Multi-Threading")
QC.write_text(t, encoding="utf-8")
print("✓ QUY_TAC_TAO_ANH_KAGGLE_FLUX.md: §5.1/§5.2 đã cập nhật")

ROW = (
    "| 170 | **Chạy 2 worker Python trong CÙNG 1 phiên Kaggle ⇒ LUÔN bị OOM-Killer (-9) — đo được, không phải lỗi ngẫu nhiên.** "
    "Tập 11 (16/11/2026): kernel v30 sinh 70 ảnh bằng 2 worker (staggered 120 s) → `GPU 0: 0, GPU 1: -9`, worker 1 chết ngay trong `from_pretrained()`. "
    "Phân tích 4/4 lượt 2-GPU trước đó (T12 13/11, T13 14/11, T15 15/11, T11 16/11): **luôn có đúng 1 worker bị -9**. "
    "Probe đo thật: System RAM 1 phiên = 32.098 MB; bỏ `cpu_offload` ⇒ **CUDA OOM** (14,53/14,56 GiB VRAM T4); giữ `cpu_offload` ⇒ weights ~15–17 GB **System RAM**/worker ⇒ 2 worker ≈ 34 GB > 31 GB ⇒ OOM. "
    "**Mô tả cũ của Giải pháp A sai**: worker 0 đâu có “nạp vào VRAM rồi giải phóng System RAM” — với `enable_model_cpu_offload()` weights **nằm lại trong RAM** suốt lượt chạy ⇒ giấc 120 s không cứu được | "
    "**Dùng 2 KERNEL RIÊNG = 2 PHIÊN CHẠY ĐỘNG LẬP** (mỗi kernel 1 tiến trình / 1 GPU; mỗi phiên có System RAM riêng ~32 GB ⇒ không tranh nhau). "
    "Đã kiểm chứng 16/11/2026: 2 kernel chạy đồng thời cùng lúc. Công cụ: `.work/kaggle_flux/make_2kernel_batches.py` (tách đôi jobs → 2 notebook + 2 metadata → push 2 kernel). "
    "Giữ nguyên `enable_model_cpu_offload()` ⇒ không đổi tốc độ (75,5 s/ảnh). Nguồn: `QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` §5 |")

s = STD.read_text(encoding="utf-8")
i = s.find("## A11")
lines = s[i:].split("\n")
j = None
for n, l in enumerate(lines):
    if l.startswith("| 169"):
        j = n
        break
assert j is not None, "khong tim thay dong 169"
lines = lines[:j + 1] + [ROW] + lines[j + 1:]
STD.write_text(s[:i] + "\n".join(lines), encoding="utf-8")
print("✓ TIEU_CHUAN_DUNG_VIDEO.md: thêm A11 #170")
