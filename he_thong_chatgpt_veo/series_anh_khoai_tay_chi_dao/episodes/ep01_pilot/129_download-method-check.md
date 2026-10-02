# Kiểm lại phương thức tải — không tạo lại video

Ngày: 2026-10-02. Chủ dự án xác nhận tự thao tác tải được trên cùng giao diện.

## Bằng chứng mới và đính chính

Đã tìm thấy `C:/Users/PC/Downloads/Two_friends_having_casual_meal_20261002111259.mp4`, kích thước 2.390.372 byte. ffprobe đọc được video 720×1280, 24 fps, dài 8 giây và một luồng âm thanh. SHA256: `87AB54CFA7B46C683D5DD33C7321147E9ECB9993447471937A4839BF63253A4D`.

File này chứng minh tải thủ công đã tạo được file local. Tên trùng giữa R02/R03 nên chưa tự gán mã lượt. Chưa kiểm nội dung hoặc giọng của file trong vòng này.

Không có căn cứ kết luận Flow không tải được hoặc video nguồn hỏng. Vướng mắc hiện tại là đường thao tác/tải tự động của tôi; nguyên nhân kỹ thuật chưa xác định. Đề nghị tạo lại video trước khi làm rõ đường tải là chưa phù hợp: không có bằng chứng generation mới sẽ giải quyết được lỗi vận chuyển file.

## Phép kiểm trên R01

1. Mở đúng mã `61bf42a2-f657-49a4-919f-5f4c2faa64d1`, chọn tải 720p kích thước gốc qua giao diện.
2. Giữ nguyên tab, không chuyển clip, chờ và kiểm Downloads: chưa có file R01. Việc giữ tab chưa giải quyết lỗi, nên chưa kết luận chuyển clip quá sớm là nguyên nhân.
3. Mở lại menu, đối chiếu screenshot và bấm trực tiếp vị trí 720p bằng công cụ điều khiển trình duyệt. Trang báo đã tải; sau khi chờ và kiểm file vẫn không có file mới.

Vì cả cách bấm theo phần tử lẫn theo vị trí đều chưa tạo file, không gọi thao tác đã hoàn tất chỉ dựa vào thông báo. Trình quản lý download bên ngoài nội dung website chưa được công cụ hiện tại đọc, nên chưa thấy lý do “Stopped” mà chủ dự án báo. Không sửa quyền, không đổi trình duyệt/tài khoản, không tạo video hoặc upscale.

## Bước tiếp theo

### Kiểm bổ sung: mở lại và tải từ thẻ thư viện

Theo yêu cầu mở lại, tab cũ không còn trong phiên nên đã mở tab Flow mới tại đúng R01. Sau đó về thư viện, mở menu ngữ cảnh thẻ `Two friends talking over meal` → `Tải xuống` → `720p kích thước gốc`, thay vì nút tải trong editor. Giữ nguyên tab và chờ; kiểm Downloads vẫn chỉ có file chủ dự án tải lúc 11:12:59, chưa có file R01. Công cụ bundle nguồn video vừa quan sát trong tab mới cũng lỗi fetch. Chưa xác định nguyên nhân của đường tải tự động; không tạo thêm video. Bằng chứng: `artifacts/opening127-r1/reopened-card-download.png`.

Cần đối chiếu đúng bước tải thủ công thành công với đường điều khiển của tôi, đặc biệt có hộp thoại lưu/xác nhận hoặc thao tác ở bảng Downloads hay không. Cần một mô tả ngắn hoặc ảnh phần trạng thái tải và lý do dừng; không yêu cầu chủ dự án tạo lại video. Sau khi xác định cách nhận file, kiểm một lượt thành công trước rồi mới tải hai lượt còn lại. Quality và review bộ ba vẫn chưa hoàn tất.
