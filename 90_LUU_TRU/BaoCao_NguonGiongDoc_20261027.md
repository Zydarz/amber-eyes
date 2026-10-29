# BÁO CÁO — NGUỒN THÔNG TIN GIỌNG ĐỌC

**Ngày:** 27/10/2026 · **Người lập:** Mavis · **Phạm vi:** đọc tài liệu + mã nguồn dự án `D:\TEST\Gax\Audi` (kênh Amber Eyes)

---

## 1. KẾT LUẬN (trả lời câu hỏi)

> *"Thông tin giọng đọc ở đây là lấy từ đâu, có phải từ `MINIMAX_API_KEY` không?"*

# ❌ KHÔNG PHẢI.

Dự án **không dùng `MINIMAX_API_KEY` ở bất kỳ đâu**. Giọng đọc được đọc ra bằng **MiniMax Connector (App)** thông qua CLI `mcode-tools`, với credential do **runtime MiniMax Code** quản lý (OAuth token) — không phải biến môi trường, không phải file trong dự án.

**Ba kiểm đã chạy (đều trả về 0 kết quả):**

| Kiểm | Lệnh | Kết quả |
|---|---|---|
| Quét toàn dự án | `MINIMAX_API_KEY\|MINIMAX_GROUP_ID\|minimax_api_key` trong `*.py, *.md, *.json, *.yaml, *.yml, *.txt, *.ps1, *.cmd, *.bat, *.sh, *.toml, *.ini, *.cfg, *.env` | **0 hit** |
| Biến môi trường | `Get-ChildItem Env:` lọc `MINIMAX\|GEMINI\|FREESOUND\|API_KEY\|GROUP` | **rỗng** |
| File key trong dự án | `Get-ChildItem -Recurse -Include '.env*','*.key','*api_key*'` | **không có** |

Ngoài ra: quét `api.minimax|group_id|GROUP_ID|api.minimax.chat` trong `.work/*.py` + toàn bộ `.md` → **0 hit**. Không có đoạn nào gọi API MiniMax thẳng qua `urllib`/`requests`.

---

## 2. Ba tầng "thông tin giọng đọc" — dễ nhầm lẫn nhất

Từ "thông tin giọng đọc" có 3 tầng khác nhau, mỗi tầng một nguồn:

| Tầng | Nội dung | Nguồn thật | Bằng chứng |
|---|---|---|---|
| **(1) Xác thực** | Token để gọi được dịch vụ TTS | OAuth của `mcode-tools` trong runtime MiniMax Code | `C:\Users\ADMIN\.minimax\integrations\mcode-tools\credentials.json` (`access_token`, `refresh_token`, `client_id`, `electron_session_id`) · `C:\Users\ADMIN\.minimax\auth\prod\en\mcode-public\auth.json` |
| **(2) Danh mục giọng** | 332 `voice_id` của MiniMax | MiniMax TTS qua connector `connector__matrix__get_voice_list` | Gọi thử 27/10/2026: `code=0`, `message=ok`, `total=332` → lưu tại `.work/_voice_list_live_20261027.json` |
| **(3) Bộ giọng kênh dùng** | 5 giọng bộ A + các bộ theo ngôn ngữ/tập | **Hardcode trong mã** — `.work/edition.py` dòng 1078–1093 (`CAST`) | `edition.py:1072-1093` |

> **Điểm mấu chốt:** `get_voice_list` **tồn tại và chạy tốt**, nhưng **code dự án không hề gọi nó** — 0 lần trong toàn bộ `.work/*.py`. Giọng được chọn tay trong `02_SAN_XUAT/Tap02/BaoCao_GiongDoc_Tap02.md` §4 (23/10/2026), rồi chép vào `edition.py` và giữ nguyên từ đó.

---

## 3. Luồng gọi thật trong mã (mã → connector → MiniMax)

```
.work/tts_sentences.py
  └─ mcode(["connector","call","connector__matrix__batch_text_to_audio",
            "--args-file", str(af)])                          ← dòng 210
       └─ requests[].{text, voice_id, emotion, speed, pitch, volume, output_file}
                                                              ← dòng 204-206
            └─ res.success_items[].node_id
                 └─ mcode(["get_asset_url", node_id])["download_url"]   ← dòng 224
                      └─ urllib.request.urlretrieve(...) → .work/audio_s/<id>.mp3  ← dòng 225
```

Các chỗ gọi connector khác trong dự án:

| Script | Connector tool | Dùng để |
|---|---|---|
| `.work/tts_sentences.py:210` | `connector__matrix__batch_text_to_audio` | đọc giọng từng câu (bước 4) |
| `.work/voice_audition.py:100` | `connector__matrix__batch_text_to_audio` | thử giọng (bước 0) |
| `.work/voice_audition.py:127` | `connector__matrix__listen_audio` | nghe lại bản thử |
| `.work/voice_role_check.py:62` | `connector__matrix__audios_understand` | G10 — nghe mù theo vai |
| `.work/tts_sentences.py:224` | `get_asset_url` (top-level) | tải mp3 về đĩa |

---

## 4. Vì sao dễ hiểu nhầm là "lấy từ MINIMAX_API_KEY"

`C:\Users\ADMIN\.minimax\config.yaml` **có** key MiniMax:

```yaml
provider:
  minimax:
    options:
      apiKey: sk-xxx…          ← key cho LLM
      baseURL: https://agent.minimax.io/mavis/api/v1/llm/v1
```

Nhưng đó là key cho **LLM** (chat / `llm-call`), **không** phải key TTS. Dự án **không đọc file này** — `config.yaml` nằm ngoài `D:\TEST\Gax\Audi` và không được tham chiếu ở đâu.

---

## 5. Bảng giọng thật — đọc từ CODE, không đọc từ tài liệu

### 5.1 Bộ A — mặc định bản tiếng Việt (`edition.py:1090-1093`)
| Vai | `voice_id` | Tốc độ gốc |
|---|---|---|
| Host (H) | `English_CaptivatingStoryteller` | 0,90 |
| Điều tra viên (D) | `Korean_ColdYoungMan` | 0,95 |
| Chuyên gia (C) | `English_AssertiveQueen` | 0,92 |
| N1 | `Vietnamese_kindhearted_girl` | 0,95 |
| N2 | `English_captivating_female1` | 0,95 |

### 5.2 Bộ EN (`edition.py:1078-1080`)
`H=English_magnetic_voiced_man` 0,95 · `D=English_Trustworth_Man` 0,97 · `C=English_Wiselady` 0,95 · `N1=English_SentimentalLady` 0,95 · `N2=English_captivating_female1` 0,95

### 5.3 Bộ JA (`edition.py:1081-1084`)
`Japanese_GentleButler` 0,95 · `Japanese_SeriousCommander` 0,97 · `Japanese_DependableWoman` 0,95 · `Japanese_KindLady` 0,95 · `Japanese_DecisivePrincess` 0,95

### 5.4 Bộ KO (`edition.py:1085-1089`)
`Korean_CalmGentleman` 0,95 · `Korean_ColdYoungMan` 0,95 · `Korean_DecisiveQueen` 0,92 · `Korean_GentleWoman` 0,95 · `Korean_SweetGirl` 0,95

### 5.5 Tập 01 — ghim bộ riêng (`edition.py:100`, `cast` của EPISODES Tập 01)
`H=audiobook_male_1` 0,90 · `D=male-qn-qingse` 0,95 · `C=audiobook_female_1` 0,92
*(README dòng 29 ghi: "giọng bộ cũ")*

---

## 6. Đối chiếu tài liệu ↔ code — 3 chỗ lệch

| # | Nơi | Tài liệu nói | Code thực tế | Mức độ |
|---|---|---|---|---|
| **L1** | `AGENTS.md` §4, dòng 82–88 | Bảng bộ A, cột "Tốc độ gốc" để **trống** cho N1/N2 | `edition.py:1092-1093` ghi N1=0,95 · N2=0,95 | Nhỏ — thiếu số |
| **L2** | `AGENTS.md` §4, dòng 107 | *"Lấy ứng viên từ `get_voice_list`"* | Code **không** gọi `get_voice_list`; ứng viên hardcode tại `voice_audition.py:26` (`CANDS`) | Trung bình — hướng dẫn mô tả sai thực tế |
| **L3** | `AGENTS.md` §4 + `README.md:15` | Chỉ nói **bộ A** là "giọng đọc chuẩn của kênh" | Bản **EN** dùng bộ riêng (5 giọng khác hoàn toàn); **Tập 01** ghim bộ riêng (3 giọng cũ) | **Cao** — người đọc tài liệu sẽ hiểu sai bản EN và Tập 01 |
| L4 ✓ | `TIEU_CHUAN_DUNG_VIDEO.md:184` | "Kho giọng chỉ có một giọng tiếng Việt gốc" | Đúng — kiểm live: đúng **1** giọng `Vietnamese_*` / 332 | Khớp |

---

## 7. ⚠️ Rủi ro phát hiện: 3 `voice_id` của Tập 01 không có trong danh mục live

Đối chiếu **23** `voice_id` mà dự án hardcode với **332** giọng live:

- **20/23 khớp** — toàn bộ bộ A, EN, JA, KO.
- **3 vắng mặt:** `audiobook_male_1`, `male-qn-qingse`, `audiobook_female_1`.
  Không phải đổi tên: quét `qingse` / `audiobook` / `male-qn` trong danh mục → **0 kết quả**.

**Chưa kết luận là chết**, vì 2 lý do:
1. Schema của `batch_text_to_audio` ghi rõ `voice_id` mặc định là **`male-qn-qingse`** → API vẫn công nhận nó làm giọng mặc định.
2. MiniMax có 2 lớp giọng: *voice library* (trả về qua `get_voice_list`) và **system voice cũ** (`audiobook_*`, `male-qn-qingse`) không được liệt kê trong catalog nhưng vẫn dùng được bằng API.

⇒ Cần **1 lần gọi TTS thật** mới chốt. Tốn credit → theo `AGENTS.md` L4 phải hỏi trước.

**Rủi ro nếu các giọng này đã chết:** chạy lại TTS cho **Tập 01** sẽ fail **toàn bộ 128 câu** (file `.work/audio_s/` của Tập 01 đã xuất nên chưa lộ). Đây là bộ giọng mà Tập 01 và bản review cũ đang dùng.

---

## 8. Hai việc còn mở phát hiện được (ngoài câu hỏi, nhưng liên quan trực tiếp)

### 8.1 Điều khoản thương mại MiniMax cho **giọng** chưa được kiểm
`provenance.json` có **2.103 bản ghi**. Hai bản ghi "audio tổng" ghi:

```
file:  02_SAN_XUAT/Tap01/xuat_ban/Tap01_master.mp3
cong_cu: TTS MiniMax (5 giọng, 128 câu) + nhạc assets/bgm + 11 SFX …
dieu_khoan: <điều khoản MiniMax — cần kiểm tra>
kiem_tra_thuong_mai: chưa
```

`AGENTS.md` mục 9 yêu cầu kiểm điều khoản thương mại MiniMax (giọng, ảnh, nhạc) **trước khi bật kiếm tiền**. Trạng thái vẫn là "chưa".

### 8.2 Freesound API key đang hardcode trong mã nguồn
`.work/freesound.py:49` chứa **key Freesound dạng chữ thường** ngay trong mã. Nếu thư mục này từng được chia sẻ hoặc gửi đi, key đó đã lộ. Cơ chế an toàn đã có sẵn ở `freesound_client.py:66` (`FREESOUND_API_KEY` → `.work/.freesound_key`) — chỉ cần dùng thay vì giá trị ghi cứng.

---

## 9. Việc người dùng phải làm

| # | Việc | Mức độ |
|---|---|---|
| 1 | **Duyệt 1 lần gọi TTS thử** cho 3 `voice_id` Tập 01 (`audiobook_male_1` / `male-qn-qingse` / `audiobook_female_1`) — vài giây, chi phí cực nhỏ. Chưa tự chạy vì `AGENTS.md` L4 chặn việc tiêu credit | Cần duyệt |
| 2 | **Cập nhật `AGENTS.md` §4 + `README.md`**: ghi rõ 3 bộ giọng (A / EN / Tập 01), điền tốc độ N1-N2, sửa câu "Lấy ứng viên từ `get_voice_list`" | Nên làm |
| 3 | **Chốt điều khoản thương mại MiniMax cho giọng** (provenance vẫn ghi "chưa") — trước khi bật kiếm tiền | Bắt buộc trước khi đăng |
| 4 | **Chuyển Freesound key** ra khỏi mã nguồn (dùng `freesound_client.py`) | Nên làm |

---

## 10. Phụ lục — lệnh tái lập

```powershell
# 1. Danh mục giọng live từ connector
mcode-tools connector call connector__matrix__get_voice_list --args '{}' `
  | Out-File .work/_voice_list_live_20261027.json -Encoding utf8

# 2. Đối chiếu 23 voice_id của dự án với danh mục live
py -3 .work/_audit_voice_nguon.py

# 3. Schema TTS (emotion/speed/pitch/voice_id + default)
mcode-tools connector tool connector__matrix__batch_text_to_audio

# 4. Quét tìm MINIMAX_API_KEY trong dự án (kết quả: 0)
Select-String -Path 'D:\TEST\Gax\Audi\**\*.py','D:\TEST\Gax\Audi\**\*.md' `
  -Pattern 'MINIMAX_API_KEY' -ErrorAction SilentlyContinue
```

**File sinh ra lượt này:**
- `.work/_voice_list_live_20261027.json` — ảnh chụp 332 giọng live từ connector
- `.work/_audit_voice_nguon.py` — script đối chiếu 23 `voice_id` hardcode với danh mục live

---

*Báo cáo này chỉ đọc tài liệu + mã nguồn + 1 lần gọi connector không tốn credit (`get_voice_list` — chỉ liệt kê danh mục, không sinh audio). Chưa chạy TTS thật, chưa sửa file nào trong dự án.*
