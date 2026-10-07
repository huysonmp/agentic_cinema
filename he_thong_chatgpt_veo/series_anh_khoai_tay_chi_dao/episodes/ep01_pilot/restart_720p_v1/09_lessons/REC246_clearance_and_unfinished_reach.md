# REC246 — Khoảng hở phải nhìn thấy, không chỉ ghi trong prompt

## Bằng chứng

C01A T01, native SHA256 `0c42df876e8d3b7b46fe1b7930f3fc33ecf1e462f6c3f66ddabf677efb6c67d4`: prompt yêu cầu tay gần mép đĩa có khoảng hở, không chạm và không thu sớm. Output vươn đúng tay, nhưng ngón che mép từ khoảng3,333 giây; lời offline kết khoảng3,66 giây; tay bắt đầu thu khoảng4,083 giây. Reviewer kiểm52 khung, gồm84–101 liên tiếp, không chứng nhận playback/actual hearing. Không có range đã kiểm giữ đủ lời và khoảng hở rõ.

## Điều rút ra và giới hạn

- Món không di chuyển không chứng minh tay chưa chạm; phải thấy bàn tay, mép đĩa và khoảng hở trong hình tại đoạn được giữ.
- Thu tay ở đuôi đôi khi xử lý được bằng dựng, nhưng chỉ khi đoạn trước đó đã đủ lời và đạt toàn nhiệm vụ. Cắt đuôi không đóng lỗi clearance đang có trong câu.
- Một gesture sinh đủ vòng vươn–thu làm “Khoan” sau đó mất nguyên nhân; cần ý định chưa hoàn tất ở điểm ra, không chỉ pose cuối đẹp.
- “Near rim” có thể không mô tả đủ khoảng hở đọc được. Đích cao hơn, khoảng trống hình rõ và hold là giả thuyết sửa có mục tiêu; không là bằng chứng chắc chắn model hiểu hoặc một nguyên nhân duy nhất.
- Giữ hand intent theo hướng vươn, không xòe lòng bàn tay giới thiệu món. Gap lớn nhưng mất ý định lấy vẫn chưa đạt diễn xuất.
- ASR khoảng0,76–3,66 giây và đo im lặng ở ngưỡng-40dB là hai loại tín hiệu, không định nghĩa sample-accurate word cut hoặc chất D06. Owner nghe output thực trước mở rộng thoại Đào.

## Áp dụng lượt kế

T02 giữ ảnh/voice/lời/camera/món, chỉ dàn điểm dừng và trạng thái vươn chưa hoàn tất rõ hơn; wording có tái diễn đạt, không coi đây là thí nghiệm cô lập một biến. Trước gửi kiểm lại binding/quote/readback. Sau tạo kiểm cả đường tay và khoảng lời; nếu cùng MAJOR lặp hai output, dừng thay vì chạy tiếp vì còn credit. Kết quả T02 sẽ được bổ sung, không ghi đã khắc phục trước output.

## Cập nhật actual T02 và học hồi quy

T02 hash `0b5615beef4e23a42428771109fe36544510270281ae35129de6f6c585a398a7`, native6s/144 khung. Full0/56/88/143 và board6fps có dòng chữ mới dưới bàn, nguồn F0 không có. Phát sinh trước dựng, không phải caption root; không cắt đuôi để cứu lỗi nằm từ đầu. “Preserve source watermark” là hướng dẫn chung thiếu phạm vi, cần mô tả đúng biểu tượng nguồn, nhưng không kết luận một câu này là nguyên nhân đã chứng minh.

Truy cẳng tay từ vai phải màn hình cho thấy đúng tay ngoài; rút lại nghi ngờ nhầm tay ban đầu. Bảng thumbnail phải kiểm lại trên ảnh đủ lớn trước ghi lỗi. ACT/DOP đánh giá palm-up/xòe giống giới thiệu món: sửa clearance có thể làm mất intent. Hồi quy phải kiểm ý nghĩa động tác, không chỉ khoảng hở/không-chạm.

Owner nghe riêng exact T02 audio, chấp nhận D06/lời/nhịp. Điều này không đóng picture/lip-sync hoặc take mới. Không ghi SIA đã nghe từ câu trả lời owner; đó là human listening evidence.

Đề xuất ACT/DOP: palm-down/ngón hơi cong và đích gỗ thấp trước rim, bỏ đích cao/gap cứng. Khả thi có điều kiện trên ảnh, không bảo đảm motion. Draft T03 giữ nguyên source/lời/voice/camera, chưa gửi. Trước retake phải tích hợp critic và quyết định stop-rule, không đổi tên lỗi để né ngưỡng dừng.

## T04 và quy tắc không tự nới tiêu chuẩn

T03 không có output; T04 sau một clarification về canon trưởng thành có native. Hình mẫu không còn chữ/palm-up nhưng tay tới vành và đĩa bị kéo ở đuôi. Không coi lỗi trước không lặp là whole-task PASS. Root giữ beforecontact HOLD và hỏi owner về phạm vi ngoại lệ rim-touch + gesture tay trong, vẫn không kéo/lấy món.

Owner đã cho phép ngoại lệ hạn chế; không approval native6s hoặc voice T04. Bản cắt phải có đủ lời, chưa di chuyển đĩa và actual range/hash, C01B tiếp đúng pose rồi dừng/thả/thu sau “Khoan”. Không dùng ngoại lệ để nhận đuôi kéo đĩa đã đạt.

Trong Flow, Addclip trên trang native tạo draftscene đã tự có original rồi thêm một instance nữa, thành12s. Root nhìn timeline, gỡ chỉ instance thứ hai, kiểm lại6s; native vẫn giữ. Trước trim/export luôn kiểm số clip và duration, không suy trang preview đồng nghĩa timeline trống. Đây là lỗi thao tác nháp đã khắc phục, không finalcut/creditgeneration.
