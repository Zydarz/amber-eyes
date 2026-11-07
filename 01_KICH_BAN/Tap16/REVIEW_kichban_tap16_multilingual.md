# BÁO CÁO THẨM ĐỊNH KỸ THUẬT ĐA NGÔN NGỮ (MULTILINGUAL TECHNICAL AUDIT)
## TẬP 16: HỒ SƠ JOHN LIST (BẢN TIẾNG VIỆT, TIẾNG ANH, TIẾNG NHẬT, TIẾNG HÀN)

> **Căn cứ tiêu chuẩn:**
> - Quy tắc L1–L10, G1–G13, V1–V9 (`AGENTS.md`).
> - Tiêu chuẩn kỹ thuật kịch bản A2b, A2c (`00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md`).
> - Bộ công cụ kiểm định tự động:
>   - `.work/_qc_all_4scripts_tap16.py`
>   - `.work/_qc_ko_parity.py`
>   - `.work/_qc_ja.py 16`
>   - `.work/scratch/verify_parity_tap16.py`

---

### I. BẢNG TỔNG HỢP SỐ ĐO THỰC TẾ (RULE L3)

| Chỉ số kỹ thuật | Bản Tiếng Việt (VN Master) | Bản Tiếng Anh (EN) | Bản Tiếng Nhật (JA) | Bản Tiếng Hàn (KO) | Trạng thái đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Đường dẫn file** | `01_KICH_BAN/Tap16/kichban_tap16_23102026.md` | `01_KICH_BAN/Tap16_EN/kichban_tap16_EN.md` *(+ bản sao `Tap16/`)* | `01_KICH_BAN/Tap16_JA/kichban_tap16_JA.md` | `01_KICH_BAN/Tap16_KO/kichban_tap16_KO.md` | Đầy đủ 4 ngôn ngữ |
| **Số Hồi (Acts)** | 5 Hồi | 5 Hồi | 5 Hồi | 5 Hồi | **Khớp 100% (1, 2, 3, 4, 5)** |
| **Tổng số phần tử (Elements)** | **51** | **51** | **51** | **51** | **Khớp 100%** |
| **Số lượt thoại (LOI turns)** | **32** | **32** | **32** | **32** | **Khớp 100%** |
| **Số thẻ hiệu ứng (SFX)** | 13 | 13 | 13 | 13 | **Khớp 100%** |
| **Số thẻ nhạc nền (BGM)** | 6 | 6 | 6 | 6 | **Khớp 100%** |
| **Tổng số câu đọc (Sentences)** | **220** | **220** | **220** | **220** | **Khớp 100% (>= 200 câu)** |
| **Tổng số từ (Word Count)** | 6.843 từ | 4.474 từ | 238 từ (cụm) | 3.653 từ | Phù hợp đặc thù ngôn ngữ |
| **Thời lượng ước tính** | 26 – 28 phút | 25 – 27 phút | 26 – 28 phút | 26 – 28 phút | Đạt chuẩn video chuyên sâu |

---

### II. BẢNG CHI TIẾT ĐỒNG BỘ CÂU THEO TỪNG HỒI & TỪNG LƯỢT THOẠI (1:1 PARITY)

#### HỒI 1: BIỆT THỰ U ÁM BREEZE KNOLL VÀ KHÁM PHÁ KINH HOÀNG SAU MỘT THÁNG (12 phần tử, 7 lượt thoại, 50 câu)
| ID Phần tử | Loại (Kind) | Vai (Role) | Hướng diễn xuất chính | Số câu VN | Số câu EN | Số câu JA | Số câu KO |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **1.01** | BGM | — | Dark Ambient tôn giáo u uất, Organ lạnh lẽo | — | — | — | — |
| **1.02** | LOI | **H** (Host) | Trầm ấm, mở đầu hồ sơ bí ẩn thế kỷ | 6 | 6 | 6 | 6 |
| **1.03** | SFX | — | Tiếng gió rít, tiếng gõ cửa gỗ biệt thự bỏ hoang | — | — | — | — |
| **1.04** | LOI | **D** (Điều tra viên) | Khách quan, sắc lạnh, hiện trường ban đầu | 8 | 8 | 8 | 8 |
| **1.05** | SFX | — | Tiếng tra chìa khóa, tiếng cửa nặng nề mở kẽo kẹt | — | — | — | — |
| **1.06** | LOI | **H** (Host) | Kịch tính, vỡ lở khủng hoảng tài chính | 7 | 7 | 7 | 7 |
| **1.07** | LOI | **N** (N1 - Jean Phillips) | Bàng hoàng, linh cảm bất an của học sinh | 6 | 6 | 6 | 6 |
| **1.08** | LOI | **D** (Điều tra viên) | Nghiệp vụ, bóc tách dấu vết hiện trường | 7 | 7 | 7 | 7 |
| **1.09** | SFX | — | Tiếng bước chân thám tử trên sàn gỗ, tiếng nhạc đài | — | — | — | — |
| **1.10** | LOI | **H** (Host) | Lặng đi, khoảnh khắc phát hiện thảm kịch | 8 | 8 | 8 | 8 |
| **1.11** | SFX | — | Tiếng radio rè rè phát thánh ca, tiếng gió lùa | — | — | — | — |
| **1.12** | LOI | **C** (Chuyên gia) | Điềm đạm, đặt câu hỏi bản chất tội phạm | 8 | 8 | 8 | 8 |

#### HỒI 2: VỤ MẤT TÍCH THẾ KỶ VÀ CHIẾC KÉO CẮT MẶT TRONG ALBUM ẢNH (11 phần tử, 6 lượt thoại, 41 câu)
| ID Phần tử | Loại (Kind) | Vai (Role) | Hướng diễn xuất chính | Số câu VN | Số câu EN | Số câu JA | Số câu KO |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **2.01** | BGM | — | Tiếng đàn Organ nhà thờ u tối, nhịp điệu rình rập | — | — | — | — |
| **2.02** | LOI | **D** (Điều tra viên) | Sắc bén, hành vi cắt mặt trong album ảnh | 7 | 7 | 7 | 7 |
| **2.03** | SFX | — | Tiếng kéo sắt lách cách cắt mép ảnh, tiếng giấy rơi | — | — | — | — |
| **2.04** | LOI | **H** (Host) | Cuộc truy lùng vô vọng và dấu vết sân bay JFK | 7 | 7 | 7 | 7 |
| **2.05** | SFX | — | Tiếng còi tàu hỏa hú dài trong đêm, tiếng bánh xe nghiến | — | — | — | — |
| **2.06** | LOI | **D** (Điều tra viên) | Thấu thị, kế hoạch xóa dấu vết có tính toán | 6 | 6 | 6 | 6 |
| **2.07** | SFX | — | Tiếng lật trang tài liệu điều tra, tiếng gõ bàn phím cơ | — | — | — | — |
| **2.08** | LOI | **H** (Host) | Thời gian trôi qua, vụ án đóng băng 18 năm | 7 | 7 | 7 | 7 |
| **2.09** | SFX | — | Tiếng đồng hồ quả lắc tích tắc cô tịch, tiếng củi nổ | — | — | — | — |
| **2.10** | LOI | **C** (Chuyên gia) | Phân tích cơ chế biến mất của hung thủ OCPD | 7 | 7 | 7 | 7 |
| **2.11** | LOI | **H** (Host) | Đúc kết ngõ cụt 18 năm của lực lượng điều tra | 7 | 7 | 7 | 7 |

#### HỒI 3: GIẢI MÃ TÂM LÝ: RỐI LOẠN NHÂN CÁCH ÁM ẢNH CƯỠNG CHẾ (OCPD) & BẪY NGỤY BIỆN ĐẠO ĐỨC (9 phần tử, 7 lượt thoại, 45 câu)
| ID Phần tử | Loại (Kind) | Vai (Role) | Hướng diễn xuất chính | Số câu VN | Số câu EN | Số câu JA | Số câu KO |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **3.01** | BGM | — | Minimalist Piano sâu lắng, Drone điện tử căng thẳng | — | — | — | — |
| **3.02** | LOI | **C** (Chuyên gia) | Học thuật, định danh OCPD và vị tha méo mó | 6 | 6 | 6 | 6 |
| **3.03** | LOI | **H** (Host) | Tuổi thơ ngột ngạt và sự sụp đổ của trật tự giả tạo | 6 | 6 | 6 | 6 |
| **3.04** | LOI | **C** (Chuyên gia) | Bóc tách kỹ thuật "Mục đích cao cả" | 6 | 6 | 6 | 6 |
| **3.05** | LOI | **H** (Host) | Bức thư 5 trang gửi mục sư và sự ngụy biện đức tin | 7 | 7 | 7 | 7 |
| **3.06** | SFX | — | Tiếng ngòi bút máy sột soạt trên giấy, tiếng thở dài | — | — | — | — |
| **3.07** | LOI | **C** (Chuyên gia) | Sự chia ngăn nhận thức (Compartmentalization) | 7 | 7 | 7 | 7 |
| **3.08** | LOI | **D** (Điều tra viên) | Thực tế nghiệt ngã đối lập với ngụy biện tâm lý | 7 | 7 | 7 | 7 |
| **3.09** | LOI | **H** (Host) | Đúc kết sự nguy hiểm của ảo tưởng đạo đức | 6 | 6 | 6 | 6 |

#### HỒI 4: BỨC TƯỢNG SÁP CỦA FRANK BENDER VÀ CÚ ĐIỆN THOẠI TỪ AMERICA’S MOST WANTED (13 phần tử, 8 lượt thoại, 49 câu)
| ID Phần tử | Loại (Kind) | Vai (Role) | Hướng diễn xuất chính | Số câu VN | Số câu EN | Số câu JA | Số câu KO |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **4.01** | BGM | — | Tiếng đàn Violin dồn dập, tiết tấu phá án khẩn trương | — | — | — | — |
| **4.02** | LOI | **H** (Host) | Bước ngoặt truyền hình và điêu khắc pháp y | 7 | 7 | 7 | 7 |
| **4.03** | SFX | — | Tiếng gõ nhẹ dụng cụ nặn đất sét, hơi thở tập trung | — | — | — | — |
| **4.04** | LOI | **H** (Host) | Cặp kính gọng sừng định mệnh của Frank Bender | 6 | 6 | 6 | 6 |
| **4.05** | SFX | — | Tiếng nhạc hiệu truyền hình, tiếng chuông điện thoại | — | — | — | — |
| **4.06** | LOI | **D** (Điều tra viên) | Buổi phát sóng định mệnh và cuộc gọi Colorado | 7 | 7 | 7 | 7 |
| **4.07** | SFX | — | Tiếng phanh xe FBI, tiếng cửa kính văn phòng đẩy mạnh | — | — | — | — |
| **4.08** | LOI | **H** (Host) | Cuộc vây bắt chớp nhoáng tại Virginia | 6 | 6 | 6 | 6 |
| **4.09** | LOI | **N** (N2 - Wanda Flanery) | Chân thực, sự bàng hoàng về người hàng xóm | 6 | 6 | 6 | 6 |
| **4.10** | LOI | **D** (Điều tra viên) | Lăn dấu vân tay và khoảnh khắc cúi đầu | 6 | 6 | 6 | 6 |
| **4.11** | SFX | — | Tiếng còng số tám tra vào cổ tay, tiếng sập cửa sắt | — | — | — | — |
| **4.12** | LOI | **C** (Chuyên gia) | Sự sụp đổ của chiếc mặt nạ bình thường hóa | 6 | 6 | 6 | 6 |
| **4.13** | LOI | **H** (Host) | Kết thúc 18 năm trốn chạy dưới hai thân phận | 5 | 5 | 5 | 5 |

#### HỒI 5: BÀI HỌC ĐẮT GIÁ VỀ SỰ CUỒNG KIỂM SOÁT & 4 CẢNH BÁO ĐỎ (6 phần tử, 4 lượt thoại, 35 câu)
| ID Phần tử | Loại (Kind) | Vai (Role) | Hướng diễn xuất chính | Số câu VN | Số câu EN | Số câu JA | Số câu KO |
|:---:|:---:|:---:|---|:---:|:---:|:---:|:---:|
| **5.01** | BGM | — | Tiếng Piano ấm áp, trang trọng, triết lý nhân văn | — | — | — | — |
| **5.02** | LOI | **H** (Host) | Tuyên đọc phán quyết 5 án tù chung thân | 6 | 6 | 6 | 6 |
| **5.03** | LOI | **D** (Điều tra viên) | Di sản khoa học hình sự và sự khép lại vụ án | 5 | 5 | 5 | 5 |
| **5.04** | LOI | **C** (Chuyên gia) | Bóc tách bản ngã ái kỷ độc hại và tình yêu gia đình | 6 | 6 | 6 | 6 |
| **5.05** | LOI | **H** (Host) | Đúc kết 4 cảnh báo đỏ thực tế và thông điệp kết | 18 | 18 | 18 | 18 |
| **5.06** | BGM | — | Piano ngân vang trang trọng rồi fade out | — | — | — | — |

**Tổng cộng toàn tập:** **51 phần tử · 32 lượt thoại · 220 câu thoại (khớp tuyệt đối 1:1 trên toàn bộ 4 ngôn ngữ).**

---

### III. KẾT QUẢ KIỂM ĐỊNH CÁC CỔNG CHẤT LƯỢNG (QC GATES)

#### 1. Kiểm định YouTube Safe & Quy tắc V9 (Tất cả 4 ngôn ngữ)
- **Từ cấm tiếng Việt (V9 / A9.2):** `máu`, `thi thể`, `đập tan`, `đập loạn`, `tự sát`, `cắt cổ`, `chặt`, `bóp cổ`, `khí độc`, `ngạt thở` $\rightarrow$ **0 vi phạm**.
- **Từ cấm tiếng Anh:** `blood`, `corpse`, `decapitat`, `strangl`, `suicide` $\rightarrow$ **0 vi phạm**.
- **Từ cấm tiếng Nhật:** `自殺`, `死体`, `血液`, `窒息` $\rightarrow$ **0 vi phạm** (đã thay thế `心血` $\rightarrow$ `心魂`, `窒息` $\rightarrow$ `押し潰す/破滅的`).
- **Từ cấm tiếng Hàn:** `자살`, `시체`, `혈흔`, `질식` $\rightarrow$ **0 vi phạm** (đã thay thế `질식` $\rightarrow$ `억누르고 짓밟습니다`).
- **Quy tắc G1 (Dấu ba chấm `...` / `…` trong câu):** **0 vi phạm** trên cả 4 bản.

#### 2. Cổng kiểm định 4 ngôn ngữ tổng thể (`.work/_qc_all_4scripts_tap16.py`)
```
==========================================
PARITY AUDIT ACROSS 4 EDITIONS
==========================================
VN: 51 elements, 32 LOI turns, 220 sentences -> MATCH
EN: 51 elements, 32 LOI turns, 220 sentences -> MATCH
JA: 51 elements, 32 LOI turns, 220 sentences -> MATCH
KO: 51 elements, 32 LOI turns, 220 sentences -> MATCH

>>> FINAL STATUS TAP 16: ALL PASS <<< (Exit Code: 0)
```

#### 3. Cổng kiểm định Tiếng Hàn (`.work/_qc_ko_parity.py`)
```
ok    acts: 5 (1,2,3,4,5)
ok    51 elements aligned (kind/role/sentence-count/pause)
ok    total sentences: 220
ok    hangul share of narration: 87.9% (yêu cầu >= 60%)
ok    no vietnamese-only diacritics in KO narration
ok    no hanja/chinese characters in KO narration
ok    list items: 0 (same order, same kind)
ok    quotes: 10 (type-1 = keep English inside, type-2 = translate inside)
PASS  kichban_tap16_KO.md — 51 elements, 220 sentences, parity with kichban_tap16_23102026.md (Exit Code: 0)
```

#### 4. Cổng kiểm định Tiếng Nhật (`.work/_qc_ja.py 16`)
```
OK   Tap16: câu VN=220 JA=220 | lượt VN=32 JA=32 | lượt lệch câu=0 | lỗi: không
==> 1/1 tập đạt · -> D:\TEST\Gax\amber-eyes\.work\_ja_qc.txt (Exit Code: 0)
```
- Đã đồng bộ cấu trúc bảng thông số kỹ thuật (8 hàng chuẩn hóa).
- Đã áp dụng chuẩn danh mục thuật ngữ `TERMS` trong `ja_glossary.py`:
  - `Rối loạn nhân cách ám ảnh cưỡng chế` $\rightarrow$ `強迫性人格障害`
  - `KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM` $\rightarrow$ `犯罪心理学オーディオ／ポッドキャスト台本`
  - `THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN` $\rightarrow$ `制作仕様とナレーション構成`
  - `4 cảnh báo đỏ` $\rightarrow$ `4つの赤い警告`
  - `đặc vụ FBI` $\rightarrow$ `FBI特別捜査官`

---

### IV. TÍNH TƯƠNG THÍCH PIPELINE SẢN XUẤT VIDEO & ÂM THANH

1. **Biên dịch JSON kịch bản:**
   - Đã chạy thành công `parse_kichban.py` tạo `.work/script_tap16.json` với chính xác 51 phần tử và 220 câu đọc.
2. **Cấu hình Tập 16 trong `.work/edition.py`:**
   - `summary`: `("1.02#1", "3.02#1")` $\rightarrow$ Cả hai câu mở đầu tóm tắt đều tồn tại nguyên vẹn.
   - `n_element`: `{"1.07": "N1", "4.09": "N2"}` $\rightarrow$ Cả 2 lượt thoại nhân chứng khớp chính xác vị trí và vai N1 (Jean Phillips) / N2 (Wanda Flanery).
   - `act1_cue`: `1.10` $\rightarrow$ Thẻ chuyển nhạc nằm ở vị trí hợp lệ trong Hồi 1.
   - `click_cues`: `("1.03", "4.05")` $\rightarrow$ Khớp chuẩn các điểm nhấn SFX.
3. **Sẵn sàng cho các công đoạn tiếp theo:**
   - Kịch bản đạt chuẩn sẵn sàng chuyển giao cho công đoạn Diễn xuất (`make_acting_tap16.py`), Đọc giọng AI (`tts_sentences.py`), và Dựng hình (`build_video3.py`).
