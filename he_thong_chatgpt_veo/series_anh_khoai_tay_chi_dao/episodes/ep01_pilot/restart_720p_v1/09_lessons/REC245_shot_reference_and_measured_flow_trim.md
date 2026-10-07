# REC245 — Bài học từ sửa C02 và cắt trên Flow

## Bằng chứng, không suy đoán thành cam kết

T01 dùng master rộng và yêu cầu bằng lời chuyển sang cận vừa: actual đổi nền, cỡ cảnh rộng và có cử chỉ Đào chắp tay. T02 dùng một ảnh cận vừa thể hiện trực tiếp camera/nền/bốn tay nghỉ và prompt diễn nhẹ: ba lỗi này không lặp trong 66 khung mẫu reviewer xem. Vì ảnh conditioning và cách yêu cầu camera cùng thay đổi, chưa tách được tác động riêng từng biến hoặc chứng minh cơ chế nội tại model. Bài học làm việc: chuẩn bị source đúng coverage, không bắt một master rộng thực hiện mọi góc; luôn kiểm video thực và hồi quy các phần bất biến.

## Đuôi sai không mặc định cần sinh lại

T02 Đào hé môi từ frame 182/7,583333 giây, sau vùng lời được ASR ước lượng kết thúc 6,94 giây và vùng im lặng đo từ 6,968604. Miệng hé là lỗi so với prompt khép môi, nhưng không chứng minh có lời/giọng sai vai. Giữ nguyên nguồn, định vị lỗi, đo lời/handle và đề xuất cắt; chỉ dùng sau nghiệm thu nghe/AV. Không chuyển audio approval T01 sang T02. Không sửa script theo chữ ASR độ tin cậy thấp.

## Biên Flow phải đo trên file xuất

UI trim0–7,5 cho export181 khung ở24fps, video7,541667 giây và audio7,509333 giây; không đúng tuyệt đối180 khung như khoảng [0,7,5). Khung cuối actual180/7,5 vẫn khép môi. T01 trim0–9 cũng đã có217 khung. Đây là hai quan sát, chưa là quy tắc mọi mode/phiên bản. EDL30s phải dùng số khung/thời lượng export đo thật, không cộng mốc UI rồi gọi đủ30s.

## Đầu vào picker và tiếng phải truy được

Đã tải media đang được chọn trong picker, hash khớp native T02 trước Add. So PCM export với đầu nguồn đạt tương quan0,999990, xác nhận giữ đúng track trong bản cắt; không thay actual listening, voice identity hoặc sync. Tách source UUID, source hash, export hash, range UI, range/frame xuất và người duyệt đúng version.

## Công cụ và phục hồi

Binding trình duyệt cũ không còn khả dụng: inventory cho thấy IAB hiện hành và project đúng, tạo tab mới; tab mới không còn lỗi kết nối reCAPTCHA thấy ở tab cũ. Không giải/bỏ qua CAPTCHA hoặc dùng cơ chế ngoài UI.

QC helper chạy ở `.venv` báo thiếu Pillow; không cài mới. Dùng Python bundled đã có Pillow để trích khung, còn ASR chạy môi trường `.venv` đã có faster-whisper và cache offline. Lưu lỗi/đường chạy thật; không giả helper đã thành công ở môi trường đầu tiên. Native không bị sửa.

## Áp dụng ở clip sau

Tab tạo video hiển thị1.020 sau T02, tab mới sau export hiển thị1.050. Chưa có xác nhận hoàn phí hoặc nguyên nhân; ghi riêng từng nguồn quan sát và giữ accounting bảo thủ30 đã dùng, không tự cộng credit trả lại. Số dư UI không thay quyền chi hoặc chứng minh một tác vụ khác miễn phí.

Giữ source theo shot và state thật, chỉ một người nói/voice mỗi request; kiểm người nghe, đầu–cuối và điểm nối. Dùng trim để bỏ phần ngoài nhiệm vụ khi vẫn giữ trọn lời/nhịp; không dùng trim để che lỗi trong lượt nói. Hai output liên tiếp cùng lỗi lớn vẫn kích hoạt dừng, không đổi tên lỗi để né giới hạn.
