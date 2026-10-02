# Review bộ sửa khói 133

Trạng thái: CẦN SỬA / KHÔNG CÓ MẪU ĐƯỢC DUYỆT / QUALITY HOLD.

## Phương pháp và giới hạn

Root kiểm kỹ thuật toàn file và xem 16 frame/mẫu, lấy mỗi 0,5 giây từ 0 đến 7,5 giây, qua contact sheet trong `artifacts/opening133-r1/C01-sheet.png` đến C03. Không phải báo cáo reviewer độc lập. Chưa nghe thật, chạy ASR hoặc kiểm liên tục lip-sync. Không dùng luồng audio hoặc ảnh mẫu để kết luận lời/giọng đạt.

## Kết quả đối chiếu

| Tiêu chí | C01 | C02 | C03 |
|---|---|---|---|
| Tải/metadata/giải mã | Đạt kỹ thuật | Đạt kỹ thuật | Đạt kỹ thuật |
| Món nguội không có hơi/khói | Không đạt: vệt hơi rõ trong các frame khoảng 2–3,5 giây | Không đạt: vệt hơi trong các frame khoảng 1,5–3 giây | Không đạt: vệt hơi trong các frame khoảng 1,5–3 giây |
| Tay/đạo cụ theo gói | Đào đưa cả hai tay, Khoai tự diễn tay ngoài ràng buộc | Đào đưa cả hai tay, Khoai tự diễn tay | Cuối đoạn Khoai cầm đũa, trái yêu cầu |
| Chữ tự sinh | Có chữ “Đào” khoảng 6,5–7,5 giây | Chưa thấy trong ảnh mẫu | Chưa thấy trong ảnh mẫu |
| Lời, chất giọng, đồng bộ môi | Chưa kiểm đủ | Chưa kiểm đủ | Chưa kiểm đủ |

Các mốc là thời điểm mẫu đã xem, không khẳng định ranh giới bắt đầu/kết thúc chính xác của lỗi. Không thấy chữ trong ảnh mẫu không đồng nghĩa toàn clip không có chữ. Bộ mới vẫn còn cùng lỗi món nguội bốc hơi mà chủ dự án chỉ ra ở N01; không có bằng chứng prompt v1.1 đã sửa thành công. Không đánh giá mẫu nào hay hơn N01 về giọng khi chưa nghe đối chiếu.

## Điều rút ra và hướng tiếp theo

Quan sát: thêm mô tả món nguội và cấm hơi/khói chưa đủ trong cả ba mẫu này. Không suy thành giới hạn cố định của Veo hoặc kết luận rằng nhắc từ steam chính là nguyên nhân. Có thể đang tồn tại liên tưởng giữa thoại về mùi, động tác tiếp cận món và hiệu ứng hơi; đó là giả thuyết cần kiểm.

Đề xuất vòng kế tiếp: tách một phép thử hình/động tác không thoại và không mô tả mùi để kiểm vùng món có tự sinh hơi không; giữ nguyên ảnh và món nguội, không đổi canon/kịch bản. Nếu lớp hình đạt, mới thử đưa hai câu nguyên bản trở lại để kiểm regression. Đây là phép chẩn đoán riêng, không phải đề nghị bỏ hai câu khỏi tập. Không chạy lặp nguyên prompt v1.1 chỉ để tìm một mẫu đẹp.

Chưa chạy gói kế tiếp hoặc dựng hậu kỳ che khói; chưa sửa N01. Chủ dự án không cần chuẩn bị đầu vào. Ngân sách thử còn 180 theo 133; còn ngân sách không đồng nghĩa phải dùng hết trước review.

Đã xác định: tải ổn trong bộ này, nhưng 3/3 mẫu có vệt hơi ở các frame kiểm. Đã chốt: bộ này cần sửa, chưa mở Quality. Giả định: liên tưởng mùi/diễn xuất có thể gây hơi, chưa chứng minh. Còn mở: nguyên nhân, phương án khống chế hình và voice/lip-sync. Tiếp theo: thiết kế phép thử tách lớp rồi kiểm bộ ba, hoặc chủ dự án đổi hướng xử lý.
