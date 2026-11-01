# -*- coding: utf-8 -*-
"""Sua bang shot (muc 6) cua ho so Tap05 cho khop script 162 cau (Higgs).

Ly do: kich ban duoc tach lai 164 -> 162 cau; 4 element doi so cau
(2.02, 2.04, 4.02, 4.12) va nhieu cau bi VIET LAI => bang shot cu tro toi
ma khong ton tai + chu tren hinh khong con nam trong cau (H6/V3).

Cach sua: chi sua 3 cot cua tung dong (Cot "Cau", "Chu", "Beat") va cot
"Nen + bong" khi can doi nen. Giu nguyen phan con lai cua dong.
Sao luu file goc vao .work/_cu/ truoc khi ghi (L5).
"""
import re
import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")
PLAN = ROOT / "02_SAN_XUAT" / "Tap05" / "KeHoach_Video_Tap05.md"
BACKUP = ROOT / ".work" / "_cu" / "t05_shots_patch_20261101"

# shot_id -> {"range":..., "chu":..., "beat":..., "nen":...}
PATCH = {
    "1-02": {"chu": "**TÒA SOẠN BÁO THE WICHITA EAGLE** · *Nhận được một phong bì thư ký tên người gửi giả*"},
    "1-03": {"chu": "**BẢN SAO BẰNG LÁI VICKI WEGERLE** · *Cùng ba bản sao ảnh liên quan đến vụ án ấy*"},
    "1-06": {"chu": "**RÚNG ĐỘNG TOÀN BỘ NƯỚC MỸ** · *Tước đoạt mạng sống của 10 người từ 1974 đến 1991*"},
    "1-10": {"chu": "*HÃY HÌNH DUNG TÂM TRẠNG TỪ* · **MỘT NGƯỜI DÂN THỊ TRẤN PARK CITY**"},
    "1-11": {"chu": "“Khi nghe tin BTK gửi thư trở lại sau hơn một thập kỷ, cả thị trấn chúng tôi nín thở trong sợ hãi” → `#2`: “Người ta lại kiểm tra then cài cửa sổ, mua thêm súng và khóa chặt cửa trước khi trời tối.”"},
    "1-12": {"chu": "“Không một ai có thể ngờ rằng, kẻ thủ ác mà cả nước Mỹ đang lùng sục suốt 30 năm qua lại chính là người đàn ông mẫn cán hàng ngày đi đo chiều cao từng bãi cỏ”"},
    "1-13": {"chu": "**NGHỊCH LÝ KỲ DỊ NHẤT CỦA NGÀNH ĐIỀU TRA HÌNH SỰ** · *Kẻ thủ ác an toàn ngủ đông suốt 13 năm* → `#3`: *Các manh mối đã nguội lạnh* → `#4`: *Công nghệ lúc bấy giờ vẫn chưa lần ra được danh tính của hắn*"},
    "1-16": {"chu": "*XIN MỜI ĐIỀU TRA VIÊN MỞ LẠI HỒ SƠ CHUYÊN ÁN* · **BẮT ĐẦU CUỘC ĐẤU TRÍ LỊCH SỬ**"},
    "1-18": {"chu": "**BÀI BÁO KỶ NIỆM 30 NĂM CỦA THE WICHITA EAGLE** · *Luật sư Robert Beattie đang viết sách và nêu giả thuyết BTK đã chết hoặc đang ngồi tù*"},
    "2-02": {"range": "`2.02#3`–`#5`",
             "chu": "*BIỆT DANH TỰ ĐẶT* · **BTK** · *Chương trình xin không diễn giải chi tiết ba chữ ấy*"},
    "2-03": {"chu": "*KHOA HỌC HÀNH VI FBI · CHỮ KÝ TÂM LÝ ĐẶC TRƯNG* · *Đặc điểm thứ nhất là nhu cầu áp chế tuyệt đối* · *Được biến những người vô tội thành người hoàn toàn bất lực và sợ hãi*"},
    "2-04": {"nen": "`t5_trophy_lockbox`, `push`",
             "chu": "**THỨ HAI: NHU CẦU LƯU GIỮ CHIẾN LỢI PHẨM** · *Lấy đi bằng lái xe, đồng hồ hoặc đồ trang sức*"},
    "2-05": {"range": "`2.04#6`",
             "nen": "`t5_narcissist_mirror_shadow`",
             "chu": "**MÓN ĐỒ KHÔNG MANG GIÁ TRỊ VẬT CHẤT** · *Chúng kích hoạt cảm xúc để hắn hồi tưởng lại cảm giác thống trị mỗi khi ở một mình*"},
    "2-06": {"range": "`2.04#7`–`#8`"},
    "2-07": {"chu": "**MỘT KẺ SĂN MỒI TỈ MỈ VÀ CỰC KỲ KIÊN NHẪN** · *Nắm rõ kỹ thuật trinh sát, cẩn thận không lưu lại vân tay* → `#3`: *Danh tính thực sự phía sau chiếc mặt nạ*"},
    "2-10": {"chu": "**CHỦ TỊCH HỘI ĐỒNG NHÀ THỜ LUTHERAN CHÚA KITÔ** · *Người được cả giáo đoàn tin tưởng giao trọng trách*"},
    "2-11": {"chu": "**ĐỘI TRƯỞNG HƯỚNG ĐẠO SINH CUB SCOUT** · *Dạy trẻ em trong thị trấn cách dựng lều và rèn luyện tính trung thực*"},
    "3-06": {"chu": "*CƠ CHẾ PHÒNG VỆ ĐIỂN HÌNH* · **PHÓNG CHIẾU VÀ NGỤY BIỆN (RATIONALIZATION & PROJECTION)** · *Không phải hắn muốn làm, mà chính Nhân tố X bên trong buộc hắn phải làm*"},
    "3-07": {"chu": "**RỨ BỎ HOÀN TOÀN TRÁCH NHIỆM ĐẠO ĐỨC** · *Vừa thỏa mãn hưng tưởng đen tối, vừa quay về nhà ăn tối cùng vợ như một người đàn ông vô tội*"},
    "4-01": {"chu": "**ĐẦU NĂM 2005** · *Mệt mỏi với cắt dán bưu kiện giữa trời đông giá rét* → `#3`: *Muốn chuyển sang gửi tập tin vi tính* → `#4`: *Rader 59 tuổi và hoàn toàn mù mờ về công nghệ số*"},
    "4-02": {"chu": "**BÃI ĐỖ XE HOME DEPOT WICHITA** · *Hộp ngũ cốc đặt trên thùng xe bán tải cuối tháng 1 năm 2005*"},
    "4-03": {"range": "`4.02#6`–`#10`",
             "chu": "**CÂU HỎI NGÂY THƠ ĐẾN MỨC KHÓ TIN:** *'Tôi có thể liên lạc bằng Đĩa mềm vi tính mà không bị truy vết đến máy tính hay không?'*"},
    "4-05": {"chu": "**GIỮA THÁNG 2 NĂM 2005** · *Bưu phẩm gửi tới đài truyền hình KSAS-TV*"},
    "4-10": {"chu": "**TÌM KIẾM TRÊN CÔNG CỤ: 'Nhà thờ Lutheran Chúa Kitô Wichita Dennis'** · *Chủ tịch Hội đồng Nhà thờ: Dennis Rader*"},
    "4-11": {"chu": "**CHIẾC XE JEEP CHEROKEE MÀU ĐEN TRÊN CAMERA AN NINH** · *Khớp với chiếc xe xuất hiện tại bãi đỗ xe Home Depot*"},
    "4-12": {"chu": "*KẾT QUẢ ĐỐI CHIẾU ADN TẾ BÀO PAP SMEAR* · **XÁC NHẬN QUAN HỆ CHA CON** · *Mẫu tế bào y tế của con gái Rader từ trường đại học*",
             "beat": "Dấu mộc ở \"Quan hệ cha con\""},
    "4-13": {"chu": "**TRƯA NGÀY 25 THÁNG 2 NĂM 2005** · *Nhiều xe cảnh sát bao vây và chặn đứng đầu xe của hắn*"},
    "4-14": {"chu": "**CUỘC ĐỐI CHẤT KINH ĐIỂN TRONG PHÒNG HỎI CUNG** · *Hắn hỏi vì sao cảnh sát lại nói dối hắn về chiếc đĩa mềm* · *Và câu trả lời hắn nhận được rất ngắn gọn: Vì cảnh sát đang tìm cách bắt hắn*"},
    "4-15": {"range": "`4.12#5`–`#6`",
             "chu": "**CHIẾC MẶT NẠ VỠ VỤN HOÀN TOÀN** · *Thao thao bất tuyệt thú nhận từng vụ án trong nhiều giờ liền*"},
    "4-16": {"chu": "*HÃY HÌNH DUNG KHOẢNH KHẮC ĐỊNH MỆNH ẤY* · **KERRI RAWSON — CON GÁI RUỘT CỦA DENNIS RADER**"},
    "4-17": {"chu": "“Cả thế giới biết đến ông ấy như một con quái vật.” → `#4`: **“Kẻ bị cả đất nước truy lùng lại chính là người từng chúc cô ngủ ngon mỗi đêm.”**"},
    # --- vong 2: chinh xac 4 diem con lai ---
    # 5-08/5-09: cau "Và dấu hiệu thứ tư" (5.06#3) phai nam o shot CẢNH BÁO 04
    "5-08": {"range": "`5.06#1`–`#2`"},
    "5-09": {"range": "`5.06#3`–`#5`"},
    # 4-04: script moi bo so "494" -> khong duoc hien so nay tren hinh
    "4-04": {"chu": "*MỤC RAO VẶT BÁO THE WICHITA EAGLE* · **'REX, MỌI CHUYỆN SẼ ỔN ĐỂ GỬI NÓ'** · *Cú lừa tâm lý ngoạn mục của Trung úy Ken Landwehr*"},
}

IDX = {"range": 1, "nen": 4, "chu": 5, "beat": 6}


def main():
    BACKUP.mkdir(parents=True, exist_ok=True)
    bak = BACKUP / PLAN.name
    if not bak.exists():
        shutil.copy2(PLAN, bak)
        print("sao luu ->", bak)
    else:
        print("ban sao luu da ton tai, giu nguyen ->", bak)

    lines = PLAN.read_text(encoding="utf-8").splitlines()
    done, skipped = [], []
    for i, line in enumerate(lines):
        m = re.match(r"\|\s*([1-5]-\d+)\s*\|", line)
        if not m:
            continue
        sid = m.group(1)
        spec = PATCH.get(sid)
        if spec is None:
            # dang khoa gia: "1-12b" -> id thuoc "1-12"
            for key, val in PATCH.items():
                if val.get("id") == sid:
                    spec = val
                    break
        if spec is None:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 9:
            print("!! bo qua (thieu cot):", sid)
            continue
        before = list(cells)
        for key, val in spec.items():
            if key == "id":
                continue
            cells[IDX[key]] = val
        if cells == before:
            skipped.append(sid)
            continue
        lines[i] = "| " + " | ".join(cells) + " |"
        done.append(sid)

    PLAN.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("da sua %d dong:" % len(done), done)
    if skipped:
        print("KHONG doi (gia tri da dung):", skipped)
    missing = [k for k in PATCH if k not in done and k not in skipped and not PATCH[k].get("id")]
    if missing:
        print("!! KHONG tim thay dong:", missing)



if __name__ == "__main__":
    main()
