# Quy định: ba lượt Lite và nhật ký học từ công cụ

Ngày chốt: 2026-10-02. Chủ dự án yêu cầu mỗi vòng thử mặc định gồm **ba lượt Lite, sau đó đối chiếu và review**.

## Phạm vi và điểm dừng

- Với phép thử độ ổn định, giữ nguyên ảnh, prompt, model và cấu hình trong cả ba lượt. Nếu thử ba phương án khác nhau, phải đăng ký rõ từng phương án; không gọi đó là phép thử lặp lại.
- Đăng ký mục tiêu, nguồn đầu vào, phiên bản prompt, tiêu chí đạt, chi phí và ngân sách còn lại trước khi gửi. Quy định ba lượt không cấp ngân sách vô hạn, không mở Quality, API, Extend hoặc quyền công bố.
- Dừng sau ba lượt. Không tự tạo lượt thứ tư để tìm một bản đẹp. Lỗi, kết quả thiếu hoặc thao tác gián đoạn đều phải đối soát trước khi gửi lại.
- Chỉ chuyển Quality khi đầu vào, prompt và thử Lite tương ứng đã qua điều kiện duyệt; không suy từ một clip đẹp rằng toàn bộ quy trình đạt.

## Hồ sơ bắt buộc

1. Gói thử trong `episodes/ep01_pilot`: mục tiêu, approval, input/hash, prompt nguyên văn hoặc liên kết phiên bản, cấu hình, báo giá và giới hạn.
2. Nhật ký từng lượt: thời điểm gửi, mã tài sản/URL, trạng thái, file native/hash, lỗi thao tác và chi phí quan sát. Không lưu thông tin tài khoản hoặc bí mật trong Git.
3. Báo cáo so sánh: kỹ thuật, hình/đạo cụ, diễn xuất, lời/giọng, đồng bộ và điểm nối. Phân biệt đã kiểm, cần sửa và chưa đủ bằng chứng. ASR không thay thế nghe; ảnh mẫu không thay thế xem liên tục.
4. Media và bằng chứng local trong `artifacts`, bản bàn giao trong folder chủ dự án. Tài liệu có đường dẫn cụ thể; không commit media lớn hoặc thông tin nhạy cảm.
5. Bài học tái sử dụng trong `learning`: tách quan sát thực tế, giả thuyết nguyên nhân, cách xử lý và điều kiện kiểm lại. Không biến một lỗi đơn lẻ thành quy luật của Veo.

Mỗi vòng kết thúc phải ghi điều đã xác định, quyết định, giả định, vấn đề mở và bước tiếp theo. Review chưa được thực hiện thì không ghi agent đã kiểm. Commit/push tài liệu theo nhóm công việc có ý nghĩa.
