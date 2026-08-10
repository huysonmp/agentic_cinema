# Đóng góp cho Agentic Cinema

## Quy trình

1. Mở issue mô tả vấn đề, người dùng bị ảnh hưởng và tiêu chí chấp nhận.
2. Nếu thay đổi kiến trúc, bảo mật, dữ liệu hoặc nhà cung cấp, thêm một ADR vào `docs/12-nhat-ky-quyet-dinh.md`.
3. Tạo branch ngắn, bổ sung test/eval tương ứng và không commit dữ liệu sản xuất hay secret.
4. Pull request phải nêu: thay đổi gì, cách kiểm tra, chi phí/rủi ro mới và kế hoạch rollback.

## Chuẩn chất lượng dự kiến

- Python được format/lint/type-check; logic miền có unit test.
- Mỗi tool có input/output schema, timeout, retry policy, idempotency và phân loại rủi ro.
- Mỗi thay đổi prompt/agent phải chạy regression eval.
- Media fixture chỉ dùng dữ liệu tổng hợp, public domain hoặc đã được cấp quyền.
- Log không chứa nội dung kịch bản, PII, token truy cập hay URL đã ký.

## Commit

Ưu tiên Conventional Commits, ví dụ `docs: add production safety guide`, `feat: add screenplay parser`, `test: add tool trajectory evals`.
