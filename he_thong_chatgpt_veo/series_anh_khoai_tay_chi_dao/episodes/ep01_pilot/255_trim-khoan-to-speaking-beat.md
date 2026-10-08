# 255 — Cắt gọn nhịp “Khoan”

## Yêu cầu và phạm vi

Owner: “cắt bớt khung hình dư thừa đi, có mẫu câu khoan thôi mà nhở”. Được cắt đầu/đuôi bản sửa áo REC254; không phải duyệt hình/giọng/khẩu hình, chọn BM chính thức hoặc mở BR. Không tạo video/giọng mới và không dùng Flow.

## Bản cắt để xem

- File: `restart_720p_v1/07_edits/C01B_KHOAN_SHORT_0p75S_T01_FOR_REVIEW.mp4`.
- SHA-256: `c6bbc9de803badf608f576f5dc47f126581db317434dcd92c00abd06698887bc`.
- Nguồn: `C01B_BM_T02_LOCAL_SHIRT_REPAIR_T01_FOR_REVIEW.mp4`, SHA-256 `cd4213d393798ca3baf45603a9c40215b7f08ffcf7091418238e183abb76b198`.
- Giữ F20–37, đánh số từ 0; khoảng nửa mở [20,38), tương đương 0,833333–1,583333 giây nguồn. Đầu ra 18 khung, 24 fps, 0,75 giây, 720×1280; bỏ 3,25 giây hình dư.
- Hình và tiếng cùng dịch gốc 0,833333 giây, không đổi tốc độ, âm lượng hoặc vị trí tương đối. Không thêm fade, khung đứng hoặc thoại.
- MP4 mã hóa lại H.264/AAC để cắt chính xác; tiếng đầu ra không bit-exact. Bản PCM đi kèm giữ đúng 36.000 mẫu stereo nguồn [40.000,76.000) ở 48 kHz để dùng khi dựng.

## Bằng chứng kiểm

Giải mã toàn file thành công. Root xem đủ 18 khung trên ba bảng đối soát có offset nguồn +20; giữ trọn mặt, nhịp miệng mở rồi khép, không thấy chữ trên áo. Bản PCM đi kèm bằng tuyệt đối lát nguồn; tương quan PCM của AAC xuất với lát nguồn, tại độ trễ 0, là 0,9992246982. Tương quan không phải nghe/nhận dạng lời hoặc chứng nhận khẩu hình.

Reviewer độc lập `/root/solo_critic_250` xem đủ 18 khung, xác nhận mapping +20, không thấy blocker hình; **GO_FOR_OWNER_SHORT_AV_CHECK**. Root đã đọc đầy đủ report `C01B_KHOAN_short_independent_255.md`. Trạng thái: `restart_720p_v1/06_qc/run-registry-255.json`. Evidence đầy đủ tại `C:/Users/PC/Downloads/du_an_nem_bui/255_KHOAN_SHORT/`; script tái lập kiểm nguồn: `scripts/check_ep01_khoan_trim_255.py`. Script QC chỉ chạy một lần trên thư mục mới, không ghi đè bằng chứng cũ.

## Chốt vòng và việc tiếp theo

- Đã xác định: chỉ cần nhịp “Khoan”, không giữ cả clip 4 giây.
- Đã chốt: được cắt local; chi thêm 0 credit. Dự án vẫn 108/500, còn 392; đợt coverage 34/34, reserve 110 đóng, BR chưa được phép chạy.
- Giả định làm việc: phạm vi F20–37 đủ bao chuyển động miệng và đuôi âm; chưa là range được owner chọn.
- Còn mở: owner nghe/xem đúng bản ngắn để xác nhận đủ “Khoan”, đúng Khoai/K20 và nhịp/khẩu hình/áo chấp nhận được. AI chưa nghe thực tế; không ghi FULL_AV_PASS.
- Tiếp theo: gửi bản ngắn; sau duyệt mới cập nhật lựa chọn BM và kiểm điểm nối thực với A/BR/C02. Không tự mở paid generation hoặc finishing cả phim.
