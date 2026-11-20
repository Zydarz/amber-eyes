# -*- coding: utf-8 -*-
"""Ghi muc 15 (mo ta + caption TikTok Tap 02) vao KE_HOACH_TIKTOK.md — L6."""
import pathlib
import shutil
import time

P = pathlib.Path("02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md")

TEXT = """
---

## 15. MÔ TẢ + CAPTION TIKTOK TẬP 02 — 5/5 ĐẠT (20/11/2026)

### 15.1 File bàn giao (đo được)

| File | Ký tự | Dán vào đâu |
|---|---|---|
| `MoTa_Dai_TK1.txt` | **2.930** | ô **Description** của TikTok Studio |
| `MoTa_Dai_TK2.txt` | **2.920** | ô Description |
| `MoTa_Dai_TK3.txt` | **3.093** | ô Description |
| `MoTa_Dai_TK4.txt` | **3.139** | ô Description |
| `MoTa_Dai_TK5.txt` | **2.253** | ô Description |
| `Caption_TK1.txt` … `Caption_TK5.txt` | **399 / 407 / 417 / 402 / 399** (phần dán) | ô **caption** khi đăng |

Tất cả nằm trong `02_SAN_XUAT/TIKTOK/Tap02/`. Mỗi file caption = **phần dán** (trước dấu `---`) + **phần "Ghi chú khi đăng"** (KHÔNG dán).

### 15.2 Cấu trúc mô tả dài (5 khối, giữ nguyên cho mọi tập sau)

`hook` → `Tập N · tên tập — chỉ dấu #X` → `📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio` → `——————` → **khối CHỈ DẤU** (phân tích) → `——————` → **BỐI CẢNH HỒ SƠ** → `——————` → **NGUỒN THAM KHẢO** → `——————` → **LƯU Ý** (6 dòng: AI tạo hình/giọng · không phù hợp trẻ em · giáo dục, không thay thế tư vấn y tế/pháp lý · tư liệu công khai, không kết tội ai · Cú/Sói/Cáo là linh thú minh hoạ · hồ sơ có thật) → 7 hashtag.

### 15.3 QC độc lập — `.work/_qc_mota_tap02.py` — **0 lỗi / 10 tệp**

| Cổng | Kết quả |
|---|---|
| Từ cấm V9/A9.2 (máu · thi thể · sát hại · đòn · trói · bầm · đập · đầu độc · diệt cỏ · bỏ đói · móc áo) trong caption + mô tả dài | **0 lỗi** (10/10 tệp) |
| Giới hạn ký tự | caption 399–417 ≤ 2.200 · Description 2.253–3.139 ≤ 4.000 |
| Hashtag | **7** mỗi tệp (5–8), đủ `#AmberEyes` + `#HosoCoThat` |
| Nhãn AIGC trong caption | 5/5 có, **nằm trong phần dán** |
| Mô tả dài | 5/5 có `LƯU Ý` + `NGUỒN THAM KHẢO` + cảnh báo trẻ em + "không phải phóng sự" |
| Số liệu truy về nguồn | **15/15 mục** có trong `kichban_tap02_22102026.md` / `nguon_tham_khao.md` (82 · 88 · 25 năm · 46 tuổi · 37 tuổi · Marie-France Comeau · Jessica Lloyd · Nissan Pathfinder · Hubert Genest · Robert Scott · Jim Smyth · Trenton · Tweed · Belleville · 2010 ONSC 5946) |

Thời lượng tập YouTube đo được: `timeline_s_t02.json` → **1.519,08 s = 25,3 phút** ⇒ dòng "Xem tập đầy đủ (25 phút)" trong mô tả dài là **đúng số đo thật**.

### 15.4 Một lỗi thật đã sửa: nhãn AIGC nằm ngoài phần dán (T23)

**Bẫy:** generator ghi dòng *"Nội dung do AI tạo hình và giọng…"* vào **phần "Ghi chú khi đăng"** (KHÔNG dán) ⇒ người đăng phải **tự gõ thêm** khi dán. Bất kỳ lần đăng nào quên ⇒ **vi phạm luật T3** (TikTok bắt buộc ghi nhãn AIGC trong caption) ⇒ video bị gỡ hoặc hạn chế.

**Đã sửa ở nguồn:** `.work/_build_tk_tap02.py` — `DONG_AIGC` nay nằm **trong thân caption** (ngay trước dòng hashtag), và thêm mục QC **7b** kiểm nhãn AIGC nằm đúng trong phần dán (`cap.split("\\n---")[0]`). Sau khi sửa: **5/5 đạt**, caption dài thêm ~85 ký tự (vẫn ≤ 2.200).

⇒ Nguyên tắc: **thứ bắt buộc phải nằm trong phần dán**, không được đẩy sang phần ghi chú. Phần ghi chú chỉ chứa việc *thao tác* khi đăng (bật toggle, dán link, tên file).

### 15.5 Ba bẫy QC mới (T24–T26)

| # | Bẫy | Hậu quả | Cách tránh |
|---|---|---|---|
| **T24** | QC đếm hashtag bằng `#\w+` ⇒ **mã chỉ dấu `#8`, `#9`, `#10` bị tính là hashtag** | Báo động giả "9 hashtag, vượt giới hạn" → mất thời gian điều tra | Lọc `re.fullmatch(r"#\\d+", t)` trước khi đếm |
| **T25** | QC kiểm tra caption **cả file** (gồm phần ghi chú) thay vì **phần dán** | Báo động giả "thiếu cảnh báo trẻ em" — dòng đó cố ý nằm ở mô tả dài (ô Description), không phải caption | Tách `cap.split("\\n---")[0]` rồi kiểm riêng caption và mô tả dài |
| **T26** | Caption ghi "Độ dài caption: NNN ký tự" **tính cả phần ghi chú** | Báo nhầm độ dài (1.126 thay vì 399) ⇒ tưởng gần trần 2.200 | `len(cap)` phải đo **phần dán**; con số trong file phải khớp độ dài thật khi dán |

### 15.6 Việc còn lại

| # | Việc | Người |
|---|---|---|
| 1 | **Điền link YouTube Tập 02** — đang là placeholder `[LINK_TẬP 02 — cần điền]` trong cả 5 file caption; **không tự bịa** (L2) | Người dùng |
| 2 | Thay dòng "Xem tập đầy đủ ở link trong bio" trong caption bằng URL thật **nếu** TikTok cho phép (URL gõ tay trong caption không click được — dán vào ô Links/Website của profile mới click được) | Người dùng |
| 3 | Bật toggle **"AI-generated content"** khi đăng (dòng nhãn AIGC **đã có sẵn** trong caption) | Người dùng |
| 4 | Xác minh quyền thương mại BGM MiniMax (mục 2.4) — chưa làm, ảnh hưởng cả 5 clip | Người dùng + AI |
"""

OLD_ROW = "| 7 | Dựng 5 clip 9:16 + chạy 14 cổng QC clip + `BaoCao_QC_TikTok_Tap02.md` | AI (sau khi được duyệt) |"
NEW_ROW = (OLD_ROW + "\n"
           "| 8 | **Điền link YouTube Tập 02** vào 5 file caption + profile (đang placeholder) | Người dùng |")


def main():
    t = P.read_text(encoding="utf-8-sig")
    if "## 15. MÔ TẢ + CAPTION TIKTOK TẬP 02" in t:
        print("muc 15 da ton tai — bo qua")
        return
    if OLD_ROW not in t:
        raise SystemExit("khong tim thay dong 13.5 de them muc 8")
    t = t.replace(OLD_ROW, NEW_ROW, 1)
    bak = pathlib.Path(".work/_cu") / ("KE_HOACH_TIKTOK_%s.md" % time.strftime("%Y%m%d_%H%M"))
    bak.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(P, bak)
    P.write_text(t.rstrip("\n") + "\n" + TEXT, encoding="utf-8")
    print("da them muc 15 · backup: %s" % bak)


if __name__ == "__main__":
    main()
