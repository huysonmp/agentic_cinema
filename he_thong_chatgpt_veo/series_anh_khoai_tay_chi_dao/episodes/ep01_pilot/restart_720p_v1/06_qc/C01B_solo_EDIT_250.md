# REC250 — Đóng góp EDIT cho coverage BM solo

Phạm vi: khuyến nghị dựng trên giấy; không phải final độc lập hoặc media PASS. Ảnh v2 còn chờ owner duyệt.

- Nối 1, C01A → BM: dùng C01A đã chọn 3,375 giây; kiểm nguồn thật ở out/in về trục Khoai trái–Đào phải, hướng nhìn, ánh sáng và đạo cụ thấy được. Cận solo phải giữ đủ mặt/miệng Khoai.
- BM phải chứa trọn tiếng “Khoan.” cùng khẩu hình thực của Khoai đang nhìn thấy, từ onset đến hết âm; chọn cả khoảng vào/ra tự nhiên sau khi nghe native. Không cắt mất đầu/cuối từ hoặc chuyển phần lời sang mặt khuất.
- Nối 2, BM → BR: trở về góc bàn gốc để thấy Đào nghe, nâng mắt, buông rồi thu tay; đối chiếu trạng thái tiếp xúc và thứ tự hành động bằng nguồn thật. Tay Đào ngoài khung BM là UNKNOWN, không chứng minh giữ contact.
- BR_START giữ exact A80 (`0cf422f2b28dae631785af6ec19fc7488800c0cf8d22bb95dddd04e1b7ae2acb`); đây là mốc cần kiểm với BM out, không bảo đảm nối đã khớp.
- Nối 3, BR → C02: BR phải hoàn thành buông–thu trước trạng thái C02F0 (`c59ad1e436ad42e7525c564a883269ef9f80288f4c76b675e64bba1798500cad`); kiểm tay, gaze, đạo cụ và âm nền qua cut thật.

A 3,375 + C02 7,541667 = 10,916667 giây. Tổng chuỗi = 10,916667 + BM_selected + BR_selected; BM/BR selected ranges và timing vẫn UNKNOWN tới khi có native. Request BM 4 giây không bắt buộc sử dụng hết 4 giây. EDIT chỉ khóa EDL sau kiểm nguồn/range thực; không tự giảm lời đoạn sau để ép 30 giây.

Xung đột giấy thiết yếu: chưa thấy giữa brief và prompt. Prompt chỉ giữ đạo cụ thấy được ở cận, phù hợp giới hạn coverage; “both hands resting” mô tả tay Khoai, không xác nhận tay Đào. Việc BM không thấy Đào chỉ chuyển kiểm continuity sang hai cut và BR.

Không crop caption, freeze, overlay miệng khép/ghép voice hoặc che lỗi bằng món. Native lỗi thì HOLD, không auto retake, không dùng lượt BR làm retry. Approval still/nguồn/giọng cũ không chuyển sang native mới; BM đạt dependency mới cho xét BR, và bản nối thật vẫn cần nghiệm thu riêng.
