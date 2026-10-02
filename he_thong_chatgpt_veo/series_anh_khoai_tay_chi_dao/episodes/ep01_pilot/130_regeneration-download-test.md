# EP01 — tạo lại Lite để kiểm đường tải

Ngày: 2026-10-02. Trạng thái: ĐÃ TẠO VÀ NHẬN ĐỦ BA FILE / KIỂM KỸ THUẬT ĐẠT / CHỜ REVIEW NỘI DUNG.

Chủ dự án báo tải vẫn Stopped và yêu cầu tạo lại video rồi thử tải. Áp dụng quy định governance 08: bộ ba Lite, giữ nguyên ảnh OPEN7 và prompt 126, không sửa lời/staging. Đây là thử giả thuyết tài sản mới có tải được, không chứng minh nguyên nhân lỗi cũ.

Giới hạn: 3 × 10 = 30 credit, Veo 3.1 Lite, Frames, START OPEN7/END trống, 9:16, 720p, 8 giây. Thực hiện một yêu cầu **x3 đầu ra**: giao diện đã xác nhận giá 30; không phải ba lần gửi x1 như bộ 127. Cùng prompt và ảnh cho ba mẫu, không sửa biến giữa các mẫu. Trước thử số dư UI 890, ngân sách thử cũ dùng 160/200. Nếu đủ ba mẫu, dự kiến 190/200; không dùng khoản Quality 100 hay V02. Không gửi thêm yêu cầu hoặc tạo mẫu thứ tư. Bằng chứng: `artifacts/opening130-r1/settings.png`, `preflight.png`.

Input: `C:/Users/PC/Downloads/du_an_nem_bui/T2-CODEX-OPEN_v0.7.png`, SHA256 `A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A`. Prompt nguyên văn ở `126_opening-dialogue-action-lite-request.md`.

| Lượt | Thời điểm / mã | Kết quả tạo | File local / hash | Tải thử |
|---|---|---|---|---|
| N01 | `784f476a-86e1-409a-8528-17f42510f2ee` | Đã tạo | `N01.mp4`, 2.658.700 byte | Đã nhận local, 11:27:08 |
| N02 | `e513a108-9bb6-44ad-b96e-0c22c1ba1dc6` | Đã tạo | `N02.mp4`, 2.368.394 byte | Đã nhận local, 11:28:03 |
| N03 | `ac29077a-d73b-4f72-83cb-2674e3ae785d` | Đã tạo | `N03.mp4`, 2.584.231 byte | Đã nhận local, 11:28:55 |

Cả ba cùng yêu cầu gửi 11:24:17 giờ Việt Nam. URL mỗi clip: `https://flow.google.com/u/1/project/9276788e-9781-44fb-ba5b-083006667374/edit/` cộng mã ở bảng.

## File và kiểm kỹ thuật

Đã lưu trong `artifacts/opening130-r1/N01.mp4` đến `N03.mp4`, bản bàn giao ở `C:/Users/PC/Downloads/du_an_nem_bui/130_regeneration_lite/`. Giữ nguyên file tải, không re-encode hoặc bỏ watermark.

| File | SHA256 |
|---|---|
| N01 | `88F11EE821581FF17C3FEF158305FBA5E4C658B0BD43ADA7B63C755393566503` |
| N02 | `732FC30252EA11760904CEFCF17CD5877CA4D2A9BF33E8D85DC7DE093529FAF8` |
| N03 | `3FDAC619BD4B2411119AF6FF8E9425CA0C41571DF68C9E1D7E0622CD450B8E6A` |

ffprobe: cả ba có video 720×1280, 24 fps, thời lượng 8 giây và luồng âm thanh. ffmpeg giải mã toàn file, không báo lỗi, mã thoát 0. Đây là kiểm kỹ thuật, **không duyệt thoại, giọng, diễn xuất, tay/đạo cụ, đồng bộ môi hoặc điểm nối**. Chưa chạy ASR hay review độc lập trong vòng này.

## Kết quả thử tải và ngân sách

Đường thực hiện: thư viện → menu thẻ của từng clip mới → Tải xuống → 720p kích thước gốc. Sau mỗi clip giữ nguyên tab, chờ và kiểm file thực tế rồi mới chuyển sang clip tiếp theo. Bấm menu ngữ cảnh N01 theo index ban đầu có lỗi xác định phần tử; đã đọc lại AX/screenshot và dùng nút Tuỳ chọn khác trên đúng thẻ, không gửi generation lại. Nhận được các file Downloads:

- `Friends_talking_during_casual_meal_20261002112707.mp4` → N01.
- `Friends_talking_during_casual_meal_20261002112802.mp4` → N02.
- `Friends_talking_during_casual_meal_20261002112854.mp4` → N03.

Số dư trực tiếp trước/sau: 890 → 860, chênh lệch 30, khớp báo giá x3. Ngân sách thử cũ cập nhật 190/200, còn 10 theo hồ sơ; không dùng Quality 100. Đã trả cấu hình từ x3 về x1 sau khi hoàn tất để tránh gửi nhầm bộ ba lần sau; không bấm tạo thêm. Bằng chứng: `download-n01.png`, `three-new-results.png` trong `artifacts/opening130-r1`.

Đã xác định: bộ mới có đủ file tải local đọc/giải mã được. Đã chốt: dừng generation tại ba mẫu. Giả thuyết còn mở: vì sao lượt cũ Stopped; lần này thành công không chứng minh tạo lại là cách sửa tổng quát. Tiếp theo: xem/nghe, đối chiếu ba mẫu và chọn hướng sửa; không tự mở Quality.

Không xóa hay thay thế bộ 127. Chỉ xác nhận tải thành công khi file hiện hữu, đúng metadata và giải mã được; thông báo Flow không đủ. Nếu tải lại vẫn dừng, giữ clip mới và ghi lỗi, không tự tạo tiếp. Quality và review chất lượng vẫn HOLD.
