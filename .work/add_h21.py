with open("AGENTS.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

h21 = (
    "| **H21** | **Quy chuẩn tạo ảnh nền bằng Kaggle FLUX (Deep Noir):** Bắt buộc áp dụng "
    "kiến trúc prompt 4 tầng (Style Prefix + Bối cảnh + Mood tâm lý học rùng rợn + Negative) "
    "kết hợp hậu kỳ dìm bão hoà màu 35%, tăng tương phản bóng tối 15%, phủ vignette 4 góc "
    "và thêm hạt phim 35mm. **CẤM** dùng upscaler ảnh thực Real-ESRGAN làm bóng bẩy/mất chất noir comic 2D | "
    "Xem toàn văn tài liệu hướng dẫn kỹ thuật: `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` |\n"
)

# Insert after H20
inserted = False
for idx, line in enumerate(lines):
    if line.startswith("| **H20** |"):
        lines.insert(idx + 1, h21)
        inserted = True
        break

if inserted:
    with open("AGENTS.md", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("Added H21 rule to AGENTS.md successfully.")
else:
    print("Could not find H20 line.")
