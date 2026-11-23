# -*- coding: utf-8 -*-
"""Update REVIEW documents for Episode 21 to reflect the 248-sentence deep psychology upgrade."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 1. Update REVIEW_kichban_tap21_10chiau.md
path_10chiau = ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap21" / "REVIEW_kichban_tap21_10chiau.md"
content_10chiau = path_10chiau.read_text(encoding="utf-8")
content_10chiau = content_10chiau.replace("212 câu (kịch bản lớn > 200 câu)", "248 câu (kịch bản lớn nâng cấp chiều sâu tâm lý)")
content_10chiau = content_10chiau.replace("**212**", "**248**")
content_10chiau = content_10chiau.replace("~25,5 phút", "~28,5 phút")
content_10chiau = content_10chiau.replace("212 câu thoại", "248 câu thoại")
content_10chiau = content_10chiau.replace(
    "- **Thái độ trước bản án & Bệnh lý phân ly:**",
    "- **Hiện tượng Sự thức tỉnh sau loạn thần (Post-Psychotic Awakening) & Sụp đổ bản ngã:** Sau nhiều tuần được điều trị Haldol trong nhà tù, sương mù hoang tưởng tan biến, Andrea đối diện với sự thật tàn khốc rằng chính tay mình đã hại con; chấn thương đạo đức cực hạn khiến cô suy sụp không lời.\n- **Bản án lương tâm tự nguyện suốt đời:** Suốt gần 20 năm tại Bệnh viện Nhà nước Kerrville, Andrea kiên quyết từ chối nộp đơn xin phóng thích, tự giam mình trong bản án lương tâm và ngày ngày đan áo trẻ em gây quỹ tưởng niệm các con."
)
path_10chiau.write_text(content_10chiau, encoding="utf-8")
print(f"Updated: {path_10chiau}")

# 2. Update REVIEW_kichban_tap21_multilingual.md
path_multi = ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap21" / "REVIEW_kichban_tap21_multilingual.md"
content_multi = path_multi.read_text(encoding="utf-8")
content_multi = content_multi.replace("212", "248")
path_multi.write_text(content_multi, encoding="utf-8")
print(f"Updated: {path_multi}")
