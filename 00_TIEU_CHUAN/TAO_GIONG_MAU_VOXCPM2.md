# TẠO GIỌNG MẪU CHO HIGGS — BẰNG VOXCPM2 (VOICE DESIGN)

**Ngày:** 28/10/2026 · **Người lập:** Mavis · **Phạm vi:** kênh Amber Eyes, bản tiếng Việt
**Trạng thái:** đã chốt hướng, **chưa chạy thử** (cần người dùng tải audio từ web về).

> Tài liệu này là **phần trước** của `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md`. Đọc file đó trước (đặc biệt mục 4 — chuẩn file tham chiếu, mục 9 — cổng nghiệm thu). Tài liệu này chỉ nói **lấy mẫu giọng bằng cách nào**.

---

## 0. Quyết định đã chốt (28/10/2026)

| # | Quyết định | Lý do |
|---|---|---|
| 1 | **Nguồn mẫu: VoxCPM2** (`voxcpm2.org` → HF Space `openbmb-voxcpm-demo`) | Apache-2.0, **thương mại thoải mái** ⇒ **giải quyết nút thắt L4** (điều khoản MiniMax chưa rõ) |
| 2 | **Giọng Việt chuẩn, bản địa** (không cố giữ chất "nước ngoài đọc tiếng Việt" của bộ A) | VoxCPM2 sinh tiếng Việt ra giọng bản địa; bản địa = đúng thanh điệu ⇒ khửa điểm yếu **CER 3,1%** của vai D |
| 3 | **Tuổi:** H 35–45 · D 35–45 · C 50–60 | Tài liệu cũ không có con số tuổi; C = "bác sĩ lớn tuổi, tóc hoa hâm" (`PhuongAn_TaoHinh_5NhanVat.md`) |
| 4 | **Phạm vi lần này: 7 vai** — 3 vai chính + 4 giọng nhân chứng | N1/N2 **đổi giới tính theo tập** ⇒ không dùng 1 file tham chiếu chung được |
| 5 | **Cảnh báo thay đổi thương hiệu âm thanh:** Tập 08+ sẽ đổi chất giọng so với Tập 01–07 (bộ A MiniMax) | Chấp nhận để đổi chất giọng; đổi lại tiếng Việt đúng thanh điệu |

---

## 1. Vì sao VoxCPM2 (đã kiểm chứng 28/10/2026)

| Tiêu chí | Số liệu |
|---|---|
| Giấy phép | **Apache-2.0** — weights + code, thương mại thoải mái, **không cần ghi công** |
| Chế độ **Voice Design** | Có. Mô tả giọng bằng **chữ** (giới tính, tuổi, cao độ, chất giọng, cảm xúc, nhịp đọc) → sinh giọng mới, **không cần audio tham chiếu** |
| Tiếng Việt | Có trong danh sách **30 ngôn ngữ**. Đo nội bộ: **WER 1,56%**. Minimax-MLS-test: WER **3,31%** (MiniMax 0,88%) · SIM **80,6%** (MiniMax 74,3%) |
| Đầu ra | **48 kHz** (README GitHub). ⚠ FAQ trên `voxcpm2.org` ghi 24 kHz — **đã lỗi thời**, tin README |
| Kích thước | 2B, backbone MiniCPM-4. Chạy local: Python 3.10–3.13, PyTorch ≥ 2.5, CUDA ≥ 12 (Apple Silicon dùng MPS) |
| Độ ổn định | README ghi rõ: *"Voice Design … results can vary between runs — you may try to generate 1~3 times"* ⇒ **phải sinh nhiều bản** (mục 5) |

**Vì sao bỏ đường "MiniMax → làm mẫu"**: bộ mẫu hiện tại trong `assets/voice_ref_higgs/` được cắt từ audio MiniMax, và `QUY_TAC_AUDIO_HIGGS.md:68` ghi trạng thái **"chờ người dùng xác nhận điều khoản MiniMax cho phép dùng đầu ra làm tham chiếu"**. VoxCPM2 loại bỏ hẳn ràng buộc đó.

---

## 2. Vị trí trong pipeline

```
VoxCPM2 (Voice Design)  →  mẫu giọng .wav 24kHz mono, -18 LUFS, 8–15 s
        ↓  clone (mỗi vai 1 file tham chiếu + ref_text chép đúng từng chữ)
Higgs Audio v3 (Mac mini M2, MLX-Audio)  →  đọc cả tập
        ↓
build_audio3.py → video
```

**Quy tắc bất di bất dịch (theo `QUY_TAC_AUDIO_HIGGS.md` §4):**
- **Mỗi vai = MỘT file tham chiếu, cố định cho cả tập và cả kênh.** Đổi file tham chiếu = đổi giọng nhân vật.
- **File tham chiếu phải trung tính về cảm xúc.** Tham chiếu buồn/nhanh ⇒ mọi câu đều buồn/nhanh. Vì vậy câu mẫu bên dưới được viết **nội dung trung tính**, chỉ đủ 6 thanh — không phải câu hé lộ.
- `ref_text` = **chép đúng từng chữ** file mẫu đọc ra (kể cả "ờ, à").
- **Cấm** clone giọng người thật (người trong vụ án, phóng viên, diễn viên, giọng tải từ YouTube).

---

## 3. Bảng vai + F0 mục tiêu

| Vai | Linh thú | Giới | F0 mục tiêu | Chất giọng | Nguồn mô tả |
|---|---|---|---|---|---|
| **H** | Cú · Host | nam | **100–106 Hz** | trầm ấm, điềm tĩnh, sắc sảo, sâu lắng | "Giọng nam trầm ấm, điềm tĩnh, sắc sảo" (Tập 01–07) |
| **D** | Sói · Điều tra viên | nam | **138–148 Hz** | đanh thép, sắc bén, chững chạc, lạnh lùng | "Giọng nam đanh thép, lạnh lùng, dứt khoát" |
| **C** | Cáo · Chuyên gia | nữ | **202–212 Hz** | điềm đạm, học thuật, sâu sắc, rõ ràng | "Giọng nữ điềm đạm, học thuật" + bác sĩ lớn tuổi |
| **W1** | nhân chứng nữ trẻ | nữ | **228–242 Hz** | trẻ, sáng, hơi thở, đời thường | "nữ trẻ bàng hoàng, nghẹn ngào" |
| **W2** | nhân chứng nữ TB | nữ | **180–192 Hz** | ấm, trầm, chậm, người lớn | "nữ trung niên nghẹn ngào, đau xót" |
| **W3** | nhân chứng nam trẻ | nam | **162–175 Hz** | trẻ, sôi nổi, đời thường | "nam trẻ, bàng hoàng, dồn dập" |
| **W4** | nhân chứng nam TB | nam | **120–128 Hz** | khàn, già, run, chắn chắn | "nam trung niên uất nghẹn, cay đắng" |

> **W1–W4 thay cho N1/N2.** N1/N2 là *vai động* — giới tính và tuổi đổi theo tập:
> N1 nam ở T05 · T23 · T25 · T26 · T29; N2 nam ở T06 · T08 · T11 · T12 · T13 · T24 · T25 · T27 · T28.
> Bộ A hiện tại ép **cả N1/N2 là giọng nữ** ⇒ đã lệch với chú thích trong kịch bản. Dùng 4 file tham chiếu + khai `cast` riêng cho từng tập trong `edition.py`.

### 3.1 Ghép N1/N2 → W1–W4 cho 29 tập (chốt 29/10/2026)

Nguồn: chú thích vai trong `01_KICH_BAN/TapXX/kichban_tapXX_*.md`. Bản máy đọc: `.work/voxcpm_cast_n_tap.json`. **Chưa vào `edition.py`** — chỉ khai sau khi qua cổng V8 và người dùng đồng ý (L4, L8).

**Cách ghép:** nữ trẻ / thanh niên = W1 · nữ trung niên / lớn tuổi = W2 · nam trẻ / thanh niên = W3 · nam trung niên / lớn tuổi = W4.
**✎ = vị trí đã sửa chú thích trong kịch bản tiếng Việt ngày 29/10/2026** (thêm giới/tuổi để cột "→" đọc thẳng từ kịch bản, không phải đoán). Bản gốc từng file lưu ở `.work/_cu/kichban_truoc_sua_vai_N_20261029/`. Chỉ đổi dòng chú thích trong ngoặc; **lời đọc không đổi** (đã kiểm: tách câu 18/18 file giống hệt bản cũ, trừ trường `direction`, trường này chỉ để tham khảo).

| Tập | N1 (vai · kịch bản ghi → giọng) | N2 (vai · kịch bản ghi → giọng) |
|---|---|---|
| T01 | nhân chứng/dư luận · ? → **cần chốt** | người băn khoăn · ? → **cần chốt** |
| T02 | đồng nghiệp căn cứ Trenton · nam trung niên → **W4** ✎ | cư dân Tweed · nữ trung niên → **W2** ✎ |
| T03 | cảnh sát địa phương 1.09 · nam trung niên → **W4** ✎ | cảnh sát quán The Jury Room 2.09 · nam trẻ → **W3** ✎ |
| T04 | đồng nghiệp ca đêm · nữ trẻ → **W1** ✎ | y tá Amy Loughren · nữ trung niên → **W2** ✎ |
| T05 | người dân Park City · nam trung niên → **W4** | con gái hung thủ · nữ thanh niên → **W1** ✎ |
| T06 | Kim Byers · nữ trẻ (17) → **W1** | sĩ quan Mike Albrecht · nam trung niên → **W4** |
| T07 | bà Lynn Roy · nữ trung niên → **W2** | Samantha Boardman · nữ trẻ → **W1** |
| T08 | hành khách tuyến Chiyoda · nữ trẻ → **W1** ✎ | bác sĩ Ikuo Hayashi · nam trung niên → **W4** |
| T09 | cư dân Los Angeles · nữ trung niên → **W2** ✎ | Linda Kasabian · nữ trẻ → **W1** |
| T10 | bạn của Colleen Stan · nữ trẻ → **W1** ✎ | Janice Hooker · nữ trung niên → **W2** ✎ |
| T11 | hàng xóm Port Dalhousie · nữ trẻ → **W1** ✎ | điều tra viên / công tố viên · nam trung niên → **W4** ✎ |
| T12 | Leslie Wagner-Wilson · nữ trẻ → **W1** ✎ | nhân viên FBI / nhà ngoại giao · nam trung niên → **W4** ✎ |
| T13 | bạn học phổ thông của Jennifer · nữ trẻ → **W1** ✎ | ông Huei Hann Pan · nam lớn tuổi → **W4** |
| T14 | bạn thân của Betty · nữ trung niên → **W2** ✎ | Kim Broderick (con gái) · nữ trẻ → **W1** ✎ |
| T15 | bạn, đồng nghiệp của Travis · nữ trẻ → **W1** ✎ | bồi thẩm viên Maricopa · nữ trung niên → **W2** ✎ |
| T16 | cô giáo Jean Phillips · nữ trung niên → **W2** ✎ | hàng xóm Wanda Flanery · nữ trẻ → **W1** ✎ |
| T17 | tổng đài 911 Riverside · nữ trẻ → **W1** ✎ | đại diện trung tâm y tế · nữ trung niên → **W2** ✎ |
| T18 | Kay Woodcock · nữ lớn tuổi (bà nội) → **W2** | bồi thẩm viên Hạt Ada · nữ trẻ → **W1** ✎ |
| T19 | học sinh Parkland · nữ thanh niên → **W1** | bồi thẩm viên Broward · nữ trung niên → **W2** |
| T20 | bạn học Mercer · nữ thanh niên → **W1** | Kaitlyn Giddings Wheeler · nữ trung niên → **W2** |
| T21 | hàng xóm Clear Lake · nữ thanh niên → **W1** ✎ | bồi thẩm viên Harris · nữ trung niên → **W2** |
| T22 | hàng xóm Boynton Beach · nữ thanh niên → **W1** ✎ | bồi thẩm viên Palm Beach · nữ trung niên → **W2** |
| T23 | cư dân Đông LA · nam thanh niên → **W3** | nhà báo phiên tòa LA · nữ trung niên → **W2** |
| T24 | cư dân Hwaseong · nữ trung niên → **W2** | Yoon Sung-yeo · nam trung niên → **W4** |
| T25 | chủ cơ sở massage Seoul · nam thanh niên → **W3** ✎ | đại diện gia đình nạn nhân · nam trung niên → **W4** |
| T26 | cảnh sát Waseda 1948 · nam trẻ → **W3** | người mẹ hậu chiến · nữ trung niên → **W2** |
| T27 | người làm xưởng gỗ · nữ trung niên → **W2** | nhân chứng phiên tòa Bình Phước · nam trung niên → **W4** |
| T28 | người dân Phố Sàn · nữ trung niên → **W2** | nhân chứng phiên tòa Bắc Giang · nam trung niên → **W4** |
| T29 | Tracy Edwards · nam thanh niên → **W3** | đại diện thân nhân · nữ trung niên → **W2** |

**Số liệu (58 vị trí):** 56 có giọng · 2 còn "cần chốt" (T01). Dùng W1 ×19 · W2 ×20 · W3 ×5 · W4 ×12. **Không còn tập nào N1 trùng giọng N2.**

**Cách chọn các điểm đã sửa (để người sau không phải đoán lại):**
- **T02:** N1 (đồng nghiệp ở căn cứ Trenton) = nam trung niên; N2 (cư dân thị trấn Tweed) = nữ trung niên. Lời thoại không có chi tiết giới/tuổi nên đây là **quyết định phân vai**, không phải dữ kiện.
- **T03:** cả hai là cảnh sát năm 1973 → cả hai nam; N1 trung niên (W4), N2 trẻ (W3) để tách giọng.
- **21 vị trí "đề xuất" cũ:** N1 → trẻ, N2 → trung niên làm mặc định. Ngoại lệ do **lời thoại buộc**: T05 N2 và T14 N2 là con gái nhắc cha mẹ ("tuổi thơ", "mẹ tôi… cha tôi") → trẻ; T14 N1 nhắc "tuổi thanh xuân" của Betty → trung niên; T16 N1 là cô giáo → trung niên.
- **T21 · T22:** đổi **N1** (hàng xóm) từ trung niên sang thanh niên (W1); N2 (bồi thẩm viên) giữ trung niên (W2). Lời N1 không có chi tiết tuổi.
- **T25:** đổi **N1** (chủ cơ sở massage) sang thanh niên (W3). **Không** đổi N2 vì lời N2 nói "cha mẹ tôi… những người già" ⇒ N2 phải ở tuổi trung niên (K8).

**Còn lại cần chú ý:**
1. **T01:** kịch bản vẫn không ghi giới cho N1/N2 (người dùng chưa yêu cầu sửa). Tập này hiện dùng giọng MiniMax đã dựng.
2. **Nhãn tuổi mô tả giọng, không phải khẳng định tuổi người thật.** Với người có thật (Kasabian, Hooker, Boardman, Byers, Kay Woodcock, Wanda Flanery, Kerri Rawson…) tôi **chưa đối chiếu tuổi thật** (K1/L2); nhãn chỉ để chọn W. Lời dẫn vẫn phải giữ "dựng lại từ hồ sơ" (K3).
3. **T16 N2 · T18 N2:** lời là bồi thẩm viên / hàng xóm "trầm tĩnh, nghiêm nghị" nhưng bị ép vào W1 (trẻ, sáng, hơi thở) vì N1 đã giữ W2. **Nghe thử ở cổng V8**; không hợp thì đổi tuổi người còn lại (không đổi người thật).
4. **Bản EN / KO / JA chưa đổi theo:** T21, T22, T25 bản KO/JA/EN vẫn ghi N1 "trung niên". Các bản đó chưa có giọng mẫu riêng (§8 mục 6); khi làm phải đồng bộ.
5. **Kịch bản mới từ nay PHẢI ghi giới + tuổi trong chú thích vai N1/N2** (mẫu: `*(N1: Hàng xóm, giọng nữ thanh niên nghẹn ngào)*`) — xem A11 #51.

### ⚠ Cặp F0 dưới 4 nửa cung (G9) — phải tách bằng chất âm
G9 yêu cầu hai giọng cùng giới cách nhau ≥ 4 nửa cung. Ba cặp dưới đây vi phạm, phải bù bằng **chất âm**:

| Cặp | Khoảng cách | Bù bằng |
|---|---|---|
| H ↔ W4 | ~2,8 nc | H = ấm, mượt, ngực · W4 = **khàn, run, già** |
| D ↔ W4 | ~2,4 nc | D = **sắc, gọn, phẳng, không cảm xúc** · W4 = run, uất nghẹn |
| W2 ↔ C | ~2,0 nc | C = **rõ ràng, học thuật, không cảm xúc** · W2 = ấm, mềm |

⇒ **Bắt buộc** nghe mù 3 vai chính (G9) **và** nghe mù H vs W4, D vs W4 trước khi dựng.

---

## 4. PROMPT — dán thẳng vào web

### 4.1 Cách dùng demo (VoxCPM2 Voice Design)

Mở `https://voxcpm2.org/` (nhúng `openbmb-voxcpm-demo.hf.space`) hoặc space chính thức `https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo`.

| # | Ô trên web | Điền gì |
|---|---|---|
| 1 | 🎤 **Reference Audio** | **ĐỂ TRỐNG** ← đây là điều kiện để vào Voice Design |
| 2 | ☑️ **Ultimate Cloning Mode** | **TẮT** (bật thì Control Instruction bị vô hiệu hoá) |
| 3 | 🎙️ Transcript of Reference Audio | trống |
| 4 | 🎛️ **Control Instruction** | dán **Control Instruction** của vai (mục 4.2) |
| 5 | ✍️ **Target Text** | dán **Target Text** của vai (mục 4.2) |
| 6 | ⚙️ Advanced → **Text normalization** | **TẮT** (normalizer là bộ tiếng Anh `wetext` → có thể phá thanh điệu tiếng Việt) |
| 7 | ⚙️ Advanced → Reference audio enhancement | không dùng (không có ref) |
| 8 | ⚙️ Advanced → **CFG** | **2.0** lần đầu; bám mô tả chưa đủ thì tăng **2.5 → 3.0** |
| 9 | 🔊 Generate Speech | xuất ra **MP3** |

**Lưu ý cơ chế (đã đọc mã nguồn `app.py` của Space):**
- `final_text = f"({control}){text}"` — chỉ khi **không** có reference audio. Có ref ⇒ chế độ clone.
- **Web demo KHÔNG có ô seed** ⇒ không tái lập được lần chạy. **Lưu file ngay sau khi sinh**, đặt tên theo vai + số thứ tự bản.
- Lỗi *"backend busy" / "backend timeout"* (429) ⇒ chờ rồi thử lại, không phải lỗi prompt.
- Muốn **seed cố định** (tái lập được) ⇒ chạy CLI local: `voxcpm design --text "…" --control "…" --seed 42 --output out.wav`.

### 4.2 Bảng prompt — 7 vai

> **Control Instruction** viết bằng **tiếng Anh** (Space hỗ trợ "Chinese & English"; tiếng Anh bám mô tả ổn định hơn).
> **Target Text** là câu tham chiếu — trung tính, đủ 6 thanh, không số, không tên nước ngoài, 16–25 s (chuẩn ~20 s, ~75–95 từ).

---

#### H — Host (Cú) · nam 35–45 · F0 100–106 Hz

**Control Instruction**
```
A man in his early forties, low-pitched and warm with a deep chesty resonance, calm and unhurried, intimate late-night podcast narration, Vietnamese Standard, neutral and reflective tone, moderately slow pace
```

**Target Text**
```
Chào mừng bạn đến với chuyên mục giải mã tâm lý tội phạm. Mỗi hồ sơ đều bắt đầu bằng câu hỏi nặng trĩu, mà không ai trả lời nổi, dù sự thật vẫn luôn nằm ở đó. Khi lần theo từng trang tài liệu, chúng ta không tìm kiếm sự phán xét vội vàng, mà cùng nhìn nhận những chuyển biến thầm lặng bên trong một con người, qua từng lời kể và dấu vết còn lưu lại.
```
*(Cập nhật 29/10/2026: mở rộng lên 79 từ để độ dài phát âm đạt ~20 s theo chuẩn dải tối ưu của Higgs Audio v3)*

---

#### D — Điều tra viên (Sói) · nam 35–45 · F0 138–148 Hz

**Control Instruction**
```
A man in his late thirties, mid-low-pitched and firm with a crisp clipped delivery, cold and detached, precise and clinical, Vietnamese Standard, neutral and unemotional tone, slightly brisk pace
```

**Target Text**
```
Hồ sơ ghi lại từng chi tiết. Chẳng lời khai nào khớp với những gì tìm được trong căn nhà. Câu hỏi vẫn còn nguyên, và cả hồ sơ này chưa nói hết. Hiện trường được bảo vệ cẩn thận ngay từ đầu, mọi vật chứng nhỏ nhất đều được đánh số và niêm phong theo đúng trình tự. Chúng tôi phải đối chiếu từng mốc thời gian, kiểm tra lại toàn bộ sơ đồ di chuyển, trước khi đưa ra kết luận cuối cùng.
```
*(Cập nhật 29/10/2026: mở rộng lên 85 từ đạt ~20 s)*

---

#### C — Chuyên gia tâm lý (Cáo) · nữ 50–60 · F0 202–212 Hz

**Control Instruction**
```
A woman in her mid-fifties, mid-pitched and clear with precise articulation, scholarly and composed, strictly neutral and unemotional, Vietnamese Standard, deliberate and measured pace
```

**Target Text**
```
Cơ chế này không đến từ trí nhớ, mà từ cách người ta lặp lại mẫu hình quen thuộc. Đó là lý do hành vi ấy luôn quay trở lại đúng chỗ cũ, và cần được giải thích kỹ. Trong các nghiên cứu lâm sàng, những phản ứng phòng vệ thường bộc lộ rõ nhất khi đối tượng cảm thấy mất quyền kiểm soát. Việc phân tích cấu trúc tâm lý đòi hỏi cái nhìn khách quan, dựa trên chuỗi dữ liệu hành vi đã được ghi nhận trong thời gian dài.
```
*(Cập nhật 29/10/2026: mở rộng lên 92 từ đạt ~20 s)*

---

#### W1 — Nhân chứng nữ trẻ · nữ 18–28 · F0 228–242 Hz

**Control Instruction**
```
A young woman in her early twenties, higher-pitched and bright with a light youthful timbre, conversational and slightly breathy, Vietnamese Standard, neutral and relaxed tone, natural everyday pace
```

**Target Text**
```
Đường này buổi tối vắng lặng, chỉ có tiếng xe chạy rất xa. Tôi hay đi bộ qua chợ, và thường dừng lại ở quầy bán hoa quả. Ai hỏi chuyện ấy, tôi cũng chỉ nhún vai, nửa như không nghe thấy. Dạo đó trời bắt đầu trở gió, mấy hàng quán ven đường đều dọn dẹp sớm hơn thường ngày. Tôi nhớ có nhìn thấy bóng người đứng dưới bóng cây đèn đường, nhưng lúc đó chỉ nghĩ là người đi bộ qua lại bình thường thôi.
```
*(Cập nhật 29/10/2026: mở rộng lên 88 từ đạt ~20 s)*

---

#### W2 — Nhân chứng nữ trung niên · nữ 40–60 · F0 180–192 Hz

**Control Instruction**
```
A woman in her early fifties, mid-pitched and soft with a mature rounded timbre, warm and unhurried, conversational, Vietnamese Standard, neutral and calm tone, slow natural pace
```

**Target Text**
```
Căn nhà này xây từ lâu, nên mùa nào cũng giữ mùi riêng. Tôi thường mở cửa sổ vào buổi sáng, để ánh nắng lọt vào tận góc bếp. Có hỏi về căn nhà, tôi cũng kể từng chuyện, và nhớ rõ từng chi tiết. Quanh đây hàng xóm sống với nhau từ hồi còn trẻ, nhà nào có việc gì thì cả ngõ đều hay biết. Mỗi buổi chiều tôi đều ra tưới mấy chậu cây trước sân, lắng nghe tiếng xe cộ ngoài phố lớn vọng lại chầm chậm.
```
*(Cập nhật 29/10/2026: mở rộng lên 91 từ đạt ~20 s)*

---

#### W3 — Nhân chứng nam trẻ · nam 18–30 · F0 162–175 Hz

**Control Instruction**
```
A young man in his mid twenties, medium-pitched and clear with a light youthful timbre, open and casual, Vietnamese Standard, neutral and relaxed tone, natural everyday pace
```

**Target Text**
```
Xe buýt cuối tuyến chạy khá thưa, nên tôi thường phải đi bộ thêm đoạn dài nữa. Đường lúc đó vắng lặng, chỉ có mấy cây đèn còn sáng, và tôi hay tự hỏi mình sẽ đi bao xa, nửa như không biết. Bình thường tôi hay vừa đi vừa nghe mấy bản nhạc quen thuộc để đỡ thấy đường dài. Gió đêm thổi qua hàng rào sắt kêu lách cách nhè nhẹ, thỉnh thoảng có vài chiếc xe máy chạy lướt qua rồi mất hút vào bóng tối.
```
*(Cập nhật 29/10/2026: mở rộng lên 89 từ đạt ~20 s)*

---

#### W4 — Nhân chứng nam trung niên · nam 40–60 · F0 120–128 Hz

**Control Instruction**
```
A man in his early fifties, lower mid-pitched and slightly rough with an aged timbre, steady and grounded, conversational, Vietnamese Standard, neutral and calm tone, slow natural pace
```

**Target Text**
```
Tôi mở quán trước nhà từ sáng sớm, và mỗi ngày đều đóng cửa khá muộn. Hàng xóm quen mặt, nên ai gọi cửa tôi cũng mở. Có hỏi chuyện buôn bán, tôi cũng chịu nói, nửa như người quen. Khu phố này trước đây vốn yên tĩnh, người qua lại chủ yếu là mấy bác hưu trí đi tập thể dục buổi sáng. Ngồi pha ấm trà bên hiên, tôi quan sát từng sự đổi thay của con đường, ghi nhớ từng bước chân và gương mặt quen thuộc qua từng năm tháng.
```
*(Cập nhật 29/10/2026: mở rộng lên 94 từ đạt ~20 s)*

---

### 4.3 Bảng kiểm nhanh Target Text (trước khi bấm Generate)

> ⚠ **29/10/2026: bảng đếm tay dưới đây có sai** (vd. "với" là thanh sắc, không phải nặng; hàng C liệt kê "bếp" không có trong câu C). **Không dùng bảng này để duyệt** — dùng `tone_coverage` trong `.work/voxcpm_do_mau.py` (luật VX3 của `QUY_TAC_GIONG_MAU_VOXCPM2.md`). Đếm bằng script: H 30 âm tiết (ngang 6 · huyền 8 · sắc 4 · hỏi 4 · ngã 3 · nặng 5) · D 33 (10·11·5·3·2·2) · C 39 (8·10·10·2·4·5) · W1 42 (13·6·9·7·**1**·6) · W2 45 (9·14·8·7·4·3) · W3 43 (14·7·11·4·2·5) · W4 40 (9·7·10·6·3·5). Cả 7 câu đủ 6 thanh; W1 chỉ 1 từ thanh ngã ("cũng").

| Câu | ngang | huyền | sắc | hỏi | ngã | nặng | số | tên NN |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| H | ✓ | ✓ | ✓ *bắt* | ✓ *hỏi, trả, nổi* | ✓ *trĩu* | ✓ *với, tội, nặng* | – | – |
| D | ✓ | ✓ | ✓ *bắt, được, đặt, nói* | ✓ *hỏi, trả, nổi* | ✓ *kỹ* | ✓ *với, nào, và, cả* | – | – |
| C | ✓ | ✓ | ✓ *lặp, được* | ✓ *nhớ* | ✓ *kỹ, giữ* | ✓ *người, thuộc, và, bếp* | – | – |
| W1 | ✓ | ✓ | ✓ *tối, vắng, lặng, tiếng, rất, bộ, thấy* | ✓ *hỏi* | ✓ *nửa* | ✓ *và* | – | – |
| W2 | ✓ | ✓ | ✓ *xây, sổ* | ✓ *hỏi, nhớ* | ✓ *giữ* | ✓ *nào, bếp, về, và* | – | – |
| W3 | ✓ | ✓ | ✓ *buýt, bộ, vắng, lặng* | ✓ *hỏi* | ✓ *nửa* | ✓ *dài, và* | – | – |
| W4 | ✓ | ✓ | ✓ *sớm, mặt* | ✓ *hỏi* | ✓ *nửa* | ✓ *và, muộn, người* | – | – |

> **Nghe bắt buộc:** nếu VoxCPM2 đọc sai 1 từ trong câu (sai thanh điệu, đọc lệch chữ) ⇒ **đổi câu**, đừng đổi giọng. Câu sai thanh điệu được clone ⇒ Higgs học luôn lỗi (đã xảy ra với `Korean_ColdYoungMan`: "Thứ hắn lấy đi" → "Thương hiệu Han Lady", CER 28%).

---

## 5. Sinh nhiều bản, chọn 1 (bắt buộc)

README VoxCPM2: *Voice Design results can vary between runs*. ⇒ **sinh 3–5 bản mỗi vai**, không dùng bản đầu tiên.

1. Sinh 3–5 bản, đặt tên `H_take01.mp3 … H_take05.mp3` (tải về ngay, web không có seed nên không tái lập được).
2. Nghe lọt: đọc đúng chữ? đủ 6 thanh? cảm xúc trung tính (không buồn, không hào hứng)? độ dài 8–15 s?
3. Đo F0 trung vị (`voice_audition.f0_median`) — có nằm trong dải mục tiêu mục 3?
4. Chọn **1 bản** → đóng gói (mục 6). Mọi bản khác giữ lại để đối chiếu.

**Thứ tự ưu tiên khi còn nhiều bản tốt:** đúng chữ → đúng thanh điệu → F0 gần mục tiêu → cảm xúc trung tính → độ dài 8–15 s.

---

## 6. Đóng gói thành file tham chiếu Higgs

Đã có sẵn script: **`.work/higgs_make_refs_voxcpm.py`** (viết mới theo đúng chuỗi của `higgs_make_refs.py`).

```powershell
# 1) đặt audio tải về vào .work/voxcpm_raw/<vai>/takeNN.mp3
# 2) ghi lựa chọn bản thắng vào .work/voxcpm_raw/chosen.json
# 3) chạy
py -3 .work/higgs_make_refs_voxcpm.py
```

**Chuỗi ffmpeg** (giống hệt `higgs_make_refs.py:73-76` — đã dùng & kiểm chứng cho bộ mẫu MiniMax):

```
apad=pad_dur=0.25,aresample=24000:resampler=soxr,loudnorm=I=-18:TP=-1.5:LRA=11,silenceremove=start_periods=1:start_threshold=-50dB
→ -ac 1 -ar 24000 -c:a pcm_s16le
```

**Đầu ra:**
| Đường dẫn | Nội dung |
|---|---|
| `assets/voice_ref_voxcpm2/<vai>.wav` | WAV mono 24 kHz, −18 LUFS (nằm trong dải −20…−16 của `QUY_TAC` §4) |
| `assets/voice_ref_voxcpm2/<vai>.txt` | **ref_text chép đúng từng chữ** |
| `assets/voice_ref_voxcpm2/refs.json` | vai · control_instruction · target_text · file nguồn · F0 đo · số giây · license |

> **KHÔNG ghi đè `assets/voice_ref_higgs/`** (bộ mẫu MiniMax). Thư mục mới song song để so sánh A/B. Chỉ thay khi bộ VoxCPM2 thắng.
> `QUY_TAC_AUDIO_HIGGS.md` §4 ghi chuẩn thư mục là `assets/voice_ref/` — hiện **chưa tồn tại**. Xem mục 8.

**`provenance.json`** — mỗi file mẫu ghi:
```json
{ "tool": "VoxCPM2 (OpenBMB, Voice Design)",
  "license": "Apache-2.0",
  "attribution_required": false,
  "commercial_checked": true,
  "model": "openbmb/VoxCPM2",
  "note": "Giọng tổng hợp từ mô tả văn bản; không clone giọng người thật." }
```

---

## 7. Nghiệm thu (theo cổng H0–H5 của `QUY_TAC_AUDIO_HIGGS.md` §9)

> **Ngưỡng số và cách đo chính thức: `QUY_TAC_GIONG_MAU_VOXCPM2.md` §3–§6** (cổng V1–V8, script `.work/voxcpm_do_mau.py`). Bảng dưới là tóm tắt; mâu thuẫn thì theo file quy tắc.

| # | Việc | Đạt khi |
|---|---|---|
| 1 | **Nghe 7 file mẫu** | đúng chữ, đủ 6 thanh, cảm xúc trung tính, 8–15 s, không tiếng ồn |
| 2 | **Đo F0** | mỗi vai trong dải mục 3 |
| 3 | **Đo CER mẫu** (qua `listen_audio`) | **< 2%** mỗi vai — ngưỡng của kênh (G12) |
| 4 | **Higgs đọc thử 1 câu/vai bằng file mẫu** | nghe ra đúng giọng vừa thiết kế |
| 5 | **G8** — 1 câu × 4 cảm xúc an toàn | nghe mù ra **1 người** |
| 6 | **G9** — xen kẽ H · D · C | gán đúng **100%**, F0 ≥ 4 nc |
| 7 | **G9 phụ** — xen kẽ H ↔ W4, D ↔ W4 | không lẫn (tách bằng chất âm) |
| 8 | **So A/B với bộ mẫu MiniMax** | cùng 20 câu/vai, cùng cảm xúc production → bộ nào thắng |
| 9 | **Khai `CAST_HIGGS` trong `edition.py`** | bộ mới, **không** đè `CAST` (L8, L9) |

Script dùng được: `.work/voice_audition.py` (`f0_median`, `cer`) · `.work/_g8_g9_kiem_tra_giong.py` · `.work/_do_cer_bo_a_tap02.py` · `.work/higgs_tts_mac.py` (đọc Higgs với `ref_audio` + `ref_text` theo vai).

---

## 8. Việc còn mở

| # | Việc | Mức |
|---|---|---|
| 1 | **`assets/voice_ref/` chưa tồn tại** — `QUY_TAC` §4 quy định chuẩn ở đó, nhưng bản thực tế nằm ở `assets/voice_ref_higgs/`. Cần chốt 1 đường dẫn chuẩn rồi sửa `QUY_TAC` | Nên làm |
| 1b | **Bảng ghép N1/N2 → W1–W4 đã chốt** (§3.1, 29/10/2026). Còn: T01 chưa ghi giới · đồng bộ bản EN/KO/JA · nghe thử T16/T18 N2 ở V8 | Chờ người dùng |
| 2 | **Chưa khai `CAST_HIGGS`** trong `edition.py` — `QUY_TAC` §4 yêu cầu bộ mới | Nên làm |
| 3 | **Dòng ghi công Boson** vẫn bắt buộc trong mô tả YouTube mọi tập dùng Higgs (`This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio`) — điều khoản của Higgs, không liên quan VoxCPM2 | Bắt buộc khi đăng |
| 4 | **Đã sinh & nghiệm thu (29/10/2026)** — 7/7 vai đạt chuẩn V1–V6 tại `assets/voice_ref_voxcpm2/`, báo cáo lưu ở `90_LUU_TRU/BaoCao_DoGiongMau_VoxCPM2_20261029.md` | ✅ ĐÃ ĐẠT |
| 5 | **Higgs clone từ giọng tổng hợp** = giọng của một giọng. Phải đo lại G8/G9 trên audio Higgs sinh ra, không được mượn số đo của bộ A | Bắt buộc ở bước 5–7 |
| 6 | Bản EN / JA / KO chưa làm — khi làm phải có **file tham chiếu riêng cho từng ngôn ngữ** (Higgs clone theo vai, mà cùng một vai ở bản EN là giọng khác) | Để sau |

---

## 9. Nguồn (truy cập 28/10/2026)

- Trang demo + mô tả 3 chế độ: https://voxcpm2.org/
- Space chính thức: https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo
- Mã nguồn Space (đã đọc `app.py` để xác nhận cơ chế trường): https://huggingface.co/spaces/OpenBMB/VoxCPM-Demo/raw/main/app.py
- README + danh sách 30 ngôn ngữ + benchmark: https://github.com/OpenBMB/VoxCPM
- Model card: https://huggingface.co/openbmb/VoxCPM2
- Hướng dẫn dùng (Voice Design, Ultimate Cloning): https://voxcpm.readthedocs.io/en/latest/usage_guide.html
- Giấy phép Apache-2.0: https://github.com/OpenBMB/VoxCPM/blob/main/LICENSE
- Báo cáo VoxCPM2: https://arxiv.org/abs/2606.06928
