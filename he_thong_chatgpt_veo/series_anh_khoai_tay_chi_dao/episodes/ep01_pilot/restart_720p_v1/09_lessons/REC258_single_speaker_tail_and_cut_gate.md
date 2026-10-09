# REC258 — Kiểm lời ngắn và phần đuôi của người nghe

## Quan sát thực

- Đã dùng đúng một ảnh khung cuối C02, một preset Đào/D06, lời ngắn duy nhất và chỉ dẫn Khoai khép môi. Một output 4 giây vẫn có Khoai bắt đầu khe môi F42, mở rõ F43–47 và khép lại F49 sau khi Đào đã hỏi; prompt phủ định không khóa được toàn bộ biểu diễn của người nghe. Reviewer xem PNG riêng cũng thấy khe nhẹ đuôi F94–95.
- Root đã xem đủ 96 khung qua 12 board; không thấy gắp, kéo đĩa, hơi nóng hoặc chữ thoại. Không suy ra đúng giọng hay đồng bộ lời–môi từ ảnh tĩnh.
- ASR offline không mồi kịch bản ghi “Anh chờ anh à?”, kết đoạn 1,36 giây; từ “ăn” còn mơ hồ. Không tự sửa transcript thành lời dự kiến hoặc kết luận chắc chắn output nói sai. Cần nghe bản thực.
- Ảnh Ingredients là tham chiếu, không khóa pixel/camera. C03A F0 có kích thước nhân vật nhỏ/thấp hơn khung cuối C02; tay ngoài Khoai đổi từ cạnh đũa vào gần bát. Phải kiểm chỗ nối thực, không duyệt continuity từ hash ảnh đầu vào hoặc chỉ hỏi cỡ khung mà bỏ sai khác tư thế tay.
- Khi kiểm chip, click chip hiện hành đã xóa giọng. Đã nhận ra trước submit, gắn lại đúng UUID D06 qua picker và đọc lại đủ hai chip; không phát sinh output sai do thao tác này. Sau này kiểm chip bằng đọc DOM/preview picker, không click thử chip để tìm thông tin.

## Xử lý trong vòng này

- Giữ nguyên native 4 giây. Candidate [0,42) dài 1,75 giây: giữ câu hỏi và khoảng nghỉ sau lời, bỏ trước F43. Không đổi tốc độ/pitch, không vá môi hoặc lồng thêm giọng.
- Nối candidate vào opening owner đã chấp nhận: 372 khung, 15,5 giây; kiểm đủ 48 khung liên tiếp quanh cut và toàn candidate sau encode. Không gọi bản nối là phim cuối.
- Các điểm nghe đúng “ăn”, trọn “à”, đúng D06, nhịp hỏi và chỗ đổi cỡ khung vẫn chờ owner xem/nghe. Không mở C03B theo approval preset cũ.
- Một lượt chi 7 credit; không tự retry. Số dư cùng tab 1.015→1.008. Tăng 50 giữa snapshot trước và lần này chưa rõ nguyên nhân, không tăng trần chi dự án.

## Quy tắc tái sử dụng

Lời thoại ngắn cần kiểm cả phần đuôi người nghe. Chọn đoạn chỉ sau khi kiểm trọn lời, lips-rest, hành vi và chỗ nối actual; ASR là tín hiệu cần kiểm, không là chứng nhận giọng hoặc căn cứ sửa chữ cho khớp kịch bản.
