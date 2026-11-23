# CHỮ CỐ ĐỊNH · BẢN TIẾNG NHẬT (Tập 01 + kênh)

*Tài liệu chuẩn chữ cố định cho Tập 01 bản tiếng Nhật (Japanese Edition).*
*Cập nhật: 24/10/2026.*

---

## 1. Thương hiệu

| Mục | Tiếng Việt | Tiếng Nhật | Chỗ trong code |
|---|---|---|---|
| Tên kênh | Amber eyes | **Amber eyes** (giữ nguyên) | `edition.py` |
| Khẩu hiệu ⚠ | Phân tích tâm lý tội phạm qua những hồ sơ có thật | **実際の事件記録から読み解く犯罪心理学** | `edition.py:TAGLINE` |

## 2. Intro kênh (`make_intro.py` → xuất `assets/brand/intro_kenh_JA_t01.mov`) ⚠

Giữ nguyên nhạc `bgm_music_box` (22,41 s), thời điểm, bố cục. Chữ **đậm** = phần tô màu hổ phách.

**Thẻ A — tiêu đề: `この動画について`** (ABOUT THIS VIDEO)

| # | Tiếng Nhật | Ý nghĩa |
|---|---|---|
| 1 | 本動画は**教育目的**の犯罪心理学分析コンテンツです。 | Nội dung giáo dục, phân tích tâm lý học tội phạm. |
| 2 | **公開記録**に基づいており、出典は概要欄に記載されています。 | Dựa trên tư liệu công khai, nguồn ở phần mô tả. |
| 3 | 特定の個人を非難または中傷する意図はありません。 | Không nhằm kết tội hay bôi nhọ bất kỳ ai. |

**Thẻ B — tiêu đề: `ご視聴前の注意`** (BEFORE YOU WATCH)

| # | Tiếng Nhật | Ý nghĩa |
|---|---|---|
| 1 | **お子様向けではありません**。 | Nội dung không phù hợp cho trẻ em. |
| 2 | 音声および画像は**イメージ**です。 | Âm thanh và hình ảnh chỉ mang tính minh hoạ. |
| 3 | 医学的、心理学的、または法的なアドバイスに代わるものではありません。 | Không thay thế tư vấn y khoa, tâm lý hay pháp lý. |

## 3. Nhãn nhân vật

**Badge góc trên trái** (`build_video3.py:ROLE_NAME`):

| Vai | Tiếng Nhật — Dòng 1 | Tiếng Nhật — Dòng 2 | Ghi chú |
|---|---|---|---|
| H · Cú | **ホスト** | ストーリーテラー | Host |
| D · Sói | **捜査官** | 事件記録 Blanchard | Investigator |
| C · Cáo | **心理学者** | 犯罪心理学 | Psychologist |
| N1 · Cừu | **スプリングフィールド住民** | 長年の隣人 | Springfield Resident |
| N2 · Mèo | **視聴者** | 事件を見守る人 | Viewer |

**Nhãn vai trong phụ đề** (`subtitles.py:SUB_TAG`):
- `捜査官` · `心理学者` · `証人` · `視聴者` (Host không gắn nhãn).

## 4. Chữ giao diện trong renderer (`build_video3.py`)

| Thành phần | Tiếng Nhật | Ghi chú |
|---|---|---|
| Host mời (`→X`) | **次へ** | NEXT |
| Thẻ giới thiệu `✦` | **架空のキャラクター · AI音声 · 演出** | Fictional character · AI voice · Dramatized |
| Nhãn minh hoạ | **イメージ** | ILLUSTRATION |
| Dấu mộc mật | **機密** | CONFIDENTIAL |
| Dấu mộc giả mạo | **偽造** | FORGED |

## 5. Thẻ kết (Shot 5-21) — theo chuẩn H12

- Nhãn hồ sơ: `事件記録 第01話 · 完結`
- Tên kênh: **AMBER EYES**
- Khẩu hiệu: *実際の事件記録から読み解く犯罪心理学*
