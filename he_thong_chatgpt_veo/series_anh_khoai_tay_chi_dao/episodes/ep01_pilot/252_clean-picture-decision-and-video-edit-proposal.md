# REC252 — Owner giữ hình sạch chữ

Owner trả lời **B** của vòng251. Chốt không chấp nhận chữ “Khoan” tự sinh; không dùng T02 cho EDL hiện hành, BR/C03A/finishing vẫn HOLD. ChọnB không cấp quyền paid generation mới.

## Đã xác định

Lỗi nằm ở nativegeneration, không do ảnh đầu vào/tải/cắt ghép. Không có bằng chứng một clause hoặc savedvoice là nguyên nhân duy nhất. Hai outputBM đã lặp chữ; không tự đổi wording rồi chạy lại.

Tài liệu Google Flow hiện mô tả tuyến chỉnh sửa video bằng Omni Flash. Root kiểm trực tiếp đúng nguồn T02, toàn đoạn 0–4 giây, với một video tham chiếu. Dự thảo chỉ phục hồi áo dưới chữ, không yêu cầu diễn lại hoặc đổi lời. Cấu hình Omni 1.1 Flash, 720p, dọc, x1, Tác nhân tắt báo giá **20 credit**. Đây chưa phải bằng chứng hệ thống sẽ nhận yêu cầu hoặc đầu ra đạt. Chưa gửi tạo; ô nhập đã được xóa, nút tạo bị vô hiệu hóa, số dư vẫn 992.

## Giả định, rủi ro và câu hỏi quyết định

Giả thuyết: sửa vùng chữ trên nguồn hiện có đáng cân nhắc hơn việc tiếp tục sinh lại thoại từ ảnh cho cùng lỗi. Đây là nhiệm vụ hẹp có tuyến công cụ hỗ trợ, chưa có tỷ lệ thành công được kiểm chứng. Rủi ro: từ chối chỉnh sửa liên quan lời nói như lần 232, áo méo hoặc nhấp nháy, đổi mặt, miệng, thời gian hoặc tiếng. Tiếng nguồn T02 vẫn chưa được nghe và duyệt; không kế thừa phê duyệt mẫu giọng K20.

Đề nghị owner cho **một lượt sửa 720p, x1, tối đa 20 credit**, từ phần ngân sách tạo lại. Đây là ngoại lệ vượt trần 15 credit mỗi lượt và tăng trần đợt từ 30 lên 34 cho đầu ra sửa thứ ba. Không tự thử lại, không mở 110 credit dự phòng, chưa cấp quyền chi cho BR tiếp theo. Nếu owner không duyệt, tiếp tục giữ và chỉ nghiên cứu phương án khác; không tự chuyển API, model hoặc công cụ.

## Bước tiếp

Đã đọc đầy đủ phản biện độc lập: `06_qc/C01B_clean_picture_repair_independent_252.md`, kết luận đủ trình owner, chưa cho phép gửi tạo. Nếu owner duyệt, kiểm lại nguồn, hash, nội dung nhập, giá không quá 20 và phạm vi phê duyệt; gửi một lần, tải rồi đối soát từng khung vùng chữ cùng hình và PCM. Chỉ gửi nghe/xem mới khi hình hết lỗi chặn; BR và bản nối thực có cổng riêng. Chỉ dẫn giữ tiếng không phải bằng chứng tiếng đã được giữ.

## Hồ sơ

- Quyết định: `restart_720p_v1/00_decisions/C01B-clean-picture-owner-decision-252.json`.
- Kế hoạch và tài liệu Google: `restart_720p_v1/00_decisions/C01B-clean-picture-repair-proposal-252.md`.
- Draft/quote: `restart_720p_v1/04_requests/C01B_BM_T02_REMOVE_TEXT_DRAFT_252.txt`, `C01B_REMOVE_TEXT_quote_preparation_252.json`.
- EvidenceUI: `C:/Users/PC/Downloads/du_an_nem_bui/252_BM_REPAIR_PLAN/`.

REC252 chưa gửi tạo, chi 0. Tổng dự án đã chi 88/500, còn 412; đợt coverage đã chi 14/30; 110 credit dự phòng chưa mở.
