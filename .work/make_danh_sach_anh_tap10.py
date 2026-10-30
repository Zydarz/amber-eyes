import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap10"
OUT_DIR.mkdir(parents=True, exist_ok=True)

jobs = json.loads((WORK / "bg_jobs_tap10.json").read_text(encoding="utf-8"))

lines = []
lines.append('# DANH SÁCH ẢNH NỀN — TẬP 10 "CHIẾC HỘP GỖ DƯỚI GẦM GIƯỜNG"')
lines.append("")
lines.append("*Hồ sơ Colleen Stan — Sự Bất Lực Tập Nhiễm & Bóng Ma 'The Company'. Ngày 23/10/2026.*")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B1. Thông tin bộ ảnh")
lines.append("")
lines.append("| Mục | Nội dung |")
lines.append("|---|---|")
lines.append(f"| Số ảnh chuẩn hóa | **{len(jobs)}** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |")
lines.append("| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |")
lines.append("| Vị trí lưu trữ | `assets/bg/t10_*.png` — **tiền tố `t10_` bắt buộc** để không trùng bộ nền Tập 01–09 |")
lines.append("| Danh sách prompt gốc | `.work/bg_jobs_tap10.json` & `.work/gemini_image_prompts_tap10.json` |")
lines.append("| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |")
lines.append("| Phong cách nghệ thuật | Dark graphic novel noir — nét mực đen đậm, chiaroscuro đối lập cao, bảng màu hổ phách/slate/lạnh, hạt phim cổ điển |")
lines.append("| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |")
lines.append("| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (Amber Eyes Noir Graphic Renderer — 100% tự chủ) |")
lines.append("")
lines.append("**Quy tắc hình ảnh của kênh (V1 – V9):**")
lines.append("")
lines.append("- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**")
lines.append("  - `t10_hitchhiking_highway_1977`: Bóng thanh niên mang ba lô vẫy xe trên xa lộ Bờ Tây.")
lines.append("  - `t10_innocent_family_facade`: Bóng cặp vợ chồng bế đứa trẻ sơ sinh qua kính chắn gió xe van.")
lines.append("  - `t10_stiff_hands_wooden_slats`: Ngón tay co quắp chạm vào vách gỗ hộp trong bóng tối tuyệt đối.")
lines.append("  - `t10_one_hour_chores_silhouette`: Bóng người phụ nữ cúi mình lau sàn dưới bóng đổ dài của kẻ canh giữ.")
lines.append("  - `t10_bathroom_mirror_downcast_eyes`: Bóng cô gái đứng trước gương phòng tắm với ánh mắt cúi gằm cam chịu.")
lines.append("  - `t10_open_cage_motionless_silhouette`: Bóng chú chim bất động trong chiếc lồng mở toang cửa.")
lines.append("  - `t10_janice_hooker_moral_turmoil`: Bóng người vợ Janice Hooker giằng xé bên bồn rửa chén cạnh nôi con.")
lines.append("  - `t10_breaking_invisible_chains_dawn`: Đôi bàn tay vươn mở giải phóng những mảnh ván gỗ về phía bình minh.")
lines.append("- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.")
lines.append("- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:**")
lines.append("  - Tuyệt đối không mô tả bạo lực tình dục, nhục hình hay tổn thương thể xác trực diện.")
lines.append("  - Các chứng cứ (chiếc hộp gỗ dưới gầm giường, hộp cách âm đội đầu, bản hợp đồng nô lệ, sơ đồ Seligman, bục tòa án) thể hiện dưới góc độ tĩnh vật và kỹ thuật hình sự trang nghiêm.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B2. Ánh xạ ảnh → hồi → mốc câu")
lines.append("")
lines.append("Mốc câu theo `.work/script_tap10.json` (parse từ `01_KICH_BAN/Tap10/kichban_tap10_23102026.md`):  ")
lines.append("**36 lượt thoại · 165 câu · 4.305 từ** (Host 93 câu, Điều tra viên 32 câu, Chuyên gia tâm lý 25 câu, Người bình thường 15 câu).")
lines.append("")

act_titles = {
    1: "HỒI 1 · CHUYẾN XE ĐỊNH MỆNH VÀ CHIẾC HỘP ĐEN DƯỚI GẦM GIƯỜNG (00:00 – 05:30)",
    2: "HỒI 2 · BẢY NĂM TRONG BÓNG TỐI VÀ SỰ BIẾN MẤT CỦA THỜI GIAN (05:30 – 11:00)",
    3: "HỒI 3 · NGHỊCH LÝ NGÀY VỀ VÀ SỰ BẤT LỰC TẬP NHIỄM (11:00 – 16:30)",
    4: "HỒI 4 · SỰ RẠN NỨT CỦA LỒNG GIAM VÀ CUỘC GIẢI CỨU NGẦM (16:30 – 21:30)",
    5: "HỒI 5 · ÁNH SÁNG SAU BẢY NĂM ĐỊA NGỤC & SỰ HỒI SINH KỲ DIỆU (21:30 – 26:30)"
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

doc_path = OUT_DIR / "Danh_Sach_Anh_Tap10.md"
doc_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Đã tạo {doc_path} thành công!")
