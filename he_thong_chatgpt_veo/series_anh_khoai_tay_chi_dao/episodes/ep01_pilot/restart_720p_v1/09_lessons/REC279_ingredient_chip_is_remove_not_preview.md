# REC279 — Chip thành phần có thể gỡ ảnh, không phải nút preview

Ngày 13-10-2026. Khi chuẩn bị C07 T03, click chip ảnh cảnh gỡ attachment. Ảnh screenshot ngay sau click còn hiển thị ba chip, nhưng AX/DOM refresh xác nhận chỉ còn voice và pair. Đây là rủi ro của thao tác đọc/kiểm có tác dụng thay đổi đầu vào, không phải lỗi video hoặc lỗi model.

Đã khôi phục exact ảnh C06 F56 qua picker trước final, kiểm lại ba chip: một D06, pair ID `ded2a157-f2d7-4be7-9185-31d5fc87f3ea`, scene ID `9d2280e2-bb03-437a-98f2-553a7d481144`; giữ hash source và prompt. Chưa submit/chi credit, chưa output để kết luận chất lượng.

Quy tắc tiếp theo: không click chip composer để preview; lấy provenance lúc chọn/upload, đọc DOM loại/count/image IDs từ UI và screenshot mới. Không đọc hidden app state hoặc dùng screenshot cũ thắng DOM mới. Nếu số/loại/ID thiếu thì dừng, khôi phục rồi kiểm lại **toàn gói**, không chỉ gắn thêm và bấm tạo ngay. Voice phải chọn tên/performance/ID đúng trước Add; không dùng logo âm thanh làm bằng chứng D06.

Bằng chứng đầy đủ cuối cùng: `279_C07_T03_PREFLIGHT/C07_T03_FULL_INPUTS_CONFIG_QUOTE10.png`, preparation279 và prompt exact readback. Screenshot trung gian lưu riêng, không làm proof final. Quy tắc này bổ sung gate input toàn dự án, không mở quyền trả phí hoặc đổi căn nguyên hai C07 nguồn lỗi trước.
