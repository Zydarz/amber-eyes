# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 02 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Đại tá Russell Williams — Hai mặt quân hàm & Vực thẳm leo thang  
> **Thời điểm thẩm định:** 05/11/2026  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap02/kichban_tap02_22102026.md`](kichban_tap02_22102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap02_EN/kichban_tap02_EN.md`](../Tap02_EN/kichban_tap02_EN.md)  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md`](../Tap02_JA/kichban_tap02_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap02_KO/kichban_tap02_KO.md`](../Tap02_KO/kichban_tap02_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và các công cụ kiểm tra tự động độc lập:

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **63** | **63** | **63** | **63** | **Khớp 100% (63/63)** |
| **Lượt lời thoại (LOI)** | **36** | **36** | **36** | **36** | **Khớp 100% (36/36)** |
| **Tổng số câu đọc (Sentences)** | **203** | **203** | **203** | **203** | **Khớp 1:1 tuyệt đối** |
| **Số điểm ngắt nghỉ (NGHI)** | 11 | 11 | 11 | 11 | **Khớp 100% (cùng giây)** |
| **Số cue âm thanh (BGM / SFX)** | 16 (6 BGM / 10 SFX) | 16 | 16 | 16 | **Khớp 100% vị trí & thứ tự** |
| **Số mục danh sách (Bullets)** | 6 | 6 | 6 | 6 | **Khớp 100% (vị trí `2.05` & `3.08`)** |
| **Số câu trích dẫn (Quotes)** | 17 | 17 | 17 | 17 (`‘...’`) | **Khớp 100% (17/17)** |
| **Dung lượng văn bản** | 4.872 từ / 21.779 ký tự | 3.533 từ / 22.512 ký tự | 10.749 ký tự | 2.926 từ / 12.975 ký tự | Chuẩn tỷ lệ đa ngôn ngữ |
| **Ước tính thời lượng lời** | ~25,7 phút | ~25,2 phút | ~26,0 phút | ~25,5 phút | Chuẩn tập 25–28 phút |

### Phân bổ số câu theo từng Hồi:
- **Hồi 1 (The Hook & Sự tương phản cực đại):** VN = 39 | EN = 39 | JA = 39 | KO = 39
- **Hồi 2 (Hiện trường & Quỹ đạo leo thang):** VN = 38 | EN = 38 | JA = 38 | KO = 38
- **Hồi 3 (Phân tích chuyên sâu & Cơ chế tự bào chữa):** VN = 37 | EN = 37 | JA = 37 | KO = 37
- **Hồi 4 (Đấu trí thẩm vấn & Sụp đổ bức tường tâm lý):** VN = 46 | EN = 46 | JA = 46 | KO = 46
- **Hồi 5 (Phán quyết, Bản án tâm lý & Cảnh báo đỏ):** VN = 43 | EN = 43 | JA = 43 | KO = 43

### Phân bổ tỷ lệ thoại giữa 4 vai diễn:
- **Host (Cú) — Trầm ấm, bao quát:** 23 lượt thoại, 97 câu (**47,8%**) — *Đạt chuẩn thiết kế (~45–50%)*.
- **Điều tra viên (Sói) — Sắc lạnh, nghiệp vụ:** 6 lượt thoại, 53 câu (**26,1%**) — *Đạt chuẩn thiết kế (~25%)*.
- **Chuyên gia tâm lý (Cáo) — Học thuật, sâu sắc:** 5 lượt thoại, 45 câu (**22,2%**) — *Đạt chuẩn thiết kế (~25%)*.
- **Người bình thường (Cừu/Mèo) — Cảm xúc, chân thật:** 2 lượt thoại, 8 câu (**3,9%**) — *Đạt chuẩn thiết kế (~5%)*.

---

## 2. Thẩm định chi tiết Hệ sinh thái 10 Chỉ Dấu Tâm Lý & Hành Vi (A2c)

Toàn bộ 10 chỉ dấu đã được rà soát đối chiếu chéo trong cả 4 ngôn ngữ, đảm bảo truyền tải trọn vẹn góc nhìn khoa học hành vi, không biến video thành bản tin phóng sự thuần túy:

### 1. Ảnh hưởng & Sự quan tâm của xã hội (Social Impact & Public Fascination)
- **Vị trí:** `1.03`, `1.05`, `1.10`, `5.04`, `5.07`
- **Nội dung:** 
  - Vị thế biểu tượng của Căn cứ Không quân Trenton — nơi tiếp nhận linh cữu tử sĩ Canada từ chiến trường Afghanistan trở về dọc theo *“Con lộ Anh hùng” (Highway of Heroes)* do chính Williams điều hành nghi lễ thiêng liêng.
  - Cơn hoang tưởng tập thể *(Collective Paranoia)*: phụ nữ tại Tweed và Belleville chèn ghế chặn cửa phòng ngủ, cư dân nghi kỵ lẫn nhau trong đêm đông.
  - Cuộc đại cải tổ quy trình an ninh và đánh giá tâm lý trong Quân đội Canada sau chấn động.
- **Đối chiếu ngôn ngữ:**
  - **EN:** `"Highway of Heroes"`, `"collective paranoia gripped the local communities"`, `"shattered trust in Canada's most prestigious institutions"`.
  - **JA:** `「英雄の高速道路」`, `「地域社会には集団的偏執病が広がりました」`, `「カナダ軍は上級将校に対する保安審査と心理評価システムを全面的に刷新せざるを得なくなりました」`.
  - **KO:** `‘영웅의 고속도로’`, `‘집단적 편집증이 지역 사회를 엄습했습니다’`, `‘가장 존경받던 국가 기관에 대한 신뢰가 근본부터 흔들렸고’`.

### 2. Cách hung thủ nhìn nhận nạn nhân & Vì sao (Victim Perception & Objectification)
- **Vị trí:** `2.07`, `3.05`, `3.11`
- **Nội dung:** 
  - Hung thủ hạ thấp nạn nhân thành *"đạo cụ sống"* *(Living Props)*, biến họ thành công cụ thỏa mãn bản năng thống trị *(Objectification)*.
  - Nguyên nhân: Sự kết hợp giữa Ái kỷ ác tính *(Malignant Narcissism)* và Rối loạn nhân cách chống đối xã hội *(ASPD)* triệt tiêu hoàn toàn sự đồng cảm *(Empathy Deficit)* và khiếm khuyết Thuyết tâm trí *(Theory of Mind)*.
- **Đối chiếu ngôn ngữ:**
  - **EN:** `"degraded into living props"`, `"psychological objectification"`, `"empathy deficit"`.
  - **JA:** `「客体化（Objectification）」`, `「支配本能を満たすための道具」`, `「生きている小道具」`.
  - **KO:** `‘객체화(Objectification)’`, `‘살아있는 소품’`, `‘타인의 고통에 대한 병적인 공감 결여’`.

### 3. Cách hung thủ nhìn nhận người thân & Phân mảnh tâm lý (Perception of Family & Compartmentalization)
- **Vị trí:** `3.08`, `3.11`, `4.10`, `4.11`
- **Nội dung:** 
  - Cơ chế *Chia ngăn tâm lý (Compartmentalization)*: Ngăn kéo 1 (Đại tá mẫu mực, người chồng chu đáo tại Ottawa) và Ngăn kéo 2 (Kẻ săn mồi bóng đêm tại Tweed).
  - Williams không coi gia đình là tình cảm thiêng liêng mà là *"Lá chắn bình thường hóa"* *(Shield of Normalization)* để duy trì chiếc mặt nạ công khai.
- **Đối chiếu ngôn ngữ:**
  - **EN:** `"Compartmentalization"`, `"Shield of Normalization"`, `"two mutually exclusive mental drawers"`.
  - **JA:** `「精神の分断（コンパートメンタライゼーション）」`, `「正常性の防壁」`, `「二つの独立した引き出し」`.
  - **KO:** `‘심리적 구획화(Compartmentalization)’`, `‘정상성의 방패’`, `‘완벽하게 분리된 마음의 서랍’`.

### 4. Thái độ tâm lý trước bản án (Attitude towards Verdict: Narcissistic Collapse)
- **Vị trí:** `4.11`, `5.02`, `5.06`
- **Nội dung:** 
  - Lời xin lỗi khô khốc, máy móc trước tòa; tuyệt thực và mưu toan tự sát trong phòng giam Kingston Penitentiary.
  - Bản chất là *Sự sụp đổ cái tôi ái kỷ (Narcissistic Collapse)* và *Thương hại bản thân bệnh hoạn (Pathological Self-Pity)* khi mất toàn bộ quyền lực và danh dự, hoàn toàn không phải sự ăn năn chân chính *(genuine remorse)*.
- **Đối chiếu ngôn ngữ:**
  - **EN:** `"Narcissistic Collapse"`, `"Pathological Self-Pity"`, `"stripped of elite status"`.
  - **JA:** `「自己愛の完全崩壊（ナルシシスティック・コラプス）」`, `「病的な自己憐憫」`.
  - **KO:** `‘자기애적 붕괴(Narcissistic Collapse)’`, `‘극단적인 자기연민(Pathological Self-Pity)’`.

### 5. Hệ thống tự bào chữa & Trung hòa đạo đức (Self-Justification & Neutralization)
- **Vị trí:** `3.08`
- **Nội dung:** 
  - Ứng dụng lý thuyết *Kỹ thuật Trung hòa Đạo đức (Techniques of Neutralization — Sykes & Matza)*:
    - Khi đột nhập: *“mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm”* (Phủ nhận tổn hại).
    - Khi giết người: *“nạn nhân đã thấy mặt mình, cô ta ép mình phải ra tay để tự vệ”* (Đổ lỗi cho nạn nhân).
  - Câu trả lời gây sốc trong phòng thẩm vấn: *“Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng.”*
- **Đối chiếu ngôn ngữ:** Cả 4 ngôn ngữ bảo toàn nguyên vẹn ngữ nghĩa triết học và câu trích nguyên văn đối thoại.

### 6. Ngòi nổ & Điểm gãy tâm lý (Precipitating Trigger & Breaking Point)
- **Vị trí:** `1.03`, `3.05`
- **Nội dung:** Cột mốc tháng 7/2009 khi nhận quyền chỉ huy tối cao CFB Trenton. Cảm giác quyền lực toàn năng kết hợp áp lực điều hành khổng lồ đóng vai trò *Ngòi nổ tâm lý (Precipitating Trigger)* làm sụp đổ chốt chặn kiểm soát cuối cùng, dẫn đến vụ sát hại Marie-France Comeau chỉ sau 4 tháng.
- **Đối chiếu ngôn ngữ:** Thuật ngữ `Precipitating Trigger` được giữ nguyên trong văn cảnh học thuật của cả EN, JA, KO.

### 7. Dấu ấn Signature vs. Thủ đoạn Modus Operandi (Signature vs. MO)
- **Vị trí:** `2.08`
- **Nội dung:** Phân định rõ giữa MO (kỹ thuật hoàn thành tội ác và tẩu thoát: đi tất, găng tay, cắt dây điện thoại, gây án đêm bão tuyết — liên tục thay đổi qua 82 vụ) và Signature (nhu cầu tâm lý bất biến: lưu giữ chiến lợi phẩm Trophies, tự sướng trước gương, ghi nhật ký tỉ mỉ trong ổ cứng bí mật).
- **Điểm sáng nghiệp vụ:** MO giúp hung thủ lẩn trốn, nhưng Signature (ổ cứng) lại chính là bằng chứng duy nhất vạch trần bộ mặt thật.

### 8. Ảo tưởng & Quỹ đạo leo thang 4 nấc thang (Fantasy Escalation Trajectory)
- **Vị trí:** `2.05`, `3.05`
- **Nội dung:** Cơ chế nghiện dopamine và lờn kích thích dẫn tới 4 nấc thang: (1) Nhìn trộm ban đêm $\rightarrow$ (2) Đột nhập trộm đồ lót $\rightarrow$ (3) Đột nhập khống chế nạn nhân $\rightarrow$ (4) Tước đoạt mạng sống.
- **Đối chiếu ngôn ngữ:** Phân chia danh sách `* **Nấc thang thứ X**` chuẩn xác 100% qua 4 thứ tiếng.

### 9. Hiệu ứng Hào quang & Điểm mù hệ thống (Halo Effect & Systemic Blind Spots)
- **Vị trí:** `1.05`, `1.08`, `1.14`, `5.07`
- **Nội dung:** Chiếc mặt nạ danh gia vọng tộc (phi công của Nữ hoàng Elizabeth II, Thủ tướng) tạo nên *Hiệu ứng Hào quang (Halo Effect)* khiến cấp dưới tuyệt đối sùng kính và tổ tuần tra ban đầu e dè khi chặn chiếc Nissan Pathfinder đêm 4/2/2010.

### 10. Nạn nhân học & Cảnh báo đỏ sinh tồn (Victimology & Red Flags)
- **Vị trí:** `2.07`, `5.07`, `5.08`
- **Nội dung:** 
  - Bất đối xứng quyền lực giữa kẻ săn mồi với cấp dưới (Marie-France Comeau) và cô gái trẻ độc thân (Jessica Lloyd).
  - Cảnh báo đỏ sinh tồn: Tội ác không bắt đầu từ nhát dao mà từ những vụ lấn ranh giới nhỏ (đồ đạc bị xới xáo, cửa có dấu cạy); bài học sống còn: *“Hãy luôn tin vào trực giác của chính mình”*.

---

## 3. Đối chiếu 17 Câu trích dẫn nguyên văn & Dữ kiện Lịch sử (Luật K1, K2, K3)

| # | Vị trí | Bản gốc Tiếng Việt | English (EN) | 日本語 (JA) | 한국어 (KO) |
|---|---|---|---|---|---|
| **1** | `1.05#3` | ‘Con lộ Anh hùng’ | "Highway of Heroes" | 「英雄の高速道路」 | ‘영웅의 고속도로’ |
| **2** | `1.08#4` | ‘Hiệu ứng Hào quang’ | "Halo Effect" | 「ハロー効果」 | ‘후광 효과’ |
| **3** | `3.05#8` | ‘đói ảo tưởng’ | "fantasy starvation" | 「妄想の飢餓」 | ‘망상의 굶주림’ |
| **4** | `3.08#7` | ‘Lá chắn bình thường hóa’ | "Shield of Normalization" | 「正常性の防壁」 | ‘정상성의 방패’ |
| **5** | `3.08#8` | ‘mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm’ | "I only look, I don't hurt anyone, I'm just keeping a keepsake" | 「見ているだけで誰も傷つけていない、記念品を保管しているだけだ」 | ‘나는 단지 바라보기만 할 뿐 아무도 해치지 않는다, 기념품을 보관할 뿐이다’ |
| **6** | `3.08#9` | ‘nạn nhân đã thấy mặt mình, cô ta ép mình phải ra tay để tự vệ’ | "the victim saw my face, she forced my hand to protect myself" | 「被害者が自分の顔を見た、身を守るためにやむを得なかった」 | ‘피해자가 내 얼굴을 보았으니, 나를 지키기 위해 어쩔 수 없었다’ |
| **7** | `3.08#11`| ‘Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng.’ | "Yes, but I don't know the answer, and I'm pretty sure the answer doesn't really matter." | 「ええ、ですが答えは分かりませんし、答えが重要だとも思えません」 | ‘예, 하지만 답은 모르겠고, 답이 중요하다고 생각하지도 않습니다.’ |
| **8** | `3.11#6` | ‘đạo cụ sống’ | "living props" | 「生きている小道具」 | ‘살아있는 소품’ |
| **9** | `4.08#6` | ‘Chúng giống hệt nhau.’ | "They are identical." | 「完全に一致しています」 | ‘완전히 일치합니다.’ |
| **10**| `4.08#7` | ‘Cứ gọi tôi là Russ.’ | "Call me Russ, please." | 「Russと呼んでくれ」 | ‘그냥 Russ라고 불러주십시오.’ |
| **11**| `4.10#2` | ‘Các điều tra viên đang ở nhà ông.’ | "Investigators are at your home right now." | 「捜査員が今、あなたの自宅に入っています」 | ‘수사관들이 지금 당신 집에 가 있습니다.’ |
| **12**| `4.10#3` | ‘Vợ ông giờ đã biết chuyện gì đang xảy ra.’ | "Your wife now knows what is happening." | 「あなたの奥様も今、何が起きているかを知りました」 | ‘부인께서도 지금 무슨 일이 벌어지고 있는지 알게 되었습니다.’ |
| **13**| `4.10#6` | ‘Tôi không biết phải nói gì.’ | "I don't know what to say." | 「何と言えばいいのか分かりません」 | ‘무슨 말을 해야 할지 모르겠습니다.’ |
| **14**| `4.10#7` | ‘Vậy, cô ấy ở đâu?’ | "So, where is she?" | 「では、彼女はどこにいるのですか？」 | ‘그래서, 그녀는 어디에 있습니까?’ |
| **15**| `4.10#8` | ‘Có bản đồ không?’ | "Is there a map?" | 「地図はありますか？」 | ‘혹시 지도가 있습니까?’ |
| **16**| `4.11#4` | ‘Tôi muốn giảm thiểu ảnh hưởng lên vợ tôi.’ | "I want to minimize the impact on my wife." | 「妻への影響を最小限に抑えたい」 | ‘제 아내에게 미칠 영향을 최소화하고 싶습니다.’ |
| **17**| `5.04#8` | ‘Khi đặt dấu chấm cuối câu, dấu chấm ấy nhỏ thôi, nhưng nó mang rất nhiều ý nghĩa.’ | "Like the period at the end of a sentence, it's very small, but it means a great deal." | 「文末に打たれるピリオドのように、その点は極めて小さいが、極めて重大な意味を持つのだ」 | ‘문장의 끝에 찍히는 마침표처럼, 그 점은 매우 작지만 대단히 중대한 의미를 지닌다.’ |

---

## 4. Kiểm tra An toàn YouTube (V9) & Pháp lý (Luật K4, K5)

1. **Tuân thủ Tiêu chuẩn YouTube Safe (V9 / A9.2):**
   - **0 từ cấm bạo lực máu me:** Không sử dụng các từ ngữ mô tả chi tiết thương tích giải phẫu, khám nghiệm tử thi rùng rợn, hoặc công cụ gây thương tích trực diện.
   - Các từ nhạy cảm như "thi thể" trong ngữ cảnh tử sĩ đã được thay bằng "linh cữu tử sĩ / caskets / 遺骨 / 유해".
   - Không xuất hiện bất kỳ chi tiết xâm hại tình dục liên quan trẻ vị thành niên.
   - Các cụm từ liên quan đồ vật trong vụ án được diễn đạt trang nhã, đúng bản chất vụ án: "đồ riêng tư / intimate apparel / 私的な衣服 / 사적 의류".

2. **Bọc lót pháp lý (Luật K5):**
   - Tuyệt đối không khẳng định chẩn đoán tâm thần lâm sàng cá nhân đối với người thật ngoài đời.
   - Toàn bộ phân tích tâm lý được dẫn dắt bằng ngôn ngữ nhận định khoa học:
     - VN: *"Williams hoàn toàn tỉnh táo và mang những đặc điểm thường thấy trong Ái kỷ ác tính..."*
     - EN: *"Under public court records and behavioral analysis frameworks, Williams presented classic traits of Malignant Narcissism..."*
     - JA: *"精神医学的見地および公的裁判記録の分析において、Williamsは悪性自己愛の典型的な特徴を示していました..."*
     - KO: *"공개된 재판 기록과 행동과학적 분석의 틀에서 볼 때, Williams는 악성 자기애의 전형적인 특성을 명확히 드러냈습니다..."*

---

## 5. Kết quả chạy kiểm định mã tự động (Pipeline QC Logs)

### 1. English Parity QC (`verify_en_script.py 02`):
```text
[EXEC] python .work/verify_en_script.py 02
✅ Episode 02 PASSED: 63 elements, 203 sentences perfectly matched!
```

### 2. Japanese Quality & Structure QC (`_qc_ja.py 02`):
```text
[EXEC] python .work/_qc_ja.py 02
OK   Tap02: câu VN=203 JA=203 | lượt VN=36 JA=36 | lượt lệch câu=0 | lỗi: không
==> 1/1 tập đạt · -> D:\TEST\Gax\amber-eyes\.work\_ja_qc.txt
```

### 3. Korean Parity & Character QC (`_qc_ko_parity.py`):
```text
[EXEC] python .work/_qc_ko_parity.py 01_KICH_BAN/Tap02/kichban_tap02_22102026.md 01_KICH_BAN/Tap02_KO/kichban_tap02_KO.md
ok    acts: 5 (1,2,3,4,5)
ok    63 elements aligned (kind/role/sentence-count/pause)
ok    total sentences: 203
ok    hangul share of narration: 86.0%
ok    no vietnamese-only diacritics in KO narration
ok    no hanja/chinese characters in KO narration
ok    list items: 6 (same order, same kind)
ok    quotes: 17 (type-1 = keep English inside, type-2 = translate inside)
PASS  kichban_tap02_KO.md — 63 elements, 203 sentences, parity with kichban_tap02_22102026.md
```

---

## 6. Kết luận & Đề xuất

- Cả 4 phiên bản kịch bản **VN — EN — JA — KO** đã đạt trạng thái hoàn thiện cao nhất, đồng bộ cấu trúc 1:1 tuyệt đối từ cấp Hồi, Element đến từng câu thoại đơn lẻ.
- Kịch bản giải quyết triệt để 5 câu hỏi trọng tâm của người dùng và tích hợp đầy đủ **Hệ sinh thái 10 chỉ dấu tâm lý & hành vi** (A2c).
- Đã sẵn sàng 100% để người dùng phê duyệt thông qua Cổng Bước 1 trước khi tiến hành các bước sản xuất âm thanh và hình ảnh tiếp theo.
