# EP01 — Thử cơ bản bằng Lite trước Quality

2026-10-01 (Asia/Saigon). Owner: “test thử trên bản chất lượng thấp trước đi đã xem có ok k rồi mới chọn quality, bạn phải hiểu nó cơ bản trước đã”. `LITE_FIRST_DIRECTION_AUTHORIZED / PREFLIGHT_VERIFIED / BUDGET_HOLD / NOT_GENERATED`.

## Thay đổi hướng thử

Không tiếp tục đề nghị hai lượt Quality100+100 của86 làm vòng đầu. Chuyển hai probe V01/V02 của85 sang Veo3.1Lite; giữ exact prompts,8giây/9:16/x1, cùng ảnh đầu v0.8, không thêm diễn gắp/ăn. Mục tiêu trước là có tiếng Việt đủ lời/đúng speaker/tự nhiên và diễn đúng tính cách, không tối ưu hình final. Không dùng việc Lite đạt làm bằng chứng Quality giữ cùng giọng; cần bài kiểm riêng khi nâng model và owner chọn take.

Root chọn Lite trong composer trực tiếp. Actual UI: Video/Khung hình/9:16/x1, badge720p/8giây, giá10credit. Không thấy chọn độ phân giải thấp hơn cho Lite ở panel hiện hành; không gọi Lite720p là360p hoặc khẳng định đó là mọi mức rẻ nhất của nền tảng. Đây là đổi model, không chỉ giảm độ phân giải. Chưa audio toggle/voice-ID được quan sát; tính năng tiếng Việt phải thử mới xác nhận.

Đã mở picker ảnh đầu và xem actual preview `Two people sitting at table`, khớp reference v0.8 đã duyệt: hai người cùng cạnh, Khoai trái/Đào phải, bàn ăn/đĩa lá riêng/cốc bên Đào và background sửa. Đã thêm vào slot đầu; không upload mới, không chọn khung cuối. Preview là đối chiếu thị giác, không tải lại/hash-check exact bytes trong vòng này. Trước submit phải kiểm binding version nếu có thay đổi thư viện. Chưa nhập prompt hoặc bấm tạo.

Proof local: `C:/Users/PC/Downloads/du_an_nem_bui/P6_VOICE_LITE_x1_10credits.jpg` hiển thị Lite,10credit,x1,dọc và attached first-frame. Giữ confirmation agent settings Luôn luôn; không lưu default mới. Composer non-agent là direct generation: nút Bắt đầu tạo sẽ là final action, không dựa vào agent confirmation để bảo vệ lượt đó.

## Test tuần tự và tiêu chí quyết định

1. V01 Lite: hai câu Khoai trích32, không sửa thoại; kiểm có audio thực, đủ nguyên văn, đúng giọng nam trưởng thành, không narration/Đào nói thay; lưu file/terminal/chi phí, đo thật và nghe. Nếu không có kênh nghe thực thì LISTENING_PENDING và owner nghe, không audio PASS bằng hình/transcript.
2. Chỉ sau khi V01 được nghe và lỗi cơ bản không chặn: V02 Lite đối đáp ba câu cuối32; kiểm speaker order, dấu thanh, giọng Đào trưởng thành/trêu kín và Khoai chữa cháy tỉnh. So Khoai giữa hai mẫu, không khóa toàn series từ hai clip.
3. Lỗi → báo vị trí cụ thể và đề nghị chỉnh yếu tố liên quan. Không auto retry/mở variant; nếu V01 fail không dùng V02 như phép chữa mù.
4. Sau kết quả owner chọn có tiếp tục hướng giọng hay không. Quality chỉ xem xét sau basic gate và request/model/cost riêng; không chạy Quality tự động.

## Ngân sách còn cần giải quyết

GiáUI dự kiến10/mẫu, hai mẫu tối đa20, không200. Trần200 cũ chưa xác nhận phần còn lại theo85/86; owner chỉ đổi hướng thử, chưa cấp ngân sách riêng. Đề nghị **ngân sách riêng tối đa20credit cho đúng hai probe Lite**, không retry/mua thêm; thay điều kiện cap-remaining của85 cho vòng này, không sửa lịch sử cap41. HOLD trước submit đến khi điểm này được giải quyết. Nếu giá thay đổi/vượt20 thì dừng, không tự đổi model.

## Tổng hợp

Đã xác định: Lite cùng workflow frames có giáUI10, input đã gắn; Quality quá sớm cho basic validation. Đã chốt: thử thấp trước, giữ thoại/ref, không tự nâng Quality. Giả định:8giây phù hợp thoại và Lite có thể thực hiện speech; chưa kiểm. Còn mở: ngân sách20 riêng hoặc đối soát cap cũ, audio thực/độ tự nhiên/consistency/timing. Tiếp theo: giải quyết ngân sách rồi chạyV01 một lần, lưu/nghe/đối soát trướcV02. Chưa có voice candidate để owner chọn.
