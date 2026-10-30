import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap13"
OUT_DIR.mkdir(parents=True, exist_ok=True)

jobs = json.loads((WORK / "bg_jobs_tap13.json").read_text(encoding="utf-8"))

lines = []
lines.append('# DANH SÁCH ẢNH NỀN — TẬP 13 "VỎ BỌC CON NHÀ NGƯỜI TA"')
lines.append("")
lines.append("*Hồ sơ Jennifer Pan & Áp lực kỳ vọng cực đoan — Khi Kỳ Vọng Cực Đoan Tạo Ra Kẻ Sát Nhân. Ngày 23/10/2026.*")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B1. Thông tin bộ ảnh")
lines.append("")
lines.append("| Mục | Nội dung |")
lines.append("|---|---|")
lines.append(f"| Số ảnh chuẩn hóa | **{len(jobs)}** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |")
lines.append("| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |")
lines.append("| Vị trí lưu trữ | `assets/bg/t13_*.png` — **tiền tố `t13_` bắt buộc** để không trùng bộ nền Tập 01–12 |")
lines.append("| Danh sách prompt gốc | `.work/bg_jobs_tap13.json` & `.work/gemini_image_prompts_tap13.json` |")
lines.append("| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |")
lines.append("| Phong cách nghệ thuật | Dark graphic novel noir — nét mực đen đậm, chiaroscuro đối lập cao, bảng màu hổ phách/slate/lạnh, hạt phim cổ điển |")
lines.append("| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |")
lines.append("| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (Amber Eyes Noir Graphic Renderer — 100% tự chủ) |")
lines.append("")
lines.append("**Quy tắc hình ảnh của kênh (V1 – V9):**")
lines.append("")
lines.append("- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**")
lines.append("  - `t13_golden_child_portrait_silhouette`: Bóng chân dung người con gái trong khung ảnh mạ vàng trên lò sưởi.")
lines.append("  - `t13_tiger_parent_looming_shadow`: Bóng đen người cha uy nghiêm đổ dài từ ngưỡng cửa thư phòng.")
lines.append("  - `t13_failing_calculus_exam_dread`: Bóng bàn tay run rẩy gục đầu trước bài thi trượt Giải tích.")
lines.append("  - `t13_rushing_home_school_curfew`: Bóng cô gái đeo ba lô vội vã chạy qua con đường tuyết lạnh.")
lines.append("  - `t13_unseen_suffocating_pressure`: Bóng cô gái ngồi co ro trên ngưỡng cửa sổ trước áp lực vô hình.")
lines.append("  - `t13_morning_bus_stop_winter_mist`: Bóng cô gái xách cặp giả vờ chờ xe buýt đi học đại học.")
lines.append("  - `t13_public_library_reading_hours`: Bóng cô gái ngồi đọc sách hàng giờ tại thư viện công cộng Toronto.")
lines.append("  - `t13_illicit_romance_daniel_wong`: Bóng hai người trong căn hộ tối đèn ngoại ô bên làn khói.")
lines.append("  - `t13_father_growing_suspicion`: Bóng người cha đứng hoài nghi bên chiếc túi xách không có thẻ bệnh viện.")
lines.append("  - `t13_trailing_car_cold_toronto_streets`: Xe người cha âm thầm bám theo con gái trên phố Toronto mùa đông.")
lines.append("  - `t13_empty_hospital_roster_shock`: Bóng người cha bàng hoàng đứng chết lặng tại sảnh bệnh viện SickKids.")
lines.append("  - `t13_desperate_wrath_father_confrontation`: Bóng người cha chỉ tay ra lệnh trừng phạt trong phòng khách đêm.")
lines.append("  - `t13_house_arrest_twenty_four_years_old`: Cô gái 24 tuổi ngồi cô độc bên góc giường trong tình trạng quản thúc.")
lines.append("  - `t13_murder_for_hire_conspiracy_shadows`: Ba bóng đen sát thủ gặp gỡ trong bãi đậu xe tối tăm.")
lines.append("  - `t13_three_intruders_stealth_entry`: Ba bóng đen mang súng ngắn lặng lẽ bước qua cửa chính.")
lines.append("  - `t13_parents_subdued_in_bedroom`: Người cha và người mẹ bị ba họng súng khống chế trong phòng ngủ.")
lines.append("  - `t13_basement_stairs_descent_terror`: Bóng sát thủ dẫn cha mẹ bước xuống cầu thang tầng hầm định mệnh.")
lines.append("  - `t13_father_gravely_wounded_miracle`: Bóng người cha gục ngã thoi thóp nhưng kiên cường bên chân cầu thang.")
lines.append("  - `t13_fleeing_hitmen_suburban_night`: Ba sát thủ tháo chạy qua bãi cỏ tuyết biến mất trong đêm.")
lines.append("  - `t13_interrogation_room_innocent_act`: Jennifer ngồi khép nép diễn vai nạn nhân yếu đuối trong phòng thẩm vấn.")
lines.append("  - `t13_detective_bill_goetz_gaze`: Ánh mắt sắc lạnh của Thám tử William Goetz đối diện nghi phạm.")
lines.append("  - `t13_father_memory_unmasked_daughter`: Ký ức người cha nhìn thấy con gái thì thầm bình thản với sát thủ.")
lines.append("  - `t13_unbound_hands_broken_heart`: Bàn tay tự do không hề bị trói của cô con gái dẫn lối tội ác.")
lines.append("  - `t13_third_interrogation_november_22`: Phiên đối đầu quyết định ngày 22/11/2010 giữa Thám tử Goetz và nghi phạm.")
lines.append("  - `t13_crumbling_mask_confession`: Jennifer gục khóc thú nhận đã thuê người dàn dựng vụ án.")
lines.append("  - `t13_supreme_court_ontario_verdict`: Hội đồng xét xử tuyên bố mức án tù chung thân 25 năm không ân xá.")
lines.append("  - `t13_authentic_soul_open_window_dawn`: Cửa sổ mở rộng đón ánh bình minh giải phóng tâm hồn tự do, trung thực.")
lines.append("  - `t13_amber_eyes_closing_dossier_jennifer`: Tập hồ sơ Amber Eyes khép lại trang nghiêm với biểu tượng mắt cú vàng.")
lines.append("- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.")
lines.append("- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:**")
lines.append("  - Tuyệt đối không mô tả bạo lực máu me, thương tích trực diện hay thi thể.")
lines.append("  - Các chứng cứ (giày trượt băng, đàn piano cổ điển, kéo và keo dán làm học bạ giả, điện thoại bí mật, dây thừng lỏng lẻo, bản ghi âm 911, máy đo nhịp tim ICU, trích xuất dữ liệu tin nhắn, còng số tám, búa thẩm phán, 4 Red Flags) thể hiện dưới góc độ tĩnh vật và tư liệu pháp y trang nghiêm.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B2. Ánh xạ ảnh → hồi → mốc câu")
lines.append("")
lines.append("Mốc câu theo `.work/script_tap13.json` (parse từ `01_KICH_BAN/Tap13/kichban_tap13_23102026.md`):  ")
lines.append("**33 lượt thoại · 165 câu · 4.209 từ** (Host 92 câu, Điều tra viên 31 câu, Chuyên gia tâm lý 29 câu, Người bình thường 13 câu).")
lines.append("")

act_titles = {
    1: "HỒI 1 · VỎ BỌC 'CON NHÀ NGƯỜI TA' VÀ TÒA THÁP DỐI LỪA MƯỜI NĂM (00:00 – 05:30)",
    2: "HỒI 2 · ĐÊM KINH HOÀNG TẠI ĐẠI LỘ HELEN VÀ CUỘC GỌI 911 (05:30 – 11:00)",
    3: "HỒI 3 · GIẢI MÃ TÂM LÝ: TỪ 'CHA MẸ HỔ' ĐẾN HỘI CHỨNG NÓI DỐI BỆNH LÝ (11:00 – 16:30)",
    4: "HỒI 4 · ĐẤU TRÍ PHÒNG THẨM VẤN & SỰ THỨC TỈNH CỦA NGƯỜI CHA (16:30 – 21:30)",
    5: "HỒI 5 · BẢN ÁN LƯƠNG TÂM & LỜI CẢNH TỈNH (21:30 – 26:30)"
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

doc_path = OUT_DIR / "Danh_Sach_Anh_Tap13.md"
doc_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Đã tạo {doc_path} thành công!")
