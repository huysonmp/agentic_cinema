# REC224 — Nhật ký tạo bốn ảnh tham chiếu

Ngày: 2026-10-07. Owner duyệt bằng “ok”; xem `owner-approval.json`.

Flow project: `9276788e-9781-44fb-ba5b-083006667374`. Model hiển thị: Nano Banana 2.1. Chỉ ảnh dọc 9:16, x1, Tác nhân tắt. Nguồn chung: frame-0175.jpg của N02 B; không trộn nguồn cũ. Số dư trước chạy: 77 credit.

| ID | Lượt | Giá trước gửi | Trạng thái |
|---|---:|---:|---|
| REF01-S | 1 | 0 credit | Đã tải native 1K, chờ kết quả QC |
| REF01-M | 1 | 0 credit | Đã tải native 1K, chờ kết quả QC |
| REF01-E | 1 | 0 credit | Đã tải native 1K, chờ kết quả QC |
| REF03-S | 1 | 0 credit | Đã tải native 1K, chờ kết quả QC |

Bằng chứng trước/sau gửi lưu theo ID trong thư mục này. Các prompt dùng nguyên văn từ evidence/223. Không retry, không tạo video/voice. Kết quả chưa được duyệt làm đầu vào sản xuất.

## Đối soát thực thi

- Đã tạo đúng 4 lượt, x1/lượt. Model mới hiển thị Nano Banana 2.1; không tự suy ra chất lượng từ thông báo nhà cung cấp.
- Tải bằng nút Flow → 1K kích thước gốc; không chọn tăng độ phân giải. Bốn file JPG thực tế là 768 × 1376, gần tỷ lệ 9:16 đã chọn, không phải chính xác 1080 × 1920.
- `waitForEvent('download')` hết thời gian ở cả bốn lượt, nhưng các file đã xuất hiện trong Downloads. Đã kiểm decode, hash và ba bản sao (download gốc / owner / repo) bằng nhau. Không tạo lại media vì lỗi tín hiệu download.
- Tên ảnh: thao tác setValue + Tab chưa lưu tên vào danh sách; đã thay bằng fill + Enter và đọc lại lưới có đủ bốn ID. Không đổi nội dung ảnh.
- Script đối soát lần đầu không chạy do venv thiếu Pillow. Dùng Python runtime có sẵn của Codex; không cài mới. Chạy thành công: 4 native decode được, các bản sao bằng nhau, đúng prompt trong bằng chứng trước gửi và nhật ký kết quả.
- Số dư UI trước/sau: 77 → 77. Đây là số dư quan sát và quote trước gửi, không phải hóa đơn thanh toán.
- Nguồn frame-0175 giữ nguyên SHA256. Manifest đầy đủ: `native-output-manifest.json`.
- REC224-EDIT-POSE-QC và REC224-CONT-IMAGES đã hoàn tất; root đọc đầy đủ hai report. Chỉ nhận scope ảnh tĩnh, không nhận đã nghe/xem AV hay kiểm chuyển động. Giữ S làm ứng viên, M cần làm rõ/sửa đích tay, E và REF03-S cần sửa môi. Không mở generation mới.
- Ba draft sửa và request có exact input/output/prompt hash đã được tạo local; CONT đã phản biện chúng. Request vẫn PROPOSED_NOT_APPROVED_NOT_SUBMITTED. Hash prompt và input trong đề nghị đã được kiểm khớp; không gọi tính rõ ràng của prompt là model đã làm được.
- Compile script và git diff --check đều exit 0. Chưa commit/push; không bao gồm các thay đổi recovery cũ trong một commit không kiểm.
