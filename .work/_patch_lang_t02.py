# -*- coding: utf-8 -*-
"""Patch chinh ta + ngon nguu cho bo text TikTok Tap 02 — sua o GENERATOR (G6).
Che do: --dry (chi bao cao) hoac --apply (ghi file, co backup).
Chi sua phan TEXT BAN GIAO (15 file .txt). KHONG sua loi doc (voice) va KHONG sua
chuoi QC noi bo, de tranh lech voiceover va lam hong co so kiem tra.
"""
import io, os, sys, shutil, datetime

GEN = r"D:/TEST/Gax/amber-eyes/.work/_build_tk_tap02.py"
BAK = r"D:/TEST/Gax/amber-eyes/.work/_cu"
DRY = "--dry" not in sys.argv

# (old, new, expected_count)
REPL = [
    # --- 1. "dữ kiện" -> "dữ liệu" (chuẩn dự án: Tap01 caption + MoTa_Dai + slogan LƯU Ý) ---
    ('"Hồ sơ có thật, dữ kiện có nguồn.",', '"Hồ sơ có thật, dữ liệu có nguồn.",', 1),          # caption
    ('\nHồ sơ có thật, dữ kiện có nguồn.\n', '\nHồ sơ có thật, dữ liệu có nguồn.\n', 4),       # mo ta dai TK2-TK5
    ('🔎 Hồ sơ có thật, dữ kiện có nguồn.', '🔎 Hồ sơ có thật, dữ liệu có nguồn.', 7),             # 5 ngan + comment + QC

    # --- 2. "chỉ dấu" -> "Chỉ dấu" trong MO_TA_DAI (khớp Tap01/MoTa_Dai_TK1) ---
    ('\nTập 02 · Đại tá hai mặt — chỉ dấu #', '\nTập 02 · Đại tá hai mặt — Chỉ dấu #', 5),

    # --- 3. "toà" -> "tòa" (dau sac; dang lan 2 kieu trong cung file) ---
    ('trước toà', 'trước tòa', 4),
    ('hồ sơ toà án', 'hồ sơ tòa án', 5),

    # --- 4. Dau nhay cong -> thang (chuẩn Tap01 dung nhay thang) ---
    ('trạng thái “đói ảo tưởng”,', 'trạng thái "đói ảo tưởng",', 1),
    ('về dọc “Con lộ Anh hùng”.', 'về dọc "Con lộ Anh hùng".', 2),
    ('làm “lá chắn bình thường hóa”.', 'làm "lá chắn bình thường hóa".', 1),
    ('hắn tự nhủ: “mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm”.',
     'hắn tự nhủ: "mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm".', 1),
    ('trống rỗng đến lạnh người: “Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng.”',
     'trống rỗng đến lạnh người: "Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng."', 1),
    ('• Phim tài liệu CBC “The Detective and the Colonel”', '• Phim tài liệu CBC "The Detective and the Colonel"', 1),
    ('• Christie Blatchford, “Unmasking Freedom”', '• Christie Blatchford, "Unmasking Freedom"', 1),

    # --- 5. Caption: them (25 phút) + YouTube (khớp Tap01 + bản dài) ---
    ('f"📺 Xem tập đầy đủ ở link trong bio"', 'f"📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio"', 1),

    # --- 6. TK1 ngắn: ghi "bốn nấc thang" nhung chi liet ke 3 -> bo sung NẤC 4 ---
    ('• NẤC 3 — xâm nhập khi có người ở nhà, tháng 9/2009.\n',
     '• NẤC 3 — xâm nhập khi có người ở nhà, tháng 9/2009.\n'
     '• NẤC 4 — đoạt mạng nạn nhân: cuối tháng 11/2009, nữ hạ sĩ Marie-France Comeau, 37 tuổi. '
     'Chỉ hai tháng sau đó là Jessica Lloyd.\n', 1),

    # --- 7. TK1 ngắn: bo sung "phụ nữ" (nguyên van kich ban:91) + "bất thành" ---
    ('đứng ngoài bóng tối để nhìn qua khung cửa sổ.', 'đứng ngoài bóng tối để rình rập phụ nữ qua khung cửa sổ.', 1),
    ('tổng cộng 82 vụ đột nhập.', 'tổng cộng 82 vụ đột nhập và đột nhập bất thành.', 1),

    # --- 8. TK2: "thay vì chiếc BMW mà..." (nguyên van kich ban:54) + dau phay ---
    ('thay vì chiếc BMW ông ta vẫn thường đi.', 'thay vì chiếc BMW mà ông ta vẫn thường đi.', 2),
    ('nữ nhân viên 27 tuổi sống một mình ở Belleville', 'nữ nhân viên 27 tuổi, sống một mình ở Belleville', 1),

    # --- 9. TK4: ten toa thong nhat + "cung cuc" + "toan quyen" ---
    ('Tháng 10/2010, Tòa án Cấp cao Ontario xét xử tại thị trấn Belleville',
     'Tháng 10/2010, Tòa Thượng thẩm Ontario xét xử tại thị trấn Belleville', 2),
    ('nỗi đau đớn của những người phụ nữ hay gia đình nạn nhân',
     'nỗi đau đớn cùng cực của những người phụ nữ hay gia đình nạn nhân', 1),
    ('• Bản án lớn nhất là sự sụp đổ hoàn toàn về danh dự và quyền lực: quân hàm bị thu hồi, huân chương bị cắt',
     '• Bản án lớn nhất là sự sụp đổ hoàn toàn về danh dự và quyền lực: quân hàm bị toàn quyền Canada thu hồi, huân chương bị cắt', 1),
    ('kẻ săn mồi chỉ còn lại sự tự thương hại bản thân thảm hại.',
     'kẻ săn mồi chỉ còn lại sự thương hại bản thân tột độ.', 1),
    ('Robert F. Scott, Tòa Thượng thẩm Belleville', 'Robert F. Scott, Tòa Thượng thẩm Ontario (phiên xử tại Belleville)', 1),

    # --- 10. TK3: lam ro cau hoi (nguon: tham van) ---
    ('Khi thám tử hỏi hắn đã từng nghĩ vì sao mình làm những việc đó chưa',
     'Khi thám tử hỏi hắn có bao giờ tự hỏi vì sao mình làm những việc đó', 1),

    # --- 11. TK5: "Nguyên ly" -> "Sach" + bo khoang trong ngoac ---
    ('• Nguyên lý “The Gift of Fear” ( Gavin de Becker) — nguồn khung lý thuyết được trích trong kịch bản tập',
     '• Sách "The Gift of Fear" (Gavin de Becker) — nguồn cho khung lý thuyết trong kịch bản tập', 1),
]

src = io.open(GEN, encoding="utf-8").read()
out = src
bad = []
for old, new, cnt in REPL:
    got = out.count(old)
    if got != cnt:
        bad.append((old[:70], got, cnt))
    else:
        out = out.replace(old, new)

if bad:
    print("KHONG PATCH (so lan khong khop):")
    for o, g, c in bad:
        print("  [%d/%d] %s" % (g, c, o))
    sys.exit(1)

print("OK - tat ca %d cua hang khop so lan." % len(REPL))
if DRY:
    print("DRY RUN - chua ghi file.")
    sys.exit(0)

os.makedirs(BAK, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
bk = os.path.join(BAK, "_build_tk_tap02_%s.py" % stamp)
shutil.copy2(GEN, bk)
print("Backup:", bk)

with io.open(GEN, "w", encoding="utf-8", newline="\n") as f:
    f.write(out)
print("Da ghi:", GEN, len(out), "bytes")
