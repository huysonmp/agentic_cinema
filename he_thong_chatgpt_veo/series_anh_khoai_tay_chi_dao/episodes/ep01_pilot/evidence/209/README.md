# Bằng chứng 209 — sản xuất phần còn lại và ráp 30 giây

- `prompt-U01-v0.1.txt`, `prompt-U02-v0.1.txt`, `prompt-U08-v0.1.txt`: prompt thực, đã đối soát nội dung trong Flow.
- `*_preflight.png`, `*_completed.png`: cấu hình và kết quả Flow; không lưu bảng tài khoản.
- `U01_full_grid.png`: 4 mẫu/giây, nhãn là thứ tự mẫu, không phải frame native.
- `U01_S03_all33.png`: từng frame 146–178, trái sang phải, trên xuống dưới.
- `U02_full_grid.png`, `U08_full_grid.png`: 4 mẫu/giây, 8 cột × 4 hàng.
- `U08_first36.png`: từng frame 0–35, chưa gắp xong, không dùng cho cảnh kết.
- `U08_candidate66-101.png`: từng frame 66–101, 6 cột × 6 hàng, ứng viên có điều kiện.
- `timeline-v0.5.json`: bind frame/hash chính xác cho mười shot, không lặp nguồn, không dùng U03 REWORK.
- `AV_contact.png`: một mẫu/giây từ bản ráp 30 giây, 10 cột × 3 hàng.
- `AV_cut_boundaries.png`: native frame của bản ráp theo thứ tự: 337, 338, 370, 371, 511 / 512, 526, 527, 589, 590 / 625, 626, 683, 684, 719. Không phải bằng chứng xem động liên tục.
- `technical-report.json`: decode, 30 giây/720 frame, hash và bảo toàn PCM; không là creative/owner/SIA PASS.
- `results.json`: đối soát ba lượt, số dư 57; sổ 419/422/còn 3; ngoại lệ và gate.

Native và bản ráp nằm trong folder owner, không đưa video lớn vào Git. Chưa phụ đề, nhãn món/địa phương, thông báo AI, ambience/final mix. Xem `../../209_approved-coverage-production.md` cho phạm vi duyệt và các vấn đề còn mở.

## Kinh nghiệm thao tác và nguyên nhân lỗi

Download event có thể timeout sau 20 giây dù file native đã được tải xuống. Lượt này U02/U08 đều có file mới trong Downloads sau khi bấm 720p một lần; đối soát tên/thời điểm, hash/probe/decode trước khi sao lưu. Không bấm tải liên tục, không tạo lại chỉ vì event timeout.

Chỉ dẫn “xong trong 1,3 giây” không khóa được thời gian diễn trong lượt này. U08 mất hơn ba giây mới gắp; phải kiểm timeline thực, không chọn mù 36 frame đầu. Bản xem dùng đoạn gắp sau, ghi rõ temporal ellipsis chứ không giả vờ đạt chỉ đạo ban đầu. Cốc trượt đã có trong native U01, không do assembler. Giả thuyết cần kiểm chứng nếu sửa sau: prompt khóa cốc ở trên bàn nhưng chưa nói rõ giữ nguyên tọa độ; chưa có thử nghiệm đối chứng để kết luận đây là nguyên nhân duy nhất.

Assembler kiểm hash/range/khoảng trống/tái sử dụng và PCM giúp ngăn dùng nhầm nguồn/tiếng; không thể tự xác nhận giọng đúng vùng miền hoặc cảnh hấp dẫn. Root review hiện tại là kiểm ảnh mẫu và điểm cắt, không mang danh agent độc lập.
