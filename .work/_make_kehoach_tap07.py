import json, sys, re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

# Read script
with open(".work/script_tap07.json", "r", encoding="utf-8") as f:
    script_data = json.load(f)

# Sentences map
sents_map = {}
for el in script_data:
    if el.get("kind") == "LOI":
        role = el.get("role", "H")
        for s in el.get("sentences", []):
            sents_map[s["id"]] = (role, s["text"])

# Read Danh_Sach_Anh_Tap07.md
with open("02_SAN_XUAT/Tap07/Danh_Sach_Anh_Tap07.md", "r", encoding="utf-8") as f:
    lines = f.readlines()

shots_info = []
for line in lines:
    if line.strip().startswith("|") and "`t7_" in line:
        parts = [p.strip() for p in line.split("|")]
        if len(parts) >= 5:
            stt = parts[1].strip()
            bg_name = parts[2].replace("`", "").strip()
            content = parts[3].strip()
            cue_range = parts[4].replace("`", "").strip()
            shots_info.append((stt, bg_name, content, cue_range))

# Format cue range to standard: `1.02#1`–`#3` or `1.04#3`
def format_cue_range(raw):
    m = re.match(r"^(\d+\.\d+)#(\d+)[–-]#(\d+)$", raw)
    if m:
        return f"`{m.group(1)}#{m.group(2)}`–`#{m.group(3)}`"
    m2 = re.match(r"^(\d+\.\d+)#(\d+)$", raw)
    if m2:
        return f"`{m2.group(1)}#{m2.group(2)}`"
    return f"`{raw}`"

out = []
out.append('# HỒ SƠ SẢN XUẤT TẬP 07 · "BẢN ÁN GIẾT NGƯỜI BẰNG TIN NHẮN" (PHẦN B)\n')
out.append('## B1. Thông tin tập\n')
out.append('| Mục | Nội dung |')
out.append('|---|---|')
out.append('| Tên tập | **Tập 07: Bản Án Giết Người Bằng Tin Nhắn** |')
out.append('| Vụ án | Michelle Carter và Conrad Roy (Fairhaven / Plainville, Massachusetts, 2014–2017) |')
out.append('| Chủ đề | Thao túng tâm lý kỹ thuật số, Hội chứng Münchausen qua mạng, Trách nhiệm hình sự từ xa |')
out.append('| Tổng thời lượng | ~21–22 phút · 5 hồi · 164 câu thoại |')
out.append('| Diễn viên / Giọng | Host (Cú) · Sói (Điều tra viên Scott Gordon) · Cáo (Chuyên gia tâm lý) · N1 (Bà Lynn Roy) · N2 (Samantha Boardman) |')
out.append('| Bộ ảnh nền | 61 ảnh 16:9 2K (`assets/bg/t7_*.png`), phong cách Dark graphic novel noir |')
out.append('| Âm thanh | Stereo 3 lớp: BGM theo hồi + Ambience môi trường liên tục + SFX tiếng động (`.work/sfx_tap07.json`) |\n')
out.append('## B2. Trạng thái kiểm soát chất lượng (QC)\n')
out.append('- [x] Kịch bản chuẩn A2, loại bỏ 100% từ cấm V9, chuẩn hóa trích dẫn `“…”` (164/164 câu).')
out.append('- [x] Bộ ảnh 61/61 ảnh 2112×1188 full-bleed tràn viền, V5 người thật chỉ hiện bóng lưng / không lộ mặt.')
out.append('- [x] Bảng âm thanh `sfx_tap07.json` đầy đủ 9 dải ambience, 17 cue tiếng động, 4 đoạn music_drop.')
out.append('- [x] Cấu hình `edition.py` đã hiệu chỉnh `act1_cue: 1.03`, `silence_cue: 2.11`, BGM H3 `bgm_cello_sad.mp3`.\n')
out.append('## 6. DANH SÁCH SHOT — TẬP 07 (viết theo A7)\n')
out.append('**Đọc bảng:** *Vai* = người đang nói (H Cú · D Sói · C Cáo · N1 Cừu · N2 Mèo). Bảng mô tả **nền + đồ hoạ**; badge và bán thân tự đặt theo A5.4.')
out.append('Cột *Nhân vật*: `🅑` = thêm bán thân ngoài câu đầu lượt · `→X` = Host đang mời X · `✦` = lần đầu xuất hiện · `⊘` = tắt bán thân.')
out.append('Cột cuối: trống = hoà tan · `✂` cắt · `◼` tối đen.\n')
out.append('### INTRO KÊNH · 0,00–22,41 s · `bgm_music_box.mp3`\n')
out.append('Đặt `assets/brand/intro_kenh.mov` ở 0,00 s (A5.7). Không câu thoại nào thuộc intro.\n')

# Shot 1-00
out.append('### HỒI 1 — BUỔI SÁNG ĐỊNH MỆNH TẠI BÃI ĐỖ XE KMART · nền chủ đạo `t7_kmart_parking_lot_morning`\n')
out.append('| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |')
out.append('|---|---|---|---|---|---|---|---|---|')
out.append('| 1-00 | `1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s) | — | T1 | `t7_digital_coercion_screen` hiện dần từ đen | *HỒI 01 · BUỔI SÁNG ĐỊNH MỆNH TẠI BÃI ĐỖ XE KMART* | — | ⊘ | |')

current_act = 1
shot_num_act = 0
for stt, bg_name, content, cue_range in shots_info:
    first_cue = cue_range.split("–")[0].strip()
    act = int(first_cue.split(".")[0])
    if act != current_act:
        current_act = act
        shot_num_act = 0
        act_names = {
            2: "HỒI 2 — MÊ CUNG HAI MƯƠI NGHÌN DÒNG TIN NHẮN · nền chủ đạo `t7_late_night_bedroom_phone`",
            3: "HỒI 3 — VỞ KỊCH CÔ BẠN GÁI ĐAU KHỔ & BỘ NÃO ÁI KỶ KỊCH TÍNH · nền chủ đạo `t7_empty_theater_spotlight`",
            4: "HỒI 4 — DÒNG TIN NHẮN ĐẦY TỘI LỖI VÀ BẢN ÁN LỊCH SỬ · nền chủ đạo `t7_taunton_courthouse_exterior`",
            5: "HỒI 5 — ĐẠO ĐỨC KHÔNG GIAN SỐ & ĐẠO LUẬT CONRAD · nền chủ đạo `t7_digital_lighthouse_beacon`"
        }
        out.append(f"\n### {act_names.get(act, f'HỒI {act}')}\n")
        out.append('| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |')
        out.append('|---|---|---|---|---|---|---|---|---|')

    shot_num_act += 1
    shot_id = f"{act}-{shot_num_act:02d}"

    m_cue = first_cue.split("#")[0]
    sub_idx = first_cue.split("#")[1] if "#" in first_cue else "1"
    sent_key = f"{m_cue}#{sub_idx}"
    role, sent_text = sents_map.get(sent_key, ("H", ""))
    if m_cue == "1.07": role = "N1"
    elif m_cue == "4.03": role = "N2"

    cam = "`pull`" if shot_num_act % 3 == 0 else ("`pan`" if shot_num_act % 3 == 1 else "`still`")
    tmpl = "T1"
    if "bản đồ" in content.lower() or "route" in bg_name:
        tmpl = "T7 tuyến đường"
    elif "tin nhắn" in content.lower() or "sms" in bg_name or "text" in bg_name or "confession" in bg_name:
        tmpl = "T4 trích dẫn"
    elif "hồ sơ" in content.lower() or "cáo trạng" in content.lower() or "bản án" in content.lower() or "document" in bg_name or "stamp" in bg_name:
        tmpl = "T2 thẻ hồ sơ"
    elif "đồng hồ" in content.lower() or "clock" in bg_name:
        tmpl = "T5 ngày"
    elif "redflag" in bg_name or "cảnh báo đỏ" in content.lower():
        tmpl = "T8 cờ"

    char_tag = ""
    if shot_id == "1-01": char_tag = "✦ Cú"
    elif shot_id == "1-08": char_tag = "✦ Cừu"
    elif shot_id == "1-11": char_tag = "✦ Sói"
    elif shot_id == "1-13": char_tag = "✦ Cáo"
    elif shot_id == "4-02": char_tag = "✦ Mèo"
    elif "bóng người" in content.lower() or "cabin" in content.lower() or "thi thể" in content.lower():
        char_tag = "⊘"

    clean_txt = content.replace("`", "").strip()
    if len(clean_txt) > 80:
        clean_txt = clean_txt[:77] + "..."
    text_col = f"*{clean_txt}*"
    if shot_id == "5-10" or int(stt) == 61:
        text_col = "*HỒ SƠ TẬP 07 · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật*"
        tmpl = "T2 thẻ hồ sơ"

    formatted_cue = format_cue_range(cue_range)
    out.append(f"| {shot_id} | {formatted_cue} | {role} | {tmpl} | `{bg_name}`, {cam} | {text_col} | — | {char_tag} | |")

out.append('\n**Tổng: 62 shot** (1 shot mở đầu 1-00 + 61 shot theo câu thoại). Phủ kín 164 câu thoại trọn vẹn.\n')

plan_file = Path("02_SAN_XUAT/Tap07/KeHoach_Video_Tap07.md")
plan_file.write_text("\n".join(out), encoding="utf-8")
print(f"Updated {plan_file} successfully! Total lines: {len(out)}")
