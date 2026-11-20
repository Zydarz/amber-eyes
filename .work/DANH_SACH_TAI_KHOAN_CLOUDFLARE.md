# DANH SÁCH TÀI KHOẢN CLOUDFLARE WORKERS AI (POOL)
> File lưu trữ cấu hình nội bộ danh sách 6 tài khoản Cloudflare Workers AI phục vụ sinh ảnh nền FLUX.1 schnell (`@cf/black-forest-labs/flux-1-schnell`) cho kênh Amber Eyes.
> Cập nhật ngày: 20/11/2026.

| STT | Tên tài khoản | Account ID | Trạng thái API Token | Ghi chú hạn mức |
|---|---|---|:---:|---|
| 1 | `ACCOUNT_1` | `a550014febb0c9d8c313c1f930fee064` | `Active` | Đang trong pool quay vòng tự động |
| 2 | `ACCOUNT_2` | `d6147ae5f06ea4802abdfca4bb677059` | `Active` | Đang trong pool quay vòng tự động |
| 3 | `ACCOUNT_3` | `e12fcbf87fea393852201f531ee59633` | `Active` | Đang trong pool quay vòng tự động |
| 4 | `ACCOUNT_4` | `60baab69689cbd29f96b5cc88f28b5ab` | `Active` | Đang trong pool quay vòng tự động |
| 5 | `ACCOUNT_5` | `deeb32f84326e44bd003ba2aa7eb0950` | `Active` | Bổ sung sáng 20/11/2026 (đã sinh 85 ảnh Tập 23) |
| 6 | `ACCOUNT_6` | `f8e80ee8bf02a653c33a83014320c9c2` | `Active` | Bổ sung trưa 20/11/2026 (đã sinh 27 ảnh cuối Tập 23) |

---

### File cấu hình kỹ thuật thực thi:
- Đường dẫn file cục bộ: `.work/.cloudflare_accounts`
- Cơ chế failover: Tự động chuyển tài khoản tiếp theo khi gặp mã lỗi `HTTP 429` (Quota 10,000 neurons hàng ngày hết).
- Script client gọi API: `.work/flux_client.py`
