"""Ghi trạng thái bản EN Tập 02 vào memory (agent memory) — bài học dùng lại được."""
import subprocess
import sys
from pathlib import Path

MEM = Path(r"C:\Users\ADMIN\.minimax\agents\mavis\memory\MEMORY.md")
text = """
### AMBER EYES — đổi giọng TTS: CẢM XÚC làm đổi danh tính người, TỐC ĐỘ thì không (24/10/2026)
Type: technique

**Bài học (đo bằng model nghe, không phải suy đoán):** với giọng `English_Deep-VoicedGentleman`,
G10 báo "Investigator → 3 người" cho bản EN Tập 02. Thí nghiệm `.work/_voice_band_test.py`
(đọc CÙNG một câu ở nhiều tốc độ → ghép → hỏi `audios_understand` "SPEAKERS: n") cho kết quả:
- **TỐC ĐỘ đọc 0,91 → 0,99: SPEAKERS = 1.** Tốc độ KHÔNG làm đổi danh tính người.
- **CẢM XÚC neutral/sad/fearful/surprising ở cùng tốc độ: SPEAKERS = 3.** `sad` nghe "khàn thì thầm",
  `fearful` nghe "trầm rất sâu" ⇒ bị đếm thành người khác.
⇒ Khi G10 fail, **đổi giọng trước, đừng siết tốc độ**. `English_Trustworth_Man` giữ được
SPEAKERS = 1 ở cả 4 cảm xúc (đã dùng cho vai D của bản EN Tập 02).
`Korean_ColdYoungMan` (bộ VN) cũng ổn với cảm xúc — lý do bản VN Tập 02 pass G10 dù có sad/fearful.

**Công cụ đo (dùng lại được):** `.work/_voice_band_test.py <voice_id>` — 4 ca: wide (0,91–0,99),
mid, tight, emo; in ra SPEAKERS cho từng ca.

**Bẫy khi đổi giọng giữa chừng:** xoá mp3 cũ rồi đọc lại ⇒ nếu hết số dư gói (API trả **402
"plan balance has run out"**, không phải lỗi tạm thời — **đừng retry**) thì mất file.
⇒ **Luôn lưu `node_id` của từng file TTS** (script `tts_sentences.py` đã ghi vào
`.work/tts_s_EN_t02/res_*.json`). Khôi phục được bằng `.work/_restore_from_nodes.py <sid> ...`
(đọc node_id → `mcode-tools get_asset_url` → tải lại mp3). Cả `batch_text_to_audio` lẫn
`synthesize_speech` đều dùng chung hạn mức nên không có đường vòng.
"""
with MEM.open("a", encoding="utf-8") as f:
    f.write(text)
print("đã ghi vào", MEM)
