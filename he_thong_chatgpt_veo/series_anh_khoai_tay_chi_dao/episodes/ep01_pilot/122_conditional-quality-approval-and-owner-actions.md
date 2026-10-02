# EP01 — ngân sách Quality có điều kiện và việc cần chủ dự án xử lý

Ngày: 2026-10-02.

## 1. Quyết định đã chốt

Chủ dự án: “chấp nhận duyệt ngân sách 100 credit thử, ta chỉ test thử xem có thật sự làm ok k sau khi các nguồn đầu vào, promt và thử nghiệm đã đạt với lite”.

- Duyệt ngân sách riêng tối đa **100 credit cho một lượt thử Quality**, không phải chạy cả tập.
- Chỉ chạy sau khi **đầu vào, prompt và thử nghiệm tương ứng đã đạt trên Lite**.
- Không lấy bộ 10 lượt lỗi trong tài liệu 119 làm bằng chứng đã đạt Lite.
- Không tự thêm lượt Quality, chuyển sang thử nghiệm khác hoặc mua credit. Nếu giá vượt 100 credit, dừng và trình lại.
- Ngân sách này tách khỏi ngân sách thử cũ 200 credit; không mở rộng trần của các thử nghiệm Lite.
- Chưa có yêu cầu Quality được gửi. Không dùng ngân sách Quality để chạy thêm Lite.

Hướng cảnh mở kết hợp đã được chọn. Giữ kịch bản C-v0.5, quan hệ bạn bè, bố trí bàn ăn và ranh giới thông tin đã duyệt.

## 2. Những việc chủ dự án cần xử lý

Không có việc chuẩn bị file hoặc cài công cụ nào cần chủ dự án làm ngay. Các quyết định dưới đây cần sản phẩm cụ thể trước khi hỏi; không yêu cầu trả lời khi chưa có mẫu.

| Việc cần quyết định | Khi nào tôi trình | Chủ dự án cần làm |
|---|---|---|
| Cảnh mở kết hợp có đúng chất T2 không | Khi có bản thử local cùng bản đồ nối thoại/hành động | Xem và chọn giữ hoặc sửa; tôi không yêu cầu bạn tự tạo ảnh |
| Giọng Khoai và Đào | Khi có mẫu thật, lời đúng và báo cáo kỹ thuật | Nghe, đánh giá sắc thái, độ tự nhiên và chọn mẫu; chưa hỏi lại hướng giọng |
| Clip Lite có đạt ý đồ sáng tạo không | Khi có clip đúng đầu vào/prompt và các lỗi kỹ thuật đã kiểm | Xem và chọn mẫu đối chứng cho lượt Quality |
| Ngoại lệ so với kịch bản hoặc cách quay | Chỉ khi bằng chứng cho thấy cần thay đổi | Duyệt hoặc bác thay đổi; không tự đổi cảnh S04–S05 |
| Quyền tài nguyên còn thiếu | Nếu việc đối soát phát hiện ảnh/nhạc có phạm vi quyền chưa rõ | Cung cấp bằng chứng đang có hoặc chọn loại tài nguyên đó |
| Bản cuối | Khi có bản xuất và báo cáo kiểm đầy đủ | Nghiệm thu; quyết định công bố vẫn thuộc bạn |

Nếu gói thử Lite mới cần quyền hoặc chi phí ngoài phạm vi đã duyệt, tôi sẽ trình **một gói cụ thể** gồm mục tiêu, đầu vào, prompt, số lượt, tổng credit và điều kiện dừng. Không xin duyệt lại ngân sách Quality đã chốt.

## 3. Những việc tôi nhận xử lý

1. Sửa tài liệu trình duyệt bằng tiếng Việt rõ ràng; giữ nguyên prompt đã chạy, số liệu, hash và lịch sử quyết định.
2. Lập bản thiết kế bổ sung cho cảnh mở kết hợp. Không bỏ câu thoại, động tác kéo đĩa hoặc ý đồ món dẫn vào ký ức.
3. Chuẩn bị bản thử local và kiểm đủ mặt, món, rau, chấm, bát, đũa, cốc và hình mờ. Không gọi chuyển động 2D là đổi góc máy 3D.
4. Chuẩn bị đầu vào, prompt và checklist cho từng thử nghiệm giọng/động tác; không thay nhiều nhóm yếu tố rồi suy nguyên nhân tùy tiện.
5. Kiểm quyền chạy, cấu hình, giá và giới hạn trước khi gửi yêu cầu Lite.
6. Ghi lỗi theo phiên bản; sửa và kiểm lại. Chỉ ghi vai trò đã chạy khi có báo cáo thật.
7. Khi điều kiện Lite đủ: khóa bộ đối chứng, chuẩn bị một lượt Quality, kiểm giá không vượt 100 credit và so sánh kết quả với Lite.
8. Lưu tài liệu, file kết quả, nguồn và quyết định; commit/push hồ sơ theo nhóm công việc. Media vẫn lưu local theo cách hiện tại.

## 4. Điều kiện mở lượt Quality

Phải có đủ:

- Đúng đầu vào và phiên bản, có nguồn, hash và quyền dùng phù hợp.
- Prompt cuối đã thử trên Lite; phạm vi lời thoại/hành động rõ ràng.
- Clip Lite cụ thể không còn lỗi chặn mục tiêu thử; đã kiểm trên đúng bề mặt cần đánh giá. Ảnh mẫu không đủ để chứng nhận toàn bộ chuyển động hoặc giọng.
- Chủ dự án chọn mẫu Lite về mặt sáng tạo trước khi dùng làm đối chứng.
- Bộ kiểm mục tiêu: nhân vật, món/đạo cụ, động tác, góc máy; nếu có thoại thì thêm lời, giọng và đồng bộ môi. Ghi rõ điều không thuộc phạm vi.
- Cấu hình Quality phù hợp đầu vào; giá giao diện không vượt 100 credit; một đầu ra, không retry tự động.

“Đạt Lite” ở đây là đạt thử nghiệm tương ứng, không yêu cầu toàn bộ tập đã hoàn tất. Sau khi đổi model, kết quả Quality vẫn phải kiểm lại; không kế thừa PASS từ Lite.

## 5. Trạng thái và bước tiếp theo

Đã chốt: phương pháp cảnh mở kết hợp và ngân sách Quality có điều kiện.

Giả định: có thể chuẩn bị bản thử cảnh mở bằng công cụ local hiện có; phải xem kết quả trước khi kết luận chất lượng.

Còn mở: bản thiết kế cảnh mở, mẫu giọng, thử động tác, quyền chạy Lite mới và lựa chọn đối chứng.

Bước tiếp theo: hoàn thiện tài liệu tiếng Việt và thiết kế cảnh mở để làm bản thử local. **Chưa cần bạn trả lời thêm ngay lúc này.**
