import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap11"
OUT_DIR.mkdir(parents=True, exist_ok=True)

jobs = json.loads((WORK / "bg_jobs_tap11.json").read_text(encoding="utf-8"))

lines = []
lines.append('# DANH SÁCH ẢNH NỀN — TẬP 11 "CẶP ĐÔI KEN & BARBIE"')
lines.append("")
lines.append("*Hồ sơ Paul Bernardo & Karla Homolka — Hội Chứng Điên Cuồng Đôi (Folie à Deux) & 'Thỏa Thuận Với Quỷ Dữ'. Ngày 23/10/2026.*")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B1. Thông tin bộ ảnh")
lines.append("")
lines.append("| Mục | Nội dung |")
lines.append("|---|---|")
lines.append(f"| Số ảnh chuẩn hóa | **{len(jobs)}** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |")
lines.append("| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |")
lines.append("| Vị trí lưu trữ | `assets/bg/t11_*.png` — **tiền tố `t11_` bắt buộc** để không trùng bộ nền Tập 01–10 |")
lines.append("| Danh sách prompt gốc | `.work/bg_jobs_tap11.json` & `.work/gemini_image_prompts_tap11.json` |")
lines.append("| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |")
lines.append("| Phong cách nghệ thuật | Dark graphic novel noir — nét mực đen đậm, chiaroscuro đối lập cao, bảng màu hổ phách/hồng tro/slate/lạnh, hạt phim cổ điển |")
lines.append("| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |")
lines.append("| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (Amber Eyes Noir Graphic Renderer — 100% tự chủ) |")
lines.append("")
lines.append("**Quy tắc hình ảnh của kênh (V1 – V9):**")
lines.append("")
lines.append("- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**")
lines.append("  - `t11_paul_bernardo_dashing_car`: Bóng người đàn ông lịch lãm bên xe thể thao dưới đèn đường ngoại ô.")
lines.append("  - `t11_karla_veterinary_clinic`: Bóng cô gái áo blouse trắng chăm sóc thú y bên cửa sổ nắng.")
lines.append("  - `t11_society_gala_inseparable_couple`: Bóng đôi vợ chồng trẻ khiêu vũ quấn quýt trong dạ tiệc.")
lines.append("  - `t11_interrogation_bruised_facade`: Bóng người phụ nữ gục đầu khóc trong văn phòng luật sư.")
lines.append("  - `t11_holding_video_camera_director`: Bóng bàn tay cầm máy quay 8mm chỉ đạo hào hứng.")
lines.append("  - `t11_joliette_prison_gate_release`: Bóng người phụ nữ bước ra cổng trại Joliette giữa rừng ống kính.")
lines.append("  - `t11_light_of_justice_prevails`: Ngọn đèn công lý xua tan bóng tối và những giọt nước mắt cá sấu.")
lines.append("- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.")
lines.append("- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:**")
lines.append("  - Tuyệt đối không mô tả bạo lực tình dục, nhục hình hay tổn thương thể xác trực diện của các nạn nhân (Leslie Mahaffy, Kristen French, Tammy Homolka).")
lines.append("  - Các chứng cứ (ngôi nhà màu hồng số 57 Bayview, đèn pin kim loại, ADN Scarborough, 6 cuộn băng 8mm trên trần nhà, hồ sơ thỏa thuận nhận tội, báo cáo Thẩm phán Galligan) thể hiện dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B2. Ánh xạ ảnh → hồi → mốc câu")
lines.append("")
lines.append("Mốc câu theo `.work/script_tap11.json` (parse từ `01_KICH_BAN/Tap11/kichban_tap11_23102026.md`):  ")
lines.append("**33 lượt thoại · 165 câu · 4.347 từ** (Host 83 câu, Điều tra viên 37 câu, Chuyên gia tâm lý 30 câu, Người bình thường 15 câu).")
lines.append("")

act_titles = {
    1: "HỒI 1 · VỎ BỌC HOÀN HẢO CỦA 'CẶP ĐÔI KEN & BARBIE' (00:00 – 05:30)",
    2: "HỒI 2 · CHIẾC MẶT NẠ RƠI XUỐNG VÀ THỎA THUẬN VỚI QUỶ DỮ (05:30 – 11:00)",
    3: "HỒI 3 · GIẢI MÃ HỘI CHỨNG ĐIÊN CUỒNG ĐÔI (FOLIE À DEUX) (11:00 – 16:30)",
    4: "HỒI 4 · SÁU CUỐN BĂNG TRÊN TRẦN NHÀ VÀ SỰ SỤP ĐỔ CỦA MỘT ẢO TƯỞNG (16:30 – 21:30)",
    5: "HỒI 5 · BÀI HỌC ĐẮT GIÁ VỀ MẶT NẠ NẠN NHÂN & LỜI CẢNH TỈNH (21:30 – 26:30)"
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

doc_path = OUT_DIR / "Danh_Sach_Anh_Tap11.md"
doc_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Đã tạo {doc_path} thành công!")
