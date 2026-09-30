# EP01 — Owner dựng Canva, bàn giao theo cảnh/đoạn

Ngày ghi nhận: 2026-09-30. Status: OWNER_DELIVERY_SCOPE_CONFIRMED / MEDIA_NOT_CREATED.

## Quyết định đã xác nhận

Owner: “cứ làm chuẩn đi, tôi sẽ tự ghép được qua canva, đầu ra cứ chuẩn từng cảnh đoạn ok là được;”

- Owner tự ghép và hoàn thiện video bằng Canva.
- Phạm vi đầu ra của phía hỗ trợ là các clip cảnh/đoạn đã kiểm chất lượng, kèm thông tin để ghép đúng câu chuyện. Không cần tự dựng master hoặc cài phần mềm dựng.
- Không rút gọn các gate chất lượng. Không diễn giải câu này thành quyền tạo media, upload tài sản, tiêu credit hoặc retry không giới hạn.
- Đây là bổ sung phạm vi bàn giao EP01 so với [baseline P0](../../00_governance/06_generation-credit-delivery-policy.md); giữ nguyên bản P0 đã duyệt để truy vết.

## Trách nhiệm và điểm kiểm

| Phần việc | Trách nhiệm | Điều kiện hoàn tất |
|---|---|---|
| Nội dung, research, hình/giọng, shot và generation package | Phía hỗ trợ chuẩn bị; owner duyệt các gate | Có đúng phiên bản được duyệt, không nhảy gate |
| Tạo clip thử | Theo request và giới hạn owner duyệt riêng | Có log đầu vào, settings, credit thực tế và kết quả |
| Chọn clip, QC từng clip và khả năng nối | Phía hỗ trợ kiểm, owner chấp nhận clip pack | Clip dùng được, thứ tự và điểm nối rõ; không chỉ đẹp từng cảnh riêng |
| Dựng, nhạc, phụ đề, thông tin món/địa phương, nhãn AI trên Canva | Owner thực hiện, phía hỗ trợ bàn giao chỉ dẫn và nội dung đã duyệt | Owner kiểm bản dựng cuối trước sử dụng |
| QC master cuối | Chưa thực hiện; có thể hỗ trợ nếu owner gửi bản xuất | Không tuyên bố PASS khi chưa xem bản xuất thực tế |

`CLIP_PACK_ACCEPTED` không đồng nghĩa `EPISODE_DONE`, `MASTER_QC_PASS` hoặc `PUBLISHED`. Những điều kiện DONE của P0 chưa được miễn; phần master/project dựng do owner quản lý. Nếu chưa được kiểm bản cuối, hồ sơ phải ghi rõ giới hạn này, không xác nhận chất lượng toàn tập thay owner.

## Quy cách làm việc đề xuất v0.1

Các mục sau là baseline chuẩn bị, chưa phải thông số đã thử với Flow/Canva:

- Clip dọc 9:16; mục tiêu bàn giao 1080×1920, MP4 H.264 với tiếng AAC. Ghi thông số thật từ file; nếu nguồn thấp hơn mục tiêu thì trình lựa chọn, không upscale rồi gọi là chất lượng nguồn đạt chuẩn.
- Một clip ứng với đơn vị shot/đoạn trong shot plan; không khóa số clip, số giây mỗi clip hoặc hứa một lần sinh đủ 30 giây khi chưa thử.
- Lời thoại và âm thanh cần thiết phải nghe rõ, đúng người, đồng bộ và không bị cắt đầu/cuối. Nhạc nền toàn tập để owner xử lý khi dựng; không mặc định mỗi clip có nhạc riêng gây đứt nhịp.
- Giữ bản sạch để dựng; kèm nội dung chữ đã duyệt và cue thời điểm hiển thị. Không mặc định chữ sinh trực tiếp trong video là đúng. Bản preview có chữ chỉ là bản kiểm, không thay file sạch.
- Tổng thời lượng sau dựng hướng tới khoảng 30 giây; tính theo timeline thực tế, không cộng máy móc độ dài các file nguồn.
- Đặt tên `EP01_Sxx_Txx_vN`; clip được chọn ghi riêng, không để owner phải đoán giữa các take.

## Checklist bắt buộc trước nhận clip pack

Hiện tại mọi kiểm media bên dưới đều CHƯA KIỂM vì chưa có file thật.

1. Nội dung: đúng script C-v0.5 và claim/fiction đã duyệt; không tự thêm câu, nguyên liệu, brand hoặc chi tiết văn hóa.
2. Nhân vật: diện mạo, giọng, trang phục và tính cách nhất quán; không biến thành cặp đôi hoặc trẻ em.
3. Hành động: Khoai đổi hướng gắp trước khi nem chạm miệng, đặt vào bát Đào; tay/đũa/bát/món không lỗi hoặc biến dạng làm sai ý.
4. Tiếng và diễn: đúng lời, đúng người, tiếng Việt tự nhiên; nhịp bắt gặp và chữa cháy đọc được bằng hình/tiếng, không chỉ có trong prompt.
5. Điểm nối: trạng thái người, tay, đồ vật, hướng nhìn, ánh sáng, tiếng và nhịp tương thích; ghi in/out, khoảng giữ hình hoặc phương án cắt nếu cần. Không ép continuity tuyệt đối khi cắt có chủ ý nhưng phải đọc được câu chuyện.
6. Kỹ thuật: mở/phát được file, đúng khung hình, thông số thực tế được ghi; kiểm tiếng rè, hình lỗi, mất khung, chữ thừa và watermark nếu có.
7. Handoff: thứ tự clip, thời lượng sử dụng, lời thoại, cue chữ, QC, ngoại lệ và approval có thể đọc lại; lỗi chưa sửa không được đánh dấu PASS.

## Gói bàn giao

- File clip đã chọn và danh mục take: selected/rejected/needs_fix, lý do, phiên bản.
- Bảng hướng dẫn dựng: clip ID, thứ tự, in/out, thời lượng sử dụng, hành động đầu/cuối, cue âm thanh/chữ và lưu ý điểm nối.
- Nội dung chữ theo đúng ranh giới đã duyệt: “Nem Bùi — gắn với Bùi Xá, Bắc Ninh.”; “Thính gạo rang góp một phần vào mùi vị của Nem Bùi.”; “Video được tạo bằng AI.” Vị trí/thời điểm còn cần thiết kế; không tự bỏ vì bàn giao clip sạch.
- Source/evidence, reference/rights, prompt/settings/credit log, QC và approval/change log. Giữ nguồn raw và lý do chọn để audit.
- Media lưu trong folder media do owner quản lý, không commit Git; tài liệu và metadata được version/commit/push. Không hứa file audio rời/SRT khi chưa tạo hoặc kiểm.

## Hiện trạng và bước tiếp theo

- Đã xác định: owner dựng Canva, phía hỗ trợ bàn giao clip pack có QC và chỉ dẫn nối.
- Đã chốt: đổi phân công khâu ghép; không đổi nội dung C-v0.5 hoặc các gate.
- Giả định làm việc: clip sạch + lời thoại cần thiết + cue chữ; nhạc toàn tập đặt ở khâu dựng. Thông số xuất là mục tiêu cần kiểm bằng file thật.
- Còn mở: [ba review cuối P5](34_p5-final-review-gap-register-c-v0.5.md), hình/giọng, shot plan, request/cap thử và khả năng thực tế của Flow.
- Tiếp theo: khép review cuối P5 → P6 hình/giọng → P7 shot/continuity và hướng dẫn nối → P8 request được owner duyệt → tạo thử/QC clip. Chưa có generation chạy hoặc file bàn giao.
