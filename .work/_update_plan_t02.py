# -*- coding: utf-8 -*-
import io

path = r"02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

sec19 = u"""

## 19. GÓI SẢN XUẤT CLIP TIKTOK TẬP 02 ĐA NGÔN NGỮ (EN · JA) (20/11/2026)

*Vụ án Đại tá Russell Williams · "Đại tá hai mặt và Vực thẳm leo thang hành vi"*
*Kế hoạch chi tiết: `02_SAN_XUAT/TIKTOK/Tap02/KE_HOACH_CLIP_TAP02.md` (VN) · `Tap02_EN/KE_HOACH_CLIP_TAP02_EN.md` (EN) · `Tap02_JA/KE_HOACH_CLIP_TAP02_JA.md` (JA)*

### 19.1 Tổng quan bộ 3 ngôn ngữ (VN · EN · JA)

| Bản | Thư mục | Số clip | Tổng câu | Thời lượng ước lượng | File đặc tả TTS | Trạng thái |
|---|---|---|---|---|---|---|
| **Tiếng Việt (VN)** | `02_SAN_XUAT/TIKTOK/Tap02/` | 5 | 53 | 56.1 – 82.6 s | `SPEC_AUDIO_CLIP_TAP02.json` | ✅ Kịch bản và mô tả đã rà soát chính tả, sẵn sàng đọc giọng |
| **Tiếng Anh (EN)** | `02_SAN_XUAT/TIKTOK/Tap02_EN/` | 5 | 53 | 56.1 – 81.9 s | `SPEC_AUDIO_CLIP_TAP02.json` | ✅ Đồng bộ 100%, chuẩn tốc độ đo timeline_s_EN_t02 |
| **Tiếng Nhật (JA)** | `02_SAN_XUAT/TIKTOK/Tap02_JA/` | 5 | 53 | 64.3 – 81.2 s | `SPEC_AUDIO_CLIP_TAP02.json` | ✅ Đồng bộ 100%, chuẩn tốc độ đo timeline_s_JA_t02 |

### 19.2 Bảng 5 clip và chỉ dấu tâm lý Tập 02 (3 ngôn ngữ)

| Clip | Chỉ dấu tâm lý (K10) | Chủ đề | Hook tiếng Việt | Hook tiếng Anh (EN) | Hook tiếng Nhật (JA) |
|---|---|---|---|---|---|
| **TK1** | #8 · #6 | Quỹ đạo leo thang | *"Bốn nấc thang. Tám mươi hai vụ trộm. Rồi một vụ án mạng."* | *"Four escalation steps. Eighty-two burglaries. Then murder."* | *「4つの階段。82件の侵入。そして殺人へと至る軌跡。」* |
| **TK2** | #9 · #1 | Hiệu ứng hào quang | *"Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào."* | *"Matching tire treads. Yet the police saluted him on his way."* | *「タイヤ痕の一致。それでも警察はその男に敬礼して見送った。」* |
| **TK3** | #5 · #3 | Phân mảnh tâm trí | *"Hai cuộc đời. Một cơ thể. Một câu chuyện để tự bào chữa."* | *"Two lives. One body. A story to self-justify."* | *「2つの人生。1つの身体。自己正当化のための物語。」* |
| **TK4** | #4 · #1 | Sụp đổ cái tôi ái kỷ | *"Không một lời xin lỗi nào nhắc tới nạn nhân."* | *"Not a single apology mentioned the victims."* | *「被害者に向けられた謝罪はただの一言もなかった。」* |
| **TK5** | #10 | Nạn nhân học và Trực giác | *"Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó."* | *"If you feel unease, never rationalize it away."* | *「曖昧な違和感を覚えたなら、決して見過ごしてはならない。」* |

### 19.3 Công cụ và tài nguyên đã tạo
- Bộ sinh tự động: `.work/_build_tk_tap02_multilang.py` (sinh 100% tài nguyên EN và JA từ dữ liệu gốc, không sửa tay).
- Sổ theo dõi tập trung: `02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv` đã cập nhật 10 dòng clip EN và JA cho Tập 02.
"""

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text.rstrip() + sec19)

print("Updated KE_HOACH_TIKTOK.md successfully.")
