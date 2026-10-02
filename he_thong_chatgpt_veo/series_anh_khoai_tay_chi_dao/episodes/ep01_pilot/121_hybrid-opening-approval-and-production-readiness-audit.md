# EP01 — hướng sản xuất kết hợp và mức độ sẵn sàng

Ngày kiểm: 2026-10-02. Bản biên tập lại tiếng Việt; giữ kết quả kiểm và giới hạn bằng chứng của bản trước. Lịch sử bản trước được lưu trong Git.

## 1. Kết luận

Chủ dự án đã chọn hướng A trong tài liệu 120: dùng chuyển động có kiểm soát trên ảnh cho phần dẫn mắt của cảnh mở; dùng Veo cho diễn xuất có chủ đích. Đây là quyết định về phương pháp, không phải duyệt mọi khung hình, điểm cắt hoặc sản phẩm cuối.

**Có đủ công cụ nền tảng để chuẩn bị thử nghiệm, nhưng chưa sẵn sàng chạy cả tập bằng Quality hoặc bàn giao video hoàn chỉnh.**

Còn thiếu: mẫu giọng được nghe duyệt, đầu vào đúng trạng thái từng cảnh, bằng chứng động tác và nối cảnh, bản ráp thử và kiểm chất lượng bản xuất cuối. Bộ 10 clip trong tài liệu 119 chưa có bản đạt toàn bộ yêu cầu.

**Cập nhật quyết định:** ngân sách thử Quality riêng tối đa 100 credit đã được duyệt có điều kiện tại [tài liệu 122](122_conditional-quality-approval-and-owner-actions.md). Điều kiện mới yêu cầu đầu vào, prompt và thử nghiệm tương ứng đạt trên Lite trước. Điều kiện này thay đề xuất thử Quality trực tiếp trong bản cũ của tài liệu này. Chưa chạy Quality.

## 2. Trạng thái các giai đoạn

| Giai đoạn | Đã có | Còn thiếu |
|---|---|---|
| P2 — Nghiên cứu | Gói nghiên cứu và ranh giới claim được duyệt trong tài liệu 08 | Đối chiếu thông tin trên tiếng, chữ và hình cuối |
| P5 — Kịch bản | C-v0.5 và vị trí thông tin bổ sung được duyệt trong tài liệu 38 | Kiểm lời thoại trên đầu ra thật; không tự viết lại |
| P6 — Phát triển hình và giọng | Tạo hình chính, bàn ăn, hướng món và cách cầm đũa đã được chọn | Giọng thực, biểu cảm và đầu vào theo trạng thái hành động |
| P7 — Thiết kế cảnh quay | T2 và hướng quay được duyệt trong tài liệu 100 | Bổ sung phương pháp cảnh mở kết hợp; điểm nối S04–S05 còn mở |
| P8 — Chuẩn bị tạo video | Các thử nghiệm cũ có hồ sơ riêng | Gói yêu cầu mới theo cảnh, đầu vào, cấu hình, giá và điều kiện dừng |
| P9 — Tạo và kiểm video | Có mẫu V01 và 12 lượt thử camera/trạng thái nghỉ | Chưa có clip được chọn làm đầu ra sản xuất |
| P10 — Chọn và ráp cảnh | Đã ghép thử kỹ thuật bằng FFmpeg | Bản ráp nhiều cảnh với nguồn và thời lượng đo thật |
| P11 — Hậu kỳ | Có công cụ hỗ trợ | Chốt hình, tiếng, chữ, màu và chuyển cảnh trên bản ráp |
| P12–P13 — Kiểm cuối và bàn giao | Có thiết kế vai trò, checklist | Bản xuất thật, báo cáo kiểm và chủ dự án nghiệm thu |
| P14 — Tổng kết | Có kết quả vòng thử trong tài liệu 119–120 | Tổng kết toàn tập sau bàn giao |

Không mở lại nội dung đã duyệt. Phải phân biệt quyết định mới với các dòng “chờ duyệt” trong hồ sơ lịch sử.

## 3. Công cụ đã kiểm

Các kiểm dưới đây được thực hiện trong vòng kiểm trước, cùng ngày 2026-10-02. Việc biên tập tài liệu không được tính là chạy lại công cụ.

| Công cụ | Bằng chứng đã có | Giới hạn |
|---|---|---|
| Flow/Veo | Mở được dự án; menu có Lite, Fast, Quality và Omni | Chưa kiểm hoặc gửi yêu cầu Quality cụ thể |
| Scenebuilder | Có mục Cảnh; hướng dẫn Google mô tả sắp xếp, cắt, xem và tải chuỗi clip | Mục Cảnh của dự án hiện trống ở lần kiểm; chưa thử nhập clip cảnh mở và xuất bản ráp |
| FFmpeg/FFprobe 9.0.2 | Chạy được; có bộ lọc pan/zoom, crop, ghép, chữ và âm thanh; bộ clip 119 giải mã không báo lỗi | Chưa có quy trình dựng cảnh mở được thử đạt |
| Python 3.12.14 | Kiểm thư viện không có lỗi phụ thuộc | Không chứng minh chất lượng video |
| faster-whisper 1.2.1, PyAV 16.1.0, CTranslate2 4.8.2 | Nạp được model small từ cache ngoại tuyến | ASR chỉ hỗ trợ đối chiếu lời; không thay nghe giọng và sắc thái |
| local_voice_qc.py | Đã trích âm thanh và tạo bằng chứng ASR tại tài liệu 89 | Chưa kiểm mẫu giọng mới |
| voice_assembly_diagnostic.py | Năm kiểm thử đơn vị đạt; đã có bản ghép thử tại tài liệu 90 | Chỉ nhận đúng file V01; không phải công cụ dựng tổng quát |
| Canva | Chủ dự án đã chọn làm phương án hoàn thiện/dự phòng | Chưa kiểm đăng nhập, nhập file và xuất file hiện tại |

Chưa cần cài thêm nền tảng lớn hoặc kết nối Gemini API. Nếu Flow không đáp ứng ghép cảnh kết hợp, sẽ trình phương án FFmpeg local và Canva; không tự đổi quyền nghiệm thu hoặc công bố sản phẩm.

Khả năng kiểm nghe vẫn là khoảng trống: không được gọi kết quả ASR hoặc ảnh mẫu là đã nghe, đã xem liên tục, hoặc đã kiểm đồng bộ môi.

## 4. Quality: khả năng và ngân sách

Nguồn đã đọc ngày 2026-10-02:

- [Model và tính năng Flow](https://support.google.com/flow/answer/16352836?hl=en).
- [Chi phí Flow](https://support.google.com/flow/answer/16526234).
- [Ghép cảnh trong Flow](https://support.google.com/flow/answer/16935718?hl=en).

Tài liệu model nêu Quality hỗ trợ tạo từ văn bản hoặc khung hình đầu/đầu–cuối, ở cả hai tỷ lệ. Không hỗ trợ Ingredients/References hoặc chỉnh video bằng video-to-video. Vì vậy không thể mặc định chuyển một gói nhiều ảnh tham chiếu dạng Ingredients sang Quality.

Trang tính năng liệt kê thời lượng 4/6/8 giây, nhưng bảng giá chỉ ghi Quality 8 giây với 100 credit mỗi lượt tạo. Cần đọc cấu hình và giá ngay trên giao diện trước khi gửi yêu cầu. Trang tính năng không hỗ trợ Extend trên Quality; không lấy chữ Extend trong bảng giá để suy ra tính năng khả dụng.

Ở lần kiểm gần nhất, tài khoản còn 920 credit; đã dùng 130 trong ngân sách thử cũ 200 credit. Ngân sách riêng 100 credit mới được duyệt tại tài liệu 122, chỉ cho một thử nghiệm Quality sau khi đạt điều kiện Lite. Không mở quyền mua credit, chạy hàng loạt hoặc dùng hết số dư tài khoản.

Quality không được xem là cam kết sửa cử chỉ, tiếp xúc đạo cụ, giọng hoặc tính liên tục. Nâng độ phân giải cũng không đồng nghĩa tạo bằng model Quality.

## 5. Tài nguyên và thông tin còn thiếu

Đã kiểm file và hash trong vòng kiểm trước:

| Tài nguyên | Kết quả |
|---|---|
| Tạo hình đôi v0.3 | Hash khớp quyết định 45 |
| Bàn ăn T-NB-03_v0.8.jpg | Hash khớp quyết định 78 |
| T2-CODEX-OPEN_v0.7.png | Hash khớp tài liệu 119; chỉ được dùng trong phạm vi thử nghiệm hiện có |
| Hai ảnh Nem Bùi thật | File có tại thư mục chủ dự án; quyền sử dụng đã được ghi tại tài liệu 68 |

Hash đầy đủ và phạm vi nguồn vẫn truy xuất được từ các hồ sơ 45, 68, 78 và 119; không thay file gốc hoặc trạng thái duyệt.

Cần bổ sung:

1. Bản thiết kế cảnh mở kết hợp: cảnh nào dùng ảnh, cảnh nào có thoại/hành động, điểm cắt và trạng thái nối. Ảnh đứng yên không thể đồng thời thực hiện Đào kéo đĩa và Khoai nói; không được bỏ hai nhịp này để phù hợp công cụ.
2. Mẫu giọng Khoai theo hướng 93, mẫu Đào và đối đáp. V01 chưa được chấp nhận; tài liệu 95 mới là gói đề xuất thử lại.
3. Đầu vào và video thử S04–S05: đúng tay, cốc được đặt trước khi đưa bát, nem đổi hướng trước khi chạm miệng, trao món đúng một lần. Đề xuất CR-01 gộp cảnh chưa được duyệt.
4. Hồ sơ yêu cầu riêng cho từng lượt: phiên bản ảnh, hash, prompt nguyên văn, cấu hình, giá, tiêu chí đạt, giới hạn thử và file kết quả.
5. Bản đồ dựng theo nguồn/thời điểm: đủ chín câu, không lặp hoặc cắt từ; F01/F02 giữ đúng mức khẳng định; nhãn AI, chữ và âm thanh có vị trí cụ thể.
6. Quy cách bàn giao: mục tiêu video dọc khoảng 30 giây; độ phân giải, fps, âm thanh và các phiên bản xuất cần xác định theo thử nghiệm thật. Giữ hình mờ gốc.

Chủ dự án cho dùng ảnh không tự chứng minh đầy đủ quyền thương mại của mọi ảnh, nhạc hoặc tài nguyên khác. Vai trò kiểm quyền phải ghi nguồn và phạm vi trước bàn giao; không tự tải lên ảnh chỉ được dùng để nghiên cứu.

## 6. Vai trò kiểm chất lượng

| Nhóm vai trò đã thiết kế | Đầu ra cần thực hiện |
|---|---|
| Đạo diễn tập, hình ảnh, diễn xuất, thiết kế cảnh và dựng | Bản thiết kế cảnh mở, chỉ dẫn diễn xuất, bản đồ nguồn và điểm cắt |
| Kiểm quay phim–ánh sáng, diễn xuất, tính liên tục, nhân vật và món | Báo cáo trên đúng phiên bản ảnh/video, có vị trí lỗi và giới hạn kiểm |
| Giọng, ghép lời, ghép cảnh và đồng bộ hình–tiếng | Kiểm nghe, ranh giới câu, thời lượng, đồng bộ môi và điểm nối bản xuất |
| Cầu nối Flow, prompt và quyền tài nguyên | Kiểm yêu cầu cụ thể, vai trò ảnh đầu vào, giá giao diện và phạm vi quyền |
| Kiểm bản cuối và chủ dự án | Báo cáo bản xuất có hash, lựa chọn và nghiệm thu |

Không có báo cáo độc lập mới trong vòng kiểm này. Có thiết kế agent không đồng nghĩa vai trò đã chạy trên media thật. Không gọi ảnh mẫu của root là review độc lập.

## 7. Bước tiếp theo

1. Biên tập tài liệu, lập bản thiết kế cảnh mở và bản thử local không tiêu credit.
2. Chuẩn bị gói thử giọng và động tác riêng; ghi rõ quyền chạy còn hiệu lực.
3. Kiểm Lite đúng mục tiêu đã chọn. Sau khi đầu vào, prompt và kết quả tương ứng đạt, mới dùng ngân sách Quality tại tài liệu 122.
4. Clip đạt và được chọn → bản ráp theo thời lượng thật → hậu kỳ → kiểm bản cuối → chủ dự án nghiệm thu → bàn giao.

Giả định đang dùng: công cụ local hiện có, ưu tiên giọng từ Veo, chưa thêm nhạc ngoài, video dọc khoảng 30 giây là mục tiêu. Chưa có bằng chứng đủ để khóa mọi thời lượng hoặc toàn tập.

Bản này được biên tập lại để sửa tiếng Việt và cập nhật quyết định, không chạy thêm media, không tiêu credit và không công bố sản phẩm.
