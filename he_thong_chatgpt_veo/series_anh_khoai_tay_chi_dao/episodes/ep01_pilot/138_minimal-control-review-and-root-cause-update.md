# Review đối chứng M0 và cập nhật truy nguyên nhân

Ngày: 2026-10-02. Root thực kiểm file và ảnh mẫu; không gọi đây là review độc lập của các agent. Gói đăng ký và prompt nguyên văn ở 137.

## Thu nhận và kỹ thuật file

Đã tải đủ M01/M02/M03 qua tab IAB mới. M02 và M03 dùng cùng tab đã tải được M01, menu tải 720p bản gốc; chỉ chuyển mẫu khi file trước hiện hữu. Không tạo media mới hoặc tiêu thêm credit. Số dư lần đọc gần nhất 770, ngân sách thử còn 120; chưa đọc lại số dư trong lượt chỉ tải.

Folder bàn giao: `C:/Users/PC/Downloads/du_an_nem_bui/137_minimal_motion_control`. Cả ba video 8 giây, 720×1280, có stream audio/video; giải mã ffmpeg exit 0. M02/M03 24 fps. Có audio stream không chứng minh âm thanh đúng yêu cầu.

| Mẫu | Asset ID | Tên file gốc trong Downloads | Byte | SHA-256 |
|---|---|---|---:|---|
| M01 | 7fd4e397-b1a0-4904-a7e1-59b66855676d | Subjects_holding_poses_at_table_20261002151930.mp4 | 1939066 | 2B7FE619034F0B365BCD32B9E3EDB1B2695FD4A7C46CE5D38ED4F92FC80F52D7 |
| M02 | 85067d39-6473-4b8c-958c-f017f5399ba5 | Subjects_holding_poses_at_table_20261002153136.mp4 | 2160807 | 658BDD5974EC3B616C7A4199E3968B335ED6A67D0D5612E74E45043F97565E1D |
| M03 | 6b7d6d5d-c1d0-498f-81b0-0a401f7bee15 | Subjects_holding_poses_at_table_20261002153216.mp4 | 2092436 | EB4C7F5D498A95A7B3387703F180F95EAD5D57198228C430369F5B27A49C69DB |

## Quan sát ảnh mẫu

Root xem 16 khung mỗi clip, lấy mỗi 0,5 giây từ 0 đến 7,5. Bằng chứng `artifacts/opening137-r1/M01-sheet.png` đến `M03-sheet.png`, cũng có trong folder bàn giao. Thời điểm dưới đây là nhãn mẫu xấp xỉ, không là thời điểm bắt đầu/kết thúc chính xác của lỗi.

| Mẫu | Hơi bốc từ đĩa nem | Tay và miệng trái yêu cầu giữ tư thế | Bàn/camera/chữ |
|---|---|---|---|
| M01 | Chưa thấy trong 16 mẫu | Đào mở miệng và giơ tay khoảng 0,5–3,5 giây; Khoai mở miệng, giơ tay khoảng 7–7,5 giây | Bố cục và đồ trên bàn tương đối giữ; chưa thấy chữ thêm ngoài watermark |
| M02 | Chưa thấy trong 16 mẫu | Khoai mở miệng, giơ hai tay khoảng 0,5–2 giây và giơ tay cuối clip; Đào cũng mở miệng/diễn tay | Bố cục và đồ trên bàn tương đối giữ; chưa thấy chữ thêm ngoài watermark |
| M03 | Chưa thấy trong 16 mẫu | Khoai mở miệng, giơ tay khoảng 0,5–2 và 7–7,5 giây; Đào diễn tay ở giữa clip | Bố cục và đồ trên bàn tương đối giữ; chưa thấy chữ thêm ngoài watermark |

Ánh sáng ấm vẫn gần ảnh nguồn, chưa có lỗi ánh sáng rõ trong mẫu. Không xem ảnh đèn ấm là bằng chứng món nóng. Phông phố có chuyển động; không quy mọi chuyển động nền là lỗi. Chưa kiểm toàn bộ chuyển động liên tục, nghe thật, thoại tự sinh, lip-sync, food texture chi tiết hoặc review độc lập. Không khẳng định clip sạch khói toàn thời lượng.

**Kết luận:** FILE_TECHNICAL_OK / STEAM_NOT_OBSERVED_IN_SAMPLES / POSE_REWORK / NO_PRODUCTION_WINNER. Ba clip dùng làm bằng chứng chẩn đoán, không thay cảnh chính thức. Chưa nâng Quality.

## Truy nguyên nhân: đã biết và chưa biết

1. Hơi trong các bộ trước không thể kết luận là do ảnh OPEN7 bắt buộc chứa hơi: cùng ảnh đã sinh bộ M0 chưa thấy hơi trong mẫu. Đây là phản chứng cho nhận định tuyệt đối, không loại ảnh/ngữ cảnh khỏi yếu tố góp phần.
2. Giả thuyết nhóm prompt phức tạp/hành động ảnh hưởng đến hơi được hỗ trợ sơ bộ bởi khác biệt 135 và 137. Tuy nhiên nhiều nhóm cùng bị bỏ, cấu hình phục hồi âm thanh khác và thời điểm/seed không ghép cặp. Không đủ quy lỗi cho từ `steam`, lời thoại hay một động tác riêng.
3. Bỏ hành động yêu cầu không loại được cử chỉ tự sinh: cả ba M0 vẫn mở miệng/giơ tay dù yêu cầu giữ tư thế. Đây là lỗi tuân thủ quan sát được trong bộ này; nguyên nhân cơ chế còn mở. Không chứng minh đó là lời nói vì chưa nghe audio.
4. Lỗi tải tách khỏi lỗi hình: tab mới tải đủ ba file. Biện pháp phục hồi được kiểm chứng cho bộ này, nguyên nhân tab cũ chưa xác định. Không suy diễn cache/token khi chưa có đối chứng.
5. Nguyên nhân tạo hơi còn UNRESOLVED; vấn đề thiết kế phép thử đã rõ: sửa nhiều lớp cùng lúc làm mất khả năng truy riêng từng yếu tố. Quy trình sửa phải bổ sung kiểm soát biến và đọc lại actual input, không chỉ thêm câu cấm vào cuối prompt.

## Bước tiếp được đề xuất, chưa gửi

Ưu tiên kiểm xem liên tục/nghe ba file, rồi một phép thử bổ sung đúng một nhóm: giữ nguyên M0 và chỉ thêm câu cấm từ 135: `No steam, smoke, vapor, heat shimmer or animated scent trails rise from the food.` Không thêm tên món, nhiệt độ, động tác, thoại hay camera. Ba mẫu Lite tối đa 30 trong ngân sách hiện có; đọc lại model/START/END/audio recovery/giá trước gửi. Đây là đối chứng câu cấm trong prompt chính Flow, không là negativePrompt API.

Nếu hơi xuất hiện trở lại, giả thuyết câu cấm góp phần được hỗ trợ nhưng cần tái lập M0 cùng phiên để giảm nhiễu; nếu không, chuyển kiểm nhóm hành động/mô tả ở phép thử riêng, không cộng tất cả lại ngay. Dù kết quả khói tốt, cổng diễn xuất vẫn chưa đạt. Chưa chạy phép thử này trong lượt tải/review; không tự sửa canon hoặc công bố nguyên nhân đã xác nhận.
