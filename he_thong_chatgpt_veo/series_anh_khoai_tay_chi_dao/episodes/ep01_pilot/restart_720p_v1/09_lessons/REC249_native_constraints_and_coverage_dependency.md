# REC249 — Nguồn thật chặn dependency, không sửa bằng ghép

## Điều đã xác định

Owner duyệt gói BM→BR, tối đa hai output / 30 credit, từng lượt x1 và không automatic retry. Root chọn đúng saved K20 từ catalog và đối soát full prompt/config. Reviewer độc lập paper đọc bốn hồ sơ; root đọc đầy đủ báo cáo trước một click BM. Một output 7 credit được tạo, tải native 720p bằng listener đăng ký trước click; ba bản download/repo/archive cùng hash `33ccb60ce91eac26620040944811d16e6f566ee3110aef2a15d5b5f4d880f60a`.

Native 720×1280, 96 khung hình ở 24 fps; video 4 giây, tiếng 4,01 giây, giải mã đủ. Đã trích toàn bộ 96 khung và audio. Root xem hai bảng ảnh lấy mẫu 6 fps, tổng 24 mẫu, ảnh tham chiếu và F0. Reviewer độc lập xem ảnh tham chiếu, các bảng ảnh và thêm F0/F12/F36/F40/F60; root đọc đầy đủ báo cáo. Đây không phải nghe/xem AV liên tục hoặc chứng nhận lip-sync.

Mặt/khẩu hình Khoai rõ và hai tay nghỉ trong mẫu. Nhưng chữ “Khoan” đã burn-in vào native quanh đoạn mở miệng; Đào nhìn lên từ F0 thay vì xuống, rồi đổi gaze và hạ tay hover. Không có range được chứng minh vừa sạch chữ vừa đủ lời. Nguồn không được chọn; BR chưa gửi. Contact tay ngoài khung vẫn UNKNOWN.

## Truy nguyên đúng mức bằng chứng

- Hai lỗi đã nằm trong file native tải trực tiếp, trước mọi cắt/ghép. Không đổ cho editor, Canva, download hoặc proxy720.
- Prompt live trùng file và đã cấm lettering/Đào nhìn lên/thu tay. Vì vậy không phải do root vô tình gửi prompt cũ hoặc bỏ các điều kiện này; model không thực hiện đầy đủ điều kiện ở output này.
- Ingredients đã diễn giải lại pose ở F0 trong lượt thực này. Không coi ảnh reference và câu giữ nguyên là chứng cứ đã khóa first frame.
- Chưa có bằng chứng một cụm từ cụ thể, dấu ngoặc kép, voice performance hoặc cơ chế provider là nguyên nhân duy nhất gây caption/gaze. Không ghi phỏng đoán thành kết luận.
- Tách nhiệm vụ nói và thu tay đã giảm việc cần diễn đồng thời, nhưng BM vẫn chứa phần Đào nhìn thấy và yêu cầu giữ gaze/hover. Giả thuyết thiết kế còn mở: speaker coverage chỉ Khoai có thể loại mâu thuẫn gaze nhìn thấy trong BM, không tự chứng minh contact ngoài khung hoặc chất lượng BR.

## Đối soát công cụ

Chip mới không lộ UUID; lựa chọn đúng custom được đối soát bằng unique saved-name/performance, UUID chỉ mapping SoT. Không có toggle Agent trong composer hiện hành; direct-generate không được ghi thành đọc live OFF. Hai giới hạn được ghi trước submit, không dùng để tự duyệt tiếng.

Khảo sát UI Frames sau review: có ô Bắt đầu/Kết thúc; cấu hình vẫn là Omni 1.1 Flash, 720p, dọc, 4 giây, x1, giá 7 credit khi trống. Composer Frames không hiện nút thêm ingredient/voice như Ingredients. Chưa chứng minh có tuyến Frames kèm custom K20 hoặc đường chuyển động không lời đúng. Không đề xuất chuyển BM sang Frames rồi hứa vẫn giữ K20 khi chưa có cách thao tác thực. BR không lời vẫn cần kiểm đầy đủ đầu vào và đầu ra.

Tải xuống đã thành công ngay; không lặp tải hoặc tạo video chỉ vì thiếu file. Số dư tài khoản 1.006→999; dự án đã chi 81/500 credit, còn 419 gồm 309 đã phân bổ và 110 dự phòng chưa mở. Đợt quay này đã dùng một đầu ra, 7 credit; còn 23 credit trong trần 30, nhưng quyền tối đa hai đầu ra không đồng nghĩa được thêm cả BM sửa và BR thành đầu ra thứ ba.

## Quyết định đã chốt và phần còn mở

Giữ C01A/C02 đã chọn, toàn bộ nguồn, giọng và lời canon; không crop chữ, freeze, thêm voice lên môi khép hoặc chạy BR để che nguồn không đạt. Không chuyển approval giọng cũ sang output mới. Không hỏi owner hợp thức hóa hình sai như toàn phim đã đạt.

Đề xuất chưa duyệt: đổi BM thành cận riêng Khoai, Đào hoàn toàn ngoài khung; tạo reference mới để owner duyệt trước video. Phản ứng Đào chỉ diễn/kiểm ở BR góc bàn gốc. Giữ K20 và kiểm tiếng output mới thực tế; diễn giải spoken word là audio, clean cinematic plate không chữ, nhưng không cam kết prompt mới hết caption.

Bước tiếp cần một quyết định phạm vi: cho đổi cỡ cảnh và ảnh tham chiếu BM, rồi mở tối đa hai đầu ra tiếp theo (BM sửa và BR chỉ nếu đạt), tổng đợt vẫn không quá 30 credit, thêm không quá 23 credit, mỗi đầu ra không quá 15 credit, x1. Giá hiện tại 7 credit chỉ là tham khảo. Đây là mở số đầu ra từ hai thành tối đa ba cả đợt, không tự coi đã duyệt. Sau khi ảnh mới, preflight độc lập và cổng live mới được chốt mới gửi lượt tạo. Chưa có đoạn được chọn, nghe thực, kiểm điểm nối thực hoặc approval toàn phim.
