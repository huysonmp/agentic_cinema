# REC306 — Tiếng C07 đã duyệt; sửa hình cần quyết định riêng

Ngày 14/10/2026. Owner xác nhận: “Đúng D06 xuyên suốt, đủ lời và nhịp chấp nhận được”.

## Điều đã xác định và chốt

Approval chỉ áp dụng tiếng trong đúng bản `C07_TWOREF_0_3s_REVIEW_ONLY_305.mp4`, range [0,72), dài 3 giây. Hash tệp đã kiểm lại: `7a7d2bc4d4fdd7a4ec220daa67477e3063583d1b2f9366a089318b9ab1104e18`.

Đào/D06 xuyên suốt; đủ câu “Thế em quay lại đúng lúc rồi.”, âm cuối rõ, nhịp chấp nhận được. Đây là xác nhận nghe của owner, không phải root/reviewer đã nghe. Không tự chuyển approval sang toàn native 4 giây hoặc một bản tiếng mới.

## Vấn đề còn mở

Khoai có chuỗi khẩu hình mở–khép ở F5–14 dù chỉ Đào nói. Tiếng đã được chốt không làm khẩu hình người nghe trở thành hợp lệ. Bản 3 giây đã bỏ phần bát thứ ba xuất hiện từ F77; toàn native vẫn chưa được chọn. Khớp miệng–tiếng, khoảng hở bát với tay Khoai, điểm nối C06→C07 và endpoint cho C08 chưa được duyệt.

Không sửa hình, ghép vào EDL, chuẩn input C08 hay chạy thêm video trong REC306. REC305 giữ snapshot tại thời điểm hỏi tiếng; REC306 là quyết định tiếp nối, không hồi tố thành whole-source PASS.

## Quyết định tiếp theo đề xuất

**A — Thử sửa khẩu hình cục bộ bằng công cụ local, không dùng credit Flow (khuyến nghị sơ bộ).** Chỉ tác động vùng miệng Khoai trong đoạn lỗi F5–14, lấy hình môi khép từ chính native này; giữ nguyên Đào, hành động, bát, cốc, nem và thời gian. Giữ nguyên track tiếng của bản 3 giây bằng remux, không tạo hoặc đọc lại lời, không cắt đầu câu và không tăng tốc. Xuất bản nháp riêng, tuyệt đối không ghi đè native hoặc EDL. Phải kiểm viền ghép, chuyển động mặt, khung trước/sau đoạn sửa và AV trước khi trình owner. Nếu vùng ghép lộ hoặc tracking không ổn, loại bản nháp; không tự mở rộng sửa toàn mặt hoặc chạy trả phí. Hiện chưa thử nên chưa bảo đảm cách này thành công; quyền local sửa món trước đây không được coi là quyền sửa mặt.

**B — Không sửa local; chuẩn phương án tạo lại để trình duyệt riêng.** Giữ bản đã có nhưng không đưa vào phim. Cần gói mới và nguồn chi cụ thể vì bucket tạo lại đã hết; phải duyệt quote/lượt và chuyển bucket nếu cần. Không dùng approval một lượt REC305 đã tiêu hết và không tự mở dự phòng. Chưa đưa một con số giá hoặc tỷ lệ thành công chưa kiểm.

Giả định làm việc: ưu tiên giữ tiếng đã duyệt, không bỏ lời để né khẩu hình và không coi lỗi miệng là phản ứng ngạc nhiên nếu owner chưa chốt. Đề xuất A nhằm khảo sát khả năng cứu phần hình với chi phí Flow bằng 0, không phải tuyên bố đã có bản đạt. Cổng C08 vẫn đóng cho tới khi có range hình–tiếng đủ điều kiện.

## Ngân sách và lưu trữ

Chi mới 0; sổ dự án 265/500, còn 235. Tạo mới 80 / tạo lại 0 / hậu kỳ 45 / dự phòng 110 vẫn đóng. Quyết định tiếng ở `restart_720p_v1/00_decisions/C07-two-ref-3s-audio-owner-acceptance-306.json`; registry306 nối tới run305 và actual review305. Food seam C05→C06 và thời lượng final 30 giây vẫn là vấn đề mở riêng.
