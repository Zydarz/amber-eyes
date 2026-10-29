# BRIEF DỊCH TIẾNG HÀN — DÙNG CHUNG CHO WORKER (Amber Eyes)

Bạn đang dịch MỘT kịch bản tiếng Việt của dự án Amber Eyes (`D:\TEST\Gax\Audi`) sang **bản tiếng Hàn**.
Đây là **bản ngôn ngữ (language edition)**, KHÔNG phải bản dịch tự do: cùng số màn, cùng thứ tự yếu tố,
cùng vai, cùng **số câu** trong mỗi lượt thoại, cùng cấu trúc bullet/danh sách, cùng vị trí cue.

## BƯỚC 1 — Sinh blueprint và CHỈ đọc blueprint

```powershell
Set-Location 'D:\TEST\Gax\Audi'
$env:PYTHONIOENCODING='utf-8'
py -3 .work/ko_blueprint.py 01_KICH_BAN/TapXX/kichban_tapXX_23102026.md .work/_bp_tXX.txt
```

Đọc TOÀN BỘ `.work/_bp_tXX.txt`. Nó cho biết: id từng yếu tố, vai, **số câu chính xác**, số block,
từng câu nguồn được đánh số, các số phải giữ, các tên riêng Latin phải giữ, danh sách trích dẫn, tổng.

⛔ **KHÔNG mở file tiếng Việt gốc, KHÔNG mở bản tiếng Anh** — chúng 30–40 KB và sẽ làm bạn timeout 300 s.
Blueprint là bản đồ đầy đủ. Nếu cần thêm ngữ cảnh cho 1 câu cụ thể, hãy đọc file VN với `offset`/`limit`
quanh đúng dòng đó.

## BƯỚC 2 — Đọc chuẩn

- `00_TIEU_CHUAN/CHU_CO_DINH_KO.md` — các mục B, C, C1b, C1c, D, D3, D4, E, F, G.
- 30 dòng đầu `01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md` — mẫu tham chiếu về định dạng.

## BƯỚC 3 — Ghi file (MỘT lần gọi Write)

Đường dẫn đích: `01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md`

### 13 quy tắc bắt buộc (vi phạm bất kỳ quy tắc nào ⇒ QC FAIL)

1. **Đúng số yếu tố** như blueprint, đúng thứ tự.
2. **Đúng số câu** trong từng yếu tố. Đếm cẩn thận.
3. **Giữ số dòng vật lý** của nguồn: parser tách câu **theo từng dòng**, nên 1 dòng nguồn = 1 đoạn.
   Mỗi dòng Hàn phải là một nhóm câu hoàn chỉnh; đừng gộp 2 câu nguồn vào 1 dòng Hàn theo cách
   làm thay đổi điểm tách.
4. **Giữ nguyên vị trí mọi cue**: `**[SFX]:**` và `**[BGM]:**` **giữ bằng tiếng Anh** (video renderer
   khớp đúng các nhãn này). Cue mở đầu màn `## 막 N` giữ nguyên chỗ.
5. `blocks=N`: khi blueprint ghi một yếu tố có N block, viết N block có nhãn vai **liền nhau**
   (không có cue ở giữa) — parser tự gộp các block cùng vai liền kề thành 1 yếu tố.
6. **Không câu nào được bắt đầu bằng chữ số** (trừ câu đầu tiên của dòng). Số ở đầu câu chặn điểm tách
   ⇒ mất câu. Hãy diễn đạt lại.
7. **Giữ mọi dấu `:`** — dấu hai chấm nối hai mệnh đề trong **một** câu, không bao giờ đổi thành dấu chấm.
   Dấu `…`/`...` giữa câu thành ` – ` (chữ Hàn ngay sau dấu ba chấm sẽ tách sai).
8. **Mọi số viết bằng chữ số Ả Rập.** Mọi giá trị số có trong tiếng Việt phải còn trong bản Hàn.
9. **Tên riêng Latin giữ nguyên chữ Latin**, y hệt tiếng Việt. Nếu một từ tiếng Anh đứng trước sẽ bị
   gộp vào tên (vd "First Lady Rosalynn Carter" ⇒ tên bị hiểu là "Rosalynn Carter"), hãy thêm dấu phẩy
   trước tên hoặc bỏ từ tiếng Anh dẫn nhập.
10. **Chỉ Hangul + Latin + chữ số.** KHÔNG Hán tự, KHÔNG ký tự Cyrillic, KHÔNG dấu tiếng Việt sót lại,
    KHÔNG ký tự rác, KHÔNG dán Latin sát Hangul.
11. **Số trích dẫn phải đúng bằng** danh sách trong blueprint. Trích dẫn loại 1 (nguồn giữ tiếng Anh
    trong `‘…’`) phải giữ tiếng Anh trong `‘…’` và đặt bản dịch Hàn **trước** trích dẫn, nối bằng ` – `.
    Trích dẫn loại 2 (nhãn do kịch bản tự đặt) **dịch bên trong** `‘…’`. Dùng đúng dấu cong `‘ ’`.
12. Cùng số bullet/danh sách và cùng kiểu như blueprint (gạch đầu dòng `-`, danh sách đánh số).
13. Nhãn vai bằng tiếng Hàn: H → `**호스트**`, D → `**수사관**`, C → `**심리학자**`, N → `**일반인**`.
    Đầu màn → `## 막 N: …`. Cue dừng → `**[정지 X초]**`.

### Giọng văn

- Lời dẫn `호스트` / `수사관` / `심리학자` dùng văn **trang trọng `-습니다`**.
- `일반인` (nhân chứng / người thường) giữ **giọng cá nhân, ngôi thứ nhất** — như người đang kể,
  không phải người dẫn chương trình.
- Nhãn kỹ thuật/tâm lý giữ tiếng Hàn nhưng giữ thuật ngữ Latin khi nguồn giữ (vd `Mythomania`).
- Giữ **mức độ bạo lực đã được dịu** của nguồn. Không thêm chi tiết máu me, không bịa thêm.

## BƯỚC 4 — Kiểm tra trước khi báo cáo

```powershell
$env:PYTHONIOENCODING='utf-8'
py -3 .work/_qc_ko_parity.py 01_KICH_BAN/TapXX/kichban_tapXX_23102026.md 01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md
py -3 .work/_lint_ko.py      01_KICH_BAN/TapXX/kichban_tapXX_23102026.md 01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md
```

`_qc_ko_parity.py` phải in ra **`PASS`**. Lint không được có Hán tự / ký tự rác / Latin lạ (bỏ qua
tiếng Anh trong trích dẫn loại 1 và tên riêng hợp lệ).

## RANH GIỚI (cứng)

- Chỉ được tạo/sửa: `01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md` và `.work/_bp_tXX.txt`.
- **KHÔNG** sửa file tiếng Việt nguồn, tập khác, `00_TIEU_CHUAN/`, hay các script dùng chung trong
  `.work/` (`parse_kichban.py`, `edition.py`, `tts_sentences.py`, `_qc_ko_parity.py`, `_lint_ko.py`,
  `ko_blueprint.py`). Một phiên song song đang sửa các file dùng chung đó.
- Không chạy script LLM/API nào. Không dùng `llm-call`.

## BÁO CÁO

Trả về: dòng `PASS` chính xác, tổng số yếu tố / số câu, và 3–5 quyết định dịch đáng chú ý
(xử lý trích dẫn, tách dòng, tên riêng, chỗ phải diễn đạt lại vì luật số / dấu hai chấm).
