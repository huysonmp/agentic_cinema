# T2 — kết quả 10 lượt Lite và hướng tiếp theo

Ngày: 2026-10-02. Bản biên tập lại tiếng Việt. Số liệu và kết luận không đổi; bản cũ còn trong lịch sử Git.

## 1. Kết quả chính

Đã tạo, tải và lưu đủ 10 clip bằng Veo 3.1 Lite, chế độ Frames, dọc 9:16, một đầu ra mỗi lượt. Mỗi clip dài 8 giây, độ phân giải 720×1280, 24 fps, có luồng âm thanh. Giải mã toàn bộ file không báo lỗi.

Số dư giao diện từ 1.020 xuống 920: giảm 100 credit, phù hợp 10 lượt có giá hiển thị 10 credit. Đây là đối soát số dư, không phải sao kê từng giao dịch. Từ mốc 1.050 trước V01 đến 920 là 130 credit trong ngân sách thử cũ 200 credit.

**Chưa có clip đạt toàn bộ yêu cầu hoặc được chọn làm đầu ra sản xuất.** Không chạy lượt thứ 11 trong vòng này.

Đầu vào thống nhất là OPEN7 trong phạm vi thử nghiệm đã duyệt. Có lượt dùng ảnh đầu riêng, có lượt dùng cùng ảnh cho đầu và cuối. Không dùng ảnh trích từ clip lỗi làm chuẩn mới.

## 2. Kết quả từng lượt

Root kiểm 16 ảnh mẫu mỗi clip, khoảng 0,25–7,75 giây. Các mốc lỗi chỉ xấp xỉ theo ảnh mẫu. Chưa nghe đầy đủ âm thanh, chưa kiểm liên tục toàn bộ hình–tiếng và chưa có review độc lập cho bộ này.

| Lượt | Điều kiện | Lỗi hoặc kết quả quan sát | Kết luận |
|---|---|---|---|
| R01 | Prompt A: nghỉ tự nhiên; ảnh đầu riêng | Tay ổn trong mẫu nhưng thêm hơi khói khoảng 1,75–3,75 giây | Cần sửa |
| R02 | Lặp nguyên prompt A | Khoai giơ tay, mở miệng; rau và món bị dịch hoặc biến đổi | Cần sửa |
| R03 | Prompt B: ảnh chân dung có chuyển động nhẹ; ảnh đầu riêng | Khoai giơ tay đầu clip; trạng thái mặt thay đổi | Cần sửa |
| R04 | Prompt B; cùng ảnh đầu–cuối | Đào giơ hai tay khoảng 1,25–2,75 giây; miệng thay đổi | Cần sửa |
| R05 | Prompt C: chỉ chớp mắt; cùng ảnh đầu–cuối | Tay, mắt và miệng vẫn chuyển động ngoài yêu cầu | Cần sửa |
| R06 | Prompt D ngắn, chỉ dẫn chuyển động; cùng ảnh đầu–cuối | Đào cử động tay khoảng 0,75–1,25 giây; phần sau trông ổn hơn trong mẫu | Chưa đạt cả clip |
| R07 | Prompt D; ảnh đầu riêng | Hai người giơ tay đầu clip, Khoai cử động thêm cuối clip | Cần sửa |
| R08 | Prompt E: đứng yên tuyệt đối; ảnh đầu riêng | Tay, đầu và miệng vẫn chuyển động | Cần sửa |
| R09 | Prompt E; cùng ảnh đầu–cuối | Khoai giơ tay khoảng 1,25 giây; miệng mở ở nhiều mẫu | Cần sửa |
| R10 | Lặp nguyên prompt A lần thứ ba | Khoai giơ hai tay khoảng 0,75–3,25 giây; đầu và miệng thay đổi | Cần sửa |

Nhiều lượt giữ được món, rau, đồ chấm và hai nhân vật trong khung. Tuy nhiên việc giữ nguyên tư thế nghỉ chưa ổn định: R01 không lặp lại được ở R02/R10; cùng ảnh đầu–cuối cũng không khóa được chuyển động giữa clip.

Kết quả này chỉ áp dụng cho các đầu vào, prompt và cấu hình đã thử. Không kết luận mọi clip Lite hoặc Quality đều thất bại. Không có seed cố định; số mẫu ít và các nhóm prompt thay đổi, nên không suy ra quan hệ nhân quả chắc chắn.

## 3. Hướng tiếp theo và quyết định mới

Ba phương án đã trình:

- A: dùng chuyển động 2D có kiểm soát trên ảnh cho phần dẫn mắt của cảnh mở; dùng Veo cho diễn xuất.
- B: giữ hoàn toàn Veo, thay thử nghiệm đứng yên bằng một hành động nhỏ có chủ đích.
- C: xem liên tục và nghe R06 để kiểm xem có đoạn ngắn tận dụng được hay không.

**Chủ dự án đã chọn A**, được ghi tại [tài liệu 121](121_hybrid-opening-approval-and-production-readiness-audit.md). Không hỏi lại lựa chọn A/B/C.

Chuyển động 2D không tạo góc nhìn 3D hoặc vùng ảnh chưa tồn tại. Bản thử phải chứng minh giữ đủ bữa ăn, mặt và đạo cụ; không tự bỏ hành động hoặc thoại của kịch bản để phù hợp ảnh đứng yên. Chưa có bản thử local đạt hoặc được duyệt.

Ngân sách Quality riêng tối đa 100 credit đã được duyệt có điều kiện tại [tài liệu 122](122_conditional-quality-approval-and-owner-actions.md): chỉ thử sau khi đầu vào, prompt và thử nghiệm tương ứng đạt trên Lite. Bộ 10 clip này không đáp ứng điều kiện đó.

## 4. File bàn giao vòng thử

Thư mục: C:\Users\PC\Downloads\du_an_nem_bui.

- Clip nguyên bản: 119_R01.mp4 đến 119_R10.mp4.
- Bảng ảnh theo thời gian: 119_R01_sheet.png đến 119_R10_sheet.png.
- Bằng chứng giao diện: 119_R##_PRE.jpg và 119_R##_RESULT.jpg.
- Prompt nguyên văn, mã clip, file và SHA256: [nhật ký 119](119_t2-idle-performance-experiment-round.md).

Ảnh tài khoản dùng đối soát số dư chỉ lưu local, không nhúng công khai. Giữ hình mờ gốc. Media không đưa lên Git; tài liệu và hồ sơ truy xuất được quản lý phiên bản.

## 5. Tổng hợp

Đã xác định: đủ 10 đầu ra, không có clip đạt toàn bộ mục tiêu trạng thái nghỉ.

Đã chốt: dừng vòng thử; chọn hướng A; không đổi kịch bản C-v0.5, nhân vật hoặc claim món ăn.

Giả định: OPEN7 phù hợp cho chẩn đoán, chưa tự trở thành đầu vào cuối cho mọi cảnh.

Còn mở: giọng, đầu vào theo cảnh, diễn xuất, nối cảnh, bản ráp khoảng 30 giây và nghiệm thu. P6/P7 vẫn mở.

Bước tiếp theo: thiết kế bổ sung cảnh mở kết hợp, tạo bản thử local và chuẩn bị các gói thử Lite đúng mục tiêu. Không tự nâng Quality hoặc chọn sản phẩm cuối.
