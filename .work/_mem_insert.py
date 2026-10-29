import io, sys
p = r"C:\Users\ADMIN\.minimax\agents\mavis\memory\MEMORY.md"
s = io.open(p, encoding="utf-8").read()
anchor = "**Apply when:** đo CER/độ đúng chữ cho TTS đa ngôn ngữ;"
add = """**BẪY 4 — bộ lọc nội dung Gemini chặn câu TTS (code vẫn = 0):**
- Câu như *"Xâm nhập khi có người ở nhà"* bị `listen_audio` trả về `{"code":0,"message":"ok","transcription":"This request was blocked by Gemini's filters..."}` ⇒ **mã lỗi KHÔNG phản ánh thất bại**. Phải kiểm nội dung `transcription`, cắt đuôi lỗi, và **loại câu đó khỏi mẫu** (2/20 câu bị chặn là hỏng mẫu, không phải lỗi giọng).

**BẪY 5 — `batch_text_to_audio` chỉ nhận TỐI ĐA 10 request/lượt gọi:**
- Schema `requests` có `"maxItems": 10`. Gửi 51 request ⇒ lỗi `connector_tool_error: Connector tool execution failed (latency_ms=0)` — **không có thông báo rõ là do quá giới hạn**. Phải chia chunk 10.
- Lỗi này làm 4 ứng viên TTS "hỏng" trong 1 lượt chạy; phải đọc `success_items[]` từng batch thay vì tin exit code.

"""
if "BẪY 4 — bộ lọc nội dung Gemini" not in s:
    s = s.replace(anchor, add + anchor, 1)
    io.open(p, "w", encoding="utf-8", newline="").write(s)
    print("inserted")
else:
    print("already present")
