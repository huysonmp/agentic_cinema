# EP01 — bộ ba Lite sửa khói và bổ sung ngân sách

Ngày: 2026-10-02. Trạng thái: ĐÃ TẢI ĐỦ BA FILE / KỸ THUẬT ĐẠT / CẦN SỬA KHÓI VÀ DIỄN XUẤT.

Chủ dự án yêu cầu chạy và cấp **thêm 200 credit cho thử nghiệm**. Trần thử tích lũy từ 200 lên 400; đã dùng 190 theo hồ sơ 130, còn 210 trước bộ này. Đây là quyền tiêu trong hạn mức, không phải việc mua/nạp credit hoặc tăng số dư tài khoản. Quality 100 và phạm vi V02 giữ nguyên, không tự mở Quality.

Bộ này: ba mẫu Lite, cùng ảnh OPEN7 và nguyên văn prompt v1.1 tại tài liệu 132, chỉ sửa ràng buộc nhiệt độ/khói. Một yêu cầu x3 dự kiến giá 30; kiểm giao diện trước gửi. Frames, START OPEN7/END trống, dọc 9:16, 720p, 8 giây. Dừng sau ba mẫu, tải từng file rồi review và đối chiếu N01 cũ. Không hứa giữ đúng giọng/diễn xuất của N01 qua generation mới.

| Mẫu | Mã tài sản | File native | Kiểm kỹ thuật | Review |
|---|---|---|---|---|
| C01 | `936a253a-074b-495f-8972-cca37a9e1490` | `C01.mp4`, 2.708.837 byte | Giải mã sạch | Hơi trên món; chữ Đào tự thêm |
| C02 | `91406b20-d350-4004-98b4-266c1cdb91a5` | `C02.mp4`, 3.002.314 byte | Giải mã sạch | Hơi trên món; sai staging tay |
| C03 | `3485fd28-cb22-4231-a3f0-e6d26d6ef636` | `C03.mp4`, 2.517.424 byte | Giải mã sạch | Hơi trên món; cầm đũa ngoài yêu cầu |

Số dư trước: 860 credit, đọc trên Flow. Đã kiểm Lite/Frames/9:16/720p/8 giây/x3, báo giá 30, START OPEN7 và END trống. Đã gửi lúc 12:23:47 giờ Việt Nam. Số dư sau và chi phí thực tế: chờ kiểm. Bằng chứng local `artifacts/opening133-r1/settings.png`, `preflight.png`; bản bàn giao dự kiến `C:/Users/PC/Downloads/du_an_nem_bui/133_cool_food_lite`.

Preflight phát hiện thông báo website không kết nối được dịch vụ reCAPTCHA; đã nạp lại trang khi chưa nhập/gửi yêu cầu. Nếu xuất hiện thử thách CAPTCHA cần chủ dự án xử lý/duyệt tại thời điểm đó; không tự vượt hoặc bỏ qua.

## Đối soát hoàn tất

Đã tải từ menu từng thẻ thư viện → 720p kích thước gốc, giữ tab và kiểm file trước khi tải mẫu kế tiếp. File Downloads lần lượt: `Friends_having_a_meal_dialogue_20261002122551.mp4`, `...20261002122639.mp4`, `...20261002122751.mp4`. Sao lưu nguyên file tại `artifacts/opening133-r1/C01.mp4` đến C03; bàn giao tại `C:/Users/PC/Downloads/du_an_nem_bui/133_cool_food_lite`.

| File | SHA256 |
|---|---|
| C01 | `0D33D8F8CC1CAD8BD18CEC2F1E6D1EC8EE1C745073B0DE955523D278EA139EA0` |
| C02 | `A1246B66AD90BE670B76943C8EF1E4C894D926ECC4F3D3BA45F9B316FE3DAFAB` |
| C03 | `758D41E9F65E54EF830F386595C66500D81B3147C063EF178EF4D985BB065433` |

ffprobe: cả ba 720×1280, 24 fps, 8 giây, có luồng âm thanh. ffmpeg giải mã toàn file không lỗi, mã thoát 0. Số dư Flow 860 → 830, chênh lệch 30 khớp báo giá. Trần thử mới 400, đã dùng 220, còn 180. Khoản Quality 100 không dùng. Sau thử trả x3 về x1, không gửi thêm. Bằng chứng screenshot `settings.png`, `preflight.png`, `results.png`; review tại 134.
