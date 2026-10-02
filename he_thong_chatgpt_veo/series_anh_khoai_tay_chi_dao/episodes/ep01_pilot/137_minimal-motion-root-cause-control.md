# Đối chứng tối giản để truy lỗi hơi trắng

Ngày: 2026-10-02. Owner đồng ý thực hiện và lưu kinh nghiệm. Trạng thái lúc đăng ký: CHƯA GỬI, CHƯA CÓ KẾT QUẢ.

## Phạm vi

Giữ START OPEN7, END trống, Veo 3.1 Lite, Frames, 9:16, 720p, 8 giây; ba đầu ra cùng prompt, tối đa 30 credit trong 150 credit còn lại. Không Quality, không API, không thay canon hoặc kịch bản. Đọc lại UI model, giá và số dư trước gửi. Không lấy ngân sách Quality 100 riêng.

Đây là control mới cho các phép thử tăng từng lớp, không là so sánh một biến với 135: bỏ cả nhóm mô tả món, tên, động tác tay và câu cấm. Không thể quy thay đổi kết quả cho riêng từ steam. Chưa thay ảnh/crop bỏ nhân vật. Hướng dẫn chuyên môn đã đọc ngày 2026-10-02: Google khuyến nghị image-to-video tập trung chuyển động, tránh mô tả lại ảnh: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/video/best-practice. Khuyến nghị không bảo đảm hiệu quả cho Flow Lite; prompt chính không phải trường negativePrompt API.

## Prompt nguyên văn control M0

```text
Locked tripod shot for eight seconds. Both subjects hold their starting poses with relaxed closed mouths and resting hands. They blink naturally once. The table setting remains stationary. Quiet street ambience.
```

M0 cố ý không nhắc nhiệt, mùi/chảo, hơi/khói hoặc tên nhân vật. Đây là phép kiểm nền, không là cảnh diễn xuất cuối.

## Giả thuyết và tiêu chí

- H1: nhóm mô tả/cấm phức tạp góp phần vào hơi. Nếu M0 giảm hơi, chỉ hỗ trợ giả thuyết cấp nhóm, chưa xác nhận từ gây lỗi.
- H2: diễn xuất tiếp cận món góp phần. M0 bỏ hành động tay; muốn tách H1/H2 phải thêm lại đúng một lớp ở vòng sau.
- H3: ảnh/ngữ cảnh hoặc đặc tính sinh video có thể tạo hơi ngay cả với M0. Nếu có hơi, chưa loại H1/H2 nhưng chúng không đủ giải thích lỗi.
- R03 lịch sử chỉ là tham chiếu có giới hạn, không control cùng thời điểm/seed. Không dùng ba mẫu để ước lượng tỷ lệ lỗi chung.

Kiểm vệt hơi riêng với tay, miệng, chữ, mặt/món, camera. Lưu file/hash/giải mã và 16 ảnh mẫu mỗi clip; không thấy lỗi trong mẫu chỉ ghi chưa thấy. Nếu cần xác nhận sạch toàn clip phải xem liên tục. Nếu lỗi âm thanh: giữ bằng chứng, không tự coi request thất bại là hình lỗi. Cấu hình trả video câm chỉ đổi khi ghi riêng và không dùng so audio hay voice.

## Nhật ký và bước kế

Chờ kiểm UI và gửi. Dừng sau bộ ba để đánh giá. Chưa chạy các treatment thêm trạng thái món nguội, hành động hoặc thoại. Mọi bài học phải ghi kết quả thực, không ghi thành công trước thử.

## Thực thi và trạng thái mới nhất

Đã gửi đúng M0 một request x3 ngày 2026-10-02. UI xác nhận Veo 3.1 Lite, Khung hình, 9:16, 720p, 8 giây, START có OPEN7, END trống, giá 30. Ba ô mới cùng tên `Subjects holding poses at table` xuất hiện đầu lưới. Không đổi tùy chọn phục hồi âm thanh trong vòng này; chưa đọc lại switch đó, không coi trạng thái lịch sử là kiểm chứng mới.

Số dư đọc trực tiếp trước/sau: 800 → 770, ròng 30. Trần thử 400, tổng đã dùng 280, còn 120. Quality 100 vẫn giữ riêng, chưa dùng. Không gửi thêm request sau bộ ba.

Sau đối soát đã trả số lượng về x1, UI giá 10; không gửi thêm. Lần thử tiếp theo vẫn phải chọn x3 và kiểm lại đầy đủ cấu hình trước gửi theo quy ước test ba mẫu.

M01 là ô thứ nhất của bộ mới; trang chi tiết: https://flow.google.com/u/1/project/9276788e-9781-44fb-ba5b-083006667374/edit/7fd4e397-b1a0-4904-a7e1-59b66855676d. Trang hiện tổng thời lượng 8 giây và phát được xem trước; ảnh UI lưu khoảng 4 giây. M02/M03 chỉ xác nhận ô đã tạo, chưa thu ID riêng.

**DOWNLOAD_UNRESOLVED / QC_PENDING:** tải M01 từ lưới hai lần và từ chi tiết một lần chưa có MP4 mới trong Downloads. Theo dõi sự kiện tải lần hai hết 45 giây không có sự kiện. Xuất các tài nguyên video đã quan sát bằng chức năng trình duyệt cũng lỗi fetch, không có file. Không dùng URL ký tạm để tải bằng shell hoặc lưu vào Git. Không chứng minh lỗi tải nằm ở Flow, browser hay mạng; chưa có bằng chứng phân biệt. Không tự tạo lại để chữa lỗi tải.

Bằng chứng local: `D:/Workspace/agentic_cinema/artifacts/opening137-r1/preflight.png`, `generated-three.png`, `M01-preview.png`. Chưa có native MP4, hash, giải mã, contact sheet, nghe âm thanh hoặc review độc lập. Ảnh xem trước nhỏ không đủ kết luận có/không hơi trắng. H1/H2/H3 vẫn UNRESOLVED, không production PASS.

Bước tiếp: lấy đủ ba file gốc, đối soát từng file với ô mới; sau đó kiểm 16 mẫu/clip và xem liên tục trước chọn control. Nếu owner tải được, đặt file theo thứ tự ba ô vào folder bàn giao, ghi tên gốc để tránh nhầm với các lượt cũ. Chưa thêm lớp prompt khi control chưa được kiểm.
