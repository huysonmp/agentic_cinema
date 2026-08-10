# 00 — Tổng quan và phạm vi

## Tuyên bố sản phẩm

Agentic Cinema giúp biên kịch, producer và nhóm tiền kỳ biến một kịch bản cùng kho tư liệu rời rạc thành một kế hoạch sản xuất có cấu trúc, có thể kiểm tra và truy xuất nguồn gốc. Đây không phải “chatbot biết làm phim”; đây là workflow system trong đó agent đảm nhận công việc nhận thức, công cụ thực hiện thao tác xác định được và con người giữ quyền quyết định.

## Người dùng chính

| Vai trò | Nhu cầu | Giá trị đầu tiên |
|---|---|---|
| Biên kịch | Kiểm tra continuity, nhân vật, nhịp cảnh | Báo cáo có citation về mâu thuẫn và thay đổi |
| Producer/1st AD | Breakdown và ước lượng quy mô | Danh sách cảnh, cast, prop, location, VFX có thể duyệt |
| Đạo diễn/DP | Chuyển ý đồ thành shot plan | Shot list và prompt storyboard bám kịch bản |
| Art/VFX/Sound | Nhận brief nhất quán | Gói yêu cầu theo bộ phận, có nguồn và phiên bản |
| Quản trị dự án | Quyền, chi phí, audit | Lịch sử tool call, phê duyệt và provenance |

## Vấn đề cần giải quyết

- Kịch bản, ghi chú và media nằm ở nhiều định dạng, khó tìm và khó giữ đồng bộ.
- Breakdown thủ công tốn thời gian, dễ bỏ sót và khó truy ngược về trang/đoạn nguồn.
- Các bộ phận diễn giải cùng một cảnh theo cách khác nhau.
- Nội dung do AI tạo thường thiếu schema, nguồn gốc, kiểm soát phiên bản và điểm phê duyệt.
- Tự động hóa bằng agent có thể gây hậu quả nếu cho phép tool ghi/xóa/gửi mà không kiểm soát.

## Vertical slice MVP

**Đầu vào:** một kịch bản PDF/TXT đã được người dùng xác nhận quyền sử dụng, cộng với tối đa một tập tài liệu tham chiếu nhỏ.

**Đầu ra:**

- screenplay manifest;
- danh sách scene có source span;
- character/prop/location/VFX/sound breakdown;
- continuity warnings với confidence và citation;
- shot-list draft và storyboard prompts;
- export JSON + CSV;
- audit log cho từng bước và quyết định phê duyệt.

**Điểm phê duyệt bắt buộc:**

1. Chấp nhận kết quả parse trước khi tạo kế hoạch.
2. Chấp nhận breakdown trước khi sinh asset hoặc gọi dịch vụ có phí cao.
3. Chấp nhận riêng trước khi ghi sang hệ thống ngoài hoặc chia sẻ dữ liệu.

## Ngoài phạm vi MVP

- Lập lịch/quản lý ngân sách sản xuất hoàn chỉnh.
- Tạo phim hoàn chỉnh hoặc tự động phát hành lên nền tảng công cộng.
- Sao chép khuôn mặt/giọng nói của người thật khi chưa có consent có thể kiểm chứng.
- Fine-tuning trên dữ liệu kịch bản riêng tư.
- Multi-agent phân tán chỉ để trình diễn; chỉ tách agent khi có ranh giới nghiệp vụ hoặc bảo mật rõ.
- Cam kết pháp lý rằng đầu ra không xâm phạm bản quyền; hệ thống chỉ hỗ trợ provenance và quy trình duyệt.

## North-star và chỉ số

North-star: **tỷ lệ scene được người dùng chấp nhận sau tối đa một vòng sửa**, trong đó mọi field quan trọng có thể truy về nguồn.

| Nhóm | Chỉ số MVP | Mục tiêu khởi đầu |
|---|---|---|
| Chất lượng | Scene boundary F1 trên bộ gold | ≥ 0,90 |
| Chất lượng | Field precision cho cast/location/props | ≥ 0,90 |
| Grounding | Claim quan trọng có citation hợp lệ | 100% |
| An toàn | Tool rủi ro cao chạy thiếu approval | 0 |
| Trải nghiệm | Thời gian đến draft đầu tiên | Theo baseline và giảm dần |
| Ổn định | Workflow hoàn tất không lỗi | ≥ 95% trên eval set |
| Chi phí | Chi phí trên mỗi screenplay | Có budget và cảnh báo; chốt sau benchmark |

Các con số là release gate ban đầu, không phải tuyên bố chất lượng đã đạt.

## Giả định cần kiểm chứng

- PDF kịch bản có thể là text-native hoặc scan; scan cần OCR riêng.
- Một dự án có thể chứa dữ liệu mật và chịu NDA.
- Cùng một thuật ngữ có thể khác nhau theo thị trường/ngôn ngữ; schema phải giữ nguyên văn và normalized value.
- Người dùng muốn sửa đầu ra có cấu trúc thay vì trò chuyện lại từ đầu.
- Media generation có chi phí và hạn mức đáng kể, nên mặc định chỉ tạo prompt/preview sau approval.

## Definition of Product Success

Một producer có thể nạp kịch bản, kiểm tra breakdown có citation, sửa vài trường, phê duyệt, nhận shot-plan/export và xem lại toàn bộ lịch sử trong một phiên mà không phải chỉnh JSON thủ công hoặc cung cấp credential trực tiếp cho model.
