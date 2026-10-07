# 235 — Dự trù làm lại EP01 trên tài khoản Flow trắng

Ngày: 2026-10-07. Trạng thái: **ESTIMATE_ONLY / ACCOUNT_NOT_RECEIVED / NOT_SPENDING_APPROVAL**.

Owner hỏi: với kinh nghiệm triển khai, bắt đầu lại hoàn toàn trên tài khoản mới cần khoảng bao nhiêu credit để hoàn thành video, cho phép dự trù cả test và kiểm. Đây là yêu cầu lập dự toán mới, không cấp sẵn quyền chạy, đăng nhập tài khoản mới, tạo media hoặc dùng hết ngân sách. Lượt này không generation, không chi credit.

## 1. Phạm vi và giả định

- Tạo một EP01 Nem Bùi, 30 giây, dọc 9:16, đủ câu chuyện và mặt người nói theo C-v0.6/178 và storyboard214. Khoai/Đào là bạn, giọng nam/nữ Bắc theo chất đã chọn, món nguội, phục vụ đúng và đường A → bát Đào → B không sai.
- Giữ nghiên cứu, kịch bản, canon, tư liệu gốc hợp lệ và kinh nghiệm đã tích lũy. Không quay lại discovery hay tuyển 20–30 chất giọng khác. Nếu owner muốn sáng tạo lại cả câu chuyện/hình tượng, dự toán này chưa bao phần thay đổi đó.
- Tài khoản/project mới không có clip sản xuất được chọn sẵn. Tạo lại bộ tham chiếu và preset giọng trên tài khoản mới; sản xuất lại toàn bộ footage, **kể cả N02**. Không lấy clip N02 B cũ làm nguồn hình/tiếng trong phim mới.
- Preset ID K20/D06 cũ không mặc định có trên tài khoản mới. Tái dựng từ thông số base/performance đã lưu, lấy ID mới và nghiệm thu lại. Không hứa preset được tái tạo sẽ giống tuyệt đối giọng cũ chỉ vì cùng Orus/Aoede. Nguồn cũ có thể làm đối chứng nghe nếu hợp lệ, không tự trở thành ingredient hoặc soundtrack phim mới.
- Tài khoản có quyền truy cập các feature Omni/voice cần thiết. Chưa xác minh plan, region hoặc quote của tài khoản mới; phải kiểm trước chi. Không tính daily credits hoặc refund chưa phát sinh như nguồn bù ngân sách.
- Hướng chính: thử khả năng ở Omni 360p; footage dùng cho bản cuối ưu tiên **Omni 720p native**, không mặc định upscale bản nháp là tương đương tạo gốc720p. Kiểm regression khi đổi độ phân giải: test360p đạt không chứng minh prompt720p luôn đạt.
- Ảnh tham chiếu dùng tuyến có quote0 nếu đáp ứng chất lượng; tạo/sửa/preview voice phải kiểm chi phí thực. Nếu có phí, dùng dự phòng chỉ khi được duyệt đúng request; không tự ghi mọi thao tác ảnh/voice là miễn phí.
- Cắt–ghép thông thường và QC trên file sẵn có không cần generation credit. Ưu tiên ghép Flow nếu chức năng thực đáp ứng; trích khung/đo/đối soát local không bắt buộc dựng local. Sửa cảnh bằng AI, extend, retake hoặc sinh chuyển cảnh mới là khoản generation, không gọi ghép miễn phí.
- Không dùng Veo Quality hoặc thuê API/vendor mới trong dự toán cơ sở. Không xóa lịch sử/project cũ, không chuyển quyền tài khoản hay nạp tiền.

## 2. Giá dùng lập dự toán

Nguồn chính thức đọc lại ngày 2026-10-07:

- [Credit Google Flow](https://support.google.com/flow/answer/16526234?hl=en): Omni360p4/6/8/10s =4/5/6/7credit; Omni720p4/6/8/10s =7/10/12/15credit. VeoQuality100/output. Giá theo từng đầu ra; x3 không là một clip tính phí.
- [Tạo video và voice](https://support.google.com/flow/answer/16353334?hl=en): voice reference chỉ dùng trên Ingredients. Không lập kế hoạch Frames START/END + customvoice như tổ hợp đã hỗ trợ.
- [Model/features](https://support.google.com/flow/answer/16352836?hl=en): Omni có draft360 và720, customvoice tùy vùng; Pro/Ultra có upscale Omni360→720 giá0 theo tài liệu. Đây là lựa chọn tiết kiệm có điều kiện, không bằng chứng giữ chi tiết hoặc đạt final trên tài khoản mới.

Trần dưới dùng7 cho output thử và15 cho output sản xuất/sửa dài tối đa10s. Các clip ngắn hơn có thể rẻ hơn, nhưng timing chưa khóa nên không lấy giá4/7 thấp nhất cho tất cả. Quote actual đủ ingredients phải đọc trước mỗi request. Không dùng giá edit232 lịch sử10 để lập dự toán tuyến tạo mới; public video-edit40 không nằm trong phép tính mỗi output15 dưới đây.

## 3. Ngân sách khuyến nghị: 500 credit, cấp theo chặng

Mức lập kế hoạch chính khoảng 400–500 credit; **khuyến nghị dành 500** để có dự phòng cho cảnh khó. Đây là trần dự toán, không dự đoán chắc chắn sẽ dùng hết hoặc bảo đảm hoàn thành bằng 500.

| Hạng mục | Cơ sở số lượng | Khoản dành tối đa |
| --- | --- | ---: |
| Kiểm preset trên tài khoản mới và thử các nhiệm vụ rủi ro | Tối đa8 output360p ×7 =56; làm tròn hạn mức60 |60|
| Lượt sản xuất đầu toàn phim | Dự kiến9–11 output720p; trần11×15 |165|
| Retake có mục tiêu tại cảnh lỗi | Dành tối đa10 output720p ×15; không có quyền tự retry |150|
| Sửa coverage/điểm nối sau ráp toàn phim | Dành tối đa3 output720p ×15; không thu phí cho mỗi lần xem/ghép |45|
| Dự phòng chưa phân bổ | Chênh feature/ảnh/preset có phí, cảnh phải tách thêm hoặc repair khác sau xem xét |80|
| **Tổng trần lập kế hoạch** | |**500**|

Khoản60 đã gồm dư4 trên56; không cộng lại4 vào80. Khoản150 và45 phân biệt:150 sửa clip nguồn sai nhiệm vụ,45 cho thiếu/sai coverage chỉ phát hiện qua rough cut. Một output không được tính trùng cả hai. 80 là tiền dự phòng chưa dùng, không phải fee QC hoặc quyền thêm batch. Nếu test output đủ điều kiện dùng trong phim mới, giảm số output sản xuất tương ứng; không tạo lại chỉ để đủ bảng chi.

### Các kịch bản minh họa, không xác suất

Giả sử quote thực không vượt7/15 và không cần công đoạn trả phí khác:

| Kịch bản | Phép tính | Dự toán kể cả khoản giữ lại |
| --- | --- | ---: |
| Thuận lợi, ít phải tách |8 thử×7 +9 sản xuất×15 +6 sửa×15 +2 sửa sau ráp×15 =311; giữ50 |361, khoảng360|
| Có thêm coverage và nhiều cảnh khó |8 thử×7 +11 sản xuất×15 +8 sửa×15 +3 sửa sau ráp×15 =386; giữ50 |436, khoảng440|
| Mức dự phòng khuyến nghị |8 thử×7 +11 sản xuất×15 +10 sửa×15 +3 sửa sau ráp×15 =416; giữ80 và làm tròn4 |500|

Số sửa6/8/10 là giả định lập ngân sách, không tỷ lệ lỗi đo được. Các batch trước khác source/model/route/brief, chưa cho phép dự báo xác suất thành công hoặc số retake trung bình. Kịch bản thuận lợi không được dùng làm lời hứa hoàn thành360.

## 4. Vì sao không tiếp tục lấy77 hoặc chỉ cộng tiền cho7 cảnh?

Dự toán233 tái dùng N02 B, dự kiến7 đơn vị thiếu và tạo mới360p. Tài khoản trắng phải tạo lại N02 và các input/preset; phương án235 còn chọn720p native và cho phép tách coverage có chủ đích. **Thay đổi phạm vi và đơn giá**, không phải cùng phương án77 bị nâng giá tùy ý.

Không hứa300credit đủ cho cùng bản720p native và dự phòng trên. Một tuyến chủ yếu360p + upscale có thể rẻ hơn đáng kể, nhưng cần nghiệm thu mức chi tiết và feature trên tài khoản mới; phải lập dự toán riêng nếu owner chọn. Không gọi Quality cần thiết để sửa người nói/tay/đường nem: Quality100/output sẽ thay đổi ngân sách và không bảo đảm hết lỗi.

## 5. Cách dùng kinh nghiệm để ngăn thử lặp

### Trước generation — chuẩn bị/kiểm đầu vào

Lập source-of-truth riêng cho project mới, giữ project cũ read-only. Copy tài liệu/brief chuẩn, không thừa kế các cloud IDs, snapshot balance, acceptance của clip cũ hoặc nguồn sai. Khóa ảnh/bàn/món/góc/voice ID mới trước chạy; một bảng thoại→speaker→mặt→listener→giọng→trạng tháiA/B cho cả tập. Nhịp30s phải có cơ sở đo, không phủ đủ giây bằng cảnh món.

### Chặng đầu — tối đa 60 credit để đánh giá khả năng thực hiện

Đề xuất tối đa8 output có mục tiêu, không8 mẫu audition ngẫu nhiên: khoảng2 kiểm từng voice qua lời ngắn/dài và diễn;2 cho mở câu chuyện/đối thoại theo cách dàn cảnh khác rõ;2 cho pick→hold có mặt/ý định;2 cho đổi hướng/nhận→release theo trạng thái hợp lý. Số lượng và thứ tự actual đăng ký trước mỗi request; không bắt buộc chạy đủ8, không tự phục hồi x3 cũ hoặc lặp nếu không có thay đổi được giải thích.

**Trước khi giải ngân chặng sản xuất:** phải có bằng chứng nghe đúng giọng/vai và footage đại diện cho cảnh tương tác tay–mặt–món đạt tiêu chí liên quan. Không thông qua gate chỉ bằng tay cận đơn lẻ, thumbnail đẹp, ASR đúng hoặc file decode sạch. Nếu 60 credit chưa tìm được cách làm cảnh đích, dừng đánh giá nguyên nhân/capability/staging và trình quyết định; không mặc định còn 440 thì thử cho hết. Không hứa chặng đầu 60 sẽ chắc chắn chứng minh đủ.

### Sản xuất và sửa

Một output rồi kiểm và ráp vào toàn mạch. Không chuyển mọi cảnh sang một khung khóa chung chỉ vì dễ kiểm; DIR/DOP/ACT/EDIT phải giữ góc máy, mặt, biểu cảm và lý do cắt phù hợp câu chuyện. Khó ở R04–R08 nên ưu tiên đóng đường hành động và điểm nối trước tiêu nhiều cho trang trí/finishing.

Retake phải có: lỗi/timecode, nguyên nhân xác nhận hoặc giả thuyết, thay đổi nguồn/brief/route, kết quả kỳ vọng, quote, tác động tới cảnh kế. Hai output liên tiếp vẫn cùng blocker thì dừng để chẩn đoán/phê duyệt hướng khác; không biến quy tắc này thành quyền mặc định chạy hai lần. Không né lỗi bằng che mặt người nói, trộn tiếng lên môi khép, tạo nem nóng hoặc bỏ đườngA/B.

### QC và nghiệm thu cuối

Trích toàn khung khi cần, kiểm dày quanh gắp/dừng/thả/cắt và xem/nghe chuyển động thực đúng capability. Phân biệt root/agent đã kiểm bằng công cụ với owner đã nghe; không ghi report độc lập mới khi chưa chạy. Bản toàn30s phải qua review lời–vai–giọng, mặt/lip-sync, diễn/continuity/món, phụ đề/AI disclosure, mix và export. Có500credit không thay nghiệm thu nghề nghiệp.

## 6. Rủi ro và các quyết định còn mở

Chưa có dự báo xác suất cao được hiệu chuẩn cho cả phim.500 giúp có ngân sách để kiểm khả năng và sửa có mục tiêu, không giải quyết một công nghệ không thực hiện được exact nhiệm vụ. Rủi ro chính vẫn là speaker attribution, tái dựng image Ingredients, hand/food conservation và điểm nối; tài khoản mới tự nó không chữa các lỗi này.

Owner cần chốt khi bắt đầu thật: quyền/tính năng tài khoản mới; có đồng ý làm bản720p native theo phương án cơ sở hay chọn tuyến draft-upscale; phạm vi tái tạo preset/nguồn và hạn mức chặng đầu. Không hỏi lại tên/nhân vật/lời/câu chuyện đã chốt. Nếu muốn làm lại cả creative design hoặc bắt buộc đúng waveform/identity giọng cũ, phải dự toán lại; freshpreset chưa chứng minh exact identity.

## 7. Tổng hợp vòng

- **Đã xác định:** phạm vi account/project/media mới lớn hơn kế hoạch77; giá tạo mới360/720 đọc lại, không quote live tài khoản chưa nhận.
- **Đã chốt trước:** creative canon và chất giọng đã chọn; chưa có approval500 hoặc quyền test/generation mới từ câu hỏi dự toán.
- **Giả định:** giữ creative/tư liệu, tạo lại toàn bộ footage/preset/refs; account đủ feature, draft360 để thử và native720 cho sản xuất,9–11 output lượt đầu.
- **Còn mở:** feature tài khoản mới, mức giống preset tái dựng, gói nguồn/timing/capability, số retake và tiêu chuẩn resolution được owner chọn.
- **Bước tiếp:** owner xác nhận phạm vi và ngân sách/chặng; sau đó intake tài khoản và lập gói preflight trước một request thử cụ thể. Không tiêu ngân sách hoặc chuyển tài khoản trong lượt235.
