# REC249 — Đối soát cổng live BM

Owner đã duyệt gói REC248 và tối đa hai đầu ra / 30 credit, tuần tự BM trước BR. Chưa bấm tạo tại thời điểm ghi bản này.

## Bằng chứng hiện hành

- Đúng project EP01 720p v1, tài khoản owner xác nhận; số dư trước lượt là 1.006.
- Một ảnh BM đã xử lý, cloud ID `767d2cb9-2d1e-457c-a8a1-42261428fcfb`; hash local giữ nguyên.
- Chọn một mục custom `EP01_Khoai_K20_Orus_720p_v1` từ catalog có tên và toàn bộ performance đã đọc. Không chọn base Orus hoặc D06.
- Prompt file 249 được đọc lại từ ô nhập, trim bằng nhau. Cấu hình cuối Omni 1.1 Flash, Ingredients, 720p, 9:16, 4 giây, x1, quote 7 credit; screenshot lưu ở request manifest.
- Watermark vùng được yêu cầu, bật và không thể tắt; không thay đổi.

## Hai giới hạn giao diện, không biến UNKNOWN thành PASS

Chip custom voice mới không hiện UUID. ID K20 trong SoT là mapping đã có, không phải ID vừa đọc live. Root dùng lựa chọn từ catalog theo tên unique và performance làm bằng chứng chọn đúng custom; đây không phải bằng chứng đã nghe output. Nếu output khác giọng, HOLD, không dùng approval take cũ.

Composer và bảng cài đặt hiện không có toggle Agent. Root bấm direct-generate với đầu vào đã chốt, không khởi tạo agent workflow. Không ghi “đã đọc Agent OFF”. Điều này chỉ đối soát cách thực thi hiện có, không mở quyền dùng agent tự chi hoặc tool/model mới.

Hai điểm trên cập nhật cách thu bằng chứng live của brief248 cho UI hiện hành, không gỡ bất kỳ cổng media/voice/join nào. Không truy tìm state nội bộ hoặc API để giả lập ID. Independent preflight và review nguồn thực vẫn bắt buộc.

## Dependency giữ nguyên

BM cần Khoai nói trọn “Khoan”, mặt rõ, tay nghỉ; Đào chưa nâng mắt/buông/thu trong range chọn. Contact ngoài khung UNKNOWN. BR chỉ chạy sau nguồn BM phù hợp và cổng tiếng có capability/owner kiểm; dùng đúng A80→C02F0, không reset phản ứng đã xảy ra.
