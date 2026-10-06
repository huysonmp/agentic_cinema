# EP01 — Một lượt sửa U05 có giới hạn

Ngày 2026-10-06. U05 lượt 203 đã REWORK về môi/tay/hướng nhìn dù không có audio. Không chọn đoạn lỗi làm production. Lượt này dùng **một lần sửa x1** trong dự phòng gói 198, không mở audition hoặc bộ ba mẫu.

**Cập nhật205:** owner đã duyệt phương án phản ứng ngắn và tiếp tục trong ngân sách còn lại. Trạng thái chờ quyết định ở phần kết quả dưới là lịch sử; xem [approval và timing hiện hành205](205_short-reaction-approved-and-u04-continuation.md). Approval không bao gồm đoạn môi mở về sau.

## Thay đổi có mục tiêu

Giữ câu chuyện: Đào đang nhìn về cốc; sau khi Khoai gắp và nâng nem, cú cắt sang Đào cho thấy chị đã nhìn Khoai và bắt gặp. Thay cách biểu đạt S06 từ quay đầu thấy trọn trong shot sang **lộ ánh nhìn qua cú cắt**. Không đổi lời/người nói, không bỏ phản ứng bắt gặp và không thêm thoại.

Dùng chính END195 đã duyệt cho cả START và END: cùng file/hash `0e6a2f348ecd1cde923fa668d7b2163ad8b584f3be1e3a8cb7a91fa04b33e4de`, không sinh ảnh mới. Đào đã nhìn trái; yêu cầu một blink tự nhiên nhẹ, hai tay và môi giữ tư thế. Prompt sửa bỏ nhiệm vụ quay đầu và thay đổi biểu cảm, giới hạn vận động. Đây là sửa phối hợp nguồn/diễn để hoàn thiện, **không phải thí nghiệm đơn biến hoặc bằng chứng đã xác định nguyên nhân nội bộ của model**.

Shot dựng S06 vẫn 20,4583–21,9583 giây theo timeline 203; phải có đoạn chuyển động sạch đủ 1,5 giây. Không freeze, loop, crop mặt để che môi hoặc nói rằng đã giữ môi nếu actual vẫn mở. Phải kiểm output thật; nếu có đoạn sạch, chỉ chọn đúng range đã kiểm, không suy cả clip đạt.

## Preflight và điều kiện dừng

Giữ Lite/Frames/9:16/720p/8 giây/x1; quote phải đọc lại là 10 trước gửi. Không audio reference, lời thoại, API mới, Quality hoặc x3. Giữ watermark. Số dư account đã kiểm sau 203 là 137, không dùng để mở cap.

Sổ trước lượt sửa: trần 422/đã chi 339/còn 83. Nếu charge 10: đã chi 349/còn 73. Bảy đơn vị chưa tạo dự kiến 70, còn 3 dự phòng; **không đủ một lượt sửa 10 tiếp theo**. Nếu U05 vẫn không có range đạt, dừng chi tiếp và trình ngoại lệ theo 197/198. Không tự lấy 70 earmark cho các cảnh khác để thử U05 lần nữa.

## Kết quả và ngoại lệ cần chốt

Gửi đúng một lần. Account 137 → 127, chi thực 10; sổ **349/422, còn 73**, trong đó bảy đơn vị chưa tạo dự kiến 70 và dự phòng 3. Clip mới `b586e1ab-467e-48a4-a8d0-99252fbfda2c` hoàn tất. Một yêu cầu tải 720p không trả event trong 20 giây nhưng file đã có ở Downloads; kiểm file trước retry nên không tải lại. Bản gốc và owner copy cùng SHA256 `a44da6d29321d0bb9df6b25f27e58036fe0dc8ff995366f85e31acbbdeb44c2c`, 1.835.987 byte. H264 720×1280/24 fps/8 giây/192 frame, không audio; giải mã toàn bộ sạch.

Root kiểm 48 frame lấy mẫu tám giây và đủ 36 frame cận môi/toàn thân trong 1,5 giây đầu. **REWORK theo yêu cầu đoạn phản ứng 1,5 giây**: môi bắt đầu mở khoảng 0,75 giây và thay đổi ở các mẫu về sau, nhiều blink/chuyển động đầu hơn chỉ đạo. Tay/cốc ổn định hơn lượt 203 trong đoạn đầu, nhưng không biến tiến bộ riêng đó thành PASS cả shot. Chưa chọn range sạch đủ 1,5 giây; không nói đã kiểm từng frame cả tám giây hoặc agent độc lập đã chạy. [Kết quả và hash](evidence/204/results.json), [môi đủ 36 frame đầu](evidence/204/opening_mouth_all36.png), [toàn thân đủ 36 frame đầu](evidence/204/opening_body_all36.png).

Đã **dừng paid dispatch** theo giới hạn dự phòng; không lấy 70 dành cảnh khác để thử U05 lần ba. Chuẩn bị phương án dựng không thêm lượt U05: dùng source 0–0,625 giây (15 frame đầu đã kiểm, môi khép/ánh nhìn trái, blink nhẹ), chuyển 0,875 giây/21 frame sang nhịp Khoai khựng tay trước cú cắt. Không thay tiếng, tổng 30 giây hoặc cơ chế bị bắt gặp; không freeze/loop/slowdown. S06 đề xuất còn frame 512–527, S05 tăng đến512; S07 giữ nguyên. Cần U04 có actual range sạch thêm 0,875 giây; nguồn của hai đoạn U04 phải liên tiếp hoặc khác nhau không lặp. Đây là **đề xuất chờ owner duyệt**, chưa áp vào timeline hiện hành hoặc gọi đã nối thành công.

Owner file xem thử: `C:/Users/PC/Downloads/du_an_nem_bui/204_u05_repair/U05_0.000-0.625_SHORT_ALTERNATIVE_NOT_APPROVED.mp4`, SHA256 `3470254b657ecc371fb29d7def13a972302b6f05f8ec5afb2e7cccc7996f7e81`. Không coi phim ngắn này là đầu ra final. Skill computer-use giúp đọc lại đầu vào/quote, gửi x1 và nhận native qua UI; thiếu event tải không đồng nghĩa thiếu file.

## Tổng hợp

- Đã xác định: tiếng bảy lượt được duyệt; hai U05 chưa đạt shot 1,5 giây, bản sửa có 0,625 giây đầu dùng được về mặt kiểm hình của root.
- Đã chốt: giữ tiếng/script; không mở thêm thử U05 trong dự phòng còn 3.
- Giả định: U04 có thể cung cấp thêm 0,875 giây khựng tay, phải kiểm actual trước dựng.
- Còn mở: owner có chấp nhận phản ứng ngắn không; các nguồn cảnh khác, nối hình–tiếng, mix/phụ đề/xuất vẫn chưa hoàn tất.
- Tiếp: owner chốt nhịp thay thế; nếu duyệt, cập nhật range/frame và chuẩn bị U04 theo continuity, không tự sinh khi đầu vào chưa đạt.
