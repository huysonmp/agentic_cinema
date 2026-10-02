# Nhật ký học từ Flow và công cụ kiểm

## 2026-10-02 — bộ thử 127

### L-001: khôi phục tab khi phiên trình duyệt thay đổi

Quan sát: kết nối cũ mất trước lúc gửi generation. Sau khi đọc lại inventory, đã nối lại đúng tab và đúng dự án; không tạo video trong quá trình khôi phục.

Cách xử lý: đọc lại hướng dẫn và trạng thái tab; xác minh yêu cầu nào thực sự đã gửi trước khi thao tác. Không bấm tạo lại dựa riêng vào lỗi kết nối vì có thể trùng yêu cầu và tốn credit.

Giới hạn: sự cố phiên kết nối không chứng minh Flow mất dữ liệu hoặc Veo lỗi. Chưa có thử nghiệm đối chứng về nguyên nhân.

### L-002: chức năng sử dụng lại câu lệnh

Quan sát: sau R01 và R02, dùng nút sử dụng lại câu lệnh đã phục hồi prompt đầy đủ và ảnh đầu vào; END trống, cấu hình vẫn 720p/8 giây/x1. Đã chụp màn hình trước mỗi lần gửi.

Ứng dụng: thuận tiện cho bộ thử lặp lại, nhưng mỗi lần vẫn phải kiểm trạng thái phục hồi. Không coi nút này là bảo đảm mọi tham số luôn được giữ trong các phiên hoặc phiên bản Flow khác.

### L-003: thông báo tải không phải bằng chứng đã lưu local

Quan sát: Flow báo đã tải, nhưng chưa nhận được file ở các đường lưu đã kiểm. API chờ download hết thời gian; bundle các tài sản video quan sát trên trang lỗi fetch. Chưa xác định nguyên nhân; không khẳng định lỗi mạng, quyền hay hết hạn URL khi chưa có bằng chứng.

Cách xử lý trong bộ 127: giữ tài sản và URL, đối soát số dư, nhờ chủ dự án tải native. Không generation lại để chữa lỗi vận chuyển file; không gọi clip đã bàn giao khi thiếu file/hash.

Điều kiện kiểm lại: khi có file, xác minh nội dung/mã clip, kích thước, hash và khả năng giải mã; ghi cách tải thực sự thành công. Lần sau thử đường tải với tài sản sẵn có trước khi mở bộ tạo mới nếu tình trạng chưa được giải quyết.

Kiểm lại theo yêu cầu chủ dự án: chọn tải 720p gốc thêm một lần cho từng R01–R03, vẫn chưa có file local dù R02/R03 có thông báo thành công. Đường Downloads Windows không đổi. Bấm lại cùng tùy chọn chưa giải quyết được lỗi trong lần kiểm này; cần kiểm đường chuyển file hoặc hỗ trợ tải trực tiếp, không cần tạo lại media.

Đính chính theo kiểm 129: chủ dự án tải thủ công được và đã có file MP4 local đọc được metadata. Không quy lỗi cho Flow hoặc nguồn video. Thử giữ tab và bấm tọa độ 720p trên R01 vẫn chưa nhận được file; chưa chứng minh nguyên nhân nằm ở kiểu click hoặc chuyển tab. Cần đối chiếu đường thao tác thủ công và bảng Downloads của ứng dụng trước khi kết luận. Không dùng generation mới để thay thế việc sửa phương thức tải.

Kết quả media và bài học về diễn xuất/thoại: chờ kiểm sau khi đủ ba file. Không kết luận từ trạng thái đang tạo hoặc thumbnail.

### L-004: bộ tạo lại 130 đã nhận đủ file

Theo yêu cầu chủ dự án, tạo một yêu cầu Lite x3 cùng ảnh/prompt, tổng giá 30. Tải lần lượt từ menu thẻ thư viện, giữ tab và kiểm file trước khi chuyển clip; nhận đủ ba MP4. ffprobe và giải mã sạch, hash/path lưu tại tài liệu 130. Đây là đường thực hiện đã thành công trong vòng này, không phải kết luận nguyên nhân Stopped của vòng cũ. Không tuyên bố tạo lại luôn chữa được lỗi tải; cần kiểm lại đường tải trên tài sản cũ ở một vòng diagnostic riêng nếu cần tìm nguyên nhân.

Bài học thao tác: khi index thẻ không còn đúng và click lỗi, đọc lại AX/screenshot, dùng nút menu của đúng thẻ; không lặp click hoặc generation mù. x3 là một yêu cầu ba đầu ra, phải ghi khác ba lần x1. Sau hoàn tất trả x1, và kiểm lại giá/cấu hình trước lần gửi sau. Thông báo tải chỉ là tín hiệu trung gian; file/hash/giải mã mới là bằng chứng nhận file.

### L-005: mùi của món nguội không được minh họa bằng hơi nóng

Chủ dự án thấy N01 có khói dù nem nguội; prompt đã cấm `extra steam` nhưng vẫn chưa đạt. Kiểm nguồn và frame tại hồ sơ 131, chưa có đối chứng nguyên nhân. Đề xuất mô tả trạng thái vật lý tích cực (món nguội, không khí trên đĩa trong và tĩnh), loại rõ khói/hơi/heat shimmer/đường mùi; diễn mùi bằng phản ứng nhân vật. Không bảo đảm prompt sửa sẽ đạt cho tới khi thử. Checklist món phải kiểm nhiệt độ và vật lý, không dùng vẻ đẹp hoặc độ hấp dẫn bù lỗi này.
