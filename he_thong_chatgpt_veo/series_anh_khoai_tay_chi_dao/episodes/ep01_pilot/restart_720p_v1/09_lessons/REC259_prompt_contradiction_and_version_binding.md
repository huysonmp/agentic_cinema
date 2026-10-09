# REC259 — Nụ cười khép môi và kiểm phiên bản trước khi chạy

## Quan sát

DOP/ACT phát hiện prompt C03B ban đầu vừa yêu cầu Đào mỉm cười, vừa cấm tuyệt đối chuyển động môi. Hai điều này không mô tả rõ cùng một biểu cảm. Đây là lỗi đặc tả đầu vào phát hiện trước khi tạo, không phải nguyên nhân đã chứng minh của một output lỗi.

## Xử lý

- Giữ nguyên N04 của Khoai, preset K20, tư thế bốn tay nghỉ và trình tự Đào phản ứng sau lời.
- Cho phép nụ cười khép môi; cấm mở miệng hoặc chuyển động môi giống đang nói. Quay đầu nhẹ về cốc nhưng mặt và mắt còn đọc được.
- Rehash prompt thành `9add23d02c3d0bfe68af9f943b6f3fa9a2e8f9c5f195622c8a5f1f13fb953ed5`, cập nhật request và đọc lại toàn bộ báo cáo phản biện theo hash mới. Báo cáo phiên bản cũ không đóng gate cho prompt mới.
- Chỉ gửi một lượt sau khi đối soát ảnh F41, K20 đúng ID, hai thành phần, readback, 720p/4 giây/x1, tiếng bật và giá 7 credit. Kết quả thực vẫn phải kiểm riêng.

## Quy tắc tái sử dụng

1. Phân biệt chuyển động biểu cảm và chuyển động khẩu hình nói; không cấm toàn bộ một chuyển động rồi lại yêu cầu nó ở câu khác.
2. Approval nguồn/giọng không đảm bảo output mới hoặc điểm nối mới đạt. Đối soát native → range được chọn → bản nối thực.
3. Ảnh trích từ bản cắt đã mã hóa lại có thể khác byte với PNG trích trực tiếp từ native. Ghi đúng file nguồn, hash và số khung; không tuyên bố pixel-identical nếu chưa đo.
4. ASR và ảnh rời là bằng chứng hỗ trợ, không phải xác nhận đã nghe giọng hoặc đã xem AV liên tục.

## Quan sát output đầu tiên

Native259 giữ môi Đào khép và bốn tay nghỉ, nhưng thay cue nhìn cốc bằng quay mặt ra trước. Cả root và reviewer xác nhận trên 96 khung. Không quy lỗi chắc chắn cho câu prompt vừa sửa: model không thực hiện đầy đủ chuỗi diễn xuất là quan sát, nguyên nhân nội bộ chưa biết.

Bản cắt có thể giữ lời đáp và đầu nụ cười nhưng **không tạo ra hướng nhìn cốc bị thiếu**. Chuyển cue này sang đầu C04 là đề xuất thay ranh giới cảnh cần owner chốt; quan hệ nhân quả “Đào quay trước → Khoai mới gắp” vẫn bắt buộc. Không lấy một đoạn thoại dùng được làm bằng chứng mọi nhiệm vụ shot đã hoàn thành.
