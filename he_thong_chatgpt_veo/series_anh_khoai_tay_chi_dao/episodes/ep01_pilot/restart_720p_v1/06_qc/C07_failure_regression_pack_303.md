# REC303 — Hồi quy bắt buộc trước C07 kế tiếp

13-10-2026. Đã đọc lại actual history trước chuẩn đầu vào mới. Đây là điều kiện kiểm, không phải chứng minh video tiếp theo sẽ đạt.

| Nguồn đã kiểm | Kết quả ghi trong native QC | Điều phải giữ hoặc kiểm lại |
| --- | --- | --- |
| REC277 C07 T02, một ảnh cảnh + D06 | Đào hóa người toàn nguồn; bát Khoai mất, tư thế đầu và cốc lệch | Không coi một ảnh cảnh hoặc nhãn “peach woman” đủ giữ nhận diện; hai bát và trạng thái cốc phải kiểm ngay từ F0 |
| REC280 C07 T03, ảnh cảnh + portrait + D06 | Giữ được dạng nhân vật thực phẩm, nhưng reset tư thế, đưa A tới miệng, cốc hạ và bát kết sai | Khôi phục neo nhận diện như một giả thuyết hợp lý; không dùng lại choreography cũ, không coi hai ảnh là khóa hành động |
| REC302 C07 RECEIVE T01, F47 + D06 | Đào hóa người F0–95; cốc về bàn, hai tay nâng bát; đũa nghỉ mất; A còn kẹp | Giữ một tay ngoài nâng cốc, một tay trong đỡ đúng bát; không che lỗi mặt bằng cắt/crop và không dùng endpoint sai cho C08 |

## Biện pháp giữ, bổ sung và không nhập lại

- Giữ exact scene F47 native C06 và approval range/đối thoại REC300; không redraw ảnh cảnh.
- Giữ một D06, N07 nguyên văn, Khoai nghe/giữ A và nhịp nhận trước–thả sau REC295.
- Bổ sung portrait nhận diện mới từ F47: chỉ hình thái/mặt, không đạo cụ hoặc endpoint hành động. Portrait cũ REC278 không đưa vào gói mới.
- Bổ sung mô tả rõ Khoai là củ khoai tây và toàn đầu Đào là quả đào có cleft/skin/stem/leaf, không tóc/tai người; không hứa wording giải quyết độc lập.
- Làm rõ một tay ngoài luôn giữ cốc, chỉ tay trong nâng bát. Không nhập lại động tác kéo bát trên bàn hoặc đưa A tới miệng của lịch sử279/280.
- Hai ảnh + wording thay đồng thời, nên không gọi đây là phép thử một biến hoặc bằng chứng causal. Mục đích là khôi phục controls và sản xuất có kiểm, không chạy batch thử tự động.

## Cổng kiểm kế tiếp

1. Ảnh: shape/mặt/trang phục/gaze/màu so F47; vai từng ảnh và mọi redraw phải được khai báo. Owner duyệt neo nhận diện, không phải diễn hoặc tư thế đầu mới.
2. Request: actual hai ảnh đúng + chỉ D06, toàn prompt hiện hành, route/quote/x1/720p/toggle, bucket đủ và quyền một lượt mới. Không dùng quyền REC302 đã tiêu hết.
3. Native F0: còn quả đào/không tóc, cốc đang nâng, đủ hai bát và đũa nghỉ; reset MAJOR → loại, không xin owner miễn lỗi.
4. Toàn nguồn: tay đúng chức năng, bát trống/nâng trước/sang sau/khoảng hở, A kẹp chưa thả/ăn, không miệng Khoai nói. Quan sát che khuất không tự thành physics PASS.
5. Audio/AV: D06, N07 đủ âm cuối/khẩu hình/nhịp phải kiểm thực theo capability hoặc owner exactfile; ASR không thay nghe.
6. Chỉ sau chọn source/range C07 mới chuẩn nhịp thả từ exit thực. Món tại cut C05→C06 và conflict final30/rough35 vẫn mở.

## Quyền và ngân sách

Owner hiện chỉ duyệt chuẩn đầu vào mới, không chạy trả phí. Sổ 258/500, còn 242; tạo lại 5, dự phòng 110 đóng. Đề nghị dùng cấu hình như trước không đồng nghĩa quote hiện hành vẫn 7; phải kiểm lại sau duyệt input. Mức 7 cũ cũng đã vượt phần tạo lại còn 5, nên cần quyết định phân bổ trước request mới; không tự lấy phần tạo mới/hậu kỳ/dự phòng.
