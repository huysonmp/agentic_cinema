# REC243 — Phân biệt lỗi take với khả năng dựng

## Bằng chứng và nguyên nhân

Một lượt C02 giá 15 đã sinh, tải và kiểm native 720×1280, 24 fps, 240 khung, 10 giây. Reviewer độc lập chỉ ra ba lỗi: đổi nền, khung quá rộng và cử chỉ tay đầu cảnh sai. Exact v5 và K20 đã được kiểm qua UI trước gửi; không có bằng chứng gắn nhầm ảnh hoặc giọng.

Điều đã biết: output không thực hiện đúng giữ scene, framing và trạng thái đầu đã yêu cầu. Giả thuyết: master toàn cảnh trong Ingredients, cùng yêu cầu đổi framing bằng chữ, làm model tái dựng set và vẫn giữ cỡ khung rộng. Chưa có bằng chứng cơ chế để coi đó là nguyên nhân duy nhất. Prompt có khóa geography bàn nhưng chưa nêu cụ thể các dấu hiệu nhận diện nền.

## Hướng sửa đề xuất — chưa chạy

Chuẩn bị reference cận vừa riêng C02 từ master v5, giữ mái bạt, đèn lồng, phố và tay nghỉ. Ảnh nguồn thể hiện framing trực tiếp; request video chỉ yêu cầu diễn mắt/đầu/miệng nhẹ và bảo toàn nền. Không đổi script/K20 hoặc tăng Quality để chữa attribution. Reference và take mới vẫn phải review; không cam kết thành công.

Đào chắp tay trong mẫu 0–0,667 giây, hạ tay ở 0,833 giây, nghỉ ở 1 giây. ASR ước lượng onset “Mùi” ở 0,88 giây. Chưa nghe và chưa đủ bằng chứng handle để cắt đầu an toàn. Cắt đầu cũng không chữa nền hoặc khung rộng; không bỏ âm hay phủ lời bằng món.

## Kinh nghiệm công cụ

- Tab cũ không cập nhật thư viện/số dư sau job: tab cũ báo 1.050, tab đã tạo và cập nhật báo 1.035. Không lấy stale UI làm bằng chứng không tốn credit.
- “Lưu vào dự án” tạo bản sao native, không là job sinh thứ hai. Picker ở tab scene cũ vẫn trống. Đóng tab đó, mở tab mới cùng scene thì thấy clip; download preview và đối chiếu hash trùng native trước khi thêm.
- Tải lại local video phát sinh thông báo xác nhận quyền sử dụng. Đã hủy, không bấm đồng ý; đường thư viện native dùng được sau khi mở tab mới. Không cần vượt thông báo.
- Slider trim không điều khiển được bằng bàn phím trong lượt này. Dùng tay nắm từ screenshot, kéo rồi đọc giá trị UI: điểm cuối 9. Sau thêm clip, AX tạm báo 10 rồi cập nhật 9; không kết luận trim thất bại từ trạng thái quá sớm.
- Scene trống mặc định 16:9. Đổi và đọc lại DOM 9:16 trước export. File xuất 720×1280, 217 khung/24 fps = 9,041667 giây dù UI ghi 9. Phải đo file thật khi lập EDL, không cộng các số giây UI để khẳng định đúng 30 giây.
- Audio xuất dài 9,002667 giây. Tương quan PCM với phần nguồn là 0,9999898. Điều này xác nhận giữ tín hiệu track, không xác nhận chất giọng hoặc đồng bộ môi.
- Chưa kiểm nối nhiều clip, chữ, mix hoặc phim 30 giây. Một clip cắt–xuất không tự PASS toàn khâu dựng.

## Cổng còn mở

Human nghe exact native để kiểm K20 và “mẹ rang gạo”. ASR small offline ghi “mẹ Giang Gạo”, với độ tin cậy từ “Giang” thấp; chỉ là cờ cần nghe, không tự đổi lời hoặc chấm fail audio.

Các kiểm trên giấy, ảnh mẫu và tín hiệu audio không thay FULL_AV. C02 vẫn cần sửa hình; output mới phải có nguồn, hash, report và quyết định mới.
