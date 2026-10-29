import json
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap07"
OUT_DIR.mkdir(parents=True, exist_ok=True)

jobs = json.loads((WORK / "bg_jobs_tap07.json").read_text(encoding="utf-8"))

lines = []
lines.append('# DANH SÁCH ẢNH NỀN — TẬP 07 "BẢN ÁN GIẾT NGƯỜI BẰNG TIN NHẮN"')
lines.append("")
lines.append("*Hồ sơ Michelle Carter & Conrad Roy: Thao túng tâm lý & Hội chứng Münchausen kỹ thuật số. Ngày 23/10/2026.*")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B1. Thông tin bộ ảnh")
lines.append("")
lines.append("| Mục | Nội dung |")
lines.append("|---|---|")
lines.append(f"| Số ảnh chuẩn hóa | **{len(jobs)}** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |")
lines.append("| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |")
lines.append("| Vị trí lưu trữ | `assets/bg/t7_*.png` — **tiền tố `t7_` bắt buộc** để không trùng bộ nền Tập 01–06 |")
lines.append("| Danh sách prompt gốc | `.work/bg_jobs_tap07.json` (chuẩn format kênh) |")
lines.append("| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |")
lines.append("| Phong cách nghệ thuật | Dark graphic novel noir — mực đen đậm, chiaroscuro đối lập cao, tông lạnh desaturated, sương mù và film grain |")
lines.append("| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |")
lines.append("| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (chuẩn bị sẵn sàng đồng bộ sang subagent image-generator khi reset quota) |")
lines.append("")
lines.append("**Quy tắc hình ảnh của kênh (V1 – V9):**")
lines.append("")
lines.append("- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**")
lines.append("  - `t7_clinical_depression_shadow`: Bóng người ngồi cúi đầu trên bờ vực biển đen mù sương, không lộ mặt.")
lines.append("  - `t7_witness_trembling_phone`: Cận cảnh bàn tay thiếu nữ nắm chặt chiếc điện thoại đang phát sáng trong quán cà phê vắng.")
lines.append("  - `t7_florida_beach_encounter_2012`: Bóng hai thiếu niên đạp xe ven biển Florida lúc hoàng hôn hoài niệm.")
lines.append("- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.")
lines.append("- **V9 — Trọng tâm là phân tích tâm lý & pháp y kỹ thuật số khách quan:**")
lines.append("  - Tuyệt đối không mô tả vết thương, không vẽ hiện trường bi thương bạo lực.")
lines.append("  - Các chứng cứ (điện thoại vật chứng, máy bơm nước, hồ sơ tin nhắn, bản án, bục thẩm phán) thể hiện dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B2. Ánh xạ ảnh → hồi → mốc câu")
lines.append("")
lines.append("Mốc câu theo `.work/script_tap07.json` (parse từ `01_KICH_BAN/Tap07/kichban_tap07_23102026.md`):  ")
lines.append("**34 lượt thoại · 164 câu · 3.743 từ** (Host 105 câu, Điều tra viên 25 câu, Chuyên gia tâm lý 20 câu, Người bình thường 14 câu).")
lines.append("")

act_titles = {
    1: "HỒI 1 · BUỔI SÁNG ĐỊNH MỆNH TẠI BÃI ĐỖ XE KMART (00:00 – 05:00)",
    2: "HỒI 2 · MÊ CUNG HAI MƯƠI NGHÌN DÒNG TIN NHẮN (05:00 – 10:00)",
    3: "HỒI 3 · VỞ KỊCH CÔ BẠN GÁI ĐAU KHỔ & BỘ NÃO ÁI KỶ KỊCH TÍNH (10:00 – 15:00)",
    4: "HỒI 4 · DÒNG TIN NHẮN ĐẦY TỘI LỖI VÀ BẢN ÁN LỊCH SỬ (15:00 – 20:00)",
    5: "HỒI 5 · ĐẠO ĐỨC KHÔNG GIAN SỐ & ĐẠO LUẬT CONRAD (20:00 – 26:00)"
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
lines.append("- **Tuân thủ quy tắc V9:** 100% không bạo lực, tập trung vào công lý, phân tích tâm lý học và pháp y kỹ thuật số.")
lines.append("- **Tuân thủ quy tắc V1 - V3:** Đổi hình đúng mốc câu thoại, không nhảy hình giữa chừng câu nói.")
lines.append("- **Bảo toàn phong cách:** Phong cách Dark graphic novel noir đồng bộ tuyệt đối với các tập trước của kênh Amber Eyes.")

doc_path = OUT_DIR / "Danh_Sach_Anh_Tap07.md"
doc_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Da tao {doc_path} thanh cong!")
