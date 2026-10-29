# CHUỨ CỐ ĐỊNH — BẢN TIẾNG HÀN (KOREAN EDITION)

*Tài liệu này là chuẩn bắt buộc cho **bản tiếng Hàn** của kịch bản Amber Eyes.
Áp dụng cho **Tập 01 – Tập 29**. Ngày lập: 23/10/2026.*

> Bản tiếng Hàn **không phải** bản dịch lơ là. Nó là **phiên bản ngôn ngữ** của kịch bản: cùng cấu trúc,
> cùng mã câu, cùng vai, cùng số câu — chỉ đổi ngôn ngữ. Mọi thứ được **đọc thành tiếng**, nên văn phong
> phải **đọc được bằng tai**, không phải văn phong viết học thuật.

---

## A. ĐƯỜNG DẪN & TÊN FILE

| Việc | Quy ước |
|---|---|
| Thư mục | `01_KICH_BAN/TapXX_KO/` (đặt cạnh `TapXX/`, `TapXX_EN/`) |
| File kịch bản | `01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md` |
| Nguồn (file tiếng Việt) | `01_KICH_BAN/TapXX/kichban_tapXX_<ngày>.md` — **không sửa file nguồn** |
| Bản EN (để đối chiếu) | `01_KICH_BAN/TapXX_EN/kichban_tapXX_EN.md` (chỉ có Tập 01–03) |

**Tập 01 dùng file nguồn `kichban_tap01_22102026_v2.md`** (bản đã làm dịu mô tả bạo lực).
Tập 02 dùng `kichban_tap02_22102026.md`. Tập 03–29 dùng file `kichban_tapXX_23102026.md` (trừ Tập 04–08 cũng là `23102026`).

---

## B. ÁNH XẠ CẤU TRÚC (bắt buộc — không đổi)

| Thành phần | Tiếng Việt (nguồn) | **Tiếng Hàn (bản KO)** | Ghi chú |
|---|---|---|---|
| Tiêu đề hồi | `## HỒI 1: ...` | `## 막 1: ...` | `막` = act. Parser đã hỗ trợ. **Giữ nguyên số thứ tự 1–5.** |
| Vai | `**HOST**` | `**호스트**` | → H |
| Vai | `**ĐIỀU TRA VIÊN**` | `**수사관**` | → D |
| Vai | `**CHUYÊN GIA TÂM LÝ**` | `**심리학자**` | → C |
| Vai | `**NGƯỜI BÌNH THƯỜNG**` | `**일반인**` | → N |
| Vai | `**ĐẶC VỤ FBI**` | `**연방수사국**` | → D (chỉ Tập 03, 06) |
| Vai | `**CẢNH SÁT ĐỊA PHƯƠNG**` | `**지역경찰**` | → N (chỉ Tập 03) |
| Chỉ dẫn đọc | `**HOST** *(giọng trầm)*:` | `**호스트** *(낮고 깊은 목소리)*:` | Dịch chỉ dẫn. Không đọc. |
| Nghỉ | `**[Nghỉ 1.5 giây]**` | `**[정지 1.5초]**` | **Giữ đúng số giây.** Parser đã hỗ trợ. |
| Nghỉ có chú thích | `**[Nghỉ 2 giây – Nhạc nền dừng đột ngột]**` | `**[정지 2초 – 음악이 갑자기 멈춤]**` | Dịch phần chú thích. |
| Hiệu ứng | `**[BGM]:** ...` · `**[SFX]:** ...` | `**[BGM]:** ...` · `**[SFX]:** ...` | **Giữ nguyên nhãn tiếng Anh** (đồ hoạ dựng đọc nhãn này). Chỉ dịch phần mô tả. |
| Gạch đầu dòng | `*   ` hoặc `1.  ` | `*   ` hoặc `1.  ` | **Giữ nguyên số lượng và thứ tự gạch đầu dòng.** |
| Nhấn mạnh | `**đậm**` · `*nghiêng*` | `**강조**` · `*기울임*` | Giữ đúng vị trí và cấp độ nhấn mạnh. |
| Trích dẫn nguyên văn | `'…'` | `‘…’` | **Nội dung trong dấu nháy GIỮ NGUYÊN tiếng Anh.** Xem §D. |
| Bọc đoạn thoại | `"…"` (Tập 01–18) | `"…"` | Giữ nguyên cách bọc của nguồn (Tập 19–29 không bọc → KO cũng không bọc). |

> **Lưu ý đánh số câu.** Parser tự đánh số `N.01`, `N.02`… theo thứ tự phần tử trong tập. Mã câu của bản KO
> **phải khớp đúng** bản tiếng Việt (cùng số phần tử, cùng thứ tự, cùng vai). Đó là điều kiện để dùng chung
> `acting_tapXX.json`, `shots.json`, `sfx_tapXX.json` với bản VN. Xem §F.

---

## C. QUY TẮC DỊCH — BẤT BUỘC

### C1. Một câu tiếng Việt → đúng một câu tiếng Hàn

- **Tỷ lệ câu phải giống hệt.** Bản EN dùng nguyên tắc "One English sentence for every Vietnamese
  sentence". Bản KO dùng cùng nguyên tắc. Không gộp hai câu VN thành một câu KO, không tách một câu VN
  thành hai câu KO.
- Câu tiếng Hàn kết thúc bằng `.` `?` `!` `…` — **giữ đúng dấu câu của nguồn** (nguồn dùng `?` thì KO dùng `?`).
- Câu trong bảng EN đã tách sẵn ở dấu chấm + chữ hoa; câu Hàn phải tách được như vậy. Nghĩa là **sau mỗi dấu
  chấm kết thúc câu phải có một khoảng trắng rồi tới chữ Hangeul** (không bỏ khoảng trắng, không xuống dòng giữa câu).

### C1b. Bốn quy tắc "đừng làm hỏng cấu trúc" — ĐÂY LÀ CHỖ SAI NHIỀU NHẤT

Parser cắt câu tại `. ? !` khi **sau đó** là khoảng trắng + chữ Hangeul / chữ hoa / dấu nháy.
Hậu quả: **mọi thay đổi về dấu câu đều đổi số câu.**

| # | Quy tắc | Ví dụ |
|---|---|---|
| 1 | **Dấu `:` trong bản VN nối vào CÙNG một câu.** Giữ nguyên dấu `:`, **đừng đổi thành dấu chấm.** | VN `chính là: *Tại sao?*` → KO `바로 이것이다: *왜?*` — nếu đổi thành `.` thì tách thành 2 câu. |
| 2 | **Dấu `…` / `...` ở giữa câu → dùng ` – `.** Vì sau `…` là chữ Hangeul thì luôn bị tách câu. | VN `... của người lớn... thì thứ khoác áo` → KO `... 어른의 이기심을 채우는 도구가 되면 – 그 성인` |
| 3 | **Số luôn viết bằng chữ số Ả Rập**, kể cả số nhỏ. | `3 tầng` → `3개 층` (KHÔNG `세 개 층` — QC đòi đủ chữ số của bản VN). |
| 4 | **Sau dấu chấm phải có khoảng trắng rồi tới chữ Hangeul.** | `…이었다. 그 애가…` (đúng) — `…이었다.그 애가…` thì **không** tách câu. |

> **Cách tự kiểm tra nhanh:** chạy QC (§F). Nếu báo `sentence count mismatch`, nghĩa là đã phá vỡ
> cấu trúc ở một trong 4 quy tắc trên.

### C1c. Chỉ dùng Hangul + chữ Latin

- **Không dùng chữ Hán (한자)** trong phần thoại. Chỉ Hangul + chữ Latin + số + dấu câu.
- Nếu bản VN có dấu tiếng Việt còn sót trong bản KO → lỗi (QC báo). Ngoại lệ hợp lệ: tên riêng
  nước ngoài như `Folie à Deux`, `Münchausen` — để nguyên.

### C1d. Cơ chế parser — 5 điều bắt buộc (đọc trước khi viết)

Đây là những điều **đã kiểm chứng bằng công cụ**, sai một là QC FAIL. Xem `.work/parse_kichban.py`.

| # | Điều bắt buộc | Hệ quả |
|---|---|---|
| 1 | **Parser tách câu theo từng DÒNG VẬT LÝ (paragraph), không theo cả khối.** Một dòng = một đoạn văn; các câu trong đó tách ra bằng `LATIN_SPLIT`. | Bản KO phải **giữ số dòng vật lý** của bản VN. Một lượt thoại VN nằm trên 1 dòng ⇒ bản KO cũng nằm trên 1 dòng (các câu cách nhau bằng `. `). |
| 2 | **Không câu nào được bắt đầu bằng chữ số** (trừ câu đầu tiên của dòng). `LATIN_SPLIT` chỉ tách sau `. ? ! …` + khoảng trắng + **chữ Hangeul / chữ hoa / dấu nháy**. Số ở đầu câu **chặn** điểm tách ⇒ hai câu bị nuốt làm một. | `…사면 검토가 가능합니다. 2025년과 2026년까지…` ⇒ **mất 1 câu**. Viết lại thành `…가능합니다. 상고 절차는 2025년과 2026년까지…`. |
| 3 | **Các block cùng vai, đứng liền nhau, không có cue ở giữa ⇒ parser GỘP thành MỘT phần tử.** | Blueprint ghi `blocks=N` ⇒ viết N block có nhãn vai **liền kề nhau**, không chèn cue. (Tập 13 mục 5.05 = 6 block `호스트` liền nhau = 1 phần tử 17 câu.) |
| 4 | **Dấu `:` không bao giờ tách câu.** Dấu `…`/`...` giữa câu phải đổi thành ` – ` (chữ Hangeul ngay sau `…` sẽ bị tách sai). | Giữ nguyên `:` của nguồn. Đổi `…` → ` – `. |
| 5 | **QC tên riêng: tên Latin nhiều từ là lỗi NẶNG (FAIL), tên một từ chỉ là CẢNH BÁO mềm.** | Tên nhiều từ (`Huei Hann Pan`, `Daniel Wong`, `David Mylvaganam`, `Helen Avenue`, `Amber Eyes`, `Nhi SickKids`…) **bắt buộc** phải có nguyên chữ Latin trong bản KO. Tên một từ (`Khu`, `Thay`, `Quan`, `Cha`, `Hoang`, `Ban`, `Chi`, `Kho`, `Ngay`…) là **từ tiếng Việt bị regex bắt nhầm** — bỏ qua, không sửa. |

> **Bẫy thêm:** regex tên riêng chỉ nhận từ có **≥ 3 chữ Latin** sau chữ hoa đầu. Vì vậy `Bich Ha Pan` bị tách thành `Bich` + `Pan` (không phải một tên 3 từ), còn `Huei Hann Pan` là một tên 3 từ. Nếu một từ tiếng Anh đứng trước sẽ bị **gộp vào** tên (`First Lady Rosalynn Carter` ⇒ QC báo thiếu `Rosalynn Carter`), hãy thêm dấu phẩy trước tên hoặc bỏ từ dẫn nhập.

### C2. Văn phong đọc thành tiếng (radio documentary)

- Câu ngắn, trung tính, dễ phát âm. **Tránh** câu quá dài, tránh phép từ Hán nối dài chồng nhau.
- Dùng `-습니다` cho lời dẫn chuyện phân tích (HOST, 심리학자). Lời kể nhân chứng (일반인) dùng `-어요/-습니다`
  tùy ngữ cảnh, giữ **tính cá nhân** của lời kể.
- **Không** dùng phong cách văn chương hoa mỹ. Đây là tài liệu điều tra, giọng kể tối giản.
- Cách xưng hô: người kể dùng `저는` / `저희는`; chuyên gia dùng `저는 … 으로/로 보고 있습니다` khi phân tích.

### C3. Giữ nguyên tuyệt đối (không dịch, không đổi)

| Hạng mục | Quy tắc |
|---|---|
| **Tên riêng** | Giữ nguyên chữ Latin: `Dee Dee Blanchard`, `Edmund Kemper`, `Jefferson Dahmer`, `Springfield`. **Không phiên âm, không dịch.** |
| **Địa danh** | Giữ nguyên tiếng Anh: `Missouri`, `Pueblo`, `Milwaukee`, `Oxford Apartments`. Thêm nội suy nếu cần: `밀워키(Milwaukee)`. |
| **Số** | Giữ **đúng giá trị**. Định dạng Hàn: `1991년`, `7월 22일`, `32세`, `85%`, `16년`. Xem §D3. |
| **Danh từ tiếng Anh** | Giữ tiếng Anh trong ngoặc khi là thuật ngữ chuyên ngành: `범인 프로파일링(profiling)`. |
| **Trích dẫn nguyên văn** | Giữ nguyên tiếng Anh trong `‘…’`. Xem §D. |
| **Tiêu đề vụ án** | Giữ nguyên tên: `Münchausen`, `DSM-5-TR`, `FBI Behavioral Science Unit`. |

### C4. Cấm

- ❌ Tóm tắt, lược bỏ, hay bổ sung thông tin không có trong nguồn.
- ❌ Bịa thêm chi tiết về vụ án, nạn nhân, hoặc phương pháp điều tra.
- ❌ Mô tả bạo lực chi tiết hơn bản nguồn. **Bản nguồn đã được làm dịu (violence-softened) — giữ nguyên mức đó.**
- ❌ Đổi số thứ tự hồi, số câu, số gạch đầu dòng, vai.
- ❌ Bỏ dấu `**` / `*` / `‘…’` hoặc đổi vị trí.

---

## D. XỬ LÝ RIÊNG 4 THỨ DỄ SAI

### D1. Vai (giọng đọc)

Tên vai trong ngoặc `*(…)*` phải mô tả **giọng**, không phải cảm xúc nhất thời.

| Nguồn | KO |
|---|---|
| `*(Giọng đọc chậm, trầm, giữ khoảng cách khách quan)*` | `*(느리고 깊게, 관찰자 시선의 거리를 유지하며)*` |
| `*(Đẩy nhanh nhịp độ hơn một chút)*` | `*(조금 더 빠른 호흡으로)*` |
| `*(Giọng hạ trầm, sắc lạnh và dứt khoát)*` | `*(낮고 차분하며, 날카롭고 단호하게)*` |
| `*(Giọng điềm đạm, học thuật)*` | `*(차분하고 학문적인)*` |

### D2. Bảng vai / PRODUCTION BRIEF (phần đầu tập)

Tập 01–18 có bảng `## THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN (PRODUCTION BRIEF)`;
Tập 19–29 có bảng `## BẢNG PHÂN VAI VÀ CẤU TRÚC GIỌNG ĐỌC`.

- **Dịch nội dung bảng sang tiếng Hàn, giữ nguyên số dòng và số cột.**
- Cột `Ký hiệu` (`H`, `D`, `C`, `N1`, `N2`, `TỔNG`) giữ nguyên — đây là mã vai dùng máy đọc.
- **Số câu trong bảng KHÔNG được sửa.** Nếu bảng ghi 165 câu thì bản KO vẫn ghi 165 câu.
- Tên vai trong bảng dịch sang Hàn nhưng **tên nhân vật thể hiện giữ nguyên tiếng Anh**.

### D3. Số — quy tắc chuyển sang cách viết Hàn

| Nguồn (VN) | KO |
|---|---|
| `ngày 22 tháng 7 năm 1991` | `1991년 7월 22일` |
| `32 tuổi` | `32세` |
| `85% bản án` | `판결의 85%` |
| `2 mét 06 (6 feet 9 inch)` | `키 206cm(약 6피트 9인치)` |
| `127 ký (280 pounds)` | `약 127kg(약 280파운드)` |
| `khoảng 1.600 cây số` | `약 1,600km` |
| `mức án 10 năm tù` | `10년 형` |

**Giá trị số tuyệt đối không được đổi.** Đổi cách viết là được; đổi số là không.

### D4. Trích dẫn nguyên văn

Quy ước của kênh: `'…'` trong bản VN là **trích dẫn**. Có **hai loại**, xử lý khác nhau:

**Loại 1 — trích dẫn nguyên văn** (lời nói thật của người thật, hoặc câu trích nguyên văn từ tài liệu gốc):
giữ **nguyên văn tiếng Anh** trong `‘…’`, đặt **ý nghĩa tiếng Hàn ở NGOÀI** dấu nháy.

```
VN:  *'Ở trong nhà tù của pháp luật, lần đầu tiên trong đời tôi cảm thấy mình được tự do hơn cả khi sống trong ngôi nhà của mẹ.'*
KO:  *'In prison, for the first time in my life, I feel freer than I ever did in my mother's house.'*
    的法監獄에서,这是我平생第一次觉得自己比住在母亲家里时还要自由。
```

**Loại 2 — nhãn/nickname do chính kịch bản đặt ra** (`'Vị thánh tử đạo'`, `'bảo vệ sức khỏe'`, `'saintly'`):
**dịch bên trong** dấu nháy, vẫn giữ dấu nháy.

```
VN:  Cơn nghiện ánh hào quang của 'Vị thánh tử đạo'.
KO:  ‘성자의 영광'에 대한 중독.
```

**Cách phân biệt (bắt buộc):**

| Nguồn | Loại | Xử lý |
|---|---|---|
| Lời khai của nghi phạm / nhân chứng / chuyên gia | 1 | giữ tiếng Anh, dịch nghĩa ra ngoài |
| Câu trích từ sách bài báo gốc (tiếng Anh) | 1 | giữ tiếng Anh, dịch nghĩa ra ngoài |
| Nhãn do kịch bản tự đặt (nickname, slogan, scare-quote) | 2 | dịch bên trong, giữ dấu nháy |

> **Phân biệt loại 1 / loại 2 theo BẢN CHÂN DÒNG — KHÔNG theo ngôn ngữ của câu trong bản VN.**
> Bản VN thường đã dịch sẵn lời thoại tiếng Anh sang tiếng Việt (`'Tôi chỉ muốn chấm dứt nỗi đau đớn cho họ'`,
> `'Vậy, cô ấy ở đâu?'`, `'Tên tôi là Nik…'`), nhưng đó vẫn là **loại 1** vì là lời nói thật của
> nhân chứng / nghi phạm / chuyên gia. **Chuẩn đối chiếu là bản EN** (`01_KICH_BAN/TapXX_EN/kichban_tapXX_EN.md`):
> EN giữ tiếng Anh trong ngoặc ⇒ KO cũng giữ tiếng Anh trong `‘…’` **và đặt nghĩa Hàn ở ngoài ngoặc**;
> EN dịch bên trong (nhãn/nickname do kịch bản tự đặt) ⇒ KO dịch bên trong, giữ dấu nháy.
> **Không được dịch các quote loại 1 sang Hàn** — sẽ mất tính nguyên văn của lời khai.
> Kiểm tra nhanh: **mọi quote tiếng Anh trong bản KO phải có chữ Hangeul ngoài dấu nháy**
> (toàn bộ 29 tập hiện tại đều đạt; xem `.work/_gloss_audit.py`).

Trong bản KO dùng dấu nháy đơn cong `‘…’` (parser tự đổi thành `“…”` khi hiển thị).
**Số lượng dấu nháy phải khớp với bản nguồn** — QC sẽ báo lỗi nếu lệch.

**Cách đặt phần dịch nghĩa tiếng Hàn mà không làm vỡ cấu trúc câu.**
Không được đặt phần dịch nghĩa **sau** dấu chấm của trích dẫn — sẽ thành câu mới. Đặt **trước**,
nối bằng ` – ` (dấu gạch ngang), rồi mới tới trích dẫn:

```
KO:  ... 감방 안에서 Gypsy가 남긴 한 문장이었다 – 법의 감옥 안에서 그녀가 평생 처음으로
     어머니의 집에 살 때보다 더 자유롭게 느껴졌다는, *'In prison, for the first time in my life,
     I feel freer than I ever did in my mother's house.'*
```

(đây là **1 câu**, khớp với 1 câu của bản VN)

---

## E. ĐẦU FILE (tiêu đề) CHO TỪNG NHÓM TẬP

### Tập 01–18

```markdown
# 범죄심리 오디오 / 팟캐스트 스크립트 — 한국어판
**주제:** <주제 번역>
**원본:** `01_KICH_BAN/TapXX/kichban_tapXX_<ngày>.md`. vietnamese 문장마다 한글 문장 하나, 구조·코드 동일.
**사실 및 법률 검토:** <한 문장, xem file REVIEW tương ứng>

---

## 제작 브리프(PRODUCTION BRIEF)

| 항목 | 기준 설정(내레이터 주도 다큐멘터리) |
| :--- | :--- |
| **에피소드 제목** | <제목 번역> |
| **형식** | <번역> |
| **목표 길이** | 25 – 27분 (5개 파트 + 전환 음악) |
| **배경음악(BGM) 권장** | <번역> |
| **음성 배분 방식** | - **호스트(60%):** …<br>- **수사관(15%):** …<br>- **심리학자(20%):** …<br>- **일반인(5%):** … |

---
```

> `**원본:**` phải **ghi đúng đường dẫn file nguồn thật**.

### Tập 19–29

Giữ **đúng cấu trúc file nguồn**: tiêu đề `# …` + khối metadata dạng gạch đầu dòng (`* **주제:** …`) +
`## 배역표 및 음성 구성` với bảng 5–7 cột. Dịch toàn bộ nội dung, giữ số.

---

## F. QC BẮT BUỘC (chạy trước khi bàn giao)

```powershell
py -3 .work/_qc_ko_parity.py <file_vn.md> <file_ko.md>
```

QC kiểm tra tự động, từng mục phải xanh:

| # | Kiểm tra | Mức |
|---|---|---|
| 1 | Số hồi (5) và số thứ tự hồi | phải khớp |
| 2 | Chuỗi phần tử (lượt nói / SFX / BGM / nghỉ) — **thứ tự y hệt** | phải khớp |
| 3 | Vai của từng lượt nói | phải khớp |
| 4 | Số câu của từng lượt nói | phải khớp |
| 5 | Số giây của từng mốc nghỉ | phải khớp |
| 6 | Mọi **số** trong bản VN phải có trong bản KO (theo lượt tương ứng) | phải khớp |
| 7 | Mọi **tên riêng tiếng Anh** trong bản VN phải có trong bản KO | phải khớp |
| 8 | Tỉ lệ ký tự Hangeul trong phần thoại | ≥ 60 % |
| 9 | Không còn dấu tiếng Việt trong phần thoại (`ệ ộ ữ ầ ồ ế ờ ạ ả …`) | 0 lỗi |

Ngoài QC tự động, **phải tự đọc lại** ít nhất:

- 2 câu có trích dẫn nguyên văn → đối chiếu với nguồn, chắc chắn nguyên văn **không bị dịch**;
- 1 lượt nói của vai **일반인** → phải có **tính cá nhân**, không giống giọng phát thanh;
- 1 lượt nói của vai **심리학자** → thuật ngữ đúng theo §G.

### F1. Checklist 13 điểm — dùng cho TỪNG tập trước khi bàn giao

| # | Kiểm tra | Lệnh / cách kiểm |
|---|---|---|
| 1 | Đúng số phần tử, đúng thứ tự | QC mục 2 |
| 2 | Đúng số câu từng lượt | QC mục 4 |
| 3 | Giữ **số dòng vật lý** của nguồn | đọc song song file VN |
| 4 | Mọi cue `**[BGM]:**` / `**[SFX]:**` giữ **nguyên nhãn tiếng Anh**, đúng vị trí | QC mục 2 |
| 5 | `blocks=N` ⇒ N block cùng vai **liền nhau**, không cue xen giữa | QC mục 2 |
| 6 | **Không câu nào bắt đầu bằng chữ số** (trừ câu đầu dòng) | `_lint_ko.py` mục cuối |
| 7 | Giữ nguyên mọi dấu `:`; `…` → ` – ` | QC mục 4 |
| 8 | Mọi số của bản VN còn trong bản KO, viết bằng chữ số Ả Rập | QC mục 6 |
| 9 | Tên riêng / địa danh Latin giữ **nguyên chữ Latin** (không phiên âm sang Hangeul) | QC mục 7 + lint |
| 10 | Chỉ Hangul + Latin + số: **không Hán tự**, không Cyrillic, không dấu tiếng Việt sót, không ký tự rác | `_lint_ko.py` |
| 11 | Số cặp dấu nháy `‘…’` **khớp** bản VN; loại 1 giữ tiếng Anh, loại 2 dịch bên trong | QC mục trích dẫn |
| 12 | Cùng số bullet/danh sách, cùng kiểu | QC mục list items |
| 13 | Nhãn vai Hàn, `## 막 N`, `**[정지 X초]**`; lời dẫn `-습니다`, lời `일반인` có **tính cá nhân** | đọc tay |

### F2. Lệnh kiểm tra

```powershell
# QC cặp (bắt buộc) — phải in PASS
py -3 .work/_qc_ko_parity.py 01_KICH_BAN/TapXX/kichban_tapXX_<ngày>.md 01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md

# Lint ký tự (Hán tự, ký tự rạc, dấu tiếng Việt, câu bắt đầu bằng số)
py -3 .work/_lint_ko.py 01_KICH_BAN/TapXX/kichban_tapXX_<ngày>.md 01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md

# Chạy cho cả 29 tập
py -3 .work/_qc_ko_all.py
py -3 .work/_lint_ko_all.py
```

> **Đọc kết quả WARN của QC:** `single-word names not found anywhere in the KO file` là **báo động giả** —
> regex tên riêng bắt nhầm các từ tiếng Việt bắt đầu câu (`Khu`, `Thay`, `Quan`, `Cha`, `Hoang`, `Ban`,
> `Chi`, `Kho`, `Ngay`…). Không sửa theo WARN này. Tên **nhiều từ** báo thiếu mới là lỗi thật.

---

## G. THUẬT NGỮ CHÍNH (dùng thống nhất trong cả 29 tập)

| Tiếng Việt | **Tiếng Hàn** |
|---|---|
| Hội chứng Münchausen qua trung gian (FDIA) | **대리 뮌하우젠 증후군(FDIA)** / 타인에게 강요된 사기성장애(FDIA) |
| Tâm lý học tội phạm | **범죄심리학** |
| Tâm thần học pháp y | **법의정신의학** |
| Giải phẫu tâm lý | **심리해부(psychological autopsy)** |
| Lập hồ sơ tâm lý tội phạm (profiling) | **범인 프로파일링(profiling)** |
| Kẻ thái nhân cách | **사이코패스** |
| Người bình thường | **일반인** |
| Chuyên gia tâm lý | **심리학자** |
| Điều tra viên | **수사관** |
| Sự bất lực tập nhiễm | **학습된 무력감(learned helplessness)** |
| Gắn kết chấn thương | **트라우마 본딩(trauma bonding)** |
| Phương thức hành động (Modus Operandi) | **범행 수법(modus operandi)** |
| Chẩn đoán giả bệnh | **사기성 장애(factitious disorder)** |
| Chấn thương mẫu hệ | **부모–자식 병리(mother-son pathology)** |
| Rối loạn nhân cách ranh giới (BPD) | **경계선 인격장애(BPD)** |
| Chẩn đoán giả bệnh tự thú | **자진 보고형 사기성 장애** |
| Hồ sơ vụ án | **사건 기록** |
| Lời khai | **진술** |
| Thẩm vấn | **심문** |
| Phiên tòa | **재판** |
| Phán quyết | **판결** |
| Nhân chứng | **증인** |
| Nạn nhân | **피해자** |
| Nghi phạm | **용의자** |
| Chứng cứ | **증거** |
| Manh mối | **단서** |
| Kẻ thao túng | **조종자** |
| Dấu hiệu cảnh báo đỏ | **위험 신호(red flags)** |
| Bài học cảnh tỉnh | **각성의 교훈** |
| Điện thoại bốt (payphone) | **공중전화(public payphone)** |
| Băng ghi âm | **테이프 레코더** |
| Lời đọc riêng | `(aside)` → **`(독백)`** — dùng cho lời thoại tự thú nội tâm |

---

## H. SAU KHI BẢN KO ĐƯỢC DUYỆT

Bản KO dùng chung được `acting_tapXX.json`, `shots.json`, `sfx_tapXX.json` của bản VN **nhờ mã câu trùng khớp**.
Khi bắt đầu sản xuất âm thanh:

1. `AE_LANG=ko AE_EP=XX py -3 .work/parse_kichban.py 01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md .work/script_tapXX_KO.json`
2. Chọn giọng Hàn (bộ H) — chạy **G8–G10** trước khi dựng.
3. Số trong bản KO **không cần** đổi sang chữ như bản VN (tiếng Hàn đọc số tự nhiên).

---

*Xem thêm: `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (mục A2 – định dạng kịch bản), `02_SAN_XUAT/Tap02_EN/CHU_CO_DINH_EN.md` (bản EN).*
