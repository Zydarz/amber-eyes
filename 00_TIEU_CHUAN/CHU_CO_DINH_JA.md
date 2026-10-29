# CHỮ CỐ ĐỊNH — BẢN TIẾNG NHẬT (JAPANESE EDITION)

*Tài liệu này là chuẩn bắt buộc cho **bản tiếng Nhật** của kịch bản Amber Eyes.*
*Áp dụng cho **Tập 01 – Tập 29**. Ngày lập: 24/10/2026.*

> Bản tiếng Nhật **không phải** bản dịch thô bằng máy. Nó là **phiên bản ngôn ngữ** chính thức của kịch bản: cùng cấu trúc, cùng mã câu, cùng vai, cùng số câu — chỉ đổi ngôn ngữ sang tiếng Nhật chuẩn phát thanh tài liệu (ドキュメンタリー／朗読調). Mọi thứ được **đọc thành tiếng**, nên văn phong phải **tự nhiên khi nghe bằng tai**, không lẫn từ vựng tiếng Trung, không có chữ Hán giản thể (chữ Trung Quốc), và không sót ký tự lỗi.

---

## A. ĐƯỜNG DẪN & TÊN FILE

| Việc | Quy ước |
|---|---|
| Thư mục | `01_KICH_BAN/TapXX_JA/` (đặt cạnh `TapXX/`, `TapXX_EN/`, `TapXX_KO/`) |
| File kịch bản | `01_KICH_BAN/TapXX_JA/kichban_tapXX_JA.md` |
| File cache câu | `.work/ja_cache/tapXX.json` |
| Nguồn (file tiếng Việt) | `01_KICH_BAN/TapXX/kichban_tapXX_<ngày>.md` — **không sửa file nguồn** |
| Script kiểm tra tự động | `.work/_qc_ja.py` (kiểm tra 29 tập: số câu, số lượt, từ cấm, thuật ngữ, chữ Hán) |

---

## B. ÁNH XẠ CẤU TRÚC (BẮT BUỘC — KHÔNG ĐỔI)

| Thành phần | Tiếng Việt (nguồn) | **Tiếng Nhật (bản JA)** | Ghi chú |
|---|---|---|---|
| Tiêu đề hồi | `## HỒI 1: ...` | `## 第1幕：...` | Giữ nguyên số thứ tự 1–5. |
| Vai | `**HOST**` | `**ホスト**` | → H |
| Vai | `**ĐIỀU TRA VIÊN**` | `**捜査官**` | → D |
| Vai | `**CHUYÊN GIA TÂM LÝ**` | `**心理学者**` | → C |
| Vai | `**NGƯỜI BÌNH THƯỜNG**` | `**一般人**` | → N |
| Vai | `**ĐẶC VỤ FBI**` | `**FBI特別捜査官**` | → D (chỉ tập có FBI) |
| Vai | `**CẢNH SÁT ĐỊA PHƯƠNG**` | `**地方警察**` | → N |
| Chỉ dẫn đọc | `**HOST** *(giọng trầm)*:` | `**ホスト** *(低く落ち着いた声で)*:` | Dịch chỉ dẫn diễn xuất, không đọc thành tiếng. |
| Nghỉ | `**[Nghỉ 1.5 giây]**` | `**[休止 1.5秒]**` | Giữ đúng số giây. |
| Hiệu ứng | `**[BGM]:** ...` · `**[SFX]:** ...` | `**[BGM]:** ...` · `**[SFX]:** ...` | **Giữ nguyên nhãn tiếng Anh in hoa.** Chỉ dịch mô tả tiếng Nhật. |
| Bảng | `\| ... \|` | `\| ... \|` | Giữ nguyên cấu trúc cột/hàng. Cột vai dùng `キャスト構成` (không dùng `配声`). |

---

## C. CÁC BẪY DỊCH MÁY TIẾNG NHẬT & QUY TẮC CHỈNH SỬA

Khi dịch kịch bản bằng mô hình ngôn ngữ lớn (LLM), có 5 nhóm lỗi đặc thù cần quét và sửa triệt để:

### 1. Bẫy từ vựng tiếng Trung (Chinese Interference)
Mô hình dịch thường nhầm lẫn giữa chữ Hán tiếng Trung và từ vựng tiếng Nhật:
- **转場** → phải là **場面転換** hoặc **シーン転換**
- **配声** → phải là **キャスト構成** hoặc **配役**
- **深沉 / 低沉** → phải là **低く落ち着いた声** hoặc **重々しい声**
- **沉思** → phải là **思索的**
- **沉默** → phải là **沈黙** (dùng chữ 黙 chuẩn Nhật, không dùng 默)
- **上崗 / 上岗** → rác sinh ra cuối câu, sửa thành **広がる** / **漂う**
- **卧室** → phải là **寝室**
- **骚扰** → phải là **つきまとい** hoặc **嫌がらせ**
- **刑罚** → phải là **刑罰** (dùng 罰 chuẩn Nhật)
- **真诚** → phải là **真摯** hoặc **誠実**
- **亲自** → phải là **自ら**
- **她的 / 他的** → phải là **彼女の / 彼の**
- **所谓** → phải là **いわゆる**
- **嫉妒** → phải là **嫉妬** (dùng 妬 chuẩn Nhật)
- **妇女** → phải là **女性たち**
- **规律** → phải là **生活リズム** hoặc **習慣**
- **拒绝了** → phải là **拒否するなら** / **拒絶するなら**
- **動摇** → phải là **動揺**
- **撕裂** → phải là **引き裂く** / **切り裂く**
- **極贅** → phải là **極めて贅沢に**
- **艰苦** → phải là **過酷な捜査**
- **霉臭** → phải là **カビ臭さ**
- **市中心** → phải là **中心街** hoặc **都心部**
- **吞** → phải là **呑** / **飲み込まれた**
- **别扭** → phải là **歪んだ**

### 2. Chữ Hán Giản Thể (Simplified Chinese Glyphs)
Toàn bộ kịch bản tiếng Nhật **phải dùng chữ Hán Tân Tự Thể (新字体 - Joyo Kanji)**:
- `聪` → `聡` (聡明)
- `类` → `類` (人類)
- `亲` → `親`
- `洁` → `潔` (身ぎれい)
- `壳` → `殻` (外殻)
- `寻` → `尋` (尋常)
- `轻` → `軽` (かすかな)
- `础` → `礎` (基礎)
- `纤` → `細` (細い)
- `碎` → `砕` (砕け散る)
- `剥` thay vì dạng dị thể `剝`

### 3. Nhầm lẫn đại từ nhân xưng tiếng Việt
- "Ông cho biết..." trong lời kể ngôi thứ 3: LLM hay dịch nhầm thành `あなたは...と述べました` (xưng "bạn"). Phải sửa thành `その男は...と明かしました` hoặc `男の供述によれば...`.
- "Người phu xe" dịch thành `添乗者` (hướng dẫn viên du lịch): phải sửa thành `荷車を押していた男`.

### 4. Thuật ngữ và viết tắt
- Giữ nguyên chuẩn quốc tế: **DNA** (không dùng từ tiếng Pháp/Việt `ADN`).
- Phiên âm địa danh: `ミズーリ州` (Missouri - không viết `ミズリー`), `フロリダ州`, `カリフォルニア州`.

### 5. Văn phong đọc thành tiếng (Audio Documentary)
- Giọng Host dẫn chuyện dùng thể lịch sự `です・ます` hoặc thể trần thuật tài liệu nhất quán.
- Lời trích dẫn nhân chứng/thủ phạm trong ngoặc `「...」` dùng lối nói tự nhiên của nhân vật.
- Tuyệt đối giữ đúng tỷ lệ 1 câu tiếng Việt = 1 câu tiếng Nhật để khớp timeline và diễn xuất khi đọc TTS.
