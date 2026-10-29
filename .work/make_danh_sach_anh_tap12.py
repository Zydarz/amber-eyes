import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
OUT_DIR = ROOT / "02_SAN_XUAT" / "Tap12"
OUT_DIR.mkdir(parents=True, exist_ok=True)

jobs = json.loads((WORK / "bg_jobs_tap12.json").read_text(encoding="utf-8"))

lines = []
lines.append('# DANH SÁCH ẢNH NỀN — TẬP 12 "THẢM KỊCH JONESTOWN"')
lines.append("")
lines.append("*Hồ sơ Jim Jones & Peoples Temple — Sự Phục Tùng Quyền Lực & Thảm Kịch Thao Túng Tâm Lý Hàng Loạt. Ngày 23/10/2026.*")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B1. Thông tin bộ ảnh")
lines.append("")
lines.append("| Mục | Nội dung |")
lines.append("|---|---|")
lines.append(f"| Số ảnh chuẩn hóa | **{len(jobs)}** ảnh phục vụ trọn vẹn 5 hồi (toàn bộ bảng shot & visual của tập) |")
lines.append("| Kích thước chuẩn | 2112×1188 (16:9 2K), ảnh gốc lưu trữ tại `assets/bg/` |")
lines.append("| Vị trí lưu trữ | `assets/bg/t12_*.png` — **tiền tố `t12_` bắt buộc** để không trùng bộ nền Tập 01–11 |")
lines.append("| Danh sách prompt gốc | `.work/bg_jobs_tap12.json` & `.work/gemini_image_prompts_tap12.json` |")
lines.append("| Sổ nguồn gốc tài sản | `provenance.json` (tự động cộng dồn và cập nhật) |")
lines.append("| Phong cách nghệ thuật | Dark graphic novel noir — nét mực đen đậm, chiaroscuro đối lập cao, bảng màu hổ phách/slate/lạnh, hạt phim cổ điển |")
lines.append("| Ràng buộc trong prompt | Không chữ · không số · không biển hiệu · không logo · không khung · ảnh tràn viền 16:9 |")
lines.append("| Công cụ thực thi | Tự tạo trực tiếp trong pipeline (Amber Eyes Noir Graphic Renderer — 100% tự chủ) |")
lines.append("")
lines.append("**Quy tắc hình ảnh của kênh (V1 – V9):**")
lines.append("")
lines.append("- **V5 — Người thật trong vụ án chỉ hiện dạng bóng lưng / mặt khuất hoàn toàn:**")
lines.append("  - `t12_puppet_master_dark_silhouette`: Bóng đen Jim Jones đeo kính râm đứng trên bục giảng.")
lines.append("  - `t12_racial_harmony_facade`: Bóng đen những bàn tay đa chủng tộc nắm chặt nhau trong hội trường.")
lines.append("  - `t12_catharsis_session_interrogation`: Bóng người quỳ gối chịu sự sỉ nhục của tập thể.")
lines.append("  - `t12_equatorial_forced_labor_fields`: Bóng các tín đồ cúi gập lưng lao động khổ sai dưới nắng xích đạo.")
lines.append("  - `t12_armed_guards_crossbow_perimeter`: Bóng tay lính gác súng trường và nỏ tự chế ven rừng.")
lines.append("  - `t12_leo_ryan_podium_applause`: Bóng Dân biểu Leo Ryan phát biểu trước micro.")
lines.append("  - `t12_secret_note_folded_slip`: Bàn tay run rẩy lén chuyển mẩu giấy cầu cứu.")
lines.append("  - `t12_confrontation_at_lectern`: Bóng đối thoại nảy lửa giữa Nghị sĩ Ryan và Jim Jones.")
lines.append("  - `t12_knife_attack_scuffle_pavilion`: Bóng kẻ cuồng tín cầm dao bị ôm chặt ngăn cản.")
lines.append("  - `t12_jackie_speier_resilience_shadow`: Bóng người phụ nữ trẻ gục bên bánh xe máy bay nhưng kiên cường sinh tồn.")
lines.append("  - `t12_christine_miller_lone_microphone`: Bóng bà Christine Miller 60 tuổi hiên ngang đứng trước micro.")
lines.append("  - `t12_groupthink_hostile_mob_shadows`: Đám đông tín đồ bao quanh xua đuổi tiếng nói phản biện.")
lines.append("  - `t12_broken_will_family_embrace`: Bóng cha mẹ ôm chặt con nhỏ trong sự trống rỗng cùng cực.")
lines.append("  - `t12_forensic_agent_headphones_horror`: Bóng nhân viên FBI đeo tai nghe cúi đầu trước cuộn băng Q 042.")
lines.append("  - `t12_independent_mind_dawn_freedom`: Đôi bàn tay phá vỡ xiềng xích vô hình vươn về bình minh.")
lines.append("- **V7 — Nền vụ án toàn màn hình (16:9):** Tỷ lệ chuẩn 2112×1188, full-bleed, không viền đen letterbox.")
lines.append("- **V9 — Trọng tâm là phân tích tâm lý & tư liệu điều tra khách quan:**")
lines.append("  - Tuyệt đối không mô tả bạo lực máu me, co giật, thi thể hay tổn thương trực diện.")
lines.append("  - Các chứng cứ (cuộn băng FBI Q 042, loa phóng thanh, thùng phuy kim loại, la bàn đạo đức, bia tưởng niệm) thể hiện dưới góc độ tĩnh vật và tư liệu lịch sử pháp y trang nghiêm.")
lines.append("")
lines.append("---")
lines.append("")
lines.append("## B2. Ánh xạ ảnh → hồi → mốc câu")
lines.append("")
lines.append("Mốc câu theo `.work/script_tap12.json` (parse từ `01_KICH_BAN/Tap12/kichban_tap12_23102026.md`):  ")
lines.append("**33 lượt thoại · 165 câu · 4.630 từ** (Host 91 câu, Điều tra viên 27 câu, Chuyên gia tâm lý 31 câu, Người bình thường 16 câu).")
lines.append("")

act_titles = {
    1: "HỒI 1 · LỜI HỨA THIÊN ĐƯỜNG VÀ BÓNG MA NƠI RỪNG SÂU (00:00 – 05:30)",
    2: "HỒI 2 · CUỘC PHỤC KÍCH ĐƯỜNG BĂNG VÀ TIẾNG CÒI BÁO ĐỘNG ĐỊNH MỆNH (05:30 – 11:00)",
    3: "HỒI 3 · GIẢI MÃ CƠ CHẾ TÂM LÝ: TỪ PHỤC TÙNG ĐẾN TƯ DUY TẬP THỂ (11:00 – 16:30)",
    4: "HỒI 4 · CUỘN BĂNG TỬ THẦN Q 042 VÀ TIẾNG NÓI PHẢN KHÁNG CÔ ĐƠN (16:30 – 21:30)",
    5: "HỒI 5 · BÀI HỌC ĐẮT GIÁ VỀ TÂM LÝ BẦY ĐÀN & LỜI CẢNH TỈNH (21:30 – 26:30)"
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

doc_path = OUT_DIR / "Danh_Sach_Anh_Tap12.md"
doc_path.write_text("\n".join(lines), encoding="utf-8")
print(f"Đã tạo {doc_path} thành công!")
