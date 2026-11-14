# TIÊU CHUẨN DỰNG VIDEO — KÊNH AMBER EYES (PHẦN A)

**Phiên bản 11 · Bản mẫu tiêu chuẩn** · Cập nhật 23/10/2026
**Trạng thái:** đã chạy thật trọn vẹn với Tập 01 (`Tap01_master.mp4`, 18:53) và **Tập 02** (`Tap02_master.mp4`, ~26:45, giọng bộ A). Mọi lệnh, số liệu và lỗi trong file này lấy từ hai lần chạy đó.
**Thay đổi lớn ở bản 11:** giọng bộ A + quy tắc giọng G1–G11 (A4.1–A4.2) · chọn tập bằng `AE_EP` và cấu hình tập trong `edition.py` (A12) · âm thanh stereo có nền môi trường (A4.4, `sfx_tapXX.json`) · ảnh tĩnh mọi shot trước khi dựng · bẫy #17–24 (A11).

## Cách dùng file này

| Tài liệu | Nội dung | Tập mới làm gì |
|---|---|---|
| **File này — `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md`** (Phần A) | Quy tắc, quy trình, lệnh chạy, âm thanh, đồ hoạ, kiểm tra, pháp lý, các bẫy đã gặp | **Giữ nguyên.** Chỉ sửa khi đổi tiêu chuẩn của kênh |
| **Hồ sơ tập — `02_SAN_XUAT/TapXX/KeHoach_Video_TapXX.md`** (Phần B) | Số liệu, ánh xạ riêng, bảng shot, phụ lục của từng tập | Sao chép `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md` làm mẫu, thay nội dung tập mới |

**Cấu trúc thư mục chuẩn:** xem `README.md` ở thư mục gốc.

Người dùng chỉ cần đưa **kịch bản đúng định dạng A2**. AI làm phần còn lại theo A3, dừng lại báo khi gặp vấn đề.

---

# PHẦN A — TIÊU CHUẨN CHUNG

## A0. Chín quy tắc vàng

| # | Quy tắc | Vì sao |
|---|---|---|
| **V1** | **Đơn vị đồng bộ là CÂU.** TTS đọc từng câu thành một file riêng; mọi mốc thời gian đo bằng ffprobe trên file đó | Chia block theo tỉ lệ từng làm hình lệch lời tới 16 s |
| **V2** | **Hình chỉ đổi ở đầu câu.** Cấm chia shot theo tỉ lệ thời gian | Lỗi "vào nội dung rồi hình mới xuất hiện" |
| **V3** | **Chữ trên hình lấy từ chính câu đang đọc.** Không thêm dữ kiện, con số; câu trích phải **nguyên văn** (được lược bằng `…`, không được cắt cụt rồi tự thêm dấu) | Từng tự bịa "19 tuổi"; từng cắt cụt câu trích ở Tập 01 |
| **V4** | **Không có im lặng tuyệt đối quá 0,3 s.** Lớp nền trầm luôn chạy | Từng câm 6 s ở 0:26 |
| **V5** | **Người thật trong vụ án chỉ hiện dạng bóng**, mặt chìm hoàn toàn. **Quan chức, bác sĩ thật không được vẽ** — chỉ hiện tên | Người thật; có thể là trẻ vị thành niên |
| **V6** | **Linh thú là nhân vật minh hoạ**, nhãn *"Nhân vật minh hoạ · giọng đọc AI"* ở lần xuất hiện đầu | Không để người xem hiểu là phỏng vấn thật |
| **V7** | **Nền vụ án luôn toàn màn hình; linh thú ≤ 20% khung**, chỉ ở góc | Bố cục đã chốt |
| **V8** | **Mọi tập mở đầu bằng intro kênh 22,41 s; mọi tài sản có dòng trong `provenance.json`** | Nhận diện kênh; hồ sơ khi bị khiếu nại |
| **V9** | **Trọng tâm là phân tích tâm lý theo 5 trụ cột (A2c).** Không mô tả chi tiết bạo lực, thương tích, thi thể, cách gây hại — cả lời lẫn hình | Định hướng kênh; chiều sâu kịch bản; giảm rủi ro quảng cáo hạn chế |

## A1. Đầu vào và đầu ra của mỗi tập

**Đầu vào (người dùng):**
- [ ] `01_KICH_BAN/TapXX/kichban_tapXX.md` đúng định dạng A2, **đã giảm bạo lực theo V9** (xem Phụ lục B trong `02_SAN_XUAT/Tap01/KeHoach_Video_Tap01.md` làm mẫu)
- [ ] Tên tập
- [ ] (tuỳ chọn) ghi chú phong cách, cảnh đặc biệt

**Đầu ra (AI)** — tất cả nằm trong `02_SAN_XUAT/TapXX/xuat_ban/` (riêng `provenance.json` ở thư mục gốc, cộng dồn các tập):

| File | Nội dung |
|---|---|
| `TapXX_master.mp4` | Video chính (H.264 + AAC 192k) |
| `TapXX_master.mp3` | Âm thanh tổng |
| `TapXX.srt` | Phụ đề có tên vai |
| `thumbnail.png` | 1280×720 |
| `mo_ta.txt` | Mô tả YouTube có mốc chương |
| `nguon_tham_khao.md` | Danh sách câu cần nguồn — **người dùng điền link** |
| `provenance.json` | Nguồn gốc mọi tài sản (cộng dồn qua các tập) |

## A2. Định dạng kịch bản bắt buộc

`.work/parse_kichban.py` chỉ hiểu đúng các mẫu sau:

| Dòng | Mẫu chính xác | Ghi chú |
|---|---|---|
| Hồi | `## HỒI N: tên hồi` | N = 1…5; mã phần tử đếm lại từ `N.01` |
| Lượt nói | `**HOST** *(chỉ dẫn)*:` | Tên vai đúng 1 trong 4: `HOST` · `ĐIỀU TRA VIÊN` · `CHUYÊN GIA TÂM LÝ` · `NGƯỜI BÌNH THƯỜNG`. Chỉ dẫn không đọc |
| Hiệu ứng | `**[SFX]:** mô tả` · `**[BGM]:** mô tả` | |
| Nghỉ | `**[Nghỉ X giây – ghi chú]**` | Tối đa 2,5 s khi dựng |
| Gạch đầu dòng | `*   ` hoặc `1.  ` | Mỗi dòng thành một câu riêng |
| Trích dẫn | `'…'` | Hiện `“…”` trên hình; bỏ dấu khi đọc |
| Nhấn mạnh | `**…**` · `*…*` | Bỏ ký hiệu, giữ chữ |

Lượt nói có đoạn văn được bọc trong `"…"` như Tập 01. Câu được cắt tại `. ? ! …` (kể cả `.”`) khi theo sau là chữ hoa. Cue nằm giữa lượt nói cắt lượt thành 2 phần tử cùng vai.

**Hai "Người bình thường" khác nhau** trong cùng tập phải được khai ở `N_ELEMENT` (A12) để có hình và giọng riêng (N1, N2).

### A2b. Bản ngôn ngữ — tiếng Anh, tiếng Hàn, tiếng Nhật

Ngoài bản tiếng Việt (nguồn chuẩn), mỗi tập có thể có các **bản ngôn ngữ**. Bản ngôn ngữ là **bản dịch theo ngôn ngữ**, không phải bản rút gọn: nó phải giữ nguyên cấu trúc để chạy lại đúng pipeline.

| Bản | Thư mục kịch bản | Chuẩn riêng | Lệnh pipeline |
|---|---|---|---|
| EN | `01_KICH_BAN/TapXX_EN/kichban_tapXX_EN.md` | `02_SAN_XUAT/Tap02_EN/CHU_CO_DINH_EN.md` | `$env:AE_LANG='en'; $env:AE_EP='XX'` |
| KO | `01_KICH_BAN/TapXX_KO/kichban_tapXX_KO.md` | **`00_TIEU_CHUAN/CHU_CO_DINH_KO.md`** | `$env:AE_LANG='ko'; $env:AE_EP='XX'` |
| JA | `01_KICH_BAN/TapXX_JA/kichban_tapXX_JA.md` | (theo bản JA) | `$env:AE_LANG='ja'; $env:AE_EP='XX'` |

**Bốn điều tuyệt đối không được phá vỡ** khi dịch (chung cho mọi bản ngôn ngữ):

1. **Số hồi** giữ nguyên (`## HỒI N` / `## ACT N` / `## 막 N` / `## 第N幕`) và thứ tự element trong hồi giữ nguyên.
2. **Vai** giữ nguyên — mỗi lượt nói phải là một vai (H/D/C/N), không gộp, không tách.
3. **Số câu** trong mỗi lượt nói giữ nguyên (QC đếm từng câu).
4. **Số giây nghỉ** giữ nguyên.

**Cách đổi nhãn theo ngôn ngữ** (parser chấp nhận cả hai dạng):

| Nhãn VN | Nhãn EN | Nhãn KO | Nhãn JA |
|---|---|---|---|
| `## HỒI N:` | `## ACT N:` | `## 막 N:` | `## 第N幕` |
| `**[Nghỉ X giây]**` | `**[Pause X seconds]**` | `**[정지 X초]**` | `**[休止 X秒]**` |
| `HOST` | `HOST` | `호스트` | `ホスト` |
| `ĐIỀU TRA VIÊN` | `INVESTIGATOR` | `수사관` | `捜査官` |
| `CHUYÊN GIA TÂM LÝ` | `PSYCHOLOGIST` | `심리학자` | `心理学者` |
| `NGƯỜI BÌNH THƯỜNG` | `ORDINARY PERSON` | `일반인` | `一般人` |
| `ĐẶC VỤ FBI` | `FBI AGENT` | `연방수사국` | `FBI特別捜査官` |
| `CẢNH SÁT ĐỊA PHƯƠNG` | `LOCAL POLICE` | `지역경찰` | `地方警察` |

`**[BGM]:**` và `**[SFX]:**` **giữ nguyên tiếng Anh** ở mọi bản — bộ dựng video khớp theo nhãn này.

**Vài bẫy riêng khi dịch:**
- Dấu `:` trong tiếng Việt nối hai mệnh đề **trong một câu** — bản dịch phải giữ dấu `:` (đổi thành `.` sẽ sinh thêm câu và làm lệch QC).
- Dấu `…` / `...` giữa câu → dùng ` – ` (sau dấu chấm lửng mà có Hangul, parser sẽ cắt sai câu).
- Trích dẫn nguyên văn (tiếng Anh) giữ **nguyên tiếng Anh** trong `‘…’`, phần giải nghĩa tiếng Hàn đặt **trước** và nối bằng ` – `.
- Tên riêng / địa danh giữ **chữ Latin** (không chuyển sang Hán tự); số viết bằng **chữ số Ả Rập**; lời đọc chỉ dùng **Hangul + Latin + số**, không dùng chữ Hán.
- `tts_sentences.py` chỉ đổi số thành chữ cho bản **tiếng Việt** (G11) — bản EN/KO/JA giữ nguyên chữ số.

**QC bản KO:** `py -3 .work/_qc_ko_parity.py <file_vn.md> <file_ko.md>` — phải in `PASS` (đối chiếu hồi, thứ tự element, vai, số câu, số giây nghỉ, mọi con số, tên riêng, tỉ lệ Hangul). Chạy cả 29 tập: `py -3 .work/_qc_ko_all.py`.

### A2c. Hệ sinh thái phân tích tâm lý tội phạm — Bộ 10 chỉ dấu chiều sâu kịch bản

Kênh **Amber eyes** định vị là *phân tích tâm lý tội phạm qua những hồ sơ có thật*, **tuyệt đối không phải là bản tin thời sự, phóng sự điều tra hay bản tóm tắt pháp đình thuần túy**. Một kịch bản chỉ kể diễn biến vụ án, quá trình khám nghiệm và kết quả tuyên án là **CHƯA ĐẠT**.

Mọi kịch bản (bản tiếng Việt gốc và các bản dịch ngôn ngữ EN/JA/KO) **BẮT BUỘC** phải vận dụng **Hệ sinh thái 10 chỉ dấu tâm lý & hành vi** được chia thành 2 nhóm:
- **Nhóm I: 5 Trụ cột tâm lý cốt lõi** (Định vị chiều sâu nhân văn, đạo đức và tác động xã hội).
- **Nhóm II: 5 Yếu tố khoa học hành vi bổ trợ** (Giải mã cơ chế phát triển tội ác, dấu ấn tâm thần học và giá trị thức tỉnh thực tiễn).

---

#### 1. Nhóm I: 5 Trụ cột tâm lý cốt lõi

| # | Trụ cột | Bản chất & Chiều sâu cần khai thác | Vị trí khuyến nghị trong 5 hồi |
|---|---|---|---|
| 1 | **Ảnh hưởng xã hội & Sự quan tâm của dư luận** | - **Chấn thương tập thể & hoang tưởng xã hội (Collective Trauma & Paranoia):** Cảm giác an toàn bị phá vỡ; người dân hoảng loạn, mua súng, khóa cửa, nghi kỵ lẫn nhau.<br>- **Cơn sốt truyền thông (Media Frenzy):** Xã hội theo dõi, chia rẽ hoặc phẫn nộ tột cùng trước tội ác.<br>- **Khủng hoảng niềm tin & Cải cách thể chế (Institutional Betrayal & Reform):** Sự rạn nứt uy tín của quân đội, cảnh sát, cơ quan quản lý; những cải cách quy trình, điều luật hoặc tiền lệ tư pháp lịch sử sau vụ án. | **Hồi 1** (thiết lập tầm vóc và sức nặng vụ án) & **Hồi 5** (đúc kết di chứng xã hội). |
| 2 | **Góc nhìn của hung thủ về nạn nhân & Lý do** | - **Vật hóa & Phi nhân hóa (Objectification & Dehumanization):** Nạn nhân không được nhìn nhận như con người có tri giác và gia đình, mà bị giáng cấp thành "đạo cụ" (props), "dự án" (projects), hoặc "công cụ cung cấp sự thỏa mãn ái kỷ" (narcissistic supply).<br>- **Lý do gốc rễ (The Why):** Sự thiếu hụt thấu cảm cảm xúc (Affective Empathy Deficit), khuyết tật Thuyết tâm trí (Theory of Mind), ảo tưởng đặc quyền săn mồi (predatory entitlement). Tiếng khóc van xin không gây trắc ẩn mà kích hoạt sự hưng phấn quyền lực (power arousal). | **Hồi 2** (hành vi hiện trường) & **Hồi 3** (giải phẫu tâm lý). |
| 3 | **Góc nhìn của hung thủ về người thân & Nghịch lý chia ngăn** | - **Cơ chế Chia ngăn nhận thức (Compartmentalization):** Bộ não tội phạm hai mặt khóa chặt "ngăn gia đình bình thường" và "ngăn bóng tối săn mồi" thành hai thế giới riêng biệt không giao thoa.<br>- **Gia đình là "Lá chắn bình thường hóa" (Shield of Normalcy):** Dùng gia đình để tự thuyết phục mình vẫn là người tốt, hoặc coi người thân là tài sản danh dự cần bảo vệ quyền sở hữu.<br>- **Bi kịch của nạn nhân thứ hai:** Người thân (vợ, con, cha mẹ) bị sụp đổ toàn bộ danh tính khi sự thật bại lộ; nỗi sợ mất mặt trước người thân thường lớn hơn nỗi sợ tòa án. | **Hồi 3** (giải phẫu động cơ) & **Hồi 4** (sự sụp đổ phòng thẩm vấn khi đối diện gia đình). |
| 4 | **Thái độ của hung thủ trước bản án nhận được** | - **Hối hận giả tạo vs. Tự thương hại bệnh lý (False Remorse vs. Pathological Self-Pity):** Kẻ ái kỷ/thái nhân cách không khóc vì xót thương nạn nhân, mà khóc vì tiếc thương danh vọng, tự do và đặc quyền của chính mình đã tan vỡ (narcissistic collapse).<br>- **Phản ứng trước sự trừng phạt:** Có kẻ ngoan cố chối tội, coi mình là nạn nhân của tư pháp, thách thức đến phút chót; có kẻ tìm cách tự sát hoặc sụp đổ hoàn toàn khi mất quyền kiểm soát.<br>- **Bản án tâm lý:** Tòa án trừng phạt thể xác, nhưng bản án tâm lý phơi bày sự trơ tráo, trống rỗng tột cùng của nhân cách. | **Hồi 5** (Phán quyết & Lời kết). |
| 5 | **Hệ thống tự bào chữa & Cơ chế trung hòa đạo đức** | - **Kỹ thuật Trung hòa đạo đức (Techniques of Neutralization) & Ngắt kết nối đạo đức (Moral Disengagement):** Cách hung thủ tự lừa dối để vô hiệu hóa lương tri và ngủ ngon mỗi đêm:<br>  + *Đổ lỗi cho nạn nhân (Victim Blaming):* "Cô ta bất cẩn", "Cậu ta vốn muốn chết".<br>  + *Ngoại hóa trách nhiệm (Displacement of Responsibility):* "Do quỷ dữ/Factor X bên trong ép tôi", "Do cấp dưới làm".<br>  + *Giảm thiểu tổn hại (Minimization):* "Tôi chỉ xem trộm thôi", "Tôi chỉ giúp giải thoát".<br>  + *Tự khoác áo thiên thần (Hero Complex):* Đóng vai người mẹ tận tụy, người cứu rỗi.<br>  + *Cưỡng chế hoàn cảnh:* "Cô ta thấy mặt tôi rồi nên ép tôi phải ra tay để tự vệ". | **Hồi 3** (cơ chế nhận thức) & **Hồi 4** (lời khai bào chữa khi đối chất). |

---

#### 2. Nhóm II: 5 Yếu tố khoa học hành vi bổ trợ

| # | Yếu tố hành vi | Bản chất & Chiều sâu cần khai thác | Vị trí khuyến nghị trong 5 hồi |
|---|---|---|---|
| 6 | **Ngòi nổ & Điểm gãy tâm lý (Precipitating Stressor & Tipping Point)** | - **Biến cố kích hoạt (Trigger):** Vì sao tội ác bùng phát vào đúng thời điểm đó? Giọt nước nào làm tràn ly?<br>- Khủng hoảng sự nghiệp, đổ vỡ tình cảm, mất quyền kiểm soát, sự sỉ nhục cái tôi, hoặc áp lực thăng tiến vượt ngưỡng chịu đựng đã đánh sập cơ chế ức chế hành vi. | **Hồi 1** (bối cảnh dẫn nhập) & **Hồi 2** (mốc bắt đầu chuỗi hành vi). |
| 7 | **Dấu ấn tâm lý ("Chữ ký") vs. Thủ đoạn gây án (Signature vs. Modus Operandi)** | - **Thủ đoạn (Modus Operandi - MO):** Cách thức hung thủ làm để gây án và tẩu thoát (găng tay, chọn ban đêm, cắt liên lạc); MO liên tục thay đổi và tiến hóa theo kinh nghiệm.<br>- **Chữ ký tâm lý (Signature):** Hành vi không nhằm phục vụ mục đích trốn thoát, mà để thỏa mãn nhu cầu cảm xúc bệnh lý (chụp ảnh chiến lợi phẩm, các nút thắt dây trói kỳ quặc, trang phục, gửi thư trêu ngươi). Signature là "vân tay linh hồn", không bao giờ thay đổi. | **Hồi 2** (phân tích hiện trường) & **Hồi 3** (giải mã động cơ). |
| 8 | **Chu kỳ ảo tưởng & Quỹ đạo leo thang (Fantasy Addiction & Escalation Cycle)** | - **Cơ chế dung nạp kích thích (Tolerance Buildup):** Tội ác không xuất hiện tức thì mà leo thang như một cơn nghiện. Hành vi ban đầu (nhìn trộm, lấy trộm vặt, nói dối bệnh lý) chỉ thỏa mãn tạm thời.<br>- Khi não bộ quen liều, hung thủ rơi vào "đói ảo tưởng" (fantasy starvation) và buộc phải nâng ngưỡng liều: từ rình mò $\rightarrow$ đột nhập $\rightarrow$ khống chế $\rightarrow$ hủy diệt mạng sống. | **Hồi 2** (diễn biến leo thang) & **Hồi 3** (quy luật tâm lý học). |
| 9 | **Hiệu ứng Hào quang & Điểm mù xã hội (Halo Effect & Collective Blindspots)** | - **Hiệu ứng Hào quang (Halo Effect):** Xã hội đánh đồng "Thành đạt/Lịch thiệp/Đạo mạo = Người tốt". Quân phục đại tá, chức danh chủ tịch nhà thờ, danh xưng chính trị gia hay bộ mặt người mẹ hiền trở thành tấm khiên tàng hình hoàn hảo.<br>- **Thành kiến bình thường hóa (Normalcy Bias):** Người xung quanh vô thức lờ đi các dấu hiệu kỳ quặc vì não bộ từ chối tin vào điều kinh hoàng nhất. | **Hồi 1** (vỏ bọc ban đầu) & **Hồi 4** (sự bàng hoàng khi sự thật phơi bày). |
| 10 | **Nạn nhân học & Tín hiệu cảnh báo đỏ sinh tồn (Victimology & Survival Red Flags)** | - **Nạn nhân học (Victimology):** Phân tích sự bất đối xứng quyền lực và tiêu chí chọn mồi của kẻ săn mồi (sự cô lập xã hội, phụ thuộc cảm xúc, tổn thương tâm lý sẵn có). Tuyệt đối không đổ lỗi nạn nhân; luôn tôn vinh phẩm giá, nỗ lực phản kháng và nhân vị trọn vẹn của nạn nhân.<br>- **Bài học sinh tồn (The Gift of Fear):** Cung cấp giá trị thực tiễn cho người xem: cách lắng nghe trực giác bất an, nhận diện các vi tín hiệu thao túng (phá vỡ ranh giới, làm thân dồn dập, đóng vai nạn nhân, kiểm soát đội lốt chăm sóc). | **Hồi 2** (chân dung nạn nhân) & **Hồi 5** (bài học cảnh giác đời thực). |

---

#### 3. Phân vai thể hiện Hệ sinh thái 10 chỉ dấu
- **Host (Cú - Trầm ấm, sâu sắc):** Nêu bật bối cảnh chấn động xã hội (1), hiệu ứng hào quang đánh lừa dư luận (9), dẫn dắt các nghịch lý đạo đức, và đúc kết bài học cảnh tỉnh sinh tồn/trực giác cho khán giả (10) ở đầu và cuối tập.
- **Điều tra viên (Sói - Lạnh lùng, chuẩn xác):** Phân tích rạch ròi giữa thủ đoạn MO và chữ ký Signature (7), ngòi nổ kích hoạt (6), hồ sơ thẩm vấn, phản ứng thực tế của hung thủ với người thân (3), thái độ trước búa tòa (4) và các phát ngôn tự bào chữa nguyên văn (5).
- **Chuyên gia tâm lý (Cáo - Nhấn mạnh, học thuật):** Bóc trần cơ chế chia ngăn nhận thức (3), quá trình leo thang dung nạp ảo tưởng (8), sự vật hóa và khuyết tật thấu cảm đối với nạn nhân (2), kỹ thuật trung hòa đạo đức (5) và sự sụp đổ của bản ngã ái kỷ (4).

---

#### 4. Cổng kiểm kịch bản (Checklist 10 chỉ dấu trước khi duyệt sản xuất)
Trước khi chuyển sang bước Diễn xuất (Bước 1b), biên kịch và AI **PHẢI** đối soát và trả lời được 10 câu hỏi:
- [ ] 1. **Dư chấn xã hội:** Đã làm rõ vụ án gây chấn động, hoang tưởng tập thể hoặc thúc đẩy cải cách thể chế/luật pháp nào chưa?
- [ ] 2. **Góc nhìn về nạn nhân:** Đã bóc trần hung thủ xem nạn nhân là gì (đạo cụ/dự án) và lý giải gốc rễ thiếu hụt thấu cảm chưa?
- [ ] 3. **Góc nhìn về người thân:** Đã mổ xẻ cơ chế chia ngăn nhận thức và bi kịch sụp đổ danh tính của người thân chưa?
- [ ] 4. **Thái độ trước bản án:** Đã phân biệt đúng sự hối hận giả tạo/tự thương hại bản thân so với sự ăn năn chân chính chưa?
- [ ] 5. **Hệ thống tự bào chữa:** Đã vạch trần các lý lẽ trung hòa đạo đức (đổ lỗi nạn nhân, ngoại hóa trách nhiệm) hung thủ dùng để ru ngủ lương tri chưa?
- [ ] 6. **Ngòi nổ tâm lý:** Đã chỉ ra biến cố kích hoạt (giọt nước tràn ly) khiến tội ác bùng phát vào đúng thời điểm đó chưa?
- [ ] 7. **Chữ ký vs. Thủ đoạn:** Đã tách bạch giữa phương thức tẩu thoát (MO) và dấu ấn thỏa mãn nhu cầu cảm xúc bệnh lý (Signature) chưa?
- [ ] 8. **Quỹ đạo leo thang:** Đã cho thấy chu kỳ phát triển của tội ác từ những hành vi xâm lấn ranh giới nhỏ ban đầu chưa?
- [ ] 9. **Hiệu ứng hào quang:** Đã lý giải tại sao vỏ bọc đạo mạo/thành đạt lại tạo ra điểm mù che mắt cộng đồng suốt thời gian dài chưa?
- [ ] 10. **Nạn nhân học & Bài học sinh tồn:** Đã trả lại nhân phẩm cho nạn nhân và đúc kết những tín hiệu cảnh báo đỏ (Red Flags) thực tiễn cho người xem chưa?

## A3. Quy trình chuẩn — lệnh chạy và thời gian đo được

Chạy từ `D:\TEST\Gax\Audi`, đặt `PYTHONIOENCODING=utf-8`. Connector gọi qua `mcode-tools` (có sẵn tại `C:\Users\ADMIN\.minimax\bin`).

| Bước | Lệnh | Đầu ra | Thời gian Tập 01 |
|---|---|---|---|
| **0. Một lần cho series** | `make_logo.py` · `make_intro.py` · `make_cast_cutouts.py` · `voice_audition.py` | Logo, intro, 5 linh thú, chọn giọng | đã xong |
| **1. Tách kịch bản** | `py -3 .work/parse_kichban.py 01_KICH_BAN/TapXX/kichban_tapXX.md .work/script_tapXX.json` | lượt nói, câu | < 1 s |
| **1b. Diễn xuất** | `py -3 .work/make_acting_tapXX.py` (theo G1–G8 của A4.2) | `.work/acting_tapXX.json` | < 1 s |
| **2. Đọc giọng** | `py -3 .work/tts_sentences.py` (số tự đổi sang chữ — G11) | `.work/audio_s_tXX/*.mp3` | Tập 02: 215 câu / ~12 phút |
| **2b. Nghe theo vai (G10)** | `py -3 .work/voice_role_check.py` — **không đạt thì dừng** | `<EP_DIR>/thu_giong_kiem_vai/report.md` | ~3 phút |
| **3. Âm thanh tổng** | `py -3 .work/build_audio3.py` | `TapXX_master.mp3`, `timeline_s_tXX.json`, `stems_tXX/` | Tập 02 (stereo, nền dài): ~12 phút |
| **4. Kiểm tra âm thanh** | lệnh A9.1 | — | 1 phút |
| **5. Nền mới (nếu cần)** | `py -3 .work/gen_images.py .work/bg_jobs_tapXX.json` | `assets/bg/*.png` | ~1 phút / ảnh |
| **6. Bảng shot** | AI viết mục 6 của hồ sơ tập → `py -3 .work/parse_shots.py` | `.work/shots.json` | < 1 s |
| **6b. Cổng nền dùng chung mọi ngôn ngữ** | chạy **sau `parse_shots.py` của mọi ngôn ngữ, trước ảnh tĩnh**: `py -3 .work/qc_bg_shared.py --ep XX` — bộ nền **và nền từng shot** trùng mọi ngôn ngữ, mọi nền có file, 0 file có hậu tố ngôn ngữ (A8.1) | — | < 1 s |
| **7. Kiểm tra chữ** | lệnh A9.2 | — | < 1 s |
| **8. Ảnh tĩnh duyệt — MỌI shot** | `py -3 .work/build_video3.py --stills <giữa mỗi shot>`; ghép 16 ảnh/tờ để soi (A9.3) | `.work/video3_tXX/stills/` | Tập 01: 151 ảnh / ~2 phút · **Tập 08 × 3 ngôn ngữ: 223×3 ảnh / ~5 phút** (đo 09/11) |
| **9. Dựng hình** | `py -3 .work/build_video3.py --workers 6` | `.work/video3_tXX/picture.mp4` | Tập 01: 1.133 s / ~22 phút · Tập 02: 1.604 s / **~85 phút** |
| **10. Sửa cục bộ** | `py -3 .work/rerender_part.py K` (K = 0…5) | dựng lại 1/6 tập rồi ghép | ~5 phút / phần |
| **11. Phụ đề** | `py -3 .work/subtitles.py` | `TapXX.srt` | < 1 s |
| **12. Đóng gói** | `py -3 .work/package.py --mux` | `.mp4`, thumbnail, mô tả, nguồn | 1 phút |

**Chọn tập (từ 22/10/2026):** đặt `AE_EP=02` (03…) trước mọi lệnh. Mọi thông số riêng của tập — kịch bản, thư mục, N1/N2, file diễn xuất, bảng âm thanh, mốc nhạc, cảnh ghép, tên hồi, câu cần nguồn — khai **một chỗ** trong `EPISODES` của `.work/edition.py`. File trung gian của tập ≠ 01 có hậu tố `_tXX` nên không ghi đè tập khác. Không có `AE_EP` = Tập 01 như cũ.

**Bản ngôn ngữ khác (từ 22/10/2026):** đặt `AE_LANG=en` trước mọi lệnh trên để chạy bản tiếng Anh.
- Đường dẫn, giọng và chữ giao diện nằm trong `.work/edition.py`. Mọi đầu ra có hậu tố `_EN` hoặc nằm trong `02_SAN_XUAT/TapXX_EN/`.
- Bảng shot EN được sinh từ bảng VN bằng `.work/_build_plan_en.py`: giữ cột Câu, Vai, Mẫu, Nền và lời mô tả beat tiếng Việt (renderer dò từ khoá tiếng Việt); chỉ thay chữ màn hình và cụm `ở "…"`.
- QC giọng toàn tập: `py -3 .work/qc_asr.py`.
- **Diễn xuất từng câu (chống đọc đều đều):** `.work/acting_EN.json`, mỗi câu gồm `[cảm xúc, độ lệch tốc độ, cao độ −12…12, lời đọc riêng]`.
  - Thẻ ngắt `<#0.4#>` được engine hiểu, không đọc thành chữ.
  - Quy tắc tự động: `...` nghỉ 0,45 s · ` — ` nghỉ 0,15 s · `: ` trước chữ hoa nghỉ 0,3 s.
  - Sau câu buồn hoặc căng thẳng nghỉ thêm 0,2 s.
- **SFX theo shot:** `.work/make_sfx2.py` (25 âm tự tổng hợp) cộng `.work/sfx_shots_EN.json` (shot, file, mốc, lệch, dB).
  - Cần chạy 2 lượt: `build_audio3` → `parse_shots` → `build_audio3`.
- Mẫu đầu tiên: `02_SAN_XUAT/Tap01_EN/README.md`.
| **13. Kiểm tra cuối** | lệnh A9.3 + A9.4 | — | ~5 phút |

**Tính phần cần dựng lại (bước 10):** `bước = ceil(tổng_khung / 6)`; khung = `giây × 30`; phần = `khung // bước`. Ví dụ Tập 01: bước 5.668 khung ≈ 188,9 s → giây 829 thuộc **phần 4**. *(Tập 01 từng tính nhầm thành phần 3 — luôn tính bằng công thức.)*

Mọi lệnh đặt `AE_EP=XX` trước (PowerShell: `$env:AE_EP="02"`); Tập 01 không cần.

**Mốc duyệt với người dùng** (người dùng có thể bỏ qua): sau bước 2b (nghe giọng theo vai), sau bước 8 (ảnh tĩnh mọi shot), sau bước 13 (video cuối).

## A4. Âm thanh chuẩn

### A4.1 Năm giọng — BỘ A (chốt 23/10/2026, dùng từ Tập 02)

Ba vai chính phải **khác hẳn nhau** về chất giọng:

| Nhân vật | Chất giọng yêu cầu | `voice_id` | `speed` gốc | F0 đo | **CER đo (T2, 20 câu)** | Kiểm |
|---|---|---|---:|---:|---:|---|
| Cú · Host | **Trầm ấm**, gần, kiểu podcast đêm | `English_CaptivatingStoryteller` | 0,90 | 102,6 Hz | **0,1%** · 0/20 vượt ngưỡng | Hợp vai 9/10 · ổn định 4 cảm xúc → 1 người |
| Sói · Điều tra viên | **Lạnh lùng**, phẳng, chính xác | `Korean_ColdYoungMan` | 0,95 | 140 Hz | **3,1%** · max **28,6%** ⚠ | 8,5/10 · ổn định → 1 người |
| Cáo · Chuyên gia | **Nhấn mạnh**, chín chắn, phân tích (nữ) | `English_AssertiveQueen` | 0,92 | 207,8 Hz | 0,9% | 8,5/10 · ổn định → 1 người |
| Cừu · N1 | Nữ trẻ, hiền | `Vietnamese_kindhearted_girl` | 0,95 | 248,1 Hz | 0,0% | |
| Mèo · N2 | Nữ, tò mò | `English_captivating_female1` | 0,95 | 230,3 Hz | 0,0% | |

- **Ba bộ giọng của kênh.** Bản VN dùng **bộ A** (trên). Bản EN dùng bộ riêng: `English_magnetic_voiced_man` 0,95 · `English_Trustworth_Man` 0,97 · `English_Wiselady` 0,95 · `English_SentimentalLady` 0,95 · `English_captivating_female1` 0,95. **Tập 01 ghim bộ riêng** (`audiobook_male_1` 0,90 · `male-qn-qingse` 0,95 · `audiobook_female_1` 0,92) để dựng lại ra đúng bản đã xuất.
- Khai ở `edition.py`: `CAST` (mặc định bản VN) · `EPISODES["01"]["cast"]` (ghim Tập 01). **Code KHÔNG gọi `get_voice_list`** — `CAST` là hardcode.
- Hồ sơ đầy đủ: `02_SAN_XUAT/Tap02/BaoCao_GiongDoc_Tap02.md` §4. File nghe: `02_SAN_XUAT/Tap02/thu_giong_vai/`.
- **Ba vai chính nghe mù xen kẽ (Tập 07):** gán đúng S1/S2/S3, tách bạch **10/10**.

**Vì sao bỏ bộ cũ** (phản hồi người dùng về Tập 02: "Host nghe như 3 người", "giọng nam giống hệt nhau"):
- `audiobook_male_1` **đổi danh tính** mỗi khi đổi cảm xúc hoặc cao độ: 7 thiết lập → 6 "người".
- Hai giọng nam cùng baritone miền Nam, chỉ cách nhau ~2 nửa cung.

**Giọng đã thử và loại:**
- Điểm hợp vai cao nhưng **không ổn định**: `English_Deep-VoicedGentleman` (4 người), `English_ReservedYoungMan` (3), `English_MatureBoss` (2), `Korean_IntellectualMan` (2).
- Đổi người giữa 2 câu neutral: `English_ConfidentWoman`, `English_Wiselady`.
- Sai thanh điệu: `Chinese (Mandarin)_News_Anchor`.

**Kho giọng chỉ có MỘT giọng tiếng Việt gốc** (`Vietnamese_kindhearted_girl`, nữ) — chỉ đọc cho vai N1, chiếm **2% số câu**. 3 vai chính đọc tiếng Việt bằng giọng `English_`/`Korean_`: **giọng hệ thống MiniMax đa ngôn ngữ** — tiền tố là ngôn ngữ *gốc* của giọng, KHÔNG giới hạn ngôn ngữ đầu vào (endpoint TTS không có tham số `language`; engine tự nhận diện ngôn ngữ từ văn bản). Đổi giọng ở tập sau thì phải qua đủ **G8–G10 + G12**.

### A4.1b ĐO CHẤT LƯỢNG PHÁT ÂM TIẾNG VIỆT — CER (đo 27/10/2026, Tập 02)

**Vì sao phải có mục này:** G8–G10 đo **danh tính** và **tách bạch** của giọng, nhưng **không đo giọng đọc tiếng Việt có đúng không**. Đo 27/10 mới phát hiện `Korean_ColdYoungMan` (vai Điều tra viên) đọc tiếng Việt **sai thanh điệu nặng**: *"Thứ hắn lấy đi"* → nghe ra *"Thương hiệu Han Lady"* (3 lượt ASR khác nhau, đều sai) → CER 28%.

### Cách đo (tái lập được)

| Bước | Cách làm |
|---|---|
| Mẫu | 20 câu của **đúng vai đó**, dùng **đúng `emotion` + `speed` của production** (đọc từ `tts_manifest_t02.json`) |
| Chuẩn | Trường `text` của manifest — đúng thứ đã gửi cho engine |
| ASR | `connector__matrix__listen_audio` + hàm `cer()` sẵn có trong `.work/voice_audition.py` |
| ⚠ Chuẩn hoá | **Áp `vi_numbers()` cho CẢ HAI Vế.** Chuẩn là CHỮ (`"tám mươi tám"`), ASR trả SỐ (`"88"`) — không chuẩn hoá thì CER phình to giả (một câu đúng bị tính **21%**, một câu **300%**) |
| ⚠ Lọc lỗi | Câu bị **bộ lọc Gemini chặn** (nội dung nhạy cảm) → `transcription` dính đuôi *"This request was blocked…"* mà `code` vẫn `0`. Cắt đuôi + **loại câu khỏi mẫu** |
| Mẫu nhỏ | Câu < 12 từ → 1 lỗi = 20%+ CER. Tách riêng khi báo cáo |
| Lặp lại | ASR **không tất định**: 3/9 câu vượt ngưỡng đổi kết quả giữa 2 lượt ⇒ **≥ 2 lượt** cho mọi kết luận về 1 câu |
| Tiết kiệm | Nếu audio TTS **đã xuất** → đo thẳng trên file thành phẩm, **không cần tổng hợp lại** |

### Kết quả — 3 vai, cùng 20 câu, audio thành phẩm Tập 02

| Vai | `voice_id` | CER tb | median | max | >2% | F0 | cách Host |
|---|---|---:|---:|---:|---:|---:|---:|
| Host | `English_CaptivatingStoryteller` | **0,1%** | 0,0% | 2,0% | **0/20** | 103 Hz | — |
| **Điều tra viên** | **`Korean_ColdYoungMan`** | **3,1%** | 0,0% | **28,6%** | 4/20 | 140 Hz | +5,4 nc |
| Chuyên gia | `English_AssertiveQueen` | 0,9% | 0,0% | 5,4% | 4/20 | 203 Hz | +9,4 nc |

### Kết quả — 5 ứng viên thay vai Điều tra viên (cùng 20 câu)

| `voice_id` | CER tb | max | F0 | cách Host | dao động F0 | G8 | G9 | trong catalog |
|---|---:|---:|---:|---:|---:|---|---|---|
| **`English_Diligent_Man`** | **0,6%** | 6,0% | 158 Hz | **+7,7 nc** | 55 Hz | ✅ 1 | 9/10 | ✅ |
| `male-qn-qingse` | 0,6% | 9,5% | 137 Hz | +5,0 nc | 44 Hz | ✅ 1 | **10/10** | ❌ *nhưng còn sống* |
| `English_DecentYoungMan` | 0,6% | 4,0% | 128 Hz | **+3,8 nc ✗** | 75 Hz | ✅ 1 | **10/10** | ✅ |
| `Korean_CockyGuy` | 1,6% | 20,0% | 152 Hz | +6,8 nc | 76 Hz | ✅ 1 | 9/10 | ✅ |
| `Korean_ColdYoungMan` *(đang dùng)* | 3,1% | 28,6% | 140 Hz | +5,4 nc | **17 Hz** | — | 8–9/10 | ✅ |

- **G8/G9 đo bằng `audios_understand` mù** (đúng cách `voice_role_check.py`): G8 = gộp 12 câu của 1 giọng → "SPEAKERS: n" (đạt = 1). G9 = xen kẽ Host · D · C (12 câu) → "SPEAKERS: n" + rating tách bạch 1–10.
- **Giọng đang dùng bị chấm thấp nhất về tách bạch (8–9/10)**: *"cả ba chia sẻ cùng một nhịp đọc tin không cảm xúc"*. Cả 3 vai đều là giọng Hàn Quốc/English.
- **`audiobook_male_1`** loại: F0 116 Hz chỉ cách Host **+2,0 nc** (G9 fail) + đã biết đổi danh tính khi đổi cảm xúc.
- **`English_DecentYoungMan`** loại: F0 128 Hz → chỉ **+3,8 nc** (< 4 của G9).
- **Kiểm tra sống của giọng legacy** (không có trong danh mục 332): `male-qn-qingse` ✅ · `audiobook_male_1` ✅ (27/10/2026, gọi TTS thật). **Vắng mặt trong danh mục ≠ chết.**
- **Phạm vi áp dụng**: Tập 03–07 đã có master (đã xuất) · **Tập 08–29 chưa có master** → đổi giọng vai D từ Tập 08 **không tốn dựng lại video nào đã xuất**.

Báo cáo đầy đủ: `90_LUU_TRU/BaoCao_SangLocGiongDieuTraVien_20261027.md` · đo bộ A: `90_LUU_TRU/BaoCao_CER_GiongBoA_Tap02_20261027.md`.

### A4.2 Diễn xuất từng câu — BẮT BUỘC từ Tập 02

**Vì sao:** khán giả Tập 01 phản hồi "mọi giọng đều đều, không điểm nhấn, nghe buồn ngủ". Đo lại Tập 01: Sói và Cáo đọc 100% câu `neutral`, cao độ giữa các câu chỉ lệch ~0,85 nửa cung, 3,5–3,8 âm tiết/giây. Nguyên nhân: cảm xúc chỉ đổi theo **cả lượt nói** (bảng từ khoá A4.2b), mọi câu trong lượt đọc y hệt nhau.

**Cách làm:** mỗi tập có `.work/make_acting_tapXX.py` → `.work/acting_tapXX.json`, khai ở `EPISODES[..]["acting"]` trong `edition.py`. Mỗi câu: `[cảm xúc, lệch tốc độ, cao độ, lời đọc riêng | null]`, cộng `_pause_after` (giây nghỉ thêm **sau** câu). `tts_sentences.py` đọc file này; `build_audio3.py` cộng `_pause_after` vào khoảng nghỉ.

**Quy tắc (rút từ 3 vòng thử, 74 bản đọc, 23/10/2026 — `02_SAN_XUAT/Tap02/AmThanh_Tap02.md` §2.4):**

| # | Quy tắc | Giá trị | Bằng chứng |
|---|---|---|---|
| G1 | **Không đặt `...` hay thẻ ngắt `<#s#>` giữa câu.** Tiếng Việt có thanh điệu: ngắt giữa câu làm ngữ điệu vụn, "như robot" | Duy nhất: **một** thẻ `<#0.35#>` sau dấu `:` đứng trước câu trích “…” | Có ngắt giữa câu: nhịp 3–4/10, thắng 2/7 câu. Không ngắt: nhịp 5–6/10, thắng 7/7 |
| G2 | **Kịch tính đặt GIỮA các câu**, không trong câu | `_pause_after` 0,2–1,2 s sau câu hé lộ, câu "đóng đinh", cuối nấc thang | Tập 02: 70 chỗ, 27 s |
| G3 | **Cảm xúc đổi theo nhịp truyện**, không theo lượt — **chỉ trong bộ cảm xúc an toàn của giọng (G8)** | Dẫn chuyện `neutral` → căng `fearful` → hé lộ `surprised` → lắng `sad`; câu hỏi `surprised`. Bộ A: chỉ `neutral · sad · fearful · surprised` | Tập 02 (bản sửa): neutral 160 · sad 28 · fearful 14 · surprised 13 |
| G4 | **Tốc độ chỉ chậm vừa** | Lệch so với tốc độ gốc của vai trong **−0,06 … +0,02** | `sad`/`fearful` tự làm máy đọc chậm; cộng thêm −0,1 làm câu dài gấp đôi |
| G5 | **Cao độ = 0** (sửa 23/10; bản cũ −4…+3 gây lỗi "Host thành 3 người") | Không dùng tham số `pitch`. Biểu cảm lấy từ cảm xúc an toàn, tốc độ, khoảng lặng, nhạc, tiếng động | `audiobook_male_1`: cao độ +1 → F0 +4,5 nửa cung **và đổi người**; −1/−2 → đổi sang giọng miền Bắc khàn |
| G6 | **Lời đọc riêng chỉ để sửa cách đọc, không đổi chữ** | Phụ đề và chữ trên hình luôn lấy câu gốc; lời đọc riêng dựng lại từ câu gốc, giữ nguyên dấu câu | Kiểm bằng script: so từng chữ (bỏ dấu câu và thẻ) với câu gốc |
| G7 | **Không để giọng Việt đọc tiếng Anh dài** | Bỏ chú thích tiếng Anh trong ngoặc khỏi lời đọc khi không cần (vd. `(Signature)`); câu trích tiếng Anh dịch sang tiếng Việt | |
| G8 | **Mỗi giọng có bộ tham số an toàn** — chỉ dùng thiết lập mà giọng vẫn là CÙNG MỘT NGƯỜI | Thử: cùng một câu × mọi cảm xúc/cao độ định dùng; ghép vào một file, hỏi `audios_understand` "mấy người?" → phải ra **1** | Bộ A: 4 cảm xúc → 1 người. Bị loại: Deep-VoicedGentleman 4 người, ReservedYoungMan 3… |
| G9 | **Các vai phải khác hẳn nhau** | Hai giọng cùng giới cách nhau **≥ 4 nửa cung** F0 trung vị và khác rõ chất giọng; file xen kẽ 3 vai × 2 câu, nghe mù phải gán **đúng 100%** | Bộ A: 6/6, tách bạch 9/10; nam–nam cách ~6 nửa cung |
| G10 | **Nghe liền theo vai trước khi dựng** | Sau khi đọc toàn tập: mỗi vai ghép 10–12 câu rải đều → nghe mù phải ra **1 người**; đạt mới chạy `build_audio3` | Lỗi Tập 02 lọt qua vì chỉ so các bản của CÙNG MỘT CÂU |
| G11 | **Số đọc bằng chữ tiếng Việt** (tự động) | `tts_sentences.vi_numbers()` đổi mọi chữ số trong LỜI ĐỌC sang chữ: "1.400" → "một nghìn bốn trăm" (dấu chấm giữa nhóm 3 số = dấu nghìn), "2009" → "hai nghìn không trăm lẻ chín", "21" → "hai mươi mốt", "Elizabeth II" → "Elizabeth Đệ nhị". Phụ đề và chữ trên hình giữ chữ số | Tập 02: giọng đa ngôn ngữ đọc "1.400" thành "một phẩy bốn trăm" (người dùng phát hiện) |

**Trước khi đọc toàn tập:** chạy `.work/voice_act_test_tapXX.py` cho 5–7 câu then chốt: bản cũ, bản diễn xuất, bản với giọng thay thế. Kiểm ba thứ:
- **CER** bằng `listen_audio`.
- **Thẻ ngắt có bị đọc thành tiếng không.**
- **Chấm so sánh** bằng `audios_understand`: ghép các bản của **cùng một câu** vào một file, hỏi về biểu cảm, nhịp, thanh điệu, độ hợp phim tài liệu.

Người dùng nghe file so sánh để chốt.

**Lưu ý khi đọc số đo:**
- CER "13%" thường do bộ nhận dạng viết số ("4 tiếng 40 phút"); kết quả "290%" là do bộ lọc của dịch vụ nhận dạng chặn. Phải đọc bản chép lại trước khi kết luận giọng sai.
- Dải cao độ **trong** câu tiếng Việt luôn rộng (11–15 nửa cung, do thanh điệu). Chỉ số "đều đều" thật là cao độ và tốc độ **giữa** các câu.

### A4.2b Chỉ dẫn → tham số TTS (cách cũ, chỉ dùng khi tập không có file diễn xuất)

`emotion` chỉ nhận `happy · sad · angry · fearful · disgusted · surprised · neutral`.

| Chỉ dẫn chứa | `emotion` | `speed` cộng thêm |
|---|---|---:|
| "xúc động" | `sad` | 0 |
| "Đẩy nhanh" | `neutral` | +0,04 |
| "sắc lạnh" · "đanh thép" | `neutral` | +0,02 |
| "trầm lắng" · "trăn trở" | `sad` | −0,02 |
| "Hạ giọng trầm, chậm rãi" | `neutral` | −0,04 |
| "trầm ấm" · "chậm, trầm" | `neutral` | −0,02 |
| (khác / không ghi) | `neutral` | 0 |

Lượt không có chỉ dẫn kế thừa lượt trước cùng vai, cùng hồi.

### A4.3 Khoảng ngắt

| Vị trí | Độ dài |
|---|---:|
| Giữa 2 câu cùng lượt | 0,35 s |
| Sau câu hỏi | 0,60 s |
| Đổi người nói | 0,70 s |
| `[Nghỉ X giây]` | X, tối đa 2,5 s (khoảng nghỉ thay cho khoảng ngắt) |
| Ranh giới hồi | 2,0 s |

### A4.3b Nhịp nghỉ giữa câu — CỔNG BẮT BUỘC khi tạo audio (07/11/2026, AGENTS A13)

Khoảng ngắt cố định ở bảng trên **không đủ**: chỉ 0,35 s giữa 2 câu cùng lượt ⇒ cả tập nghe "đọc nhanh, không chậm rãi" dù tốc độ đọc trong câu bình thường. Nhịp chậm rãi đến từ `_pause_after` của **file diễn xuất**, cộng thêm vào sau câu.

| Vị trí | `_pause_after` |
|---|---:|
| Câu nối ý tiếp theo (cùng lượt) | 0,3 s |
| Hết một đoạn ý, câu dài ≥ 120 ký tự | 0,4–0,5 s |
| Sau câu hé lộ / con số nặng / câu kết hồi | 0,6–0,9 s |
| Cuối lượt nói trước khi đổi vai | ≥ 0,4 s (cộng với 0,70 s đổi người) |

**Quy định:**
- **Mỗi ngôn ngữ một file diễn xuất có `_pause_after`**: `acting_tapXX.json` (VN) · `acting_tapXX_EN.json` · `acting_tapXX_JA.json` · `acting_tapXX_KO.json`. Bản JA/KO có cùng mã câu với VN ⇒ được lấy bảng nghỉ VN làm điểm xuất phát. **Thiếu file ⇒ DỪNG**: `build_audio3.py` không báo lỗi mà trộn với 0 khoảng nghỉ.
- **Mọi mã trong `_pause_after` phải tồn tại** trong `script_tapXX[_LANG].json`. Mã sót từ kịch bản cũ bị bỏ qua **im lặng** (Tập 06 EN: 21/162 mã sót).
- Sửa kịch bản / đổi mã câu ⇒ chuyển `_pause_after` **theo nội dung câu**, so số mục trước–sau. Kịch bản viết lại nhiều ⇒ bổ sung bằng `.work/_fix_pause_t06.py` (mẫu: chuyển theo nội dung rồi bổ sung 0,3/0,4 s đến khi dự đoán đạt cổng).
- Số mục thường **50–65% số câu** (T04 104, T05 100, T06 135 VN/JA · 141 EN). Đây là hệ quả — **cổng đo mới là chuẩn**.

**Cổng — `py -3 .work/qc_pause_gate.py`** (đặt `AE_EP`, `AE_LANG`):

| Lúc chạy | Lệnh | ĐẠT khi |
|---|---|---|
| **Trước** `build_audio3.py` | `qc_pause_gate.py --pre` | Có file diễn xuất đúng ngôn ngữ · 0 mã lạ · mọi giá trị 0,2–1,2 s |
| **Sau** `build_audio3.py`, trước `parse_shots.py` | `qc_pause_gate.py` | **Trung vị nghỉ giữa 2 câu liền kề (cùng hồi) ≥ 0,60 s** · **≤ 25% khoảng nghỉ < 0,40 s** · `timeline.total` = master mp3 ± 0,05 s |

Mốc đo: Tập 05 VN 0,74 s / 16% ✅ · Tập 05 EN 0,84 s / 4% ✅ · Tập 06 VN 0,35 s / 67% ❌ · Tập 06 JA 0,35 s / 83% ❌ · Tập 06 EN 0,65 s / 43% ❌.

### A4.4 Nhạc và lớp nền

| Lớp | Quy tắc |
|---|---|
| Intro | `bgm_music_box.mp3` trọn 22,41 s, đặt ở t = 0 trong master, thấp hơn lời 4 dB |
| Drone nối Hồi 1 | `bgm_sub_drone` vào từ 19,5 s, −40 → −26 dB, tắt dần khi nhạc Hồi 1 vào |
| Lời đầu tiên | 23,0 s |
| Nhạc theo hồi | 1 cello · 2 piano_minimal + _v2 · 3 ambient (đoạn đã cắt) · 4 violin · 5 piano_warm. **Bắt đầu tại ranh giới hồi** (2 s trước lời đầu hồi) để thẻ chương có nhạc |
| Mức nhạc | −26 dB khi có lời, −14 dB ở khoảng nghỉ (tự hạ theo hoạt động giọng) |
| Nền trầm (V4) | `bgm_ambient_deep.mp3` **chỉ đoạn 0,5–13,4 s** (file gốc có 3 khoảng câm), lặp xuyên tập ở −34 dB |
| "Im lặng tuyệt đối" trong kịch bản | Tắt nhạc có giai điệu, giữ nền trầm |
| SFX | Tiếng "Tách" máy ghi âm (tổng hợp bằng code trong `build_audio3.py`) + **11 file SFX trong `assets/sfx/`** (tự tổng hợp bằng `.work/make_sfx.py`, không tải file ngoài). Đặt theo bảng `SFX_CUES` trong `build_audio3.py`: `offset` âm = đặt trước mốc để nối vào câu thoại kế tiếp. Mức tính theo RMS lời, hiệu chuẩn bằng cách nghe thật trong bản thành phẩm, neo theo tiếng "Tách" (−6 dB): dấu câu to (búa tòa +1, gấp hồ sơ −8, khóa cửa −2), sự kiện (−2…−8), nền (−12…−18). Thiếu file → bỏ qua, không làm hỏng cả tập |
| **Nền môi trường** (từ Tập 02) | Bảng `sfx_tapXX.json` → `ambience`: [từ câu, đến câu, file, dB]. Chạy **liên tục** dưới lời theo cảnh (gió tuyết, phòng thẩm vấn, tầng hầm…), −27…−38 dB so với lời, hạ thêm 4 dB khi có lời, mờ vào/ra 1,5 s, nối vòng hoà chồng 1 s. **Mọi đoạn nhạc bị tắt phải có nền bên dưới** (nếu không sẽ vi phạm V4 — Tập 02 từng câm 0,6 s ở lời kết) |
| **Tiếng động theo câu** (từ Tập 02) | `sfx_tapXX.json` → `cues`: [mốc câu/SFX, start\|end, lệch, file, dB]. Tập 02: 37 tiếng (gấp 2,6 lần Tập 01/phút). Tiếng tải về phải **cắt đúng đoạn** và nghe kiểm trước khi nhập (bẫy #20) |
| **Tắt nhạc ở câu hé lộ** | `sfx_tapXX.json` → `music_drop`: tắt nhạc có giai điệu, giữ nền môi trường + nền trầm |
| **Stereo** | Lớp nền/tiếng động trộn stereo (tiếng có vị trí trái/phải và vang theo không gian); lời và nhạc giữa |
| Kết | Piano_warm 6 s mờ dần, 3 s cuối |
| Chuẩn hoá | `loudnorm I=-16:TP=-1.5:LRA=11` **2 lượt, `linear=true`** |

## A5. Hệ thống đồ hoạ chuẩn

### A5.1 Phong cách
Graphic Novel Noir: nét mực đậm, chiaroscuro, viền sáng màu vai, hạt phim. Hai tầng nhân vật: **linh thú dẫn chuyện ở góc** / **người trong vụ án dạng bóng trong cảnh**.

### A5.2 Bảng màu

| Token | Hex | | Token | Hex |
|---|---|---|---|---|
| `ink` | `#0E0E11` | | `amber` · Cú | `#E2B467` |
| `night` | `#151A2A` | | `cold` · Sói | `#86A9CC` |
| `slate` (badge) | `#1C1F2B` | | `violet` · Cáo | `#A99BD6` |
| `paper` / `paper_ink` | `#E6DED0` / `#1C1B1F` | | `sand` · Cừu | `#D9B99B` |
| `text` / `muted` | `#F2EFE9` / `#9C988F` | | `cyan` · Mèo | `#6E8CA0` |
| `pink` / `pink_deep` (**chỉ vụ án**) | `#E8A0BF` / `#A85273` | | `red` (gạch bỏ, cờ, dấu mộc) | `#C8423A` |

### A5.3 Font — **đã đo độ phủ tiếng Việt**

| Vai trò | Font | Ghi chú |
|---|---|---|
| Tiêu đề, nhãn, phụ | Segoe UI Bold / Semibold / Regular | đủ 100% |
| Trích dẫn, lời kể | **Cambria Italic** `cambriai.ttf` | đủ 100% |
| Tiêu đề chương, thẻ hồ sơ | **Cambria** / **Cambria Bold** | đủ 100% |
| Hồ sơ, dữ liệu (Sói) | Consolas | đủ 100% |
| Con số lớn | Bahnschrift | **thiếu "ỷ" và "−"** → chỉ dùng cho chữ số, dấu trừ viết "-" |
| Logo "AMBER EYES" | Georgia | **Georgia thiếu 92 ký tự tiếng Việt — cấm dùng cho chữ có dấu** |

Kiểm tra font mới: script đo ký tự thiếu ở A9.2. Chữ ≥ 24 px; ≤ 3 khối chữ/khung; mọi chữ do Pillow vẽ, không để AI vẽ chữ.

### A5.4 Bố cục khung 1920×1080

- Nền 2112×1188 (dư 10% cho camera). Lề 96 px trái/phải, 72 px trên/dưới; tránh 140 px đáy.
- **Badge người nói:** góc trên-trái (64, 56), 470×124, P0 88 px + tên + chức danh + sóng âm thật (từ `stems/`). Hiện suốt mọi lượt của cả 5 vai; trượt vào 0,3 s.
- **Bán thân:** góc dưới-trái, 420×500, thở 1,000↔1,006 (4 s), viền sáng nhấp ở đầu câu. Hiện ở câu đầu mỗi lượt (3–6 s) và các shot `🅑`. Lần đầu mỗi vai có thẻ giới thiệu (tên · chức danh · *Nhân vật minh hoạ · giọng đọc AI*) 4 s.
- **Vùng cấm chữ khi có bán thân:** `x < 560`, `y > 560` → mẫu T1 / T5-ngày / T6 tự dời khối chữ sang phải.
- **Lời mời (→X):** badge mờ của người sắp nói ở góc trên-phải, chữ *TIẾP THEO*.
- **Hai badge:** đoạn hai vai cùng bàn (Cáo trái, Sói phải; người đang nói sáng).
- **Dàn khách mời:** 5 biểu tượng 150 px cách nhau 250 px ở `y = 300`, tên 18 px.
- **Watermark:** logo 96 px, 35%, góc dưới-phải; ẩn trong intro và thẻ chương ở khoảng nghỉ.

### A5.5 Mười một mẫu khung (đã cài trong `build_video3.py`)

| Mẫu | Tên | Bố cục chuẩn |
|---|---|---|
| T1 | Toàn cảnh | Lớp tối 45% đáy; khối chữ đáy `y = 900`, `x = 96` (hoặc 560) |
| T2 | Thẻ hồ sơ | Giấy rộng 860, **cao theo chữ** (≥ 340), xoay −1,5°, tại `x = 960`; nhãn Consolas đỏ, tiêu đề Cambria Bold, dòng Consolas; **dấu mộc đặt ngay dưới dòng chữ cuối** |
| T3 | Chia đôi / so sánh | Vạch màu vai `x = 920`, chữ phải `x = 970`; biến thể so sánh phủ tối cả khung, cột phải hiện ở câu 2 |
| T4 | Trích dẫn / lời kể | Phủ tối 70%; dấu “ màu vai; Cambria Italic 46–54 px tại `x = 600`, rộng 1180 |
| T5 | Con số | Bahnschrift 250 px đếm lên 1,2 s tại `x = 760`; biến thể ngày gõ từng ký tự |
| T6 | Dòng thời gian | Trục `y = 520`; mốc chấm hồng + nhãn so le trên/dưới; mỗi câu một mốc |
| T7 | Tuyến đường | 2 ghim + đường đứt nét cong tự vẽ 1,5 s |
| T8 | Danh sách | Mục ở `x = 980`, hàng 88 px; biến thể **gạch bỏ** (mỗi câu gạch một mục) và **cờ đỏ** (4 cờ, tô dần) |
| T9 | Thuật ngữ | Vạch màu vai + tên Việt 70 px + tên Anh Consolas 32 px tại `x = 760` |
| T10 | Thẻ chương | Nền `void`; `HỒI 0X` Consolas + tên hồi Cambria 70 px |
| T11 | Bài đăng mạng xã hội | Thẻ trung tính có nhãn MINH HOẠ, không logo, dòng nội dung mờ không đọc được |

### A5.6 Chuyển động và hoàn thiện
- Camera: `push` 1,00→1,05 (mặc định) · `pull` · `pan` · `hero` 1,00→1,10 · `still`.
- Phần tử: mờ dần + nhích 24 px, 0,35 s. Dòng **giữ hình** hiện sẵn mọi thứ (không hiện lại).
- Chuyển cảnh: hoà tan 0,35 s · ✂ cắt · ◼ tối đen 0,6 + 0,6 s.
- Hạt phim + vignette + lệch kênh đỏ 1 px **chỉ trên nền**; chữ, badge, bán thân vẽ sau, sạch.
- Encoder: `libopenh264 -b:v 3000k -maxrate 5000k`; 6 phần ghép bằng `concat -c copy`.

### A5.7 Intro kênh (dùng chung, đã dựng)

`assets/brand/intro_kenh.mov` — chỉ hình, 22,41 s:

| Thời gian | Nội dung |
|---|---|
| 0–4 s | Sợi chỉ đỏ tự vẽ; đôi mắt hổ phách bừng sáng ở 1,5 s; **AMBER EYES** gõ từng chữ; khẩu hiệu *Phân tích tâm lý tội phạm qua những hồ sơ có thật* |
| 4–12,25 s | **Thẻ A — VỀ NỘI DUNG NÀY:** *Nội dung giáo dục, phân tích tâm lý học tội phạm. / Dựa trên tư liệu công khai, nguồn ở phần mô tả. / Không nhằm kết tội hay bôi nhọ bất kỳ ai.* |
| 12,25–20,5 s | **Thẻ B — LƯU Ý TRƯỚC KHI XEM:** *Nội dung không phù hợp cho trẻ em. / Âm thanh và hình ảnh chỉ mang tính minh hoạ. / Không thay thế tư vấn y khoa, tâm lý hay pháp lý.* — 5 vòng màu vai sáng từ 18 s |
| 20,5–22,41 s | Mờ về đen; nền đầu Hồi 1 của từng tập hiện chồng lên |

Nội dung hai thẻ **đã được người dùng chốt** — không tự sửa. Lời miễn trừ không thay được bảo vệ pháp lý thật (A10).

## A6. Tài sản dùng chung (đã có, tập sau dùng lại)

| Nhóm | Đường dẫn | Ghi chú |
|---|---|---|
| Logo, avatar, watermark | `assets/brand/` | Vẽ bằng code (`make_logo.py`), kênh sở hữu trọn vẹn |
| Intro | `assets/brand/intro_kenh.mov` | `make_intro.py`; đổi 5 vòng màu thành biểu tượng linh thú khi cần |
| 5 linh thú | `assets/cast/{H,D,C,N1,N2}/` — `full.png`, `P1.png` (840×1000), `P0.png` (256 tròn) | Tách nền BiRefNet; chưa có P2 |
| 45 nền 16:9 | `assets/bg/*.png` (2112×1188) | Xem danh sách ở Phần B; nhiều cảnh dùng lại được (nhà hồng, bảng ghim, phòng xử, `void`…) |
| Nhạc | `assets/bgm/` (9 file MiniMax) | Lưu ý khoảng câm của `ambient_deep` |
| Hiệu ứng âm thanh | `assets/sfx/` (11 file WAV tự tổng hợp) | `make_sfx.py` — không tải file ngoài nên không vướng bản quyền; dùng lại được cho tập sau |
| Kênh | `assets/brand/channel.json` | Tên, khẩu hiệu, bảng màu, font |
| Ý tưởng các tập sau | `01_KICH_BAN/KHO_Y_TUONG_28_HO_SO.md` | Kho 28 hồ sơ |

## A7. Cách viết bảng shot (mục 6 của hồ sơ tập)

`parse_shots.py` đọc trực tiếp bảng này. Tiêu đề mục phải bắt đầu bằng `## 6. DANH SÁCH SHOT`; bảng kết thúc trước dòng bắt đầu bằng `**Tổng:`.

**Cột:** `Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | chuyển cảnh`

| Cột | Cú pháp |
|---|---|
| Shot | `H-NN` (H = số hồi) |
| Câu | `` `1.11#3`–`#4` `` (khoảng câu trong một phần tử) · `` `1.04` (nghỉ 2 s) `` · `nghỉ chuyển hồi (2 s)` · `` `1.01`–`1.02` `` (mở đầu) |
| Vai | `H` · `D` · `C` · `N1` · `N2` · `—` (không lời) |
| Mẫu | `T1`…`T11`, thêm chữ: `ngày`, `gạch bỏ`, `cờ`, `lời kể`, `so sánh`, `hero` |
| Nền + bóng | Tên nền trong backtick, phải có file `assets/bg/<tên>.png`; camera `` `pull` `` `` `pan` `` `` `still` `` |
| Chữ | `**tiêu đề**` · `*nhãn / dòng phụ*` · `“trích nguyên văn”` · ` → ` tách đoạn hiện sau · `` `#k`: `` đoạn hiện ở câu k · mục danh sách cách nhau ` · ` |
| Beat | `ở "cụm từ trong câu"` → thời điểm theo vị trí cụm từ |
| Nhân vật | `✦` lần đầu · `🅑` thêm bán thân · `⊘` tắt bán thân · `→D` / `→C+D` lời mời · `hai badge` · `dàn khách mời` |
| Chuyển cảnh | trống = hoà tan · `✂` · `◼` |

**Dòng không có câu và không có mẫu** (ví dụ `` `1.04` (nghỉ) `` với mẫu `—`) là **dòng giữ hình**: kế thừa nền và chữ của shot trước. Shot không ghi nền dùng lại nền shot trước.

**Cảnh ghép "nền + bóng người"** (ví dụ phòng thẩm vấn + Gypsy đứng) được tạo sẵn thành một ảnh và khai trong `COMBO` của `parse_shots.py` (A12). Nền đổi trong shot khai trong `BG2`; ảnh nhỏ ghim lên bảng khai trong `INSET`.

**Nguyên tắc biên kịch hình:** mỗi shot 3–15 s; câu > 15 s cần beat mỗi ≤ 7 s; tắt bán thân `⊘` ở khoảnh khắc nặng nề nhất; vai nào nói thì đồ hoạ theo "ngôn ngữ" của vai đó (Sói: hồ sơ, bảng ghim, dòng thời gian · Cáo: thuật ngữ, sơ đồ, so sánh · Người dân: lời kể · Host: cảnh toàn khung).

## A8. Tạo ảnh nền mới

- Công cụ: `connector__matrix__generate_image`, 16:9, 2K, 4 ảnh/lần (~1 phút/ảnh). Ảnh cùng bối cảnh tạo bằng **ảnh tham chiếu** (`"ref"` → script tự `upload-temp-url`).
- Prompt = phong cách chung + mô tả + phần cấm (đã cài sẵn trong `gen_images.py`): `no text, no letters, no numbers, no signs, no labels, no logos, no watermark, no frame, no letterbox bars`.
- Người trong vụ án: `seen from behind`, `face completely hidden in deep shadow, no facial features`; nạn nhân viết là `slender young woman`, không phải trẻ em.
- Không đưa địa chỉ, tên đường vào prompt (AI sẽ vẽ biển tên).
- Script tự cắt viền đen; **viền sáng (trắng, be) phải cắt tay** như Tập 01 (`empty_room`, `fog`).
- **Duyệt bằng mắt mọi ảnh:** chữ lạ, mặt người lộ nét, viền khung, watermark.

### A8.1 Nền là tài sản DÙNG CHUNG cho mọi ngôn ngữ

Nền nằm ở `assets/bg/tXX_*.png` — **2112×1188, phẳng, không có hậu tố ngôn ngữ**. Chữ luôn do Pillow vẽ lúc dựng (H5) nên **cùng một file nền phục vụ mọi ngôn ngữ** (VN/EN/JA/KO…). Cùng một mã shot ở mọi ngôn ngữ phải dùng **cùng một nền** (Tập 08: 223 shot, 74 nền, trùng 100 %).

**Cổng tự động** — chạy sau `parse_shots.py` của mọi ngôn ngữ, trước ảnh tĩnh: `py -3 .work/qc_bg_shared.py --ep XX` (exit 1 = lỗi). Kiểm 4 điều: (1) bộ nền mọi ngôn ngữ bằng nhau · (2) **nền của từng shot theo mã shot** bằng nhau · (3) mọi nền có file trong `assets/bg/` · (4) 0 file nền mang hậu tố ngôn ngữ. So bộ nền thôi **không đủ** (Tập 05 trùng 60 = 60 nhưng 2 shot lệch). Chạy không `--ep` = quét mọi tập; tập trong `MIEN_TRU` chỉ cảnh báo.

**Điều kiện tiên quyết:** các ngôn ngữ phải dựng từ **cùng một phiên bản kịch bản / bảng shot** (mã shot trùng nhau). Cổng báo "mã shot không khớp" ⇒ bản ngôn ngữ đó **chưa đồng bộ** (vd Tập 01 KO còn ở bảng shot 24/10, 122 shot; VN/EN/JA đã dựng lại 09/11, 203 shot) ⇒ đồng bộ bảng shot trước, rồi mới xét nền.

**Phạm vi áp dụng (người dùng chốt 10/11/2026): MỌI yêu cầu tạo ảnh cho video đa ngôn ngữ đều PHẢI theo quy định này — không có ngoại lệ theo tập.**

- **Tạo mới** một tập (vd Tập 20) ⇒ theo quy định này.
- **Tạo lại ảnh của tập cũ** (vd Tập 01, Tập 03 — kể cả tập đang nằm trong `MIEN_TRU`) ⇒ **cũng theo quy định này**: sinh 1 bộ nền dùng chung, đồng bộ bảng shot của **mọi** ngôn ngữ của tập đó về cùng mã shot + cùng nền, và `qc_bg_shared.py --ep XX` phải `DAT` trước khi xuất ảnh tĩnh. `MIEN_TRU` **không** phải giấy phép làm lệch: nó chỉ làm dịu kết quả khi quét toàn bộ; chạy `--ep XX` luôn báo lỗi thật. Làm lại xong tập nào ⇒ **gỡ tập đó khỏi `MIEN_TRU`**.
- **Chỉ thêm / sửa vài nền** của một tập ⇒ nền mới vẫn là nền dùng chung; đổi nền ở shot nào thì đổi ở mọi ngôn ngữ.
- Điều duy nhất quy định này **không** bắt buộc: tự động dựng lại các bản đã xuất mà người dùng không yêu cầu đụng tới (Tập 01, 02, 03, 05 hiện lệch nền giữa các ngôn ngữ — A11 #145 — giữ nguyên cho đến khi người dùng yêu cầu làm lại).
- AI nhận yêu cầu "tạo ảnh riêng cho bản EN/JA/KO" ⇒ **không làm theo cách đó**; nhắc quy định này và làm theo trình tự dưới đây (muốn bỏ quy định phải do người dùng nói rõ là đổi luật).

**Trình tự làm hình — dùng cho cả tập mới lẫn tập cũ làm lại (mọi ngôn ngữ):**

| Bước | Việc | ĐẠT khi |
|---|---|---|
| a | Viết file jobs, **sinh nền 1 lần** bằng `gen_images.py` (A8) | Mỗi nền 1 file `assets/bg/tXX_*.png`, không hậu tố ngôn ngữ, có dòng trong `provenance.json` (L7) |
| b | **Duyệt mắt mọi nền** | Không chữ lạ, không lộ mặt, không viền (H2) · đọc tên nền ra một cảnh cụ thể (H19, A8.2) |
| c | Viết bảng shot **bản gốc (VN)** rồi làm bảng shot các ngôn ngữ khác **từ chính bảng đó**: giữ nguyên **mã shot, nền, mẫu T, camera**; chỉ đổi **cột Chữ** sang ngôn ngữ đích | Số shot và mã shot các ngôn ngữ bằng nhau |
| d | `parse_shots.py` cho **từng** ngôn ngữ (`AE_EP=XX`, thêm `AE_LANG=..` — L8) | Mỗi ngôn ngữ có `shots*.json` |
| e | **Cổng nền dùng chung**: `py -3 .work/qc_bg_shared.py --ep XX` | `DAT` — bộ nền và nền từng shot trùng mọi ngôn ngữ |
| f | Ảnh tĩnh **mọi shot × mọi ngôn ngữ**, soi contact sheet (A9.3) | Không đè chữ, không tràn mép, chữ đọc được trên nền (A11 #130) |
| g | Chữ một ngôn ngữ bị tràn/khó đọc | Rút gọn cột Chữ ở bảng shot của ngôn ngữ đó hoặc khai `text_scrim` theo ngôn ngữ — **không đổi nền, không sinh lại nền**; đổi nền thì đổi ở mọi ngôn ngữ rồi chạy lại bước d–f |

**Quy định sinh nền dùng chung (10/11/2026, người dùng chốt):**
1. **Sinh nền 1 lần cho mỗi tập** — CẤM sinh nền riêng cho từng ngôn ngữ; CẤM tên file có hậu tố `_EN/_JA/_KO/_VI/_VN`.
2. **Nền sạch chữ 100 %** (biển hiệu, nhãn, giấy tờ, màn hình) — chữ do AI vẽ vừa sai H5 vừa khoá ảnh vào 1 ngôn ngữ.
3. *(NÊN — đang thử nghiệm, chưa chốt)* **Tránh chi tiết dày ở 1/3 dưới** để chữ T1 (góc dưới) đọc được ở mọi ngôn ngữ — **mặc định TẮT**; chỉ bật cho từng ảnh bằng khoá `"caption_space": true` trong file jobs của `gen_images.py` (không nằm trong `STYLE` chung, nên nền cũ sinh lại không đổi bố cục). **Chưa sinh thử.** Chỉ bật cho nền dùng ở shot T1; T4/T5/T9/T10 chữ ở giữa/thẻ riêng nên không cần. **Không được** đánh đổi nội dung cảnh (H19). Chốt thành luật sau khi sinh thử 2–3 nền và soi mắt (L3, L4 vì tốn credit).
4. **Chữ theo ngôn ngữ chỉ vẽ lúc dựng** (Pillow, H5). Chữ dài đè/tràn ⇒ rút gọn ở bảng shot của ngôn ngữ đó hoặc khai `text_scrim` theo ngôn ngữ (A11 #130) — **không** sinh lại nền **chỉ vì chữ của một ngôn ngữ bị tràn**. Nền có chữ lạ / lộ mặt / sai cảnh (H2, H19) thì vẫn phải sinh lại (cho mọi ngôn ngữ).
5. **Duyệt ảnh tĩnh của MỌI ngôn ngữ** (VN/EN/JA/KO…) — VN đạt không có nghĩa ngôn ngữ khác đạt.
6. Đổi nền ở 1 ngôn ngữ ⇒ đổi bảng shot của **mọi** ngôn ngữ, chạy lại `qc_bg_shared.py` đến khi ĐẠT.

### A8.2 Nền PHẢI có nội dung cảnh — không được là nền trừu tượng

Nền chỉ là gradient/ánh sáng thì **vi phạm H3** dù cổng QC vẫn xanh (QC đo chữ/số/thời lượng, không đo ngữ nghĩa ảnh).

**Duyệt bằng mắt: đọc tên nền phải ra một cảnh cụ thể** ("bệnh viện", "sân ga Tokyo", "xe bán tải trên camera an ninh"). Đọc tên mà chỉ ra màu sắc ⇒ nền vô dụng.

Chỉ số tự động **không phân biệt được** (đo 09/11/2026): entropy luminance MiniMax 5,18 vs procedural 4,39 — hai nhóm chồng nhau; Tập 08 có vân tia nên tỉ lệ "nội dung" cao (87%) dù về mặt thị giác là gradient. ⇒ **bắt buộc soi mắt, không được tin chỉ số**.

### A8.3 Bảng công cụ đã dùng (đo trên `provenance.json`)

| Nhóm tập | Công cụ | Số ảnh | Ghi chú |
|---|---|---|---|
| Tập 01 (nền gốc) | Ảnh người dùng tạo + inpaint xoá chữ | 8 | Bộ ảnh ban đầu |
| **Tập 02–07** | **MiniMax** — `connector__matrix__generate_image` qua `mcode-tools` (`.work/gen_images.py`) | 402 | Style Graphic Novel chuẩn |
| **Tập 08–29** | **`Amber Eyes Noir Graphic Renderer`** — procedural Pillow & Numpy | 1361 | Bộ nền trừu tượng cũ (đang thay thế dần) |
| **Tập 11+** | **Kaggle GPU · FLUX.2-klein-4B** (kèm hậu kỳ Deep Noir) | 70+ | Chuẩn tạo ảnh mới 0 đồng chi phí (xem `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md`) |
| Tập 06 | 1 ảnh thử `image-generator` (Google Imagen / Antigravity Native) | 1 | Thử nghiệm |

`gen_gemini_api.py` (Imagen 3) chỉ là script thử cho Tập 07 và **hiện không chạy được** — không có `.gemini_key`, không có env `GEMINI_API_KEY`.

**Khi sinh lại nền tập cũ:** ghi đè đúng file `assets/bg/tXX_*.png` ⇒ **sao lưu trước** (L5), và cập nhật **cả** `provenance.json` (`cong_cu`) **và** `REVIEW_Bo_Anh_TapXX.md` (đang khẳng định "100% tự chủ, không sử dụng MiniMax") — nếu không, hồ sơ mâu thuẫn với thực tế.

### A8.4 Tối ưu ảnh tĩnh (đo 09/11/2026, Tập 08)

Chi phí thật mỗi ảnh tĩnh (median 5 lần): `finishing()` **86 ms** · `resize` 25 ms · **ghi PNG 221 ms (nửa tổng)** · chữ + avatar **22 ms**.

| Cách | 223 shot × 3 ngôn ngữ | Ảnh byte-identical? |
|---|---|---|
| A — hiện tại (render lại cả 3 ngôn ngữ) | **5,0 phút** | — |
| B — nền dùng chung + chỉ vẽ thêm chữ | **3,6 phút** (−27%) | shot `still` khớp byte; `pan`/`pull` lệch nhỏ (xem AGENTS T24) |
| B' — B + ghi PNG `compress_level=1` | **2,5 phút** (−49%) | như trên |

**Cách đo đúng:** xen kẽ A/B **≥ 3 vòng**, mỗi vòng xoá file tạm, lấy **median**. Đo "A lạnh rồi B nóng" **phóng đại** kết quả (09/11: báo 12,5 → 4,3 phút; đo lại công bằng: 5,0 → 3,6 phút).

Ràng buộc kỹ thuật: `camera_box()` phụ thuộc thời lượng shot (khác nhau giữa 3 ngôn ngữ) ⇒ shot `pan`/`pull` **lệch khung crop**; dùng `t = fi/FPS` (đúng convention của `render()`), không dùng `(start+end)/2`; **shot cuối có fade-to-black ⇒ render riêng**.

## A9. Kiểm tra (chạy và đạt hết trước khi giao)

### A9.1 Âm thanh
```bash
F=.work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe
$F -i .work/audio_master.wav -af silencedetect=n=-60dB:d=0.3 -f null -   # 0 đoạn
$F -i .work/audio_master.wav -af silencedetect=n=-35dB:d=2.5 -f null -   # chỉ được là đoạn "im lặng tuyệt đối" có chủ đích
$F -i .work/audio_master.wav -af ebur128=peak=true -f null -             # -16 ± 1 LUFS
```
Lời đầu tiên 22,8–23,5 s; mỗi câu đúng giọng vai (`tts_manifest.json`).

### A9.2 Chữ và font
- Phủ câu: 100% câu thuộc đúng một shot, đúng thứ tự, cột Vai khớp người nói.
- Mọi con số trên hình có trong câu của shot; mọi câu trích có nguyên văn trong kịch bản.
- Không còn từ bạo lực (danh sách: máu ngoài "ung thư máu", thi thể, sát hại, đòn, trói, bầm, đập, đầu độc, diệt cỏ, bỏ đói, móc áo…).
- Font: đo ký tự tiếng Việt thiếu (`getmask` so với ký tự `\uffff`) — 0 với mọi font chứa chữ có dấu.

### A9.3 Hình
- Ảnh ghép 1 khung giữa mỗi shot → AI xem từng ô: hình đúng câu? biết ai đang nói? chữ đè nhau? mặt người lộ? chữ lạ do AI?
- **Thêm: đọc tên nền ra được cảnh cụ thể không?** ("bệnh viện", "sân ga Tokyo") — nếu chỉ ra màu sắc ⇒ nền trừu tượng, vi phạm H3 (xem A8.2).
- Sửa → dựng lại đúng phần (công thức A3) → ghép lại.

> **Ảnh tĩnh là CỔNG QC, không phải nguyên liệu dựng video.** Luồng đúng: **sinh ảnh → dựng video**. Video được dựng lại từ đầu bằng `--workers 6` và **không đọc ảnh tĩnh**. Cổng này tồn tại để chặn lỗi trước khi bỏ ~1 giờ dựng — không được thay bằng "trích frame từ video cũ" (video chưa tồn tại ở bước này).

### A9.4 File cuối
- Hình và tiếng cùng thời lượng (±0,05 s); `ffmpeg -v error -i TapXX_master.mp4 -f null -` không lỗi.

### A9.5 QC ảnh tĩnh tiết kiệm — đo 100 %, soi mắt chọn lọc (luật H20)

**Nguyên tắc: KHÔNG hạ ngưỡng chất lượng, chỉ giảm phần đọc bằng mắt.**

Vẫn bắt buộc:
- Render **ảnh tĩnh 100 % shot × mọi ngôn ngữ** (H9).
- Chạy **cổng đo chữ chìm 100 %** với ngưỡng **8 % — không nới, không bỏ ngôn ngữ nào**.
- **Nền mới sinh: soi 100 %, không được lược** (H2/H19).

Chỉ **soi bằng mắt** trên 4 nhóm rủi ro (mỗi ngôn ngữ tính riêng):

| # | Nhóm rủi ro | Ngưỡng |
|---|---|---|
| ① | Mẫu đặc biệt: T4 (lời kể) · T8 (cờ) · T10 (thẻ hồi) · T2 (thẻ kết) | — |
| ② | Shot có `text_scrim` (lớp phủ đổi tương phản nền) | — |
| ③ | Nền **sáng** ở vùng đặt chữ | `--lum` (mặc định 75/255) |
| ④ | **Chữ dài** của ngôn ngữ đó | `--chars` (mặc định 150 ký tự) |

**Lệnh:**
```bash
# 1) lấy danh sách shot bắt buộc soi (in ra danh sách + lý do từng shot)
py -3 .work/qc_eyeball_list.py --ep 10 --lang vi --lum 75 --chars 150 --json .work/_t10/eyeball_vi.json
# 2) ghép thành 1 tờ montage để soi (1 lần đọc, thay nhiều tờ contact sheet)
py -3 .work/qc_montage.py --ep 10 --kind stills --lang vi --list .work/_t10/eyeball_vi.json --cell 512 --cols 8
# 3) nền (luôn soi 100 % nền mới)
py -3 .work/qc_montage.py --ep 10 --kind bg
```
Ghi ra `.work/qc_montage/epXX_<kind>[_<lang>].jpg`.

**Shot bị lược** chỉ soi khi: đo tự động báo vượt ngưỡng, hoặc vừa đổi nền / đổi bảng shot (⇒ soi lại đúng các shot vừa đổi).

**Báo cáo QC phải ghi rõ:** tập nào đã soi mắt, tập nào dựa vào đo tự động, kèm số shot và ngưỡng đã dùng.

> **Montage không thay zoom 100 %.** Ô nhỏ quá thì mở full-res đúng ô đó (H2). Ô nhỏ cũng không đủ để kết luận "chữ không bị chìm" — việc đó do cổng đo 8 % lo.

**Số đo thật (Tập 10, 12/11/2026):** 211 shot × 3 ngôn ngữ ⇒ bắt buộc soi **VI 91 (43 %) · EN 75 (36 %) · JA 66 (31 %)**, lược 120/136/145 shot; H9 vẫn đo 100 % và đạt **0 shot chữ chìm** (tệ nhất VI 7,8 % · EN 7,8 % · JA 7,4 %). Trước đây QC tốn **19 lần đọc ảnh ≈ 30–42k token**; nay **1 tờ montage/ngôn ngữ** (91 ô, 4128×4104 px). Montage đã bắt được lỗi mà contact sheet bỏ sót: nền `t10_truth_revealed_shattered_phantom` có chữ AI vẽ "THE COMPANY" và nền `t10_fbi_academy_profiling_archive` có bìa sách khắc "Stan Case Study / Psychological / …" ⇒ **2 nền phải sinh lại** (đã sửa prompt + sinh lại + soi lại ⇒ sạch).

## A10. Đóng gói, pháp lý, kiếm tiền

- **Mô tả:** mẫu trong `package.py` (mốc chương tự tính từ `timeline_s.json`; lưu ý; nguồn; Tổng đài 111). **Không có email liên hệ.**
- **Nguồn:** `nguon_tham_khao.md` liệt kê câu nói về người thật cần link — **người dùng điền, AI không bịa**.
- **Hồ sơ nguồn gốc:** mọi file tạo ra ghi vào `provenance.json` (công cụ, prompt, ngày, điều khoản). Trước khi đăng phải kiểm tra điều khoản thương mại của MiniMax và công cụ tạo ảnh của người dùng.
- **YouTube:** bật "Nội dung bị thay đổi hoặc tổng hợp" · chọn "Không dành cho trẻ em" · không tự bật 18+ · danh mục Giáo dục · tự đánh giá quảng cáo trung thực ("chủ đề gây tranh cãi — thảo luận, không mô tả chi tiết").
- Lời miễn trừ không ngăn được khiếu nại; bảo vệ thật là tài sản có giấy phép + nguồn cho từng dữ kiện.

## A11. Bẫy đã gặp — đừng lặp lại

| # | Bẫy | Cách làm đúng |
|---|---|---|
| 1 | `output_file` có dấu chấm (`1.03_01`) → server coi là đuôi file, mọi câu trùng tên `1.mp3` | Tên không dấu chấm: `s1_03_01` |
| 2 | `--args '<json>'` chứa URL có `&` bị `cmd` cắt | Luôn dùng `--args-file` |
| 3 | `mcode-tools` thỉnh thoảng báo "Network request failed" | Tự thử lại 4 lần, giãn 10/20/30 s (đã cài trong script) |
| 4 | `listen_audio` trả trường `transcription` | Đọc đúng tên trường |
| 5 | Georgia thiếu 92 ký tự tiếng Việt; Bahnschrift thiếu "ỷ", "−" | Cambria / Segoe; đo font trước khi dùng |
| 6 | `bgm_ambient_deep` có khoảng câm bên trong → lặp ra khoảng câm | Chỉ lặp đoạn liên tục |
| 7 | Nhạc hồi mới vào sau thẻ chương → ranh giới hồi hụt tiếng | Nhạc hồi bắt đầu tại ranh giới |
| 8 | Ảnh AI: viền đen, viền trắng, chữ (biển tên, "FEEDING TUBE", "DSM-5"), lộ mặt | Prompt cấm + tự cắt viền + inpaint chữ + duyệt mắt |
| 9 | Tách nền bằng khoá độ sáng làm quần áo tối trong suốt | BiRefNet + lấp lỗ **chỉ khi lỗ có màu** (lỗ đen tuyền là nền) |
| 10 | Giải mã cả intro vào RAM (~4 GB × 6 tiến trình) | Đọc intro tuần tự từng khung |
| 11 | Dòng giữ hình làm chữ, thẻ hiện lại từ đầu | Dòng giữ hình hiện sẵn mọi phần tử |
| 12 | Dấu mộc đặt theo đáy thẻ → đè chữ khi thẻ dài | Đặt theo dòng chữ cuối |
| 13 | Câu trích bị cắt cụt rồi thêm "?" | Kiểm tra nguyên văn (A9.2) |
| 14 | Tính nhầm phần cần dựng lại | Dùng công thức A3 |
| 15 | Ảnh concept từ Pollinations có watermark | Tạo lại không watermark, không tự xoá |
| 16 | Kịch bản ghi 25–27 phút nhưng thực đọc ~19 phút | Ước tính 3,1–3,2 từ/giây; muốn dài hơn phải thêm lời |
| 17 | Giọng đều đều — cảm xúc đặt theo lượt, Sói/Cáo 100% `neutral` (phản hồi khán giả Tập 01) | Diễn xuất từng câu theo A4.2 |
| 18 | Ngắt `...` / `<#s#>` giữa câu làm giọng Việt vụn như robot | Chỉ ngắt GIỮA các câu (`_pause_after`); trong câu chỉ một thẻ trước câu trích (G1) |
| 19 | Dịch vụ TTS lỗi "audio post-processing failed" nhiều giờ (22–23/10); vòng chờ báo nhầm là đã chạy lại | Chỉ coi là chạy lại khi phản hồi có `node_id`; script đã có bộ đệm, chạy lại chỉ đọc câu còn thiếu |
| 20 | Tiếng động tải về là cả bài 14–59 s, hoặc sai nội dung (búa tòa thành tiếng lắc bình xịt, có giọng radio lẫn vào) | Nghe từng file bằng `audios_understand` trước khi nhập; cắt đúng đoạn (`CUTS`), file sai giữ bản code (`KEEP_CODE`) trong `import_sfx_video.py` |
| 21 | Renderer viết theo bảng shot Tập 01: T3 "so sánh" chỉ hiểu một đoạn có ≥ 2 tiêu đề đậm; T8 chỉ đọc đoạn đầu; T7 có nhãn ghim "SPRINGFIELD/WISCONSIN" viết cứng; T7 vẽ mọi đoạn cùng một chỗ (Tập 02: lỗi `IndexError`, chữ bị mất, sai địa danh, đè chữ) | Đã sửa 23/10: T3 nhận `trái → phải` và giữ thứ tự nhãn/tiêu đề, hiện câu trích; T8 đọc mọi đoạn, dòng đậm không đánh số; T7 xếp chồng đoạn, nhãn ghim khai ở `EPISODES[..]["route_pins"]`. **Luôn chạy ảnh tĩnh cho MỌI shot (A9.3) trước khi dựng cả tập** — một shot lỗi làm hỏng cả lượt dựng 30 phút |
| 22 | **T5 (con số) chỉ hiện MỘT số/tiêu đề lớn** — đoạn thứ hai có chữ đậm đè lên ("B8ẾN 01 · 2010", "82" chồng "88") | Ở T5 chỉ một `**…**`; thông tin thêm viết nghiêng, hoặc tách sang shot kế |
| 23 | "Host nghe như 3 người", "giọng nam giống hệt nhau" (Tập 02): tham số cao độ/cảm xúc làm `audiobook_male_1` đổi danh tính; 2 giọng nam cùng vùng giọng; buổi thử chỉ so các bản của cùng một câu | Bộ A + G8–G10; cao độ luôn 0 |
| 24 | Giọng đa ngôn ngữ đọc số kiểu tiếng Anh: "1.400" → "một phẩy bốn trăm"; số La Mã "II" đọc thành chữ cái | G11 — đổi số sang chữ trong lời đọc. Khi soạn kịch bản: đơn vị, ký hiệu (%, km, $) nên viết bằng chữ |
| 25 | Shot cuối (bìa hồ sơ gập, mẫu T2) để cột Chữ là "—" → video kết thúc bằng **tờ giấy trống** (Tập 01, Tập 02; người dùng phát hiện) | Cột Chữ shot cuối: `*HỒ SƠ TẬP XX · ĐÃ ĐÓNG* · **AMBER EYES** · *Phân tích tâm lý tội phạm* · *qua những hồ sơ có thật*`. Hai dòng khẩu hiệu viết thành hai mục nghiêng riêng (mỗi dòng ≤ 48 ký tự, tránh tiền tố "—") |
| 26 | **Freesound API: mọi từ trong `query` đều BẮT BUỘC** → truy vấn 3–4 từ luôn trả 0 kết quả (7/19 mã SFX rỗng lần đầu) | Từ khóa chỉ **1–2 từ**: "library ambience" ✓, "library quiet room tone" ✗. Client đã có `fallback` tự bỏ dần từ |
| 27 | **Freesound không hỗ trợ `grant_type=client_credentials`** (trả 400 `unauthorized_client`) | Dùng **Token auth**: cột "Client secret/Api key" làm API key, header `Authorization: Token <key>`. Chỉ khi cần **file gốc** mới làm OAuth2 `authorization_code` (cần đăng nhập trình duyệt) |
| 28 | Freesound endpoint `download/` (file gốc) là **OAuth2-required** → Token auth trả 401 | Token auth chỉ lấy được **preview hq mp3 160 kbps stereo** qua CDN — đủ dùng cho mix video |
| 29 | Hạn mức Freesound: **60 req/phút · 2000 req/ngày**, tính theo USER (mọi client cùng tài khoản dùng chung hạn mức) | Client throttle ≥ 1,1 s/lần (~54 req/phút); `GET /apiv2/usage/` để xem đã dùng bao nhiêu (endpoint này không bị throttle) |
| 30 | Ghi `provenance.json` bằng `indent=2` làm file phình 1,83 MB → 1,89 MB, không mất dòng nào nhưng **đổi định dạng toàn file** | `provenance.json` dùng **`indent=1`** — giữ nguyên khi ghi |
| 31 | Ghi provenance cho ứng viên Freesound vào sổ chính bị **skip hết** vì `file` trùng đường dẫn đích đã có dòng từ YouTube Audio Library | Ứng viên **chưa duyệt** ghi vào sổ tạm `.work/freesound_provenance.json`; chỉ `--merge` vào `provenance.json` sau khi người dùng nghe duyệt |
| 32 | **Lệch pha ngữ nghĩa giữa câu thoại và hình ảnh/chữ trên hình (Tập 06: người dùng phát hiện đang nói mức lương 5$ thì hình đã chuyển sang tủ áo khoác mỏng)**: Phân bổ ranh giới câu thoại vào shot bị vội, cắt shot ở giữa hai câu cùng chủ đề hoặc đặt shot hiển thị trước khi câu thoại bắt đầu | **Rà soát đồng bộ ngữ nghĩa 100% trước khi dựng**: Mỗi khi câu thoại chuyển sang đối tượng/vật chứng/địa điểm mới thì ảnh và chữ mới chuyển theo; các câu cùng một nội dung cốt lõi (như 2 câu về mức lương 5$) phải gom trọn vẹn trong cùng 1 shot; chữ hiển thị phải lấy đúng từ câu đang đọc trong shot đó (H3, V3) |
| 33 | **Lệch chữ trên hình, ảnh nền và vai nhân vật (Tập 04)**: Chữ trên hình tự tóm tắt ý niệm hoặc trích dẫn bịa không có trong câu thoại (vi phạm H6/V3); nền chuyển trước khi câu thoại đề cập (nền kho dịch truyền hiện khi đang nói về hủy lệnh bỏ túi áo); gán nhầm vai Host cho câu của Điều tra viên (vi phạm G9/H3) | **Quy tắc đối soát 3 lớp trước khi render**: 1) Script quét chữ trên hình đối chiếu 100% với lời đọc; 2) Mỗi shot chỉ dùng ảnh nền tương ứng với ngữ cảnh câu đang đọc; 3) Kiểm tra khớp vai và avatar bán thân 100% với kịch bản gốc. |
| 34 | **Tắc nghẽn CPU khi tính đường bao ducking trên mảng mẫu lớn (Tập 03 EN)**: `np.convolve` trực tiếp trên ~85 triệu mẫu (32 phút) tốn ~5 phút CPU 100% | Thay bằng trung bình trượt tích lũy `np.cumsum` chạy trong **0,05 giây**, kết quả toán học đồng nhất |
| 35 | **Khoảng câm > 0,3 s ở đoạn kết video dài > 30 phút (Tập 03 EN)**: Sàn môi trường đặt −34 dB bị hụt dưới −60 dBFS khi nhạc nền fade out | Đặt sàn môi trường −31 dB và kéo dài đuôi piano ấm 7,8 s với fade out mượt giúp video không bao giờ câm > 0,3 s |
| 36 | **Lỗi `IntroReader` văng `AttributeError` khi worker render seek vượt đuôi video intro (Tập 04 EN)**: Worker bắt đầu từ frame $\ge$ thời lượng của `intro_kenh_*.mov` hoặc shot `1-00` gọi blend khi $t \ge 20.5 + 1.9$ s khiến FFmpeg hết frame (`self.last` là `None`) | Trong `IntroReader.get`: nếu `self.last is None` trả ảnh đen RGBA; trong `render()` chỉ blend intro ở shot `1-00` khi $t < 20.5 + 1.9$ s |
| 37 | **Sửa bảng shot xong nhưng KHÔNG dựng lại video → thành phẩm vẫn còn lỗi cũ** (Tập 02, phát hiện 25/10/2026): `shots_t02.json` sửa lúc 24/10 09:22 (thêm chữ cho thẻ kết `5-29`) nhưng `Tap02_master.mp4` dựng lúc 23/10 19:43 → **video kết bằng tờ giấy trắng trơn + 2,7 s màn đen**, đúng bẫy #25 đã ghi là "đã sửa" | **Trước khi giao bất kỳ tập nào: so `mtime` bảng shot (`shots_tXX.json`) với `mtime` file mp4 thành phẩm — bảng shot phải CŨ HƠN video.** Luôn trích **khung tại giữa shot cuối** từ mp4 (không dùng ảnh tĩnh) và đảm bảo khung đó có chữ, không phải nền trắng/đen trơn. Nếu chỉ sửa 1 shot cuối thì `build_video3.py --stills` + `rerender_part.py` + `package.py --mux`, **không cần dựng lại toàn bộ** |
| 38 | **Đo đỉnh âm lượng trên WAV trung gian → tưởng là đạt, nhưng file mp4 vượt trần** (Tập 02): WAV đo −1,5 dBFS nhưng AAC trong mp4 đo **−0,9 dBTP** (vượt trần −1,5 của chính dự án) vì bộ mã hoá đẩy đỉnh lên ~0,6 dB | **Luôn đo `ebur128=peak=true` trên chính file mp4 cuối**, không đo WAV trung gian. Khi đóng gói, áp giới hạn trước khi mã hoá rồi đo lại trên mp4. **Cách đã dùng và đo được (Tập 02, 31/10/2026):** `-af "alimiter=limit=0.7943:attack=5:release=50:level=disabled"` (sample peak −2 dBFS; `level=disabled` để không đổi loudness tổng) → mp4 đo **−1,9 dBTP · −16,0 LUFS**. Đã vá trong `package.py` cho **mọi tập**. Đo lại các master đã xuất (cùng ngày): **Tap04 −1,2 · Tap04_EN −1,2 · Tap05 −0,7 · Tap05_EN −1,1 · Tap06 −1,2 · Tap07 −1,1 dBTP ⇒ đều vượt trần, cần ghép lại**; Tap01_JA −4,1 · Tap01_KO −4,2 (đạt) |
| 39 | **Copy pattern `bed` của tập khác cho tập mới → nhạc nền không khớp kịch bản** (phát hiện 25/10/2026): 20/29 tập dùng chung 1 pattern; T09/T16 kịch bản đòi guitar/organ nhưng bed trỏ piano/cello; 2 track tải về (220 s + 196 s) nằm không ai dùng | **Bed mỗi hồi = mood thẻ `[BGM]` ĐẦU TIÊN của hồi đó** trong `01_KICH_BAN/TapXX/` (Hồi 1 lấy tại mốc `act1_cue`). Kiểm bằng `.work/_qc_bgm_bed_start.py` (đối chiếu 145 slot hồi) trước khi dựng. **Cấm** copy y hồi sẵn tập khác |
| 40 | **Vá `edition.py` bằng script → mất dấu nháy → `py_compile` vẫn PASS nhưng file hỏng khi chạy** (25/10/2026): dựng lại literal `"bed"` bằng `", ".join(...)` làm mất `"` → `1: bgm_cello_sad.mp3` thành **biểu thức thuộc tính** (NameError lúc chạy), và làm hỏng cả các giá trị tuple cũ | Vá **chỉ giá trị của đúng hồi** trong literal gốc (regex `(\d+): ("[^"]*"\|\([^()]*\))`), không dựng lại cả khối. Sau khi vá **phải `import edition` thật** để bắt lỗi tên biến — `py_compile` chỉ kiểm cú pháp. Có bản sao lưu ở `.work/_cu/` để quay lại |
| 41 | **`package.py --mux` crash `KeyError: '1.01#1'` vì `EPISODES[*]["summary"]` trỏ vào element không có câu thoại** (Tập 07, 08 — 25/10/2026): element `1.01` của 2 tập này là thẻ `[BGM]` (không có câu), nên mã câu `1.01#1` không tồn tại trong script hiện tại (script đã được sửa sau lúc dựng). Mp4 đã ghép xong nhưng **mô tả + thumbnail không được tạo** | Kiểm `summary` của cả 29 tập trước khi đóng gói: `.work/_patch_summary_t07.py` (in ra tập nào hỏng và tự sửa về câu thoại đầu hồi 1). Sau khi sửa kịch bản phải cập nhật lại `summary` |
| 42 | **`audio_master.wav` là 48 kHz, không phải 44,1 kHz** (25/10/2026): `loudnorm` trong `build_audio3.py` dùng `aresample=48000`. Đo/cắt bằng hằng số 44100 lệch mốc thời gian **8,8 %** → kết luận sai là "các hồi không sửa cũng thay đổi" | Khi phân tích file âm thanh, **đọc `framerate` từ header WAV** (`wave.getframerate()`), không hard-code. Bài học còn lại: khi đo "phần nào thay đổi", so bằng **tương quan với file nguồn** (`.work/_qc_bgm_pause.py`) chứ không chỉ so trước/sau |
| 43 | **`batch_text_to_audio` chỉ nhận tối đa 10 request/lượt** (27/10/2026): gửi 51 request trong 1 lượt → lỗi `connector_tool_error: Connector tool execution failed (latency_ms=0)` — **không có thông báo nào nói nguyên nhân là vượt giới hạn**, trông như server chết | Chia chunk **10 request/lượt**; đọc `success_items[]`/`failed_items[]` của **từng** batch thay vì tin exit code. Cùng lỗi này đã làm 4 ứng viên TTS "hỏng" trong 1 lượt chạy |
| 44 | **Đo CER bằng ASR mà không chuẩn hoá số ở CẢ HAI VẾ** (27/10/2026): `ref` = lời đọc trong manifest (đã qua `vi_numbers()` → chữ: "tám mươi tám") nhưng `hyp` = ASR trả về **dạng số** ("88") → 1 câu hoàn toàn đúng bị tính **CER 21,4 %**, câu khác **300 %** | Áp `vi_numbers()` cho **cả `ref` lẫn `hyp`** trước khi tính CER. Sau khi sửa, toàn bộ "lỗi nặng" biến mất |
| 45 | **Bộ lọc nội dung Gemini chặn câu TTS nhưng mã lỗi vẫn `code = 0`** (27/10/2026): `listen_audio` trả `{"code":0,"message":"ok","transcription":"This request was blocked by Gemini's filters..."}` → tưởng đó là lỗi phát âm của giọng | **Đọc nội dung `transcription` chứ không chỉ `code`**; cắt đuôi lỗi bằng regex rồi chạy lại câu đó. Câu bị chặn là **mẫu hỏng** → loại khỏi mẫu đo (2/20 câu), không tính là lỗi giọng |
| 46 | **Vắng mặt trong `get_voice_list` ≠ giọng đã chết** (27/10/2026): `audiobook_male_1`, `male-qn-qingse`, `audiobook_female_1` không có trong danh mục live 332 giọng, nhưng `male-qn-qingse` lại là **default** của schema TTS | MiniMax có 2 lớp: *voice library* (danh mục) và **system voice cũ** không được liệt kê nhưng API vẫn nhận. Chỉ kết luận "giọng chết" sau **1 lần gọi TTS thật**; không kết luận từ tên |
| 47 | **`pitch` của connector KHÔNG phải chỉnh cao độ (F0)**: `pitch` = `voice_setting.pitch` = đổi **âm sắc (timbre)**, 0 = giữ nguyên âm sắc gốc | Muốn đổi F0 thì đổi `voice_id` và **đo lại F0**, không dùng `pitch`. Cũng **không có tham số `language`** — ngôn ngữ đến từ **văn bản**, chất giọng đến từ `voice_id` (synthesis, không phải dịch) |
| 48 | **ASR không tất định — cùng 1 file, 2 lượt cho kết luận khác nhau** (27/10/2026): 3/9 câu vượt ngưỡng đổi kết quả giữa 2 lượt (28 %→18 %, 4,3 %→1,1 %) | Mỗi kết luận về **từng câu** phải chạy **≥ 2 lượt**; câu vượt ngưỡng thì chạy thêm lượt nữa (rẻ, ~10 lượt). Với `audios_understand`, cùng 1 file bed đổi verdict **10/45 file** ⇒ verdict AI chỉ là **tín hiệu mềm**, không dùng làm gate cứng |
| 49 | **Đoán giới tính giọng từ tên** → sai (`"female"` chứa `"male"`, `"woman"` chứa `"man"`) | Không đoán từ tên — **đo F0 thật**. Và chỉ đo trên **file TTS rời**: đo trên master (đã có nhạc + SFX) sinh 164 nhóm nhiễu và ra kết luận sai |
| 50 | **Bảng kiểm 6 thanh của câu mẫu VoxCPM2 đếm bằng tay → sai** (29/10/2026): ghi "với" là thanh nặng, liệt kê từ không có trong câu. Script đóng gói `higgs_make_refs_voxcpm.py` viết cứng `ROOT = D:\TEST\Gax\Audi` (sai repo) | Đếm thanh bằng `tone_coverage` của `.work/voxcpm_do_mau.py`; đường dẫn tính từ `__file__`. Luật: `QUY_TAC_GIONG_MAU_VOXCPM2.md` |
| 51 | **Chú thích vai N1/N2 trong kịch bản không ghi giới/tuổi** (29/10/2026: 27/58 vị trí thiếu, 3 tập T21·T22·T25 hai vai trùng một giọng) → không ghép được giọng mẫu W1–W4 nếu không đoán | Chú thích vai PHẢI ghi **giới + tuổi** (nữ/nam × trẻ·thanh niên·trung niên·lớn tuổi); hai N cùng tập khác giọng. Đổi tuổi chỉ ở nhân vật minh hoạ, **kiểm lời thoại không mâu thuẫn** (T25 N2 nhắc "cha mẹ già" nên không đổi được). Bảng ghép: `TAO_GIONG_MAU_VOXCPM2.md` §3.1 |
| 52 | **Higgs: giọng mẫu nghe khác nhau ≠ bản clone khác nhau** (30/10/2026): `H.wav` 108 Hz và `D.wav` 128 Hz bị Higgs kéo về cùng ~125 Hz (0,22 nc); chữa bằng `M_HIGH` (192 Hz) thì D thành giọng nữ, cách C 1,03 nc → người nghe nhầm D với C. G9 cũ chỉ xét cặp cùng giới nên lọt | Đo F0 **trên bản Higgs clone**, không trên giọng mẫu. G9 xét **mọi cặp vai liền kề, kể cả khác giới**. Giọng nam rất trầm (≤ 96 Hz) Higgs giữ được; vùng 108–128 Hz bị hút về ~125 Hz. Số đo: `90_LUU_TRU/BaoCao_DoGiongMau_DC_20261030.md` |
| 53 | **Thẻ cảm xúc Higgs làm giọng nam vọt ~1 quãng tám** (pilot v9, 30/10/2026): Host sản xuất câu `sad` ra 203–228 Hz (6/15 câu cảm xúc lệch ≥ 4 nc so với câu neutral), D mới câu `surprised` ra 169–247 Hz → giọng nam nghe thành nữ, vi phạm G8 | Đo F0 **riêng câu có thẻ** so với câu neutral của cùng vai (`.work/_v9_final.py`); câu lệch ≥ 4 nc → sinh lại không thẻ hoặc chọn bản không lệch. Chưa dùng thẻ `sadness`/`surprise` cho vai nam khi chưa có quyết định |
| 54 | **VoxCPM2: seed quyết định cao độ hơn câu mô tả** (30/10/2026): cùng câu mô tả ra 90–195 Hz tuỳ seed; mọi take D đạt đều là seed 42 hoặc 7 | Muốn thêm ứng viên: giữ seed tốt, đổi câu mô tả; sinh nhiều ứng viên (`--candidates`/`--seeds`) rồi đo trên bản clone |
| 55 | **Đổi audio (đọc lại giọng / cắt lại nhạc) mà KHÔNG dựng lại hình → video lệch tiếng hàng trăm giây** (Tập 02, 31/10/2026): audio mới 1411,9 s nhưng `picture.mp4` dài **1554,3 s** (bảng shot dựng 25/10 từ timeline cũ) ⇒ đóng gói `-shortest` **cắt mất thẻ kết** và hình lệch dần tới **142 s**; `mtime` bảng shot vẫn CŨ HƠN mp4 nên bẫy #37 không bắt được | `parse_shots.py` lấy mốc thời gian **chỉ từ timeline** ⇒ **đổi audio = phải chạy lại `parse_shots.py` + `build_video3.py`**, không chỉ `package.py --mux`. **Cổng bắt buộc trước khi đóng gói**: (1) so thời lượng `picture.mp4` với `timeline.total` — lệch > 0,05 s là phải dựng lại; (2) trích khung tại `timeline.total − 2 s` từ chính mp4 và xem thẻ kết có thật không (ảnh tĩnh không bảo chứng); (3) trích khung tại `timeline.total − 140 s` để thấy hình đang ở đâu — nếu vẫn là giữa hồi 5 thì cả tập đang lệch |
| 56 | **`script_tapXX.json` lệch kịch bản mà không ai biết** (Tập 03, 31/10/2026): JSON 220 câu, kịch bản sau review chỉ tách ra 218 ⇒ mã câu hồi 2, 4, 5 lệch; bảng shot dựng trên mã cũ | Sửa kịch bản xong PHẢI chạy lại `parse_kichban.py <md> <json>` (script **bắt buộc 2 tham số**, chạy thiếu sẽ IndexError và JSON cũ vẫn nằm đó) rồi so số câu |
| 57 | **Payload Higgs Tập 02 làm tay, không script nào sinh lại được** — chứa 3 phép đổi chữ ngầm (bỏ `...`, `<#0.35#>`→`<\|prosody:pause\|>`, bỏ ngoặc ngoại ngữ G7) | Dùng `export_higgs_payload.py` (QUY_TAC_AUDIO_HIGGS §7); kiểm hồi quy `AE_EP=02 … --check` |
| 58 | **Kịch bản đổi số câu ⇒ MỌI file khoá theo mã câu lệch theo** (Tập 03, 31/10/2026): `acting_tapXX.json` (lời đọc riêng `alt`), `sfx_tapXX.json`, `tts_manifest_tXX.json`, bảng shot vẫn theo 220 câu cũ ⇒ Higgs đọc câu 5.02#12 thành câu khác và đọc **lại câu cũ vi phạm V9** ở 2.06#2 (CER không bắt được vì CER so với chính chữ đã gửi) | Sau khi tách lại kịch bản: (1) đối chiếu mọi mã câu trong acting/sfx/edition theo **nội dung** câu cũ → mới; (2) so mọi `alt` với câu hiện tại; (3) sinh lại `tts_manifest`. Câu đã sinh sai chữ: loại bằng `--exclude`, sinh lại bằng `build_spec_r2.py --ids` |
| 59 | **`loudnorm linear` không ép được đỉnh thật** (Tập 03 Higgs, 31/10/2026): WAV −1,2 / mp3 −1,0 dBFS > −1,5 | `build_audio3.py` tự đo đỉnh mp3; vượt −1,5 thì giới hạn đỉnh −2,5 dBFS rồi nén lại (Tập 03 → −1,7). Tập đã đạt không đổi |
| 60 | **Higgs đọc một câu ngắn của Host trầm ~5 nửa cung ở MỌI bản** (Tập 03 1.03#8 "…hắn đã giết mẹ mình.", 6/6 bản ~95 Hz) — sinh thêm không sửa được | Giữ bản CER tốt nhất, đưa vào danh sách nghe; `build_spec_r2.py` nay đưa câu có mọi bản bị loại vào vòng sau |
| 61 | **Giọng mẫu ngôn ngữ khác sinh độc lập = nhân vật khác; dùng chung tên/thư mục = ghi đè giọng đã chốt** (31/10/2026): bộ `voice_ref_voxcpm2_en` (30/10) sinh trước vòng D/C mới nên D/C EN không phải D3_SH/C2_AB03; clip VN tên trần (`H.wav`) nằm chung dataset sẽ bị clip EN cùng tên ghi đè; chuỗi Higgs chưa có `AE_LANG` | **Tách riêng hoàn toàn** bộ VN và EN: thư mục, dataset Kaggle `…-voxcpm2-en`, `g9_role_map_EN.json`, clip đuôi `_EN`; code tự chặn trộn ngôn ngữ. Bộ EN sinh theo câu mô tả + seed của giọng VN đã chốt, đo F0 + nghe so VN↔EN (Higgs §4.4). **Đã đo en2: cùng seed KHÔNG giữ giọng** (D seed 7: VN 88 Hz → EN 85–145 Hz) ⇒ seed chỉ là điểm xuất phát, danh tính do tai người dùng chốt |
| 62 | **Kaggle CLI tải output có thể thiếu file** (Tập 02 EN hồi 4, 31/10/2026): lượt đầu được 100/102 wav, mất cả `higgs_manifest.json` — CLI phân trang (`--page-size` mặc định 20, max 200) + phiên CLI gián đoạn | `watch_kernel.py` nay tải manifest rồi tải bù đúng tên file còn thiếu theo lô < 200, in "thieu N". Cổng P5: dòng "sau tai bu: thieu 0" |
| 63 | **Bộ lọc "câu bị chặn" của `measure_cer_prod.py` bắt chữ `safety` trần** ⇒ loại nhầm câu EN "…boundaries of safety…" (5.12#3) — ASR thật ra đúng 100% | Chỉ bắt câu báo chặn ("This request was blocked", "blocked by", "blocked due to safety"). Khi một câu "thiếu ASR", đọc cache trước khi kết luận |
| 64 | **`alimiter` của ffmpeg chèn trễ `attack` ms và không bù trễ ⇒ âm thanh lệch hình 5 ms + một "tiếng click" full-scale** (Tập 04, 31/10/2026): `package.py` ghép `-af alimiter=limit=0.7943:attack=5:release=50:level=disabled` (A11 #38). Kết quả: file cuối đo **true peak 0,0 dBFS** (vượt trần −1,5 của A7) và âm thanh lệch WAV master **+239 mẫu = 4,98 ms** ở mọi điểm đo. Trùng hợp: master WAV đã ở −2,5 dBFS nên limiter **không kích hoạt**, nhưng đường trễ vẫn gây burst 13 mẫu full-scale tại 869,496 s (nguồn chỉ có −4.345) — mã hoá lại cùng đoạn thì **không lỗi** ⇒ lỗi ở bộ lọc, không ở AAC | **Thêm `latency=1`** vào chuỗi limiter: `alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1` ⇒ true peak −1,8 dBFS, hết burst, lag 0 mẫu. Thêm khoá `mux_af` trong `EPISODES[*]` để **mỗi tập tự chọn chuỗi filter lúc ghép** (T04 dùng chuỗi có `latency=1`; T01/T02 giữ chuỗi cũ). Khi ghép lại tập nào cần **đo lại true peak trên chính mp4** + **đo lag âm thanh–hình** (tương quan tín hiệu WAV master với audio giải mã từ mp4) |
| 65 | **Cổng QC báo lỗi giả vì đo sai thứ cần đo** (Tập 04, 31/10/2026): (a) *"lời đầu = 1256,52 s"* — `silencedetect` trên hỗn hợp **có nhạc nền** không tìm thấy khoảng lặng nào ⇒ `silence_end` đầu tiên rơi vào cuối tập ⇒ phải đo trên **stem giọng** (`.work/stems_tXX/*.wav`, 16 kHz, chỉ giọng): T04 = 23,07 s; (b) *"324 cue ≠ 154 câu"* — `subtitles.py` **tách câu dài thành nhiều cue** (2 dòng × 42 ký tự, ≤ 6 s) nên phải so **nội dung** (bỏ nhãn vai rồi so chuỗi phụ đề với lời kịch bản), không so số cue; (c) *"thẻ kết OK"* chỉ vì PNG đen vẫn 44 KB ⇒ phải **đo tỉ lệ pixel sáng** của khung thẻ kết, không xem kích thước file | Ba cổng trên đã vá trong `.work/qc_video_t04.py`: `first_speech(master, ED.w("stems"))`, gate E so nội dung phụ đề, gate G đo `% pixel sáng` (T04: 18,45 % tại 1248,0 s). Lưu ý: khung tại `total − 2 s` **đen** là do renderer mờ dần 3 s cuối (dùng chung T01–T03) ⇒ kiểm thẻ kết ở **giữa shot cuối**, không ở khung cuối |
| 66 | **`vi_numbers` làm hỏng số thập phân** (Tập 05, 01/11/2026): "1.44 Megabyte" thành **"một.bốn mươi tư"** (dấu chấm chỉ được hiểu là phân cách nghìn khi đủ 3 chữ số); Tập 03 "0,13%" thành "không,mười ba". Lỗi lọt vào payload Higgs lượt 1; chỉ lộ nhờ ASR chép lại "1.44" | Thêm luật số thập phân trong `tts_sentences.vi_numbers`: `\d+[.,]\d{1,2}` → "X phẩy Y". Kiểm hồi quy 1.524 câu VN mọi tập: chỉ đổi 2 câu (T03 1.13#2, T05 4.04#8); Tập 01 không đổi. Khi đổi chữ một câu đã sinh: thêm mọi bản cũ vào `higgs_exclude_f0_tXX.json` rồi sinh lại ở vòng 2 |
| 67 | **Tách lại kịch bản (số câu đổi) làm bảng shot + phụ đề mất hiệu lực mà không ai báo** (Tập 05, 01/11/2026): kịch bản Higgs đổi 164 → **162 câu** (2.02 4→5, 2.04 10→8, 4.02 9→10, 4.12 8→6 bỏ lời thoại trực tiếp) trong khi mục 6 của hồ sơ vẫn trỏ mã cũ ⇒ `parse_shots.py` **KeyError**; các element giữ nguyên số câu nhưng **câu bị viết lại** ⇒ chữ trên hình (số, trích dẫn) không còn nằm trong câu đang đọc, vi phạm H6/V3 | Mỗi lần kịch bản đổi: (1) **QC bảng shot trước khi dựng** — `qc_shots_t04.py --ep XX` (bản riêng cho T05: `_qc_shots_t05.py`, có whitelist *có ghi chú*) để bắt "mã câu không tồn tại", "thiếu câu", "số không có trong câu", "trích dẫn không nguyên văn"; (2) **sửa bảng shot theo nội dung câu mới** (map cũ→mới bằng diff nội dung, không đoán số thứ tự) — dải mã câu, chữ trên hình, trích dẫn, và **nền** khi chủ đề câu đã bị gỡ khỏi kịch bản; (3) `parse_shots.py` → `subtitles.py` → ảnh tĩnh `--stills all` → soi mắt → mới dựng hình |
| 68 | **Báo cáo G10 ghi sai tên giọng sau khi đổi engine TTS** (Tập 05, 01/11/2026): `voice_role_check.py` in nhãn vai bằng `ED.CAST[role][0]` — tức tên giọng **MiniMax** (`English_CaptivatingStoryteller`, `Korean_ColdYoungMan`…) — trong khi audio đã chạy **Higgs Audio v3** với file tham chiếu `H.wav / D3_SH.wav / C2_AB03.wav / W6_LOW.wav / W5_HIGH.wav` ⇒ báo cáo nói sai giọng thật đã dùng để dựng. Lưu ý: `tts_manifest_tXX.json` **không có** field `ref_wav` (chỉ có `voice` kiểu MiniMax); `ref_wav` nằm ở `higgs_selection_tXX.json` | Nhãn giọng phải lấy từ **nguồn audio thật của tập**: đọc `ref_wav` trong `higgs_selection_tXX.json` (tệp chỉ tồn tại ở tập đã chạy Higgs) ⇒ in `` `H.wav` (Higgs Audio v3) ``; tập không có tệp này (MiniMax) thì giữ nguyên `ED.CAST[role][0]`. **Sửa script dùng chung ⇒ phải kiểm hồi quy Tập 01** (L9): chạy `_verify_voice_label.py` trên các tổ hợp (vi/en × tập 01–07) và chứng minh nhãn Tập 01 **không đổi**; báo cáo đang tồn tại của tập khác sửa tay bằng đúng logic của script đã vá, **không** sửa tay lệch logic |
| 69 | **Higgs sinh đuôi gần câm ~40 s mà CER vẫn 0%** (Tập 02 JA, 01/11/2026): 2/203 file dài đúng 47,6 s (= trần `max_new_tokens`), sau lời là −61…−72 dB; nền môi trường trong master che nên `silencedetect` −60 dB báo 0 khoảng câm ⇒ master thừa 82,5 s chết | Sau P9, trước khi duyệt master: quét mọi file trong `audio_s_higgs_*` tìm đoạn cuối < −45 dB dài > 0,8 s (nghi nhất: file dài ≈ trần token); cắt giữ 0,3 s + fade 30 ms (sao lưu gốc), chạy lại `build_audio3.py` — **không** chạy lại `finish_prod.py` (nó cài lại file gốc) |
| 70 | **File mô tả `mo_ta.txt` là file SINH RA — sửa tay bị ghi đè mất** (Tập 02, 02/11/2026): `.work/package.py` `description()` viết lại `mo_ta.txt` + `nguon_tham_khao.md` mỗi lần chạy; sửa tay trong file thành phẩm là **sửa trên bản sao**, lần chạy pipeline sau ghi đè sạch | Muốn đổi mô tả ⇒ sửa **generator + cấu hình tập**: `package.py` (template) + `edition.py` (`act_titles`, khoá mới `roles_line`). Chạy lại `AE_EP=XX python .work/package.py` **không kèm `--mux`** (chỉ sinh mô tả + thumbnail, không ghép lại video). Sau đó **kiểm hồi quy Tập 01** (L9) bằng cách sinh thử trong bộ nhớ (chặn `Path.write_text`) rồi diff — không chạy thật để khỏi đụng file Tập 01 |
| 71 | **Mốc chương hardcode lệch với thẻ hồi thật trên màn hình** (Tập 02, 02/11/2026): `package.py` hardcode `starts = {1: 20.5}` ⇒ mô tả ghi `00:20 Hồi 1` nhưng thẻ "HỒI 01" hiện lúc **~22,0 s** (intro kênh 22,41 s, lời đầu 23,0 s) ⇒ người xem bấm chương vẫn thấy intro. Mốc hồi 2–5 lấy từ ACT marker trong `timeline_s*.json` ⇒ **đã đúng** (303,64 / 519,59 / 812,09 / 1.112,64 s) | Lấy mốc hồi 1 từ `timeline["intro"]` (`TL.get("intro", 20.5)` — mọi timeline tiếng Việt đều = 22,41 s) ⇒ `00:22`. **Đo lại trên chính mp4**: trích frame tại từng mốc, thẻ hồi phải hiện trong **±1 s**. Kiểm hồi quy Tập 01: chỉ đổi đúng 1 dòng (`00:20` → `00:22`), tên hồi và câu disclaimer giữ nguyên |
| 72 | **Dòng hashtag cuối mô tả chỉ có ở bản EN** (02/11/2026): `CHU_CO_DINH_EN.md` có dòng `#TrueCrime #CriminalPsychology …`, còn template VN/JA/KO **không có** ⇒ video tiếng Việt đăng lên YouTube không có tag nào. Không có quy ước hashtag nào trong `AGENTS.md`/tiêu chuẩn | Thêm khoá `EPISODES["XX"]["hashtags"]` (`edition.py`) + `package.py` đọc khoá đó **chỉ ở nhánh VN** (EN lấy từ `CHU_CO_DINH_EN.md`, JA/KO chưa có). Bộ tag = tag EN của tập + `#TamLyToiPham #PhamVan #HoiTo` (người dùng chốt 02/11/2026). Sinh lại bằng **gọi `description()` trực tiếp**, không chạy CLI (CLI còn gọi `thumbnail()` ⇒ **ghi đè thumbnail đã xuất** của tập cũ). File nguồn `nguon_tham_khao.md` sinh lại có thể **đổi** nội dung trích dẫn nếu kịch bản đã viết lại ⇒ kiểm `git diff` sau khi sinh |
| 73 | **`measure_cer_prod.py` báo "0/N câu vượt ngưỡng" khi ASR KHÔNG chạy** (Tập 06, 02/11/2026): `mcode-tools` nằm ở thư mục `.minimax/bin` của người dùng, không có trong PATH của phiên Claude Code ⇒ mọi lượt ASR lỗi, script nuốt lỗi và in báo cáo "đạt" giả (CER "-" mọi vai, ASR 7 s cho 309 file). AI còn kết luận nhầm "máy không có mcode-tools" | Thêm `.minimax/bin` vào PATH trước khi đo. Script đã vá: quá nửa file không có bản chép ⇒ thoát mã 2, không ghi báo cáo (hồi quy Tập 05: rows + report giống từng byte). Dấu hiệu nghi: ASR vài giây cho hàng trăm file |
| 74 | **Whisper large-v3 tiếng Việt bịa câu** (Tập 06, 02/11/2026): 1 file D 13,5 s bị chép thành *"Hãy subscribe cho kênh Ghiền Mì Gõ…"* (CER 82%) trong khi `listen_audio` chép đúng; Whisper còn hay bỏ chữ đầu câu ("Thế nhưng"→"Nhưng"). Hai ASR chỉ trùng 12 câu > 2% | Whisper + UTMOS chạy trên Kaggle (`build_qc_nb.py`; CER ở máy bằng `qc_whisper_cer.py`) làm **phép thử thứ hai**; `listen_audio` vẫn là chuẩn chọn bản. Câu cả hai ASR cùng báo lỗi ⇒ nghe trước. UTMOS (mô hình tiếng Anh) chỉ so tương đối |
| 75 | **Host đọc trầm ~4 nc ở mọi seed với một số câu** (Tập 06: 3.11#3, 3.13#1, 5.06#12 — mọi bản ~90–100 Hz qua 2 vòng) | Thêm từ dẫn đầu câu ("Khi tin tức lan đi, …", "Trong khi đó, …", "Vì vậy, xin quý vị …") — người dùng duyệt — vòng 3: lệch còn −1,2 / −2,1 / −2,6 nc, CER 0%. Bản cũ của câu đổi chữ vào danh sách loại (#66) |
| 76 | **CER không bắt được sai đại từ** (Tập 07, 03/11/2026): câu 4.06#2 "Ông ta viện dẫn…" — bản CER thấp nhất (2,1%) đọc **"Cô ta"** (đổi giới tính người nói), bản 2,7% đọc đúng. Đổi 1 âm tiết đầu câu chỉ tốn ~2% CER nên chọn theo CER tự động lấy nhầm | Với câu < 3% CER, đọc bản chép của các bản ứng viên, ưu tiên bản đúng **đại từ / tên / số** hơn bản CER thấp hơn vài phần trăm; ghi lý do chọn tay vào `higgs_selection_tXX.json` (trường `note`) và sao lưu bản tự chọn |
| 77 | **Cột "Nhân vật" của bảng shot Tap06 đặt mã handoff `→X` SAI CỘT ⇒ badge "TIẾP THEO" chưa bao giờ hiện** (Tập 06, 02/11/2026): Tap06 đặt `→N1`/`→D` ở **cột chuyển cảnh (cột 9)** trong khi `parse_shots.py` đọc handoff từ **cột Nhân vật (cột 8)** ⇒ `flags["handoff"]` rỗng ở **0/73 shot** (Tap04 có 7, Tap05 có 2). Lỗi nằm trong bảng mục 6 ⇒ chạy lại `parse_shots.py` cũng không hết | `→X` **phải nằm ở cột 8** (cùng cột `✦`/`🅑`/`⊘`), cột 9 chỉ dành cho `✂`/`◼`. Quy tắc: **`handoff(dòng i) = vai của dòng i+1`** (quy tắc này tái tạo đúng bảng gốc Tap04/Tap05 ⇒ dùng để kiểm). QC bảng shot **phải có cổng chuỗi handoff**, không chỉ cổng "phủ câu" — `_qc_tap06_shots_v2.py` (10 cổng) |
| 78 | **Bảng shot viết cho bản kịch bản cũ vẫn "hợp lệ" về cú pháp nhưng sai 10 dòng về nghĩa** (Tập 06, 02/11/2026): kịch bản tách 165→154 câu; bảng shot cũ trỏ mã cũ ⇒ `parse_shots.py` **không báo lỗi** (mã cũ vẫn là chuỗi hợp lệ) nhưng: **10 dòng sai cột Vai** (badge + bán thân hiện **sai người nói**), số trên hình không có trong câu (`13 · 03 · 1980` trong khi kịch bản ghi **12**/3), câu trích không nguyên văn (`"MẸ ƠI, MẸ ĐỢI CON VÀI PHÚT NHÉ"`, `"Kiss my ass"` — đã bị gỡ khỏi kịch bản), nền không còn khớp câu, và 1 câu mới không có shot | QC bảng shot phải có **4 cổng nội dung** (không chỉ phủ câu): (1) **vai khớp vai trong script** (map `N`→`N1`/`N2` theo `EPISODES[*]["n_element"]`); (2) **mọi con số trên hình có trong câu của shot** (đối chiếu cả dạng chữ: "hai mươi tư" = "24"); (3) **câu trích nguyên văn** (ngoặc kép “…” phải là cụm từ có thật trong câu); (4) **nền khớp chủ đề câu**. Sửa bảng shot bằng **map cũ→mới theo nội dung câu**, không đoán số thứ tự (`#67`) |
| 79 | **`⊘` (tắt bán thân) trong bảng shot bị bỏ sót ở đúng những khoảnh khắc nặng nề nhất** (Tập 06, 02/11/2026): quy tắc B2 của hồ sơ Tập 06 liệt kê 5 khoảnh khắc phải tắt bán thân (nắp hầm crawl space · khai quật · sông Des Plaines · buồng tử tù Menard · phòng thi hành án Stateville) — bảng shot cũ **không dòng nào** có `⊘` ở Hồi 3/5 | Áp `⊘` cho đúng các shot đó khi viết lại bảng shot. `⊘` là cờ **độc lập** với handoff ⇒ hàng có `⊘` vẫn được mang `→X` (2 cờ khác nhau trong cùng cột 8). Cờ `✦` lần đầu là **vô hại**: renderer chỉ hiện thẻ nhân vật tại `FIRST_TURN[role]` (lượt đầu tiên của vai trong cả tập) nên `✦` lặp ở shot sau là vô nghĩa |
| 80 | **Tập có `mux_af` riêng mới có `latency=1` — tập KHÔNG có khoá đó sẽ lệch âm thanh 5 ms** (Tập 06, 02/11/2026): `package.py` mặc định dùng chuỗi limiter **không** `latency=1`; `EPISODES["06"]` cũng chưa có khoá `mux_af` ⇒ giới hạn đỉnh chạy trên master có đỉnh −1,6 dBFS (cao hơn ngưỡng −2,0 dBFS của `limit=0.7943`) ⇒ limiter **có kích hoạt** ⇒ chèn trễ `attack` 5 ms ⇒ âm thanh lệch hình 5 ms + burst full-scale | **Mọi tập dựng lại bằng giọng mới (Higgs) phải có `mux_af` kèm `latency=1`** trong `EPISODES["XX"]`. Sau khi ghép: đo true peak **trên chính mp4** (A11 #38) và đo **lag âm thanh–hình** bằng tương quan giữa WAV master và audio giải mã từ mp4 (A11 #64) — đạt khi lag = 0 mẫu |
| 81 | **Căn chỉnh bảng shot theo VỊ TRÍ (`difflib` positional) cho kết quả SAI** (Tập 07, 03/11/2026): kịch bản tách 164→147 câu; căn chỉnh theo thứ tự dòng lệch ngay từ element `1.07` ⇒ tin máy thì 1 shot đổi hẳn câu (sai người nói, sai nền, sai chữ) | Map cũ→mới bằng **KEY trong `make_acting_tapXX.py` + nội dung câu**, không theo vị trí. Đối chiếu bằng script: `.work/qc_final_t07/_diff_script_t07.py` (82 câu đổi: 59 đổi chữ · 20 xoá · 3 thêm) + `_diff_plan_detail.py` (diff bảng shot **theo từng cột**, 27 dòng đổi mã câu) |
| 82 | **Mẫu T8 (cờ) chỉ hiện CỜ, mất TIÊU ĐỀ, nếu caption không bắt đầu bằng số** (Tập 07, 03/11/2026): 3 shot cờ đỏ dùng caption viết tay "Cảnh báo đỏ N: …" ⇒ renderer không vẽ tiêu đề ⇒ **mất thông tin chính trên hình** mà mọi cổng QC vẫn xanh (lỗi chỉ lộ khi **soi bằng mắt**) | Caption của shot T8 phải theo định dạng renderer hiểu (mẫu Tập 01): `*01* · **CẢNH BÁO ĐỎ 1 — CẢNH GIÁC…**` ⇒ số cờ tô đầy đúng (Đỏ 3 → 3 cờ). Sửa caption ⇒ **render lại ảnh tĩnh của các shot đó** rồi soi lại; đừng dựng lại cả tập chỉ để sửa caption |
| 83 | **Link 403 KHÔNG phải link dùng được — "mở bằng trình duyệt" không cứu được** (Tập 06, 02/11/2026): trong 50 URL ứng viên, **6** nguồn trả 403 (Cloudflare/bot-block: Britannica, People, CBS Chicago, FBI.gov, NBC Chicago) và **7** trả 404 (sai slug). Một số nguồn rất "uy tín" nhưng **không tải được nội dung** ⇒ không thể đối chiếu dữ kiện ⇒ phải loại, không được ghi vào bảng nguồn chỉ vì "mở được bằng trình duyệt" | Kiểm chứng link nguồn bằng **HTTP status thật + đọc được nội dung**, không dựa vào **snippet của search**. Nguồn dùng được phải có **200** và tải về ≥ 500 byte. `journal-topics.com` timeout ⇒ loại (thay bằng Esquire/Oxygen/TheWrap). Nguồn thay thế phải mở được: `supreme.justia.com` 403, `murderpedia` 409, `web.archive.org` 429 ⇒ loại hết |
| 84 | **Bảng nguồn phải sinh bằng GENERATOR có validator, không gõ tay** (Tập 06, 02/11/2026): bảng nguồn là file **sinh ra** (`xuat_ban/nguon_tham_khao.md` bị `package.py` ghi đè mỗi lần chạy — A11 #70) ⇒ chỉ sửa được ở `02_SAN_XUAT/TapXX/nguon_*.txt` + `edition.py`. Gõ tay 58 dòng × 20 nguồn = 58 cơ hội lệch mã câu / lộ 1 URL sai | Generator `.work/_gen_t06_sources.py` có **4 cổng chặn ghi file**: (1) mọi URL phải có meta **200** trong cache `.work/_src_cache/` **và** nội dung ≥ 500 byte; (2) mọi mã câu phải tồn tại thật trong `script_tapXX.json`; (3) khoá nguồn hợp lệ **và mọi nguồn đều phải được dùng** (nguồn thừa cũng bị chặn); (4) không trùng mã câu. Cùng bộ `need` trong `EPISODES["06"]` phải khớp đúng 58 mã câu |
| 85 | **Khối nguồn trong mô tả YouTube vượt giới hạn 5000 ký tự** (Tập 06, 02/11/2026): 20 nguồn với nhãn dài + mô tả dài = **3903 ký tự** ⇒ `mo_ta.txt` lên **5467 ký tự** ⇒ **vượt trần YouTube** ⇒ video không đăng được mà không ai báo | Khối nguồn dùng **nhãn ngắn 1 dòng + URL**, mô tả dài để ở bảng nguồn ⇒ còn **2503 ký tự**, `mo_ta.txt` = **4067 ký tự**. Validator phải đo `len(mô tả) < 5000` **trước khi ghi**, và chặn file nếu có BOM/byte NUL. Sinh lại bằng `description()` **trực tiếp** (A11 #72) để không ghi đè `thumbnail.png` |
| 86 | **Mô tả YouTube giới hạn 5.000 ký tự — phải ĐO file thật, không ước lượng** (Tập 07, 03/11/2026): khối nguồn 54 mục làm `mo_ta.txt` lên **5.127 ký tự**; cách tính “phần đầu + khối nguồn” bỏ sót **phần đuôi** (dòng 🆘 + hashtag) nên vẫn tưởng vừa ⇒ phải sinh file rồi đếm ký tự thực, cắt dần số nguồn cho tới khi ≤ 5.000. Nguồn dùng cho mô tả lấy **nhãn rút gọn**; danh mục đầy đủ để ở `nguon_tham_khao.md`. Cơ chế: `package.py` đọc `02_SAN_XUAT/<Tap>/nguon_mo_ta.txt` (khối nguồn trong mô tả) + `02_SAN_XUAT/<Tap>/nguon_tham_khao.md` (bảng đối chiếu từng câu) ⇒ **chạy lại `package.py` không làm mất nguồn**. Nhóm tiêu đề `▸` phải render **theo nhóm**, không theo thứ tự ưu tiên, nếu không nguồn sẽ nằm sai nhóm |
| 87 | **Hai nguồn ghi hai ngày khác nhau KHÔNG có nghĩa kịch bản sai** (Tập 06, 02/11/2026): nghi vấn "ngày phán quyết 12/3/1980 vs 13/3/1980" (Wikipedia ghi 13/3, kịch bản ghi 12/3) — tưởng sai. Hồ sơ viện chưởng viện làm rõ: **12/3 = phán quyết có tội**, **13/3 = ngày tuyên án** ⇒ kịch bản đúng, **không sửa** | Khi nguồn xung đột về ngày, **đọc hồ sơ gốc** (biên bản tòa) để tách "ngày Xảy ra" vs "ngày Xử lý" trước khi kết luận kịch bản sai. Sửa kịch bản = dựng lại toàn bộ (TTS → ảnh → video 28 phút → phụ đề → đóng gói) ⇒ cần người dùng quyết (L4) |
| 88 | **Bảng shot Tập 07 không có DÒNG HANDOFF nào (0/62)** (Tập 07, 03/11/2026): cột "Nhân vật" chỉ có `✦`/`⊘` ⇒ badge "TIẾP THEO" **chưa bao giờ hiện** ở Tập 07 (cùng lớp lỗi với #77 ở Tap06, nhưng ở dạng **thiếu hẳn** chứ không sai cột) | Tính lại theo quy tắc `handoff(dòng i) = vai của dòng i+1` ⇒ 27/66 shot có handoff. QC bảng shot **phải có cổng chuỗi handoff** (đối chiếu `→X` với vai dòng kế tiếp) **và** cổng "cột chuyển cảnh phải trống" |
| 89 | **Số liệu so sánh "bản cũ vs bản mới" phải ĐO bằng script, không nhớ/suy đoán** (Tập 07, 03/11/2026): AI suýt chép con số của **Tập 06** ("54 shot > 15 s") vào báo cáo Tập 07; đo lại bằng script ra **47/62 (76 %)**, TB 20,6 s, dài nhất 40,5 s — số đúng khác hẳn | Mọi con số trong báo cáo phải **truy về script đã chạy** (giữ log trong `.work/qc_final_t07/`). Trước khi ghi báo cáo: spot-check bằng mắt 5–8 dòng của bảng sinh ra, đối chiếu với dữ liệu thật — tin script tự kiểm là tin **không** kiểm |
| 90 | **H10 có 2 vế (3–15 s · không lặp nền > 4 shot) nhưng KHÔNG vế nào có cổng QC** (Tập 07, 03/11/2026): đo tay bằng mắt trên contact sheet ⇒ dễ bỏ sót; cần đo bằng script trên `shots_tXX.json` | Dùng `.work/qc_final_t07/_qc_h10_t07.py`: thời lượng từng shot (TB / max / số shot > 15 s) + chuỗi nền liên tiếp (đoạn dài nhất). Tập 07 đo được: 66 shot · TB 16,9 s · max 32,0 s · **0** đoạn lặp > 4 shot (bản cũ: 62 shot · TB 20,6 s · max 40,5 s · 47/62 > 15 s) |
| 91 | **`music_drop` đặt lên quãng nghỉ có nền môi trường thưa → câm 0,47 s** (Tập 04, 31/10/2026: tắt nhạc `4.08#5`–`4.11#1`, nền `fx_glasses_clink` chỉ là tiếng ly chạm rời rạc) | Khoảng tắt nhạc chỉ phủ câu **có lời**; quãng nghỉ dưới khoảng tắt nhạc phải có nền `amb_*` liên tục, không dùng `fx_*`. Kiểm `silencedetect` sau mỗi lần đổi `sfx_tapXX.json` |
| 92 | **F0 câu rất ngắn (≤ 3 từ) không tin được** (Tập 04 `2.08#1` "Đúng như vậy.": AC 94–115 Hz, YIN 122–159 Hz trên cùng file → bị loại G8 cả 4 bản dù CER 0%) | Câu ≤ 3 từ bị G8 loại: không chạy thêm vòng, đưa vào danh sách nghe |
| 93 | **Sửa 1 câu kịch bản của tập đã dựng bằng Higgs = cần chạy lại Kaggle GPU** (Tập 06, 03/11/2026): đổi bất kỳ câu nào ⇒ phải tạo lại file TTS của câu đó ⇒ **engine Higgs Audio v3 của dự án chỉ chạy trên Kaggle GPU** (`QUY_TAC_AUDIO_HIGGS.md` §PHẠM VI: chạy chỗ khác = **engine mới**, phải đo lại CER/G8/G9 từ đầu). Máy dựng (Windows, không GPU) đo ngày 03/11/2026: không `nvidia-smi`, không `kaggle` CLI, không `~/.kaggle/kaggle.json`, không module `kaggle`/`torch`/`mlx_audio` ⇒ **không tạo lại được TTS** ⇒ không dựng lại được tập | **Kiểm tra engine TTS CÓ chạy được ở máy hiện tại TRƯỚC khi hứa dựng lại** — đừng sửa kịch bản rồi mới phát hiện không có GPU. Nếu thiếu: (1) **đóng gói sẵn gói sửa** (câu hiện tại trích tự động từ `script_tapXX.json` + câu đề xuất + nguồn + tên file WAV cần tạo lại + quy trình 6 bước) rồi **dừng**; (2) ghi blocker vào hồ sơ + báo cáo QC + A11; (3) để người dùng quyết có chạy 1 lượt Kaggle hay không. **Chỉ sửa chữ trên hình thì không cần TTS**, nhưng vẫn phải khớp timeline âm thanh ⇒ làm cùng đợt |
| 94 | **Chữ trên hình là một nguồn khẳng định — cổng "số trên hình có trong câu" KHÔNG bắt được loại lỗi này** (Tập 06, 03/11/2026): audit 73/73 caption cho ra 4 lỗi mà mọi cổng QC vẫn xanh: `2-15` "RÚT TIỀN MẶT CHUẨN BỊ BỎ TRỐN" (không nguồn nào xác nhận) · `3-03` "NẮP HẦM KỸ THUẬT **PHÒNG NGỦ**" (nguồn: trap door trong **tủ quần áo**) · `5-07` "BÀI HỌC KINH ĐIỂN TẠI **HỌC VIỆN FBI**" (không nguồn nào nhắc FBI Academy) · `1-05` "gần **một thập kỷ**" (nguồn: các vụ giết 1972–1978 = 6 năm). Vì đây là *hành vi* khẳng định chứ không phải *số* ⇒ cổng số không bắt được | Thêm cổng QC mới: **caption có mệnh đề khẳng định hành vi/sự kiện cụ thể thì phải có nguồn**, không chỉ số. Cách làm: audit caption của **từng shot** đối chiếu câu kịch bản (`.work/_audit_caption_tXX.py`) rồi grep nguồn theo từ khoá của từng caption đáng nghi. Khi sửa caption mà **không** sửa câu ⇒ chỉ cần render lại ảnh tĩnh của các shot đó, **không** cần TTS |
| 95 | **Thêm mục vào bảng A11 mà không quét số đã dùng ⇒ TRÙNG SỐ, mọi trích dẫn `A11 #N` trỏ nhầm mục** (Tập 07, 03/11/2026): bảng A11 là bảng đánh số, mọi tài liệu + script trong repo trích dẫn nó theo số. Trong 2 lượt liên tiếp đã thêm mục mà không kiểm số đã dùng ⇒ trùng ở **62, 63** (2 mục Tập 04 chen giữa), **76** (3 mục khác nhau cùng mang #76: handoff Tập 06 · sai đại từ Tập 07 · handoff Tập 07), **82 / 83 / 84** (mỗi số 2 lần) ⇒ 3 tài liệu trích `#76` cho 3 ý nghĩa khác nhau, **không ai báo lỗi** vì bảng Markdown vẫn hiển thị bình thường | **Thêm mục bằng SCRIPT, không gõ tay**: đọc file, quét cột `#` để lấy số lớn nhất, cấp số = max+1, rồi **kiểm lại toàn bảng**: các số phải liên tiếp 1..N và **không trùng** (validator chặn ghi nếu trùng). Khi phải **đánh số lại** (vá một mục cũ làm lệch cả đuôi bảng) thì **đánh số lại theo thứ tự vật lý** cho tới khi liên tiếp, và **sửa mọi trích dẫn bên ngoài** theo bảng ánh xạ cũ→mới — kiểm bằng script quét repo tìm `A11 #N` rồi đối chiếu tiêu đề mục N (đừng tin mắt). Có 2 mục từng trùng số nhưng **không mục nào trích dẫn chúng** ⇒ chỉ sửa được khi chuyển mục đó xuống cuối bảng, **không** dời số mục giữa bảng (sẽ phá hàng loạt trích dẫn đang đúng) |
| 96 | **Kaggle chạy kernel với BẢN DATASET CŨ dù `datasets status` đã `ready`** (Tập 06, 03/11/2026): đẩy kernel ngay sau `datasets version` ⇒ kernel gắn bản trước ⇒ vòng 4 chạy lại **spec vòng 3** (12 file cũ thay vì 24 file mới), `watch_kernel` vẫn báo "thiếu 0" vì so với manifest **của chính lượt đó** | Trước khi `kernels push`: tải `prod_spec*.json` (hoặc payload) **từ Kaggle về** (`kaggle datasets download -f …`) và kiểm có mã câu của vòng mới. Sau khi tải output: đếm file theo **mã câu mong đợi**, không chỉ tin "thiếu 0" |
| 97 | **`build_audio3.py` chỉ giới hạn đỉnh MỘT lần ⇒ master trượt cổng −1,5 dBFS** (Tập 06, 03/11/2026): `alimiter 0.75` + mã hoá mp3 vẫn ra **−1,3 dBFS**, script in số đo nhưng không chặn | Đã sửa: siết dần 0,75 → 0,70 → 0,65 → 0,60 tới khi mp3 ≤ −1,5, quá 0,60 ⇒ dừng mã lỗi. Lần đầu vẫn 0,75 ⇒ hồi quy Tập 05: master giống từng byte. Chạy `build_audio3.py` tay cho Higgs PHẢI đặt `AE_AUDIO_DIR=audio_s_higgs` (không đặt ⇒ đọc thư mục MiniMax) |
| 98 | **AI kết luận "máy không có kaggle CLI" ⇒ dừng cả tập** (Tập 06, 03/11/2026 — cùng kiểu lỗi `mcode-tools` ở #73): chỉ kiểm PATH + `~/.kaggle/kaggle.json` | Công cụ ngoài PATH trên máy này: `kaggle` = `%LOCALAPPDATA%/kaggle-venv/Scripts/kaggle.exe` · `mcode-tools` = `~/.minimax/bin`. Kết luận "không có" chỉ sau khi tìm trong tài liệu (QUY_TAC_AUDIO_HIGGS §7) **và** gọi thử lệnh thật (`kaggle kernels list --mine`) |
| 99 | **Đề xuất sửa kịch bản dựa trên con số sai** (Tập 06, 03/11/2026): báo cáo nguồn ghi lương tối thiểu liên bang 1978 = 2,35 USD và đề xuất đổi `1.08#1` sang "bang Illinois"; Bộ Lao động Mỹ ghi **2,65 USD** từ 01/01/1978 ⇒ câu gốc đúng, đề xuất sai | Con số dùng làm căn cứ sửa kịch bản PHẢI có nguồn gốc (cơ quan chính phủ, hồ sơ toà) trích **nguyên văn dòng số liệu**, không lấy số từ trí nhớ hay bài báo thứ cấp (L2) |
| 100 | **Pipe 4 KB mặc định của Windows khiến build video mất 34% throughput — đo được, không phải suy đoán** (Tập 06, 03/11/2026): 6 tiến trình chỉ render (không encode) = **12,6 fps**; cùng 6 tiến trình nhưng đẩy frame 6,2 MB qua pipe cho ffmpeg = **8,3 fps**. Pipe ẩn danh của Windows mặc định chỉ **4 KB** ⇒ mỗi frame phải qua ~1.550 vòng ghi/giác lịch. CPU lúc đó chỉ 330% python + 40% ffmpeg trên 12 luồng ⇒ **không phải kẹt CPU** | Tăng buffer pipe bằng cách **patch `_winapi.CreatePipe`** để `subprocess` tự tạo cả hai đầu (giữ nguyên cơ chế handle/EOF) ⇒ **11,58 fps**, đạt 92% trần render thuần. **Không** tự tạo pipe rồi trả về: làm vậy `p2cwrite = -1` ⇒ ffmpeg **không** nhận handle làm stdin ⇒ lỗi `Bad file descriptor`; và phải truyền `stdin=subprocess.PIPE` cho lời gọi `Popen` nếu không thì `p.stdin` là `None`. Áp dụng ở `.work/_build_video3_split.py` (biến thể) chứ không sửa `build_video3.py` dùng chung |
| 101 | **Máy bão hoà ở ~13 fps dù CPU chỉ 42% ⇒ nút thắt là băng thông bộ nhớ, thêm worker KHÔNG giúp** (Tập 06, 03/11/2026): 6 tiến trình = 12,6 fps · **10 tiến trình = 13,27 fps (+5%)** trong khi mỗi tiến trình chỉ dùng ~55% CPU ⇒ tổng ~42% của 12 luồng. Kết luận sai kinh niên "tăng `--workers` sẽ nhanh hơn" làm lần build đầu vượt giới hạn 1 giờ của một lệnh bash và bị hủy | Đo **aggregate** ở 2 mức worker (6 vs 10) trước khi quyết cấu hình; nếu tăng worker không tăng aggregate thì nút thắt là băng thông bộ nhớ ⇒ phải **giảm chi phí mỗi frame**, không phải thêm tiến trình. Đo trong lúc build bằng `Get-Process python,ffmpeg` (CPU s tích luỹ) để phân biệt kẹt CPU với kẹt băng thông |
| 102 | **Tối ưu `finishing()` phải BIT-IDENTICAL — và phải tự khởi tạo globals** (Tập 06, 03/11/2026): `finishing()` khởi tạo `VIGNETTE`/`GRAIN`/`ABUF` **lazy** ở lần gọi đầu; bản tối ưu gọi `np.repeat(B.VIGNETTE, …)` trước khi globals có giá trị ⇒ `AxisError: axis 2 is out of bounds` trong worker ⇒ **mọi part ra rỗng**, không ai báo vì lỗi chỉ hiện ở traceback của tiến trình con | Gọi **bản gốc 1 lần** để khởi tạo globals rồi mới dùng giá trị đã khởi tạo (phải giữ tham chiếu tới bản gốc, tránh tự gọi lại chính bản đã patch ⇒ đệ quy). **Kiểm byte-for-byte** trên ≥ 120 frame × 2 nguồn (mảng ngẫu nhiên + frame thật) trước khi dùng (A11 #89). Đo được: **127,8 → 94,0 ms/frame (−26%)**, frame sau khi tối ưu giống hệt bản gọc ⇒ **ảnh tĩnh đã QC vẫn hợp lệ**, không phải render lại |
| 103 | **Giới hạn 1 giờ của một lệnh bash ⇒ phải chia build theo FRAME rồi ghép nhiều lần** (Tập 06, 03/11/2026): một lần build 37.751 frame ở 30 fps mất ~73 phút > trần 60 phút ⇒ task bị hủy giữa chừng, 6 part chỉ còn ~3.000 frame mỗi part và **không có moov atom** (ffprobe: `moov atom not found`) | `render(fi)` chỉ phụ thuộc `fi` ⇒ chia theo khoảng frame cho kết quả **y hệt** một lần build liên tục. Dùng **bản sao** `.work/_build_video3_split.py` (đọc `AE_VID` từ env) để không sửa `build_video3.py` dùng chung ⇒ không phát sinh nghĩa vụ hồi quy Tập 01 (L9). Chia **theo frame, không theo giây** (`int(t × 30)`) để khớp tổng: A = [0, 18875) · B = [18875, 37751) ⇒ tổng 37.751. Ghép **một** lần `ffmpeg -f concat -safe 0 -c copy` (không ghép 2 vòng) và kiểm: tổng frame == `int(timeline.total × 30)`, đủ 1920×1080@30, DTS không N/A |
| 104 | **Renderer dùng `hash()` của Python làm seed ⇒ cùng 1 shot render ra 2 khung hình khác nhau** (Tập 03 EN, 03/11/2026): `np.random.default_rng(abs(hash(shot["id"])) % 999)` trong `t2_card` — `hash()` của chuỗi trong Python **được ngẫu nhiên hoá theo PYTHONHASHSEED ở mỗi tiến trình** ⇒ 2 lần render cho 2 khung hình khác nhau (đo được: 1/6 shot lệch, lệch tới 90/765 mức xám trên vùng thẻ T2). Hậu quả: **ảnh tĩnh QC (H9) KHÔNG bảo đảm khớp với video dựng thật** ⇒ cổng QC hình ảnh vô nghĩa với shot T2 | Dùng seed **ổn định giữa các tiến trình**: `np.random.default_rng(zlib.crc32(shot["id"].encode("utf-8")) % 999)`. Sau khi sửa, A/B 2 lần render cho **6/6 shot giống byte** (`.work/_ab_pipe_test.py`). Sửa script dùng chung ⇒ kiểm hồi quy Tập 01 (L9) |
| 105 | **Bản tiếng Anh thiếu khoá `roles_en` ⇒ badge vai rơi về nhãn CỨNG của Tập 01 — sai vụ án hiện lên màn hình** (Tập 03 EN, 03/11/2026): `ROLE_NAME`/`SUB_TAG` trong `edition.py` dùng `EP.get("roles_en") or {…nhãn cứng Tập 01…}`; chỉ Tập 02/04/05 (+29) có khoá này ⇒ **Tập 03 EN hiện badge Điều tra viên "Blanchard case file"** (vụ Gypsy Rose Blanchard) và N1 "**SPRINGFIELD RESIDENT**" trong khi đang kể vụ Edmund Kemper; phụ đề `.srt` cũng gắn nhãn sai | Mỗi tập EN **bắt buộc** khai `roles_en` + `sub_tags_en` trong `EPISODES["XX"]` (mẫu: Tập 02/04/05) — lấy N1/N2 từ `EP["n1"]`/`EP["n2"]` của chính tập đó. Hoặc sửa **fallback dùng chung** để suy ra từ `EP["case"]`/`EP["n1"]`/`EP["n2"]` (Tập 01 không đổi vì `n1/n2` Tập 01 EN trùng nhãn cứng). Kiểm sau khi khai: badge N1/N2 trên ảnh tĩnh phải là nhãn của tập, và nhãn vai trong `.srt` phải khớp |
| 106 | **Validator "trích dẫn nguyên văn" chỉ quét dấu nháy cong (“ ”) ⇒ dấu nháy thẳng ASCII (") lọt qua** (Tập 03 EN, 03/11/2026): `_build_plan_tap03_en.py` dùng `re.findall(r"“([^”]+)”", chu)` ⇒ shot `2-15` có `hunting knife ("The General")` — **nhãn thương hiệu không hề có trong lời thoại, cũng không có trong bản tiếng Việt** — vẫn qua cổng QC; chỉ 1/110 shot lộ, số còn lại sạch | Quét **cả hai kiểu**: `re.findall(r"“([^”]+)”", t) + re.findall(r'"([^"]+)"', t)`. Nhớ rằng "chữ trên hình là một nguồn khẳng định" (A11 #94): mọi nhãn trong ngoặc kép đều phải nguyên văn trong câu đang đọc |
| 107 | **Đổi audio ⇒ phải SINH LẠI cả phụ đề `.srt`, không chỉ dựng lại hình** (Tập 03 EN, 03/11/2026): audio Tập 03 EN được dựng lại 02/11 (timeline mới 1646,62 s) nhưng `.srt` vẫn là bản 25/10 ⇒ **cue cuối kết thúc lúc 1961,75 s — dài hơn video 315 s** ⇒ phụ đề lệch toàn bộ phần sau | `subtitles.py` đọc `ED.w("timeline_s.json")` ⇒ chạy lại sau **mỗi** lần đổi audio: `AE_EP=03 AE_LANG=en py -3 .work/subtitles.py`. Cổng: cue cuối kết thúc **≤** `timeline.total`, không cue chồng nhau |
| 108 | **`Tee-Object` của PowerShell 5.1 ghi log UTF-16LE ⇒ đọc log ra ký tự `\x00`; và kích thước file `part_*.mp4` KHÔNG phản ánh tiến độ** (Tập 03 EN, 03/11/2026): đo file size cho ra "còn 912 phút" trong khi render thật đang chạy ~12,4 fps ⇒ **ước lượng sai gấp 2 lần** (ffmpeg ghi `mdat` theo lô) | Đọc log bằng `Path.read_text(encoding="utf-16")` khi file bắt đầu bằng BOM `fffe`; **đo tiến độ bằng bộ đếm khung trong log** (`[part_XX] fi/total`), không bằng kích thước file. Ghi log bằng `Out-File -Encoding utf8` khi cần đọc bằng công cụ khác |
| 109 | **Mỗi chunk video bắt đầu ở frame CỤC BỘ 0 ⇒ script so/điều khiển theo thời gian TOÀN CỤC sẽ trích NHẦM khung hình** (Tập 03 EN, 03/11/2026): khi chia render thành nhiều chunk (A11 #103), chunk B bắt đầu ở frame toàn cục 16470 nhưng file mp4 của chunk tự đếm từ 0. Script `_check_stills_vs_video.py` seek bằng `t` toàn cục ⇒ ở chunk B/C nó trích **khung hình của shot khác** ⇒ MAE khổng lồ. Lỗi này **không xuất hiện ở chunk A** (offset = 0) nên dễ tưởng script đã đúng | Luôn trừ offset khi seek trong file chunk: `lfi = int(mid*FPS) - int(round(lo*FPS))`, `lo` = giá trị `--from` của chunk. **Tự kiểm** bằng shot đầu tiên của chunk: đúng phải ~2–6/255 (chỉ tổn thất nén H.264), lệch phải > 15/255. Sau khi sửa: chunk B **33/33 shot khớp · MAE TB 4,07 · lớn nhất 5,49** (chunk A: 45/45 · MAE TB 4,04) |
| 110 | **`np.correlate(mode="full")` là O(n²) ⇒ treo máy khi đo đồng bộ A/V; dùng FFT kèm self-test** (Tập 03 EN, 03/11/2026): script đo lệch A/V của Tập 07 lấy 60 s @ 8 kHz = 480.000 mẫu ⇒ `np.correlate` cần ~2,3×10¹¹ phép ⇒ chạy hàng giờ, không kịp trong giới hạn lệnh | Tương quan chéo bằng FFT: `c = np.fft.irfft(np.fft.rfft(x,N) * np.conj(np.fft.rfft(y,N)), N)` với `N` = 2^k ≥ len(x)+len(y)−1; đỉnh tại `m` = độ trễ của x so với y; lag âm nằm ở đuôi mảng (`m ≥ len(x)` ⇒ lag = `m − N`). **Luôn kèm self-test**: dịch tín hiệu vài mẫu, kiểm đúng dấu ở **cả hai chiều** trước khi tin kết quả. Mẫu: `.work/_qc_sync_t03_en.py` |
| 111 | **`verified_links()` chỉ hiểu bảng 4 cột, nhưng CẢ 29 tập EN dùng bảng 3 cột ⇒ chạy `package.py` làm MẤT TOÀN BỘ link nguồn trong mô tả** (Tập 03 EN, 03/11/2026): hàm đòi `cells[3].startswith("✅")` và link ở `cells[2]` (bảng `\| Câu \| Dữ kiện \| Nguồn \| ✅ \|`), nhưng `nguon_tham_khao_EN.md` thật của **mọi** tập EN là bảng **3 cột** `\| link \| Type \| ✅ \|` ⇒ hàm trả `""` ⇒ `description_en()` ghi vào mô tả `[PENDING — add the verified public links…]`. Tập 03 EN mất **24/24 link** ngay sau lần `package.py --mux` đầu tiên; **không có lỗi nào được báo** | Thêm nhánh (b) cho bảng 3 cột (link ở `cells[0]`, ✅ ở `cells[2]`) — **thuần bổ sung**, không đổi nhánh cũ. **Kiểm hồi quy bắt buộc (L9)** trên TOÀN BỘ file nguồn EN/JA/KO: link cũ **không được mất** (228 → 1.053, mất 0) và link mới phải **trùng khớp** với link đang có trong `mo_ta.txt` trên đĩa của 28 tập EN còn lại (`.work/_qc_regress_links.py`) — kết quả **28/28 GIONG**, chỉ Tập 03 EN là khác (đúng lý do cần sửa) |
| 112 | **Mô tả YouTube giới hạn 5.000 ký tự ⇒ phải ĐO sau khi sinh; "sinh xong" ≠ "đạt"** (Tập 03 EN, 03/11/2026): mẫu mô tả "rich" (3 đoạn dẫn + 5 bullet + CHAPTERS + disclaimer 5 dòng + khối crisis 6 dòng + 24 URL nguồn) sinh ra **5.201 ký tự** ⇒ vượt trần ⇒ YouTube cắt mô tả. Đây là lỗi **kiểu chung**: Tap04 EN sinh **5.366 ký tự** cùng kiểu (tập này chưa bị sinh lại nên file trên đĩa còn 3.683, cũ) | Sau mỗi lần sinh mô tả: đo `len()` file thật và **fail nếu > 5.000** (`.work/_dry_desc_len.py` đo cho mọi tập mà **không ghi file**). Rút gọn bằng cách **nén câu chữ** (giữ nguyên mọi dữ kiện và mọi link), không cắt bỏ nội dung. Tap03 EN đã rút từ 5.201 → **4.935 ký tự**, vẫn đủ 24 link + 5 mốc CHAPTERS đo từ timeline |
| 113 | **KHÔNG được dừng tiến trình không rõ lai — phải xác định owner trước** (Tập 03 EN, 03/11/2026): lúc 19:53 dừng 6 tiến trình `ffmpeg` "mồ côi" (StartTime 19:08:44) vì tưởng là rác sót của lượt QC đã kết thúc ⇒ **chúng thuộc lượt render Tập 04 EN đang chạy SONG SONG** (log ghi vào `test.txt` ở gốc repo) ⇒ lượt đó crash lúc 19:58:14, mất **4200/7941 khung mỗi part**. `Get-Process` **chỉ cho StartTime, không cho biết tiến trình đó là của ai** | Trước khi `Stop-Process` một tiến trình mình không spawn: (1) xem **CommandLine** bằng `Get-CimInstance Win32_Process`; (2) xem **tệp log/tệp mà nó đang ghi** và mốc sửa gần nhất; (3) nếu **không xác định được owner ⇒ ĐỂ NGUYÊN** — tiến trình thừa chỉ làm chậm, còn tiến trình bị giết có thể phá việc của session khác. Dùng `task_stop` trên task cha đã biết thay vì giết theo PID. Bài học bổ sung: **2 session có thể chạy cùng lúc trong 1 workspace** ⇒ đừng giả định mình là tiến trình duy nhất |
| 114 | **Chuỗi limiter phải khai theo TỪNG NGÔN NGỮ, không chỉ theo tập — bản JA/KO rơi vào chuỗi không `latency=1`** (Tập 03 JA, 04/11/2026): `EPISODES["03"]["mux_af"]` viết dạng `... if EN else <chuỗi mặc định>` ⇒ **mọi bản không phải EN** (JA, KO, VN) nhận `alimiter=limit=0.7943:attack=5:release=50:level=disabled` (**thiếu `latency=1`**). Hai hậu quả đo được trên bản JA: (a) master wav có **đỉnh mẫu −1,903 dBFS** ⇒ trần −2,0 dBFS chỉ bóp đúng **1 mẫu** ⇒ limiter không kích hoạt ⇒ **AAC dựng lại vọn true peak ~+1,8 dB** (đúng như #64/#38 đã ghi) ⇒ **vượt trần A7 −1,5 dBFS**; (b) thiếu `latency=1` ⇒ lệch âm thanh–hình ~**4,98 ms**. Không phải lỗi "bản JA" — là lỗi **cấu hình theo ngôn ngữ** chưa tách | Khai `mux_af` theo **tập × ngôn ngữ**: `("alimiter=limit=0.63:...:latency=1" if (EN or JA) else "alimiter=limit=0.7943:...")` — **trần −4 dBFS bóp 14.529 mẫu = 0,0157 %** (không gây pumping) và cho true peak **−3,3 dBFS**, lệch A/V **0,0 ms**. **Trước khi ghép, ĐO đỉnh mẫu của master wav**: nếu đỉnh > ngưỡng trần thì limiter **không kích hoạt** ⇒ phải hạ trần. Sau khi ghép: đo true peak **trên chính mp4** (#38) + đo lag (#64). Mọi thay đổi `edition.py` phải kèm **hồi quy L9 theo tập × ngôn ngữ** |
| 115 | **Cổng hồi quy tra `EPISODES` bằng `str(ep)` ⇒ mọi lần tra đều TRƯỢT ⇒ cổng báo "không khác biệt" trong khi đã sửa** (Tập 03 JA, 04/11/2026): khoá của `EPISODES` là chuỗi **2 chữ số** (`"01"`…`"29"`) còn mã so sánh dùng `str(ep)` = `"3"` ⇒ `EPISODES.get("3", {})` trả `{}` ⇒ cả bản cũ lẫn bản mới đều `None` ⇒ **"không có khác biệt"** ⇒ dễ tưởng đã sửa đúng. Cùng kiểu: dựng `f"3-{i-1}"` thay vì `f"3-{i-1:02d}"` làm mã không khớp key nào ⇒ **dòng biến mất khỏi bảng mà không ai báo** | Luôn format khoá theo **độ rộng của khoá gốc**: `"%02d" % ep`, `f"{i-1:02d}"`. Sau mỗi lần đánh lại ID: assert (a) mọi ID khớp regex đúng định dạng, (b) **số dòng trước == sau**, (c) `len(set(id)) == len(id)`. Cổng hồi quy phải **in ra giá trị đọc được** (ví dụ `EP03 mux_af = …`), không chỉ in "không khác biệt" — và phải **fail** khi không có khác biệt dù đã kỳ vọng có |
| 116 | **Cổng "hình không đen" cho INTRO phải là PARITY với intro chuẩn, không phải ngưỡng tuyệt đối** (Tập 03 JA, 04/11/2026): intro có **fade-in đen 0–1,5 s** (và fade-out 21–22,4 s) **cố ý** ⇒ cổng "khung t=1 s không đen" báo FAIL giả. Đối chiếu profile độ sáng 10 mốc thời gian của intro JA với `assets/brand/intro_kenh.mov`: khớp trong sai số **0,45 điểm %** ⇒ đúng thiết kế | Cổng kiểm intro = **so profile độ sáng** (% pixel > 140) của bản mới với bản chuẩn của dự án ở cùng bộ mốc thời gian ⇒ sai lệch ≤ 1,5 điểm %. Đừng dùng ngưỡng "phải sáng" tuyệt đối cho 1,5 s đầu. Cùng nguyên tắc với #65 (khung cuối đen là do renderer mờ dần) — **ngưỡng tuyệt đối phải đi kèm lý do thiết kế** |
| 117 | **File trong `.work/` có thể bị GHI ĐÈ bởi session khác — phải kiểm hash/mtime ngay trước khi mux** (Tập 03 JA, 03–04/11/2026): lúc 22:24 đọc `timeline_s_JA_t03.json` cho `total` = **1936,71 s**; lúc 22:40:06 file bị **ghi đè hàng loạt** (cùng lúc `build_video3.py`, `edition.py`, `package.py`, `timeline_s_JA_t02/t04`, `shots_EN_t03.json`…) ⇒ `total` = **1927,91 s**. Lệch **8,80 s** toàn video, và mọi mốc thời gian đã đọc trước đó thành sai. Dùng bản 1936,71 sẽ ghép video lệch audio master ⇒ **mất thẻ kết** (A11 #55) | Trước khi mux: in **hash SHA-256 (12 ký tự) + mtime** của `timeline_s_*.json`, `shots_*.json`, `build_video3.py`, `edition.py`, `package.py` ⇒ lưu vào báo cáo. Nếu timeline có **nhiều bản**, chọn bản khớp audio master: **đo bằng ASR** (upload audio tạm → `connector__matrix__listen_audio`) và so **nhiều mốc rải rác** (22 mốc / 0–1910 s) — bản 1927,91 khớp tuyệt đối (lệch TB −0,50 s, max +0,10, min −1,36 = sai số timestamp ASR), bản 1936,71 là file stale. Sau khi đọc lại file đã dùng ⇒ **kiểm hash còn nguyên** |
| 118 | **Kịch bản sa đà vào nghiệp vụ phá án thuần túy, thiếu chiều sâu tâm lý và dư chấn xã hội** (Nhận xét người dùng 05/11/2026): video kể đủ tình tiết, pháp y và điều tra nhưng không làm sáng tỏ tác động xã hội, thế giới quan của hung thủ về nạn nhân/người thân, thái độ trước bản án, cơ chế tự bào chữa và các yếu tố hành vi (ngòi nổ, chữ ký, leo thang, hào quang, nạn nhân học) ⇒ video biến thành phóng sự phá án thông thường, mất bản sắc "giải phẫu tâm lý" của kênh | **Tuân thủ Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c) & cổng K10 (AGENTS.md)**: Đối soát đủ 10 câu hỏi cốt lõi trước khi duyệt kịch bản (Nhóm I: 5 trụ cột cốt lõi; Nhóm II: 5 yếu tố khoa học hành vi). Phân vai rõ: Host dẫn dắt dư chấn xã hội/triết lý/cảnh báo sinh tồn; Điều tra viên cung cấp dữ kiện/MO vs Signature/ngòi nổ; Chuyên gia tâm lý mổ xẻ chia ngăn/vật hóa/nghiện ảo tưởng |
| 119 | **Ghi file mà không kiểm line-ending ⇒ CR thừa làm diff TOÀN FILE, mọi cổng "nội dung không đổi" vẫn xanh** (Tap04, 05/11/2026): `.work/edition.py` bị ghi thành `\r\r\n` (1372/1372 dòng) vì đọc file giữ CRLF rồi ghi bằng writer tự dịch `\n`→`\r\n` trên Windows (`write_text()` / `open('w')` không truyền `newline=''`). Hậu quả: blob trong git thành CRLF (không phải LF thuần như phần còn lại của repo) ⇒ `git diff` hiện **2684 dòng thay đổi** thay vì 84 dòng thật ⇒ mọi thay đổi thật bị chôn vùi. File vẫn **chạy được** (Python coi `\r\r\n` là 2 dòng) nên không cổng nào báo lỗi | Đọc-ghi file văn bản **luôn truyền `newline=''`** (`open(p, encoding='utf-8', newline='')`) để giữ nguyên EOL, hoặc chuẩn hoá một lần về LF trước khi ghi. **Đo trước khi commit**: `b.count(b'\r\r\n')` phải = 0 (nếu = số dòng ⇒ file đang bị nhân đôi CR) và `git diff --stat` phải khớp quy mô thay đổi thật (1 file nhỏ mà diff > 1000 dòng ⇒ kiểm EOL). Sửa: `b.replace(b'\r\r\n', b'\r\n')` + `py_compile` + so nội dung sau khi bỏ hết `\r` phải **giống hệt** trước đó. `core.autocrlf=true` (Git for Windows) ⇒ git tự quy đổi CRLF→LF khi add, nên blob trong repo phải là LF thuần |
| 120 | **Sửa kịch bản (thêm câu) mà không chuyển `acting_tapXX.json` + `sfx_tapXX.json` theo NỘI DUNG ⇒ lời đọc riêng gắn nhầm câu** (Tập 06 VN, 06/11/2026): kịch bản 154 → 212 câu (đồng bộ 10 chỉ dấu 05/11) nhưng acting/sfx vẫn mã cũ ⇒ 10 `alt` sẽ đọc câu KHÁC (4.10#1 đọc câu bản án thay câu Jack Hanley); tiếng động, nền, tắt nhạc rơi sai câu. CER **không** bắt được | P0 Higgs: so mọi `alt` với câu gốc hiện tại (tỉ lệ giống ≥ 0,9) + mọi mã trong sfx phải tồn tại. Chuyển theo nội dung dựa trên bản kịch bản cũ trong git; `alt` chỉ được chèn `<#0.35#>` sau `:` (G6). Bản cũ: `.work/_cu/t06_higgs_redo_20261106/` |
| 121 | **QC Whisper vỡ khi lô có file > 30 s; `qc_whisper_cer.py` luôn chuẩn hoá tiếng Việt** (Tập 06 EN/JA, 06/11/2026): file Higgs chạm trần token 47,6 s (đuôi gần câm) làm pipeline lô lỗi `RuntimeError 3000 vs 4756` ⇒ kernel ERROR. Sau khi chạy được, JA ra 161/212 câu “> 2%” vì dùng `vi_cer` cho tiếng Nhật | `build_qc_nb.py`: lô có file > 30 s chạy từng file (timestamps). `qc_whisper_cer.py` chọn `en_cer`/`ja_cer` theo `AE_LANG` ⇒ JA 30/212, EN 8/212; VN giữ 46/212 (hồi quy). Kernel QC lỗi = **dấu hiệu có file đuôi câm** — quét `> 30 s` ngay sau khi tải |
| 122 | **`measure_cer_prod.py` phụ thuộc ứng dụng MCode đang mở** (06/11/2026): tiến trình nền chết im lặng giữa chừng; lượt sau báo 446/446 file `MCode host authentication broker is unavailable` | Cache ASR giữ phần đã đo ⇒ chạy lại không mất. Trước khi chạy dài: thử 1 file. Lỗi broker ⇒ dừng, nhờ người dùng mở MCode (AI không tự mở được) |
| 123 | **Nhánh `text_scrim` của template T5 không phủ nhãn** (06/11/2026, Tập 07): scrim phủ `y 360–800` nhưng nhãn T5 vẽ ở `y ≈ 330` ⇒ chữ vẫn "chìm" 43,8 % sau khi bật scrim | T5 chỉ hợp khi câu có **ngày/số** để vẽ số lớn (`5.04#4` kiểu "thứ nhất"). T5 mà câu **không có số** ⇒ đổi mẫu sang **T1** (chữ nằm đáy khung, dùng đúng nhánh scrim đã chứng minh chạy tốt). Không sửa `build_video3.py` để không ảnh hưởng tập khác |
| 124 | **Đo tương phản báo nhầm cho template T2** (06/11/2026): element T2 là **tấm thẻ sáng** (nét ~295 000 px) nên phép đo lấy màu tấm thẻ, không phải màu chữ ⇒ báo "chìm 47 %" dù chữ đỏ trên nền kem đọc rõ | Chỉ kết luận "chìm" sau khi **soi mắt ảnh**. T2 không có nhánh scrim trong renderer ⇒ đừng thêm T2 vào `text_scrim` |
| 125 | **Regex số của cổng A9.2 nuốt dấu phẩy**: `\d[\d.,]*` lấy cả `16,` ⇒ "16," không khớp câu ⇒ báo sai dù chữ đúng | Chữ trên hình **không đặt chữ số ngay trước dấu phẩy** (`16,` → `16 years old,`). Cũng tránh `1.600` (dấu chấm = phân tách nghìn) |
| 126 | **Kịch bản viết lại ⇒ timeline + bảng shot cũ vẫn "hợp lệ"** (06/11/2026, Tập 07): `parse_shots.py` **không báo lỗi** vì mã câu cũ vẫn là chuỗi hợp lệ, nhưng 144/147 câu VN đã đổi nội dung ⇒ lớp chữ trên hình sai âm thầm | Viết lại kịch bản ⇒ **dựng lại timeline** (neo theo ID element) + **viết lại lớp chữ** + render lại ảnh. Luôn đo `mtime ảnh > mtime bảng shot` và so **md5** với ảnh cũ trước khi tin là đã render |
| 127 | **Master mới thay giữa chừng ⇒ JSON kịch bản + timeline cũ lỗi thời mà mọi cổng cũ vẫn xanh** (Tập 04 EN/JA, 06/11/2026): master EN 1658,31 s / JA 1946,67 s nhưng `script_tap04_{EN,JA}.json` chỉ 161/166 câu (kịch bản đã 212) và timeline cũ 1391,53 / 1578,91 s. Cổng `qc_shots_t04.py` nạp **cứng `script_tap04.json` (bản VN)** ⇒ so trích dẫn EN/JA với câu tiếng Việt, báo sai | Khi master đổi: `parse_kichban.py` lại ⇒ ASR master (faster-whisper small, `word_timestamps`) ⇒ căn DP ⇒ dựng timeline từ chính mp3 (cổng T20). EN căn theo **từ** (`_align_words_t04_en.py`); JA căn theo **ký tự** (`_align_chars_t04_ja.py`, katakana→hiragana). Cổng bảng shot theo ngôn ngữ: `qc_shots_t04_en.py` / `qc_shots_t04_ja.py` (bản sao trỏ `script_tap04_{EN,JA}.json`) |
| 128 | **ASR bỏ sót vài từ đầu câu sau quãng ngắt ⇒ biên câu nằm trong khoảng lặng** (Tập 04 EN: 3.07#7, 2.02#3, 5.04#5; JA: 5.04#1 lệch 1,6 s, 1.08#4, 3.08#2…). Chạy cổng số liệu vẫn xanh | Quét `_qc_boundaries_t04.py <timeline> <wav16k>`: (a) khoảng lặng < −40 dB ≥ 0,9 s **trong thân câu**; (b) khoảng trống > 0,8 s có > 0,45 s tiếng. JA tự cắt biên theo khoảng lặng ≥ 0,4 s sát rìa câu (`_edge_trim`, 19 câu). Câu bị ASR bỏ hẳn ⇒ ghi đè tay theo đo năng lượng 16 kHz và ghi vào `OVERRIDE`/`ADJ` |
| 129 | **`subtitles.py` cho JA: `MAXC=84` quá lỏng ⇒ 186/213 cue > 6 s bị cắt giờ hiển thị; `two_lines` có thể để lại dòng chỉ có `。`** (Tập 04 JA) | JA: `MAXC=40`, không cắt ra mẩu < 3 ký tự. Hồi quy: SRT VN và EN Tập 04 **giống byte** trước/sau. Còn 28 cue JA vẫn bị rút về 6 s (câu không có điểm ngắt) — xuất lại các tập JA cũ sẽ ra SRT khác bản đã đăng |
| 130 | **Chữ tiếng Anh/Nhật dài hơn tiếng Việt ⇒ cùng bảng shot nhưng chữ đè nhau / sát mép / mờ trên nền sáng** (Tập 04 EN/JA): 1-17, 4-11, 4-17 đè hoặc sát mép; ~20 shot chữ phụ khó đọc. Cổng chữ số/trích dẫn không bắt được | Xem contact sheet **toàn bộ** 103 ảnh tĩnh trước khi dựng (H9). `text_scrim` khai theo ngôn ngữ trong `edition.py` (`+ ([...] if EN else [])`; EN 49, JA 57, VN 27 — VN không đổi, L9). Rút gọn tiêu đề ở bảng shot của ngôn ngữ đó, không sửa script dùng chung |
| 131 | **Master mp3 có thể thuộc PHIÊN BẢN KỊCH BẢN CŨ mà mọi cổng mp3↔timeline vẫn không báo** (Tập 05 VN, 06–07/11/2026): master 1299 s khớp bản 162 câu (8 câu yếu), chỉ 122/209 câu khớp kịch bản mới; master thay lúc 23:53 (1704,49 s) mới khớp 209/209 | Trước khi dựng: ASR master (`_transcribe_t05_vi_small.py`) + căn từ (`_align_words_t05.py`) ⇒ **câu yếu < 2% mới đạt**. Câu yếu phải nghe lại cửa sổ (ASR bỏ sót ≠ audio thiếu). Whisper ảo giác "subscribe…" trên nhạc cuối: đo năng lượng trước khi kết luận. Ảnh nền AI có thể có chữ/số (đồng hồ camera 4-15 "03:47:12 AM") ⇒ vá bản sao, giữ bản gốc ở `.work/_cu/` |
| 132 | **Script QC/dựng sao từ tập khác mang HARDCODE của tập đó — cổng vẫn "xanh" hoặc đỏ sai** (Tập 05 EN, 07/11/2026): `_align_words_t05_en.py` sao từ T04 giữ `N1 nếu id=='1.07'` ⇒ 5 câu N1 (`1.09`) ghi vai N2; cổng `_qc_shots_en_t05.py` cứng shot cuối `5-15`, "164 câu", "83 shot" ⇒ báo FAIL thẻ kết dù đúng và in số cũ khi ĐẠT | Sau khi sao script: grep id/số cứng (`1.07`, `5-15`, `164`, `83`, tổng giây); vai N lấy từ `EPISODES[ep]["n_element"]`. Cổng in số đếm **tính từ dữ liệu**, không chuỗi cố định. ASR bỏ sót câu (`4.15#6` im 6,7 s trong ASR) ⇒ đo năng lượng + OVERRIDE; nhãn T5 ngày phải chỉ chứa số CÓ trong câu EN ("August 18" ⇒ `AUGUST 18 · 2005`, không `18 · 08`) |
| 133 | **Timeline JA có trong repo là bản ƯỚC LƯỢNG — master mp3 mới lệch tới 18 s; JA tiếng Nhật không có từ để căn nên phải căn theo KÝ TỰ** (Tập 05 JA, 07/11/2026): `timeline_s_JA_t05.json` cũ (total 1745,37) đã có 209 câu nhưng mốc câu lệch −18…+6 s so với master 1745,72 s; `script_tap05_JA.json` còn bản cũ 164 câu. | Làm lại: parse kịch bản JA → ASR whisper small (`_transcribe_t05_ja_small.py`) → căn ký tự kana-hoá (`_align_chars_t05_ja.py`) → `_build_timeline_t05_ja.py` (OVERRIDE/ADJ đo năng lượng 16 kHz cho câu ASR bỏ sót hoặc tốc độ >10 ký tự/s) → `total` = mp3 ± 0,05. Kiểm chéo mọi câu bằng ASR trong khoảng câu (195/209 ≥ 0,6; phần còn lại là tên Latin/số và 2 câu ghi đè). Nhãn ngày viết `2004年3月19日` (không `19 · 03 · 2004`, H6). Chữ trên hình tiếng Nhật ngắt dòng theo ký tự ⇒ tiêu đề ≤ ~16 ký tự để tránh chữ mồ côi / số bị tách (6220 → 622\|0). |
| 134 | **Bảng shot có thể ĐÚNG ID câu nhưng SAI NỘI DUNG sau khi kịch bản đổi — cổng "phủ câu / số trên hình" vẫn xanh; và true peak có thể vượt trần chỉ ở MỘT tiếng động ngắn** (Tập 03 EN, 07/11/2026): (a) kịch bản mới đổi câu nên 5 shot mang chữ thuộc câu cũ (`2-07` "chôn đầu nạn nhân" khi lời nói "cô ấy không bao giờ về nhà"; `2-15` "dao, túi nhựa"; `5-09` "chôn mèo sống" — chi tiết bạo lực không có trong lời đọc; `1-23`, `4-07` chữ hiện trước lời) — chỉ lộ khi in từng shot cạnh **toàn văn câu**; (b) mục danh sách T8 dài > ~40 ký tự xuống dòng và **đè** mục sau (`2-05`, `2-06`, `3-12`) — ảnh tĩnh giữa shot không thấy vì mục 02 chưa hiện, phải render thêm tại `end − 0,6 s`; (c) true peak **−0,7 dBFS** dù đã có `alimiter limit=0.63:latency=1`: nguồn có tiếng "cạch" cassette ở 1640,8 s (−2,4 dBFS giữa nền −22 dB), limiter chặn không ổn định, AAC làm vọt thêm; cùng chuỗi trên đoạn 18 s cho −3,9. | (a) In `SAY` (toàn văn) cạnh `SCR` cho 110 shot, tự rà từng chi tiết sự kiện; chữ tóm tắt chấp nhận, **sự kiện/vật thể không có trong lời** thì sửa. (b) Mục T8 ≤ ~38 ký tự; render ảnh tại `end − 0,6 s` cho mọi shot T8. (c) Thêm tầng `asoftclip=type=hard:threshold=0.63` sau `alimiter` ⇒ true peak **−2,6 dBFS**, lệch A/V 0,0 ms, −16,4 LUFS. Đo true peak **trên mp4 cuối**, tìm vị trí đỉnh bằng nội suy 4× nếu vượt. |
| 135 | **Master "đọc nhanh, không chậm rãi" — lỗi là KHOẢNG NGHỈ, không phải tốc độ đọc** (Tập 06 VN/JA, 07/11/2026): tốc độ trong câu 3,61 tiếng/s (= Tập 05) nhưng trung vị nghỉ giữa câu 0,35 s (Tập 05: 0,74 s). Nguyên nhân: chuyển mã câu 154→212 làm `_pause_after` của `acting_tap06.json` còn 37/93 mục; `acting_tap06_JA.json` không tồn tại ⇒ JA 0 khoảng nghỉ. CER, LUFS, `silencedetect`, khớp hình–tiếng đều đạt nên không cổng nào bắt | AGENTS A13: đo trung vị nghỉ ≥ 0,6 s và ≤ 25% chỗ < 0,4 s trên timeline trước khi dựng hình; `_pause_after` cho **từng ngôn ngữ** đến khi đạt cổng (T06: chỉ 26/93 mục cũ chuyển được theo nội dung vì kịch bản viết lại; bổ sung bằng `.work/_fix_pause_t06.py` ⇒ VN/JA 135, EN 162 mục); thiếu file diễn xuất ⇒ dừng. Mốc tham chiếu: T04 104 · T05 100 · T06 EN 113 mục, TB 0,44–0,48 s |
| 136 | **Sinh ảnh nền bằng renderer procedural (gradient) ⇒ ảnh KHÔNG có nội dung cảnh, vi phạm H3, mà MỌI cổng QC vẫn xanh** (Tập 08–29, phát hiện 09/11/2026): 1361 ảnh nền Tập 08–29 do "Amber Eyes Noir Graphic Renderer" (Pillow & Numpy procedural) dựng — soi mắt thấy **gradient tối trừu tượng**, không có gợi hình nào (không sở huynh đô, không bệnh viện, không xe). QC vẫn xanh vì cổng chỉ đo **chữ / số / thời lượng**, **không đo ngữ nghĩa ảnh**; shot tĩnh Tập 08 như `shot_1-02.png` chỉ có chữ trên nền trừu tượng | Nền PHẢI có nội dung cảnh khớp lời (AGENTS H19, A8.2). **Chỉ số tự động không phân biệt được** (đo 09/11: entropy luminance MiniMax 5,18 vs procedural 4,39 — chồng nhau; Tập 08 có vân tia nên tỉ lệ "nội dung" 87 % dù là gradient) ⇒ **bắt buộc soi mắt**: đọc tên nền phải ra một cảnh cụ thể. Sinh lại bằng `gen_images.py` (MiniMax) cho Tập 08+; nhớ cập nhật **cả** `provenance.json` (`cong_cu`) **và** `REVIEW_Bo_Anh_TapXX.md` (đang ghi "100 % tự chủ") |
| 137 | **Đo tối ưu bằng "chạy A lạnh rồi chạy B nóng" ⇒ PHÓNG ĐẠI kết quả gấp 2–3 lần** (09/11/2026): benchmark đầu tiên báo "12,5 phút → 4,3 phút (−66 %)" cho phương án nền dùng chung. Đo lại bằng cách **xen kẽ A/B 3 vòng, mỗi vòng xoá file tạm, lấy median** ⇒ **5,0 → 3,6 phút (−27 %)**. Lý do: lượt A đầu phải nạp module + font + bộ đệm `VIGNETTE/GRAIN/ABUF` (~150 ms) và ghi file lần đầu vào đĩa | Benchmark **xen kẽ ≥ 3 vòng**, mỗi vòng xoá file tạm, lấy **median**. Đo lại từng thành phần bằng **median 5 lần** sau 1 lượt warm-up: `finishing()` 86 ms · `resize` 25 ms · **ghi PNG 221 ms (nửa tổng)** · chữ + avatar 22 ms. ⇒ **chỉ ~10 % là chữ** ⇒ tối ưu phần nền, đừng tối ưu chữ (AGENTS T23) |
| 138 | **Dùng nền chung cho 3 ngôn ngữ ⇒ camera `pan`/`pull` LỆCH khung crop, ảnh không khớp byte** (09/11/2026): `camera_box()` tính theo % tiến trình trong shot, mà thời lượng shot khác nhau giữa 3 ngôn ngữ (Tập 08 shot 3-09: VI 8,16 s · EN 8,74 s · JA 9,60 s) ⇒ crop lệch ~0,03 px ⇒ **97–99 % pixel khác**, biên độ tới 255/255. Shot `camera=still` thì crop giống hệt (1-11, 4-14: 0 px). Ngoài ra `finishing()` chọn hạt phim theo `fi % 6` — 3 ngôn ngữ có `fi` khác nhau ⇒ hạt phim khác | Muốn **byte-identical**: dùng nền chung + tính lại `finishing()` theo `fi` của **từng ngôn ngữ** ⇒ 3 ngôn ngữ khớp byte ở shot `still`; shot `pan`/`pull` chấp nhận lệch nhỏ hoặc render riêng. **Dùng `t = fi/FPS`** (đúng convention của `render()`), **không** dùng `(start+end)/2` — lệch 2–21 ms làm crop lệch ⇒ ảnh không khớp byte (đo: shot 3-09 lệch 807.416 px, biên độ 6). **Shot cuối có fade-to-black từ `start+4,0 s` ⇒ render riêng** |
| 139 | **Bảng markdown có ô NHIỀU hơn header ⇒ GFM BỎ MẤT ô đó, không báo lỗi, không ai thấy** (09/11/2026): rule H17–H19/T23–T24 viết 3 ô (`mã \| luật \| bằng chứng`) nhưng header bảng chỉ khai **2 cột** ⇒ cột *bằng chứng* (lý do, số đo, lỗi đã gặp) **không hiện khi render**, chỉ còn khi đọc file thô — người đọc trên GitHub/VS Code coi như rule không có lý do | Mọi dòng trong bảng phải có **đúng số ô = số cột header**: **thiếu ô** ⇒ GFM thêm ô rỗng (vô hại); **thừa ô** ⇒ GFM **bỏ mất** (mất nội dung). Cổng đo: script đếm ô, bỏ qua pipe đã escape, cho `AGENTS.md` + `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` + `README.md` — sau khi vá header 3 bảng A/H/T và gộp ô thừa 2 dòng README: **ERROR = 0** |
| 140 | **Dòng TRỐNG giữa 2 dòng bảng ⇒ GFM CẮT bảng ⇒ các dòng sau đó KHÔNG render thành bảng (mất header, mất căn cột); và chèn dòng mới bằng anchor `\| 138 \|` ⇒ cắt NGANG GIỮA dòng cũ** (09/11/2026): bảng A11 bị 2 dòng trống (dòng 705, 710) nên #114–#139 không thuộc bảng nào; lần chèn #139 bằng anchor `\| 138 \|` đã cắt dòng #138 làm đôi và làm hỏng cả dòng #139 (chứa `\|` thô trong code span ⇒ thêm ô ⇒ mất nội dung) | **Không có dòng trống giữa 2 dòng bảng** (trừ khi đó là header của bảng mới); chèn dòng mới bằng anchor **trọn vẹn của dòng cũ** (kèm phần đuôi) hoặc chèn theo chỉ số dòng; pipe `\|` trong ô phải escape `\|`; **cổng đo** `.work/_check_md_tables3.py` phải **tự kiểm** (tiêm 1 dòng thừa ô vào bản sao tạm và đòi checker phải bắt) — checker dừng quét ở dòng trống nên báo 'xanh' giả cho phần bảng đã bị cắt |
| 141 | **Nền MiniMax vẫn VẼ CHỮ dù prompt đã cấm (H5) — cổng grep prompt báo XANH trong khi ảnh sai** (Tập 09, 09/11/2026): 3/65 ảnh nền `t9_*` còn chữ đọc được (`Unfreezing \| Changing \| Refreezing` trên bảng đen, `LOST`/`FOUND` khắc trên ghế xe buýt) và 1 ảnh có vật thể trắng lơ lửng (bìa “White Album” thành mảng trắng) ⇒ **kiểm prompt không đủ, phải soi bằng mắt** | Mọi ảnh nền phải đi qua **contact sheet + soi mắt** trước khi dùng (H19). Khi phát hiện: sửa prompt (bỏ tên/nhãn khỏi prompt, thêm `ABSOLUTELY NO WRITING`), `--force` sinh lại **đúng ảnh đó** (không sinh lại cả lô), cập nhật `provenance.json` (prompt mới + mục `hau_xu_ly` nếu cắt viền trắng) |
| 142 | **Thẻ giới thiệu vai (`intro_card_pos`) đè lên khối chữ T4 “lời kể”** (Tập 09, 09/11/2026): vị trí (490, 250) — vị trí của Tập 07/08 — che **dòng chữ đầu tiên** của mẫu T4 (T4 đặt chữ ở x=470, y≥330) ⇒ lời kể của N1/N2 **không đọc được** (xem ảnh tĩnh Tập 08 `shot_1-17`: chữ bị thẻ vai phủ) | `intro_card_pos` phải kiểm theo **MẪU của shot đầu tiên của vai** (T1 đáy khung, T4 giữa-trái, T8 cờ, T2 thẻ hồ sơ), không chỉ T1. Tập 09 đặt **(960, 90)** = góc trên phải ⇒ không đè T1 lẫn T4; sau khi đổi phải **render lại 5 shot lượt đầu mỗi vai** (H, D, C, N1, N2) |
| 143 | **Timeline ƯỚC LƯỢNG (EN/JA) phải ép vai `N` → `N1`/`N2` theo `edition.py`** (Tập 09, 09/11/2026): timeline VN (đo từ master mp3) đã có N1/N2, nhưng timeline dựng bằng công thức kế thừa vai `N` của kịch bản ⇒ `build_video3` crash `KeyError: 'N'` lúc vẽ badge ⇒ **không render được ảnh tĩnh EN/JA** | Sau khi dựng timeline ước lượng, chạy script ép vai cho **mọi** item có `element` trong `EPISODES[EP]["n_element"]`; kiểm bằng `Counter(item["role"])` cho cả 3 file timeline. Sao lưu file timeline cũ trước khi ghi |
| 144 | **Gom câu cho H10 bằng DP: phải giới hạn ≤ 2 câu/shot và tính chi phí theo MỨC ĐỘ vi phạm** (Tập 09, 09/11/2026): DP không giới hạn ⇒ gom cả element 2.06 (13 câu) thành **1 shot 62 s**; DP chỉ đếm “số lần vi phạm” ⇒ lại chọn **shot 26 s** để đổi 2 vi phạm thành 1 | cost = (vi phạm **VN**, vi phạm EN, vi phạm JA, số lần gom) với vi phạm tính bằng **số giây** vượt 15 s / thiếu 3 s; ngôn ngữ **đo thật** (VN) xét trước ngôn ngữ **ước lượng** (EN/JA). Shot > 15 s **không tách được** (ranh giới shot = ranh giới câu) ⇒ tách **chữ trên hình** thành 2 đoạn nguyên văn + beat `ở "<cụm từ>"` để đạt A7 |
| 145 | **Cổng H17 chỉ ghi trong tài liệu, không có script ⇒ 4 tập lệch nền giữa các ngôn ngữ không ai bắt** (10/11/2026): **Tập 01** KO còn ở bảng shot cũ 24/10 (122 shot) trong khi VN/EN/JA đã dựng lại 09/11 (203 shot) ⇒ 83 mã shot không khớp, 102 shot khác nền; **Tập 02** VN/KO 161 shot, EN/JA 151 shot ⇒ 58 shot khác nền, EN/JA thiếu `t2_cell_medical` (lệch phiên bản bảng shot — chưa kiểm nội dung); **Tập 03** EN/JA shot 2-07 dùng `t3_car_door` thay `t3_backyard_garden`; **Tập 05** EN/JA shot 2-04, 2-05 khác nền VN dù bộ nền trùng 60 = 60 (so bộ nền **không đủ**). *Đính chính:* bản ghi đầu của mục này viết "Tập 01 KO lấy nhầm nền Tập 02 (`*_gypsy`)" — **sai, là suy đoán không đo**: `*_gypsy` là nền của chính Tập 01 | Cổng tự động `.work/qc_bg_shared.py --ep XX` (bộ nền + nền từng shot theo mã + file tồn tại + 0 hậu tố ngôn ngữ), chạy **sau `parse_shots.py` của mọi ngôn ngữ, trước ảnh tĩnh**. Điều kiện: các ngôn ngữ cùng phiên bản bảng shot. Tập 01–03 nằm trong `MIEN_TRU` (đã dựng trước khi có cổng). **Người dùng chốt 10/11/2026: mọi yêu cầu tạo ảnh đa ngôn ngữ — tập mới hay tạo lại tập cũ (kể cả Tập 01–03) — đều theo A8.1**; các bản đã xuất không tự động dựng lại, nhưng hễ làm lại ảnh tập nào thì tập đó phải `DAT` với `--ep XX` và được gỡ khỏi `MIEN_TRU` (Tập 05 không nằm trong `MIEN_TRU` nên quét toàn bộ vẫn báo `LOI` ở tập này). Câu prompt chừa chỗ cho chữ: tuỳ chọn `caption_space` theo từng ảnh, mặc định tắt, chưa sinh thử. Quy định: A8.1 |
| 146 | **Timeline ASR cũ đặt mốc câu sớm ~1 từ; Whisper chia chunk có chồng lặp từ** (Tập 08, 10/11/2026) | Căn lại: điểm cắt = khoảng lặng thật (250–3500 Hz < −35 dB) ngay sau từ cuối câu trước; **khử lặp từ** ở vùng chồng giữa các chunk; kiểm chéo Whisper cửa sổ 3 s đầu/cuối mỗi câu (654 cửa sổ: VN/EN 0 lỗi, JA 1 lỗi `4.02#5` đã sửa). Luật "lấy từ đầu tiên Whisper nghe được" CHỈ dùng cho câu đầu hồi (Whisper hay bỏ sót nửa đầu câu ⇒ cắt trễ 3–4 s) |
| 147 | **`package.py --mux` lấy tiếng từ `.work/audio_master*_tXX.wav` (có thể là bản cũ) và tập không khai `mux_af` rơi vào limiter thiếu `latency=1`** (Tập 08) | Khi master mp3 mới hơn wav: ghép thủ công `-map 0:v -map 1:a -c:v copy -af "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1"`. Thẻ kết kiểm tại `total − 6 s` (từ −4 s là fade đen) |
| 148 | **Thumbnail tập không khai `thumb_bg` mượn nền Tập 01 và EN/JA in chữ tiếng Việt** (Tập 07, 08 — cập nhật 12/11/2026): Tập 07 cấu hình `EPISODES["07"]["thumb"]` thiếu rẽ nhánh ngôn ngữ `if EN else ... if JA else ...` dẫn tới thumbnail EN/JA mang chữ tiếng Việt ("BẢN ÁN GIẾT NGƯỜI / BẰNG TIN NHẮN"). Đã sửa trong `edition.py` sang `("MURDER BY", "TEXT MESSAGE")` (EN) và `("メッセージによる", "殺人判決")` (JA); sinh lại trực tiếp bằng `package.thumbnail()` (A11 #72) | Khai `thumb` theo ngôn ngữ + `thumb_bg` của đúng tập trong `EPISODES` (H11) |
| 149 | **ASR alignment JA: tên riêng tiếng Latinh làm Whisper phiên âm Katakana lệch text kịch bản** (Tập 09, 11/11/2026): kịch bản chứa từ Latinh ("Beverly Hills", "Sharon Tate") nhưng Whisper nhận dạng "ビバリーヒルズ", "シャロン・テート" ⇒ match score rơi xuống 85,9% (< 97% gate) | Thêm bảng ánh xạ tên riêng `JA_MAP` sang Katakana trong `_t09_align4.py`, hạ `K=4` gram cho JA, đặt ngưỡng khớp câu $\ge 0,35$ ⇒ tỷ lệ match đạt **97,5% (194/199 câu)** |
| 150 | **Whisper transcribe lọt hallucination vào đoạn nhạc dạo Intro** (Tập 09 EN, 11/11/2026): Whisper nhận diện chữ ảo ("In the late...") tại 19,16 s trong nền nhạc intro | Thêm rule ghim cứng $S[0] \ge 22,8\text{ s}$ cho câu thoại đầu tiên của Hồi 1 trong `_t09_timeline_from_asr.py` |
| 151 | **Faster-Whisper trên Python 3.14 lỗi PyAV `metadata_errors` và timeout HuggingFace Hub** (Tập 09, 11/11/2026): truyền đường dẫn audio vào `transcribe()` bị crash `TypeError: open() got unexpected keyword argument 'metadata_errors'` | Đọc audio 16 kHz mono bằng `wave` thành mảng `np.float32` trước khi truyền vào `model.transcribe()`, đặt `local_files_only=True` cho `WhisperModel('base')` |
| 152 | **`INTRO_MOV` của JA tìm `intro_kenh_JA_tXX.mov` không tồn tại** (Tập 09, 11/11/2026): `edition.py` ép `EP["intro"] = f"intro_kenh_JA_t{EPN}.mov"` nhưng thư mục brand chỉ có bản t06/t07 | Sao chép intro chuẩn JA (`assets/brand/intro_kenh_JA_t07.mov`) sang `intro_kenh_JA_t09.mov` trước khi dựng hình |
| 153 | **`mux_af` limiter với `:latency=1` giữ True Peak $\le -1,72\text{ dBFS}$ và khử trễ 5 ms** (Tập 09, 11/11/2026): khai báo `"mux_af": "alimiter=limit=0.7943:attack=5:release=50:level=disabled:latency=1"` trong `EPISODES["09"]` | Cả 3 ngôn ngữ đạt I = -16,28 LUFS, True Peak từ -2,05 đến -1,72 dBFS, 0 lỗi trôi hình-tiếng |
| 154 | **Connector `generate_image` đổi schema giữa 10/11 và 11/11/2026: bỏ `resolution`, chỉ còn `area` (1K/2K/4K, **mặc định 4K**), `additionalProperties: false`; ảnh tham chiếu là `reference_images: [{url}]` (không còn `input_urls`)**. Dấu hiệu: ảnh gốc 2752×1536 → 2720×1536, dung lượng TB 3,4–3,8 MB → 1,55 MB. Script cũ gửi `resolution` ⇒ bị từ chối hoặc rơi về 4K. Đã sửa 7 script (`gen_images.py`, `gen_one*.py`, `_healthcheck.py`, `_try_gavel.py`, `_t08/_t09_gen_bg_minimax.py`), bản lưu `.work/_cu/area_fix_20261111/`. Bài học kèm: hết credit ngày 11/11 **không** do ảnh đắt lên — bảng MiniMax Usage cho thấy 7 ngày gần nhất dùng ÍT hơn 23 ngày trước (LLM ~197 vs ~308 triệu token/ngày; ảnh ~21 vs ~31/ngày); số dư cạn do tiêu cả tháng (8,47 tỷ token LLM, 850 ảnh). "Làm lại ảnh tĩnh" (vẽ chữ, 0 credit) ≠ "sinh lại nền" (MiniMax) | Trước khi gọi connector: `mcode-tools connector tool <tên>` để đối chiếu schema hiện hành; mọi request ảnh khai rõ `area` |
| 155 | **Soi ảnh hàng loạt bằng nhiều tờ contact sheet nhỏ ⇒ bỏ sót chữ AI vẽ trong nền.** Tập 10 (12/11/2026): 71 nền soi qua 6 tờ contact sheet, tưởng sạch; ghép 1 tờ montage 3104×2160 thấy ngay nền `t10_truth_revealed_shattered_phantom` có chữ "THE COMPANY" khắc trên bảng hiệu vỡ; soi tiếp nhóm nền có giấy/bìa ở ô 900 px thấy nền `t10_fbi_academy_profiling_archive` có bìa sách khắc "Stan Case Study / Psychological / …" ⇒ vi phạm H2/H5/H17. Ô nhỏ ở mức thumbnail **không đủ để đọc chữ** | Duyệt nền bằng **montage** (`.work/qc_montage.py --kind bg`, ô ≥ 384 px; nền có giấy/bìa thì ô ≥ 900 px) và **mở full-res đúng nền bị nghi** (montage chỉ thay tờ nhiều, **không thay zoom 100 %**). Với ảnh tĩnh: dùng `--list` để chỉ ghép shot rủi ro (luật H20). **Cổng QC xanh không bảo chứng nền sạch chữ** — phải soi mắt |
| 156 | **Kịch bản sửa lại SAU khi đã xuất bản video ⇒ mã câu dịch chuyển ⇒ bảng ánh xạ nền (`BG_FIX`) và bảng shot cũ trỏ SAI câu.** Tập 09 (13/11/2026): người dùng viết lại kịch bản VN 199 → 207 câu (1.02 +3 · 2.06 +1 · 3.08 +1 · 4.05 +1 · 4.09 +2 · 5.04 +1 · 5.05 −1) và commit lúc 08:07. `BG_FIX` gắn nền theo **mã câu** ⇒ chỉ cần chèn 3 câu ở đầu 1.02 là mọi mã sau đó lệch hết, nền cũ rơi sang câu khác | Dựng bảng OLD → NEW bằng `git show HEAD~1:...` so với HEAD, khớp theo **văn bản nguyên văn** (KHÔNG dùng “câu nào không có trong old” vì câu viết lại cùng nghĩa sẽ bị tính nhầm là câu mới) → dựng lại khối `BG_FIX` theo thứ tự element. Sau khi sửa: 207/207 mã có nền, **mọi nền trên đĩa đều được gán ≥ 1 lần**, và đo H10 vế 2 (đoạn lặp nền) bằng xấp xỉ “1 câu = 1 shot” (trần trên, gom câu chỉ làm ngắn đoạn lặp) |
| 157 | **Kịch bản còn đang sửa dở (chưa đủ 3 ngôn ngữ) ⇒ CHỈ sinh ảnh gốc, KHÔNG render chữ.** Tập 09 (13/11/2026): bảng shot tra chữ theo **cùng một mã câu** cho cả 3 ngôn ngữ (`S[lang][sid]`) và timeline cũng tra theo mã câu ⇒ EN/JA còn 199 câu trong khi VN đã 207 ⇒ `KeyError` khi render, timeline thiếu 9 mã câu mới | Khi kịch bản đang sửa: **sinh trước ảnh nền + cập nhật `BG_FIX`**, chờ cả 3 script khớp mã câu và timeline đã đủ mã rồi mới sinh bảng shot / render chữ. Quyết định của người dùng 13/11/2026: “chỉ tạo ảnh gốc, phần render chữ thì chờ tôi sửa kịch bản đủ 3 ngôn ngữ” |
| 158 | **MiniMax hết credit khi sinh nền MỚI cho một tập đã có checkpoint.** Tập 09 (13/11/2026): `gen_bg_minimax_t09.jsonl` đã ghi 65 tên ⇒ 3 nền mới không tự được sinh; MiniMax trả lỗi `image generation needs at least 100 credits` vì số dư < 100 credit | Thêm job mới vào `bg_jobs_t09.json` rồi chạy `--only <tên>` (checkpoint cũ không chặn), và chạy supervisor `_t09_gen_supervisor.py` (nghỉ 180 s/vòng, tối đa 8 h) ⇒ người dùng chỉ cần **nạp credit là ảnh tự sinh**, không phải canh |
| 159 | **Chạy song song 2 GPU Kaggle (2x Tesla T4) bị văng tiến trình do tràn System RAM (Linux OOM-Killer mã lỗi -9).** Tập 12 (13/11/2026): Kaggle cấp 2 GPU T4 (16GB VRAM mỗi GPU) nhưng System Host RAM chỉ ~30GB. Khởi chạy 2 process Python độc lập đồng thời (`subprocess.Popen` cho `worker_0` và `worker_1`) khiến cả 2 nạp weights 4B vào RAM hệ thống cùng lúc ($2 \times 10\text{ GB} = 20\text{ GB} + \text{runtime} > 30\text{ GB}$) ⇒ kernel Linux gửi tín hiệu SIGKILL (-9) tiêu diệt GPU 0 | **CẤM khởi động đồng thời 2 process Python độc lập.** Chạy song song 2 GPU chuẩn bằng 1 trong 2 cách: (1) **Staggered Subprocess Startup:** Worker 0 khởi động trước, nạp xong model vào VRAM giải phóng Host RAM (~90 s) rồi `time.sleep(120)` mới khởi chạy Worker 1 (`CUDA_VISIBLE_DEVICES=1`); (2) **Thread-based Parallelism:** dùng 1 process Python với `ThreadPoolExecutor(max_workers=2)`, nạp trực tiếp model vào `cuda:0` và `cuda:1` chia sẻ chung runtime. Giảm 50% thời gian render (từ ~55 phút xuống ~25–28 phút) |

## A12. Cấu hình tập mới — một mục trong `.work/edition.py`

Từ 23/10/2026 **không sửa script** cho tập mới. Thêm mục `"XX"` vào `EPISODES` của `edition.py` và chạy mọi lệnh với `AE_EP=XX`. File trung gian của tập ≠ 01 có hậu tố `_tXX`, nên các tập không ghi đè nhau.

| Khoá | Ý nghĩa | Tập 02 |
|---|---|---|
| `script` · `dir` · `plan` · `master` · `srt` | đường dẫn kịch bản json, thư mục tập, hồ sơ, tên file ra | `script_tap02.json` · `Tap02` · `KeHoach_Video_Tap02.md` · `Tap02_master` · `Tap02.srt` |
| `n_element` | phần tử nào là N1/N2 | `{"1.07": "N1", "4.06": "N2"}` |
| `acting` | file diễn xuất từng câu (A4.2) | `acting_tap02.json` |
| `sfx_sheet` | bảng âm thanh stereo (nền · tiếng động · tắt nhạc) | `sfx_tap02.json` |
| `act1_cue` · `silence_cue` · `click_cues` | mốc nhạc Hồi 1 vào · "nhạc dừng đột ngột" · tiếng "Tách" | `"1.16"` · `"1.09"` · `("1.06",)` |
| `bed` | nhạc nền theo hồi | cello · piano · cello_v2 · sub_drone · piano_warm |
| `sfx_cues` | SFX kiểu cũ (Tập 01) | `[]` |
| `combo` · `inset` · `bg2` | cảnh ghép, ảnh ghim, đổi nền trong shot (theo **mã shot của tập đó**) | `{}` |
| `flag_hold_shots` · `route_pins` | dòng giữ hình vẽ cờ · nhãn 2 ghim T7 | `()` · `{}` (ghim không nhãn) |
| `thumb` · `thumb_bg` · `title` · `act_titles` · `summary` · `need` | chữ và nền thumbnail, tiêu đề mô tả, tên 5 hồi, câu tóm tắt, câu cần nguồn | "ĐẠI TÁ / HAI MẶT" · `t2_two_chairs` · … |
| `case` · `n1` · `n2` | tên vụ trên badge Điều tra viên, nhãn N1/N2 | `Williams` · "BINH SĨ CĂN CỨ TRENTON" · "KHÁN GIẢ" |
| `cast` | **chỉ khai khi đổi giọng** (đã qua G8–G10); để `None` = dùng bộ A | `None` — Tập 01 ghim bộ giọng cũ |

**Kiểm tra hồi quy khi sửa script dùng chung:** chạy lại `tts_sentences.plan_items()` và `parse_shots.py` của Tập 01, so với bản cũ — phải giống hệt (đã làm 22/10: 122 shot giống hệt, âm thanh lệch 1 mẫu / 50 triệu do thứ tự cộng số thực).

## A13. Rủi ro chung

| Rủi ro | Xử lý |
|---|---|
| Linh thú làm nhẹ tính nghiêm trọng | Biểu cảm nghiêm, ≤ 20% khung, `⊘` ở khoảnh khắc nặng nề |
| Người xem tưởng nhân vật là người thật | V6 + dàn khách mời + mô tả |
| Intro 22 s trước phần mồi làm người xem thoát | Theo dõi tỉ lệ giữ chân; phương án B: đưa intro ra sau câu mồi đầu tiên |
| Nhạc AI bị Content ID nhận nhầm | Kháng nghị bằng `provenance.json` |
| Điều khoản thương mại chưa rõ | Kiểm tra trước khi bật kiếm tiền |

---

*Tách từ bản v10 gộp ngày 22/10/2026 (lưu ở `90_LUU_TRU/ke_hoach_cu/`).*
