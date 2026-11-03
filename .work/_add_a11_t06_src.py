import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
P = pathlib.Path(r"D:/TEST/Gax/amber-eyes/00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md")
t = P.read_text(encoding="utf-8-sig")

NEW = [
    "| 93 | **Sửa 1 câu kịch bản của tập đã dựng bằng Higgs = cần chạy lại Kaggle GPU** (Tập 06, 03/11/2026): đổi bất kỳ câu nào ⇒ phải tạo lại file TTS của câu đó ⇒ **engine Higgs Audio v3 của dự án chỉ chạy trên Kaggle GPU** (`QUY_TAC_AUDIO_HIGGS.md` §PHẠM VI: chạy chỗ khác = **engine mới**, phải đo lại CER/G8/G9 từ đầu). Máy dựng (Windows, không GPU) đo ngày 03/11/2026: không `nvidia-smi`, không `kaggle` CLI, không `~/.kaggle/kaggle.json`, không module `kaggle`/`torch`/`mlx_audio` ⇒ **không tạo lại được TTS** ⇒ không dựng lại được tập | **Kiểm tra engine TTS CÓ chạy được ở máy hiện tại TRƯỚC khi hứa dựng lại** — đừng sửa kịch bản rồi mới phát hiện không có GPU. Nếu thiếu: (1) **đóng gói sẵn gói sửa** (câu hiện tại trích tự động từ `script_tapXX.json` + câu đề xuất + nguồn + tên file WAV cần tạo lại + quy trình 6 bước) rồi **dừng**; (2) ghi blocker vào hồ sơ + báo cáo QC + A11; (3) để người dùng quyết có chạy 1 lượt Kaggle hay không. **Chỉ sửa chữ trên hình thì không cần TTS**, nhưng vẫn phải khớp timeline âm thanh ⇒ làm cùng đợt |",
    "| 94 | **Chữ trên hình là một nguồn khẳng định — cổng \"số trên hình có trong câu\" KHÔNG bắt được loại lỗi này** (Tập 06, 03/11/2026): audit 73/73 caption cho ra 4 lỗi mà mọi cổng QC vẫn xanh: `2-15` \"RÚT TIỀN MẶT CHUẨN BỊ BỎ TRỐN\" (không nguồn nào xác nhận) · `3-03` \"NẮP HẦM KỸ THUẬT **PHÒNG NGỦ**\" (nguồn: trap door trong **tủ quần áo**) · `5-07` \"BÀI HỌC KINH ĐIỂN TẠI **HỌC VIỆN FBI**\" (không nguồn nào nhắc FBI Academy) · `1-05` \"gần **một thập kỷ**\" (nguồn: các vụ giết 1972–1978 = 6 năm). Vì đây là *hành vi* khẳng định chứ không phải *số* ⇒ cổng số không bắt được | Thêm cổng QC mới: **caption có mệnh đề khẳng định hành vi/sự kiện cụ thể thì phải có nguồn**, không chỉ số. Cách làm: audit caption của **từng shot** đối chiếu câu kịch bản (`.work/_audit_caption_tXX.py`) rồi grep nguồn theo từ khoá của từng caption đáng nghi. Khi sửa caption mà **không** sửa câu ⇒ chỉ cần render lại ảnh tĩnh của các shot đó, **không** cần TTS |",
]

lines = t.splitlines()
last = max(i for i, L in enumerate(lines) if L.startswith("| 92 | "))
lines[last + 1:last + 1] = NEW
out = "\n".join(lines) + "\n"
if "\x00" in out:
    raise SystemExit("CHẶN — byte NUL")
P.write_text(out, encoding="utf-8")
print(f"OK  them #93, #94 sau dong #92 (dong {last + 1})")
