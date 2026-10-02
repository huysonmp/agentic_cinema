# Owner loại bộ giọng K2/K3/K4 — sai vùng giọng

Ngày 2026-10-02. Owner phản hồi nguyên văn: “sai hết rồi, đây là giọng nam miền nam mà, tôi cần giọng nam miền bắc”.

## Đã xác định và quyết định

- Cả chín mẫu ở 142/143: OWNER_REJECTED / ACCENT_FAIL. Không tiếp tục dùng bộ này làm ứng viên, tham chiếu giọng hoặc đầu vào production. Giữ file làm bằng chứng thử nghiệm, không xóa.
- Yêu cầu bắt buộc: giọng nam miền Bắc. Chất Khoai trầm ấm, kể thân mật, ký ức có nét cười kín vẫn giữ; không thay vùng giọng để cứu take.
- Đây là kết luận nghe của owner. Root chưa có đánh giá nghe độc lập, không giả là đã tự xác nhận ngữ âm.
- Technical decode PASS của 143 vẫn đúng trong phạm vi file; không phải voice PASS. Số dư gần nhất 650, ngân sách thử 400/400 đã hết. Không có generation, chi phí mới hoặc sử dụng ngân sách Quality trong lượt này.

## Lỗi quy trình đã thấy / nguyên nhân còn mở

Prompt thực đã có “natural Northern Vietnamese accent”, nhưng yêu cầu đó không được đáp ứng theo owner. Không thể kết luận do một từ, ảnh đầu vào, Lite hoặc model không thể nói giọng Bắc chỉ từ bộ này.

Lỗi thiết kế phép thử: chạy ba hướng diễn (tổng chín mẫu) trước khi khóa tiêu chí nền là đúng vùng giọng; cả ba dùng cùng chỉ dẫn vùng giọng chưa được kiểm chứng. Mở rộng sắc thái quá sớm làm tiêu ngân sách mà chưa có baseline đạt. File/âm thanh giải mã sạch không phát hiện được lỗi vùng giọng; cần cổng nghe riêng trước vòng phát triển diễn xuất.

## Nghiên cứu sơ bộ và bước đề xuất — chưa chạy

Đã đọc [Google Flow supported features](https://support.google.com/flow/answer/16352836?hl=en), ngày 2026-10-02: phần custom voices/preset được mô tả thuộc Gemini Omni, không được suy ra là nút khóa giọng của Veo Lite. Tài liệu không xác nhận preset nam miền Bắc hoặc mức bảo đảm accent cho tài khoản này. Không tự đổi model/công cụ hoặc kết nối API.

Đề xuất tách phép thử accent khỏi diễn: một hướng trung tính, một câu thoại ngắn, giữ các điều kiện khác, ba mẫu Lite rồi owner nghe; chỉ khi đúng Bắc mới thử độ trầm/ấm/nhịp và tính nhất quán. Có thể dùng mô tả nam trưởng thành nói tiếng Việt giọng Hà Nội tự nhiên làm giả định thử, nhưng Hà Nội chưa là lựa chọn đã chốt của owner và prompt mới chưa chứng minh hiệu quả. Không gắn các quy tắc ngữ âm giản lược để giả giọng.

Trước khi tạo thêm: cần ngân sách Lite mới do trần cũ hết. Phương án khác là kiểm tra tính năng chọn giọng trong Flow hoặc tạo voice riêng rồi kiểm ghép/môi; chỉ đề xuất, chưa đổi pipeline. Bước hiện hành: thông báo bộ cũ bị loại và trình thử accent nhỏ trước khi mở rộng. Không hứa chỉ sửa prompt là giải quyết được.
