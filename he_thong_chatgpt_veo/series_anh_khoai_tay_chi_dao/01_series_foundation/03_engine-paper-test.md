# P1 Engine — paper stress test

- **Version:** P1-Test-v0.1
- **Status:** SUPERSEDED FOR P1 DECISION; lưu làm tư liệu về engine thử món cũ, không phải script hoặc test khán giả
- **Lý do:** owner chỉ ra engine này nghiêng về review. Series cần thể hiện các góc nhìn xưa–nay, truyền thống–hiện đại, cởi mở–kén chọn, hợp–chưa hợp, riêng–chung. Ba case dưới đây không chứng minh được engine mới; phải paper-test lại sau khi xác định trục đa chiều.
- **Mục đích:** thử xem dynamic Khoai–Đào có thể tạo các tập khác nhau mà không ép mọi tập cùng một câu đùa hay verdict.

Các case dưới đây dùng placeholder. `MÓN`, `ĐỊA PHƯƠNG` và `CHI TIẾT CÓ NGUỒN` chỉ được thay bằng thông tin đã kiểm chứng tại P2. Không có claim văn hóa nào được phê duyệt từ bài test này.

## Case A — Món có chi tiết dễ chơi chữ

1. Đào bắt được một nghĩa khác của từ chỉ nguyên liệu/cách ăn, trêu Khoai.
2. Khoai giải thích rất ngắn, đưa `CHI TIẾT CÓ NGUỒN`.
3. Đào đẩy món tới trước mặt người kén ăn.
4. Hình cho thấy món rõ ràng; Khoai thử và đưa verdict tự nhiên.

**Giữ được:** chemistry và hook. **Nguy cơ:** trò chơi chữ lấn át địa phương/món; đoạn giải thích trở thành đọc fact. **Điều kiện đạt:** người xem vẫn nhớ tên món + địa phương dù bỏ joke đi.

## Case B — Món không có wordplay

1. Khoai nêu một chi tiết thị giác hoặc cách làm đáng tò mò của `MÓN` ở `ĐỊA PHƯƠNG`.
2. Đào muốn thử ngay, Khoai còn cân nhắc vì khẩu vị riêng.
3. Food reveal thể hiện đúng `CHI TIẾT CÓ NGUỒN`.
4. Hai người thử; payoff đến từ phản ứng khác nhau, không từ câu chơi chữ.

**Giữ được:** hành trình ẩm thực, hai tính cách, kiến thức. **Nguy cơ:** Khoai thành người thuyết minh. **Điều kiện đạt:** có xung đột nhẹ và hình ảnh làm một phần công việc kể chuyện.

## Case C — Khoai chưa thích món

1. Khoai giới thiệu món có một nét vị/kết cấu đặc trưng đã kiểm chứng.
2. Đào hào hứng thử và rủ Khoai.
3. Khoai nói “vị này chưa hợp mình” hoặc nhận xét tương đương, nêu đặc điểm cảm nhận thay vì phán món dở.
4. Đào thích hoặc đưa góc nhìn khác; câu kết mời người xem tự cảm nhận.

**Giữ được:** lời khen của Khoai có giá trị vì không tự động xuất hiện. **Nguy cơ:** người xem hiểu thành chê món/địa phương. **Điều kiện đạt:** verdict là `OPINION`, chi tiết văn hóa vẫn tích cực/chính xác, không bị ép đổi thành lời khen.

## Kết luận ở mức paper test

Engine có thể tạo ba kiểu payoff khác nhau: wordplay, khám phá bằng hình và bất đồng khẩu vị. Điều này chứng minh **tính khả dụng trên giấy**, chưa chứng minh video 15–30 giây chạy tốt, người xem thấy hấp dẫn hay Veo giữ được nhân vật/món. Các bước kiểm tra đó thuộc timed script, visual test và pilot.

**Kết luận hiện hành:** không dùng kết quả này để khóa engine P1. Tham chiếu Series Bible v0.2 và thực hiện test mới theo trục đa chiều trước khi duyệt.
