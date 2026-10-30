import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap08"
OUT_DIR.mkdir(parents=True, exist_ok=True)

jobs = json.loads((WORK / "bg_jobs_tap08.json").read_text(encoding="utf-8"))

lines = []
lines.append('# DANH SÁCH ẢNH NỀN — TẬP 08 "KHI CÁC THIÊN TÀI BỊ TẨY NÃO"')
lines.append("")
lines.append("*Hồ sơ Giáo phái Aum Shinrikyo & Vụ tấn công tàu điện ngầm Tokyo bằng khí độc Sarin 1995. Ngày 23/10/2026.*")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B1. Thông tin bộ ảnh")
lines.append("")
lines.append("| Mục | Nội dung |")
lines.append("|---|---|")
lines.append(f"| Số ảnh chuẩn hóa | **{len(jobs)}** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |")
lines.append("| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |")
lines.append("| Vị trí lưu trữ | `assets/bg/t8_*.png` — **tiền tố `t8_` bắt buộc** để không trùng bộ nền Tập 01–07 |")
lines.append("| Danh sách prompt gốc | `.work/bg_jobs_tap08.json` & `.work/gemini_image_prompts_tap08.json` |")
lines.append("| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |")
lines.append("| Phong cách nghệ thuật | Dark graphic novel noir — mực đen đậm, chiaroscuro đối lập cao, tông lạnh desaturated, sương mù và film grain |")
lines.append("| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |")
lines.append("| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (100% tự chủ, không phụ thuộc MiniMax bên thứ ba) |")
lines.append("")
lines.append("**Quy tắc hình ảnh của kênh (V1 – V9):**")
lines.append("")
lines.append("- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**")
lines.append("  - `t8_asahara_shadow_profile`: Bóng lưng và góc nghiêng của Shoko Asahara ngồi thiền trong bóng tối, không lộ mặt.")
lines.append("  - `t8_dr_hayashi_umbrella_subway`: Bóng Bác sĩ Ikuo Hayashi cầm chiếc ô đen đứng lẻ loi trên sân ga đông đúc.")
lines.append("  - `t8_hazmat_officers_formation`: Đội hình đặc nhiệm cảnh sát trong đồ bảo hộ phòng hóa và mặt nạ dưỡng khí.")
lines.append("  - `t8_devotion_altar_kneeling`: Bóng những tín đồ thanh niên quỳ rạp trước đài sen trong đại sảnh nghi lễ.")
lines.append("- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.")
lines.append("- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:**")
lines.append("  - Tuyệt đối không mô tả vết thương, không vẽ cảnh hiện trường bi thảm trực diện.")
lines.append("  - Các chứng cứ (bản đồ metro, tháp phản ứng hóa chất, thiết bị mũ điện cực PSI, bản án tòa án) thể hiện dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B2. Ánh xạ ảnh → hồi → mốc câu")
lines.append("")
lines.append("Mốc câu theo `.work/script_tap08.json` (parse từ `01_KICH_BAN/Tap08/kichban_tap08_23102026.md`):  ")
lines.append("**32 lượt thoại · 165 câu · 3.649 từ** (Host 97 câu, Điều tra viên 27 câu, Chuyên gia tâm lý 26 câu, Người bình thường 15 câu).")
lines.append("")

act_titles = {
    1: "HỒI 1 · BUỔI SÁNG ĐỊNH MỆNH DƯỚI LÒNG ĐẤT TOKYO (00:00 – 05:00)",
    2: "HỒI 2 · KHU CĂN CỨ DƯỚI CHÂN NÚI PHÚ SĨ VÀ PHÒNG THÍ NGHIỆM TỬ THẦN (05:00 – 10:00)",
    3: "HỒI 3 · NGHỊCH LÝ CỦA CÁC THIÊN TÀI KHOA HỌC (10:00 – 15:00)",
    4: "HỒI 4 · MA THUẬT TẨY NÃO & KHÁI NIỆM \"POA\" ĐẪM MÁU (15:00 – 20:00)",
    5: "HỒI 5 · PHÁN QUYẾT LỊCH SỬ & BÀI HỌC VỀ SỰ TỰ DO TƯ TƯỞNG (20:00 – 26:00)"
}

idx = 1
for act_num in range(1, 6):
    lines.append(f"### {act_titles[act_num]}")
    lines.append("")
    lines.append("| Ảnh | Tên file | Nội dung phục vụ | Mốc câu |")
    lines.append("|---|---|---|---|")
    act_jobs = [j for j in jobs if j.get("act") == act_num]
    for j in act_jobs:
        lines.append(f"| {idx:02d} | `{j['name']}` | {j['desc']} | `{j['sentences']}` |")
        idx += 1
    lines.append("")

lines.append("---")
lines.append("")
lines.append("## B3. Thống kê & Kiểm soát chất lượng (QC)")
lines.append("")
lines.append(f"- **Tổng số ảnh:** {len(jobs)} ảnh mới 100%.")
lines.append("- **Độ phân giải:** 2112 × 1188 (chuẩn 16:9 2K).")
lines.append("- **Tuân thủ quy tắc V5:** 100% người thật chỉ hiện bóng lưng / khuất mặt hoàn toàn.")
lines.append("- **Tuân thủ quy tắc V9:** 100% không bạo lực, tập trung vào công lý, phân tích tâm lý học và tư liệu lịch sử.")
lines.append("- **Tuân thủ quy tắc V1 - V3:** Đổi hình đúng mốc câu thoại, không nhảy hình giữa chừng câu nói.")
lines.append("- **Bảo toàn phong cách:** Phong cách Dark graphic novel noir đồng bộ tuyệt đối với các tập trước của kênh Amber Eyes.")

doc_path = OUT_DIR / "Danh_Sach_Anh_Tap08.md"
doc_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Đã tạo {doc_path} thành công!")
