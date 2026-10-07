# REC239/240 — Duyệt giọng, chuẩn bị C02 và sửa khung master

Ngày 07/10/2026. Phạm vi kế hoạch làm lại236, nick/project mới. Chưa sinh video C02.

## Điều đã xác định và quyết định đã chốt

- Owner “giọng ok rồi nhé”: chấp nhận hai preview K20/Orus và D06/Aoede phục hồi; không nghiệm thu giọng/khẩu hình của video chưa có.
- “Tiếp tục đi nào” cho phép chuẩn bị chuyên môn và request. Root không suy thành bỏ checkpoint master.
- Khi hỏi exact master v2, owner chọn **“Sửa khung ảnh master trước khi chạy C02”**. Giữ giọng đã chọn; v2 không accepted, video HOLD.
- DIR/DOP/ACT/EDIT đã chạy nhiệm vụ bounded, root đọc toàn bộ báo cáo và tích hợp. C02 một khung cận vừa hai người, Khoai kể trọn phần N02 sau “Khoan”, Đào nghe, tay nghỉ F0. Không insert món phủ lời, flashback hoặc gắp sớm. Slot8,5s chỉ target; chưa EDL/timing thực.
- Phản biện độc lập đã đọc draft và actual v2: PAPER_PASS_CONDITIONAL cho logic, SUBMIT_HOLD vì ảnh mới, quote/input cuối và khả năng dựng account chưa đóng.

## Các lượt hình thực

V3: sửa trên v2 trong editor, NanoBanana2.1/9:16, fullpromptquote0, một lần gửi; đã tải native riêng. 768×1376, SHA25649f672ca0fd63ab0539b9dde90f7a181aa5acc1b0d88a632c91ecb40b04e1aa4. Root xem ảnh thực: khung gần như cũ, rau còn cắt trái và cốc còn sát phải. **REWORK**, không trình làm ảnh đạt.

V4: chuyển từ sửa trong editor sang một camera composition mới với cùng ảnh v2 làm reference trong Flow, không đổi API/model/creative. Upload đúng native v2 theo tên riêng để picker không tự dùng v3/latest. Một imagechip UUIDdd3836e2-abbd-481c-abfd-33e2e320b3b3; x1,9:16,AgentOFF,NanoBanana2.1, quote0 đầy đủ. Một lần gửi. Kết quả chưa được nghiệm thu trong thời điểm ghi phần này; cập nhật manifest/report khi có native.

**Cập nhật sau tải v4:** native768×1376, SHA256f5f5b9e767dab5007d6de2b1cca8671f07e25c5adeaba56cea01ede8a5da65b0; root trực tiếp xem và vẫn thấy rau cắt trái/cốc sát phải. REWORK, không owner-review-ready. Hai output framing liên tiếp không đạt: STOP sinh tiếp; không coi đây là lỗi major food đã lặp. Số dư sau cả hai lượt vẫn1.050, observed debit0. Chưa có video mới.

Reviewer frame đã gửi nhận xét giữa chừng về v3/v4 nhưng chạm giới hạn sử dụng trước khi lưu báo cáo. Run được ghi FAILED_BEFORE_REPORT; không nhận review độc lập ảnh mới đã hoàn tất. Root vẫn kiểm native thực; muốn đóng production gate phải có evidence review đủ và owner checkpoint, không gắn nhãn PASS giả.

## Giả định, rủi ro và kiểm tiếp

- V3 gần như giữ khung cũ là quan sát. Giả thuyết editing/source composition có sức neo lớn hơn yêu cầu reframe bằng chữ chưa chứng minh cơ chế model. V4 thử tuyến bố cục mới có lý do, không guarantee.
- Khoảng80%width trong promptv4 là design intent, không metric đã đo. Kiểm thực margin/serving/face readability/F0/geography/food và kích thước native.
- CropUI chỉ cắt phần đang có; không phục hồi rau/cốc đã nằm ngoài ảnh. Đã hủy crop, không dùng crop che lỗi hoặc gọi sửa thành công.
- Nếu lỗi framing lặp sau v3/v4, dừng sinh tiếp và trình phương án khác. Không sinh video để chữa ảnh đầu vào.
- Catalog StringoutCreator được thấy; mở template tự tạo remix, chưa chạy. Chưa kiểm linked audio/trim/arrange/export, không hứa ghép miễn phí hoặc tool đủ finishing. Chi tiết trong lesson239.
- Đã dùng computer-use để kiểm thực nguồn/cấu hình/quote; imagegen hướng dẫn sửa một biến, giữ invariants. Theo lựa chọn owner, ảnh thực tạo trong Flow, không gọi API/CLI khác.

## Bước tiếp

Tải/kiểm v4, ghi actualfindings và trình owner exactfile nếu đạt; nếu không đạt, báo blocker/phương án. Khi master và đường dựng sẵn sàng, cập nhật binding/prompt rồi kiểm quote cuối trước một C02720p theo quyền238. Không mở C01A khi C02actual chưa qua checkpoint.

**Bước tiếp hiện hành:** trình lựa chọn đổi cách dựng master trong Flow: không dùng toàn ảnh v2 làm neo khung nữa, mà dùng nguồn nhân vật riêng và ảnh món riêng để tái bố cục bàn rộng. Hệ quả: dễ thay khung nhưng có rủi ro drift mặt/geography nên phải kiểm hồi quy và owner duyệt lại. Phương án khác là công cụ mở rộng viền có kiểm soát; đó là route/tool mới cần owner quyết định trước. Chưa chạy một trong hai.
