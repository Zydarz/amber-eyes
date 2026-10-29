#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Probe chất lượng dịch VN->JA: 2 model x (thinking bật/tắt). Ghi ra file UTF-8."""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ja_llm  # noqa: E402

OUT = Path(__file__).parent / "_ja_probe_out.txt"

SAMPLES = [
    "Ngày 14 tháng 6 năm 2015. Tại thị trấn yên bình Springfield, bang Missouri, nước Mỹ.",
    "Trong mắt tất cả chúng tôi, ngôi nhà màu hồng ấy là biểu tượng của tình mẫu tử thiêng liêng. Bà Dee Dee là một người mẹ đơn thân vĩ đại, người đã dành trọn cuộc đời mình để chăm sóc cô con gái Gypsy Rose.",
    "Ban đầu, chúng tôi phát lệnh truy tìm trên toàn quốc với giả định Gypsy Rose là nạn nhân bị bắt cóc đang nguy kịch tính mạng.",
    "**Tầng thứ nhất là: Cơn nghiện ánh hào quang của 'Vị thánh tử đạo'.**",
    "Chào mừng bạn đến với hồ sơ phân tích tâm lý học tội phạm.",
    "Câu hỏi lớn đặt ra cho cơ quan điều tra chúng tôi lúc bấy giờ là: *Tại sao cả một hệ thống y tế hiện đại với hàng trăm bác sĩ lại không phát hiện ra?*",
    "Thứ nhất, bà cho Gypsy uống thuốc chống động kinh liều cao dù cô không hề bị động kinh, khiến sức khỏe răng miệng của cô bé bị tổn hại nghiêm trọng.",
]

SYSTEM = (
    "Bạn là biên dịch chuyên nghiệp cho một kênh podcast tâm lý học tội phạm (tiếng Việt -> tiếng Nhật). "
    "Dịch sang tiếng Nhật tự nhiên, văn phong tài liệu kể chuyện (ナレーション調), không dịch nghĩa đen, không thêm bớt ý. "
    "Giữ nguyên tên riêng (người, địa danh, tổ chức) ở dạng chữ Latin gốc. "
    "Giữ nguyên thẻ ** in đậm ** và * in nghiêng * nếu có. "
    "Trả về DUY NHẤT một mảng JSON, mỗi phần tử {\"id\": <số thứ tự từ 1>, \"ja\": \"<bản dịch>\"}, đúng số phần tử, không thêm chú thích."
)


def main():
    prompt = json.dumps([{"id": i + 1, "vi": s} for i, s in enumerate(SAMPLES)], ensure_ascii=False)
    chunks = []
    for model in ["minimax/MiniMax-M3.1-Flash", "minimax/MiniMax-M3"]:
        for thinking in (False, True):
            m = model.split("/")[1]
            t0 = time.time()
            try:
                out = ja_llm.call(prompt, SYSTEM, model=m, thinking=thinking, max_tokens=4096)
                dt = time.time() - t0
                chunks.append(f"### {m} thinking={thinking} ({dt:.1f}s)\n{out}\n")
            except Exception as e:
                chunks.append(f"### {m} thinking={thinking}: FAILED {e}\n")
    OUT.write_text("\n" + ("=" * 78 + "\n").join(chunks), encoding="utf-8")
    print(f"written -> {OUT}")


if __name__ == "__main__":
    main()
