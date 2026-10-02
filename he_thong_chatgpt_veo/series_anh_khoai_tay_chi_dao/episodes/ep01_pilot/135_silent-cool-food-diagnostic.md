# Phép thử tách hình và hành động: nem nguội

Ngày: 2026-10-02. Chủ dự án đồng ý hướng thử sau biên bản 134 bằng “ok”. Đây là chẩn đoán kỹ thuật, không thay lời thoại hoặc kịch bản chính thức.

## Gói và tiêu chí

- Một yêu cầu tạo ba đầu ra cùng prompt: Veo 3.1 Lite, 720p, 8 giây, dọc 9:16.
- START: T2-CODEX-OPEN_v0.7.png đã có trong Flow; END để trống.
- Tạm bỏ toàn bộ lời thoại, diễn giọng và mô tả mùi/chảo. Giữ món nguội, bố cục, hai nhân vật và hành động tay trái Đào.
- Chi phí dự kiến 30 credit, trong 180 credit thử còn lại. Chưa mở Quality.
- Kiểm hơi/khói trên món, tay trái/phải, chuyển động đĩa, đạo cụ, chữ tự sinh và hình thể. Có hơi/khói là loại về tiêu chí món nguội.
- Đây không phải phép thử một biến duy nhất: cả lời thoại và mô tả diễn thoại đều bỏ. Nếu kết quả khác bộ 133, chỉ có thể khoanh vùng tổ hợp điều kiện, chưa chứng minh nguyên nhân riêng lẻ.
- Review ban đầu bằng khung hình lấy mỗi 0,5 giây; thiếu review liên tục và nghe thật phải được ghi rõ. Không coi không thấy trong ảnh mẫu là bảo đảm toàn clip sạch lỗi.

## Prompt nguyên văn

```text
Use the supplied starting image for one continuous eight-second visual-and-action diagnostic. A locked tripod holds the starting composition throughout. The adult potato man Khoai is seated on screen left; the adult peach woman Dao is seated on screen right. They are friends having a casual meal.

The plate contains ready-to-eat Nem Bui served cool at room temperature. The space above the food stays transparent, clear and still throughout. No steam, smoke, vapor, heat shimmer or animated scent trails rise from the food.

Both characters remain silent with closed, relaxed mouths. Dao looks at Khoai with friendly curiosity and a small teasing smile. In the middle of the shot, she slowly reaches ONLY her left hand toward the near-right edge of the shared food plate, then pauses before touching it. Her right hand remains resting near her own bowl. The shared plate stays motionless on the table. Khoai watches her with a subtle change of eye direction while both his hands stay resting in their original positions.

Keep the food plate, herb plate, both sauces, both eating bowls, both resting chopstick pairs and water glass in the frame. Apart from Dao's small left-hand reach and natural blinking, preserve the table layout and object positions. Neither person picks up chopsticks or the glass, eats, drinks, transfers food, lifts or pulls the plate. Preserve the reference faces, clothing, food appearance, warm lighting and background. No camera move, zoom, cut, smoke, steam, vapor, heat shimmer, animated scent trails, added text, captions, speech, narration or music. Only quiet street ambience. Preserve the native output watermark.
```

## Nhật ký

- Gửi bộ x3 lúc 12:36:28 giờ Việt Nam. Cấu hình và giá 30 credit được đọc từ giao diện, lưu `artifacts/opening135-r1/settings.png`.
- Cả ba báo “Không tạo được âm thanh” và “Bạn chưa bị tính phí cho lượt tạo này”. Không có đầu ra để đánh giá hình; không quy lỗi dịch vụ này thành lỗi khói hoặc bằng chứng đạt.
- Bật tạm tùy chọn Flow “Trả về video không có âm thanh” (ban đầu tắt), rồi bấm Thử lại một lần cho từng thẻ lỗi; hoàn tất ba thao tác lúc 12:39:01. Prompt không đổi. Đây là thay đổi cấu hình phục hồi, không phải sửa kịch bản. Không xóa thẻ hoặc dữ liệu.
- Ảnh lỗi lưu `artifacts/opening135-r1/audio-failure.png`. Chờ đối soát kết quả và số dư trước khi ghi chi phí thực tế.
- SHA-256 ảnh START: A3D80F09BFB7242BAE3007AD7B4F37473BB2F0ED019A84CC4956C4D32A8DBF9A.

## Kết quả thực và lưu trữ

Ba thẻ phục hồi đã trả video, đều hiển thị “Chưa tạo âm thanh nào”. File gốc tải bằng menu Tải xuống → 720p Kích thước gốc, từng file một; chỉ chuyển sang file tiếp theo sau khi file trước xuất hiện trên ổ đĩa. Đây là ba yêu cầu lỗi được thử lại, không phải thêm ba yêu cầu x3.

| Mẫu, thứ tự từ trái sang phải trong lưới | Tên file gốc trong Downloads | Byte | SHA-256 |
|---|---|---:|---|
| S01 — Characters having a casual meal | Characters_having_a_casual_meal_20261002124039.mp4 | 2866098 | 5ADFB171A456329B4B34AC8602038B57F884770E09235C277FC34F465D396109 |
| S02 — Friends having casual meal | Friends_having_casual_meal_20261002124125.mp4 | 2620196 | B480DAD796A5F533A917CB9F7DB0D2B0D67A7AA84C9E5C9F4C348A5C6741F6C1 |
| S03 — Two friends having casual meal | Two_friends_having_casual_meal_20261002124155.mp4 | 2266670 | 5FEC05DF5A5D24CCC6D56B76E6CF870B5BD514AF3E9434364026ADF119B80FBF |

Bản local tại `D:/Workspace/agentic_cinema/artifacts/opening135-r1/S01.mp4` đến S03. Bản bàn giao để xem tại `C:/Users/PC/Downloads/du_an_nem_bui/135_silent_cool_food_lite`. Media không commit vào Git. Bằng chứng lưới kết quả: `artifacts/opening135-r1/results.png`.

Cả ba: 720×1280, 24 fps, 8 giây, chỉ có stream video; giải mã toàn file bằng ffmpeg không báo lỗi (exit 0). Kỹ thuật file đạt, nội dung cần sửa theo 136.

Số dư Flow sau bộ được đọc trực tiếp: 800. Đối chiếu số dư đã xác minh cuối bộ 133 là 830, chênh lệch ròng 30 credit; không thấy phát sinh thao tác tạo khác trong lượt này. Các yêu cầu lỗi ban đầu được UI báo không tính phí. Tổng ngân sách thử tích lũy 400, đã dùng 250, còn 150. Khoản Quality 100 riêng không sử dụng; không mua hoặc nạp thêm tài khoản.

Sau thử: trả “Trả về video không có âm thanh” về tắt, xác minh UI Value 0 và thông báo Flow sẽ chặn video lỗi âm thanh; trả cấu hình x3 về x1. Không gửi thêm yêu cầu. Các lần thử thoại sau phải kiểm âm thanh, không dùng cơ chế trả video câm để coi voice đạt.
